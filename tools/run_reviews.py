#!/usr/bin/env python3
"""Lecture review runner: plan / run / adjudicate / report / verify.

Two-stage review of finished audio lectures. A bounded single-shot reviewer
(27b-class, no tools) *finds* under-supported or under-explained passages;
an agentic session *adjudicates*. Findings are identity-bearing records in
``reviews/registry/`` keyed by (track, lecture, category, anchor hash); runs
live in ``reviews/runs/`` with a compaction-safe progress checkpoint.

Invariants (see reviews/README.md): the tool reads pack content, writes only
under reviews/, never commits, and never blocks delivery.

Stdlib only. The reviewer is called through an OpenAI-compatible
``/chat/completions`` endpoint (default: this machine's LiteLLM proxy,
resolved from the pi settings file).
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import tempfile
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

# ---------------------------------------------------------------- paths

CATEGORIES = ("unverified_claim", "glossed_step", "unintroduced_term", "internal_conflict",
             "missing_wiki_link")
DEFAULT_REVIEWER_MODEL = "qwen3.8-27b-dbirks-hyperqwen-long"
DEFAULT_CONTRACT_VERSION = "v2"
TRACK_ROOTS = ("content", "draft-stages")


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sha_hex(data: bytes, n: int = 16) -> str:
    return hashlib.sha256(data).hexdigest()[:n]


def find_repo_root(start: Path) -> Path:
    d = start.resolve()
    while True:
        if (d / "reviews").is_dir() and any((d / r).is_dir() for r in TRACK_ROOTS):
            return d
        if d.parent == d:
            sys.exit(f"error: no repository root (with reviews/ and a track dir) at or above {start}")
        d = d.parent


def resolve_track(root: Path, name: str) -> Path:
    cands = [root / r / name for r in TRACK_ROOTS]
    hits = [c for c in cands if (c / "track.json").is_file()]
    if not hits:
        sys.exit(f"error: no track '{name}' under {', '.join(TRACK_ROOTS)}")
    if len(hits) > 1:
        print(f"warning: track '{name}' exists in several places; using {hits[0].relative_to(root)}",
              file=sys.stderr)
    return hits[0]


class Track:
    def __init__(self, root: Path, dir: Path):
        self.root = root
        self.dir = dir
        self.name = dir.name
        self.track_json = json.loads((dir / "track.json").read_text(encoding="utf-8"))
        self.sources_json_path = dir / "metadata" / "sources.json"
        self.sources = {}
        if self.sources_json_path.is_file():
            doc = json.loads(self.sources_json_path.read_text(encoding="utf-8"))
            self.sources = doc.get("sources", {}) if isinstance(doc, dict) else {}

    def lectures(self):
        return self.track_json.get("lectures", [])

    def unit(self, lecture_id: str):
        for l in self.lectures():
            if l.get("id") == lecture_id:
                return l
        return None

    def manuscript_path(self, lecture) -> Path:
        return self.dir / lecture["file"]

    def sidecar_path(self, lecture_id: str) -> Path:
        return self.dir / "metadata" / f"{lecture_id}.json"

    def sidecar(self, lecture_id: str):
        p = self.sidecar_path(lecture_id)
        if p.is_file():
            return json.loads(p.read_text(encoding="utf-8"))
        return None


# ---------------------------------------------------------------- extraction

BEGIN = "<!-- BEGIN SPOKEN LECTURE -->"
END = "<!-- END SPOKEN LECTURE -->"


def extract_spoken(text: str) -> str:
    """Spoken narration between the markers; headers/emphasis stripped."""
    if text.count(BEGIN) != 1 or text.count(END) != 1:
        raise ValueError("expected exactly one spoken-region marker pair")
    spoken = text[text.index(BEGIN) + len(BEGIN):text.index(END)].strip()
    if not spoken:
        raise ValueError("empty spoken region")
    spoken = re.sub(r"(?m)^#{1,6}\s+", "", spoken)
    spoken = re.sub(r"(?<!\*)\*\*([^\n*]+?)\*\*(?!\*)", r"\1", spoken)
    spoken = re.sub(r"(?<!\w)(?<!\*)\*([^\n*]+?)\*(?!\w)", r"\1", spoken)
    return spoken + "\n"


def extract_companion(text: str) -> str:
    """The non-spoken material after the END marker (further reading etc.)."""
    if text.count(END) != 1:
        return ""
    return text[text.index(END) + len(END):].strip()


# ---------------------------------------------------------------- revision

def unit_revision(track: Track, lecture_id: str) -> str:
    h = hashlib.sha256()
    lec = track.unit(lecture_id)
    if lec is None:
        raise ValueError(f"unknown lecture {lecture_id}")
    h.update(b"man\x00" + track.manuscript_path(lec).read_bytes())
    sp = track.sidecar_path(lecture_id)
    h.update(b"side\x00" + (sp.read_bytes() if sp.is_file() else b""))
    h.update(b"src\x00" + (track.sources_json_path.read_bytes() if track.sources_json_path.is_file() else b""))
    h.update(b"trk\x00" + (track.dir / "track.json").read_bytes())
    return h.hexdigest()[:16]


# ---------------------------------------------------------------- anchor

def _collapse(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def verify_anchor(as_quoted: str, narration: str) -> str | None:
    """Return the verbatim text in ``narration`` matching ``as_quoted``, else None.

    Tries the raw quote first, then a whitespace-tolerant match (word-by-word
    regex) so a reviewer that reflows a line break still lands on the true
    text. The stored anchor is always the narration's own bytes."""
    q = as_quoted.strip()
    if not q:
        return None
    if q in narration:
        return q
    words = [_collapse(w) for w in q.split()]
    if not words:
        return None
    pat = r"\s+".join(re.escape(w) for w in words)
    m = re.search(pat, narration)
    return m.group(0) if m else None


# ---------------------------------------------------------------- store

def _write_json(path: Path, obj) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=str(path.parent), prefix=path.name + ".", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            json.dump(obj, fh, indent=1, ensure_ascii=False)
            fh.write("\n")
        os.replace(tmp, path)
    finally:
        if os.path.exists(tmp):
            os.remove(tmp)


def _read_jsonl(path: Path) -> list[dict]:
    if not path.is_file():
        return []
    out = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line:
            out.append(json.loads(line))
    return out


def _write_jsonl(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=str(path.parent), prefix=path.name + ".", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            for r in rows:
                fh.write(json.dumps(r, ensure_ascii=False) + "\n")
        os.replace(tmp, path)
    finally:
        if os.path.exists(tmp):
            os.remove(tmp)


class Store:
    def __init__(self, root: Path):
        self.root = root
        self.reg_dir = root / "reviews" / "registry"
        self.runs_dir = root / "reviews" / "runs"

    def findings_path(self, track_name: str) -> Path:
        return self.reg_dir / f"findings-{track_name}.jsonl"

    def coverage_path(self, track_name: str) -> Path:
        return self.reg_dir / f"coverage-{track_name}.jsonl"

    def load_findings(self, track_name: str) -> list[dict]:
        return _read_jsonl(self.findings_path(track_name))

    def save_findings(self, track_name: str, rows: list[dict]) -> None:
        _write_jsonl(self.findings_path(track_name), rows)

    def load_coverage(self, track_name: str) -> list[dict]:
        return _read_jsonl(self.coverage_path(track_name))

    def save_coverage(self, track_name: str, rows: list[dict]) -> None:
        _write_jsonl(self.coverage_path(track_name), rows)

    def coverage_row(self, track_name: str, lecture_id: str):
        for r in self.load_coverage(track_name):
            if r.get("lecture_id") == lecture_id:
                return r
        return None

    def put_coverage(self, track_name: str, row: dict) -> None:
        rows = [r for r in self.load_coverage(track_name) if r.get("lecture_id") != row["lecture_id"]]
        rows.append(row)
        rows.sort(key=lambda r: r.get("lecture_id", ""))
        self.save_coverage(track_name, rows)


def new_run_id(store: Store, track_name: str, today: str | None = None) -> str:
    today = today or datetime.now(timezone.utc).strftime("%Y%m%d")
    base = f"R-{today}-{track_name}"
    rid = base
    n = 2
    while (store.runs_dir / rid).exists():
        rid = f"{base}-{n}"
        n += 1
    return rid


class Run:
    def __init__(self, store: Store, run_id: str):
        self.store = store
        self.id = run_id
        self.dir = store.runs_dir / run_id
        self.progress_path = self.dir / "progress.json"

    def exists(self) -> bool:
        return self.progress_path.is_file()

    def create(self, track: Track, units: list[str], contract: str, model: str) -> None:
        _write_json(self.dir / "run.yaml", {
            "run": self.id,
            "track": track.name,
            "created": now_iso(),
            "contract_version": contract,
            "reviewer": {"model": model, "session": os.environ.get("PI_SESSION_ID", "")},
            "adjudicator": {"model": "", "session": os.environ.get("PI_SESSION_ID", ""),
                            "model_actual": ""},
        })
        _write_json(self.progress_path, {
            "run": self.id,
            "track": track.name,
            "created": now_iso(),
            "units_total": len(units),
            "order": units,
            "stages": {},
            "in_progress": None,
        })

    def progress(self) -> dict:
        return json.loads(self.progress_path.read_text(encoding="utf-8"))

    def save_progress(self, p: dict) -> None:
        _write_json(self.progress_path, p)

    def set_stage(self, lecture_id: str, stage: str, revision: str, meta: dict | None = None) -> None:
        p = self.progress()
        p["stages"][lecture_id] = {"stage": stage, "at": now_iso(), "revision": revision}
        if meta:
            p["stages"][lecture_id].update(meta)
        p["in_progress"] = None if stage == "adjudicated" else {"unit": lecture_id, "stage": stage}
        self.save_progress(p)

    def stage_of(self, lecture_id: str) -> str | None:
        return (self.progress()["stages"].get(lecture_id) or {}).get("stage")

    def raw_path(self, lecture_id: str) -> Path:
        return self.dir / "raw" / f"{lecture_id}.json"


def load_run_yaml(run: Run) -> dict:
    return json.loads((run.dir / "run.yaml").read_text(encoding="utf-8"))


# ---------------------------------------------------------------- reviewer

def resolve_litellm():
    base = os.environ.get("LITELLM_BASE_URL")
    key = os.environ.get("LITELLM_API_KEY")
    if not (base and key):
        cfg = Path.home() / ".pi" / "agent" / "settings.json"
        if cfg.is_file():
            try:
                doc = json.loads(cfg.read_text(encoding="utf-8"))
                prov = doc.get("litellm", {}).get("providers", {}).get("litellm", {})
                base = base or prov.get("baseUrl")
                key = key or prov.get("apiKey")
            except (json.JSONDecodeError, OSError):
                pass
    if not (base and key):
        sys.exit("error: no LITELLM_BASE_URL/LITELLM_API_KEY (and no pi settings fallback)")
    if "0.0.0.0" in base:
        base = base.replace("0.0.0.0", "127.0.0.1")
    return base, key


def call_reviewer(base: str, key: str, model: str, system: str, user: str,
                  timeout: int = 900, attempts: int = 3) -> dict:
    body = json.dumps({
        "model": model, "temperature": 0, "max_tokens": 32768,
        "messages": [{"role": "system", "content": system},
                     {"role": "user", "content": user}],
    }).encode("utf-8")
    last = None
    for i in range(attempts):
        req = urllib.request.Request(
            base.rstrip("/") + "/chat/completions", data=body, method="POST",
            headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                doc = json.loads(resp.read().decode("utf-8"))
            return doc
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, json.JSONDecodeError) as e:
            detail = ""
            if isinstance(e, urllib.error.HTTPError):
                detail = e.read()[:800].decode("utf-8", "replace")
            last = RuntimeError(f"{e} {detail}")
            if i < attempts - 1:
                time.sleep(5 * (i + 1))
    raise RuntimeError(f"reviewer call failed after {attempts} attempts: {last}")


class ReviewerOutputError(RuntimeError):
    pass


def parse_findings(doc: dict) -> list[dict]:
    msg = doc["choices"][0]["message"]
    content = msg.get("content") or msg.get("reasoning_content") or ""
    text = content.strip()
    if text.startswith("```"):
        text = text.strip("`")
        if text.lower().startswith("json"):
            text = text[4:]
    try:
        arr = json.loads(text)
    except json.JSONDecodeError:
        # Reasoning models may prefix or surround the array with prose;
        # take the outermost bracket span once.
        i, j = text.find("["), text.rfind("]")
        if i < 0 or j <= i:
            raise ReviewerOutputError(
                f"no JSON array in reviewer output (finish={doc['choices'][0].get('finish_reason')!r}, "
                f"first 200 chars: {text[:200]!r})")
        try:
            arr = json.loads(text[i:j + 1])
        except json.JSONDecodeError as e:
            raise ReviewerOutputError(f"bracket span is not JSON: {e}")
    if not isinstance(arr, list):
        raise ReviewerOutputError("reviewer did not return a JSON array")
    out = []
    for f in arr:
        if not isinstance(f, dict):
            continue
        cat = f.get("category")
        anchor = f.get("anchor")
        if cat not in CATEGORIES or not isinstance(anchor, str) or not anchor.strip():
            continue
        if not isinstance(f.get("claim"), str) or not isinstance(f.get("detail"), str):
            continue
        conf = f.get("confidence")
        sids = f.get("source_ids")
        rec = {
            "category": cat,
            "anchor_as_quoted": anchor.strip(),
            "claim": f["claim"].strip(),
            "detail": f["detail"].strip(),
            "confidence": conf if conf in ("high", "low") else "low",
            "source_ids": [s for s in sids if isinstance(s, str)] if isinstance(sids, list) else [],
        }
        if isinstance(f.get("wiki_articles"), list):
            rec["wiki_articles"] = [str(s)[:120] for s in f["wiki_articles"]][:3]
        out.append(rec)
    return out[:12]


def build_payload(track: Track, lecture: dict, spoken: str, companion: str = "",
                  lean: bool = False) -> str:
    """lean: bulk wiki pass — narration + companion + sidecar only; the source
    registry and policy are irrelevant to the missing_wiki_link check."""
    lec_id = lecture["id"]
    sidecar = track.sidecar(lec_id) or {}
    parts = [
        f"TRACK: {track.track_json.get('title', track.name)}",
        "LECTURE: " + str(lecture.get("title", lec_id)),
        "",
        "SPOKEN NARRATION (the only text you may quote verbatim in anchors):",
        "<<<NARRATION",
        spoken.strip(),
        "NARRATION>>>",
    ]
    if lean:
        parts += [
            "",
            "LECTURE METADATA (sidecar; context only, never quote from it):",
            json.dumps(sidecar, ensure_ascii=False, indent=1) if sidecar else "(none)",
        ]
        if companion:
            parts += [
                "",
                "FURTHER READING / NON-SPKEN COMPANION (context only; shows which "
                "entry points the lecture already offers, including any Wikipedia "
                "links; never quote from it):",
                "<<<COMPANION",
                companion,
                "COMPANION>>>",
            ]
        return "\n".join(parts)

    policy = track.track_json.get("editorial_policy") or "(none)"
    parts = [
        f"TRACK: {track.track_json.get('title', track.name)}",
        "TRACK EDITORIAL POLICY (context only):",
        policy,
        "",
        "SPOKEN NARRATION (the only text you may quote verbatim in anchors):",
        "<<<NARRATION",
        spoken.strip(),
        "NARRATION>>>",
        "",
        "LECTURE METADATA (sidecar; context only, never quote from it):",
        json.dumps(sidecar, ensure_ascii=False, indent=1) if sidecar else "(none)",
        "",
        f"RESOURCES REGISTERED FOR THIS LECTURE ({len(sidecar.get('related_resources', []))} of {len(track.sources)} track sources; id | title | kind | access | url | why registered):",
    ]
    seen = set()
    for rr in sidecar.get("related_resources", []):
        sid = rr.get("source_id")
        rec = track.sources.get(sid, {})
        parts.append(f"- {sid} | {rec.get('title','?')} | {rec.get('kind','?')} | "
                     f"{rec.get('access','?')} | {rec.get('url','')} | {rr.get('reason','')}")
        seen.add(sid)
    if not sidecar.get("related_resources"):
        parts.append("- (none registered)")
    parts += [
        "",
        f"FULL TRACK SOURCE REGISTRY ({len(track.sources)} sources; id | title | kind | url):",
    ]
    for sid, rec in track.sources.items():
        parts.append(f"- {sid} | {rec.get('title','?')} | {rec.get('kind','?')} | {rec.get('url','')}")
    if companion:
        parts += [
            "",
            "FURTHER READING / NON-SPKEN COMPANION (context only; shows which entry "
            "points the lecture already offers, including any Wikipedia links; "
            "never quote from it):",
            "<<<COMPANION",
            companion,
            "COMPANION>>>",
        ]
    return "\n".join(parts)


# ---------------------------------------------------------------- registry

def finding_identity(track_name: str, lecture_id: str, category: str, anchor: str) -> str:
    return f"{track_name}/{lecture_id}#{category}#{sha_hex(_collapse(anchor).encode('utf-8'), 12)}"


def upsert_findings(store: Store, track: Track, lecture_id: str, run_id: str,
                    revision: str, findings: list[dict], narration: str) -> tuple[list[dict], int]:
    """Apply this run's accepted findings to the registry. Returns (rows, dropped)."""
    rows = store.load_findings(track.name)
    dropped = 0
    at = now_iso()
    for f in findings:
        anchor = verify_anchor(f["anchor_as_quoted"], narration)
        if anchor is None:
            dropped += 1
            continue
        f = {**f, "anchor": anchor}
        fid = finding_identity(track.name, lecture_id, f["category"], anchor)
        existing = next((r for r in rows if r.get("finding_id") == fid), None)
        if existing is None:
            rows.append({
                "finding_id": fid, "track": track.name, "lecture_id": lecture_id,
                **f,
                "status": "open",
                "first_seen": {"run": run_id, "revision": revision, "at": at},
                "last_seen": {"run": run_id, "revision": revision, "at": at},
                "history": [{"status": "open", "run": run_id, "at": at}],
            })
        else:
            st = existing.get("status")
            existing["last_seen"] = {"run": run_id, "revision": revision, "at": at}
            if "wiki_articles" not in existing and "wiki_articles" in f:
                existing["wiki_articles"] = f["wiki_articles"]
            if st == "resolved" and revision != (existing.get("resolution") or {}).get("revision"):
                existing["status"] = "open"
                existing["history"].append({"status": "open", "run": run_id, "at": at,
                                           "note": "regression: re-flagged at new revision"})
            elif st not in ("open", "confirmed", "deferred"):
                # rejected / stale: keep status; persistence visible via last_seen
                pass
    # Stale sweep: prior live findings whose anchor no longer occurs in this
    # revision were reworded or removed by a fix.
    for r in rows:
        if r.get("lecture_id") != lecture_id:
            continue
        if r.get("status") in ("open", "confirmed", "deferred"):
            if (r.get("last_seen") or {}).get("revision") != revision:
                if verify_anchor(r.get("anchor", ""), narration) is None:
                    r["status"] = "stale"
                    r["history"].append({"status": "stale", "run": run_id, "at": at,
                                         "note": "anchor no longer present at new revision"})
    rows.sort(key=lambda r: (r.get("lecture_id", ""), r.get("finding_id", "")))
    return rows, dropped


def unit_finding_rows(store: Store, track_name: str, lecture_id: str) -> list[dict]:
    return [r for r in store.load_findings(track_name) if r.get("lecture_id") == lecture_id]


def unit_active(store: Store, track_name: str, lecture_id: str) -> int:
    return sum(1 for r in unit_finding_rows(store, track_name, lecture_id)
               if r.get("status") in ("open", "confirmed", "deferred"))


def unit_is_adjudicated(store: Store, track_name: str, lecture_id: str) -> bool:
    rows = unit_finding_rows(store, track_name, lecture_id)
    return all(r.get("status") in ("rejected", "resolved", "stale") for r in rows)


# ---------------------------------------------------------------- plan

def version_num(contract: str | None) -> int:
    if not contract:
        return 0
    m = re.search(r"(\d+)", str(contract))
    return int(m.group(1)) if m else 0


def unit_status(store: Store, track: Track, lecture_id: str,
                current_contract: str | None = None):
    rev = unit_revision(track, lecture_id)
    cov = store.coverage_row(track.name, lecture_id) or {}
    active = unit_active(store, track.name, lecture_id)
    if not cov:
        needed = "never_reviewed"
    elif cov.get("revision") != rev:
        needed = "stale"
    elif active:
        needed = "has_active"
    else:
        needed = "current"
    recheck = bool(current_contract) and version_num(cov.get("contract")) > 0 and \
        version_num(cov.get("contract")) < version_num(current_contract)
    # A wiki-bulk-only pass (contract ending in 'w') has not reviewed the other
    # categories: a full-contract run must not treat it as current.
    if needed == "current" and current_contract and cov.get("contract") and \
            str(cov["contract"]).endswith("w") != str(current_contract).endswith("w"):
        needed = "contract_kind"
    return {"id": lecture_id, "revision": rev, "last_run": cov.get("run"),
            "outcome": cov.get("outcome"), "active": active, "needed": needed,
            "contract": cov.get("contract"), "recheck": recheck}


def needs_work(u: dict) -> bool:
    return u["needed"] in ("never_reviewed", "stale", "has_active", "contract_kind")


def unit_wiki_needed(store: Store, track: Track, lecture_id: str) -> bool:
    """Bulk wiki pre-pass: skip units whose wiki question is already answered
    at the current revision — a live or rejected finding, a resolved finding
    last seen here, or a wiki:clean coverage row at this revision."""
    rev = unit_revision(track, lecture_id)
    for r in store.load_findings(track.name):
        if r["lecture_id"] != lecture_id or r["category"] != "missing_wiki_link":
            continue
        if r["status"] in ("open", "confirmed", "rejected"):
            return False
        if r["status"] == "resolved" and (r.get("last_seen") or {}).get("revision") == rev:
            return False
    cov = store.coverage_row(track.name, lecture_id)
    if cov and str(cov.get("contract", "")).endswith("w") and \
            cov.get("revision") == rev and cov.get("outcome") == "wiki:clean":
        return False
    return True


# ---------------------------------------------------------------- commands

def cmd_plan(args) -> None:
    root = find_repo_root(Path(args.repo) if args.repo else Path.cwd())
    track = Track(root, resolve_track(root, args.track))
    store = Store(root)
    rows = []
    for l in track.lectures():
        if not track.manuscript_path(l).is_file():
            continue
        rows.append(unit_status(store, track, l["id"], args.contract_version))
    if args.format == "json":
        print(json.dumps(rows, indent=1))
        return
    print(f"{'id':>8}  {'needed':<15} {'active':>6}  {'contract':<9} {'last run':<22} "
          f"{'outcome':<14} title")
    for u in rows:
        mark = " *" if needs_work(u) or u["recheck"] else ""
        print(f"{u['id']:>8}  {u['needed']:<15} {u['active']:>6}  "
              f"{str(u['contract'] or '-'):9.9} {str(u['last_run'] or '-'):22.22} "
              f"{str(u['outcome'] or '-'):14.14} "
              f"{track.unit(u['id']).get('title','')[:56]}{mark}")
    work = [u for u in rows if needs_work(u)]
    recheck = [u for u in rows if u["recheck"] and not needs_work(u)]
    print(f"\n{len(work)} of {len(rows)} units need work "
          f"(never: {sum(1 for u in work if u['needed']=='never_reviewed')}, "
          f"stale: {sum(1 for u in work if u['needed']=='stale')}, "
          f"active: {sum(1 for u in work if u['needed']=='has_active')}); "
          f"{len(recheck)} more would be rechecked under contract "
          f"{args.contract_version} with --recheck-contract")


def contract_text(root: Path, version: str) -> str:
    return (root / "reviews" / "contract" / f"prompt-{version}.md").read_text(encoding="utf-8")


def process_unit(track: Track, store: Store, run: Run, lecture: dict, model: str,
                 base: str, key: str, contract: str, wiki: bool = False) -> dict:
    lec_id = lecture["id"]
    revision = unit_revision(track, lec_id)
    stage = run.stage_of(lec_id)
    raw_text = track.manuscript_path(lecture).read_text(encoding="utf-8")
    spoken = extract_spoken(raw_text)
    companion = extract_companion(raw_text)

    stage_rec = run.progress()["stages"].get(lec_id) or {}
    # If the content moved since the raw response was captured, the old
    # response must not be applied to the new revision: re-bill the reviewer.
    if stage in ("reviewed", "verified", "adjudicated") and \
            stage_rec.get("revision") != revision:
        stage = None

    raw = None
    if stage in (None, "review_failed"):
        try:
            doc = call_reviewer(base, key, model,
                                contract_text(root_of(run), contract),
                                build_payload(track, lecture, spoken, companion, lean=wiki))
        except ReviewerOutputError as e:
            _write_json(run.raw_path(lec_id), {"model": model, "at": now_iso(),
                                               "error": str(e)[:500], "response": None,
                                               "reasoning": None, "usage": None})
            run.set_stage(lec_id, "review_failed", revision, meta={"error": str(e)[:500]})
            return {"id": lec_id, "stage": "review_failed", "findings": 0, "dropped": 0,
                    "active": unit_active(store, track.name, lec_id),
                    "revision": revision, "error": str(e)[:200]}
        choice = doc["choices"][0]
        msg = choice["message"]
        raw = {"model": model, "at": now_iso(),
               "request_chars": len(build_payload(track, lecture, spoken, companion,
                                                  lean=wiki)),
               "usage": doc.get("usage"),
               "finish_reason": choice.get("finish_reason"),
               "response": msg.get("content"),
               "reasoning": msg.get("reasoning_content")}
        _write_json(run.raw_path(lec_id), raw)
        run.set_stage(lec_id, "reviewed", revision)
    else:
        raw = json.loads(run.raw_path(lec_id).read_text(encoding="utf-8")) if run.raw_path(lec_id).is_file() else None

    if raw is None:
        findings = []
    else:
        try:
            findings = parse_findings({"choices": [{"message": {
                "content": raw.get("response"), "reasoning_content": raw.get("reasoning")}}]})
        except ReviewerOutputError as e:
            run.set_stage(lec_id, "review_failed", revision, meta={"error": str(e)[:500]})
            return {"id": lec_id, "stage": "review_failed", "findings": 0,
                    "dropped": 0, "active": unit_active(store, track.name, lec_id),
                    "revision": revision, "error": str(e)[:200]}
    rows, dropped = upsert_findings(store, track, lec_id, run.id, revision, findings, spoken)
    store.save_findings(track.name, rows)
    accepted = len(findings) - dropped

    active = unit_active(store, track.name, lec_id)
    outcome = "clean" if not accepted else f"findings:{accepted}"
    if wiki:
        outcome = "wiki:clean" if not accepted else f"wiki:{accepted}"
    cov = {"track": track.name, "lecture_id": lec_id, "revision": revision, "run": run.id,
           "reviewed_at": now_iso(), "contract": contract,
           "outcome": outcome,
           "open": active}
    if unit_is_adjudicated(store, track.name, lec_id):
        cov["adjudicated_at"] = now_iso()
    store.put_coverage(track.name, cov)

    new_stage = "adjudicated" if unit_is_adjudicated(store, track.name, lec_id) else "verified"
    run.set_stage(lec_id, new_stage, revision,
                  meta={"findings": accepted, "dropped": dropped,
                        "active": active} if raw else None)
    return {"id": lec_id, "stage": new_stage, "findings": accepted,
            "dropped": dropped, "active": active, "revision": revision}


def root_of(run: Run) -> Path:
    return run.store.root


def cmd_run(args) -> None:
    root = find_repo_root(Path(args.repo) if args.repo else Path.cwd())
    track = Track(root, resolve_track(root, args.track))
    store = Store(root)
    base, key = resolve_litellm()
    wiki = args.prompt_variant == "wiki"
    contract = args.contract_version + ("w" if wiki else "")

    if args.fresh or not args.resume:
        run = Run(store, new_run_id(store, track.name))
    else:
        run = Run(store, args.resume)
        if not run.exists():
            sys.exit(f"error: no run {args.resume} under {store.runs_dir}")

    statuses = {u["id"]: u for u in
                (unit_status(store, track, l["id"], args.contract_version) for l in track.lectures()
                 if track.manuscript_path(l).is_file())}
    if args.unit:
        missing = [u for u in args.unit if u not in statuses]
        if missing:
            sys.exit(f"error: unknown lecture id(s): {', '.join(missing)}")
        order = args.unit
    elif wiki:
        # Bulk pre-pass: only units that still need a wiki check; already
        # flagged / rejected / cleared units are not re-billed.
        order = [u for u in statuses if unit_wiki_needed(store, track, u)]
        if args.limit:
            order = order[:args.limit]
    else:
        order = [u for u, s in statuses.items()
                 if needs_work(s) or (args.recheck_contract and s.get("recheck"))]
        if args.limit:
            order = order[:args.limit]
    if not order:
        print(f"nothing to review in {track.name}; all units current")
        return

    if args.dry_run:
        for lec_id in order:
            lec = track.unit(lec_id)
            raw_text = track.manuscript_path(lec).read_text(encoding="utf-8")
            payload = build_payload(track, lec, extract_spoken(raw_text),
                                    extract_companion(raw_text), lean=wiki)
            print(f"[dry-run] {lec_id} would call {args.model} ({len(payload)} chars payload)")
        return

    if not run.exists():
        run.create(track, order, f"prompt-{contract}", args.model)
        print(f"started run {run.id} ({len(order)} units, reviewer {args.model}, "
              f"contract prompt-{contract})")

    done = 0
    for lec_id in order:
        lecture = track.unit(lec_id)
        try:
            result = process_unit(track, store, run, lecture, args.model, base, key,
                                  contract, wiki=wiki)
        except Exception as e:
            run.set_stage(lec_id, "failed", unit_revision(track, lec_id),
                          meta={"error": f"{type(e).__name__}: {str(e)[:200]}"})
            print(f"FAILED {lec_id}: {type(e).__name__}: {str(e)[:160]} "
                  f"(recorded in progress; retry on --resume)", file=sys.stderr)
            continue
        note = f"{result['findings']} findings ({result['dropped']} dropped), {result['active']} active"
        print(f"reviewed {lec_id} [{result['stage']}]: {note}; "
              f"commit when ready (small batches keep attribution clean)")
        done += 1
        if args.one:
            break
    print(f"{done} unit(s) this invocation; progress at {run.progress_path}")


def cmd_adjudicate(args) -> None:
    root = find_repo_root(Path(args.repo) if args.repo else Path.cwd())
    track = Track(root, resolve_track(root, args.track))
    store = Store(root)
    run = Run(store, args.run)
    if not run.exists():
        sys.exit(f"error: no run {args.run}")

    as_ = args.as_id or os.environ.get("PI_SESSION_ID") or "human"
    rows = store.load_findings(track.name)
    targets = unit_finding_rows(store, track.name, args.unit) if args.unit else rows
    if not targets and not args.decisions_file:
        sys.exit(f"error: no findings on record{f' for {args.unit}' if args.unit else ''}")

    decisions = {}
    if args.finding and args.decision:
        for fid, d in zip(args.finding, args.decision):
            decisions[fid] = {"decision": d, "note": args.note or ""}
    if args.decisions_file:
        valid = {"confirmed", "rejected", "deferred", "resolved"}
        data = json.loads(Path(args.decisions_file).read_text(encoding="utf-8"))
        for fid, item in data.items():
            if not isinstance(item, dict) or item.get("decision") not in valid:
                sys.exit(f"error: bad decision {item.get('decision')!r} for {fid} "
                         f"in {args.decisions_file}")
            decisions[fid] = {"decision": item["decision"],
                              "note": str(item.get("note", ""))}
        print(f"loaded {len(data)} decision(s) from {args.decisions_file}")

    spoken = ""
    if args.unit:
        spoken = extract_spoken(track.manuscript_path(track.unit(args.unit)).read_text(encoding="utf-8"))
    if (args.interactive or not decisions) and targets:
        for r in targets:
            if r.get("status") not in ("open", "confirmed", "deferred") or (
                    decisions and r["finding_id"] in decisions):
                continue
            anchor = r.get("anchor", "")
            i = spoken.find(anchor)
            ctx = spoken[max(0, i - 200): i + len(anchor) + 200] if i >= 0 else "(anchor not located)"
            print(f"\n=== {r['finding_id']}  [{r['status']}] conf={r.get('confidence')}")
            print(f"category : {r['category']}")
            print(f"claim    : {r['claim']}")
            print(f"detail   : {r['detail']}")
            print(f"sources  : {', '.join(r.get('source_ids', [])) or '(none)'}")
            print(f"--- context ---\n…{ctx}…")
            if args.interactive:
                d = input("decision [c]onfirmed / [r]ejected / [d]eferred / [s]resolved / [e]nter skip: ").strip().lower()
                note = input("note: ").strip() if d in "crds" else ""
                if d:
                    decisions[r["finding_id"]] = {"decision": {"c": "confirmed", "r": "rejected",
                                                               "d": "deferred", "s": "resolved"}[d[0]],
                                                  "note": note}
    if not decisions:
        print("no decisions given; nothing changed")
        return

    now = now_iso()
    for r in rows:
        if r["finding_id"] not in decisions:
            continue
        d = decisions[r["finding_id"]]
        r["adjudication"] = {"by": as_, "decision": d["decision"], "note": d["note"], "at": now}
        if d["decision"] == "resolved":
            r["status"] = "resolved"
            r["resolution"] = {"revision": unit_revision(track, r["lecture_id"]),
                               "note": d["note"], "at": now}
        else:
            r["status"] = d["decision"]
        r["history"].append({"status": d["decision"], "run": run.id, "at": now, "by": as_})
    rows.sort(key=lambda r: (r.get("lecture_id", ""), r.get("finding_id", "")))
    store.save_findings(track.name, rows)

    if args.model:
        meta = load_run_yaml(run)
        meta["adjudicator"].update({"model": args.model,
                                    "model_actual": args.model_actual or ""})
        _write_json(run.dir / "run.yaml", meta)

    if args.unit:
        active = unit_active(store, track.name, args.unit)
        cov = store.coverage_row(track.name, args.unit) or {}
        cov.update({"open": active})
        if unit_is_adjudicated(store, track.name, args.unit):
            cov["adjudicated_at"] = now
            stage = "adjudicated"
        else:
            stage = "verified"
        store.put_coverage(track.name, {**cov, "lecture_id": args.unit})
        run.set_stage(args.unit, stage, cov.get("revision", ""))
        print(f"{len(decisions)} decision(s) recorded for {args.unit}; "
              f"{active} still active; unit={stage}")
    else:
        affected = sorted({r["lecture_id"] for fid in decisions
                           for r in rows if r["finding_id"] == fid})
        for lec in affected:
            active = unit_active(store, track.name, lec)
            cov = store.coverage_row(track.name, lec) or {}
            cov.update({"open": active})
            if unit_is_adjudicated(store, track.name, lec):
                cov["adjudicated_at"] = now
            store.put_coverage(track.name, {**cov, "lecture_id": lec})
        print(f"{len(decisions)} decision(s) recorded across {len(affected)} lecture(s)")


def cmd_report(args) -> None:
    root = find_repo_root(Path(args.repo) if args.repo else Path.cwd())
    store = Store(root)
    run = Run(store, args.run) if args.run else None
    if run and run.exists():
        meta = load_run_yaml(run)
        track = Track(root, resolve_track(root, meta["track"]))
    else:
        track = Track(root, resolve_track(root, args.track))
        meta = None

    out = ["# Review report", ""]
    if meta:
        out += [f"- run: `{meta['run']}` (track `{meta['track']}`, contract `{meta['contract_version']}`)",
                f"- reviewer: `{meta['reviewer'].get('model')}` "
                f"(session `{meta['reviewer'].get('session') or 'n/a'}`)",
                f"- adjudicator: `{meta['adjudicator'].get('model') or 'session tier'}` "
                f"(session `{meta['adjudicator'].get('session') or 'n/a'}`)", ""]
    rows = store.load_findings(track.name)
    covs = {c["lecture_id"]: c for c in store.load_coverage(track.name)}
    prog = run.progress() if run and run.exists() else None

    by_status = {s: [] for s in ("open", "confirmed", "deferred", "resolved", "rejected", "stale")}
    for r in rows:
        by_status[r.get("status", "open")].append(r)

    out += [f"## Findings ({len(rows)} total)", ""]
    for s in ("open", "confirmed", "deferred"):
        if not by_status[s]:
            continue
        out.append(f"### {s} ({len(by_status[s])})")
        out.append("")
        for r in sorted(by_status[s], key=lambda r: r["lecture_id"]):
            out += [f"- **{r['lecture_id']}** `{r['category']}` (conf={r.get('confidence')})",
                    f"  - claim: {r['claim']}",
                    f"  - detail: {r['detail']}",
                    f"  - anchor: “{r['anchor']}”",
                    f"  - adjudication: {json.dumps(r.get('adjudication') or {}, ensure_ascii=False)}"]
        out.append("")
    for s in ("resolved", "rejected", "stale"):
        if by_status[s]:
            out += [f"### {s} ({len(by_status[s])}) — closed", ""]
            for r in sorted(by_status[s], key=lambda r: r["lecture_id"])[:25]:
                out.append(f"- {r['lecture_id']} `{r['category']}`: {r['claim'][:110]}")
            if len(by_status[s]) > 25:
                out.append(f"- …and {len(by_status[s]) - 25} more")
            out.append("")

    if prog:
        stages = prog.get("stages", {})
        out += ["## Unit progress", ""]
        out.append("| unit | stage | findings | active | at |")
        out.append("|---|---|---|---|---|")
        for uid, st in stages.items():
            out.append(f"| {uid} | {st.get('stage')} | {st.get('findings', '-')} | "
                       f"{st.get('active', '-')} | {st.get('at','')} |")
        out.append("")

    text = "\n".join(out)
    if args.out:
        Path(args.out).write_text(text, encoding="utf-8")
        print(f"wrote {args.out}")
    elif run:
        p = run.dir / "report.md"
        p.write_text(text, encoding="utf-8")
        print(f"wrote {p}")
    else:
        print(text)


def cmd_verify(args) -> None:
    root = find_repo_root(Path(args.repo) if args.repo else Path.cwd())
    store = Store(root)
    problems = 0

    # Disjointness: nothing under reviews/ may live inside a pack scope.
    for p in root.glob("content/*/") :
        if (p / "reviews").exists():
            print(f"FAIL: {p} contains a reviews/ dir (packs must be disjoint)")
            problems += 1
    for p in root.glob("draft-stages/*/"):
        if (p / "reviews").exists():
            print(f"FAIL: {p} contains a reviews/ dir (packs must be disjoint)")
            problems += 1

    for reg in sorted(store.reg_dir.glob("findings-*.jsonl")):
        track_name = reg.stem.replace("findings-", "")
        try:
            track = Track(root, resolve_track(root, track_name))
        except SystemExit:
            print(f"FAIL: registry {reg.name} but no track '{track_name}' in the repo")
            problems += 1
            continue
        rows = store.load_findings(track_name)
        seen_ids = set()
        for r in rows:
            fid = r.get("finding_id")
            if fid in seen_ids:
                print(f"FAIL: duplicate finding_id {fid}")
                problems += 1
            seen_ids.add(fid)
            if r.get("category") not in CATEGORIES:
                print(f"FAIL: {fid} bad category {r.get('category')}")
                problems += 1
            if r.get("status") not in ("open", "confirmed", "deferred", "resolved", "rejected", "stale"):
                print(f"FAIL: {fid} bad status {r.get('status')}")
                problems += 1
            if r.get("status") in ("confirmed", "resolved") and not r.get("adjudication"):
                print(f"FAIL: {fid} is {r['status']} without an adjudication record")
                problems += 1
            if r.get("status") == "resolved" and not (r.get("resolution") or {}).get("revision"):
                print(f"FAIL: {fid} resolved without a revision")
                problems += 1
        # Anchor re-check against the CURRENT text for findings live at the
        # current revision; a miss means the text moved without a review.
        for r in rows:
            if r.get("status") in ("open", "confirmed", "deferred"):
                cov = store.coverage_row(track_name, r["lecture_id"])
                if cov and cov.get("revision") == (r.get("last_seen") or {}).get("revision"):
                    try:
                        spoken = extract_spoken(
                            track.manuscript_path(track.unit(r["lecture_id"])).read_text(encoding="utf-8"))
                    except (OSError, ValueError, KeyError):
                        continue
                    if verify_anchor(r.get("anchor", ""), spoken) is None:
                        print(f"WARN: {fid} anchor not found in current text "
                              f"(coverage says revision unchanged — check drift)")
                        problems += 1
    for run_dir in sorted(store.runs_dir.iterdir()) if store.runs_dir.is_dir() else []:
        if not run_dir.is_dir() or not run_dir.name.startswith("R-"):
            continue
        if not (run_dir / "progress.json").is_file() or not (run_dir / "run.yaml").is_file():
            print(f"FAIL: run {run_dir.name} missing progress.json or run.yaml")
            problems += 1
            continue
        prog = json.loads((run_dir / "progress.json").read_text(encoding="utf-8"))
        for uid, st in prog.get("stages", {}).items():
            if st.get("stage") in ("reviewed", "verified", "adjudicated") and not (run_dir / "raw" / f"{uid}.json").is_file():
                print(f"FAIL: {run_dir.name}/{uid} stage={st['stage']} but no raw response")
                problems += 1
    print(f"verify: {'OK' if problems == 0 else f'{problems} problem(s)'}")
    return 1 if problems else 0


# ---------------------------------------------------------------- main

def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--repo", default=None, help="repository root (default: nearest with reviews/)")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("plan")
    p.add_argument("--track", required=True)
    p.add_argument("--format", choices=("table", "json"), default="table")
    p.add_argument("--contract-version", default=DEFAULT_CONTRACT_VERSION,
                   help="contract version to compare recorded coverage against")

    p = sub.add_parser("run")
    p.add_argument("--track", required=True)
    p.add_argument("--unit", action="append", help="specific lecture id (repeatable)")
    p.add_argument("--limit", type=int, default=None)
    p.add_argument("--model", default=DEFAULT_REVIEWER_MODEL)
    p.add_argument("--resume", default=None, help="run id to continue")
    p.add_argument("--fresh", action="store_true", help="force a new run id")
    p.add_argument("--contract-version", default=DEFAULT_CONTRACT_VERSION)
    p.add_argument("--prompt-variant", choices=("full", "wiki"), default="full",
                   help="wiki: bulk missing_wiki_link-only pre-pass (lean payload, "
                        "no full-contract coverage claim)")
    p.add_argument("--recheck-contract", action="store_true",
                  help="also include units last reviewed under an older contract version")
    p.add_argument("--one", action="store_true", help="process one unit and exit")
    p.add_argument("--dry-run", action="store_true")

    p = sub.add_parser("adjudicate")
    p.add_argument("--track", required=True)
    p.add_argument("--run", required=True)
    p.add_argument("--unit", default=None, help="lecture id (omit for decisions-file batches)")
    p.add_argument("--finding", action="append", help="finding id (repeatable)")
    p.add_argument("--decision", action="append", help="confirmed|rejected|deferred|resolved (repeatable, in --finding order)")
    p.add_argument("--note", default=None)
    p.add_argument("--interactive", action="store_true")
    p.add_argument("--as", dest="as_id", default=None, help="adjudicator identity (default: PI_SESSION_ID or 'human')")
    p.add_argument("--decisions-file", default=None, help="JSON file: {finding_id: {decision, note}}")
    p.add_argument("--model", default=None, help="adjudicator model, recorded in run.yaml (per the attribution rule)")
    p.add_argument("--model-actual", default=None, help="free-text note if the model alias understates the deployment")

    p = sub.add_parser("report")
    p.add_argument("--run", default=None)
    p.add_argument("--track", default=None, help="required when --run is not given")
    p.add_argument("--out", default=None)

    p = sub.add_parser("verify")
    p.add_argument("--track", default=None)

    args = ap.parse_args()
    if args.cmd == "plan":
        cmd_plan(args)
    elif args.cmd == "run":
        cmd_run(args)
    elif args.cmd == "adjudicate":
        if args.finding and args.decision and len(args.finding) != len(args.decision):
            sys.exit("error: --finding and --decision counts differ")
        cmd_adjudicate(args)
    elif args.cmd == "report":
        if not args.run and not args.track:
            sys.exit("error: report needs --run or --track")
        cmd_report(args)
    elif args.cmd == "verify":
        sys.exit(cmd_verify(args))


if __name__ == "__main__":
    main()
