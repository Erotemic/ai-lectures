"""Optional pack-local companions; no renderer is needed to read their links."""

import mimetypes

from .core import checksum, contained, file_digest, name, relative


def available_companions(row):
    """Optional malformed records never prevent browsing the spoken lecture."""
    declared = row.get("companions", [])
    for item in declared if isinstance(declared, list) else []:
        try:
            name(item["id"])
            relative(item["path"])
            checksum(item["sha256"])
            if not isinstance(item["media_type"], str):
                continue
            yield item
        except (KeyError, TypeError, ValueError):
            continue


def discover_companions(directory, metadata, issue):
    declared = metadata.get("companions", [])
    if not isinstance(declared, list):
        issue("companions must be a list; ignoring optional companions")
        return [], {}, []
    companions, files, seen, paths = [], {}, set(), []
    for item in declared:
        try:
            identifier = name(item["id"])
            if identifier in seen:
                raise ValueError("duplicate companion ID")
            path = contained(directory, item["path"])
            paths.append(item["path"])
            if not path.is_file():
                raise ValueError("companion file is unavailable")
            role = item.get("role", "prepared")
            if role not in {"source", "prepared"}:
                raise ValueError("companion role must be source or prepared")
            binding = item.get("input_spoken_sha256")
            if binding is not None:
                checksum(binding)
            row = dict(
                id=identifier,
                title=str(item.get("title") or identifier),
                path=item["path"],
                role=role,
                media_type=mimetypes.guess_type(path.name)[0]
                or "application/octet-stream",
                sha256=file_digest(path),
            )
            for field in ("attribution", "input_spoken_sha256", "recipe"):
                if field in item:
                    row[field] = item[field]
            companions.append(row)
            files[item["path"]] = path
            seen.add(identifier)
        except (OSError, ValueError, KeyError, TypeError) as exc:
            issue(f"Optional companion unavailable: {exc}")
    return companions, files, paths


def companion_file(directory, companions, identifier, expected):
    """An old source link must never silently return revised companion bytes."""
    checksum(expected)
    row = next((item for item in companions if item["id"] == identifier), None)
    if row is None:
        raise KeyError("Companion is unavailable")
    path = contained(directory, row["path"])
    if row["sha256"] != expected or file_digest(path) != expected:
        from .core import Conflict

        raise Conflict("Companion has changed; reopen the lecture to load its update")
    return path, row
