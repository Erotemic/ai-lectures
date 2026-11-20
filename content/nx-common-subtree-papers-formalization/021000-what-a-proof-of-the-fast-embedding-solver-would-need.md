# What a Proof of the Fast Embedding Solver Would Need: The 2018 Formalization Frontier

<!-- BEGIN SPOKEN LECTURE -->

Imagine that a computer program returns a beautiful common subtree embedding. It identifies original vertices from two input trees, tells you which paths connect the selected vertices, and computes a score that includes vertex-label rewards, edge-label rewards, and penalties for every skipped interior vertex. You can inspect the output and verify that its paths really form a valid topological embedding. You can even compare it with an exhaustive solver on small examples, and the results agree.

What, exactly, have you proved?

You have considerable evidence that the implementation is useful. You may have checked a particular witness's feasibility and numerical score. But you have not necessarily proved that the result is globally optimal, that the algorithm does not miss a skipped-highest-vertex case, or that it always finishes within the bound advertised in the 2018 paper. And if the implementation uses floating-point numbers while the mathematical theorems speak of real-valued weights, even the relationship between the program's score and the mathematical score needs an explicit contract.

This lecture takes the existing common-subtree formalization seriously as an object of study. Instead of starting from an empty Lean file, we ask what the uploaded repository actually establishes, how the different proofs fit together, and what theorem would have to be added at each remaining interface. The goal is to make it possible to read a proof obligation and recognize what would close it, without mistaking a nearby theorem for the one we really need.

## First distinguish the object being optimized from the method of optimization

The mathematical problem starts with a common abstract tree. Its vertices map injectively into selected vertices of each input tree. Its edges are realized by paths. Apart from selected endpoints, the paths do not overlap in a way that would create an unseen branch point. This is a nonempty witness: there must be at least one selected common-tree vertex.

The score of a selected common-tree vertex comes from its pair of input vertices. The score of an abstract common-tree edge comes from its two realizing paths. Only if both paths are direct edges do their edge labels contribute an edge-pair reward. If either path is longer, the edge contributes minus the penalty multiplied by the total number of skipped interior vertices. The path has not become two independent edge matches. One of the strongest lessons from this formalization is that the right score must be attached to the right notion of witness before any dynamic programming begins.

The repository's Lean specification formalizes those independent objects. Its representation results connect the common-tree skeleton to source-style embeddings, and its scoring lemmas establish the intended path-score identities. This is the specification layer. It defines what a valid answer means even if every algorithm in the repository were deleted tomorrow.

The next layer defines an optimum: take the maximum score over independently valid nonempty witnesses, using a bottom value when a chosen boundary condition cannot be realized. A bottom value is not the score zero. Zero is a perfectly ordinary finite score. There might be a legal negative-scoring singleton, in which case the mathematical optimum is negative. The default application-facing API, by contrast, may choose to return an empty result with score zero whenever every nonempty answer is nonpositive. Both conventions can be sensible, but they are different functions. A refinement theorem must say which one the source actually computes.

The third layer proves recurrence equations. For rooted trees, a selected boundary pair has a child matching that combines independent branches; an unselected boundary pair must descend along at least one input path, charging a penalty for the skipped boundary vertex. In the supplied Lean files, the independent boundary states are not defined by the recurrence. The declarations called mappedValue and skippedValue optimize over actual witnesses. Then mapped_recurrence and skipped_recurrence_two_state prove that the recurrence calculates those independent quantities.

That order is essential. If we had defined the specification as whatever a dynamic program returns and then proved the dynamic program equals its own definition, the theorem would tell us little about common subtree embeddings. Here the separation is genuine: the dynamic-programming equations are derived from the topological and scoring requirements.

## A verified reference is not yet the fast solver

The file RootedDynamicProgram.lean contains an executable finite-state evaluator. It builds a table, evaluates states, and proves the result equals the independent objective under hypotheses describing complete vertex lists and the correct children for the chosen orientations. Its solve_correct theorem is a functional correctness result for a rooted score calculation. Its unrootedOptimum_correct theorem also establishes a correct but more exhaustive unrooted method by trying all root pairs.

That result is a strong baseline. It means we can write down the desired unrooted value independently of the optimized implementation and can point to an executable reference evaluator with a correctness proof. But the reference takes the mathematically safe route of trying all roots. It does not establish the speedup from the fixed-first-root decomposition in Lemmas nine through eleven.

The latter proof has a very different character. It is not a local recurrence lemma. It is a global geometric statement about a completed embedding. Choose an arbitrary root in the first input tree, then take the union of every selected image and every physical path used by the witness. That union is connected, so it has a unique highest physical vertex relative to the chosen root. If this vertex is selected, the embedding can be expressed as one of the rooted candidates. If it is skipped but belongs to the realized structure, it is internal to one abstract common edge. The selected portions of the witness then lie in exactly two distinct descendant branches below that skipped vertex.

A formal proof needs more than that verbal classification. It must show that the highest vertex exists and is unique, that an unselected highest vertex cannot be a hidden branch point, that the two pieces of the cut witness are independently valid, and that their scores sum to the original score after subtracting exactly one central skipped-vertex penalty. For the reverse inequality, it must show that two compatible boundary witnesses from different descendant branches can be reassembled into a valid common tree without violating the path-disjointness condition.

One can then define the two candidate families, conventionally called M one and M two, and prove that the unrestricted nonempty optimum is exactly the maximum of those two families. Merely showing that every candidate from the families is valid proves only that the family optimum is at most the unrestricted optimum. The converse requires showing that every unrestricted optimum falls into one of the cases. Both directions are necessary.

In the uploaded snapshot, this fixed-first-root structural equivalence is not yet a completed Lean theorem. The already proved all-root-pairs theorem can provide a reliable target for comparing the two families, but it cannot be cited as a proof of the shortcut itself.

## Reusing right-hand views needs a semantic bridge

The unrooted algorithm introduces a compact way of naming oriented right-tree subproblems. A right vertex is either considered with all of its neighbors or with one designated parent neighbor removed. Therefore there are only three m minus two full and directed-edge views across a right tree with m vertices. This count is elementary, yet the optimized solver's correctness depends on more than the count.

We need a statement that each stored view denotes precisely the rooted component intended by the mathematical recurrence. For a directed edge from v to w, the view at v excluding w must include exactly those vertices reachable from v without crossing that edge. Adjacent views must agree about their shared physical edge, but must not confuse which side contains a selected endpoint. A one-off indexing error can produce a perfectly finite score for the wrong component.

In a proof-oriented design, I would define the semantic right view first: a root vertex and an optional excluded adjacent vertex, interpreted as a finite rooted component. Then define the compact numeric identifier used by the actual Rust arrays. Prove that decoding the identifier returns the intended component, that every required component has an identifier, and that excluding a neighbor changes exactly one incident branch. The counting bound is a corollary of that representation, not a substitute for its semantic correctness.

This would also make the paper's scalar-maximum optimization a reusable theorem. Given a finite family of candidates indexed by distinct neighbors, take the two best candidate-origin pairs. Prove that excluding any one neighbor leaves the best permitted candidate among those two. If the best two have equal scores, their distinct origins are still essential. If all candidates are impossible, the result is bottom rather than zero. If there is only one candidate and it is excluded, the result is also bottom.

The Rust source has a helper that retains two candidates with their excluded-view identities and uses them while propagating skipped-state messages. The mathematical lemma should describe what that helper returns, not commit to its array layout. A later source-refinement proof can then establish that the array-based helper implements the mathematical operation, including ties and missing candidates.

## Matching families: one correctness theorem, one cost theorem

At a mapped pair of tree vertices, the right-hand oriented views differ by deletion of one neighbor. The mathematical object is an optimal partial weighted matching on the full child graph and, for each excluded neighbor, an optimal partial matching on the graph with that neighbor removed. A representation-independent theorem might say: the returned base matching is valid and optimal for the full graph, and the returned matching indexed by c is valid and optimal after deleting c.

That theorem must be parameterized by the exact edge weights derived from already correct child states. Those weights are not raw label similarities. Each one is the greater of a direct/direct branch score and a longer-path continuation score. It may be impossible, and a nonpositive value may be ignored by the partial matching because leaving the branch unused is permitted. Getting this local reduction wrong can invalidate the global tree algorithm even when the matching solver itself is perfect.

For the deletion family, the 2018 proof uses two algorithmic regimes. The first borrows the 2016 family method when the smaller side is at least the logarithm of the larger. The second uses one augmenting repair after each matched deletion and pays an additional small-side fourth-power term. A mathematical correctness theorem for family results is independent of this case distinction. A complexity theorem then assigns a cost to each regime and establishes that both are bounded by the same family-wide order, s squared times t.

In the actual source tree, max_weight_bipartite_matching_with_right_deletions accepts a matrix of optional floating-point weights and returns a base matching plus right-deletion results. Its implementation contains a fast path for a complete equal-positive-weight matrix, an assignment solver with dummy choices, a transposed branch for rectangular shapes, and a repair for each matched deleted right vertex. Some deletions reuse the base result rather than materialize a new matching. That is not simply a transcription of the graph in the paper's proof.

The repository has extensive Lean work on exact assignment, copied matching graphs, deletion repair, and related integer Rust entry points. Those results are valuable reusable infrastructure. But an exact-integer sparse-assignment theorem does not prove that this separate floating-point, sometimes transposed function returns the same original-index pairs and score. One needs a bridge that establishes the matrix conversion, preserves forbidden entries, translates positive-profit partial matchings through dummy assignments, handles the two deletion orientations, and restores original input indices. The bridge must also state what happens if an intermediate floating-point sum overflows or ceases to be finite.

This is a classic formalization trap. Two algorithms can implement the same mathematical optimization and still require distinct source proofs. The amount of shared mathematics is substantial, but their programs are not identical.

## Why the evaluation order deserves its own theorem

Even with perfect local matching and maximum operations, we could compute a table in the wrong order. A skipped state at u,v may descend to a different right orientation at the same left vertex u. The opposite orientation can appear to request a value that depends back on the first one. The paper solves this by a careful main-versus-sub scheduling rule. The production Rust algorithm uses a fixed left postorder, calculates mapped matching families from completed left-child tables, and then runs two right-tree passes to compute skipped messages.

To prove this procedure, it is useful to make the dependency graph explicit. Every table entry has a semantic interpretation and a set of required input entries. Some dependencies decrease the left-tree subtree size. Others stay at the same left vertex but move through a right-tree message schedule. A simple induction only on the pair of vertex depths will not necessarily explain the same-u right rerooting dependencies.

A more suitable proof separates the phases. Before processing u, assert that all mapped and skipped values for every strict left child of u and every right view have been computed correctly. Then prove that the matching-family phase completes every mapped value for u because its inputs all lie in those completed child tables. Finally prove that the two right passes, treating these mapped values as fixed, compute the correct skipped values for every right view. The first pass supplies child-to-parent information; the second supplies parent-to-child exclusions, where the two-best-origin lemma handles the missing neighbor. After both phases, the full invariant holds at u. Structural induction on the fixed left postorder then closes the entire table.

This is not necessarily the only way to formalize the source, but it follows the actual organization of compute_embeddings closely enough to make the proof obligations inspectable. It also isolates the reason the program does not accidentally recurse around a right-tree edge. The absence of a cycle becomes an invariant about the phases, rather than a property inferred from successful test runs.

Once the table is correct, the source still needs the M one versus M two theorem. The final source loop enumerates the highest skipped-left-vertex case, splits across right edges, chooses the two best distinct left child branches, and joins their recorded witnesses. Its proof requires the independent structural case split from Lemmas nine and ten and the top-two cardinality-two exchange argument from Lemma eleven. This is why I would prove the mathematical structural bridge before attempting a line-by-line verification of that last loop.

## The resource theorem is a separate composition

Suppose all those correctness results are proved. Are we finished? Not if the objective includes proving the time and space bounds. The paper's running time counts arithmetic operations in its abstract matching model. The source contains loops, allocations, choice storage, matrix construction, and reconstruction. A resource theorem has to decide what counts as one operation and how many resources the actual program may retain at once.

We can decompose the cost into named pieces. Constructing all constant-sized scalar state transitions. Scanning child-pair matrices at each vertex pair. Solving one matching family per appropriate pair instead of repeating a full solve for every excluded right neighbor. Propagating skipped messages in the two right passes. Evaluating the M one and M two candidates. Reconstructing the selected original vertices and physical paths. Each part needs a bound, and the bound has to be applied to the exact number of times its source operation occurs.

Some mathematical counting infrastructure is already available. The Lean file Complexity/MatchingFamilies.lean proves bounds about stored matching pair cells and uses finite-tree degree sums to aggregate certain families. These are meaningful pieces of mathematics. But the file explicitly does not claim the actual Rust allocation cost. A source theorem would need to connect allocated vector capacities, shared or copied witness choices, and the lifetimes of temporary matrices to the abstract counts.

A subtlety appears here: a table with order n times m entries need not use order n times m memory if every entry holds a full copied witness. The current Rust code records compact choices and uses a choice arena, but whether that achieves the paper's stated space bound under a specified allocation model must be established rather than assumed. Conversely, if some component genuinely exceeds the mathematical space budget, the correct response is to identify the additional retained structure and adjust the implementation or claim. The theorem should describe the program we actually run.

## The numeric and Python boundaries

Lean's abstract scores use exact ordered algebraic structures with explicit bottom values, and the penalty type can represent infinity. The graph implementation uses finite floating-point weights, with infinity treated specially for the skip penalty. It compares scores strictly, retains the first encountered candidate on a tie, and rejects invalid penalties or nonfinite arithmetic. Floating-point addition is not real-number addition. Its order and rounding can change which of two nearly tied candidate embeddings wins.

A defensible source contract can take different forms. One approach is to restrict the claims to an exact integer or rational kernel and prove that implementation against the abstract optimum. Another is to define an independent floating-point scoring semantics and prove that the floating-point source computes that discrete objective, then separately quantify approximation error relative to real scores under suitable assumptions. A third is to use exact values when formal guarantees are requested and expose the faster float variant with a more limited assurance. None of those options can be silently substituted for another.

The Python interface adds one final boundary. A graph may have user-level node objects rather than sequential integer IDs. Native code frequently works with compact integers. A returned common subtree must then recover the original input objects, the actual physical paths, and the correct edge metadata. Invalid inputs and selected ambient roots also need declared behavior. Differential tests and independent rescorers are excellent engineering tools, but the complete API refinement theorem would have to preserve those identities and conventions as part of the result.

## A practical sequence for extending the formalization

I would not start by proving the entire Theorem fifteen complexity claim in one enormous Lean statement. The mathematical geometry of the fixed-first-root reduction should come first, since it defines what the optimized algorithm has to compute. Establish the two-case M one/M two identity against the independent unrooted optimum. Then prove the finite two-best candidate lemmas, including the exact bottom and tie cases. After that, establish the semantic view representation and the two-phase table invariant. These proofs supply a verified high-level algorithm independent of Rust's internal data structures.

Next, connect the actual matching-family routine to its independent partial-matching optimum, choosing a numeric model that reflects the implementation being certified. Finally, combine the table's state-count and operation-count lemmas with the matching-family bound and the actual allocation and reconstruction costs. At each step, we should be able to point to one newly closed interface, not merely a larger count of tactics in a file.

This agenda is not a demand to rewrite an already useful solver. The repo has a good deal of tested optimized behavior and multiple independent correctness baselines. The purpose of formal verification here is to turn those distinct forms of evidence into a chain in which each link has an exact claim: the common-tree specification, the mathematical recurrence, the faster unrooted decomposition, the scheduled source implementation, its result representation, and its resource usage.

The most important habit is to ask what the theorem's conclusion actually says. A finite optimum theorem establishes that a best witness exists. A recurrence theorem establishes a decomposition of that optimum. A reference evaluator theorem establishes a correct executable way to calculate it. A matching-family theorem establishes reuse of nearby optimization problems. A source refinement theorem connects concrete operations to the abstract algorithm. A complexity theorem bounds the cost of those concrete operations. The same research program needs all of them, but we make progress by keeping them distinct enough that each one can be proved honestly.

<!-- END SPOKEN LECTURE -->

## Companion: source-aware proof dependency map

**Pinned repository:** `networkx_algo_common_subtree` archive uploaded 2026-11-19. Status below refers to this snapshot; it is not a claim about subsequent commits.

| Layer | Proved in the snapshot | Further theorem or source bridge |
| --- | --- | --- |
| Independent embedding | `Droschinsky2018/Specification.lean`, `Witness.lean`, `PointedWitness.lean`, source/skeleton equivalences | Preserve source graph identities through Rust/Python conversion |
| Score | `GraftScore.lean`, `ScoreDecomposition.lean`, `BranchReward.lean` | Define/enforce source `f64`, infinity and error semantics |
| Rooted recurrence | `SkippedRecurrence.skipped_recurrence_two_state`, `MappedDecomposition.mapped_recurrence` | Efficient source matching calculation |
| Executable reference | `RootedDP.solve_correct`, `RootedDP.unrootedOptimum_correct` | Refine production `compute_embeddings` and final joins |
| Optimized unrooted M₁/M₂ | Paper Lemmas 9–11; no corresponding complete Lean proof | Highest-realized-vertex dichotomy, cut/assembly and top-two cardinality-two equivalence |
| Right exclusion and families | Paper Lemmas 12–14; exact integer infrastructure in `Shared/` and `Rust/` | Best-two maxima and main/sub scheduling, complete `f64` right-deletion source bridge |
| Complexity | Abstract `Complexity/MatchingFamilies` pair-cell/degree bounds and paper cost analysis | Actual-source operation and allocation costs, including choice storage and readback |
| Public API | Tested root modes, negative nonempty optima, empty-allowed option, reconstructed paths | End-to-end Python/NetworkX identity, score and error refinement |

### Candidate high-level theorem interfaces

These are *proposed* interfaces, not existing Lean declaration names.

1. **`unrooted_eq_fixed_left_cases`**. Given finite trees, a nonempty weighted common-tree optimum, and fixed first-tree root `r`, prove `unrootedValue = max(M1(r),M2(r))` with separate soundness and completeness witness maps. `M2` charges one penalty at its central skipped vertex and requires two distinct first-tree child origins.
2. **`delete_one_max_via_best_two`**. For a finite family of scored options indexed by distinct right-neighbor IDs, prove the maximum excluding `c` is attained among the two best candidates with distinct origins; handle ties, all-bottom inputs and size-zero/one families explicitly.
3. **`view_decode_component`**. Prove every compact directed-edge or root-view ID denotes the intended rooted physical component and every required exclusion is represented uniquely, with `m+2(m-1)` total view IDs for nonempty trees.
4. **`scheduled_table_correct`**. Given complete and correct tables for all strict left children of `u`, prove one mapped matching-family phase and two right-skipped-message passes produce the correct mapped/skipped values for every right view at `u`.
5. **`source_right_deletions_correct`**. Relate `max_weight_bipartite_matching_with_right_deletions` to mathematical partial matching optima and original column identities under explicit finite-weight, shape and overflow premises, covering both transposed and non-transposed rectangular branches.
6. **`source_runtime_space`**. Refine paper unit-cost operations and stored-state counts to the concrete loop, allocations, cached matching results, choice arena, and witness reconstruction. This is not implied by a recurrence theorem alone.

### A small source-level reading route

- `proofs/SubtreeProofs/Droschinsky2018/OverallOptima.lean`: `unrootedValue_eq_max_rerooted_mapped` is the independently correct all-roots target. It does **not** state the optimized fixed-first-root M₁/M₂ identity.
- `proofs/SubtreeProofs/Droschinsky2018/RootedDynamicProgram.lean`: `step_correct`, `solve_correct` and `unrootedOptimum_correct` certify the exhaustive reference table.
- `proofs/SubtreeProofs/Complexity/MatchingFamilies.lean`: `storedPairs_le_product`, `tree_degree_sum`, `tree_family_pairs_le` bound mathematical finite-set objects, not actual Rust heap usage.
- `rust/crates/common_subtree_algorithms/src/tree.rs`: `embedding_matching_family` and `compute_embeddings` implement per-left-child matching families and two right-message passes. `largest_weight_nonempty_common_subtree_embedding_with_roots` collects M₁ and, in its unrooted branch, M₂.
- `rust/crates/common_subtree_algorithms/src/matching.rs`: `max_weight_bipartite_matching_with_right_deletions` performs tested optional-`f64` matching family operations, with dummy choices, transposition, fast paths and repairs.
- `docs/planning/paper_statement_crosswalk.md`: snapshot statement ledger, including precise open statuses for 2018 Lemmas 9–14 and Theorems 6/15.

**Primary source:** [Droschinsky, Kriege and Mutzel, *Largest Weight Common Subtree Embeddings with Distance Penalties*](https://doi.org/10.4230/LIPIcs.MFCS.2018.54), MFCS 2018; [pinned preprint](https://arxiv.org/pdf/1805.00821v1). **Project source:** the accompanying `networkx_algo_common_subtree` archive and its proof-status ledger. This lecture proposes potential theorem interfaces; they are not claims of already implemented Lean proofs.

### Listening checks

1. Why is a proof of `RootedDP.unrootedOptimum_correct` not already a proof of the M₁/M₂ fixed-first-root shortcut?
2. What semantic invariant must relate a stored right-view index to a physical component of an unrooted tree?
3. Why can an exactly verified integer matching helper not be cited as a correctness proof for the separate optional-`f64` deletion function?
4. How can a dynamic program have `O(nm)` table entries but use more than `O(nm)` memory in an actual implementation?
5. If the final Python answer contains original node objects and realized paths, what must an API refinement theorem preserve beyond the scalar optimum?
