"""Private, immutable microphone references for colocated local-ai speech services."""

from __future__ import annotations

import base64
import binascii
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
from urllib.parse import urlparse
from uuid import uuid4
import wave

from .core import canonical, file_digest

SCHEMA = "ailectures-voice-reference-v1"
PROMPT = (
    "On a quiet morning, I opened the window and listened to the world outside. "
    "A bird called from a nearby tree, and a gentle breeze moved through the leaves. "
    "There was no need to hurry. I took a breath, gathered my thoughts, and began "
    "to tell a story, speaking clearly and at a comfortable pace."
)
MAX_BYTES = 4 * 1024**2
MIN_SECONDS, MAX_SECONDS = 3, 45
VOICE_ID = re.compile(r"recorded-[a-f0-9]{32}")
FORMATS = {"audio/webm": "matroska", "audio/ogg": "ogg", "audio/mp4": "mov",
           "audio/wav": "wav", "audio/x-wav": "wav", "audio/mpeg": "mp3"}


def reference_directory():
    configured = os.environ.get("DKVIS_TTS_REFERENCE_DIR")
    return Path(configured).expanduser() if configured else Path.home() / "code/local-ai/services/tts/voice-references"


def uses_local_references(backend):
    return bool(
        backend.get("available")
        and backend.get("model") in {"breeze-tts2", "fish-s2-pro"}
        and urlparse(backend["endpoint"]).hostname in {"localhost", "127.0.0.1", "::1"}
    )


def supports_recording(backend):
    directory = reference_directory()
    return bool(uses_local_references(backend) and directory.is_dir()
                and os.access(directory, os.W_OK | os.X_OK) and shutil.which("ffmpeg"))


def recording_capability(backend):
    return dict(available=supports_recording(backend), prompt=PROMPT,
                min_seconds=MIN_SECONDS, max_seconds=MAX_SECONDS, max_bytes=MAX_BYTES)


def recorded_references():
    directory = reference_directory()
    records = []
    try:
        manifests = list(directory.glob("recorded-*.reference.json"))
    except OSError:
        return records
    for path in manifests:
        voice = path.name.removesuffix(".reference.json")
        if not VOICE_ID.fullmatch(voice) or path.is_symlink():
            continue
        try:
            record = json.loads(path.read_text(encoding="utf-8"))
            if record["schema"] != SCHEMA or record["voice"] != voice:
                continue
            if not isinstance(record["label"], str) or not 1 <= len(record["label"]) <= 80:
                continue
            reference = record["reference"]
            if any(reference[kind]["basename"] != voice + suffix for kind, suffix in (("audio", ".wav"), ("transcript", ".txt"))):
                continue
            if any(not (directory / (voice + suffix)).is_file()
                   or (directory / (voice + suffix)).is_symlink() for suffix in (".wav", ".txt")):
                continue
            records.append(record)
        except (OSError, ValueError, KeyError, TypeError):
            continue
    return records


def save_recording(payload):
    label, transcript = payload.get("label"), payload.get("transcript")
    if not isinstance(label, str) or not 1 <= len(label.strip()) <= 80:
        raise ValueError("Reference name must contain 1–80 characters")
    if not isinstance(transcript, str) or not 20 <= len(transcript.strip()) <= 4000:
        raise ValueError("Supply the exact spoken prompt (20–4000 characters)")
    encoded = payload.get("audio_base64")
    if not isinstance(encoded, str) or not 1 <= len(encoded) <= (MAX_BYTES + 2) // 3 * 4:
        raise ValueError("Recording must be at most 4 MiB")
    try:
        audio = base64.b64decode(encoded, validate=True)
    except (ValueError, binascii.Error):
        raise ValueError("Invalid recording data") from None
    if not audio or len(audio) > MAX_BYTES:
        raise ValueError("Recording must be at most 4 MiB")
    media_type = payload.get("media_type")
    media_type = media_type.split(";", 1)[0].strip().lower() if isinstance(media_type, str) else ""
    if media_type not in FORMATS:
        raise ValueError("Use a WebM, Ogg, MP4, WAV, or MP3 audio recording")
    directory = reference_directory()
    voice = "recorded-" + uuid4().hex
    created = []
    try:
        with tempfile.TemporaryDirectory(prefix=".ailectures-reference-", dir=directory) as temp:
            temp = Path(temp)
            wav = temp / (voice + ".wav")
            try:
                result = subprocess.run([
                    "ffmpeg", "-nostdin", "-hide_banner", "-loglevel", "error",
                    "-protocol_whitelist", "pipe", "-f", FORMATS[media_type], "-i", "pipe:0",
                    "-map", "0:a:0", "-vn", "-ac", "1", "-ar", "24000",
                    "-c:a", "pcm_s16le", "-t", str(MAX_SECONDS + 1), "-f", "wav", str(wav),
                ], input=audio, capture_output=True, timeout=30)
            except subprocess.TimeoutExpired:
                raise ValueError("Recording could not be decoded in time; try a shorter take") from None
            if result.returncode:
                # Decoder output can contain private upload details; keep it off responses/logs.
                raise ValueError("Could not decode this recording; record another take or upload a supported audio file")
            with wave.open(str(wav), "rb") as stream:
                seconds = stream.getnframes() / stream.getframerate()
            if not MIN_SECONDS <= seconds <= MAX_SECONDS:
                raise ValueError(f"Read a prompt lasting {MIN_SECONDS}–{MAX_SECONDS} seconds; this take is {seconds:.1f} seconds")
            text = temp / (voice + ".txt")
            text.write_text(transcript.strip() + "\n", encoding="utf-8")
            record = dict(schema=SCHEMA, voice=voice, label=label.strip(), seconds=seconds,
                          reference=dict(source="local-ai/services/tts/voice-references", basis="user-recorded prompt",
                                         audio=dict(basename=wav.name, sha256=file_digest(wav), seconds=seconds),
                                         transcript=dict(basename=text.name, sha256=file_digest(text))))
            manifest = temp / (voice + ".reference.json")
            manifest.write_bytes(canonical(record))
            # Publish text before audio: the service discovers WAVs dynamically.
            # Exclusive links never replace an existing reference, even a symlink.
            for source in (text, wav, manifest):
                source.chmod(0o600)
                destination = directory / source.name
                os.link(source, destination)
                created.append(destination)
            return record
    except OSError:
        for path in created:
            path.unlink(missing_ok=True)
        raise ValueError("Could not save the reference in the server's voice directory") from None
