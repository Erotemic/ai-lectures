# Review report

- run: `R-20261116-tts-world-history` (track `tts-world-history`, contract `prompt-v1`)
- reviewer: `qwen3.8-27b-dbirks-hyperqwen-long` (session `01a1e543-5cac-70bc-820f-5ac6878acec9`)
- adjudicator: `qwen3.8-27b-dbirks-hyperqwen-long` (session `01a1e543-5cac-75f1-b17f-a5c981f73129`)

## Findings (5 total)

### confirmed (3)

- **001000** `unverified_claim` (conf=low)
  - claim: The lecture asserts that the transfer of Nineveh tablets to Europe occurred within imperial archaeology and raises modern ownership and heritage questions.
  - detail: The registered sources cover the flood tablet and rediscovery but not the stated scope of modern provenance, repatriation, or imperial archaeology, so a source on the provenance and heritage status of the tablets would be needed.
  - anchor: “Their removal took place in the context of imperial archaeology, and the modern location of ancient objects raises questions about ownership, access, and cultural heritage.”
  - adjudication: {"by": "01a1e543-5cac-75f1-b17f-a5c981f73129", "decision": "confirmed", "note": "Genuine scope gap: the registered gilgamesh-flood record (museum_collection, notes: 'recovered tablet and its place in the modern rediscovery') does not reach the imperial-archaeology / ownership / cultural-heritage interpretive layer the lecture asserts. Fix: register a provenance or heritage-history source for the Nineveh/Rassam acquisitions, or soften the sentence to what the collection page actually states. Low severity; non-blocking.", "at": "2026-11-16T18:29:00Z"}
- **001000** `unverified_claim` (conf=low)
  - claim: The lecture asserts that some of the earliest Mesopotamian writing arose for administrative accounting purposes.
  - detail: The registered sources are about the Gilgamesh epic and its manuscript tradition rather than the origins of writing, so a source on early cuneiform administrative tablets would be needed.
  - anchor: “Some of the earliest writing in Mesopotamia developed in precisely this environment, first serving administrative purposes such as accounting.”
  - adjudication: {"by": "01a1e543-5cac-75f1-b17f-a5c981f73129", "decision": "confirmed", "note": "Genuine scope gap: the claim concerns the administrative origins of writing, but this lecture's registered sources are all about the Gilgamesh epic. The track registry already holds a fitting source (uruk-met-writing: Spar, 'The Origins of Writing', Met). Fix: add that (or an equivalent) to this lecture's sidecar, or move the claim to a companion note with attribution. Low severity; non-blocking.", "at": "2026-11-16T18:29:00Z"}
- **001000** `unverified_claim` (conf=low)
  - claim: The lecture asserts that the Atrahasis flood tradition gives reasons for the flood that differ from Genesis.
  - detail: The registered Gilgamesh sources do not state that they cover the Atrahasis text or a comparative study of its flood motives against Genesis, so a source on Atrahasis and Genesis comparison would be needed.
  - anchor: “Within the wider Mesopotamian flood tradition, including the story of Atrahasis, the reasons for destroying humanity are expressed differently from Genesis.”
  - adjudication: {"by": "01a1e543-5cac-75f1-b17f-a5c981f73129", "decision": "confirmed", "note": "Genuine scope gap: the lecture names Atrahasis and makes a comparative claim about its flood motives, but no Atrahasis source is registered for this lecture. The track registry holds the standard edition (lit-atrahasis-epic: Lambert & Millard, Atra-Hasis: The Babylonian Story of the Flood) and free translations. Fix: register one of them in this lecture's sidecar. Low severity; non-blocking.", "at": "2026-11-16T18:29:00Z"}

### rejected (2) — closed

- 001000 `unverified_claim`: The lecture asserts that written Mesopotamian flood narratives predate the final form of Genesis and that thei
- 001000 `unverified_claim`: The lecture asserts that tall cedar trees grew in mountainous regions north and west of southern Mesopotamia.

## Unit progress

| unit | stage | findings | active | at |
|---|---|---|---|---|
| 001000 | verified | - | - | 2026-11-16T18:29:00Z |
