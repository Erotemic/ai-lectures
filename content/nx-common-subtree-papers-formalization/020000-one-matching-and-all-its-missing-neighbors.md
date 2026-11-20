# One Matching and All Its Missing Neighbors: Droschinsky 2018, Lemmas 12–14 and Theorem 15

<!-- BEGIN SPOKEN LECTURE -->

The largest weight common subtree embedding problem can be solved by a dynamic program with two states. One state selects the current pair of tree vertices. The other state allows one or both boundary vertices to be skipped, charging a penalty for the extra length of the realized path. At a selected pair, a bipartite matching chooses which branches to connect. These ideas give a correct algorithm, but they do not yet explain the running time announced in the 2018 paper by Droschinsky, Kriege, and Mutzel.

There is a fairly dramatic gap between having a recurrence and having a fast implementation of it. If we choose every possible root of the second tree and solve a fresh rooted dynamic program, we repeatedly encounter almost the same branches and matching problems. Every rerooting changes which neighbor is considered the parent. A vertex with four neighbors has four ways to exclude one neighbor, plus a view in which it excludes none. Those five views look like separate subproblems if we name them by their roots. Mathematically they differ in only one incident branch.

The last section of the paper exploits that resemblance. It does not invent a new notion of topological embedding. It asks a more operational question: how can we calculate all the rooted states needed by the unrooted reduction without repeatedly paying for the same work? Lemmas twelve, thirteen, and fourteen answer pieces of that question. Theorem fifteen then combines the pieces, including an evaluation order that prevents circular dependencies.

We will reconstruct the cost argument rather than merely recite its asymptotic bound. The final statement is a time proportional to the product of the input sizes and the smaller maximum degree, and space proportional to the product of the input sizes. We will also identify exactly where the proof depends on earlier matching algorithms and where a Lean or Rust implementation would need a different kind of theorem.

## What the rooted bound already tells us

Start with the simpler rooted problem. Let the first tree have n vertices and the second have m. Let the maximum degrees be Delta one and Delta two, and let Delta be the smaller of those two numbers. For a fixed pair of selected vertices, suppose the first has a children and the second has b children. The mapped-state recurrence asks for a maximum weight partial matching between two sets of those sizes. Each candidate edge between a first child and a second child represents a previously solved subtree embedding, including its possible path penalties.

The paper imports a rectangular weighted matching bound. For a complete bipartite instance, the matching can be computed in time proportional to a times b times the smaller of a and b. Now sum that cost over every pair of tree vertices. We do not need a sharp bound on every individual degree. The smaller of a and b is at most Delta, and the sum of all child counts in a rooted tree is exactly its number of edges, n minus one. Consequently the double sum is bounded by Delta times n minus one times m minus one, up to a constant. This is the rooted real-weight time bound of Theorem six: order n times m times Delta. The table of mapped and skipped values uses order n times m space.

There is a second rooted result for integral, bounded weights. An imported weighted matching algorithm improves the dependence on the smaller degree from Delta to its square root, with a logarithm in the weight scale. The paper states a time proportional to n times m times the square root of Delta times the logarithm of C times the smaller input size, where C bounds the integral label weights. The same section explicitly notes a qualification about the imported algorithm's space usage: a linear-space guarantee is not supplied by its source. We should not silently strengthen that into an unconditional space theorem for the integral variant. We should also remember that applying an integral matching theorem to the actual dynamic-programming weights requires those derived matching weights to satisfy the needed integrality hypothesis. A distance penalty allowed to be a real number makes that a proof obligation, not a formality.

For unrooted trees, the earlier structural result lets us fix the first tree's orientation, but not simply choose one root in the second and be done. The best solution is either represented by one of the rooted states, or it crosses a highest skipped vertex in the first tree and must be assembled by joining two descendant branches. The extra join can be evaluated cheaply once the right rooted states are available. Obtaining those states economically is the main challenge now.

## A vertex has neighbors, not a fresh tree for every root

Think of an unrooted tree as a collection of vertices and undirected edges. If we root it at some vertex s, each other vertex v has exactly one parent neighbor, and its children are all the remaining neighbors. If we reroot at a different vertex, v may get a different parent, but its local neighborhood itself does not change.

For purposes of the rooted recurrence, we can identify the orientation at v by naming the neighbor we exclude. There is also a special view in which we exclude no neighbor, corresponding to v as the root of the whole tree. Across every possible root, the distinct views at v are therefore just one full-neighborhood view and one view for each neighbor of v. A tree with m vertices has two times m minus two directed edges. Adding the m full-neighborhood views yields three times m minus two possible right-hand views. That is linear in m, not quadratic.

Pair every such right-hand view with each of the n left-hand vertices. There are only order n times m mathematically distinct table addresses to retain, even though they arise while considering many possible global roots. A space bound begins to come into focus. But a small number of table addresses does not guarantee a small amount of computation. We could still recompute the matching from scratch each time we visit one address.

There are two sorts of work in the recurrence. The skipped state repeatedly asks for the best continuation from among child regions. The mapped state repeatedly asks for a maximum-weight matching among those regions. Lemma twelve concerns the first sort: the repeated maxima. Lemmas thirteen and fourteen concern the second: the matching families.

## Lemma twelve: all the maxima after every exclusion

Fix a left vertex u and a right vertex v. Suppose the right vertex has neighbors Alice, Bob, Carol, and Dave, with previously computed continuation values eleven, seven, eleven, and minus three. The full-neighborhood maximum is eleven. If we exclude Dave, it stays eleven. If we exclude Bob, it stays eleven. If we exclude Alice, it is still eleven, because Carol supplies the same score. If we exclude Carol, Alice supplies it.

The right data structure needs to remember not merely the largest numerical value, but its origin, and enough information to recover the best different origin when that one is excluded. Keeping the two best candidates with distinct neighbor identities is sufficient. Each exclusion query then takes constant additional work after one linear scan of the neighbors.

If the top two values tie, as they do here, they must still be associated with distinct neighbors. Otherwise we might erroneously think that excluding Alice eliminates both elevens. This is the same top-two principle used for the cardinality-two join in the unrooted structural argument, but applied to a different objective. Here we want one continuation after excluding one neighbor, not two simultaneous common-tree branches.

The first kind of maximum looks down through children of u. Once the left tree's orientation is fixed, its child set does not change when the right tree is rerooted. Therefore those scans can be charged across left vertices using the identity that the sum of child counts is n minus one. The second kind of maximum scans right neighbors, and all exclusions at v are produced together by the top-two trick. Summing over right vertices uses the identity that the sum of undirected degrees is two times m minus two.

After multiplying by the possible choices in the other input, each entire family of scalar maxima costs order n times m. Lemma twelve states this conclusion with an explicit hypothesis: a sequence of computations exists in which every value needed for a maximum has already been calculated. The hypothesis is not decorative. If computing a maximum requires a table entry that itself requires the maximum we are currently computing, an optimistic work count will not make the algorithm executable.

The paper postpones that dependency problem until after it handles matching costs. We will do the same.

## Why the mapped states form deletion families

At a selected pair u,v, the mapped state assembles independent common-tree child branches by taking an optimal partial weighted matching. In a view where v has no excluded right neighbor, the bipartite graph has the left children of u on one side and all the neighbors of v on the other. Call this graph G.

Now give v a parent neighbor c. That neighbor is no longer a child. The matching graph is exactly G with c deleted and all incident candidate edges removed. Call it G sub c. If v has five neighbors, we need the optimum of G and the optima of five graphs obtained by deleting one right vertex. This is not six unrelated weighted matching instances. It is one related family.

The matching objective remains partial. An unmatched vertex contributes nothing. If a right vertex c is unmatched in an optimal matching M on G, removing c leaves M feasible with the same score. Any better matching after deletion would also have been feasible before deletion, contradicting optimality. Therefore the original optimum can simply be reused.

If c is matched, removing it destroys one chosen pair. The remaining pairs are still feasible, but they need not be optimal. A repair may rearrange several assignments. Importantly, it is enough to search for a single augmenting or alternating-path improvement relative to the matching we already have, rather than initialize a completely new matching problem. This is the idea behind the deletion-family reuse in the 2016 paper, but the 2018 paper needs to handle both sides of a potentially very rectangular graph.

Consider the numerical example from the 2018 paper's Figure three. There are three left vertices, called u one, u two, and u three, and four right vertices, v one through v four. Some edges are absent. The initially chosen matching pairs u one with v two for weight three, u two with v three for weight two, and u three with v four for weight three. Total weight: eight.

Delete v four. Simply discarding its matched edge gives the two remaining pairs with total weight five. But u three can now take v three for weight four, while u two becomes unmatched. The resulting valid matching contains u one to v two for weight three and u three to v three for weight four, total seven. The deleted optimum is seven, not five. We have repaired the matching, but we have not recomputed every pairing from the beginning.

The example is valuable because the repair is not just a new assignment for the deleted vertex's former partner. That partner may take a previously occupied vertex, forcing someone else out. A proof of repair must reason about alternating paths and the optimality certificate retained by the original matching. A code path that merely removes the chosen edge and returns the remaining score is incorrect.

## Lemma fourteen: the strongly rectangular case

Write s for the smaller vertex-set size in the matching graph and t for the larger. The original matching can be computed in time order s squared times t. The problem is to compute the optima after deleting each vertex on one selected side, either the smaller or the larger side, without paying that full cost for every deletion.

Lemma fourteen gives a family-wide bound: s to the fourth plus s squared times t. Let us see where the terms arise.

The paper adds zero-weight copy choices to allow a matching of exactly s edges in a modified graph. This step turns optional matching into a fixed-cardinality representation. It then computes one optimum of that fixed-cardinality instance. A deletion of an unmatched vertex is free to reuse, as before. When a matched vertex is deleted, the old matching loses one edge and has a single deficit.

The analysis differs slightly depending on which side contains the deleted vertex. If the deleted vertex lies on the large side, a matched deletion creates an unmatched small-side vertex. A maximum-gain alternating path can repair that deficit. If the deleted vertex lies on the small side, one uses the old occupied large-side vertices as a compact set of candidates and restores the fixed-cardinality representation with a zero-profit dummy choice. In both cases the paper describes a small directed auxiliary graph whose shortest path encodes the necessary matching adjustment.

The graph for a repair has order s vertices and at most order s squared edges, so the paper bounds a repair by order s cubed using a shortest-path calculation of the indicated type. At most s deleted vertices are matched by the original matching. So the total repair cost is order s to the fourth, not t times s cubed. The base graph, the initial optimum, and the bookkeeping contribute the s squared times t part. This establishes the bound claimed in Lemma fourteen.

There is a conceptual distinction between this proof and an implementation using a different assignment representation, such as a rectangular Hungarian solver with dummy columns. Both may exploit a one-pair deficit, but one does not automatically verify the other's array indexing, choice of dummy vertices, dual potentials, or arithmetic. We should preserve the paper's mathematical theorem while stating source-level refinement as a separate goal.

The fourth-power term may seem disappointing, but the authors use Lemma fourteen only where one side of the graph is very small compared with the other. Their split is especially clever because it lets two different algorithms cover the entire range of rectangular shapes.

## Lemma thirteen: two matching algorithms meet

Again let s be the smaller side and t the larger. If s is at least the logarithm of t, the earlier 2016 matching-family algorithm provides a bound of s times t times the sum of s and log t. Because log t is then at most s, the family bound simplifies to s squared times t.

Now consider the other case, where s is less than log t. Lemma fourteen offers s to the fourth plus s squared times t. For sufficiently large t, the square of log t is bounded above by a constant times t. Since s is smaller than log t, s squared is at most a constant times t. Multiplying by s squared gives s to the fourth bounded by a constant times s squared times t. The same family-wide bound follows: order s squared times t.

Notice what has happened. The paper has not shown that every individual deletion can be solved in time s squared times t. That was already possible for an individual matching. It has shown that the base instance and every deletion of one right vertex can be handled together within that bound. One family costs about what an inefficient method might spend on one member.

At a tree-vertex pair u,v, put s equal to the smaller of their relevant degrees and t equal to the larger. The cost of the whole related family is then degree of u times degree of v times the smaller degree, up to a constant. We obtain Lemma thirteen's conditional total-work statement by summing this over the n times m possible vertex pairs.

The smaller local degree never exceeds Delta, the smaller of the two trees' maximum degrees. Pull Delta outside the sum. What remains is the product of the sum of first-tree degrees and the sum of second-tree degrees. Each sum equals twice the number of edges in its tree, so the product is order n times m. The total matching work is therefore order n times m times Delta.

This double-sum calculation is short enough to fit on a line of mathematics, but we have now unpacked its entire dependency chain. It relies on the matching-family algorithms, the ability to reuse a family across right-parent exclusions, the summation of degree products, and a valid schedule that actually supplies all the needed edge weights before the family is solved.

## The dependency cycle that cost analysis alone cannot remove

There is one more obstacle. Fix a left vertex u and an edge v-w in the second tree. Some skipped-state values at u,v depend on right-hand continuation values at u,w. Reorient the right tree the other way, and the skipped-state values at u,w may appear to depend on values at u,v. Matching entries also depend on the two kinds of boundary state. If we simply write a recursive program that asks for the desired neighbor whenever a value is missing, we can travel around the same dependency cycle forever.

The paper describes a schedule in terms of main and sub instances. The main instance at a right vertex includes every neighbor. A sub instance excludes one neighbor. If the first request at a vertex pair is for the main instance, the algorithm solves it and immediately derives the related sub instances. If the first request is for a sub instance, the algorithm can solve that one without yet claiming the main instance is ready. When the second distinct sub instance is requested, the value missing from the first exclusion is now available. The main instance can be completed, and then all its other sub instances follow.

The reason this works is structural. Each apparent cycle crosses one edge of a tree. The two orientations of that edge do not create an arbitrary strongly connected computation graph. Once the required boundary information on the opposite side is present, the main-versus-sub family supplies the missing states. The schedule restricts which state can be demanded first and when a whole family may be completed. That is what allows the conditional Lemmas twelve and thirteen to be used together.

An implementation might express the same dependencies differently. The uploaded production Rust source processes left vertices in a postorder, completing the mapped matching families for the current left vertex from already completed left children. It then propagates skipped-state messages across the right tree in two passes. The first handles downward continuations; the second propagates exclusions using the best two incoming neighbors. This is a plausible executable realization of the paper's dependency discipline, but its loop structure is not itself a machine-checked proof of Theorem fifteen.

## Theorem fifteen and the last accounting step

The unrooted optimum was already divided into two structural cases. The first, often called M one, uses the best rooted states with the fixed first-tree orientation and varying right-tree orientation. The second, M two, joins two distinct descendant branches across a skipped highest vertex of the first tree, paying one central penalty. The two-best-child argument allows the additional join work to be bounded by order n times m, once the table states are available.

Lemma twelve bounds the scalar maximum work by order n times m. Lemma thirteen bounds the matching families by order n times m times Delta. The scheduling argument ensures these bounds can be realized without unresolved cyclic dependencies. The table uses order n times m values because right views correspond to full neighborhoods and directed edges. A single matching uses no more than the product of the two input sizes as scratch space, and the state table and recorded decisions fit within the same asymptotic envelope in the paper's model.

The resulting theorem gives an unrooted largest weight common subtree embedding in time order n times m times Delta, and space order n times m. It handles vertex and edge labels and the defined distance penalty. Unlike the rooted square-root-degree improvement, Theorem fifteen does not claim the same stronger bound for bounded integral unrooted weights. The authors explicitly leave the possibility of such an improvement as an open problem in their conclusion, noting that their imported weight-scaling methods are not immediately incremental across the matching family.

This is a good place to distinguish three statements. The paper has proved an asymptotic algorithmic bound under its abstract cost model. A Lean theorem may establish the numerical correctness of the rooted recurrence, independently of any optimized matching routine. And a production implementation may actually reuse all right-deletion matching instances, yet still lack a formal connection from its concrete floating-point operations and allocation behavior to the paper's bound. None of those statements replaces another.

The complexity proof is not an afterthought. It is a second mathematical construction layered on top of the correctness proof. The first construction says which embedding wins. The second shows that all the evidence required to choose that winner can be assembled by sharing work across locally related problems. The shared unit is neither one vertex nor one root-to-root comparison. It is a family consisting of one matching and all the matchings formed by deleting one of its neighbors.

Once that family is the unit of accounting, the global bound follows from an elementary identity about trees: total degree is twice the number of edges. That is a satisfying conclusion to a fairly intricate paper. Its hardest-looking local operation becomes manageable not because tree matching ceases to be difficult, but because the surrounding tree structure exposes exactly which matching instances should be solved together.

<!-- END SPOKEN LECTURE -->

## Companion: exact scope of the 2018 results

Let `n = |V(T)|`, `m = |V(T')|` and `Δ = min(Δ(T), Δ(T'))`. Let `deg_T(u)` be the unrooted degree; child counts in fixed rooted views are no larger.

**Theorem 6, rooted real-weight case.** From complete bipartite matching at a child-pair `(u,v)`:

\[
\sum_{u,v} |C_T(u)|\,|C_{T'}(v)|\min(|C_T(u)|,|C_{T'}(v)|)
\le \Delta\left(\sum_u |C_T(u)|\right)\left(\sum_v |C_{T'}(v)|\right)
=\Delta(n-1)(m-1).
\]

Time `O(nmΔ)`; score-table space `O(nm)`. The 2018 paper states a rooted bounded-integer improvement `O(nm sqrt(Δ) log(C min(n,m)))`, importing Lemma 8. The paper qualifies the associated integer-solver space bound. Derived edge scores and arbitrary real `p` require a separate exact-integrality audit before invoking an integer-only matching theorem.

**Lemma 12.** Given a valid dependency order, all reused scalar maximum queries across right-parent exclusions take `O(nm)` time. For neighbor scores `(11,7,11,-3)`, tracking two best **distinct-origin** candidates gives the exclusion maximum `11` regardless of the deleted neighbor.

**Lemma 14.** For a weighted bipartite graph `G=(U,V)` with `s=|U| <= |V|=t` and a family `G_c` deleting one `c` on either designated side, computing the base MWM plus the entire deletion family costs `O(s^4+s^2 t)`. Only at most `s` deleted vertices can be matched in the base optimum; the one-deficit repairs are bounded by `O(s^3)` each in the paper's auxiliary-graph construction.

**Lemma 13, family bound.** Split into `s >= log t` and `s < log t`. The first uses the 2016 family bound `O(s t (s+log t))`. The second uses Lemma 14 with `(log t)^2=O(t)`. Both give `O(s²t)` for the **entire** deletion family. Therefore

\[
\begin{aligned}
\text{total matching work}
&=O\left(\sum_{u,v}\deg_T(u)\deg_{T'}(v)\min(\deg_T(u),\deg_{T'}(v))\right)\\
&\subseteq O\left(\Delta \sum_u \deg_T(u)\sum_v \deg_{T'}(v)\right)\\
&=O\left(4\Delta(n-1)(m-1)\right)=O(nm\Delta).
\end{aligned}
\]

**Theorem 15.** Conditional maximum/matching work is made executable by the paper's *main/sub instance schedule*. Together with the structural unrooted `M₁/M₂` reduction and the `O(nm)` view count, this gives unrooted time `O(nmΔ)` and space `O(nm)`.

### Figure 3 example, independently checkable

Allowed edges and weights from MFCS 2018 Figure 3(a), rows `u1,u2,u3`, columns `v1,v2,v3,v4`:

| | v1 | v2 | v3 | v4 |
| --- | ---: | ---: | ---: | ---: |
| u1 | 1 | 3 | 2 | impossible |
| u2 | impossible | 2 | 2 | impossible |
| u3 | impossible | impossible | 4 | 3 |

Base matching `u1-v2 (3), u2-v3 (2), u3-v4 (3)` scores `8`. Deleting `v4` leaves the old remaining assignment at `5`, but `u1-v2 (3), u3-v3 (4)` scores `7` and is optimal. The graph also admits the tied optimum `u1-v1 (1),u2-v2 (2),u3-v3 (4)` scoring `7`. Deletion repair must allow reassignment.

### Proof boundaries in the November 19, 2026 repository snapshot

- Proved in Lean: independent topological-embedding/score specification, the mapped and skipped recurrence (`mapped_recurrence`, `skipped_recurrence_two_state`), the executable all-root-pairs score optimum (`RootedDP.unrootedOptimum_correct`).
- Open as paper-specific Lean proofs: the fixed-first-root structural `M₁/M₂` reduction (Lemmas 9–11), maximum exclusion families and evaluation order (Lemma 12), matching-family bound (Lemmas 13–14), exact optimized Theorem 15 resource theorem.
- Proved in `Complexity/MatchingFamilies.lean`: several **mathematical** pair-cell and tree-degree bounds used in 2016 matching-family models. These do **not** verify 2018 production allocations or its complete running time.
- Tested production features: `embedding_matching_family`, `compute_embeddings`, right-view IDs, two-pass skipped messages, right-deletion matching families, `M₂` split and witness reconstruction in `rust/crates/common_subtree_algorithms/src/tree.rs`. No full source-refinement/f64/running-time theorem is established by tests.

**Primary source:** Droschinsky, Kriege and Mutzel, [*Largest Weight Common Subtree Embeddings with Distance Penalties*](https://doi.org/10.4230/LIPIcs.MFCS.2018.54), MFCS 2018, Sections 4–5, especially Theorem 6, Lemmas 12–14 and Theorem 15. [Pinned arXiv v1](https://arxiv.org/pdf/1805.00821v1). This lecture's prose and explanatory decomposition are original; the Figure 3 matching data follow the paper.

### Listening checks

1. Why does `3m-2` count all distinct full-neighborhood and parent-exclusion right views, even though there are `m` possible right roots?
2. Why is the correct unit of matching analysis **one whole deletion family** rather than each of its member graphs?
3. What fails if a matching deletion simply removes the old paired edge without repairing it?
4. Which hypothesis is still missing when Lemma 12 or Lemma 13 claims a cost bound, and how does Theorem 15 close it?
5. Why does the rooted integer-weight improvement not automatically imply the same unrooted result?
