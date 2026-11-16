"""One local server: live packs, playback, optional synthesis, and open profiles."""

from __future__ import annotations

import asyncio
import json
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
)
from starlette.routing import Mount, Route

from .core import Conflict, checksum, finite, qualified
from .library import Library
from .state import ListenerState, utcnow
from .organization import collection_metadata, item_organization
from .companions import available_companions
from .assets import LibraryAssets

STATIC = Path(__file__).with_name("static")


class LazyLegacy:
    """Load the old presentation/reader app only when one of its URLs is opened."""

    def __init__(self, factory):
        self.factory = factory
        self.app = None
        self.context = None
        self.lock = asyncio.Lock()

    async def __call__(self, scope, receive, send):
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
    listeners = ListenerState(library.store.state)
    legacy = LazyLegacy(legacy_factory) if legacy_factory else None
    producer = generation_manager
    assets = LibraryAssets(directory=STATIC)

    def production():
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

    async def document(request):
        if request.url.path == "/" and "deck" in request.query_params and legacy:
            return RedirectResponse("/presentations?" + request.url.query)
        return assets.document()

    def annotate(row):
        row = deepcopy(row)
        origin = row["origin"]
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
                    f"/api/library/production/jobs/{rec['_job']}/media/{segment['index']}/{segment['sha256']}"
                    if rec.get("_job")
                    else f"/api/library/media/{release}/{rec['id']}/{segment['index']}"
                )
        row["words"] = len(row["transcript"].split())
        row["estimated_minutes"] = round(row["words"] / 145, 1)
        return row

    def catalog(request):
        snapshot = library.snapshot(refresh=request.query_params.get("refresh") == "1")
        collections = [
            dict(course, **collection_metadata(course, course["id"].split(":")[0]))
            for course in snapshot["courses"].values()
        ]
        items = []
        for row in snapshot["lectures"].values():
            summary = annotate(row)
            summary.update(item_organization(row, collections))
            for key in ("source", "transcript", "metadata", "sources"):
                summary.pop(key, None)
            for rec in summary.get("recordings", []):
                rec["page_count"] = len(rec.pop("pages"))
                rec.pop("segments", None)
            items.append(summary)
        return JSONResponse(
            {
                "generation": snapshot["generation"],
                "lectures": items,
                "courses": collections,
                "packs": snapshot["packs"],
                "errors": snapshot["errors"],
                "legacy": bool(legacy),
            },
            headers={"Cache-Control": "no-store"},
        )

    def storage(request):
        from .storage import storage_summary

        return JSONResponse(
            storage_summary(library.store), headers={"Cache-Control": "no-store"}
        )

    def references(request):
        from .references import reference_index

        lecture_id = request.query_params.get("lecture_id")
        release = request.query_params.get("release")
        snapshot = library.snapshot()
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
        snapshot = library.snapshot()
        key = snapshot.get("aliases", {}).get(key, key)
        if request.query_params.get("release"):
            row = library.historical(request.query_params["release"], key)
            row.setdefault("origin", {"release": request.query_params["release"]})
        else:
            row = library.snapshot()["lectures"][key]
        return JSONResponse(annotate(row), headers={"Cache-Control": "no-store"})

    def transcript(request):
        key = qualified(request.path_params["lecture_id"])
        release = request.query_params.get("release")
        row = (
            library.historical(release, key)
            if release
            else library.snapshot()["lectures"][key]
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
        return FileResponse(
            path,
            media_type=item["media_type"],
            filename=path.name,
            headers={"Cache-Control": "no-store", "X-Content-Type-Options": "nosniff"},
        )

    async def profiles(request):
        if request.method == "GET":
            return JSONResponse({"profiles": listeners.profiles()})
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

    def production_profiles(request):
        return JSONResponse(
            production().profiles(probe=request.query_params.get("probe", "1") != "0")
        )

    def production_narrators(request):
        key = qualified(request.query_params["lecture_id"])
        release = request.query_params.get("release")
        row = (
            library.historical(checksum(release), key)
            if release
            else library.snapshot()["lectures"][key]
        )
        return JSONResponse(
            production().narrators(
                row, speed=float(request.query_params.get("speed", 1))
            )
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
            path, media_type="audio/mpeg", headers={"Cache-Control": "no-store"}
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

    async def prepare(request):
        payload = await body(request)
        if payload.get("course_id") or payload.get("lecture_ids"):
            selection = payload.get("lecture_ids", [])
            if payload.get("course_id"):
                snapshot = library.snapshot()
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
            and library.snapshot()["lectures"][qualified(payload["lecture_id"])][
                "revision"
            ]
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
        return JSONResponse({"jobs": production().list()})

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
                if producer is not None:
                    await run_in_threadpool(producer.tick)
            except (OSError, ValueError) as exc:
                library.store.errors = [str(exc)]
            await asyncio.sleep(max(0.05, interval))

    @asynccontextmanager
    async def lifespan(app):
        # Inspect durable intent without importing renderers for an ordinary reader.
        if (library.store.state / "production.sqlite3").exists():
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
            "/lectures/{namespace}/{local_id}",
            "/listening",
            "/packs",
            "/feedback",
            "/references",
            "/production",
        ]
    ]
    routes += [
        Route("/api/library/catalog", catalog),
        Route("/api/library/storage", storage),
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
        Route("/api/library/feedback", feedback, methods=["GET", "POST"]),
        Route("/api/library/feedback/status", feedback_status, methods=["POST"]),
        Route("/api/library/feedback/import", feedback_import, methods=["POST"]),
        Route("/api/library/packs", pack_change, methods=["POST"]),
        Route("/api/library/production", production_profiles),
        Route("/api/library/production/narrators", production_narrators),
        Route("/api/library/production/voices", production_voices),
        Route(
            "/api/library/production/voices/register", register_voice, methods=["POST"]
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
        },
    )
    app.state.library = library
    app.state.listeners = listeners
    return app
