"""Coarse/fine discovery is explicit, portable and bounded for deep time."""
from copy import deepcopy
import json

from starlette.testclient import TestClient

from ailectures.catalog import repository_track
from ailectures.chronology import normalize_chronology
from ailectures.discovery import discovery_fields, time_paths
from ailectures.packs import export_release
from ailectures.tagging import normalize_paths
from ailectures.web import create_app


def labels(row):
    return set(discovery_fields(row)['tags'])


def test_only_recorded_specificity_is_expanded_upward():
    row = {'tags': ['DNA'], 'metadata': {'places': ['Paris', 'Troy', 'Cambridge']}}
    before = deepcopy(row)
    result = discovery_fields(row)
    assert ['Science', 'Biology', 'Molecular biology', 'DNA'] in result['tag_paths']
    assert ['Place: Europe', 'Place: France', 'Place: Paris'] in result['tag_paths']
    assert result['places'] == ['Paris', 'Troy', 'Cambridge']
    assert 'Place: Turkey' not in result['tags']
    assert 'Place: England' not in result['tags']  # Cambridge is ambiguous.
    broad = labels({'tags': ['Biology'], 'places': ['Europe']})
    assert 'Science' in broad and 'DNA' not in broad and 'Place: France' not in broad
    assert row == before
    repeated = discovery_fields(dict(row, **result))
    assert sum(path[-1] == 'Place: Paris' for path in repeated['tag_paths']) == 1
    assert ['Place: Paris'] not in repeated['tag_paths']


def test_custom_paths_do_not_require_a_shared_registry_or_reinterpret_slashes():
    path = ['Mathematics', 'Geometry', 'Example custom topic']
    fields = discovery_fields({'metadata': {'tag_paths': [path]}, 'tags': ['a/b']})
    assert path in fields['tag_paths']
    assert 'Example custom topic' in fields['tags']
    assert 'a' not in fields['tags'] and 'a/b' in fields['tags']
    assert normalize_paths([['A', 'a'], ['A', 'bad\nlabel'], 'A/B', [5], [], path]) == [path]
    assert labels({'title': 'Physics in Paris in 1922'}) == set()


def test_time_hierarchy_retains_meaning_uncertainty_and_exact_point_dates():
    record = normalize_chronology({'work': {'start': 1922}})['work']
    paths = time_paths('work', record)
    path = next(path for path in paths if path[-1] == 'Work date: 1922 CE')
    assert path == ['Work date: CE', 'Work date: 2nd millennium CE', 'Work date: 20th century CE',
                    'Work date: 1920 CE–1929 CE', 'Work date: 1922 CE']
    fields = discovery_fields({'chronology': {'work': {'start': 1922, 'approximate': True},
                                               'setting': {'start': -1, 'end': 1}}})
    assert 'Work date: c. 1922 CE' in fields['tags']
    assert 'Work date: 1922 CE' not in fields['tags']
    assert 'Story setting: BCE' in fields['tags'] and 'Story setting: CE' in fields['tags']
    assert not any('0 BCE' == label or '0 CE' == label for path in fields['tag_paths'] for label in path)
    broad = normalize_chronology({'period': {'start': -10**12, 'end': 2020}})['period']
    assert len(time_paths('period', broad)) <= 3
    assert not any('century' in label for path in time_paths('period', broad) for label in path)


def test_publication_composition_and_fictional_setting_stay_distinct():
    result = normalize_chronology({'work': {'start': 1982}, 'composition': {'start': 1913, 'end': 1935},
                                  'fictional_setting': {'start': 1815, 'end': 1833}})
    assert result['work']['start'] == 1982
    assert result['composition']['start'] == 1913
    assert result['setting']['start'] == 1815
    assert normalize_chronology({'setting': {'start': 10}, 'fictional_setting': {'start': 20}})['setting']['start'] == 10
    assert 'Composition date: 20th century CE' in discovery_fields({'chronology': result})['tags']


def test_authored_paths_survive_source_export_catalog_and_graph(tmp_path):
    source = tmp_path/'source';source.mkdir();(source/'metadata').mkdir()
    (source/'001000.md').write_text('# A cell\n<!-- BEGIN SPOKEN LECTURE -->\nAn original explanation.\n<!-- END SPOKEN LECTURE -->\n')
    (source/'track.json').write_text(json.dumps({'id':'test','title':'Cells','tag_paths':[['Science','Biology']],
        'lectures':[{'id':'001000','file':'001000.md','tag_paths':[['Science','Biology','Cell biology']]}]}))
    path = ['Science','Biology','Cell biology','A custom organelle']
    (source/'metadata/001000.json').write_text(json.dumps({'tag_paths':[path]}))
    pack = repository_track(source)
    export_release(pack,tmp_path/'release')
    app = create_app(tmp_path/'library');app.state.library.store.install(tmp_path/'release')
    with TestClient(app) as client:
        summary = client.get('/api/library/catalog').json()['lectures'][0]
        detail = client.get('/api/library/lectures/test:001000').json()
        graph = client.get('/api/library/learning-map').json()['nodes']['test:001000']
        assert path in summary['tag_paths']
        assert detail['tag_paths'] == summary['tag_paths'] == graph['tag_paths']
        assert 'A custom organelle' in summary['tags']
        assert 'transcript' not in summary


def test_qualified_city_associations_roll_up_without_guessing_ambiguous_names():
    fields = discovery_fields({'places': ['Cambridge (Massachusetts)', 'Urbana, Illinois', 'Edo (Tokyo)']})
    assert ['Place: North America', 'Place: United States', 'Place: Massachusetts', 'Place: Cambridge (Massachusetts)'] in fields['tag_paths']
    assert 'Place: United States' in fields['tags']
    assert 'Place: Japan' in fields['tags']
    assert 'Place: United States' not in labels({'places': ['Cambridge']})
    assert 'Place: England' not in labels({'places': ['Cambridge']})
