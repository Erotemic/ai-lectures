#!/usr/bin/env python3
"""Compare archived content with a checkout without applying or deleting anything."""

from __future__ import annotations
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
from zipfile import ZipFile

MANUSCRIPT = re.compile(r"(?:^|/)\d{6}-.+\.md$")


def inspect_archives(repository, inputs):
    root = Path(repository).resolve()
    archives = sorted(
        {
            p.resolve()
            for item in inputs
            for p in (Path(item).glob("*.zip") if Path(item).is_dir() else [Path(item)])
        }
    )
    archive_hashes, versions, results = {}, {}, []
    for archive in archives:
        sha = hashlib.sha256(archive.read_bytes()).hexdigest()
        item = dict(
            archive=str(archive),
            sha256=sha,
            duplicate_of=archive_hashes.get(sha),
            files=[],
            catalog_issues=[],
            missing_source_ids=[],
        )
        archive_hashes.setdefault(sha, str(archive))
        with ZipFile(archive) as bundle:
            names = [info.filename for info in bundle.infolist() if not info.is_dir()]
            if len(names) != len(set(names)):
                raise ValueError("Duplicate member paths in " + archive.name)
            for filename in names:
                path = PurePosixPath(filename)
                if path.is_absolute() or ".." in path.parts or "\\" in filename:
                    raise ValueError("Unsafe archive path: " + filename)
                target = root.joinpath(*path.parts)
                if not target.resolve().is_relative_to(root):
                    raise ValueError("Archive path escapes repository")
                data = bundle.read(filename)
                state = (
                    "missing"
                    if not target.is_file()
                    else "same" if target.read_bytes() == data else "different"
                )
                record = dict(path=filename, state=state)
                item["files"].append(record)
                if MANUSCRIPT.search(filename):
                    versions[(filename, hashlib.sha256(data).hexdigest())] = record
                if target.is_file() and path.name == "track.json":
                    incoming, current = json.loads(data), json.loads(target.read_text())
                    current = {row["id"]: row for row in current.get("lectures", [])}
                    for row in incoming.get("lectures", []):
                        other = current.get(row["id"])
                        if other is None:
                            item["catalog_issues"].append(
                                dict(
                                    track=filename,
                                    id=row["id"],
                                    kind="missing_index_entry",
                                    incoming=row,
                                )
                            )
                        elif (row.get("file"), row.get("title")) != (
                            other.get("file"),
                            other.get("title"),
                        ):
                            item["catalog_issues"].append(
                                dict(
                                    track=filename,
                                    id=row["id"],
                                    kind="different_assignment",
                                    incoming=row,
                                    current=other,
                                )
                            )
                if target.is_file() and filename.endswith("/metadata/sources.json"):
                    incoming, current = json.loads(data).get("sources", {}), json.loads(
                        target.read_text()
                    ).get("sources", {})
                    if isinstance(incoming, dict) and isinstance(current, dict):
                        item["missing_source_ids"].extend(
                            sorted(set(incoming) - set(current))
                        )
        item["counts"] = dict(Counter(row["state"] for row in item["files"]))
        item["missing_manuscripts"] = [
            row["path"]
            for row in item["files"]
            if row["state"] == "missing" and MANUSCRIPT.search(row["path"])
        ]
        item["changed_manuscripts"] = [
            row["path"]
            for row in item["files"]
            if row["state"] == "different" and MANUSCRIPT.search(row["path"])
        ]
        results.append(item)
    counts = Counter(row["state"] for row in versions.values())
    return dict(
        scope="Byte comparison and indexed identities; not a semantic completeness judgment.",
        summary=dict(
            archives=len(results),
            unique_archives=len(archive_hashes),
            manuscript_versions=len(versions),
            matching_manuscripts=counts["same"],
            missing_manuscripts=counts["missing"],
            changed_manuscripts=counts["different"],
        ),
        archives=results,
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("inputs", nargs="+", type=Path)
    parser.add_argument(
        "--repository", type=Path, default=Path(__file__).resolve().parents[1]
    )
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = inspect_archives(args.repository, args.inputs)
    if args.output:
        args.output.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps(report["summary"], indent=2))


if __name__ == "__main__":
    main()
