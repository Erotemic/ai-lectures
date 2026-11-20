# The Map Is the Object: Weighted Common Subtree Isomorphism

<!-- BEGIN SPOKEN LECTURE -->

Two trees can have a large common shape and still have a poor common score. A smaller shared shape may be worth much more. If some vertex correspondences are forbidden, or if matching a particular pair of edges carries a penalty, counting the vertices tells us almost nothing about which correspondence is best.

That is the problem studied by Andre Droschinsky, Nils Kriege and Petra Mutzel in their 2016 paper, *Faster Algorithms for the Maximum Common Subtree Isomorphism Problem*. Their trees are unrooted and unordered. Their objective is weighted. The weights belong not just to vertices but also to corresponding edges. A solution is a partial mapping between the original trees, and it must describe a connected common tree without stretching an edge into a longer path.

It is worth spending a whole lecture on the problem before looking at the algorithm. The formalization succeeds only if we know what we intend the program to compute independently of how it computes it. We will define the witnesses, make the objective precise, explore some cases that defeat a size-based intuition, and finish with a guide to the Lean specification. The following recurrence lecture will then have a definite proposition to prove.

## What is actually being mapped?

Let the input trees be called G and H. Their vertices are not assumed to have a preferred left-to-right order, and neither input is assumed to come with a root. If G has a vertex called a and H has a vertex called x, a possible contribution to a solution is the declaration that a corresponds to x. We can represent an entire candidate by a finite set of such declarations: a to x, b to y, c to z, and so forth.

There are immediate requirements. No source vertex may have two images. No target vertex may be assigned to two source vertices. Thus the selected declarations form a partial bijection: a bijection between the subset of G that was selected and the subset of H that was selected. We do not require all vertices of either tree to be selected.

This is already more precise than saying that the trees have some matching labels. A label might influence the desirability of mapping a to x, but the mapping itself is an assignment between actual vertices. If the first tree contains several indistinguishable-looking leaves, the witness still records which leaf is paired with which.

Next, collect the selected vertices of G. Retain every edge of G that has both endpoints selected. That is the induced subgraph on the selected set. Do the same in H. The word *induced* is important: we do not independently choose which edges to remember after selecting the endpoints. The input graph determines them.

The selected graphs must be connected, and adjacency must be preserved in both directions. Whenever two selected vertices of G are adjacent, their images in H must be adjacent. Whenever two images in H are adjacent, their preimages in G must be adjacent. Because the selected graphs are connected subgraphs of trees, they are themselves trees. We have an isomorphism between these two selected trees, not merely a collection of appealing vertex similarities.

Consider a three-vertex path in G, with vertices a, b and c, and edges a-b and b-c. Suppose H contains a path x-y-z. The mapping a to x, b to y, c to z is a valid structural isomorphism. Reversing the path, a to z, b to y, c to x, is valid too. Nothing in the paper fixes an order of children that would distinguish those two correspondences.

Now lengthen the second path to four vertices, x-y-z-t. The assignment a to x, b to z, c to t looks as though it lines up three vertices in sequence, but it is not a common subtree isomorphism. The required edge a-b would map to x-z, which is not an edge of H. There is a path from x to z, but it has two edges. Such a path is not a substitute for an edge in the 2016 problem.

That is the clearest dividing line between this paper and the 2018 Droschinsky paper. The later problem permits an edge of a common tree to be represented by a longer path under carefully defined conditions, and it charges penalties for the skipped vertices. Here, in 2016, an edge is still an edge. We must not import the later notion of embedding into this earlier specification.

## Connected means one shared object

Why require connectivity? Without it, an optimizer could select profitable vertex pairs scattered across the trees, with no common structure joining them. That could solve a different optimization problem, but not the one in the paper.

Imagine G has a long path, and H has a long path with a completely different region of high pairwise rewards near each end. If we could select two separated singleton correspondences and call their union a solution, we would have two disconnected common components. A subtree is not a bag of disconnected pieces. The 2016 witness must select one connected component, and all its edges must survive the correspondence.

Connectivity also creates the recursive structure the algorithm will exploit. Once two vertices are mapped and chosen as roots, deleting them separates their descendant regions into branches. A connected correspondence cannot visit two different branches without passing through the mapped root. This is the reason bipartite matching appears later. The branch independence is not a programming trick; it follows from tree geometry and from connectivity of the selected witness.

There is another consequence: a singleton is a perfectly good common tree. Choose any vertex a of G and any vertex x of H. The map containing just a to x is injective, has no edges to check, and has connected selected sets. So for nonempty input trees, there is always at least one structurally valid witness. A poor numerical score does not make the witness invalid.

The singleton will be especially important when weights are negative. It prevents the mathematical objective from quietly turning into a maximum with an empty candidate of score zero.

## A weight is attached to a correspondence

The paper supplies a commutative weight function. It can score a pair of mapped vertices, and it can score a pair of mapped edges. For instance, mapping a to x might contribute seven, and mapping the edge a-b to the edge x-y might contribute negative ten. The score of a complete witness is the sum over all its mapped vertices plus the sum over all its mapped edges. Each undirected edge contributes exactly once.

The edge part is not an afterthought. It permits a correspondence that looks attractive on node features but damages a relationship to be penalized. Conversely, a pair of edges may fit extremely well even if the participating node matches have modest scores. The method allows arbitrary real weights, including negative ones, and uses negative infinity as a possible value.

The symmetry of undirected edges is not a claim that the vertex similarity is constant. It means the edge a-b is the same edge as b-a, and reversing the written order of its endpoints must not alter its reward. We do not count each edge twice just because it has two endpoint orderings.

Here is a very small example that completely changes our notion of an optimum. G contains one edge a-b, and H contains one edge x-y. Assign the vertex correspondence a to x a reward of seven, and b to y a reward of two. Assign the edge correspondence a-b to x-y a reward of negative ten. Suppose the other vertex correspondences are forbidden by negative-infinity rewards.

There are three relevant finite-score connected witnesses. The singleton a to x scores seven. The singleton b to y scores two. Mapping both vertices and the edge scores seven plus two minus ten, which is negative one. The maximum-cardinality common tree has two vertices. The maximum-weight common tree has just one, with score seven. An algorithm that insists on retaining an available edge would return the wrong answer.

Change that edge reward to positive ten, without changing the vertex scores. Now the two-vertex mapping scores nineteen and becomes optimal. The structural feasibility problem has not changed at all. Only the objective has changed. This separation between legality and desirability should stay fixed in our thinking.

There is no guarantee that a locally attractive vertex or edge pair belongs to a globally best witness. In the two-vertex example the large edge penalty reverses a size preference. In a larger tree, a vertex pairing that appears attractive can block two mutually compatible branch pairings. The optimization must account for whole connected correspondences.

## Negative scores and the missing zero

Suppose G and H each consist of just one vertex, and the weight of their unique correspondence is negative three. What is the maximum common subtree-isomorphism score?

For the paper's nonempty problem, the answer is negative three. The unique singleton is structurally valid, and there are no other nonempty candidates. It would be incorrect to announce zero merely because an empty mapping has no reward. The empty mapping is not a nonempty connected common tree.

A library can reasonably offer a different convention. It may permit the empty result and give it score zero, so a caller asking for an optional similarity might prefer no correspondence to a negative one. The NetworkX project does expose empty-allowed behavior, and it also distinguishes explicit nonempty modes. Those interface choices must not be confused with the paper's mathematical definition.

The distinction survives even inside a rooted dynamic program. Once a mapped root pair is required, we may omit any number of negative-contribution branches, but we cannot omit the root itself. The best rooted value might be negative. A recurrence that clamps each rooted state to zero will silently replace the rooted problem with an optional-root problem. It can be used as part of another design only if the wrapper reconstructs the intended nonempty objective correctly.

What should we make of negative infinity? The paper allows it in its weight domain. It is a way to make some correspondences prohibitively bad, for example to express incompatible labels. But we should distinguish two assertions: a structurally invalid correspondence is excluded from the feasible family, whereas a structurally valid correspondence might have negative-infinity score. The latter still has a legitimate witness in the specification. If every feasible witness has score negative infinity, an optimum still exists, and its value is negative infinity.

This sounds pedantic until we build a formal definition. The logic of graph isomorphism and the arithmetic of the score are different fields of the specification. Treating negative infinity as if it literally deleted a vertex or rewrote an adjacency relation makes the formal problem harder to state and can conceal errors in edge cases.

## Rooted and unrooted are different restrictions

There is no root in the original problem. Nevertheless, we will introduce roots to perform the recursion. Rooting a tree does not alter its edges. It selects a parent direction on those edges and divides the tree into descendant regions. The rooted version of the problem also requires the chosen roots of the two subproblems to correspond.

That last sentence is the actual restriction. A root is not merely a convenient pointer into a representation; saying that u must map to v removes candidates. For example, if the best unrooted correspondence consists of the singleton a to x, then a rooted subproblem that insists on b to y cannot return that witness, even though the original two-edge input might contain both pairs.

To study a rooted state, fix an ambient root in each input, then choose a vertex u in G and a vertex v in H. Restrict attention to the descendant subtree of u and the descendant subtree of v. Insist that u corresponds to v. Among all connected witnesses obeying these conditions, take the best score. That number is the independent rooted optimum. It exists before we have written any recurrence, matching code, or dynamic-programming table.

A minor subtlety is that we need two levels of roots in the formalization. The ambient roots determine what *descendant* means throughout a table, and u and v are the current subproblem roots required to correspond. Keeping the ambient orientation fixed avoids changing the meaning of a table entry while the recursion runs. A later theorem allows us to choose one ambient left root without losing the unrooted optimum, but that theorem will require a proof.

## How a finite specification earns an optimum

We can define the optimum without knowing an efficient algorithm. Enumerate, conceptually, all subsets of pairs of input vertices. Keep those subsets that form partial bijections, whose selected subgraphs are connected, and whose selected adjacency is preserved both ways. Compute each feasible candidate's score. Pick a candidate with maximum score.

This is not how we intend to solve a large instance. The number of candidate subsets is immense. But it is a perfectly sound mathematical specification, and it is finite. The singleton observation shows the feasible collection is nonempty. A nonempty finite set of scores in a linearly ordered domain has a maximum. Thus the optimum is actually attained by a witness. We do not need compactness, limits, or convergence arguments. The existence proof rests on the finiteness of the original vertex sets.

This supplies a helpful discipline for later formalization: when we prove that an algorithm is optimal, we should compare it with this independently defined family, not with another copy of the same algorithm. Two implementations agreeing with each other would not establish that either one computes the intended common subtree.

## The formal witness in Lean

The uploaded repository gives the specification concrete names. In `Droschinsky2016/Specification.lean`, `Mapping` is a finite set of vertex pairs. `PartialBijection` says that the two projections are injective. `Valid` adds nonemptiness, connected induced subgraphs on both sides, and the adjacency equivalence for every pair of selected mappings. `ValidOrEmpty` is the separate empty-allowed convention.

The scoring structure has a `node` function on vertex pairs and an `edge` function on pairs of undirected edges. The source stores an undirected pair using the symmetric-pair construction, often pronounced 'sym two.' The function `mappedEdges` collects each abstract edge of the selected common tree once. The function `score` sums the selected node rewards and the selected edge rewards. `IsMaximum` then asserts both validity of a proposed witness and that every independently valid competitor has score no greater.

There is an important type choice: the weight type is `WithBot K`. It means an ordered numeric type K, extended with a bottom element. For the real-valued paper, K can be the real numbers, and bottom represents negative infinity. The development also generalizes these arguments to ordered integer scoring. It has not thereby proved that a bounded machine integer cannot overflow, or that a floating-point implementation agrees exactly with real arithmetic. The theorem concerns mathematical values.

In `Witness.lean`, the declaration `Valid.inducedIso` takes a valid finite mapping and constructs an actual graph isomorphism between the induced selected subgraphs. This is a meaningful bridge. The initial definition is convenient for enumerating and manipulating finite maps. The conclusion uses the graph-theoretic isomorphism object supplied by Mathlib. The theorem shows that the finite witness is not merely a pair list that happened to pass several unrelated checks.

The development also proves `singleton_valid` and `score_singleton`. These express the foundational edge cases we reasoned through: one pair always forms a legal structural common tree, and its score is precisely its vertex-pair reward. The theorem `exists_maximum` then gives an attaining witness for every pair of finite trees, without requiring nonnegative weights.

The proof of existence is intentionally not a polynomial-time algorithm. The independent finite feasible family is defined by a powerset and a filter. That is a specification. The future algorithm will use a far smaller family of rooted states and reduce local choices to matching problems. Its correctness will mean that the efficient computation reaches the same optimum as the powerset specification.

This is the basic point of keeping the map independent of the code. The legal objects are finite, connected, and exact. Their score can be negative. Each selected edge is counted once. Empty is a different convention. Only after those facts are fixed can we ask why a child-matching recurrence computes the greatest score.

<!-- END SPOKEN LECTURE -->

## Non-spoken companion: precise 2016 specification

### Independent feasible witnesses

Let `G=(V_G,E_G)` and `H=(V_H,E_H)` be nonempty finite trees. A witness is a finite relation

\[
P\subseteq V_G\times V_H
\]

such that

1. `P` is nonempty.
2. `P` is injective in both coordinates, so it represents a bijection between selected vertex sets `S_G`, `S_H`.
3. The induced graphs `G[S_G]` and `H[S_H]` are connected.
4. For all `(u,v),(u',v')` in `P`, `uu' in E_G` if and only if `vv' in E_H`.

Since the input graphs are trees, the connected induced subgraphs are themselves trees. No edge can be realized by a length-two or longer path.

### Score and optimum

For a commutative weight function on paired vertices and paired undirected edges,

\[
W(P)=\sum_{(u,v)\in P}\omega_V(u,v)
  +\sum_{\{(u,v),(u',v')\}\in E(P)}
       \omega_E(\{u,u'\},\{v,v'\}).
\]

Here `E(P)` contains each unordered selected common edge exactly once. The paper's weight codomain is `R union {-infinity}`; Lean uses `WithBot K`. The nonempty optimum is `max { W(P) : Valid(P) }`.

For `G=a-b`, `H=x-y`, define `omega_V(a,x)=7`, `omega_V(b,y)=2`, `omega_E(ab,xy)=-10`, with other vertex pairs at `-infinity`. Scores: singleton `(a,x)` is `7`; singleton `(b,y)` is `2`; both pairs together yield `-1`. Thus maximum *weight* is `7`, while maximum *vertex count* is `2`. With single-vertex inputs scored `-3`, the paper's optimum is `-3`, not `0`.

### Source/Lean correspondence (2026-11-19 source snapshot)

| Concept | Code declaration | Meaning |
| --- | --- | --- |
| Finite pair relation | `Droschinsky2016.Mapping` | Candidate list of actual vertex pairs |
| Partial bijection | `PartialBijection` | No repeated left or right endpoint |
| Structural validity | `Valid` | Nonempty, induced connected subsets, adjacency equivalence |
| Optional-empty extension | `ValidOrEmpty` | An explicit API alternative, not the paper's nonempty contract |
| Node and edge weights | `Scoring` / `score` | `WithBot K` and each unordered edge counted once |
| Optimum | `IsMaximum`, `feasible`, `exists_maximum` | Finite specification independent of an algorithm |
| Graph-isomorphism bridge | `Valid.inducedIso` | Constructs Mathlib graph isomorphism of selected induced trees |
| Rooted restriction | `RootedValid`, `rootedValue` in `Rooted.lean` | Maps a designated root pair inside two descendant regions |

**Paper:** Droschinsky, Kriege and Mutzel (2016), arXiv `1602.07210v4`, Section 2 (Definitions and MCSI/MCST weighting) and the opening of Section 3. [Pinned PDF](https://arxiv.org/pdf/1602.07210v4). Published version: *MFCS 2016*, DOI `10.4230/LIPIcs.MFCS.2016.33`.

**Repository evidence:** `proofs/SubtreeProofs/Droschinsky2016/Specification.lean`, `Witness.lean`, `Rooted.lean`, `proofs/PROOF_STATUS.md`, `docs/planning/paper_statement_crosswalk.md` in the supplied 2026-11-19 source archive.

**Boundaries:** `exists_maximum` is mathematical attainment, not a complexity theorem. `WithBot K` is exact arithmetic and is not a proof of f64 behavior. Valid finite relations with score negative infinity are not excluded merely by their score; structural validity and numerical score are separate.
