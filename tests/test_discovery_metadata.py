"""Discovery metadata is portable, qualified, optional, and independent of speech."""
from copy import deepcopy
import json
from pathlib import Path

from starlette.testclient import TestClient

from ailectures.discovery import creators, discovery_fields, time_buckets
from ailectures.chronology import normalize_chronology
from ailectures.descriptions import description_fields, lecture_outline
from ailectures.catalog import repository_track
from ailectures.packs import export_release
from ailectures.web import create_app


def test_time_facets_keep_axes_uncertainty_and_historical_year_numbering():
    fields = discovery_fields(dict(metadata={'chronology': {
        'work': {'start': 1900, 'end': 1901, 'approximate': True},
        'setting': {'start': -1, 'end': 1},
        'life': {'start': 0},
    }}))
    assert fields['time_coverage'] == {'work': ['19th century CE', '20th century CE'],
                                       'setting': ['1st century BCE', '1st century CE']}
    assert 'Work date: c. 1900 CE–1901 CE' in fields['tags']
    assert 'Story setting: 1 BCE–1 CE' in fields['tags']
    assert not any(tag.startswith('Lifetime:') for tag in fields['tags'])
    assert discovery_fields({'title': 'Life in Paris, 1914', 'id': '191400'})['tags'] == []


def test_broad_ranges_do_not_expand_into_millions_of_centuries():
    record = normalize_chronology({'period': {'start': -10**12, 'end': 2020}})['period']
    assert len(time_buckets(record)) == 1
    assert time_buckets(record)[0].startswith('Broad range:')
    assert time_buckets(normalize_chronology({'period': {'start': -500, 'end': -401}})['period']) == ['5th century BCE']


def test_associations_do_not_invent_borders_authorship_or_dependencies():
    row = dict(tags=['Epic'], metadata={
        'places': ['Troy', 'Troy', '../not a filename', 'bad\nlabel'],
        'periods': ['Bronze Age'],
        'creators': [{'name': 'Homer', 'role': 'attributed_author', 'note': 'Traditional attribution.'},
                     {'name': 'An editor', 'role': 'compiler'}, {'name': 'An oral tradition', 'role': 'oral_tradition'}],
    })
    before = deepcopy(row)
    result = discovery_fields(row)
    assert result['places'] == ['Troy', '../not a filename']
    assert 'Place: Troy' in result['tags']
    assert 'Place: Turkey' not in result['tags']
    assert 'Author: Homer' in result['tags']
    assert 'Author: An editor' not in result['tags']
    assert row == before
    assert creators([None, {'role': 'invented', 'name': 'Someone'}, {'name': 'bad\nname'}]) == []
    assert creators({'name': 'Not a list'}) == []


def test_descriptions_prefer_authored_scope_and_keep_outline_previews_honest():
    source = '# A title\n**Aim:** Derive a useful bound. **Background:** Algebra.\n\n<!-- BEGIN SPOKEN LECTURE -->\n## A construction\nText\n## Companions, sources, and study material (not spoken)\nIgnore\n<!-- END SPOKEN LECTURE -->\n## Private appendices\n'
    assert lecture_outline(source) == ['A construction']
    result = description_fields({'source': source})
    assert result['description'] == 'Derive a useful bound.'
    assert result['description_basis'] == 'authored'
    assert description_fields({'source': source, 'metadata': {'description': 'A curated description.'}})['description'] == 'A curated description.'
    result = description_fields({'source': '## A meaningful section\nWords'})
    assert result['description_basis'] == 'outline'
    assert description_fields(result)['description_basis'] == 'outline'
    assert description_fields({'outline': None, 'metadata': {'description': []}})['description'] == ''


def test_metadata_survives_export_and_is_available_without_fetching_transcript(tmp_path):
    pack_dir = tmp_path / 'source'
    pack_dir.mkdir()
    (pack_dir/'metadata').mkdir()
    transcript = '# A book\n<!-- BEGIN SPOKEN LECTURE -->\n## Language and power\nThe original spoken words.\n<!-- END SPOKEN LECTURE -->\n'
    (pack_dir/'001000-book.md').write_text(transcript)
    (pack_dir/'track.json').write_text(json.dumps(dict(id='test', title='Literature', lectures=[dict(id='001000', file='001000-book.md')])))
    before = repository_track(pack_dir)
    (pack_dir/'metadata/001000.json').write_text(json.dumps(dict(description='Examines language, power, and memory in a novel.', places=['London'], periods=['Modernism'], creators=[dict(name='A writer', role='author')], chronology={'work': {'start': 1922}, 'setting': {'start': 1904}})))
    after = repository_track(pack_dir)
    key = 'test:001000'
    assert after['lectures'][key]['spoken_sha256'] == before['lectures'][key]['spoken_sha256']
    assert after['lectures'][key]['transcript'] == before['lectures'][key]['transcript']
    export_release(after, tmp_path/'release')
    app = create_app(tmp_path/'library')
    app.state.library.store.install(tmp_path/'release')
    with TestClient(app) as client:
        summary = client.get('/api/library/catalog').json()['lectures'][0]
        detail = client.get('/api/library/lectures/'+key).json()
        compact = client.get('/api/library/lectures/'+key+'?summary=1').json()
        assert not {'source', 'transcript', 'metadata'} & compact.keys()
        graph = client.get('/api/library/learning-map').json()['nodes'][key]
        assert 'transcript' not in summary and 'source' not in summary
        for field in ('description', 'outline', 'creators', 'places', 'periods', 'tags', 'time_coverage'):
            assert summary[field] == detail[field] == compact[field] == graph[field]
        assert summary['creators'][0]['name'] == 'A writer'
        assert 'Work date: 1922 CE' in summary['tags']
        assert 'Story setting: 1904 CE' in summary['tags']


def test_backfill_uses_whole_work_names_and_leaves_manuscripts_alone():
    from tools.enrich_discovery_metadata import propose
    root = Path(__file__).resolve().parents[1]
    rules = json.loads((root/'tools/data/discovery-rules.json').read_text())
    metadata = {'historical_claims': [{'id': 'claim'}]}
    entry = dict(id='001000', title='Shijing: Songs', section='ancient-chinese-poetry')
    result, evidence = propose(entry, metadata, '# Songs\n\n## Fields\n', 'literature-survey', rules)
    assert result['creators'][0]['role'] == 'anonymous'
    assert result['creators'][0]['name'] != 'Sima Qian'
    assert metadata == {'historical_claims': [{'id': 'claim'}]}
    assert result['historical_claims'] == metadata['historical_claims']
    assert evidence
    second, _ = propose(entry, result, '# Songs\n\n## Fields\n', 'literature-survey', rules)
    assert second == result


def test_geographic_override_survives_title_enrichment_and_preserves_authored_places():
    import pytest
    from tools.enrich_discovery_metadata import propose
    root = Path(__file__).resolve().parents[1]
    rules = json.loads((root/'tools/data/discovery-rules.json').read_text())
    rules['geography_overrides'] = {'history:001000': {'places': ['Africa', 'Kenya'], 'anchor': 'Regional evidence'}}
    metadata = {'places': ['Paris']}
    row = dict(id='001000', title='Egypt and a traveler')
    after, _ = propose(row, metadata, '# Regional evidence\n', 'history', rules)
    assert set(after['places']) == {'Paris', 'Africa', 'Kenya', 'Egypt'}
    assert metadata == {'places': ['Paris']}
    assert propose(row, after, '# Regional evidence\n', 'history', rules)[0] == after
    with pytest.raises(ValueError):
        propose(row, metadata, '# Changed source\n', 'history', rules)


def test_enrichment_can_target_a_single_lecture_without_writing_other_sidecars(tmp_path):
    from tools.enrich_discovery_metadata import run
    folder = tmp_path/'content' / 'history'
    (folder/'metadata').mkdir(parents=True)
    entries = [dict(id=key, file=key+'-example.md', title='A subject') for key in ['001000', '002000']]
    (folder/'track.json').write_text(json.dumps(dict(id='history', lectures=entries)))
    for entry in entries:
        (folder/entry['file']).write_text('# A subject\n')
        (folder/'metadata'/f"{entry['id']}.json").write_text('{}')
    result = run(tmp_path, True, only=['history:001000'])
    assert result['changed'] == {'history': 1}
    assert (folder/'metadata/002000.json').read_text() == '{}'
    assert run(tmp_path, True, only=['history:001000'])['changed'] == {}
