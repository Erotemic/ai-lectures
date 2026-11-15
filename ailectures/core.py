"""Dependency-free content identities and canonical speech extraction."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path, PurePosixPath
import re

SCHEMA_VERSION = 1
NAME = re.compile(r"^[a-z0-9][a-z0-9._-]{0,95}$")
QUALIFIED = re.compile(r"^[a-z0-9][a-z0-9._-]{0,95}:[a-zA-Z0-9][a-zA-Z0-9._-]{0,127}$")
SHA256 = re.compile(r"^[a-f0-9]{64}$")
BEGIN = "<!-- BEGIN SPOKEN LECTURE -->"
END = "<!-- END SPOKEN LECTURE -->"


class Conflict(ValueError):
    """A stale update or conflicting identity would overwrite existing work."""


def canonical(value):
    return json.dumps(
        value,
        sort_keys=True,
        ensure_ascii=False,
        separators=(",", ":"),
        allow_nan=False,
    ).encode("utf-8")


def digest(value):
    return hashlib.sha256(
        value if isinstance(value, bytes) else canonical(value)
    ).hexdigest()


def text_digest(text):
    return digest(text.encode("utf-8"))


def file_digest(path):
    with Path(path).open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def read_json(path):
    def unique(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"Duplicate JSON key: {key}")
            result[key] = value
        return result

    return json.loads(
        Path(path).read_text(encoding="utf-8"),
        object_pairs_hook=unique,
        parse_constant=lambda x: (_ for _ in ()).throw(
            ValueError(f"Invalid number: {x}")
        ),
    )


def write_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(canonical(value) + b"\n")


def name(value):
    if not isinstance(value, str) or not NAME.fullmatch(value):
        raise ValueError("Invalid pack or variant name")
    return value


def qualified(value):
    if not isinstance(value, str) or not QUALIFIED.fullmatch(value):
        raise ValueError("Expected a qualified identifier")
    return value


def checksum(value):
    if not isinstance(value, str) or not SHA256.fullmatch(value):
        raise ValueError("Expected a SHA-256 digest")
    return value


def finite(value, minimum=0):
    if (
        isinstance(value, bool)
        or not isinstance(value, (int, float))
        or not math.isfinite(value)
        or value < minimum
    ):
        raise ValueError("Expected a finite nonnegative number")
    return value


def relative(value):
    if not isinstance(value, str) or "\\" in value or "\x00" in value:
        raise ValueError("Invalid pack path")
    path = PurePosixPath(value)
    if (
        path.is_absolute()
        or not path.parts
        or any(p in {".", ".."} or p.startswith(".") for p in path.parts)
        or str(path) != value
    ):
        raise ValueError("Pack paths must be normalized relative paths")
    return value


def contained(root, value):
    relative(value)
    root = Path(root).resolve()
    path = root / value
    for parent in [path, *path.parents]:
        if parent == root:
            break
        if parent.is_symlink():
            raise ValueError("Pack symlinks are not supported")
    path.resolve().relative_to(root)
    return path


def extract_text(data, source="transcript"):
    if data.count(BEGIN) != 1 or data.count(END) != 1:
        raise ValueError(f"{source}: expected exactly one spoken-region marker pair")
    begin = data.index(BEGIN) + len(BEGIN)
    end = data.index(END)
    if begin >= end:
        raise ValueError(f"{source}: end marker precedes begin marker")
    spoken = data[begin:end].strip()
    if not spoken:
        raise ValueError(f"{source}: empty spoken portion")
    for token in ("```", "$$", "\\[", "\\(", "<script", "<!--"):
        if token in spoken:
            raise ValueError(f"{source}: non-spoken markup {token!r} within narration")
    spoken = re.sub(r"(?m)^#{1,6}\s+", "", spoken)
    spoken = re.sub(r"(?<!\*)\*\*([^\n*]+?)\*\*(?!\*)", r"\1", spoken)
    return re.sub(r"(?<!\w)(?<!\*)\*([^\n*]+?)\*(?!\w)", r"\1", spoken) + "\n"


def extract(path):
    return extract_text(Path(path).read_text(encoding="utf-8"), str(path))


def lecture_revision(row):
    return digest(
        {
            k: v
            for k, v in row.items()
            if k not in {"revision", "recordings", "origin", "url"}
        }
    )
