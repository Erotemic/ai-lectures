# From a Proved Recurrence to Fast Rust: The 2016 Formalization Frontier

<!-- BEGIN SPOKEN LECTURE -->

Suppose a theorem prover has checked that a dynamic-programming recurrence gives the optimal answer to a combinatorial problem. Suppose a Rust program runs quickly on real inputs and repeatedly agrees with an independent oracle on small trees. Suppose, further, that several individual Rust matching functions have themselves been translated into Lean and verified. Do we now have a verified fast implementation of the algorithm described in the paper?

Not necessarily. The three achievements can be entirely genuine while the desired end-to-end theorem remains open. The gap is not a semantic quibble. The recurrence, the algorithm that evaluates it, the data representation, and the public function invoked by a user are different objects. A proof about one is useful only to the extent that we can connect it to the next.

This lecture is a guided reading of that gap in the supplied November 2026 common-subtree repository. The immediate paper is Droschinsky, Kriege, and Mutzel's 2016 weighted maximum common subtree isomorphism algorithm. We have seen its mathematical objective, the rooted child-matching recurrence, the fixed-root reduction, the copied-assignment construction, and the one-vertex deletion trick. Now we will ask what is actually proved in Lean, what the production Rust code actually does, and which missing theorems would take us from one to the other.

The answer is not a binary verdict of verified or unverified. There are several distinct guarantees, and they can be composed only when their contracts line up.

## Begin with an independent object, not a program

The first layer is the mathematical specification. Given two finite trees, a valid common subtree isomorphism selects connected induced vertex sets and gives a bijection between them preserving adjacency. The selected set is nonempty. Every mapped vertex pair and mapped edge pair contributes its specified weight. Forbidden pairs have no finite reward, and negative permitted weights are allowed.

The crucial independence is that the definition of a valid witness does not refer to matching tables, memoization, Hungarian potentials, or any particular traversal. If we changed the algorithm tomorrow, that mathematical definition should stay intact.

In the source repository, this layer lives in the Droschinsky 2016 specification and witness modules. The statements establish the existence of a maximum among finite valid candidates and spell out how a witness earns its score. They can be instantiated with exact real or integer arithmetic through the generic ordered-ring development. This does not automatically say anything about floating-point rounding in the native implementation.

Why is a separate specification indispensable? Consider a parent vertex pair whose score is negative eight. One child branch, if included, contributes eleven. A rooted common subtree that includes the parent and child has value three. If we mistakenly clamp the parent's contribution to zero before adding the branch, we would report eleven for a witness that actually scores three. If we discard the parent altogether, we may violate the required connected root-to-root state. The independent witness definition catches both mistakes because it specifies which vertices are mapped and how they are scored.

The empty partial child matching is allowed and contributes zero. The empty common subtree is not allowed under the paper's nonempty objective. This distinction persists in source proof obligations. A Python-facing convenience function may separately offer an empty result of score zero, but then its API statement is not identical to the paper's mathematical optimum when every nonempty candidate is negative.

## The first verified bridge: from witnesses to recurrence

Once validity and score are defined, the central problem is to justify the rooted recurrence. Take a valid root-to-root witness. Remove its mapped roots. The remaining selected vertices fall into branches hanging below children of the first root. Because the witness is an isomorphism and the selected subtrees are connected, these branches map into distinct branches below the second root. Thus the witness induces a *partial matching* of child branches.

Each matched pair of branches contains a smaller root-to-root witness. Its score can be bounded above by the independently defined optimum for that smaller pair, plus the weight of the edge joining it to the two mapped roots. Add up those bounds and the matched-root reward: every global witness is bounded above by one of the matching recurrence's candidates.

The converse direction is just as important. Given a valid partial matching of child branches and suitable optimal witnesses for the selected smaller states, we can glue those witnesses together with the mapped roots and incident edges. Their vertex sets remain disjoint outside the roots, so the union is connected and induces the required isomorphism. Its score is exactly the proposed sum.

Together these give equality, not merely an upper bound. In Lean, the branch decomposition and branch assembly modules develop the two directions, and `Oriented.rooted_matching_recurrence` extends the result to descendant states in a fixed pair of ambient orientations. The assertion is about the *mathematical optimum* and the matching objective, not yet about a particular Rust memory layout.

A separate fixed-root theorem shows that the maximum over the needed left descendant roots and right root choices equals the unrooted optimum. This is another mathematical representation bridge. It is why the source paper can pick one left root without excluding any global solution.

Notice how much has been proved already. A reader who understands these theorems has a real correctness result for the heart of the algorithm. The remaining work is not to rediscover the recurrence. It is to show that the executable work, performed efficiently, is exactly the work the recurrence prescribes.

## The second verified bridge: an executable Lean table

The next question is more operational. Can a concrete evaluator fill a table and return the independent optimum? `Droschinsky2016/RootedDynamicProgram.lean` answers yes for an intentionally straightforward model. It builds finite lists of vertices, computes child weights from earlier entries, and uses an exhaustive finite matching optimizer for each state. Its `step_correct` theorem says that if the required earlier values are correct, one step gives the independently specified rooted value.

The whole-table theorem, `solve_correct`, eliminates those local prerequisites through an evaluation-order argument. The dependency rank decreases when a state moves to a child pair. The solver's successive rounds eventually provide all required entries. The unrooted baseline theorem, `unrootedOptimum_correct`, then combines these tables with the fixed-root result and obtains the correct nonempty unrooted score.

There are two lessons in this. First, the implementation of the recurrence can be proved correct *without* relying on a fast matching algorithm. Exhaustive matching is mathematically acceptable for a reference solver even though it is expensive. Second, this particular evaluator constructs a table for each possible right root. It is not Algorithm 1's fully shared right-oriented view schedule. Its theorem cannot be substituted for a source correctness or resource bound for the faster implementation.

This is a useful research pattern. Prove a simple evaluator first, so the mathematics and the evaluation-order proof can be checked independently. Then refine to a faster schedule without changing the meaning of the result. The difficult part is making the refinement theorem explicit rather than treating the resemblance of the two programs as self-evident.

## Matching is already a separate proof project

The recurrence delegates most of its computation to maximum-weight bipartite matching. The repository does not leave this entire subproblem as a black box. Its shared Lean modules specify signed partial matchings with optional forbidden edges. They prove an exhaustive optimum and the copied-graph reduction used by Lemma 5. Dual-feasibility and tightness results establish the mathematical certificates that a Hungarian-style solver should maintain.

For Lemma 6, the mathematical development proves that deleting an unused right vertex preserves an optimal matching. It proves that at most the smaller side's cardinality many deletions can invalidate the chosen base optimum. For a matched deletion, it identifies precisely one missing pair in the copied perfect assignment. Further results recover feasible and tight assignments, relate cyclic repair to the optimum, and preserve the original vertex coordinates when decoding the repaired result.

Those are not merely conjectures translated into identifiers. They are accepted Lean statements under their declared assumptions. But different modules establish different parts of the story. An existence theorem for a repair does not prove that the production program computes the repair. A proof that two assignments share a dual certificate does not count the operations required to find one of them.

The repository also has translated source-level proofs for an exact-integer reference assignment and matching-deletion family. One public family theorem establishes that the actual reference API terminates on admitted inputs and returns the independently optimal original and deleted matchings with their original indices. The reference family may still recompute matched deletions from scratch. It is verified for functional behavior, not the paper's optimized running time.

There is also a more specialized sparse repair path. The actual Rust source can remove a row and column from a compatible copied assignment, preserve the surviving dual data, and perform a single sparse augmentation. A theorem named `Rust.SparseDeletion.repair_deleted_sparse_vertex_spec` establishes the returned optimum and certificate under a stated old copied-graph numeric invariant. Related proofs cover the source search, index compression, path flip, and output coordinates.

The phrase *under a stated invariant* is not a weakness to conceal. It is a precise interface. The next caller must establish that its matching construction and maintained potentials really satisfy the invariant every time this function is invoked. That global connection is different from the already proved internal correctness of the helper.

## Why two correct assignment representations may still need a bridge

The paper's proof uses a copied bipartite graph. Each vertex has a copy, selected identity edges have weight zero, and a perfect assignment decodes into two partial matchings of the original instance. This representation is excellent for proving the objective relationship and analyzing matched-vertex deletion.

The production floating-point Rust matcher, however, uses a smaller-side assignment layout with dummy columns. Its `max_weight_bipartite_matching_with_right_deletions` function can transpose an instance, reuse the base assignment and repair only deletions that actually touch the selected matching. It also has a special case for a complete uniform positive matrix. The code is not simply a transcription of the paper's copied graph.

These two designs can compute the same optimal partial matching and still have different invariants, different indexing, and different costs. To relate them formally, we need a representation theorem. It must say which assignment columns correspond to actual original right vertices, how dummy entries contribute zero, how transposition changes coordinates, and how an augmented assignment decodes back into a legal matching with the correct original indices and objective.

The distinction matters especially for deletion families. In a smaller-side orientation, deleting a right vertex may correspond to deleting a column, while after transposition it corresponds to removing a row. The Rust implementation handles those cases differently. A proof of a copied-graph deletion theorem is extremely useful, but it does not certify the transposed dummy-column code without an explicit connecting argument.

This is the difference between a good mathematical algorithm and a specific software artifact. The mathematical reduction permits many representations. The program chooses one. Source verification must account for that choice.

## The actual tree solver has its own optimization strategy

Open `rust/crates/common_subtree_algorithms/src/tree.rs` and find `compute_rooted_isomorphism`. It works with an oriented view of the right-hand tree and a fixed-left orientation. It builds a matrix of child-pair continuation scores and retains choice nodes for reconstruction. Most calls use the ordinary weighted matcher. For selected higher-degree states, it calls the related right-deletion family and populates the memo entries for the full right view and all one-neighbor-excluded views together.

This selective use of matching families is a performance decision. The implementation need not materialize every family if small instances are cheaper to solve separately. But a theorem for the *actual* schedule would have to include both paths. For the states that use the family, it must show that the base and deletion results fill the correct oriented table entries. For the states that do not, it must show that their extra ordinary matching calls remain within the global bound.

The source also stores reconstruction choices, not full copied subtrees in every DP entry. A solver result carries a score and a witness identifier into an arena of choices. Reconstructing a mapping by following those choices has a separate correctness and cost obligation. An algorithm that computes the optimal *score* but returns wrong original node identities does not satisfy the expected public witness contract.

The source documentation records independent exhaustive tests, installed Python tests and benchmark improvements for these optimizations. These are useful evidence that the implementation is functioning and faster in the measured cases. They do not replace a theorem connecting the production function to the independent validity and optimum predicates.

## What a complete functional-refinement proof would say

Imagine a Lean theorem about the actual production entry point. It starts from two well-formed finite input trees and a scoring interpretation satisfying the permitted numeric contract. It runs the translated function on representations of those inputs. It ends with a witness, or a correctly defined absence result if the API permits one.

The theorem should establish at least three properties of a returned witness. It is feasible: selected nodes really belong to their original input graphs, mapping is injective, edges are preserved, and the selected pieces are connected. Its returned score agrees with the independent mathematical score. And no other feasible witness has a larger score under the same objective and root restrictions.

There may also be a root-mode theorem. The public API distinguishes unrestricted solutions, a fixed ambient orientation, and a forced mapped root pair. A correct theorem for one mode does not certify the others merely because they call related code. The conversion to and from NetworkX nodes, including arbitrary Python node identities and edge attribute lookup, introduces further contracts outside the pure Rust core.

The existing exact-integer matching APIs prove narrower claims and provide reusable building blocks. Their theorem statements do not automatically imply the entire graph-DP and PyO3 contract. One reason to read the declarations rather than only their names is to see precisely which input representation, result and preconditions each proof covers.

## What the complexity proof would have to add

Even a complete source functional-correctness proof would not finish the 2016 research program. Theorem 7 is a bound on a *family of computations*. It assumes a particular augmentation strategy and a work model. Theorem 4 adds the DP schedule and the rest of the algorithm.

The paper's central local estimate is a product of the two matching-side sizes times the smaller side plus a logarithm of the larger side. To verify this for an implementation, we would want a costed operation model that records the actual work done by the matching routine. The model must charge for building or visiting matrix entries, scanning or relaxing eligible edges, changing dual potentials, maintaining whatever queue or heap supplies the logarithmic factor, and reconstructing a matched-pair result.

A function that recomputes the entire matching after every deletion may return the exact correct family and still exceed this bound. Conversely, one that uses a single augmentation per deletion can be asymptotically too slow if each augmentation scans too many irrelevant entries or if a repeated allocation silently copies a quadratic matrix. Counting augmentation rounds is not the same as counting primitive operations.

The supplied exact-integer sparse search is verified for functional correctness but currently uses matrix scans instead of the paper's optimized sparse priority-queue routine. Its proof is a strong correctness foundation. It is not a claim about a logarithmic queue implementation that has not been established.

There is already a nearby, narrower cost result in Lean. `Complexity/MatchingFamilies.lean` proves bounds for the number of pair cells stored in a mathematical family where unmatched deletions share the base result. A family with smaller side k stores at most k plus k squared pair cells in that model. There are also tree-degree aggregation theorems that produce a quadratic total bound for such stored pairs over all vertex-pair families.

This is meaningful progress, because it isolates one resource whose bound follows from matching feasibility alone. But it is not a space theorem for all production vectors, memo tables, scratch arrays, cached choices and allocator capacity. And, being a storage count, it cannot substitute for Theorem 7's time theorem. A proof of space use has to follow the actual representation if we want to describe what the installed program allocates.

## A practicable sequence of next theorems

There is a way to attack the remaining work without taking on the entire Python binding and optimizing matching implementation at once.

First, state a clean abstract interface for one weighted matching family. The input is a finite matrix with forbidden and signed entries. The result contains the base maximum and an optimum for every one-right-vertex deletion, all with original-index witnesses. This functional specification is already well supported by the existing mathematics. Make its representation-independent contract explicit at the boundary where the tree DP consumes it.

Second, prove the *tree schedule* correct assuming only that family contract, rather than assuming the structure of a particular Hungarian solver. For each fixed pair u and v, the full view and each excluded-parent view must receive the corresponding matching score. All child entries must already be correct. An induction over left postorder or a suitable ranked dependency order should then establish that every filled view equals the independently defined rooted optimum. The fixed-root theorem gives the final global optimum.

This is an attractive milestone because it can close the gap from matching-family correctness to Algorithm 1's mathematical evaluation without depending on a difficult priority-queue runtime proof. It would create a precise interface that the optimized Rust matcher could later be shown to implement.

Third, introduce a costed matching-family interface. The proof obligation is no longer just that the returned family is optimal, but also that the family construction consumes at most the claimed number of primitive operations. The paper's base assignment, retained dual certificate and one-deficit repairs tell us what invariants and cost accounting to seek. Here an explicit asymptotic model and a priority-queue realization become central.

Fourth, sum those charges over the actual oriented tree schedule. This is where the formal degree-sum theorem and the previously proved storage counts become reusable. The local bound is expressed in local degrees. We upper-bound the smaller and larger degrees by their respective global maxima, factor the double sum, and obtain Theorem 7. Charge the remaining DP and reconstruction work to obtain Theorem 4 under the declared cost model.

Fifth, establish source refinement for a chosen practical implementation. The graph-matrix constructor must preserve the branch-pair weights and forbidden entries. The matching function must implement the abstract family contract. The memo and right-view index representations must preserve the mathematical state identities. The choice arena and public result conversion must reconstruct original input witnesses. The actual source-level cost needs its own theorem if the intended guarantee is the published running time.

Finally, give the public Python boundary a separate theorem or explicit trusted-interface contract. NetworkX inputs and returned Python node objects are not mathematical finite types without a conversion layer. The proof needs to say what the conversion preserves, how weights are interpreted and which errors or empty-result conventions are admitted. Otherwise, the theorem is correctly about Rust or Lean, not yet about the installed Python API.

This sequence is not the only proof strategy, but it has a useful property: each stage would establish a self-contained result and expose exactly the hypotheses needed by the next stage.

## A research reader's test

When reading a new theorem in this repository, try three questions. What is independently specified? What actual computation does this theorem describe? And what cost, if any, is counted?

A theorem may connect a source function to a mathematical optimum but say nothing about its runtime. A theorem may establish a state-count or storage bound but leave source code unverified. A source-level theorem may depend on an old dual certificate being valid, requiring a caller theorem to supply that certificate. None of these is a failure. They are different pieces of a larger chain.

For this particular 2016 paper, the independent graph problem, its rooted recurrence, the fixed-root reduction, and considerable matching mathematics are already formalized. The repository also contains source-proved exact-integer matching and sparse-repair components, and it has an optimized floating-point tree implementation with substantial testing and benchmark evidence. What remains is to connect the optimized global computation and its resource use to those mathematical theorems, then decide how much of the numeric and Python boundary belongs inside the eventual assurance claim.

That is the point from which formalization becomes an active research program rather than merely an exercise in reading a paper. We can identify the missing interfaces, see why each one is needed, and choose the next lemma for the guarantee it would actually buy us.

<!-- END SPOKEN LECTURE -->

## Formalization companion: the actual assurance graph

The following statuses refer to the supplied `networkx_algo_common_subtree` snapshot dated **2026-11-19**; they are not claims about the current state of an evolving checkout.

| Layer | Existing checked result or evidence | What it does **not** establish |
| --- | --- | --- |
| Independent mathematical specification | `Droschinsky2016/Specification.lean`, `Witness.lean`: finite valid induced connected isomorphisms; score and optimum | Production representation or runtime |
| Rooted mathematics | `RootedRecurrence.lean`, `OrientedRecurrence.lean`, `Rooted.lean`: `rooted_matching_recurrence`, fixed-root theorem | An efficient evaluator or f64 semantics |
| Executable mathematical baseline | `RootedDynamicProgram.lean`: `step_correct`, `solve_correct`, `unrootedOptimum_correct` | The shared Algorithm 1 schedule or optimized matching cost |
| Copied graph and deletion correctness | `Shared/CopiedAssignmentReduction.lean`, `CopiedMatchingInitialization.lean`, `CopiedMatchingDeletion.lean`, `CopiedMatchingRepair.lean`: reduction, feasible/tight duals, repair, decoding | A cost bound or the actual production dummy-column representation |
| Exact-integer reference APIs | `Rust/MatchingDeletionEntrypoint.lean`: `max_weight_matching_deletions_total_spec` | Optimized matching-family runtime |
| Actual source sparse repair | `Rust/SparseDeletionEntrypoint.lean`: `repair_deleted_sparse_vertex_spec` under `DeletionReady` and old numeric invariants | The global family caller, f64 tree kernel or priority-queue complexity |
| Model pair-cell resource count | `Complexity/MatchingFamilies.lean`: `storedPairs_le`, `tree_family_pairs_le` | Theorem 7 time or actual production allocation |
| Optimized graph backend | `rust/crates/common_subtree_algorithms/src/tree.rs`, `matching.rs`: fixed-left views, dense memo, selected deletion-family reuse, arena witnesses | Independent full source refinement or formal Theorem 4/7 resource bound |
| Installed Python API | PyO3/NetworkX integration and independent tests | End-to-end formal node/weight/empty/error contract |

### What to seek in a future theorem statement

The following is an **interface sketch, not existing Lean code**:

```text
matchingFamily_correct(matrix):
  base is maximum for matrix
  for every valid original right index j,
    deleted[j] is maximum for matrix without right vertex j
  each pair list uses original matrix indices

orientedSolver_correct(family_contract):
  all filled D(u,s,v) equal independent oriented rootedValue(u,s,v)
  global maximum equals independent nonempty unrootedValue

matchingFamily_cost(implementation, cost_model):
  cost(base + all right deletions)
    <= C * a * b * (min(a,b) + log(2+max(a,b)))

globalCost(orientation_contract, family_cost, degree_sum):
  cost(Algorithm1) in
    O(|G|*|H|*(min(DeltaG,DeltaH)+log(2+max(DeltaG,DeltaH))))
```

These are *proposed* proof interfaces. A proper Lean implementation must define the costed computation, input size, finite domains, and source representation explicitly. No runtime claim should be imported by giving a function a suggestive name.

### Practical reading sequence

1. `proofs/SubtreeProofs/Droschinsky2016/Specification.lean`, `Witness.lean` — identify the independent `Valid`, optimum and scoring definitions.
2. `BranchDecomposition.lean`, `BranchAssembly.lean`, `OrientedRecurrence.lean` — trace witness decomposition and construction, then the descendant recurrence.
3. `RootedDynamicProgram.lean` — inspect `step_correct` and `solve_correct` hypotheses, and see that the unrooted baseline reroots H.
4. `Shared/CopiedAssignmentReduction.lean`, `CopiedMatchingDeletion.lean`, `CopiedMatchingRepair.lean` — identify the source matching invariants and the one-deficit repair.
5. `Rust/MatchingDeletionEntrypoint.lean`, `Rust/SparseDeletionEntrypoint.lean` — inspect the complete stated preconditions and the proved actual source result.
6. `rust/crates/common_subtree_algorithms/src/matching.rs`, `tree.rs` — compare *actual* dummy-column assignment, transposition and selective family calls to the paper's copied graph.
7. `proofs/SubtreeProofs/Complexity/MatchingFamilies.lean`, `docs/planning/paper_statement_crosswalk.md` — separate mathematical storage from source-running-time guarantees.

### Three useful candidate projects, ranked by compositional leverage

- **The family-to-DP bridge:** assume independently correct indexed matching families and prove a score/witness-correct shared oriented-table evaluator. This can close a central correctness gap before any resource proof.
- **The matching representation bridge:** prove objective and original-index equivalence between the paper's copied assignment and the production dummy-column/transposed family, including both deletion orientations.
- **The costed scheduler:** specify and verify a real operation model for optimized augmentations and charge each family in the oriented tree schedule; compose with `tree_degree_sum` to obtain Theorems 7 and 4 for the chosen implementation model.

The repository's current priority and open obligations are recorded in `docs/planning/droschinsky_2016_2018_verified_rust_lean.md` and `docs/planning/paper_statement_crosswalk.md`. Refresh them against the user's latest checkout before treating this as a live task list.
