"""Course paths reuse source lectures; conceptual edges remain validated."""
import json
from pathlib import Path

import pytest
from starlette.testclient import TestClient

from dkvis.presentation.course_graph import build_course_graph, connected_components, connections
from dkvis.presentation.serve import create_app


def authored_relations(graph):
    """Source evidence includes claims now internal to a combined manuscript."""
    return {
        (component['from'], edge['type'], component['to'])
        for edge in graph['edges']
        for component in edge.get('component_relations', [edge])
    } | {
        (edge['from'], edge['type'], edge['to'])
        for edge in graph.get('internal_component_relations', [])
    }


def test_course_graph_inventory_and_yws_reuse():
    graph = build_course_graph()
    assert set(graph['nodes']) == {node for track in graph['tracks'] for node in track['path']}
    assert set(graph['relations']) == {
        'hard_depends_on', 'soft_depends_on', 'expands_on',
        'original_parent', 'alternative_presentation', 'related_to',
        'listening_next', 'proof_depends_on'}
    tracks = {track['id']: track for track in graph['tracks']}
    assert len(tracks['g1']['path']) == 22
    g2_rows = json.loads((Path(__file__).resolve().parents[1] / 'content/g2/track.json').read_text())['lectures']
    assert tracks['g2']['path'] == ['g2:' + row['id'] for row in g2_rows]
    g3_rows = json.loads((Path(__file__).resolve().parents[1] / 'content/g3/track.json').read_text())['lectures']
    assert tracks['g3']['path'] == ['g3:' + row['id'] for row in g3_rows]
    assert tracks['g4']['available_count'] == 7
    assert tracks['g4']['planned_count'] == 6
    assert tracks['g4']['path'].count('g3:003000') == 1
    assert graph['nodes']['g4:residual-proof']['url'] is None
    assert graph['nodes']['g2:147000']['url'].startswith('/audio?track=g2')
    assert graph['nodes']['g3:003000']['url'].startswith('/audio?track=g3')
    original = [e for e in graph['edges'] if e['type'] == 'original_parent']
    expected = {('g3:' + row['id'], 'g2:' + row['source_g2']) for row in g3_rows if row.get('source_g2')}
    assert {(e['from'], component['to']) for e in original for component in e['component_relations']} == expected
    assert all(graph['nodes'][e['from']]['track'] == 'g3' for e in original)
    assert any(e['type'] == 'hard_depends_on' and e['to'] == 'g3:003000'
               for e in graph['edges'])


def test_graph_rejects_invalid_edges_and_cycles(tmp_path):
    from dkvis.presentation.course_graph import GRAPH_DIRECTORY
    for filename in ('g4-yws.json', 'relationships.json'):
        (tmp_path / filename).write_bytes((GRAPH_DIRECTORY / filename).read_bytes())
    rpath = tmp_path / 'relationships.json'
    data = json.loads(rpath.read_text())
    data['edges'].append(['g4:unknown', 'soft_depends_on', 'g3:001000'])
    rpath.write_text(json.dumps(data))
    with pytest.raises(ValueError, match='Invalid course edge'):
        build_course_graph(graph_directory=tmp_path)
    data['edges'].pop()
    data['edges'].extend([
        ['g3:001000', 'hard_depends_on', 'g3:002000'],
        ['g3:002000', 'hard_depends_on', 'g3:001000'],
    ])
    rpath.write_text(json.dumps(data))
    with pytest.raises(ValueError, match='cycle'):
        build_course_graph(graph_directory=tmp_path)


def test_graph_api_and_reader_links(tmp_path):
    render = tmp_path / 'renders'
    render.mkdir()
    with TestClient(create_app(render)) as client:
        response = client.get('/api/course-graph')
        assert response.status_code == 200
        assert response.json()['tracks'][-1]['id'] == 'g4'
        assert client.get('/learning-paths?track=g4').status_code == 200
        assert 'DKPS · Course graph' in client.get('/learning-paths').text
        tracks = client.get('/api/audio-tracks').json()['tracks']
        assert {'g1', 'g2', 'g3', 'history', 'world-history', 'world-reconsidered',
                'category-theory', 'logic-types', 'optimization-duality',
                'probability-measure', 'g4'} <= {track['id'] for track in tracks}
        assert tracks[-1]['kind'] == 'graph'
        detail = client.get('/api/audio-lectures/147000?track=g2').json()
        assert any(row['node_id'] == 'g1:003875_yws'
                   for row in detail['course_connections'])
        audio_html = client.get('/audio').text
        assert 'Course graph connections' in audio_html
        assert '/learning-paths?track=g4' in audio_html


def test_curated_topic_graph_covers_every_lecture():
    graph = build_course_graph()
    assert len(graph['topics']) == 13
    assert set(graph['nodes']) == {node for track in graph['tracks'] for node in track['path']}
    assert all(edge['from'] in graph['nodes'] and edge['to'] in graph['nodes'] for edge in graph['edges'])
    assert all(node.get('topic') for node in graph['nodes'].values())
    topics = {topic['id'] for topic in graph['topics']}
    assert set(node['topic'] for node in graph['nodes'].values()) == topics
    sources = {edge['from'] for edge in graph['edges']}
    g2_path = next(track['path'] for track in graph['tracks'] if track['id'] == 'g2')
    assert set(g2_path[:-1]) <= sources
    assert graph['nodes']['g2:147000']['topic'] == 'statistics'
    assert graph['nodes']['g3:020000']['topic'] == 'davis-kahan'
    assert graph['nodes']['g4:residual-proof']['topic'] == 'statistics'


def test_curated_links_have_explanations_and_cross_track_connections():
    graph = build_course_graph()
    reasons = [e for e in graph['edges'] if e.get('why')]
    assert reasons
    assert ('g2:110000', 'hard_depends_on', 'g2:108000') in authored_relations(graph)
    assert ('g3:020000', 'alternative_presentation', 'g2:110000') in authored_relations(graph)
    assert any(e['from'] == 'g4:application' and e['to'] == 'g2:148000'
               and e['type'] == 'expands_on' for e in reasons)
    assert all(e['why'].strip() and len(e['why']) > 20 for e in reasons)
    assert any('why' in c for c in connections(graph, graph['component_lectures'].get('g2:110000', 'g2:110000')))


def test_new_graph_ui_controls_and_api(tmp_path):
    render = tmp_path / 'renders'
    render.mkdir()
    with TestClient(create_app(render)) as client:
        response = client.get('/api/course-graph')
        assert response.status_code == 200
        data = response.json()
        assert 'topics' in data and len(data['topics']) == 13
        assert any(edge.get('why') for edge in data['edges'])
        text = client.get('/learning-paths?track=g4&node=g4:overview').text
        for marker in ('id="graph"', 'id="relations"', 'id="topic"',
                       'id="extent"', 'id="zoom-in"', 'id="fit"',
                       'id="connections"', 'id="edges-all"', 'id="edges-none"',
                       'id="edges-core"', 'id="node-labels"', 'id="maximize"', '/api/course-graph'):
            assert marker in text
        assert '<option value="all" selected>' in text
        assert 'listening_next' in text and 'proof_depends_on' in text


def test_g1_syllabus_links_to_exact_deck_and_uses_authored_background():
    graph = build_course_graph()
    assert graph['nodes']['g1:003875_yws']['url'] == '/?deck=yws-population-gap'
    assert graph['nodes']['g1:001000_projections']['url'] == '/?deck=prereq-projections'
    assert any(e['from'] == 'g1:003875_yws' and e['to'] == 'g1:003750_sine_theta'
               and e['type'] == 'soft_depends_on' and e.get('why')
               for e in graph['edges'])


def test_all_nodes_connected_by_navigation_and_real_cross_track_relationships():
    graph = build_course_graph()
    assert len(connected_components(graph)) == 1
    # Course order alone connects each path, not the different tracks.
    order_only = connected_components(graph, relation_types={'listening_next'})
    assert len(order_only) == 2
    g1_count = len(next(track['path'] for track in graph['tracks'] if track['id'] == 'g1'))
    assert sorted(map(len, order_only)) == sorted([g1_count, len(graph['nodes']) - g1_count])
    # Actual alternative presentations tie G1 to the audio tracks.
    overview_types = {'listening_next', 'proof_depends_on', 'alternative_presentation'}
    assert len(connected_components(graph, relation_types=overview_types)) == 1
    assert len(connected_components(graph, relation_types=set())) == len(graph['nodes'])
    assert len(connected_components(graph, node_ids={'g2:000000','g2:001000'})) == 1


def test_listening_order_is_explicit_and_not_a_mathematical_dependency():
    graph = build_course_graph()
    path_edges = {(e['from'], e['to']): e for e in graph['edges'] if e['type'] == 'listening_next'}
    expected_pairs = {
        (first, second)
        for track in graph['tracks']
        for first, second in zip(track['path'], track['path'][1:])
    }
    assert set(path_edges) == expected_pairs  # Shared pairs are counted once.
    for track in graph['tracks']:
        for first, second in zip(track['path'], track['path'][1:]):
            row = path_edges[first, second]
            assert track['id'].upper() in row['why']
    assert ('g1:000505_history_overview', 'g1:000670_history_people_foundations') in path_edges
    g3_path = next(track['path'] for track in graph['tracks'] if track['id'] == 'g3')
    assert (g3_path[0], g3_path[1]) in path_edges
    assert ('g4:overview', 'g3:001000') in path_edges
    assert 'Next' in graph['relations']['listening_next']


def test_proof_links_are_curated_with_explicit_reasons():
    graph = build_course_graph()
    proof_edges = [e for e in graph['edges'] if e['type'] == 'proof_depends_on']
    from dkvis.presentation.course_graph import GRAPH_DIRECTORY
    authored = json.loads((GRAPH_DIRECTORY / 'proof-relationships.json').read_text())['edges']
    assert {(row[0], row[1], row[2]) for row in authored} == {relation for relation in authored_relations(graph) if relation[1] == 'proof_depends_on'}
    assert all(e['why'] and len(e['why']) > 25 for e in proof_edges)
    assert ('g2:110000', 'proof_depends_on', 'g2:071000') in authored_relations(graph)
    assert ('g2:134000', 'proof_depends_on', 'g2:133000') in authored_relations(graph)
    assert any(e['from'] == 'g4:residual-proof' and e['to'] == 'g3:003000'
               for e in proof_edges)


def test_proof_graph_rejects_cycles(tmp_path):
    from dkvis.presentation.course_graph import GRAPH_DIRECTORY
    for filename in ('g4-yws.json', 'relationships.json', 'proof-relationships.json'):
        (tmp_path / filename).write_bytes((GRAPH_DIRECTORY / filename).read_bytes())
    data = json.loads((tmp_path / 'proof-relationships.json').read_text())
    data['edges'] += [
        ['g2:110000', 'proof_depends_on', 'g2:112000', 'A test-only cycle edge'],
        ['g2:112000', 'proof_depends_on', 'g2:110000', 'The reverse test-only cycle edge'],
    ]
    (tmp_path / 'proof-relationships.json').write_text(json.dumps(data))
    with pytest.raises(ValueError, match='proof_depends_on cycle'):
        build_course_graph(graph_directory=tmp_path)


def test_consolidated_components_keep_evidence_and_manifest_order(tmp_path):
    g1, g2, g3, records = [tmp_path / name for name in ('g1', 'g2', 'g3', 'records')]
    for directory in (g1, g2, g3, records):
        directory.mkdir()
    for name in ('000000-combined.md', '002000-later.md'):
        (g2 / name).write_text('# A unit\n')
    (g2 / 'track.json').write_text(json.dumps(dict(lectures=[
        dict(id='002000', file='002000-later.md'),
        dict(id='000000', file='000000-combined.md', consolidated_from=['000000', '001000']),
    ])))
    (g3 / '000000-adapted.md').write_text('# Adaptation\n')
    (g3 / 'track.json').write_text(json.dumps(dict(title='Adapted', lectures=[dict(id='000000', title='Adapted', file='000000-adapted.md', source_g2='001000')])))
    (records / 'g4-yws.json').write_text(json.dumps(dict(title='Planned', summary='', nodes=[], path=[])))
    relations = dict(schema_version=1, edges=[
        ['g2:002000', 'related_to', 'g2:000000', 'An original connection.'],
        ['g2:002000', 'related_to', 'g2:001000', 'Another original connection.'],
        ['g2:001000', 'proof_depends_on', 'g2:000000', 'A proof now internal to the combined unit.'],
    ])
    (records / 'relationships.json').write_text(json.dumps(relations))
    graph = build_course_graph(g1_directory=g1, g2_directory=g2, g3_directory=g3, graph_directory=records)
    assert next(track for track in graph['tracks'] if track['id'] == 'g2')['path'] == ['g2:002000', 'g2:000000']
    assert 'g2:001000' not in graph['nodes']
    assert set(authored_relations(graph)) >= {tuple(row[:3]) for row in relations['edges']}
    assert ('g3:000000', 'original_parent', 'g2:001000') in authored_relations(graph)
    assert len([edge for edge in graph['edges'] if edge['type'] == 'related_to']) == 1
    assert graph['internal_component_relations'][0]['lecture'] == 'g2:000000'
    # A source-level proof cycle is invalid even if both parts share one unit.
    relations['edges'].append(['g2:000000', 'proof_depends_on', 'g2:001000', 'Reverse proof claim.'])
    (records / 'relationships.json').write_text(json.dumps(relations))
    with pytest.raises(ValueError, match='proof_depends_on cycle'):
        build_course_graph(g1_directory=g1, g2_directory=g2, g3_directory=g3, graph_directory=records)
