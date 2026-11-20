# From Optional Branches to a Perfect Assignment: Droschinsky 2016, Lemma 5

<!-- BEGIN SPOKEN LECTURE -->

A rooted common-subtree algorithm has to make a choice at every pair of roots. Which child of the first root should be paired with which child of the second? We have seen why the answer is a maximum-weight matching, rather than a sequence of locally attractive choices. Now we must ask how expensive that matching is, especially when one root has only a few children and the other has many.

Suppose a vertex in one tree has two available child branches, while a vertex in the other has fifty. There are one hundred possible branch pairings, but a legal common subtree can retain at most two of them. A generic assignment algorithm might construct a large square table, introduce dummy choices, and spend substantial work moving among rows and columns that cannot all participate in a nonempty pairing. Droschinsky, Kriege and Mutzel exploit the imbalance. Their Lemma 5 computes a maximum-weight matching between sides of sizes k and l, where k is at most l, in time proportional to k times l times the sum of k and log l.

That is a claim about an algorithm and its cost, not merely an existence theorem for a matching. To understand it, we will separate three ideas. First, how a matching that is allowed to leave vertices unmatched becomes a perfect assignment without changing its optimum. Second, how dual numbers certify that an assignment is optimal. Third, why the algorithm needs only k augmentation rounds, even though its constructed graph is larger than the original one. We will finish by identifying which parts have already been expressed and proved in Lean and which parts of the runtime claim remain open.

## The problem behind the subroutine

Start with a weighted bipartite graph. Its left side contains k vertices and its right side contains l vertices. Let us call the left side V and the right side U. Assume k is no greater than l. A matching is a set of edges in which no two share an endpoint. Its weight is the sum of the weights of its selected edges.

We are looking for a maximum-weight matching, not necessarily a maximum-cardinality matching. The distinction changes the behavior of negative weights. If every incident edge of some vertex is harmful, the matching can simply omit that vertex. The empty matching is legal and scores zero. It is therefore harmless to discard every strictly negative edge before solving the problem. No optimal solution needs one: deleting a selected negative edge leaves a valid matching and strictly increases its score.

What about zero-weight edges? They may appear in an optimum, but they do not improve its score. We can retain them or omit them, depending on the implementation. What we may not do is assume that an absent edge has weight zero. An absent edge is forbidden; a zero-weight edge is allowed. We must preserve that distinction when we construct the assignment problem.

Here is a small example to carry through the lecture. The left vertices are Alice and Bob. The right vertices are P, Q, R and S. Alice's candidate weights, in that order, are eight, six, one and negative two. Bob's are nine, two, four and zero.

The best choice is Alice to Q for six and Bob to P for nine, totaling fifteen. Alice to P and Bob to R total twelve. Alice to P and Bob to Q total ten. Alice to Q and Bob to R total ten. No single edge exceeds nine. The optimum is therefore fifteen. R and S are unused. We have a two-by-four instance, yet the answer selects only two edges.

A maximum-weight perfect matching is a different problem. It requires every vertex of its bipartite graph to be paired, which is possible only when its two sides have the same size. Our two-by-four example does not even have a perfect matching, and a generic matching problem may have missing edges. We need an exact reduction, not a silent change of meaning.

## Make a second copy, then connect each vertex to itself

The paper's construction is strikingly symmetric. Take the original bipartite graph and make a complete second copy of its vertices and edges, preserving the weights. Finally connect every original vertex to its own copy with a new edge of weight zero. Call the resulting graph B prime.

To see why B prime is still bipartite, distribute its vertices across the two assignment sides in a slightly surprising way. On the first assignment side place the original left vertices and the copied right vertices. On the second place the original right vertices and the copied left vertices. Original edges cross between the sides as expected. Copied edges cross in the reverse direction. Each new original-to-copy identity edge crosses as well.

There are k plus l vertices on each assignment side. There are two copies of the original edges, plus one identity edge for each original vertex. After the deletion of negative original edges, all these edges are permitted; arbitrary other row-column pairs remain forbidden. The identity edges guarantee that a perfect matching exists, even when the original graph has no usable edges at all. Pair each vertex to its own copy and obtain a perfect assignment of total weight zero.

Now take our optimal original matching: Alice to Q, Bob to P. Repeat those selected pairs in the copied graph. This uses four assignment edges: two original, two copied. For each original vertex not used by those pairs, take its identity edge to its copy. Here R and S are unused, so the identities R to copied R and S to copied S complete the perfect assignment. There are six edges altogether, exactly the number required for a perfect assignment on six vertices per side.

The total assignment weight is thirty. The original pairs contribute fifteen, the copied pairs another fifteen, and the identity edges zero.

This construction works for any nonnegative-weight original matching, and it gives twice the original matching score. But perhaps B prime has some unexpected perfect assignment with score higher than twice the original optimum? This is where the proof is more interesting than the recipe.

## Decode both halves of a perfect assignment

Take any perfect assignment in B prime. Look at those selected edges that belong to the original graph. They form a partial matching in the original bipartite graph, because no assignment vertex is used twice. Call it the original projection. Separately, look at those selected edges belonging to the copied graph, and translate their endpoints back to the original names. They form another partial matching. Call it the copy projection.

The two projections do not have to be identical for an arbitrary perfect assignment. That is important. The reduction does not claim that a perfect assignment literally consists of two identical matchings. It claims something stronger and more useful about their scores.

Every selected assignment edge is either an original edge, a copied edge, or an identity edge. Identity edges cost zero. Hence the weight of the perfect assignment is exactly the sum of the weights of its two partial-matching projections.

Let OPT denote the greatest possible partial-matching weight in the original graph. Neither projection can exceed OPT. Thus every perfect assignment has weight at most twice OPT.

In the other direction, start from an original optimum of weight OPT, repeat it in the copied graph, and fill every remaining vertex with an identity edge. That gives a perfect assignment of weight exactly twice OPT. The two bounds meet. The perfect assignment optimum is exactly twice the original matching optimum.

And there is one more consequence. If a perfect assignment reaches the value twice OPT, both its original projection and its copy projection must separately reach OPT. Neither can contribute less without reducing the sum, since neither can contribute more. Therefore simply reading the original edges from an optimal perfect assignment returns a maximum-weight partial matching of the original problem.

This is the heart of the correctness reduction in Lemma 5. It is a clean argument because it uses independent feasible objects. We do not define the answer to the original problem by appealing to the assignment algorithm. We define OPT first, show the translation preserves the optimum in both directions, and then use that equivalence to justify the algorithm.

Notice another benefit. All-negative original instances are handled naturally. After removing their negative edges, the copied graph still contains all identity edges. Its best assignment scores zero, and its decoded original matching may be empty. We never force a negative branch into a common subtree merely to fill a row.

## Why attach dual numbers to vertices?

An optimal assignment algorithm needs a way to tell that it has reached an optimum. The Hungarian method supplies both a candidate perfect matching and a family of numbers, sometimes called potentials or dual values, that provide an upper bound on every possible assignment.

For a maximum-weight assignment, give each row vertex a number and each column vertex a number. Require that the sum of the two numbers at the endpoints of every allowed edge be at least that edge's weight. This inequality is called dual feasibility.

Now choose any perfect assignment. Add the inequalities for the selected edges. Because a perfect assignment uses every row exactly once and every column exactly once, the sum of its edge weights cannot exceed the sum of all row potentials plus all column potentials. The potentials have produced a global upper bound on the value of every perfect assignment.

An edge is called tight when its weight equals the sum of its endpoint potentials. If a perfect assignment uses only tight edges, then its total weight equals that upper bound. No other assignment can be better. Dual feasibility plus tightness of every selected edge certifies optimality.

There is no requirement that an arbitrary intermediate matching use all rows. The algorithm maintains the feasibility of the dual values while building a progressively larger matching of tight edges. An augmentation changes the matching, possibly rerouting several assignments along an alternating path, and may adjust the potentials to expose new tight edges. When the matching is perfect and every chosen edge is tight, the upper and lower bounds coincide.

This is why the Hungarian method is more than a complicated way to choose edges. It returns a primal object, the assignment, and a dual certificate of that assignment's value. For formalization, the two objects can be specified independently and their equality checked by a theorem, rather than by trusting the path-search procedure's intent.

## A starting assignment of the right size

The copied graph has k plus l vertices per assignment side. Starting the Hungarian method with an empty matching would require k plus l augmentation rounds. Lemma 5 gives us a useful head start.

Pair every original right vertex with its own copy. We already know these l identity edges are disjoint. This initial matching contains exactly l edges. It is incomplete, because a perfect matching in B prime needs k plus l edges, but it is already larger than an empty matching by l edges. Only k augmentation rounds remain.

We must make sure this initial matching is compatible with feasible potentials, and that its selected identity edges are tight. Give every original right vertex the potential zero. Give each original left vertex the maximum of zero and its allowed nonnegative incident weights. Give each copy the same potential as its original.

Return to Alice and Bob. Alice's initial potential is eight, the largest of her nonnegative incident weights. Bob's is nine. All P, Q, R and S potentials are zero, as are their copies. Copied Alice receives eight and copied Bob nine.

An original edge such as Alice to Q has weight six; the endpoint potential sum is eight plus zero, which is at least six. Bob to P has weight nine; the endpoint sum is nine, making that edge tight. Every copied edge satisfies the analogous inequality. Every identity edge joins a vertex to its copy and has weight zero; both endpoint potentials are nonnegative, so that inequality also holds. Finally, the selected P-to-copied-P identity, and similarly those for Q, R and S, has potentials zero on both ends. All l initially selected edges are tight.

There is a small detail hidden in the phrase 'largest incident weight.' A row might have no allowed edges after negative edges are removed. The correct initial potential for that row is zero. This is how the verified formulation avoids taking a maximum over an empty set, and it maintains the necessary nonnegativity for identity edges.

We now have a dual-feasible start with l tight matching edges. A primal-dual assignment algorithm can extend it k times while maintaining the certificate conditions. After those k augmentations it reaches k plus l matched edges, and is therefore perfect. The final tightness and feasibility certify that the result is maximum-weight. Decoding its original edges gives the required partial matching.

Notice where the difference between a balanced and unbalanced graph has entered. The total copied graph has expanded, but the *deficit* between the initial matching and a perfect assignment depends only on the smaller original side. That number, k, controls the number of full augmentation rounds.

## Read the runtime expression instead of memorizing it

Let us account for the work using the paper's chosen Hungarian implementation. In the copied graph there are twice k plus l vertices in total, meaning two times the sum of k and l. There are at most twice k times l plus k plus l edges. For a sparse assignment implementation with the stated heap machinery, one augmentation takes time proportional to the number of edges plus the number of vertices times the logarithm of the vertex count.

Because k is no greater than l, the vertex count is proportional to l and the edge count is proportional to k times l, ignoring harmless small-case constants. One augmentation therefore costs on the order of l times the sum of k and log l.

There are k augmentations, because l tight identity edges were already present. Multiply the cost per augmentation by k. The result is k times l times the sum of k and log l. That is the precise asymptotic conclusion of Lemma 5.

When the two sides are balanced, k and l are of similar size. The expression is cubic in their common scale. When k is small and l is large, it can be substantially better than cubic in l. That improvement is valuable in tree dynamic programming because child matching problems can be extremely rectangular: a path vertex may have one eligible child while a hub has many.

The expression also rests on a particular implementation of augmentation: its data structures, edge scans and priority-queue operation costs. Proving the mathematical reduction does not by itself prove the complexity of a Rust function. A formal proof of this bound needs a cost model that accounts for the actual sequence of operations, including how forbidden edges are represented and how the potentials and paths are maintained.

## Where the Lean development begins and ends

In the uploaded project, the mathematical reduction appears in the shared weighted-matching proof files. `CopiedAssignmentReduction.lean` introduces the allowed copied-graph edges, exact assignment weights and the two decoding projections. The theorem `assignmentWeight_decode` expresses the sum-of-projections identity. The theorem `extend_allowed` constructs a full allowed assignment from any valid nonnegative partial matching. The theorem `dominates_allowed_decodes` proves that an assignment dominating all other allowed assignments decodes to independent maxima on both original and copy sides.

These theorems cover the core correctness proof we just worked through, including the subtle point that the two decoded matchings need not be defined as the same object. Their weights, not the incidental shape of the assignment, establish the result.

`CopiedMatchingInitialization.lean` handles the starting certificate. Its definitions choose row maxima with a zero option for missing or nonpositive rows. `initial_dual_feasible` proves the endpoint inequalities. `initialPairs_tight` proves that the larger-side identity edges meet equality. `initial_edge_deficit` identifies exactly the smaller-side number of still-missing pairs.

`CopiedMatchingDuality.lean` connects feasible and tight certificates to decoded maxima. Thus the source snapshot supports much more than a comment saying 'use Hungarian.' It contains a mathematical specification of the copied reduction, its dual conditions, and the exact initial deficit.

There is also a proved exact integer partial-matching reference API in the translated Rust development. That is a different layer. The reference implementation uses its own assignment adapter and proves its returned matching is optimal for the specified integer inputs. Such an end-to-end correctness theorem is valuable, but it does not automatically establish that the reference uses the exact sparse copied construction of the 2016 paper, or that the optimized production floating-point solver obeys the same complexity bound. We must keep a source-level guarantee separate from an asymptotic argument about a future optimized path.

At the close of Lemma 5, we can say precisely what has been achieved. We started with a partial weighted matching that can omit harmful branches. We built a larger graph in which every vertex can be matched. We proved that the perfect-assignment objective is exactly twice the original optimum, so decoding an optimum is sound. We found a feasible dual starting point with l already matched identity edges, leaving exactly k augmentation rounds. Under the paper's augmentation-cost assumptions, that yields the rectangular bound.

The next speedup exploits a property of the many matching problems the tree algorithm actually asks. They are not independent instances. Often the only difference between one and the next is the deletion of a single child. Having invested in a maximum matching and its dual certificate, we should not throw them away each time. Lemma 6 shows how much can be reused.

<!-- END SPOKEN LECTURE -->

## Non-spoken companion: Lemma 5 and the copied graph

### Exact problem statement

For a bipartite graph `B=(V ⊎ U,E)` with real edge weights and `k=|V|≤l=|U|`, the paper claims a maximum-weight **partial** matching in

\[
O\bigl(kl(k+\log l)\bigr)
\]

time (Lemma 5, Section 4). Negative edges may be removed; forbidden edges are not zero-weight edges.

### Explicit nonnegative example after discarding one negative edge

| `w` | P | Q | R | S |
| --- | ---: | ---: | ---: | ---: |
| Alice | 8 | 6 | 1 | -2 (discard) |
| Bob | 9 | 2 | 4 | 0 |

A best partial matching is `{(Alice,Q),(Bob,P)}`, weight `6+9=15`; the optimum on B is `15`.

### Exact copied-graph bipartition

Original types `V`, `U`; their copies `V^C`, `U^C`. Let

\[
X=V\mathbin{\sqcup} U^C,\qquad Y=U\mathbin{\sqcup}V^C.
\]

Allowed edges of `B'`:

- original `v∈V` to `u∈U`, with original nonnegative weight;
- copied `u^C∈U^C` to `v^C∈V^C`, with the same weight;
- identity `v` to `v^C` and `u^C` to `u`, each weight `0`.

The new sides have `k+l` vertices each, and `|E(B')|≤2kl+k+l`. Identities certify existence of a perfect assignment even if B has no allowed positive edge.

For a perfect assignment `A`, write `M_1(A)` for original selected edges and `M_2(A)` for copied selected edges decoded back to `V×U`. In general `M_1(A)≠M_2(A)`. Exactly,

\[
w'(A)=w(M_1(A))+w(M_2(A))\le 2\operatorname{OPT}(B).
\]

An optimum `M` can be doubled on original/copy edges and completed with identities, achieving `2 OPT(B)`. Hence `OPT(B')=2 OPT(B)`, and any optimal perfect assignment projects to an optimum of B on both components.

### Dual certificate and the exact augmentation deficit

For assignment row/column potentials `p_x,q_y` on B', dual feasibility means

\[
p_x+q_y\ge w'(x,y)\quad\text{for every allowed }xy.
\]

Every perfect assignment has score at most `Σp+Σq`. A perfect assignment consisting entirely of *tight* edges, `p_x+q_y=w'(x,y)`, attains that upper bound and is optimal.

Initialize `d(u)=d(u^C)=0` for `u∈U`, and `d(v)=d(v^C)=max(0,max_{u:vu allowed}w(vu))` for `v∈V` (empty max treated as `0`). Start with `M''={(u,u^C):u∈U}`, of cardinality `l`. A perfect assignment needs `k+l` pairs, hence exactly `k` augmentations. Under the paper's heap implementation,

\[
\operatorname{cost/augment}=O(m+n\log n)=O(l(k+\log l)),
\]

so `k` rounds cost `O(kl(k+log l))`. This is a *paper runtime derivation*, not yet a verified cost theorem for the optimized Rust code.

### Reading path in supplied Lean snapshot

| Mathematical step | Declaration | Relative source file in `proofs/SubtreeProofs/Shared` |
| --- | --- | --- |
| Reject negative matched edges | `IsMaximum.selected_nonnegative` | `CopiedAssignmentReduction.lean` |
| Allowed source/copy/identity edges | `CopiedAssignmentReduction.Allowed` | `CopiedAssignmentReduction.lean` |
| Complete a partial matching | `CopiedAssignmentReduction.extend_allowed` | `CopiedAssignmentReduction.lean` |
| Split perfect assignment into both matching scores | `CopiedAssignmentReduction.assignmentWeight_decode` | `CopiedAssignmentReduction.lean` |
| Maximum assignment decodes to maximum matching | `CopiedAssignmentReduction.dominates_allowed_decodes` | `CopiedAssignmentReduction.lean` |
| Row maxima and feasible starting dual | `CopiedAssignmentReduction.rowMaximum`, `initial_dual_feasible` | `CopiedMatchingInitialization.lean` |
| Initial matched identities tight | `CopiedAssignmentReduction.initialPairs_tight` | `CopiedMatchingInitialization.lean` |
| Exactly k starting augmentations required | `CopiedAssignmentReduction.initial_edge_deficit` | `CopiedMatchingInitialization.lean` |
| Final feasible+tight assignment decodes optimally | `CopiedAssignmentReduction.feasible_tight_decodes` | `CopiedMatchingDuality.lean` |

The independent matching specification and exact integer reference Rust API are additional layers. In the source status crosswalk, **optimized sparse/rectangular augmentation, production graph integration, floating arithmetic equivalence, and actual-source runtime** remain distinct open obligations.

**Primary source:** Droschinsky, Kriege and Mutzel, *Faster Algorithms for the Maximum Common Subtree Isomorphism Problem* (2016), [MFCS 2016, Section 4, Lemma 5, p. 33:7](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2016.33), original pinned [arXiv v4](https://arxiv.org/pdf/1602.07210v4). The supplied repository crosswalk is `docs/planning/paper_statement_crosswalk.md` (2016 Lemma 5) and its status ledger is `proofs/PROOF_STATUS.md`.
