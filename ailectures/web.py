"""One local server: live packs, playback, optional synthesis, and open profiles."""

from __future__ import annotations

import asyncio
import json
import re
import threading
from contextlib import asynccontextmanager
from copy import deepcopy
from pathlib import Path
from uuid import uuid4
from urllib.parse import quote

from starlette.applications import Starlette
from starlette.concurrency import run_in_threadpool
from starlette.exceptions import HTTPException
from starlette.responses import (
    FileResponse,
    JSONResponse,
    PlainTextResponse,
    RedirectResponse,
    Response,
)
from starlette.routing import Mount, Route

from .core import Conflict, checksum, finite, qualified, digest
from .library import Library
from .state import ListenerState, utcnow
from .organization import collection_metadata, item_organization
from .companions import available_companions
from .assets import LibraryAssets
from .slide_companions import SlideCompanionsUnavailable
from .chronology import chronology_for, collection_chronology
from .discovery import discovery_fields
from .descriptions import description_fields

STATIC = Path(__file__).with_name("static")


class LazyLegacy:
    """Load the old presentation/reader app only when one of its URLs is opened."""

    def __init__(self, factory, disabled=lambda: False):
        self.disabled = disabled
        self.factory = factory
        self.app = None
        self.context = None
        self.lock = asyncio.Lock()

    async def __call__(self, scope, receive, send):
        if self.disabled():
            await JSONResponse(
                {"error": "Compatibility production is disabled in playback-only mode"},
                status_code=403,
            )(scope, receive, send)
            return
        async with self.lock:
            if self.app is None:
                self.app = await run_in_threadpool(self.factory)
                self.context = self.app.router.lifespan_context(self.app)
                await self.context.__aenter__()
        if scope.get("path") == "/presentations":
            scope = dict(scope, path="/", raw_path=b"/")
        await self.app(scope, receive, send)

    async def close(self):
        if self.context:
            await self.context.__aexit__(None, None, None)


def create_app(
    root,
    *,
    repository=None,
    discovery_roots=(),
    interval=2,
    tts_config=None,
    tts_profile=None,
    tts_endpoint=None,
    legacy_factory=None,
    generation_manager=None,
    playback_only=False,
    slide_companion_service=None,
    pins=None,
    excluded=(),
):
    library = Library(
        root,
        repository=repository,
        discovery_roots=discovery_roots,
        interval=interval,
        pins=pins,
        excluded=excluded,
    )
    from .settings import ServerSettings, voice_identity

    preferences = ServerSettings(library.store.state)

    def playback_disabled():
        return playback_only or preferences.read()["playback_only"]

    listeners = ListenerState(library.store.state)
    legacy = (
        LazyLegacy(legacy_factory, disabled=playback_disabled)
        if legacy_factory and not playback_only
        else None
    )
    producer = generation_manager
    slide_service = slide_companion_service
    assets = LibraryAssets(directory=STATIC)
    catalog_cache = {}
    catalog_lock = threading.Lock()
    cloud_cache = {}
    cloud_lock = threading.Lock()

    def production():
        if playback_disabled():
            raise HTTPException(
                403,
                "Audio generation and cache clearing are disabled on this playback-only server",
            )
        return configured_production()

    def configured_production():
        nonlocal producer
        if producer is None:
            from .production import GenerationManager

            producer = GenerationManager(
                library,
                config=tts_config,
                repository=repository,
                profile=tts_profile,
                endpoint=tts_endpoint,
            )
        return producer

    def slides():
        nonlocal slide_service
        if slide_service is None:
            from .slide_companions import SlideCompanions

            slide_service = SlideCompanions(library.repository)
        return slide_service

    def require_local_action(request):
        origin = request.headers.get("origin")
        if origin and origin.rstrip("/") != str(request.base_url).rstrip("/"):
            raise HTTPException(403, "Use this library's own page for this action")

    async def document(request):
        if request.url.path == "/" and "deck" in request.query_params and legacy:
            return RedirectResponse("/presentations?" + request.url.query)
        return assets.document()

    async def favicon(request):
        return RedirectResponse("/library-assets/favicon.svg")

    def annotate(row, *, summary=False):
        words = len(row["transcript"].split())
        chronology = chronology_for(row)
        discovery = {**discovery_fields(row), **description_fields(row)}
        # Catalog cards do not need a copy of every source record and claim.
        row = deepcopy(
            {
                k: v
                for k, v in row.items()
                if k not in {"source", "transcript", "metadata", "sources"}
            }
            if summary
            else row
        )
        origin = row["origin"]
        if not summary:
            from .narration import transcript_headings

            row["transcript_headings"] = transcript_headings(
                row.get("source"), row["transcript"]
            )
        row.update(discovery)
        row.pop("chronology", None)
        if chronology:
            row["chronology"] = chronology
        if "companions" in row:
            row["companions"] = list(available_companions(row))
        for item in row.get("companions", []):
            release = (
                "source"
                if origin.get("source")
                else origin.get("pack_release", origin["release"])
            )
            item["url"] = (
                f"/api/library/companions/{release}/{quote(row['id'], safe='')}/"
                f"{quote(item['id'], safe='')}/{item['sha256']}"
            )
            item["stale"] = (
                item.get("input_spoken_sha256", row["spoken_sha256"])
                != row["spoken_sha256"]
            )
        for rec in row.get("recordings", []):
            release = rec.pop("_release", row["origin"]["release"])
            for segment in rec["segments"]:
                segment["url"] = (
                    f"/api/library/media/{segment.pop('_release')}/{segment.pop('_recording')}/{segment['index']}"
                    if segment.get("_release")
                    else (
                        f"/api/library/production/jobs/{rec['_job']}/media/{segment['index']}/{segment['sha256']}"
                        if rec.get("_job")
                        else f"/api/library/media/{release}/{rec['id']}/{segment['index']}"
                    )
                )
        row["words"] = words
        row["estimated_minutes"] = round(row["words"] / 145, 1)
        if summary:
            for recording in row.get("recordings", []):
                recording["page_count"] = len(recording.pop("pages", []))
                recording.pop("segments", None)
        return row

    def catalog(request):
        snapshot = library.snapshot(
            refresh=request.query_params.get("refresh") == "1", copy=False
        )
        key = (snapshot["generation"], tuple(snapshot["errors"]))
        etag = 'W/"' + digest(key) + '"'
        if request.headers.get("if-none-match") == etag:
            return Response(
                status_code=304, headers={"Cache-Control": "no-cache", "ETag": etag}
            )
        with catalog_lock:
            if catalog_cache.get("key") != key:
                catalog_cache["response"] = catalog_response(snapshot, etag)
                catalog_cache["key"] = key
            return catalog_cache["response"]

    async def word_cloud(request):
        from .word_cloud import cloud_data, render_svg

        params = request.query_params
        top = int(params.get("top", 60))
        if not 1 <= top <= 150:
            raise ValueError("top must be between 1 and 150")
        options = dict(
            n=int(params.get("n", 2)), rank=params.get("rank", "lectures"),
            min_lectures=int(params.get("min_lectures", 2)),
            include_common=params.get("include_common", "0") == "1",
            pack=params.get("pack") or None,
        )
        snapshot = library.snapshot(copy=False)
        key = (snapshot["generation"], tuple(options.items()))
        with cloud_lock:
            cached = cloud_cache.get(key)
        if cached is None:
            # Cache the largest selection so switching top-k does not recount
            # an entire library. Rendering a shorter SVG is inexpensive.
            cached = await run_in_threadpool(
                cloud_data, snapshot["lectures"].values(), top=150, **options
            )
            with cloud_lock:
                if any(k[0] != snapshot["generation"] for k in cloud_cache):
                    cloud_cache.clear()
                if len(cloud_cache) >= 8:
                    cloud_cache.pop(next(iter(cloud_cache)))
                cloud_cache[key] = cached
        items = cached["items"][:top]
        svg, drawn = render_svg(items)
        return JSONResponse(dict(cached, top=top, items=items, svg=svg, drawn=drawn))

    async def word_cloud_find(request):
        from .word_cloud import phrase_data

        params = request.query_params
        snapshot = library.snapshot(copy=False)
        result = await run_in_threadpool(
            phrase_data, snapshot["lectures"].values(), params.get("phrase", ""),
            pack=params.get("pack") or None, limit=15,
        )
        return JSONResponse(result)

    def catalog_response(snapshot, etag):
        collections = []
        for course in snapshot["courses"].values():
            organization = collection_metadata(course, course["id"].split(":")[0])
            collection = dict(course, **organization)
            for field in ("browse_sections", "guide_for"):
                if field not in organization:
                    collection.pop(field, None)
            collections.append(collection)
        for collection in collections:
            chronology = collection_chronology(collection, snapshot["lectures"])
            collection.pop("chronology", None)
            if chronology:
                collection["chronology"] = chronology
        items = []
        for row in snapshot["lectures"].values():
            summary = annotate(row, summary=True)
            summary.update(item_organization(row, collections))
            if row.get("metadata", {}).get("short_format_reason"):
                summary["short_format_reason"] = row["metadata"]["short_format_reason"]
            items.append(summary)
        return JSONResponse(
            {
                "generation": snapshot["generation"],
                "lectures": items,
                "courses": collections,
                "packs": snapshot["packs"],
                "errors": snapshot["errors"],
                "legacy": bool(legacy),
                "capabilities": {"learning_map": True, "learning_plan": True, "pack_export": True,
                                 "slide_companions": library.repository is not None or slide_companion_service is not None},
            },
            headers={"Cache-Control": "no-cache", "ETag": etag},
        )

    def storage(request):
        from .storage import storage_summary

        result = storage_summary(library.store)
        result["repository_root"] = str(library.repository.root) if library.repository else None
        return JSONResponse(result, headers={"Cache-Control": "no-store"})

    def learning_map(request):
        from .graph import learning_map as build_map

        return JSONResponse(build_map(library.snapshot(copy=False)), headers={"Cache-Control": "no-cache"})

    async def learning_plan(request):
        from .graph import build_learning_map
        from .learning_plan import build_learning_plan

        payload = await body(request)
        expected_generation = payload.pop("generation", None)
        if expected_generation is not None and not isinstance(expected_generation, str):
            raise ValueError("generation must identify a learning-map snapshot")
        def compute():
            graph = build_learning_map(library.snapshot(copy=False))
            if expected_generation is not None and expected_generation != graph["generation"]:
                raise Conflict("The lecture library changed. Refresh the learning map and rebuild the plan.")
            return build_learning_plan(graph, payload)
        return JSONResponse(await run_in_threadpool(compute), headers={"Cache-Control": "no-store"})

    async def learning_state(request):
        selected = request.path_params["profile"]
        if request.method == "GET":
            return JSONResponse(listeners.learning(selected), headers={"Cache-Control": "no-store"})
        require_local_action(request)
        return JSONResponse(listeners.set_learning(selected, await body(request)), headers={"Cache-Control": "no-store"})

    def slide_decks(request):
        key = qualified(request.query_params["lecture_id"])
        if key not in library.snapshot(copy=False)["lectures"]:
            raise KeyError("This lecture is not installed")
        try:
            result = slides().list_for_lecture(key)
        except KeyError:
            result = {"available": False, "items": [], "reason": "No repository slide decks are linked to this installed lecture."}
        return JSONResponse(result, headers={"Cache-Control": "no-store"})

    def slide_status(request):
        return JSONResponse(slides().status(request.path_params["deck_id"]), headers={"Cache-Control": "no-store"})

    async def slide_build(request):
        require_local_action(request)
        await body(request)
        result = await run_in_threadpool(slides().build, request.path_params["deck_id"])
        return JSONResponse(result, headers={"Cache-Control": "no-store"})

    def slide_html(request):
        path = slides().html_file(request.path_params["deck_id"])
        return FileResponse(path, media_type="text/html",
                            filename=path.name if request.query_params.get("download") == "1" else None,
                            headers={"Cache-Control": "no-store"})

    async def deployment(request):
        from .deployment import deployment_plan, browser_deployment
        from .maintenance import media_lock
        require_local_action(request)
        payload = await body(request)
        def perform():
            with media_lock(library.store.root):
                return (deployment_plan(library,payload["selection"]) if payload.get("preview",False)
                        else browser_deployment(library,payload["selection"],title=payload.get("title","Selected lecture library")))
        result = await run_in_threadpool(perform)
        if result.get("id"): result["url"] = "/api/library/exports/"+result["id"]
        return JSONResponse(result,headers={"Cache-Control":"no-store"})

    async def garbage_preview(request):
        from .garbage import garbage_plan
        return JSONResponse(await run_in_threadpool(garbage_plan,library),headers={"Cache-Control":"no-store"})

    async def pack_export(request):
        from .exports import export_pack

        require_local_action(request)
        payload = await body(request)
        result = await run_in_threadpool(export_pack, library, payload["pack_id"], source_only=payload.get("source_only", False))
        return JSONResponse(dict(result, url="/api/library/exports/" + result["id"]), status_code=201)

    def exported_pack(request):
        from .exports import export_file

        path, filename = export_file(library, request.path_params["export_id"])
        return FileResponse(path, media_type="application/zip", filename=filename)

    def references(request):
        from .references import reference_index

        lecture_id = request.query_params.get("lecture_id")
        release = request.query_params.get("release")
        snapshot = library.snapshot(copy=False)
        rows = snapshot["lectures"]
        if lecture_id:
            lecture_id = qualified(lecture_id)
            selected = [
                library.historical(release, lecture_id) if release else rows[lecture_id]
            ]
        elif request.query_params.get("course_id"):
            selected = [
                rows[key]
                for key in snapshot["courses"][
                    qualified(request.query_params["course_id"])
                ]["lectures"]
                if key in rows
            ]
        else:
            selected = list(rows.values())
        items = reference_index(selected)
        if request.url.path.endswith(".txt"):
            return PlainTextResponse(
                "References\n\n"
                + "\n\n".join(
                    json.dumps(item["source"], ensure_ascii=False, indent=2)
                    + "\nUsed by: "
                    + "; ".join(row["title"] for row in item["used_by"])
                    + ("\n" + "\n".join(item["reasons"]) if item["reasons"] else "")
                    for item in items
                )
            )
        return JSONResponse({"items": items}, headers={"Cache-Control": "no-store"})

    def lecture(request):
        key = qualified(request.path_params["lecture_id"])
        snapshot = library.snapshot(copy=False)
        key = snapshot.get("aliases", {}).get(key, key)
        if request.query_params.get("release"):
            row = library.historical(request.query_params["release"], key)
            row.setdefault("origin", {"release": request.query_params["release"]})
        else:
            row = snapshot["lectures"][key]
        return JSONResponse(annotate(row, summary=request.query_params.get("summary") == "1"), headers={"Cache-Control": "no-store"})

    def transcript(request):
        key = qualified(request.path_params["lecture_id"])
        release = request.query_params.get("release")
        row = (
            library.historical(release, key)
            if release
            else library.snapshot(copy=False)["lectures"][key]
        )
        return PlainTextResponse(row["transcript"])

    def media(request):
        path, segment = library.store.media_file(
            request.path_params["release"],
            request.path_params["recording"],
            int(request.path_params["index"]),
        )
        return FileResponse(
            path,
            media_type=segment["media_type"],
            headers={
                "Cache-Control": "private, max-age=31536000, immutable",
                "ETag": '"' + segment["sha256"] + '"',
            },
        )

    def companion(request):
        from .companions import companion_file

        params = request.path_params
        key = qualified(params["lecture_id"])
        if params["release"] == "source" and library.repository:
            path, item = library.repository.companion_file(
                key, params["identifier"], params["sha256"]
            )
        else:
            row, directory = library.store.historical(params["release"], key)
            path, item = companion_file(
                directory,
                row.get("companions", []),
                params["identifier"],
                params["sha256"],
            )
        inline = request.query_params.get("view") == "1" and item["media_type"] == "text/html"
        headers = {"Cache-Control": "no-store", "X-Content-Type-Options": "nosniff"}
        if inline:
            headers["Content-Security-Policy"] = "sandbox allow-scripts allow-modals allow-popups"
        return FileResponse(
            path,
            media_type=item["media_type"],
            filename=None if inline else path.name,
            headers=headers,
        )

    async def profiles(request):
        if request.method == "GET":
            return JSONResponse(
                {"profiles": listeners.profiles(), "aliases": listeners.aliases()}
            )
        payload = await body(request)
        return JSONResponse(listeners.create_profile(payload["name"]), status_code=201)

    async def progress(request):
        profile = request.path_params["profile"]
        if request.method == "GET":
            return JSONResponse(
                listeners.progress(profile), headers={"Cache-Control": "no-store"}
            )
        payload = await body(request)
        qualified(payload["lecture_id"])
        if payload.get("revision") is None and isinstance(payload.get("legacy"), dict):
            # The old reader retained a page index, not a content revision.
            index = payload["legacy"].get("page_index")
            if isinstance(index, bool) or not isinstance(index, int) or index < 0:
                raise ValueError("Invalid legacy page selection")
        else:
            checksum(payload["revision"])
        if payload.get("recording_id") is not None:
            checksum(payload["recording_id"])
        result = listeners.save_progress(profile, payload)
        return JSONResponse(result, status_code=409 if result.get("conflict") else 200)

    async def reactions(request):
        profile = request.path_params["profile"]
        value = (listeners.reactions(profile) if request.method == "GET"
                 else listeners.save_reaction(profile, await body(request)))
        return JSONResponse(value, headers={"Cache-Control": "no-store"})

    async def reaction_summary(request):
        return JSONResponse(listeners.reaction_summary(), headers={"Cache-Control": "no-store"})

    async def listener_transfer(request):
        if request.method == "GET":
            return JSONResponse(
                listeners.export_listener(request.path_params["profile"])
            )
        return JSONResponse(listeners.import_listener(await body(request)))

    async def listening_queue(request):
        profile = request.path_params["profile"]
        entries = (
            listeners.queue(profile)
            if request.method == "GET"
            else listeners.edit_queue(profile, await body(request))
        )
        return JSONResponse({"entries": entries}, headers={"Cache-Control": "no-store"})

    async def feedback(request):
        if request.method == "GET":
            return JSONResponse(
                listeners.export_feedback(request.query_params.get("lecture_id"))
            )
        payload = await body(request)
        text = payload.get("text")
        if not isinstance(text, str) or not text.strip() or len(text) > 10000:
            raise ValueError("Enter feedback of 1–10,000 characters")
        key, release = qualified(payload["lecture_id"]), checksum(payload["release"])
        row = library.historical(release, key)
        if payload["revision"] != row["revision"]:
            raise Conflict(
                "Feedback does not match the selected historical revision; your draft is retained"
            )
        recording = None
        context = None
        if payload.get("recording_id"):
            rec = next(
                (r for r in row["recordings"] if r["id"] == payload["recording_id"]),
                None,
            )
            if rec is None:
                raise Conflict("Unknown recording for this historical revision")
            index = payload.get("segment", 0)
            segment = next((s for s in rec["segments"] if s["index"] == index), None)
            if segment is None:
                raise Conflict("Unknown recording segment")
            seconds = finite(payload.get("seconds", 0))
            if seconds > segment["duration"] + 1:
                raise ValueError("Feedback position exceeds recording duration")
            recording = {
                "id": rec["id"],
                "variant": rec["variant"],
                "segment": index,
                "seconds": seconds,
                "sha256": segment["sha256"],
            }
            context = rec["pages"][index]
        event = dict(
            id=payload.get("id", str(uuid4())),
            type="submission",
            lecture_id=key,
            release=release,
            pack_release=row.get("origin", {}).get("pack_release", release),
            revision=row["revision"],
            spoken_sha256=row["spoken_sha256"],
            recording=recording,
            text=text.strip(),
            context=context,
            transcript_snapshot=row["transcript"],
            created_at=payload.get("created_at", utcnow()),
        )
        result = listeners.add_feedback_event(event)
        return JSONResponse(result, status_code=201)

    async def feedback_status(request):
        payload = await body(request)
        event = dict(
            id=payload.get("id", str(uuid4())),
            type="status",
            lecture_id=qualified(payload["lecture_id"]),
            feedback_id=payload["feedback_id"],
            status=payload["status"],
            addressed_revision=payload.get("addressed_revision"),
            note=payload.get("note", ""),
            created_at=payload.get("created_at", utcnow()),
        )
        return JSONResponse(listeners.add_feedback_event(event), status_code=201)

    async def feedback_import(request):
        return JSONResponse({"added": listeners.import_feedback(await body(request))})

    async def pack_change(request):
        payload = await body(request)
        if payload.get("action") == "remove":
            await run_in_threadpool(library.store.remove, payload["pack_id"])
            return JSONResponse({"removed": payload["pack_id"]})
        # Paths are local operator selections; browsers cannot invoke shell commands.
        result = await run_in_threadpool(
            library.store.install, payload["path"], expected=payload.get("expected")
        )
        return JSONResponse(result, status_code=201)

    def metadata_audit(request):
        from .metadata_audit import AuditStore, structural_hints

        rows = library.snapshot(copy=False)["lectures"]
        report = AuditStore(library.store.state).report(rows)
        report["structural_hints"] = [
            dict(lecture=key, title=rows[key]["title"], hints=hints)
            for key, hints in structural_hints(rows).items()
            if hints
        ]
        if request.url.path.endswith("/export"):
            report["findings"] = [
                item
                for item in report["findings"]
                if item["decision"] == "approved" and not item["stale"]
            ]
            return JSONResponse(
                report,
                headers={
                    "Content-Disposition": 'attachment; filename="approved-metadata-proposals.json"',
                    "Cache-Control": "no-store",
                },
            )
        return JSONResponse(report, headers={"Cache-Control": "no-store"})

    async def metadata_audit_decision(request):
        from .metadata_audit import AuditStore

        require_local_action(request)
        payload = await body(request)
        return JSONResponse(
            await run_in_threadpool(
                AuditStore(library.store.state).decide,
                checksum(request.path_params["finding_id"]),
                payload["decision"],
                library.snapshot(copy=False)["lectures"],
            )
        )

    def production_profiles(request):
        if playback_disabled():
            return JSONResponse(
                {
                    "profiles": [],
                    "tools_available": False,
                    "playback_only": True,
                    "error": "Playback-only server: existing recordings are available; generation and cache clearing are disabled.",
                }
            )
        return JSONResponse(
            production().profile_catalog(probe=request.query_params.get("probe", "1") != "0")
        )

    def production_narrators(request):
        key = qualified(request.query_params["lecture_id"])
        release = request.query_params.get("release")
        row = (
            library.historical(checksum(release), key)
            if release
            else library.snapshot(copy=False)["lectures"][key]
        )
        if playback_disabled():
            policy = preferences.read()
            return JSONResponse(
                dict(
                    default_profile=policy["default_profile"],
                    profiles=[],
                    tools_available=False,
                    playback_only=True,
                    pages=next(
                        (r["pages"] for r in row["recordings"]), [row["transcript"]]
                    ),
                    choices=[
                        dict(
                            key="recording:" + r["variant"],
                            label=r.get("label") or r["variant"],
                            recording_id=r["id"],
                            recording_complete=r["complete"],
                            **prepared_preferences(r, policy),
                        )
                        for r in row["recordings"]
                    ],
                )
            )
        return JSONResponse(
            production().saved_narrators(row)
        )

    async def production_playback(request):
        if request.method == "POST":
            payload = await body(request)
            return JSONResponse(
                await run_in_threadpool(
                    production().prioritize,
                    checksum(request.path_params["job_id"]),
                    payload["index"],
                ),
                status_code=202,
            )
        row = await run_in_threadpool(
            production().playback, checksum(request.path_params["job_id"])
        )
        return JSONResponse(
            annotate(library.remember_playback(row)),
            headers={"Cache-Control": "no-store"},
        )

    def production_media(request):
        path = production().playback_file(
            checksum(request.path_params["job_id"]),
            request.path_params["index"],
            checksum(request.path_params["sha256"]),
        )
        return FileResponse(
            path, media_type="audio/ogg" if path.suffix == ".ogg" else "audio/mpeg", headers={"Cache-Control": "no-store"}
        )

    def production_voices(request):
        return JSONResponse(
            production().voices(
                request.query_params["profile"],
                probe=request.query_params.get("probe") == "1",
            ),
            headers={"Cache-Control": "no-store"},
        )

    async def register_voice(request):
        payload = await body(request)
        return JSONResponse(
            await run_in_threadpool(
                production().register_voice,
                payload["profile"],
                payload["voice"],
                payload.get("label"),
            ),
            status_code=201,
        )

    def prepared_preferences(recording, policy):
        profile, voice = voice_identity(recording)
        selected = policy["profiles"].get(profile, {})
        quick = selected.get("quick_voices")
        return dict(
            aliases=[f"tts:{profile}:{voice}"] if profile != "prepared" else [],
            quick_select=voice in quick if quick is not None else None,
            server_default=policy["default_profile"] == profile
            and selected.get("default_voice") == voice,
        )

    def settings_document(*, probe_profile=None):
        configuration = preferences.read()
        manager = configured_production()
        configured = manager.profiles(probe=False)
        profiles = {
            row["id"]: dict(row, configured=True) for row in configured["profiles"]
        }
        voices = {}
        for key, row in profiles.items():
            voices[key] = manager.voices(key, probe=key == probe_profile)
        for row in library.snapshot(copy=False)["lectures"].values():
            for recording in row["recordings"]:
                key, voice = voice_identity(recording)
                if key not in profiles:
                    profiles[key] = dict(
                        id=key,
                        label=key if key != "prepared" else "Prepared recordings",
                        configured=False,
                        voice=voice,
                        model=recording.get("generator", {}).get("model"),
                        output_format=recording.get("generator", {}).get(
                            "output_format"
                        ),
                    )
                    voices[key] = dict(voices=[], registered=[], default_voice=voice)
                if voice not in voices[key]["voices"]:
                    voices[key]["voices"].append(voice)
                if (
                    not profiles[key]["configured"]
                    and recording.get("label")
                    and not any(
                        item["voice"] == voice for item in voices[key]["registered"]
                    )
                ):
                    voices[key]["registered"].append(
                        dict(voice=voice, label=recording["label"])
                    )
        return dict(
            configuration=configuration,
            revision=digest(configuration),
            playback_only=playback_disabled(),
            playback_locked=bool(playback_only),
            profiles=list(profiles.values()),
            voices=voices,
            tools_available=configured["tools_available"],
        )

    async def server_settings(request):
        if request.method == "GET":
            return JSONResponse(await run_in_threadpool(settings_document))
        require_local_action(request)
        payload = await body(request)
        document = payload["configuration"]
        # Validate before applying any runtime effects.
        current = await run_in_threadpool(settings_document)
        ServerSettings.validate(document)
        if playback_only and not document.get("playback_only"):
            raise ValueError(
                "Playback-only mode was set at startup; restart without that flag to enable generation"
            )
        available = current["voices"]
        if (
            document.get("default_profile") is not None
            and document["default_profile"] not in available
        ):
            raise ValueError("Select an available profile")
        for profile, policy in document.get("profiles", {}).items():
            if profile not in available:
                if policy == current["configuration"]["profiles"].get(profile):
                    continue
                raise ValueError("Unknown voice profile")
            if not isinstance(policy, dict):
                raise ValueError("Invalid voice preferences")
            known = available[profile]["voices"]
            if (
                policy.get("default_voice") is not None
                and policy["default_voice"] not in known
            ):
                raise ValueError("Select an available default voice")
            if policy.get("quick_voices") is not None and (
                not isinstance(policy["quick_voices"], list)
                or any(v not in known for v in policy["quick_voices"])
            ):
                raise ValueError("Select available quick-select voices")
        await run_in_threadpool(
            preferences.save, document, expected=payload["revision"]
        )
        if (
            playback_disabled()
            and not current["playback_only"]
            and producer is not None
        ):
            for job in producer.list():
                if job["state"] in {"queued", "running"}:
                    await run_in_threadpool(producer.cancel, job["id"])
        elif not playback_disabled():
            # Resuming configured serving makes durable queued work eligible again.
            await run_in_threadpool(configured_production().tick)
        return JSONResponse(await run_in_threadpool(settings_document))

    async def settings_voices(request):
        require_local_action(request)
        payload = await body(request)
        profile = payload["profile"]
        manager = configured_production()
        if not any(row["id"] == profile for row in manager.profiles()["profiles"]):
            raise ValueError("Select a configured TTS profile")
        if "voice" in payload:
            await run_in_threadpool(
                manager.register_voice, profile, payload["voice"], payload.get("label")
            )
        return JSONResponse(
            await run_in_threadpool(
                settings_document,
                probe_profile=profile if payload.get("refresh") else None,
            )
        )

    def voice_profile_catalog(request):
        return JSONResponse(
            configured_production().profile_catalog(
                include_archived=request.query_params.get("archived") == "1"
            ),
            headers={"Cache-Control": "no-store"},
        )

    def voice_profile_editor(request):
        return JSONResponse(
            configured_production().profile_editor(request.path_params["profile_id"]),
            headers={"Cache-Control": "no-store"},
        )

    async def voice_profile_template(request):
        require_local_action(request)
        return JSONResponse(
            await run_in_threadpool(
                configured_production().save_profile,
                await body(request),
                template_only=True,
            )
        )

    async def voice_profile_preview(request):
        require_local_action(request)
        return JSONResponse(
            await run_in_threadpool(production().preview_profile, await body(request))
        )

    def voice_profile_preview_audio(request):
        token = request.path_params["token"]
        if not re.fullmatch(r"[a-f0-9]{32}", token):
            raise KeyError("Unknown preview")
        folder = library.store.root / "build-cache" / "profile-previews" / token
        path = next(
            (
                p
                for p in [folder / "preview.ogg", folder / "preview.mp3"]
                if p.is_file()
            ),
            None,
        )
        if path is None:
            raise KeyError("Unknown preview")
        return FileResponse(
            path, media_type="audio/ogg" if path.suffix == ".ogg" else "audio/mpeg"
        )

    async def voice_profile_save(request):
        require_local_action(request)
        payload = await body(request)
        return JSONResponse(
            await run_in_threadpool(configured_production().save_profile, payload),
            status_code=201,
        )

    async def voice_profile_action(request):
        require_local_action(request)
        payload = await body(request)
        manager = configured_production()
        manager.sync_saved_profiles()
        store = manager.saved_profile_store()
        key = request.path_params["profile_id"]
        if payload.get("action") == "default":
            store.set_default(key)
        elif payload.get("action") == "pin":
            store.set_presentation(key, quick=payload.get("quick"))
        elif payload.get("action") == "rename":
            store.set_presentation(key, label=payload.get("label"))
        elif payload.get("action") in {"archive", "restore"}:
            store.archive(key, payload["action"] == "archive")
        else:
            raise ValueError("Choose default, archive or restore")
        return JSONResponse(manager.profile_catalog())

    async def voice_profile_voices(request):
        manager = configured_production()
        key = request.path_params["backend_id"]
        if request.method == "POST":
            require_local_action(request)
            payload = await body(request)
            manager.sync_saved_profiles()
            backend = next(
                (
                    b
                    for b in manager.saved_profile_store().backends()
                    if b["id"] == key and b["available"]
                ),
                None,
            )
            if backend is None:
                raise ValueError("Backend unavailable")
            if payload.get("voice") is not None:
                manager.register_voice(
                    backend["anchor"], payload["voice"], payload.get("label")
                )
            return JSONResponse(
                await run_in_threadpool(
                    manager.profile_backend_voices,
                    key,
                    probe=bool(payload.get("refresh")),
                )
            )
        return JSONResponse(
            await run_in_threadpool(manager.profile_backend_voices, key)
        )

    async def voice_reference_record(request):
        require_local_action(request)
        manager = production()
        # Bound the actual stream, including requests without Content-Length.
        raw = bytearray()
        async for chunk in request.stream():
            if len(raw) + len(chunk) > 6 * 1024**2:
                raise HTTPException(413, "Recording upload too large")
            raw.extend(chunk)
        try:
            payload = json.loads(raw)
        except (ValueError, UnicodeDecodeError):
            raise ValueError("Expected a recording upload") from None
        if not isinstance(payload, dict):
            raise ValueError("Expected a recording upload")
        return JSONResponse(await run_in_threadpool(
            manager.save_voice_reference, request.path_params["backend_id"], payload,
        ), status_code=201, headers={"Cache-Control": "no-store"})

    async def clear_voice_cache(request):
        require_local_action(request)
        manager = production()
        payload = await body(request)
        if payload.get("profile_revision"):
            return JSONResponse(
                await run_in_threadpool(
                    manager.clear_saved_cache,
                    qualified(payload["lecture_id"]),
                    payload["profile"],
                    revision=payload["revision"],
                    profile_revision=payload["profile_revision"],
                )
            )
        return JSONResponse(
            await run_in_threadpool(
                manager.clear_voice_cache,
                qualified(payload["lecture_id"]),
                payload["profile"],
                payload.get("voice"),
                revision=payload["revision"],
            )
        )

    async def prepare(request):
        require_local_action(request)
        payload = await body(request)
        if isinstance(payload.get("profile"), str) and payload["profile"].startswith(
            "voice-"
        ):
            manager = production()
            manager.sync_saved_profiles()
            profile = manager.saved_profile_store().get(
                payload["profile"], payload.get("profile_revision")
            )
            if (
                payload.get("voice") not in (None, profile["recipe"]["config"]["voice"])
                or payload.get("speed", 1) != 1
            ):
                raise ValueError(
                    "A saved profile has a fixed voice, speaking rate and tempo; edit or duplicate the profile"
                )
            if payload.get("base_recording_id"):
                raise ValueError(
                    "Legacy recordings cannot be extended as a new recipe revision"
                )
            selection = payload.get("lecture_ids")
            if payload.get("course_id"):
                snapshot = library.snapshot(copy=False)
                selection = [
                    key
                    for key in snapshot["courses"][qualified(payload["course_id"])][
                        "lectures"
                    ]
                    if snapshot["lectures"][key].get("kind") == "audio"
                ]
            single = selection is None
            if single:
                selection = [qualified(payload["lecture_id"])]
            if not isinstance(selection, list):
                raise ValueError("Select a lecture list")
            if not single and payload.get("blocks") is not None:
                raise ValueError("Choose blocks within one lecture")
            if (
                single
                and payload.get("revision")
                and library.snapshot(copy=False)["lectures"][selection[0]]["revision"]
                != payload["revision"]
            ):
                raise Conflict("This lecture changed; reopen it before generation")
            jobs = await run_in_threadpool(
                manager.prepare_saved,
                [qualified(key) for key in selection],
                payload["profile"],
                profile_revision=profile["revision"],
                blocks=payload.get("blocks"),
            )
            return JSONResponse(jobs[0] if single else {"jobs": jobs}, status_code=202)
        if payload.get("course_id") or payload.get("lecture_ids"):
            if payload.get("blocks") is not None or payload.get("base_recording_id"):
                raise ValueError("Select blocks within one lecture")
            selection = payload.get("lecture_ids", [])
            if payload.get("course_id"):
                snapshot = library.snapshot(copy=False)
                selection = snapshot["courses"][qualified(payload["course_id"])][
                    "lectures"
                ]
                selection = [
                    key
                    for key in selection
                    if key in snapshot["lectures"]
                    and snapshot["lectures"][key].get("kind") == "audio"
                ]
            if not isinstance(selection, list):
                raise ValueError("Select a list of lectures or one course")
            result = await run_in_threadpool(
                production().prepare_many,
                [qualified(key) for key in selection],
                payload["profile"],
                voice=payload.get("voice"),
                speed=payload.get("speed", 1),
            )
            return JSONResponse({"jobs": result}, status_code=202)
        if (
            payload.get("revision")
            and library.snapshot(copy=False)["lectures"][
                qualified(payload["lecture_id"])
            ]["revision"]
            != payload["revision"]
        ):
            raise Conflict(
                "This lecture has changed; open its current revision before generating audio."
            )
        result = await run_in_threadpool(
            production().prepare,
            qualified(payload["lecture_id"]),
            payload["profile"],
            voice=payload.get("voice"),
            speed=payload.get("speed", 1),
            **({"blocks": payload["blocks"]} if "blocks" in payload else {}),
            **(
                {"base_recording_id": payload["base_recording_id"]}
                if payload.get("base_recording_id")
                else {}
            ),
        )
        return JSONResponse(result, status_code=202)

    async def job(request):
        if request.method == "DELETE":
            return JSONResponse(
                await run_in_threadpool(
                    production().cancel, request.path_params["job_id"]
                )
            )
        return JSONResponse(
            await run_in_threadpool(production().status, request.path_params["job_id"])
        )

    def jobs(request):
        if playback_disabled():
            return JSONResponse({"jobs": []})
        lecture_id = request.query_params.get("lecture_id")
        return JSONResponse(
            {"jobs": production().list(qualified(lecture_id) if lecture_id else None)}
        )

    async def retry_job(request):
        return JSONResponse(
            await run_in_threadpool(production().retry, request.path_params["job_id"]),
            status_code=202,
        )

    async def body(request):
        raw = await request.body()
        if len(raw) > 8 * 1024**2:
            raise HTTPException(413, "Request too large")
        try:
            payload = await request.json()
        except (ValueError, UnicodeDecodeError):
            raise HTTPException(400, "Expected JSON")
        if not isinstance(payload, dict):
            raise ValueError("Expected a JSON object")
        return payload

    async def error(request, exc):
        code = (
            503
            if isinstance(exc, SlideCompanionsUnavailable)
            else
            409
            if isinstance(exc, Conflict)
            else (
                404
                if isinstance(exc, (KeyError, FileNotFoundError, StopIteration))
                else 400
            )
        )
        return JSONResponse({"error": str(exc)}, status_code=code)

    async def reconcile():
        while True:
            try:
                await run_in_threadpool(library.store.reconcile)
                if producer is not None and not playback_disabled():
                    await run_in_threadpool(producer.tick)
            except (OSError, ValueError) as exc:
                library.store.errors = [str(exc)]
            await asyncio.sleep(max(0.05, interval))

    @asynccontextmanager
    async def lifespan(app):
        from .maintenance import media_lock
        with media_lock(library.store.root):
            # Inspect durable intent without importing renderers for an ordinary reader.
            if (
                not playback_disabled()
                and (library.store.state / "production.sqlite3").exists()
            ):
                from .jobs import JobStore

                if any(
                    record["state"] in {"queued", "running"}
                    for record in JobStore(library.store.state).list()
                ):
                    production()
            task = asyncio.create_task(reconcile())
            try:
                yield
            finally:
                task.cancel()
                try:
                    await task
                except asyncio.CancelledError:
                    pass
                if producer is not None:
                    await run_in_threadpool(producer.close)
                if legacy:
                    await legacy.close()

    routes = [
        Route(path, document)
        for path in [
            "/",
            "/courses",
            "/courses/{course_id}",
            "/collections",
            "/collections/{collection_id}",
            "/lectures",
            "/lectures/{namespace}/{local_id}",
            "/listening",
            "/packs",
            "/stats",
            "/word-cloud",
            "/feedback",
            "/references",
            "/learning-map",
            "/learning-plan",
            "/production",
            "/settings",
            "/topic-graph",
            "/metadata-audit",
        ]
    ]
    routes += [
        Route("/favicon.ico", favicon),
        Route("/api/library/catalog", catalog),
        Route("/api/library/word-cloud", word_cloud),
        Route("/api/library/word-cloud/find", word_cloud_find),
        Route("/api/library/storage", storage),
        Route("/api/library/deployment", deployment, methods=["POST"]),
        Route("/api/library/storage/gc", garbage_preview),
        Route("/api/library/learning-map", learning_map),
        Route("/api/library/learning-plan", learning_plan, methods=["POST"]),
        Route(
            "/api/listeners/{profile}/learning", learning_state, methods=["GET", "POST"]
        ),
        Route("/api/library/slide-decks", slide_decks),
        Route(
            "/api/library/slide-decks/{deck_id}/build", slide_build, methods=["POST"]
        ),
        Route("/api/library/slide-decks/{deck_id}/html", slide_html),
        Route("/api/library/slide-decks/{deck_id}", slide_status),
        Route("/api/library/exports", pack_export, methods=["POST"]),
        Route("/api/library/exports/{export_id}", exported_pack),
        Route("/api/library/references", references),
        Route("/api/library/references.txt", references),
        Route("/api/library/lectures/{lecture_id}/transcript.txt", transcript),
        Route("/api/library/lectures/{lecture_id}", lecture),
        Route("/api/library/media/{release}/{recording}/{index:int}", media),
        Route(
            "/api/library/companions/{release}/{lecture_id}/{identifier}/{sha256}",
            companion,
        ),
        Route("/api/listeners", profiles, methods=["GET", "POST"]),
        Route("/api/listeners/import", listener_transfer, methods=["POST"]),
        Route("/api/listeners/{profile}/export", listener_transfer),
        Route("/api/listeners/{profile}/progress", progress, methods=["GET", "POST"]),
        Route(
            "/api/listeners/{profile}/queue", listening_queue, methods=["GET", "POST"]
        ),
        Route("/api/listeners/{profile}/reactions", reactions, methods=["GET", "POST"]),
        Route("/api/library/reactions", reaction_summary),
        Route("/api/library/feedback", feedback, methods=["GET", "POST"]),
        Route("/api/library/feedback/status", feedback_status, methods=["POST"]),
        Route("/api/library/feedback/import", feedback_import, methods=["POST"]),
        Route("/api/library/packs", pack_change, methods=["POST"]),
        Route("/api/library/metadata-audit", metadata_audit),
        Route("/api/library/metadata-audit/export", metadata_audit),
        Route(
            "/api/library/metadata-audit/{finding_id}",
            metadata_audit_decision,
            methods=["POST"],
        ),
        Route("/api/library/voice-profiles",voice_profile_catalog),
        Route("/api/library/voice-profiles/template",voice_profile_template,methods=["POST"]),
        Route("/api/library/voice-profiles/preview",voice_profile_preview,methods=["POST"]),
        Route("/api/library/voice-profiles/preview/{token}",voice_profile_preview_audio),
        Route("/api/library/voice-profiles/save",voice_profile_save,methods=["POST"]),
        Route("/api/library/voice-profiles/backends/{backend_id}/voices",voice_profile_voices,methods=["GET","POST"]),
        Route("/api/library/voice-profiles/backends/{backend_id}/references",voice_reference_record,methods=["POST"]),
        Route("/api/library/voice-profiles/{profile_id}/action",voice_profile_action,methods=["POST"]),
        Route("/api/library/voice-profiles/{profile_id}",voice_profile_editor),
        Route("/api/library/settings", server_settings, methods=["GET", "POST"]),
        Route("/api/library/settings/voices", settings_voices, methods=["POST"]),
        Route("/api/library/production", production_profiles),
        Route("/api/library/production/narrators", production_narrators),
        Route("/api/library/production/voices", production_voices),
        Route(
            "/api/library/production/voices/register", register_voice, methods=["POST"]
        ),
        Route(
            "/api/library/production/clear-cache", clear_voice_cache, methods=["POST"]
        ),
        Route("/api/library/production/prepare", prepare, methods=["POST"]),
        Route("/api/library/production/jobs", jobs),
        Route(
            "/api/library/production/jobs/{job_id}/playback",
            production_playback,
            methods=["GET", "POST"],
        ),
        Route(
            "/api/library/production/jobs/{job_id}/media/{index:int}/{sha256}",
            production_media,
        ),
        Route(
            "/api/library/production/jobs/{job_id}/retry", retry_job, methods=["POST"]
        ),
        Route("/api/library/production/jobs/{job_id}", job, methods=["GET", "DELETE"]),
        Mount("/library-assets", assets),
    ]
    if legacy:
        routes.append(Mount("/", legacy))
    app = Starlette(
        routes=routes,
        lifespan=lifespan,
        exception_handlers={
            ValueError: error,
            KeyError: error,
            FileNotFoundError: error,
            StopIteration: error,
            SlideCompanionsUnavailable: error,
        },
    )
    app.state.library = library
    app.state.listeners = listeners
    return app
