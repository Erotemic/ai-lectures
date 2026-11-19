"""Local saved rendering recipes. Connections and private references never enter source packs."""

from __future__ import annotations

from contextlib import contextmanager
from copy import deepcopy
from datetime import datetime, timezone
import json
import math
from pathlib import Path
import sqlite3
from uuid import uuid4

from .core import Conflict, canonical, digest
from .narration import TITLE_INSTRUCTION, TITLE_POLICY
from .voices import VOICE

SCHEMA = "voice-profiles-v1"
PIPELINE = "reader-render-profile-v1"
INSTRUCTION_FIELDS = {"instruction", "instructions", "voice_direction", "direction"}


def profile_cache_key(lecture_id, profile, epoch=None):
    return digest(
        dict(
            lecture=lecture_id,
            profile=profile["id"],
            revision=profile["revision"],
            epoch=epoch,
        )
    )


def capabilities(model, declared=None):
    key = model.lower()
    result = dict(
        adapter=(
            "kokoro"
            if key == "kokoro"
            else "breeze-tts2" if key == "breeze-tts2" else "openai-compatible"
        ),
        native_rate=key == "kokoro",
        native_rate_field="speed" if key == "kokoro" else None,
        instruction_field="instruction" if key == "breeze-tts2" else None,
        paragraph_delivery=key == "breeze-tts2",
        output_formats=["ogg", "mp3"],
    )
    declared = declared or {}
    if not isinstance(declared, dict) or set(declared) - {
        "native_rate_field",
        "instruction_field",
    }:
        raise ValueError("Unknown backend capability declaration")
    if "native_rate_field" in declared:
        if declared["native_rate_field"] not in {None, "speed", "duration_factor"}:
            raise ValueError("Unsupported native speaking-rate field")
        result["native_rate_field"] = declared["native_rate_field"]
        result["native_rate"] = bool(declared["native_rate_field"])
    if "instruction_field" in declared:
        if declared["instruction_field"] not in INSTRUCTION_FIELDS | {None}:
            raise ValueError("Unsupported instruction field")
        result["instruction_field"] = declared["instruction_field"]
    return result


def _stable(value):
    if isinstance(value, dict):
        return {
            k: _stable(v)
            for k, v in value.items()
            if k not in {"observed_at", "loaded_at_unix"}
        }
    if isinstance(value, list):
        return [_stable(v) for v in value]
    return value


def revision_id(recipe):
    # Operational location, labels and timeout do not describe the sound.
    data = deepcopy(recipe)
    for key in (
        "endpoint",
        "profile",
        "display_name",
        "narrator_voice",
        "timeout_seconds",
        "record_server_runtime",
        "pronunciation_lexicon",
    ):
        data.get("config", {}).pop(key, None)
    return digest(_stable(data))


def recipe_from_config(config, backend_id, *, reference=None, environment=None):
    config = deepcopy(config)
    reference = reference if reference is not None else config.pop("reference", None)
    config.pop("reference", None)
    cap = capabilities(config["model"], config.pop("capabilities", None))
    from dkvis.presentation.audio_quality import (
        settings as processing_settings,
        VERSION,
    )

    processing = processing_settings(config.pop("postprocess", {}))
    # The legacy reader did not run the slide-production loudness processor.
    processing = dict(processing, enabled=False)
    for key in (
        "endpoint",
        "profile",
        "display_name",
        "narrator_voice",
        "pronunciation_lexicon",
    ):
        config.pop(key, None)
    config["output_format"] = (environment or {}).get(
        "DKVIS_AUDIO_OUTPUT_FORMAT"
    ) or config.get("output_format", "ogg")
    paragraph = (
        cap["paragraph_delivery"]
        and (environment or {}).get("DKVIS_AUDIO_BREEZE_LONG_FORM", "1") != "0"
    )
    return dict(
        schema=SCHEMA,
        capabilities=cap,
        pipeline=PIPELINE,
        title_policy=TITLE_POLICY,
        backend_id=backend_id,
        config=config,
        reference=_stable(reference),
        fixed_reference=bool(reference),
        native_rate=1.0,
        tempo=1.0,
        body_mode="paragraph" if paragraph else "directed",
        title_enabled=True,
        title_instruction_field=config.get(
            "title_instruction_field", cap["instruction_field"]
        ),
        title_instruction=config.get("title_instruction", TITLE_INSTRUCTION),
        title_pause_before=config.get("title_pause_before_seconds", 0.25),
        title_pause_after=config.get("title_pause_after_seconds", 0.5),
        title_cfg_scale=4.0 if cap["adapter"] == "breeze-tts2" else None,
        processing=processing,
        processing_version=VERSION,
        generation_revision=str(config.get("voice_revision", "configured-1")),
        reader=dict(
            page_chars=int((environment or {}).get("DKVIS_AUDIO_PAGE_CHARS", "600")),
            segment_chars=int(
                (environment or {}).get("DKVIS_AUDIO_SEGMENT_CHARS", "140")
            ),
            segment_words=int(
                (environment or {}).get("DKVIS_AUDIO_SEGMENT_WORDS", "12")
            ),
            segment_seconds=float(
                (environment or {}).get("DKVIS_AUDIO_SEGMENT_SECONDS", "12")
            ),
        ),
    )


def validate_recipe(recipe, backend):
    if (
        not isinstance(recipe, dict)
        or recipe.get("schema") != SCHEMA
        or recipe.get("pipeline") != PIPELINE
    ):
        raise ValueError("Unknown render profile schema")
    if recipe["backend_id"] != backend["id"]:
        raise ValueError("Profile/backend mismatch")
    config, cap = recipe["config"], backend["capabilities"]
    if not isinstance(config, dict) or config.get("model") != backend["model"]:
        raise ValueError(
            "The backend model changed; create a revision for its current model"
        )
    if not isinstance(config.get("voice"), str) or not VOICE.fullmatch(config["voice"]):
        raise ValueError("Invalid fixed voice")
    if config.get("output_format") not in cap["output_formats"]:
        raise ValueError("Unsupported output format")
    for key in ("native_rate", "tempo"):
        value = recipe[key]
        if (
            type(value) not in (float, int)
            or not math.isfinite(value)
            or not 0.5 <= value <= 2
        ):
            raise ValueError(
                "Speaking rate and saved-audio tempo must be between 0.5 and 2"
            )
    if recipe["native_rate"] != 1 and not cap["native_rate"]:
        raise ValueError("This backend does not advertise native speaking-rate control")
    if recipe["body_mode"] not in {"paragraph", "directed"}:
        raise ValueError("Unknown body delivery")
    if recipe["body_mode"] == "paragraph" and not cap["paragraph_delivery"]:
        raise ValueError("This backend does not support paragraph narration")
    request = config.get("request", {})
    if not isinstance(request, dict) or set(request) & {
        "model",
        "voice",
        "input",
        "response_format",
        "speed",
        "duration_factor",
    }:
        raise ValueError(
            "Request settings cannot replace fixed identity, input, format or rate"
        )
    for key in INSTRUCTION_FIELDS:
        if key in request and key != cap["instruction_field"]:
            raise ValueError("This backend does not support that instruction field")
    if recipe["body_mode"] == "paragraph" and any(
        request.get(key) for key in INSTRUCTION_FIELDS
    ):
        raise ValueError(
            "Paragraph narration uses stable cloning; choose directed delivery to set prose instructions"
        )
    if (
        cap["adapter"] == "breeze-tts2"
        and recipe["body_mode"] == "directed"
        and any(request.get(key) for key in INSTRUCTION_FIELDS)
        and float(request.get("cfg_scale", 1)) == 1
    ):
        raise ValueError("Directed Breeze instructions require CFG other than 1")
    if cap["adapter"] == "breeze-tts2":
        cfg = recipe["title_cfg_scale"]
        if type(cfg) not in (int, float) or not math.isfinite(cfg) or not 0 < cfg <= 20:
            raise ValueError("Title CFG must be positive and at most 20")
        if (
            recipe["title_enabled"]
            and recipe["title_instruction_field"] not in (None, "none")
            and cfg == 1
        ):
            raise ValueError("Breeze title instructions require CFG other than 1")
    if type(recipe["title_enabled"]) is not bool:
        raise ValueError("Title delivery must be on or off")
    if recipe["title_instruction_field"] not in {
        None,
        "none",
        cap["instruction_field"],
    }:
        raise ValueError("Unsupported title instruction field")
    if (
        not isinstance(recipe["title_instruction"], str)
        or not 1 <= len(recipe["title_instruction"]) <= 4000
    ):
        raise ValueError("Title instruction must contain 1–4000 characters")
    for key in ("title_pause_before", "title_pause_after"):
        value = recipe[key]
        if (
            type(value) not in (int, float)
            or not math.isfinite(value)
            or not 0 <= value <= 5
        ):
            raise ValueError("Title pauses must be between zero and five seconds")
    if (
        not isinstance(recipe["generation_revision"], str)
        or not 1 <= len(recipe["generation_revision"]) <= 120
    ):
        raise ValueError("Supply a voice/model generation revision")
    reader = recipe["reader"]
    for key, low, high in [
        ("page_chars", 250, 1500),
        ("segment_chars", 40, 280),
        ("segment_words", 2, 24),
    ]:
        if type(reader.get(key)) is not int or not low <= reader[key] <= high:
            raise ValueError("Invalid reader chunk bounds")
    if (
        type(reader.get("segment_seconds")) not in (int, float)
        or not math.isfinite(reader["segment_seconds"])
        or reader["segment_seconds"] <= 0
    ):
        raise ValueError("Invalid duration bound")
    from dkvis.presentation.audio_quality import settings

    recipe["processing"] = settings(recipe["processing"])
    from dkvis.presentation.pronunciation import validate_replacements

    validate_replacements(config.get("pronunciation_replacements", {}))
    return recipe


class RenderProfiles:
    def __init__(self, state):
        Path(state).mkdir(parents=True, exist_ok=True)
        self.database = Path(state) / "render-profiles.sqlite3"
        with self.connect() as db:
            db.executescript(
                """CREATE TABLE IF NOT EXISTS backends (id TEXT PRIMARY KEY, anchor TEXT, aliases TEXT, document TEXT);
                CREATE TABLE IF NOT EXISTS profiles (id TEXT PRIMARY KEY, label TEXT NOT NULL, revision TEXT NOT NULL,
                    origin TEXT UNIQUE, quick INTEGER NOT NULL, archived INTEGER NOT NULL DEFAULT 0, updated TEXT);
                CREATE TABLE IF NOT EXISTS revisions (profile TEXT, revision TEXT, recipe TEXT, PRIMARY KEY(profile,revision));
                CREATE TABLE IF NOT EXISTS preferences (key TEXT PRIMARY KEY,value TEXT);"""
            )

    @contextmanager
    def connect(self):
        db = sqlite3.connect(self.database, timeout=30)
        db.row_factory = sqlite3.Row
        try:
            with db:
                yield db
        finally:
            db.close()

    def sync(self, sources, *, default_source=None, environment=None):
        """One-time recipe imports; later file edits never overwrite saved recipes."""
        groups = {}
        for alias, config in sources.items():
            groups.setdefault((config["endpoint"], config["model"]), []).append(alias)
        with self.connect() as db:
            db.execute("BEGIN IMMEDIATE")
            old = [dict(row) for row in db.execute("SELECT * FROM backends")]
            assigned = set()
            mapping = {}
            ordered = sorted(
                groups.items(),
                key=lambda item: not any(row["anchor"] in item[1] for row in old),
            )
            for (endpoint, model), aliases in ordered:
                existing = next(
                    (
                        row
                        for row in old
                        if row["id"] not in assigned and row["anchor"] in aliases
                    ),
                    None,
                )
                existing = existing or next(
                    (
                        row
                        for row in old
                        if row["id"] not in assigned
                        and set(json.loads(row["aliases"])) & set(aliases)
                    ),
                    None,
                )
                backend_id = existing["id"] if existing else "backend-" + uuid4().hex
                anchor = (
                    existing["anchor"]
                    if existing and existing["anchor"] in aliases
                    else sorted(aliases)[0]
                )
                cap = capabilities(model, sources[anchor].get("capabilities"))
                document = dict(
                    id=backend_id,
                    model=model,
                    endpoint=endpoint,
                    anchor=anchor,
                    aliases=sorted(aliases),
                    capabilities=cap,
                    available=True,
                )
                db.execute(
                    "INSERT OR REPLACE INTO backends VALUES (?,?,?,?)",
                    (
                        backend_id,
                        anchor,
                        json.dumps(aliases),
                        canonical(document).decode(),
                    ),
                )
                assigned.add(backend_id)
                for alias in aliases:
                    mapping[alias] = backend_id
            for row in old:
                if row["id"] not in assigned:
                    data = json.loads(row["document"])
                    data["available"] = False
                    db.execute(
                        "UPDATE backends SET document=? WHERE id=?",
                        (canonical(data).decode(), row["id"]),
                    )
            for alias, config in sources.items():
                if db.execute(
                    "SELECT 1 FROM profiles WHERE origin=?", (alias,)
                ).fetchone():
                    continue
                recipe = recipe_from_config(
                    config, mapping[alias], environment=environment
                )
                if recipe["body_mode"] == "paragraph":
                    recipe["config"]["request"] = {
                        k: v
                        for k, v in recipe["config"].get("request", {}).items()
                        if k not in INSTRUCTION_FIELDS
                    }
                    recipe["config"]["request"]["cfg_scale"] = 1.0
                profile_id = "voice-" + uuid4().hex
                revision = revision_id(recipe)
                db.execute(
                    "INSERT INTO profiles VALUES (?,?,?,?,?,?,?)",
                    (
                        profile_id,
                        config.get("display_name", alias),
                        revision,
                        alias,
                        1,
                        0,
                        datetime.now(timezone.utc).isoformat(),
                    ),
                )
                db.execute(
                    "INSERT INTO revisions VALUES (?,?,?)",
                    (profile_id, revision, canonical(recipe).decode()),
                )
            if (
                default_source
                and not db.execute(
                    "SELECT 1 FROM preferences WHERE key='default'"
                ).fetchone()
            ):
                row = db.execute(
                    "SELECT id FROM profiles WHERE origin=?", (default_source,)
                ).fetchone()
                if row:
                    db.execute(
                        "INSERT INTO preferences VALUES ('default',?)", (row[0],)
                    )

    def backends(self):
        with self.connect() as db:
            return [
                json.loads(row[0])
                for row in db.execute("SELECT document FROM backends ORDER BY id")
            ]

    def get(self, profile_id, revision=None):
        with self.connect() as db:
            row = db.execute(
                "SELECT * FROM profiles WHERE id=?", (profile_id,)
            ).fetchone()
            if row is None:
                raise KeyError("Unknown saved voice profile")
            item = dict(row)
            wanted = revision or item["revision"]
            recipe = db.execute(
                "SELECT recipe FROM revisions WHERE profile=? AND revision=?",
                (profile_id, wanted),
            ).fetchone()
            if recipe is None:
                raise KeyError("Unknown voice-profile revision")
            item["recipe"] = json.loads(recipe[0])
            item["revision"] = wanted
            return item

    def list(self, *, archived=False):
        with self.connect() as db:
            ids = [
                row[0]
                for row in db.execute(
                    "SELECT id FROM profiles WHERE archived=? ORDER BY label,id",
                    (int(archived),),
                )
            ]
        return [self.get(key) for key in ids]

    def default(self):
        with self.connect() as db:
            row = db.execute(
                "SELECT value FROM preferences WHERE key='default'"
            ).fetchone()
        return row[0] if row else None

    def save(self, *, label, recipe, profile_id=None, expected=None, quick=True):
        if not isinstance(label, str) or not 1 <= len(label.strip()) <= 100:
            raise ValueError("Profile name must contain 1–100 characters")
        if type(quick) is not bool:
            raise ValueError("Quick select must be true or false")
        backend = next(
            (
                row
                for row in self.backends()
                if row["id"] == recipe.get("backend_id") and row["available"]
            ),
            None,
        )
        if backend is None:
            raise ValueError("Select an available backend")
        recipe = validate_recipe(deepcopy(recipe), backend)
        revision = revision_id(recipe)
        with self.connect() as db:
            db.execute("BEGIN IMMEDIATE")
            if profile_id:
                row = db.execute(
                    "SELECT revision FROM profiles WHERE id=?", (profile_id,)
                ).fetchone()
                if row is None:
                    raise KeyError("Unknown saved voice profile")
                if row[0] != expected:
                    raise Conflict("Profile changed; reload before saving")
                old = json.loads(
                    db.execute(
                        "SELECT recipe FROM revisions WHERE profile=? AND revision=?",
                        (profile_id, row[0]),
                    ).fetchone()[0]
                )
                if (old["backend_id"], old["config"]["voice"]) != (
                    recipe["backend_id"],
                    recipe["config"]["voice"],
                ):
                    raise ValueError(
                        "Duplicate the profile to change its backend or fixed voice"
                    )
                db.execute(
                    "UPDATE profiles SET label=?,revision=?,quick=?,updated=? WHERE id=?",
                    (
                        label.strip(),
                        revision,
                        int(quick),
                        datetime.now(timezone.utc).isoformat(),
                        profile_id,
                    ),
                )
            else:
                profile_id = "voice-" + uuid4().hex
                db.execute(
                    "INSERT INTO profiles VALUES (?,?,?,?,?,?,?)",
                    (
                        profile_id,
                        label.strip(),
                        revision,
                        None,
                        int(quick),
                        0,
                        datetime.now(timezone.utc).isoformat(),
                    ),
                )
            db.execute(
                "INSERT OR IGNORE INTO revisions VALUES (?,?,?)",
                (profile_id, revision, canonical(recipe).decode()),
            )
        return self.get(profile_id)

    def set_default(self, profile_id):
        if self.get(profile_id)["archived"]:
            raise ValueError("Choose an active profile")
        with self.connect() as db:
            db.execute(
                "INSERT OR REPLACE INTO preferences VALUES ('default',?)", (profile_id,)
            )

    def set_presentation(self, profile_id, *, label=None, quick=None):
        self.get(profile_id)
        if label is not None and (
            not isinstance(label, str) or not 1 <= len(label.strip()) <= 100
        ):
            raise ValueError("Invalid profile name")
        if quick is not None and type(quick) is not bool:
            raise ValueError("Quick select must be true or false")
        with self.connect() as db:
            if label is not None:
                db.execute(
                    "UPDATE profiles SET label=? WHERE id=?",
                    (label.strip(), profile_id),
                )
            if quick is not None:
                db.execute(
                    "UPDATE profiles SET quick=? WHERE id=?", (int(quick), profile_id)
                )

    def archive(self, profile_id, archived=True):
        self.get(profile_id)
        with self.connect() as db:
            db.execute(
                "UPDATE profiles SET archived=? WHERE id=?", (int(archived), profile_id)
            )
            if archived:
                db.execute(
                    "DELETE FROM preferences WHERE key='default' AND value=?",
                    (profile_id,),
                )

    @staticmethod
    def public(item):
        recipe = item["recipe"]
        config = recipe["config"]
        # Full recipes stay local. Recording provenance uses only opaque IDs.
        return dict(
            id=item["id"],
            label=item["label"],
            revision=item["revision"],
            backend_id=recipe["backend_id"],
            voice=config["voice"],
            model=config["model"],
            output_format=config["output_format"],
            quick_select=bool(item["quick"]),
            archived=bool(item["archived"]),
            fixed_reference=recipe["fixed_reference"],
            native_rate=recipe["native_rate"],
            tempo=recipe["tempo"],
        )
