# Lecture description audit queue and provenance

The description audit is **separate** from factual reviews in `reviews/README.md`
and metadata-coverage proposals in `docs/metadata-audit-agent.md`. A review of
math, sources, or tags does not certify a human-facing description.

This workflow uses a **heuristic ranking**, not a calibrated probability that a
description is wrong. Scripts identify candidates. A reviewer judges the
meaning against the manuscript. Keywords can be false positives and can miss
substantive errors; the score is not evidence that a candidate is defective.

## Rank the current repository

```bash
python3 tools/description_audit.py rank --csv /tmp/lecture-description-priorities.csv --top 30
```

Rows contain stable `track:lecture_id` keys, a priority score, observable
risk cues, the last description audit's date/model/depth/outcome, the last
*current* full-manuscript audit, and the manuscript and description hashes.
The queue is recomputed from the current checkout; it does not depend on
outdated exported spreadsheets. No audit history is modified by `rank`.

The score combines a **coverage baseline** with **review cues**. A current
unresolved follow-up leads; a stale review or no recorded review ranks ahead
of a current full review. Cues include section-list placeholders, generic
previews, short descriptions of long lectures, descriptions that omit
recognizable title subjects, absolute claims, and strong proof-scope verbs.
Weights are explicitly heuristic and are intended for triage, not comparison
as percentages. A high score can be a false alarm. A low score does not mean
that a description is guaranteed correct. The CLI exposes reasons so a model
can reject bad cues instead of rewriting to satisfy keywords.

## Record the work actually done

After reviewing the final manuscript and description:

```bash
python3 tools/description_audit.py record spider-man:004000 \
  --model GPT-6 --depth full_manuscript --outcome corrected \
  --note 'Compared the full narration; replaced a generic preview with its main topics.'
python3 tools/description_audit.py history spider-man:004000
```

Use the **actual** model identifier available in the session. If the exact
model variant is unknown, do not make one up. The ledger records:

- `audited_at` in UTC, actual reviewer kind and model, and scope `description`;
- `depth`: `automated` (programmatic cues only), `excerpts` (selected brief
  excerpts), `targeted_passages` (relevant passages checked in the manuscript),
  `full_manuscript` (entire spoken manuscript read), or `source_verified`
  (full manuscript *and* independent sources checked);
- `outcome`: `screened`, `clean`, `corrected`, or `needs_followup`;
- SHA-256 of the **spoken manuscript** and the exact description reviewed;
- the rationale in a short note, and an immutable event ID.

Only automated depth can use the `screened` outcome; code-only reviews cannot
claim semantic verification or a clean result. Full-text scrutiny must really
read the full spoken lecture, not just headings or a keyword report. An
external-source review must verify those sources, not merely read the lecture's
bibliography.

Records are **append-only**, in
`reviews/registry/description-audits-<track>.jsonl`. `history` shows all
records, including stale ones. A hash mismatch makes an audit stale instead
of erasing it. A later automated scan never replaces a current full audit.
The most recent unresolved `needs_followup` remains high priority until a
later current full review clears it. A corrected description should be
recorded **after** the edit is applied, so the receipt identifies the final
preview that was verified. If either narration or description changes again,
the old receipt ceases to be current.

## Historical data

Earlier broad catalog scans and targeted edits were not systematically
recorded per lecture with reproducible depth. **Do not fabricate full-text
coverage by converting those bulk statistics into thousands of clean
records.** The initial queue therefore says `never_recorded` for lectures
without a new per-lecture description receipt. This means *no dependable
receipt*, not necessarily *never looked at by anybody*.

The existing independent `reviews/registry/coverage-*.jsonl` factual-review
records are deliberately not counted as description-review clearance. The
separate registries preserve each audit's actual scope.

## Slow editorial loop

1. Generate the ranked queue. Pick a small batch from the top (some high
   scores will be false positives).
2. Read each selected lecture's full spoken text for a `full_manuscript`
   review. Compare the description with the lecture's primary subject,
   coverage balance, important distinctions, named entities, proof scope, and
   omissions. Do not treat keyword presence as truth.
3. Change only the descriptions with demonstrable problems. Leave accurate
   descriptions untouched; `clean` is a useful result.
4. Record the audit outcome for the **final revision**, preserving the model
   and depth, then re-run `rank` to receive the next batch.
5. Periodically audit a few lower-ranked lectures too, to identify error
   patterns that the scoring heuristics miss. Revise the cues when actual
   corrected/clean outcomes support doing so.
6. Keep the ledger and reports outside content packs; audits should not block
   importing, playing, or authoring lectures.
