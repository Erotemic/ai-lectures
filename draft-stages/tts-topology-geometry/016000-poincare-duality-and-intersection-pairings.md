# 016000 — Poincaré Duality: Why a Manifold's Dimensions Pair Up

**Track:** Topology and Geometry. **Background:** homology, cohomology, cup products, orientation, manifolds. **Central question:** why should cohomology in one degree know about homology in the complementary degree?

<!-- BEGIN SPOKEN LECTURE -->

# Poincaré Duality: Why a Manifold's Dimensions Pair Up

A sphere has a zero-dimensional homology class representing its one connected component and a two-dimensional class representing the entire oriented surface. The group in degree one vanishes. A torus has the same groups at the extremes, but two independent one-dimensional cycles wind around its two directions.

These patterns are not independent. On a closed, connected, oriented manifold of dimension n, the cohomology in degree k is naturally related to the homology in degree n minus k. This is Poincaré duality. It is among the strongest reasons that manifolds are more than arbitrary topological spaces.

## Orientation creates a global class

A manifold looks locally like Euclidean space. If we can choose orientations consistently from one coordinate neighborhood to the next, it is orientable. If it is also compact and has no boundary, it possesses a fundamental homology class in its top dimension, once an orientation has been chosen.

For a connected n-dimensional manifold, this class expresses the manifold itself as an oriented cycle. It is not the same as a physical boundary: the manifold has none. Algebraically, the local orientations join into a global top-dimensional homology class.

The fundamental class is the ingredient that turns cohomology into homology. Cohomology classes can be thought of as rules for evaluating, measuring, or detecting cycles. The cap product lets a cohomology class act on a homology class and lower its dimension.

Apply a degree-k cohomology class to the degree-n fundamental class. The result is a homology class in degree n minus k. Poincaré duality says this map is an isomorphism, not merely a useful construction.

## A torus makes the pairing visible

Consider a torus, the surface of a doughnut. It has two independent one-dimensional loops: one goes around the hole, and the other goes around the tube. Call their homology classes a and b. They cannot be continuously deformed into one another, and together they generate the first homology group, a copy of the integers squared.

Now consider the corresponding degree-one cohomology classes. They can evaluate on oriented loops, counting winding in one direction or the other. Their cup product is a degree-two cohomology class. When evaluated on the fundamental class of the torus, the product of the two basic degree-one classes gives plus one for a consistent choice of orientation.

Reverse their order, and the cup product changes sign, because degree-one cohomology products anticommute. The resulting alternating form records the oriented intersection of the two types of loops. This is not just a count of holes; it remembers how different cycles meet.

On a closed oriented surface of genus g, the first homology has rank two g. One can choose g pairs of basic cycles whose intersection form is the standard alternating pairing. The fact that the rank is even is a geometric constraint visible in the algebra.

## Duality beyond a surface

In dimension three, Poincaré duality pairs degree-one cohomology with degree-two homology. An oriented surface inside a three-manifold can represent a degree-two homology class, while a degree-one cohomology class may detect how loops cross such surfaces. The pairing is the higher-dimensional analogue of winding and intersection on a torus.

In even dimensions, complementary middle-dimensional cycles can intersect in isolated points. Their signed intersections define a bilinear pairing. For a closed oriented four-manifold, for example, the intersection form on its second homology modulo torsion can carry deep information about the manifold's topology.

Duality is not claiming all homology groups in complementary degrees are literally the same. It relates cohomology to homology. If we work over a field, finite-dimensional vector-space duality can turn this into a symmetry of Betti numbers. Over the integers, torsion makes the relationship more subtle, and universal coefficient theorems must be handled explicitly.

## The proof idea is local-to-global

Why should one global fundamental class produce an isomorphism everywhere? At a point of an oriented manifold, the local relative homology in degree n is a copy of the integers. This is the infinitesimal version of a fundamental class.

To pass from local to global, one proves that the cap-product construction behaves naturally under suitable restrictions and open covers. The Mayer–Vietoris sequences on the cohomology side and homology side form a compatible diagram. On small neighborhoods, where the topology is that of a ball, the desired map is readily checked. Exactness and diagram-chasing then let the result propagate through a cover.

This is a broad proof strategy in topology: prove a local claim on simple neighborhoods, show the construction respects gluing, and obtain the global theorem. The gluing algebra from Mayer–Vietoris is not incidental. It is part of why Poincaré duality exists.

## What changes at a boundary or without orientation

The familiar theorem has hypotheses. For a compact oriented manifold with boundary, the fundamental class naturally lives in relative homology, not the absolute top homology. The appropriate version is Poincaré–Lefschetz duality, pairing absolute cohomology with relative homology, and vice versa.

Take a disk. Its ordinary second homology is zero: the disk can contract, and its boundary prevents it from being an absolute two-cycle. But its relative second homology, measured modulo the boundary circle, is the integers. The relative class is precisely what duality needs.

If a manifold is nonorientable, integral Poincaré duality cannot be stated using an ordinary globally chosen fundamental class. With coefficients modulo two, orientation signs disappear and a version still holds. More generally, an orientation local system gives the correct integral formulation.

Noncompact manifolds require another change, often involving compactly supported cohomology. A noncompact oriented plane, for example, does not possess the same ordinary top-dimensional fundamental class as a closed sphere.

## What this theorem explains

Poincaré duality is a structural symmetry. It tells us that on a closed oriented manifold, topological information in degree k has a complementary life in dimension n minus k. Cup products and intersection pairings turn the symmetry into calculations with genuine geometric meaning.

And it explains why exact hypotheses matter. Orientation, compactness, and the presence of boundary are not small print. They determine which fundamental class exists and therefore which form of duality is true. A theorem that pairs dimensions so elegantly is powerful because it says exactly when—and exactly how—the pairing works.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For a connected, closed, oriented \(n\)-manifold \(M\), the chosen fundamental class \([M]\in H_n(M;\mathbb Z)\) induces isomorphisms
\[D_M:H^k(M;\mathbb Z)\xrightarrow{\ \frown[M]\ }H_{n-k}(M;\mathbb Z)\quad\text{for all }k.\]
For a compact orientable manifold with boundary, one Poincaré–Lefschetz form is \(H^k(M;\mathbb Z)\cong H_{n-k}(M,\partial M;\mathbb Z)\), and the complementary form is \(H^k(M,\partial M;\mathbb Z)\cong H_{n-k}(M;\mathbb Z)\).

**Torus:** \(H^*(T^2;\mathbb Z)\cong\Lambda_{\mathbb Z}(\alpha,\beta)\), with \(|\alpha|=|\beta|=1\), \(\alpha\smile\beta=-\beta\smile\alpha\), and orientation chosen so \(\langle\alpha\smile\beta,[T^2]\rangle=1\). For a closed orientable genus-\(g\) surface \(\Sigma_g\), \(H_1\cong\mathbb Z^{2g}\), with nondegenerate skew-symmetric intersection form on the free part.

**Boundary example:** \(H_2(D^2;\mathbb Z)=0\) while \(H_2(D^2,S^1;\mathbb Z)\cong\mathbb Z\). Ordinary top homology cannot replace the relative fundamental class. For nonorientable manifolds, \(\mathbb Z/2\)-coefficient duality or orientation local coefficients give appropriate replacements. For noncompact oriented manifolds, compactly supported cohomology enters: \(H_c^k(M;\mathbb Z)\cong H_{n-k}(M;\mathbb Z)\), with the usual hypotheses and correct cohomology theory.

### Exercises with answers

1. What is the dual of \(H^0(M;\mathbb Z)\cong\mathbb Z\) in a connected closed oriented \(n\)-manifold? **Answer:** \(H_n(M;\mathbb Z)\cong\mathbb Z\), via the fundamental class.
2. Why can an oriented torus have two independent degree-one classes? **Answer:** its first homology and cohomology both have rank two, and the two loops pair by a nondegenerate intersection form.
3. Does integral duality in this form apply directly to a Möbius band? **No:** it is nonorientable and has boundary; use suitable coefficients/local systems and relative groups.
4. Why does \(D^2\) not contradict duality when \(H_2(D^2)=0\)? **Answer:** the disk has boundary; its fundamental class is relative in \(H_2(D^2,\partial D^2)\).

### Reading and source notes

- Allen Hatcher, [*Algebraic Topology*, Section 3.3](https://pi.math.cornell.edu/~hatcher/AT/ATpage.html), orientation, cap products, duality theorem, and boundary variants.
- [Hatcher's cap-product and duality excerpt](https://pi.math.cornell.edu/~hatcher/AT/ATcapprod.pdf), naturality and Mayer–Vietoris proof architecture.
- [MIT 18.905 Algebraic Topology I](https://ocw.mit.edu/courses/18-905-algebraic-topology-i-fall-2016/), homology and cohomology foundations.
