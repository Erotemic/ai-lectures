import json

from starlette.testclient import TestClient

from ailectures.library import Library
from ailectures.production import GenerationManager
from ailectures.web import create_app


def test_profiles_voice_registration_and_original_reader_share_choices(
    tmp_path, monkeypatch
):
    from dkvis.presentation.audio_library import AudioLectureHub

    monkeypatch.setattr("dkvis.presentation.tts.load_env", lambda: None)
    monkeypatch.delenv("DKVIS_AUDIO_TTS_PROFILE", raising=False)
    monkeypatch.delenv("DKVIS_TTS_PROFILE", raising=False)

    config = tmp_path / "tts.toml"
    config.write_text(
        'profile="second"\n[profiles.first]\nendpoint="http://127.0.0.1:1/v1/audio/speech"\nmodel="kokoro"\nvoice="af_alloy"\nresponse_format="mp3"\n[profiles.second]\nendpoint="http://127.0.0.1:1/v1/audio/speech"\nmodel="breeze-tts2"\nvoice="af_alloy"\nresponse_format="wav"\n[profiles.unfinished]\nvoice="af_alloy"\n'
    )
    repo = tmp_path / "repo"
    (repo / "audio-cache").mkdir(parents=True)
    (repo / "audio-cache" / "registered-voices.json").write_text(
        json.dumps(
            {
                "voices": [
                    {
                        "profile": "first",
                        "voice": "af_heart",
                        "label": "Previous narrator",
                    }
                ]
            }
        )
    )
    root = tmp_path / "library"
    manager = GenerationManager(Library(root), config=config, repository=repo)
    try:
        profiles = manager.profiles()
        assert profiles["default_profile"] == "second"
        assert {row["id"] for row in profiles["profiles"]} == {"first", "second"}
        assert profiles["errors"]  # One unfinished profile does not hide good ones.
        assert "af_heart" in manager.voices("first")["voices"]
        monkeypatch.setattr(
            "dkvis.presentation.tts.remote_voices",
            lambda *args: ["af_alloy", "am_echo"],
        )
        assert "am_echo" in manager.voices("first", probe=True)["voices"]
        monkeypatch.setattr("dkvis.presentation.tts.remote_voices", lambda *args: [])
        assert "am_echo" in manager.voices("first", probe=True)["voices"]
        app = create_app(root, generation_manager=manager)
        with TestClient(app) as client:
            result = client.post(
                "/api/library/production/voices/register",
                json={"profile": "first", "voice": "am_adam", "label": "New narrator"},
            )
            assert result.status_code == 201
            assert (
                "am_adam"
                in client.get("/api/library/production/voices?profile=first").json()[
                    "voices"
                ]
            )
            assert (
                "am_adam"
                not in client.get(
                    "/api/library/production/voices?profile=second"
                ).json()["voices"]
            )
            assert (
                client.post(
                    "/api/library/production/voices/register",
                    json={"profile": "unknown", "voice": "af_alloy"},
                ).status_code
                == 400
            )
        sources = tmp_path / "sources"
        sources.mkdir()
        (sources / "001000-lecture.md").write_text(
            "# Lecture\n<!-- BEGIN SPOKEN LECTURE -->\nAn explanation.\n<!-- END SPOKEN LECTURE -->"
        )
        hub = AudioLectureHub(
            sources=sources,
            cache=tmp_path / "old-cache",
            config=config,
            profile="first",
            voice_store=manager.voice_store(),
        )
        try:
            assert any(
                row["voice"] == "am_adam" for row in hub.registered_voices("first")
            )
            hub.register_voice("second", "af_heart", "Another narrator")
            assert "af_heart" in manager.voices("second")["voices"]
        finally:
            hub.close()
    finally:
        manager.close()


def test_native_voice_catalog_accepts_service_records(tmp_path):
    from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
    import threading
    from dkvis.presentation.tts import remote_voices

    class Handler(BaseHTTPRequestHandler):
        def log_message(self, *args):
            pass

        def do_GET(self):
            data = json.dumps(
                {"voices": [{"id": "af_heart"}, {"name": "am_echo"}]}
            ).encode()
            self.send_response(200)
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)

    server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        assert remote_voices(
            f"http://127.0.0.1:{server.server_port}/v1/audio/speech", "af_alloy"
        ) == ["af_alloy", "af_heart", "am_echo"]
    finally:
        server.shutdown()
        thread.join()
        server.server_close()
