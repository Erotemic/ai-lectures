# One Saved Assignment, Every Deleted Neighbor: Refining the Fast Matching Family

<!-- BEGIN SPOKEN LECTURE -->

A tree algorithm repeatedly asks a question that seems wasteful to ask more than once. We have one weighted bipartite graph. We know its maximum-weight matching. Now, for each vertex on the right, we want the maximum after that particular vertex is forbidden. If the right side has a hundred vertices, we appear to have a hundred new optimization problems.

But these are not a hundred unrelated problems. They are a hundred small changes to one problem whose solution we already possess. Some changes do not disturb that solution at all. The others create a defect so localized that the matching can be repaired rather than reconstructed from scratch. Droschinsky, Kriege, and Mutzel exploit this in their 2016 and 2018 tree algorithms. The common-subtree repository implements a fast family solver, contains Lean proofs for several pieces of the mathematical argument, and contains a separately verified exact-integer reference. What it does not yet have is a theorem connecting the entire optimized floating-point implementation to its specification and running-time bound.

Today we will design that missing bridge. We will not pretend that a proposed theorem is already a checked theorem. We will read the source as a specific mathematical machine: its inputs, its stored assignment, its two repair branches, its output representation, and the work each branch performs. By the end, we will be able to describe a feasible sequence of proof obligations and explain where the existing Lean results belong.

## First specify the result without mentioning the implementation

Let the left vertices be a finite set L and the right vertices a finite set R. For each possible pair, there is either a real weight or no permitted edge. A matching is a set of permitted pairs in which no left vertex and no right vertex occurs twice. Its score is the sum of its weights. Either side may leave vertices unmatched, and an unmatched vertex contributes zero.

Call the best possible score on the original graph V. For each right vertex r, call the best score after deleting r, V sub r. Deletion means that every edge incident to r becomes forbidden. We can keep the original right-vertex labels; no renumbering is needed in the mathematical specification.

A correct family result has two layers. First, it returns a maximum matching of score V. Second, for every right vertex r, it returns a valid matching that avoids r and has score V sub r. If we care about actual witness reconstruction, returning only the values is not enough. The pairs must use original input indices, must have no duplicate endpoint, and must add up to the reported score. A subtree solver will later use those pairs to select child witnesses.

Notice what the specification does not say. It does not prescribe a Hungarian algorithm, an augmenting path, copied vertices, a cache, or a particular tie-breaking rule. There may be many optimal matchings. The formalization should accept all of them unless the surrounding API deliberately promises a canonical choice. This separation is the first protection against accidentally proving a theorem about one implementation that fails to express the actual optimization problem.

In the Lean library, `WeightedMatching.IsMaximum` expresses the independent optimum. `WeightedMatching.deleteRight` models the forbidden right vertex. The theorem `IsMaximum.deleteRight` is already checked: if the deleted right vertex does not occur in an existing maximum matching, that very same matching remains maximum after deletion. This proof is short but powerful. Every feasible matching in the deleted graph was also feasible before deletion, so it cannot beat the original maximum. And the old maximum remains feasible because it never used the deleted vertex.

There is no promise that the old solution is the only optimum. There is no need for one. The reuse theorem works for whichever optimal matching our solver happened to return.

## A small family that shows both kinds of deletion

Here is a two-by-three example. Call the left vertices Alice and Bob, and the right vertices P, Q, and R. Alice may match P for weight nine or Q for weight six; Alice cannot match R. Bob may match P for eight, Q for seven, or R for five. All the stated weights are positive.

The original optimum matches Alice to P and Bob to Q. Its score is nine plus seven, or sixteen. We should check that rather than assume it. Matching Alice to Q and Bob to P gives fourteen. Matching Alice to P and Bob to R also gives fourteen. Alice to Q and Bob to R gives eleven. A single edge cannot beat sixteen. So sixteen is the maximum.

Now delete R. The chosen optimum never used R. Alice to P and Bob to Q still scores sixteen, and no solution on a smaller set of allowed edges can exceed the original optimum. That is the entire repair. It consists of reusing the old answer.

Delete Q instead. The old Bob-to-Q edge disappears. Alice to P remains, and Bob can now match R for five. The optimum is fourteen. The missing right endpoint Q has forced a change to one assignment, but we did not need to solve a new matching problem independently to discover the logical structure of the change.

Delete P. Alice loses her chosen partner. If Alice takes Q for six, Bob must vacate Q. Bob can then take R for five. The repaired total is eleven. That change is an alternating path: Alice moves to Q, displacing Bob, who moves to R. In the original matching Bob occupied Q and R was unused. The repair travels through a sequence of occupied and unoccupied edges until it reaches freedom. We can confirm eleven is optimal by enumerating the surviving possibilities: Alice-Q with Bob-R scores eleven, Bob-Q alone scores seven, Bob-R alone scores five, and no other compatible pair assignment does better.

The example gives three deletion requests but only two potentially difficult ones. The old matching uses exactly two right vertices. In general, at most the smaller bipartition size can be used. The Lean theorem `deletion_repair_card_bound` proves precisely that counting statement. It counts how many deletions can require a repair; it does not yet price each repair.

Keep this example in mind. We will return to its original labels after the assignment algorithm has temporarily rearranged indices and introduced dummy vertices.

## The assignment state as a reusable certificate

A maximum-weight partial matching can be transformed into a minimum-cost assignment. The production Rust solver turns a compatible positive profit into its negative cost. Missing and nonpositive profits are treated as zero-cost assignment choices and then omitted from the returned real matching. This is legitimate for the mathematical objective: choosing a nonpositive edge can never improve a partial matching when leaving both endpoints unmatched is permitted.

The solver orients the smaller bipartition as assignment rows. The larger side becomes real assignment columns. Additional zero-cost dummy columns make the assignment extensible even when real edges are absent or have no positive profit. Thus an assignment may fill every row while the decoded partial matching leaves several real vertices unmatched.

The crucial thing it saves is not merely a list of selected pairs. It saves a primal assignment together with dual potentials. A potential belongs to every row and every column. In the minimum-cost convention, dual feasibility means the row potential plus the column potential is at most the cost of their edge. The difference between cost and that sum is the reduced cost, or slack. It is nonnegative when the dual is feasible. A matched edge is tight when its slack is zero.

Those facts form an optimality certificate. If we have a feasible assignment in which the chosen edges are tight, and the appropriate rectangular unused-column conditions hold, then the assignment reaches the dual bound. There is no cheaper competitor. This is why an augmenting-path algorithm can do more than find some replacement: while changing the assignment, it updates potentials so the replacement can be proved optimal.

In the source, the type is `AssignmentState`. It stores arrays called `u` and `v` for the potentials, `p` for the assignment, `way` for predecessors, and `minv` and `used` for the search. The arrays have a reserved zero index for the augmenting-path sentinel. In `p`, a nonzero entry at a real column identifies the row assigned there, with a one-based offset. The source method `augment_row` starts from one free row, searches across reduced costs, updates the duals, and flips the resulting alternating path.

A future Lean invariant for this concrete state must describe more than array lengths. It must express that real occupied columns name distinct rows, all other rows remain assigned, the retained edges are tight, and the dual is feasible. The unique free row is the only intended defect at the start of a repair. It must also specify that index zero is a sentinel rather than a real vertex, and that every conversion between one-based internal indices and original zero-based input labels is sound.

The existing mathematical matching proofs already express much of this certificate structure. That does not automatically connect their `Equiv.Perm` and finite-function objects to the `Vec` arrays and floating-point comparisons of this Rust code. The representation relation is one of the missing bridges.

## The direct deletion branch: remove a column, then augment

We can now follow the public production function, named `max_weight_bipartite_matching_with_right_deletions`, in `rust/crates/common_subtree_algorithms/src/matching.rs`.

The function validates the matrix and handles easy cases first. Empty sides return an empty family. If no positive compatible weight exists, every matching optimum is empty. If all entries have the same strictly positive weight, an independently proved uniform-pair constructor supplies an optimal family without running the general assignment solver. The hard branch handles the rest.

When the input has no more left vertices than right vertices, the original right side is the assignment's column side. The solver computes one full assignment and decodes a base matching. It marks which original right vertices occur in that decoded matching. Then it iterates through the original right indices.

If a right vertex is unmarked, its deletion entry is `None`. Here `None` is not an infeasible result. In the `WeightedMatchingFamily` representation, it means: share the already stored base matching. The method `without_right` makes this distinction explicit. A reader must not confuse an optional stored replacement with an optional mathematical solution.

If the deleted right vertex is marked, the source removes its assignment column from the saved state. It copies the relevant potentials and column occupancy into a repair state with one fewer column. Exactly one old row becomes free: the row previously assigned to that removed column. The source invokes `augment_row` once, not once for each possible new pair. A reconstructed assignment is then filtered to positive compatible real-real pairs, and its columns are converted back to their original right indices.

That last operation is easy to overlook. Removing column Q from an array makes the next surviving column move one position left in the compact array. But the API must still report R as R, not as Q. The production closure maps every compact column back by adding one after the removed position. In the exact-integer sparse reference, separate Lean lemmas already prove a related index-compression and original-column readback. Reusing the proof idea is appropriate; declaring the production closure verified because a different source function was verified would not be.

Our Alice-and-Bob example is a small instance of this branch. Deleting R reuses the base. Deleting Q frees Bob's row and allows Bob to take R. Deleting P initiates the alternating path from Alice through the occupied Q column to Bob and then to R. The algorithm's dummy assignments ensure a complete assignment remains possible even when the best partial matching uses fewer real pairs.

## The transposed branch: deleting a right vertex removes a row

There is a second case, and it deserves its own proof. Suppose the original matrix has more left vertices than right vertices. To keep the assignment rectangular with fewer rows, the Rust code transposes the assignment view. The original right vertices are now rows. Deleting an original right vertex therefore deletes an assignment row, not a column.

We cannot simply reuse the previous argument with the words row and column exchanged, because the production code performs an additional optimization. After computing a base assignment, it records the columns that its rows occupy. For a matched deletion, it builds a square repair instance using just those previously occupied columns. It replaces the deleted row's costs by zero, regards that row as a dummy, and performs one augmentation. When decoding, it discards the dummy row and maps every selected occupied column back to its original left-vertex index.

Why is it safe to ignore all other columns? Perhaps one of the previously unoccupied real left vertices ought to enter the matching after deletion. That is a genuine mathematical question. The source comments appeal to alternating components, but a comment does not establish that a restricted optimum is globally optimal.

Here we can name a checked theorem. `Shared/TransposedMatchingDeletion.lean` proves `transposed_repair_global_minimum`. Its hypotheses include the old rectangular feasible dual, zero potentials on unused old columns, a feasible and tight repaired square assignment, and a bound on how much the warm repair increased the nonroot row potentials relative to the root. Its conclusion says that the repaired assignment, lifted through the original occupied-column injection, is globally minimum for the full rectangular zeroed-row problem. In other words, it justifies the restricted-column argument under explicit certificate assumptions.

The theorem has an instructive proof strategy. Normalize the repaired row potentials by subtracting the repaired root potential. Extend the repaired column potentials to every original column, assigning zero outside the previously occupied set. On occupied columns, repaired feasibility applies. On previously unused columns, old feasibility and the row-growth bound establish the missing inequalities. Tightness survives for every selected edge. The extended potentials certify optimality on the full rectangular instance, not merely the small square one.

There is another Lean result named `dummy_initialization` that justifies the finite minimum used to choose the dummy row's starting potential. And `warm_rows_adjust` explains how a sequence of nonnegative potential updates preserves the required growth invariant. These are substantive pieces of the transposed-case mathematics. To finish the source proof, one must connect the exact updates in `AssignmentState.augment_row` to those hypotheses and prove the representation remains valid through reconstruction. The existing theorem is not itself a verification of the production floating-point repair.

## The exact-integer reference is a different program

At this point the repository can be misleading if we speak of 'the verified deletion solver' without saying which function we mean.

In `verified_assignment_core/src/deletion.rs`, the function `max_weight_matching_deletions` really is source-verified by `Rust.MatchingDeletionEntrypoint.max_weight_matching_deletions_total_spec`. It handles signed optional integer weights, preserves the original matrix indices, returns exact totals, reuses the base matching when the deleted vertex is unmatched, and otherwise calls the previously verified single-instance solver again. This is a correct reference family, not the production one-augmentation implementation.

There is a different exact-integer helper, `repair_deleted_sparse_vertex`, in `verified_assignment_core/src/sparse_deletion.rs`. Under its declared feasible and tight old-assignment conditions and numeric envelope, `Rust.SparseDeletion.repair_deleted_sparse_vertex_spec` proves the actual source caller: it projects surviving vertices, carries the duals, repairs a one-pair deficit with a single sparse augmentation when needed, and returns original-index labels. Its repaired flag distinguishes a genuine augmentation from an already fixed deleted vertex.

This is much closer to the optimization we want, but it still does not prove the public optimized family. The sparse helper expects an already constructed square assignment and valid numeric certificate. The exact reference family does not call it to construct all of its answers. The production graph solver instead uses a rectangular Hungarian state with floating-point values and a separate transposed-row strategy. Its tree callers also construct the child-branch weight matrices and reconstruct subtree witnesses around the returned matching pairs.

So we have at least three different things: a proven reference family that may recompute; a proven conditional exact-integer sparse repair caller; and a fast production floating-point family whose complete source theorem remains open. They are related by mathematics, not by identity of source code.

## Designing the theorem chain, one boundary at a time

A workable proof program starts with a pure functional specification. For an admissible optional-weight matrix, define a family to be correct when the base is independently maximum, every returned deletion answer is independently maximum on its corresponding masked instance, and every returned pair uses valid original indices. The definition should account for the production representation: an absent stored replacement means the base is reused, not that there is no maximum.

Next define a representation relation between `AssignmentState` and an abstract rectangular assignment with potentials. State precisely the one-free-row condition after a matched deletion, the compact-to-original coordinate maps, and the exact meaning of the transposed Boolean. Every internal vector length, sentinel and assignment index belongs in this relation. This is the point at which the mathematics becomes a statement about the source representation rather than a parallel algorithm in Lean.

Then prove local transitions. Validation establishes the matrix and arithmetic preconditions. The initial solve establishes a feasible tight certificate. The unmatched branch preserves the independent maximum. The direct matched branch deletes a column and uses one augmentation. The transposed branch uses the dummy-row initialization and the occupied-column theorem. The decoder preserves compatibility, uniqueness, positive-profit selection, score and original labels. The family loop must retain correctness of all previous entries as it appends the next one.

Notice the modularity. We can prove a correct `without_right` accessor and family encoding without proving the Hungarian search. We can prove the unmatched branch by transporting the already checked `IsMaximum.deleteRight`. We can prove index translation independently of weighted optimality. And we can state the augmenting-path theorem against an abstract cost oracle before connecting it to the closure that reads an actual input matrix.

The hardest functional bridge is likely the optimizer itself: making the production `augment_row` implementation satisfy the certificate-preservation and eventual-tightness theorem, including the transposed repair. The exact sparse reference proof offers a template, but not a shortcut that erases different representations and arithmetic.

## Where the work bound comes from

Now that we understand what a successful repair is, we can count the work of one family. Let k be the smaller side size and l the larger side size, with k positive. The production hard branch uses k assignment rows and at most k plus l assignment columns. Building and solving the original rectangular Hungarian problem has on the order of k squared times l primitive arithmetic work. A single augmentation can visit at most k row stages, scanning on the order of l columns per stage, so its dense work is on the order of k times l.

How many augmentations do we perform after the base solve? Not l, even though there can be l different right deletions. Only a right vertex present in the base matching triggers one. The base has at most k real pairs, so there are at most k such deletions. All repairs together therefore cost on the order of k squared times l, the same order as the base solve. The remaining deletion entries need only constant bookkeeping or reuse. Reading and validating the matrix and building result vectors contribute lower-order or comparable work when k is positive.

That argument is a source-informed operation-count sketch. To make it a Lean resource theorem, we would give the source operations a declared cost semantics, show that each pass through the augmentation loops contributes bounded work, and prove that the outer family loop invokes augmentation at most k times. Actual vector capacities, sorting, copying and weight accumulation also need charges. For the transposed branch, the square repair uses k columns, so this general k times l bound is conservative. We do not need to assert a particular machine instruction count to get a legitimate abstract big-O theorem.

Memory needs a separate proof. The family stores one base matching and at most k materialized repaired matchings, each using at most k pairs. That suggests on the order of k squared retained pair cells, plus one entry for each original right vertex. `Complexity/MatchingFamilies.lean` already proves a mathematical tagged-pair counting bound and aggregates degree-indexed families over trees. But a live Rust `Vec` has length, capacity, allocation metadata and possibly temporary buffers. The input matrix and the child-witness tables also occupy memory. A mathematical pair-cell theorem is not a bound on the peak resident memory of the whole program.

A useful source work certificate would thus distinguish at least four quantities: the number of family deletions visited, the number of actual augmentations, the number of reduced-cost cells examined, and the number of pair cells copied or retained. A cache-wide theorem can later aggregate these costs over the specific child-branch matrices built by the tree dynamic program. Without that last link, even a fully verified matching-family cost does not automatically imply Theorem 4 or Theorem 15 for a complete tree solver.

## Floating-point arithmetic is a separate boundary

The production `Weight` is a floating-point type. The code validates finite input weights and asserts that intermediate arithmetic and returned totals stay finite. It uses strict comparisons for selecting positive edges and reduced-cost improvements. These details are real parts of the implementation's contract.

An exact ordered-ring proof says that two algebraically equal expressions can be exchanged without changing a comparison. Floating-point addition does not generally have that property. Rounding can also make a theoretically zero reduced cost slightly positive or negative. A termination, no-panic and numerical-correctness theorem for this production function would therefore need explicit floating-point assumptions or an implementation-oriented error policy. Merely importing the exact integer or exact real matching theorem does not prove that the floating-point code always returns an exact mathematical optimum.

There are several possible research directions. One could introduce a separate exact-arithmetic reference path for which the mathematical theorem applies literally. One could prove a floating-point result under quantitative separation and no-overflow hypotheses. Or one could specify the program's observable floating-point result relative to a rounded operational semantics, then prove a more modest guarantee. Which is appropriate depends on the project's promised API. The current source does not supply the finished correspondence, so the lecture does not manufacture one.

## Finally, reconnect the matching family to trees

The fast family exists because one vertex of the right tree must be considered with several choices of excluded parent direction. In `tree.rs`, a sufficiently branching rooted-isomorphism state constructs one child-weight matrix, invokes `max_weight_bipartite_matching_with_right_deletions`, uses the base matching for the whole view, and uses each deletion result for the corresponding excluded right view. The embedding solver also creates related right-view families from its mapped and skipped child candidates. Its scoring and witness construction are different, but it consumes the same family abstraction.

A theorem about the matching function can guarantee that these pairs solve their input matrices. A second theorem must show that each matrix entry means the independently defined best score for that child pair. A third must show that the selected child witnesses assemble into a legal subtree isomorphism or topological embedding and carry the correct total score. A fourth must show that the table schedule supplies each needed child value before it is read. The source index relationship between a right neighbor and its excluded view must survive all of these layers.

The final runtime proof then combines the family work bound with the tree's degree sums and with the chosen evaluation schedule. This is the conceptual route from one saved Hungarian assignment to a theorem about the running time of a complete common-subtree solver. Every intermediate theorem should say exactly what it establishes, so a missing implementation bridge cannot hide behind a correct recurrence.

## A practical stopping point

We can now state a concrete proof-development order. Begin with the existing `WeightedMatching.IsMaximum.deleteRight` and `deletion_repair_card_bound`. Read the source's `WeightedMatchingFamily` and prove what `None` and `Some` mean as observable results. Connect base assignment arrays to a mathematical feasible and tight certificate. Handle original-label decoding. Prove direct column-deletion repair and the transposed zero-row repair as separate transitions. Compose them into the family loop. Only then attach a work trace and charge the augmentations, copies and allocations. Finally, connect the family contract to the two tree callers.

That is not the same as demanding one enormous theorem before any useful progress can be made. The repository already contains several of the pieces, including an exact-integer source-correct reference and an independent mathematical theorem for the transposed restriction. The next contribution can target one narrow interface: for instance, a production state-to-assignment invariant, or the correctness of the original-index readback in the direct repair branch. Each interface should eliminate a real assumption from the eventual complete theorem.

A good formalization does not merely repeat a paper's proof in a language that a checker understands. It establishes that the objects named by the proof are the objects actually computed by the program. In this example, that means the same deleted neighbor, the same optimum, the same pair indices, the same dual certificate, and a count of the operations the source really performs. The mathematics supplies the reason one repair is sufficient. The remaining formal work is to make that reason apply to this implementation.

<!-- END SPOKEN LECTURE -->

## Source and theorem companion (not narrated)

The claims below describe the **2026-11-19 supplied `networkx_algo_common_subtree` source snapshot**. Proposed theorem interfaces are marked as proposals and are **not** existing Lean declarations.

### Independent objective

For an `a × b` optional-weight matrix `W`, let `M(W)` be valid compatible partial injections, with objective

\[
\operatorname{opt}(W) = \max_{m\in M(W)}\sum_{(i,j)\in m} W_{ij},\qquad
W\setminus j\text{ forbids all pairs incident to original right index }j.
\]

The family postcondition is `base ∈ argmax M(W)` and for every `j < b`, `without_right(j) ∈ argmax M(W \setminus j)`, including original index labels, pair uniqueness and checked score. The production representation uses `deletions[j] = None` to share the base; this is **not** an absent optimum.

### Exhaustively checked two-by-three example

| | P | Q | R |
|---|---:|---:|---:|
| Alice | 9 | 6 | forbidden |
| Bob | 8 | 7 | 5 |

| Request | Maximum pairs | Score | Repair type |
|---|---|---:|---|
| Original | Alice–P, Bob–Q | 16 | Initial solve |
| Delete R | Alice–P, Bob–Q | 16 | Reuse |
| Delete Q | Alice–P, Bob–R | 14 | One direct reassignment |
| Delete P | Alice–Q, Bob–R | 11 | Alternating path through Q |

### Actual-source paths to read

- `rust/crates/common_subtree_algorithms/src/matching.rs`: `WeightedMatchingFamily::without_right`, `max_weight_bipartite_matching_with_right_deletions`, `AssignmentState::solve`, `AssignmentState::augment_row`, `matching_from_pairs`. The production routine uses floating-point `Weight`, a lazy right-deletion result vector, a direct column-deletion branch, and a transposed zero-row/occupied-column branch.
- `rust/crates/common_subtree_algorithms/src/tree.rs`: `compute_rooted_isomorphism` and the embedding-family assembly path (search for `max_weight_bipartite_matching_with_right_deletions`). They build child matrices, map excluded right views, and materialize subtree witnesses.
- `rust/crates/verified_assignment_core/src/deletion.rs`: **verified** exact-integer reference family; matched deletions are re-solved with the single-instance reference solver.
- `rust/crates/verified_assignment_core/src/sparse_deletion.rs`: `repair_deleted_sparse_vertex`, a **different** exact-integer source-verified, conditional single-augmentation caller.
- `proofs/SubtreeProofs/Shared/MatchingDeletion.lean`: `WeightedMatching.IsMaximum.deleteRight`, `deletion_repair_card_bound`, and the independent reference deletion family.
- `proofs/SubtreeProofs/Shared/CopiedMatchingDeletion.lean`: `matched_deletion_ready`, `deletion_preserves_tight`.
- `proofs/SubtreeProofs/Shared/CopiedMatchingRepair.lean`: `matched_single_cycle_repair`.
- `proofs/SubtreeProofs/Shared/TransposedMatchingDeletion.lean`: `dummyBaseline_spec`, `dummy_initialization`, `warm_rows_adjust`, `transposed_repair_global_minimum`.
- `proofs/SubtreeProofs/Rust/MatchingDeletionEntrypoint.lean`: `max_weight_matching_deletions_total_spec` for the exact-integer **reference** API.
- `proofs/SubtreeProofs/Rust/SparseDeletionEntrypoint.lean`: `repair_deleted_sparse_vertex_spec` for the exact-integer **conditional repair** caller.
- `proofs/SubtreeProofs/Complexity/MatchingFamilies.lean`: mathematical retained-pair bounds, not Rust peak-allocation bounds.
- `docs/planning/paper_statement_crosswalk.md` (2016 Lemma 6 and Theorem 7; 2018 Lemmas 13–14 and Theorem 15) and `proofs/PROOF_STATUS.md` (2026-11-14 matching progress) delimit the existing proof frontier.

### Proposed proof interfaces, not existing Lean declarations

1. **Family representation.** For each valid deleted index, `without_right` returns either a shared base proof when its deletion slot is `None`, or a separately represented matching from a `Some` slot. Invalid indices produce no result. The base, repaired pairs, and scores use original input labels.
2. **Assignment-state invariant.** The Hungarian arrays describe an injective row-to-column assignment, feasible dual potentials and tight selected edges, with sentinel-index safety. The initial solve establishes it. An unmatched deletion preserves the old certificate. A matched deletion yields exactly one free row plus retained tight edges.
3. **Two repair refinement theorems.** The nontransposed path projects the old column assignment and performs one sound augmentation with compact-to-original readback. The transposed path discharges `dummy_initialization` and `transposed_repair_global_minimum`, with an explicit warm-update invariant, before original-left-index readback.
4. **Whole-family correctness.** Compose validation/fast paths, initial solve, at most `min(a,b)` repairs, result appends and reconstruction. Separately state numerical behavior for finite `f64`, NaN/overflow rejection and exact-versus-rounded comparison semantics.
5. **Work and space.** In a declared dense arithmetic model, with `k=min(a,b)>0` and `l=max(a,b)`, bound the base solve by `O(k²l)`, each augmentation by `O(kl)`, the count by `k`, and retained matching pairs by `O(k²)` plus `b` deletion slots. Prove source-operation/copy/allocation correspondence separately. Neither the pure bound nor the exact-integer caller implies a whole-tree or Python/NetworkX resource theorem.

### Primary sources

- Droschinsky, Kriege, and Mutzel (2016), *Faster Algorithms for the Maximum Common Subtree Isomorphism Problem*, pinned arXiv v4, Lemmas 5–6, Algorithm 2 and Theorems 4/7: https://arxiv.org/pdf/1602.07210v4
- Droschinsky, Kriege, and Mutzel (2018), *Largest Weight Common Subtree Embeddings with Distance Penalties*, pinned arXiv v1, Lemmas 12–14 and Theorem 15: https://arxiv.org/pdf/1805.00821v1
