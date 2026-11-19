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
import urllib.request
from concurrent.futures import ThreadPoolExecutor
import subprocess
import threading
from uuid import uuid4

from .core import digest, file_digest, write_json, finite
from .packs import export_release, recording_id
from .jobs import JobStore
from .narration import TITLE_POLICY, speech_cache_key


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
            "output_format": getattr(engine, "output_format", "mp3"),
            "title_policy": TITLE_POLICY if getattr(engine, "title_handling", False) else None,
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
            f"artifacts/{variant}/{row['id'].replace(':', '-')}/{index:04d}-{sha}{target.suffix}"
        )
        segment = dict(
            index=index,
            path=path,
            sha256=sha,
            duration=duration,
            media_type="audio/ogg" if target.suffix == ".ogg" else "audio/mpeg",
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
        from .settings import ServerSettings

        self.preferences = ServerSettings(library.store.state)
        self.library = library
        self.config = config
        self.repository = Path(repository) if repository else None
        self.default_profile = profile
        self.endpoint = endpoint
        self.engine_factory = engine_factory
        self._jobs = {}
        self._lock = threading.RLock()
        self._health = {}
        self._backend_workers = {}
        self._voice_store = None
        self.jobs = JobStore(library.store.state)
        self.owner = uuid4().hex
        self.max_active_jobs = max_active_jobs
        self.retry_delay = retry_delay
        self.lease_seconds = lease_seconds
        self._closing = False
        self._heartbeat_stop = threading.Event()
        self._heartbeat_thread = None

    def speech_workers(self, endpoint, model):
        """Operational concurrency follows the gateway, independently of recipes."""

        if model.lower() != "breeze-tts2":
            return 1
        cached = self._backend_workers.get(endpoint)
        if cached and time.monotonic() - cached[0] < 30:
            return cached[1]
        workers = 1
        try:
            with urllib.request.urlopen(
                endpoint.removesuffix("/v1/audio/speech") + "/v1/runtime", timeout=2
            ) as response:
                runtime = json.load(response)
            gateway = runtime.get("gateway", {})
            replicas = gateway.get("workers")
            if isinstance(replicas, list):
                workers = sum(
                    isinstance(row, dict) and row.get("ready") is True
                    for row in replicas
                )
            else:
                workers = gateway.get(
                    "replicas", runtime.get("long_form_jobs", {}).get("workers", 1)
                )
            workers = max(1, min(64, int(workers)))
        except (OSError, ValueError, TypeError, AttributeError):
            workers = cached[1] if cached else 1
        self._backend_workers[endpoint] = (time.monotonic(), workers)
        return workers

    def saved_profile_store(self):
        from .voice_profiles import RenderProfiles

        if not hasattr(self, "_render_profiles"):
            self._render_profiles = RenderProfiles(self.library.store.state)
        return self._render_profiles

    def sync_saved_profiles(self):
        sources = {}
        if self.config is not None or self.repository is not None:
            from dkvis.presentation.tts import load_profiles, resolve_profile

            document = load_profiles(self.config)
            preferences = self.preferences.read()
            for key in document.get("profiles", {}):
                try:
                    source = resolve_profile(document, key)
                    source["endpoint"] = (
                        self.endpoint
                        or os.environ.get("DKVIS_AUDIO_TTS_ENDPOINT")
                        or source["endpoint"]
                    )
                    source["model"] = (
                        os.environ.get("DKVIS_AUDIO_TTS_MODEL") or source["model"]
                    )
                    if not source.get("reference"):
                        source["voice"] = (
                            os.environ.get("DKVIS_AUDIO_TTS_VOICE")
                            or preferences["profiles"].get(key, {}).get("default_voice")
                            or source["voice"]
                        )
                    source["response_format"] = (
                        os.environ.get("DKVIS_AUDIO_TTS_RESPONSE_FORMAT")
                        or source["response_format"]
                    )
                    sources[key] = source
                except (ValueError, KeyError, OSError):
                    continue
            default = (
                preferences["default_profile"]
                or self.default_profile
                or os.environ.get("DKVIS_AUDIO_TTS_PROFILE")
                or document.get("profile")
                or os.environ.get("DKVIS_TTS_PROFILE")
            )
        else:
            default = None
        self.saved_profile_store().sync(
            sources,
            default_source=default or next(iter(sources), None),
            environment=dict(os.environ),
        )
        return sources

    def profile_catalog(self, *, probe=False, include_archived=False):
        from .voice_profiles import SCHEMA, RenderProfiles

        self.sync_saved_profiles()
        store = self.saved_profile_store()
        profiles = []
        backends = store.backends()
        for item in store.list() + (
            store.list(archived=True) if include_archived else []
        ):
            row = RenderProfiles.public(item)
            backend = next((b for b in backends if b["id"] == row["backend_id"]), None)
            row["available"] = bool(
                backend and backend["available"] and backend["model"] == row["model"]
            )
            profiles.append(row)
        default = store.default()
        if default not in {p["id"] for p in profiles if not p["archived"]}:
            default = next(
                (p["id"] for p in profiles if p["available"] and not p["archived"]),
                None,
            )
        return dict(
            schema=SCHEMA,
            profiles=profiles,
            default_profile=default,
            preferred_profile=default,
            tools_available=bool(
                shutil.which("ffmpeg")
                and shutil.which("ffprobe")
                and any(p["available"] for p in profiles)
            ),
            backends=[
                dict(
                    id=b["id"],
                    model=b["model"],
                    label=b["model"]
                    + " · "
                    + str(urlparse(b["endpoint"]).hostname)
                    + ":"
                    + str(
                        urlparse(b["endpoint"]).port
                        or (443 if b["endpoint"].startswith("https:") else 80)
                    ),
                    available=b["available"],
                    capabilities=b["capabilities"],
                )
                for b in backends
            ],
        )

    def profile_backend_voices(self, backend_id, *, probe=False):
        sources = self.sync_saved_profiles()
        backend = next(
            (
                b
                for b in self.saved_profile_store().backends()
                if b["id"] == backend_id and b["available"]
            ),
            None,
        )
        if backend is None:
            raise ValueError("Backend unavailable")
        from dkvis.presentation.tts import remote_voices

        voices = {}
        registry = self.voice_store()
        for alias in backend["aliases"]:
            config = sources[alias]
            value = config["voice"]
            voices[value] = dict(
                voice=value, label=value, reference=bool(config.get("reference"))
            )
            labels = {v["voice"]: v["label"] for v in registry.registered(alias)}
            for value in set(registry.catalog(alias)) | set(labels):
                voices.setdefault(
                    value,
                    dict(voice=value, label=labels.get(value, value), reference=False),
                )
        discovery = "cached"
        if probe:
            fetched = remote_voices(
                backend["endpoint"], sources[backend["anchor"]]["voice"]
            )
            discovery = "live" if fetched else "unavailable"
            if fetched:
                registry.catalog(backend["anchor"], fetched)
                for value in fetched:
                    voices.setdefault(
                        value, dict(voice=value, label=value, reference=False)
                    )
        return dict(
            backend_id=backend_id,
            voices=sorted(voices.values(), key=lambda row: row["label"].casefold()),
            discovery=discovery,
        )

    @staticmethod
    def _profile_editor_settings(recipe):
        return dict(
            native_rate=recipe["native_rate"],
            tempo=recipe["tempo"],
            body_mode=recipe["body_mode"],
            body_request=recipe["config"].get("request", {}),
            title_enabled=recipe["title_enabled"],
            title_instruction_field=recipe["title_instruction_field"],
            title_instruction=recipe["title_instruction"],
            title_pause_before=recipe["title_pause_before"],
            title_pause_after=recipe["title_pause_after"],
            title_cfg_scale=recipe["title_cfg_scale"],
            processing=recipe["processing"],
            output_format=recipe["config"]["output_format"],
            generation_revision=recipe["generation_revision"],
            pronunciation_replacements=recipe["config"].get(
                "pronunciation_replacements", {}
            ),
            reader=recipe["reader"],
        )

    def profile_editor(self, profile_id):
        self.sync_saved_profiles()
        item = self.saved_profile_store().get(profile_id)
        return dict(
            profile=self.saved_profile_store().public(item),
            settings=self._profile_editor_settings(item["recipe"]),
        )

    def save_profile(self, payload, *, template_only=False):
        from .voice_profiles import recipe_from_config, INSTRUCTION_FIELDS

        sources = self.sync_saved_profiles()
        store = self.saved_profile_store()
        existing = store.get(payload["id"]) if payload.get("id") else None
        duplicate = (
            store.get(payload["duplicate_of"]) if payload.get("duplicate_of") else None
        )
        source = existing or duplicate
        backend_id = payload.get("backend_id") or (
            source["recipe"]["backend_id"] if source else None
        )
        backend = next(
            (b for b in store.backends() if b["id"] == backend_id and b["available"]),
            None,
        )
        if backend is None:
            raise ValueError("Choose an available backend")
        voice = payload.get("voice") or (
            source["recipe"]["config"]["voice"] if source else None
        )
        if existing and existing["recipe"]["backend_id"] != backend_id:
            raise ValueError("Duplicate the profile to change its backend")
        if (
            source
            and source["recipe"]["backend_id"] == backend_id
            and source["recipe"]["config"]["voice"] != voice
        ):
            if voice not in {
                v["voice"] for v in self.profile_backend_voices(backend_id)["voices"]
            }:
                raise ValueError("Select a voice known to this backend")
            recipe = deepcopy(source["recipe"])
            matching = [sources[key] for key in backend["aliases"] if sources[key]["voice"] == voice]
            reference = next((item for item in matching if item.get("reference")), matching[0] if matching else {})
            recipe["config"]["voice"] = voice
            recipe["reference"] = deepcopy(reference.get("reference"))
            recipe["fixed_reference"] = bool(recipe["reference"])
            recipe["config"].pop("voice_revision", None)
            if "voice_revision" in reference:
                recipe["config"]["voice_revision"] = reference["voice_revision"]
        elif source and (
            source["recipe"]["backend_id"],
            source["recipe"]["config"]["voice"],
        ) == (backend_id, voice):
            recipe = deepcopy(source["recipe"])
        else:
            if voice not in {
                v["voice"] for v in self.profile_backend_voices(backend_id)["voices"]
            }:
                raise ValueError("Select a voice known to this backend")
            template = next(
                (
                    sources[key]
                    for key in backend["aliases"]
                    if sources[key]["voice"] == voice and sources[key].get("reference")
                ),
                None,
            )
            template = deepcopy(template or sources[backend["anchor"]])
            if template["voice"] != voice:
                template.pop("reference", None)
                template["voice"] = voice
                template["request"] = {}
            recipe = recipe_from_config(
                template, backend_id, environment=dict(os.environ)
            )
            if recipe["body_mode"] == "paragraph":
                recipe["config"]["request"] = {
                    k: v
                    for k, v in recipe["config"].get("request", {}).items()
                    if k not in INSTRUCTION_FIELDS
                }
                recipe["config"]["request"]["cfg_scale"] = 1.0
        patch = payload.get("settings", {})
        direct = {
            "native_rate",
            "tempo",
            "body_mode",
            "title_enabled",
            "title_instruction_field",
            "title_instruction",
            "title_pause_before",
            "title_pause_after",
            "title_cfg_scale",
            "processing",
            "generation_revision",
            "reader",
        }
        if not isinstance(patch, dict) or set(patch) - direct - {
            "body_request",
            "output_format",
            "pronunciation_replacements",
        }:
            raise ValueError("Unknown voice-profile settings")
        for key in direct:
            if key in patch:
                recipe[key] = deepcopy(patch[key])
        for key, target in [
            ("body_request", "request"),
            ("output_format", "output_format"),
            ("pronunciation_replacements", "pronunciation_replacements"),
        ]:
            if key in patch:
                recipe["config"][target] = deepcopy(patch[key])
        from .voice_profiles import PIPELINE
        from dkvis.presentation.audio_quality import VERSION

        recipe.update(
            pipeline=PIPELINE,
            title_policy=TITLE_POLICY,
            processing_version=VERSION,
            capabilities=deepcopy(backend["capabilities"]),
        )
        if template_only:
            from .voice_profiles import validate_recipe

            validate_recipe(recipe, backend)
            return dict(
                recipe=recipe,
                settings=self._profile_editor_settings(recipe),
                fixed_reference=recipe["fixed_reference"],
            )
        result = store.save(
            label=payload["label"],
            recipe=recipe,
            profile_id=existing["id"] if existing else None,
            expected=payload.get("expected_revision"),
            quick=payload.get(
                "quick_select", bool(existing["quick"]) if existing else True
            ),
        )
        if payload.get("default"):
            store.set_default(result["id"])
        return store.public(result)

    def preview_profile(self, payload):
        from .render_recipe import compile_recipe, page_processor
        from .voice_profiles import revision_id
        from dkvis.presentation.audio_library import AudioLectureLibrary

        draft = self.save_profile(payload, template_only=True)
        recipe = draft["recipe"]
        token = uuid4().hex
        backend = next(
            b
            for b in self.saved_profile_store().backends()
            if b["id"] == recipe["backend_id"]
        )
        snapshot = dict(
            id="preview-" + token, revision=revision_id(recipe), recipe=recipe
        )
        document, speed = compile_recipe(snapshot, backend)
        folder = self.library.store.root / "build-cache" / "profile-previews" / token
        sources = folder / "source"
        sources.mkdir(parents=True)
        (sources / "000000-preview.md").write_text(
            "# Preview\n<!-- BEGIN SPOKEN LECTURE -->\n## A new section\n\nThis short paragraph demonstrates the profile’s normal delivery, pacing, and audio processing.\n<!-- END SPOKEN LECTURE -->\n"
        )
        engine = (self.engine_factory or AudioLectureLibrary)(
            sources=sources,
            cache=folder / "audio",
            document=document,
            profile=snapshot["id"],
            voice=recipe["config"]["voice"],
            workers=1,
            output_format=recipe["config"]["output_format"],
            title_handling=recipe["title_enabled"],
            page_chars=recipe["reader"]["page_chars"],
            page_processor=page_processor(recipe),
        )
        try:
            settings = engine.settings(recipe["config"]["voice"], speed)
            engine.prepare_lecture("000000", settings)
            deadline = time.monotonic() + 180
            while time.monotonic() < deadline:
                inventory = engine.inventory("000000", settings)
                if inventory["ready"] == inventory["total"] and inventory["total"]:
                    target = folder / ("preview." + recipe["config"]["output_format"])
                    # The fixed sample fits in one normal reader page.
                    if inventory["total"] != 1:
                        raise ValueError(
                            "Preview sample unexpectedly spans multiple pages"
                        )
                    shutil.copyfile(engine.audio_file("000000", 0, settings), target)
                    return dict(
                        url="/api/library/voice-profiles/preview/" + token,
                        output_format=recipe["config"]["output_format"],
                    )
                if any(state == "error" for state in inventory.get("states", [])):
                    raise ValueError(
                        "Preview generation failed; inspect the configured backend and profile settings"
                    )
                time.sleep(0.05)
            raise ValueError("Preview timed out; check the speech backend")
        finally:
            engine.close()

    def saved_narrators(self, row):
        from dkvis.presentation.audio_library import split_pages

        catalog = self.profile_catalog()
        store = self.saved_profile_store()
        choices = []
        matched = set()
        for profile in catalog["profiles"]:
            spec = dict(
                profile=profile["id"],
                voice_profile=dict(id=profile["id"], revision=profile["revision"]),
            )
            variant = self.variant(spec)
            recordings = [
                r
                for r in row["recordings"]
                if r.get("generator", {}).get("profile") == profile["id"]
                and r["generator"].get("profile_revision") == profile["revision"]
            ]
            recording = max(
                recordings,
                key=lambda r: (r["complete"], len(r["segments"])),
                default=None,
            )
            matched.update(r["id"] for r in recordings)
            choices.append(
                dict(
                    key="profile:" + profile["id"],
                    label=profile["label"],
                    profile=profile["id"],
                    profile_revision=profile["revision"],
                    voice=profile["voice"],
                    speed=1,
                    variant=variant,
                    quick_select=profile["quick_select"],
                    pages=split_pages(
                        row["transcript"],
                        max_chars=store.get(profile["id"])["recipe"]["reader"][
                            "page_chars"
                        ],
                    ),
                    server_default=profile["id"] == catalog["default_profile"],
                    recording_id=recording["id"] if recording else None,
                    recording_complete=bool(recording and recording["complete"]),
                    available=profile["available"],
                    fixed_recipe=True,
                )
            )
        # Historical media keeps its exact IDs. Unknown legacy recipes are never
        # silently treated as evidence that a new profile revision is prepared.
        for recording in row["recordings"]:
            if recording["id"] in matched:
                continue
            generator = recording.get("generator", {})
            profile_id = generator.get("profile")
            known = next(
                (p for p in catalog["profiles"] if p["id"] == profile_id), None
            )
            label = (
                (known["label"] + " · earlier revision")
                if known
                else (recording.get("label") or recording["variant"])
                + " · existing recording"
            )
            aliases = []
            if generator.get("profile") and generator.get("voice"):
                aliases = ["tts:" + generator["profile"] + ":" + generator["voice"]]
            choices.append(
                dict(
                    key="recording:" + recording["variant"],
                    label=label,
                    recording_id=recording["id"],
                    recording_complete=recording["complete"],
                    aliases=aliases,
                )
            )
        pages = next(
            (r["pages"] for r in row["recordings"]),
            split_pages(row["transcript"], max_chars=600),
        )
        return dict(**catalog, choices=choices, pages=pages)

    def prepare_saved(
        self, lecture_ids, profile_id, *, profile_revision=None, blocks=None
    ):
        self.sync_saved_profiles()
        store = self.saved_profile_store()
        profile = store.get(profile_id, profile_revision)
        if profile["archived"]:
            raise ValueError("Select an active profile")
        backend = next(
            (b for b in store.backends() if b["id"] == profile["recipe"]["backend_id"]),
            None,
        )
        from .render_recipe import compile_recipe

        compile_recipe(profile, backend or {})
        snapshot = self.library.snapshot(copy=False)
        requests = []
        for lecture_id in dict.fromkeys(lecture_ids):
            row = deepcopy(snapshot["lectures"][lecture_id])
            if row.get("kind") != "audio":
                raise ValueError("Select an audio lecture")
            row.pop("origin", None)
            row["recordings"] = []
            from dkvis.presentation.audio_library import split_pages

            pages = split_pages(
                row["transcript"], max_chars=profile["recipe"]["reader"]["page_chars"]
            )
            if blocks is not None and (
                not isinstance(blocks, list)
                or not blocks
                or any(type(i) is not int or not 0 <= i < len(pages) for i in blocks)
            ):
                raise ValueError("Select valid audio blocks")
            configuration = dict(
                settings=deepcopy(profile["recipe"]["config"]),
                environment={},
                reference=None,
                render_revision=profile["revision"],
            )
            spec = dict(
                row=row,
                profile=profile_id,
                voice=profile["recipe"]["config"]["voice"],
                speed=1,
                configuration=configuration,
                voice_profile=dict(
                    id=profile_id,
                    revision=profile["revision"],
                    recipe=deepcopy(profile["recipe"]),
                ),
            )
            scope = self.jobs.cache_scope(spec)
            epoch = self.jobs.cache_epoch(scope)
            if epoch:
                spec["cache_epoch"] = epoch
            job_id = digest(
                dict(
                    lecture=lecture_id,
                    revision=row["revision"],
                    profile=profile_id,
                    render_revision=profile["revision"],
                    cache_epoch=epoch,
                )
            )
            requests.append((job_id, spec))
        self.jobs.enqueue(
            requests, blocks=sorted(set(blocks)) if blocks is not None else None
        )
        self.tick()
        return [self._public(self.jobs.get(key)) for key, _ in requests]

    def _open_saved(self, record, *, start=True):
        from .render_recipe import compile_recipe, page_processor
        from .voice_profiles import profile_cache_key
        from dkvis.presentation.audio_library import AudioLectureLibrary

        spec = record["specification"]
        saved = spec["voice_profile"]
        if spec.get("cache_epoch") != self.jobs.cache_epoch(
            self.jobs.cache_scope(spec)
        ):
            raise ValueError("This profile cache was cleared; prepare it again")
        # Resolve only the operational connection. All audio settings come from
        # the immutable job snapshot, even after the current profile is edited.
        self.sync_saved_profiles()
        backend = next(
            (
                b
                for b in self.saved_profile_store().backends()
                if b["id"] == saved["recipe"]["backend_id"]
            ),
            None,
        )
        document, speed = compile_recipe(saved, backend or {})
        directory = (
            self.library.store.root / "build-cache" / "generation" / record["id"]
        )
        sources = directory / "source"
        sources.mkdir(parents=True, exist_ok=True)
        source = (
            "# Lecture\n<!-- BEGIN SPOKEN LECTURE -->\n"
            + spec["row"]["transcript"]
            + "\n<!-- END SPOKEN LECTURE -->\n"
        )
        from .core import extract_text

        authored = spec["row"].get("source")
        if isinstance(authored, str):
            try:
                if extract_text(authored).strip() == spec["row"]["transcript"].strip():
                    source = authored
            except ValueError:
                pass
        (sources / "000000-lecture.md").write_text(source)
        cache = (
            self.library.store.root
            / "build-cache"
            / "speech"
            / profile_cache_key(spec["row"]["id"], saved, spec.get("cache_epoch"))
        )
        cache.mkdir(parents=True, exist_ok=True)
        factory = self.engine_factory or AudioLectureLibrary
        engine = factory(
            sources=sources,
            cache=cache,
            document=document,
            profile=saved["id"],
            voice=saved["recipe"]["config"]["voice"],
            workers=self.speech_workers(backend["endpoint"], backend["model"]),
            output_format=saved["recipe"]["config"]["output_format"],
            title_handling=saved["recipe"]["title_enabled"],
            page_chars=saved["recipe"]["reader"]["page_chars"],
            page_processor=page_processor(saved["recipe"]),
        )
        settings = engine.settings(saved["recipe"]["config"]["voice"], speed)
        job = dict(
            engine=engine,
            settings=settings,
            row=spec["row"],
            variant=self.variant(spec),
            label=self.saved_profile_store().get(saved["id"])["label"],
            published=None,
            whole_lecture=False,
            base_recording=None,
            voice_profile=saved,
        )
        if start:
            self._request_blocks(job, record["requested_blocks"])
        return job

    def clear_saved_cache(self, lecture_id, profile_id, *, revision, profile_revision):
        with self._lock:
            row = self.library.snapshot(copy=False)["lectures"][lecture_id]
            if row["revision"] != revision:
                raise ValueError("This lecture changed; reopen it first")
            self.saved_profile_store().get(profile_id, profile_revision)
            recordings = [
                r
                for r in row["recordings"]
                if r.get("generator", {}).get("profile") == profile_id
                and r["generator"].get("profile_revision") == profile_revision
            ]
            scope = digest([lecture_id, profile_id, profile_revision])
            self.jobs.clear_voice(
                scope,
                uuid4().hex,
                lambda: self.library.clear_recordings(lecture_id, recordings),
            )
            return dict(
                cleared_recordings=len(recordings),
                lecture_id=lecture_id,
                profile=profile_id,
            )

    def profiles(self, *, probe=False):
        try:
            if self.config is None and self.repository is None:
                return {"profiles": [], "tools_available": False}
            from dkvis.presentation.tts import load_profiles, resolve_profile

            document = load_profiles(self.config)
            preferences = self.preferences.read()
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
                        "output_format": os.environ.get("DKVIS_AUDIO_OUTPUT_FORMAT")
                        or profile.get("output_format", "ogg"),
                        "voice": os.environ.get("DKVIS_AUDIO_TTS_VOICE")
                        or preferences["profiles"].get(key, {}).get("default_voice")
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
                        preferences["default_profile"],
                        self.default_profile,
                        os.environ.get("DKVIS_AUDIO_TTS_PROFILE"),
                        document.get("profile"),
                        os.environ.get("DKVIS_TTS_PROFILE"),
                    )
                    if key in available
                ),
                None,
            )
            rows.sort(key=lambda row: row["id"] != selected)
            return {
                "profiles": rows,
                "errors": errors,
                "tools_available": bool(
                    shutil.which("ffmpeg") and shutil.which("ffprobe")
                ),
                "preferred_profile": selected,
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
        policy = self.preferences.read()["profiles"].get(profile, {})
        default_voice = (
            os.environ.get("DKVIS_AUDIO_TTS_VOICE")
            or policy.get("default_voice")
            or config["voice"]
        )
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
            set(available)
            | {default_voice, config["voice"]}
            | {row["voice"] for row in registered}
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

        original = resolve_profile(document, profile)
        if original.get("reference") and voice and voice != original["voice"]:
            raise ValueError(
                "This reference voice is fixed; choose or create another saved profile"
            )
        config = resolve_profile(document, profile, {"voice": voice} if voice else None)
        config = dict(config)
        config["output_format"] = os.environ.get(
            "DKVIS_AUDIO_OUTPUT_FORMAT"
        ) or config.get("output_format", "ogg")
        relevant = {k: v for k, v in config.items() if k != "reference"}
        relevant['reader_title_policy'] = TITLE_POLICY
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

    def prepare(
        self,
        lecture_id,
        profile,
        *,
        voice=None,
        speed=1,
        blocks=None,
        base_recording_id=None,
    ):
        return self.prepare_many(
            [lecture_id],
            profile,
            voice=voice,
            speed=speed,
            blocks=blocks,
            base_recording_id=base_recording_id,
        )[0]

    def narrators(self, row, *, speed=1):
        """Describe selectable recordings and configured voices without synthesis."""
        finite(speed, 0.5)
        if speed > 2:
            raise ValueError("Invalid speech speed")
        profiles = self.profiles()
        preferences = self.preferences.read()
        choices = []
        cache_epochs = self.jobs.cache_epochs()
        matched = set()
        pages = next((rec["pages"] for rec in row["recordings"]), [row["transcript"]])
        if profiles["profiles"]:
            from dkvis.presentation.audio_library import split_pages
            from dkvis.presentation.tts import load_profiles, resolve_profile

            pages = split_pages(
                row["transcript"],
                max_chars=int(os.environ.get("DKVIS_AUDIO_PAGE_CHARS", "600")),
            )
            document = load_profiles(self.config)
            for profile in profiles["profiles"]:
                voices = self.voices(profile["id"])
                original_voice = (
                    os.environ.get("DKVIS_AUDIO_TTS_VOICE")
                    or resolve_profile(document, profile["id"])["voice"]
                )
                labels = {v["voice"]: v["label"] for v in voices["registered"]}
                for voice in dict.fromkeys([profile["voice"], *voices["voices"]]):
                    _, configuration = self._configuration(
                        document, profile["id"], voice, self.endpoint
                    )
                    variant = self.variant(
                        dict(
                            cache_epoch=cache_epochs.get(
                                digest([row["id"], profile["id"], voice])
                            ),
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
                    legacy = [
                        r
                        for r in row["recordings"]
                        if not r.get("generator")
                        and r.get("label") == profile["id"]
                        and voice == original_voice
                        and speed == 1
                        and r["pages"] == pages
                    ]
                    recordings.extend(legacy)
                    recording = max(
                        recordings,
                        key=lambda r: (r["complete"], len(r["segments"]), r["variant"] == variant),
                        default=None,
                    )
                    matched.update(r["id"] for r in recordings)
                    choices.append(
                        dict(
                            key=f"tts:{profile['id']}:{voice}",
                            label=f"{profile['label']} · {labels.get(voice, voice)} · new audio: {'Ogg Opus' if configuration['settings']['output_format'] == 'ogg' else 'MP3'}",
                            output_format=configuration["settings"]["output_format"],
                            profile=profile["id"],
                            profile_default=voice == profile["voice"],
                            voice=voice,
                            speed=speed,
                            variant=variant,
                            recording_id=recording["id"] if recording else None,
                            recording_complete=bool(
                                recording and recording["complete"]
                            ),
                            base_recording_id=(
                                max(legacy, key=lambda r: len(r["segments"]))["id"]
                                if legacy
                                else None
                            ),
                            aliases=["recording:" + r["variant"] for r in legacy],
                        )
                    )
        for recording in row["recordings"]:
            if recording["id"] not in matched:
                choices.append(
                    dict(
                        key="recording:" + recording["variant"],
                        label=recording.get("label") or recording["variant"],
                        recording_id=recording["id"],
                        recording_complete=recording["complete"],
                    )
                )
        from .settings import voice_identity

        recordings_by_id = {r["id"]: r for r in row["recordings"]}
        for choice in choices:
            profile, voice = (
                (choice["profile"], choice["voice"])
                if choice.get("profile")
                else voice_identity(recordings_by_id[choice["recording_id"]])
            )
            policy = preferences["profiles"].get(profile, {})
            quick = policy.get("quick_voices")
            choice["quick_select"] = voice in quick if quick is not None else None
            choice["server_default"] = (
                preferences["default_profile"] == profile
                and policy.get("default_voice") == voice
            )
        return dict(**profiles, choices=choices, pages=pages)

    def prepare_many(
        self,
        lecture_ids,
        profile,
        *,
        voice=None,
        speed=1,
        blocks=None,
        base_recording_id=None,
    ):
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
        profiles = self.profiles()
        if not profiles["tools_available"]:
            raise ValueError(
                "Generation requires the production installation and FFmpeg tools"
            )
        from dkvis.presentation.tts import load_profiles

        document = load_profiles(self.config)
        if voice is None:
            voice = (
                self.preferences.read()["profiles"]
                .get(profile, {})
                .get("default_voice")
            )
        config, configuration = self._configuration(
            document, profile, voice, self.endpoint
        )
        default_voice = (
            os.environ.get("DKVIS_AUDIO_TTS_VOICE")
            or self._configuration(document, profile, None, self.endpoint)[0]["voice"]
        )
        if base_recording_id is not None and len(lecture_ids) != 1:
            raise ValueError("Extend a recording within one lecture")
        snapshot = self.library.snapshot(copy=False)
        requests = []
        for lecture_id in dict.fromkeys(lecture_ids):
            row = deepcopy(snapshot["lectures"][lecture_id])
            if row.get("kind") != "audio":
                raise ValueError(
                    "Use the existing presentation renderer for this lecture"
                )
            base = None
            if base_recording_id:
                recording = next(
                    (r for r in row["recordings"] if r["id"] == base_recording_id), None
                )
                if (
                    recording is None
                    or recording.get("generator")
                    or recording.get("label") != profile
                    or (voice or config["voice"]) != default_voice
                    or speed != 1
                ):
                    raise ValueError(
                        "This recording does not identify the selected profile's default voice"
                    )
                from dkvis.presentation.audio_library import split_pages

                if recording["pages"] != split_pages(
                    row["transcript"],
                    max_chars=int(os.environ.get("DKVIS_AUDIO_PAGE_CHARS", "600")),
                ):
                    raise ValueError(
                        "The recording uses different audio block boundaries"
                    )
                base = dict(
                    recording=deepcopy(recording), release=recording["_release"]
                )
                base["recording"].pop("_release", None)
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
            cache_epoch = self.jobs.cache_epoch(
                self.jobs.cache_scope(
                    dict(
                        row=row,
                        profile=profile,
                        voice=voice,
                        configuration=configuration,
                    )
                )
            )
            job_id = digest(
                {
                    **({"cache_epoch": cache_epoch} if cache_epoch else {}),
                    "lecture": lecture_id,
                    "revision": row["revision"],
                    "configuration": configuration,
                    "speed": speed,
                    **({"base_recording": base_recording_id} if base else {}),
                }
            )
            specification = {
                **({"cache_epoch": cache_epoch} if cache_epoch else {}),
                "row": row,
                "profile": profile,
                "voice": voice,
                "speed": speed,
                "configuration": configuration,
                **({"base_recording": base} if base else {}),
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
        if spec.get("voice_profile"):
            return self._open_saved(record, start=start)
        if spec.get("cache_epoch") != self.jobs.cache_epoch(
            self.jobs.cache_scope(spec)
        ):
            raise ValueError("This voice cache was cleared; start a new preparation")
        document = load_profiles(self.config)
        config, configuration = self._configuration(
            document, spec["profile"], spec["voice"], self.endpoint
        )
        saved = spec["configuration"]["settings"]
        title_handling = saved.get('reader_title_policy') == TITLE_POLICY
        # Jobs queued before reader delivery defaults were explicit keep their
        # old codec and sentence delivery, while all other settings stay guarded.
        if 'output_format' not in saved:
            configuration['settings'].pop('output_format', None)
            config['output_format'] = 'mp3'
        if 'reader_title_policy' not in saved:
            configuration['settings'].pop('reader_title_policy', None)
        if configuration != spec["configuration"]:
            raise ValueError(
                "Configured speech settings changed; start a new preparation with the revised settings"
            )
        directory = (
            self.library.store.root / "build-cache" / "generation" / record["id"]
        )
        sources = directory / "source"
        sources.mkdir(parents=True, exist_ok=True)
        source = "# Lecture\n<!-- BEGIN SPOKEN LECTURE -->\n" + spec["row"]["transcript"] + "\n<!-- END SPOKEN LECTURE -->\n"
        if title_handling:
            from .core import extract_text
            authored = spec['row'].get('source')
            if isinstance(authored,str):
                try:
                    if extract_text(authored).strip() == spec['row']['transcript'].strip(): source = authored
                except ValueError:
                    pass
        (sources / "000000-lecture.md").write_text(source)
        # Source revisions share request-addressed pages when speech inputs agree.
        cache = (
            self.library.store.root
            / "build-cache"
            / "speech"
            / speech_cache_key(
                spec["row"]["id"],
                {
                    **configuration,
                    **(
                        {"cache_epoch": spec["cache_epoch"]}
                        if spec.get("cache_epoch")
                        else {}
                    ),
                },
            )
        )
        cache.mkdir(parents=True, exist_ok=True)
        legacy_cache = directory / "audio"
        if legacy_cache.is_dir():
            for path in legacy_cache.iterdir():
                if path.is_file() and (
                    path.suffix in {".mp3", ".ogg"} or path.name.endswith(".timings.json")
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
            workers=self.speech_workers(
                self.endpoint
                or os.environ.get("DKVIS_AUDIO_TTS_ENDPOINT")
                or config["endpoint"],
                os.environ.get("DKVIS_AUDIO_TTS_MODEL") or config["model"],
            ),
            output_format=config["output_format"],
            title_handling=title_handling,
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
            "base_recording": spec.get("base_recording"),
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
    def _inventory(job):
        inventory = job["engine"].inventory("000000", job["settings"])
        base = job.get("base_recording")
        if base:
            for segment in base["recording"]["segments"]:
                inventory["states"][segment["index"]] = "ready"
            inventory["ready"] = inventory["states"].count("ready")
            inventory["percent"] = round(
                100 * inventory["ready"] / max(1, inventory["total"]), 1
            )
            inventory["counts"] = {
                state: inventory["states"].count(state) for state in inventory["counts"]
            }
        return inventory

    def _blend_recording(self, job, recording, files):
        base = job.get("base_recording")
        if not base:
            return
        directory = self.library.store.historical(base["release"], job["row"]["id"])[1]
        current = {segment["index"]: segment for segment in recording["segments"]}
        inherited = []
        for segment in base["recording"]["segments"]:
            if segment["index"] not in current:
                current[segment["index"]] = deepcopy(segment)
                files[segment["path"]] = directory / segment["path"]
                inherited.append(segment["index"])
        recording["segments"] = [current[index] for index in sorted(current)]
        recording["complete"] = len(current) == len(recording["pages"])
        if inherited:
            recording["generator"]["inherited_recordings"] = [
                dict(
                    id=base["recording"]["id"],
                    recipe=base["recording"]["recipe"],
                    blocks=inherited,
                )
            ]
        recording["id"] = recording_id(recording)

    @staticmethod
    def _request_blocks(job, blocks):
        engine, settings = job["engine"], job["settings"]
        if blocks is None and not job.get("base_recording"):
            if not job["whole_lecture"]:
                engine.prepare_lecture("000000", settings)
                job["whole_lecture"] = True
            return
        inventory = GenerationManager._inventory(job)
        if blocks is None:
            blocks = list(range(inventory["total"]))
        busy = sum(
            state in {"queued", "rendering", "canceling"}
            for state in inventory["states"]
        )
        for index in blocks:
            if busy >= max(3, getattr(engine, "workers", 1)):
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
                recording, files = recording_from_engine(
                    job["engine"],
                    "000000",
                    job["row"],
                    variant=job["variant"],
                    label=job["label"],
                    voice=job["settings"].voice,
                    speed=job["settings"].speed,
                )
                if job.get("voice_profile"):
                    recording["generator"]["profile_revision"]=job["voice_profile"]["revision"]
                    recording["id"]=recording_id(recording)
                self._blend_recording(job, recording, files)
                base = job.get("base_recording")
                inherited = {
                    index
                    for item in recording["generator"].get("inherited_recordings", [])
                    for index in item["blocks"]
                }
                for segment in recording["segments"]:
                    if segment["index"] in inherited:
                        segment["_release"] = base["release"]
                        segment["_recording"] = base["recording"]["id"]
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
        if spec.get("voice_profile"):
            return (
                "profile-"
                + digest(
                    dict(
                        id=spec["voice_profile"]["id"],
                        revision=spec["voice_profile"]["revision"],
                    )
                )[:20]
            )
        config = spec["configuration"]["settings"]
        environment = spec["configuration"]["environment"]
        return (
            "narrator-"
            + digest(
                {
                    **(
                        {"cache_epoch": spec["cache_epoch"]}
                        if spec.get("cache_epoch")
                        else {}
                    ),
                    "profile": spec["profile"],
                    "voice": (
                        settings.voice
                        if settings
                        else spec["voice"]
                        or environment.get("DKVIS_AUDIO_TTS_VOICE")
                        or config["voice"]
                    ),
                    "speed": (
                        settings.speed if settings else round(float(spec["speed"]), 3)
                    ),
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
            "profile_revision": spec.get("voice_profile", {}).get("revision"),
            "variant": GenerationManager.variant(spec),
            "voice": spec["voice"]
            or spec["configuration"]["environment"].get("DKVIS_AUDIO_TTS_VOICE")
            or spec["configuration"]["settings"]["voice"],
            "model": spec["configuration"]["environment"].get("DKVIS_AUDIO_TTS_MODEL")
            or spec["configuration"]["settings"]["model"],
            "speed": spec["speed"],
            "state": record["state"],
            "created_at": record["created_at"],
            "updated_at": record["updated_at"],
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

    def list(self, lecture_id=None):
        return [
            self._public(record)
            for record in self.jobs.list(lecture_id)
            if record["state"] != "cleared"
        ]

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
                            job_id, self._inventory(job)
                        )
                    job["engine"].close()
                    del self._jobs[job_id]
                    continue
                try:
                    self._request_blocks(job, record["requested_blocks"])
                    inventory = self._inventory(job)
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
            result["inventory"] = self._inventory(job)
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
        self._blend_recording(job, rec, files)
        if job.get("voice_profile"):
            saved = job["voice_profile"]
            rec["generator"].update(
                profile_revision=saved["revision"], profile_schema="voice-profiles-v1"
            )
            rec["id"] = recording_id(rec)
        pack_id = "audio-" + digest(row["id"])[:24]
        previous = next(
            (r for r in self.library.store.active() if r["pack_id"] == pack_id), None
        )
        recordings = [(row["id"], rec, files)]
        if previous:
            old = deepcopy(json.loads(previous["catalog"])["lectures"].get(row["id"]))
            if old:
                visible = {
                    r["id"]
                    for r in self.library.snapshot(copy=False)["lectures"]
                    .get(row["id"], {})
                    .get("recordings", [])
                }
                old["recordings"] = [r for r in old["recordings"] if r["id"] in visible]
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

    def clear_voice_cache(self, lecture_id, profile, voice, *, revision):
        from dkvis.presentation.tts import load_profiles

        with self._lock:
            row = self.library.snapshot(copy=False)["lectures"][lecture_id]
            if row["revision"] != revision:
                raise ValueError(
                    "This lecture changed; reopen it before clearing audio"
                )
            if row.get("kind") != "audio":
                raise ValueError("Select an audio lecture")
            config, configuration = self._configuration(
                load_profiles(self.config), profile, voice, self.endpoint
            )
            selected = (
                voice
                or configuration["environment"].get("DKVIS_AUDIO_TTS_VOICE")
                or config["voice"]
            )
            default = (
                os.environ.get("DKVIS_AUDIO_TTS_VOICE")
                or self._configuration(
                    load_profiles(self.config), profile, None, self.endpoint
                )[0]["voice"]
            )
            recordings = [
                r
                for r in row["recordings"]
                if (
                    r.get("generator", {}).get("profile") == profile
                    and r["generator"].get("voice") == selected
                )
                or (
                    not r.get("generator")
                    and r.get("label") == profile
                    and selected == default
                )
            ]
            scope = digest([lecture_id, profile, selected])
            self.jobs.clear_voice(
                scope,
                uuid4().hex,
                lambda: self.library.clear_recordings(lecture_id, recordings),
            )
            return {
                "cleared_recordings": len(recordings),
                "lecture_id": lecture_id,
                "voice": selected,
            }

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
