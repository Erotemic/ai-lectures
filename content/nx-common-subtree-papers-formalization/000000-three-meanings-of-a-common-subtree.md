# 000000 — Three Meanings of a Common Subtree

**Track:** NX Common Subtree Papers & Formalization. **Section:** Orientation. **Background:** Basic graph vocabulary; this lecture defines the distinctions needed for the papers. **Focus:** What the three optimization problems ask, what a witness proves, and why mathematical correctness, source correctness and complexity are different obligations.

<!-- BEGIN SPOKEN LECTURE -->

# Three Meanings of a Common Subtree

Suppose we have two trees and want to know how much structure they have in common. This sounds like an easy sentence to turn into an algorithm. Compare their branches, keep what agrees, and discard everything else. But the word “discard” is already hiding several different mathematical operations. Are we allowed to remove an entire branch? Are we allowed to shorten a chain of vertices without removing its endpoints? Can we merge a parent into a child and promote the child's descendants? Does it matter which child came first? And if two candidate matches have different sizes but different scores, what does “largest” mean?

Those questions lead to the three papers at the center of this course. They are connected by trees and optimization, but they do not solve three versions of one interchangeable definition. The differences are the reason their dynamic programs look different, and the reason a formal proof must begin by specifying the problem before proving an algorithm correct.

We will work through an example small enough to hold in the imagination. Picture a tree whose root is named Alice. Alice has one child, a vertex called Bridge. Bridge has two children, Bob and Carol. In another tree, Alice has Bob and Carol directly as children. The first tree has a branching point one level below Alice. The second branches immediately.

Could a common subtree use Alice, Bob, and Carol on both sides? If we may contract the Alice-to-Bridge edge in the first tree, yes: merging Bridge into Alice promotes Bob and Carol to Alice's children. If we must preserve every selected edge exactly, no. Neither Alice-to-Bob nor Alice-to-Carol is an edge of the first tree. If we may replace an edge of a common tree by an entire path in an input tree, there is another question: can the two paths, Alice through Bridge to Bob and Alice through Bridge to Carol, share Bridge as an internal vertex? Under the usual topological embedding condition, they cannot. The two intended common edges would share an interior vertex. So even the ability to skip vertices does not automatically authorize this branching contraction.

We have just distinguished edge contraction from topological path embedding, and both from strict subtree isomorphism. A drawing can make those operations look deceptively similar. A proof cannot.

## What a tree gives us

A finite, undirected tree is a connected graph with no cycles. Between any two vertices there is exactly one simple path. The uniqueness is powerful: we do not need to choose among alternative routes when asking how two retained vertices are connected. Nevertheless, we must still decide what operations are permitted on that path.

A root is a distinguished vertex. Once chosen, every other vertex has a unique parent: its neighbor on the route toward the root. Its other neighbors are children. If a child has descendants, those descendants form a smaller rooted tree. An unrooted tree has no distinguished direction until we give it one for purposes of an algorithm.

Order is an additional structure. In an ordered rooted tree, the children of each vertex form a list, not just a set. A root whose first child is a leaf and second child is a chain is different, as an ordered object, from the root with those two children reversed. In an unordered tree, the two presentations describe the same structural shape. Drawing children from left to right does not make an unordered input ordered; the ordering has to be part of the problem's contract.

These distinctions determine what counts as a solution. A candidate is usually not just a number. It is a mapping between selected vertices, or a common tree equipped with two mappings back into the inputs. Such a mapping is a witness. A validator should be able to check that the witness respects exactly the relevant constraints, without needing to solve the optimization problem again.

## The first paper: contractions and balanced words

Antoni Lozano and Gabriel Valiente's 2004 paper, On the Maximum Common Embedded Subtree Problem for Ordered Trees, considers rooted, ordered trees and edge contractions. Contracting the edge from a parent to one of its children merges the two vertices; the grandchildren are inserted into the parent's child sequence at that child's position. The relative ordering of surviving branches is preserved.

There is a productive way to write an ordered tree as a balanced sequence of opening and closing symbols. Every edge contributes a matching pair. Walking down the edge contributes an opening symbol; returning contributes a closing symbol. Contracting an edge corresponds to deleting its matched pair, including when the pair occurs deep inside another pair. The structure of the nesting remembers which child belonged to which parent and in what order.

Now we can ask for the largest structure obtainable from each tree by a sequence of edge contractions. After encoding, the question becomes a longest common balanced sequence problem. It resembles longest common subsequence, but ordinary deletion of individual letters would destroy the matching-pair structure. Valid deletions have to respect the tree interpretation.

A key part of the 2004 algorithm is finding a restricted collection of balanced-word subproblems, small enough to support a dynamic program. Its size depends on the number of edges, depth and leaves of the original trees. That accounting is not decorative: it is what turns a recursive idea into a particular polynomial-time bound.

There is also a small but consequential issue in the published definition of containment. The formalization repository preserves its literal recursive wording and separately defines the operational relation generated by deleting arbitrary matched pairs. These two relations are not equivalent. For example, deleting a matched pair inside the word zero-zero-one-zero-one-one can produce zero-zero-one-one, but the least relation generated by the printed containment clauses cannot produce that result. The project has a compiled counterexample and a general operational correspondence to tree contractions. This is a useful reminder that the paper's intended problem, a particular printed formulation, and the recurrence used to solve the problem must each be examined on their own terms.

## The second paper: strict structural agreement

The 2016 paper by Andre Droschinsky, Nils Kriege and Petra Mutzel studies maximum common subtree isomorphism for unordered, initially unrooted trees. Here a common tree must be realized by an isomorphism between selected connected subtrees. Its edges remain genuine edges on both sides. We may discard branches, but we do not turn a two-edge route into one edge by collapsing the internal vertex.

The result can be scored with a weight for each matched pair of vertices and for each matched pair of edges. Setting every vertex-pair weight to one and edge-pair weights to zero gives the familiar largest-by-vertex-count objective. More general weights can favor certain correspondences and disfavor others. With negative weights, it is essential to distinguish a nonempty common tree from an empty answer of score zero. Those are different optimization conventions.

The most important structural observation comes when we temporarily fix roots. If a matched root on the left has children Alice, Bob and Carol, and a matched root on the right has children X and Y, every retained left child branch must map to a distinct retained right child branch. Alice cannot map to both X and Y, and X cannot simultaneously receive both Alice and Bob. The legal pairings are exactly a matching in a bipartite graph. Each potential pairing is weighted by the best solution already computed inside those two child subtrees, plus the weight of the matched connecting edges.

So the recursion has two layers. A tree problem asks for a matching problem; an edge of that matching problem represents another tree problem. The 2016 paper improves performance by exploiting how the matching instances are related across the tree's many possible root orientations. That reuse is a mathematical contribution in its own right. Proving the rooted recurrence is not the same as proving the optimized matching schedule and total running time.

## The third paper: replace common edges with paths

The 2018 paper by the same three authors studies largest-weight common subtree embeddings with distance penalties. A common tree is mapped into two input trees. A common edge may correspond to a path rather than a direct edge. The paths must fit together as a topological embedding: we cannot arbitrarily merge branching vertices or allow unrelated common edges to share interior vertices.

This becomes relevant when two structures contain the same branching architecture but differ in how many intermediate vertices lie along particular connections. A long chain can stand in for a short edge. Yet the paper allows the scoring rule to penalize the extra steps, so two possible embeddings are not automatically equally good.

The exact scoring rule is worth learning now because it is easy to implement incorrectly. If an edge of the common tree is represented by a single edge in each input, the two edge labels contribute their specified match weight. If either representing path is longer, the edge-label reward is not added; instead, the paths incur a penalty proportional to the total number of skipped interior vertices. The positive reward for a direct edge pair and the cost of path expansion are alternatives under this definition, not terms indiscriminately added together.

The dynamic program must therefore remember more than a single best score for each pair of vertices. It distinguishes a state where two current roots are matched from a state where at least one current vertex is skipped along a future path. That second state makes it possible to move downward while charging penalties correctly. The same bipartite matching idea returns when matched roots branch into independently paired child subproblems, but the candidate edge weights now depend on both mapped and skipped states.

The 2018 paper also treats unrooted trees. Its proof requires additional reasoning about where the highest retained vertices lie, how the two structural cases cover all feasible embeddings, and how rerooted matching instances can be reused without introducing circular dependencies. Some of that independent mathematics is already proved in the supplied Lean development; significant unrooted and runtime results remain obligations.

## Three different meanings of “correct”

Suppose we write a Rust program that returns a score and two lists of original vertices. We test it on hundreds of tree pairs. The scores agree with an exhaustive checker for small cases. We even translate a portion of its source into Lean. What exactly do we now know?

There are several separate questions. First, is our mathematical definition the right problem? For the 2018 paper, does it really implement the paper's direct-edge reward versus skipped-path penalty? For the 2004 paper, does the containment relation permit every edge contraction? No amount of program testing substitutes for getting the specification right.

Second, is every returned witness feasible? A claimed common object must use valid original vertices and edges, preserve the required structure, and have the reported score. Third, is the witness optimal? It is not enough that it is valid. For every other feasible witness, there must be a reason its score cannot be larger. Fourth, is the program we ship the program whose behavior has been proved? A correct mathematical recurrence does not prove the correctness of an optimized implementation with mutable tables, index conversions and numeric overflow possibilities. Fifth, is its advertised running time established under an explicit cost model? Counting recursive calls is not automatically counting hash comparisons, word copies, memory allocation or floating-point operations.

The common-subtree repository is interesting precisely because it contains work at all these levels. The ordered paper's central recurrence and decomposition mathematics have extensive machine-checked coverage. The 2016 rooted recurrence is proved against an independent optimization definition, while the most ambitious optimized complexity results remain open. The 2018 mapped-and-skipped rooted recurrence is proved, but the larger unrooted argument and efficient production refinement are less complete. There are also verified reference and exact-rational ordered paths with different contracts from the optimized floating-point implementation.

A responsible account of this project should not compress all that into a single green check mark. Its achievement is a collection of precise, separately supported statements, together with an equally precise list of what has not yet been shown.

## A map for the journey

Our first mathematical tools are elementary: rooted-tree structure, ordered versus unordered children, finite partial maps, induction on tree size, and optimization over a finite set of feasible witnesses. We will then add dynamic programming, balanced words, bipartite matching and their precise recurrence proofs. From there we can read the papers rather than merely hear their abstracts.

To understand the formalization, we will learn why Lean often begins with an independent inductive relation for valid objects, proves a finite optimum exists, and only later establishes the equivalence to a computational representation. We will distinguish mathematical witnesses from numerical scores and both from the executable Rust that must return real input identities. The eventual complexity lectures will ask what each bound counts and why a source-level bound may be harder than a combinatorial one.

This course has a practical destination. We want to be able to open a theorem in the repository and say, in ordinary mathematical language, exactly what it establishes; to read its hypotheses without accidentally assuming away the hard case; to trace it back to the relevant paper statement; and to decide which missing lemma would genuinely advance the verified algorithm. That skill begins by refusing to treat three different kinds of common subtree as the same object.

<!-- END SPOKEN LECTURE -->

## Non-spoken companion: comparison table

| Feature | Lozano–Valiente 2004 | Droschinsky et al. 2016 | Droschinsky et al. 2018 |
|---|---|---|---|
| Inputs | Rooted ordered trees | Unrooted unordered trees | Rooted/unrooted unordered trees, labels |
| Feasible transformation | Ordered edge contractions | Connected common subgraph isomorphism (strict adjacency) | Topological path embedding, internally disjoint mapped paths |
| Objective | Maximum number of retained edges | Sum of mapped vertex and edge weights | Vertex match weights plus direct-edge rewards or skipped-path penalties |
| Core DP mechanism | First-return balanced-word decomposition | Bipartite matching between child branches | Mapped/skipped states plus child matching |
| Major advanced proof issue | Containment specification, state counts and resource cost | Related matching instances, rerooting and runtime | Path score, unrooted structural split, rerooted schedule and runtime |

A strict connected tree isomorphism preserves mapped edges as mapped edges. An edge-contraction relation can merge a parent with a child and promote its children. A topological embedding replaces edges by internally disjoint paths. In particular, contracting a branching vertex need not be a topological embedding.

**Paper editions used:** 2004 original PDF; 2016 arXiv `1602.07210v4`; 2018 arXiv `1805.00821v1`. The project statement ledger is `docs/planning/paper_statement_crosswalk.md` in `networkx_algo_common_subtree`; status is a snapshot, not a live claim about future revisions.

**Read further:**

- [Lozano & Valiente, 2004, original manuscript](https://www.cs.upc.edu/~antoni/subtree.pdf)
- [Droschinsky, Kriege & Mutzel, 2016, pinned v4](https://arxiv.org/pdf/1602.07210v4)
- [Droschinsky, Kriege & Mutzel, 2018, pinned v1](https://arxiv.org/pdf/1805.00821v1)
- Existing course connections: `algorithms-computability-complexity:011000` (dynamic programming), `discrete-mathematics:005000` (matchings), and `logic-types:008000` (what a proof assistant checks).

## Questions to carry into a paper

1. Given a specific proposed common tree, what finite evidence would establish feasibility independently of the optimizer?
2. Does a proof concern the optimum **score**, a reconstructible witness, or an executed program?
3. When a paper states an asymptotic bound, which computational operations are being counted?
