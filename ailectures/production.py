"""Optional legacy production adapters, imported only when generation is requested."""

from __future__ import annotations

from copy import deepcopy
import json
import os
import re
from pathlib import Path
import shutil
import socket
import sqlite3
import time
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor
import subprocess
import threading
from uuid import uuid4

from .core import digest, file_digest, write_json, finite
from .packs import export_release, recording_id
from .jobs import JobStore


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
        max_active_jobs=2,
        retry_delay=5,
        lease_seconds=60,
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
        self.jobs = JobStore(library.store.state)
        self.owner = uuid4().hex
        self.max_active_jobs = max_active_jobs
        self.retry_delay = retry_delay
        self.lease_seconds = lease_seconds
        self._closing = False
        self._heartbeat_stop = threading.Event()
        self._heartbeat_thread = None

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

    @staticmethod
    def _configuration(document, profile, voice, endpoint):
        from dkvis.presentation.tts import resolve_profile

        config = resolve_profile(document, profile, {"voice": voice} if voice else None)
        relevant = {k: v for k, v in config.items() if k != "reference"}
        return config, {
            "settings": relevant,
            "reference": document["profiles"][profile].get("reference"),
            "endpoint_override": endpoint,
            "environment": {
                key: value
                for key, value in os.environ.items()
                if key.startswith("DKVIS_AUDIO_") and key != "DKVIS_AUDIO_TTS_CONFIG"
            },
        }

    def prepare(self, lecture_id, profile, *, voice=None, speed=1):
        return self.prepare_many([lecture_id], profile, voice=voice, speed=speed)[0]

    def prepare_many(self, lecture_ids, profile, *, voice=None, speed=1):
        finite(speed, 0.5)
        if speed > 2 or (
            voice is not None and not re.fullmatch(r"[A-Za-z0-9_.+\-]{1,80}", voice)
        ):
            raise ValueError("Invalid speech speed or voice")
        if not self.profiles()["tools_available"]:
            raise ValueError(
                "Generation requires the production installation and FFmpeg tools"
            )
        from dkvis.presentation.tts import load_profiles

        document = load_profiles(self.config)
        config, configuration = self._configuration(
            document, profile, voice, self.endpoint
        )
        snapshot = self.library.snapshot()
        requests = []
        for lecture_id in dict.fromkeys(lecture_ids):
            row = deepcopy(snapshot["lectures"][lecture_id])
            if row.get("kind") != "audio":
                raise ValueError(
                    "Use the existing presentation renderer for this lecture"
                )
            row.pop("origin", None)
            row["recordings"] = []
            job_id = digest(
                {
                    "lecture": lecture_id,
                    "revision": row["revision"],
                    "configuration": configuration,
                    "speed": speed,
                }
            )
            specification = {
                "row": row,
                "profile": profile,
                "voice": voice,
                "speed": speed,
                "configuration": configuration,
            }
            requests.append((job_id, specification))
        self.jobs.enqueue(requests)
        self.tick()
        return [self._public(self.jobs.get(job_id)) for job_id, _ in requests]

    def _heartbeat(self):
        while not self._heartbeat_stop.wait(max(0.05, self.lease_seconds / 3)):
            try:
                self.jobs.heartbeat(self.owner, self.lease_seconds)
            except (OSError, sqlite3.Error):
                pass

    def _open(self, record):
        from dkvis.presentation.audio_library import AudioLectureLibrary
        from dkvis.presentation.tts import load_profiles

        spec = record["specification"]
        document = load_profiles(self.config)
        config, configuration = self._configuration(
            document, spec["profile"], spec["voice"], self.endpoint
        )
        if configuration != spec["configuration"]:
            raise ValueError(
                "Configured speech settings changed; start a new preparation with the revised settings"
            )
        directory = (
            self.library.store.root / "build-cache" / "generation" / record["id"]
        )
        sources = directory / "source"
        sources.mkdir(parents=True, exist_ok=True)
        (sources / "000000-lecture.md").write_text(
            "# Lecture\n<!-- BEGIN SPOKEN LECTURE -->\n"
            + spec["row"]["transcript"]
            + "\n<!-- END SPOKEN LECTURE -->\n"
        )
        # Source revisions share request-addressed pages when speech inputs agree.
        cache = (
            self.library.store.root
            / "build-cache"
            / "speech"
            / digest({"lecture": spec["row"]["id"], "configuration": configuration})
        )
        cache.mkdir(parents=True, exist_ok=True)
        legacy_cache = directory / "audio"
        if legacy_cache.is_dir():
            for path in legacy_cache.iterdir():
                if path.is_file() and (
                    path.suffix == ".mp3" or path.name.endswith(".timings.json")
                ):
                    target = cache / path.name
                    if not target.exists():
                        shutil.copyfile(path, target)
        factory = self.engine_factory or AudioLectureLibrary
        engine = factory(
            sources=sources,
            cache=cache,
            document=document,
            profile=spec["profile"],
            voice=spec["voice"],
            endpoint=self.endpoint,
            workers=1,
        )
        settings = engine.settings(spec["voice"], spec["speed"])
        variant = (
            "narrator-"
            + digest(
                {
                    "profile": spec["profile"],
                    "voice": settings.voice,
                    "speed": settings.speed,
                    "model": settings.model,
                    "voice_revision": config.get("voice_revision"),
                    "reference": document["profiles"][spec["profile"]].get("reference"),
                }
            )[:16]
        )
        job = {
            "engine": engine,
            "settings": settings,
            "row": spec["row"],
            "variant": variant,
            "label": f"{settings.voice} ({settings.model})",
            "published": None,
        }
        write_json(
            directory / "batch.json",
            {
                "id": record["id"],
                "lecture_id": spec["row"]["id"],
                "revision": spec["row"]["revision"],
                "profile": spec["profile"],
                "voice": settings.voice,
                "speed": settings.speed,
            },
        )
        engine.prepare_lecture("000000", settings)
        return job

    @staticmethod
    def _public(record):
        spec = record["specification"]
        return {
            "id": record["id"],
            "lecture_id": spec["row"]["id"],
            "revision": spec["row"]["revision"],
            "title": spec["row"]["title"],
            "profile": spec["profile"],
            "state": record["state"],
            "attempts": record["attempts"],
            "retry_at": record["retry_at"],
            "error": record["error"],
            "published": record["published"],
            "inventory": record["inventory"]
            or {
                "ready": 0,
                "total": 0,
                "queue": [],
                "preparation": {"state": record["state"]},
            },
        }

    def list(self):
        return [self._public(record) for record in self.jobs.list()]

    def tick(self):
        with self._lock:
            if self._closing:
                return
            self.jobs.heartbeat(self.owner, self.lease_seconds)
            for job_id, job in list(self._jobs.items()):
                record = self.jobs.get(job_id)
                if record["state"] != "running" or record["owner"] != self.owner:
                    job["engine"].close()
                    del self._jobs[job_id]
                    continue
                try:
                    inventory = job["engine"].inventory("000000", job["settings"])
                    self.jobs.save(job_id, self.owner, inventory=inventory)
                    if inventory["ready"] == inventory["total"]:
                        self.jobs.publish(
                            job_id, self.owner, inventory, lambda: self.publish(job)
                        )
                        job["engine"].close()
                        del self._jobs[job_id]
                    elif (inventory.get("preparation") or {}).get(
                        "state"
                    ) == "finished_with_errors":
                        errors = [
                            job["engine"]
                            .status("000000", index, job["settings"])
                            .get("error", "")
                            for index, state in enumerate(inventory.get("states", []))
                            if state == "error"
                        ]
                        self.jobs.fail(
                            job_id,
                            self.owner,
                            "; ".join(errors) or "Speech preparation failed",
                            delay=self.retry_delay,
                        )
                        job["engine"].close()
                        del self._jobs[job_id]
                except (
                    OSError,
                    ValueError,
                    KeyError,
                    subprocess.SubprocessError,
                ) as exc:
                    self.jobs.fail(job_id, self.owner, str(exc), delay=self.retry_delay)
                    job["engine"].close()
                    del self._jobs[job_id]
            for record in self.jobs.claim(
                self.owner, limit=self.max_active_jobs, lease_seconds=self.lease_seconds
            ):
                try:
                    if self.config is None and self.repository is None:
                        raise ValueError(
                            "Configure a TTS connection to resume this preparation"
                        )
                    self._jobs[record["id"]] = self._open(record)
                    if self._heartbeat_thread is None:
                        self._heartbeat_thread = threading.Thread(
                            target=self._heartbeat, daemon=True
                        )
                        self._heartbeat_thread.start()
                except (ImportError, OSError, ValueError, KeyError) as exc:
                    self.jobs.fail(record["id"], self.owner, str(exc), retry=False)

    def status(self, job_id):
        self.tick()
        record = self.jobs.get(job_id)
        result = self._public(record)
        job = self._jobs.get(job_id)
        if job:
            result["variant"] = job["variant"]
            result["inventory"] = job["engine"].inventory("000000", job["settings"])
        return result

    def retry(self, job_id):
        record = self.jobs.get(job_id)
        self.jobs.enqueue([(job_id, record["specification"])])
        return self.status(job_id)

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
                if any(existing["id"] == rec["id"] for existing in old["recordings"]):
                    return previous["release"]
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
        with self._lock:
            self.jobs.cancel(job_id)
            job = self._jobs.pop(job_id, None)
            if job:
                job["engine"].cancel("000000", job["settings"])
                job["engine"].close()
            return {"id": job_id, "state": self.jobs.get(job_id)["state"]}

    def close(self):
        with self._lock:
            self._closing = True
            self._heartbeat_stop.set()
            for job in self._jobs.values():
                job["engine"].close()
            self._jobs.clear()
            self.jobs.release(self.owner)
        if self._heartbeat_thread:
            self._heartbeat_thread.join(timeout=2)
