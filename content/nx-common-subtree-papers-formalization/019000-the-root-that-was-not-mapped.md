# The Root That Was Not Mapped: Droschinsky 2018, Lemmas 9–11

<!-- BEGIN SPOKEN LECTURE -->

When we solve a problem on a tree, choosing a root is often a harmless convenience. Pick a vertex, direct all edges away from it, and use dynamic programming on descendants. The answer may depend on which root we choose for a rooted problem, but perhaps the unrooted version can be recovered by trying a few root positions.

That hope worked particularly well for the 2016 common-subtree isomorphism algorithm. Its selected common subgraph is connected by actual physical edges. If we fix an arbitrary root in one input tree, the highest selected vertex has a useful property: it is a real, selected vertex. We can arrange the dynamic program around it.

The 2018 paper studies a different feasible object. An abstract edge may pass through physical vertices that are not mapped. The highest point of an embedding, viewed from a chosen root, might be one of those skipped vertices. It might even sit exactly where two selected branches pass through the chosen root direction. Fixing a root and looking only for the best rooted embedding can then miss an unrooted optimum.

Droschinsky, Kriege, and Mutzel handle this with a structural split. Their Lemmas 9, 10, and 11 explain why the missing case has a simple shape, how to express it using already computed rooted states, and why the additional maximization can be performed efficiently. There is a beautiful separation here: the local rooted recurrence knows how to continue a branch, while the unrooted argument identifies where two such branches must be joined.

## The counterexample to an easy shortcut

Imagine the first input tree is rooted arbitrarily at r. Somewhere below r is an interior vertex u, with two branches leading to selected vertices. The common embedding may realize an abstract edge by a physical path that comes up from one child branch of u, passes through u, and goes back down through another. The abstract endpoints are selected; u itself is not. The common edge passes through u without placing a mapped common-tree vertex there.

Now ask the rooted dynamic program to regard the input tree as rooted at r. A rooted topological embedding requires each abstract parent to map above its children. But the abstract edge connecting the two selected endpoints crosses from one descendant branch of u to another. Neither selected endpoint is an ancestor of the other in the orientation from r. The common tree cannot put that edge into a parent-to-child descent while retaining the chosen orientation. Trying every root of the second input will not repair the problem on the first side.

The paper makes this failure concrete in its Figure 2. With the first tree fixed at its pictured root, the best available rooted embedding has weight two point eight under the displayed node scores and penalty zero point two. Rerooting the first tree at another vertex makes a weight-three-point-six embedding available. The difference is not a numerical accident caused by a tie. It is a structural consequence of allowing an abstract edge to pass through a skipped physical vertex.

This is an important contrast with the 2016 paper. The problem is not that the two-state recurrence of Lemma 5 is incorrect. Every computed rooted state can be exactly right. The problem is that the family of candidate rooted solutions is too small when we insist on one fixed orientation of the first input.

We could avoid the issue by trying every possible root pair. That is mathematically correct. For a sufficiently small tree it is also a reasonable reference algorithm. But it repeats much of the same work under many orientations. The paper's goal is to recover the missing candidates without paying for all those separate dynamic programs.

## Look at the highest point of the realized structure

Fix the root r of the first tree. Consider a particular valid unrooted embedding, not necessarily one returned by an algorithm. Take the union of all physical paths that realize its abstract common-tree edges, together with the selected images of its common vertices. This is a connected physical subtree. It has a unique highest vertex relative to r: the point nearest r in that connected set.

There are two cases. The highest vertex is an image of an actual common-tree vertex, or it is an interior point of a realized abstract edge.

In the first case, we can orient the abstract common tree with that selected vertex as its root. The other selected vertices lie beneath it in the first input's fixed orientation. The second input can be rooted appropriately so that its corresponding image is also above the rest of its realized structure. Thus the optimum is represented among rooted embeddings using the fixed first-tree orientation and some choice of root in the second tree. This will be the first family of candidates in Lemma 10.

In the second case, the highest physical vertex is not selected. Since it lies inside the realized structure, it must be an interior vertex of the physical path for some abstract edge. The realized structure reaches it from two directions: one toward each selected endpoint of that abstract edge. Because it is the highest vertex, those directions lead into two distinct child branches under r, rather than one direction continuing upward toward r. This is the missing case.

There is a subtle but decisive restriction. Could a third selected branch also pass through this skipped vertex? No. If another abstract edge used this same skipped interior vertex, the topological path-separation condition would be violated. Branching must occur at the image of a common-tree vertex, not at an unselected waypoint. So a skipped interior vertex cannot serve as an invisible branching junction for three selected common branches.

This is the content behind Lemma 9. When an unselected physical vertex lies inside an abstract edge's realized path, the selected vertices occupy exactly two components of the tree after that vertex is removed, on the two sides of the path. There cannot be a third component containing selected vertices without forcing an extra abstract branch through the unselected interior.

It helps to distinguish this from a claim about every unselected vertex of an input tree. Most input vertices can be absent from a solution entirely. Lemma 9 concerns a vertex lying inside an actual realized common edge. Only that kind of skipped vertex is constrained to have selected material on exactly two sides.

## Cut the witness through that vertex

Let u be the highest skipped vertex in the second case, and let b one and b two be the two distinct children of u whose descendant regions contain the selected portions of the witness. The original embedding's common tree can be cut along the abstract edge whose physical realization passes through u. Cutting an edge in a tree creates exactly two connected components. Each component is itself a nonempty common tree, with a top selected endpoint in each input.

On the first input, the two components lie inside the descendant subtrees rooted at b one and b two. Both components are compatible with the fixed orientation from r when considered separately. They do not need to be compatible with each other as one rooted embedding, because the connecting abstract edge runs between their tops across u.

On the second input, take the physical path realizing the same abstract common edge. Choose any physical edge along that path and cut the second tree there. Let the endpoints of the cut edge be v and w. Deleting the physical edge v-w separates the second tree into two opposite connected regions. The two abstract components lie on opposite sides. Root those regions at v and w respectively, toward their own selected endpoints.

Now each half of the original unrooted embedding is a rooted subproblem of exactly the kind we already know how to score. Its boundary pair is one first-tree child b and one endpoint of the chosen second-tree cut edge. The selected top of that half might equal its boundary pair, or might be deeper in one or both components. So for each half we take the better of the mapped state and the skipped state from Lemma 5.

It is worth checking the penalty accounting. The skipped-state boundary cost for the first half counts every physical interior vertex from its boundary child to its first mapped pair. The second half does the same. The second-tree cut edges separate the two regions, so interior vertices away from the cut are accounted for by the corresponding half. But the central first-tree vertex u does not belong to either child-descendant region. It lies between them on the newly reassembled abstract edge. It must be charged once more, with one additional penalty p.

The score of the original embedding therefore splits into the score of the first rooted component, plus the score of the second rooted component, minus p. There is no direct physical-edge reward on this crossing abstract edge. On the first input, its path has at least two edges, entering u and leaving u. Since one realized path is long, Definition 4 calls for distance penalties rather than an edge-label comparison, regardless of what happens on the second input.

For the paper's numerical Figure 2, this is exactly the calculation. One side contributes two. The other contributes one point eight, including its own skipped vertices. The shared skipped vertex u costs an additional zero point two. Two plus one point eight minus zero point two gives three point six. The score that a fixed-root-only method misses has been reconstructed from two ordinary rooted states and one extra penalty.

## The exact two-family maximum

We can now understand Lemma 10. Its first family, call it M one, takes the maximum rooted embedding score while keeping the first input rooted at r and allowing every possible root in the second input. All embeddings whose highest physical vertex in the first input is selected belong to this family.

The second family, call it M two, ranges over a potential skipped crossing vertex u in the first input, a physical edge v-w in the second input, and two distinct child regions b one and b two under u. For each side of the cut we take the best of its mapped and skipped rooted boundary values. We add those two scores and subtract p for u. Finally we maximize over every such split.

The unrooted optimum is the larger of M one and M two. This is more than an upper bound. We have shown that every genuine unrooted embedding belongs to one of those families, giving one inequality. We also need the constructive converse. An M-one candidate is a rooted embedding, so it is also an unrooted embedding after forgetting the chosen roots.

For an M-two candidate, take the two feasible rooted component witnesses. Their physical images in the first tree lie in different children of u. Their physical images in the second tree lie on opposite sides of the cut edge v-w. Join the two abstract common trees with one new abstract edge between their selected tops. In the first input, realize that edge by traveling from one selected top up through u and down to the other. In the second input, realize it by the unique physical path joining the two selected tops across the cut edge. The component regions on both sides are disjoint. Their internal paths remain valid, and the new connecting edge cannot intersect an old branch except at its proper selected endpoint.

The joined abstract tree is therefore a valid common topological embedding. Its score is exactly the two component scores minus p, because the crossing vertex u is the one interior point not already accounted for by the component boundaries. This proves that M two does not contain spurious numerical combinations. We have both directions of the maximum identity.

There are two easy mistakes to avoid. First, the children b one and b two must be distinct. If they were the same, both candidate component witnesses could occupy the same first-tree branch and their realizations could collide. Second, a split must contain two actual nonempty components. We cannot let one half be the empty matching of an unrelated child-matching problem. Here the crossing abstract edge has two selected endpoints; a nonexistent side would not realize that edge.

## Why a matching of cardinality two appears

Lemma 10 describes an optimization over two distinct children of u. Lemma 11 explains how to evaluate it without trying every ordered pair of children.

Fix u and an edge v-w in the second input. Think of the children of u as one side of a small weighted bipartite graph. On the other side place just two terminals, one for the component of the second tree reached from v after cutting v-w, and one for the component reached from w. The edge weight from a first-tree child b to one terminal is the best of the mapped and skipped boundary values for that corresponding rooted subproblem.

We need a matching of cardinality exactly two. Its two edges choose two distinct first-tree children, one assigned to each of the two right-hand regions. This is not the ordinary maximum-weight partial matching from Lemma 5, where an empty matching is allowed and negative branches may simply be ignored. The two-sided split only makes sense if both terminals are used. A maximum-weight matching of cardinality two expresses that constraint exactly.

At first this sounds quadratic in the number of first-tree children: try every child for the v side, then every different child for the w side. The paper uses a small exchange argument to reduce the work.

List the child candidates for the v side from best to worst, and keep only the two best. Do the same for the w side. Why can we discard all lower-ranked options? Suppose an optimal two-edge matching uses a child b for v that is ranked third or worse. At most one other child is occupied by the w-side edge. Of the two best children for v, at least one is therefore free. Replace b with that free child. The score does not decrease and the distinct-child constraint remains satisfied. So there exists an optimum using one of the top two candidates for v. Apply the same argument to the w side. The search now has at most four possible assignment pairs, rather than the square of the number of children.

A concrete number example makes the collision constraint clear. Suppose u has children Alice, Bob, and Carol. The v-side values are nine for Alice, eight for Bob, and one for Carol. The w-side values are ten for Alice, two for Bob, and zero for Carol. A naive choice of the best score on each side selects Alice twice and claims nineteen. That is invalid. The best valid two-sided split instead assigns Bob to the v side for eight, and Alice to the w side for ten. The resulting score is eighteen before subtracting the central penalty p. Keeping the best two candidates for each side is enough to find it.

What if there are fewer than two distinct feasible children? Then there is no cardinality-two matching. The value of this split is negative infinity, not zero and not a one-sided score. Again, the extended bottom value expresses the absence of a feasible nonempty structural configuration.

To compute the two best candidate weights for each terminal, scan the children of u once. That takes time proportional to the number of children. The final choice among at most four combinations is constant work. Now sum that over every u in the first input and every physical edge in the second. The sum of the numbers of children in a rooted tree is its number of edges, which is one fewer than its vertex count. The second input also has one fewer edge than vertex. So, once the needed rooted table entries are available, all the M-two maximizations together take time proportional to the product of the two tree sizes.

That is the useful conclusion of Lemma 11's two-branch argument. It does not mean the entire unrooted algorithm already has the best published time bound. Computing and reusing the many rooted table entries is still expensive if we simply rerun a fresh dynamic program for every second-tree root. The paper first gives a slower bound for that work, then develops a more careful matching-reuse and evaluation-order method in its later section.

## What the existing Lean formalization proves

The source repository supplied for this lecture makes a meaningful distinction between the correct but straightforward solution and the optimized unrooted theorem we have just studied.

In OverallOptima.lean, the independent unrooted objective maximizes the scores of independently valid common-tree witnesses. The theorem unrootedValue_eq_max_rerooted_mapped proves that we can recover that objective by trying every pair of ambient root vertices and taking the corresponding mapped-root state. The theorem is strong: it concerns the genuine nonempty topological-embedding specification, not a hand-written test oracle. Its proof does not rely on Lemma 10's fixed-first-root shortcut. It takes the safe, brute-force mathematical route.

The executable RootedDynamicProgram module also has an unrootedOptimum function. It enumerates the possible orientations, solves the rooted score tables and maximizes the mapped state at the chosen root pair. Its unrootedOptimum_correct theorem connects that explicit evaluator to the independent unrooted optimum, given correct finite vertex lists and oriented child lists. This is a verified functional baseline.

But that result does not prove Lemma 9's two-branch geometry for a skipped highest vertex. It does not show the Lemma 10 M-one/M-two identity or Lemma 11's top-two reduction. And it does not prove that the optimized production Rust path implements those structural choices and meets the intended running-time bound. The repository's paper statement crosswalk lists the structural unrooted lemmas and the optimized scheduling/cost work as open proof frontiers, while documenting tested optimized Rust behavior.

A useful future proof exercise is therefore concrete. Define the union of selected images and realized physical paths for an independent common-tree witness, and choose its highest vertex in a fixed ambient orientation. Prove the dichotomy: that vertex is either selected or an interior vertex of exactly one common edge. In the second case, prove there are exactly two selected descendant components. Then construct the two boundary witnesses after cutting both inputs and prove the score equation with exactly one central penalty. Reverse the construction to obtain the lower bound. Once that equivalence is accepted, Lemma 11's cardinality-two exchange argument can be formalized as a separate finite matching lemma.

This is how a paper proof and a formalization plan fit together. A correct all-roots baseline establishes what the answer means and gives a trusted comparison. The more efficient fixed-root structural theorem explains why we can avoid so many repeated orientations. The two-state rooted recurrence supplies the values needed to evaluate each structural case. And the matching optimization supplies the cost improvement, but only after its input states have been produced in a valid dependency order.

The central lesson is that choosing a root is not harmless when a valid edge may conceal unselected vertices. The problem is repaired not by adding more cases to the local recurrence, but by analyzing the geometry of the highest point of an entire embedding. Once that point is classified, the global optimum reduces to one ordinary rooted family and one carefully constrained two-branch family. That is the structural bridge from Lemma 5 to the paper's unrooted algorithm.

<!-- END SPOKEN LECTURE -->

## Companion: the fixed-first-root dichotomy

Let \(T,T'\) be unrooted trees and fix any vertex \(r\) as the ambient root of \(T\). For a feasible unrooted witness, let \(H\subseteq T\) be the union of its selected images and physical paths representing common-tree edges. The unique highest vertex of \(H\) under the orientation away from \(r\) is either:

1. a selected image of some common-tree vertex, so the witness is compatible with an appropriate rooted subproblem in the fixed first orientation; or
2. an unselected interior vertex \(u\) of a realized common edge, with selected vertices in exactly two distinct child regions of \(u\).

The second case is the structural phenomenon of 2018 Lemma 9. A skipped input vertex absent from the realized structure is **not** governed by Lemma 9.

### Two-family optimum, in explicit boundary notation

Let \(A^r_s(b,c)\) and \(D^r_s(b,c)\) be the mapped/skipped values for fixed first-root \(r\) and second-root \(s\). Define \(Q(b;v\mid w)\) as the maximum of the two rooted boundary states for the subtree of \(T\) rooted at \(b\) and the component of \(T'\setminus vw\) containing \(v\), rooted at \(v\):

\[
Q(b;v\mid w)=\max\{A^r_w(b,v),D^r_w(b,v)\}.
\]

The subscript \(w\) orients the right tree so \(v\) is its child; equivalently, orient just the right component at \(v\). The notation is pedagogical and not a verbatim identifier from the paper. The correct right-side component must be used throughout the boundary state.

Then a conceptual form of Lemma 10 is

\[
\begin{aligned}
M_1 &= \max_{s\in V(T')}\operatorname{RootedOpt}(T^r,T'^s),\\
M_2 &= \max_{\substack{u\in V(T)\\vw\in E(T')\\b_1\ne b_2\in C_r(u)}}
\bigl[Q(b_1;v\mid w)+Q(b_2;w\mid v)-p\bigr],\\
\operatorname{UnrootedOpt}(T,T')&=\max\{M_1,M_2\}.
\end{aligned}
\]

**Orientation note:** The paper uses \(\mathcal L^s\) for a table under the chosen second root. For the component of \(T'\) across the edge \(vw\), write \(Q(b;v\mid w)=\max_t\mathcal L^{w}(b,v,t)\), and \(Q(b;w\mid v)=\max_t\mathcal L^{v}(b,w,t)\), with the first-tree orientation held at \(r\). These are precisely the two sides of the cut. Empty two-branch choices have value \(-\infty\).

### Cardinality-two optimization in Lemma 11

At each \((u,vw)\), choose a matching of cardinality **exactly two** between \(C_r(u)\) and terminals \(\{v,w\}\), using the corresponding \(Q\) weights. Retain only the two best candidate children for each terminal. If an optimum uses a worse candidate for one terminal, at most one of its two top candidates is occupied by the other terminal, so exchanging the worse child with a free top candidate cannot decrease its score.

For example:

| First-tree child | Weight toward `v` | Weight toward `w` |
| --- | ---: | ---: |
| Alice | 9 | 10 |
| Bob | 8 | 2 |
| Carol | 1 | 0 |

Independent maxima would collide on Alice (invalid score 19). The two-terminal matching chooses Bob for `v` and Alice for `w`: score \(18\), before the central \(-p\). A full child scan and constant-size final choice give \(O(|C_r(u)|)\) work for each \((u,vw)\). Therefore

\[
\sum_{u\in V(T)}\sum_{vw\in E(T')} O(|C_r(u)|)
=O\bigl(|T||T'|\bigr).
\]

This is the cost of the extra \(M_2\) maximization **after** the necessary rooted table values are available, not an end-to-end complexity certificate for the optimized unrooted algorithm. The paper's Lemma 11 reports a slower total rooted-table phase for \(M_1\); Section 5.2 then optimizes that phase with related matching families and careful scheduling.

### Source correspondence and current proof frontier

- Primary text: [Droschinsky, Kriege and Mutzel, MFCS 2018](https://doi.org/10.4230/LIPIcs.MFCS.2018.54), Section 5.1, Figure 2, Lemmas 9–11, pp. 54:8–54:10; [pinned arXiv v1](https://arxiv.org/pdf/1805.00821v1). The paper's Figure 2 yields \(2.8\) for the fixed-root candidate and \(3.6=2+1.8-0.2\) for the crossing case.
- `proofs/SubtreeProofs/Droschinsky2018/OverallOptima.lean`: `rootedValue_eq_max_mapped`, `unrootedValue_eq_max_rerooted_mapped` — mathematical correctness of a different, all-root-pairs baseline.
- `proofs/SubtreeProofs/Droschinsky2018/RootedDynamicProgram.lean`: `RootedDP.unrootedOptimum`, `unrootedOptimum_correct` — executable **score-only** all-root-pairs baseline, assuming supplied vertex/child lists represent the actual finite trees.
- `docs/planning/paper_statement_crosswalk.md` and `proofs/PROOF_STATUS.md`: the fixed-first-root structural Lemmas 9–11, optimized evaluation order, matching reuse, source-level optimized Rust refinement and runtime proofs remain open in the uploaded November 19, 2026 snapshot. Tested production behavior is not a Lean proof of those claims.

### Listening checks

1. Give an embedding that is valid unrooted but cannot be rooted with a fixed first-tree orientation. Which physical vertex is the highest point of its realized structure?
2. Why does Lemma 9 describe two selected sides of an *interior realized-path vertex*, rather than any unselected input vertex?
3. Where does the extra \(-p\) in the M-two formula come from, and why does it occur exactly once?
4. Why is the optimization for M two a cardinality-two matching, not the optional matching of Lemma 5?
5. Which theorem in the uploaded Lean code already establishes correctness of the slower all-root-pairs baseline, and what structural claim remains to be proved to justify Lemma 10?
