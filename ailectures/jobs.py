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
            db.execute("""CREATE TABLE IF NOT EXISTS jobs (
                id TEXT PRIMARY KEY, specification TEXT NOT NULL,
                state TEXT NOT NULL, attempts INTEGER NOT NULL DEFAULT 0,
                retry_at REAL NOT NULL DEFAULT 0, owner TEXT, lease_until REAL,
                published TEXT, error TEXT, inventory TEXT,
                created_at REAL NOT NULL, updated_at REAL NOT NULL)""")

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
        return result

    def get(self, job_id):
        checksum(job_id)
        with self.connect() as db:
            row = db.execute("SELECT * FROM jobs WHERE id=?", (job_id,)).fetchone()
        if row is None:
            raise KeyError("Unknown preparation job")
        return self.decode(row)

    def list(self):
        with self.connect() as db:
            return [
                self.decode(row)
                for row in db.execute("SELECT * FROM jobs ORDER BY created_at,id")
            ]

    def enqueue(self, specifications):
        now = time.time()
        with self.connect() as db:
            db.execute("BEGIN IMMEDIATE")
            for job_id, specification in specifications:
                checksum(job_id)
                data = canonical(specification).decode()
                previous = db.execute(
                    "SELECT * FROM jobs WHERE id=?", (job_id,)
                ).fetchone()
                if previous is None:
                    db.execute(
                        "INSERT INTO jobs (id,specification,state,created_at,updated_at) VALUES (?,?,?,?,?)",
                        (job_id, data, "queued", now, now),
                    )
                elif previous["specification"] != data:
                    raise ValueError(
                        "Preparation identity has conflicting specifications"
                    )
                elif previous["state"] in {"failed", "cancelled", "settings_changed"}:
                    db.execute(
                        "UPDATE jobs SET state='queued',attempts=0,retry_at=0,error=NULL,owner=NULL,lease_until=NULL,updated_at=? WHERE id=?",
                        (now, job_id),
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
            candidates = db.execute(
                "SELECT id FROM jobs WHERE state='queued' AND retry_at<=? ORDER BY created_at,id LIMIT ?",
                (now, max(0, limit - active)),
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

    def publish(self, job_id, owner, inventory, callback):
        """Fence activation against another process reclaiming this request.

        Activation and the final job receipt happen while the ownership row is
        write-locked. Immutable files can remain staged if a process crashes;
        retrying the same output is idempotent in the pack store.
        """
        with self.connect() as db:
            db.execute("BEGIN IMMEDIATE")
            row = db.execute(
                "SELECT state,owner FROM jobs WHERE id=?", (job_id,)
            ).fetchone()
            if row is None or row["state"] != "running" or row["owner"] != owner:
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
