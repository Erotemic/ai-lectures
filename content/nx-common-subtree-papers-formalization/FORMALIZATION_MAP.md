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

- `008000`: the separate `PrintedContains` grammar, its `001011 → 0011` counterexample, the differing optima, and the independently proved tree/Dyck equivalence.
- `009000`: a reading path through `OrderedTree`, `ContractionCompleteness`, `OptimalEncoding`, `DynamicProgram`, `CanonicalIndexedWord`, `TokenMaximum` and source-proved `Rust` reference endpoints. Includes exact original pair/token coordinate examples and statements of unresolved optimized/API/cost boundaries.

The 2004 branch now has paper-centered derivations and a formalization reading guide. It does **not** claim to teach every Lean tactic or close the source-verified optimized running-time and Python API gaps. The paper’s printed relation and independent operational objective remain separate.

## 2016 — weighted unordered subtree isomorphism

**The source paper:** [Droschinsky, Kriege & Mutzel, *Faster Algorithms for the Maximum Common Subtree Isomorphism Problem*](https://arxiv.org/pdf/1602.07210v4), pinned v4.

| Source obligation | Status in supplied repository | Where to begin reading | Teaching consequence |
| --- | --- | --- | --- |
| Independent weighted connected isomorphism and finite optima | Proved; root restrictions, valid witnesses and edge/vertex scores explicit | `Droschinsky2016/Specification.lean`, `Witness.lean`, `Rooted.lean` | Begin with feasible mappings and score function, not DP storage |
| Rooted matching recurrence (Eq. 1, Prop. 1) | Proved for whole and descendant problems; executable reference score table/optimum proved | `RootedRecurrence.lean`, `BranchDecomposition.lean`, `BranchAssembly.lean`, `RootedDynamicProgram.lean` | Work through both directions and reconstruction |
| Fixed-left-root structural sufficiency (Lemma 2) | Proved with highest-vertex reasoning | `Rooted.lean`, `OrientedRecurrence.lean` and source crosswalk | Make root reduction a named theorem, not a heuristic |
| Rectangular matching (Lemma 5) | Exact copied-graph optimum reduction, signed-optional edges, initial dual feasibility, tight identity pairs and smaller-side deficit proved; optimized augmentation/runtime open | `Shared/CopiedAssignmentReduction.lean`, `CopiedMatchingInitialization.lean`, `CopiedMatchingDuality.lean` | Distinguish mathematical doubled optimum, dual certificate and the paper cost model |
| Deletion matching family (Lemma 6) | Unmatched reuse and affected-count bound proved; matched one-pair deficit, feasible/tight repair and original-index decoding proved; exact integer reference family and sparse repair API source theorems proved under stated contracts; production graph integration/runtime still open | `Shared/MatchingDeletion.lean`, `CopiedMatchingDeletion.lean`, `CopiedMatchingRepair.lean`, `Rust/MatchingDeletionEntrypoint.lean`, `Rust/SparseDeletionEntrypoint.lean` | Keep one mathematical augmentation distinct from the work to find it and from actual-source cost |
| Optimized Theorem 4, total work Theorem 7 | Open in the crosswalk as source formalization/runtime theorems; the publication proves them on its matching cost model | `paper_statement_crosswalk.md`, `Complexity/MatchingFamilies.lean`, production `tree.rs`/`matching.rs` | Derive the degree-sum argument and isolate cost/refinement gaps without treating a pair-cell storage theorem as a time bound |
| Assignment-hardness reduction (Proposition 8) and output-sensitive enumeration (Theorem 9) | Open in the crosswalk | `paper_statement_crosswalk.md`, paper Sections 5–6 | Optional follow-ups distinct from the core Theorems 4 and 7 |

The pinned v4 unrestricted-weight target is

\[
O\left(|G||H|\left(\min(\Delta_G,\Delta_H)+\log\max(\Delta_G,\Delta_H)\right)\right).
\]

The shorter `O(n²Δ)` expression is useful in a symmetric presentation, but the degrees and logarithmic term should not be erased when teaching the precise statement.

### Lectures now available for the 2016 mathematical core

- `010000`: Source Section 2, exact nonempty connected induced-isomorphism witnesses, finite score and optimum, singleton edge cases, `WithBot` negative infinity, and the separate empty-allowed API convention. Reading map: `Specification.lean`, `Witness.lean`, `Rooted.lean`.
- `011000`: Section 3 Equation (1) and Lemma 2; matching table with explicit signed node/edge scores; decomposition via `score_decomposition`; converse via `BranchFamily.assemble_valid` and `score_assemble`; `RootedDP.solve_correct` and `unrootedOptimum_correct`. These are mathematical and exhaustive-reference proofs, **not** an optimized Rust or full runtime theorem.
- `012000`: Section 4 Lemma 5, allowed copied/identity edges, `assignmentWeight_decode`, `extend_allowed`, `dominates_allowed_decodes`, initial row maxima, feasible/tight dual conditions and initial deficit; proof of the paper bound from its stated per-augmentation model.
- `013000`: Section 4 Lemma 6 and Algorithm 2, exact original-index deletion, `IsMaximum.deleteRight`, `deletion_repair_card_bound`, matched copied-graph deficit, dual-tight reuse and single-cycle repair; reference Rust family `max_weight_matching_deletions_total_spec` and `repair_deleted_sparse_vertex_spec`.
- `014000`: Algorithm 1 full oriented-state schedule and the step-by-step summation behind Theorems 7 and 4; the count `|G|(3|H|-2)` and factorization of rooted child sums and right vertex degrees. `tree_degree_sum` and `tree_family_pairs_le` are explicitly identified as mathematical **storage** landmarks, not complete runtime proofs.
- `015000`: independent specification → oriented recurrence → executable reference table → checked exact-integer reference/sparse repair → production floating-point matching and choice-arena frontend. Explains the proved sparse repair preconditions, copied-graph versus transposed/dummy-column representation, source/runtime and Python contracts, and a compositional research strategy.

The fixed-root proof itself is in `Droschinsky2016/Rooted.lean` (`Valid.fixed_root_representative`, `fixedRootValue_eq_unrootedValue`); `OrientedRecurrence.lean` handles the descendant-state recurrence while keeping ambient roots fixed.

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

### Lectures now available for the 2018 paper

- `016000`: Definitions 1–2, a common-tree fork with two valid path realizations, a hidden branch-point counterexample, exact `Valid` skeleton requirements, `Valid.commonTree`, `valid_iff_source_embeddings`, and rooted/root-to-root representation bridges. Both representation directions are mathematical theorems; neither asserts optimized-source refinement.
- `017000`: Definition 4 with edge rewards only when **both** realized paths are direct, skipped interior counts for all other path pairs, a numerical comparison of three explicitly feasible mappings, negative/infinite/zero-penalty cases, and the formal `pathScore` / `one_two_path_score` / `maximum_score_antitone` results. The worked example is not claimed to cover all possible embeddings because unrelated pair weights are not specified.

The supplied proof snapshot supports independent nonempty finite optimum, exact source-to-skeleton and score correspondences, both halves of the mapped/skipped recurrence, and executable reference score correctness. Lecture `018000` derives the actual two-state Bellman equalities against independent boundary witnesses and reads `skipped_recurrence_two_state`, `mapped_recurrence` and `RootedDP.solve_correct`. Lecture `019000` presents the paper's Lemmas 9–11 and distinguishes the still-open fixed-first-root M1/M2 structural formalization from the **already proved all-root-pairs baseline** (`unrootedValue_eq_max_rerooted_mapped`, `RootedDP.unrootedOptimum_correct`). The optimized source graph algorithm, its complete output-path reconstruction proof, `f64` refinement, Python boundary and paper time/space bounds remain separate research obligations.

### New 2018 proof-reading guide (`018000`–`019000`)

- **Independent state:** `BoundaryStates.StateValid`, `stateScore`, `mappedValue`, `skippedValue` represent actual nonempty common-tree witnesses, not recurrence outputs. Boundary skip distances are charged once per physical descent.
- **Lemma 5, skipped half:** `StateValid.skipped_cover`, `extend_left` / `extend_right`, and `stateScore_step_left` / `step_right` yield `SkippedRecurrence.skipped_recurrence_two_state` for empty and nonempty child families, including infinite penalties.
- **Lemma 5, mapped half:** `BranchOptimum.matchingBranchValue_attained`, `MatchingAssembly.familyOfMatching_score`, `MappedDecomposition.source_score_upper`, and `mapped_recurrence` prove the two directions of optimality. Edge rewards require both realized paths to be direct. `RootedDP.solve_correct` supplies an executable but exhaustive score table; it is not production Rust refinement.
- **Lemmas 9–11, paper only:** An arbitrarily fixed first root can miss an unrooted optimum when the highest realized vertex is skipped along a crossing path. The paper adds a cardinality-two matching of two distinct child branches across a cut edge in the second tree, with one central penalty. Its top-two exchange argument makes the added M2 maximization linear in the rooted child-family size. These specific fixed-first-root structural and cost proofs are **open** in the uploaded Lean snapshot.
- **Certified baseline for contrast:** `OverallOptima.unrootedValue_eq_max_rerooted_mapped` and `RootedDP.unrootedOptimum_correct` prove correctness of evaluating every input root pair, under the stated finite vertex and true child-list hypotheses. They do not imply the optimized Lemma 10/11 representation or runtime.

### New 2018 proof-reading guide (`020000`–`021000`)

- **`020000`, Lemma 12:** A full-neighborhood maximum and every one-neighbor exclusion maximum can be obtained from the best two candidates with distinct right-neighbor origins. Conditional on the necessary state values being ready, the aggregate scalar work is `O(|T||T'|)`.
- **`020000`, Lemmas 13–14:** Related matching graphs differ by removing one right neighbor. The all-deletions algorithm has `O(s^4+s²t)` cost for `s<=t` (Lemma 14). Combining it with the earlier 2016 family method at the `s >= log t` threshold yields one-family cost `O(s²t)`, not that cost multiplied by the number of deletions. Summing degree products yields `O(|T||T'| min(Delta(T),Delta(T')))`. These are paper results; their optimized Rust complexity proofs remain open.
- **`020000`, Theorem 15:** The paper's main/sub-instance evaluation schedule discharges the conditional ordering hypothesis and gives unrooted time `O(|T||T'| Delta)` and space `O(|T||T'|)`. `Complexity/MatchingFamilies.lean` is a partial mathematical counting result, not full Rust memory evidence.
- **`021000`, source reading:** `RootedDP.unrootedOptimum_correct` proves an exhaustive all-roots optimum, **not** the optimized fixed-left-root M1/M2 theorem. The production `embedding_matching_family`, `compute_embeddings`, `max_weight_bipartite_matching_with_right_deletions`, skipped-highest join, and Python node/path conversions require separate source, numeric and resource refinement.
- **`021000`, proof interfaces:** Proposed high-level obligations are highest-realized-vertex soundness/completeness, right-view decoding, two-best distinct-origin exclusions, matching-family correctness, a two-phase table invariant and concrete resource accounting. The interfaces are suggestions, not implemented Lean declaration names.

## Shared source-refinement vocabulary

A future lecture should use the following vocabulary consistently:

1. **Independent specification:** feasible objects and maximum score defined without reference to the algorithm.
2. **Recurrence correctness:** a dynamic program returns the independent optimum, often via exhaustive decomposition and constructive assembly.
3. **Witness/readback:** computed choices reconstruct a feasible object with the claimed original input identities and exact score.
4. **Source refinement:** the actual Rust function (possibly translated through Charon/Aeneas) implements the proved algorithm with a defined numeric/error/memory contract.
5. **API refinement:** Python/NetworkX input conversion, typed node identities, returned graph objects and backend dispatch preserve that contract.
6. **Resource theorem:** a stated cost model bounds actual work, allocation or space; mathematical state-count theorems and empirical benchmarks are not interchangeable with it.

**Why these categories need separate lectures:** A machine-checked `RootedDP.solve_correct` theorem does not by itself prove that a fast production solver implements its mathematical table, and a source-level correctness theorem does not by itself prove the paper's optimized asymptotic bound. Likewise, a compiled source proof may cover exact integers or rationals without claiming IEEE-754 numerical equivalence.

## Shared formalization reading — new lectures `022000`–`023000`

- **`022000` — theorem statement versus algorithm:** `Droschinsky2016/Specification.lean` (`Valid`, `IsMaximum`, `singleton_valid`, `exists_maximum`), `RootedRecurrence.lean` (`rooted_matching_recurrence`, two inequalities), and `Droschinsky2018/RootedDynamicProgram.lean` (`step_correct`, `evaluate_correct`, `solve_correct`). The existence theorem concerns the independent finite witness family; the table theorem has explicit complete-enumeration and child-representation hypotheses. Neither asserts correctness of the optimized production algorithm.
- **`023000` — reversible representation versus semantic contraction:** `Paper2004/EncodingEquivalence.lean` (`orderedTreeEquivDyck` and both inverse laws), `ContractionSoundness.lean` (`contractStep_encodeDyck`, `embeds_encodeDyck`), and `ContractionCompleteness.lean` (`dyckContractStep_decodeDyck`, `dyckEmbeds_decodeDyck`, `embeds_iff_dyckEmbeds`). `PrintedContainmentCounterexample.lean` proves the literal printed relation is strictly weaker on the `001011 → 0011` example. `TokenEncoding.positionPairs_bounds`, `IndexedWord.Retains.tokenIndices_sublist` and `TokenReading.retained_readsTokens` are separate original-identity obligations, not consequences of a mere shape equivalence.

These recordings explain existing, pinned source proofs and their hypotheses. They do not add new Lean declarations or close source-level runtime/resource obligations.

## Shared formalization continuation — lectures `024000`–`025000`

- **`024000` — local recurrence to verified finite-table evaluator:** `Droschinsky2018/BoundaryStates.lean` and `SkippedRecurrence.lean` give independent state values; `MappedDecomposition.lean` and `MatchingAssembly.lean` prove the mapped identity. `RootedDynamicProgram.lean` defines executable `step`, `evaluate`, `solve` and proves `step_correct`, `evaluate_correct`, `solve_correct`, `rootedOptimum_correct`, and `unrootedOptimum_correct` against `sourceState`. `Shared/RootedEvaluationOrder.lean` supplies `Depends`, `rank_decreases`, `rank_lt_size`; `Shared/FiniteTable.lean` proves generic `rounds_correct`. The proof uses complete vertex lists, exact child-list relations, the exhaustive matching oracle and sufficient synchronous rounds. No optimized unrooted schedule or source-level complexity bound follows.
- **`025000` — actual Rust matching source theorem:** `dev/regenerate_rust_lean.sh` pins Charon/Aeneas and checks `Rust/Generated/VerifiedAssignmentCore.lean`. `Rust/MatchingEntrypoint.lean` proves `max_weight_partial_matching_total_spec` / `max_weight_partial_matching_spec` for a rectangular `Option I64` matrix under dimension limits, or its documented shape/size rejection. `Rust/MatchingSolveBuiltMatrix.lean` defines `CorrectPartial` with indexed-pair correctness, exact weight and independent optimality. `Rust/MatchingValidation.lean`, `MatchingDecoding.lean`, and the assignment bridge establish the underlying loop/data-representation steps. The theorem does not cover optimized 2016/2018 tree solver integration, production `f64` scores, path-choice reconstruction, Python/NetworkX conversion or global runtime cost. The 2004 indexed public Rust path has a *different* theorem in `Rust/IndexedOrderedEntrypoint.lean`.

These lectures explain the theorem chain present in the pinned archive; they do not modify its formal proofs or establish additional runtime claims.

## Formalizing complexity — lecture `026000`

- **Generic memo work is already proved in an interpreter model.** `Complexity/Memo/Bounds.lean` (`roots_request_identity`, `roots_envelope`) separates actual lookup requests from distinct new completions, including arbitrary sound warm caches. `Complexity/Memo/Work.lean` (`roots_weighted_work_envelope`, `roots_weighted_work_wp`) derives an explicit weighted whole-run bound using an initially missing finite dependency-closed envelope and primitive cache work contracts. This is a proof of `Event.totalWork`, not physical CPU cycles or an actual optimized Rust loop.
- **Representation-specific work has checked instantiations.** `Complexity/Memo/RepresentationWork.lean` supplies list and direct/product-array primitive work models; `Complexity/EditDistance/Work.lean` proves whole-run abstract costs for both with cache setup and nonuniform boundary charges. `Complexity/Paper2004/MemoWork.lean` (`cold_list_work`) specializes the model to a cold ordered-tree memo evaluator. That file explicitly excludes structural word/key construction, witness materialization and source execution from its declared work units. `Paper2004/TreeStateBounds.lean` proves a separate decomposition-cardinality theorem.
- **Pair-cell space is mathematical, not source allocation.** `Complexity/MatchingFamilies.lean` proves `storedPairs_le_product`, `family_sum_le`, `tree_degree_sum`, and `tree_family_pairs_le`, giving an `8*(n-1)*(m-1)` bound on tagged retained matching pairs across feasible tree-indexed base/deletion families. It does not include Rust vector capacity, headers, temporary matrices, caches, output storage, or a peak-live allocation theorem.
- **Source resources are further along in the ordered reference branch, but not closed.** `Rust/SourceResourceCanonical.lean`, `Rust/SourceHeapResources.lean`, and the `proofs/PROOF_STATUS.md` snapshot describe addressed-source work/ownership models and proved concrete evaluator/public-core fragments. They explicitly leave complete production resource/representation/global time-space closure open. The 2016 and 2018 optimized backends additionally need source representation and family/schedule refinement, `f64`/error semantics, choice reconstruction, Python/NetworkX API correspondence and full runtime/space proofs.

The published 2016/2018 asymptotic bounds are paper mathematics and the corresponding source/runtime refinements are separate obligations. The lecture introduces no new theorem or performance assertion about the compiled program.

## Good next proof-reading exercises

- For 2004, open `ContractionCompleteness.lean`, explain both directions of ordered-tree versus Dyck-word contraction, then find the `PrintedContainmentCounterexample.lean` statement whose converse fails.
- For 2016, trace `rooted_matching_recurrence` through branch decomposition and assembly before inspecting the matching solver.
- For 2018, trace `skipped_recurrence_two_state` and `RootedDP.solve_correct`; locate the exact hypothesis that distinguishes mapped and skipped states and follow the `Definition 4` scoring branch.

These exercises refer to **existing** files and declarations in the supplied snapshot. When later sessions aim to teach the current state or draft completion work, reopen the latest source rather than relying on this dated map.
