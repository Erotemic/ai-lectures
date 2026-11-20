# Formalization map — verified claims versus remaining work

**Snapshot basis:** the `networkx_algo_common_subtree` source archive supplied 2026-11-19, especially `docs/planning/paper_statement_crosswalk.md`, `proofs/PROOF_STATUS.md`, `docs/planning/README.md` and the corresponding `proofs/SubtreeProofs/` directories. **No fresh `lake build` or Rust benchmark is claimed here.** This map is a guide for teaching the supplied source and for choosing future lectures, not a substitute for the repository's maintained proof ledger.

The source crosswalk is authoritative if the two records disagree; older plan paragraphs sometimes retain historical “pending” language even when their opening updates say the proof has since compiled.

## 2004 — ordered contraction and balanced words

**The source paper:** [Lozano & Valiente, *On the Maximum Common Embedded Subtree Problem for Ordered Trees*](https://www.cs.upc.edu/~antoni/subtree.pdf), original manuscript.

| Source obligation | Status in supplied repository | Where to begin reading | Teaching consequence |
| --- | --- | --- | --- |
| Balanced-word encoding and edge counts (Definition 1, Fact 1) | Round trips and an explicit linear encoder cost proved | `Paper2004/OrderedTree.lean`, `BalancedSequence.lean`, `EncodingEquivalence.lean`, `LinearEncoding.lean` | Teach the independent tree and Dyck representations before equating them |
| Definition 2 containment | Literal printed relation formalized but its completeness is refuted; operational matched-pair deletion corresponds to edge contraction | `PaperContainment.lean`, `PrintedContainmentCounterexample.lean`, `ContractionCompleteness.lean` | Preserve the correction and small `001011 → 0011` counterexample |
| Decomposition families D/R/S, Lemmas 1–7 and Theorem 1 | Closure, enumeration and cardinality bounds proved, including actual depth/leaf measures | `Decomposition.lean`, `TreeStateBounds.lean` | Understand which states are counted, not all imaginable contractions |
| Correspondence and Lemma 8 | Operational longest-common-balanced-word/tree optimum and three-way numerical recurrence proved | `OptimalEncoding.lean`, `DynamicProgram.lean` | Prove soundness, completeness and witness assembly separately |
| Theorem 3 runtime | Concrete table-call/state bounds proved; complete structural word comparison/copy, expected-hash and cost-accounting bridge remains open | `MemoizedDynamicProgram.lean`, `Rust/` memo/cost modules; source crosswalk | Never conflate recurrence call count with wall-clock runtime |
| Actual Rust / ordered API | Source-proved Boolean token/indexed/guided reference paths, proof of independent optimum and preserved indices under specified representations; exact rational ordered-isomorphism execution is a separate proved project extension | `Rust/` modules, `RationalOrderedSolver.lean`, `IndexedTokenPositions.lean`, `TokenMaximum.lean` | Explain whether a theorem is about embedding, isomorphism, graph conversion or typed API |

The paper's original leaf measure needs care: the repository proves statements in actual tree depth and actual leaf count rather than silently identifying the paper's printed recurrence with true leaves. The displayed Theorem 3 bound is **expected** under a dictionary model; it is not a blanket runtime theorem for the source Rust implementation.


### Lectures now available for the Lozano–Valiente proof chain

- `005000`: D/R/S, the actual-leaf correction, `decomposition_card_bound` and its underlying finite-set inclusions.
- `006000`: the first-pair structural split, constructive optimum (`paperCommon_correct`), numerical optimum (`paperLcs_optimum`), and tree correspondence.
- `007000`: `memoLcs_tree_operation_bound`, real association-list comparison work, the paper's expected dictionary model, and the still-open source-level cost bridge.

These are mathematical/paper walkthroughs with Lean entry points, **not** yet a complete line-by-line formalization tutorial. The next planned lecture (`008000`) audits the printed containment relation independently.

## 2016 — weighted unordered subtree isomorphism

**The source paper:** [Droschinsky, Kriege & Mutzel, *Faster Algorithms for the Maximum Common Subtree Isomorphism Problem*](https://arxiv.org/pdf/1602.07210v4), pinned v4.

| Source obligation | Status in supplied repository | Where to begin reading | Teaching consequence |
| --- | --- | --- | --- |
| Independent weighted connected isomorphism and finite optima | Proved; root restrictions, valid witnesses and edge/vertex scores explicit | `Droschinsky2016/Specification.lean`, `Witness.lean`, `Rooted.lean` | Begin with feasible mappings and score function, not DP storage |
| Rooted matching recurrence (Eq. 1, Prop. 1) | Proved for whole and descendant problems; executable reference score table/optimum proved | `RootedRecurrence.lean`, `BranchDecomposition.lean`, `BranchAssembly.lean`, `RootedDynamicProgram.lean` | Work through both directions and reconstruction |
| Fixed-left-root structural sufficiency (Lemma 2) | Proved with highest-vertex reasoning | `OrientedRecurrence.lean` and source crosswalk | Make root reduction a named theorem, not a heuristic |
| Rectangular matching (Lemma 5) | Copied-graph reduction, source dual and signed-integer references have substantial proved components; full optimized runtime open | `WeightedMatching/`, `Rust/` matching modules | Separate reference matching, dual certificate, reduction and optimized solver |
| Deletion matching family (Lemma 6) | Reference family, source row/potential invariants and substantial repair/export steps proved; final production family integration and optimized runtime remain open | `WeightedMatching.CopiedAssignmentReduction` and `Rust.SparseDeletion` modules | Explain how related instances can be reused without assuming indexing is trivial |
| Optimized Theorem 4, total work Theorem 7; reduction Theorem 8; enumeration Theorem 9 | Open in the crosswalk | `paper_statement_crosswalk.md`, production algorithm docs | Derive the theoretical target and identify missing end-to-end theorems |

The pinned v4 unrestricted-weight target is

\[
O\left(|G||H|\left(\min(\Delta_G,\Delta_H)+\log\max(\Delta_G,\Delta_H)\right)\right).
\]

The shorter `O(n²Δ)` expression is useful in a symmetric presentation, but the degrees and logarithmic term should not be erased when teaching the precise statement.

## 2018 — topological embedding and distance penalties

**The source paper:** [Droschinsky, Kriege & Mutzel, *Largest Weight Common Subtree Embeddings with Distance Penalties*](https://arxiv.org/pdf/1805.00821v1), pinned v1.

| Source obligation | Status in supplied repository | Where to begin reading | Teaching consequence |
| --- | --- | --- | --- |
| Path-embedding specifications (Definitions 1–2) | Independent common-skeleton correspondence proved in unrooted and rooted variants | `Droschinsky2018/Specification.lean`, `Witness.lean`, `PointedWitness.lean` | Make path images, disjointness and mapped vertices explicit |
| Weight and penalty (Definition 4) | Direct-edge reward versus skipped-path penalty, finite optima and score properties proved | `GraftScore.lean`, `ScoreDecomposition.lean`, `BranchReward.lean` | Reproduce the precise path-length test, not a generic edit-distance score |
| Mapped/skipped recurrence (Lemma 5) | Two-state recurrence and rooted reference objective/score table proved against independent witnesses | `BoundaryStates.lean`, `SkippedRecurrence.lean`, `MappedAssembly.lean`, `RootedDynamicProgram.lean` | Teach why two states are necessary and how matching assembles branches |
| Rooted Theorem 6 and bounded-integer Lemma 8 | Complexity/scaling reduction open; cited prior matching bounds not independently new paper theorems | Paper crosswalk | Separate functional recurrence from resource and imported algorithm guarantees |
| Unrooted structural split, Lemmas 9–11 | Lean proofs open; production Rust implements tested retained/skipped structural cases | `OverallOptima.lean`, Rust implementation and independent small-input oracles | Map exact high-vertex/join cases before source refinement |
| Matching reuse Lemmas 12–14 and Theorem 15 | Lean proofs and optimized complexity open; production schedule, view IDs and matching families implemented/tested | Paper crosswalk, `docs/planning/droschinsky_2016_2018_verified_rust_lean.md` | Formalize acyclic evaluation order and full cost composition |
| Rust/Python refinement | Actual optimized source/path reconstruction and numeric bridge open | Source and public API docs | Distinguish nonempty theoretical optima from optional empty-result APIs and bounded `f64` execution |

Definition 4's path score for representing paths `P₁,P₂` of lengths `k,l` is

\[
\omega_p(P_1,P_2)=
\begin{cases}
\omega_E(e_1,e_2), & k=l=1,\\
-p(k+l-2), & \text{otherwise}.
\end{cases}
\]

Every matched common vertex additionally contributes its vertex-pair score. In the non-direct case, do **not** add the direct-edge reward on top of the skipped-vertex penalty. The paper's rooted and unrooted real-weight time target is `O(|T||T'|Δ)` with `Δ = min(Δ(T), Δ(T'))` under its stated model; the bounded-integer rooted improvement has separate hypotheses and an imported scaling-solver space qualification.

## Shared source-refinement vocabulary

A future lecture should use the following vocabulary consistently:

1. **Independent specification:** feasible objects and maximum score defined without reference to the algorithm.
2. **Recurrence correctness:** a dynamic program returns the independent optimum, often via exhaustive decomposition and constructive assembly.
3. **Witness/readback:** computed choices reconstruct a feasible object with the claimed original input identities and exact score.
4. **Source refinement:** the actual Rust function (possibly translated through Charon/Aeneas) implements the proved algorithm with a defined numeric/error/memory contract.
5. **API refinement:** Python/NetworkX input conversion, typed node identities, returned graph objects and backend dispatch preserve that contract.
6. **Resource theorem:** a stated cost model bounds actual work, allocation or space; mathematical state-count theorems and empirical benchmarks are not interchangeable with it.

**Why these categories need separate lectures:** A machine-checked `RootedDP.solve_correct` theorem does not by itself prove that a fast production solver implements its mathematical table, and a source-level correctness theorem does not by itself prove the paper's optimized asymptotic bound. Likewise, a compiled source proof may cover exact integers or rationals without claiming IEEE-754 numerical equivalence.

## Good next proof-reading exercises

- For 2004, open `ContractionCompleteness.lean`, explain both directions of ordered-tree versus Dyck-word contraction, then find the `PrintedContainmentCounterexample.lean` statement whose converse fails.
- For 2016, trace `rooted_matching_recurrence` through branch decomposition and assembly before inspecting the matching solver.
- For 2018, trace `skipped_recurrence_two_state` and `RootedDP.solve_correct`; locate the exact hypothesis that distinguishes mapped and skipped states and follow the `Definition 4` scoring branch.

These exercises refer to **existing** files and declarations in the supplied snapshot. When later sessions aim to teach the current state or draft completion work, reopen the latest source rather than relying on this dated map.
