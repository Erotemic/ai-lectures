"""Durable local voice choices, separate from distributable content packs."""

import json
from pathlib import Path
import re
import sqlite3
from contextlib import contextmanager

VOICE = re.compile(r"^[A-Za-z0-9_.+\-]{1,80}$")


class VoiceStore:
    def __init__(self, state, *, legacy=None):
        self.database = Path(state) / "voices.sqlite3"
        self.database.parent.mkdir(parents=True, exist_ok=True)
        self.legacy = Path(legacy) if legacy else None
        with self.connect() as db:
            db.executescript(
                "CREATE TABLE IF NOT EXISTS voices (profile TEXT,voice TEXT,label TEXT,PRIMARY KEY(profile,voice)); CREATE TABLE IF NOT EXISTS catalogs (profile TEXT PRIMARY KEY,voices TEXT);"
            )

    @contextmanager
    def connect(self):
        db = sqlite3.connect(self.database, timeout=30)
        try:
            with db:
                yield db
        finally:
            db.close()

    def registered(self, profile):
        # Original registrations remain usable. Import is additive; a stale JSON
        # file cannot replace a label edited through the new local library.
        if self.legacy:
            try:
                records = json.loads(self.legacy.read_text()).get("voices", [])
                with self.connect() as db:
                    for row in records:
                        if (
                            isinstance(row, dict)
                            and isinstance(row.get("profile"), str)
                            and isinstance(row.get("voice"), str)
                            and VOICE.fullmatch(row["voice"])
                            and isinstance(row.get("label"), str)
                        ):
                            db.execute(
                                "INSERT OR IGNORE INTO voices VALUES (?,?,?)",
                                (row["profile"], row["voice"], row["label"]),
                            )
            except (OSError, ValueError, TypeError, AttributeError):
                pass
        with self.connect() as db:
            return [
                dict(profile=profile, voice=voice, label=label)
                for voice, label in db.execute(
                    "SELECT voice,label FROM voices WHERE profile=? ORDER BY voice",
                    (profile,),
                )
            ]

    def register(self, profile, voice, label=None):
        if not isinstance(voice, str) or not VOICE.fullmatch(voice):
            raise ValueError("Voice ID must use 1–80 letters, digits, _, ., +, or -")
        label = voice if label is None else label
        if not isinstance(label, str) or not 1 <= len(label.strip()) <= 80:
            raise ValueError("Voice label must contain 1–80 characters")
        with self.connect() as db:
            db.execute(
                "INSERT OR REPLACE INTO voices VALUES (?,?,?)",
                (profile, voice, label.strip()),
            )
        return dict(profile=profile, voice=voice, label=label.strip())

    def catalog(self, profile, values=None):
        with self.connect() as db:
            if values is not None:
                db.execute(
                    "INSERT OR REPLACE INTO catalogs VALUES (?,?)",
                    (profile, json.dumps(values)),
                )
                return values
            row = db.execute(
                "SELECT voices FROM catalogs WHERE profile=?", (profile,)
            ).fetchone()
            return json.loads(row[0]) if row else []
