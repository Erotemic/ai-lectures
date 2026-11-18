"""Shared reader preferences, kept with local server state rather than packs."""

from copy import deepcopy
import json
from pathlib import Path
import sqlite3

from .core import Conflict, digest, name
from .voices import VOICE

DEFAULTS = {"playback_only": False, "default_profile": None, "profiles": {}}


def voice_identity(recording):
    generator = recording.get("generator", {})
    if generator.get("profile") and generator.get("voice"):
        return generator["profile"], generator["voice"]
    return "prepared", recording["variant"]


class ServerSettings:
    def __init__(self, state):
        Path(state).mkdir(parents=True, exist_ok=True)
        self.database = Path(state) / "settings.sqlite3"
        with sqlite3.connect(self.database) as db:
            db.execute(
                "CREATE TABLE IF NOT EXISTS settings (id INTEGER PRIMARY KEY CHECK(id=1), document TEXT NOT NULL)"
            )

    def read(self):
        with sqlite3.connect(self.database) as db:
            row = db.execute("SELECT document FROM settings WHERE id=1").fetchone()
        return json.loads(row[0]) if row else deepcopy(DEFAULTS)

    @staticmethod
    def validate(document):
        if not isinstance(document, dict) or set(document) != set(DEFAULTS):
            raise ValueError(
                "Expected playback_only, default_profile and profiles settings"
            )
        if type(document["playback_only"]) is not bool:
            raise ValueError("playback_only must be true or false")
        if document["default_profile"] is not None:
            name(document["default_profile"])
        if (
            not isinstance(document["profiles"], dict)
            or len(document["profiles"]) > 200
        ):
            raise ValueError("Invalid voice preferences")
        for profile, policy in document["profiles"].items():
            name(profile)
            if not isinstance(policy, dict) or set(policy) != {
                "default_voice",
                "quick_voices",
            }:
                raise ValueError(
                    "Expected default_voice and quick_voices for each profile"
                )
            voice, quick = policy["default_voice"], policy["quick_voices"]
            if voice is not None and (
                not isinstance(voice, str) or not VOICE.fullmatch(voice)
            ):
                raise ValueError("Invalid default voice")
            if quick is not None and (
                not isinstance(quick, list)
                or len(quick) > 1000
                or any(not isinstance(v, str) or not VOICE.fullmatch(v) for v in quick)
                or len(set(quick)) != len(quick)
            ):
                raise ValueError("Invalid quick-select voices")

    def save(self, document, *, expected):
        self.validate(document)
        with sqlite3.connect(self.database, timeout=30) as db:
            db.execute("BEGIN IMMEDIATE")
            row = db.execute("SELECT document FROM settings WHERE id=1").fetchone()
            current = json.loads(row[0]) if row else DEFAULTS
            if expected != digest(current):
                raise Conflict("Settings changed on another page; reload before saving")
            db.execute(
                "INSERT OR REPLACE INTO settings VALUES (1,?)", (json.dumps(document),)
            )
        return deepcopy(document)
