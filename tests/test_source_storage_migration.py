"""Moving source packs preserves identity, media reuse and import protection."""
from pathlib import Path
import json
from zipfile import ZipFile

import pytest

from ailectures.source_paths import pack_directory, relocated_path
from tools.content_overlay import apply, OverlayConflict, OVERLAY, sha


def test_canonical_directory_and_legacy_fallback(tmp_path):
    old = tmp_path / 'draft-stages/tts-lectures'
    old.mkdir(parents=True)
    assert pack_directory(tmp_path, 'g2') == old
    assert relocated_path(tmp_path, 'draft-stages/tts-lectures/001000-test.md').startswith('draft-stages/')
    new = tmp_path / 'content/g2'
    new.parent.mkdir()
    old.rename(new)
    assert pack_directory(tmp_path, 'g2') == new
    # A checkout can retain ignored bytecode in the old directory after git mv.
    (old / '__pycache__').mkdir(parents=True)
    (old / '__pycache__/local.pyc').write_bytes(b'ignored cache')
    assert relocated_path(tmp_path, 'draft-stages/tts-lectures/001000-test.md') == 'content/g2/001000-test.md'
    assert relocated_path(tmp_path, 'draft-stages/prerequisites/plan.json') == 'draft-stages/prerequisites/plan.json'


def test_legacy_overlay_relocates_only_after_checksum_validation(tmp_path):
    source = tmp_path / 'content/music'
    source.mkdir(parents=True)
    target = source / 'README.md'
    target.write_bytes(b'Base')
    original = 'draft-stages/tts-music/README.md'
    archive = tmp_path / 'update.zip'
    manifest = dict(schema_version=1, pack_roots=['draft-stages/tts-music'], files={original: dict(base_sha256=sha(b'Base'), sha256=sha(b'Update'))})
    with ZipFile(archive, 'w') as z:
        z.writestr(original, b'Update')
        z.writestr(OVERLAY, json.dumps(manifest))
    assert list(apply(tmp_path, archive, pack='draft-stages/tts-music')) == ['content/music/README.md']
    assert target.read_bytes() == b'Update'
    target.write_bytes(b'Concurrent edit')
    with pytest.raises(OverlayConflict):
        apply(tmp_path, archive)
    assert target.read_bytes() == b'Concurrent edit'
    assert not (tmp_path / 'draft-stages').exists()


def test_mixed_aliases_cannot_overwrite_one_destination(tmp_path):
    (tmp_path / 'content/music').mkdir(parents=True)
    archive = tmp_path / 'ambiguous.zip'
    with ZipFile(archive, 'w') as z:
        z.writestr('draft-stages/tts-music/README.md', 'old alias')
        z.writestr('content/music/README.md', 'new alias')
    with pytest.raises(ValueError, match='Duplicate destination'):
        apply(tmp_path, archive)
    assert not (tmp_path / 'content/music/README.md').exists()


def test_legacy_audio_cache_is_reused_after_source_move(tmp_path):
    from dkvis.presentation.audio_library import AudioLectureLibrary
    old = tmp_path / 'draft-stages/tts-music'
    old.mkdir(parents=True)
    (old / '001000-interval.md').write_text('# Interval\n<!-- BEGIN SPOKEN LECTURE -->\nAn interval compares two pitches.\n<!-- END SPOKEN LECTURE -->\n')
    cache = tmp_path / 'audio'
    first = AudioLectureLibrary(sources=old, cache=cache, profile='kokoro')
    try:
        settings = first.settings('af_heart', 1)
        target, text, identity = first._target('001000', 0, settings)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(b'cached audio bytes' * 30)
        pages = first.detail('001000')['pages']
    finally:
        first.close()
    new = tmp_path / 'content/music'
    new.parent.mkdir()
    old.rename(new)
    second = AudioLectureLibrary(sources=new, cache=cache, profile='kokoro', sender=lambda *a, **kw: pytest.fail('Migration must not synthesize cached audio'))
    try:
        assert second.detail('001000')['pages'] == pages
        assert second._target('001000', 0, second.settings('af_heart', 1)) == (target, text, identity)
        assert second.audio_file('001000', 0, second.settings('af_heart', 1)) == target
    finally:
        second.close()


def test_installed_recording_stays_associated_with_relocated_live_source(tmp_path):
    from ailectures.core import BEGIN, END
    from ailectures.library import Library
    from ailectures.packs import export_release
    from test_content_packs import source_pack, media_for
    repo = tmp_path / 'repository'
    old = repo / 'draft-stages/tts-music'
    old.mkdir(parents=True)
    pack = source_pack()
    row = pack['lectures']['music:001000']
    (old / '001000-interval.md').write_text('# Intervals\n' + BEGIN + '\n' + row['transcript'] + '\n' + END)
    (old / 'track.json').write_text(json.dumps(dict(id='music', title='Music', lectures=[dict(id='001000', title='Intervals', file='001000-interval.md')])))
    media = media_for(pack, tmp_path)
    export_release(pack, tmp_path / 'prepared', media=[media], kind='media')
    library = Library(tmp_path / 'reader', repository=repo)
    library.store.install(tmp_path / 'prepared')
    before = library.snapshot()['lectures']['music:001000']
    assert before['recordings'] and before['recordings'][0]['complete']
    new = repo / 'content/music'
    new.parent.mkdir()
    old.rename(new)
    after = library.snapshot()['lectures']['music:001000']
    assert after['id'] == before['id']
    assert after['spoken_sha256'] == before['spoken_sha256']
    assert after['recordings'] == before['recordings']
    assert after['origin']['pack'] == before['origin']['pack'] == 'music'


def test_existing_editorial_registry_keeps_its_identity_after_move(tmp_path):
    from tools.run_reviews import resolve_track, Track
    directory = tmp_path / 'content/world-history'
    directory.mkdir(parents=True)
    (directory / 'track.json').write_text(json.dumps(dict(id='world-history', lectures=[])))
    registry = tmp_path / 'reviews/registry'
    registry.mkdir(parents=True)
    (registry / 'findings-tts-world-history.jsonl').write_text('')
    assert resolve_track(tmp_path, 'tts-world-history') == directory
    assert resolve_track(tmp_path, 'world-history') == directory
    assert Track(tmp_path, directory).name == 'tts-world-history'
