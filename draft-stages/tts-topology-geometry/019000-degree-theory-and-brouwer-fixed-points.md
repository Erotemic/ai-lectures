# 019000 — Degree Theory, Brouwer Fixed Points, and Global Constraints

**Track:** Topology and Geometry. **Background:** homology, continuous maps, orientation, the sphere and disk. **Central question:** how can a map's algebraic winding force it to attain a value?

<!-- BEGIN SPOKEN LECTURE -->

# Degree Theory, Brouwer Fixed Points, and Global Constraints

A map can fold a sphere, stretch one hemisphere over another, and reverse orientation in some regions. If we watch only its image, it may be hard to tell what the map does globally. Yet there is an integer that survives every continuous deformation of the map. It is called the degree.

On the circle, degree is familiar from winding numbers. Take a point running once around the unit circle. A map that sends its angle to three times that angle makes the image run around three times. Its degree is three. Reverse the angle and the degree becomes minus one. Collapse the entire circle to one fixed point and the degree is zero.

The circle is only the first case. For every positive dimension n, a continuous map from the n-dimensional sphere to itself induces multiplication by an integer on its top homology group. That integer is the degree. This definition needs no differentiability, and it remembers orientation as well as multiplicity.

## Why degree cannot change continuously

Imagine a continuous family of maps from the sphere to itself. At the start, the map wraps the sphere twice. At the end, suppose it somehow wraps only once. That would require the integer degree to move from two to one during a homotopy. But homotopic maps induce the same map on homology. Degree therefore stays fixed.

This makes degree useful for existence questions. If a map has nonzero degree, it must be onto. For suppose some point of the target sphere were missing. Then the map would factor through the sphere with that point removed. A punctured sphere is contractible and has no top-dimensional homology. The induced map on top homology would be zero. But nonzero degree says it is not zero. Contradiction.

The proof doesn't identify a preimage. It proves that a preimage has to exist. That distinction is the strength of a topological argument: it can force a solution even when no formula is available.

## Counting preimages with signs

For a smooth map between compact oriented manifolds of the same dimension, degree also has a local description. Pick a regular target value. Its preimages are isolated and, under compactness, finite. At each preimage the derivative either preserves or reverses orientation. Assign plus one or minus one accordingly, then add the signs.

The signed total is the degree. A fold may create two new preimages, but typically one contributes plus one and the other minus one. Their total is zero. That is how the integer survives geometric changes that alter the raw number of preimages.

Counting unsigned preimages would be too unstable. One pair can appear or disappear under a small deformation. The orientation signs cancel exactly the kind of change that would spoil the invariant.

## The fixed-point problem on a disk

Now take a continuous map from a closed disk to itself. Must some point stay fixed? Brouwer's fixed-point theorem says yes. The claim is not that every point stays in place, nor that we can easily compute the fixed point. It is a pure existence result.

For a two-dimensional disk, suppose instead that no point is fixed. From each proposed point x, draw the ray that starts at its image and passes through x. Because the image differs from x, the ray is defined. Continue it until it reaches the boundary circle. This constructs a continuous map from the disk onto its boundary that fixes every boundary point.

Such a map is called a retraction. But a disk cannot retract onto its boundary circle. The boundary circle has a nontrivial first homology group, while the disk is contractible and has zero first homology. If a retraction existed, composing the inclusion of the circle into the disk with the retraction back onto the circle would be the identity. On first homology the composition would have to be both the identity and zero. Impossible.

The same argument works in higher dimensions with the appropriate reduced homology group. Degree theory expresses the same obstruction in a particularly compact language: the identity map of the boundary sphere has degree one, yet any map from the sphere extending over the disk must have degree zero.

## Why topology does not compute the answer

This theorem does not make fixed-point iteration automatically converge. A continuous map of a disk may have several fixed points, and a naïve numerical iteration may cycle or behave badly. Existence and effective computation are different questions.

Nor can we drop the disk's compactness and convexity without replacing them with other hypotheses. Translation on the real line, for example, has no fixed point. Topology says which structural constraints are responsible for existence, not that fixed points must appear everywhere.

Degree provides a kind of algebraic conservation law for maps. As long as a deformation respects the boundary and stays continuous, the signed count cannot change. The consequence is a proof that a missing solution would violate an integer invariant. This reasoning underlies many existence theorems in nonlinear analysis.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For n>=1, \(\widetilde H_n(S^n;\mathbf Z)\cong\mathbf Z\). The induced map of continuous \(f:S^n\to S^n\) is multiplication by \(\deg(f)\in\mathbf Z\). Degree is homotopy invariant and multiplicative under composition. For n=1, the map \(z\mapsto z^m\) has degree m. Reflection in a hyperplane has degree -1; the antipodal map has degree \((-1)^{n+1}\).

If f is smooth and y a regular value, \(\deg f=\sum_{x\in f^{-1}(y)}\mathrm{sign}\det(Df_x)\) relative to chosen orientations. This sum is finite for maps between compact manifolds of the same dimension. If \(\deg f\ne0\), f is onto, because \(S^n\setminus\{y\}\) has trivial degree-n homology.

**Brouwer's theorem:** every continuous \(F:D^n\to D^n\), n>=1, has a fixed point. For n>=2, if there were none, the ray from F(x) through x determines a continuous retraction r:D^n->S^{n-1}. Since inclusion i:S^{n-1}->D^n satisfies r o i=id, reduced \(H_{n-1}\) would imply id=0. For n=1 the same proof uses reduced \(\widetilde H_0(S^0)\cong\mathbf Z\). The continuous ray construction requires F(x) different from x everywhere and uses compactness of D^n.

### Exercises with answers

1. What is the degree of z->z^5 on S^1? **Answer:** 5.
2. Can a degree minus two map S^2->S^2 omit a point? **Answer:** no; every nonzero-degree map is surjective.
3. Can a disk deformation retract onto its boundary? **Answer:** no; the induced homology map would give identity=zero.
4. Does Brouwer's theorem imply iteration x_{k+1}=F(x_k) converges? **Answer:** no; existence of a fixed point is not a convergence theorem.

### Reading and source notes

- [Allen Hatcher, Algebraic Topology](https://pi.math.cornell.edu/~hatcher/AT/AT.pdf), degree, homology and the Brouwer fixed-point theorem.
- [University of Chicago topology notes](https://math.uchicago.edu/~may/REUDOCS/06-25-2015.pdf), a disk retraction argument for Brouwer's theorem.
