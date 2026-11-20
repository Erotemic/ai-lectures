# When an Edge Becomes a Path: The Common Tree in Droschinsky 2018

<!-- BEGIN SPOKEN LECTURE -->

Imagine comparing two trees that describe nearly the same branching structure. In one tree, a parent connects directly to a child. In the other, the corresponding parent reaches the corresponding child through an extra intermediate vertex. If we demand a literal graph isomorphism, the two shapes do not agree at that edge. If we allow an edge to stand for a path, they may express the same branching relationship.

That one relaxation changes the mathematics of the common-subtree problem. It also changes what a proof must establish. A pair of vertex mappings is no longer enough merely because the mapped vertices have compatible labels, or because their relative depths look plausible. The paths joining them have to fit together into a coherent tree. In particular, two different branches cannot secretly travel along the same stretch of a target tree and then split later.

This is the starting point of Droschinsky, Kriege, and Mutzel's 2018 paper, *Largest Weight Common Subtree Embeddings with Distance Penalties*. The 2016 paper studied weighted connected subtree isomorphism: the vertices selected in each tree must make isomorphic connected induced subgraphs, and an abstract edge is represented by an actual edge on each side. The 2018 paper allows a common abstract edge to stretch across several physical edges in either input tree. Its target is a weighted *common topological embedding*.

There are three objects to keep separate. There is the first input tree, there is the second input tree, and there is the smaller common tree that can be embedded into both. Many arguments become easier once the common tree is treated as an independent mathematical object rather than as an informal picture of highlighted vertices.

## A small tree hiding in a larger one

Start with the smallest interesting example. The abstract common tree has a root and two children. Call them Alice, Bob, and Carol, with Alice the parent of Bob and Carol. It has three vertices and two edges. Its branching happens at Alice.

The first input tree has Alice's image at a vertex we will call capital A. Capital A has one child, x, which in turn has a child, capital B. Capital A also has a direct child, capital C. The physical paths from A to B and from A to C have lengths two and one, respectively.

The second input tree has a vertex lower-case a with a direct child, lower-case b, and another child, y, which has a child, lower-case c. The paths from a to b and a to c have lengths one and two.

Map abstract Alice to capital A and lower-case a. Map abstract Bob to capital B and lower-case b. Map abstract Carol to capital C and lower-case c. Every abstract edge is realized by a path in each input. The two paths leaving A intersect only at A. The two paths leaving a intersect only at a. There is no mapped vertex hidden in the interior of another abstract edge's path.

So the two larger trees admit the same three-vertex common tree even though the path lengths differ. The intermediate vertices x and y are not images of vertices in the common tree. They exist to carry the paths. When we later introduce distance penalties, these are precisely the kinds of vertices that will be charged for a long realized edge.

Now keep the same two input trees but change the correspondence of the abstract children. Let Bob's image in the first tree be B and his image in the second be c; let Carol map to C in the first and b in the second. The abstract tree is unchanged. Its first branch uses two physical edges on each side; its second branch uses one edge on each side. This is also a valid topological embedding. The two assignments of mapped vertices will receive different weights once labels and penalties enter the problem.

We have already learned a useful lesson. A common embedding is a structured *choice* of which input vertices represent the abstract vertices. The input trees do not themselves dictate a unique correspondence, nor a unique number of skipped vertices.

## The two conditions in Definition 1

The 2018 paper begins with a rooted version of topological embedding, expressed through a function from the vertices of a smaller rooted tree into those of a larger rooted tree. The function is injective. Distinct abstract vertices receive distinct physical images.

Injectivity alone would be trivial to satisfy on large enough trees, so Definition 1 imposes two geometric conditions.

The first says that if Bob is a child of Alice in the common tree, then Bob's image must be a descendant of Alice's image in the target. It need not be an immediate child. A direct abstract edge may become a path with one, two, or many physical edges. The image of a parent stays above the image of its child. This is the ancestry condition.

The second says that two different children of the same abstract parent must head down different branches. The path from the parent's image to one child's image and the path from the parent's image to the other child's image may intersect at the parent's image, but nowhere else. This is the branch-separation condition.

It is worth spending time on why the second condition is necessary. Suppose the target tree has a vertex r, a single child x, and then two leaves b and c descending from x. Could we embed the three-vertex fork of Alice, Bob, and Carol by sending Alice to r, Bob to b, and Carol to c? The parent-child ancestry rule holds. Bob and Carol are both descendants of r. Injectivity holds too.

But both realized branches begin by traveling from r to x. They share the edge from r to x, and then they split at x. The fork in the abstract tree would have its branching at Alice, while the physical target has that branching at x. The images fail Definition 1's second condition. We cannot simply skip x while pretending the two branches depart independently at r.

We have choices. We could map Alice to x instead, if the other embedding permits it. Or we could choose a smaller common tree with a single branch rather than a fork. What we cannot do is keep the three-vertex fork while using a shared hidden segment for both of its edges.

This restriction is deeper than a convention about drawing. It ensures that the embedded tree retains its branching structure. Edge subdivision is allowed; relocating an abstract branching point into the unselected interior of a shared path is not.

## What does it mean to be common?

A topological embedding describes how one smaller tree appears in one larger tree. To compare two input trees, the paper takes a single common tree S and two embeddings: one from S into the first input tree, and another from S into the second.

We can pair up the two physical images of each abstract vertex. If an abstract vertex maps to u in the first input and v in the second, record the pair u and v. Because both embeddings are injective, this collection of pairs is a partial bijection: no selected vertex on either side can appear in two different pairs.

The paper calls the induced correspondence a common subtree embedding. Conceptually, the common tree witnesses why those pairs fit together. The same abstract edge has one realized path in the first input and another in the second. The same abstract fork has separated branches in both.

There is a tempting but incorrect shortcut here. We might take an arbitrary partial bijection between two vertex sets, connect every pair of selected vertices whose physical path has no other selected vertex inside, and assume we have obtained a common tree. That procedure sometimes works, but it can also invent extra edges or conceal an invalid branch point.

Return to the target with r, x, b, and c, where r is above x and x branches to the two leaves. Select r, b, and c, but leave x unselected. The unique path between r and b contains no *selected* vertex in its interior. The same is true of r and c. Even the path from b to c has no selected vertex in its interior. Connecting every such pair creates a triangle: r to b, r to c, and b to c.

A triangle is not a tree. And the three candidate physical paths share x, an interior vertex. Both failures point to the same problem: the selected set omitted an essential branching vertex. Merely selecting vertices and connecting consecutive selected endpoints is not a sufficient definition of a topological tree embedding.

The independent Lean specification pays attention to exactly this issue. It defines a relation called `BranchAdjacent` between two selected vertices when no other selected vertex lies inside their unique path. From these adjacencies it constructs a candidate `skeleton`. Then it *requires* the skeleton to be a tree and separately requires the interiors of distinct skeleton-edge paths to be disjoint. A valid common witness must satisfy both conditions on both input trees, along with partial bijectivity and correspondence of skeleton adjacency.

The additional requirements are not ornamental proof bureaucracy. They prevent the kind of false triangle or shared-stem realization we just constructed. They make the finite pair set describe a genuine common topological tree, not merely a collection of independently plausible endpoints.

## Roots are geometry, not necessarily selected endpoints

The rooted terminology deserves care because the papers compare several closely related problems.

A rooted topological embedding preserves the descendant direction. But that alone does not require the root of the common tree to map to the root of the ambient input. Its image could be deeper in the tree. A *root-to-root* embedding imposes the extra equality between those roots.

The distinction is visible in our example. If the first input tree had an extra vertex Z above A, an embedding of the three-vertex common fork could still begin at A. Under the rooted ancestry rules, A is a perfectly good place for the image of the common root. But it would not be root-to-root relative to the ambient input root Z.

We must also distinguish root choice from underlying unrooted geometry. The original first input tree has a unique physical path between any two vertices whether or not we pick a root. Rooting it allows us to speak about descendants, children, and the highest selected vertex. These are essential to the dynamic program, but they are not additional physical edges.

In the 2018 paper, the rooted algorithm can use an orientation to enumerate subproblems. The later unrooted algorithm has to account for common embeddings whose important junctions lie in different places relative to an arbitrary chosen orientation. Its structural lemmas are therefore more involved than the fixed-root argument from the 2016 isomorphism paper.

For now, the essential boundary is simple: a proof about a root-to-root subproblem is not automatically a proof about the unrestricted maximum. One needs an argument explaining how the subproblem results cover every feasible common tree.

## Two directions of the Lean representation proof

The repository supplies an independent formalization of this geometry rather than simply taking the dynamic program's output as a definition of a valid embedding.

Begin in `Droschinsky2018/Specification.lean`. Its `Valid` predicate describes nonempty finite pairs. It requires a partial bijection, tree-shaped skeletons on each side, internal path disjointness, and agreement of the skeleton adjacency relation. At this layer, there is no table lookup, matching algorithm, or notion of an optimal subproblem. A valid witness is just a mathematical object meeting those conditions.

Then visit `Shared/TopologicalEmbedding.lean`. Its `TopologicalEmbedding` structure describes a genuine abstract common tree mapped into a physical tree. It records the vertex map, injectivity, avoidance of mapped vertices inside realized edges, and disjoint interiors of different realized edges. The rooted variants add ancestry and root conditions.

These are two ways to represent the same intended geometry. One starts from pairs of selected physical vertices. The other starts from an abstract common tree and explicit maps into both inputs. Because both representations are useful, the formalization needs a correspondence theorem.

In one direction, start with a valid pair set. The left skeleton supplies a candidate abstract common tree. The pairing gives an isomorphism between the left and right skeletons. The inclusion of each skeleton into its ambient tree becomes a topological embedding because the interior-disjointness requirements were already proved. That construction appears in `Droschinsky2018/Witness.lean`: `Valid.commonTree`, `Valid.leftEmbedding`, `Valid.rightEmbedding`, and `Valid.embedding_pairs` record the concrete tree and recover the original pair set exactly.

In the opposite direction, suppose we are given a common tree and two valid topological embeddings. Pair the two physical images of each abstract vertex. The proof must show the resulting pair set is nonempty, partially bijective, has tree-shaped skeletons, and respects every path separation. It cannot quietly assume that these properties hold just because the maps were called embeddings; the requirements must be propagated through the unique paths in each target tree.

In `Droschinsky2018/Reconstruction.lean`, the theorem `valid_iff_source_embeddings` closes the equivalence with explicit common-tree realizations. The rooted analogues, including the root-to-root restrictions, appear in `Droschinsky2018/Rooted.lean`. There are also score-preservation results so that changing representation does not change the value eventually optimized. Those are separate theorems from geometric validity.

This two-direction proof is especially valuable in a formally verified algorithm. If we only proved that a reconstructed output was a valid common embedding, we could still have a dynamic program that overlooked better embeddings. To prove optimality, we must also be able to take *any* valid common embedding and bring it into the representation used by the recurrence. That is where the converse direction earns its place.

## A common tree is not the set of all convenient vertices

There is another point that becomes important when weights are introduced. The common tree is allowed to omit input vertices that are not needed for the selected branching structure. But the way an omitted vertex is used determines its role.

Some unselected input vertices lie on the unique path between two consecutive selected endpoints. Those are the skipped internal vertices of a realized abstract edge. Other unselected vertices lie in entire branches that the embedding does not use at all. Those are simply outside the witness. They are not intermediate vertices of any realized common edge.

In our example, x is an internal vertex of the A-to-B realized path, so it is a skipped vertex if the common tree uses that edge. If we abandon the B branch completely and keep only the A-to-C edge, x is no longer on a realized path. It does not become a penalty merely because it exists in the input tree.

That distinction prevents a misleading interpretation of the distance penalty introduced in Definition 4. We are not charged for the number of vertices deleted from an input. We are charged for interior vertices that the chosen common edges actually traverse. The choice of common tree, the choice of its physical endpoints, and the choice of which branches survive therefore interact with the score.

This is why a topological embedding problem is more subtle than an ordinary tree edit or pruning problem. The same physical vertex may be absent from one witness because its whole branch was discarded, and absent from another because it lies on the path joining mapped endpoints. The second absence incurs a cost; the first does not.

## The first formal milestone

At the end of this geometric development, there is an independent, finite family of common-tree witnesses. The repository proves that there is at least one: we can choose one vertex from each nonempty input tree and map a one-vertex common tree to those two vertices. There are no abstract edges to realize, so all path conditions are vacuous.

Because the inputs are finite, there are finitely many possible pair relations. Once their scores are defined, the set of valid witnesses has an attained maximum. The existence proof does not use the dynamic-programming recurrence. The recurrence must later prove that it computes this independently specified maximum.

We are now ready to add the weight model. We know exactly which vertices are mapped and which pairs of physical paths represent the common edges. We have seen why the paths cannot collide in their interiors, why a hidden branch point cannot be waved away, and why the notion of a selected common tree is more than a collection of plausible node correspondences.

Those structural facts are the foundation for the 2018 algorithm. Without them, a numerical recurrence could be beautifully optimized and still solve the wrong problem.

<!-- END SPOKEN LECTURE -->

## Mathematical companion: Definition 1 and independent witnesses

Let the common tree be \(S\). A rooted topological embedding \(\psi:S\to T\) is injective and, for every abstract parent \(a\) and its children \(b,c\) with \(b\ne c\), satisfies:

\[
\psi(b)\text{ is a descendant of }\psi(a),\qquad
P_T(\psi(a),\psi(b))\cap P_T(\psi(a),\psi(c))=\{\psi(a)\}.
\]

A root-to-root embedding adds \(\psi(r(S))=r(T)\). Two embeddings \(\psi:S\to T\) and \(\psi':S\to T'\) induce a finite partial bijection \(\varphi=\psi'\circ\psi^{-1}\) on their selected images. The independent Lean witness stores this relation as a finite set of pairs \(P\subseteq V(T)\times V(T')\), not a total map from every input vertex.

For a selected set \(X\subseteq V(T)\), define candidate adjacency:

\[
a\sim_X b\quad\Longleftrightarrow\quad a\ne b\text{ and }P_T(a,b)^{\circ}\cap X=\varnothing.
\]

The independent `Valid` contract additionally requires this skeleton to be a tree and distinct skeleton edges to have disjoint path interiors in *each* ambient tree. For the counterexample \(r-x-\{b,c\}\) with \(X=\{r,b,c\}\), all three pairs of distinct selected vertices have no selected interior vertex; the candidate skeleton is a triangle, and its realized paths share \(x\). Thus it is **not** a valid three-vertex fork embedding with the root at \(r\).

### Example data

- Left tree \(T\): edges \(A-x\), \(x-B\), \(A-C\).
- Right tree \(T'\): edges \(a-b\), \(a-y\), \(y-c\).
- First common correspondence: \((A,a),(B,b),(C,c)\). Abstract edge lengths \((2,1)\) and \((1,2)\).
- Second common correspondence: \((A,a),(B,c),(C,b)\). Abstract edge lengths \((2,2)\) and \((1,1)\).
- Both use the same abstract fork at the mapped pair \((A,a)\). The intermediate vertices \(x,y\) occur in realized edges, not as abstract nodes.

### Proof reading route (supplied 2026-11-19 source snapshot)

1. `proofs/SubtreeProofs/Droschinsky2018/Specification.lean`: `BranchAdjacent`, `skeleton`, `InteriorDisjoint`, `Valid`, `singleton_valid`.
2. `proofs/SubtreeProofs/Shared/TopologicalEmbedding.lean`: `TopologicalEmbedding` and rooted variants, path-intersection and path-lifting lemmas.
3. `proofs/SubtreeProofs/Droschinsky2018/Witness.lean`: `Valid.commonTree`, `Valid.leftEmbedding`, `Valid.rightEmbedding`, `Valid.embedding_pairs`, `Valid.rooted_realizations`.
4. `proofs/SubtreeProofs/Droschinsky2018/Reconstruction.lean`: `valid_iff_source_embeddings`; this is the converse bridge as well as the source-realization direction.
5. `proofs/SubtreeProofs/Droschinsky2018/Rooted.lean`: `rootedValid_iff_source_embeddings`, `rootToRootValid_iff_source_embeddings`.

**Primary reading:** Droschinsky, Kriege, Mutzel, *Largest Weight Common Subtree Embeddings with Distance Penalties*, [arXiv:1805.00821v1](https://arxiv.org/pdf/1805.00821v1), Definitions 1–2, Section 3; [MFCS 2018](https://doi.org/10.4230/LIPIcs.MFCS.2018.54). These are independent specification and representation results, not claims about optimized Rust, floating arithmetic, or a proved runtime.

### Listening checks

1. Why do injectivity and descendant preservation not suffice for a topological embedding of a fork?
2. Why does selecting three vertices \(r,b,c\) but not their branching junction \(x\) produce a candidate triangle in the skeleton representation?
3. What is the difference between an internal vertex of a realized edge and an unused vertex in a discarded branch?
4. Which direction of the source/pair correspondence is needed to prove that a recurrence loses no optimal witnesses?
