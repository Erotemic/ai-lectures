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

`--scope` accepts `description`, `title`, `tags`, `tag_paths`, `chronology`, `geography`, `learning`, `related_resources`, or `claim_evidence`. The description queue uses heuristic risk cues: heading lists, missing identifying subjects, strong proof verbs, unusually brief or generic summaries, and prior follow-ups. After eight high-scoring animal-physiology descriptions passed full-manuscript review in batch 11, a missing title word was made a *weak* cue for general titles: metaphorical titles and morphological variants had generated false positives. Named biographical subjects still receive a stronger title-anchor cue. This is a triage adjustment, not a calibrated prediction model. Other scopes mainly rank by whether a current review exists; there are a few conservative cues for empty biography geography/chronology, absent tag paths, and generic source rationales. The score is a **priority score, not a calibrated probability of an error**. A high score can be a false alarm, and a low score can miss a serious issue.

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

## Audit progress (22 November 2026, batch 22)

**268 current distinct full-manuscript description reviews out of 2,392 lectures (11.2%)** are recorded. Batch 22 adds fourteen scope-specific reviews: twelve comedy-history manuscripts spanning humor psychology, sociology, improv and revue, persona, physical theater, translation, surrealism, existential philosophy and anti-comedy; plus two consolidated mathematics lectures covering discrete combinatorics and finite spectral theory. All fourteen titles match their full manuscript headings; their current review receipts track description, title and taxonomy scopes, with grounded geography reviewed where relevant.

Six descriptions needed correction. The Harold preview now separates Close/Halpern's flexible long-form structure from UCB-style *game of the scene* analysis; the audiovisual-translation preview includes live interpreting and visual/linguistic timing; the surreal-comedy preview accounts for Jarry and Breton, as well as Dada and later television; and the anti-comedy preview explains reality-based framing and consent rather than only delay and refusal. The two long mathematics previews now identify the distinct proof subjects actually treated: local decoding and list decoding, small-bias generators, Boolean thresholds and tribes, Reed–Muller testing, and additive Fourier counting; and finite self-adjoint spectral decomposition, Rayleigh stationary points, Courant–Fischer, and Rayleigh–Ritz. These description changes do not certify the proofs or historical sources independently.

All twelve comedy-history sidecars gain subject tags and more specific hierarchical paths, in addition to mathematical paths on the two consolidated lectures. Five geography fields now index locations explicitly discussed in the manuscripts: the comparative North American and East Asian humor studies, Dutch and British taste research, Chicago's Second City, Chicago/San Francisco improvisation lineages, and the Paris/Zürich avant-garde settings. No setting was inferred from a fictional workshop scene, and no single misleading date range was assigned to mixed-era cultural surveys. Descriptions found accurate were kept rather than rewritten for variety.

These are **full-spoken-manuscript metadata-alignment** records, not source-verified historical or scientific fact checks, validation of empirical effects, or independent mathematical proof verification. Each audited field has a revision-sensitive receipt. Batch 22 builds on the 22 November source snapshot with batches 17–21 applied in order; the overlay changes only the listed sidecars, append-only audit ledgers, and this progress document.
