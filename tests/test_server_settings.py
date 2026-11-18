"""Shared defaults and serving mode cannot change existing recording identity."""

from copy import deepcopy
import shutil

import pytest
from starlette.testclient import TestClient

from ailectures.core import Conflict, digest
from ailectures.settings import ServerSettings
from ailectures.web import create_app
from test_production_recovery import setup_library, manager_for, finished


def test_settings_validate_and_fence_concurrent_updates(tmp_path):
    store = ServerSettings(tmp_path)
    original = store.read()
    updated = dict(
        original,
        default_profile="test",
        profiles={"test": {"default_voice": "af_alloy", "quick_voices": ["af_alloy"]}},
    )
    store.save(updated, expected=digest(original))
    assert ServerSettings(tmp_path).read() == updated
    with pytest.raises(Conflict):
        store.save(original, expected=digest(original))
    for malformed in [
        dict(updated, playback_only="yes"),
        dict(updated, profiles=[]),
        dict(
            updated,
            profiles={
                "test": {
                    "default_voice": "af_alloy",
                    "quick_voices": ["af_alloy", "af_alloy"],
                }
            },
        ),
    ]:
        with pytest.raises(ValueError):
            store.save(malformed, expected=digest(updated))
    assert store.read() == updated


def test_shared_voice_defaults_and_quick_select_survive_restart(tmp_path, monkeypatch):
    library, pack, manifest, audio, config = setup_library(tmp_path, monkeypatch)
    calls = []

    def sender(text, settings, dest):
        calls.append(settings.voice)
        shutil.copyfile(audio, dest)

    manager = manager_for(library, config, sender)
    manager.register_voice("test", "am_echo", "Alternate")
    try:
        with TestClient(
            create_app(
                library.store.root, tts_config=config, generation_manager=manager
            )
        ) as client:
            assert client.get("/settings").status_code == 200
            settings = client.get("/api/library/settings").json()
            document = deepcopy(settings["configuration"])
            document.update(
                default_profile="test",
                profiles={
                    "test": {"default_voice": "am_echo", "quick_voices": ["am_echo"]}
                },
            )
            response = client.post(
                "/api/library/settings",
                json={"configuration": document, "revision": settings["revision"]},
            )
            assert response.status_code == 200, response.text
            assert (
                client.post(
                    "/api/library/settings",
                    json={"configuration": document, "revision": settings["revision"]},
                ).status_code
                == 409
            )
            assert (
                client.post(
                    "/api/library/settings",
                    headers={"Origin": "https://elsewhere.example"},
                    json={},
                ).status_code
                == 403
            )
            row = library.snapshot()["lectures"]["music:001000"]
            choices = manager.narrators(row)["choices"]
            assert next(c for c in choices if c["voice"] == "am_echo")[
                "profile_default"
            ]
            assert not next(c for c in choices if c["voice"] == "af_alloy")[
                "quick_select"
            ]
            result = finished(manager, manager.prepare(row["id"], "test")["id"])
            assert result["state"] == "ready" and calls == ["am_echo"]
        restarted = manager_for(library, config, sender)
        try:
            assert restarted.profiles()["profiles"][0]["voice"] == "am_echo"
            assert restarted.profiles()["default_profile"] == "test"
        finally:
            restarted.close()
    finally:
        manager.close()


def test_settings_can_disable_generation_and_cannot_unlock_startup_mode(
    tmp_path, monkeypatch
):
    library, pack, manifest, audio, config = setup_library(tmp_path, monkeypatch)
    with TestClient(create_app(library.store.root, tts_config=config)) as client:
        settings = client.get("/api/library/settings").json()
        document = dict(settings["configuration"], playback_only=True)
        assert (
            client.post(
                "/api/library/settings",
                json={"configuration": document, "revision": settings["revision"]},
            ).status_code
            == 200
        )
        assert (
            client.post(
                "/api/library/production/prepare",
                json={"lecture_id": "music:001000", "profile": "test"},
            ).status_code
            == 403
        )
        assert client.get("/api/library/production").json()["playback_only"]
        settings = client.get("/api/library/settings").json()
        assert (
            client.post(
                "/api/library/settings",
                json={
                    "configuration": dict(document, playback_only=False),
                    "revision": settings["revision"],
                },
            ).status_code
            == 200
        )
        assert client.get("/api/library/production?probe=0").json()["profiles"]
    with TestClient(
        create_app(library.store.root, tts_config=config, playback_only=True)
    ) as client:
        settings = client.get("/api/library/settings").json()
        assert settings["playback_locked"]
        assert (
            client.post(
                "/api/library/settings",
                json={
                    "configuration": dict(
                        settings["configuration"], playback_only=False
                    ),
                    "revision": settings["revision"],
                },
            ).status_code
            == 400
        )


def test_prepared_only_server_can_choose_a_default_voice(tmp_path, monkeypatch):
    library, pack, manifest, audio, config = setup_library(tmp_path, monkeypatch)
    manager = manager_for(
        library, config, lambda text, settings, dest: shutil.copyfile(audio, dest)
    )
    try:
        finished(manager, manager.prepare("music:001000", "test")["id"])
        finished(
            manager, manager.prepare("music:001000", "test", voice="am_echo")["id"]
        )
    finally:
        manager.close()
    # No TTS config on the receiving machine: use recording metadata alone.
    with TestClient(create_app(library.store.root, playback_only=True)) as client:
        settings = client.get("/api/library/settings").json()
        assert settings["profiles"][0]["id"] == "test"
        assert set(settings["voices"]["test"]["voices"]) == {"af_alloy", "am_echo"}
        document = dict(
            settings["configuration"],
            playback_only=True,
            default_profile="test",
            profiles={
                "test": {"default_voice": "am_echo", "quick_voices": ["am_echo"]}
            },
        )
        assert (
            client.post(
                "/api/library/settings",
                json={"configuration": document, "revision": settings["revision"]},
            ).status_code
            == 200
        )
        choices = client.get(
            "/api/library/production/narrators?lecture_id=music:001000"
        ).json()["choices"]
        assert sum(c["server_default"] for c in choices) == 1
        assert sum(c["quick_select"] for c in choices) == 1


def test_disabling_generation_cancels_active_work_and_voice_registration_is_validated(
    tmp_path, monkeypatch
):
    import threading

    library, pack, manifest, audio, config = setup_library(tmp_path, monkeypatch)
    release = threading.Event()

    def sender(text, settings, dest):
        release.wait(4)
        shutil.copyfile(audio, dest)

    manager = manager_for(library, config, sender)
    try:
        job = manager.prepare("music:001000", "test")
        with TestClient(
            create_app(
                library.store.root, tts_config=config, generation_manager=manager
            )
        ) as client:
            assert (
                client.post(
                    "/api/library/settings/voices",
                    json={"profile": "test", "voice": ""},
                ).status_code
                == 400
            )
            assert (
                client.post(
                    "/api/library/settings/voices",
                    json={"profile": "test", "voice": "am_echo", "label": "Alternate"},
                ).status_code
                == 200
            )
            settings = client.get("/api/library/settings").json()
            assert "am_echo" in settings["voices"]["test"]["voices"]
            response = client.post(
                "/api/library/settings",
                json={
                    "configuration": dict(
                        settings["configuration"], playback_only=True
                    ),
                    "revision": settings["revision"],
                },
            )
            assert response.status_code == 200
            assert manager.jobs.get(job["id"])["state"] == "cancelled"
            release.set()
    finally:
        release.set()
        manager.close()


def test_voice_settings_in_startup_playback_mode_leave_queued_jobs_idle(
    tmp_path, monkeypatch
):
    library, pack, manifest, audio, config = setup_library(tmp_path, monkeypatch)
    manager = manager_for(
        library, config, lambda text, settings, dest: shutil.copyfile(audio, dest)
    )
    manager.max_active_jobs = 0
    job = manager.prepare("music:001000", "test")
    assert manager.jobs.get(job["id"])["state"] == "queued"
    manager.close()
    with TestClient(
        create_app(library.store.root, tts_config=config, playback_only=True)
    ) as client:
        settings = client.get("/api/library/settings").json()
        document = dict(
            settings["configuration"], playback_only=True, default_profile="test"
        )
        assert (
            client.post(
                "/api/library/settings",
                json={"configuration": document, "revision": settings["revision"]},
            ).status_code
            == 200
        )
    assert manager.jobs.get(job["id"])["state"] == "queued"
