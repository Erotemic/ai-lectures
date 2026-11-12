"""Concurrent World History contributions preserve other agents' work."""

import json
from pathlib import Path
from zipfile import ZipFile

import pytest

from tools.merge_world_history_overlay import (
    MergeConflict, SOURCES_PATH, TRACK_PATH, WORLD_HISTORY, merge_world_history_overlay,
)


def _encode(value):
    return json.dumps(value, indent=2).encode('utf-8') + b'\n'


def _entry(lecture_id, name, section='how-we-know'):
    return {'id': lecture_id, 'title': name, 'section': section,
            'file': f'{lecture_id}-{name}.md', 'spoken_words': 3501}


def _source(name):
    return {'title': name, 'url': f'https://example.org/{name}'}


def _metadata(row, source_id):
    return {'schema_version': 1, 'lecture_id': row['id'],
            'transcript': row['file'],
            'related_resources': [{'source_id': source_id, 'reason': 'Research'}]}


def _repo(tmp_path):
    directory = tmp_path / WORLD_HISTORY
    (directory / 'metadata').mkdir(parents=True)
    original = _entry('001000', 'existing')
    (directory / original['file']).write_text('# Existing\n')
    (tmp_path / TRACK_PATH).write_bytes(_encode({
        'id': 'world-history', 'sections': ['how-we-know'], 'lectures': [original],
    }))
    (tmp_path / SOURCES_PATH).write_bytes(_encode({
        'schema_version': 1, 'sources': {'existing': _source('existing')},
    }))
    (directory / 'metadata' / '001000.json').write_bytes(_encode(
        _metadata(original, 'existing')))
    return original


def test_recovery_bundle_is_additive_and_idempotent(tmp_path):
    original = _repo(tmp_path)
    newcomer = _entry('200000', 'new-research')
    (tmp_path / WORLD_HISTORY / newcomer['file']).write_text('# New\n')
    (tmp_path / WORLD_HISTORY / 'metadata' / '200000.json').write_bytes(
        _encode(_metadata(newcomer, 'new')))
    bundle = tmp_path / 'recover.json'
    bundle.write_bytes(_encode({
        'sections': ['how-we-know'], 'lectures': [newcomer],
        'sources': {'new': _source('new')},
    }))
    merge_world_history_overlay(tmp_path, bundle=bundle)
    once = (tmp_path / TRACK_PATH).read_bytes()
    merge_world_history_overlay(tmp_path, bundle=bundle)
    assert (tmp_path / TRACK_PATH).read_bytes() == once
    assert json.loads(once)['lectures'] == [original, newcomer]
    assert set(json.loads((tmp_path / SOURCES_PATH).read_text())['sources']) == {'existing', 'new'}


def test_zip_merges_shared_json_and_does_not_replace_previous_entries(tmp_path):
    original = _repo(tmp_path)
    newcomer = _entry('200000', 'new-research')
    # An older agent's proposal sees its own work and may omit another
    # agent's entries. The existing catalog must be preserved.
    incoming_track = {'id': 'world-history', 'sections': ['how-we-know'],
                      'lectures': [newcomer]}
    incoming_sources = {'schema_version': 1,
                        'sources': {'new': _source('new')}}
    archive = tmp_path / 'new-series.zip'
    with ZipFile(archive, 'w') as zipfile:
        zipfile.writestr(str(TRACK_PATH), _encode(incoming_track))
        zipfile.writestr(str(SOURCES_PATH), _encode(incoming_sources))
        zipfile.writestr(str(WORLD_HISTORY / newcomer['file']), '# New\n')
        zipfile.writestr(str(WORLD_HISTORY / 'metadata' / '200000.json'),
                         _encode(_metadata(newcomer, 'new')))
    merge_world_history_overlay(tmp_path, archive=archive)
    data = json.loads((tmp_path / TRACK_PATH).read_text())
    assert data['lectures'] == [original, newcomer]
    assert (tmp_path / WORLD_HISTORY / original['file']).read_text() == '# Existing\n'


def test_conflicting_id_cannot_overwrite_existing_lecture(tmp_path):
    _repo(tmp_path)
    bundle = tmp_path / 'bad.json'
    bundle.write_bytes(_encode({
        'lectures': [_entry('001000', 'renamed')],
        'sources': {},
    }))
    previous_track = (tmp_path / TRACK_PATH).read_bytes()
    with pytest.raises(MergeConflict, match='differs from an existing record'):
        merge_world_history_overlay(tmp_path, bundle=bundle)
    assert (tmp_path / TRACK_PATH).read_bytes() == previous_track


def test_conflicting_source_cannot_overwrite_existing_definition(tmp_path):
    _repo(tmp_path)
    bundle = tmp_path / 'bad.json'
    bundle.write_bytes(_encode({
        'lectures': [],
        'sources': {'existing': _source('changed')},
    }))
    with pytest.raises(MergeConflict, match='conflicts with an existing record'):
        merge_world_history_overlay(tmp_path, bundle=bundle)
    assert json.loads((tmp_path / SOURCES_PATH).read_text())['sources']['existing'] == _source('existing')


def test_stale_shared_file_is_rejected_before_any_write(tmp_path):
    _repo(tmp_path)
    (tmp_path / WORLD_HISTORY / 'README.md').write_text('Concurrent edits\n')
    archive = tmp_path / 'stale.zip'
    with ZipFile(archive, 'w') as zipfile:
        zipfile.writestr(str(TRACK_PATH), (tmp_path / TRACK_PATH).read_bytes())
        zipfile.writestr(str(SOURCES_PATH), (tmp_path / SOURCES_PATH).read_bytes())
        zipfile.writestr(str(WORLD_HISTORY / 'README.md'), 'Old content\n')
        zipfile.writestr(str(WORLD_HISTORY / 'new.md'), 'Should not be written\n')
    with pytest.raises(MergeConflict, match='Refusing to overwrite'):
        merge_world_history_overlay(tmp_path, archive=archive)
    assert not (tmp_path / WORLD_HISTORY / 'new.md').exists()
    assert (tmp_path / WORLD_HISTORY / 'README.md').read_text() == 'Concurrent edits\n'


def test_unsafe_zip_path_is_rejected(tmp_path):
    _repo(tmp_path)
    archive = tmp_path / 'bad.zip'
    with ZipFile(archive, 'w') as zipfile:
        zipfile.writestr('../escape.txt', 'bad')
    with pytest.raises(MergeConflict, match='Unsafe ZIP path'):
        merge_world_history_overlay(tmp_path, archive=archive)


def test_out_of_scope_file_is_rejected(tmp_path):
    _repo(tmp_path)
    archive = tmp_path / 'bad.zip'
    with ZipFile(archive, 'w') as zipfile:
        zipfile.writestr(str(TRACK_PATH), (tmp_path / TRACK_PATH).read_bytes())
        zipfile.writestr(str(SOURCES_PATH), (tmp_path / SOURCES_PATH).read_bytes())
        zipfile.writestr('.git/hooks/pre-commit', 'malicious write')
    with pytest.raises(MergeConflict, match='out-of-scope'):
        merge_world_history_overlay(tmp_path, archive=archive)
    assert not (tmp_path / '.git').exists()
