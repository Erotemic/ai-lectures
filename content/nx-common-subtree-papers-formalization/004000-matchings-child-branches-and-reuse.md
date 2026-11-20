# 004000 — Matching Child Branches and Reusing the Answer

**Track:** NX Common Subtree Papers & Formalization. **Section:** Droschinsky prerequisites. **Background:** Tree DP; basic graph theory; no prior matching algorithms required. **Focus:** Weighted bipartite matching, partial assignments, certificates, related instances and why deletion reuse drives the two Droschinsky algorithms.

<!-- BEGIN SPOKEN LECTURE -->

# Matching Child Branches and Reusing the Answer

Suppose we have already found the best similarity score for every pair of subtrees hanging below two matched vertices. Why can't we simply add all the best scores? Because a single branch cannot be matched to several branches at once. We may know that child A resembles child X, and child B also resembles child X, but a common subtree cannot reuse X as two different children. The subproblems are independent only after we decide which children are paired.

This is the role of weighted bipartite matching in the Droschinsky papers. It is a small, self-contained optimization problem inside a much larger tree problem. The recurrence asks a matching solver to align child branches, and the papers' faster algorithms obtain much of their speed not by discovering a different recurrence, but by solving many closely related matching problems without starting over each time.

We will first understand matching as a mathematical object and a proof obligation. Then we will see why a whole family of matchings can be easier than its members look individually.

## What counts as a matching?

A bipartite graph has two classes of vertices, traditionally called left and right, and edges only between the classes. Imagine three left children A, B, C and two right children X, Y. A matching is a selection of edges in which no vertex appears more than once. We might choose A-to-X and C-to-Y. We cannot choose A-to-X and B-to-X together, because X would be used twice. We cannot select three edges here: there are only two right vertices.

Assign a weight to each possible edge. In a tree-alignment problem, this weight is the value of matching the corresponding two child subtrees, including the connecting edge contribution. The objective is to select a matching with maximum total weight. For a *partial* matching, some children on either side may remain unmatched. In many common-subtree applications, allowing unmatched children is exactly right: we are allowed to discard entire branches.

There is a distinction between maximum cardinality and maximum weight. A matching with two low-weight edges may have a smaller total score than a matching with one very valuable edge. A maximum-weight matching must optimize the sum, not automatically the number of pairs. There is another distinction between an arbitrary maximum-weight partial matching and a maximum-weight matching of a fixed cardinality. The two Droschinsky papers need to discuss several variants because reductions and specialized matching algorithms make different demands on the number of matched pairs.

Negative weights reveal why these distinctions are substantive. If the only available edge weighs minus five, the best partial matching is empty, with total weight zero. If we require cardinality one, we must take the negative edge. If a paper allows minus infinity to represent a forbidden pairing, that is not merely a very negative finite number. The algorithm's feasibility logic must exclude that edge rather than hope its score is unattractive enough.

## A small assignment puzzle

Let A and B be two left children and X and Y two right children. Suppose A-to-X weighs eight, A-to-Y weighs seven, B-to-X weighs six, and B-to-Y weighs zero.

A greedy algorithm that chooses the single highest edge first picks A-to-X for eight. It then can only add B-to-Y for zero, giving eight. But the alternative matching A-to-Y and B-to-X scores seven plus six, or thirteen. The locally best edge is not part of the globally best matching.

Now replace the zero with minus four. The optimum remains thirteen. If X and Y were the only right children, an algorithm forced to choose two edges might still compare the two two-edge options, but a partial matching would also consider one-edge and empty outcomes. On a larger instance, the presence of negative edges and forbidden pairs means we must state exactly which assignment problem our solver addresses.

There are two independent correctness arguments to make. First, show that every legal child-branch pairing defines a matching and every matching can be assembled into a valid set of child branches. Second, show that the matching algorithm finds a matching of maximum total weight. The first argument belongs to tree combinatorics. The second belongs to matching theory. Their composition proves the tree recurrence.

That separation is valuable when reading a proof repository. If the optimum over matchings is correct, but the reduction from tree children to matching edges has an indexing or scoring error, the complete tree algorithm may still fail. Conversely, a correct reduction can be composed with a slow reference matching solver to establish functional correctness while optimization remains open.

## Why the matching problem is related to assignment

The assignment problem is a familiar constrained form of bipartite matching. Workers are assigned to jobs, one worker per job and one job per worker, while minimizing cost or maximizing reward. In its standard square version, a complete assignment pairs every worker with exactly one job. Rectangular instances have different numbers of workers and jobs. Partial assignments let some workers or jobs remain unused.

We can often convert one variant into another by adding dummy rows, dummy columns or copied vertices, and adjusting weights. But such a reduction must preserve objective values and feasible solutions in both directions. A naive dummy scheme can accidentally force a negative edge that should have been omitted, allow two copies of the same original vertex to be used, or make forbidden edges look legal. Correct matching reductions need their own soundness and optimality lemmas.

The Hungarian method, one classical family of assignment algorithms, works with a system of numerical potentials or dual variables. An intuitive way to think about it is to assign prices to rows and columns, so that the sum of the corresponding prices bounds the reward of each possible edge. Summing these inequalities over a legal matching gives a global upper bound on the matching's score. If an assignment uses edges whose weights exactly meet those bounds, and the dual accounting has the right matching-size conditions, the assignment attains the bound and is optimal.

This is a certificate argument. Rather than trusting a search procedure because it tried many options, we can check a feasible matching and numerical inequalities that show no other matching could do better. For partial, rectangular, copied-graph and forbidden-edge instances, the exact primal and dual conditions vary. We should learn the appropriate version instead of assuming the square perfect-assignment formula works unchanged.

The common-subtree Lean project contains a substantial matching subdevelopment for exactly these reasons. It has independently stated optimum problems, reference algorithms, and proofs about reductions and retained dual feasibility. Its remaining work includes connecting these mathematical certificates and reference operations to the actual optimized matching families and their full runtime.

## The recurrence uses a family, not one instance

In the 2016 problem, fixing a root on one input tree and considering other root orientations generates repeated local tree-pair comparisons. At a particular vertex on the right, the child set depends on which neighbor is currently treated as its parent. Reorienting the tree may change the matching graph by excluding a single right-side neighbor or by restoring it.

Imagine a bipartite matching instance with left side A, B, C and right side X, Y, Z. Now imagine three related questions: what is the best matching when X is forbidden? What is the best when Y is forbidden? What is the best when Z is forbidden? If we solve the original problem and all three deletions from scratch, we repeatedly rediscover nearly the same structure. The 2016 paper instead analyzes how to compute and reuse solutions across a family of related instances.

A key fact is that deleting a vertex that is unmatched in an existing optimum does not damage that matching. The same selected edges remain feasible after deletion. Could the smaller graph have a better solution? No: every matching in the smaller graph was already feasible in the original graph. So the old optimum is still optimal. This is a complete and pleasantly short proof.

If the deleted vertex was matched, the situation is harder. Removing it destroys one selected edge. The rest of the matching remains feasible, but it may no longer be optimal. Repair may be possible by rerouting through alternating paths or by a carefully controlled assignment update. The structural promise is that the new problem differs in a small way from the old one. A sophisticated algorithm exploits that promise to avoid repeating the full optimization.

There are important limits to the simple observation. If our data structure includes copied vertices, dense internal arrays, potential labels and compact indices, deleting an original vertex is not necessarily identical to deleting one simple row from the internal solver. The proof must establish how original identities map to internal indices, which previously tight edges remain tight, and whether the numerical invariants still hold. Reusing a matching is not the same as proving all the data structures required by the reuse algorithm remain valid.

## The unrooted 2016 result

The paper's first major speed improvement is to avoid treating every possible pair of roots as a fresh global problem. A suitable fixed-root reduction and a controlled collection of directed-edge subproblems reduce redundant work. The second is to exploit the related matching instances just described. Combining them yields the source paper's optimized bound for unrestricted weights.

For unequal input sizes and unequal maximum degrees, the exact version of that bound in the pinned 2016 manuscript contains the minimum degree bound plus a logarithmic contribution from the maximum degree bound, multiplied by the product of the two tree sizes. A simpler order-n-squared-times-Delta expression is useful when the maximum degrees are treated symmetrically, but it is not the entire asymmetric statement. We will derive the precise formula in a later complexity lecture.

What does the existing proof project establish? Its independent mathematical definition of weighted common-subtree isomorphism and its rooted child-matching recurrence are proved. Its fixed-root reduction is proved. Reference rooted computation is proved. Several building blocks of the matching-deletion machinery, including dual and repair results, are proved. But the complete optimized matching family, the production Rust graph solver refinement, and the paper's final resource bound are not automatically entailed by those pieces. The paper ledger keeps those endpoints open.

That status is intelligible once we see the layers. Proving one matching's optimum is a theorem about a local optimization. Proving the relationship among a whole family of matching problems is a different theorem. Proving a table update in Rust actually realizes that relation is another. Proving it runs in the claimed number of arithmetic and memory operations is yet another.

## The 2018 problem changes the edge weights

The 2018 embedding problem also matches branches, but its weights are not simply the score of a strict common subtree below two children. An edge in the common tree may be represented by a longer path in one or both input trees. The state therefore distinguishes mapping current vertices from skipping them as interior path vertices. For a matched pair of parent vertices, a potential pairing of children can either continue with a mapped subproblem using a direct pair of edges or use the skipped-state alternative.

The paper's Lemma 5 packages these choices into a maximum-weight matching instance, using the better of the applicable mapped-edge and skipped-path contributions. The skipped case has already accounted for a distance penalty. The direct-edge case adds an edge-label reward only when both representing paths really have one edge. Treating skipped paths as if they also earned the direct edge reward would change the optimization problem.

The unrooted 2018 algorithm then has to reuse similar matching computations across root orientations while also managing the possibility of skipped vertices. Because a skipped path can connect across an orientation boundary, the structural classification is more delicate than in the strict isomorphism case. The implementation uses a more elaborate schedule; the Lean development has the rooted mapped/skipped recurrence but still lists the unrooted structural and optimized complexity results as open.

This is a useful progression for us. The same core tool, bipartite matching, appears in both papers. It plays the same role of enforcing one-to-one pairing between independent child branches. But the legal branches and the numerical meaning of each candidate edge differ between the strict and topological problems. We can reuse matching theory without identifying the two tree specifications.

## Counting the work without wishful thinking

Suppose the matching graph at one state has k left vertices and l right vertices. A statement that one matching can be solved in a particular polynomial number of operations is helpful, but it does not settle the whole tree algorithm. We need to sum its costs across all pairs of tree states. We also need to count how many related deletion instances are requested and how much each repair costs after the first computation.

A tree's total degree is twice its number of edges. That identity often makes degree-sum bounds surprisingly effective: although some vertices may have high degree, the sum of degrees across the entire tree is linear in its size. The 2016 and 2018 analyses exploit degree sums, asymmetry between the input trees, and matching reuse. A single worst-case cost multiplied by every possible root pair can discard exactly the structural savings the algorithm was built to achieve.

In a formal complexity proof, the relevant operation count must be stated before it can be bounded. Are we counting abstract matching augmentations, comparison operations, row scans, hash lookups, allocations, or machine instructions? A recurrence theorem over mathematical integers or real numbers does not bound native floating-point error. An optimality theorem for a signed-integer reference algorithm does not silently prove that arbitrary additions in a bounded native integer type cannot overflow. These are modeling decisions, not merely programming details.

The 2016 and 2018 papers are good cases for learning how a convincing algorithm analysis is assembled. The combinatorial optimum identifies the right answer. The matching certificate identifies an optimal local assignment. The family-reuse argument controls how many expensive changes are needed. The graph degree sums and state indexing account for total work. Finally, an implementation proof must connect all those abstractions to the data structures that actually run.

When we read the matching lemmas in the proof repository, we should ask exactly where we are in that chain. Does the lemma only show feasibility of surviving selected edges? Does it prove a replacement matching has maximum weight? Does it preserve dual potentials? Does it refer to original children or copied assignment indices? Does it count updates or prove end-to-end time? Those are concrete, answerable questions, and each one points to a different next proof obligation.

<!-- END SPOKEN LECTURE -->

## Non-spoken companion: matching mathematics

### Weighted partial matching

For bipartite graph `B=(L⊔R,E)` and edge weights `w : E → K`, where `K` is an ordered additive domain, a matching `M⊆E` has no two edges sharing an endpoint and weight

\[
W(M)=\sum_{e\in M}w(e).
\]

For partial matching, `M=∅` is feasible with score zero. For fixed cardinality `k`, add the constraint `|M|=k`. For a perfect assignment, every vertex in the relevant parts is matched. These specifications are not interchangeable.

### Greedy counterexample

| | X | Y |
|---|---:|---:|
| A | 8 | 7 |
| B | 6 | 0 |

Greedy highest edge `(A,X)` yields best completion `(B,Y)`, total 8. Matching `(A,Y),(B,X)` gives 13. Choosing a locally greatest edge is not a correct general method.

### A valid simple reuse lemma

Let `M` be a maximum-weight partial matching in graph `B`. If vertex `x` is **unmatched** in `M`, then `M` remains maximum-weight in `B-x`. Proof: it remains feasible, and any matching feasible in `B-x` was also feasible in `B`, so none can exceed `W(M)`.

For a **matched** deleted vertex, the old matching loses its incident edge; reconstructing an optimum requires additional reasoning. In assignment reductions, copied vertices, potentials and indices add further conditions.

### Ideal square assignment dual (maximization)

For a complete `n×n` weight matrix `wᵢⱼ`, consider row and column potentials `aᵢ,bⱼ` such that `aᵢ+bⱼ ≥ wᵢⱼ`. For any perfect assignment `π`:

\[
\sum_i w_{i,\pi(i)} \leq \sum_i (a_i+b_{\pi(i)})
=\sum_i a_i+\sum_j b_j.
\]

If a perfect assignment uses only tight pairs, equality holds and it is optimal. A partial or rectangular matching needs an appropriate reduction or a different exact dual formulation; do not transplant this certificate without adjusting its conditions.

### Two source-paper boundaries

- 2016 Eq. (1): each child-pair matching edge gets a rooted strict-isomorphism value plus the corresponding connecting-edge match weight.
- 2018 Lemma 5: each child-pair matching edge compares mapped continuation with direct edge reward **against** skipped continuation, incorporating the path penalty according to Definition 4.

### Source and Lean references

- [Droschinsky–Kriege–Mutzel (2016), Lemmas 5–6 and Theorem 4](https://arxiv.org/pdf/1602.07210v4)
- [Droschinsky–Kriege–Mutzel (2018), Definition 4 and Lemmas 5, 12–14](https://arxiv.org/pdf/1805.00821v1)
- `proofs/SubtreeProofs/Droschinsky2016/RootedRecurrence.lean`
- `proofs/SubtreeProofs/Droschinsky2018/SkippedRecurrence.lean`
- `docs/planning/paper_statement_crosswalk.md` for the current matching/complexity proof frontier.
- Existing background: `discrete-mathematics:005000` teaches graph matchings and flow certificates; `algorithms-computability-complexity:015000` develops optimality certificates for flows and cuts.
