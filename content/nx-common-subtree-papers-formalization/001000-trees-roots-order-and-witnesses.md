# 001000 — Trees, Roots, Order, and the Shape of a Witness

**Track:** NX Common Subtree Papers & Formalization. **Section:** Shared mathematics. **Background:** Graphs, finite sets, and elementary proof by induction. **Focus:** Root orientations, connectedness, ordered trees, certificates of feasibility, and why root choice enters the algorithms.

<!-- BEGIN SPOKEN LECTURE -->

# Trees, Roots, Order, and the Shape of a Witness

There is an attractive way to draw a tree: place a node at the top, draw lines downward, and let its branches spread across the page. That drawing suggests a root, a direction, perhaps even a left-to-right ordering. But a mathematical tree need not possess either of those extra structures. The picture is giving us convenient coordinates. The algorithm must know whether the coordinates belong to the input or were merely chosen to solve a problem.

This distinction becomes central when we compare trees. In a rooted tree, we know which way to recurse. In an unrooted tree, we must establish why a particular rooting can be used without losing the best solution. And for ordered trees, the left-to-right position of a branch is part of the answer, while for unordered trees it is irrelevant. The combinatorial language is simple enough to learn from a handful of examples, yet it carries much of the mathematical burden of the three papers.

## The unique path and all its consequences

A finite undirected graph has vertices and edges. We will work with simple graphs: no parallel edges and no loops. A path is a sequence of adjacent vertices with no repetition. A graph is connected if any two vertices can be joined by a path. A cycle starts and ends at the same vertex without repeating its other vertices.

A tree is a connected graph with no cycles. There are several equivalent formulations. If a finite graph has one unique simple path between every pair of vertices, it is a tree. If a connected finite graph has n vertices and n minus one edges, it is a tree. The edge count alone does not prove connectedness; a disconnected graph can have n minus one edges if it has a cycle somewhere else. In a proof, we retain the actual hypotheses rather than remembering only an attractive numerical slogan.

Why is the unique-path characterization so useful? Remove one edge from a tree. The graph splits into exactly two connected components. If an alternative route still linked the endpoints, the original edge plus that route would form a cycle. The same fact works backward: adding an edge between vertices already connected in a tree creates exactly one cycle. This is why each child branch of a rooted tree is naturally isolated by a single parent edge, and why its subtree can be solved independently once that edge's role is fixed.

For example, consider five vertices: a center R connected to A, B, and C, with C connected to D. There are four edges. The path from A to D is A, R, C, D, and it is the only such path. Cut the R-to-C edge. The C,D component separates completely from R,A,B. Every possible connection between these components in the original tree crossed that one edge.

A candidate common subtree must usually be connected. Suppose we select A and D but not R or C. The original induced graph on those selected vertices has no edge at all. We cannot claim to have selected a connected two-vertex subtree merely because a path existed between them before we deleted its interior. That path could become relevant in a topological embedding, where skipped interior vertices are represented explicitly, but it is not a strict subtree isomorphism. There is the first example of a property that a program's output validator needs to check under one contract but not another.

## Rooting is an orientation, not a new tree

Choose R as a root in our example. Then A, B, and C are children of R, and D is a child of C. Root the exact same undirected tree instead at D. Now C is a child of D, R is a child of C, and A and B are children of R. No undirected edge changed. What changed is which endpoint of each edge we call the parent.

A rooted subtree at a vertex u consists of u and all vertices whose route to the global root passes through u. Its size and shape depend on the global root, even though the ambient undirected tree is unchanged. A formula referring to “the subtree rooted at u” is therefore incomplete unless the ambient orientation is clear.

The 2016 and 2018 algorithms often represent a subtree by a directed-edge view. Imagine an undirected edge p–u. Remove it. Take the connected component containing u and regard u as its root. We can describe the view by saying “enter u from p.” For a fixed edge, the two directions give complementary views; a special whole-tree view is used when no parent edge is excluded. This language makes rerooting much more concrete than rebuilding every tree from scratch for every root.

There are only two orientations of each undirected edge, so there are linearly many directed-edge views in a tree, plus whole-tree roots as needed. That does not by itself prove an efficient algorithm. A view can have many children, and evaluating all pairs of views can generate expensive matching instances. But it explains how a huge-looking family of rootings can share its underlying combinatorial pieces.

## A connected selection has a highest vertex

Now fix an arbitrary root r of a tree T. Consider any nonempty connected selection of original vertices. Among those vertices there is exactly one with minimum distance from r. Call it the highest selected vertex.

Why must it be unique? Suppose two distinct selected vertices u and v had the same minimum depth. Their unique path in the tree passes through a lowest common ancestor at strictly smaller depth, unless one is an ancestor of the other; equal depth rules that out. Because our selected vertices induce a connected subtree, the path between u and v must lie inside the selection. Its shallower ancestor would therefore also be selected, contradicting minimality. So there can be only one highest selected vertex.

This modest lemma has considerable algorithmic force. If the best strict common subtree maps some selected vertex u in the left tree to some selected vertex v in the right tree, then, relative to a fixed root on the left, u is the unique highest selected left vertex. The selected left component lies entirely in the descendant subtree below u. The corresponding right object can be oriented to make v its appropriate root. The proof of a fixed-root reduction can then work with one family of left-root choices rather than treating all pairs of global roots as independent new problems.

Notice what we proved and what we did not. We did not prove that the optimum always includes the arbitrary root r. It need not. We proved that every nonempty connected candidate has a well-defined top relative to r, and that we can classify candidates by their tops. An optimization identity that takes a maximum over those cases requires a second argument: each candidate is accounted for, and each candidate produced by the algorithm is valid. This is exactly the two-direction style of proof we will see repeatedly.

There is a subtle boundary here. The highest-vertex lemma used connected selections in the original tree. For embeddings represented by internally disjoint paths, the image of the common tree may include skipped vertices along those paths, and the set of **mapped endpoints** alone may not be connected by original edges. We cannot automatically reuse every strict-subtree argument unchanged in the 2018 setting. The image paths and their internal vertices have to be included in the structure of the relevant proof.

## When order is mathematical data

In a rooted ordered tree, children of each node form a sequence. Consider a root with two subtrees: a leaf first and a two-edge chain second. Swap the positions of those children. As unordered rooted trees, the results are isomorphic. As ordered rooted trees, the isomorphism that simply swaps children is not permitted. An order-preserving map must send first surviving child to first surviving child, and similarly for all retained children.

Order has an immediate computational benefit. If we are comparing two ordered child lists, we can use sequence-style dynamic programming. We can decide whether to keep corresponding items or skip items while preserving relative positions. In an unordered tree, there is no first child with inherent significance. We must instead choose which child on one side pairs with which child on the other. That is a matching problem rather than a sequence-alignment problem.

The contrast persists even if our Python data structure happens to enumerate the neighbors of an unordered node in a stable order. An implementation may need such an enumeration to store arrays, but the result must be invariant under permutations that leave the abstract unordered tree unchanged. In a verified implementation, we may formalize the abstract optimum first and prove that the chosen indexing does not alter its value or validity.

Contraction adds a further detail for ordered trees. Suppose a parent has children A, B, C, in that order, and B has children X and Y. Contracting the edge from the parent to B does not simply delete B and everything below it. It replaces B at its position by X and Y, giving A, X, Y, C. The relative positions preserve the ordering. Delete B in the sense of deleting its entire rooted subtree, and we instead get A, C. These are different transformations and need different mathematical relations.

## The certificate comes before the optimizer

What should an independent definition of a valid common structure look like? Consider strict weighted subtree isomorphism. We might select a nonempty connected set of vertices on each side and give a bijection between them. The bijection must preserve adjacency in both directions. In trees, requiring selected edges to be present and the selected subgraphs to be connected rules out various invalid maps. The score is the sum of weights for matched vertices and corresponding edges.

For a topological embedding, this certificate is insufficient. We also need the paths that realize the edges of the common tree in each input, and conditions that their interiors do not overlap improperly. For an ordered contraction, an operational certificate could be a finite sequence of edge contractions, or a relation proved equivalent to all such sequences. For the ordered balanced-word representation, we can store surviving original pair positions and check that deleting the other complete pairs produces the claimed output.

This is why the common-subtree repository separates specification from implementation. In the 2004 branch, independent ordered-tree contractions are defined before the balanced-sequence algorithm is certified. In the 2016 branch, valid connected isomorphisms and their scores are defined separately from the matching table. In the 2018 branch, paths, common skeletons, mapped vertices and their score are treated as mathematical objects rather than as accidental properties of an array layout.

A proof assistant does not choose the right definition for us. It can check that our algorithm satisfies the definition we give it. If the definition omits the preservation of order, the machine may happily prove a theorem about a broader class of matches than the one we meant. The original problem is an intellectual commitment made before proof checking begins.

## Feasibility, existence, and maximum

Every finite pair of input trees has only finitely many possible vertex subsets, bijections and paths. So the set of feasible scores is finite once the witness definition and scores are fixed. If at least one candidate exists and the weights live in an ordered domain where finite maxima exist, an optimum exists. That is the first easy mathematical theorem we should expect to prove.

But nonemptiness is a genuine hypothesis. With arbitrary negative weights, an empty common tree of score zero could beat every nonempty candidate. A library might choose to allow empty output for convenience, while a paper's mathematical specification excludes it. These conventions are related by explicit cases, not by pretending they are the same optimum.

To prove an algorithm returns a maximum, it is useful to separate two obligations. Soundness: the algorithm's output describes a feasible candidate with the reported score. Completeness or optimality: no feasible candidate has a greater score. An exhaustive reference algorithm can search all finite witnesses and select a maximum; it gives a mathematically simple specification even when it is impractically slow. A fast dynamic program can then be proved equal to the reference optimum without using its own implementation as the definition of correctness.

This is not extra bureaucracy. It is how we find out whether a shortcut threw away a legal candidate. The finite witness set also lets us build tiny independent oracles for testing: enumerate all legal mappings for small trees, score them separately, and compare the result with the optimized implementation. The oracle and the proof play different roles. The oracle catches mistakes on a finite set of cases; the proof explains why every case is covered.

## The invariant beneath the picture

We began with a drawing of a tree, then removed the root and the left-to-right arrangement that the drawing seemed to provide. We added them back deliberately, one at a time, with precise meanings. We also learned to read “subtree” as a question: strict selected edges, contracted edges, or realized paths? And we saw why every proposed optimum should come with an independently meaningful witness.

When we encounter a complicated Lean theorem, we can now ask what its quantifiers range over. Is it every finite tree? Every rooted orientation? Every nonempty connected selection? Every order-preserving contraction? Every valid topological path family? A long proof can be technically impressive and still be about the wrong domain if one of those qualifiers has been lost.

Our first useful habit is therefore not to memorize a recurrence. It is to name the object whose optimum the recurrence is supposed to compute. The recurrence comes next, after the possible solutions have a clear mathematical shape.

<!-- END SPOKEN LECTURE -->

## Exact companion

### Tree identities

For a finite simple undirected graph `T`, the following are equivalent when `T` is nonempty:

1. `T` is connected and acyclic.
2. There is exactly one simple path between any two vertices.
3. `T` is connected and `|E(T)| = |V(T)| - 1`.

For rooted orientation `r`, define `parent_r(u)` as the neighbor of `u` on the unique route to `r` for `u != r`. For an oriented edge `p → u`, the directed-edge view `T[p | u]` is the component containing `u` in `T - {p,u}`, rooted at `u`.

### Highest-vertex lemma (strict connected selection)

Let `S` be a nonempty vertex subset such that the induced subgraph `T[S]` is connected. Fix any root `r` and let `depth_r(v)` be distance from `r`. Then there is a **unique** `u ∈ S` minimizing `depth_r`. All of `S` belongs to the descendant component rooted at `u`.

*Proof outline.* Two distinct minimal-depth vertices would have a common ancestor strictly closer to `r`, which must lie on their unique connecting path in `T[S]`, contradicting minimality. For every `v ∈ S`, its path to `u` lies in `S`, and the unique minimum-depth condition makes `u` an ancestor of `v`.

### Independent witness models

- **Strict isomorphism:** nonempty selected connected vertex subsets `S ⊆ V(G)`, `R ⊆ V(H)`, bijection `f : S ≃ R`, adjacency in both directions, a score on all mapped vertices and corresponding edges.
- **Ordered contraction:** existence of a finite sequence of valid parent-child edge contractions respecting ordered child-forest splicing.
- **Topological embedding:** common finite tree `C`, vertex injections `f : V(C) ↪ V(G)`, `g : V(C) ↪ V(H)`, a path for every common edge in each input, plus disjointness and incidence restrictions on path interiors.

### Relevant Lean source landmarks

- `proofs/SubtreeProofs/Paper2004/OrderedTree.lean`
- `proofs/SubtreeProofs/Paper2004/OrderedForest.lean`
- `proofs/SubtreeProofs/Droschinsky2016/Specification.lean`
- `proofs/SubtreeProofs/Droschinsky2016/OrientedRecurrence.lean`
- `proofs/SubtreeProofs/Droschinsky2018/Specification.lean`
- `proofs/SubtreeProofs/Droschinsky2018/Witness.lean`

All paths refer to the uploaded `networkx_algo_common_subtree` repository, not to the lecture repository.

### Further reading

- Droschinsky et al. 2016, Sections 2–3 and Lemma 2 (rooted formulation and root reduction): https://arxiv.org/pdf/1602.07210v4
- Droschinsky et al. 2018, Sections 2–3, Definitions 1–2 (topological embeddings): https://arxiv.org/pdf/1805.00821v1
- Lozano & Valiente 2004, Sections 1–3 (ordered contractions): https://www.cs.upc.edu/~antoni/subtree.pdf
- Existing preparation: `mathematical-proof:009000` for sets, functions and induction; `algorithms-computability-complexity:013000` for graph traversal arguments.
