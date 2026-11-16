# Library ordering and coverage review

Read-only audit,16 November 2026, authored by GPT-6 (exact configuration unavailable).
The audit was prepared separately from implementation; its route proposals are
now integrated into the owning packs. No existing lecture narration or model
code was changed for these ordering decisions.

This is an organization review of every source inventory, its current ordering
and section names, relevant README intent, and selected opening/closing passages.
It is not a claim to have listened to every recording, revalidated every factual
claim, or derived a complete formal prerequisite graph. Existing source IDs,
paired episodes, full original listening orders, mathematical models and frozen
presentation compositions must remain stable.

The captured audio snapshot contains **50 source packs and 2,631 manuscripts**,
plus **22 authored presentation lectures**. Counts were checked against the integrated worktree; rerun the route audit
when authors add material.
Time estimates below use canonical extracted speech at 145 words/minute and are
measurements, not duration requirements or editorial acceptance tests.

## Decisions that change the route design

1. **Do not split every pack.** The short proof, linear algebra, multivariable,
   logic, probability and practical courses have identifiable progression. Their
   complete courses should remain the main routes. Their length alone is not an
   argument for a new overview or a deeper branch.
2. **Separate genuinely braided advanced subjects.** Abstract Algebra’s later
   additions rotate between arithmetic, representation theory, enumerative/quantum
   geometry and DT/wall crossing. Numerical Analysis similarly rotates among
   sparse solvers, sensitivity, validated dynamics and PDE certification.
   Optimization and Differential Equations show the same pattern in their later
   specialist material. The pack-local navigation files give exact ordered IDs for
   selectable strands while retaining every existing source in its archive.
3. **Music has two different practical goals.** Composition 001000–016000 is a
   coherent entrance. Recording/processing/delivery should offer its own route,
   placing notes-to-waveforms 021000 and capture 025000 before detailed processing
   and delivery. Hearing 029000–032000 and reconstruction 033000–036000 are a
   third useful route; later development/orchestration/fugue/complete-work studies
   deserve a composition workshop route. Preserve every existing numerical lab.
4. **Writing and comedy already contain useful overview material.** Fiction’s
   first seven lessons and 007500 map, and comedy’s global traditions plus 030500
   field guide, are sufficient entrances. The school, practitioner, voice/time,
   translation, improvisation and performance studies can branch from them.
   No new survey manuscript is required to make those branches intelligible.
5. **Biographies are a subject collection, not world chronology.** Group the
   71 episodes about 52 people into optional thematic strands, keep every I/II pair
   together, and use an accurate mathematical/scientific-lives title. Do not turn
   a biography into a prerequisite for its subject’s theorem.
6. **G2 already owns a maintained topic map.** Its13 topics in
   `curriculum/topics.json` cover the 156 audio lectures. Reuse that assignment
   for topic navigation; retain the coherent complete learner path unchanged.
   G3’s deliberate paper order is meaningful even when its numeric IDs jump.

## Full pack disposition

| Source pack | Items | Estimated hours | Disposition and reason |
| --- | ---: | ---: | --- |
| `ancient-medieval-world` | 180 | 26.42 | **Keep the new survey/regional routes.** The 50 existing survey entries give a geographic/chronological backbone;130 regional/evidence studies should remain optional. Do not interleave the 32-entry East African elaboration into the broad survey. |
| `bedtime-stories` | 57 | 3.98 | **Retain standalone story order; unified category.** 57 independently usable stories do not require a chronological curriculum. Group under Children’s Stories; retain thematic sections and story IDs. |
| `brook-road-builders-ages-3-4` | 90 | 7.13 | **Retain season/episode order; unified category.** 90 episodes in 15 seasons preserve evolving objects, places and relationships. Sequence is recommended; the character’s fifth birthday does not change the listener age label. |
| `childrens-bedtime-stories-episodic-ages-3-4` | 66 | 5.64 | **Retain season/episode order; unified category.** 66 episodes in 11 seasons preserve Willow Bend continuity. Use the series title in navigation, and do not combine its world with Brook Road. |
| `literature-survey` | 3 | 1.50 | **Keep only usable introductions indexed.** The new compact introductions point to pre-existing work studies. They count as new treatments of existing works, not new works. Unfinished authoring reservations are not playback entries or organization gates. |
| `abstract-algebra` | 84 | 10.50 | **Use selectable strands; original archive retained.** After the elementary group/ring/field/Galois spine, the order develops into interleaved arithmetic, representation, derived/algebraic geometry and curve-counting strands. In particular 057000–084000 cycles repeatedly among these subjects. Follow coherent strands with explicit preparation instead of treating every extension as the next introductory algebra lesson. |
| `algorithms-computability-complexity` | 12 | 2.83 | **Retain the existing12-entry sequence.** Orientation/cost/verification leads to undecidability, then automata/grammars, then design paradigms. These are distinct introductions, not an accidental chronological braid; the mathematics category fix is sufficient. |
| `analysis` | 76 | 13.92 | **Retain the new foundation/branch routes.** Real analysis 001000–012000 provides the entrance. Complex, measure/functional, spectral, and PDE routes expose their different preparation without forcing every student through all 76 entries. |
| `category-theory` | 35 | 13.13 | **Retain the new foundation/branch routes.** Foundations through string diagrams precede tools, semantics and geometry. Keep chain complexes/resolutions before derived-geometry use; show additional topology/algebra preparation rather than inventing formal proof edges. |
| `comedy-history` | 34 | 9.86 | **Use selectable strands; original archive retained.** The first six global tradition lectures and the field guide are a coherent entrance. Modern theory, institutions, improvisation, stage forms and translation currently follow acquisition order and should be selectable strands. |
| `deep-time` | 36 | 9.30 | **Retain broad sequence and human-prehistory branch.** Cosmos→Earth→life→human prehistory is coherent. Historical learners may enter through human prehistory without making the entire cosmology sequence a prerequisite. |
| `differential-equations` | 42 | 5.54 | **Use selectable strands; original archive retained.** A beginner can follow the first nine ODE lectures without being forced immediately through weak PDE theory. Later entries braid qualitatively different PDE and dynamics programs; named routes make their analytic assumptions visible. |
| `discrete-mathematics` | 42 | 5.41 | **Use selectable strands; original archive retained.** The first twelve lectures form a broad introductory backbone; later graph, probabilistic, discrepancy and code/pseudorandomness strands can be pursued independently with preparation links. |
| `fiction-writing` | 44 | 12.02 | **Use selectable strands; original archive retained.** The first seven craft lectures and the map are a coherent entrance. The following school histories, author arguments and specialist narrative techniques need separate routes rather than a mandatory 44-entry run. |
| `history` | 71 | 33.68 | **Use selectable strands; original archive retained.** The existing71 episodes are a thematically accumulated collection of 52 people, not a chronological world-history survey. A subject hub makes that scope clear, preserves paired episodes, and offers optional families without inventing teaching or influence prerequisites. |
| `g2` | 156 | 29.54 | **Use selectable strands; original archive retained.** Use the 13 maintained topic assignments to expose the long learner library without changing the coherent original sequence. Do not mechanically sort folders or copy transcripts. |
| `linear-algebra` | 15 | 1.68 | **Retain the complete introductory order.** 15 calculation/proof entries progress from equations and bases to maps, spectral/SVD geometry, duals, tensors and exact sequences. This is a coherent short foundation, not a survey/deep-dive imbalance. |
| `logic-types` | 8 | 2.56 | **Retain all 8 entries in order.** Proofs-as-objects and normalization lead to dependent quantifiers/inductives, then equality, transport, dependent matching and the kernel. Later items use the objects established earlier. |
| `mathematical-proof` | 18 | 1.67 | **Retain all 18 entries in order.** Statements/logic/quantifiers/definitions precede proof methods, sets/functions/quotients, induction/infinity, then epsilon and compactness arguments. The actual short duration makes another main/deep split unnecessary. |
| `modern-literature` | 218 | 42.21 | **Retain work-level survey/deep routes and session groups.** The 47-work survey is now publication-oriented rather than addition-oriented. Keep complete story components for long novels and explicit selected-story labeling for Ficciones. |
| `modern-world` | 94 | 25.79 | **Retain the connected94-entry chronological course.** The order runs from around1500 through interconnected early-modern economies, imperial/industrial transformations, world wars, decolonization, late Cold War and contemporary crises. Large size alone does not imply that half the history should be demoted. Optional chapter headings 001000–012000,013000–026000,027000–040000,041000–058000,059000–074000,075000–094000 can improve orientation without altering order. |
| `multivariable-calculus` | 18 | 1.90 | **Retain all 18 entries in order.** Neighborhoods/limits→total derivative/chain rule→inverse/implicit/Taylor/extrema→multiple integrals/change of variables→curves/Green/surfaces/Stokes. These endpoints directly prepare manifold and PDE routes. |
| `music-theory` | 42 | 12.12 | **Use selectable strands; original archive retained.** Composition foundations 001000–016000 form a coherent main route. The later production, hearing, ear-training and advanced composition units are distinct tracks; a production learner should encounter notes-to-sound and capture before detailed mixing and delivery. |
| `numerical-analysis` | 28 | 4.47 | **Use selectable strands; original archive retained.** The first thirteen entries establish error, conditioning, algorithms and interval certification. Later topics braid sparse solvers, sensitivity, validated ODEs and PDE estimators. Topic branches preserve local mathematical progression. |
| `optimization-duality` | 25 | 4.35 | **Use selectable strands; original archive retained.** Foundations 001000–012000 are coherent. Later submodular, splitting, robust-risk and exact-conic topics should follow their own line of development rather than alternate by addition date. |
| `g3` | 32 | 8.62 | **Retain the declared paper order; do not sort numeric IDs.** The manifest intentionally orders geometry→exact spectral data/domains/residual/gaps→norms→Sylvester→angle families→transport. The local ID 011000 belongs early because domains are part of the general theorem’s hypotheses. Beginner preparation can link to G2/Analysis without weakening source scope. |
| `physical-world` | 6 | 1.29 | **Retain all 6 entries in order.** The small introductory sequence moves from motion/energy to heat, fields, waves and matter. It is already a broad general-audience entrance. |
| `practical-contractors-estimates` | 18 | 2.08 | **Retain the compact principles-to-cases route.** Scope and diagnosis→estimate/contract distinctions→inspection/punch lists→commissioning and acceptance. The 18 entries form a compact process route. |
| `practical-first-aid` | 21 | 2.48 | **Retain the compact principles-to-cases route.** Recognition, communication and coordinated first response precede condition-specific cases. Retain the existing entry points and training-oriented limits; no new clinical sequence is inferred by this organization audit. |
| `practical-food-science` | 21 | 2.35 | **Retain the compact principles-to-cases route.** Heat, water and ingredient structure precede increasingly specific cooking examples, ending in vegetables, grains/legumes and egg structures. The 21 entries are a short concept-to-case course. |
| `practical-gardening` | 21 | 2.30 | **Retain the compact principles-to-cases route.** Soil/water/root models precede cultivation and crop-specific planning, with rotation and seed saving later. Retain the 21-entry biological progression. |
| `practical-household-maintenance` | 18 | 2.09 | **Retain the compact principles-to-cases route.** Systems inventory and failure mechanisms precede diagnosis and concrete case studies. The 18-entry sequence already separates general reasoning from later applications. |
| `practical-mechanics` | 21 | 2.30 | **Retain the compact principles-to-cases route.** Force, torque and wear precede transmissions/bearings/fluid systems and later pump, seal and stored-energy cases. Retain the 21-entry progression. |
| `practical-navigation-outdoors` | 18 | 2.13 | **Retain the compact principles-to-cases route.** Terrain and bearings precede uncertainty, weather interpretation and unplanned-stop case handling. The 18-entry route has an identifiable planning-to-response arc. |
| `practical-networking-controls` | 21 | 2.43 | **Retain the compact principles-to-cases route.** Physical packet/power paths precede switching/routing, devices, automations, repeatable configuration and identity recovery. The 21-entry sequence develops the layers it later combines. |
| `practical-sewing-textiles` | 21 | 2.33 | **Retain the compact principles-to-cases route.** Fiber/grain and machine interaction precede construction and later knit, bias and trouser-fitting cases. Keep the 21-entry foundations-to-alterations path. |
| `practical-tools-and-measurement` | 18 | 2.06 | **Retain the compact principles-to-cases route.** References, precision and calibration precede controlled setup, quality control, under-load diagnostics and acceptance fixtures. Keep the 18-entry measurement path. |
| `practical-vehicle-maintenance` | 21 | 2.30 | **Retain the compact principles-to-cases route.** Forces/tires/powertrains precede system-specific diagnosis, with fuel-trim and electric/hybrid cooling/diagnostic boundaries later. Retain the 21-entry order. |
| `pre-1900-literature` | 465 | 37.84 | **Retain period/work survey and work-level extended studies.** The new period grouping repairs the previous Hamlet→Quixote→Dante→Lear→Flatland→Macbeth accumulation. Keep Austen separate from Shelley. Expanded Journey to the West must say opening chapters1–12 and remain extension-friendly. |
| `probability-measure` | 12 | 4.40 | **Retain all 12 entries; optional preparation only.** Finite events/conditioning/random variables precede measure/conditional expectation, limits/martingales and inference/Markov/product/weak convergence. Product measures 010000 could optionally be taken after 004000 by a learner needing it, but the existing lecture establishes its own variables; no mandatory reorder was demonstrated. |
| `topology-geometry` | 114 | 13.83 | **Retain the new foundational and specialist routes.** Foundational topology leads to named manifold/forms, algebraic/curvature, symplectic, and gauge/Floer routes. Preserve original source order in the archive and use explicit analytic/algebraic preparation for the advanced strands. |
| `trades-building-science` | 21 | 2.49 | **Retain the compact principles-to-cases route.** Coupled heat/air/water flows precede assemblies and later foundation, retrofit-moisture and below-grade diagnosis. Retain the 21-entry progression rather than making case studies mandatory preparation. |
| `trades-carpentry` | 21 | 2.35 | **Retain the compact principles-to-cases route.** Loads, wood and layout precede assemblies, connections, decks and roof systems. Retain the 21-entry route and original instructional boundaries. |
| `trades-electrical` | 41 | 8.31 | **Retain the compact principles-to-cases route.** Principles and safe-work boundary precede home-system anatomy, code literacy, materials and diagnostics; the later load/circuit/requirement cases synthesize earlier concepts. Retain the 41-entry authored sequence; optional Tools/Measurement preparation is useful but not a gate. |
| `trades-hvac` | 21 | 2.40 | **Retain the compact principles-to-cases route.** Heat/airflow and refrigeration-cycle models precede loads, distribution, ventilation and later commissioning/measurement/VRF cases. Retain the 21-entry route. |
| `trades-masonry` | 21 | 2.25 | **Retain the compact principles-to-cases route.** Hydration/materials/support precede loads/joints and later rain-entry, reinforcement/corrosion and condition testing. Retain the 21-entry progression. |
| `trades-metalworking` | 21 | 2.25 | **Retain the compact principles-to-cases route.** Material structure/heat treatment precede forming/joining and later weld inspection, coatings and fabrication drawings. Retain the 21-entry route. |
| `trades-plumbing` | 21 | 2.42 | **Retain the compact principles-to-cases route.** Supply pressure and gravity drainage precede specific fixtures/systems and later pressure-loss, simultaneous-venting and tankless-control cases. Retain the 21-entry progression. |
| `world-history` | 110 | 54.62 | **Retain separate case-study, evidence, and literary routes.** Literary retellings and archaeological methods are different purposes from the historical case studies. The existing IDs/complete mixed course remain compatible. Label Water Margin’s partial expanded narrative honestly. |
| `world-reconsidered` | 12 | 6.16 | **Retain all 12 question-centered lectures.** The track moves from evidence and perception through judgment/cooperation/social norms/systems into information, consequences and ethical futures. It intentionally offers standalone questions rather than a comprehensive chronological survey. |
| `g1` | 22 | — | **Preserve authored prerequisite order and all frozen deck compositions.** The 22 authored presentation lectures have explicit prerequisite metadata. Organization must reuse stable IDs and lecture_path; no scene/deck order change is proposed. Kitware and reference decks remain untouched. |

## Evidence for the proposed boundaries

The audit inspected every listed title/section and the source-pack intent.
Representative boundary passages were read in fiction 007500,028000,038000,
039000; comedy 030500,042000,054000; music 016000,017000,029000,033000,037000;
algebra 016000,057000–060000; numerical 014000,018000,024000;
optimization 012000–015000; discrete 013000,015000,028000,034000;
differential 010000,019000,023000,029000; probability 008000,010000;
G3 exact-subspace/domain/residual/gap entries; and biography 029000,035000,
039000,040000. Those passages establish that the examples and objects are
introduced locally and reveal real changes in mathematical/craft purpose.
They do not prove all later formal proof dependencies.

Notable examples:

- Fiction 038000 introduces its own greenhouse-repair situation;039000 introduces
  its own repair-shop/radio experiment. They can be reached through craft and
  revision routes without pretending they are continuations of an earlier plot.
- Algebra 057000 opens with local solvability and rational points;058000 moves to
  rotations/representation lattices;059000 to enumerating projective curves;
 060000 to localization of an integral. This is a clear research-strand braid,
  not a single elementary-algebra staircase.
- Differential 023000 develops dispersive spreading, while 029000 explicitly
  develops the Strichartz estimate. The proposed scattering route places 029000
  before critical-wave applications 028000, while retaining 023000 as orientation.
- G3’s 011000 explains why unbounded domains belong to Davis–Kahan’s actual
  source scope. Its early placement is intentional, rather than an ID-sorting
  error. The complete paper route should not silently become finite-only.

## Literary attention and breadth

[the literary coverage snapshot](literature-coverage-2026-11-16.json) records **88 distinct named work units** across the
current literary holdings:24 pre-1900 works,47 twentieth-century works and 18 World
History literary works, with Journey to the West deduplicated across packs.
A novel cycle, framed tale collection or sacred/epic narrative is counted as one
named unit, not as a claim about how many autonomous texts it contains. The new
compact introductions are additional treatments of existing works.

The primary imbalance is partly a navigation issue and partly a commissioning
issue. The Decameron has129 existing entries taking approximately 510 minutes;
Three Kingdoms’17 entries take approximately 550 minutes; Journey has about 434
minutes split between a complete older treatment and an expanded opening.
A seven-entry Hamlet unit, by contrast, is only about 42 minutes. Entry totals
alone cannot measure the attention given to a work.

The twentieth-century track has47 work units, but44 are novels or novel cycles.
The other three are a poetry work, a drama and a short-story collection. Creating
subtracks does not itself fill that genre imbalance. Additional poetry/drama/
short-fiction commissioning is an optional future editorial decision, not a gate
for completing the current organization.

The old pre-1900 shelf concentrates European and United States writing. Major
Mesopotamian, Egyptian, Greek, South Asian, Maya, Persian and Chinese narratives
already exist in World History. A global period/genre route should surface those
works before describing such traditions as absent. Distinguish the date of a
story’s setting from its composition, earliest surviving witness and publication;
Popol Wuj’s colonial written witnesses and the layered Sanskrit epics particularly
resist a naive publication-year sort.

Language/tradition fields are editorial inventory descriptions supported by named
works and editions in the source manuscripts. Region/identity fields are left
null where a precise claim was not established. A story’s setting is not used to
infer the author’s identity. This is a coverage map, not an identity census.

## Journey to the West: concrete continuation handoff

The authoritative existing guide is
`draft-stages/tts-pre-1900-literature/notes/journey-west-expanded-retelling-source-map.md`.
The current 25 expanded entries 441000–465000 cover the selected witness’s chapters
1–12. The last entry is Guanyin’s revelation and Xuanzang’s oath. Continue with
chapter13(the first mountain danger, loss of the attendants, and hunter Liu
Boqin), then14(Wukong’s release and the difficult start of their relationship),
then15(the White Dragon Horse/Eagle-Sorrow Stream). Let scenes determine episode
boundaries; the previous installments do not use one lecture per chapter.

At this audit,466000 and above were unused in both the current track index and
numbered manuscripts. **466000 is a candidate next ID, not a permanent reservation:**
the original writing agent must recheck the current repository before taking its
assigned range. Maintain the exact section key
`late-ming-chinese-novel-journey-to-the-west-expanded-retelling` so the root’s
extension-friendly route selector includes new indexed chapters automatically.

Keep manuscripts, per-lecture sources/anchors and the updated chapter-to-lecture
map together in the assigned source pack. Propose catalog additions rather than
replacing a stale shared track/source catalog. The normal content-overlay import
protects conflicting existing files; this literary pack does not become subject
to World History’s specialized merge command merely because the earlier overview
lives there. Keep the expanded series distinct from World History 048000–054000.

The source-map’s River Child warning is essential: the selected witness labels
it chapter9 and identifies a later insertion; other editions number subsequent
material differently. Match chapter subjects/titles when comparing editions.
Do not silently treat the inserted origin tale as a historical biography of
Xuanzang or as proven original to the 1592 printing.

The route should say that the expanded telling currently covers opening chapters
1–12 and continues as new entries arrive. Finishing chapters13–100 or authoring a
new short overview is **not required to finish the reorganization**. The existing
complete six-part narrative and historical/textual companion remain available.

## Integration and verification

Ten pack-local navigation files implement the audit’s additional route proposals.
Each proposes an explicit default route and child routes using stable local IDs;
all original IDs are covered. Preparation links are soft learning suggestions,
not formal proof or historical-influence edges. Some repeat a foundational item
in a specialist route; that reuses its identity and recording rather than copying
content. The audit agent did not change repository files. The ten objects have been integrated; the reorganization’s focused checks cover
route membership and portable export, with browser inspection recorded in the
main reorganization notes.

Strongest interventions are the advanced mathematics braids, music’s production
path, and the misleadingly broad biography collection title. Fiction/comedy and
G2 topic navigation are useful conveniences. The existing short courses remain
complete main routes. The organization requires no further lecture commissioning. Recompute references after combining proposals, since
`:main` becomes the compatibility archive when a new default route is installed;
preparation should prefer the new `:survey` when that is the intended foundation.

A mechanical source audit should verify unique IDs, resolvable installed-pack
references, session flattening and unchanged speech identities. Inspect browser
navigation and portable export. No source-count quota, duration ceiling, caption
string test, TTS run or media build is warranted for this organization pass.
