"""Ordinary ZIP imports, rollback, coherent reads, and usable partial catalogs."""

from concurrent.futures import ThreadPoolExecutor
import json
from pathlib import Path
import subprocess
import sys
import threading
from zipfile import ZipFile

import pytest

from ailectures.catalog import RepositoryCatalog
from ailectures.source_updates import apply_files, atomic_bytes, source_lock
from tools.content_overlay import OverlayConflict, apply, build
from test_content_overlay import pack


def plain_zip(root, path, *, prefix=""):
    with ZipFile(path, "w") as archive:
        for file in root.rglob("*"):
            if file.is_file():
                archive.write(file, prefix + file.relative_to(root).as_posix())


def test_plain_zip_build_needs_no_snapshot_and_imports_in_one_step(tmp_path):
    author = tmp_path / "author"
    author.mkdir()
    pack(author, "music")
    archive = tmp_path / "music.zip"
    build(author, ["content/music"], archive)
    with ZipFile(archive) as source:
        assert "content-overlay.json" not in source.namelist()
    target = tmp_path / "target"
    target.mkdir()
    assert len(apply(target, archive)) == 3
    assert "music:001000" in RepositoryCatalog(target).snapshot()["music"]["lectures"]
    assert apply(target, archive) == []


def test_wrapped_plain_zip_and_owned_replacement_keep_previous_files(tmp_path):
    author = tmp_path / "author"
    author.mkdir()
    directory = pack(author, "music")
    plain_zip(directory, tmp_path / "first.zip", prefix="download/")
    target = tmp_path / "target"
    target.mkdir()
    apply(target, tmp_path / "first.zip")
    path = directory / "001000-introduction.md"
    old = path.read_bytes()
    path.write_text(path.read_text().replace("an example", "a revised example"))
    plain_zip(directory, tmp_path / "changed.zip", prefix="download/")
    with pytest.raises(OverlayConflict):
        apply(target, tmp_path / "changed.zip")
    assert (target / "content/music/001000-introduction.md").read_bytes() == old
    result = apply(target, tmp_path / "changed.zip", replace_owned=True)
    assert (
        result.backup / "before/content/music/001000-introduction.md"
    ).read_bytes() == old
    assert (
        target / "content/music/001000-introduction.md"
    ).read_bytes() == path.read_bytes()


def test_plain_zip_does_not_need_valid_metadata_to_import(tmp_path):
    source = tmp_path / "source"
    source.mkdir()
    pack(source, "music")
    (source / "content/music/track.json").write_text("unfinished JSON")
    plain_zip(source, tmp_path / "draft.zip")
    target = tmp_path / "target"
    target.mkdir()
    apply(target, tmp_path / "draft.zip")
    catalog = RepositoryCatalog(target)
    assert catalog.snapshot()["music"]["lectures"]
    assert catalog.errors


def test_failed_write_rolls_back_all_changes(tmp_path):
    pack(tmp_path, "music")
    first = "content/music/001000-introduction.md"
    second = "content/music/metadata/001000.json"
    original = {path: (tmp_path / path).read_bytes() for path in [first, second]}
    calls = []

    def failing_write(path, data):
        calls.append(path)
        if len(calls) == 2:
            raise OSError("injected disk error")
        atomic_bytes(path, data)

    with source_lock(tmp_path, write=True), pytest.raises(OSError, match="disk error"):
        apply_files(
            tmp_path,
            {first: b"new manuscript", second: b"new metadata"},
            replace_file=failing_write,
        )
    assert all(
        (tmp_path / path).read_bytes() == data for path, data in original.items()
    )
    assert not (tmp_path / ".content-update/active.json").exists()


def test_hard_process_exit_recovers_before_a_fresh_catalog_reads(tmp_path):
    directory = pack(tmp_path, "music")
    before = RepositoryCatalog(tmp_path).snapshot()["music"]
    paths = [
        "content/music/001000-introduction.md",
        "content/music/metadata/001000.json",
    ]
    original = {path: (tmp_path / path).read_bytes() for path in paths}
    code = """
import os,sys
from pathlib import Path
from ailectures.source_updates import source_lock,apply_files,atomic_bytes
root=Path(sys.argv[1])
def interrupted(path,data):
    atomic_bytes(path,data)
    os._exit(81)
with source_lock(root,write=True):
    apply_files(root,{'content/music/001000-introduction.md':b'new source','content/music/metadata/001000.json':b'new metadata'},replace_file=interrupted)
"""
    result = subprocess.run([sys.executable, "-c", code, str(tmp_path)])
    assert result.returncode == 81
    assert (tmp_path / ".content-update/active.json").exists()
    after = RepositoryCatalog(tmp_path).snapshot()["music"]
    assert after == before
    assert all(
        (tmp_path / path).read_bytes() == data for path, data in original.items()
    )
    assert not (tmp_path / ".content-update/active.json").exists()


def test_reader_waits_for_a_coherent_import(tmp_path):
    directory = pack(tmp_path, "music")
    reader = RepositoryCatalog(tmp_path)
    reader.snapshot()
    first = "content/music/001000-introduction.md"
    second = "content/music/metadata/001000.json"
    replacement = (
        (tmp_path / first).read_bytes().replace(b"an example", b"a revised example")
    )
    payload = {
        first: replacement,
        second: json.dumps({"revision_note": "new"}).encode(),
    }
    written = threading.Event()
    release = threading.Event()
    reading = threading.Event()

    def writer():
        def slow(path, data):
            atomic_bytes(path, data)
            if not written.is_set():
                written.set()
                assert release.wait(3)

        with source_lock(tmp_path, write=True):
            apply_files(tmp_path, payload, replace_file=slow)

    def read():
        reading.set()
        return reader.snapshot()

    with ThreadPoolExecutor(2) as pool:
        writing = pool.submit(writer)
        assert written.wait(2)
        result = pool.submit(read)
        assert reading.wait(2)
        assert not result.done()
        release.set()
        writing.result()
        published = result.result()["music"]["lectures"]["music:001000"]
        assert published["source"].encode() == replacement
        assert published["metadata"]["revision_note"] == "new"


def test_bad_item_and_missing_citation_do_not_hide_usable_neighbors(tmp_path):
    directory = pack(tmp_path, "music")
    second = directory / "002000-next.md"
    second.write_text(
        "# Next\n<!-- BEGIN SPOKEN LECTURE -->An independent explanation.<!-- END SPOKEN LECTURE -->"
    )
    metadata = directory / "metadata/001000.json"
    metadata.write_text(
        json.dumps({"related_resources": [{"source_id": "unfinished-reference"}]})
    )
    reader = RepositoryCatalog(tmp_path)
    first = reader.snapshot()["music"]
    assert set(first["lectures"]) == {"music:001000", "music:002000"}
    assert first["courses"]["music:main"]["lectures"] == ["music:001000"]
    assert reader.errors
    second.write_text("incomplete spoken markers")
    restarted = RepositoryCatalog(tmp_path)
    assert set(restarted.snapshot()["music"]["lectures"]) == {
        "music:001000",
        "music:002000",
    }
    third = directory / "003000-unfinished.md"
    third.write_text("not yet narratable")
    assert set(restarted.snapshot()["music"]["lectures"]) == {
        "music:001000",
        "music:002000",
    }
    assert restarted.errors


def test_optional_catalog_cache_failure_does_not_block_sources(tmp_path, monkeypatch):
    pack(tmp_path, "music")

    def unavailable(*args):
        raise PermissionError("read-only snapshot cache")

    monkeypatch.setattr("ailectures.catalog.atomic_bytes", unavailable)
    reader = RepositoryCatalog(tmp_path)
    assert reader.snapshot()["music"]["lectures"]
    assert reader.errors


def test_side_notes_do_not_invalidate_an_installed_playable_pack(tmp_path):
    from ailectures.packs import PackStore, export_release
    from test_content_packs import source_pack

    release = tmp_path / "release"
    manifest = export_release(source_pack(), release)
    (release / "notes.txt").write_text("Local notes outside the runtime index.")
    store = PackStore(tmp_path / "library")
    assert store.install(release)["release"] == manifest["release"]
    assert "music:001000" in store.snapshot()["lectures"]
