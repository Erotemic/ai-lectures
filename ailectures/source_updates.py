"""Coherent source updates shared by the importer and repository reader.

A small undo journal covers interrupted multi-file writes. Readers use the same
lock and recover unfinished imports before scanning. No teaching-content checks
or runtime builds are performed at this boundary.
"""

from __future__ import annotations

from contextlib import contextmanager

try:
    import fcntl
except ImportError:  # Windows readers use the same lock exclusively.
    fcntl = None
import json
import os
from pathlib import Path, PurePosixPath
from uuid import uuid4

JOURNAL = ".content-update"


def source_path(root, relative):
    pure = PurePosixPath(relative)
    if (
        not pure.parts
        or pure.is_absolute()
        or "\\" in relative
        or str(pure) != relative
        or any(part.startswith(".") for part in pure.parts)
    ):
        raise ValueError(f"Unsafe source path: {relative}")
    path = Path(root) / relative
    for parent in (path, *path.parents):
        if parent == root:
            break
        if parent.is_symlink():
            raise ValueError(f"Symlink destination: {relative}")
    path.resolve().relative_to(Path(root).resolve())
    return path


def _sync_directory(directory):
    if os.name == "nt":
        return
    descriptor = os.open(directory, os.O_RDONLY)
    try:
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


def atomic_bytes(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name("." + path.name + "-" + uuid4().hex)
    try:
        with temporary.open("xb") as stream:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
        _sync_directory(path.parent)
    finally:
        temporary.unlink(missing_ok=True)


def recover(root):
    """Undo an unfinished import. Caller must hold the exclusive source lock."""
    root = Path(root).resolve()
    pointer = root / JOURNAL / "active.json"
    if not pointer.exists():
        return
    record = json.loads(pointer.read_text())
    transaction = root / JOURNAL / record["transaction"]
    for item in reversed(record["files"]):
        target = source_path(root, item["path"])
        backup = transaction / "before" / item["path"]
        current = target.read_bytes() if target.is_file() else None
        before = backup.read_bytes() if item["existed"] else None
        staged = transaction / "after" / item["path"]
        incoming = staged.read_bytes()
        if current not in (before, incoming, None):
            # A manual edit after a crash is preserved alongside the undo copy.
            saved = transaction / "manual-edits" / item["path"]
            atomic_bytes(saved, current)
        if item["existed"]:
            if current != before:
                temporary = target.with_name(".restore-" + uuid4().hex)
                try:
                    os.link(backup, temporary)
                    os.replace(temporary, target)
                    _sync_directory(target.parent)
                except OSError:
                    atomic_bytes(target, before)
                finally:
                    temporary.unlink(missing_ok=True)
            if item.get("mode") is not None:
                target.chmod(item["mode"])
        elif target.exists():
            target.unlink()
            _sync_directory(target.parent)
    pointer.unlink()
    _sync_directory(pointer.parent)
    # Keep the before/after copies as an ordinary local recovery backup.


def _lock(stream, *, write=False, unlock=False):
    if fcntl is not None:
        fcntl.flock(
            stream,
            fcntl.LOCK_UN if unlock else fcntl.LOCK_EX if write else fcntl.LOCK_SH,
        )
    else:
        import msvcrt

        stream.seek(0)
        msvcrt.locking(
            stream.fileno(), msvcrt.LK_UNLCK if unlock else msvcrt.LK_LOCK, 1
        )


@contextmanager
def source_lock(root, *, write=False):
    root = Path(root).resolve()
    try:
        stream = (root / ".content-overlay.lock").open("a+b")
    except OSError:
        if write or (root / JOURNAL / "active.json").exists():
            raise
        yield  # A read-only source tree can still be served.
        return
    with stream:
        if fcntl is None and stream.tell() == 0:
            stream.write(b"\0")
            stream.flush()
        _lock(stream, write=write)
        try:
            if (root / JOURNAL / "active.json").exists():
                if not write:
                    _lock(stream, unlock=True)
                    _lock(stream, write=True)
                recover(root)
            yield
        finally:
            _lock(stream, unlock=True)


def apply_files(root, payload, *, replace_file=None):
    """Apply files with rollback and a crash-recovery receipt, under source_lock.

    Backups are local implementation details. They are never required in the
    incoming ZIP or exposed as a new content-authoring format.
    """
    if not payload:
        return None
    root = Path(root).resolve()
    directory = root / JOURNAL / uuid4().hex
    directory.mkdir(parents=True)
    entries = []
    for relative, data in payload.items():
        target = source_path(root, relative)
        staged = directory / "after" / relative
        atomic_bytes(staged, data)
        existed = target.is_file()
        if existed:
            atomic_bytes(directory / "before" / relative, target.read_bytes())
        entries.append(
            {
                "path": relative,
                "existed": existed,
                "mode": target.stat().st_mode & 0o777 if existed else None,
            }
        )
    record = {"transaction": directory.name, "files": entries}
    atomic_bytes(directory / "receipt.json", json.dumps(record).encode())
    pointer = root / JOURNAL / "active.json"
    atomic_bytes(pointer, json.dumps(record).encode())
    replace_file = replace_file or atomic_bytes
    try:
        for item in sorted(
            entries,
            key=lambda item: (item["path"].endswith("/track.json"), item["path"]),
        ):
            relative = item["path"]
            target = source_path(root, relative)
            mode = target.stat().st_mode & 0o777 if target.exists() else None
            replace_file(target, (directory / "after" / relative).read_bytes())
            if mode is not None:
                target.chmod(mode)
        pointer.unlink()
        _sync_directory(pointer.parent)
    except BaseException:
        recover(root)
        raise
    return directory
