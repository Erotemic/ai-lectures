"""Live repository adapters; no synthesis configuration or rendering imports."""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path
import re
import threading

from .core import digest, extract_text, lecture_revision, name, read_json, text_digest

LECTURE_FILE = re.compile(r"^([0-9]{6})-.*\.md$")


def referenced_sources(metadata, sources):
    keys = {r["source_id"] for r in metadata.get("related_resources", [])}
    keys.update(
        key
        for claim in metadata.get("historical_claims", [])
        for key in claim.get("source_ids", [])
    )
    missing = keys - sources.keys()
    if missing:
        raise ValueError(f"Undefined reading sources: {sorted(missing)}")
    return {key: sources[key] for key in sorted(keys)}


def repository_track(directory):
    directory = Path(directory)
    manifest = directory / "track.json"
    plan = (
        read_json(manifest)
        if manifest.exists()
        else {
            "id": "g2",
            "title": "Operator Theory and Spectral Perturbation",
            "summary": "Comprehensive audio lectures from foundations through Davis–Kahan.",
            "lectures": [
                {"id": p.name[:6], "file": p.name}
                for p in sorted(directory.glob("*.md"))
                if LECTURE_FILE.fullmatch(p.name)
            ],
        }
    )
    namespace = name(plan["id"])
    rows = plan["lectures"]
    files = {p.name for p in directory.glob("*.md") if LECTURE_FILE.fullmatch(p.name)}
    names = [row["file"] for row in rows]
    ids = [row["id"] for row in rows]
    if (
        len(set(ids)) != len(ids)
        or len(set(names)) != len(names)
        or set(names) != files
    ):
        raise ValueError(f"{namespace}: manifest does not match manuscripts")
    source_path = directory / "metadata" / "sources.json"
    if not source_path.exists():
        source_path = directory.parent / "tts-lectures" / "metadata" / "sources.json"
    source_catalog = (
        read_json(source_path).get("sources", {}) if source_path.exists() else {}
    )
    lectures = {}
    for entry in rows:
        filename = entry["file"]
        if not LECTURE_FILE.fullmatch(filename) or filename[:6] != entry["id"]:
            raise ValueError(f"{namespace}: invalid lecture filename")
        path = directory / filename
        source = path.read_text(encoding="utf-8")
        transcript = extract_text(source, str(path)).strip()
        sidecar = directory / "metadata" / (entry["id"] + ".json")
        metadata = read_json(sidecar) if sidecar.exists() else {}
        title = entry.get("title") or source.splitlines()[0].removeprefix("# ").strip()
        title = re.sub(r"^\d{6}\s*[—–-]\s*", "", title)
        row = dict(
            id=f'{namespace}:{entry["id"]}',
            title=title,
            namespace=namespace,
            transcript=transcript,
            spoken_sha256=text_digest(transcript),
            source=source,
            metadata=metadata,
            sources=referenced_sources(metadata, source_catalog),
            section=entry.get("section", ""),
            kind="audio",
            recordings=[],
        )
        row["revision"] = lecture_revision(row)
        lectures[row["id"]] = row
    course = dict(
        id=f"{namespace}:main",
        title=plan["title"],
        summary=plan.get("summary", ""),
        background=plan.get("assumed_background", ""),
        sections=plan.get("sections", []),
        lectures=list(lectures),
    )
    return dict(
        id=namespace,
        title=plan["title"],
        lectures=lectures,
        courses={course["id"]: course},
        relationships=[],
        extra_files={},
    )


class RepositoryCatalog:
    def __init__(self, root):
        self.root = Path(root).resolve()
        self._stamp = None
        self._packs = {}
        self.errors = []
        self._lock = threading.RLock()

    def snapshot(self):
        with self._lock:
            drafts = self.root / "draft-stages"
            paths = sorted(
                p
                for p in drafts.glob("tts-*/*")
                if p.is_file()
                and (p.name == "track.json" or LECTURE_FILE.fullmatch(p.name))
            )
            paths += sorted(drafts.glob("tts-*/metadata/*.json"))
            paths += sorted(drafts.glob("tts-*/examples/*.json"))
            content = self.root / "content"
            directories = sorted(drafts.glob("tts-*")) + sorted(
                p for p in content.glob("*") if (p / "track.json").is_file()
            )
            paths += sorted(
                p
                for p in content.rglob("*")
                if p.is_file() and p.suffix in {".json", ".md"}
            )
            paths += sorted(
                p
                for p in (self.root / "lectures").rglob("*")
                if p.is_file() and p.suffix in {".yaml", ".md"}
            )
            paths += sorted((self.root / "curriculum").glob("*.json"))
            stamp = tuple(
                (str(p), p.stat().st_mtime_ns, p.stat().st_size) for p in paths
            )
            if stamp != self._stamp:
                packs = dict(self._packs)
                errors = []
                existing = set()
                for directory in directories:
                    if (
                        not (directory / "track.json").exists()
                        and directory.name != "tts-lectures"
                    ):
                        continue
                    try:
                        pack = repository_track(directory)
                        if pack["id"] in existing:
                            raise ValueError(f'Duplicate track namespace: {pack["id"]}')
                        existing.add(pack["id"])
                        for doc in ("README.md", "provenance.yaml"):
                            if (directory / doc).is_file():
                                pack["extra_files"][doc] = (
                                    directory / doc
                                ).read_bytes()
                        for example in sorted((directory / "examples").glob("*.json")):
                            pack["extra_files"][
                                "examples/" + example.name
                            ] = example.read_bytes()
                        packs[pack["id"]] = pack
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
                        from .presentations import presentation_pack

                        packs["g1"] = presentation_pack(self.root)
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
                            source, target = aliases.get(source, source), aliases.get(
                                target, target
                            )
                            namespace = source.split(":")[0]
                            if namespace in packs:
                                record = {
                                    "from": source,
                                    "type": relation,
                                    "to": target,
                                    "_curriculum": True,
                                }
                                if reason:
                                    record["why"] = reason[0]
                                packs[namespace]["relationships"].append(record)
                    except (OSError, ValueError, KeyError, TypeError) as exc:
                        errors.append(f"{relations.name}: {exc}")
                self._packs = {k: v for k, v in packs.items() if k in existing}
                self.errors = errors
                self._stamp = stamp
            return deepcopy(self._packs)

    def generation(self):
        return digest(
            {
                k: {i: r["revision"] for i, r in p["lectures"].items()}
                | {"courses": p["courses"]}
                for k, p in self.snapshot().items()
            }
        )
