# Review categories (contract v2)

The reviewer may flag exactly five categories. Every finding needs a
**verbatim anchor**: a contiguous substring of the spoken narration, at most
50 words, long enough to locate the issue uniquely. If the problem cannot be
pointed at with a verbatim quote, it is not a finding.

## `unverified_claim`

A factual, dated, historical, or bibliographic assertion for which the
lecture's registered sources do not adequately cover it.

Input the reviewer is given: the narration, the sidecar (`related_resources`,
`historical_claims` with their `audit_status` and `source_limitations`), the
resolved source records, and the track's full source registry.

- Flag when the assertion is the kind of thing that needs a source (a date,
  an attribution, an archaeological or documentary fact, a named work or
  edition) and no registered source plausibly supports it, **or** the
  registered source's stated scope does not reach the claim (e.g. the
  sidecar says "abstract reviewed" but the claim needs the full study).
- In `source_ids`, list the closest registered sources you considered, even
  if none suffices; empty list if none.
- Do not flag common-knowledge framings the lecture itself hedges, and do
  not flag that a source is *insufficient in depth* when it is adequate in
  scope.

## `glossed_step`

A passage that asserts a result, conclusion, or mechanism a listener cannot
follow from what the lecture has said so far, with no pointer to where the
missing material would come from.

- For mathematics and formal argument the reviewer may flag a non-obvious
  step at **low confidence** and say which step is non-derivable. It must
  **not** assert that the step is wrong. Correctness is the adjudicator's
  job, with the actual sources in hand.
- A deliberate deferral ("we will return to this") is not a gloss; check
  whether the lecture actually returns.

## `unintroduced_term`

A technical term, named object, or named person used as if established,
before the lecture establishes it (definition, role, or origin) and with no
registered source that a listener could be expected to have in hand.

- Recurring proper nouns in a world-history lecture that are central to the
  narrative (rulers, sites, texts) need a one-line establishing context at
  first use; a passing reference does not.
- Do not flag ordinary vocabulary, and do not flag a term the lecture
  intentionally leaves as a hook with a stated promise to explain it.

## `internal_conflict`

A statement in the narration that contradicts another passage of the same
lecture, or a track-level statement in `track.json`
(`summary`, `editorial_policy`, section framing) that the narration violates.

- Chronology mismatches, differing numbers for the same thing, and
  attributed-versus-reported confusion (saying what a source *says* versus
  what the evidence *shows*) are the typical forms.
- Apparent tension that the lecture itself reconciles in a later passage is
  not a conflict.

## `missing_wiki_link`

The lecture's non-spoken further-reading material offers no Wikipedia entry
point for a **central subject** of the lecture (the main person, place, text,
or event it is about), and that subject is notable enough that a substantial
Wikipedia article exists.

- This is an advisory completeness check, not a defect: lectures in this
  library are expected to give listeners a Wikipedia link as a general
  further-reading entry point in addition to any scholarly or primary
  sources. A scholarly source on the same subject does not by itself
  substitute for that entry-point role; the adjudicator may still reject on
  those grounds if the existing source genuinely serves both roles.
- Flag only central subjects, and only ones you are confident have a
  substantial article. A passing reference to a minor name is not central.
- At most three findings of this kind per lecture, most central first.
- The anchor must still come from the **narration**: quote the passage that
  names or establishes the subject (e.g. the sentence introducing the person
  or text). In `detail`, name the specific article (e.g. “Epic of Gilgamesh”)
  and note which further-reading items already exist for that subject.
- If the further-reading section (or a registered source) already contains a
  Wikipedia link for that subject, do not flag it.
- The **bulk wiki pre-pass** (contract variant `v2w`, prompt
  `prompt-v2w.md`) checks only this category with a lean payload and records
  an extra structured field `wiki_articles` — the exact English-Wikipedia
  article title(s) the finder proposes, for mechanical existence checking by
  `tools/verify_wiki_candidates.py` on a machine with network access.

## Never flag

- Style, phrasing, word choice, sentence length, repetition, and pacing.
- Pronunciation and TTS concerns.
- Notation or naming conventions, including anything governed by
  `LECTURE_STYLE_RULES.md` or a notation glossary.
- Pedagogical order or emphasis choices, including the track's
  `editorial_policy` itself (the policy is context, not a finding target;
  only *narration that violates it* is flaggable, as `internal_conflict`).
- Mathematical or historical **correctness** verdicts. The reviewer reports
  what is under-supported or under-explained; whether it is wrong is decided
  by adjudication against the primary sources.
- Coverage of topics the lecture does not claim to cover.

## Output discipline

- At most **12 findings** per lecture, most severe first.
- Zero findings is a correct and common answer; a clean lecture returns an
  empty array. Padding the count is a defect.
- Output is a JSON array only — no prose, no commentary, no markdown fences.
