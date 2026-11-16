"""The selected voice owns playback, including audio still being prepared."""

import shutil
import threading
import time

from starlette.testclient import TestClient

from ailectures.web import create_app
from test_production_recovery import setup_library, manager_for, finished


def test_voice_options_match_recordings_and_do_not_start_generation(
    tmp_path, monkeypatch
):
    library, pack, manifest, audio, config = setup_library(tmp_path, monkeypatch)
    calls = []

    def sender(text, settings, dest):
        calls.append(settings.voice)
        shutil.copyfile(audio, dest)

    manager = manager_for(library, config, sender)
    manager.register_voice("test", "am_echo", "Echo")
    try:
        completed = finished(manager, manager.prepare("music:001000", "test")["id"])
        with TestClient(
            create_app(library.store.root, generation_manager=manager)
        ) as client:
            options = client.get(
                "/api/library/production/narrators?lecture_id=music:001000"
            ).json()
            first, other = options["choices"]
            assert first["profile"] == other["profile"] == "test"
            assert first["voice"] == "af_alloy" and other["voice"] == "am_echo"
            assert first["variant"] == completed["variant"]
            assert first["recording_id"] and other["recording_id"] is None
            faster = client.get(
                "/api/library/production/narrators?lecture_id=music:001000&speed=1.25"
            ).json()
            assert not faster["choices"][0]["recording_id"]
            assert len(manager.list()) == 1 and calls == ["af_alloy"]
        # A reader without production tools still offers every installed recording.
        with TestClient(create_app(library.store.root)) as client:
            offline = client.get(
                "/api/library/production/narrators?lecture_id=music:001000"
            ).json()
            assert not offline["profiles"]
            assert offline["choices"][0]["recording_id"] == first["recording_id"]
    finally:
        manager.close()


def test_first_block_plays_before_completion_with_exact_feedback_and_ranges(
    tmp_path, monkeypatch
):
    text = (
        ("First passage has a clear example. " * 5).strip()
        + "\n\n"
        + ("Second passage gives another idea. " * 5).strip()
    )
    library, pack, manifest, audio, config = setup_library(
        tmp_path, monkeypatch, text=text
    )
    second_started, release = threading.Event(), threading.Event()
    calls = []

    def sender(text, settings, dest):
        calls.append(text)
        if len(calls) == 2:
            second_started.set()
            release.wait(8)
        shutil.copyfile(audio, dest)

    manager = manager_for(library, config, sender)
    app = create_app(library.store.root, interval=0.05, generation_manager=manager)
    try:
        with TestClient(app) as client:
            response = client.post(
                "/api/library/production/prepare",
                json={
                    "lecture_id": "music:001000",
                    "profile": "test",
                    "voice": "af_alloy",
                },
            )
            assert response.status_code == 202, response.text
            job = response.json()
            assert second_started.wait(3)
            partial = client.get(
                f"/api/library/production/jobs/{job['id']}/playback"
            ).json()
            rec = partial["recordings"][0]
            assert (
                not rec["complete"]
                and len(rec["segments"]) == 1
                and len(rec["pages"]) == 2
            )
            assert rec["generator"]["voice"] == "af_alloy"
            segment = rec["segments"][0]
            result = client.get(segment["url"], headers={"Range": "bytes=0-31"})
            assert result.status_code == 206 and len(result.content) == 32
            assert client.get(segment["url"][:-64] + "f" * 64).status_code == 404
            assert (
                client.get(f"/api/library/production/jobs/{job['id']}").json()["state"]
                == "running"
            )
            feedback = client.post(
                "/api/library/feedback",
                json={
                    "lecture_id": partial["id"],
                    "release": partial["origin"]["release"],
                    "revision": partial["revision"],
                    "recording_id": rec["id"],
                    "segment": 0,
                    "seconds": 0.1,
                    "text": "A note while listening.",
                },
            )
            assert feedback.status_code == 201, feedback.text
            old = client.get(
                f"/api/library/lectures/music:001000?release={partial['origin']['release']}"
            ).json()
            assert old["recordings"][0]["segments"][0]["url"] == segment["url"]
            release.set()
            completed = finished(manager, job["id"])
            assert completed["state"] == "ready" and len(calls) == 2
            row = client.get("/api/library/lectures/music:001000").json()
            assert row["recordings"][0]["complete"]
            assert client.get(segment["url"]).status_code == 200
    finally:
        release.set()
        manager.close()


def test_reading_cancelled_blocks_after_restart_never_restarts_synthesis(
    tmp_path, monkeypatch
):
    library, pack, manifest, audio, config = setup_library(tmp_path, monkeypatch)
    calls = []

    def sender(text, settings, dest):
        calls.append(text)
        shutil.copyfile(audio, dest)

    manager = manager_for(library, config, sender)
    job = manager.prepare("music:001000", "test")
    deadline = time.monotonic() + 3
    while time.monotonic() < deadline:
        live = manager._jobs[job["id"]]
        if live["engine"].inventory("000000", live["settings"])["ready"]:
            break
        time.sleep(0.01)
    manager.cancel(job["id"])
    manager.close()
    restarted = manager_for(library, config, sender)
    try:
        row = restarted.playback(job["id"])
        assert row["recordings"][0]["segments"]
        assert restarted.jobs.get(job["id"])["state"] == "cancelled"
        assert len(calls) == 1 and not restarted._jobs
    finally:
        restarted.close()


def test_requested_block_precedes_background_cache(tmp_path, monkeypatch):
    text = "\n\n".join(
        ((name + " passage has a clear example. ") * 5).strip()
        for name in ("First", "Second", "Third", "Fourth")
    )
    library, pack, manifest, audio, config = setup_library(
        tmp_path, monkeypatch, text=text
    )
    started, release = threading.Event(), threading.Event()
    calls = []

    def sender(text, settings, dest):
        calls.append(text)
        if len(calls) == 1:
            started.set()
            release.wait(5)
        shutil.copyfile(audio, dest)

    manager = manager_for(library, config, sender)
    try:
        with TestClient(
            create_app(library.store.root, interval=0.05, generation_manager=manager)
        ) as client:
            job = client.post(
                "/api/library/production/prepare",
                json={"lecture_id": "music:001000", "profile": "test"},
            ).json()
            assert started.wait(3)
            response = client.post(
                f"/api/library/production/jobs/{job['id']}/playback", json={"index": 2}
            )
            assert response.status_code == 202, response.text
            release.set()
            assert finished(manager, job["id"])["state"] == "ready"
            assert len(calls) == 4 and calls[1].startswith("Third")
    finally:
        release.set()
        manager.close()
