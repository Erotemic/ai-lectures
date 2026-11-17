"""Browser exports contain declared sources/media and no personal server state."""
import zipfile

import pytest

from ailectures.exports import export_file, export_pack
from ailectures.library import Library
from ailectures.packs import export_release
from test_content_packs import source_pack, media_for


def test_installed_sources_and_audio_transfer_without_original_files(tmp_path):
    pack = source_pack()
    export_release(pack, tmp_path / 'release', media=[media_for(pack, tmp_path)])
    library = Library(tmp_path / 'library')
    library.store.install(tmp_path / 'release')
    (library.store.state / 'private-listener-note.txt').write_text('Do not export this')
    report = export_pack(library, 'music')
    path, filename = export_file(library, report['id'])
    assert filename.endswith('.zip') and report['recordings'] == 1
    with zipfile.ZipFile(path) as archive:
        assert 'catalog.json' in archive.namelist()
        assert not any('private-listener' in name for name in archive.namelist())
    moved = Library(tmp_path / 'moved')
    moved.store.install(path)
    row = moved.snapshot()['lectures']['music:001000']
    assert row['spoken_sha256'] == pack['lectures']['music:001000']['spoken_sha256']
    assert row['recordings'][0]['complete']
    source = export_pack(library, 'music', source_only=True)
    only = Library(tmp_path / 'text-only')
    only.store.install(export_file(library, source['id'])[0])
    assert not only.snapshot()['lectures']['music:001000']['recordings']


def test_export_rejects_unknown_packs_and_untrusted_download_paths(tmp_path):
    library = Library(tmp_path / 'library')
    with pytest.raises(KeyError):
        export_pack(library, 'missing')
    with pytest.raises(ValueError):
        export_file(library, '../state')
