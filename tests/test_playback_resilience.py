"""Prepared bytes stay playable independently of live synthesis and recipe drift."""
import shutil

import pytest
from starlette.testclient import TestClient

from ailectures.core import file_digest
from ailectures.web import create_app
from test_production_recovery import setup_library, manager_for, finished


@pytest.mark.parametrize("saved_profile", [False, True])
def test_issued_block_urls_do_not_open_an_engine_or_need_current_configuration(tmp_path, monkeypatch, saved_profile):
    library, pack, manifest, audio, config = setup_library(tmp_path, monkeypatch)
    manager = manager_for(library, config, lambda text, settings, destination: shutil.copyfile(audio, destination))
    try:
        if saved_profile:
            profile = manager.profile_catalog()["profiles"][0]
            job = manager.prepare_saved(["music:001000"], profile["id"])[0]
        else:
            job = manager.prepare("music:001000", "test")
        finished(manager, job["id"])
        row = manager.playback(job["id"])
        segment = row["recordings"][0]["segments"][0]
        config.unlink()
        monkeypatch.setattr(manager, "_open", lambda *args, **kwargs: (_ for _ in ()).throw(AssertionError("Playback must not open a speech engine")))
        monkeypatch.setattr(manager, "_open_saved", lambda *args, **kwargs: (_ for _ in ()).throw(AssertionError("Playback must not open a speech engine")))
        monkeypatch.setattr("ailectures.production.audio_facts", lambda *args: (_ for _ in ()).throw(AssertionError("Playback must not probe duration")))
        path = manager.playback_file(job["id"], 0, segment["sha256"])
        assert file_digest(path) == segment["sha256"]
        with TestClient(create_app(library.store.root, generation_manager=manager, playback_only=True)) as client:
            response = client.get(f"/api/library/production/jobs/{job['id']}/media/0/{segment['sha256']}", headers={"Range": "bytes=0-31"})
            assert response.status_code == 206 and response.content == path.read_bytes()[:32]
    finally:
        manager.close()


def test_changed_published_bytes_warn_but_are_not_withheld_from_playback(tmp_path, monkeypatch):
    library, pack, manifest, audio, config = setup_library(tmp_path, monkeypatch)
    manager = manager_for(library, config, lambda text, settings, destination: shutil.copyfile(audio, destination))
    try:
        job = finished(manager, manager.prepare("music:001000", "test")["id"])
        row = library.snapshot()["lectures"]["music:001000"]
        recording = row["recordings"][0]
        segment = recording["segments"][0]
        path, _ = library.store.media_file(recording["_release"], recording["id"], 0)
        # A valid WAV with additional trailing metadata remains decodable.
        changed = path.read_bytes() + b"optional metadata"
        path.write_bytes(changed)
        with TestClient(create_app(library.store.root, playback_only=True)) as client:
            url = f"/api/library/media/{recording['_release']}/{recording['id']}/0"
            response = client.get(url)
            assert response.status_code == 200 and response.content == changed
            assert response.headers["x-playback-warning"]
            assert response.headers["cache-control"] == "no-store"
            assert client.head(url).headers["x-playback-warning"]
        assert path.read_bytes() == changed
    finally:
        manager.close()
