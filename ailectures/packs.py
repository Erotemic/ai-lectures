"""Immutable pack releases and transactional, live library activation.

Published directories are durable data. SQLite owns only local activation and
historical catalog snapshots; producers never edit a shared registry.
"""

from __future__ import annotations

from contextlib import contextmanager
from copy import deepcopy
import json
import os
from pathlib import Path
import shutil
import sqlite3
import stat
import tempfile
import threading
import time
from uuid import uuid4
from zipfile import ZIP_DEFLATED, ZipFile

from .core import (
    Conflict,
    canonical,
    checksum,
    contained,
    digest,
    file_digest,
    finite,
    lecture_revision,
    name,
    qualified,
    read_json,
    relative,
    text_digest,
    write_json,
)


def recording_id(recording):
    return digest({k: v for k, v in recording.items() if k != "id"})


def validate_catalog(catalog, checksums):
    if not isinstance(catalog, dict) or set(catalog) != {
        "lectures",
        "courses",
        "relationships",
    }:
        raise ValueError("Invalid catalog structure")
    if (
        not isinstance(catalog["lectures"], dict)
        or not isinstance(catalog["courses"], dict)
        or not isinstance(catalog["relationships"], list)
    ):
        raise ValueError("Invalid catalog records")
    for key, row in catalog["lectures"].items():
        qualified(key)
        if (
            row.get("id") != key
            or not isinstance(row.get("title"), str)
            or not isinstance(row.get("transcript"), str)
        ):
            raise ValueError("Invalid lecture record")
        if text_digest(row["transcript"]) != row.get(
            "spoken_sha256"
        ) or lecture_revision(row) != row.get("revision"):
            raise ValueError(f"Lecture revision mismatch: {key}")
        for recording in row.get("recordings", []):
            validate_recording(recording, row, checksums)
    for key, course in catalog["courses"].items():
        qualified(key)
        if (
            course.get("id") != key
            or not isinstance(course.get("title"), str)
            or not isinstance(course.get("lectures"), list)
        ):
            raise ValueError("Invalid course record")
        if len(set(course["lectures"])) != len(course["lectures"]):
            raise ValueError("Duplicate course member")
        for lecture_id in course["lectures"]:
            qualified(lecture_id)  # Other packs may supply optional course steps.
    for relation in catalog["relationships"]:
        qualified(relation["from"])
        qualified(relation["to"])
        if relation["type"] not in {
            "hard_depends_on",
            "soft_depends_on",
            "expands_on",
            "original_parent",
            "alternative_presentation",
            "related_to",
            "listening_next",
            "proof_depends_on",
            "historical_influence",
        }:
            raise ValueError("Unknown relationship type")


def validate_recording(recording, row, checksums):
    name(recording["variant"])
    checksum(recording["recipe"])
    if recording.get("spoken_sha256") != row["spoken_sha256"] or recording.get(
        "id"
    ) != recording_id(recording):
        raise ValueError("Recording does not match its speech or artifact identity")
    pages, segments = recording["pages"], recording["segments"]
    if (
        not isinstance(pages, list)
        or not pages
        or not all(isinstance(p, str) and p for p in pages)
    ):
        raise ValueError("Recording requires speech page text")
    if " ".join(" ".join(pages).split()) != " ".join(row["transcript"].split()):
        raise ValueError("Recording pages do not cover the canonical transcript")
    indexes = []
    for segment in segments:
        index = segment["index"]
        if (
            isinstance(index, bool)
            or not isinstance(index, int)
            or not 0 <= index < len(pages)
        ):
            raise ValueError("Invalid segment index")
        indexes.append(index)
        path = relative(segment["path"])
        if checksums.get(path) != checksum(segment["sha256"]):
            raise ValueError("Recording checksum not present in pack")
        finite(segment["duration"], 0.001)
        if segment["media_type"] not in {
            "audio/mpeg",
            "audio/wav",
            "audio/ogg",
            "audio/mp4",
        }:
            raise ValueError("Unsupported recording media type")
        timing = segment.get("timings")
        if timing is not None and not isinstance(timing, dict):
            raise ValueError("Invalid timing record")
    if indexes != sorted(set(indexes)):
        raise ValueError("Duplicate or unordered segments")
    if not isinstance(recording.get("complete"), bool) or recording["complete"] != (
        indexes == list(range(len(pages)))
    ):
        raise ValueError("Incorrect recording completeness")


def load_release(directory):
    directory = Path(directory).resolve()
    manifest = read_json(contained(directory, "pack.json"))
    sums = read_json(contained(directory, "checksums.json"))
    if manifest.get("schema_version") != 1:
        raise ValueError("Unsupported pack schema version")
    if manifest.get("kind", "source") not in {"source", "media"}:
        raise ValueError("Unsupported pack kind")
    name(manifest["id"])
    if manifest.get("parent") is not None:
        checksum(manifest["parent"])
    for key, release in manifest.get("dependencies", {}).items():
        name(key)
        checksum(release)
    if not isinstance(sums, dict) or not sums or "catalog.json" not in sums:
        raise ValueError("Missing checksum index")
    for path, expected in sums.items():
        checksum(expected)
        if file_digest(contained(directory, path)) != expected:
            raise ValueError(f"Checksum mismatch: {path}")
    for path in directory.rglob("*"):
        if path.is_symlink():
            raise ValueError("Pack symlinks are not supported")
    # Side notes and unrelated files do not invalidate declared playable media.
    # Only indexed payloads participate in the release identity and serving API.
    identity = {k: v for k, v in manifest.items() if k != "release"}
    if digest({"manifest": identity, "checksums": sums}) != manifest.get("release"):
        raise ValueError("Pack release digest mismatch")
    catalog = read_json(directory / "catalog.json")
    validate_catalog(catalog, sums)
    for key in catalog["lectures"]:
        if key.split(":")[0] not in manifest.get("namespaces", []):
            raise ValueError("Lecture namespace not declared")
    return dict(manifest=manifest, catalog=catalog, directory=directory, checksums=sums)


def export_release(
    pack, destination, *, parent=None, dependencies=None, media=None, kind="source"
):
    """Export a source pack plus explicitly selected recordings; never scan caches."""
    destination = Path(destination)
    if destination.exists():
        raise FileExistsError(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(
        prefix=".export-", dir=destination.parent
    ) as temporary:
        stage = Path(temporary) / "release"
        stage.mkdir()
        catalog = dict(
            lectures=deepcopy(pack["lectures"]),
            courses=deepcopy(pack["courses"]),
            relationships=deepcopy(pack.get("relationships", [])),
        )
        for row in catalog["lectures"].values():
            row.pop("origin", None)
            row.pop("url", None)
            row["recordings"] = []
        for item in media or []:
            lecture_id, recording, files = item
            if lecture_id not in catalog["lectures"]:
                raise ValueError("Recording refers to a lecture outside this pack")
            catalog["lectures"][lecture_id]["recordings"].append(deepcopy(recording))
            for path, source in files.items():
                target = contained(stage, path)
                target.parent.mkdir(parents=True, exist_ok=True)
                if target.exists():
                    if file_digest(target) != file_digest(source):
                        raise Conflict(
                            "Two recordings claim different bytes for the same path"
                        )
                else:
                    shutil.copyfile(source, target)
        for path, data in pack.get("extra_files", {}).items():
            target = contained(stage, path)
            if target.exists():
                raise Conflict("Duplicate extra file")
            target.parent.mkdir(parents=True, exist_ok=True)
            if isinstance(data, Path):
                shutil.copyfile(data, target)
            else:
                target.write_bytes(data)
        write_json(stage / "catalog.json", catalog)
        sums = {
            p.relative_to(stage).as_posix(): file_digest(p)
            for p in sorted(stage.rglob("*"))
            if p.is_file()
        }
        if kind not in {"source", "media"}:
            raise ValueError("Unknown pack kind")
        manifest = dict(
            schema_version=1,
            id=name(pack["id"]),
            title=pack["title"],
            parent=parent,
            kind=kind,
            namespaces=sorted({key.split(":")[0] for key in catalog["lectures"]}),
            dependencies=dependencies or {},
        )
        manifest["release"] = digest({"manifest": manifest, "checksums": sums})
        write_json(stage / "checksums.json", sums)
        write_json(stage / "pack.json", manifest)
        load_release(stage)
        stage.rename(destination)
    return manifest


def archive_release(directory, destination):
    load_release(directory)
    with ZipFile(
        destination, "x", compression=ZIP_DEFLATED, allowZip64=True
    ) as archive:
        for path in sorted(Path(directory).rglob("*")):
            if path.is_file():
                archive.write(path, path.relative_to(directory).as_posix())


def unpack_archive(archive_path, destination, *, max_bytes=100 * 1024**3):
    """Only extract indexed regular files to staging; never overlay a repository."""
    with ZipFile(archive_path) as archive:
        entries = archive.infolist()
        names = set()
        total = 0
        for entry in entries:
            path = entry.filename.rstrip("/")
            relative(path)
            if path in names:
                raise ValueError("Duplicate archive entry")
            names.add(path)
            mode = entry.external_attr >> 16
            if stat.S_ISLNK(mode) or (
                stat.S_IFMT(mode) and not (stat.S_ISREG(mode) or stat.S_ISDIR(mode))
            ):
                raise ValueError("Archive entries must be regular files or directories")
            total += entry.file_size
            if total > max_bytes:
                raise ValueError("Pack exceeds extraction size limit")
        if total > shutil.disk_usage(Path(destination).parent).free:
            raise ValueError("Insufficient disk space for pack")
        for entry in entries:
            target = contained(destination, entry.filename.rstrip("/"))
            if entry.is_dir():
                target.mkdir(parents=True, exist_ok=True)
            else:
                target.parent.mkdir(parents=True, exist_ok=True)
                with archive.open(entry) as source, target.open("xb") as output:
                    shutil.copyfileobj(source, output)
    return load_release(destination)


class PackStore:
    def __init__(
        self, root, *, discovery_roots=(), interval=2.0, pins=None, excluded=()
    ):
        self.root = Path(root).resolve()
        self.packs = self.root / "packs"
        self.state = self.root / "state"
        self.packs.mkdir(parents=True, exist_ok=True)
        self.state.mkdir(parents=True, exist_ok=True)
        self.database = self.state / "catalog.sqlite3"
        self.discovery_roots = [
            self.packs,
            *(Path(p).resolve() for p in discovery_roots),
        ]
        self.interval = interval
        self.pins = {name(k): checksum(v) for k, v in (pins or {}).items()}
        self.excluded = {name(k) for k in excluded}
        self._last_scan = -float("inf")
        self._lock = threading.RLock()
        self._validated = {}
        self.errors = []
        with self.connect() as db:
            db.executescript("""
                CREATE TABLE IF NOT EXISTS selections (
                    pack_id TEXT PRIMARY KEY, release TEXT NOT NULL, enabled INTEGER NOT NULL);
                CREATE TABLE IF NOT EXISTS releases (
                    release TEXT PRIMARY KEY, pack_id TEXT NOT NULL, directory TEXT NOT NULL,
                    manifest TEXT NOT NULL, catalog TEXT NOT NULL);
            """)

    @contextmanager
    def connect(self):
        db = sqlite3.connect(self.database, timeout=30)
        db.row_factory = sqlite3.Row
        try:
            with db:
                yield db
        finally:
            db.close()

    def active(self, db=None):
        if db is None:
            with self.connect() as connection:
                return self.active(connection)
        return [
            self.release_row(r)
            for r in db.execute("""SELECT r.* FROM releases r JOIN selections s
                ON r.release=s.release WHERE s.enabled=1 ORDER BY r.pack_id""")
        ]

    def release_row(self, row):
        # Library roots can move between machines or be restored from backup.
        # Pack identity, rather than an old machine's absolute path, owns lookup.
        row = dict(row)
        name(row["pack_id"])
        checksum(row["release"])
        row["directory"] = str(self.packs / row["pack_id"] / row["release"])
        return row

    def compose(self, rows):
        result = dict(
            lectures={},
            courses={},
            relationships=[],
            packs=[],
            media_revisions={},
            conflicts=[],
        )
        active_releases = {r["pack_id"]: r["release"] for r in rows}
        source_ids = set()
        ambiguous_media = set()
        for row in sorted(
            rows, key=lambda r: json.loads(r["manifest"]).get("kind") == "media"
        ):
            manifest, catalog = json.loads(row["manifest"]), json.loads(row["catalog"])
            is_media = manifest.get("kind") == "media"
            for key, expected in manifest.get("dependencies", {}).items():
                if active_releases.get(key) != expected:
                    raise Conflict(f"Missing required pack release: {key}:{expected}")
            result["packs"].append(manifest)
            for key, lecture in catalog["lectures"].items():
                lecture = deepcopy(lecture)
                lecture["origin"] = {"pack": row["pack_id"], "release": row["release"]}
                for rec in lecture.get("recordings", []):
                    rec["_release"] = row["release"]
                if is_media:
                    result["media_revisions"].setdefault(key, []).append(lecture)
                    if key in ambiguous_media:
                        continue
                previous = result["lectures"].get(key)
                if previous and previous["revision"] != lecture["revision"]:
                    if is_media:
                        if previous["spoken_sha256"] != lecture["spoken_sha256"]:
                            if key not in source_ids:
                                ambiguous_media.add(key)
                                result["lectures"].pop(key)
                            continue  # Retained old audio is not the revised lecture.
                    else:
                        raise Conflict(f"Conflicting lecture revision: {key}")
                if previous:
                    by_id = {r["id"]: r for r in previous["recordings"]}
                    by_id.update({r["id"]: r for r in lecture["recordings"]})
                    previous["recordings"] = list(by_id.values())
                else:
                    result["lectures"][key] = lecture
                if not is_media:
                    source_ids.add(key)
            for key, course in catalog["courses"].items():
                if key in result["courses"] and result["courses"][key] != course:
                    raise Conflict(f"Conflicting course: {key}")
                result["courses"][key] = course
            result["relationships"].extend(catalog["relationships"])
        result["conflicts"] = sorted(ambiguous_media)
        identities = {}
        for key, row in result["lectures"].items():
            for alias in [key, *row.get("aliases", [])]:
                qualified(alias)
                if alias in identities and identities[alias] != key:
                    raise Conflict(f"Conflicting lecture alias: {alias}")
                identities[alias] = key
        result["generation"] = digest(sorted(active_releases.items()))
        return result

    def _write_lock(self, db):
        """Diagnostic export only. SQLite transactions are the activation authority."""
        active = self.active(db)
        temporary = self.root / (".library-lock-" + uuid4().hex)
        try:
            write_json(
                temporary,
                {
                    "schema_version": 1,
                    "packs": {r["pack_id"]: r["release"] for r in active},
                },
            )
            os.replace(temporary, self.root / "library.lock.json")
        finally:
            temporary.unlink(missing_ok=True)

    def install(self, source, *, expected=None):
        source = Path(source).resolve()
        if source.is_file():
            with tempfile.TemporaryDirectory(
                prefix=".import-", dir=self.root
            ) as temporary:
                unpack_archive(source, Path(temporary) / "release")
                return self.install(Path(temporary) / "release", expected=expected)
        release = load_release(source)
        manifest = release["manifest"]
        pack_id, revision = manifest["id"], manifest["release"]
        destination = self.packs / pack_id / revision
        destination.parent.mkdir(parents=True, exist_ok=True)
        if source != destination:
            with tempfile.TemporaryDirectory(
                prefix=".install-", dir=self.root
            ) as temporary:
                staged = Path(temporary) / "release"
                shutil.copytree(source, staged, symlinks=True)
                load_release(staged)  # Detect edits while copying.
                try:
                    staged.rename(destination)
                except OSError:
                    if (
                        not destination.is_dir()
                        or load_release(destination)["manifest"]["release"] != revision
                    ):
                        raise
        with self.connect() as db:
            db.execute("BEGIN IMMEDIATE")
            previous = db.execute(
                "SELECT * FROM selections WHERE pack_id=?", (pack_id,)
            ).fetchone()
            if previous and previous["release"] != revision:
                base = expected if expected is not None else manifest.get("parent")
                if base != previous["release"]:
                    raise Conflict(
                        f"Stale update to {pack_id}; expected base {previous['release']}"
                    )
            elif expected is not None and previous is None:
                raise Conflict("Expected base pack is not installed")
            db.execute(
                "INSERT OR IGNORE INTO releases VALUES (?,?,?,?,?)",
                (
                    revision,
                    pack_id,
                    str(destination),
                    canonical(manifest).decode(),
                    canonical(release["catalog"]).decode(),
                ),
            )
            db.execute(
                "INSERT OR REPLACE INTO selections VALUES (?,?,1)", (pack_id, revision)
            )
            self.compose(self.active(db))  # Any conflict rolls back this activation.
            self._write_lock(db)
        return manifest

    def remove(self, pack_id):
        name(pack_id)
        with self.connect() as db:
            db.execute("BEGIN IMMEDIATE")
            db.execute("UPDATE selections SET enabled=0 WHERE pack_id=?", (pack_id,))
            self.compose(self.active(db))
            self._write_lock(db)
        # Immutable releases remain readable for active players and feedback.

    def _candidate(self, directory):
        paths = sorted(Path(directory).rglob("*"))
        signature = tuple(
            (str(p), p.lstat().st_mtime_ns, p.lstat().st_size) for p in paths
        )
        key = str(directory)
        if key not in self._validated or self._validated[key][0] != signature:
            self._validated[key] = signature, load_release(directory)
        return self._validated[key][1]

    def reconcile(self, *, force=False):
        with self._lock:
            now = time.monotonic()
            if not force and now - self._last_scan < self.interval:
                return
            self._last_scan = now
            errors, candidates = [], {}
            for root in self.discovery_roots:
                # Fixed supported depths; never descend into arbitrary media trees.
                paths = [
                    root / "pack.json",
                    *root.glob("*/pack.json"),
                    *root.glob("*/*/pack.json"),
                ]
                for path in paths:
                    if not path.is_file() or any(
                        p.startswith(".") for p in path.relative_to(root).parts
                    ):
                        continue
                    try:
                        release = self._candidate(path.parent)
                        candidates.setdefault(release["manifest"]["id"], {})[
                            release["manifest"]["release"]
                        ] = release
                    except (OSError, ValueError, KeyError, TypeError) as exc:
                        errors.append(f"{path.parent.name}: {exc}")
            for pack_id, releases in candidates.items():
                if pack_id in self.excluded:
                    with self.connect() as db:
                        selected = db.execute(
                            "SELECT enabled FROM selections WHERE pack_id=?", (pack_id,)
                        ).fetchone()
                    if selected and selected["enabled"]:
                        try:
                            self.remove(pack_id)
                        except Conflict as exc:
                            errors.append(f"{pack_id}: {exc}")
                    continue
                while True:
                    with self.connect() as db:
                        previous = db.execute(
                            "SELECT * FROM selections WHERE pack_id=?", (pack_id,)
                        ).fetchone()
                    if previous and not previous["enabled"]:
                        break
                    current = previous["release"] if previous else None
                    if pack_id in self.pins:
                        pinned = self.pins[pack_id]
                        if current == pinned:
                            break
                        if pinned not in releases:
                            errors.append(f"{pack_id}: pinned release is not available")
                            break
                        try:
                            self.install(
                                releases[pinned]["directory"], expected=current
                            )
                        except (OSError, ValueError) as exc:
                            errors.append(f"{pack_id}: {exc}")
                        break
                    eligible = [
                        r
                        for rev, r in releases.items()
                        if rev != current
                        and (
                            r["manifest"].get("parent") == current
                            if current
                            else r["manifest"].get("parent") not in releases
                        )
                    ]
                    if len(eligible) > 1:
                        errors.append(
                            f"{pack_id}: competing releases; explicit merge/selection required"
                        )
                        break
                    if not eligible:
                        break
                    try:
                        self.install(eligible[0]["directory"])
                    except (OSError, ValueError, KeyError, TypeError) as exc:
                        errors.append(f"{pack_id}: {exc}")
                        break
            self.errors = errors

    def snapshot(self):
        self.reconcile()
        return self.compose(self.active())

    def historical(self, release_id, lecture_id):
        checksum(release_id)
        qualified(lecture_id)
        with self.connect() as db:
            row = db.execute(
                "SELECT * FROM releases WHERE release=?", (release_id,)
            ).fetchone()
        if row is None:
            raise KeyError("Unknown historical release")
        row = self.release_row(row)
        lecture = json.loads(row["catalog"])["lectures"][lecture_id]
        return lecture, Path(row["directory"])

    def media_file(self, release_id, recording_id, index):
        checksum(release_id)
        checksum(recording_id)
        with self.connect() as db:
            row = db.execute(
                "SELECT * FROM releases WHERE release=?", (release_id,)
            ).fetchone()
        if row is None:
            raise KeyError("Unknown release")
        row = self.release_row(row)
        catalog = json.loads(row["catalog"])
        for lecture in catalog["lectures"].values():
            for rec in lecture.get("recordings", []):
                if rec["id"] == recording_id:
                    segment = next(s for s in rec["segments"] if s["index"] == index)
                    path = contained(row["directory"], segment["path"])
                    if file_digest(path) != segment["sha256"]:
                        raise ValueError(
                            "Published recording bytes changed; refusing an obsolete immutable URL"
                        )
                    return path, segment
        raise KeyError("Unknown recording")
