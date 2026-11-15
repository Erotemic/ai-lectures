"""On-demand storage accounting and explicit, portable library backups."""

from __future__ import annotations

import json
import os
from pathlib import Path
import shutil
import sqlite3
import stat
import tempfile
from zipfile import ZipFile, ZIP_DEFLATED

from .core import contained, read_json, relative, write_json


def tree_bytes(root):
    total = 0
    for path in Path(root).rglob("*"):
        try:
            if path.is_file() and not path.is_symlink():
                total += path.stat().st_size
        except OSError:
            pass  # A live cache can change during an accounting request.
    return total


def storage_summary(store):
    with store.connect() as db:
        rows = db.execute(
            "SELECT r.*,s.enabled,s.release AS selected FROM releases r LEFT JOIN selections s ON r.pack_id=s.pack_id ORDER BY r.pack_id,r.release"
        ).fetchall()
    releases = []
    for row in rows:
        directory = store.packs / row["pack_id"] / row["release"]
        catalog, manifest = json.loads(row["catalog"]), json.loads(row["manifest"])
        lectures = list(catalog["lectures"].values())
        recordings = [
            recording
            for lecture in lectures
            for recording in lecture.get("recordings", [])
        ]
        releases.append(
            dict(
                pack_id=row["pack_id"],
                release=row["release"],
                title=manifest["title"],
                active=bool(row["enabled"] and row["selected"] == row["release"]),
                available=directory.is_dir(),
                bytes=tree_bytes(directory),
                lectures=len(lectures),
                ready=sum(
                    any(r["complete"] for r in lecture.get("recordings", []))
                    for lecture in lectures
                ),
                narrators=len({r["variant"] for r in recordings}),
                complete_recordings=sum(r["complete"] for r in recordings),
                partial_recordings=sum(not r["complete"] for r in recordings),
                recorded_seconds=sum(
                    segment["duration"] for r in recordings for segment in r["segments"]
                ),
            )
        )
    packs_bytes = tree_bytes(store.packs)
    active = sum(row["bytes"] for row in releases if row["active"])
    retained = sum(row["bytes"] for row in releases if not row["active"])
    return dict(
        library_root=str(store.root),
        releases=releases,
        active_bytes=active,
        retained_bytes=retained,
        unregistered_bytes=max(0, packs_bytes - active - retained),
        packs_bytes=packs_bytes,
        state_bytes=tree_bytes(store.state),
        build_cache_bytes=tree_bytes(store.root / "build-cache"),
        exports_bytes=tree_bytes(store.root / "exports"),
    )


def backup_library(store, output):
    """Snapshot personal state before the append-only catalog, then immutable media.

    Catalog history retains the releases referenced by earlier listener/job state.
    SQLite's backup API includes committed WAL data without stopping the server.
    Build caches and duplicate exports are deliberately excluded.
    """
    output = Path(output).resolve()
    if output.exists():
        raise FileExistsError(output)
    if output.is_relative_to(store.packs) or output.is_relative_to(store.state):
        raise ValueError("Choose a backup path outside packs/ and state/")
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".backup-", dir=output.parent) as temporary:
        stage = Path(temporary) / "library"
        state = stage / "state"
        state.mkdir(parents=True)
        # Snapshot all other databases first. Catalog/source history comes last
        # so their retained media references are included in this backup.
        databases = sorted(
            store.state.glob("*.sqlite3"), key=lambda p: p.name == "catalog.sqlite3"
        )
        for path in databases:
            with (
                sqlite3.connect(path.as_uri() + "?mode=ro", uri=True) as source,
                sqlite3.connect(state / path.name) as target,
            ):
                source.backup(target)
        for path in store.state.rglob("*"):
            if (
                not path.is_file()
                or path.is_symlink()
                or path.name.endswith((".sqlite3", "-wal", "-shm", "-journal"))
            ):
                continue
            target = state / path.relative_to(store.state)
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(path, target)
        with sqlite3.connect(state / "catalog.sqlite3") as db:
            releases = db.execute("SELECT pack_id,release FROM releases").fetchall()
        warnings = []
        for pack_id, release in releases:
            source = store.packs / pack_id / release
            if source.is_dir():
                shutil.copytree(
                    source, stage / "packs" / pack_id / release, symlinks=True
                )
            else:
                warnings.append(f"Missing retained release: {pack_id}:{release}")
        for path in stage.rglob("*"):
            if path.is_symlink():
                warnings.append(f"Link omitted: {path.relative_to(stage)}")
                path.unlink()
        write_json(stage / "backup.json", {"schema_version": 1, "warnings": warnings})
        archive = Path(temporary) / "backup.zip"
        with ZipFile(archive, "x", compression=ZIP_DEFLATED, allowZip64=True) as zipped:
            for path in sorted(stage.rglob("*")):
                if path.is_file():
                    zipped.write(path, path.relative_to(stage).as_posix())
        os.rename(archive, output)
    return {"path": str(output), "bytes": output.stat().st_size, "warnings": warnings}


def restore_library(archive, destination):
    """Restore into a new/empty library root without overlaying live state."""
    destination = Path(destination).resolve()
    if destination.exists() and (
        not destination.is_dir() or any(destination.iterdir())
    ):
        raise ValueError("Restore requires a new or empty library directory")
    destination.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(
        prefix=".restore-", dir=destination.parent
    ) as temporary:
        stage = Path(temporary) / "library"
        stage.mkdir()
        with ZipFile(archive) as source:
            paths = set()
            size = sum(entry.file_size for entry in source.infolist())
            if size > shutil.disk_usage(destination.parent).free:
                raise ValueError("Insufficient disk space for this backup")
            for entry in source.infolist():
                path = relative(entry.filename.rstrip("/"))
                mode = stat.S_IFMT(entry.external_attr >> 16)
                if path in paths or mode not in (0, stat.S_IFREG, stat.S_IFDIR):
                    raise ValueError(
                        "Backup requires unique regular files and directories"
                    )
                paths.add(path)
                if path != "backup.json" and path.split("/")[0] not in {
                    "packs",
                    "state",
                }:
                    raise ValueError("Unexpected backup path")
                target = contained(stage, path)
                if entry.is_dir():
                    target.mkdir(parents=True, exist_ok=True)
                else:
                    target.parent.mkdir(parents=True, exist_ok=True)
                    with source.open(entry) as incoming, target.open("xb") as output:
                        shutil.copyfileobj(incoming, output)
        if read_json(stage / "backup.json").get("schema_version") != 1:
            raise ValueError("Unsupported backup schema")
        if destination.exists():
            destination.rmdir()
        stage.rename(destination)
    return destination
