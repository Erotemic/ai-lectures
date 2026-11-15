"""Optional legacy production adapters, imported only when generation is requested."""

from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path
import shutil
import socket
import time
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor
import subprocess
import threading
from uuid import uuid4

from .core import digest, file_digest, write_json, finite
from .packs import export_release, recording_id


def audio_duration(path):
    result = subprocess.run(
        [
            "ffprobe",
            "-v",
            "error",
            "-show_entries",
            "format=duration",
            "-of",
            "default=noprint_wrappers=1:nokey=1",
            str(path),
        ],
        capture_output=True,
        text=True,
        check=True,
        timeout=20,
    )
    value = float(result.stdout)
    return finite(value, 0.001)


def recording_from_engine(
    engine, local_id, row, *, variant, label=None, voice=None, speed=1
):
    """Resolve exact legacy request keys and preserve speech pages and timings."""
    settings = engine.settings(voice, speed)
    detail = engine.detail(local_id)
    if detail["transcript_sha256"] != row["spoken_sha256"]:
        raise ValueError("Legacy audio was generated from a different transcript")
    record = dict(
        variant=variant,
        label=label or variant,
        spoken_sha256=row["spoken_sha256"],
        recipe=digest(
            {
                "legacy_settings": engine._config_key(settings),
                "pagination": detail["pagination_version"],
                "page_chars": detail["page_chars"],
            }
        ),
        pages=detail["pages"],
        segments=[],
        complete=False,
        generator={
            "model": engine.model,
            "speech_policy": "paragraph80-v1" if engine.server_long_form else "legacy",
            "pagination": detail["pagination_version"],
            "page_chars": detail["page_chars"],
            "speech_speed": settings.speed,
        },
    )
    files = {}
    page_keys = []
    for index, text in enumerate(detail["pages"]):
        target, _, key = engine._target_from_text(local_id, index, settings, text)
        page_keys.append(key)
        if not engine._ready(target, key):
            continue
        sha = file_digest(target)
        path = (
            f'artifacts/{variant}/{row["id"].replace(":", "-")}/{index:04d}-{sha}.mp3'
        )
        segment = dict(
            index=index,
            path=path,
            sha256=sha,
            duration=audio_duration(target),
            media_type="audio/mpeg",
        )
        timing = target.with_name(target.name + ".timings.json")
        if timing.exists():
            segment["timings"] = json.loads(timing.read_text())
        record["segments"].append(segment)
        files[path] = target
    record["recipe"] = digest({"request_keys": page_keys})
    record["complete"] = len(record["segments"]) == len(record["pages"])
    record["id"] = recording_id(record)
    return record, files


class GenerationManager:
    def __init__(
        self,
        library,
        *,
        config=None,
        repository=None,
        profile=None,
        endpoint=None,
        engine_factory=None,
    ):
        self.library = library
        self.config = config
        self.repository = Path(repository) if repository else None
        self.default_profile = profile
        self.endpoint = endpoint
        self.engine_factory = engine_factory
        self._jobs = {}
        self._lock = threading.RLock()
        self._health = {}

    def profiles(self, *, probe=False):
        try:
            if self.config is None and self.repository is None:
                return {"profiles": [], "tools_available": False}
            from dkvis.presentation.tts import load_profiles, resolve_profile

            document = load_profiles(self.config)
            rows = []
            for key in document.get("profiles", {}):
                profile = resolve_profile(document, key)
                rows.append(
                    {
                        "id": key,
                        "label": profile.get("display_name", key),
                        "voice": profile["voice"],
                        "model": profile["model"],
                        "_endpoint": self.endpoint or profile["endpoint"],
                    }
                )
            if probe:

                def check(endpoint):
                    cached = self._health.get(endpoint)
                    if cached and time.monotonic() - cached[0] < 10:
                        return cached[1]
                    parsed = urlparse(endpoint)
                    try:
                        with socket.create_connection(
                            (
                                parsed.hostname,
                                parsed.port
                                or (443 if parsed.scheme == "https" else 80),
                            ),
                            timeout=1.5,
                        ):
                            reachable = True
                    except (OSError, ValueError):
                        reachable = False
                    self._health[endpoint] = (time.monotonic(), reachable)
                    return reachable

                endpoints = list({r["_endpoint"] for r in rows})
                with ThreadPoolExecutor(
                    max_workers=max(1, min(8, len(endpoints)))
                ) as pool:
                    health = dict(zip(endpoints, pool.map(check, endpoints)))
                for row in rows:
                    row["reachable"] = health[row["_endpoint"]]
            for row in rows:
                row.pop("_endpoint", None)
            return {
                "profiles": rows,
                "tools_available": bool(
                    shutil.which("ffmpeg") and shutil.which("ffprobe")
                ),
                "default_profile": self.default_profile
                or (rows[0]["id"] if rows else None),
            }
        except (ImportError, OSError, ValueError, KeyError) as exc:
            return {"profiles": [], "tools_available": False, "error": str(exc)}

    def prepare(self, lecture_id, profile, *, voice=None, speed=1):
        row = self.library.snapshot()["lectures"][lecture_id]
        if row.get("kind") != "audio":
            raise ValueError("Use the existing presentation renderer for this lecture")
        if not self.profiles()["tools_available"]:
            raise ValueError(
                "Generation requires the production installation and FFmpeg tools"
            )
        from dkvis.presentation.audio_library import AudioLectureLibrary
        from dkvis.presentation.tts import load_profiles, resolve_profile

        document = load_profiles(self.config)
        config = resolve_profile(document, profile, {"voice": voice} if voice else None)
        job_id = digest(
            {
                "lecture": lecture_id,
                "revision": row["revision"],
                "profile": profile,
                "settings": {k: v for k, v in config.items() if k != "reference"},
                "reference": document["profiles"][profile].get("reference"),
                "speed": speed,
                "endpoint_override": self.endpoint,
            }
        )
        with self._lock:
            if job_id in self._jobs:
                job = self._jobs[job_id]
                job["engine"].prepare_lecture("000000", job["settings"])
                return self.status(job_id)
            directory = self.library.store.root / "build-cache" / "generation" / job_id
            sources = directory / "source"
            sources.mkdir(parents=True, exist_ok=True)
            (sources / "000000-lecture.md").write_text(
                "# Lecture\n<!-- BEGIN SPOKEN LECTURE -->\n"
                + row["transcript"]
                + "\n<!-- END SPOKEN LECTURE -->\n"
            )
            factory = self.engine_factory or AudioLectureLibrary
            engine = factory(
                sources=sources,
                cache=directory / "audio",
                document=document,
                profile=profile,
                voice=voice,
                endpoint=self.endpoint,
            )
            settings = engine.settings(voice, speed)
            variant = (
                "narrator-"
                + digest(
                    {
                        "profile": profile,
                        "voice": settings.voice,
                        "speed": settings.speed,
                        "model": settings.model,
                        "voice_revision": config.get("voice_revision"),
                        "reference": document["profiles"][profile].get("reference"),
                    }
                )[:16]
            )
            job = dict(
                engine=engine,
                settings=settings,
                row=deepcopy(row),
                variant=variant,
                label=f"{settings.voice} ({settings.model})",
                published=None,
            )
            self._jobs[job_id] = job
            write_json(
                directory / "batch.json",
                {
                    "lecture_id": lecture_id,
                    "revision": row["revision"],
                    "profile": profile,
                    "voice": settings.voice,
                    "speed": speed,
                },
            )
            engine.prepare_lecture("000000", settings)
            return self.status(job_id)

    def status(self, job_id):
        with self._lock:
            job = self._jobs[job_id]
            engine, settings = job["engine"], job["settings"]
            inventory = engine.inventory("000000", settings)
            result = dict(
                id=job_id,
                lecture_id=job["row"]["id"],
                variant=job["variant"],
                inventory=inventory,
                published=job["published"],
            )
            if inventory["ready"] == inventory["total"] and not job["published"]:
                result["published"] = job["published"] = self.publish(job)
            return result

    def publish(self, job):
        row = job["row"]
        engine, settings = job["engine"], job["settings"]
        rec, files = recording_from_engine(
            engine,
            "000000",
            row,
            variant=job["variant"],
            label=job["label"],
            voice=settings.voice,
            speed=settings.speed,
        )
        pack_id = "audio-" + digest(row["id"])[:24]
        previous = next(
            (r for r in self.library.store.active() if r["pack_id"] == pack_id), None
        )
        recordings = [(row["id"], rec, files)]
        if previous:
            old = json.loads(previous["catalog"])["lectures"].get(row["id"])
            if old and old["spoken_sha256"] == row["spoken_sha256"]:
                for existing in old["recordings"]:
                    if existing["variant"] != rec["variant"]:
                        recordings.append(
                            (
                                row["id"],
                                existing,
                                {
                                    s["path"]: Path(previous["directory"]) / s["path"]
                                    for s in existing["segments"]
                                },
                            )
                        )
        pack = dict(
            id=pack_id,
            title=row["title"] + " · audio",
            lectures={row["id"]: row},
            courses={},
            relationships=[],
        )
        directory = self.library.store.root / "exports" / (pack_id + "-" + uuid4().hex)
        manifest = export_release(
            pack,
            directory,
            parent=previous["release"] if previous else None,
            media=recordings,
            kind="media",
        )
        self.library.store.install(directory)
        return manifest["release"]

    def cancel(self, job_id):
        job = self._jobs[job_id]
        return job["engine"].cancel("000000", job["settings"])

    def close(self):
        for job in self._jobs.values():
            job["engine"].close()
