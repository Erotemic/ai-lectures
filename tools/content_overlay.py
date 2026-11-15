#!/usr/bin/env python3
"""Share source snapshots and merge independently authored content overlays.

The overlay contract is intentionally independent of the runtime pack format.
Each changed file carries its source-snapshot hash; stale updates fail before
writing. Producers never provide a shared registry or server configuration.
"""

from __future__ import annotations

import argparse
from contextlib import contextmanager
import fcntl
import hashlib
import io
import json
from pathlib import Path, PurePosixPath
import shutil
import stat
import subprocess
import sys
import tempfile
from zipfile import ZipFile, ZIP_DEFLATED

ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT = "SOURCE_SNAPSHOT.json"
OVERLAY = "content-overlay.json"
TEXT = {".md", ".json", ".yaml", ".yml", ".txt", ".tsv", ".toml", ".py", ".html"}


class OverlayConflict(ValueError):
    pass


def sha(data):
    return hashlib.sha256(data).hexdigest()


def encode(value):
    return (
        json.dumps(value, sort_keys=True, ensure_ascii=False, indent=2).encode() + b"\n"
    )


def safe_path(value):
    path = PurePosixPath(value)
    if (
        "\\" in value
        or path.is_absolute()
        or str(path) != value
        or not path.parts
        or any(p.startswith(".") or p == "__pycache__" for p in path.parts)
    ):
        raise ValueError(f"Invalid overlay path: {value}")
    return path


def pack_path(value):
    path = safe_path(value)
    if len(path.parts) != 2 or not (
        path.parts[0] == "content"
        or path.parts[0] == "draft-stages"
        and path.parts[1].startswith("tts-")
    ):
        raise ValueError(
            "Pack roots must be content/<namespace> or draft-stages/tts-<namespace>"
        )
    return path


def destination(root, relative):
    path = root / safe_path(relative)
    for parent in [path, *path.parents]:
        if parent == root:
            break
        if parent.is_symlink():
            raise ValueError(f"Symlink destination: {relative}")
    path.resolve().relative_to(root)
    return path


def snapshot(repo, output):
    """Archive the committed tree only; no ignored state, media, or credentials."""
    repo = Path(repo).resolve()
    revision = subprocess.check_output(
        ["git", "-C", str(repo), "rev-parse", "HEAD"], text=True
    ).strip()
    data = subprocess.check_output(
        ["git", "-C", str(repo), "archive", "--format=zip", revision]
    )
    with (
        ZipFile(io.BytesIO(data)) as source,
        ZipFile(output, "x", compression=ZIP_DEFLATED) as target,
    ):
        files = {}
        for entry in source.infolist():
            contents = source.read(entry)
            if not entry.is_dir():
                if entry.filename == SNAPSHOT:
                    raise ValueError("Snapshot marker must not be committed")
                files[entry.filename] = sha(contents)
            target.writestr(entry, contents)
        target.writestr(
            SNAPSHOT,
            encode({"schema_version": 1, "base_commit": revision, "files": files}),
        )
    return revision


def build(repo, packs, output):
    repo = Path(repo).resolve()
    baseline = json.loads((repo / SNAPSHOT).read_text())
    if baseline.get("schema_version") != 1:
        raise ValueError("Unsupported source snapshot")
    roots = [pack_path(p) for p in packs]
    files, payload = {}, {}
    for relative in baseline["files"]:
        path = PurePosixPath(relative)
        if any(path.is_relative_to(root) for root in roots) and path.suffix in TEXT:
            if not destination(repo, relative).exists():
                raise ValueError(
                    f"Source deletion requires coordinator review: {relative}"
                )
    for pack in roots:
        folder = destination(repo, str(pack))
        if not folder.is_dir():
            raise ValueError(f"Missing pack: {pack}")
        for path in sorted(folder.rglob("*")):
            if path.is_dir():
                continue
            relative = path.relative_to(repo).as_posix()
            # Ignore build products; never include binary media or private dotfiles.
            if any(
                p.startswith(".") or p == "__pycache__"
                for p in path.relative_to(folder).parts
            ):
                continue
            if path.is_symlink():
                raise ValueError(f"Cannot export a symlink: {relative}")
            if path.suffix not in TEXT:
                continue
            data = path.read_bytes()
            data.decode("utf-8")
            if b"\0" in data:
                raise ValueError(f"Binary source payload: {relative}")
            base = baseline["files"].get(relative)
            if sha(data) == base:
                continue
            files[relative] = {"base_sha256": base, "sha256": sha(data)}
            payload[relative] = data
    if not files:
        raise ValueError("No changed source files in the selected packs")
    manifest = {
        "schema_version": 1,
        "base_commit": baseline["base_commit"],
        "pack_roots": [str(p) for p in roots],
        "files": files,
    }
    with ZipFile(output, "x", compression=ZIP_DEFLATED) as archive:
        archive.writestr(OVERLAY, encode(manifest))
        for path, data in payload.items():
            archive.writestr(path, data)
    return manifest


@contextmanager
def merge_lock(repo):
    with (repo / ".content-overlay.lock").open("a") as stream:
        fcntl.flock(stream, fcntl.LOCK_EX)
        try:
            yield
        finally:
            fcntl.flock(stream, fcntl.LOCK_UN)


def validate_candidate(repo, roots, payload):
    # Use the current extraction/manifest contract, never execute incoming code.
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))
    from ailectures.catalog import repository_track

    with tempfile.TemporaryDirectory(prefix="lecture-overlay-") as tmp:
        candidate = Path(tmp)
        for root in roots:
            existing = destination(repo, str(root))
            if existing.exists():
                shutil.copytree(existing, candidate / root, symlinks=True)
        legacy_sources = repo / "draft-stages/tts-lectures/metadata/sources.json"
        fallback = candidate / "draft-stages/tts-lectures/metadata/sources.json"
        if legacy_sources.exists() and not fallback.exists():
            fallback.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(legacy_sources, fallback)
        for path, data in payload.items():
            target = destination(candidate, path)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
        for root in roots:
            repository_track(candidate / root)


def apply(repo, archive, *, check=False):
    repo = Path(repo).resolve()
    with ZipFile(archive) as source:
        entries = source.infolist()
        names = [e.filename for e in entries]
        if len(set(names)) != len(names) or OVERLAY not in names:
            raise ValueError("Missing overlay manifest or duplicate archive entry")
        if sum(e.file_size for e in entries) > 128 * 1024**2:
            raise ValueError("Source overlay exceeds 128 MiB")
        manifest = json.loads(source.read(OVERLAY))
        if manifest.get("schema_version") != 1:
            raise ValueError("Unsupported overlay version")
        roots = [pack_path(p) for p in manifest["pack_roots"]]
        if set(names) != set(manifest["files"]) | {OVERLAY}:
            raise ValueError("Overlay manifest does not match archive contents")
        payload = {}
        for entry in entries:
            if entry.filename == OVERLAY:
                continue
            path = safe_path(entry.filename)
            if (
                not any(path.is_relative_to(root) for root in roots)
                or path.suffix not in TEXT
            ):
                raise ValueError(f"File outside declared pack: {path}")
            mode = stat.S_IFMT(entry.external_attr >> 16)
            if mode not in (0, stat.S_IFREG):
                raise ValueError("Only regular source files are accepted")
            data = source.read(entry)
            data.decode("utf-8")
            if (
                b"\0" in data
                or sha(data) != manifest["files"][entry.filename]["sha256"]
            ):
                raise ValueError("Corrupt source payload")
            payload[entry.filename] = data
    with merge_lock(repo):
        pending = {}
        for path, data in payload.items():
            target = destination(repo, path)
            base = manifest["files"][path]["base_sha256"]
            if target.exists():
                if not target.is_file():
                    raise OverlayConflict(f"Existing path is not a file: {path}")
                current = sha(target.read_bytes())
                if current == sha(data):
                    continue
                if base is None or current != base:
                    raise OverlayConflict(
                        f"File changed since this agent's snapshot: {path}"
                    )
            elif base is not None:
                raise OverlayConflict(f"Previously existing file was removed: {path}")
            pending[path] = data
        validate_candidate(repo, roots, pending)
        if not check:
            # Publish manifests last; source discovery retains its last valid view
            # while new files and their metadata are being written.
            ordered = sorted(pending, key=lambda p: (p.endswith("/track.json"), p))
            for path in ordered:
                target = destination(repo, path)
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(pending[path])
        return list(pending)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=ROOT)
    commands = parser.add_subparsers(dest="command", required=True)
    for command in ["snapshot", "build"]:
        cmd = commands.add_parser(command)
        cmd.add_argument("--output", type=Path, required=True)
        if command == "build":
            cmd.add_argument("--pack", action="append", required=True)
    cmd = commands.add_parser("apply")
    cmd.add_argument("archive", type=Path)
    cmd.add_argument("--check", action="store_true")
    args = parser.parse_args(argv)
    try:
        if args.command == "snapshot":
            print(snapshot(args.repo, args.output))
        elif args.command == "build":
            print(
                f'{len(build(args.repo, args.pack, args.output)["files"])} changed source files exported'
            )
        else:
            print(
                f'{len(apply(args.repo, args.archive, check=args.check))} source files {"checked" if args.check else "applied"}'
            )
    except (OSError, ValueError, KeyError) as exc:
        parser.exit(1, f"{exc}\n")


if __name__ == "__main__":
    main()
