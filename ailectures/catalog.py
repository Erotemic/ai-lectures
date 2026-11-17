"""Live repository adapters; no synthesis configuration or rendering imports."""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path
import re
import json
import threading

from .core import (
    contained,
    digest,
    extract_text,
    file_digest,
    lecture_revision,
    name,
    qualified,
    read_json,
    text_digest,
)
from .source_updates import atomic_bytes, source_lock
from .organization import collection_metadata, topic_tags
from .navigation import route_collections
from .companions import discover_companions, companion_file

LECTURE_FILE = re.compile(r"^([0-9]{6})-.*\.md$")


def referenced_sources(metadata, sources, issue=lambda message: None):
    keys = set()

    def collect(value):
        if isinstance(value, dict):
            if isinstance(value.get("source_id"), str):
                keys.add(value["source_id"])
            if isinstance(value.get("source_ids"), list):
                keys.update(key for key in value["source_ids"] if isinstance(key, str))
            for item in value.values():
                collect(item)
        elif isinstance(value, list):
            for item in value:
                collect(item)

    collect(metadata)
    missing = keys - sources.keys()
    if missing:
        issue(f"Undefined reading sources: {sorted(missing)}")
    return {key: sources[key] for key in sorted(keys & sources.keys())}


def repository_track(directory, *, previous=None, strict=False):
    """Discover usable lectures, isolating editorial and per-file problems.

    strict=True is an optional authoring check, never the delivery/import gate.
    """
    directory = Path(directory)
    previous = previous or {}
    warnings = []

    def issue(message):
        if strict:
            raise ValueError(message)
        warnings.append(f"{directory.name}: {message}")

    def load(path, fallback):
        try:
            value = read_json(path)
            if not isinstance(value, dict):
                raise ValueError("expected a JSON object")
            return value
        except (OSError, ValueError) as exc:
            issue(f"{path.name}: {exc}")
            return fallback

    guessed = {"tts-lectures": "g2", "tts-paper": "g3"}.get(
        directory.name, directory.name.removeprefix("tts-")
    )
    namespace = previous.get("id", guessed)
    plan = (
        load(directory / "track.json", {})
        if (directory / "track.json").exists()
        else {}
    )
    try:
        namespace = name(plan.get("id", namespace))
    except ValueError:
        issue("Invalid track ID; using the previous identity or directory name")
        namespace = name(namespace)
    old_course = previous.get("courses", {}).get(f"{namespace}:main", {})
    title = (
        plan.get("title")
        or old_course.get("title")
        or (
            "Operator Theory and Spectral Perturbation"
            if namespace == "g2"
            else namespace.replace("-", " ").title()
        )
    )
    files = {
        p.name: p
        for p in sorted(directory.glob("*.md"))
        if LECTURE_FILE.fullmatch(p.name)
    }
    declared = plan.get("lectures")
    if not isinstance(declared, list):
        if declared is not None:
            issue("Lecture list is malformed; discovering numbered manuscripts")
        declared = [{"id": path[:6], "file": path} for path in files]
        old_order = old_course.get("lectures", [])
        if old_order:
            declared.sort(
                key=lambda row: (
                    old_order.index(namespace + ":" + row["id"])
                    if namespace + ":" + row["id"] in old_order
                    else len(old_order)
                )
            )
    entries = []
    seen_ids, seen_files = set(), set()
    course_members = []
    for entry in declared:
        try:
            if not isinstance(entry, dict):
                raise ValueError("lecture entry is not an object")
            filename, local_id = entry["file"], entry["id"]
            qualified(namespace + ":" + local_id)
            if (
                not isinstance(filename, str)
                or Path(filename).name != filename
                or not filename.endswith(".md")
            ):
                raise ValueError(
                    "lecture filename must name a Markdown file in this directory"
                )
            if local_id in seen_ids or filename in seen_files:
                raise ValueError(f"duplicate lecture identity or filename: {local_id}")
            seen_ids.add(local_id)
            seen_files.add(filename)
            entries.append(entry)
            course_members.append(namespace + ":" + local_id)
        except (KeyError, TypeError, ValueError) as exc:
            issue(str(exc))
    for filename in files:
        if filename not in seen_files:
            local_id = filename[:6]
            if local_id in seen_ids:
                issue(f"Ambiguous manuscript {filename}; another file uses this ID")
                continue
            entries.append({"id": local_id, "file": filename})
            seen_ids.add(local_id)
            issue(
                f"{filename} is not indexed; available in the library outside the course order"
            )
    source_path = directory / "metadata" / "sources.json"
    if not source_path.exists() and directory.name in {"tts-lectures", "tts-paper"}:
        source_path = directory.parent / "tts-lectures" / "metadata" / "sources.json"
    old_sources = {
        key: source
        for row in previous.get("lectures", {}).values()
        for key, source in row.get("sources", {}).items()
    }
    source_catalog = (
        load(source_path, {"sources": old_sources}).get("sources", {})
        if source_path.exists()
        else old_sources
    )
    if not isinstance(source_catalog, dict):
        issue(
            "Reading source catalog is malformed; using available recorded references"
        )
        source_catalog = old_sources
    lectures, extra_files, companion_paths = {}, {}, []
    for entry in entries:
        key = namespace + ":" + entry["id"]
        old = previous.get("lectures", {}).get(key)
        path = directory / entry["file"]
        try:
            source = path.read_text(encoding="utf-8")
            transcript = extract_text(source, str(path)).strip()
        except (OSError, ValueError) as exc:
            issue(f"{entry['file']}: {exc}")
            if old:
                lectures[key] = deepcopy(old)
            continue
        sidecar = directory / "metadata" / (entry["id"] + ".json")
        metadata = (
            load(sidecar, old.get("metadata", {}) if old else {})
            if sidecar.exists()
            else {}
        )
        for field in ("related_resources", "historical_claims"):
            if field in metadata and not isinstance(metadata[field], list):
                issue(f"{sidecar.name}: {field} is not a list; ignoring that field")
                metadata[field] = []
        if "related_resources" in metadata:
            readings = metadata["related_resources"]
            usable = [reading for reading in readings if isinstance(reading, dict)]
            if len(usable) != len(readings):
                issue(f"{sidecar.name}: ignoring malformed reading entries")
            metadata["related_resources"] = usable
        heading = source.splitlines()[0].removeprefix(
            "# "
        ).strip() or path.stem.replace("-", " ")
        title_text = (
            entry.get("title") if isinstance(entry.get("title"), str) else heading
        )
        row = dict(
            id=key,
            title=re.sub(r"^\d{6}\s*[—–-]\s*", "", title_text),
            namespace=namespace,
            transcript=transcript,
            spoken_sha256=text_digest(transcript),
            source=source,
            metadata=metadata,
            sources=referenced_sources(metadata, source_catalog, issue),
            section=entry.get("section", ""),
            kind="audio",
            recordings=[],
        )
        if tags := topic_tags(topic_tags(plan.get("tags")) + topic_tags(entry.get("tags")) + topic_tags(metadata.get("tags"))):
            row["tags"] = tags
        companions, files, paths = discover_companions(directory, metadata, issue)
        companion_paths.extend(paths)
        if companions:
            row["companions"] = companions
            extra_files.update(files)
        row["revision"] = lecture_revision(row)
        lectures[key] = row
    course = dict(
        id=f"{namespace}:main",
        title=title,
        summary=plan.get("summary", old_course.get("summary", "")),
        background=plan.get("assumed_background", old_course.get("background", "")),
        sections=plan.get("sections", old_course.get("sections", [])),
        lectures=course_members,
        **collection_metadata(plan, namespace),
    )
    courses = route_collections(
        directory / "navigation.json",
        course,
        known=set(course_members),
        lecture_sections={
            f"{namespace}:{entry['id']}": entry.get("section", "") for entry in entries
        },
        previous=previous.get("courses"),
        issue=issue,
    )
    return dict(
        id=namespace,
        title=title,
        lectures=lectures,
        courses=courses,
        relationships=[],
        extra_files=extra_files,
        companion_paths=sorted(set(companion_paths)),
        warnings=warnings,
    )


class RepositoryCatalog:
    def __init__(self, root):
        self.root = Path(root).resolve()
        self._stamp = None
        self._packs = {}
        self.errors = []
        self._lock = threading.RLock()
        self._cache = self.root / ".content-state"
        self._directories = {}
        self._fingerprints = {}
        self._warnings = {}
        self._extras_pending = set()
        # Parsed snapshots are valid only for the code that interpreted them.
        self._implementation = digest(
            [
                file_digest(Path(__file__).with_name(filename))
                for filename in (
                    "catalog.py",
                    "core.py",
                    "companions.py",
                    "navigation.py",
                    "organization.py",
                    "presentations.py",
                )
            ]
        )
        for path in self._cache.glob("*.json"):
            try:
                saved = read_json(path)
                if (self.root / saved["directory"]).is_dir():
                    saved["pack"]["extra_files"] = {}
                    self._packs[saved["pack"]["id"]] = saved["pack"]
                    self._directories[saved["directory"]] = saved["pack"]["id"]
                    self._extras_pending.add(saved["directory"])
                    if saved.get("implementation") == self._implementation:
                        self._fingerprints[saved["directory"]] = saved.get(
                            "fingerprint"
                        )
                        self._warnings[saved["directory"]] = saved.get("warnings", [])
            except (OSError, ValueError, KeyError, TypeError):
                continue

    def _fingerprint(self, rel, entries, pack):
        entries = list(entries)
        for relative in (pack or {}).get("companion_paths", []):
            path = contained(self.root / rel, relative)
            try:
                stat = path.stat()
                values = (stat.st_mtime_ns, stat.st_size, stat.st_ctime_ns)
            except FileNotFoundError:
                values = (None, None, None)
            entries.append((relative, *values))
        return digest(entries)

    def _extras(self, directory, pack):
        """Restore export inputs without reparsing cached lecture manuscripts."""
        warnings = []
        for extra in (
            directory / "README.md",
            directory / "provenance.yaml",
            *sorted((directory / "examples").glob("*.json")),
        ):
            if extra.is_file():
                try:
                    pack["extra_files"][
                        extra.relative_to(directory).as_posix()
                    ] = extra.read_bytes()
                except OSError as exc:
                    warnings.append(f"{directory.name}/{extra.name}: {exc}")
        for row in pack["lectures"].values():
            for companion in row.get("companions", []):
                pack["extra_files"][companion["path"]] = contained(
                    directory, companion["path"]
                )
        return warnings

    def _retain(self, rel, pack, fingerprint, warnings):
        saved = {
            "directory": rel,
            "pack": {k: v for k, v in pack.items() if k != "extra_files"},
            "fingerprint": fingerprint,
            "implementation": self._implementation,
            "warnings": warnings,
        }
        atomic_bytes(
            self._cache / (digest(rel) + ".json"),
            json.dumps(saved, ensure_ascii=False).encode(),
        )
        self._fingerprints[rel] = fingerprint
        self._warnings[rel] = warnings
        self._extras_pending.discard(rel)

    @property
    def change_token(self):
        return self._stamp

    def snapshot(self, *, copy=True):
        with self._lock:
            try:
                with source_lock(self.root):
                    return self._read_snapshot(copy=copy)
            except (OSError, ValueError, KeyError) as exc:
                self.errors = [
                    f"Source update unavailable: {exc}; serving the last published catalog"
                ]
                return deepcopy(self._packs) if copy else self._packs

    def companion_file(self, lecture_id, identifier, expected):
        namespace = lecture_id.split(":")[0]
        with self._lock, source_lock(self.root):
            pack = self._read_snapshot(copy=False)[namespace]
            directory = next(
                directory
                for directory, pack_id in self._directories.items()
                if pack_id == namespace
            )
            return companion_file(
                self.root / directory,
                pack["lectures"][lecture_id].get("companions", []),
                identifier,
                expected,
            )

    def _read_snapshot(self, *, copy=True):
        with self._lock:
            drafts = self.root / "draft-stages"
            paths = sorted(
                p
                for p in drafts.glob("tts-*/*")
                if p.is_file()
                and (
                    p.name in {"track.json", "navigation.json"}
                    or LECTURE_FILE.fullmatch(p.name)
                )
            )
            paths += sorted(drafts.glob("tts-*/metadata/*.json"))
            paths += sorted(drafts.glob("tts-*/examples/*.json"))
            paths += sorted(drafts.glob("tts-*/README.md"))
            paths += sorted(drafts.glob("tts-*/provenance.yaml"))
            content = self.root / "content"
            directories = sorted(drafts.glob("tts-*")) + sorted(
                p
                for p in content.glob("*")
                if p.is_dir()
                and (
                    (p / "track.json").is_file()
                    or any(LECTURE_FILE.fullmatch(f.name) for f in p.glob("*.md"))
                )
            )
            paths += sorted(
                p
                for p in content.rglob("*")
                if p.is_file() and p.suffix in {".json", ".md"}
            )
            paths += sorted(content.glob("*/provenance.yaml"))
            paths += sorted(
                p
                for p in (self.root / "lectures").rglob("*")
                if p.is_file() and p.suffix in {".yaml", ".md"}
            )
            paths += sorted((self.root / "curriculum").glob("*.json"))
            # Watch declared companions only; do not scan generated caches/media.
            companion_stamps = []
            for pack in self._packs.values():
                directory = next(
                    (
                        self.root / rel
                        for rel, pack_id in self._directories.items()
                        if pack_id == pack["id"]
                    ),
                    None,
                )
                if directory:
                    for relative_path in pack.get("companion_paths", []):
                        path = contained(directory, relative_path)
                        try:
                            stat = path.stat()
                            companion_stamps.append(
                                (
                                    str(path),
                                    stat.st_mtime_ns,
                                    stat.st_size,
                                    stat.st_ctime_ns,
                                )
                            )
                        except FileNotFoundError:
                            companion_stamps.append((str(path), None, None))
            file_stamps = []
            for path in paths:
                stat = path.stat()
                file_stamps.append(
                    (str(path), stat.st_mtime_ns, stat.st_size, stat.st_ctime_ns)
                )
            stamp = tuple(file_stamps) + tuple(companion_stamps)
            if stamp != self._stamp:
                grouped = {}
                for entry in file_stamps:
                    relative = Path(entry[0]).relative_to(self.root)
                    parts = relative.parts
                    rel = (
                        "/".join(parts[:2])
                        if parts[0] in {"draft-stages", "content"}
                        else parts[0]
                    )
                    grouped.setdefault(rel, []).append(
                        (relative.as_posix(), *entry[1:])
                    )
                packs = dict(self._packs)
                errors = []
                existing = set()
                for directory in directories:
                    if not (directory / "track.json").exists() and not any(
                        LECTURE_FILE.fullmatch(f.name) for f in directory.glob("*.md")
                    ):
                        continue
                    try:
                        rel = directory.relative_to(self.root).as_posix()
                        previous_id = self._directories.get(rel)
                        fingerprint = self._fingerprint(
                            rel, grouped.get(rel, []), packs.get(previous_id)
                        )
                        if (
                            previous_id in packs
                            and self._fingerprints.get(rel) == fingerprint
                        ):
                            pack = packs[previous_id]
                            if pack["id"] in existing:
                                raise ValueError(
                                    f"Duplicate track namespace: {pack['id']}"
                                )
                            existing.add(pack["id"])
                            errors.extend(self._warnings.get(rel, []))
                            if rel in self._extras_pending:
                                errors.extend(self._extras(directory, pack))
                                self._extras_pending.discard(rel)
                            continue
                        pack = repository_track(
                            directory, previous=packs.get(previous_id)
                        )
                        warnings = pack.pop("warnings", [])
                        if pack["id"] in existing:
                            raise ValueError(f"Duplicate track namespace: {pack['id']}")
                        existing.add(pack["id"])
                        warnings.extend(self._extras(directory, pack))
                        errors.extend(warnings)
                        fingerprint = self._fingerprint(rel, grouped.get(rel, []), pack)
                        packs[pack["id"]] = pack
                        self._directories[rel] = pack["id"]
                        try:
                            self._retain(rel, pack, fingerprint, warnings)
                        except (OSError, ValueError) as exc:
                            errors.append(
                                f"{directory.name}: could not retain its published snapshot: {exc}"
                            )
                    except (OSError, ValueError, KeyError, TypeError) as exc:
                        errors.append(f"{directory.name}: {exc}")
                        # A partially written update cannot erase the previous snapshot.
                        previous = next(
                            (
                                k
                                for k in packs
                                if directory.name
                                in {
                                    k,
                                    f"tts-{k}",
                                    (
                                        "tts-lectures"
                                        if k == "g2"
                                        else "tts-paper" if k == "g3" else ""
                                    ),
                                }
                            ),
                            None,
                        )
                        if previous:
                            existing.add(previous)
                if (self.root / "lectures" / "index.yaml").exists():
                    try:
                        fingerprint = digest(grouped.get("lectures", []))
                        if (
                            "g1" not in packs
                            or self._fingerprints.get("lectures") != fingerprint
                        ):
                            from .presentations import presentation_pack

                            packs["g1"] = presentation_pack(self.root)
                            self._directories["lectures"] = "g1"
                            self._retain("lectures", packs["g1"], fingerprint, [])
                        existing.add("g1")
                    except (ImportError, OSError, ValueError, KeyError) as exc:
                        errors.append(f"g1: {exc}")
                        if "g1" in packs:
                            existing.add("g1")
                aliases = {
                    alias: row["id"]
                    for pack in packs.values()
                    for row in pack["lectures"].values()
                    for alias in row.get("aliases", [])
                }
                for pack in packs.values():
                    pack["relationships"] = [
                        r for r in pack["relationships"] if not r.get("_curriculum")
                    ]
                for relations in sorted(
                    (self.root / "curriculum").glob("*relationships.json")
                ):
                    try:
                        for edge in read_json(relations).get("edges", []):
                            source, relation, target, *reason = edge
                            evidence = {"from": source, "to": target}
                            if reason:
                                evidence["why"] = reason[0]
                            source, target = (
                                aliases.get(source, source),
                                aliases.get(target, target),
                            )
                            namespace = source.split(":")[0]
                            if namespace not in existing:
                                # Planned/uninstalled sources still carry real authored
                                # evidence. Transfer it with an installed endpoint, or
                                # a deterministic source pack if both ends are optional.
                                target_namespace = target.split(":")[0]
                                namespace = target_namespace if target_namespace in existing else next(iter(sorted(existing)), None)
                            if namespace in existing:
                                record = {
                                    "from": source,
                                    "type": relation,
                                    "to": target,
                                    "_curriculum": True,
                                    "component_relations": [evidence],
                                    "evidence_source": relations.relative_to(self.root).as_posix(),
                                }
                                if reason:
                                    record["why"] = reason[0]
                                packs[namespace]["relationships"].append(record)
                    except (OSError, ValueError, KeyError, TypeError) as exc:
                        errors.append(f"{relations.name}: {exc}")
                self._packs = {k: v for k, v in packs.items() if k in existing}
                self.errors = errors
                self._stamp = stamp
            return deepcopy(self._packs) if copy else self._packs

    def generation(self):
        return digest(
            {
                k: {i: r["revision"] for i, r in p["lectures"].items()}
                | {"courses": p["courses"]}
                for k, p in self.snapshot().items()
            }
        )
