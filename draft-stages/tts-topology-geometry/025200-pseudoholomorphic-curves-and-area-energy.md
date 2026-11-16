# 025200 — Pseudoholomorphic Curves: The Equation and the Area–Energy Identity

**Track:** Topology and Geometry. **Background:** Riemann surfaces, symplectic forms, compatible almost-complex structures and basic calculus of variations. **Central question:** how can an elliptic equation convert topological area into analytic energy?

<!-- BEGIN SPOKEN LECTURE -->

# Pseudoholomorphic Curves: The Equation and the Area–Energy Identity

Suppose a small rubber sheet is stretched across a curved space. We can ask how much it bends, how much area it covers, and whether it obeys a differential equation. These are different questions. A map might have a large derivative while covering very little signed area, for example when its two derivative directions nearly cancel.

A pseudoholomorphic curve is a map for which that ambiguity largely disappears. The map respects a quarter-turn on its domain and a compatible quarter-turn on its target. As a result, its derivative is highly constrained, and its geometric area equals a natural analytic energy.

## The equation starts in ordinary complex analysis

Let the domain have coordinates s and t, and regard them as the real and imaginary parts of a complex coordinate. The quarter-turn on the domain sends the s direction to the t direction. Let J be a compatible almost-complex structure on the target symplectic manifold.

The map is J-holomorphic when differentiating after turning the domain direction gives the same result as turning the derivative in the target. Written another way, the derivative in the s direction plus J applied to the derivative in the t direction is zero.

When both domain and target are the complex plane with their standard rotations, this is exactly the Cauchy-Riemann equation. The remarkable extension is that the target rotation need only vary smoothly. It does not have to come from genuine complex coordinate charts. The equation still makes sense on arbitrary symplectic manifolds.

## Energy measures the size of the entire derivative

Use the metric built from the symplectic form and J. At each point of the domain, measure the squared lengths of the derivative in both coordinate directions, add them, and divide by two. Integrate this quantity over the surface. The result is the energy of the map.

For an arbitrary map, energy and symplectic area are different. The area is obtained by inserting the two derivative vectors into the symplectic form and integrating. It remembers orientation. Energy is nonnegative and remembers the magnitudes of derivatives, regardless of their orientation.

Here is the central calculation. Take the difference between energy and symplectic area. Complete a square. What remains is one half of the squared length of precisely the expression that appears in the Cauchy-Riemann equation. The difference is therefore nonnegative, and it vanishes exactly for a J-holomorphic map.

So any compatible J-holomorphic curve has energy equal to symplectic area. This is not a definition arranged to make the result true; it follows from linear algebra at every point of the domain.

## A sphere with energy two

Return to the Riemann sphere with its standard complex structure and normalize its total symplectic area to one. The map that squares a complex coordinate and extends across infinity is holomorphic of degree two.

Its pullback of the area form integrates to two. By the energy identity, its analytic energy is also two. We have calculated a norm involving derivatives without solving a differential equation explicitly across the whole sphere. Topological degree and compatibility did the work.

A degree-three holomorphic self-map has energy three under the same normalization. These integer values are not the energy of every possible map or every possible symplectic manifold. They arise because this particular area class pairs integrally with the degree of the map.

## Why positive area constrains maps

Now suppose we have a symplectic manifold whose symplectic form integrates to zero over every sphere mapped into it. Such a manifold is symplectically aspherical. A holomorphic sphere in this target would have energy equal to its symplectic area, hence zero. Since the energy is an integral of nonnegative squared derivative lengths, the derivative must vanish everywhere. The map is constant.

This gives a powerful nonexistence theorem: a symplectically aspherical target has no nonconstant J-holomorphic spheres for compatible J. The two-torus is an example, because every map from a sphere to a torus is null-homotopic and therefore has zero symplectic area.

This matters for Floer homology. One way for a sequence of cylinders to lose compactness is by producing tiny holomorphic spheres at points where derivatives concentrate. In an aspherical target, the spheres that such a blow-up would produce cannot be nonconstant. One major source of noncompactness is removed.

## Why the energy identity is not a compactness theorem

We still need to control what happens to a whole sequence of maps. A bound on the integral of squared derivatives does not automatically give a bound on the derivative at every point. Energy can become concentrated in a shrinking region. That failure of pointwise control is called bubbling.

The equation supplies additional elliptic estimates that ordinary maps do not enjoy. Under suitable assumptions, bounded-energy J-holomorphic maps have subsequences that converge smoothly away from finitely many concentration points, and rescaling near those points reveals holomorphic bubbles. Establishing that result takes more than the identity we just derived. It needs local regularity, monotonicity or mean-value inequalities, and a precise description of the limiting domain.

There is an important contrast with Yang-Mills instanton bubbling. In both settings energy can concentrate and a rescaled geometric solution emerges. But the dimensions, scaling exponents, topology, and analytic equations differ. One should learn the analogy without importing theorems from one theory into the other uncritically.

## Why the equation matters for geometry

In ordinary differential geometry, curves can be found by solving geodesic equations. In symplectic topology, J-holomorphic curves provide another sort of probe. Their area is tied to topology, and their behavior is governed by an elliptic equation. The target's symplectic structure limits what they can do.

The first lesson is the area–energy identity. The second, to be developed next, is that it comes from an elliptic first-order operator. The third is that control of energy plus elliptic analysis produces a compactness theory with carefully classified exceptions. Together these facts make it possible to count curves and to extract genuinely global information from local differential equations.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For a domain \((\Sigma,j)\) with local conformal coordinates \((s,t)\) and a compatible \(J\), the pseudoholomorphic equation is \(\bar\partial_Ju=\tfrac12(du+J\circ du\circ j)=0\), equivalent locally to \(u_s+J(u)u_t=0\). For a general smooth map,
\[
E(u)=\frac12\int_\Sigma (|u_s|^2+|u_t|^2)\,ds\,dt,\qquad
E(u)-\int_\Sigma u^*\omega=\frac12\int_\Sigma|u_s+J(u)u_t|^2\,ds\,dt\ge0.
\]
The identity uses a conformal domain metric and \(g(\cdot,\cdot)=\omega(\cdot,J\cdot)\). It extends globally by conformal invariance of energy in dimension two. For a \(J\)-holomorphic map, \(E(u)=\langle[\omega],u_*[\Sigma]\rangle\) on a closed oriented domain.

If \(\omega|_{\pi_2(M)}=0\), every compatible \(J\)-holomorphic \(u:S^2\to M\) is constant, because \(E(u)=\int_{S^2}u^*\omega=0\). This only rules out spherical bubbling; other degeneration modes require separate arguments.

### Exercises with answers

1. **Square identity.** What quantity must vanish for equality between energy and symplectic area? **Answer:** \(u_s+J(u)u_t\), equivalently \(\bar\partial_Ju=0\).
2. **Degree.** If \(\int_{\mathbb{CP}^1}\omega=1\), what energy does \(z\mapsto z^4\) have? **Answer:** four.
3. **Aspherical.** Why does symplectic asphericity rule out nonconstant holomorphic spheres? **Answer:** all sphere areas vanish, so the energy vanishes.
4. **Limitation.** Does bounded energy imply uniform derivative bounds for an arbitrary sequence of J-curves? **Answer:** no; derivatives may concentrate and create bubbles.

### Sources and further reading

- Mikhail Gromov, [Pseudo-holomorphic Curves in Symplectic Manifolds](https://doi.org/10.1007/BF01388806) (1985), original framework.
- Chris Wendl, [Lectures on Holomorphic Curves](https://arxiv.org/abs/1011.1690), energy and local estimates.
- [Pseudoholomorphic curve](https://en.wikipedia.org/wiki/Pseudoholomorphic_curve); [Symplectically aspherical manifold](https://en.wikipedia.org/wiki/Aspherical_space#Symplectically_aspherical_manifolds).
