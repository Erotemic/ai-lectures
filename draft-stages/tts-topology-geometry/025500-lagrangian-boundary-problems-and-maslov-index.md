# 025500 — Boundary Conditions for Holomorphic Strips and the Maslov Index

**Track:** Topology and Geometry. **Background:** Lagrangian submanifolds, holomorphic disks, elliptic boundary problems, the Maslov index survey. **Central question:** what counts as an elliptic boundary condition when a curve's edges must lie in two Lagrangians?

<!-- BEGIN SPOKEN LECTURE -->

# Boundary Conditions for Holomorphic Strips and the Maslov Index

A holomorphic curve defined on a closed sphere has no boundary. But the geometry of Lagrangian intersections naturally leads to maps from strips: two long parallel edges must land on two specified Lagrangian submanifolds. A solution may travel from one intersection point to another as we move along the strip.

The boundary condition is much more than a drawing. It has to make the Cauchy-Riemann equation into a well-posed elliptic problem. It also contributes an integer to the Fredholm index. That integer is closely related to the Maslov index.

## A strip between two lines

Work first in the complex plane. Take the horizontal real axis as one Lagrangian. Take another straight line passing through the origin at some angle as the other. Both are one-dimensional curves in a two-dimensional symplectic plane and hence are Lagrangian.

Picture a map from an infinite strip. The bottom edge lands on the horizontal line, and the top edge lands on the tilted line. Along the interior, the map satisfies the Cauchy-Riemann equation. The imposed boundary values do not specify exact positions; they say that each boundary point must remain on its assigned line.

When the two lines meet transversely at the origin, their intersection is isolated. This provides the simplest local model for the ends of Lagrangian Floer strips. In a curved manifold, the tangent spaces of the two Lagrangians play the roles of these lines, and the boundary condition varies with the map.

## The boundary cannot be chosen arbitrarily

For a first-order elliptic equation, giving completely arbitrary boundary data may be too strong, too weak, or incompatible with ellipticity. The condition that boundary variations lie inside a Lagrangian tangent space has precisely the correct half-dimensional character for a Cauchy-Riemann operator.

This is why Lagrangian boundary conditions recur in complex analysis, symplectic topology, and mathematical physics. They allow a complex-linear interior equation to interact with a real subspace at the boundary without destroying the Fredholm framework.

The domain can be a disk instead of a strip. Then the entire boundary may lie on a single Lagrangian. Holomorphic disks with Lagrangian boundary are central to understanding when Lagrangian Floer theory works as simply as the first picture suggests.

## Follow a line around a loop

Take an unoriented line through the origin in the plane. Start with the horizontal line. Rotate it continuously through half a turn. At the end it is horizontal again, because a line does not remember which direction along it counts as forward.

We have traced a nontrivial loop in the space of Lagrangian lines. The Maslov index assigns this basic loop the integer one under the standard normalization. Rotating through a full turn gives index two. In higher-dimensional symplectic spaces, the same index measures how a loop of Lagrangian subspaces winds in the Lagrangian Grassmannian.

This is not merely a winding number attached as decoration. In a holomorphic boundary problem, the changing Lagrangian boundary data affects the Fredholm index. The Maslov class records the topological part of that change.

## A holomorphic hemisphere

Use the Riemann sphere and choose its equator as a Lagrangian circle. One hemisphere is a holomorphic disk whose boundary is the equator, after choosing the appropriate complex orientation.

Double this disk across its boundary. The two halves combine to form a degree-one sphere. The disk's Maslov index is two. This is an example where the boundary winding can be calculated geometrically by reflection and doubling.

The Fredholm index of a parameterized holomorphic disk with fixed disk complex structure has a term equal to the real dimension of the Lagrangian plus its Maslov index. Here the Lagrangian dimension is one and the Maslov index is two, so the index is three. The disk has a three-dimensional group of holomorphic reparameterizations. In the regular, nonconstant setting, taking that quotient can leave an isolated unparameterized hemisphere.

This is a simple rehearsal of the more abstract dimension accounting we will need for strips.

## What the index predicts for strips

Suppose two Lagrangians intersect transversely at points x and y. A holomorphic strip may approach x as its long coordinate tends to minus infinity and y as it tends to plus infinity.

To predict the dimension of the space of such strips, we examine the linearized Cauchy-Riemann operator with Lagrangian boundary conditions. Its index is a relative Maslov index, expressed through the two asymptotic intersection points and appropriate choices of grading and trivialization.

A nonconstant strip can be translated along its infinite direction. That translation gives one parameter describing the same geometric trajectory. Consequently, the dimension after dividing by translation is the Fredholm index minus one at a regular nonconstant strip.

Rigid strips, meaning isolated solutions after this quotient, are the ones that can contribute to a Floer differential. One-dimensional families after the quotient are the ones whose boundaries will eventually prove the differential squares to zero.

## The complication of disk bubbling

A sequence of strips can degenerate in more ways than a pair of strips breaking apart. A nonconstant holomorphic disk may bubble from a boundary point and remain attached to one of the Lagrangians. Its Maslov index affects the expected dimensions of the possible boundary strata.

In an exact symplectic manifold with exact Lagrangians, such nonconstant disks are excluded by the area–energy identity and Stokes' theorem, provided the relevant hypotheses hold. In nonexact settings, disk bubbles may obstruct the naive identity that the Floer differential squares to zero. This is one reason more general Lagrangian Floer theory develops additional algebraic structures and bounding cochains.

We do not yet need the full obstruction theory. We do need to remember that a strip's boundary condition has geometry of its own, and that geometry can appear in compactness limits.

## The bridge from intersections to counts

The chain generators will be intersection points. The curves contributing to the differential will be strips with boundaries on two Lagrangians. Their expected dimensions will be governed by a relative Maslov index, just as ordinary Morse trajectories are governed by differences of Morse indices.

This connects three pieces of mathematics: real Lagrangian geometry at the boundary, complex elliptic analysis in the interior, and integer-valued topology through the Maslov index. Without all three, the words 'count holomorphic strips' would conceal much of the work needed to make the count meaningful.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For \(u:\mathbb R\times[0,1]\to M\), impose \(\bar\partial_Ju=0\), \(u(s,0)\in L_0\), \(u(s,1)\in L_1\). The linearized operator \(D_u\) acts on sections \(\xi\) with \(\xi(s,i)\in T_{u(s,i)}L_i\). On suitable weighted Sobolev spaces with transverse asymptotics, \(D_u\) is Fredholm. For regular nonconstant strips, quotienting the \(\mathbb R\)-action by translation lowers the local dimension by one.

The Lagrangian Grassmannian in complex dimension one is \(\Lambda(1)=\mathbb{RP}^1\cong S^1\). The loop \(\ell(t)=\operatorname{span}_\mathbb R(\cos(\pi t),\sin(\pi t))\), \(0\le t\le1\), is a generator of \(\pi_1(\Lambda(1))\cong\mathbb Z\), with Maslov index \(+1\) under the conventional generator orientation. A disk in \((\mathbb{CP}^1,\mathbb{RP}^1)\) covering a hemisphere has Maslov index \(2\); its fixed-domain real Cauchy–Riemann index is \(n\chi(D)+\mu=1+2=3\), before quotienting disk automorphisms and after checking stability/regularity.

For nonexact Lagrangians, boundary disk bubbling can contribute codimension-one degenerations to one-dimensional strip moduli; the naive \(\partial^2=0\) argument is then incomplete without suitable monotonicity, unobstructedness, or additional algebraic machinery.

### Exercises with answers

1. **Lines.** Is every smooth curve in a symplectic surface Lagrangian? **Answer:** every one-dimensional immersed curve is Lagrangian wherever immersed.
2. **Maslov loop.** What index does a half-turn of an unoriented line have under the stated normalization? **Answer:** one.
3. **Hemisphere.** What Maslov index does the standard hemisphere disk bounded by \(\mathbb{RP}^1\subset\mathbb{CP}^1\) have? **Answer:** two.
4. **Translation.** Why subtract one from the Fredholm index for a regular nonconstant strip modulo translation? **Answer:** moving its s-origin does not change the geometric trajectory and gives a free one-dimensional symmetry.

### Sources and further reading

- Andreas Floer, [Morse Theory for Lagrangian Intersections](https://doi.org/10.4310/JDG/1214442477), original intersection-complex construction.
- Dusa McDuff and Dietmar Salamon, [J-Holomorphic Curves and Symplectic Topology](https://bookstore.ams.org/coll-52), boundary-value and index foundations.
- [Maslov index](https://en.wikipedia.org/wiki/Maslov_index); [Lagrangian submanifold](https://en.wikipedia.org/wiki/Lagrangian_submanifold).
