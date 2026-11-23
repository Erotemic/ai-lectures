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

## Audit progress (22 November 2026, batch 23)

**305 current distinct full-manuscript description reviews out of 2,392 lectures (12.8%)** are recorded. Batch 23 adds 37 complete spoken-manuscript reviews, substantially more than the previous 14- or 15-lecture batches: four *Dragon Ball* lectures, six fiction-writing lectures, six Davis–Kahan mathematics lectures, four scientific biographies, four biology/ecology lectures, five dependent-type-theory lectures, and eight modern-literature studies. Each new receipt separately records the result for description, title, topical tags and hierarchical tag paths. Geography and, where directly supported, publication chronology were reviewed in additional scopes.

**Fourteen descriptions were revised; twenty-three remained accurate without rewriting.** The six Davis–Kahan previews now distinguish the precise result and hypotheses of each manuscript: defect dimensions and direct-rotation existence; ordered half-line Sylvester estimates and semigroup integrals; domain-compatible unbounded cutoffs; off-diagonal branch selection below 45 degrees; symmetric two-gap sine estimates and Hilbert–Schmidt limitations; and the ordered-gap doubled-tangent bound and its pole. These statements describe *what the narration develops*, not independently validated mathematical proofs. The Rayleigh, Weyl, Riesz and Gauss biographies also gained important mathematical content that their previous previews omitted. The dependent-types lecture on quantified witnesses now differentiates Lean's propositional `Exists` from computational sigma types. The *Dragon Ball* dubbing preview adds Brazilian Portuguese to the already discussed Japanese, English and Latin American Spanish traditions.

The two modern-literature preview corrections are likewise substantive: *Wide Sargasso Sea* is not narrated solely from Antoinette's perspective, and *The Master and Margarita* reimagines Pilate and Yeshua rather than reporting the canonical Gospel narrative. The other fiction-writing, biology, logic and literary descriptions were preserved when the full text confirmed their accuracy. Reviewers did not manufacture changes merely because a description was short or ranked highly.

**All 37 sidecars gained topical tags and hierarchical paths.** The added subjects are selective and grounded in sustained manuscript content, rather than indiscriminate names from passing examples. Highlights include autofiction and Oulipo, the Achebe–Ngũgĩ language debate, Gardner's profluence, slipstream and New Weird, Lenski's evolutionary contingency, river-continuum and flood-pulse ecology, phytoplankton carbon export, indexed inductive families, and the social and formal mechanisms discussed in individual novels.

**Nine place fields were corrected or expanded.** Real-world dubbing/localization geography is distinguished from fictional *Dragon Ball* settings. The biographies add substantive Cambridge, London, Princeton, Zürich and Budapest coverage, while Gauss's duplicate Göttingen listing is normalized. Literary settings are more specific where named and relevant: Jamaica, Dominica and England in *Wide Sargasso Sea*; Dresden in *Slaughterhouse-Five*; Rome and Avignon in *Catch-22*; and Moscow alongside Jerusalem in *The Master and Margarita*. Other novels' speculative locations were not treated as historical place coverage. Five publication-chronology fields were independently assessed against their own narrated dates and found consistent; no invented single-year settings were assigned to works with uncertain or fictional calendars.

These are **manuscript-to-metadata alignment reviews**, not independent historical fact checks, clinical or empirical validation, source verification, or confirmation of mathematical arguments. All 37 records were created at `full_manuscript` depth with field-specific outcomes and final-revision fingerprints. Batch 23 is based on the 22 November source snapshot with batches 17–22 already applied, and changes only the 37 listed metadata sidecars, append-only audit ledgers, and this progress document; it does not change lecture manuscripts.
