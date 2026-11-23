"""Code, source text and audio travel together with verifiable identities."""
import json
from zipfile import ZipFile, ZIP_DEFLATED

import pytest
from starlette.testclient import TestClient

from ailectures.core import file_digest
from ailectures.library import Library
from ailectures.storage import restore_library
from ailectures.web import create_app
from tools.deployments import export_curated as exporter
from tools.deployments.verify_export import verify
from test_deployment_and_gc import install


def reader_repository(tmp_path):
    repository = tmp_path / 'repo'
    source = repository / 'ailectures'
    (source / 'static').mkdir(parents=True)
    for filename in ('__init__.py', '__main__.py', 'README.md', 'pyproject.toml', 'static/__init__.py', 'static/index.html'):
        (source / filename).write_text('fixture source')
    # Neither arbitrary local files nor private voice material are package inputs.
    (source / '.env').write_text('private settings')
    (source / 'reference.wav').write_bytes(b'private reference audio')
    (source / 'static/reference.txt').write_text('private reference transcript')
    return repository


def fake_build(source, stage):
    folder = stage / 'wheelhouse'
    folder.mkdir()
    with ZipFile(folder / 'ailectures_reader-0.1.0-py3-none-any.whl', 'w') as zipped:
        zipped.writestr('ailectures_reader-0.1.0.dist-info/METADATA',
                        'Metadata-Version: 2.1\nName: ailectures-reader\nVersion: 0.1.0\n')
    (stage / 'reader-source').mkdir()
    (stage / 'reader-source/fixture.tar.gz').write_bytes(b'fixture distribution')


def test_code_content_lock_and_restored_playback_are_independent_of_original(tmp_path, monkeypatch):
    repository = reader_repository(tmp_path)
    library = Library(tmp_path / 'original')
    install(library, tmp_path)
    install(library, tmp_path, 'omitted')
    monkeypatch.setattr(exporter, 'build_reader', fake_build)
    output = tmp_path / 'handoff.zip'
    result = exporter.build_handoff(library, repository, {'packs': ['music']}, output, export_id='fixture-v1')
    assert result['sha256'] == file_digest(output) and result['complete'] == 1
    assert json.loads(output.with_suffix('.receipt.json').read_text()) == result
    manifest = verify(output)
    assert manifest['status'] == 'audio-complete'
    assert 'reference.wav' not in manifest['reader_source']['files']
    with ZipFile(output) as zipped:
        lock = json.loads(zipped.read('selection.lock.json'))
        assert lock['selection'] == {'lectures': ['music:001000']}
        assert lock['lectures']['music:001000']['recordings'][0]['complete']
        content = tmp_path / 'content.zip'
        content.write_bytes(zipped.read('content.zip'))
    replay = tmp_path / 'replayed.zip'
    exporter.build_handoff(library, repository, {}, replay, export_id='fixture-replay-v1', locked_selection=lock)
    with ZipFile(replay) as zipped:
        assert json.loads(zipped.read('selection.lock.json'))['lectures'] == lock['lectures']
    changed = json.loads(json.dumps(lock))
    changed['lectures']['music:001000']['revision'] = 'different'
    with pytest.raises(ValueError, match='differ'):
        exporter.build_handoff(library, repository, {}, tmp_path / 'mismatched.zip',
                               export_id='fixture-mismatch', locked_selection=changed)
    assert not (tmp_path / 'mismatched.zip').exists()
    destination = restore_library(content, tmp_path / 'restored')
    library.store.root.rename(tmp_path / 'retired')
    repository.rename(tmp_path / 'retired-repository')
    with TestClient(create_app(destination, playback_only=True)) as client:
        catalog = client.get('/api/library/catalog').json()
        assert {r['id'] for r in catalog['lectures']} == {'music:001000'}
        row = client.get('/api/library/lectures/music:001000').json()
        assert row['source'] and row['transcript']
        assert client.get(row['recordings'][0]['segments'][0]['url']).content.startswith(b'RIFF')
    # Replacing a code artifact after export is detected independently of reader imports.
    with ZipFile(output) as zipped:
        files = {key: zipped.read(key) for key in zipped.namelist()}
    wheel = next(key for key in files if key.endswith('.whl'))
    files[wheel] += b'changed'
    corrupt = tmp_path / 'changed.zip'
    with ZipFile(corrupt, 'w', compression=ZIP_DEFLATED) as zipped:
        for key, data in files.items():
            zipped.writestr(key, data)
    with pytest.raises(ValueError, match='checksum'):
        verify(corrupt)
    with pytest.raises(FileExistsError):
        exporter.build_handoff(library, tmp_path / 'retired-repository', {'packs': ['music']}, output, export_id='fixture-v1')


def test_missing_audio_stops_before_code_build(tmp_path, monkeypatch):
    library = Library(tmp_path / 'library')
    install(library, tmp_path, media=False)
    monkeypatch.setattr(exporter, 'build_reader', lambda *args: pytest.fail('Built before readiness check'))
    output = tmp_path / 'not-ready.zip'
    with pytest.raises(ValueError, match='audio'):
        exporter.build_handoff(library, tmp_path, {'packs': ['music']}, output, export_id='fixture-v1')
    assert not output.exists()


def test_drafts_are_explicit_and_selected_membership_is_frozen(tmp_path, monkeypatch):
    repository = reader_repository(tmp_path)
    library = Library(tmp_path / 'library')
    install(library, tmp_path, media=False)
    monkeypatch.setattr(exporter, 'build_reader', fake_build)
    original = exporter.export_deployment
    calls = []
    def export(library, selection, output, **kwargs):
        calls.append(selection)
        return original(library, selection, output, **kwargs)
    monkeypatch.setattr(exporter, 'export_deployment', export)
    output = tmp_path / 'draft.zip'
    result = exporter.build_handoff(library, repository, {'packs': ['music']}, output,
                                   export_id='fixture-draft-v1', allow_incomplete=True)
    assert calls == [{'lectures': ['music:001000']}]
    assert result['status'] == verify(output)['status'] == 'draft'
    assert result['missing'] == 1


def test_source_copy_rejects_package_symlinks(tmp_path):
    repository = reader_repository(tmp_path)
    source = repository / 'ailectures'
    (source / 'alias.py').symlink_to(source / '__init__.py')
    with pytest.raises(ValueError):
        exporter.copy_reader(repository, tmp_path / 'copy')
