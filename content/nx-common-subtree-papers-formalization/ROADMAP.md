# Roadmap — from foundations to paper proof to source verification

This is a **curriculum plan**, not an indexed list of written lectures. IDs `000000`–`028000` are complete in the current pack. Later IDs are proposed, will be written as full narration with exact companion mathematics, and may be combined or expanded when the mathematics calls for it. Lecture order is a suggested path, not a fixed dependency graph.

The teaching goal is to be able to do four things for each paper: (1) define valid solutions independently of the algorithm; (2) derive and understand its central recurrence and claimed complexity; (3) find and read the corresponding Lean theorems and source obligations; and (4) identify the next useful correctness or cost proof without conflating optimized Rust, reference Rust, formal mathematics and Python API behavior.

## A. Shared foundations — written now

| ID | Manuscript | Main result for the listener |
| --- | --- | --- |
| `000000` | Three Meanings of a Common Subtree | Understand strict isomorphism, edge contraction and topological embedding as distinct problems |
| `001000` | Trees, Roots, Order, and the Shape of a Witness | Explain roots, ordered children, edge views, connected selection and valid witnesses |
| `002000` | Tree Dynamic Programming as a Proof | Derive a rooted child-matching recurrence with both proof directions and explicit states |
| `003000` | Balanced Words and Ordered-Tree Contractions | Encode ordered trees, delete matched pairs, apply first-return decomposition |
| `004000` | Matching Child Branches and Reusing the Answer | Understand partial weighted matching, assignment certificates and one-vertex deletion reuse |

## B. Lozano–Valiente 2004: ordered edge contractions

**Suggested route:** `000000`, `001000`, `002000`, `003000`, then the following.

| ID and status | Lecture focus | Original paper | Lean/proof landmark |
| --- | --- | --- | --- |
| **`005000` — written** | The D, R and S state families and why there are few of them | Definitions 3–4, Lemmas 1–7, Theorem 1 | `Paper2004/Decomposition.lean`, `TreeStateBounds.lean` |
| **`006000` — written** | Longest common balanced sequence: derive all three recurrence branches, with witnesses | Definitions 2, 5, Theorem 2, Lemma 8 | `Paper2004/DynamicProgram.lean`, `OptimalEncoding.lean` |
| **`007000` — written** | The published running time, dictionary assumptions and the difference between state counts and actual costs | Theorem 3 | `Paper2004/MemoizedDynamicProgram.lean`, `Rust/*` memo/cost theorems, crosswalk |
| **`008000` — written** | Printed Definition 2 versus independent edge contraction: a complete specification audit | Definitions 2, 5 and Theorem 2 | `PaperContainment.lean`, `PrintedContainmentCounterexample.lean`, `ContractionCompleteness.lean` |
| **`009000` — written** | Reading the proved ordered pipeline: operational witnesses, balanced tokens, indexed reconstruction and source refinement | Paper interpreted operationally; project extension | `Paper2004/TokenEncoding.lean`, `TokenMaximum.lean`, `Rust/` indexed/guided modules |

**Milestone:** The listener can reproduce the proof idea behind Lemma 8 and Theorem 1, read a representative Lean statement for each, explain the printed containment counterexample, and identify precisely which Theorem 3 cost assumptions are still missing for an actual solver.

## C. Droschinsky–Kriege–Mutzel 2016: weighted strict isomorphism

**Suggested route:** `000000`, `001000`, `002000`, `004000`, then the following.

| ID and status | Lecture focus | Original paper | Lean/proof landmark |
| --- | --- | --- | --- |
| **`010000` — written** | Independent weighted common-tree isomorphism, negative weights and objective conventions | Section 2 | `Droschinsky2016/Specification.lean`, `Witness.lean` |
| **`011000` — written** | Rooted recurrence and why fixing one root suffices | Proposition 1 / Eq. (1), Lemma 2 | `RootedRecurrence.lean`, `OrientedRecurrence.lean`, `RootedDynamicProgram.lean` |
| **`012000` — written** | Exact copied-graph reduction, assignment duality, starting deficit and rectangular cost | Lemma 5 | `Shared/CopiedAssignmentReduction.lean`, `CopiedMatchingInitialization.lean`, `CopiedMatchingDuality.lean` |
| **`013000` — written** | Unmatched reuse, one-pair deletion deficit, dual-tight repair, family cost and Rust proof boundary | Lemma 6, Algorithm 2 | `Shared/MatchingDeletion.lean`, `CopiedMatchingDeletion.lean`, `Rust/SparseDeletionEntrypoint.lean` |
| **`014000` — written** | Algorithm 1, oriented right views, one-deletion families, degree-sum factorization, complete runtime argument | Proposition 3; Theorems 7 and 4 | `Rooted.lean`, `OrientedRecurrence.lean`, `Complexity/MatchingFamilies.lean`; published cost proof |
| **`015000` — written** | Exactly what Lean and source Rust prove; production dummy-column matching, representation and resource theorem interfaces | Paper statement ledger, production graph backend | `RootedDynamicProgram.lean`, `Rust/SparseDeletionEntrypoint.lean`, `paper_statement_crosswalk.md`, production `tree.rs`/`matching.rs` |

**Milestone:** Explain the exact 2016 asymmetric unrestricted-weight target `O(|G||H|(min(Δ_G,Δ_H)+log(max(Δ_G,Δ_H))))`, including why a source-correct rooted reference solver does not yet prove the optimized bound.

## D. Droschinsky–Kriege–Mutzel 2018: topological paths and penalties

**Suggested route:** `000000`, `001000`, `002000`, `004000`, then the following. The 2016 matching lectures are useful supporting material, but the 2016 feasible-object definition does not replace the 2018 one.

| ID and status | Lecture focus | Original paper | Lean/proof landmark |
| --- | --- | --- | --- |
| **`016000` — written** | Skeleton trees, topological embeddings and internally disjoint realized paths | Definitions 1–2 | `Droschinsky2018/Specification.lean`, `Witness.lean`, `PointedWitness.lean` |
| **`017000` — written** | Exact scoring: direct edge reward, skipped-path penalties, impossible matches and negative weights | Definition 4 | `GraftScore.lean`, `ScoreDecomposition.lean`, `BranchReward.lean` |
| **`018000` — written** | Why the DP needs mapped and skipped states; deriving Lemma 5 | Lemma 5 | `BoundaryStates.lean`, `SkippedRecurrence.lean`, `RootedDynamicProgram.lean` |
| **`019000` — written** | The unrooted structural split, highest mapped vertices, joins and root choices | Lemmas 9–11 | `OverallOptima.lean`, structural source crosswalk (open frontier) |
| **`020000` — written** | Right-view maxima, matching-deletion families, evaluation order and whole-algorithm cost | Lemmas 12–14 and Theorem 15; rooted Theorem 6 | `Complexity/MatchingFamilies.lean` (partial math bounds), production `tree.rs`/`matching.rs`, open source theorems |
| **`021000` — written** | Source-aware 2018 verification guide: independent specification, proven recurrence and reference solver, optimized structural/cost/source/numeric/API obligations | The 2018 paper as a whole | `OverallOptima.lean`, `RootedDynamicProgram.lean`, source Rust, `paper_statement_crosswalk.md` |

**Milestone:** Trace a common edge through two paths, compute exact path rewards/penalties, derive Lemma 5, reconstruct the M₁/M₂ split, recover Theorem 15 from matching-family and scheduling bounds, and distinguish published cost arguments from Lean/source/API proofs in the pinned repository.

## E. Shared formalization and research methods

These lectures can be listened to after one paper or in parallel with the paper-specific lectures.

| Proposed ID | Focus | Use in research |
| --- | --- | --- |
| **`022000` — written** | Read `Valid`, `IsMaximum`, `exists_maximum`, `rooted_matching_recurrence` and the 2018 `step_correct` / `solve_correct` chain | Separate independent specifications, theorem hypotheses, existence, recurrence and executable reference correctness |
| **`023000` — written** | Reverse Dyck encoding, one-step soundness and completeness, `embeds_iff_dyckEmbeds`, printed-containment discrepancy and original positions | Understand representation bijection versus operational biconditional and identity-preserving refinement |
| **`024000` — written** | Read the complete 2018 reference table proof: independent mapped/skipped witnesses, conditional step, full rank, synchronous rounds and global readout | Reuse the right invariant and well-founded induction when proving new table evaluators |
| **`025000` — written** | Follow actual signed-integer matching Rust through pinned Charon/Aeneas, `ResultSpec`, matrix validation, assignment decoding, indices and totality | Understand a compiled source-level functional theorem and its exact proof boundaries |
| **`026000` — written** | Lean complexity: request and completion identities, nonuniform memo work, list vs dense cache charging, matching-family pair storage, tree degree sums and concrete Rust resource gaps | Interpret exactly what source and abstract work bounds establish |
| **`027000` — written** | One production matching-deletion family: lazy reuse, rectangular Hungarian invariants, both repair orientations, source-level boundaries and proposed cost/space certificates | Follow the actual `matching.rs` code and design separately dischargeable correctness and work obligations |
| **`028000` — written** | Exact-rational verified ordered backend versus tested f64 unordered APIs; NetworkX node identity, callback tables, PyO3/ABI3, rooted/empty/error contracts and witness paths | Distinguish mathematical correctness, compiled Lean execution, indexed Rust results, Python reconstruction and installed-wheel assurances; design separable API proof interfaces |
| `029000` | A proof-completion workshop with three worked open obligations and viable theorem interfaces | Convert the crosswalk into a research plan, revisiting actual repository state |

### Reusable lectures already in other tracks

Instead of duplicating large independent courses, recommend:

- `mathematical-proof:009000` for sets, functions and mathematical induction.
- `algorithms-computability-complexity:011000` for introductory dynamic programming; `017000` for amortized data structures.
- `discrete-mathematics:005000` for matchings and flow certificates.
- `logic-types:004000` through `008000` for inductive structures, equality, rewriting and proof assistants.

The paper-specific lectures will still explain whatever piece of these prerequisites is needed at the point of use. Linking a broader recording does not license skipping a definition required for the paper.

## Next sensible authoring session

The Lozano–Valiente branch is written through `009000`, including the source-notation counterexample and formalization reading route. The 2016 branch is written through `015000`: mathematical definitions, recurrence, matching optimization, complete paper complexity argument, and a source-aware list of unresolved verification interfaces. The 2018 branch is written through `021000`: topological embeddings, path scoring, mapped/skipped two-state recurrence, fixed-first-root structural reduction, matching-family reuse, the published time/space analysis, and a detailed formalization status and source-refinement guide. Lemmas 9–14 and Theorem 15 remain open formalization frontiers in the pinned repository, despite the mathematical explanation in these lectures. The shared Lean, Rust and Python reading sequence is written through `028000`: mathematical specifications, the tree-to-Dyck equivalence, the 2018 reference-table proof, signed-integer Rust matching source verification, existing Lean work/space-count theorems, a source-oriented matching-family refinement case study, and the distinct Python/NetworkX API proof boundaries for compiled exact-rational Lean versus tested floating-point Rust. Next proposed is `029000`, a hands-on proof-completion workshop that prioritizes explicit Lean theorem interfaces and source invariants. The optimized graph backend and Python API remain open. The 2004 and 2016 source-level runtime and Python/NetworkX refinement frontiers remain open research work, not claims of completion.

Before writing *formalization status* manuscripts in any later session, inspect the **current** source repository. This roadmap records the November 19, 2026 upload rather than assuming proof status remains fixed.
