"""Serve and transfer independent lecture packs without a shared registry."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
import time
import tomllib

from .core import read_json, write_json
from .packs import PackStore, archive_release, export_release, load_release


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--library",
        type=Path,
        default=Path("library-data"),
        help="durable local packs and listener state",
    )
    commands = parser.add_subparsers(dest="command", required=True)
    serve = commands.add_parser("serve")
    serve.add_argument(
        "--repository", type=Path, help="also discover existing authored tracks"
    )
    serve.add_argument(
        "--config",
        type=Path,
        help="library.toml with pack_roots and optional tts_config",
    )
    serve.add_argument("--pack-root", action="append", type=Path, default=[])
    serve.add_argument("--poll-interval", type=float, default=2)
    serve.add_argument("--host", default="127.0.0.1")
    serve.add_argument("--port", type=int, default=8001)
    serve.add_argument("--tts-config", type=Path)
    serve.add_argument("--audio-tts-profile")
    serve.add_argument("--audio-tts-endpoint")
    export = commands.add_parser("export")
    export.add_argument("--repository", type=Path)
    export.add_argument("--pack", required=True)
    export.add_argument("--output", type=Path, required=True)
    export.add_argument("--parent")
    export.add_argument("--zip", type=Path)
    export.add_argument(
        "--audio-profile", help="explicitly import matching existing legacy cache pages"
    )
    export.add_argument("--voice")
    export.add_argument("--variant", default="narrator-a-v1")
    export.add_argument("--tts-config", type=Path)
    export.add_argument("--allow-partial", action="store_true")
    export.add_argument(
        "--source-only",
        action="store_true",
        help="omit installed media from this export",
    )
    prepare = commands.add_parser("prepare")
    prepare.add_argument("--repository", type=Path)
    prepare.add_argument("--lecture", action="append", default=[])
    prepare.add_argument("--course")
    prepare.add_argument("--profile", required=True)
    prepare.add_argument("--voice")
    prepare.add_argument("--speed", type=float, default=1)
    prepare.add_argument("--tts-config", type=Path)
    install = commands.add_parser("install")
    install.add_argument("path", type=Path)
    install.add_argument(
        "--expected", help="active release that this update is based on"
    )
    remove = commands.add_parser("remove")
    remove.add_argument("pack_id")
    validate = commands.add_parser("validate")
    validate.add_argument("path", type=Path)
    commands.add_parser("list")
    commands.add_parser("storage")
    backup = commands.add_parser("backup")
    backup.add_argument("output", type=Path)
    restore = commands.add_parser("restore")
    restore.add_argument("path", type=Path)
    feedback_export = commands.add_parser("feedback-export")
    feedback_export.add_argument("output", type=Path)
    feedback_export.add_argument("--lecture")
    feedback_import = commands.add_parser("feedback-import")
    feedback_import.add_argument("path", type=Path)
    args = parser.parse_args(argv)
    repository = getattr(args, "repository", None)
    if repository is None and (Path.cwd() / "draft-stages").is_dir():
        repository = Path.cwd()
    try:
        if args.command == "serve":
            import uvicorn
            from .web import create_app

            config = {}
            if args.config:
                config = tomllib.loads(args.config.read_text())
            config_base = args.config.resolve().parent if args.config else Path.cwd()
            roots = [
                config_base / p for p in config.get("pack_roots", [])
            ] + args.pack_root
            tts_config = args.tts_config or (
                config_base / config["tts_config"] if config.get("tts_config") else None
            )
            legacy_factory = None
            if repository and (repository / "dkvis").is_dir():

                def legacy_factory():
                    from dkvis.presentation.serve import create_app as legacy_app

                    return legacy_app(
                        repository / "renders",
                        audio_tts_profile=args.audio_tts_profile,
                        audio_tts_endpoint=args.audio_tts_endpoint,
                        audio_tts_config=tts_config,
                    )

            app = create_app(
                args.library,
                repository=repository,
                discovery_roots=roots,
                interval=args.poll_interval,
                tts_config=tts_config,
                tts_profile=args.audio_tts_profile,
                tts_endpoint=args.audio_tts_endpoint,
                pins=config.get("pins"),
                excluded=config.get("excluded", []),
                legacy_factory=legacy_factory,
            )
            print(f"AI Lectures: http://{args.host}:{args.port}/", flush=True)
            uvicorn.run(app, host=args.host, port=args.port)
        elif args.command == "prepare":
            from .library import Library
            from .production import GenerationManager

            library = Library(args.library, repository=repository)
            snapshot = library.snapshot()
            selection = list(args.lecture)
            if args.course:
                selection.extend(snapshot["courses"][args.course]["lectures"])
            if not selection:
                raise ValueError("Select --lecture or --course")
            manager = GenerationManager(
                library, config=args.tts_config, repository=repository
            )
            try:
                requested = manager.prepare_many(
                    selection, args.profile, voice=args.voice, speed=args.speed
                )
                for job in requested:
                    lecture_id = job["lecture_id"]
                    previous = None
                    while not job["published"]:
                        inventory = job["inventory"]
                        state = (inventory["ready"], inventory["total"], job["state"])
                        if state != previous:
                            print(
                                f"{lecture_id}: {state[0]}/{state[1]} passages ready · {job['state']}",
                                flush=True,
                            )
                            previous = state
                        if job["state"] in {"failed", "cancelled", "settings_changed"}:
                            raise ValueError(
                                f'{lecture_id}: preparation {job["state"]}: {job.get("error") or ""}; rerun to reuse completed pages'
                            )
                        time.sleep(0.5)
                        job = manager.status(job["id"])
                    print(f'{lecture_id}: published {job["published"]}', flush=True)
            finally:
                manager.close()
        elif args.command == "backup":
            from .storage import backup_library

            print(
                json.dumps(
                    backup_library(PackStore(args.library), args.output), indent=2
                )
            )
        elif args.command == "restore":
            from .storage import restore_library

            print(restore_library(args.path, args.library))
        elif args.command == "storage":
            from .storage import storage_summary

            print(json.dumps(storage_summary(PackStore(args.library)), indent=2))
        elif args.command == "validate":
            print(json.dumps(load_release(args.path)["manifest"], indent=2))
        elif args.command == "install":
            print(
                json.dumps(
                    PackStore(args.library).install(args.path, expected=args.expected),
                    indent=2,
                )
            )
        elif args.command == "remove":
            PackStore(args.library).remove(args.pack_id)
        elif args.command == "list":
            snapshot = PackStore(args.library).snapshot()
            print(
                json.dumps(
                    {"packs": snapshot["packs"], "lectures": len(snapshot["lectures"])},
                    indent=2,
                )
            )
        elif args.command == "export":
            media = []
            pack = None
            export_options = {"parent": args.parent}
            if repository:
                from .catalog import RepositoryCatalog

                pack = RepositoryCatalog(repository).snapshot().get(args.pack)
                if pack and not args.source_only and not args.audio_profile:
                    from .library import Library

                    library = Library(args.library, repository=repository)
                    snapshot = library.snapshot()
                    for key in pack["lectures"]:
                        for recording in snapshot["lectures"][key]["recordings"]:
                            public_record = {
                                k: v for k, v in recording.items() if k != "_release"
                            }
                            files = {
                                s["path"]: library.store.media_file(
                                    recording["_release"], recording["id"], s["index"]
                                )[0]
                                for s in recording["segments"]
                            }
                            media.append((key, public_record, files))
            if pack is None:
                store = PackStore(args.library)
                selected = next(r for r in store.active() if r["pack_id"] == args.pack)
                catalog = json.loads(selected["catalog"])
                original = load_release(selected["directory"])
                original_manifest = original["manifest"]
                pack = dict(id=args.pack, title=original_manifest["title"], **catalog)
                export_options = {
                    "parent": (
                        args.parent
                        if args.parent is not None
                        else original_manifest.get("parent")
                    ),
                    "kind": original_manifest.get("kind", "source"),
                    "dependencies": original_manifest.get("dependencies", {}),
                }
                media_paths = {
                    s["path"]
                    for row in catalog["lectures"].values()
                    for rec in row["recordings"]
                    for s in rec["segments"]
                }
                pack["extra_files"] = {
                    path: (Path(selected["directory"]) / path).read_bytes()
                    for path in original["checksums"]
                    if path != "catalog.json" and path not in media_paths
                }
                for key, row in (
                    pack["lectures"].items() if not args.source_only else []
                ):
                    for recording in row["recordings"]:
                        media.append(
                            (
                                key,
                                recording,
                                {
                                    s["path"]: Path(selected["directory"]) / s["path"]
                                    for s in recording["segments"]
                                },
                            )
                        )
            if args.audio_profile:
                if args.source_only:
                    raise ValueError(
                        "--source-only and --audio-profile cannot be combined"
                    )
                if not repository:
                    raise ValueError("Legacy audio import requires --repository")
                from dkvis.presentation.audio_library import AudioLectureLibrary
                from .production import recording_from_engine

                directory = (
                    repository
                    / "draft-stages"
                    / (
                        "tts-lectures"
                        if args.pack == "g2"
                        else "tts-paper" if args.pack == "g3" else "tts-" + args.pack
                    )
                )
                cache = repository / "audio-cache"
                engine = AudioLectureLibrary(
                    sources=directory,
                    cache=cache if args.pack == "g2" else cache / args.pack,
                    profile=args.audio_profile,
                    config=args.tts_config,
                )
                try:
                    for key, row in pack["lectures"].items():
                        rec, files = recording_from_engine(
                            engine,
                            key.split(":")[1],
                            row,
                            variant=args.variant,
                            voice=args.voice,
                        )
                        if rec["segments"] and (rec["complete"] or args.allow_partial):
                            media.append((key, rec, files))
                finally:
                    engine.close()
            manifest = export_release(pack, args.output, media=media, **export_options)
            if args.zip:
                archive_release(args.output, args.zip)
            print(json.dumps(manifest, indent=2))
        else:
            from .state import ListenerState

            state = ListenerState(args.library / "state")
            if args.command == "feedback-export":
                write_json(args.output, state.export_feedback(args.lecture))
            elif args.command == "feedback-import":
                print(state.import_feedback(read_json(args.path)))
    except (ValueError, OSError, KeyError, StopIteration) as exc:
        parser.exit(1, f"{exc}\n")


if __name__ == "__main__":
    main()
