# 025100 — Riemann Surfaces and Holomorphic Maps: The Models We Can Calculate

**Track:** Topology and Geometry. **Background:** complex differentiation, smooth manifolds, integration, degree and orientation. **Central question:** what changes when holomorphic functions become maps between curved surfaces?

<!-- BEGIN SPOKEN LECTURE -->

# Riemann Surfaces and Holomorphic Maps: The Models We Can Calculate

Before we use holomorphic curves in a symplectic manifold, it is worth returning to their simplest setting: ordinary complex analysis. There, a map can be holomorphic for a very concrete reason. The derivative respects multiplication by the imaginary number i. The Cauchy-Riemann equations express exactly that compatibility.

When the source and target are curved surfaces, the same idea survives. But the geometry of a sphere, a torus, and a disk leads to different questions about degree, energy, boundary behavior, and families of maps. Those differences will matter when we attempt to count solutions.

## What is a Riemann surface?

A smooth surface may be covered by local coordinate patches. A Riemann surface is a two-dimensional real manifold whose patches use complex coordinates, and whose coordinate-change maps are holomorphic wherever they overlap.

The sphere is a first example. Remove its north pole and project the remaining points onto a plane, giving a complex coordinate z. Remove its south pole to obtain another complex coordinate w. On their overlap, w equals one over z. This change is holomorphic away from zero. The two charts give the sphere a global complex structure even though a single complex coordinate cannot cover it.

The standard sphere viewed this way is called the Riemann sphere, or complex projective line. Its points are one-dimensional complex subspaces of a two-dimensional complex vector space. Another picture is the ordinary complex plane together with one point at infinity.

A torus also admits complex structures. Start with the complex plane and identify points that differ by integer combinations of two linearly independent complex periods. The quotient is a compact complex torus. Different period lattices can describe different complex shapes even though their underlying topological space is always a torus.

## Holomorphicity without a global coordinate

At a point of a Riemann surface, multiplication by i in the local chart determines a quarter-turn on the tangent plane. Because the coordinate changes are holomorphic, this definition does not depend on which chart we used.

A smooth map between two Riemann surfaces is holomorphic if its derivative commutes with these quarter turns. In coordinates this is the usual Cauchy-Riemann condition. The definition does not require either surface to be flat.

Take the map from the complex plane to itself sending z to z squared. It doubles the angle and squares the distance from the origin. Away from zero it is locally two-to-one. At zero the derivative vanishes: the map is branched. There is no contradiction with holomorphicity, because a holomorphic map need not have invertible derivative everywhere.

The same map extends to the Riemann sphere by sending infinity to infinity. This gives a map of degree two. A generic target point has two preimages, counted with multiplicity. The two special points, zero and infinity, are branch points.

## Degree measured by area

Give the Riemann sphere a positive area form normalized so that its total area is one. Pull that area form back through the squaring map and integrate it over the source sphere. The result is two. Each regular target area element is covered twice, with positive orientation.

More generally, the map sending z to z raised to the d-th power extends to a holomorphic map of degree d for positive integers d. Its pulled-back symplectic area is d times the target's total area. This is a geometric way to read degree from an integral.

Why emphasize orientation? In ordinary topology, maps can have positive or negative local degrees. A nonconstant holomorphic map between oriented Riemann surfaces has nonnegative local multiplicities. Complex linear maps preserve the complex orientation wherever their derivative is nonzero. In the spherical examples, the degree is a nonnegative integer.

We should not confuse degree with the number of distinct preimages of every point. A branch point changes that count. Degree is the stable multiplicity-weighted number, and the area integral remembers it even in the presence of branching.

## Why spheres and tori behave differently

The sphere admits many nonconstant holomorphic maps to itself. A torus admits translations and maps induced by suitable complex-linear transformations of its covering plane. Yet there is no nonconstant holomorphic map from the sphere to a complex torus.

Here is an approachable reason. A map from the simply connected sphere to the torus lifts to the complex plane. The lifted map is holomorphic on the compact Riemann sphere, so it must be constant: a holomorphic function on a compact connected Riemann surface cannot be nonconstant if its target is the complex plane. Thus the original map was constant.

This is a reminder that target topology and complex structure restrict which curves exist. Later, existence and nonexistence of holomorphic spheres will become decisive in compactness questions.

## Families and symmetries of maps

There is a second complication. The same geometric curve can be described by many parameterizations. A fractional linear transformation of the sphere is a holomorphic change of its coordinate. Composing a map with such a transformation changes the formula without necessarily changing the underlying image.

The group of holomorphic automorphisms of the sphere has real dimension six. When we compute the expected dimension of a space of holomorphic spheres, we need to decide whether parameterizations count as different objects. If not, we must account for these six dimensions, with care around maps having symmetries.

For the degree-one maps from the Riemann sphere to itself, every such map is a holomorphic automorphism. Modulo reparameterization, there is essentially one degree-one map. That simple example is a useful check on a much later Fredholm index calculation.

## The bridge to almost-complex targets

The formulas we have used rely on genuine complex charts, but the key equation only says that the map's derivative respects a quarter turn. In symplectic geometry, we can choose a compatible almost-complex structure on any symplectic target and write that equation even without global holomorphic target coordinates.

Gromov's theory of pseudoholomorphic curves starts from that extension. Local complex-analysis estimates survive in modified form because the equation is elliptic. Positivity of area survives because the almost-complex structure is compatible with the symplectic form. But the classification by rational functions no longer applies, and counting curves requires functional analysis and compactness.

Keep the Riemann sphere examples close at hand. They will supply explicit curves, degrees, and branch points against which more abstract definitions can be tested. They also make clear that a holomorphic curve is not merely a drawn picture: it is a smooth map satisfying a rigid differential equation with topological consequences.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Identify \(\mathbb{CP}^1=\mathbb C\cup\{\infty\}\) with atlas \(w=1/z\) on the overlap. A holomorphic map \(u_d(z)=z^d\) extends over \(\infty\) and has topological degree \(d\ge1\). Normalize the Fubini–Study form by
\[
\omega_{FS}=\frac{i}{2\pi}\frac{dz\wedge d\bar z}{(1+|z|^2)^2},\qquad \int_{\mathbb{CP}^1}\omega_{FS}=1.
\]
Then \(\int_{\mathbb{CP}^1}u_d^*\omega_{FS}=d\). The map has local branching at \(0\) and \(\infty\) when \(d>1\). The Riemann–Hurwitz formula for a degree-\(d\) sphere-to-sphere map gives total branching \(2d-2\), consistent with two branch points of order \(d-1\).

For \(\mathbb C/\Lambda\), a holomorphic map \(\mathbb{CP}^1\to\mathbb C/\Lambda\) lifts to an entire map on \(\mathbb{CP}^1\) since \(\mathbb{CP}^1\) is simply connected; it is constant. Holomorphic automorphisms of \(\mathbb{CP}^1\) form \(\mathrm{PSL}_2(\mathbb C)\), real dimension six, a fact needed when quotienting parameterized sphere moduli.

### Exercises with answers

1. **Atlas.** What is the transition function between the two standard \(\mathbb{CP}^1\) charts? **Answer:** \(w=1/z\) on their overlap.
2. **Degree.** What is the total normalized symplectic area of \(z\mapsto z^3\)? **Answer:** three.
3. **Branching.** Why does the fiber above zero have fewer than three distinct points for \(z^3\)? **Answer:** zero is a branch point of multiplicity three.
4. **Target topology.** Can a nonconstant holomorphic sphere map into a complex torus? **Answer:** no; it lifts to a holomorphic map from the compact sphere to \(\mathbb C\), hence is constant.

### Sources and further reading

- Mikhail Gromov, [Pseudo-holomorphic Curves in Symplectic Manifolds](https://doi.org/10.1007/BF01388806), *Inventiones Mathematicae* 82 (1985), 307–347.
- Chris Wendl, [Lectures on Holomorphic Curves](https://arxiv.org/abs/1011.1690), first examples and complex structures.
- [Riemann surface](https://en.wikipedia.org/wiki/Riemann_surface); [Riemann sphere](https://en.wikipedia.org/wiki/Riemann_sphere); [Riemann–Hurwitz formula](https://en.wikipedia.org/wiki/Riemann%E2%80%93Hurwitz_formula).
