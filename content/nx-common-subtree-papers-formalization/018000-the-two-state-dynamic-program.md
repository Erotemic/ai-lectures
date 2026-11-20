# The Two-State Dynamic Program: Droschinsky 2018, Lemma 5

<!-- BEGIN SPOKEN LECTURE -->

A dynamic program is often described as a table of answers to smaller versions of the original problem. That description hides the most difficult design decision: what, exactly, must an entry remember about the part of the solution that lies outside its table cell?

For strict subtree isomorphism, the answer is simple enough. We may ask for the best common subtree whose two roots are paired, then combine the children with a maximum-weight matching. But the 2018 paper by Andre Droschinsky, Nils Kriege, and Petra Mutzel permits a common edge to stretch into a path. A branch of the common tree can enter a physical subtree at its root and travel downward for several edges before reaching the first selected vertex. That means the subtree's root is not necessarily part of the mapping. And, critically, the missing vertices have a cost.

The algorithm needs to distinguish a completed, mapped top pair from an unfinished branch that is still traveling toward its first mapped pair. The paper uses two states. One is drawn as a wedge and the other as a diamond. In this lecture I will call them the mapped state and the skipped state. We will derive the exact two recurrences of Lemma 5, work an example in which choosing a longer path changes the answer, prove why each recurrence is both sound and complete, and see how the existing Lean formalization expresses the reasoning independently of its executable dynamic program.

## What the table is allowed to assume

Take two finite rooted trees, T and T prime. Their roots define a parent-to-child orientation, and every vertex has a descendant subtree. We choose a vertex u in T and a vertex v in T prime. The input trees may have labels on vertices, on edges, or both. A vertex-pair score tells us how rewarding it is to map one selected vertex to another. An edge-pair score tells us how rewarding it is to map a physical edge to a physical edge. Either score may be negative; forbidden matches may have score negative infinity. We also have a nonnegative penalty p, possibly infinite, for each physical vertex skipped inside a realized common edge.

A common subtree embedding is witnessed by a smaller tree whose vertices map injectively into each input. Its abstract edges become physical paths. Children of the same abstract parent must travel into separate physical branches. We count the selected vertex scores. For each abstract edge, we count the physical edge-pair reward only when its two realized paths both have length one. If either path is longer, we ignore edge labels on that abstract edge and subtract p for every skipped interior vertex on the two paths.

The rooted trees fix the directions of descent; they do not force the common root to be the root of T or of T prime. That distinction is the reason to introduce the second state.

At the boundary pair u and v, the mapped state asks: among feasible nonempty common embeddings contained in those descendant subtrees, what is the best score when the top vertex of the common tree is mapped to u and v themselves? No path from a previously mapped parent has yet been charged; those parents are outside this subproblem. Once u is paired with v, there is a definite common branching point.

The skipped state asks a related but different question. Suppose a parent from outside this subproblem is already mapped and wants to send one of its common branches into the subtrees at u and v. The first mapped pair in that branch might be deeper than the boundary pair. We optimize over such embeddings where the first selected pair is not u and v simultaneously. We also charge the penalty for each step from u and v down to that first pair. In other words, this state includes the unfinished connection to its boundary, but does not yet include the edge from the outside mapped parent to u and the corresponding edge to v.

That phrasing is worth holding on to. The diamond state does not mean there is no common embedding, and it does not mean that an arbitrary vertex is removed for free. It means a valid branch exists below the current boundaries, its top pair is different from the boundary pair, and the score already contains the cost of getting down to that pair.

In the supplied Lean source, the independent boundary witness consists of a finite set of mapped vertex pairs together with an explicit top pair. The predicate named StateValid checks the underlying common tree, the selected top pair, its position within both descendant regions, and consistency with the two fixed ambient orientations. A function named stateScore adds the internal common-tree score to precisely the boundary penalty. These definitions come before the recurrence. That is what makes the recurrence a mathematical theorem about feasible objects, rather than a circular definition of what feasible objects are.

## The skipped state is a first-step decision

Assume first that we are in the skipped state at u and v. The first selected pair is deeper in at least one of the two trees. In a rooted tree, there is a unique first child on the path from a boundary vertex toward a proper descendant. So one of two things must happen. Either the left boundary u is skipped and the solution continues at a child b of u, keeping v fixed. Or the right boundary v is skipped and the solution continues at a child c of v, keeping u fixed.

The two possibilities can overlap when both boundaries are skipped. That is fine: we are taking a maximum, not counting distinct witnesses. We need coverage, not a disjoint enumeration of every possible execution history.

What state follows the one-step descent? It could be mapped or skipped. If the first selected pair is now b and v, we have arrived and use the mapped value for b and v. If the first selected pair still lies farther down, we use the skipped value. Either way, the single physical vertex we have just passed over incurs one penalty p.

Consequently, the skipped value at u and v is negative p plus the best of all mapped or skipped child continuations on either side. The word 'best' here really means maximum over four families: mapped and skipped after a left descent, and mapped and skipped after a right descent. If a side has no children, its maximum is negative infinity, so it contributes no fabricated way to skip a vertex.

It is easy to invent a subtly wrong recurrence here. We might try skipping the left and right roots together, and charge p just once. That would undercharge a path which skips one vertex in each tree: it has two skipped interiors, not one. Or we might allow a skipped value at u and v to simply equal the mapped value at u and v, with no descent. That would let the algorithm classify a direct-to-direct branch as skipped, avoiding an unfavorable edge-label weight. The diamond state must require at least one genuine descent.

The correct recurrence charges a penalty once per one-sided descent. Repeating it twice, once on each side, charges two p's. With an infinite penalty, the first such descent sends the score to negative infinity. We do not need to erase the mathematical possibility of the embedding; its penalized score is simply bottom in the extended score domain.

Why is this recurrence true, not just plausible? Take an arbitrary valid diamond witness. Since its top selected pair differs from u and v, at least one side is a proper descendant. Choose that side. The unique path from its boundary to the selected top passes through some immediate child. Restricting the witness to this child's boundary leaves a feasible continuation of exactly the same common tree. The score splits into one skipped-vertex penalty plus the continuation score. This proves that every diamond witness is bounded above by the right-hand side.

For the reverse direction, take any feasible mapped or skipped continuation at a child. Extend its boundary upward one physical edge, declaring the old boundary root skipped. The common tree and all selected pairs remain the same. The new boundary path is exactly one edge longer, so its score is the old score minus one p. The extension is valid, so every candidate on the right-hand side is attainable on the left. Together, the two directions give equality.

The formalization has two names that describe these proof directions quite clearly. StateValid.skipped_cover proves that every skipped witness descends through a child on one side. StateValid.extend_left and extend_right construct the inverse extension. The score lemmas stateScore_step_left and stateScore_step_right certify the exact one-penalty identity. Then skipped_recurrence_two_state turns those structural facts into an equality of finite maxima. The paper's single line of recurrence is backed by a series of small geometric facts about actual tree paths.

## The mapped state is a matching problem

Now suppose u is selected and paired with v. Every abstract child of that common root must depart through an immediate child of u on the first side and through an immediate child of v on the second. The branch's selected top might be farther down, but its path starts with one definite child on each side. Two different common children cannot choose the same immediate child region of u, because their realized paths would share a physical segment after leaving u. The same restriction holds on the right.

Thus every collection of common children determines a partial matching between the children of u and the children of v. Partial is important: a physical child may have no corresponding selected common branch. We must not force every child to be matched, especially when all of its available matches have negative score.

Consider a proposed matched pair of physical children, b and c. We can realize a common branch by starting at b and c, then asking where the first selected pair is. There are exactly two scoring cases.

Case one: the first selected pair is b and c themselves. This is the mapped state at b and c. The newly attached abstract edge from the common root to this branch is represented by the physical edge from u to b and the physical edge from v to c. Both are length one. We add their edge-label score to the mapped branch value.

Case two: at least one of b and c is skipped on the way to the branch's first selected pair. This is the diamond state at b and c. We use its value alone. The boundary penalties already cover every extra interior vertex in the two realized paths. We do not add an edge-label reward, even if the first physical step on one side looks like a good match. The rule from Definition 4 tests the lengths of both complete realized paths. As soon as one is longer than one, its edge-pair contribution is replaced by penalties.

So each possible child pair b,c gets one weight: the larger of the diamond value at b,c and the mapped value at b,c plus the score of the two physical edges u-b and v-c. The mapped value at u,v is then the score for selecting u with v, plus the weight of a maximum-weight partial matching on this child bipartite graph.

There is no hidden choice to connect the same child twice. A matching rules that out. There is no hidden obligation to include a negative branch. The empty matching is legal and has weight zero. The current mapped pair u,v itself is always a nonempty witness, even if its node score is negative. That last detail distinguishes the theoretical objective from an optional empty-result user interface.

Observe how much work the two-state design is doing. The matching handles branching, which is a simultaneous choice over different immediate child regions. The diamond state handles stretching, which is a sequential choice along a single physical path. Each state is solving the type of dependency that the other cannot express cleanly.

## A complete small computation

We can now calculate a table entry without hand-waving. Let the first rooted tree have a root U and one child B. Let the second have a root V, its child C, and C's child D. So the physical shapes are a single edge on the left and a two-edge chain on the right.

Specify exactly three finite vertex-pair rewards. Pairing U with V scores four. Pairing B with C scores zero. Pairing B with D scores six. For this example, let every other vertex pair have score negative infinity. The reward for matching the direct physical edges U-B and V-C is four. All other edge pairings can be taken as forbidden; their values will not be needed in a long-path branch. We will vary the penalty p.

At the bottom of the table, B and D are both leaves. Their mapped value is six: select B and D and choose no children. Their diamond value is negative infinity, because there is no child in either subtree to descend into. This shows why the maximum of an empty child family must be negative infinity rather than zero.

Next evaluate B and C. B has no children; C has child D. The mapped value for B and C is zero. There is no child matching, and the singleton pair itself contributes zero. But the diamond value for B and C can skip C and descend to D, where B is paired with D for six. After charging the one skipped vertex C, the value is six minus p.

Finally consider the mapped value for U and V. Its node reward is four. There is just one possible child pair, B and C. The direct alternative attaches a mapped B-C branch of value zero and adds the physical edge reward four, for a branch contribution of four. The stretched alternative uses the diamond value at B,C, namely six minus p. We choose the larger contribution, and then add the root score four.

The result is four plus the maximum of four and six minus p. At penalty one, the stretched branch is better: the common tree has pairs U-V and B-D, its abstract edge spans one edge on the left and two on the right, and its score is four plus six minus one, or nine. At penalty three, the direct branch wins, with U-V and B-C and score four plus zero plus four, or eight. At penalty two, they tie at eight. At infinite penalty, the stretched alternative has negative-infinity score and the direct one still scores eight.

Notice a trap in this example. The physical edge pair U-B against V-C carries a reward of four. It does not contribute that four to the U-V, B-D embedding. Its realized abstract edge ends at D, not C, and therefore has one skipped interior vertex. Giving the stretched solution both the edge reward and the penalty would produce the wrong total. That is precisely the bug the diamond branch avoids.

The example is complete for the mapped U,V objective because only those three vertex pairs are allowed, and the child structure has been exhausted. It does not assert anything about an unrestricted unrooted problem: changing the ambient roots and the global choice of mapped top pair is a separate question.

## Why every mapped witness yields a matching

The proof of the mapped recurrence needs two directions too. Start with a completely arbitrary valid common embedding whose top pair is u and v. The common tree has some set of children of its root. Each such child defines a separate common branch.

By the topological embedding rule, the physical path for each branch begins in a unique immediate child region of u, and distinct branches use different regions. The same statement holds in the second input at v. We can therefore assign to each common child a pair b,c of physical children, with no repeated b and no repeated c. These pairs form a valid partial matching.

Restrict the abstract common tree to one child branch. The restricted object is an actual feasible boundary witness at b and c. Its top selected pair may equal b,c, or lie below at least one boundary. In the first case its connecting path is direct/direct, so its total contribution cannot exceed the mapped branch optimum plus the physical edge reward. In the second case the connecting paths contain skipped interiors, and its contribution cannot exceed the already-penalized diamond optimum. In either case it is bounded by the weight we assigned to matching edge b,c.

The global score decomposes into the root node contribution and one contribution per common child branch. A valid matching can have no more weight than the maximum-weight matching. Consequently, the score of every feasible mapped-root witness is at most the proposed recurrence value.

This direction is less automatic than it sounds. One cannot simply claim that all common branches are independent, because the separation theorem is exactly what justifies the distinct immediate regions. One cannot simply sum branch scores, because one must prove that every node reward and every abstract-edge contribution appears exactly once. One cannot simply replace a branch by an abstract number, because one must know whether the direct-edge reward or the path penalty applies. The Lean development proves each bridge explicitly.

The module MappedDecomposition contains an actual decomposition of common-child branches and a source_score_upper theorem. It depends on an isomorphism between the original common tree and a graft of its child components, on score preservation through that reindexing, and on branchChild_injective for assigning branches to distinct physical child regions. Its mappedValue_le_matchingValue theorem is the result we have just argued: the independent feasible optimum cannot exceed the matching expression.

## Why every matching can be assembled into a witness

Now start from the other end. Choose any partial matching of child regions and for each matched pair choose the better of its two boundary continuations. We need to show these locally optimal choices can coexist as one common tree, not merely add up as numbers.

For a selected child pair b,c, if the mapped alternative is best, choose an actual boundary witness attaining its mapped optimum and connect its common root directly to the new parent. If the skipped alternative is strictly better, choose a witness attaining the skipped optimum and connect its first mapped pair to the new parent through the appropriate physical paths. Because the chosen b values are distinct and the chosen c values are distinct, the branch realizations occupy separate immediate child regions on each side. Their paths cannot interfere with each other outside the newly introduced common root.

We construct a new abstract common tree by taking a fresh root and grafting the separate chosen common trees beneath it. The embeddings of each child common tree are already valid. The new root maps to u and v. The separation of immediate regions gives the branch-separation condition for the new embeddings. In a valid input tree there is only one path between two vertices, so the new connecting paths are precisely the paths whose rewards we used in the matching.

The score of the grafted witness is the root's node score plus the sum of the chosen branch scores. Each branch score equals the chosen matching-edge weight. Therefore the matching objective is a score actually attained by a valid common embedding. Maximizing over matchings proves that the recurrence value is at most the independent mapped optimum.

Here there is a small but important bottom-value issue. A mapped boundary always has a feasible singleton witness, although its score might be negative infinity because the node labels are forbidden. A skipped boundary may have no feasible witness at all. In an extended score domain, both situations can have maximum negative infinity. We must not treat a negative-infinity skipped value as a certificate that an actual skipped witness exists. The Lean proof selects a skipped witness only when its value strictly improves over a mapped candidate; that ensures the skipped optimum is not bottom and has an attaining witness. Otherwise it can choose the mapped candidate. The construction never invents a nonexistent branch.

The relevant Lean files are called BranchOptimum, MatchingAssembly, MappedAssembly and MappedDecomposition. They define branch values, choose attaining boundary witnesses, graft common trees, establish score identities, and prove both directions. The final mapped_recurrence theorem equates the independently defined mapped optimum to a certified exhaustive child-matching optimum.

## From two equations to an evaluator

At this point Lemma 5 is a theorem about independently defined finite witnesses. We still need a procedure that fills a table and is known to compute those values.

The dependencies are well founded because each branch step descends into at least one child. In the diamond recurrence, one coordinate descends. In the mapped recurrence, both do. A rank based on actual root-to-vertex path depths decreases along every dependency. The shared Lean file RootedEvaluationOrder constructs a well-founded order from the actual tree geometry, rather than requiring a caller to supply a mysterious acyclic graph certificate.

The module Droschinsky2018.RootedDynamicProgram then defines a score table whose entries are pairs: mapped score and skipped score. A function step computes both from an earlier table. It enumerates possible immediate-child pairs and computes an exhaustive partial matching. For simplicity and confidence in the proof, the reference evaluator uses finite association lists and repeated synchronous rounds. Its solve function chooses enough rounds using the sum of the input vertex-list lengths, and solve_correct proves that the resulting entries equal the independent mapped and skipped optima, assuming the lists really enumerate the input vertices and the child lists really represent their oriented edges.

The source also proves rootedOptimum_correct, which takes the best mapped entry over vertex pairs in the fixed orientations, and an all-root-pairs unrootedOptimum_correct baseline. These are executable score correctness theorems. They are not a proof that the optimized production Rust implementation uses this exact table, reconstructs the original mapped vertices and paths, or achieves the published time and space bounds. The reference algorithm deliberately uses exhaustive matching, linear table reads and repeated rounds; its performance should not be confused with the 2018 paper's optimized schedule.

There is a useful contrast with the 2016 strict-isomorphism recurrence. In 2016, a child pair contributes its node and edge mapping immediately; it never spends several levels looking for a top pair. In 2018, the same matching skeleton remains, but every potential branch has a second way to continue. The diamond state's simple one-child descent is what makes all those possible path lengths manageable without explicitly listing every path at every parent pair.

We can now state the two-state design in one sentence. A mapped state can branch, but only by matching separate physical child regions. A skipped state can continue along a path, but pays for every one-sided descent until a real mapped pair appears. This division makes Lemma 5 exact. Its Lean proof works because each numeric case is attached to a concrete feasible common-tree witness and each witness can be decomposed back into those cases.

The point of a proof-oriented lecture is not merely to remember two formulas. It is to know what the formulas mean strongly enough that a changed definition would set off an alarm. If we changed the rule to reward partial physical edge matches inside a long path, the branch-value formula would change. If we let two common children share an initial physical segment, the matching decomposition would fail. If we allowed a branch to be empty and called that a diamond witness, the one-step penalty argument would fail. If we returned zero for every empty optimum, the nonempty singleton case would fail on negative weights.

The two equations are compact precisely because all these geometric and semantic obligations have been settled. The next difficulty is not the rooted recurrence itself. It is how to recover a globally optimal embedding when neither physical tree has a designated root, without solving a completely new table for every pair of possible roots.

<!-- END SPOKEN LECTURE -->

## Companion: exact 2018 Lemma 5

For fixed orientations of rooted input trees, write \(A(u,v)=\mathcal L(u,v,\wedge)\) for the mapped top pair and \(D(u,v)=\mathcal L(u,v,\diamond)\) for an *unmapped boundary pair* whose first selected common-tree pair is below on at least one side. Let \(C_T(u)\), \(C_{T'}(v)\) be child sets. Empty maxima equal \(-\infty\).

\[
D(u,v)=-p+\max\left\{
\max_{b\in C_T(u)}\{A(b,v),D(b,v)\},
\max_{c\in C_{T'}(v)}\{A(u,c),D(u,c)\}
\right\}.
\]

For each child pair \((b,c)\), define

\[
B_{u,v}(b,c)=\max\left\{D(b,c),\; A(b,c)+\omega_E(ub,vc)\right\}.
\]

If \(\mathrm{MWM}(B_{u,v})\) denotes the maximum sum over a **partial** matching of \(C_T(u)\times C_{T'}(v)\), including the empty matching, then

\[
A(u,v)=\omega_V(u,v)+\mathrm{MWM}(B_{u,v}).
\]

These are paper Lemma 5's diamond and wedge cases (the scanned paper also renders the wedge as a lambda-like symbol). A long path pair contributes only \(-p(k+\ell-2)\), never its first physical edge reward plus penalties. For \(p=\infty\), a positive skip count has value \(-\infty\).

### Independently optimized boundary witness

For a common skeleton pair-set \(P\) with selected top pair \(t=(a,b)\), the Lean state is valid at boundary \((u,v)\) if `StateValid` holds: it is a valid nonempty common embedding, its other selected pairs descend from \(t\) under the two ambient orientations, and \(t\) descends from \((u,v)\). The boundary objective is

\[
\operatorname{stateScore}(u,v,P,t)
=\operatorname{score}(P)-p\bigl(d_T(u,a)+d_{T'}(v,b)\bigr).
\]

The **mapped** feasible family has \(t=(u,v)\); the **skipped** family has \(t\ne(u,v)\). The code uses `WithBot K` for the signed/bottom score and `WithTop K` for finite or infinite penalties. The independent optima are `mappedValue` and `skippedValue`, not the values of `RootedDP.step` by definition.

### Fully specified three-versus-two-vertex worked calculation

```text
T:    U                 T':   V
      |                       |
      B                       C
                              |
                              D
```

Finite node weights only: \(\omega_V(U,V)=4\), \(\omega_V(B,C)=0\), \(\omega_V(B,D)=6\); all other vertex pairs are forbidden. The only needed finite edge weight is \(\omega_E(UB,VC)=4\); all other physical edge pairs are forbidden. Then

| State | Value | Explanation |
| --- | ---: | --- |
| \(A(B,D)\) | \(6\) | Singleton mapped pair |
| \(D(B,D)\) | \(-\infty\) | Neither boundary can descend |
| \(A(B,C)\) | \(0\) | Singleton mapped pair |
| \(D(B,C)\) | \(6-p\) | Skip `C`, pair `B` with `D` |
| \(B_{U,V}(B,C)\) | \(\max(4,6-p)\) | Direct/direct versus longer right path |
| \(A(U,V)\) | \(4+\max(4,6-p)\) | Node reward plus the one optional child pair |

At \(p=1\), \(A(U,V)=9\), realized by \((U,V),(B,D)\) with path lengths \((1,2)\). At \(p=2\) there is a tie at \(8\). At \(p=3\), \(A(U,V)=8\), realized by the direct pairs \((U,V),(B,C)\). At \(p=\infty\) the long path is excluded by score, so the mapped value remains \(8\). This calculation concerns a *mapped boundary* at `U,V`, not the unrestricted unrooted objective.

### Lean proof reading route (November 19, 2026 source archive)

1. `Droschinsky2018/BoundaryStates.lean`: `StateValid`, `stateScore`, `StateValid.skipped_cover`, `StateValid.extend_left`, `StateValid.extend_right`, `stateScore_step_left`, `stateScore_step_right`.
2. `Droschinsky2018/SkippedRecurrence.lean`: `stateFeasible`, `mappedFeasible`, `skippedFeasible`, `mappedValue`, `skippedValue`, `allStateValue_eq_max`, `skipped_recurrence_two_state`.
3. `Droschinsky2018/BranchReward.lean` and `BranchOptimum.lean`: `connecting_reward_boundary`, `matchingBranchValue`, `matchingBranchValue_attained`.
4. `Droschinsky2018/MatchingAssembly.lean`: `stateChildWeights`, `familyOfMatching_score`, `bestStateMatching_correct`, `matchingValue_le_mappedValue`.
5. `Droschinsky2018/MappedDecomposition.lean`: `source_score_upper`, `mappedValue_le_matchingValue`, `mapped_recurrence`. The decomposition depends on `ScoreDecomposition.lean`, `Shared/TreeGraft.lean` and `MappedAssembly.lean`.
6. `Droschinsky2018/RootedDynamicProgram.lean`: `RootedDP.step`, `step_correct`, `evaluate_correct`, `solve_correct`, `rootedOptimum_correct`, `unrootedOptimum_correct`. The reference uses exhaustive matching and repeated rounds; no optimized-runtime or production Rust theorem follows.

**Primary source:** Droschinsky, Kriege and Mutzel, [*Largest Weight Common Subtree Embeddings with Distance Penalties*](https://doi.org/10.4230/LIPIcs.MFCS.2018.54) (MFCS 2018), Section 4, Lemma 5, pp. 54:6–54:7; [pinned arXiv v1](https://arxiv.org/pdf/1805.00821v1). The example and pedagogical proof decomposition above are original to this track.

### Listening checks

1. Why can the skipped state descend along either input tree, but must charge the penalty exactly once for each one-sided step?
2. In the numerical example, why is the long-path branch value `6-p`, not `10-p`?
3. Why does the mapped recurrence use an optional matching rather than a matching that covers every input child?
4. What separates `mapped_recurrence` from `RootedDP.solve_correct`? What additional claim would be required to connect either result to an optimized Rust solver?
