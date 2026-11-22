# Prioritizing and recording lecture metadata audits

The metadata-audit ledger is separate from the repository's factual review records. An audit receipt describes **which metadata fields were evaluated**, **how much of the manuscript was read**, **by which reviewer/model**, and **when**. A full-manuscript *metadata* audit is not a verification of historical claims, mathematical proofs, citations, or outside sources.

## Rank the next lectures

```bash
python3 tools/description_audit.py rank --scope description --top 30 \
  --csv /tmp/lecture-description-priorities.csv
python3 tools/description_audit.py rank --scope geography --top 30 \
  --csv /tmp/lecture-geography-priorities.csv
python3 tools/description_audit.py rank --scope tags --top 30
```

`--scope` accepts `description`, `title`, `tags`, `tag_paths`, `chronology`, `geography`, `learning`, `related_resources`, or `claim_evidence`. The description queue uses heuristic risk cues: heading lists, missing identifying subjects, strong proof verbs, unusually brief or generic summaries, and prior follow-ups. Other scopes mainly rank by whether a current review exists; there are a few conservative cues for empty biography geography/chronology, absent tag paths, and generic source rationales. The score is a **priority score, not a calibrated probability of an error**. A high score can be a false alarm, and a low score can miss a serious issue.

Each CSV row gives the exact `audit_scope`, revision-aware review state, last audit date/model/depth/result for *that scope*, last current full-manuscript audit, and manuscript/description fingerprints. The ranking command does not create audit records.

## Scope and depth are different

`depth` is **how** the manuscript was inspected:

- `automated`: programmatic flags and completeness checks only; cannot mark a field clean.
- `excerpts`: selected introductory or other brief excerpts checked.
- `targeted_passages`: relevant passages inspected without reading the full narration.
- `full_manuscript`: the entire spoken manuscript read and the **listed metadata scopes** assessed against it.
- `source_verified`: full manuscript and independent external sources examined for the stated metadata scopes. Do not use this unless source verification actually happened.

`scope` is **what** was evaluated:

| Scope | Metadata compared against narration |
|---|---|
| `description` | Accuracy, relative emphasis, clarity, distinctive subject matter, proof-scope language |
| `title` | Title from `track.json` identifies the lecture covered |
| `tags` | Top-level `tags` reflect primary subject matter |
| `tag_paths` | Hierarchical taxonomy paths fit the subject |
| `chronology` | `chronology`, `periods`, `spacetime_coverage` agree with stated events and ranges |
| `geography` | `places`, `geography` agree with the places the manuscript actually treats |
| `learning` | Recorded prerequisites, level, or readiness checks fit the lecture |
| `related_resources` | Resource metadata is appropriately associated with topics, **not** automatically source-verified |
| `claim_evidence` | Claim/evidence metadata corresponds to text, **not** independently fact-checked |

For example, reviewing `description`, `title`, and `tags` does *not* clear `geography` or `claim_evidence`. Checking a biography's chronology against its narration does not establish that the dates in the narration are historically correct. Record `source_verified` only when external sources were separately checked.

## Record exact scope, result, and model

```bash
python3 tools/description_audit.py record history:012000 \
  --model GPT-6 --depth full_manuscript --outcome corrected \
  --scope description --scope title --scope tags --scope geography \
  --scope-outcome description=corrected \
  --scope-outcome title=clean \
  --scope-outcome tags=corrected \
  --scope-outcome geography=corrected \
  --note 'Read entire narration and revised the preview/tags/places; sources not checked.'
python3 tools/description_audit.py history history:012000
```

With multiple scopes, a separate `--scope-outcome` is mandatory for *each*, so a correction to one field cannot be misread as a correction or clean verdict for every field. The event stores an aggregate outcome only for convenience. Use the actual reviewer/model identity; never infer a variant. For a one-scope audit, `--outcome clean` is sufficient.

Each event is append-only in `reviews/registry/description-audits-<track>.jsonl`. Schema-2 events carry `scope`, `scope_outcomes`, a fingerprint for each audited scope, `verification_basis`, model, date, depth, and an explanatory note. Spoken-manuscript changes stale all manuscript-alignment results. A metadata edit only stales the scopes whose *fingerprinted metadata* changed: changing tags does not invalidate a still-correct description review. An automated later screen cannot erase a current full-manuscript review. Old schema-1 records remain valid for `description` only; they are not silently promoted to broader metadata verification.

## Review loop

1. Choose a manageable batch near the top of the *description* queue. Periodically sample low-risk entries to check whether the ranking misses systematic errors.
2. Read the complete spoken text for `full_manuscript`, and inspect the exact metadata fields named in `scope`.
3. Correct only supported problems. Distinguish accurate descriptions from unhelpfully generic ones; do not turn a passing phrase into a main subject or inflate a proof sketch into a formal proof.
4. Record the **final** metadata fingerprints after applying any edits. Record clean fields as clean, corrected fields as corrected, and unresolved issues as `needs_followup`.
5. Generate a fresh ranking. Never convert historical bulk audits into fictitious full-manuscript receipts.

The initial eleven-lecture scoped batch covered descriptions, title alignment, and relevant taxonomy fields, with a chronology/geography check for Ky Fan. It did **not** review learning prerequisites, source support, external historical facts, or formal proof correctness. Earlier description-only full-manuscript records remain description-only. These audits should not block importing or playing lectures.

## Audit progress (22 November 2026, batch 5)

The cumulative scoped audit overlay includes **68 current full-manuscript description reviews**, with 14 additional reviews in this batch. Their scope and per-field outcome are recorded independently. Unreviewed lectures are not upgraded by an automated screening or by previous batch-level editorial changes; rerun `rank` for the current queue.
