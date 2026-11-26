"""Decode real audio bytes and exercise regeneration through the durable queue."""

from array import array
import math
import shutil
import wave

import pytest

from ailectures.audio_audit import audit_audio, queue_repairs, signal_problem
from test_production_recovery import finished, manager_for, setup_library
from test_saved_voice_profiles import catalog_profile


pytestmark = pytest.mark.skipif(not shutil.which("ffmpeg"), reason="Audio audit needs FFmpeg")


def write_tone(path, amplitude):
    with wave.open(str(path), "wb") as stream:
        stream.setparams((1, 2, 8000, 0, "NONE", "not compressed"))
        samples = array("h", (round(amplitude * math.sin(i * math.tau * 440 / 8000)) for i in range(8000)))
        stream.writeframes(samples.tobytes())


def test_signal_check_distinguishes_audible_quiet_and_invalid_files(tmp_path):
    audible, quiet, corrupt = [tmp_path / f"{name}.wav" for name in ("audible", "quiet", "corrupt")]
    write_tone(audible, 5000)
    write_tone(quiet, 12)
    corrupt.write_bytes(b"RIFF" * 1024)

    assert signal_problem(audible) is None
    assert signal_problem(quiet)["issue"] == "near_silent"
    assert signal_problem(corrupt)["issue"] == "decode_error"


def test_repair_bypasses_silent_cache_and_publishes_only_audible_audio(tmp_path, monkeypatch):
    library, _, _, silent, config = setup_library(tmp_path, monkeypatch)
    audible = tmp_path / "audible.wav"
    write_tone(audible, 5000)
    source = silent

    def sender(text, settings, dest):
        shutil.copyfile(source, dest)

    manager = manager_for(library, config, sender)
    lecture = "music:001000"
    try:
        _, profile = catalog_profile(manager)
        original_job = manager.prepare_saved([lecture], profile["id"])[0]
        original = finished(manager, original_job["id"])["published"]
        scan = audit_audio(library, [lecture])
        assert scan["files_checked"] == 1
        finding, = scan["findings"]
        assert finding["issue"] == "silent" and finding["block"] == 0
        assert finding["release"] == original

        repair, = queue_repairs(manager, [finding])["queued"]
        assert repair["job"] != original_job["id"]
        assert queue_repairs(manager, [finding])["skipped"]
        assert finished(manager, repair["job"])["state"] == "failed"
        assert library.snapshot()["lectures"][lecture]["recordings"][0]["_release"] == original

        source = audible
        retry, = queue_repairs(manager, [finding])["queued"]
        replacement = finished(manager, retry["job"])["published"]
        assert replacement and replacement != original
        assert not audit_audio(library, [lecture])["findings"]
        original_file, _ = library.store.media_file(original, finding["recording"], 0)
        assert signal_problem(original_file)["issue"] == "silent"
    finally:
        manager.close()
