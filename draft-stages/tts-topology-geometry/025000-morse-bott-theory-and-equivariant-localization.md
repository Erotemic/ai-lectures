# 025000 — Morse–Bott Theory and Equivariant Localization

**Track:** Topology and Geometry. **Background:** Morse theory, homology, Lie group actions, characteristic classes. **Central question:** how can fixed points and critical manifolds reveal global topology?

<!-- BEGIN SPOKEN LECTURE -->

# Critical points can arrive in families

Morse theory studies the critical points of a smooth function on a manifold. When critical points are isolated and nondegenerate, each one contributes a handle to a decomposition of the manifold. The number and indices of those handles constrain the manifold's homology.

But geometry often contains symmetry, and symmetry can make critical points appear in families. Think of a landscape that is constant along a circular ridge. Every point on the ridge is critical in the direction along the ridge, yet the function may curve sharply across the ridge. The usual Morse condition fails because the Hessian has a zero direction, but the failure is controlled.

Morse–Bott theory handles precisely this situation. Instead of requiring isolated critical points, it permits critical submanifolds. The Hessian may vanish along the tangent directions to a critical submanifold, but it must be nondegenerate in directions normal to it. This lets us describe what happens when a level set crosses an entire critical manifold.

## A product example

Take the product of a sphere and a circle. Use the height function on the sphere, ignoring the circle coordinate. On the sphere alone, height has two critical points: the north and south poles. On the product, each pole is accompanied by every point of the circle. The critical sets are two circles.

Near the southern circle, the function increases in the two sphere directions; near the northern circle, it decreases. Along the circle itself the function stays constant. The Hessian's kernel is exactly the tangent direction to the critical circle. The normal Hessian is nondegenerate, so the function is Morse–Bott.

Crossing a critical value attaches the disk bundle of the negative normal directions, rather than one ordinary disk. The topology contributed by a critical manifold is therefore related to the topology of the manifold *and* the rank and orientation behavior of its negative normal bundle.

This is already enough to explain a familiar phenomenon. The Euler characteristic of a product of a sphere and a circle is zero because the circle's Euler characteristic is zero. The two critical circles do not each contribute one the way isolated critical points would. Their contributions are weighted by the Euler characteristic of the critical submanifolds.

## Symmetry leads to localization

Now consider a compact oriented manifold with a circle action. The points fixed by the entire circle action form a collection of submanifolds, perhaps isolated points. At first it seems impossible that integrating a differential form over the full manifold could be recovered from information on just those fixed sets. Equivariant localization shows that, after introducing a formal variable recording the circle symmetry and inverting suitable weights, such a formula exists.

The idea is to extend ordinary cohomology to equivariant cohomology, which remembers both the space and the group action. The normal directions to each fixed component carry weights under the circle action. Those weights appear in an equivariant Euler class. Dividing by that Euler class compensates for restricting from the full manifold to the fixed set.

The resulting localization formula says that an equivariant integral over the whole manifold is a sum of contributions from fixed components. Each contribution restricts the class to the component, divides by the Euler class of its normal bundle, and integrates over that component.

The denominator is essential. Ignoring it would make the formula wrong even for the sphere.

## A sphere calculation

Rotate the two-sphere around its vertical axis. Only the north and south poles remain fixed. At each pole, the tangent plane rotates with a nonzero weight, but the signs of the weights depend on the orientations used. If we integrate the equivariant Euler class of the tangent bundle, each fixed point contributes one: its numerator and denominator are the same equivariant Euler class of that tangent representation.

The sum is two, agreeing with the Euler characteristic of the sphere. We have computed a global topological number from two local contributions.

If instead we try to integrate the constant class one, the two contributions have opposite terms proportional to the inverse of the equivariant variable, and they cancel. That matches the fact that integrating a degree-zero class over a two-dimensional closed manifold gives zero in ordinary cohomological grading.

Both examples show why localization is not simply 'count the fixed points.' It is a weighted statement about cohomology degrees, orientations, and normal representations.

## From Morse–Bott to geometry with symmetry

The link between Morse–Bott theory and equivariant localization is not accidental. Both use the way a function or group action concentrates geometry into special loci. The critical manifold has normal directions whose Hessian determines how topology changes. A fixed component has normal directions whose group weights determine its localization contribution.

These are different theories with different hypotheses, so one should not substitute one theorem for the other. Yet both reveal global information by studying local behavior transverse to a distinguished submanifold.

Such methods are useful in symplectic geometry, representation theory, and characteristic-class calculations. A moment map for a Hamiltonian circle action can supply a Morse–Bott function. Its critical points often agree with the fixed points of the action, under suitable hypotheses. The resulting geometry connects the handle picture of Morse theory with the weighted fixed-point calculations of equivariant cohomology.

The conclusion is a useful shift in perspective. Symmetry may create degenerate critical points, but it can also make topology easier to compute. Instead of perturbing away every symmetric feature, we can keep the symmetry and learn to read the information stored in its critical sets and fixed points.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

A smooth `f:M -> R` is Morse–Bott if its critical set is a disjoint union of smooth submanifolds C and `ker Hess_p f = T_p C` for all `p in C`. The normal Hessian splits the normal bundle into positive and negative bundles; attachment across a critical value is modeled by the negative normal disk bundle, with caveats concerning completeness and compactness.

For `M=S^2 x S^1`, `f(p,theta)=height(p)`, the critical components are `C_N={N} x S^1` and `C_S={S} x S^1`. The normal indices are 2 and 0 respectively. Since `chi(S^1)=0`, their Euler-characteristic contributions vanish, compatible with `chi(M)=chi(S^2)chi(S^1)=0`.

For a torus T action on a compact oriented M and a suitable equivariant cohomology class `alpha`, the Atiyah–Bott/Berline–Vergne localization formula is, after localization at the nonzero weights,
\[
\int_M \alpha=\sum_{F\subset M^T}\int_F \frac{i_F^*\alpha}{e_T(N_F)}.
\]
For the standard circle rotation of `S^2`, the two isolated fixed components contribute 1 each to `int_{S^2} e_T(TS^2)=chi(S^2)=2`. For `alpha=1`, the formal contributions are `1/u` and `-1/u` in consistent orientation conventions, summing to zero.

### Exercises with answers

1. Why is `height` on `S^2 x S^1` not Morse? **Answer:** its critical points occur in circles, and the Hessian vanishes along each tangent circle.
2. Why is it Morse–Bott? **Answer:** the Hessian is nondegenerate on the normal sphere directions, with kernel exactly tangent to each critical circle.
3. What appears in the denominator of the localization formula? **Answer:** the equivariant Euler class of the normal bundle to a fixed component.
4. What global number results from integrating the tangent Euler class of the two-sphere? **Answer:** 2, its Euler characteristic.

### Reading and source notes

- [Bott, Nondegenerate Critical Manifolds](https://doi.org/10.2307/1970034), the Morse–Bott viewpoint.
- [Atiyah and Bott, The Moment Map and Equivariant Cohomology](https://doi.org/10.1016/0040-9383(84)90021-1), localization and moment-map geometry.
- [Guillemin and Sternberg, Supersymmetry and Equivariant de Rham Theory](https://doi.org/10.1007/978-3-662-03992-7), equivariant cohomology and fixed-point formulas.
