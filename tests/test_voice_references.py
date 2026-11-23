"""Private recording uploads become reusable, immutable local-ai reference pairs."""

import base64
from io import BytesIO
import math
from pathlib import Path
import shutil
import struct
import wave

import pytest
from starlette.testclient import TestClient

from ailectures.production import GenerationManager
from ailectures.voice_references import (
    MAX_BYTES, PROMPT, recorded_references, reference_directory, save_recording,
    supports_recording,
)
from ailectures.web import create_app
from test_production_recovery import setup_library, manager_for, finished


def recording(seconds=4):
    buffer = BytesIO()
    with wave.open(buffer, "wb") as stream:
        stream.setnchannels(2)
        stream.setsampwidth(2)
        stream.setframerate(8000)
        stream.writeframes(b"".join(struct.pack("<hh", int(1200 * math.sin(i / 9)), int(1000 * math.sin(i / 9))) for i in range(int(8000 * seconds))))
    return dict(label="Example reference", transcript=PROMPT, media_type="audio/wav",
                audio_base64=base64.b64encode(buffer.getvalue()).decode("ascii"))


@pytest.fixture
def references(tmp_path, monkeypatch):
    if not shutil.which("ffmpeg"):
        pytest.skip("Reference preparation needs ffmpeg")
    directory = tmp_path / "voice-references"
    directory.mkdir()
    monkeypatch.setenv("DKVIS_TTS_REFERENCE_DIR", str(directory))
    return directory


def test_capability_requires_supported_colocated_backend_and_existing_directory(references, monkeypatch):
    backend = dict(available=True, model="breeze-tts2", endpoint="http://127.0.0.1:8821/v1/audio/speech")
    assert supports_recording(backend)
    assert not supports_recording(dict(backend, model="kokoro"))
    assert not supports_recording(dict(backend, endpoint="https://remote.invalid/v1/audio/speech"))
    assert not supports_recording(dict(backend, available=False))
    monkeypatch.setenv("DKVIS_TTS_REFERENCE_DIR", str(references / "missing"))
    assert not supports_recording(backend)
    assert not (references / "missing").exists()
    monkeypatch.delenv("DKVIS_TTS_REFERENCE_DIR")
    monkeypatch.setattr(Path, "home", lambda: references.parent)
    assert reference_directory() == references.parent / "code/local-ai/services/tts/voice-references"


def test_save_normalizes_audio_keeps_matching_prompt_and_never_replaces_a_take(references):
    payload = recording()
    first = save_recording(payload)
    files = {p.name: p.read_bytes() for p in references.iterdir()}
    second = save_recording(payload)
    assert first["voice"] != second["voice"]
    assert all((references / name).read_bytes() == data for name, data in files.items())
    wav = references / (first["voice"] + ".wav")
    with wave.open(str(wav)) as stream:
        assert (stream.getframerate(), stream.getnchannels(), stream.getsampwidth()) == (24000, 1, 2)
        assert stream.getnframes() / stream.getframerate() == pytest.approx(4)
    assert wav.with_suffix(".txt").read_text() == PROMPT + "\n"
    assert wav.stat().st_mode & 0o777 == 0o600
    assert len(recorded_references()) == 2
    wav.unlink()
    assert [row["voice"] for row in recorded_references()] == [second["voice"]]
    assert not list(references.glob(".ailectures-*"))


@pytest.mark.parametrize("patch", [
    {"label": ""}, {"transcript": "short"}, {"audio_base64": "not base64!"},
    {"audio_base64": base64.b64encode(b"not audio").decode()},
    {"media_type": "text/plain"}, {"audio_base64": "A" * (MAX_BYTES * 2)},
])
def test_invalid_uploads_publish_nothing(references, patch):
    with pytest.raises(ValueError):
        save_recording(dict(recording(), **patch))
    assert not list(references.iterdir())


@pytest.mark.parametrize("seconds", [1, 46])
def test_duration_bounds_do_not_silently_trim_or_accept_short_takes(references, seconds):
    with pytest.raises(ValueError, match="3–45 seconds"):
        save_recording(recording(seconds))
    assert not list(references.iterdir())


def test_reference_publication_failure_preserves_existing_files(references, monkeypatch):
    import ailectures.voice_references as module
    voice = "recorded-" + "a" * 32
    monkeypatch.setattr(module, "uuid4", lambda: type("ID", (), {"hex": "a" * 32})())
    destination = references / (voice + ".wav")
    destination.write_bytes(b"existing reference")
    with pytest.raises(ValueError, match="Could not save"):
        save_recording(recording())
    assert destination.read_bytes() == b"existing reference"
    assert list(references.iterdir()) == [destination]


def test_recorded_voice_is_selectable_and_generation_pins_its_recipe(references, tmp_path, monkeypatch):
    library, pack, manifest, audio, config = setup_library(tmp_path, monkeypatch)
    config.write_text(config.read_text().replace('model="kokoro"', 'model="breeze-tts2"'))
    monkeypatch.setattr("dkvis.presentation.tts.remote_voices", lambda *_: [p.stem for p in references.glob("*.wav")])
    calls = []
    def sender(text, settings, destination):
        calls.append(settings.voice)
        shutil.copyfile(audio, destination)
    manager = manager_for(library, config, sender)
    try:
        backend = manager.profile_catalog()["backends"][0]
        assert backend["reference_recording"]["available"]
        with TestClient(create_app(library.store.root, tts_config=config, generation_manager=manager)) as client:
            endpoint = f"/api/library/voice-profiles/backends/{backend['id']}/references"
            assert client.post(endpoint, json=recording(), headers={"origin": "https://other.invalid"}).status_code == 403
            assert not list(references.iterdir())
            response = client.post(endpoint, json=recording())
            assert response.status_code == 201, response.text
            saved = response.json()
            assert saved["backend_visible"] and "audio_base64" not in saved
            voices = client.get(endpoint.removesuffix("references") + "voices").json()["voices"]
            assert next(v for v in voices if v["voice"] == saved["voice"])["reference"]
            profile = client.post("/api/library/voice-profiles/save", json=dict(
                backend_id=backend["id"], voice=saved["voice"], label="Recorded example",
            )).json()
            recipe = manager.saved_profile_store().get(profile["id"])["recipe"]
            assert recipe["fixed_reference"] and recipe["config"]["voice_revision"]
            assert recipe["reference"]["audio"]["basename"] == saved["voice"] + ".wav"
            job = manager.prepare_saved(["music:001000"], profile["id"])[0]
            assert finished(manager, job["id"])["state"] == "ready"
            assert calls and set(calls) == {saved["voice"]}
            # Saving a new take creates a different identity; queued/old recipes stay pinned.
            other = client.post(endpoint, json=recording()).json()
            assert other["voice"] != saved["voice"]
            assert manager.saved_profile_store().get(profile["id"])["recipe"] == recipe
            assert client.post(endpoint, content=b"x" * (6 * 1024**2 + 1)).status_code == 413
            assert client.post(endpoint, json=[]).status_code == 400
            assert client.post(endpoint, content=b"not json").status_code == 400
    finally:
        manager.close()


def test_playback_only_and_unsupported_backends_cannot_accept_recordings(references, tmp_path, monkeypatch):
    library, pack, manifest, audio, config = setup_library(tmp_path, monkeypatch)
    manager = GenerationManager(library, config=config)
    try:
        backend = manager.profile_catalog()["backends"][0]
        endpoint = f"/api/library/voice-profiles/backends/{backend['id']}/references"
        assert not backend["reference_recording"]["available"]
        with TestClient(create_app(library.store.root, generation_manager=manager)) as client:
            assert client.post(endpoint, json=recording()).status_code == 400
        with TestClient(create_app(library.store.root, generation_manager=manager, playback_only=True)) as client:
            assert client.post(endpoint, json=recording()).status_code == 403
        assert not list(references.iterdir())
    finally:
        manager.close()
