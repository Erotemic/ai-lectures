# Counting the Whole Algorithm: Droschinsky 2016, Theorems 7 and 4

<!-- BEGIN SPOKEN LECTURE -->

A bound for one matching problem is not yet a bound for an algorithm that solves thousands of matchings. Even a very fast subroutine can dominate an algorithm if the caller invokes it too often. And a dynamic-programming table with only a quadratic number of entries can still take quartic time to fill if each entry is expensive.

That is the obstacle addressed by Theorems 7 and 4 in the 2016 paper of Andre Droschinsky, Nils Kriege, and Petra Mutzel. The local mathematics has already given us a recurrence for matching the child branches of two rooted trees. Lemma 5 gives an efficient way to solve one rectangular weighted matching. Lemma 6 gives a way to reuse the result for all the graphs obtained by deleting one right-side vertex. Now the task is to put those ingredients together without silently paying for the same computation again and again.

The result is a whole-algorithm bound for maximum-weight common subtree isomorphism in two unrooted, unordered trees. The running time is the number of vertices in the first tree times the number in the second, multiplied by the sum of the smaller maximum degree and the logarithm of the larger maximum degree. It is easy to recite this expression. The point of this lecture is to see where each factor comes from, and why no hidden factor for trying all possible roots survives.

## The problem the algorithm actually solves

Let our input trees be G and H, with k and ell vertices respectively. Their maximum degrees will be Delta G and Delta H. Neither input comes with an order on its children, and neither comes with a distinguished root as part of the mathematical problem. The solution is a nonempty connected induced subtree of G together with one of H and an isomorphism between them. The objective adds the weights of mapped vertex pairs and corresponding edge pairs. Some pairs may be forbidden, and permitted weights need not be positive.

A valid solution does not have to include a particular vertex. It may be a single vertex pair if all larger connected choices are worse. Matching child branches is only a subroutine in finding the globally best such solution.

Choose an arbitrary vertex r of G and orient every edge of G away from r. This creates a rooted tree, but does not change the set of feasible solutions. For every connected selected subtree of G there is a unique selected vertex nearest to r. Think of this as the highest selected vertex. Every other selected vertex belongs below it.

That observation is the heart of Lemma 2. We may keep the orientation of G fixed and let u range over its vertices as possible highest selected vertices. If u is mapped to v in H, we may root H at v for the purpose of examining the solution. The selected part of H then lies below v. It is not necessary to try every possible global root on both sides.

The paper's algorithm does something more careful than rerooting H and recomputing an entirely new dynamic program for each v. It represents the distinct *oriented views* that can occur at a vertex. In a tree, choosing a parent for v either selects one of its neighbors, or selects no parent and makes v the root of the whole oriented tree. Thus the rooted branch at v is determined by v and one of at most degree of v plus one parent choices.

This gives the three-coordinate table D of u, s, v. The first coordinate u specifies a descendant root in the fixed orientation of G. The third coordinate v specifies the vertex of H. The middle coordinate s specifies how H is rooted for this subproblem. If s equals v, then v has no parent; if s is a neighbor of v, that neighbor lies on the path toward the ambient root and is excluded from the children available at v.

A table entry is the optimum for a *root-to-root* common subtree isomorphism between these two oriented descendant components. For a feasible root pair it includes the vertex-pair reward of u and v. If that root pair is forbidden, the entry is negative infinity. Ordinary negative finite weights are not negative infinity: a feasible negative-weight singleton remains a legitimate mathematical candidate.

## Why the table has only quadratically many entries

For each u in G, how many distinct right-hand oriented views can the algorithm need? Vertex v of H contributes one view when v is root, plus one for each possible parent neighbor. Summing over v gives the number of vertices of H plus the sum of the degrees of H.

A tree with ell vertices has ell minus one edges. Every edge contributes two to the sum of degrees. So the number of right-hand views is ell plus twice ell minus one: three ell minus two. Repeating these views for all k vertices u gives k times three ell minus two possible table entries.

This is linear in k times ell. It is not k times ell squared. The tempting extra factor of ell would arise if we recomputed and stored a complete ell-by-ell table for every right root. The algorithm stores each distinct oriented view once instead.

There are some small bookkeeping details here. The left root has no parent, while every other left vertex has its one parent fixed by r. An oriented right view can be represented by a parent edge or by a root marker. Neither of these choices introduces a new mathematical tree of quadratic size. A view is a way of identifying a connected component by a vertex and an incident direction.

So far we have only counted states, not proved a running time. For a state where u has a children and v has b available right children, the matching graph can have up to a times b compatible branch-pair entries. A naïve implementation might solve a fresh weighted matching separately for each of v's possible parent choices. That is where a high-degree right vertex causes trouble.

## How Algorithm 1 fills the table

Algorithm 1 visits u in postorder in the fixed rooted tree G. When it reaches u, all descendant states rooted at a child of u have already been computed. This is enough to evaluate the child-matching recurrence for every eligible view of H at v.

For each u and v, consider the children of u in G and the neighbors of v in H. For one candidate child u-prime and one neighbor v-prime, the branch-pair weight is the weight of matching the two incident edges plus the previously computed optimum for u-prime and v-prime as corresponding roots. The right-hand descendant component for v-prime is oriented away from v. That component does not change when another neighbor of v becomes the parent of v.

This last fact is crucial. It says that at a fixed pair u and v, all the matching problems for the different right-parent choices use the *same* branch-pair weights on every edge they have in common.

When v is rooted at itself, all its neighbors are available children, and we solve a weighted partial matching between the children of u and all neighbors of v. If H is instead rooted across one neighbor z of v, that one neighbor becomes the parent and is no longer available for branch matching. The corresponding bipartite graph is the same graph with one right-side vertex deleted.

There are degree of v plus one problems in the family: the full graph, and one graph for each possible deleted right vertex. They are not independent matching instances. Solving them as though they were unrelated would throw away the structural information that Lemma 6 exploits.

For each matching M, the table entry adds the matched-root weight to the total weight of M. If no child pair is profitable, the empty partial matching contributes zero, and the root pair can still form a perfectly valid singleton subtree. This empty *matching* must not be confused with an empty *common subtree*, which the mathematical specification excludes.

At the end, the algorithm takes the maximum table entry. The fixed-root lemma guarantees that every global common subtree optimum is represented by one of those root-to-root states. The recurrence theorem guarantees that a table entry represents the best solution for its state. Together, these are the functional-correctness argument.

## The local family cost

Let a be the number of children of u in G, and let b be the degree of v in H. The base graph has a left side of size a and a right side of size b. The deletion family contains its full matching and all b one-right-vertex deletions.

Lemma 5 handles a single rectangular matching. Lemma 6 says that after finding the base optimum and the assignment dual certificate, an unmatched right-vertex deletion needs no reoptimization. There can be at most the smaller of a and b matched right vertices. For each such deletion, one augmenting search repairs the copied assignment. The old certificate and all surviving tight edges are retained.

The result is a cost for the *entire family* proportional to a times b, multiplied by the smaller of a and b plus the logarithm of the larger of them. Not b independent repetitions of the full matching algorithm: one initial solution and just the necessary repairs.

The logarithm comes from the priority-queue implementation of the shortest-path-like augmentation used in the paper's analysis. It is not a theorem about arbitrary dictionary or matrix representations, and it is not an empirical correction factor. If the implementation scans a dense matrix in a different way, this particular cost bound does not follow without a new implementation argument.

What about forming the weight matrix before solving the matching? Its a times b candidate entries are computed from child results and incident-edge scores. That work fits within the stated family bound for nontrivial sides. Constant-time table reads and appropriately represented tree branches are implicit implementation requirements. We must account for them when claiming the bound for actual code, even though the paper-level analysis can summarize them as standard primitive operations.

A detail worth preserving is that a can be zero. A leaf u has no child-matching problem. If b is zero, H is a singleton and likewise has no branch matching. In discussing asymptotic expressions with logarithms, we can handle these constant-size cases directly, or use a harmless shifted logarithm such as log of two plus the larger degree. No logarithm of zero is needed to justify an algorithm.

## A numerical accounting example

Take G to be a path on four vertices, rooted at one endpoint. The numbers of children encountered as we move down the path are one, one, one, and zero. Their sum is three, precisely the number of edges.

Take H to be a star on four vertices. Its center has degree three and its three leaves each have degree one. The sum of its degrees is six, twice its three edges.

At a fixed u with one child, the family at the star's center starts from a one-by-three matching graph and produces the three one-vertex-deleted answers. The family at each leaf starts from a one-by-one graph. The leaf of G with no children has only the root-pair weight to evaluate.

How many oriented right views exist? The center has four views: no parent and three possible parent choices. Each leaf has two views: no parent and its sole neighbor as parent. Four plus three times two is ten. The complete table has four times ten, or forty possible entries. That is consistent with the formula k times three ell minus two, since four times ten equals forty.

Now count the actual branch-pair entries that can appear in the *base matching graphs* for the families. For each of the three nonleaf vertices of G, the center of H contributes three candidate edges, and its three leaves contribute one each. That is six per nonleaf u, or eighteen in total.

The number eighteen is not the algorithm's complete running time, but it exposes the useful factorization: sum of a over G, multiplied by sum of b over H. Three times six equals eighteen. The same factorization will control the general theorem. It is a much more informative count than multiplying forty table entries by the cost of the largest three-by-three matching and then multiplying once more by all possible roots.

Consider a second extreme. If both trees are long paths, the degrees are at most two. Each local matching is tiny, so the entire algorithm is quadratic in the two vertex counts. If both trees are stars, one pair of centers creates a large matching graph. The same theorem permits cubic time when the trees have comparable size, because the smaller maximum degree can be linear in that size. The distinction is controlled by the *input degrees*, not by the number of distinct output subtree isomorphisms.

## The sum that proves Theorem 7

Here is the counting argument in full. Let a of u denote the number of children of u in the fixed rooted orientation of G. Let b of v denote the ordinary degree of v in H. The total matching work is bounded, up to constant factors, by the sum over all pairs of vertices u and v of a of u times b of v times the smaller of those two local degrees plus the logarithm of the larger.

The local smaller degree can never exceed the smaller of the two global maximum degrees. Similarly, the local larger degree can never exceed the larger global maximum degree. We may therefore pull one common factor, smaller global maximum degree plus logarithm of the larger, out of every term of the sum.

We are left with the double sum of a of u times b of v. Since the first quantity depends only on u and the second only on v, the double sum factors into the sum of a over G times the sum of b over H.

The first sum is exactly k minus one. Every edge of rooted G goes from one parent to one child, so each edge contributes one to the child-count sum. The second sum is exactly twice ell minus one, by the handshaking lemma for trees.

Their product is twice k minus one times ell minus one. In big-O notation that is k times ell. Multiplying back by the degree factor yields the bound of Theorem 7.

A variant of the proof uses ordinary degrees on both sides, whose sums are twice their edge counts. That gives the same asymptotic conclusion. Keeping the first side as rooted child counts makes the fixed-orientation schedule particularly clear. It also shows why we do not need to charge a new full-root traversal of G each time.

There are two logically separate ingredients in this step. The degree-sum identity is an elementary theorem about any tree. The assertion that every family can be solved within the local matching cost is the algorithmic content of Lemmas 5 and 6. Proving the first does not prove the second.

Notice also what happened to the apparent factor for right-parent choices. It was absorbed inside the *family cost*. We never added a separate factor of b to the summed expression. That is the exact place where a straightforward but slower analysis would go wrong.

## From matching work to Theorem 4

Theorem 7 concerns all maximum-weight matchings requested by Algorithm 1. Theorem 4 concerns the complete maximum common subtree isomorphism algorithm. The distinction is small in the paper but important when verifying an implementation.

The rest of Algorithm 1 traverses the fixed left tree, enumerates right-oriented views, prepares candidate branch-pair weights, adds each root-pair weight, writes table entries and takes a maximum. We already counted only a quadratic number of oriented states. The total number of candidate branch pairs is controlled by the same double degree sum. With the paper's assumed constant-time operations for the relevant views and table accesses, these costs do not exceed the bound for all the matching work.

That is why the proof of Theorem 4 in the publication is short. Theorem 7 has already carried the hard accounting. The whole algorithm has the same leading asymptotic bound as its matching families.

For bounded maximum degrees, the extra degree factor is constant and the algorithm takes time proportional to k times ell. That matches the basic requirement to examine arbitrary vertex-pair weights when they are supplied independently: there can be k times ell such values. For unbounded degrees and equal-size trees of n vertices, the theorem allows cubic time. The paper also discusses a reduction from the dense assignment problem that explains why beating cubic time in general would require progress on that famous matching problem. That reduction is a separate claim, not a premise required to establish Theorem 4.

## How to read the existing formalization

In the supplied Lean repository, begin with the rooted matching recurrence for every oriented descendant pair, then the fixed-root equivalence with the unrooted optimum. These theorems establish why the states and scores are correct. `RootedDynamicProgram.lean` then verifies a deliberately simple executable table and an unrooted baseline against the independent mathematical optimum. It does not implement this exact fast matching-family schedule.

Next read `Shared/MatchingDeletion.lean` and the copied-assignment files. They contain the soundness and witness ingredients for Lemmas 5 and 6. The actual exact-integer reference matching and sparse repair functions have additional source-level Lean proofs, including original-index reconstruction under explicit hypotheses. Those are substantial results, but they are not the same as a proof of the published family-wide running time.

The closest aggregate counting landmarks are in `Complexity/MatchingFamilies.lean`. They prove bounds on the number of stored pair cells in a mathematical family representation. The tree-degree identity is also present there. It is valuable to see a complete formal double-sum argument, but stored pair counts do not measure every assignment search, allocation, queue operation or memo-table access.

The project crosswalk therefore still lists Theorem 7 and Theorem 4 as open formalization targets. That does not mean their mathematical proofs are missing from the published paper. It means the existing repository does not yet contain the full verified connection from its optimized computation, through an explicit resource model, to those asymptotic conclusions.

## What the proof has taught us

The global efficiency is not a miracle of dynamic programming alone. It arises from three independent decisions. Fix one orientation in G, so the unrooted optimum can be captured by a small state family. Solve one weighted matching in each local family and use its dual certificate to handle neighboring deletion instances. Then sum local costs over actual degrees, not over a worst-case maximum at every vertex.

The beautiful part is that the final summation is almost trivial once the right local work has been grouped. The difficult design choice was recognizing which matching problems belonged to the same family. In many algorithms, a running-time proof reveals something about the shape of the problem that the recurrence by itself does not show. This is one of those cases.

<!-- END SPOKEN LECTURE -->

## Mathematical companion: exact schedule and cost

For trees \(G,H\), choose \(r\in V(G)\). Write

\[
a(u)=|C_{G^r}(u)|,\quad b(v)=\deg_H(v),\quad
 k=|V(G)|,\quad \ell=|V(H)|.
\]

The 2016 source stores \(D(u,s,v)\) for \(u\in V(G)\), \(v\in V(H)\), \(s\in N_H(v)\cup\{v\}\). For any root-feasible pair, a state is the root reward plus a partial weighted matching on \(C_{G^r}(u)\) and \(C_{H^s}(v)\); the candidate weight of \((u',v')\) is the matched-edge reward plus \(D(u',v,v')\). The requirement \(s\in N(v)\cup\{v\}\) is exactly the one-parent-deletion family.

\[
|S_{\mathrm{fast}}| = k\sum_{v\in V(H)}(1+\deg_H(v))=k(3\ell-2).
\]

For nontrivial \(a,b\), the Lemma 6 family bound is

\[
F(a,b)=O\bigl(ab(\min(a,b)+\log\max(a,b))\bigr).
\]

Zero sides have constant-cost or size-only handling; a shifted logarithm handles the degree-one corner without changing the asymptotic statement.

Let \(d_{\min}=\min(\Delta_G,\Delta_H)\), \(d_{\max}=\max(\Delta_G,\Delta_H)\). Then

\[
\begin{aligned}
\sum_{u,v} F(a(u),b(v))
&\in O\left(\sum_{u,v}a(u)b(v)(d_{\min}+\log d_{\max})\right)\\
&=O\left((d_{\min}+\log d_{\max})
  \left(\sum_u a(u)\right)\left(\sum_v b(v)\right)\right)\\
&=O\left((d_{\min}+\log d_{\max})(k-1)2(\ell-1)\right)\\
&=O\left(k\ell(d_{\min}+\log d_{\max})\right).
\end{aligned}
\]

The published Theorem 7 bounds matching work; Theorem 4 adds the non-matching DP work under the paper's primitive-operation assumptions. The theorem is **not** established in Lean merely by reproducing this inequality; it needs a proved implementation-specific family cost.

### Tiny exact count

For a path \(G\) with four vertices rooted at an endpoint and a four-vertex star \(H\):

- \((a(u))=(1,1,1,0)\), \((b(v))=(3,1,1,1)\).
- Number of candidate right views: \(4+3\cdot2=10\); table states: \(4\cdot10=40\).
- Candidate base matching edges summed over all vertex pairs: \((1+1+1+0)(3+1+1+1)=18\).
- The matching-family bound must include the base graph **and every deleted graph**, not multiply its cost by an extra \(\deg_H(v)\).

### Source reading locations

- 2016 MFCS paper, Section 3, Algorithm 1 and Proposition 3; Section 4, Lemmas 5 and 6, Theorem 7; Theorem 4 on the preceding page. [Published article](https://doi.org/10.4230/LIPIcs.MFCS.2016.33) and [pinned arXiv v4](https://arxiv.org/pdf/1602.07210v4).
- `proofs/SubtreeProofs/Droschinsky2016/Rooted.lean`: `fixedRootValue_eq_unrootedValue`.
- `proofs/SubtreeProofs/Droschinsky2016/OrientedRecurrence.lean`: `rooted_matching_recurrence`.
- `proofs/SubtreeProofs/Droschinsky2016/RootedDynamicProgram.lean`: `solve_correct`, `unrootedOptimum_correct` (reference correctness, not fast runtime).
- `proofs/SubtreeProofs/Complexity/MatchingFamilies.lean`: `tree_degree_sum`, `family_sum_le`, `tree_family_pairs_le` (pair-cell storage, **not** algorithmic time).
- `docs/planning/paper_statement_crosswalk.md`: 2016 Theorems 4 and 7 remain open source-formalization targets.

### Listening checks

1. Why does \(D(u,s,v)\) have three coordinates even though the number of states is \(O(k\ell)\)?
2. Which equality would fail if deleting a right-parent candidate changed all the surviving branch-pair weights?
3. Show where a superfluous factor \(\deg_H(v)\) enters if each parent choice is matched independently, and where Lemma 6 removes that factor.
4. Explain why a proof of \(\sum \deg=2|E|\) is not a source-level proof of Theorem 7.
