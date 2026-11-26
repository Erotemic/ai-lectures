"""Find unusable audio blocks in the library's current recordings."""

from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
import math
import re
import shutil
import subprocess

from .core import contained, digest, file_digest


SILENCE_DBFS = -55
REPAIR_CACHE_PREFIX = "audio-repair-"


def signal_problem(path):
    """Decode the entire first audio stream and check its aggregate RMS."""
    try:
        result = subprocess.run(
            ["ffmpeg", "-nostdin", "-hide_banner", "-nostats", "-v", "info",
             "-xerror", "-threads", "1", "-filter_threads", "1", "-i", str(path),
             "-map", "0:a:0", "-af",
             "astats=measure_perchannel=none:measure_overall=RMS_level+Number_of_samples",
             "-f", "null", "-"],
            capture_output=True, text=True, errors="replace", timeout=60,
        )
    except subprocess.TimeoutExpired:
        return {"issue": "decoder_timeout"}
    if result.returncode:
        return {"issue": "decode_error", "detail": result.stderr.splitlines()[-1][:250] if result.stderr else "FFmpeg failed"}
    samples = re.search(r"Number of samples: (\d+)", result.stderr)
    rms = re.search(r"RMS level dB: (\S+)", result.stderr)
    if not samples or not int(samples[1]) or not rms:
        return {"issue": "no_audio_samples"}
    level = float(rms[1])
    if level == float("-inf"):
        return {"issue": "silent", "rms_dbfs": None}
    if not math.isfinite(level):
        return {"issue": "invalid_signal"}
    if level <= SILENCE_DBFS:
        return {"issue": "near_silent", "rms_dbfs": round(level, 2)}
    return None


def check_block(file_key):
    directory, relative, expected = file_key
    try:
        path = contained(directory, relative)
        if file_digest(path) != expected:
            return {"issue": "checksum_mismatch"}
    except FileNotFoundError:
        return {"issue": "missing"}
    except (OSError, ValueError) as exc:
        return {"issue": "unreadable", "detail": str(exc)}
    return signal_problem(path)


def audit_audio(library, lectures=(), *, workers=4, report_progress=None):
    if not shutil.which("ffmpeg"):
        raise ValueError("Audio audit requires FFmpeg on PATH")
    if not 1 <= workers <= 16:
        raise ValueError("Set --workers between 1 and 16")
    snapshot = library.snapshot(copy=False)
    rows = snapshot["lectures"]
    keys = sorted({snapshot["aliases"].get(key, key) for key in lectures}) if lectures else sorted(rows)
    releases = {pack["release"]: pack["id"] for pack in snapshot["packs"] if not pack.get("source")}
    blocks = defaultdict(list)
    for key in keys:
        for recording in rows[key]["recordings"]:
            release = recording["_release"]
            directory = library.store.packs / releases[release] / release
            generator = recording.get("generator", {})
            for segment in recording["segments"]:
                relative = segment["path"]
                blocks[directory, relative, segment["sha256"]].append({
                    "lecture": key, "recording": recording["id"], "release": release,
                    "label": recording["label"], "profile": generator.get("profile"),
                    "profile_revision": generator.get("profile_revision"),
                    "block": segment["index"], "path": str((directory / relative).relative_to(library.store.root)),
                })

    total = len(blocks)
    if report_progress is not None:
        report_progress(0, total)
    findings = []
    with ThreadPoolExecutor(max_workers=workers) as executor:
        for checked, (owners, problem) in enumerate(zip(blocks.values(), executor.map(check_block, blocks)), 1):
            if problem:
                findings.extend({**owner, **problem} for owner in owners)
            if report_progress is not None:
                report_progress(checked, total)
    return {"files_checked": total, "threshold_dbfs": SILENCE_DBFS, "findings": findings}


def queue_repairs(manager, findings):
    """Regenerate each affected reader-produced recording from its saved recipe."""
    snapshot = manager.library.snapshot(copy=False)
    releases = {pack["release"]: pack for pack in snapshot["packs"]}
    queued, skipped = [], []
    unique = {(item["lecture"], item["recording"], item["release"]): item for item in findings}
    for (lecture, recording_id, release), item in unique.items():
        report = {"lecture": lecture, "recording": recording_id, "release": release}
        row = snapshot["lectures"].get(lecture, {})
        recording = next((rec for rec in row.get("recordings", ()) if rec["id"] == recording_id and rec["_release"] == release), None)
        pack = releases.get(release, {})
        try:
            if not item["profile_revision"] or not item["profile"]:
                raise ValueError("No saved rendering recipe for this recording")
            if recording is None:
                raise ValueError("The recording changed during the audit")
            if pack.get("kind") != "media" or pack["id"] != "audio-" + digest(lecture)[:24]:
                raise ValueError("This recording is managed by an installed pack")
            job_id = manager.queue_saved_repair(lecture, recording, snapshot=snapshot)
            queued.append({**report, "job": job_id})
        except (KeyError, ValueError) as exc:
            skipped.append({**report, "reason": str(exc)})
    return {"queued": queued, "skipped": skipped}
