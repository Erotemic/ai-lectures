# 015000 — Mayer–Vietoris and Excision: Computing Homology by Gluing

**Track:** Topology and Geometry. **Background:** singular homology, exact sequences, open covers, chain complexes. **Central question:** if a space is assembled from two simpler pieces, how does their overlap determine its holes?

<!-- BEGIN SPOKEN LECTURE -->

# Mayer–Vietoris and Excision: Computing Homology by Gluing

Imagine trying to understand the topology of a sphere without calculating homology from the definition of singular chains. Cover it with two open regions, each slightly larger than a hemisphere. Each region is contractible, so its higher homology is trivial. The overlap is a band around the equator, homotopy equivalent to a circle. Somehow the homology of the sphere is hiding inside that overlap.

The Mayer–Vietoris sequence makes this intuition exact. It says that the homology of a union is related to the homology of its parts and their intersection by a long exact sequence. The word exact is doing real mathematical work: it tells us precisely which classes disappear, which survive, and which arise from gluing.

## A homology class can come from two sides

Let X be the union of open subspaces U and V. A cycle lying in U can be regarded as a cycle in X, and similarly for V. So there is a map from the direct sum of the homology groups of U and V into the homology of X.

But overlap creates redundancy. A cycle in U intersect V can be regarded as coming from either side. To account for that double counting, an earlier map sends a class in the intersection to its images in U and V, with opposite signs.

The Mayer–Vietoris sequence places these maps into a chain of groups connected by homomorphisms. For degree n, it runs from the n-th homology of the intersection to the direct sum of the n-th homologies of the parts, then to the n-th homology of the union, then back to the homology of the intersection one degree lower.

At each stop, the image of the preceding map equals the kernel of the next. This is what exactness means. The connecting map from a cycle in X to a class one degree lower in the overlap is especially important. It measures how pieces of a global cycle fail to be cycles separately when cut along their common region.

## A circle from two overlapping arcs

Cover a circle with two open arcs, each contractible, arranged so their intersection consists of two disjoint arcs. The intersection has two connected components. Each of U and V has one connected component.

Since the pieces and overlap have no positive-degree homology, the relevant portion of the long exact sequence says the first homology of the circle is the kernel of a map between zero-dimensional homology groups. The intersection contributes two integer generators, one for each component. Each of U and V contributes one.

The map sends a pair of integers from the two overlap components to their sum in U, and to its negative in V. Its kernel consists of pairs that sum to zero. That kernel is a copy of the integers. So we recover the first homology of the circle, entirely from information about connected components.

This example explains why Mayer–Vietoris is not just a formula for adding homology groups. The topology of the overlap and the signs in the maps matter. A circle's loop is visible as a disagreement between the two places where its arcs overlap.

## A sphere from two disks

Now return to the sphere. Cover it by U and V, two open sets each homotopy equivalent to a disk. Their intersection retracts to a circle. In degree two, the Mayer–Vietoris sequence reduces to a map from the second homology of the sphere into the first homology of the overlap.

The two disk-like regions have no second or first homology. Exactness forces that connecting map to be an isomorphism. Consequently the second homology of the sphere is the first homology of the circle: one copy of the integers.

We have turned a two-dimensional hole into a one-dimensional loop in the equatorial overlap. The dimension shift is not an accident. The connecting homomorphism detects the boundary created when a global cycle is split across the cover.

The same idea works for higher-dimensional spheres. Two overlapping contractible hemispherical regions have intersection homotopy equivalent to the sphere one dimension lower. An inductive Mayer–Vietoris calculation shows the top reduced homology of an n-sphere is the integers.

## Where the exact sequence comes from

The mechanism is chain-level bookkeeping. Singular chains supported in U or V form subcomplexes of chains in X. Their intersection is the chains supported in U intersect V. Adding the two subcomplexes produces a chain complex whose homology agrees with that of X, because singular simplices can be subdivided enough to lie in a member of the open cover.

This yields a short exact sequence of chain complexes. The resulting long exact sequence in homology is precisely Mayer–Vietoris. The connecting map can be constructed by lifting a global cycle to the sum of chains on the two sides, taking its boundary, and observing that the two boundaries cancel outside the overlap.

The proof explains both the sign convention and why the cover needs appropriate hypotheses. For an open cover, subdivision supplies the needed chain equivalence. For arbitrary subsets, one cannot apply the same statement without checking an excisive-cover condition.

## Excision: discard what does not matter

Excision is a related theorem with a different flavor. Suppose Z lies inside A and the closure of Z lies in the interior of A. Then removing Z from both X and A leaves the relative homology of the pair unchanged. The part removed was sufficiently deep inside the subspace A that it carried no new relative information.

Relative homology tracks cycles in X while treating chains inside A as negligible. Excision tells us we may often replace a large global pair with a small neighborhood of the feature we care about.

For example, local homology near a point of an n-dimensional manifold can be computed by replacing the manifold with a small coordinate ball and then using a ball relative to its punctured version. This ultimately records the dimension and local orientation behavior of the manifold. That is a different kind of locality from Mayer–Vietoris, but both depend on the fact that singular chains can be subdivided.

## The meaning of a gluing theorem

The advantage of exact sequences is compositionality. A complicated space can be decomposed into pieces, while the overlap carries the instructions for putting the homology back together. But a long exact sequence does not always determine every group without further information: we may need to calculate the maps, not just the ranks of the groups.

Mayer–Vietoris and excision are foundational because they make global topology computable from local data. Their ideas also reappear in sheaf theory, derived categories, and the geometry of manifolds. Gluing is not merely a picture. It is an algebraic process with kernels, images, connecting maps, and hypotheses that tell us when the process is valid.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For an excisive cover \(X=U\cup V\) (in particular, for an open cover), the Mayer–Vietoris long exact sequence in singular homology has terms
\[\cdots\to H_n(U\cap V)\xrightarrow{(i_*,-j_*)}H_n(U)\oplus H_n(V)\xrightarrow{k_*+\ell_*}H_n(X)\xrightarrow{\partial}H_{n-1}(U\cap V)\to\cdots.\]

**Circle:** choose contractible arcs \(U,V\subset S^1\) with \(U\cap V=A\sqcup B\), two contractible components. Then \(H_1(S^1)\cong\ker(\mathbb Z^2\to\mathbb Z^2)\), where \((a,b)\mapsto(a+b,-a-b)\), hence \(H_1(S^1)\cong\mathbb Z\).

**Sphere:** choose contractible hemispherical neighborhoods \(U,V\subset S^2\) with \(U\cap V\simeq S^1\). Exactness gives \(H_2(S^2)\cong H_1(S^1)\cong\mathbb Z\).

**Excision:** if \(Z\subset A\subset X\) with \(\overline Z\subset\operatorname{int}_X A\), the inclusion \((X\setminus Z,A\setminus Z)\hookrightarrow(X,A)\) induces isomorphisms on all singular homology groups. More general excisive conditions exist.

### Exercises with answers

1. Why is the overlap of two arcs on a circle allowed to have two components? **Answer:** each arc covers almost all the circle but omits a different small closed interval; their shared region can split into two disjoint arcs.
2. Can we determine \(H_1(S^1)\) using only the number of components of \(U,V,U\cap V\)? **Here yes:** exactness and vanishing higher homology give the kernel \(\mathbb Z\).
3. For a sphere covered by two contractible open sets with annular overlap, what gives the top homology? **Answer:** the connecting homomorphism \(H_2(S^2)\to H_1(S^1)\) is an isomorphism.
4. What goes wrong if we remove a set without excision hypotheses? **Answer:** relative cycles near the removed boundary may change; excision does not apply automatically to arbitrary pairs.

### Reading and source notes

- Allen Hatcher, [*Algebraic Topology*](https://pi.math.cornell.edu/~hatcher/AT/ATpage.html), Section 2.2 (Mayer–Vietoris) and Section 2.1 (excision).
- [MIT 18.905 Algebraic Topology I](https://ocw.mit.edu/courses/18-905-algebraic-topology-i-fall-2016/), long exact sequences and computations by open covers.
