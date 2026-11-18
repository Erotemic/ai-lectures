"""Explicit browser downloads of source packs and their published recordings.

Export never synthesizes, renders, scans legacy caches, or includes listener data.
The snapshot fixes transcript/media identity before any bytes are copied.
"""
from copy import deepcopy
import json
from pathlib import Path
import re
import shutil
import tempfile
from uuid import uuid4

from .maintenance import media_operation
from .core import name
from .packs import archive_release, export_release, load_release


@media_operation
def export_pack(library, pack_id, *, source_only=False):
    name(pack_id)
    if not isinstance(source_only, bool):
        raise ValueError("source_only must be true or false")
    snapshot = library.snapshot(copy=False)
    selected = next((pack for pack in snapshot["packs"] if pack["id"] == pack_id), None)
    if not selected:
        raise KeyError("This pack is not installed")
    authored = library.repository.snapshot(copy=False).get(pack_id) if library.repository else None
    options = {}
    if authored is not None:
        pack = dict(authored)
    else:
        active = next(row for row in library.store.active() if row["pack_id"] == pack_id)
        original = load_release(active["directory"])
        manifest = original["manifest"]
        pack = dict(id=pack_id, title=manifest["title"], **original["catalog"])
        media_paths = {
            segment["path"]
            for row in pack["lectures"].values()
            for recording in row["recordings"]
            for segment in recording["segments"]
        }
        pack["extra_files"] = {
            relative: Path(active["directory"]) / relative
            for relative in original["checksums"]
            if relative != "catalog.json" and relative not in media_paths
        }
        options = dict(kind=manifest["kind"], parent=manifest.get("parent"), dependencies=manifest.get("dependencies", {}))
    rows, media = {}, []
    for key, original in pack["lectures"].items():
        current = snapshot["lectures"].get(key)
        row = current if current and current["spoken_sha256"] == original["spoken_sha256"] else original
        rows[key] = deepcopy(row)
        for recording in ([] if source_only else row.get("recordings", [])):
            public = deepcopy(recording)
            for field in list(public):
                if field.startswith("_"):
                    public.pop(field)
            files = {}
            for original_segment, segment in zip(recording["segments"], public["segments"]):
                release = original_segment.get("_release", recording.get("_release"))
                if release:
                    path, _ = library.store.media_file(release, original_segment.get("_recording", recording["id"]), segment["index"])
                elif authored is None:
                    path = Path(active["directory"]) / segment["path"]
                else:
                    raise ValueError("Finish publishing this recording before exporting it")
                files[segment["path"]] = path
                for field in list(segment):
                    if field.startswith("_"):
                        segment.pop(field)
            media.append((key, public, files))
    pack["lectures"] = rows
    output = library.store.root / "exports"
    output.mkdir(parents=True, exist_ok=True)
    ticket = uuid4().hex
    with tempfile.TemporaryDirectory(prefix=".export-", dir=output) as temporary:
        stage = Path(temporary)
        release = export_release(pack, stage / "release", media=media, **options)
        archive_release(stage / "release", stage / "pack.zip")
        shutil.rmtree(stage / "release")
        receipt = dict(id=ticket, pack_id=pack_id, release=release["release"], source_only=source_only,
                       lectures=len(rows), recordings=len(media), bytes=(stage / "pack.zip").stat().st_size,
                       filename=f"{pack_id}-{release['release'][:12]}.zip")
        (stage / "receipt.json").write_text(json.dumps(receipt), encoding="utf-8")
        stage.rename(output / ticket)
    return receipt


def export_file(library, ticket):
    if not isinstance(ticket, str) or not re.fullmatch(r"[a-f0-9]{32}", ticket):
        raise ValueError("Invalid export identifier")
    directory = library.store.root / "exports" / ticket
    receipt = json.loads((directory / "receipt.json").read_text())
    return directory / "pack.zip", receipt["filename"]
