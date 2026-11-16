"""Combine live authored sources and immutable installed media without TTS."""

from __future__ import annotations

from copy import deepcopy
import json

from .catalog import RepositoryCatalog
from .core import canonical, digest
from .packs import PackStore


class Library:
    def __init__(
        self,
        root,
        *,
        repository=None,
        discovery_roots=(),
        interval=2,
        pins=None,
        excluded=(),
    ):
        self.store = PackStore(
            root,
            discovery_roots=discovery_roots,
            interval=interval,
            pins=pins,
            excluded=excluded,
        )
        self.repository = RepositoryCatalog(repository) if repository else None
        self._saved_snapshots = set()
        with self.store.connect() as db:
            db.execute(
                "CREATE TABLE IF NOT EXISTS source_snapshots (release TEXT PRIMARY KEY, catalog TEXT NOT NULL)"
            )

    def snapshot(self, *, refresh=False):
        if refresh:
            self.store.reconcile(force=True)
        installed = self.store.snapshot()
        result = deepcopy(installed)
        sources = self.repository.snapshot() if self.repository else {}
        for pack_id, pack in sources.items():
            source_rows = deepcopy(pack["lectures"])
            for key, row in source_rows.items():
                old = result["lectures"].get(key)
                candidates = ([old] if old else []) + installed.get(
                    "media_revisions", {}
                ).get(key, [])
                recordings = {
                    r["id"]: r
                    for version in candidates
                    for r in version["recordings"]
                    if r["spoken_sha256"] == row["spoken_sha256"]
                }
                row["recordings"] = list(recordings.values())
            source_release = digest(
                {
                    "lectures": {
                        key: row["revision"] for key, row in source_rows.items()
                    },
                    "recordings": {
                        key: [(r["id"], r["_release"]) for r in row["recordings"]]
                        for key, row in source_rows.items()
                    },
                    "courses": pack["courses"],
                    "relationships": pack.get("relationships", []),
                }
            )
            for key, row in source_rows.items():
                row["origin"] = {
                    "pack": pack_id,
                    "release": source_release,
                    "source": True,
                }
                result["lectures"][key] = row
            result["courses"].update(pack["courses"])
            result["relationships"].extend(pack.get("relationships", []))
            if source_release not in self._saved_snapshots:
                with self.store.connect() as db:
                    db.execute(
                        "INSERT OR IGNORE INTO source_snapshots VALUES (?,?)",
                        (source_release, canonical(source_rows).decode()),
                    )
                self._saved_snapshots.add(source_release)
            result["packs"] = [p for p in result["packs"] if p["id"] != pack_id]
            result["packs"].append(
                {
                    "id": pack_id,
                    "title": pack["title"],
                    "release": source_release,
                    "source": True,
                    "count": len(pack["lectures"]),
                }
            )
        result["generation"] = digest(
            {
                "installed": installed["generation"],
                "sources": [p["release"] for p in result["packs"]],
            }
        )
        # A source release plus independently installed media is a composed view.
        # Retain that view so feedback can resolve its selected recording even
        # though the original source-only catalog did not contain the add-on.
        installed_groups = {}
        for key, row in result["lectures"].items():
            if not row.get("origin", {}).get("source"):
                installed_groups.setdefault(row["origin"]["release"], {})[key] = row
        for pack_release, rows in installed_groups.items():
            view = digest(
                {
                    "pack_release": pack_release,
                    "lectures": {key: row["revision"] for key, row in rows.items()},
                    "recordings": {
                        key: [(r["id"], r["_release"]) for r in row["recordings"]]
                        for key, row in rows.items()
                    },
                }
            )
            for row in rows.values():
                row["origin"] = dict(
                    row["origin"], release=view, pack_release=pack_release
                )
            if view not in self._saved_snapshots:
                with self.store.connect() as db:
                    db.execute(
                        "INSERT OR IGNORE INTO source_snapshots VALUES (?,?)",
                        (view, canonical(rows).decode()),
                    )
                self._saved_snapshots.add(view)
        result["aliases"] = {
            alias: row["id"]
            for row in result["lectures"].values()
            for alias in row.get("aliases", [])
        }
        result["errors"] = self.store.errors + (
            self.repository.errors if self.repository else []
        )
        result["errors"] += [
            f"{key}: multiple recorded transcript revisions; select a source release"
            for key in result.get("conflicts", [])
            if key not in result["lectures"]
        ]
        return result

    def historical(self, release, lecture_id):
        with self.store.connect() as db:
            row = db.execute(
                "SELECT catalog FROM source_snapshots WHERE release=?", (release,)
            ).fetchone()
        if row:
            return json.loads(row["catalog"])[lecture_id]
        return self.store.historical(release, lecture_id)[0]

    def remember_playback(self, row):
        """Bind in-progress playback and feedback to the exact completed blocks."""
        release = digest(row)
        row = deepcopy(row)
        row["origin"] = dict(
            pack="audio-" + digest(row["id"])[:24], release=release, preparing=True
        )
        if release not in self._saved_snapshots:
            with self.store.connect() as db:
                db.execute(
                    "INSERT OR IGNORE INTO source_snapshots VALUES (?,?)",
                    (release, canonical({row["id"]: row}).decode()),
                )
            self._saved_snapshots.add(release)
        return row
