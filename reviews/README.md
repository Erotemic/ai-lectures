# Lecture review layer

Reviews are a durable, **pack-disjoint** quality layer for lecture content. A
review is not a document produced about a pack; it is a set of *findings* —
stable, identity-bearing records — observed against specific content
revisions by a bounded reviewer, and adjudicated by a more capable agent
session.

This directory is infrastructure, in the same sense as the LLM resource
tally: it is read by review sessions, written only by review work, and never
by content agents.

## Disjointness invariants

1. **Reads packs, writes only here.** Review tooling reads manuscripts,
   `metadata/*.json` sidecars, `metadata/sources.json`, and `track.json`; it
   writes only under `reviews/`. A pack is never modified, gated, or blocked
   by review state: *diagnostics are separated from delivery*. An unreviewed
   or flagged lecture remains fully servable.
2. **Pack handoffs never carry review data.** Pack scopes are
   `content/<ns>/` and `draft-stages/<track>/`; `reviews/` lies outside every
   scope, so overlays and ZIPs cannot import or export findings.
3. **Verbatim anchors.** Every finding must quote the target text verbatim.
   The runner verifies the anchor against the extracted narration before a
   finding enters the registry; unlocatable findings are dropped and
   recorded, not guessed at.
4. **Finder is not the adjudicator.** A 27b-class reviewer is invoked in
   single-shot, no-tools calls. Only an agentic session with repo and source
   access may move a finding out of `open`. A finding cannot be `confirmed`,
   `rejected`, or `resolved` without an adjudication record.
5. **Revision binding.** Units are keyed by a content hash covering the
   manuscript, its sidecar, the track source registry, and `track.json`.
   Staleness is computed, not remembered.

## Layout

```
reviews/
  README.md               # this contract
  contract/
    categories.md         # what may be flagged, and explicitly may not
    prompt-vN.md          # versioned reviewer prompt (version recorded in runs;
                          # v1 frozen; current: v2 — adds missing_wiki_link and the
                          # further-reading input)
  registry/
    findings-<track>.jsonl   # one row per finding identity (durable)
    coverage-<track>.jsonl   # one row per (track, lecture, revision) reviewed
  runs/
    R-<YYYYMMDD>-<track>/
      run.yaml            # scope, contract version, reviewer/adjudicator model + session
      progress.json       # per-unit stages; the compaction-survival checkpoint
      raw/<unit>.json     # raw reviewer responses (pre-validation audit trail)
      report.md           # human-readable summary for the run
```

Track = any directory under `content/` or `draft-stages/` carrying a
`track.json`. Registry and coverage files are sharded per track; review work
on one track never touches another track's files.

## Finding record

```json
{
  "finding_id": "tts-world-history/001000#unverified_claim#a1b2c3d4",
  "track": "tts-world-history",
  "lecture_id": "001000",
  "category": "unverified_claim",
  "anchor": "verbatim contiguous quote from the narration",
  "anchor_as_quoted": "what the reviewer actually sent (if normalization changed it)",
  "claim": "one sentence: what the lecture asserts",
  "detail": "one sentence: why that is a problem in this category",
  "confidence": "high|low",
  "source_ids": ["ids of the closest registered sources, if any"],
  "status": "open|confirmed|rejected|deferred|resolved|stale",
  "first_seen":  {"run": "R-…", "revision": "…", "at": "…"},
  "last_seen":   {"run": "R-…", "revision": "…", "at": "…"},
  "adjudication": {"by": "session:<id>|human", "decision": "…", "note": "…", "at": "…"},
  "resolution":   {"revision": "…", "note": "…", "at": "…"},
  "history": [{"status": "…", "run": "…", "at": "…"}]
}
```

Identity = `(track, lecture_id, category, sha256(normalized_anchor)[:12])`.

State machine:

- `open` → `confirmed` / `rejected` / `deferred` — only via an adjudication.
- `confirmed` / `deferred` → `resolved` — when the fix lands; record the
  content hash of the fixed revision.
- Any status → `stale` — when a later review of the unit shows the anchor no
  longer occurs (the text was reworded or removed).
- `resolved` or `rejected` → `open` (**regression re-open**) — when a later
  review of a *different* revision flags the same identity again. The
  transition is appended to `history`; the prior status is never lost.
- `rejected` re-flagged at a newer revision keeps `rejected` but updates
  `last_seen`: the reviewer's persistence is visible to the adjudicator.

## Coverage record

```json
{"track": "…", "lecture_id": "…", "revision": "…", "run": "R-…",
 "reviewed_at": "…", "contract": "v2",
 "outcome": "clean|findings:N", "adjudicated_at": "…", "open": 0}
```

One row per (track, lecture) pair, replaced as newer revisions are reviewed.
`outcome: clean` is a first-class result: a reviewed-and-clean lecture is not
re-reviewed until its revision changes. `plan` consults coverage: a unit
needs work iff its revision changed since its coverage row, it carries open
findings, or it has never been reviewed. A unit reviewed under an older
*contract* version is reported for `--recheck-contract` but is not
re-billed by default: contract changes add capability (e.g. v2's
`missing_wiki_link`) rather than invalidate prior verdicts.

## Resume protocol (compaction-safe one-lecture-at-a-time work)

The unit stage in `progress.json` is `queued → reviewed → verified →
adjudicated`:

- **Persist before the next read.** After each stage transition the runner
  writes the raw response, registry rows, coverage row, and progress update,
  and the session commits in small batches before loading the next lecture.
  The expensive reviewer call is never re-bought by a later session.
- **Post-compaction ritual:** read the run's `progress.json` (one small
  file). `in_progress.stage == reviewed` → go straight to verification /
  adjudication with the raw response on disk. `adjudicating` → per-finding
  statuses in the registry are the fine-grained checkpoint; adjudicate only
  the still-`open` findings. The unit stage is *derived* from finding
  statuses, so there is one source of truth.

## Bulk wiki pre-pass

`missing_wiki_link` findings are advisory and batch-friendly, so the track can
be swept for them with a dedicated cheap pass that runs **detached** (hours,
survives compaction and session death):

```
nohup python3 tools/run_reviews.py run --track tts-world-history \
    --prompt-variant wiki --fresh > reviews/bulk-logs/wiki-v2w-$(date +%s).log 2>&1 &
```

The `wiki` variant (contract `v2w`, prompt `prompt-v2w.md`) checks only that
category with a lean payload (narration + companion + sidecar, no source
registry). Differences from a full run:

- **Order rule:** a unit is billed only if it has no live/rejected
  `missing_wiki_link` finding and no `wiki:clean` coverage row at the current
  revision — already-cleared units are never re-billed.
- **Coverage:** rows record `contract: v2w` and `outcome: wiki:0|1|2|3`.
  A v2w row does *not* count as a full-contract review: `plan` reports such
  units as `contract_kind` when a full contract is requested, and a full run
  still bills them normally.
- **Structured field:** findings carry `wiki_articles` (proposed exact
  article titles) so existence can be checked without a capable model.

After the pass completes (and after the fix for `001000` if done separately),
the pipeline is:

1. **Verify (needs network — user side):** `python3 tools/verify_wiki_candidates.py --track …`
   → `reviews/registry/wiki-verified-<track>.jsonl` (per title: exists /
   canonical / redirected).
2. **Adjudicate (this tier, batch):** read the findings plus the verification
   table, decide in batches, apply with
   `adjudicate --track … --run … --decisions-file decisions.json` (JSON:
   `{finding_id: {decision, note}}`; `--unit` omitted for cross-lecture
   batches). Titles that do not exist are rejected or re-proposed; existing
   titles are confirmed or rejected on relevance (is the subject truly
   central?). A handful of borderline cases are escalated to the user rather
   than guessed.
3. **Fix (content pass):** add the confirmed links to the companion further-
   reading sections (verify URLs in an environment with network), then
   `adjudicate … --decision resolved` per finding; the revision bump plus
   stale sweep closes the loop.

Console logs under `reviews/bulk-logs/` are gitignored; the run directory,
registry, and coverage stay committed. Per-unit failures (proxy outage, bad
output) are recorded in `progress.json` and re-billed by `--resume`.

## One-at-a-time audit mode (full v2, deliberate pace)

The deliberate audit of a track goes one lecture per pass, in **track
order** (the lecture list in `track.json`, by ID). A session — fresh or
post-compaction — reconstructs its position from the ledgers alone:

1. Read `reviews/registry/coverage-<track>.jsonl` and
   `reviews/registry/findings-<track>.jsonl`.
2. A unit is **audit-complete** iff its coverage row has contract `v2`
   (full, not a `v2w` bulk row) at the unit's current revision *and* it has
   no open/confirmed/deferred findings. (A `v2w` row or a stale revision
   means the unit still needs a full pass.)
3. The **next unit** is the first lecture ID in track order that is not
   audit-complete. Process it:

```
python3 tools/run_reviews.py run    --track <t> --unit <ID> --one --fresh
python3 tools/run_reviews.py adjudicate --track <t> --run <newest run> \
        --decisions-file <decisions.json>   # or --interactive per finding
python3 tools/run_reviews.py verify
```

4. Adjudicate every finding of the unit (including any pre-seeded by an
   earlier bulk pass) before moving on: the unit is only audit-complete
   when its findings are all terminal (rejected / resolved) or deliberately
   deferred with a reason in the adjudication note.
5. **Commit after each unit** (or a small batch of units) with the
   attribution trailer, then proceed. The commit is the checkpoint: after
   any compaction, step 2 gives the next unit; raw responses, findings,
   coverage, and run state are all on disk.

## Attribution

`run.yaml` records, for the reviewer and the adjudicator separately: the
model exactly as the runtime identifies it, the session id (tally-attributable),
and `model_actual` free text for deployments whose alias understates the
weights behind them. Review commits carry the `Co-authored-by:` trailer
required by AGENTS.md. Reviewer and adjudicator usage both land in the LLM
resource tally under their session ids.

## Commands

```
python3 tools/run_reviews.py plan     --track tts-world-history [--format table|json]
python3 tools/run_reviews.py run      --track … [--unit ID …] [--limit N]
                                      [--model M] [--resume RUN | --fresh]
                                      [--contract-version vN] [--recheck-contract]
                                      [--prompt-variant full|wiki] [--dry-run]
python3 tools/run_reviews.py adjudicate --run R --unit ID
                                      [--finding FID --decision … --note …]
                                      [--interactive] [--as …]
python3 tools/run_reviews.py report   [--run R] [--out PATH]
python3 tools/run_reviews.py verify   [--track …]
```

The tool never commits and never writes outside `reviews/`; commit batching
and the attribution trailer are the session's job.
