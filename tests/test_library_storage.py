from pathlib import Path
from zipfile import ZipFile

import pytest
from starlette.testclient import TestClient

from ailectures.core import digest
from ailectures.jobs import JobStore
from ailectures.packs import PackStore, export_release
from ailectures.storage import backup_library, restore_library, storage_summary
from ailectures.web import create_app
from test_content_packs import source_pack, media_for


def test_backup_moves_media_and_personal_state_to_a_new_root(tmp_path):
    pack = source_pack()
    media = media_for(pack, tmp_path)
    manifest = export_release(pack, tmp_path / "source", media=[media])
    root = tmp_path / "original-library"
    app = create_app(root)
    app.state.library.store.install(tmp_path / "source")
    with TestClient(app) as client:
        row = client.get("/api/library/lectures/music:001000").json()
        url = row["recordings"][0]["segments"][0]["url"]
        profile = client.post("/api/listeners", json={"name": "Listener"}).json()["id"]
        queue = [dict(id="queued", lecture_id=row["id"])]
        client.post(
            f"/api/listeners/{profile}/queue", json=dict(action="add", entry=queue[0])
        )
        client.post(
            "/api/library/feedback",
            json=dict(
                lecture_id=row["id"],
                release=row["origin"]["release"],
                revision=row["revision"],
                text="Clarify this comparison.",
            ),
        )
    JobStore(root / "state").enqueue(
        [(digest("requested"), {"original_request": "retained"})]
    )
    (root / "build-cache").mkdir()
    (root / "build-cache" / "temporary").write_text("cache")
    (root / "exports").mkdir()
    (root / "exports" / "duplicate").write_text("export")
    backup = tmp_path / "library.zip"
    result = backup_library(PackStore(root), backup)
    assert result["warnings"] == []
    with ZipFile(backup) as archive:
        assert "state/listeners.sqlite3" in archive.namelist()
        assert not any(
            name.startswith(("build-cache/", "exports/")) for name in archive.namelist()
        )
    restored = restore_library(backup, tmp_path / "elsewhere" / "restored")
    root.rename(tmp_path / "retired")  # An old absolute path cannot rescue lookup.
    assert JobStore(restored / "state").get(digest("requested"))["specification"] == {
        "original_request": "retained"
    }
    with TestClient(create_app(restored)) as client:
        assert client.get(url).content == next(iter(media[2].values())).read_bytes()
        assert client.get(f"/api/listeners/{profile}/queue").json()["entries"] == queue
        assert len(client.get("/api/library/feedback").json()["events"]) == 1
        assert client.get("/api/library/lectures/music:001000").status_code == 200
    assert PackStore(restored).active()[0]["release"] == manifest["release"]
    with pytest.raises(ValueError, match="new or empty"):
        restore_library(backup, restored)


def test_accounting_distinguishes_active_and_retained_releases(tmp_path):
    pack = source_pack()
    media = media_for(pack, tmp_path)
    first = export_release(pack, tmp_path / "first", media=[media])
    store = PackStore(tmp_path / "library")
    store.install(tmp_path / "first")
    revised = source_pack(text="A revised interval comparison.")
    export_release(revised, tmp_path / "second", parent=first["release"])
    store.install(tmp_path / "second")
    data = storage_summary(store)
    assert data["active_bytes"] > 0 and data["retained_bytes"] > 0
    assert data["packs_bytes"] == data["active_bytes"] + data["retained_bytes"]
    active = next(row for row in data["releases"] if row["active"])
    retained = next(row for row in data["releases"] if not row["active"])
    assert active["ready"] == 0
    assert retained["ready"] == 1 and retained["narrators"] == 1
    store.remove("music")
    removed = storage_summary(store)
    assert (
        removed["active_bytes"] == 0
        and removed["retained_bytes"] == data["packs_bytes"]
    )


def test_restore_rejects_escaping_paths_without_publishing(tmp_path):
    archive = tmp_path / "bad.zip"
    with ZipFile(archive, "w") as output:
        output.writestr("../outside", "content")
    destination = tmp_path / "restored"
    with pytest.raises(ValueError):
        restore_library(archive, destination)
    assert not destination.exists()
