"""Durable preparation requests and cross-process worker leases.

Only explicit preparation requests enter this queue. Backend configuration and
speech snapshots stay in ignored local state, outside portable content packs.
"""

from __future__ import annotations

from contextlib import contextmanager
import json
from pathlib import Path
import sqlite3
import time

from .core import canonical, checksum


class JobStore:
    def __init__(self, directory):
        self.database = Path(directory) / "production.sqlite3"
        self.database.parent.mkdir(parents=True, exist_ok=True)
        with self.connect() as db:
            db.execute("BEGIN IMMEDIATE")
            db.execute("""CREATE TABLE IF NOT EXISTS jobs (
                id TEXT PRIMARY KEY, specification TEXT NOT NULL,
                state TEXT NOT NULL, attempts INTEGER NOT NULL DEFAULT 0,
                retry_at REAL NOT NULL DEFAULT 0, owner TEXT, lease_until REAL,
                published TEXT, error TEXT, inventory TEXT,
                created_at REAL NOT NULL, updated_at REAL NOT NULL)""")
            if "requested_blocks" not in {
                row[1] for row in db.execute("PRAGMA table_info(jobs)")
            }:
                db.execute("ALTER TABLE jobs ADD COLUMN requested_blocks TEXT")

    @contextmanager
    def connect(self):
        db = sqlite3.connect(self.database, timeout=30)
        db.row_factory = sqlite3.Row
        try:
            with db:
                yield db
        finally:
            db.close()

    @staticmethod
    def decode(row):
        result = dict(row)
        result["specification"] = json.loads(result["specification"])
        result["inventory"] = (
            json.loads(result["inventory"]) if result["inventory"] else None
        )
        result["requested_blocks"] = (
            json.loads(result["requested_blocks"])
            if result["requested_blocks"] is not None
            else None
        )
        return result

    def get(self, job_id):
        checksum(job_id)
        with self.connect() as db:
            row = db.execute("SELECT * FROM jobs WHERE id=?", (job_id,)).fetchone()
        if row is None:
            raise KeyError("Unknown preparation job")
        return self.decode(row)

    def list(self, lecture_id=None):
        with self.connect() as db:
            where = (
                " WHERE json_extract(specification, '$.row.id')=?" if lecture_id else ""
            )
            return [
                self.decode(row)
                for row in db.execute(
                    "SELECT * FROM jobs" + where + " ORDER BY created_at,id",
                    (lecture_id,) if lecture_id else (),
                )
            ]

    def enqueue(self, specifications, *, blocks=None):
        now = time.time()
        with self.connect() as db:
            db.execute("BEGIN IMMEDIATE")
            for job_id, specification in specifications:
                checksum(job_id)
                data = canonical(specification).decode()
                requested = canonical(blocks).decode() if blocks is not None else None
                previous = db.execute(
                    "SELECT * FROM jobs WHERE id=?", (job_id,)
                ).fetchone()
                if previous is None:
                    db.execute(
                        "INSERT INTO jobs (id,specification,state,created_at,updated_at,requested_blocks) VALUES (?,?,?,?,?,?)",
                        (job_id, data, "queued", now, now, requested),
                    )
                elif previous["specification"] != data:
                    raise ValueError(
                        "Preparation identity has conflicting specifications"
                    )
                elif previous["state"] in {"failed", "cancelled", "settings_changed"}:
                    db.execute(
                        "UPDATE jobs SET state='queued',attempts=0,retry_at=0,error=NULL,owner=NULL,lease_until=NULL,published=NULL,requested_blocks=?,updated_at=? WHERE id=?",
                        (requested, now, job_id),
                    )
                else:
                    old_blocks = (
                        json.loads(previous["requested_blocks"])
                        if previous["requested_blocks"] is not None
                        else None
                    )
                    combined = (
                        blocks
                        if previous["state"] == "ready"
                        else (
                            sorted(set(old_blocks) | set(blocks))
                            if old_blocks is not None and blocks is not None
                            else None
                        )
                    )
                    merged = (
                        canonical(combined).decode() if combined is not None else None
                    )
                    if merged != previous["requested_blocks"]:
                        if previous["state"] == "ready":
                            db.execute(
                                "UPDATE jobs SET requested_blocks=?,state='queued',attempts=0,retry_at=0,owner=NULL,lease_until=NULL,published=NULL,error=NULL,updated_at=? WHERE id=?",
                                (merged, now, job_id),
                            )
                        else:
                            db.execute(
                                "UPDATE jobs SET requested_blocks=?,published=NULL,updated_at=? WHERE id=?",
                                (merged, now, job_id),
                            )

    def claim(self, owner, *, limit=2, lease_seconds=60):
        now = time.time()
        with self.connect() as db:
            db.execute("BEGIN IMMEDIATE")
            db.execute(
                "UPDATE jobs SET state='queued',owner=NULL,lease_until=NULL,updated_at=? WHERE state='running' AND lease_until<?",
                (now, now),
            )
            active = db.execute(
                "SELECT count(*) FROM jobs WHERE state='running'"
            ).fetchone()[0]
            capacity = max(0, limit - active)
            interactive_only = (
                limit > 0
                and capacity == 0
                and not db.execute(
                    "SELECT 1 FROM jobs WHERE state='running' AND requested_blocks IS NOT NULL LIMIT 1"
                ).fetchone()
            )
            # Keep one slot available for explicitly selected blocks even when
            # background whole-lecture preparations fill the normal capacity.
            scope = " AND requested_blocks IS NOT NULL" if interactive_only else ""
            candidates = db.execute(
                "SELECT id FROM jobs WHERE state='queued' AND retry_at<=?"
                + scope
                + " ORDER BY requested_blocks IS NULL,created_at,id LIMIT ?",
                (now, 1 if interactive_only else capacity),
            ).fetchall()
            for row in candidates:
                db.execute(
                    "UPDATE jobs SET state='running',owner=?,lease_until=?,attempts=attempts+1,updated_at=? WHERE id=?",
                    (owner, now + lease_seconds, now, row["id"]),
                )
        return [self.get(row["id"]) for row in candidates]

    def heartbeat(self, owner, lease_seconds=60):
        with self.connect() as db:
            db.execute(
                "UPDATE jobs SET lease_until=? WHERE owner=? AND state='running'",
                (time.time() + lease_seconds, owner),
            )

    def save(self, job_id, owner, *, inventory=None, published=None):
        now = time.time()
        with self.connect() as db:
            changed = db.execute(
                """UPDATE jobs SET inventory=?,published=COALESCE(?,published),
                state=CASE WHEN ? IS NULL THEN state ELSE 'ready' END,error=NULL,updated_at=?
                WHERE id=? AND owner=? AND state='running' """,
                (
                    canonical(inventory).decode() if inventory else None,
                    published,
                    published,
                    now,
                    job_id,
                    owner,
                ),
            ).rowcount
        return bool(changed)

    def fail(self, job_id, owner, error, *, retry=True, max_attempts=3, delay=5):
        now = time.time()
        with self.connect() as db:
            db.execute("BEGIN IMMEDIATE")
            row = db.execute(
                "SELECT * FROM jobs WHERE id=? AND owner=? AND state='running'",
                (job_id, owner),
            ).fetchone()
            if row:
                state = (
                    "queued"
                    if retry and row["attempts"] < max_attempts
                    else "failed"
                    if retry
                    else "settings_changed"
                )
                db.execute(
                    "UPDATE jobs SET state=?,error=?,retry_at=?,owner=NULL,lease_until=NULL,updated_at=? WHERE id=?",
                    (
                        state,
                        str(error)[:2000],
                        now + min(300, delay * 2 ** max(0, row["attempts"] - 1)),
                        now,
                        job_id,
                    ),
                )

    def publish(self, job_id, owner, inventory, callback, *, requested_blocks=None):
        """Fence activation against another process reclaiming this request.

        Activation and the final job receipt happen while the ownership row is
        write-locked. Immutable files can remain staged if a process crashes;
        retrying the same output is idempotent in the pack store.
        """
        with self.connect() as db:
            db.execute("BEGIN IMMEDIATE")
            row = db.execute(
                "SELECT state,owner,requested_blocks FROM jobs WHERE id=?", (job_id,)
            ).fetchone()
            if row is None or row["state"] != "running" or row["owner"] != owner:
                return None
            expected = (
                canonical(requested_blocks).decode()
                if requested_blocks is not None
                else None
            )
            if row["requested_blocks"] != expected:
                return None
            published = callback()
            db.execute(
                "UPDATE jobs SET state='ready',published=?,inventory=?,error=NULL,updated_at=? WHERE id=?",
                (published, canonical(inventory).decode(), time.time(), job_id),
            )
            return published

    def cancel(self, job_id):
        self.get(job_id)
        with self.connect() as db:
            db.execute(
                "UPDATE jobs SET state='cancelled',owner=NULL,lease_until=NULL,updated_at=? WHERE id=? AND state!='ready'",
                (time.time(), job_id),
            )

    def retain_cancelled_inventory(self, job_id, inventory):
        """Refresh stopped-block counts without changing a retried job's state."""
        with self.connect() as db:
            db.execute(
                "UPDATE jobs SET inventory=? WHERE id=? AND state='cancelled'",
                (canonical(inventory).decode(), job_id),
            )

    def release(self, owner):
        with self.connect() as db:
            db.execute(
                "UPDATE jobs SET state='queued',owner=NULL,lease_until=NULL,updated_at=? WHERE owner=? AND state='running'",
                (time.time(), owner),
            )
