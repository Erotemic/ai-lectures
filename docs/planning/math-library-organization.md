# Mathematics library organization

Audit and guide handoff, 16 November 2026. The guide and this review were
authored by GPT-6; the exact runtime variant is unavailable.

The library needs several clear entrances. A source pack is a useful authoring
boundary, but its complete inventory is often too broad to serve as a learner's
first course. Keep those inventories and specialist studies intact. Use a
subject guide and selected paths to connect the material by what a learner
wants to understand.

`content/mathematics-guide/` now supplies that guide. It has no new manuscripts.
Its default `start` hub contains six subject families and four staged paths
through existing lectures. Lecture identities and source ownership remain with
their existing packs. The guide's selections are recommendations, not new
formal dependencies or a claim that every mathematical background gap is closed.

## Source inventory and subject families

The audited inventory contains 17 mathematics audio packs and **412 indexed
manuscripts** at the final manifest read. Number theory grew from 48 to 54 during
this review; future contributions should use the live manifests. Counts here
mean entries in `track.json` whose source files exist, not a census of every
numbered file or every historical planning ID. No additional unindexed numbered
manuscripts were present in these 17 directories at that read.

| Family | Packs and current indexed manuscripts | Guide entry collections |
| --- | --- | --- |
| Proof and linear foundations | `mathematical-proof` 3; `linear-algebra` 3 | `mathematical-proof:main`, `linear-algebra:main` |
| Analysis, geometry, and continuous change | `analysis` 44; `multivariable-calculus` 3; `topology-geometry` 24 | `analysis:survey`, `multivariable-calculus:main`, `topology-geometry:survey`, with complex and measure/functional branches exposed |
| Logic, algorithms, and algebraic structure | `logic-types` 8; `algorithms-computability-complexity` 12; `abstract-algebra` 22; `category-theory` 35 | `logic-types:main`, `algorithms-computability-complexity:main`, `abstract-algebra:survey`, `category-theory:survey` |
| Number theory, combinatorics, and probability | `number-theory` 54; `discrete-mathematics` 13; `probability-measure` 12 | `number-theory:survey`, `discrete-mathematics:survey`, `probability-measure:main` |
| Numerical methods, optimization, and equations | `numerical-analysis` 15; `optimization-duality` 10; `differential-equations` 13 | `numerical-analysis:survey`, `optimization-duality:survey`, `differential-equations:survey` |
| Operator theory and Davis–Kahan | `g2` 109; `g3` 32 | `g2:topics`, `g2:davis-kahan`, `g2:matching`, `g2:statistics`, `g3:main` |

G1 adds 22 indexed visual presentation lectures as a separate format and is
linked through `g1:main`. Its frozen presentation compositions retain their
existing content and scene order. The 71 historical portraits are useful
context but include scientists as well as mathematicians; they are not counted
as another prerequisite mathematics course. G4's six proposed YWS-specific
nodes remain planned, not installed lectures.

These families are entrances, not disjoint branches of mathematics. For
example, probability uses analysis, numerical linear algebra uses spectral
theory, and algebraic geometry uses algebra, topology, and category theory.
Connections should be explained at their point of use rather than enforced
by making every listener complete all adjacent subjects.

## Topic indexing and discovery

All 412 current audio lectures have explicit entry tags in their source
`track.json` files, alongside broad inherited subject tags. The pass adds 1,508
entry assignments and tags the existing 57 navigation collections. Together
these use 620 subject and concept labels: broad terms connect courses, while
specific terms make individual constructions searchable. New number-theory
branches reuse that vocabulary. Future authors should reuse an established
label before adding another spelling of the same idea.

The browser exposes clickable topic tags, a searchable topic field, and keyword
search over tags. Topic links search across packs. Study plan and Learning map
also search tags, but shared tags do not create dependency or influence edges.
Subject directories have collapsible families and a jump control; expansion
choices persist for the selected listener on the device. The full inventory
remains accessible through search, direct links, and the all-collections view.

The tagging pass preserves all other manifest values, manuscript bytes, and
speech hashes. Number-theory route changes are separate editorial selections;
its original complete order remains available as an archive. These metadata
changes were authored by GPT-6 (exact runtime variant unavailable) and do not
replace inherited lecture attribution.

## The four implemented paths

Within each row below, arrows give the recommended order. Every reference is
to a current indexed manuscript. Repeated subjects in different paths reuse
the same lecture; no duplicate manuscript is created.

| Guide collection | Ordered stages | What completion means |
| --- | --- | --- |
| `mathematics-guide:foundations` | `mathematical-proof:001000 → 009000`; then `linear-algebra:001000 → 006000 → 012000` | An introduction to proof, functions, linear maps, spectral directions, and dual constructions. Epsilon/compactness arguments remain in `mathematical-proof:016000` when needed. |
| `mathematics-guide:calculus-and-change` | `analysis:001000 → 002000 → 003000 → 004000`; then `analysis:005000 → 006000 → 007000 → 008000`; then `multivariable-calculus:001000 → 008000 → 015000`; then `differential-equations:001000 → 004000 → 007000` | A path from limits to ODEs. It stops before measure theory, functional analysis, and PDE proofs. |
| `mathematics-guide:proofs-programs-structure` | `logic-types:001000 → 002000 → 003000 → 004000`; then `logic-types:005000 → 006000 → 007000 → 008000`; then `algorithms-computability-complexity:003000`; then `category-theory:001000 → 002000 → 003000 → 004000` | Proof objects, equality and kernel trust, followed by two applications. The category stage reaches universal properties; adjunctions, Yoneda, higher categories, and full computability remain deeper studies. |
| `mathematics-guide:reliable-computation` | `numerical-analysis:001000 → 002000 → 003000 → 004000`; then `numerical-analysis:006000 → 007000`; then `optimization-duality:001000 → 002000 → 003000 → 004000` | Distinguishing an accurate computed answer from a mathematically optimal answer, with explicit error and duality certificates. It does not establish spectral perturbation theory or a general verified solver. |

The paths contain 5, 14, 13, and 10 lectures respectively. Extracted narration
at 145 words per minute estimates approximately 184, 314, 267, and 169 minutes.
These measure current material; they impose no lecture-length or course-size
target. Each path has independent chapter boundaries and links to full studies.

Advertised preparation matters:

- The foundations path assumes school algebra. Proof-writing and vector-space
  concepts are taught within its selected lectures.
- The calculus path needs elementary functions and trigonometry. Before the
  multivariable stage, the listener needs vectors, matrices, determinants, and
  dot products; `linear-algebra:001000` and `006000` supply this preparation.
- The proofs/programs path assumes sets, functions, logic, and short proofs.
  Vector-space or group examples help the category stage. It does not require
  the complete abstract-algebra course or pretend to teach every categorical
  construction invoked by advanced geometry.
- The computation path assumes elementary linear algebra and single-variable
  calculus. Derivatives, integrals, gradients, norm estimates, and the stated
  convexity/constraint qualifications remain relevant. A small residual does
  not automatically prove a small forward error; KKT equations do not
  automatically certify a nonconvex optimum.

## Where overlap is useful

| Repeated material | Distinct purposes | Organization decision |
| --- | --- | --- |
| Linear algebra, G2 foundations, numerical linear algebra | Introductory matrix/vector reasoning; Hilbert/operator foundations; finite-precision algorithms | Use the three-lecture linear-algebra course as the general entrance. Do not require all 23 G2 foundation lectures again for a listener who already knows that material. G2 remains the detailed operator reference. |
| Analysis measure/integration and probability measure/Fubini | General analytic construction and limit theorems; probabilistic information and distributions | Cross-link `analysis:029000`–`034000` with `probability-measure:004000` and `010000`. Retain each treatment's question and hypotheses rather than mechanically merging them. |
| Sheaves in category theory and topology | Categorical gluing and universal language; Čech calculations and derived cohomology examples | `category-theory:013000` is an accessible categorical entrance; `topology-geometry:022200` supplies a more computational geometry treatment. Offer them as related approaches. |
| Complexes/resolutions in category theory, algebra, and topology | First explicit Tor calculation; module resolutions and homological machinery; chains and geometric invariants | Use `category-theory:035000` as a concrete bridge when appropriate, alongside `abstract-algebra:016000`/`021000` and `topology-geometry:011000`. These serve different destinations. |
| Finite fields and ideal factorization in algebra and number theory | Structural algebra; explicit arithmetic constructions and prime splitting | Prefer the number-theory calculations for arithmetic routes and link back to the structural algebra treatment. Familiarity should allow skipping duplicated foundations. |
| G1, G2, and G3 spectral material | Visual concept lessons; detailed operator curriculum; paper-focused reconstruction | Keep the three formats distinct and visible. G3 explicitly has its own audience and assumes linear algebra, singular values, limits, and integrals. It is not a mandatory repetition after all of G2. |

## Number-theory branches and further ordering review

The new number-theory navigation below is implemented. The topology and visual
sequence changes that follow are proposals for the existing track owners.
Existing manifests and source text are unchanged.

**Number theory now has branches.** Its original 54-entry main sequence
interleaves elementary arithmetic, analytic prime-distribution proofs,
algebraic number theory, and local arithmetic. The new
`content/number-theory/navigation.json` preserves that full order as
the `number-theory:main` archive. A six-lecture `:survey` is the default, with
seven deeper branches. Every one of the 54 indexed lectures occurs in at least
one curated route, without requiring a survey listener to take all of them:

- `:survey`: `001000 → 002000 → 003000 → 004000 → 006000 → 009000`.
- `:approximation`: `004000 → 005000 → 011000`.
- `:reciprocity`: `003000 → 006000 → 007000 → 008000 → 012000 → 024000 → 024500`.
- `:finite-fields`: `003000 → 013000 → 014000 → 025000 → 025500`.
- `:analytic-primes`, after elementary divisibility, congruences,
  arithmetic functions, and elementary analysis:
  `008000 → 009000 → 015000 → 016000 → 017000 → 018000 → 026000 → 019000 →
  020000 → 021000 → 022000 → 023000 → 026500 → 026750 → 028000`.
  Number-theory `026000` supplies the contour and Cauchy foundation before
  continuation and nonvanishing arguments; the full complex-analysis course
  is a deeper alternative. The final stage reaches the prime number theorem.
- `:algebraic-integers`, after rings, modules, finite field
  extensions, and elementary linear algebra (the class-group calculation also
  uses lattice geometry):
  `012000 → 027000 → 027250 → 027625 → 027750 → 027875 → 027500 → 029000 → 029250`.
- `:quadratic-forms`: `029500 → 029750 → 030000`, after the algebraic-integers
  and reciprocity branches.
- `:local-fields`, after congruences, finite fields, completeness, and ideal
  arithmetic, with quadratic reciprocity for the final global identity:
  `010000 → 030250 → 030500 → 030750 → 031000 → 031250 → 031500 → 031750 →
  032000 → 032250 → 032500 → 032750 → 033000`.

The important reversal is `027500`: its class-group calculation currently
precedes `027625`, `027750`, and `027875`. The current number-theory README
explicitly says these later lectures complete the algebraic prerequisites of
that earlier calculation. Those prerequisites now precede the application in
the proof-led branch. A motivation-first route can retain the example first but
must say which results it is taking as given. Do not sort by numeric ID alone.

**Topology's specialist routes should separate their jobs.** The existing
symplectic route places gauge/Chern–Weil `022000` and sheaf/Čech `022200`
between Hamiltonian geometry and Morse/holomorphic-curve/Floer foundations.
Those are useful subjects, but a more focused symplectic path is
`021100 → 023000 → 025100 → 025600 → 032000 → 036100`, after manifolds,
forms, homology, bundles/characteristic classes, and the necessary analytic
preparation. Bundle/gauge/index
work can use `022000 → 030100 → 030600 → 034100 → 039000` with Hodge,
elliptic, K-theory, and index background linked explicitly. Keep `026000`
available as a holonomy/prequantization connection rather than treating all
gauge theory as a prerequisite for first symplectic geometry.

For a proof-led index route, review putting `020000` (Hodge and elliptic
operators) and the elliptic-index portions of `023000` ahead of the index
pushforward portions already consolidated inside `018000`. Moving all of
`018000` later also moves its introductory characteristic-class material.
This is a genuine mixed-unit issue: document the assumption or select the
appropriate chapter before deciding to split or rewrite another manuscript.

**A visual finite-dimensional spectral path is already supported by the
presentation index.** The following proposed cross-presentation sequence
places every selected lesson's declared `requires` earlier in the sequence:

`g1:prereq-basics → g1:prereq-projections → g1:prereq-singular-norms →
g1:operators-minmax → g1:prereq-invariant-blocks → g1:operators-rayleigh-ritz →
g1:prereq-matrix-exponential → g1:operators-sylvester →
g1:prereq-complementary-projection → g1:sine-theta-lecture`.

This is a source-backed visual entrance, not a replacement for the full
unbounded/operator-ideal theorem scope. G2's topic collections and G3's paper
sequence remain the deeper destinations. No frozen deck's internal scene
order changes to create such a route.

## What is still missing, and what is only stale planning

The immediate organization work does not require another lecture-writing
campaign. Much of the old backlog has been delivered and then consolidated.
Analysis's proposed manifolds/forms/Stokes/connection material now exists in
the topology and multivariable packs; its proposed commutative algebra and
schemes material exists in abstract algebra. Numerical eigenproblems, stiff
time stepping, intervals, finite-element certificates, and preconditioning
also have current manuscripts. The four bridge lectures in
`docs/planning/bridge-lectures.md` are implemented G1 lessons. Older part IDs
absorbed into combined manuscripts are not missing lessons.

Actual boundaries worth retaining in route descriptions are:

- Probability `013000`–`015000` remain proposals in the foundations plan:
  decision theory/distribution shift, formal-probability exercises, and
  Brownian/continuous-time modeling. The delivered core contains `001000`–
  `012000` only.
- Category theory `036000`–`039000` remain proposed in the ninth-arc plan:
  Dold–Kan, derived functors/spectral sequences, stable infinity-categories,
  and cotangent complexes. Related examples elsewhere do not automatically
  complete that planned course.
- Number theory's latest continuation now covers general finite local
  extensions and Hilbert symbols. Its current backlog still distinguishes
  Hilbert reciprocity from a proof of Hasse–Minkowski and identifies local
  classification/two-adic and global-patching work still needed.
- Advanced PDE claims retain explicit scope boundaries. The analysis backlog
  does not claim large-data global scattering, critical-regularity estimates,
  general rough-boundary regularity, or uniqueness for all rough nonlinear
  equations. Introductory ODE completion is not preparation for every such
  theorem.
- Specialist Floer/contact work needs its own analytic and orientation/index
  hypotheses. A topical overview, elementary forms course, or a finite example
  does not by itself supply the complete background of a research theory.

## Dependency evidence and handoff

`lectures/index.yaml` supplies presentation teaching preparation. The curated
`curriculum/relationships.json` and `proof-relationships.json` distinguish
teaching requirements, recommendations, proof use, and historical material.
G2 contraction must continue to preserve absorbed component IDs as evidence;
an internal relation inside a combined lecture is not an inter-lecture cycle.
G4 planned nodes must remain visibly unavailable.

The four new guide paths contain no G2/G3 nodes and no endpoints of an authored
`hard_depends_on` relation in the current curated relationship file. Their
background statements are editorial source review, not an assertion that an
absent edge proves independence. Most non-G2 subject packs do not yet have a
complete, authored lecture-level prerequisite map. Broad preparation-collection
links are useful suggestions, but should not be promoted into hard requirements.
Do not union listening-order, soft recommendation, proof-use, and historical
edges into a single topological sort; those relations answer different questions.

For the guide, verify that its four chapter sequences contain unique installed
IDs, that every linked collection exists when its source pack is installed,
that all 17 mathematics namespaces have a family entrance, and that an absent
optional pack remains an honest unavailable reference. Verify G1's proposed
visual sequence against the actual index requirements before adding it as a
fifth path. No new prerequisites should be generated from path adjacency.

Verification completed for this handoff: all 17 mathematics source packs and
the new guide pass strict `repository_track` loading; G1 also loads through its
presentation adapter. Every compiled guide/number-theory chapter, preparation,
related-course, and family reference resolves in that source inventory, with no
duplicate lecture inside a route. All 54 number-theory lectures occur in curated
routes, and its archive exactly matches the untouched track order. The proposed
ten-lecture G1 sequence satisfies each selected lesson's declared requirements.
Source-byte hashes and extracted speech identities for the 412 indexed audio
manuscripts remained unchanged during integration verification. The new work
consists of guide metadata/documentation and number-theory navigation, with no
new narration or prerequisite edges.

Planning sources reviewed: the project vision/history plan; bridge lectures;
the three-foundations and second-foundations plans; listening-route and adult
consolidation notes; category introductory/ninth-arc plans; analysis continuation
and current backlog; numerical foundations/current backlog; topology backlog;
number-theory README/current backlog; and G3's README/coverage plan. Their dated
statuses are evidence of the plan at that time, not the current source inventory.
