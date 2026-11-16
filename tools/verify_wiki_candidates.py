#!/usr/bin/env python3
"""Verify Wikipedia article existence for missing_wiki_link findings.

Intended to be run on a machine WITH network access (the agent sandbox is
offline). For each open/confirmed finding of category missing_wiki_link that
carries the structured `wiki_articles` field (produced by the v2w bulk
pass), each proposed title is checked against the English Wikipedia API and
the result is written to

    reviews/registry/wiki-verified-<track>.jsonl

(one row per finding x title, replaced as re-checked). Batch adjudication
then uses this table: titles that do not exist are rejected or re-proposed;
titles that exist are confirmed or rejected on relevance grounds.

Usage:
  python3 tools/verify_wiki_candidates.py --track tts-world-history \
      [--statuses open,confirmed] [--throttle 0.25]
"""
import argparse
import json
import time
import urllib.parse
import urllib.request
from pathlib import Path

import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
import run_reviews as rr

API = "https://en.wikipedia.org/w/api.php"


def check_title(title: str) -> dict:
    url = API + "?" + urllib.parse.urlencode(
        {"action": "query", "format": "json", "titles": title, "redirects": 1})
    with urllib.request.urlopen(url, timeout=20) as r:
        data = json.load(r)
    for p in (data.get("query", {}).get("pages") or {}).values():
        if "missing" in p:
            return {"title": title, "exists": False, "canonical": None}
        return {"title": title, "exists": True, "canonical": p.get("title"),
                "redirected": p.get("title") != title}
    return {"title": title, "exists": False, "canonical": None}


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--track", required=True)
    p.add_argument("--statuses", default="open,confirmed",
                   help="comma list of finding statuses to verify "
                        "(default: open,confirmed)")
    p.add_argument("--throttle", type=float, default=0.25,
                   help="seconds between API calls (default 0.25)")
    args = p.parse_args()

    root = rr.find_repo_root(Path.cwd())
    store = rr.Store(root)
    statuses = set(s.strip() for s in args.statuses.split(",") if s.strip())
    rows = [r for r in store.load_findings(args.track)
            if r.get("category") == "missing_wiki_link" and r.get("status") in statuses]
    if not rows:
        print(f"no missing_wiki_link findings with status in {sorted(statuses)} "
              f"for {args.track}")
        return

    out = store.root / "reviews" / "registry" / f"wiki-verified-{args.track}.jsonl"
    prev = {}
    if out.is_file():
        for line in out.read_text(encoding="utf-8").splitlines():
            if line.strip():
                j = json.loads(line)
                prev[(j["finding_id"], j["title"])] = j

    n_exist = n_missing = n_err = n_nofield = 0
    for r in rows:
        titles = r.get("wiki_articles")
        if not titles:
            n_nofield += 1
            print(f"!! {r['finding_id']}: no wiki_articles field "
                  f"(pre-v2w finding; re-run the unit under v2w to populate it)")
            continue
        for t in titles:
            time.sleep(args.throttle)
            try:
                res = check_title(t)
            except Exception as e:  # network hiccup: record, do not crash
                res = {"title": t, "exists": None, "canonical": None,
                       "error": f"{type(e).__name__}: {str(e)[:120]}"}
            row = {"finding_id": r["finding_id"], "lecture_id": r["lecture_id"],
                   "status": r["status"], **res, "checked_at": rr.now_iso()}
            prev[(r["finding_id"], t)] = row
            tag = "OK  " if res.get("exists") else \
                  ("MISS" if res.get("exists") is False else "?   ")
            extra = f" (redirected to {res['canonical']})" if res.get("redirected") else ""
            err = f"  [{res['error']}]" if res.get("error") else ""
            print(f"{tag} {r['lecture_id']}  {t!r} -> {res.get('canonical')}{extra}{err}")
            if res.get("exists") is True:
                n_exist += 1
            elif res.get("exists") is False:
                n_missing += 1
            else:
                n_err += 1

    keys = sorted(prev)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("".join(json.dumps(prev[k], ensure_ascii=False) + "\n" for k in keys),
                   encoding="utf-8")
    print(f"\n{len(keys)} title rows at {out.relative_to(root)} "
          f"(exist: {n_exist}, missing: {n_missing}, errors: {n_err}, "
          f"without wiki_articles: {n_nofield})")


if __name__ == "__main__":
    main()
