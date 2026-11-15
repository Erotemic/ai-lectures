#!/usr/bin/env python3
"""Import ordinary content ZIPs or optional hash-aware overlays.

Imports preserve conflicting files, stage replacements with an undo journal,
and never run content checks, tests, TTS, or runtime builds.
"""

from __future__ import annotations

import argparse
import hashlib
import io
import json
from pathlib import Path, PurePosixPath
import stat
import subprocess
import sys
from zipfile import ZipFile, ZIP_DEFLATED

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from ailectures.source_updates import apply_files, source_lock

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
    baseline = None
    if (repo / SNAPSHOT).exists():
        try:
            candidate = json.loads((repo / SNAPSHOT).read_text())
            if candidate.get("schema_version") == 1:
                baseline = candidate
        except (OSError, ValueError):
            pass
    roots = [pack_path(p) for p in packs]
    files, payload = {}, {}
    for relative in baseline["files"] if baseline else []:
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
            base = baseline["files"].get(relative) if baseline else None
            if sha(data) == base:
                continue
            files[relative] = {"base_sha256": base, "sha256": sha(data)}
            payload[relative] = data
    if not files:
        raise ValueError("No changed source files in the selected packs")
    manifest = {
        "schema_version": 1,
        "base_commit": baseline["base_commit"] if baseline else None,
        "pack_roots": [str(p) for p in roots],
        "files": files,
    }
    with ZipFile(output, "x", compression=ZIP_DEFLATED) as archive:
        if baseline:
            archive.writestr(OVERLAY, encode(manifest))
        for path, data in payload.items():
            archive.writestr(path, data)
    return manifest


class ImportResult(list):
    def __init__(self, paths, backup=None):
        super().__init__(paths)
        self.backup = backup


def _infer_root(repo, payload):
    if "track.json" in payload:
        try:
            namespace = json.loads(payload["track.json"])["id"]
            if (
                not isinstance(namespace, str)
                or not namespace
                or any(
                    c not in "abcdefghijklmnopqrstuvwxyz0123456789-_."
                    for c in namespace
                )
            ):
                raise ValueError("invalid namespace")
            matches = []
            for path in [
                *(repo / "content").glob("*/track.json"),
                *(repo / "draft-stages").glob("tts-*/track.json"),
            ]:
                try:
                    if json.loads(path.read_text()).get("id") == namespace:
                        matches.append(path.parent.relative_to(repo).as_posix())
                except (OSError, ValueError, AttributeError):
                    continue
            if len(matches) == 1:
                return matches[0]
            if not matches:
                return "content/" + namespace
        except (ValueError, KeyError, TypeError):
            pass
    raise ValueError(
        "ZIP destination is ambiguous; supply --pack content/<namespace> or draft-stages/tts-<namespace>"
    )


def _read_archive(repo, archive, pack=None):
    payload = {}
    with ZipFile(archive) as source:
        entries = source.infolist()
        if sum(e.file_size for e in entries) > 128 * 1024**2:
            raise ValueError(
                "Source update exceeds 128 MiB; transfer large prepared media separately"
            )
        for entry in entries:
            if (
                entry.is_dir()
                or entry.filename.startswith("__MACOSX/")
                or PurePosixPath(entry.filename).name == ".DS_Store"
            ):
                continue
            if entry.filename in payload:
                raise ValueError("Duplicate archive entry")
            safe_path(entry.filename)
            if stat.S_IFMT(entry.external_attr >> 16) not in (0, stat.S_IFREG):
                raise ValueError("Only regular source files are accepted")
            payload[entry.filename] = source.read(entry)
    manifest = json.loads(payload.pop(OVERLAY)) if OVERLAY in payload else None
    payload.pop(SNAPSHOT, None)
    if manifest is not None:
        if manifest.get("schema_version") != 1 or set(payload) != set(
            manifest["files"]
        ):
            raise ValueError("Overlay manifest does not match archive contents")
        roots = [pack_path(p) for p in manifest["pack_roots"]]
        for path, data in payload.items():
            if sha(data) != manifest["files"][path]["sha256"]:
                raise ValueError("Corrupt source payload")
        bases = {path: item["base_sha256"] for path, item in manifest["files"].items()}
    else:
        bases = {}

        def repository_relative():
            return all(
                len(PurePosixPath(p).parts) >= 3
                and (
                    PurePosixPath(p).parts[0] == "content"
                    or PurePosixPath(p).parts[0] == "draft-stages"
                    and PurePosixPath(p).parts[1].startswith("tts-")
                )
                for p in payload
            )

        enclosing = None
        if not repository_relative():
            first = {PurePosixPath(path).parts[0] for path in payload}
            if len(first) == 1 and all(
                len(PurePosixPath(path).parts) > 1 for path in payload
            ):
                enclosing = next(iter(first))
                payload = {
                    path[len(enclosing) + 1 :]: data for path, data in payload.items()
                }
        if repository_relative():
            roots = sorted(
                {pack_path("/".join(PurePosixPath(p).parts[:2])) for p in payload},
                key=str,
            )
        else:
            inferred = (
                "draft-stages/" + enclosing
                if enclosing and enclosing.startswith("tts-")
                else None
            )
            root = str(pack_path(pack or inferred or _infer_root(repo, payload)))
            payload = {root + "/" + path: data for path, data in payload.items()}
            roots = [PurePosixPath(root)]
    if pack and {str(root) for root in roots} != {str(pack_path(pack))}:
        raise ValueError("ZIP paths do not match the selected pack")
    if not payload:
        raise ValueError("ZIP contains no source files")
    for path in payload:
        if not any(safe_path(path).is_relative_to(root) for root in roots):
            raise ValueError(f"File outside declared pack: {path}")
    return roots, payload, bases


def apply(repo, archive, *, check=False, pack=None, replace_owned=False):
    repo = Path(repo).resolve()
    roots, payload, bases = _read_archive(repo, archive, pack)
    if replace_owned and len(roots) != 1:
        raise ValueError(
            "--replace-owned applies to one exclusively owned pack at a time"
        )
    with source_lock(repo, write=True):
        pending = {}
        for path, data in payload.items():
            target = destination(repo, path)
            base = bases.get(path)
            if target.exists():
                if not target.is_file():
                    raise OverlayConflict(f"Existing path is not a file: {path}")
                current = sha(target.read_bytes())
                if current == sha(data):
                    continue
                if not replace_owned and (base is None or current != base):
                    raise OverlayConflict(
                        f"Existing file differs: {path}. Original left untouched. For one exclusively owned pack, use --replace-owned."
                    )
            elif base is not None and not replace_owned:
                raise OverlayConflict(f"Previously existing file was removed: {path}")
            pending[path] = data
        backup = apply_files(repo, pending) if not check else None
        return ImportResult(pending, backup)


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
    cmd.add_argument(
        "--check",
        action="store_true",
        help="optional conflict preview; no new update is applied",
    )
    cmd.add_argument(
        "--pack", help="destination for ZIPs without repository-relative paths"
    )
    cmd.add_argument(
        "--replace-owned",
        action="store_true",
        help="replace differing files in one exclusively owned pack, retaining a backup",
    )
    args = parser.parse_args(argv)
    try:
        if args.command == "snapshot":
            print(snapshot(args.repo, args.output))
        elif args.command == "build":
            print(
                f'{len(build(args.repo, args.pack, args.output)["files"])} changed source files exported'
            )
        else:
            result = apply(
                args.repo,
                args.archive,
                check=args.check,
                pack=args.pack,
                replace_owned=args.replace_owned,
            )
            print(
                f'{len(result)} source files {"checked" if args.check else "applied"}'
            )
            if result.backup:
                print(f"Local recovery copy: {result.backup}")

    except (OSError, ValueError, KeyError) as exc:
        parser.exit(1, f"{exc}\n")


if __name__ == "__main__":
    main()
