"""Optional listener identities, optimistic progress, and append-only feedback."""

from __future__ import annotations

from contextlib import contextmanager
from datetime import datetime, timezone
import json
from pathlib import Path
import sqlite3
from uuid import uuid4

from .core import Conflict, canonical, checksum, finite, qualified, text_digest


def utcnow():
    return datetime.now(timezone.utc).isoformat()


def identifier(value):
    if (
        not isinstance(value, str)
        or not 1 <= len(value) <= 128
        or any(ord(c) < 32 for c in value)
    ):
        raise ValueError("Invalid state identifier")
    return value


def validate_feedback(event):
    identifier(event["id"])
    qualified(event["lecture_id"])
    if event["type"] == "submission":
        for key in ("release", "revision", "spoken_sha256"):
            checksum(event[key])
        if (
            not isinstance(event["text"], str)
            or not 1 <= len(event["text"].strip()) <= 10000
        ):
            raise ValueError("Invalid feedback text")
        if (
            not isinstance(event["transcript_snapshot"], str)
            or text_digest(event["transcript_snapshot"]) != event["spoken_sha256"]
        ):
            raise ValueError(
                "Feedback transcript snapshot does not match its speech identity"
            )
        if event.get("recording"):
            checksum(event["recording"]["id"])
            checksum(event["recording"]["sha256"])
            finite(event["recording"]["seconds"])
    elif event["type"] == "status":
        identifier(event["feedback_id"])
        if event.get("status") not in {
            "open",
            "triaged",
            "resolved",
            "reopened",
            "superseded",
        }:
            raise ValueError("Unknown editorial status")
        if event.get("addressed_revision") is not None:
            checksum(event["addressed_revision"])
        if (
            not isinstance(event.get("note", ""), str)
            or len(event.get("note", "")) > 4000
        ):
            raise ValueError("Editorial note must be at most 4,000 characters")
    else:
        raise ValueError("Unknown feedback event type")


class ListenerState:
    def __init__(self, directory):
        self.database = Path(directory) / "listeners.sqlite3"
        self.database.parent.mkdir(parents=True, exist_ok=True)
        with self.connect() as db:
            db.executescript("""
                CREATE TABLE IF NOT EXISTS profiles (id TEXT PRIMARY KEY, name TEXT NOT NULL);
                CREATE TABLE IF NOT EXISTS progress (
                    profile TEXT, lecture TEXT, version INTEGER NOT NULL, record TEXT NOT NULL,
                    PRIMARY KEY(profile, lecture));
                CREATE TABLE IF NOT EXISTS progress_events (id TEXT PRIMARY KEY, record TEXT NOT NULL);
                CREATE TABLE IF NOT EXISTS device_sequences (
                    profile TEXT, lecture TEXT, device TEXT, sequence INTEGER NOT NULL,
                    PRIMARY KEY(profile, lecture, device));
                CREATE TABLE IF NOT EXISTS feedback_events (id TEXT PRIMARY KEY, record TEXT NOT NULL);
                CREATE TABLE IF NOT EXISTS listening_queues (profile TEXT PRIMARY KEY, entries TEXT NOT NULL);
            """)

    @contextmanager
    def connect(self):
        db = sqlite3.connect(self.database, timeout=30)
        db.row_factory = sqlite3.Row
        try:
            with db:
                yield db
        finally:
            db.close()

    def profiles(self):
        with self.connect() as db:
            return [
                dict(row)
                for row in db.execute("SELECT * FROM profiles ORDER BY name,id")
            ]

    def create_profile(self, label):
        if not isinstance(label, str) or not label.strip() or len(label) > 80:
            raise ValueError("Enter a listener name of 1–80 characters")
        result = {"id": str(uuid4()), "name": label.strip()}
        with self.connect() as db:
            db.execute(
                "INSERT INTO profiles VALUES (?,?)", (result["id"], result["name"])
            )
        return result

    def progress(self, profile):
        identifier(profile)
        with self.connect() as db:
            if not db.execute(
                "SELECT 1 FROM profiles WHERE id=?", (profile,)
            ).fetchone():
                raise KeyError("Unknown listener")
            return {
                row["lecture"]: json.loads(row["record"])
                for row in db.execute(
                    "SELECT * FROM progress WHERE profile=?", (profile,)
                )
            }

    def save_progress(self, profile, payload):
        identifier(profile)
        event_id, lecture_id = identifier(payload["update_id"]), qualified(
            payload["lecture_id"]
        )
        identifier(payload["device_id"])
        finite(payload["seconds"])
        sequence, expected = payload["sequence"], payload["expected_version"]
        if any(
            isinstance(v, bool) or not isinstance(v, int) or v < 0
            for v in (sequence, expected)
        ):
            raise ValueError("Invalid progress sequence/version")
        if not isinstance(payload.get("completed", False), bool):
            raise ValueError("Invalid completion state")
        encoded = canonical({"profile": profile, "payload": payload}).decode()
        with self.connect() as db:
            db.execute("BEGIN IMMEDIATE")
            if not db.execute(
                "SELECT 1 FROM profiles WHERE id=?", (profile,)
            ).fetchone():
                raise KeyError("Unknown listener")
            previous_event = db.execute(
                "SELECT record FROM progress_events WHERE id=?", (event_id,)
            ).fetchone()
            if previous_event:
                previous = json.loads(previous_event["record"])
                if previous["input"] != encoded:
                    raise Conflict("Progress update ID has conflicting contents")
                return previous["result"]
            row = db.execute(
                "SELECT * FROM progress WHERE profile=? AND lecture=?",
                (profile, lecture_id),
            ).fetchone()
            current = json.loads(row["record"]) if row else None
            version = row["version"] if row else 0
            result = dict(
                payload, profile_id=profile, updated_at=utcnow(), version=version + 1
            )
            device_state = db.execute(
                "SELECT sequence FROM device_sequences WHERE profile=? AND lecture=? AND device=?",
                (profile, lecture_id, payload["device_id"]),
            ).fetchone()
            same_device_late = (
                device_state is not None and device_state["sequence"] >= sequence
            )
            if expected != version or same_device_late:
                result = {"conflict": True, "current": current, "alternate": payload}
            else:
                db.execute(
                    "INSERT OR REPLACE INTO progress VALUES (?,?,?,?)",
                    (profile, lecture_id, version + 1, canonical(result).decode()),
                )
                db.execute(
                    "INSERT OR REPLACE INTO device_sequences VALUES (?,?,?,?)",
                    (profile, lecture_id, payload["device_id"], sequence),
                )
            db.execute(
                "INSERT INTO progress_events VALUES (?,?)",
                (event_id, canonical({"input": encoded, "result": result}).decode()),
            )
            return result

    def add_feedback_event(self, event):
        validate_feedback(event)
        data = canonical(event).decode()
        with self.connect() as db:
            db.execute("BEGIN IMMEDIATE")
            prior = db.execute(
                "SELECT record FROM feedback_events WHERE id=?", (event["id"],)
            ).fetchone()
            if prior:
                if prior["record"] != data:
                    raise Conflict("Feedback event ID has conflicting contents")
                return event
            if event["type"] == "status":
                target = db.execute(
                    "SELECT record FROM feedback_events WHERE id=?",
                    (event["feedback_id"],),
                ).fetchone()
                if not target or json.loads(target["record"])["type"] != "submission":
                    raise KeyError("Unknown feedback submission")
                if json.loads(target["record"])["lecture_id"] != event["lecture_id"]:
                    raise ValueError("Status refers to a different lecture")
            db.execute("INSERT INTO feedback_events VALUES (?,?)", (event["id"], data))
        return event

    def feedback(self, lecture_id=None):
        with self.connect() as db:
            rows = [
                json.loads(row["record"])
                for row in db.execute(
                    "SELECT record FROM feedback_events ORDER BY rowid"
                )
            ]
        return [r for r in rows if lecture_id is None or r["lecture_id"] == lecture_id]

    def export_feedback(self, lecture_id=None):
        # Listener attribution is stored separately; portable events never contain it.
        return {"schema_version": 1, "events": self.feedback(lecture_id)}

    def import_feedback(self, document):
        if document.get("schema_version") != 1 or not isinstance(
            document.get("events"), list
        ):
            raise ValueError("Unsupported feedback export")
        # One transaction: a later conflict must not leave half the import applied.
        events = document["events"]
        with self.connect() as db:
            db.execute("BEGIN IMMEDIATE")
            known = {
                r["id"]: json.loads(r["record"])
                for r in db.execute("SELECT * FROM feedback_events")
            }
            incoming = {}
            for event in events:
                validate_feedback(event)
                if event["id"] in incoming and incoming[event["id"]] != event:
                    raise Conflict("Duplicate conflicting feedback ID")
                if event["id"] in known and known[event["id"]] != event:
                    raise Conflict("Feedback event conflicts with local history")
                incoming[event["id"]] = event
            merged = known | incoming
            for event in events:
                if event["type"] == "status":
                    target = merged.get(event.get("feedback_id"))
                    if (
                        not target
                        or target["type"] != "submission"
                        or target["lecture_id"] != event["lecture_id"]
                    ):
                        raise ValueError("Feedback status has no matching submission")
                    if event.get("status") not in {
                        "open",
                        "triaged",
                        "resolved",
                        "reopened",
                        "superseded",
                    }:
                        raise ValueError("Invalid editorial status")
                db.execute(
                    "INSERT OR IGNORE INTO feedback_events VALUES (?,?)",
                    (event["id"], canonical(event).decode()),
                )
        return len(incoming.keys() - known.keys())

    def export_listener(self, profile):
        progress = self.progress(profile)
        person = next(p for p in self.profiles() if p["id"] == profile)
        return {
            "schema_version": 1,
            "profile": person,
            "progress": progress,
            "queue": self.queue(profile),
        }

    def queue(self, profile):
        identifier(profile)
        with self.connect() as db:
            if not db.execute(
                "SELECT 1 FROM profiles WHERE id=?", (profile,)
            ).fetchone():
                raise KeyError("Unknown listener")
            row = db.execute(
                "SELECT entries FROM listening_queues WHERE profile=?", (profile,)
            ).fetchone()
            return json.loads(row["entries"]) if row else []

    @staticmethod
    def queue_entry(entry):
        identifier(entry["id"])
        qualified(entry["lecture_id"])
        if entry.get("course_id"):
            qualified(entry["course_id"])
        return {
            key: entry[key] for key in ("id", "lecture_id", "course_id") if key in entry
        }

    def edit_queue(self, profile, operation):
        # Apply one user action to the current queue, never a stale full list.
        identifier(profile)
        with self.connect() as db:
            db.execute("BEGIN IMMEDIATE")
            if not db.execute(
                "SELECT 1 FROM profiles WHERE id=?", (profile,)
            ).fetchone():
                raise KeyError("Unknown listener")
            row = db.execute(
                "SELECT entries FROM listening_queues WHERE profile=?", (profile,)
            ).fetchone()
            entries = json.loads(row["entries"]) if row else []
            action = operation["action"]
            if action == "add":
                entry = self.queue_entry(operation["entry"])
                old = next(
                    (item for item in entries if item["id"] == entry["id"]), None
                )
                if old is not None and old != entry:
                    raise Conflict("Queue entry ID has conflicting content")
                if old is None:
                    entries.append(entry)
            elif action in {"remove", "move"}:
                entry_id = identifier(operation["id"])
                entry = next((item for item in entries if item["id"] == entry_id), None)
                if action == "move" and entry is None:
                    raise Conflict("This queue entry has already been removed")
                before = operation.get("before") if action == "move" else None
                if before == entry_id:
                    return entries
                entries = [item for item in entries if item["id"] != entry_id]
                if action == "move":
                    if before is not None and not any(
                        item["id"] == before for item in entries
                    ):
                        raise Conflict(
                            "The queue changed on another device; refresh before moving this item"
                        )
                    index = next(
                        (i for i, item in enumerate(entries) if item["id"] == before),
                        len(entries),
                    )
                    entries.insert(index, entry)
            else:
                raise ValueError("Unknown queue action")
            db.execute(
                "INSERT OR REPLACE INTO listening_queues VALUES (?,?)",
                (profile, canonical(entries).decode()),
            )
            return entries

    def import_listener(self, document):
        if document.get("schema_version") != 1:
            raise ValueError("Unsupported listener export")
        person, progress = document["profile"], document["progress"]
        queue = document.get("queue")
        if queue is not None:
            if not isinstance(queue, list):
                raise ValueError("Invalid listening queue")
            queue = [self.queue_entry(entry) for entry in queue]
            if len({entry["id"] for entry in queue}) != len(queue):
                raise ValueError("Duplicate queue entry IDs")
        identifier(person["id"])
        if not isinstance(person["name"], str) or not 1 <= len(person["name"]) <= 80:
            raise ValueError("Invalid listener name")
        with self.connect() as db:
            db.execute("BEGIN IMMEDIATE")
            existing = db.execute(
                "SELECT name FROM profiles WHERE id=?", (person["id"],)
            ).fetchone()
            if existing and existing["name"] != person["name"]:
                raise Conflict("Listener ID already has another name")
            db.execute(
                "INSERT OR IGNORE INTO profiles VALUES (?,?)",
                (person["id"], person["name"]),
            )
            if queue is not None:
                current = db.execute(
                    "SELECT entries FROM listening_queues WHERE profile=?",
                    (person["id"],),
                ).fetchone()
                if current and json.loads(current["entries"]) != queue:
                    raise Conflict(
                        "Listening queue conflicts with this listener's existing queue"
                    )
                db.execute(
                    "INSERT OR IGNORE INTO listening_queues VALUES (?,?)",
                    (person["id"], canonical(queue).decode()),
                )
            for key, row in progress.items():
                qualified(key)
                finite(row["seconds"])
                current = db.execute(
                    "SELECT record FROM progress WHERE profile=? AND lecture=?",
                    (person["id"], key),
                ).fetchone()
                if current and json.loads(current["record"]) != row:
                    raise Conflict(
                        "Listener progress conflicts; import into a new profile or reconcile first"
                    )
                db.execute(
                    "INSERT OR IGNORE INTO progress VALUES (?,?,?,?)",
                    (person["id"], key, row["version"], canonical(row).decode()),
                )
        return person
