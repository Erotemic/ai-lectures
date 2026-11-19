"""Saved profiles fix identity and pin complete recipes without touching legacy media."""

import json
import shutil

import pytest
from starlette.testclient import TestClient

from ailectures.core import Conflict, digest
from ailectures.production import GenerationManager
from ailectures.voice_profiles import recipe_from_config, revision_id
from ailectures.web import create_app
from test_production_recovery import setup_library, manager_for, finished


def catalog_profile(manager):
    catalog = manager.profile_catalog()
    assert len(catalog["profiles"]) == 1
    return catalog, catalog["profiles"][0]


def test_migration_is_local_idempotent_and_does_not_expand_server_voice_catalog(
    tmp_path, monkeypatch
):
    library, pack, manifest, audio, config = setup_library(tmp_path, monkeypatch)
    manager = manager_for(
        library, config, lambda text, settings, dest: shutil.copyfile(audio, dest)
    )
    try:
        manager.register_voice("test", "am_echo")
        original = config.read_bytes()
        catalog, profile = catalog_profile(manager)
        assert profile["voice"] == "af_alloy"
        assert {
            row["voice"]
            for row in manager.profile_backend_voices(profile["backend_id"])["voices"]
        } == {"af_alloy", "am_echo"}
        assert manager.profile_catalog()["profiles"][0]["id"] == profile["id"]
        assert config.read_bytes() == original
        manager.saved_profile_store().set_presentation(
            profile["id"], label="Renamed", quick=False
        )
        after = manager.profile_catalog()["profiles"][0]
        assert (
            after["revision"] == profile["revision"]
            and after["label"] == "Renamed"
            and not after["quick_select"]
        )
    finally:
        manager.close()


def test_reference_change_requires_a_saved_revision_not_a_generation_override(
    tmp_path, monkeypatch
):
    library, pack, manifest, audio, config = setup_library(tmp_path, monkeypatch)
    config.write_text(
        config.read_text().replace('model="kokoro"', 'model="breeze-tts2"')
        + '\n[profiles.test.reference]\nsource="test-fixture"\naudio="fixture.wav"\ntranscript="fixture.txt"\n'
    )
    manager = manager_for(
        library, config, lambda text, settings, dest: shutil.copyfile(audio, dest)
    )
    try:
        catalog, profile = catalog_profile(manager)
        assert profile["fixed_reference"]
        manager.register_voice("test", "another-voice")
        with pytest.raises(ValueError, match="fixed"):
            manager.prepare("music:001000", "test", voice="another-voice")
        changed = manager.save_profile(
            dict(
                id=profile["id"],
                expected_revision=profile["revision"],
                label="Changed voice",
                backend_id=profile["backend_id"],
                voice="another-voice",
            )
        )
        assert (
            changed["id"] == profile["id"]
            and changed["revision"] != profile["revision"]
        )
        assert changed["voice"] == "another-voice"
        saved = manager.saved_profile_store().get(profile["id"])
        assert (
            saved["recipe"]["reference"] is None
            and not saved["recipe"]["fixed_reference"]
        )
        assert manager.saved_profile_store().get(profile["id"], profile["revision"])[
            "recipe"
        ]["reference"]
        with TestClient(
            create_app(
                library.store.root, tts_config=config, generation_manager=manager
            )
        ) as client:
            response = client.post(
                "/api/library/production/prepare",
                json={
                    "lecture_id": "music:001000",
                    "profile": profile["id"],
                    "profile_revision": profile["revision"],
                    "voice": "another-voice",
                },
            )
            assert response.status_code == 400
    finally:
        manager.close()


def test_recipe_edits_create_revisions_and_existing_jobs_keep_their_snapshot(
    tmp_path, monkeypatch
):
    library, pack, manifest, audio, config = setup_library(tmp_path, monkeypatch)
    calls = []

    def sender(text, settings, dest):
        calls.append(settings.voice)
        shutil.copyfile(audio, dest)

    manager = manager_for(library, config, sender, max_active_jobs=0)
    try:
        catalog, profile = catalog_profile(manager)
        queued = manager.prepare_saved(["music:001000"], profile["id"])[0]
        old = manager.saved_profile_store().get(profile["id"])
        new = manager.save_profile(
            dict(
                id=profile["id"],
                expected_revision=profile["revision"],
                label="New title delivery",
                settings={"title_pause_after": 1.2},
            )
        )
        assert new["revision"] != profile["revision"]
        assert (
            manager.saved_profile_store().get(profile["id"], profile["revision"])[
                "recipe"
            ]
            == old["recipe"]
        )
        manager.max_active_jobs = 1
        result = finished(manager, queued["id"])
        assert result["state"] == "ready"
        record = library.snapshot()["lectures"]["music:001000"]["recordings"][0]
        assert record["generator"]["profile_revision"] == profile["revision"]
        second = manager.prepare_saved(["music:001000"], profile["id"])[0]
        assert second["id"] != queued["id"] and second["variant"] != queued["variant"]
        assert finished(manager, second["id"])["state"] == "ready"
        assert len(calls) == 2
        assert len(library.snapshot()["lectures"]["music:001000"]["recordings"]) == 2
        with pytest.raises(Conflict):
            manager.save_profile(
                dict(
                    id=profile["id"],
                    expected_revision=profile["revision"],
                    label="Stale edit",
                )
            )
    finally:
        manager.close()


def test_backend_relocation_and_environment_edits_do_not_change_frozen_audio_inputs(
    tmp_path, monkeypatch
):
    library, pack, manifest, audio, config = setup_library(tmp_path, monkeypatch)
    manager = manager_for(
        library,
        config,
        lambda text, settings, dest: shutil.copyfile(audio, dest),
        max_active_jobs=0,
    )
    try:
        _, profile = catalog_profile(manager)
        request = manager.prepare_saved(["music:001000"], profile["id"])[0]
        before = manager._open(manager.jobs.get(request["id"]), start=False)
        target1 = before["engine"]._target_from_text(
            "000000",
            0,
            before["settings"],
            pack["lectures"]["music:001000"]["transcript"],
        )[2]
        before["engine"].close()
        config.write_text(config.read_text().replace(":1/v1", ":9/v1"))
        monkeypatch.setenv("DKVIS_AUDIO_TTS_VOICE", "am_echo")
        monkeypatch.setenv("DKVIS_AUDIO_PAGE_CHARS", "900")
        after = manager._open(manager.jobs.get(request["id"]), start=False)
        try:
            assert (
                after["settings"].voice == "af_alloy"
                and after["engine"].page_chars == 250
            )
            assert ":9/" in after["engine"].endpoint
            target2 = after["engine"]._target_from_text(
                "000000",
                0,
                after["settings"],
                pack["lectures"]["music:001000"]["transcript"],
            )[2]
            assert target2 == target1
        finally:
            after["engine"].close()
    finally:
        manager.close()


def test_native_rate_and_tempo_are_separate_and_unsupported_native_rate_is_rejected(
    tmp_path, monkeypatch
):
    library, pack, manifest, audio, config = setup_library(tmp_path, monkeypatch)
    manager = manager_for(
        library, config, lambda text, settings, dest: shutil.copyfile(audio, dest)
    )
    try:
        _, profile = catalog_profile(manager)
        rate = manager.save_profile(
            dict(
                id=profile["id"],
                expected_revision=profile["revision"],
                label="Measured rate",
                settings={"native_rate": 1.2, "tempo": 0.9},
            )
        )
        recipe = manager.saved_profile_store().get(rate["id"])["recipe"]
        from ailectures.render_recipe import compile_recipe

        backend = manager.saved_profile_store().backends()[0]
        document, speed = compile_recipe(
            manager.saved_profile_store().get(rate["id"]), backend
        )
        assert speed == 1.2 and recipe["tempo"] == 0.9
        # A different backend family cannot inherit a native-rate control.
        config.write_text(
            config.read_text().replace('model="kokoro"', 'model="breeze-tts2"')
        )
        fresh = manager.profile_backend_voices(profile["backend_id"])
        with pytest.raises(ValueError, match="native speaking"):
            manager.save_profile(
                dict(
                    label="Unsupported",
                    backend_id=profile["backend_id"],
                    voice="af_alloy",
                    settings={"native_rate": 1.2},
                )
            )
    finally:
        manager.close()


def test_saved_cache_reset_and_archiving_preserve_other_revisions(
    tmp_path, monkeypatch
):
    library, pack, manifest, audio, config = setup_library(tmp_path, monkeypatch)
    manager = manager_for(
        library, config, lambda text, settings, dest: shutil.copyfile(audio, dest)
    )
    try:
        _, profile = catalog_profile(manager)
        first = manager.prepare_saved(["music:001000"], profile["id"])[0]
        finished(manager, first["id"])
        updated = manager.save_profile(
            dict(
                id=profile["id"],
                expected_revision=profile["revision"],
                label="Changed",
                settings={"title_pause_after": 1.0},
            )
        )
        second = manager.prepare_saved(["music:001000"], updated["id"])[0]
        finished(manager, second["id"])
        row = library.snapshot()["lectures"]["music:001000"]
        manager.clear_saved_cache(
            row["id"],
            updated["id"],
            revision=row["revision"],
            profile_revision=updated["revision"],
        )
        records = library.snapshot()["lectures"][row["id"]]["recordings"]
        assert (
            len(records) == 1
            and records[0]["generator"]["profile_revision"] == profile["revision"]
        )
        request = manager.prepare_saved([row["id"]], updated["id"])[0]
        assert request["id"] != second["id"]
        finished(manager, request["id"])
        manager.saved_profile_store().archive(profile["id"])
        assert not manager.profile_catalog()["profiles"]
        assert library.snapshot()["lectures"][row["id"]]["recordings"]
        with pytest.raises(ValueError, match="active"):
            manager.prepare_saved([row["id"]], profile["id"])
    finally:
        manager.close()


def test_profile_api_preview_and_save_never_publish_a_preview_lecture(
    tmp_path, monkeypatch
):
    library, pack, manifest, audio, config = setup_library(tmp_path, monkeypatch)
    manager = manager_for(
        library, config, lambda text, settings, dest: shutil.copyfile(audio, dest)
    )
    with TestClient(
        create_app(library.store.root, tts_config=config, generation_manager=manager)
    ) as client:
        catalog = client.get("/api/library/voice-profiles").json()
        profile = catalog["profiles"][0]
        draft = client.get("/api/library/voice-profiles/" + profile["id"]).json()
        assert draft["profile"]["voice"] == "af_alloy"
        assert (
            client.post(
                "/api/library/voice-profiles/save",
                headers={"Origin": "https://other.example"},
                json={},
            ).status_code
            == 403
        )
        response = client.post(
            "/api/library/voice-profiles/preview",
            json={"id": profile["id"], "label": "Preview"},
        )
        assert response.status_code == 200, response.text
        assert client.get(response.json()["url"]).status_code == 200
        assert set(client.get("/api/library/catalog").json()["lectures"][0])
        assert len(library.snapshot()["lectures"]) == 1
        assert not library.snapshot()["lectures"]["music:001000"]["recordings"]


@pytest.mark.parametrize("codec", ["ogg", "mp3"])
def test_postprocessing_applies_tempo_once_and_rescales_word_timing(tmp_path, codec):
    import subprocess
    from ailectures.render_recipe import page_processor
    from dkvis.presentation.media import duration
    from dkvis.presentation.audio_quality import settings

    if not shutil.which("ffmpeg"):
        pytest.skip("FFmpeg unavailable")
    audio = tmp_path / ("page." + codec)
    subprocess.run(
        [
            "ffmpeg",
            "-y",
            "-v",
            "error",
            "-f",
            "lavfi",
            "-i",
            "sine=frequency=330:duration=3",
            str(audio),
        ],
        check=True,
    )
    before = duration(audio)
    timing = audio.with_name(audio.name + ".timings.json")
    timing.write_text(
        json.dumps(dict(duration=before, chunks=[dict(start=0, end=before, words=9)]))
    )

    class Task:
        def check_cancelled(self):
            pass

    page_processor(dict(tempo=1.25, processing=settings({"enabled": True})))(
        audio, codec, Task()
    )
    after = duration(audio)
    updated = json.loads(timing.read_text())
    assert abs(after - before / 1.25) < 0.1
    assert updated["duration"] == after and updated["chunks"][0]["end"] == after
    assert updated["chunks"][0]["words"] == 9
    assert (
        audio.read_bytes().startswith(b"OggS")
        if codec == "ogg"
        else audio.stat().st_size > 256
    )


def test_new_profile_api_generation_and_catalog_keep_one_choice_per_recipe(
    tmp_path, monkeypatch
):
    library, pack, manifest, audio, config = setup_library(tmp_path, monkeypatch)
    manager = manager_for(
        library, config, lambda text, settings, dest: shutil.copyfile(audio, dest)
    )
    manager.register_voice("test", "am_echo")
    with TestClient(
        create_app(library.store.root, tts_config=config, generation_manager=manager)
    ) as client:
        profile = client.get("/api/library/voice-profiles").json()["profiles"][0]
        duplicate = client.post(
            "/api/library/voice-profiles/save",
            json=dict(
                duplicate_of=profile["id"], voice="am_echo", label="Second recipe"
            ),
        )
        assert duplicate.status_code == 201, duplicate.text
        second = duplicate.json()
        assert second["id"] != profile["id"] and second["voice"] == "am_echo"
        row = library.snapshot()["lectures"]["music:001000"]
        choices = manager.saved_narrators(row)["choices"]
        assert len(choices) == 2 and all(choice["fixed_recipe"] for choice in choices)
        response = client.post(
            "/api/library/production/prepare",
            json=dict(
                lecture_id=row["id"],
                profile=second["id"],
                profile_revision=second["revision"],
                revision=row["revision"],
            ),
        )
        assert response.status_code == 202, response.text
        assert finished(manager, response.json()["id"])["state"] == "ready"
        recording = library.snapshot()["lectures"][row["id"]]["recordings"][0]
        assert recording["generator"]["profile"] == second["id"]
        assert recording["generator"]["profile_revision"] == second["revision"]


def test_installed_only_settings_need_no_optional_production_imports(
    tmp_path, monkeypatch
):
    import builtins
    from ailectures.library import Library

    original = builtins.__import__

    def no_production(name, *args, **kwargs):
        if name == "dkvis" or name.startswith("dkvis."):
            raise ImportError("Production stack intentionally absent")
        return original(name, *args, **kwargs)

    monkeypatch.setattr(builtins, "__import__", no_production)
    library = Library(tmp_path / "reader")
    with TestClient(create_app(library.store.root, playback_only=True)) as client:
        assert client.get("/api/library/settings").status_code == 200
        catalog = client.get("/api/library/voice-profiles")
        assert catalog.status_code == 200, catalog.text
        assert catalog.json()["profiles"] == []
        assert not catalog.json()["tools_available"]


def test_saved_breeze_titles_and_prose_use_distinct_frozen_instructions(
    tmp_path, monkeypatch
):
    import io
    import urllib.request
    from test_title_delivery import wav_bytes, manuscript
    from dkvis.presentation.tts import resolve_profile
    from dkvis.presentation.audio_library import AudioLectureLibrary
    from ailectures.voice_profiles import capabilities
    from ailectures.render_recipe import compile_recipe

    monkeypatch.setenv("DKVIS_AUDIO_BREEZE_JOB_API", "0")
    monkeypatch.setenv("DKVIS_AUDIO_BREEZE_LONG_FORM", "1")
    config = resolve_profile(
        {
            "profiles": {
                "test": dict(
                    endpoint="http://127.0.0.1:1/v1/audio/speech",
                    model="breeze-tts2",
                    voice="fixture-reference",
                    response_format="wav",
                )
            }
        },
        "test",
    )
    recipe = recipe_from_config(config, "backend-fixture")
    recipe.update(
        body_mode="directed",
        title_instruction="Read as a distinct heading.",
        title_cfg_scale=6,
    )
    recipe["config"]["request"] = {
        "instruction": "Speak measured prose.",
        "cfg_scale": 3,
    }
    profile = dict(id="voice-fixture", revision=revision_id(recipe), recipe=recipe)
    backend = dict(
        id="backend-fixture",
        available=True,
        model="breeze-tts2",
        endpoint=config["endpoint"],
        capabilities=capabilities("breeze-tts2"),
    )
    document, speed = compile_recipe(profile, backend)
    requests = []

    class Response(io.BytesIO):
        pass

    def respond(request, timeout):
        requests.append(json.loads(request.data))
        response = Response(wav_bytes())
        response.headers = {"Content-Type": "audio/wav"}
        return response

    monkeypatch.setattr(urllib.request, "urlopen", respond)
    (tmp_path / "000000-test.md").write_text(
        manuscript("## First heading\n\nFirst body sentence.")
    )
    engine = AudioLectureLibrary(
        sources=tmp_path,
        cache=tmp_path / "cache",
        document=document,
        profile="voice-fixture",
        title_handling=True,
    )
    try:
        settings = engine.settings(speed=speed)
        target, text, key = engine._target("000000", 0, settings)
        engine._generate(target, text, settings)
        assert requests[0]["input"] == "First heading"
        assert (
            requests[0]["instruction"] == recipe["title_instruction"]
            and requests[0]["cfg_scale"] == 6
        )
        assert (
            requests[1]["instruction"] == "Speak measured prose."
            and requests[1]["cfg_scale"] == 3
        )
        assert not any(request.get("long_form") for request in requests)
    finally:
        engine.close()


def test_first_import_preserves_existing_default_voice_preference(
    tmp_path, monkeypatch
):
    library, pack, manifest, audio, config = setup_library(tmp_path, monkeypatch)
    manager = manager_for(
        library, config, lambda text, settings, dest: shutil.copyfile(audio, dest)
    )
    try:
        settings = manager.preferences.read()
        settings["profiles"] = {
            "test": {"default_voice": "am_echo", "quick_voices": ["am_echo"]}
        }
        manager.preferences.save(settings, expected=digest(manager.preferences.read()))
        _, profile = catalog_profile(manager)
        assert profile["voice"] == "am_echo"
        settings["profiles"]["test"]["default_voice"] = "af_alloy"
        manager.preferences.save(settings, expected=digest(manager.preferences.read()))
        assert manager.profile_catalog()["profiles"][0]["voice"] == "am_echo"
    finally:
        manager.close()


def test_backend_discovery_uses_effective_connection_merges_aliases_and_survives_outage(
    tmp_path, monkeypatch
):
    from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
    import threading

    library, pack, manifest, audio, config = setup_library(tmp_path, monkeypatch)
    config.write_text(
        config.read_text()
        + '\n[profiles.alternate]\nendpoint="http://127.0.0.1:1/v1/audio/speech"\nmodel="kokoro"\nvoice="af_heart"\nresponse_format="mp3"\n'
    )
    requested = []

    class Handler(BaseHTTPRequestHandler):
        def log_message(self, *args):
            pass

        def do_GET(self):
            requested.append(self.path)
            payload = json.dumps(
                {"voices": ["fixture-v" + str(i) for i in range(3, 8)]}
            ).encode()
            self.send_response(200)
            self.send_header("Content-Length", str(len(payload)))
            self.end_headers()
            self.wfile.write(payload)

    server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    manager = manager_for(
        library,
        config,
        lambda text, settings, dest: shutil.copyfile(audio, dest),
        endpoint=f"http://127.0.0.1:{server.server_port}/v1/audio/speech",
    )
    try:
        catalog = manager.profile_catalog()
        backend = catalog["backends"][0]["id"]
        manager.register_voice("test", "registered-first")
        manager.register_voice("alternate", "registered-second")
        with TestClient(
            create_app(
                library.store.root, tts_config=config, generation_manager=manager
            )
        ) as client:
            url = "/api/library/voice-profiles/backends/" + backend + "/voices"
            cached = client.get(url).json()
            assert not requested
            assert {"registered-first", "registered-second"} <= {
                v["voice"] for v in cached["voices"]
            }
            live = client.post(url, json={"refresh": True}).json()
            assert live["discovery"] == "live" and requested == ["/v1/audio/voices"]
            assert {"fixture-v" + str(i) for i in range(3, 8)} <= {
                v["voice"] for v in live["voices"]
            }
            assert len(manager.profile_catalog()["profiles"]) == 2
            server.shutdown()
            server.server_close()
            thread.join()
            offline = client.post(url, json={"refresh": True}).json()
            assert offline["discovery"] == "unavailable"
            assert {v["voice"] for v in live["voices"]} == {
                v["voice"] for v in offline["voices"]
            }
    finally:
        if thread.is_alive():
            server.shutdown()
            server.server_close()
            thread.join()
        manager.close()


def test_voice_reference_edit_keeps_recipe_jobs_and_previous_recordings(
    tmp_path, monkeypatch
):
    library, pack, manifest, audio, config = setup_library(tmp_path, monkeypatch)
    config.write_text(
        config.read_text()
        + '\n[profiles.other]\nendpoint="http://127.0.0.1:1/v1/audio/speech"\nmodel="kokoro"\nvoice="am_echo"\nresponse_format="mp3"\n[profiles.other.reference]\nsource="test-fixture"\naudio="second.wav"\ntranscript="second.txt"\n'
    )
    calls = []

    def sender(text, settings, dest):
        calls.append((settings.voice, settings.speed))
        shutil.copyfile(audio, dest)

    manager = manager_for(library, config, sender, max_active_jobs=0)
    try:
        profile = next(
            p for p in manager.profile_catalog()["profiles"] if p["label"] == "test"
        )
        profile = manager.save_profile(
            dict(
                id=profile["id"],
                expected_revision=profile["revision"],
                label="Narrator",
                settings={
                    "native_rate": 1.15,
                    "title_pause_after": 0.9,
                    "pronunciation_replacements": {"TTS": "text to speech"},
                },
            )
        )
        old = manager.saved_profile_store().get(profile["id"])
        queued = manager.prepare_saved(["music:001000"], profile["id"])[0]
        with TestClient(
            create_app(
                library.store.root, tts_config=config, generation_manager=manager
            )
        ) as client:
            response = client.post(
                "/api/library/voice-profiles/save",
                json=dict(
                    id=profile["id"],
                    expected_revision=profile["revision"],
                    label="Narrator",
                    voice="am_echo",
                ),
            )
            assert response.status_code == 201, response.text
            changed = response.json()
            assert (
                changed["id"] == profile["id"]
                and changed["revision"] != profile["revision"]
            )
            recipe = manager.saved_profile_store().get(profile["id"])["recipe"]
            assert recipe["native_rate"] == 1.15 and recipe["title_pause_after"] == 0.9
            assert (
                recipe["config"]["pronunciation_replacements"]
                == old["recipe"]["config"]["pronunciation_replacements"]
            )
            assert recipe["reference"]["audio"]["basename"] == "second.wav"
            assert (
                manager.saved_profile_store().get(profile["id"], profile["revision"])[
                    "recipe"
                ]
                == old["recipe"]
            )
            stale = client.post(
                "/api/library/voice-profiles/save",
                json=dict(
                    id=profile["id"],
                    expected_revision=profile["revision"],
                    label="Stale",
                    voice="af_alloy",
                ),
            )
            assert stale.status_code == 409
            manager.max_active_jobs = 1
            assert finished(manager, queued["id"])["state"] == "ready"
            new = manager.prepare_saved(["music:001000"], profile["id"])[0]
            assert new["id"] != queued["id"] and new["variant"] != queued["variant"]
            assert finished(manager, new["id"])["state"] == "ready"
            assert calls == [("af_alloy", 1.15), ("am_echo", 1.15)]
            records = library.snapshot()["lectures"]["music:001000"]["recordings"]
            assert len(records) == 2 and {r["generator"]["voice"] for r in records} == {
                "af_alloy",
                "am_echo",
            }
    finally:
        manager.close()
