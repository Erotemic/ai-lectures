# One Deletion, One Augmentation: Droschinsky 2016, Lemma 6

<!-- BEGIN SPOKEN LECTURE -->

Suppose you have already solved a difficult matching problem. You know which edges form an optimum. You may even have the dual potentials that certify its optimality. Then somebody removes one vertex and asks you to solve the problem again. It is possible that the old answer is still valid. If it is not, perhaps most of the old computation can survive.

That is the situation inside the 2016 maximum common subtree isomorphism algorithm. At a fixed pair of candidate root vertices, the algorithm does not produce one unrelated matching graph after another. It produces a family of graphs that are almost the same. The first contains all candidate child pairings. Each other graph deletes one vertex from one side. Their surviving edges have exactly the same weights.

Lemma 6 of Droschinsky, Kriege and Mutzel turns that overlap into a time bound. It says we can compute an optimal matching in the original weighted bipartite graph, and an optimal matching after deleting each of the l right-side vertices, for the same asymptotic cost as the one rectangular matching bound from Lemma 5. Solving each deleted instance independently would lose that advantage.

The mathematical insight divides neatly into two cases. If a deleted vertex is unmatched in the original optimum, we already have the answer. If it is matched, the copied perfect-assignment representation is missing exactly one pair after deletion. A single augmentation can repair it. The word 'single' counts augmentation rounds, not the number of edges along a path. This distinction is central to both the proof and the complexity calculation.

## Why tree dynamic programming generates deletion families

Choose one vertex u in the first tree and one vertex v in the second. The 2016 algorithm fixes an orientation on the first tree, so u has a definite set of children. On the second tree, v can be considered as the root of the whole tree, or as the child of any of its neighbors when the ambient root lies across that neighbor.

When the second tree is rooted at v itself, every neighbor of v is a child and is available for a branch match. When it is rooted across one neighbor, that neighbor becomes the parent and cannot also be used as a child. The other neighbors remain available. Therefore the corresponding matching graph loses precisely the vertex for that excluded neighbor.

There is a further condition that should not be skipped. The matching edge weights for the *surviving* neighbor pairs must stay the same. For a neighbor other than the excluded parent, the descendant component extending away from v is unchanged. The same smaller rooted subtree problem is used, and the same incident-edge reward is added. Only one candidate branch disappears; the surviving branch weights are not recomputed under a different definition.

Thus, at fixed u and v, the all-neighbors graph and the one-neighbor-deleted graphs form a natural family. The paper calls them similar matching instances. Lemma 6 applies exactly because their only differences are deletions, not arbitrary changes to scores or the addition of new edges.

This is already a refinement of the dynamic-programming cost story. We need to count not only how many table entries exist, but also how many distinct matching computations are necessary after sharing work among closely related entries.

## An explicit family: delete P, Q, R, or S

Let us reuse a small bipartite instance. On the left are Alice and Bob. On the right are P, Q, R and S. Alice has candidate weights eight to P, six to Q, one to R and negative two to S. Bob has nine to P, two to Q, four to R and zero to S. We discard the negative edge. The maximum partial matching uses Alice to Q, worth six, and Bob to P, worth nine. Its weight is fifteen.

Now delete right vertex R. Neither selected edge touches R. The old matching is still legal and still scores fifteen. No matching in the smaller graph can exceed fifteen, because every matching feasible after deleting R was already feasible in the larger graph. So fifteen is still optimal.

Delete S instead. The same reasoning applies. The original matching never used S. The answer remains fifteen, despite the fact that S had an allowed zero-weight edge to Bob. No path search, no assignment reset, and no reoptimization is needed for either deletion.

Deleting P changes the situation. Our old optimum used Bob to P, so it is no longer legal. After removing P, Alice can still pair with Q for six and Bob with R for four. That gives a matching of weight ten. We can compare all pairings: pairing Alice with R and Bob with Q yields three, while a single remaining edge is worth at most six. So ten is optimal.

Deleting Q also invalidates the old optimum. Now Alice to P and Bob to R give eight plus four, or twelve. That beats Alice to R and Bob to P, which would score one plus nine, or ten; it also beats any single surviving edge. The optimal deletion-family values, in the order P, Q, R and S, are ten, twelve, fifteen and fifteen.

All four answers came from one original matching instance. Two were obtained for free by reuse, while two required genuine recomputation. There are four right vertices but only two matched right vertices in the original optimum. This is not an accident of our numbers; it is a counting argument that survives at any size.

## The unmatched-vertex theorem

Let B be the original graph and M one of its maximum-weight matchings. Take a right vertex z that M does not use. Then M is also a legal matching in B with z removed. Let OPT denote the original maximum weight and OPT without z the deleted-instance maximum.

Because B without z has fewer allowed matchings, OPT without z cannot exceed OPT. On the other hand, M itself survives and has weight OPT, so OPT without z is at least OPT. Both inequalities force equality. The original matching is already optimal in the deleted graph.

We did not assume M was the only optimum. There may be several optimal matchings, and the result needs only one of them. If z happens to be used by another optimum but not by our chosen M, that is irrelevant. Reuse is justified relative to the actual M we hold.

For a valid matching between k left vertices and l right vertices, at most the smaller of k and l right vertices can be matched. Every matched edge uses exactly one distinct right vertex and one distinct left vertex. Therefore at most min of k and l deletions can require repair. All the others are already answered by M.

Notice that this is an upper bound on the *number of repairs*. It says nothing yet about how expensive one repair may be. A repair might change many matched pairs, and finding the right alternating path might be difficult. Lemma 6 obtains its time bound by combining this counting fact with the special copied-graph assignment algorithm from Lemma 5.

## Why a matched deletion leaves one missing assignment edge

Recall the copied graph construction. For every original vertex there is a copied vertex and a zero-weight identity edge. Its two assignment sides each contain k plus l vertices. An optimal perfect assignment on this graph consists of k plus l edges and decodes to a maximum-weight partial matching in the original graph.

Suppose the deleted right vertex z is matched in that decoded original matching. To represent its deletion in the copied graph, remove both the original z and the copied z. They belong to opposite assignment sides, so the reduced copied graph still has equally sized sides, each of size k plus l minus one. A perfect assignment on the reduced graph must therefore contain k plus l minus one edges.

Before deletion, original z belongs to one assignment edge, and copied z belongs to a different assignment edge. Why are the edges different? An original right vertex that is matched through an original graph edge cannot simultaneously use its zero-weight identity connection. Its copied counterpart is consequently matched somewhere else in the copied part. Removing z and its copy deletes two distinct matching edges.

Keep all other edges of the old perfect assignment. There were k plus l old edges, and we removed two. We are left with k plus l minus two edges. But the new perfect assignment requires k plus l minus one. We are short by exactly one.

Equivalently, there is one unmatched row and one unmatched column in the surviving copied graph. The retained edges still do not conflict. They also remain tight under the old dual potentials, because none of their weights or endpoint potentials changed. The original feasible dual inequalities remain feasible when we restrict them to a graph with fewer allowed edges.

This is an unusually favorable starting point for a primal-dual assignment routine. We have not forgotten the matching. We have not forgotten the dual certificate. We have a feasible and tight almost-perfect assignment with exactly one missing edge. One augmentation is enough to return to a perfect assignment, and the algorithm's dual updates can retain feasibility and restore tightness on the selected edges.

The paper states this idea using its augmentation subroutine, which it calls APM. Starting from the old optimal perfect assignment minus the two incident edges, one APM iteration solves the reduced copied assignment. Decoding the result gives a maximum-weight partial matching after the right-vertex deletion.

The proof uses complementary slackness in the same way as Lemma 5. A final perfect assignment on tight edges reaches the upper bound supplied by its feasible potentials. A different matching of the deleted graph cannot beat it. We do not need to assert that a particular local edge replacement is always optimal; we let the augmentation find a valid path and adjust potentials when necessary.

## One augmentation may rearrange several branches

Our four-right-vertex example shows why the repair is not merely 'subtract the weight of the deleted edge.' The original optimum was Alice to Q and Bob to P, scoring fifteen. Delete Q. If we simply drop Alice to Q, we retain Bob to P, scoring nine. We need to find an additional edge without violating the matching constraints.

One obvious move is Alice to R for one. That would give ten, not the optimum twelve. A better repair changes the surviving assignment as well. Alice moves to P for eight. Bob moves away from P to R for four. Now both left vertices are matched and the weight is twelve.

In ordinary matching language, the rearrangement follows an alternating path. Start at the now-unmatched Alice. Consider the available edge Alice to P. P is occupied by Bob, so move along the currently matched edge P to Bob. Then consider Bob to the free right vertex R. Flipping the path removes the old Bob-P pair and inserts Alice-P and Bob-R. The matching cardinality grows from one to two.

The weight change along this path is eight minus nine plus four, a net gain of three over the retained weight nine. Directly matching Alice to R would gain only one. The weighted problem therefore has to select a profitable augmenting route, not just any augmenting route.

When we describe the paper's single augmentation in the copied graph, we should not identify it with this exact three-edge path. The copied graph includes additional identity and mirrored edges, and a weighted primal-dual algorithm may move through that larger structure. The small original path is an illustration of the necessary rerouting. The proof of Lemma 6 works at the copied-assignment level, where feasibility and tightness can be maintained systematically.

The conceptual point is that one augmentation can flip many edges. A single augmenting-path search can be linear, or worse under some data structures, in the graph size. The efficiency comes from paying for only one such search per affected deletion, not from assuming every repair is constant time.

## Count the total work of the family

Let k and l be the original side sizes. We do not yet assume which is smaller. Let s be the smaller of k and l, and t the larger.

Lemma 5 computes the initial maximum matching, together with its copied-assignment certificate, within time proportional to k times l times the sum of s and log t. One augmentation on a copied graph costs on the order of t times the sum of s and log t, using the paper's sparse Hungarian implementation and heap assumptions.

How many deleted instances need such an augmentation? At most s. Multiply those two factors. The entire collection of repairs takes time on the order of s times t times the sum of s and log t. But s times t is exactly k times l. The family cost is therefore of the same order as the initial matching cost.

Written in the paper's notation, Lemma 6 says that all the maximum-weight matchings for B and the graphs obtained by deleting each of its l right-side vertices can be computed in total time proportional to k times l times the sum of the smaller side size and the logarithm of the larger side size.

For the earlier two-by-four example, the difference is visible even before asymptotics: four deletion queries, but only two of them require repair. For a two-by-ten-thousand example, at most two right-side deletions can disrupt the chosen matching, while the other nine thousand nine hundred ninety-eight reuse the existing optimum. The family has many outputs, but the number of costly updates is controlled by the smaller side.

There is one cost qualification worth making explicit. If an API insists on allocating and copying a complete distinct matching list for every deleted vertex, output materialization has a cost of its own. The paper's bound accommodates the size scales of the family under its chosen representation; an implementation's exact work needs to account for copying, data structures and returned witnesses rather than silently treating shared matchings as physically duplicated for free.

## A proof-reading route through Lean

The supplied formalization has a clean independent statement of the first case. In `Shared/MatchingDeletion.lean`, the function `deleteRight` makes the deleted right column unavailable while retaining the original indices of surviving columns. The theorem `IsMaximum.deleteRight` proves optimality of the old matching when the deleted vertex was not selected. The theorem `deletion_repair_card_bound` proves that at most the smaller side's cardinality can require repair.

These are not implementation facts. They speak about weighted finite matchings and independent maxima. Their value is that they expose the structural reason for reusing results, free of Rust indexing conventions or Hungarian data structures.

The copied-assignment layer then formalizes the matched case. `CopiedMatchingDeletion.lean` proves that deleting an original matched right vertex and its copy leaves exactly one missing pair in the surviving assignment. The theorem `matched_deletion_ready` packages that deficit and its free endpoints. `deletion_preserves_tight` establishes that the remaining selected edges keep their tightness under the previous potentials.

The file `CopiedMatchingRepair.lean` contains `matched_single_cycle_repair`, an existence-and-optimality result for repairing the deletion using one reassignment cycle. This result is mathematical: it can use finite independent minimization to establish the existence of a suitable optimal repair. It is not, by itself, a bound on the time an implementation spends finding that cycle. A companion theorem, `matched_single_cycle_decodes`, carries the repaired assignment back to the original indexed matching problem.

Other source theorems make the certificate argument explicit. `deletion_preserves_dual_feasible` shows the old feasible potentials restrict to the surviving graph. `feasible_tight_decodes` connects the final dual certificate to independently maximum decoded matchings. The theorem `normalize_tight` supports the same-dual normalization used by the source development. These are genuine mathematical verification results; they should not be confused with an assumption that the production algorithm always enters the repair routine with a valid old state.

There is also more actual Rust-source verification than a purely paper-level lecture might suggest. The uploaded snapshot includes a total-correctness proof for the exact integer reference deletion-family API, named `max_weight_matching_deletions_total_spec` in `Rust/MatchingDeletionEntrypoint.lean`. It proves the returned family against independently optimal deleted instances, with the API's own shape and error contracts.

Separately, `Rust/SparseDeletionEntrypoint.lean` proves the reference sparse repair caller under its stated old copied-graph numeric invariant, and `Rust/SparseAugmentationEntrypoint.lean` proves its generic one-deficit augmentation helper. Those results carry substantial responsibility for termination, arithmetic and returned indices. They do not establish the paper's priority-queue runtime, the optimized production graph caller, or floating-point equivalence. It is possible to have the exact reference behavior proved while the asymptotic improvement still awaits a cost theorem and integration proof.

The right way to read this formalization is as a stack of independently meaningful claims. First, deletion changes the feasible matching family. Second, unmatched deletion preserves an optimum. Third, matched deletion leaves a one-edge deficit in the copied assignment. Fourth, feasible dual values and tight selected edges are preserved where they survive. Fifth, an optimal repaired assignment exists and decodes correctly. Sixth, an executable reference can implement the repair under precise numeric invariants. Seventh, a future resource theorem must bound the actual operations along that source path. Each step has a separate statement and a different proof burden.

## What Lemma 6 buys the tree algorithm

The final step is to put the matching family back into the tree problem. For a fixed left-tree vertex u and a fixed right-tree vertex v, the all-neighbors matching instance corresponds to using v as its own root. Each alternative right-tree orientation excludes one neighbor of v. This is exactly a one-vertex deletion from the all-neighbors instance. Therefore the algorithm can compute one expensive base matching and obtain the rest through unmatched reuse and single-augmentation repairs.

This does not yet finish the full running-time proof for common subtree isomorphism. We still have to add the cost of all those families across all pairs u and v, account for the degree of each vertex, and show that the shared dynamic-programming values are available before they are used. Theorem 7 performs the matching-cost aggregation in the paper, and Theorem 4 applies it to the complete problem. Their claimed bound depends on the degree sums of the two input trees, not on pretending every local child set has maximum degree.

But the main local improvement is now complete in our mathematical understanding. Lemma 5 explains how to solve one rectangular maximum-weight partial matching with a specially initialized perfect assignment. Lemma 6 explains why a whole family of related matchings costs asymptotically no more: most deletions do nothing, and each of the few affected deletions inherits a nearly complete matching and dual certificate.

When reading an implementation, this should give us a concrete diagnostic. Does it retain the base matching? Does it keep the old dual information? When a matched neighbor is deleted, does it repair exactly one deficiency instead of starting over? And when proving the implementation, can we connect each of those operations back to an independent optimum and an explicit cost model? Those are the questions that turn the mathematics of this paper into useful formalization work.

<!-- END SPOKEN LECTURE -->

## Non-spoken companion: deletion-family arithmetic and proof boundaries

### Paper statement, Section 4, Lemma 6

For weighted bipartite `B=(V ⊎ U,E)` with `k=|V|`, `l=|U|≥2`, `U={u_1,...,u_l}`, and `B_j = B[V ⊎ (U\{u_j})]`, compute maximum-weight **partial** matchings for

\[
B,B_1,\ldots,B_l\quad\text{in total}\quad
O\bigl(kl(\min\{k,l\}+\log \max\{k,l\})\bigr).
\]

The phrase *in total* is essential: it is not a per-deletion cost.

### Worked instance (same as 012000)

| `w` | P | Q | R | S |
| --- | ---: | ---: | ---: | ---: |
| Alice | 8 | 6 | 1 | forbidden (negative -2) |
| Bob | 9 | 2 | 4 | 0 |

| Graph | One optimal matching | Optimal weight | Repair required from `M={(Alice,Q),(Bob,P)}`? |
| --- | --- | ---: | --- |
| `B` | `Alice-Q, Bob-P` | 15 | Base computation |
| `B\P` | `Alice-Q, Bob-R` | 10 | Yes |
| `B\Q` | `Alice-P, Bob-R` | 12 | Yes |
| `B\R` | `Alice-Q, Bob-P` | 15 | No: reuse M |
| `B\S` | `Alice-Q, Bob-P` | 15 | No: reuse M |

For `B\Q` an ordinary alternating path starts at unmatched Alice and follows `Alice -> P -> Bob -> R`. Flipping changes retained `Bob-P` of weight 9 to `Alice-P` (8) and `Bob-R` (4), gain `8-9+4=3`, yielding score 12. This is an explanatory original-graph path, *not* a claim that the copied assignment takes exactly that path.

### Unmatched deletion proof

If `M` maximizes B and `u_j` is unmatched in M, then M survives in `B_j` and

\[
\operatorname{OPT}(B_j)\le\operatorname{OPT}(B)=w(M)
\le\operatorname{OPT}(B_j).
\]

Thus `OPT(B_j)=OPT(B)` and M is itself optimal in `B_j`. At most `min{k,l}` right vertices are matched by M, so at most that many deletions need repair.

### Matched deletion in the copied perfect assignment

The original `B'` has `k+l` rows, `k+l` columns and an optimal perfect assignment `A` with `k+l` edges. For matched original right `u_j`, delete `u_j` **and its copy** `u_j^C` (opposite assignment sides). The reduced assignment requires `k+l-1` edges. Since two distinct edges of A were incident to these removed endpoints, retaining the rest gives `k+l-2` edges. There is precisely **one unmatched row and one unmatched column**.

- Old dual feasibility restricts to the induced surviving graph.
- Retained matching edges stay tight with respect to old potentials.
- One primal-dual augmentation can restore a perfect, tight matching, potentially changing many individual edges.
- A perfect tight assignment under feasible potentials is optimum; decoding returns an optimum for the original deleted instance.

Let `s=min{k,l}`, `t=max{k,l}`. Paper per-augmentation cost: `O(t(s+log t))`. Up to `s` matched deletions require augmentation, hence

\[
O(s\,t(s+\log t)) = O(kl(\min\{k,l\}+\log\max\{k,l\})).
\]

### Why this is the same family generated by the tree recurrence

For a fixed left vertex `u` and right vertex `v`, the right branch set with ambient root `s=v` is `N(v)`. With ambient root `s=w∈N(v)`, it becomes `N(v)\{w}`. For `c≠w`, the outward descendant subtree of `c` and the incident edge contribution are unchanged. Thus one base matching graph and its right-vertex deletion family cover the corresponding root-orientation subproblems.

### Verified theorems in the supplied 2026-11-19 snapshot

| Obligation | Lean declaration | File relative to `proofs/SubtreeProofs` |
| --- | --- | --- |
| Original-index deletion definition | `WeightedMatching.deleteRight` | `Shared/MatchingDeletion.lean` |
| Unmatched deletion preserves an independently maximum matching | `WeightedMatching.IsMaximum.deleteRight` | `Shared/MatchingDeletion.lean` |
| At most smaller-side repairs | `WeightedMatching.deletion_repair_card_bound` | `Shared/MatchingDeletion.lean` |
| Exact one-pair deficit on matched copied deletion | `CopiedAssignmentReduction.matched_deletion_ready` | `Shared/CopiedMatchingDeletion.lean` |
| Dual feasibility survives deletion | `CopiedAssignmentReduction.deletion_preserves_dual_feasible` | `Shared/CopiedMatchingInitialization.lean` |
| Tightness survives for retained pairs | `CopiedAssignmentReduction.deletion_preserves_tight` | `Shared/CopiedMatchingDeletion.lean` |
| Optimal single-cycle repair exists mathematically | `CopiedAssignmentReduction.matched_single_cycle_repair` | `Shared/CopiedMatchingRepair.lean` |
| Repaired matching decodes to original-index optimum | `CopiedAssignmentReduction.matched_single_cycle_decodes` | `Shared/CopiedMatchingDeletionDecode.lean` |
| Certificate implies independent decoded optima | `CopiedAssignmentReduction.feasible_tight_decodes` | `Shared/CopiedMatchingDuality.lean` |
| Exact integer reference family API total correctness | `MatchingDeletionEntrypoint.max_weight_matching_deletions_total_spec` | `Rust/MatchingDeletionEntrypoint.lean` |
| Exact reference sparse one-deficit call under old-state invariant | `SparseDeletion.repair_deleted_sparse_vertex_spec` | `Rust/SparseDeletionEntrypoint.lean` |
| Reference augmentation helper under its input invariant | `SparseAugmentation.augment_sparse_permutation_spec` | `Rust/SparseAugmentationEntrypoint.lean` |

**Unproved as a full source-cost chain in the snapshot:** paper runtime Lemma 6 on an actual optimized sparse/Rust implementation; Theorem 7's global aggregate cost; production 2016 graph DP refinement, f64 equivalence and Python/NetworkX end-to-end correspondence. Formal source correctness of a separate reference API should not be represented as a theorem about the production backend.

**Primary source:** Droschinsky, Kriege and Mutzel, *Faster Algorithms for the Maximum Common Subtree Isomorphism Problem* (2016), [MFCS 2016, Section 4, Algorithm 2, Lemma 6 and Theorem 7, pp. 33:8-33:9](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2016.33), original pinned [arXiv v4](https://arxiv.org/pdf/1602.07210v4). Source crosswalk: `docs/planning/paper_statement_crosswalk.md`; proof status: `proofs/PROOF_STATUS.md`.
