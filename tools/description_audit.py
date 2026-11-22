#!/usr/bin/env python3
"""Prioritize description audits and record review provenance, separately from packs.

Stdlib only. Ranking is heuristic triage, not an estimate of error probability.
The append-only audit ledger is in reviews/registry/description-audits-<track>.jsonl.
No command edits lecture manuscripts or metadata sidecars.
"""

from __future__ import annotations

import argparse
import csv
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import unicodedata

SCOPES = (
    "description", "title", "tags", "tag_paths", "chronology", "geography",
    "learning", "related_resources", "claim_evidence",
)
SCOPE_FIELDS = {
    "tags": ("tags",),
    "tag_paths": ("tag_paths",),
    "chronology": ("chronology", "periods", "spacetime_coverage"),
    "geography": ("places", "geography"),
    "learning": ("learning",),
    "related_resources": ("related_resources",),
    "claim_evidence": ("claim_evidence", "evidence_claims", "historical_claims", "mathematical_claims"),
}

DEPTHS = ("automated", "excerpts", "targeted_passages", "full_manuscript", "source_verified")
OUTCOMES = ("screened", "clean", "corrected", "needs_followup")
FULL_DEPTHS = {"full_manuscript", "source_verified"}
TOKEN_RE = re.compile(r"[a-z][a-z'-]{2,}")
STOP_WORDS = {
    "about", "across", "after", "against", "among", "analysis", "and", "around", "between",
    "brief", "chapter", "conclusion", "context", "critical", "early", "essay", "explained",
    "from", "history", "into", "introduction", "lecture", "lessons", "life", "later", "modern",
    "part", "parts", "readings", "story", "studies", "study", "survey", "that", "their",
    "the", "theory", "through", "time", "toward", "under", "understanding", "what", "when",
    "where", "which", "with", "world", "why", "work", "works", "more", "first", "second",
    "third", "fourth", "five", "years", "century", "mathematics", "math", "science", "literature",
}


def digest(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def normalize(value: str) -> str:
    value = unicodedata.normalize("NFKD", value)
    return "".join(ch for ch in value if not unicodedata.combining(ch)).lower()


def spoken_text(manuscript: str) -> str:
    begin, end = "<!-- BEGIN SPOKEN LECTURE -->", "<!-- END SPOKEN LECTURE -->"
    if manuscript.count(begin) == 1 and manuscript.count(end) == 1:
        return manuscript.split(begin, 1)[1].split(end, 1)[0].strip()
    # Nonstandard manuscripts are still tracked, conservatively using whole-file bytes.
    return manuscript


def inventory(repo: Path):
    for base in (repo / "content", repo / "draft-stages"):
        if not base.is_dir():
            continue
        for track_file in sorted(base.glob("*/track.json")):
            track_dir = track_file.parent
            track = track_dir.name
            track_data = json.loads(track_file.read_text(encoding="utf-8"))
            for item in track_data.get("lectures", []):
                lec_id = str(item["id"])
                md = track_dir / "metadata" / (lec_id + ".json")
                manuscript = track_dir / item["file"]
                if not md.is_file() or not manuscript.is_file():
                    continue
                meta = json.loads(md.read_text(encoding="utf-8"))
                desc = meta.get("description", "")
                if not isinstance(desc, str):
                    desc = ""
                speech = spoken_text(manuscript.read_text(encoding="utf-8"))
                scope_hashes = {"description": digest(desc),
                                "title": digest(str(item.get("title", "")))}
                for name, fields in SCOPE_FIELDS.items():
                    scoped = {field: meta.get(field) for field in fields}
                    scope_hashes[name] = digest(json.dumps(
                        scoped, ensure_ascii=False, sort_keys=True, separators=(",", ":")))
                yield {
                    "track": track, "lecture_id": lec_id, "key": f"{track}:{lec_id}",
                    "title": item.get("title", ""), "description": desc,
                    "manuscript": speech, "manuscript_sha256": digest(speech),
                    "description_sha256": digest(desc), "scope_sha256": scope_hashes,
                    "metadata": meta,
                }


def ledger_path(repo: Path, track: str) -> Path:
    if not re.fullmatch(r"[a-zA-Z0-9_-]+", track):
        raise ValueError("Invalid track name")
    return repo / "reviews" / "registry" / ("description-audits-" + track + ".jsonl")


def read_ledger(repo: Path, track: str) -> list[dict]:
    path = ledger_path(repo, track)
    if not path.exists():
        return []
    result = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            item = json.loads(line)
            if item.get("track") != track:
                raise ValueError("track mismatch")
            result.append(item)
        except (ValueError, json.JSONDecodeError) as ex:
            raise ValueError(f"Malformed audit record {path}:{line_no}: {ex}") from ex
    return result


def record_scopes(entry: dict) -> tuple[str, ...]:
    scopes = entry.get("scope", "description")
    if isinstance(scopes, str):
        return (scopes,)
    if isinstance(scopes, list) and all(isinstance(x, str) for x in scopes):
        return tuple(scopes)
    return ()


def scope_outcome(entry: dict, scope: str) -> str | None:
    if scope not in record_scopes(entry):
        return None
    return entry.get("scope_outcomes", {}).get(scope, entry.get("outcome"))


def matches(entry: dict, row: dict, scope: str | None = None) -> bool:
    """True when the specified scoped metadata and spoken text are unchanged.

    If scope is omitted, check every scope asserted by the receipt. Legacy
    schema-1 records are description-only even if they say full_manuscript.
    """
    scopes = (scope,) if scope else record_scopes(entry)
    if not scopes or any(x not in record_scopes(entry) for x in scopes):
        return False
    if entry.get("manuscript_sha256") != row["manuscript_sha256"]:
        return False
    hashes = entry.get("scope_sha256")
    for name in scopes:
        recorded = hashes.get(name) if isinstance(hashes, dict) else (
            entry.get("description_sha256") if name == "description" else None)
        if not recorded or recorded != row["scope_sha256"].get(name):
            return False
    return True


def audit_status(row: dict, records: list[dict], scope: str = "description") -> dict:
    history = sorted((r for r in records if r.get("lecture_id") == row["lecture_id"]
                      and scope in record_scopes(r)),
                     key=lambda r: (r.get("audited_at", ""), r.get("audit_id", "")))
    current = [r for r in history if matches(r, row, scope)]
    full = [r for r in current if r.get("depth") in FULL_DEPTHS]
    last = history[-1] if history else None
    last_full = full[-1] if full else None
    followups = [r for r in current if scope_outcome(r, scope) == "needs_followup"]
    last_followup = followups[-1] if followups else None
    if last_followup and (not last_full or
                          last_full.get("audited_at", "") <= last_followup.get("audited_at", "")):
        state = "needs_followup"
    elif last_full:
        state = "fully_reviewed"
    elif current and any(r.get("depth") != "automated" for r in current):
        state = "partial_review_only"
    elif history and not current:
        state = "stale"
    elif current:
        state = "automated_screen_only"
    else:
        state = "never_recorded"
    return {"state": state, "last": last, "last_current": bool(last and matches(last, row, scope)),
            "last_full": last_full, "count": len(history)}


def risk_cues(row: dict, scope: str = "description") -> list[tuple[str, int]]:
    if scope != "description":
        # Optional fields are not universally required. These are triage cues,
        # not a declaration that an absent field is an error.
        meta = row.get("metadata", {})
        biography = ("biography" in [str(x).lower() for x in meta.get("tags", [])]
                     or "scientific biography" in [str(x).lower() for path in meta.get("tag_paths", [])
                                                    for x in path])
        if scope == "geography" and biography and not meta.get("places") and not meta.get("geography"):
            return [("biography_missing_places", 16)]
        if scope == "chronology" and biography and not meta.get("chronology"):
            return [("biography_missing_chronology", 16)]
        if scope == "tag_paths" and not meta.get("tag_paths"):
            return [("tag_paths_absent", 8)]
        if scope == "related_resources":
            reasons = [str(x.get("reason", "")) for x in meta.get("related_resources", [])
                       if isinstance(x, dict)]
            if reasons and all(x.strip().lower() in {"background reference", "source"} for x in reasons):
                return [("generic_source_rationales", 8)]
        return []
    desc = row["description"].strip()
    title = row["title"]
    speech = row["manuscript"]
    d_norm = normalize(desc)
    cues = []
    words = TOKEN_RE.findall(d_norm)
    if not desc:
        cues.append(("missing_description", 40))
    if re.search(r"(addresses topics from the lecture|covers the sections|topics include [\"'])", desc, re.I):
        cues.append(("section_heading_placeholder", 32))
    if len(words) < 12:
        cues.append(("very_short_preview", 12))
    if len(words) > 44:
        cues.append(("long_topic_inventory", 8))
    if desc.count(";") >= 3:
        cues.append(("semicolon_topic_inventory", 12))
    if desc.count(",") >= 8:
        cues.append(("many_listed_topics", 8))
    if re.search(r"(?i)\b(?:proves|fully proves|establishes the theorem|complete proof)\b", desc):
        cues.append(("proof_scope_needs_confirmation", 12))
    if re.search(r"(?i)\b(?:always|never|first ever|definitively|entirely|exclusively)\b", desc):
        cues.append(("absolute_claim_needs_confirmation", 8))
    if re.search(r"(?i)^\s*(?:covers|examines|addresses|discusses|surveys)\b", desc):
        cues.append(("generic_preview_opening", 6))
    # Title/subject anchoring is a cue only: a valid summary need not repeat title words.
    special = {w for w in TOKEN_RE.findall(normalize(title)) if w not in STOP_WORDS and len(w) >= 5}
    # Split hyphenated phrases (e.g. sperm-egg), and accept closely related
    # inflections (e.g. metabolism/metabolic). A metaphorical title is not a
    # strong reason to doubt a precise technical description.
    subject_words = set(re.findall(r"[a-z]{3,}", d_norm))
    title_anchored = any(
        t == d or (len(t) >= 6 and len(d) >= 6 and t[:6] == d[:6])
        for t in special for d in subject_words
    )
    if special and not title_anchored:
        # Named biographies have a more specific and meaningful title anchor.
        named_subject = bool(re.match(r"^[A-Z][A-Za-zÀ-ÿ'-]+ [A-Z][A-Za-zÀ-ÿ'-]+:", title))
        cues.append(("title_subject_not_named", 15 if named_subject else 4))
    # Broad descriptions of long manuscripts merit attention; length is not an error.
    if len(speech.split()) > 5500 and len(words) < 19:
        cues.append(("long_lecture_short_preview", 6))
    return cues


def rank_row(row: dict, history: list[dict], scope: str = "description") -> dict:
    status = audit_status(row, history, scope)
    state = status["state"]
    baseline = {
        "needs_followup": 100, "stale": 75, "never_recorded": 65,
        "partial_review_only": 47, "automated_screen_only": 62, "fully_reviewed": 0,
    }[state]
    cues = risk_cues(row, scope)
    score = baseline + sum(weight for _, weight in cues)
    if state == "fully_reviewed":
        score = min(score, 20)  # Do not repeatedly prioritize an unchanged full review.
    last = status["last"] or {}
    last_full = status["last_full"] or {}
    return {
        "lecture": row["key"], "title": row["title"], "description": row["description"],
        "audit_scope": scope,
        "priority_points": score, "review_state": state,
        "risk_cues": "|".join(k for k, _ in cues) or "none",
        "last_audit_at": last.get("audited_at", ""),
        "last_audit_model": last.get("reviewer", {}).get("model") or "",
        "last_audit_depth": last.get("depth", ""),
        "last_audit_outcome": scope_outcome(last, scope) if last else "",
        "last_audit_current": status["last_current"],
        "last_full_audit_at": last_full.get("audited_at", ""),
        "last_full_audit_model": last_full.get("reviewer", {}).get("model") or "",
        "audits_recorded": status["count"],
        "manuscript_sha256": row["manuscript_sha256"],
        "description_sha256": row["description_sha256"],
    }


def all_ranks(repo: Path, scope: str = "description") -> list[dict]:
    if scope not in SCOPES:
        raise ValueError(f"Unknown audit scope {scope!r}")
    cache = {}
    output = []
    for row in inventory(repo):
        if row["track"] not in cache:
            cache[row["track"]] = read_ledger(repo, row["track"])
        output.append(rank_row(row, cache[row["track"]], scope))
    output.sort(key=lambda x: (-x["priority_points"], x["lecture"]))
    for index, row in enumerate(output, 1):
        row["rank"] = index
    return output


def by_key(repo: Path, key: str) -> dict:
    rows = [r for r in inventory(repo) if r["key"] == key]
    if len(rows) != 1:
        raise ValueError(f"No unique lecture named {key!r}")
    return rows[0]


def record_audit(repo: Path, key: str, kind: str, model: str | None,
                 depth: str, outcome: str, note: str,
                 scopes: tuple[str, ...] = ("description",),
                 scope_outcomes: dict[str, str] | None = None) -> dict:
    """Append a receipt for exact metadata scopes, not a broad content audit."""
    if depth not in DEPTHS or outcome not in OUTCOMES:
        raise ValueError("Invalid depth or outcome")
    scopes = tuple(dict.fromkeys(scopes))
    if not scopes or any(x not in SCOPES for x in scopes):
        raise ValueError("Specify one or more supported metadata scopes")
    if kind not in {"model", "human", "tool"}:
        raise ValueError("Invalid reviewer kind")
    if kind == "model" and not model:
        raise ValueError("--model is required for model reviews")
    if kind == "tool" and depth != "automated":
        raise ValueError("Tool-only screening cannot claim a semantic-review depth")
    per_scope = dict(scope_outcomes or {})
    if set(per_scope) - set(scopes):
        raise ValueError("Scope outcomes must reference selected scopes")
    if len(scopes) > 1 and set(per_scope) != set(scopes):
        raise ValueError("Multiple scopes require a separate --scope-outcome for each")
    for scope in scopes:
        per_scope.setdefault(scope, outcome)
    if any(x not in OUTCOMES for x in per_scope.values()):
        raise ValueError("Invalid scoped outcome")
    if depth == "automated" and any(x not in {"screened", "needs_followup"} for x in per_scope.values()):
        raise ValueError("An automated screen cannot certify clean or corrected metadata")
    if depth != "automated" and "screened" in per_scope.values():
        raise ValueError("screened is only for automated checks")
    if any(x in {"corrected", "needs_followup"} for x in per_scope.values()) and not note.strip():
        raise ValueError("Corrections and followups require a note")
    # The aggregate is descriptive only; queue clearance uses per-scope status.
    if "needs_followup" in per_scope.values():
        overall = "needs_followup"
    elif "corrected" in per_scope.values():
        overall = "corrected"
    elif "clean" in per_scope.values():
        overall = "clean"
    else:
        overall = "screened"
    row = by_key(repo, key)
    track = row["track"]
    when = datetime.now(timezone.utc).isoformat(timespec="microseconds")
    rec = {
        "schema": 2, "audit_id": "", "scope": list(scopes),
        "scope_outcomes": per_scope,
        "scope_sha256": {name: row["scope_sha256"][name] for name in scopes},
        "verification_basis": "automated_rules" if depth == "automated" else (
            "external_sources" if depth == "source_verified" else "manuscript_alignment"),
        "track": track, "lecture_id": row["lecture_id"], "audited_at": when,
        "reviewer": {"kind": kind, "model": model if kind == "model" else None,
                     "name": model if kind != "model" else None},
        "depth": depth, "outcome": overall, "note": note.strip(),
        "manuscript_sha256": row["manuscript_sha256"],
        "description_sha256": row["description_sha256"],
    }
    rec["audit_id"] = digest(json.dumps(rec, sort_keys=True, ensure_ascii=False))[:16]
    path = ledger_path(repo, track)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as stream:
        stream.write(json.dumps(rec, ensure_ascii=False, sort_keys=True) + "\n")
        stream.flush()
        os.fsync(stream.fileno())
    return rec


def report_history(repo: Path, key: str) -> list[dict]:
    row = by_key(repo, key)
    records = [r for r in read_ledger(repo, row["track"])
               if r.get("lecture_id") == row["lecture_id"]]
    return [dict(r, current=matches(r, row),
                 current_by_scope={name: matches(r, row, name) for name in record_scopes(r)})
            for r in records]


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path("."), help="Repository root")
    sub = parser.add_subparsers(dest="command", required=True)
    rank = sub.add_parser("rank", help="Rank all lectures; read-only unless --csv is supplied")
    rank.add_argument("--csv", type=Path, help="Write all ranked lectures to CSV")
    rank.add_argument("--top", type=int, default=25, help="Rows printed to stdout (0 = none)")
    rank.add_argument("--scope", choices=SCOPES, default="description",
                      help="Rank metadata audits of this field group; default description")
    history = sub.add_parser("history", help="Show recorded audits for one lecture")
    history.add_argument("lecture", help="track:id, e.g. history:003000")
    record = sub.add_parser("record", help="Record a completed audit of the CURRENT lecture revision")
    record.add_argument("lecture", help="track:id")
    record.add_argument("--reviewer-kind", default="model", choices=("model", "human", "tool"))
    record.add_argument("--model", help="Actual model identity (required when reviewer is a model)")
    record.add_argument("--depth", required=True, choices=DEPTHS)
    record.add_argument("--outcome", required=True, choices=OUTCOMES)
    record.add_argument("--note", default="", help="Concise audit findings or correction summary")
    record.add_argument("--scope", action="append", choices=SCOPES,
                        help="Specific metadata reviewed; repeat to name multiple fields")
    record.add_argument("--scope-outcome", action="append", default=[],
                        help="FIELD=clean/corrected/needs_followup (required per field for multiple scopes)")
    args = parser.parse_args(argv)
    repo = args.repo.resolve()
    try:
        if args.command == "rank":
            rows = all_ranks(repo, args.scope)
            if args.csv:
                args.csv.parent.mkdir(parents=True, exist_ok=True)
                columns = ["rank"] + [k for k in rows[0] if k != "rank"] if rows else []
                with args.csv.open("w", encoding="utf-8", newline="") as stream:
                    out = csv.DictWriter(stream, fieldnames=columns)
                    out.writeheader()
                    out.writerows(rows)
            if args.top > 0:
                for item in rows[:args.top]:
                    print(f"{item['rank']:4}  {item['priority_points']:3}  {item['lecture']:34} "
                          f"{item['review_state']:20} scope={item['audit_scope']} {item['risk_cues']}")
            from collections import Counter
            states = Counter(row["review_state"] for row in rows)
            print("Total:", len(rows), "; states:", ", ".join(f"{k}={v}" for k, v in sorted(states.items())),
                  file=sys.stderr)
            if args.csv:
                print("CSV:", args.csv, file=sys.stderr)
        elif args.command == "record":
            results = {}
            for value in args.scope_outcome:
                k, sep, v = value.partition("=")
                if not sep or k in results:
                    raise ValueError("Use unique --scope-outcome FIELD=OUTCOME pairs")
                results[k] = v
            print(json.dumps(record_audit(repo, args.lecture, args.reviewer_kind,
                                          args.model, args.depth, args.outcome,
                                          args.note, tuple(args.scope or ["description"]),
                                          results), ensure_ascii=False, indent=2))
        else:
            print(json.dumps(report_history(repo, args.lecture), ensure_ascii=False, indent=2))
    except (ValueError, OSError, KeyError) as error:
        parser.error(str(error))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
