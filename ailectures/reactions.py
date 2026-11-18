"""Per-listener lecture ratings and favorites, merged independently by field."""
from datetime import datetime, timezone
import json

from .core import canonical, checksum, qualified


def reaction_record(payload):
    if not isinstance(payload, dict):
        raise ValueError("Invalid lecture reaction")
    from .state import identifier
    lecture = qualified(payload["lecture_id"])
    field, value = payload["field"], payload["value"]
    if field == "rating":
        if value is not None and (type(value) is not int or not 1 <= value <= 5):
            raise ValueError("Rating must be 1–5 stars or null to clear")
    elif field == "favorite":
        if type(value) is not bool:
            raise ValueError("Favorite must be true or false")
    else:
        raise ValueError("Unknown lecture reaction field")
    stamp = payload["updated_at"]
    if not isinstance(stamp, str):
        raise ValueError("Invalid reaction timestamp")
    try:
        instant = datetime.fromisoformat(stamp.replace("Z", "+00:00"))
        if instant.tzinfo is None:
            raise ValueError()
        stamp = instant.astimezone(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z")
    except (ValueError, OverflowError):
        raise ValueError("Reaction timestamp must include its timezone") from None
    revision = payload.get("revision")
    if revision is not None:
        checksum(revision)
    return dict(lecture_id=lecture, field=field, value=value, updated_at=stamp,
                update_id=identifier(payload["update_id"]), revision=revision)


def merge_reaction(db, profile, record):
    """Tombstones and independent field clocks make retries/imports order-safe."""
    key = (profile, record["lecture_id"], record["field"])
    row = db.execute("SELECT record FROM lecture_reactions WHERE profile=? AND lecture=? AND field=?", key).fetchone()
    if row:
        previous = json.loads(row["record"])
        from .core import Conflict
        if previous["update_id"] == record["update_id"] and previous != record:
            raise Conflict("Reaction update ID has conflicting contents")
        if (previous["updated_at"], previous["update_id"]) >= (record["updated_at"], record["update_id"]):
            return previous
    db.execute("INSERT OR REPLACE INTO lecture_reactions VALUES (?,?,?,?)", (*key, canonical(record).decode()))
    return record


class LectureReactions:
    def reactions(self, profile):
        profile = self.resolve_profile(profile)
        with self.connect() as db:
            if not db.execute("SELECT 1 FROM profiles WHERE id=?", (profile,)).fetchone():
                raise KeyError("Unknown listener")
            result = {}
            for row in db.execute("SELECT record FROM lecture_reactions WHERE profile=?", (profile,)):
                record = json.loads(row["record"])
                result.setdefault(record["lecture_id"], {})[record["field"]] = record
            return result

    def save_reaction(self, profile, payload):
        profile = self.resolve_profile(profile)
        record = reaction_record(payload)
        with self.connect() as db:
            db.execute("BEGIN IMMEDIATE")
            if not db.execute("SELECT 1 FROM profiles WHERE id=?", (profile,)).fetchone():
                raise KeyError("Unknown listener")
            return merge_reaction(db, profile, record)

    def reaction_summary(self):
        result = {}
        with self.connect() as db:
            for row in db.execute("SELECT record FROM lecture_reactions"):
                record = json.loads(row["record"])
                if record["value"] is None or record["value"] is False:
                    continue
                summary = result.setdefault(record["lecture_id"], dict(ratings=0, stars=0, favorites=0, distribution=[0]*5))
                if record["field"] == "rating":
                    summary["ratings"] += 1
                    summary["stars"] += record["value"]
                    summary["distribution"][record["value"]-1] += 1
                else:
                    summary["favorites"] += 1
        for summary in result.values():
            stars = summary.pop("stars")
            summary["average"] = stars / summary["ratings"] if summary["ratings"] else None
        return result
