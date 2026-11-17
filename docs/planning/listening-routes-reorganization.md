# Listening-route organization and writing handoff

Organization pass dated 16 November 2026. Navigation and the three new compact
introductions were authored by GPT-6; the exact runtime variant is unavailable.
The purpose is to make the existing library coherent and let content agents
resume writing. Finishing every retelling or commissioning more introductions
is not a prerequisite for this handoff.

**Current handoff:** the route-only counts and preservation assumptions below
are historical. The [adult consolidation](adult-lecture-consolidation.md) replaced
related fragments with combined manuscripts. Subsequent contributions now put
the route inventory at 51 audio packs and 1,354 manuscripts (16 November 2026).
Journey's pack-local handoff now covers chapters 1–27 and resumes at chapter 28.
Use current pack indexes and continuation notes; this document reserves no IDs.
The [refactor completion audit](refactor-completion-audit.md) records the finished
native browser, learning-map, companion-viewing and transfer infrastructure.

## Source ownership and listening order

Manuscripts remain in their existing packs with stable namespace-qualified IDs.
`track.json` owns the full audio inventory. Pack-local `navigation.json` owns
curated main routes, extended studies, named sessions, preparation links, and
period routes. Existing `:main` bookmarks keep the complete original sequence.
The presentation index, frozen decks, numerical models, existing narration and
recordings are unchanged by this organization pass.

Nineteen audio packs have additional routes. Shorter coherent curricula retain
their existing sequence. The inventory at the handoff contains 2,631 audio
manuscripts in 50 source directories, plus 22 presentation lectures. These are
manuscript counts rather than distinct literary works or equal units of study.
The [coverage review](literature-coverage-2026-11-16.json) counts 88 named literary
work units across the literature holdings, with its counting convention stated.

The subsequent [adult-lecture consolidation](adult-lecture-consolidation.md)
changes the manuscript units themselves. The user explicitly chose single
combined manuscripts over playback-only sessions and did not require backward
compatibility. The counts and preservation assumptions below describe the
earlier route-only handoff; use current pack indexes for authoring.

## Main routes and branches

| Area | Organization |
| --- | --- |
| Children's stories | One Children's Stories category; standalone stories, Willow Bend, and Brook Road retain their separate worlds, ages, seasons, and IDs |
| Literature across packs | Five period routes reuse available recordings: ancient traditions, medieval, early modern, nineteenth century, and twentieth century |
| Pre-1900 literature | A period-ordered survey links a full available study for each work; longer selections have narrative session boundaries |
| Twentieth-century literature | 47 work units follow publication-oriented order, pairing narrative with selected criticism and linking all existing work-level material |
| World History | Historical case studies, literary epics, and How We Know are separate routes |
| Ancient and Medieval World | 50 broad survey entries form the backbone; 130 regional/evidence entries form optional branches |
| Biography | A subject hub groups the 71 episodes without presenting its accumulation order as a chronological world-history survey; paired biographies retain their order |
| Fiction and comedy | Foundational routes link schools, critical arguments, performance, translation, and practice as appropriate |
| Music | Composition foundations link listening, advanced composition, and a production route ordered from sound sources and capture through mixing and delivery |
| Advanced mathematics | Analysis, topology/geometry, category theory, abstract algebra, differential equations, numerical analysis, optimization, and discrete mathematics expose their distinct specialist strands |
| Original operator library | G2 topic routes use the maintained `curriculum/topics.json` assignments; its original 156-entry sequence remains available |
| Other curricula | Proof, linear algebra, multivariable calculus, logic/types, probability, algorithms, the paper track, modern history, short science, and practical/trades sequences retain their coherent existing orders |

The Austen entries previously labeled as Shelley's Gothic fiction now have their
own Regency social-fiction section. Canonical spoken text is unchanged.

Preparation links point to background courses as optional learner suggestions.
They do not create access gates, formal proof dependencies, or claims of
historical influence. Where a suggested course is long, review its relevant
parts. Mathematical branch boundaries were checked against the subjects and
examples actually present; they are not a completed theorem-level dependency map.

## Compact introductions and honest scope

The desired direction is usually one to three approximately 40-minute main-track
sessions per substantial literary work, with optional extended study. This is
an editorial preference rather than a duration gate. Grouping complete existing
recordings into sessions does not rewrite, split, or regenerate their audio.

Three new standalone introductions are indexed in `content/literature-survey/`:

- `001000`: Decameron, about 31 minutes. The whole frame and selected complete
  tales introduce the book; the 129-entry extended study remains intact.
- `002000`: Three Kingdoms, about 29 minutes. Includes successors and the fall
  of all three states, linked to the existing extended narrative.
- `003000`: Shahnameh, about 30 minutes. Follows the poem's full arc through
  selected episodes and distinguishes legendary and historical modes.

These have separate IDs, source notes, and attribution. They do not reassign
prior authorship or replace the earlier manuscripts. Optional ideas for compact
Water Margin and Journey introductions remain unindexed; they are not unfinished
requirements for the organization task.

Journey's main entry now uses its existing opening and historical-context
lectures, explicitly labeled as such. The complete six-part retelling plus
context remains a separate route. The expanded retelling remains in progress,
with 25 manuscripts covering selected chapters 1–12. Water Margin's main entry
similarly pairs the existing opening with the version-history essay. Its deeper
route is labeled an expanded opening narrative through Zhu Family Village,
not a complete retelling. No recording or placeholder claims later installments
already exist.

Durations are estimated from canonical spoken words at 145 words per minute,
not measured recording lengths. Counting installments alone would exaggerate
some coverage differences: Decameron's approximately 510-minute deep dive is
linked from a 31-minute introduction. The twentieth-century holdings contain
44 novel/cycle units, one poem, one play, and one short-story collection; route
organization improves access but does not itself fill those genre imbalances.
Regional/tradition labels in the coverage report are limited to evidenced
examples and are not guesses about author identity from a story's setting.

## Resume the interrupted writing

The original expanded Journey writer should open
[the pack-local continuation handoff](../../draft-stages/tts-pre-1900-literature/notes/journey-west-continuation-handoff.md)
and the existing chapter source map. As of the latest checked contribution,
17 expanded manuscripts cover selected-witness chapters 1–27; the next source
chapter is 28. Read the live handoff before writing, since another batch can
advance this boundary. Consolidated component IDs are historical evidence,
not additional playback entries. Recheck current IDs and writer ownership
before assignment; no future IDs are reserved here. The selected witness's
inserted chapter 9 and its numbering consequences remain explicitly documented.

The expanded route uses `include_sections`, selecting its existing section from
the current inventory. Append manuscripts, sidecars, source records and entries
to `track.json` in narrative order. New entries join that deep dive automatically.
Update its progress title/summary and source map as chapters are completed. The
shorter survey remains independently curated, so it does not grow into another
chapter-by-chapter retelling. No server edit, global registration, runtime pack
build, synthesis, or repository-wide test is required to continue writing.

A separate [Water Margin handoff](../../draft-stages/tts-world-history/water-margin-organization-handoff.md)
records its actual stopping point, version-specific endings, and possible
continuation units. Its shared World History IDs still require the existing
reservation/merge workflow. How We Know retains its reserved ID range.

For assignments, source ZIPs, safe imports, and portable releases, use
[the handoff guide](../agent-content-handoff.md) and
[the navigation format](../content-packs.md#main-routes-and-deep-dives).

## Verification and continued upkeep

`python tools/audit_listening_routes.py --output /tmp/listening-routes.json`
checks all current audio inventories and route references, reports material
outside curated routes, and estimates listening time. The report is an editorial
diagnostic, not a delivery gate for new or unfinished content. Runtime discovery
continues to expose usable manuscripts, including unindexed drafts. A malformed
navigation edit retains its last usable branches and refreshes the full source
collection rather than dropping new manuscripts.

Focused tests cover route flattening, session order, automatic inclusion of new
section members, source counts and anchors, portable export, recordings and saved
positions, invalid-navigation recovery, live reload, and the existing content
import/reader behavior. Browser checks inspect desktop/mobile layout, period
navigation, deep-dive return links, and unfinished Journey labeling. No TTS or
presentation/media builds are part of this organization pass.
