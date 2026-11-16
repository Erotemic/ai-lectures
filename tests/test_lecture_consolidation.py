import json
from pathlib import Path

import pytest

from ailectures.catalog import repository_track
from ailectures.core import extract_text
from tools.consolidate_lectures import apply_prepared, compose, prepare


def pack(root, namespace, *, selection=None):
    directory = root / 'content' / namespace
    directory.mkdir(parents=True)
    entries = []
    for key, text in [('001000', 'First argument.'), ('002000', 'Second argument.'), ('003000', 'Independent argument.')]:
        filename = key + '-topic.md'
        (directory / filename).write_text(f'# Topic {key}\n\nBackground {key}.\n\n<!-- BEGIN SPOKEN LECTURE -->\n# Topic {key}\n\n{text}\n\n<!-- END SPOKEN LECTURE -->\n\n## Exact companion\n\nEquation {key}.\n')
        entries.append(dict(id=key, file=filename, title=key, section='topic'))
        (directory / 'metadata').mkdir(exist_ok=True)
        (directory / 'metadata' / (key + '.json')).write_text(json.dumps(dict(lecture_id=key, transcript=filename, historical_claims=[dict(id=key, anchor=text)], related_resources=[], limits='Preserve this limitation.')))
    (directory / 'track.json').write_text(json.dumps(dict(id=namespace, title=namespace, lectures=entries, sections=['topic'])))
    if selection:
        (directory / 'navigation.json').write_text(json.dumps(dict(default_collection='survey', collections=[dict(id='survey', title='Survey', role='main', lectures=selection)])))
    return directory


def plan():
    return dict(groups=[dict(pack='sample', title='A connected argument', lectures=['sample:001000', 'sample:002000'])])


def test_compose_keeps_arguments_and_companions_outside_single_spoken_region(tmp_path):
    directory = pack(tmp_path, 'sample')
    texts = [(key, (directory / (key + '-topic.md')).read_text()) for key in ['001000', '002000']]
    merged = compose('A connected argument', texts)
    spoken = extract_text(merged)
    assert spoken.index('First argument.') < spoken.index('Second argument.')
    assert 'Equation' not in spoken and 'Background' not in spoken
    assert 'Equation 001000.' in merged and 'Equation 002000.' in merged
    assert merged.count('<!-- BEGIN SPOKEN LECTURE -->') == 1


def test_real_source_merge_removes_parts_and_updates_every_route_and_metadata(tmp_path):
    directory = pack(tmp_path, 'sample', selection=['001000', '002000', '003000'])
    elsewhere = pack(tmp_path, 'elsewhere', selection=['sample:001000', 'sample:002000'])
    observed, writes, deletes, summary = prepare(tmp_path, plan())
    assert (directory / '002000-topic.md').exists(), 'Preview has no source side effects'
    apply_prepared(observed, writes, deletes)
    result = repository_track(directory)
    assert set(result['lectures']) == {'sample:001000', 'sample:003000'}
    assert result['courses']['sample:survey']['lectures'] == ['sample:001000', 'sample:003000']
    assert repository_track(elsewhere)['courses']['elsewhere:survey']['lectures'] == ['sample:001000']
    assert not (directory / '002000-topic.md').exists()
    assert not (directory / 'metadata/002000.json').exists()
    metadata = result['lectures']['sample:001000']['metadata']
    assert len(metadata['historical_claims']) == 2
    assert metadata['limits'] == 'Preserve this limitation.'
    assert len(metadata['consolidation']['sources']) == 2
    assert (directory / 'provenance.yaml').is_file()
    assert not result['warnings']


def test_partial_survey_coverage_requires_an_explicit_editorial_choice(tmp_path):
    pack(tmp_path, 'sample', selection=['001000'])
    with pytest.raises(ValueError, match='partial selection'):
        prepare(tmp_path, plan())
    reviewed = plan()
    reviewed['collection_orders'] = {'sample:survey': ['sample:001000', 'sample:002000']}
    observed, writes, deletes, _ = prepare(tmp_path, reviewed)
    apply_prepared(observed, writes, deletes)
    assert repository_track(tmp_path / 'content/sample')['courses']['sample:survey']['lectures'] == ['sample:001000']


def test_concurrent_source_change_aborts_before_any_writes(tmp_path):
    directory = pack(tmp_path, 'sample')
    observed, writes, deletes, _ = prepare(tmp_path, plan())
    source = directory / '002000-topic.md'
    source.write_text(source.read_text() + '\nNew source notes.\n')
    with pytest.raises(ValueError, match='Changed during preparation'):
        apply_prepared(observed, writes, deletes)
    assert (directory / '001000-topic.md').exists()
    assert not (directory / '001000-a-connected-argument.md').exists()
    assert 'New source notes.' in source.read_text()


def test_failure_rolls_back_prepared_source_changes(tmp_path, monkeypatch):
    directory = pack(tmp_path, 'sample')
    observed, writes, deletes, _ = prepare(tmp_path, plan())
    old = (directory / '001000-topic.md').read_bytes()
    unlink = Path.unlink
    failed = False
    def fail_once(path, *args, **kwargs):
        nonlocal failed
        if path in deletes and not failed:
            failed = True
            raise OSError('simulated failure')
        return unlink(path, *args, **kwargs)
    monkeypatch.setattr(Path, 'unlink', fail_once)
    with pytest.raises(OSError, match='simulated'):
        apply_prepared(observed, writes, deletes)
    assert (directory / '001000-topic.md').read_bytes() == old
    assert (directory / '002000-topic.md').exists()
    assert not (directory / '001000-a-connected-argument.md').exists()


def test_discovered_pack_gets_an_explicit_track_and_new_file_conflicts_are_preserved(tmp_path):
    directory = pack(tmp_path, 'g2')
    (directory / 'track.json').unlink()
    reviewed = dict(groups=[dict(pack='g2', title='A connected argument', lectures=['001000', '002000'])])
    observed, writes, deletes, _ = prepare(tmp_path, reviewed)
    target = directory / '001000-a-connected-argument.md'
    target.write_text('Another author created this file.')
    with pytest.raises(ValueError, match='Changed during preparation'):
        apply_prepared(observed, writes, deletes)
    assert target.read_text() == 'Another author created this file.'
    target.unlink()
    apply_prepared(observed, writes, deletes)
    assert (directory / 'track.json').exists()
    assert len(repository_track(directory)['lectures']) == 2
