"""Combine live authored sources and immutable installed media without TTS."""

from __future__ import annotations

from copy import deepcopy
import json
import threading

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
        self._lock = threading.RLock()
        self._snapshot_key = None
        with self.store.connect() as db:
            db.execute(
                "CREATE TABLE IF NOT EXISTS source_snapshots (release TEXT PRIMARY KEY, catalog TEXT NOT NULL)"
            )
            db.execute(
                "CREATE TABLE IF NOT EXISTS cleared_recordings (lecture TEXT, recording TEXT, PRIMARY KEY (lecture,recording))"
            )
            self._saved_snapshots = {
                row[0] for row in db.execute("SELECT release FROM source_snapshots")
            }

    def clear_recordings(self, lecture_id, recordings):
        # Immutable releases remain available to historical links and later GC.
        with self.store.connect() as db:
            db.executemany(
                "INSERT OR IGNORE INTO cleared_recordings VALUES (?,?)",
                [(lecture_id, r["id"]) for r in recordings],
            )

    def snapshot(self, *, refresh=False, copy=True):
        """Reuse unchanged compositions; copy=False is for read-only callers."""
        with self._lock:
            if refresh:
                self.store.reconcile(force=True)
            installed = self.store.snapshot(copy=False)
            sources = self.repository.snapshot(copy=False) if self.repository else {}
            with self.store.connect() as db:
                cleared = tuple(
                    tuple(row)
                    for row in db.execute(
                        "SELECT lecture,recording FROM cleared_recordings ORDER BY lecture,recording"
                    )
                )
            key = (
                cleared,
                installed["generation"],
                self.repository.change_token if self.repository else None,
                tuple(self.store.errors),
                tuple(self.repository.errors) if self.repository else (),
            )
            if key != self._snapshot_key:
                self._snapshot_cache = self._compose(installed, sources, cleared)
                self._snapshot_key = key
            return deepcopy(self._snapshot_cache) if copy else self._snapshot_cache

    def _compose(self, installed, sources, cleared=()):
        result = deepcopy(installed)
        hidden = set(cleared)
        for row in [
            *result["lectures"].values(),
            *(
                row
                for rows in result.get("media_revisions", {}).values()
                for row in rows
            ),
        ]:
            row["recordings"] = [
                r for r in row["recordings"] if (row["id"], r["id"]) not in hidden
            ]
        for pack_id, pack in sources.items():
            # Composition replaces recordings/origin; authored fields stay
            # read-only, like the courses already shared with this snapshot.
            source_rows = {key: dict(row) for key, row in pack["lectures"].items()}
            for key, row in source_rows.items():
                old = result["lectures"].get(key)
                candidates = ([old] if old else []) + result.get(
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
                "installed": (
                    digest([installed["generation"], cleared])
                    if cleared
                    else installed["generation"]
                ),
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
