"""Optional legacy production adapters, imported only when generation is requested."""

from __future__ import annotations

from copy import deepcopy
from contextlib import contextmanager
from functools import lru_cache
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


@lru_cache(maxsize=4096)
def audio_facts(path, modified, size):
    """Probe completed, atomically published cache files once during playback."""
    return file_digest(path), audio_duration(path)


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
            "profile": engine.profile,
            "voice": settings.voice,
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
        stat = target.stat()
        sha, duration = audio_facts(target, stat.st_mtime_ns, stat.st_size)
        path = (
            f"artifacts/{variant}/{row['id'].replace(':', '-')}/{index:04d}-{sha}.mp3"
        )
        segment = dict(
            index=index,
            path=path,
            sha256=sha,
            duration=duration,
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
        self._voice_store = None
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
            errors = []
            for key in document.get("profiles", {}):
                try:
                    profile = resolve_profile(document, key)
                except (OSError, ValueError, KeyError, TypeError) as exc:
                    errors.append(f"{key}: {exc}")
                    continue
                rows.append(
                    {
                        "id": key,
                        "label": profile.get("display_name", key),
                        "voice": os.environ.get("DKVIS_AUDIO_TTS_VOICE")
                        or profile["voice"],
                        "model": os.environ.get("DKVIS_AUDIO_TTS_MODEL")
                        or profile["model"],
                        "_endpoint": self.endpoint
                        or os.environ.get("DKVIS_AUDIO_TTS_ENDPOINT")
                        or profile["endpoint"],
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
            available = {row["id"] for row in rows}
            selected = next(
                (
                    key
                    for key in (
                        self.default_profile,
                        os.environ.get("DKVIS_AUDIO_TTS_PROFILE"),
                        os.environ.get("DKVIS_TTS_PROFILE"),
                        document.get("profile"),
                    )
                    if key in available
                ),
                None,
            )
            return {
                "profiles": rows,
                "errors": errors,
                "tools_available": bool(
                    shutil.which("ffmpeg") and shutil.which("ffprobe")
                ),
                "default_profile": (
                    selected
                    if any(row["id"] == selected for row in rows)
                    else (rows[0]["id"] if rows else None)
                ),
            }
        except (ImportError, OSError, ValueError, KeyError) as exc:
            return {"profiles": [], "tools_available": False, "error": str(exc)}

    def voice_store(self):
        if self._voice_store is None:
            from .voices import VoiceStore

            self._voice_store = VoiceStore(
                self.library.store.state,
                legacy=(
                    self.repository / "audio-cache" / "registered-voices.json"
                    if self.repository
                    else None
                ),
            )
        return self._voice_store

    def voices(self, profile, *, probe=False):
        from dkvis.presentation.tts import load_profiles, resolve_profile, remote_voices

        config = resolve_profile(load_profiles(self.config), profile)
        profile = config["profile"]
        default_voice = os.environ.get("DKVIS_AUDIO_TTS_VOICE") or config["voice"]
        store = self.voice_store()
        registered = store.registered(profile)
        available = store.catalog(profile)
        if probe:
            fetched = remote_voices(
                self.endpoint
                or os.environ.get("DKVIS_AUDIO_TTS_ENDPOINT")
                or config["endpoint"],
                default_voice,
            )
            if fetched:
                available = store.catalog(profile, fetched)
        names = sorted(
            set(available) | {default_voice} | {row["voice"] for row in registered}
        )
        return dict(
            profile=profile,
            model=os.environ.get("DKVIS_AUDIO_TTS_MODEL") or config["model"],
            default_voice=default_voice,
            voices=names,
            registered=registered,
        )

    def register_voice(self, profile, voice, label=None):
        from dkvis.presentation.tts import load_profiles, resolve_profile

        config = resolve_profile(load_profiles(self.config), profile)
        return self.voice_store().register(config["profile"], voice, label)

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

    def prepare(self, lecture_id, profile, *, voice=None, speed=1, blocks=None):
        return self.prepare_many(
            [lecture_id], profile, voice=voice, speed=speed, blocks=blocks
        )[0]

    def narrators(self, row, *, speed=1):
        """Describe selectable recordings and configured voices without synthesis."""
        finite(speed, 0.5)
        if speed > 2:
            raise ValueError("Invalid speech speed")
        profiles = self.profiles()
        choices = []
        matched = set()
        pages = next((rec["pages"] for rec in row["recordings"]), [row["transcript"]])
        if profiles["profiles"]:
            from dkvis.presentation.audio_library import split_pages
            from dkvis.presentation.tts import load_profiles

            pages = split_pages(
                row["transcript"],
                max_chars=int(os.environ.get("DKVIS_AUDIO_PAGE_CHARS", "600")),
            )
            document = load_profiles(self.config)
            for profile in profiles["profiles"]:
                voices = self.voices(profile["id"])
                labels = {v["voice"]: v["label"] for v in voices["registered"]}
                for voice in dict.fromkeys([profile["voice"], *voices["voices"]]):
                    _, configuration = self._configuration(
                        document, profile["id"], voice, self.endpoint
                    )
                    variant = self.variant(
                        dict(
                            profile=profile["id"],
                            voice=voice,
                            speed=speed,
                            configuration=configuration,
                        )
                    )
                    recordings = [
                        r
                        for r in row["recordings"]
                        if r["variant"] == variant
                        or (
                            r.get("generator", {}).get("profile") == profile["id"]
                            and r["generator"].get("voice") == voice
                            and r["generator"].get("model") == profile["model"]
                            and r["generator"].get("speech_speed", 1) == speed
                        )
                    ]
                    recording = max(
                        recordings,
                        key=lambda r: (r["complete"], len(r["segments"])),
                        default=None,
                    )
                    matched.update(r["id"] for r in recordings)
                    choices.append(
                        dict(
                            key=f"tts:{profile['id']}:{voice}",
                            label=f"{profile['label']} · {labels.get(voice, voice)}",
                            profile=profile["id"],
                            profile_default=voice == profile["voice"],
                            voice=voice,
                            speed=speed,
                            variant=variant,
                            recording_id=recording["id"] if recording else None,
                        )
                    )
        for recording in row["recordings"]:
            if recording["id"] not in matched:
                choices.append(
                    dict(
                        key="recording:" + recording["variant"],
                        label=recording.get("label") or recording["variant"],
                        recording_id=recording["id"],
                    )
                )
        return dict(**profiles, choices=choices, pages=pages)

    def prepare_many(self, lecture_ids, profile, *, voice=None, speed=1, blocks=None):
        finite(speed, 0.5)
        if speed > 2 or (
            voice is not None and not re.fullmatch(r"[A-Za-z0-9_.+\-]{1,80}", voice)
        ):
            raise ValueError("Invalid speech speed or voice")
        if blocks is not None:
            if (
                not isinstance(blocks, list)
                or not blocks
                or any(
                    isinstance(index, bool) or not isinstance(index, int) or index < 0
                    for index in blocks
                )
            ):
                raise ValueError("Select one or more audio blocks")
            blocks = sorted(set(blocks))
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
            if blocks is not None:
                from dkvis.presentation.audio_library import split_pages

                pages = split_pages(
                    row["transcript"],
                    max_chars=int(os.environ.get("DKVIS_AUDIO_PAGE_CHARS", "600")),
                )
                if blocks[-1] >= len(pages):
                    raise ValueError("Unknown audio block")
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
        self.jobs.enqueue(requests, blocks=blocks)
        self.tick()
        return [self._public(self.jobs.get(job_id)) for job_id, _ in requests]

    def _heartbeat(self):
        while not self._heartbeat_stop.wait(max(0.05, self.lease_seconds / 3)):
            try:
                self.jobs.heartbeat(self.owner, self.lease_seconds)
            except (OSError, sqlite3.Error):
                pass

    def _open(self, record, *, start=True):
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
        variant = self.variant(spec, settings)
        job = {
            "engine": engine,
            "settings": settings,
            "row": spec["row"],
            "variant": variant,
            "label": f"{settings.voice} ({settings.model})",
            "published": None,
            "whole_lecture": False,
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
        if start:
            self._request_blocks(job, record["requested_blocks"])
        return job

    @staticmethod
    def _request_blocks(job, blocks):
        engine, settings = job["engine"], job["settings"]
        if blocks is None:
            if not job["whole_lecture"]:
                engine.prepare_lecture("000000", settings)
                job["whole_lecture"] = True
            return
        inventory = engine.inventory("000000", settings)
        busy = sum(
            state in {"queued", "rendering", "canceling"}
            for state in inventory["states"]
        )
        for index in blocks:
            if busy >= 3:
                break
            if inventory["states"][index] in {"missing", "cancelled"}:
                engine.request(
                    "000000",
                    index,
                    settings,
                    "playback" if index == blocks[0] else "cache",
                )
                busy += 1

    def playback(self, job_id):
        """Read completed blocks while preparation continues; never enqueue work."""
        with self._lock:
            record = self.jobs.get(job_id)
            active = self._jobs.get(job_id)
            job = active or self._open(record, start=False)
            try:
                recording, _ = recording_from_engine(
                    job["engine"],
                    "000000",
                    job["row"],
                    variant=job["variant"],
                    label=job["label"],
                    voice=job["settings"].voice,
                    speed=job["settings"].speed,
                )
                recording["_job"] = job_id
                row = deepcopy(job["row"])
                row["recordings"] = [recording]
                return row
            finally:
                if not active:
                    job["engine"].close()

    def playback_file(self, job_id, index, sha):
        with self._lock:
            record = self.jobs.get(job_id)
            active = self._jobs.get(job_id)
            job = active or self._open(record, start=False)
            try:
                path = job["engine"].audio_file("000000", index, job["settings"])
                stat = path.stat()
                if audio_facts(path, stat.st_mtime_ns, stat.st_size)[0] != sha:
                    raise KeyError("This prepared block has changed")
                return path
            finally:
                if not active:
                    job["engine"].close()

    def prioritize(self, job_id, index):
        """Promote the passage the listener requested above background caching."""
        if isinstance(index, bool) or not isinstance(index, int) or index < 0:
            raise ValueError("Select an audio block")
        with self._lock:
            record = self.jobs.get(job_id)
            job = self._jobs.get(job_id)
            if job and record["state"] == "running" and record["owner"] == self.owner:
                if index >= len(job["engine"].detail("000000")["pages"]):
                    raise ValueError("Unknown audio block")
                job["engine"].request("000000", index, job["settings"], "playback")
            return self._public(record)

    @staticmethod
    def variant(spec, settings=None):
        config = spec["configuration"]["settings"]
        environment = spec["configuration"]["environment"]
        return (
            "narrator-"
            + digest(
                {
                    "profile": spec["profile"],
                    "voice": (
                        settings.voice
                        if settings
                        else spec["voice"]
                        or environment.get("DKVIS_AUDIO_TTS_VOICE")
                        or config["voice"]
                    ),
                    "speed": settings.speed
                    if settings
                    else round(float(spec["speed"]), 3),
                    "model": (
                        settings.model
                        if settings
                        else environment.get("DKVIS_AUDIO_TTS_MODEL") or config["model"]
                    ),
                    "voice_revision": config.get("voice_revision"),
                    "reference": spec["configuration"].get("reference"),
                }
            )[:16]
        )

    @staticmethod
    def _public(record):
        spec = record["specification"]
        return {
            "id": record["id"],
            "lecture_id": spec["row"]["id"],
            "revision": spec["row"]["revision"],
            "title": spec["row"]["title"],
            "profile": spec["profile"],
            "variant": GenerationManager.variant(spec),
            "voice": spec["voice"]
            or spec["configuration"]["environment"].get("DKVIS_AUDIO_TTS_VOICE")
            or spec["configuration"]["settings"]["voice"],
            "model": spec["configuration"]["environment"].get("DKVIS_AUDIO_TTS_MODEL")
            or spec["configuration"]["settings"]["model"],
            "speed": spec["speed"],
            "state": record["state"],
            "attempts": record["attempts"],
            "retry_at": record["retry_at"],
            "error": record["error"],
            "published": record["published"],
            "requested_blocks": record["requested_blocks"],
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
                    if record["state"] == "cancelled":
                        job["engine"].cancel("000000", job["settings"])
                        self.jobs.retain_cancelled_inventory(
                            job_id, job["engine"].inventory("000000", job["settings"])
                        )
                    job["engine"].close()
                    del self._jobs[job_id]
                    continue
                try:
                    self._request_blocks(job, record["requested_blocks"])
                    inventory = job["engine"].inventory("000000", job["settings"])
                    if not self.jobs.save(job_id, self.owner, inventory=inventory):
                        self.jobs.retain_cancelled_inventory(job_id, inventory)
                        job["engine"].close()
                        del self._jobs[job_id]
                        continue
                    requested = record["requested_blocks"]
                    complete = (
                        inventory["ready"] == inventory["total"]
                        if requested is None
                        else all(
                            inventory["states"][index] == "ready" for index in requested
                        )
                    )
                    failed = (
                        any(
                            inventory["states"][index] == "error" for index in requested
                        )
                        if requested is not None
                        else (inventory.get("preparation") or {}).get("state")
                        == "finished_with_errors"
                    )
                    if complete:
                        # File probing/copying must not lock out cancellation.
                        with self._publication(job) as activate:
                            published = self.jobs.publish(
                                job_id,
                                self.owner,
                                inventory,
                                activate,
                                requested_blocks=requested,
                            )
                        if published is None:
                            continue
                        job["engine"].close()
                        del self._jobs[job_id]
                    elif failed:
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
        self.jobs.enqueue(
            [(job_id, record["specification"])], blocks=record["requested_blocks"]
        )
        return self.status(job_id)

    def publish(self, job):
        with self._publication(job) as activate:
            return activate()

    @contextmanager
    def _publication(self, job):
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
                    if (
                        existing["variant"] == rec["variant"]
                        and existing["recipe"] == rec["recipe"]
                        and existing["pages"] == rec["pages"]
                    ):
                        segments = {
                            segment["index"]: segment
                            for segment in existing["segments"]
                        }
                        segments.update(
                            {segment["index"]: segment for segment in rec["segments"]}
                        )
                        for segment in existing["segments"]:
                            if segments[segment["index"]]["path"] == segment["path"]:
                                files.setdefault(
                                    segment["path"],
                                    Path(previous["directory"]) / segment["path"],
                                )
                        rec["segments"] = [
                            segments[index] for index in sorted(segments)
                        ]
                        rec["complete"] = len(segments) == len(rec["pages"])
                        rec["id"] = recording_id(rec)
                if any(existing["id"] == rec["id"] for existing in old["recordings"]):
                    yield lambda: previous["release"]
                    return
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
        export_release(
            pack,
            directory,
            parent=previous["release"] if previous else None,
            media=recordings,
            kind="media",
        )
        with self.library.store.stage_install(directory) as staged:
            yield lambda: self.library.store.activate_install(staged)["release"]

    def cancel(self, job_id):
        # Persist first. The coordinator may be probing/copying many audio files
        # under _lock; it observes this state before it can activate a recording.
        self.jobs.cancel(job_id)
        state = self.jobs.get(job_id)["state"]
        job = self._jobs.get(job_id)
        if job and state == "cancelled":
            job["engine"].cancel("000000", job["settings"])
        # tick owns cleanup and refreshes final cached-block counts.
        return {"id": job_id, "state": state}

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
