# The Price of a Skipped Vertex: Exact Scores in Droschinsky 2018

<!-- BEGIN SPOKEN LECTURE -->

Suppose two trees have a perfectly good common branching structure. In one input, the connection between two mapped vertices is a single edge. In the other, it is a path of two edges, passing through one intermediate vertex. How should we score that agreement?

One possibility is to reward the labels of the mapped endpoints and ignore the extra vertex. Another is to charge something for the extra distance. A third is to compare the individual physical edges along the two paths. These would define three different optimization problems, even though their admissible common trees might be identical.

Droschinsky, Kriege, and Mutzel chose a particular answer in Definition 4 of their 2018 paper. It is simple enough to state in one sentence, but it is easy to implement incorrectly: **an abstract edge receives an edge-label reward only when both of its realized paths consist of exactly one edge; in every other case it receives a penalty proportional to the total number of skipped interior vertices.**

The phrase “in every other case” carries much of the mathematics. A path of length one paired with a path of length two does not receive the label reward for the direct edge. It receives one skipped-vertex penalty. Even if that direct edge has a spectacularly favorable label, the edge reward is not added. Conversely, an abstract edge represented by two direct physical edges can receive a negative reward, and the optimizer may prefer a longer, penalized alternative if a valid embedding exists.

We will derive the score from the structural object, work an example in which the preferred mapping changes as the penalty rises, and then see how the exact same distinction appears in the Lean formalization.

## The common skeleton decides what is scored

We begin with a valid topological common-tree witness. It selects a nonempty finite set of vertex pairs. Those pairs are connected into an abstract common tree whose edges are realized by internally disjoint paths in both input trees.

There are two kinds of contribution. For every selected abstract vertex, we compare the labels of its two physical images. For every abstract edge, we compare its two realized physical paths. We add all these contributions together.

The node weight is a function of two input vertices. If Alice's abstract vertex is represented by u in the first tree and v in the second, its contribution is the weight of the pair u and v. Such weights can be positive, zero, or negative. The paper also permits a value of negative infinity to forbid a particular label pairing.

The path contribution needs more care. Let the first realization of an abstract edge use k physical edges, and the second use ell physical edges. Both lengths are at least one: two distinct abstract endpoints cannot map to the same physical vertex under an injective embedding.

If k and ell are both one, we have a genuine edge-to-edge correspondence. The contribution is the edge-label comparison weight. The penalty parameter does not appear in that case.

If either length exceeds one, the edge-label reward is replaced by a distance penalty. A path with k physical edges has k minus one interior vertices. The other path has ell minus one. So the total number of skipped vertices is k plus ell minus two. If the penalty per skipped vertex is p, the abstract edge contributes the negative of p times that number.

The distinction is not between an edge in one input and a path in the other. It is between two single-edge paths and *everything else*. That includes length one versus length two, length two versus length one, length two versus length two, and arbitrarily longer pairs. A direct physical edge on one side does not preserve its label reward when the corresponding path on the other side is longer.

There is a further counting subtlety. The penalty is charged once for each interior vertex *on a realized common edge*. It is not charged for every unselected vertex of the input tree. If a whole branch is unused, its vertices do not appear in the score. If a physical vertex is the image of an abstract common-tree vertex, it contributes a node weight instead; it is not an interior skipped vertex of that abstract edge.

This precise separation makes the objective additive over the common skeleton. Each mapped abstract vertex is counted once. Each abstract edge has exactly one path pair and is counted once. Disjoint path interiors ensure that the bookkeeping corresponds to a genuine tree realization, not to several purported edges passing through the same hidden branch point.

## A fork with two possible correspondences

Let us return to a pair of small rooted trees, but give them numerical weights.

The first tree has a root A. One branch runs A to x to B, a path of length two. The other runs directly from A to C, a path of length one. The second tree has a root a. One branch goes directly from a to b, and the other goes a to y to c. The two path lengths at the second root are one and two.

We will compare two valid three-vertex common forks. In both, A maps to a and the two remaining selected vertices represent the two abstract children. Both are feasible because the chosen paths leave the respective mapped roots in distinct branches. Their difference is which child is paired with which.

First consider the *straight* correspondence: A with a, B with b, and C with c. Assign the three node weights four, six, and five. The node total is fifteen.

The branch from A to B has two physical edges, while the branch from a to b has one. That path pair contains one skipped vertex, x. Its contribution is minus p. The branch from A to C is direct, while the branch from a to c uses the intermediate vertex y. That also contributes minus p. Neither abstract edge receives an edge-label reward, because neither has two direct paths.

The total straight score is fifteen minus two p. At p equal to two, the score is eleven.

Now consider the *crossed* correspondence: A still maps to a, but B maps to c and C maps to b. Assign node weights four for A and a, five for B and c, and three for C and b. The node total is twelve.

The abstract branch from A to B is realized by A to x to B on the first side, and by a to y to c on the second. Both paths have length two. There are two skipped interior vertices, x and y, so this branch contributes minus two p.

The other abstract branch is direct on both sides: A to C in the first tree, a to b in the second. Suppose the comparison weight of those two physical edges is seven. Now, and only now, the edge-label reward seven enters the score. No penalty is applied to that direct pair.

The total crossed score is twelve plus seven minus two p: nineteen minus two p. At p equal to two, it is fifteen. It beats the straight correspondence's eleven, even though the straight correspondence has the larger node total. The direct edge-label agreement makes the difference.

Here is a detail worth checking twice. In the crossed correspondence, the long branch crosses two interior vertices, one on each side, so the penalty is four when p is two. We do not charge a penalty to the direct branch merely because its sibling is long. We also do not reward either of the physical edges along the long branch. Its entire abstract-edge contribution is minus four.

## The penalty can change the preferred common tree

The optimizer has another option. It can choose a smaller common tree and discard a branch altogether. Consider the two-vertex common tree matching only A with a and C with b. The node weights sum to seven. Its only abstract edge is direct on both sides and contributes the edge reward seven. So this two-vertex witness scores fourteen, with no skipped vertices and no dependence on p.

We now have three explicit feasible candidates: the straight three-vertex fork, worth fifteen minus two p; the crossed three-vertex fork, worth nineteen minus two p; and the direct two-vertex tree, worth fourteen.

At penalty two, the three values are eleven, fifteen, and fourteen. Among these candidates, the crossed three-vertex fork wins by one point.

At penalty three, the values are nine, thirteen, and fourteen. The smaller two-vertex tree wins. Raising the penalty has made the extra mapped vertex less valuable because keeping it requires a long realized branch. In this example, the threshold between the crossed fork and the direct smaller tree is p equal to two and a half. Above that value, the direct two-vertex witness scores better; below it, the crossed fork does.

We should be precise about what this arithmetic proves. We have compared three constructed valid witnesses. We have not specified the weights of every other possible vertex pair or edge pair, so we have not proved that one of these three is globally optimal among *all* possible embeddings. The point is that the very same geometry can support an explicit tradeoff between mapped vertices, direct edge labels, and skipped-vertex costs. Once all weights are supplied, a global algorithm must make that choice over the complete feasible family.

The threshold also shows why the distance penalty is not merely a last-minute correction to a fixed correspondence. Changing p can change which abstract tree is selected, how many vertices it has, and which pairs of physical vertices represent its nodes. It is an optimization parameter, not just an annotation on an already chosen mapping.

## An important negative example

Suppose a direct physical edge in the first tree has a label that is badly incompatible with a direct physical edge in the second. Their comparison weight is minus ten. If we insist on pairing those physical edges as an abstract edge with two length-one realizations, the contribution is minus ten.

Now suppose the geometry also permits us to realize the abstract edge through a path with one intermediate vertex in one of the inputs. At p equal to two, that alternative abstract edge contributes minus two, not minus ten. We have traded a direct label comparison for a skipped-vertex penalty.

This is not an instruction to add minus two to minus ten. It is a choice of one branch of the scoring definition *instead of* the other. A common implementation error would compute the direct-edge reward and then subtract a penalty for any extra interior vertices. That would yield minus twelve in this example. It is not the formula in Definition 4.

The opposite error is just as damaging. Suppose the direct edge reward is positive one hundred, but the other realization has length two. If an implementation awards the hundred and subtracts p, it will strongly prefer a correspondence to which the paper assigns only minus p. That mistake can change the optimum by more than the entire contribution of every mapped vertex.

The condition for the edge-label reward must therefore be tested on **both** realized path lengths. The score is not a sum of the labels of all physical edges traversed, and it is not a reward for the shorter of the two paths. The only physical edges that receive edge-label comparison weights are those paired as direct representatives of a single abstract edge in both inputs.

## Infinite penalties and forbidden matches

The paper allows p to be infinite, even though the finite-penalty case is the main algorithmic model. This turns the topological embedding problem back toward the strict edge-to-edge situation: any abstract edge realized by a longer path incurs an infinite penalty and therefore contributes negative infinity. A finite-scoring common embedding can use only direct edge pairs.

But infinite penalty does not mean that every unselected physical vertex is forbidden. You can still omit an entire unused branch. You can still choose a single abstract vertex and incur no path penalty. What becomes impossible at finite score is traversing an unselected interior vertex along an abstract edge.

There is a second infinity in the model, and it plays a different role. A node-pair or edge-pair weight can be negative infinity to express incompatibility. If both paths are direct and their edge-label pairing is forbidden, the abstract edge receives negative infinity. If one path is long, the direct-edge comparison is not used at all. The resulting penalty is determined by the number of skipped vertices instead. Those two mechanisms should not be collapsed into a single vague concept of a bad match.

It is equally important not to clamp all negative solutions to zero. The paper's feasible common tree is nonempty. If each input consists of one vertex and their only node comparison has weight minus four, the sole nonempty common embedding has score minus four. That is the optimum of the nonempty mathematical problem. An API may offer an empty mapping of score zero as a convenience, but then it is implementing a different outer convention. The independent Lean specification preserves the nonempty optimum.

At p equal to zero, long realized paths are permitted without a numeric penalty. That does not restore the edge-label reward along those paths. For any abstract edge whose realization is long on at least one side, the path contribution becomes zero. The switch between the two scoring cases remains present even when its penalized branch happens to evaluate to zero.

## One provable monotonicity statement

An increasing penalty makes a given long path no more attractive. There is a general theorem hiding in that observation.

Fix any valid common embedding and compare its score at penalties p and q, where q is at least p and both are finite and nonnegative. Its mapped-node contributions do not change. Any direct edge-to-edge contribution also does not change. Every longer path pair has a nonnegative number of skipped vertices, so multiplying that count by a larger penalty produces a contribution that is no greater than before.

Therefore the score of this *fixed witness* at q cannot exceed its score at p. This first inequality is immediate from the scoring formula.

Now let the witness change optimally with the penalty. Choose an embedding that attains the optimum for q. We know its q-score is at most its own p-score. And its p-score is at most the maximum p-score over all embeddings. Thus the optimum at q is no greater than the optimum at p.

Notice that the proof allows the actual maximizing embedding to change. That is why we used the q-optimal witness as an intermediate object rather than comparing the identities of the two optimizers. It also allows negative node scores, forbidden pair weights, and arbitrary choices of which branches to discard. Feasibility does not depend on the finite penalty value, so the same witness is available at both parameter settings.

In the Lean repository, `score_antitone` expresses the pointwise inequality for a fixed pair relation, and `maximum_score_antitone` lifts it to the independently defined optimum. This is not merely a regression about one numerical example. It is a theorem for all finite valid instances under the specified ordered-ring assumptions.

## Reading the actual Lean score

The source file `Droschinsky2018/Specification.lean` is an unusually direct place to compare paper and formalization, because the score expression closely follows Definition 4.

The `pathLength` helper extracts the length of the unique path between two selected endpoints. The endpoints are represented as unordered pairs, because the score does not depend on which endpoint we name first.

The function `skippedScore` takes the penalty and a natural number of skipped vertices. For a finite penalty, its output is the negative penalty times that count. If the penalty is infinite, a zero skipped count gives zero and a positive skipped count gives negative infinity. This explicit case avoids problematic arithmetic with zero multiplied by infinity.

The function `pathScore` first checks whether both realized paths have length one. If they do, it returns the corresponding edge-pair weight. Otherwise it computes the total interior count and calls `skippedScore`.

The `score` function then adds the node weights over every mapped pair and the path scores over every abstract skeleton edge. It does not add node weights for interior skipped vertices. It does not traverse every physical edge of a long path to accumulate label rewards. The abstract common skeleton determines what is counted.

Several named theorems make good reading checkpoints. `pathScore_direct` shows that two one-edge paths receive exactly the edge weight. `pathScore_skipped` states the complementary case. `one_two_path_score` specializes to one path of length one and another of length two and proves the contribution is exactly minus p. That last theorem is particularly useful as a guard against the mistaken edge-plus-penalty formula.

The proof goes beyond local scoring. `score_singleton` shows that a one-vertex common embedding receives precisely its node weight. `exists_maximum` establishes that the nonempty finite family attains an optimum. `maximum_score_antitone` proves the monotonicity argument we just gave. In `Droschinsky2018/Reconstruction.lean`, `score_pairedImage` connects the pair-set representation of a witness to the abstract common-tree realization and its score. `GraftScore.lean` and `ScoreDecomposition.lean` later support the additive branch accounting needed by the recurrence.

Each of these theorems solves a specific problem. None by itself asserts that an optimized Rust tree algorithm uses the same branches, preserves exact real-number arithmetic, reconstructs the same physical paths, or meets the paper's time bound. Those additional interfaces remain separate work.

## Why the dynamic program needs to remember skipping

We can now see why the 2018 recurrence cannot simply reuse the 2016 matching state with a small adjustment to its edge weights.

In the strict isomorphism setting, once two parent vertices are matched, their selected child branches must begin at their actual children. The parent-to-child edges are direct on both sides. Every matched child pair has a straightforward edge contribution.

Under topological embedding, a branch can travel down one input before reaching the next mapped vertex. The other input may remain at its current vertex, travel down too, or reach a mapped vertex at once. The branch's future score depends on whether the current boundary vertices are themselves selected as a matched pair or whether one of them is being skipped along a connecting path.

That is the reason for the paper's two table types. One is a mapped-root state, where the current pair of roots is a selected common vertex. The other is a skipped state, in which the current boundary passes through at least one vertex that is not currently selected. Its value already includes the appropriate penalty for each skip. When the algorithm later attaches the branch to a matched parent, it can choose the correct score without adding the edge-label reward to a longer path.

The next mathematical derivation is Lemma 5. Its mapped state chooses a partial matching between child branches. For a paired set of children, it compares the result of an already skipped path with a directly matched continuation plus an edge reward. Its skipped state descends through one side or the other and subtracts one penalty step. We will need to prove that these two types partition the possible geometric behaviors without losing any valid witness or charging any skipped vertex twice.

But the numerical objective is no longer mysterious. It consists of mapped vertex weights and one contribution for each abstract common edge. That contribution is either a direct edge-label comparison or a path-length penalty, never both. With that rule fixed, the two-state recurrence can be treated as a mathematical theorem rather than as a plausible piece of code.

<!-- END SPOKEN LECTURE -->

## Mathematical companion: Definition 4 as an exact score

For a valid common witness \(\varphi\), each abstract common edge \(e\) is realized by two paths \(P_e\subseteq T\) and \(Q_e\subseteq T'\). Write \(k=|E(P_e)|\ge 1\), \(\ell=|E(Q_e)|\ge 1\), and let \(p\in\mathbb{R}_{\ge0}\cup\{\infty\}\). Then

\[
\omega_p(P_e,Q_e)=
\begin{cases}
\omega_{E}(P_e,Q_e), & k=\ell=1,\\
-p\bigl((k-1)+(\ell-1)\bigr), & \text{otherwise}.
\end{cases}
\]

Here \(\omega_E\) compares the *two direct physical edges* when both paths have length one; it is not a path-sum. The whole witness score is

\[
\mathcal W_p(\varphi)
=\sum_{(u,v)\in\varphi}\omega_V(u,v)
+\sum_{e\in E(S)}\omega_p(P_e,Q_e),
\]

where \(S\) is the abstract common tree. A vertex outside all realized abstract-edge interiors and outside the selected pair set has no contribution.

### Worked example: complete numerical accounting

Input trees:

```text
First:         A           Second:       a
              / \                       / \
             x   C                     b   y
             |                               |
             B                               c
```

Specify node weights \(\omega_V(A,a)=4\), \(\omega_V(B,b)=6\), \(\omega_V(C,c)=5\), \(\omega_V(B,c)=5\), and \(\omega_V(C,b)=3\). Give the direct edge pair \((A,C)\leftrightarrow(a,b)\) weight \(7\). Other node/edge weights are not specified, so the following is a **comparison of these feasible witnesses**, not a globally certified optimum.

| Selected pairs | Node sum | Realized abstract-edge paths | Edge/path contributions | Total |
| --- | ---: | --- | --- | ---: |
| \((A,a),(B,b),(C,c)\) | \(4+6+5=15\) | \((2,1),(1,2)\) | \(-p-p\) | \(15-2p\) |
| \((A,a),(B,c),(C,b)\) | \(4+5+3=12\) | \((2,2),(1,1)\) | \(-2p+7\) | \(19-2p\) |
| \((A,a),(C,b)\) | \(4+3=7\) | \((1,1)\) | \(+7\) | \(14\) |

At \(p=2\) the scores are \(11,15,14\), respectively. At \(p=3\) they are \(9,13,14\). The crossed fork and the direct two-vertex tree tie at \(p=5/2\). For \(p=\infty\), any witness with a path of length greater than one has score \(-\infty\), while the direct two-vertex candidate still scores \(14\).

### Edge cases

- **Direct/direct:** length \((1,1)\) gives the edge-label reward even if negative or forbidden (negative infinity).
- **Direct/one-skip:** length \((1,2)\) gives \(-p\), *not* edge reward minus \(p\).
- **One-skip/one-skip:** length \((2,2)\) gives \(-2p\).
- **Zero penalty:** longer paths contribute zero, but do *not* acquire edge-label rewards.
- **Infinite penalty:** longer paths contribute negative infinity; a direct/direct edge still gets its label weight.
- **Singleton:** no abstract edges, score equals the one mapped-node weight. Negative optima are possible under the nonempty paper specification.

### Penalty monotonicity proof

For finite \(0\le p\le q\), every feasible witness satisfies \(\mathcal W_q(\varphi)\le\mathcal W_p(\varphi)\). Let \(\varphi_q\) maximize \(\mathcal W_q\). Then

\[
\max_\varphi\mathcal W_q(\varphi)
=\mathcal W_q(\varphi_q)
\le\mathcal W_p(\varphi_q)
\le\max_\varphi\mathcal W_p(\varphi).
\]

This does not assume that the same embedding maximizes both objectives.

### Proof reading route (supplied 2026-11-19 source snapshot)

- `proofs/SubtreeProofs/Droschinsky2018/Specification.lean`: `skippedScore`, `pathScore`, `score`, `pathScore_direct`, `pathScore_skipped`, `one_two_path_score`, `score_singleton`, `exists_maximum`, `score_antitone`, `maximum_score_antitone`.
- `proofs/SubtreeProofs/Droschinsky2018/Reconstruction.lean`: `score_pairedImage` bridges abstract common-tree realization and selected-pair scoring.
- `proofs/SubtreeProofs/Droschinsky2018/GraftScore.lean`: `realizationScore_graft` supports root/branch score additivity.
- `proofs/SubtreeProofs/Droschinsky2018/ScoreDecomposition.lean`: `score_decomposition` splits realized score by common-tree branches.
- `proofs/SubtreeProofs/Droschinsky2018/BranchReward.lean`: `connecting_path_score` gives the precise mapped-versus-skipped contribution at branch attachment.
- `proofs/SubtreeProofs/Droschinsky2018/BoundaryStates.lean` and `SkippedRecurrence.lean`: two boundary types and the verified skipped recurrence, developed further in the next paper lecture.

**Primary reading:** Droschinsky, Kriege, Mutzel, *Largest Weight Common Subtree Embeddings with Distance Penalties*, [arXiv:1805.00821v1](https://arxiv.org/pdf/1805.00821v1), Section 4, Definition 4 and Lemma 5; [MFCS 2018](https://doi.org/10.4230/LIPIcs.MFCS.2018.54). Numerical values above are newly constructed examples, not examples attributed to the paper.

### Listening checks

1. Why does a physical edge in a \((1,2)\) path pair contribute no edge-label weight?
2. Which exact total would an incorrect “edge reward minus skip penalty” formula assign to the crossed fork?
3. Why does raising \(p\) never raise the independent nonempty optimum, even when the maximizing witness changes?
4. Under infinite penalty, what kinds of unselected input vertices can remain absent without incurring any penalty?
