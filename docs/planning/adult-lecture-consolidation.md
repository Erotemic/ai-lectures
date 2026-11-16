# Adult lecture ordering and consolidation

16 November 2026. Editorial work by GPT-6 (exact variant unavailable).

The earlier organization review checked broad progression and main/deep routes,
but left too many short adult manuscripts presented as separate lectures. The
user clarified that related fragments should become **one combined manuscript**,
with no requirement to preserve the old playback entries. This pass implements
that decision, rather than merely placing the parts under session headings.

The comparison uses the committed source state through Journey to the West
chapter 21 (`ea704b0`). Authors added material during the audit, so its baseline
is slightly larger than the first progress report. Time is estimated from
canonical narration at 145 words per minute; it is not measured recording time.

| Measurement | Before | After |
| --- | ---: | ---: |
| Adult audio manuscripts, all 47 adult packs | 2,454 | 1,127 |
| Adult entries under ten minutes | 1,553 | 3 |
| Adult entries under five minutes | 315 | 0 |
| Exempt children's stories | 213 | 213 |

Across the 32 affected packs, 1,637 source parts became 310 combined lecture
manuscripts. Another 266 already suitable manuscripts in those packs remain
individual entries: the affected inventory is now 576 rather than 1,903.
The other adult packs already contain developed lectures and were left intact.
The [machine-readable inventory](adult-lecture-consolidation-2026-11-16.json)
lists every affected pack, combined manuscript, original component ID, measured
length, and short-format exception.

| Examples | Before | After |
| --- | ---: | ---: |
| Mathematical proof | 18 | 3 |
| Linear algebra | 15 | 3 |
| Multivariable calculus | 18 | 3 |
| Pre-1900 literature | 501 | 64 |
| Modern literature | 218 | 105 |
| Ancient and medieval world | 180 | 42 |

## What was combined

These are complete source files with one spoken-region marker pair, not playback
playlists or shortened substitutes. Original arguments, story events, exact
mathematical companions, exercises, qualifications, readings and claim records
remain with their combined lecture. Joins were reviewed to connect the argument,
scope repeated openings, and repair references to recordings that no longer
exist. Removed component files and sidecars are not unindexed library entries or
runtime aliases. Git and the composition records retain their history.

The material determines the stopping point. For example, the proof course is
approximately 45, 38 and 17 minutes; the shorter analytic-proof bridge ends at a
real boundary. Linear algebra is approximately 34, 39 and 28 minutes. We did not
pad these units to forty minutes. One connected operator-geometry lecture,
`g2:033000`, remains about 62 minutes: positivity, moduli, singular values and
polar factors form a coherent argument. This is the explicit longer exception.

Children's source files, ages, episodes and orders are byte-for-byte unchanged.

## Ordering decisions

- **Analysis and topology:** operator-algebra foundations now precede the spectral
  calculus that uses them. Weak/weak-star and measure-representation material
  accompanies functional analysis. PDE estimates precede nonlinear evolution;
  chain-complex calculations precede their topological applications; symplectic
  and analytic foundations precede reduction, index and Floer applications.
- **The operator course:** the accessible motivating overview is separate from
  advanced proof reconstruction. The latter is a capstone at the end of the full
  source order and Davis–Kahan route. G3's deliberately nonnumeric order remains
  unchanged. Teaching order and proof dependence remain distinct.
- **Practical courses:** setup, measurement, diagnosis and verification belong
  before the tasks that use them. This moves food safety/process planning, dust
  control, drawings/tolerances and diagnostic state models into the relevant
  foundation lectures. Existing safety qualifications remain; this is not a new
  medical, code-compliance or field-practice validation.
- **Literature:** complete narratives and their interpretation are grouped within
  their own work. Main routes intentionally include a coherent same-work critical
  lecture where preserving an old selected subset would leave a tiny fragment.
  Modern source order follows publication-oriented work order. Chaucer's main
  route selects its frame/tale introduction and critical lecture; other tale
  lectures remain in its deeper route. Tolkien's main route uses its three
  narrative lectures, with further interpretive studies in the full route.
- **Ancient history:** ten comparative survey lectures are separate from explicit
  regional routes. Appended regional studies no longer fall into “the world
  around 1500” merely because of their numeric IDs. Time/place transitions make
  returns to earlier periods explicit, including East African livelihoods,
  Swahili coasts and later political memory.
- **Journey to the West:** the completed expanded retelling through chapter 21 is
  now thirteen manuscripts. The continuation handoff starts at chapter 22 and
  reserves no future IDs. New writing continues through the maintained section
  selector; a fixed manuscript count must not hide later additions.

The review covered every inventory and route sequence, with representative
narration and boundary checks. It does not claim a new line-by-line factual or
formal proof audit of the entire library.

## Three deliberate short exceptions

- `ancient-medieval-world:055000`, about 9.8 minutes: a complete focused Caribbean
  case study. Adjacent regional studies concern different places and periods.
- `discrete-mathematics:040000`, about 7.1 minutes: a focused introduction to
  absorption for hypergraph matchings.
- `discrete-mathematics:042000`, about 5.9 minutes: a distinct four-cycle
  calculation in graph quasirandomness.

Combining the latter two would join different methods just to increase runtime.
Their sidecars explain the short format, and that explanation appears in browser
lists. No expanded same-method sequel is claimed for either. Genuine developed
introductions elsewhere, such as the three compact literary overviews, remain
separate from their deeper studies.

## Verification and authoring handoff

The route audit reports no unresolved installed references or unrouted material.
All 32 changed packs round-trip through portable export and installation. Focused
checks cover source consolidation, extraction, metadata, route ordering, caches,
imports, playback selection, the course graph and companion associations. Desktop
and phone browser checks inspect combined lecture counts, exact-ID search,
transcript/return navigation, literature order and the visible short exceptions.

The 405 original authored relationship records retain their endpoints, relation
kinds and explanations, including 61 relations now internal to a combined unit.
Proof cycles are checked before component contraction. Companion slides attach to
current combined lectures without changing their content. Frozen presentations,
numerical models, and the historical relationship evidence files are unchanged.

Use current pack indexes and READMEs when assigning the next writing pass; do not
restore removed parts from an old snapshot. Each pack's `provenance.yaml` and
sidecar composition records preserve inherited authorship and the scope of the
editorial revision. `LECTURE_STYLE_RULES.md` owns the duration preference and its
exceptions. The [handoff guide](../agent-content-handoff.md) explains continuation.

No production TTS or presentation build was run. Combined narration has a new
speech identity, so its recordings must be prepared from the new manuscripts.
