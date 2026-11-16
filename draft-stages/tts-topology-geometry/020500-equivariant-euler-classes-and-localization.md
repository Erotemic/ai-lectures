# 020500 — Fixed-Point Localization: Weights, Euler Classes, and Denominators

**Track:** Topology and Geometry. **Background:** equivariant cohomology, characteristic classes, oriented integration. **Central question:** why does a fixed point contribute the reciprocal of a rotation weight?

<!-- BEGIN SPOKEN LECTURE -->

# Fixed-Point Localization: Weights, Euler Classes, and Denominators

A localization formula can look suspicious at first. How could an integral over an entire compact manifold equal a finite sum over isolated points? To understand why, focus not on the sum but on the denominator. It measures the directions lost when we restrict from the manifold to its fixed set.

Near a fixed point of a circle action, the group acts linearly on the tangent space. Because the group is compact, we can choose a compatible metric and split the representation into two-dimensional rotation planes and directions on which the action is trivial. For an isolated fixed point, no nonzero tangent direction is fixed, so the tangent space splits into genuine rotation planes.

## Rotation weights are integers

On an oriented real two-plane carrying a complex structure, the circle can act by rotating a vector through n times the group angle. The integer n is the weight. Positive and negative weights give opposite oriented rotations. Weight zero means the circle acts trivially on that plane, so it would be tangent to a fixed component rather than normal to one.

For one such complex line, the equivariant Euler class is its weight multiplied by the polynomial generator u, with the orientations chosen consistently. For a direct sum of rotation planes, multiply the individual Euler classes. Thus an isolated fixed point in a four-dimensional manifold with two weights a and b has tangent equivariant Euler class a times b times u squared.

This is why the weights cannot be omitted. Two fixed points with the same value of an integrand may contribute differently if their normal representations have different weights.

## The localization statement

For a compact oriented manifold with a torus action, the Atiyah–Bott–Berline–Vergne formula expresses the equivariant integral of a closed equivariant class as a sum over fixed components. On each component, restrict the class, divide by the equivariant Euler class of its normal bundle, and integrate over that component.

Division requires care. Before localization, the coefficient ring consists of polynomials in equivariant parameters. After localization, we invert nonzero weights and the necessary polynomial factors. The individual fixed-point contributions may be rational functions, even though their sum is a polynomial. This cancellation is one of the most instructive features of the theorem.

If the fixed points are isolated, integration over a point does nothing. The formula reduces to a sum of the values of the equivariant class divided by tangent Euler classes. If a fixed component has positive dimension, we must integrate over that component and use the Euler class of its *normal* bundle. Tangent directions within the fixed component are not divided out.

## Two poles and two opposite weights

Rotate a two-sphere around its vertical axis. Only the north and south poles are fixed. With the complex orientation induced by the sphere's area form, the linearized rotation has weight plus one at the north pole and minus one at the south pole, when the circle generator and orientations are normalized consistently.

Integrate the equivariant unit class one. The north contribution is one divided by u. The south contribution is one divided by minus u. They cancel. That is exactly what the cohomological degree rule predicts: integrating a degree-zero class over an oriented two-dimensional manifold produces an element in degree minus two, which must vanish in the unlocalized polynomial ring.

Now integrate the equivariant Euler class of the tangent bundle. At a fixed point its restriction equals the tangent Euler class itself, so each quotient is one. The result is two, equal to the Euler characteristic of the sphere. In ordinary Gauss–Bonnet language, curvature integrated over the sphere also yields two after the conventional normalization. The localization formula has converted a global curvature invariant into two local representation calculations.

## Why the formula is geometrically plausible

On the part of the manifold where the circle acts without fixed points, the generating vector field does not vanish. One can use an invariant one-form that evaluates to one on the generator and construct a homotopy showing, after inverting u, why equivariant cohomology there is severely constrained. Near the fixed set that construction breaks down because the generating vector field becomes zero.

So after localization, the fixed set is precisely where the surviving equivariant information concentrates. A rigorous proof uses equivariant Thom classes, pushforwards and the self-intersection formula, or an equivalent differential-form argument. The Euler-class denominator is the correction factor for inserting a fixed component into the ambient manifold.

## Boundaries of the theorem

The compactness and orientation assumptions are not optional decoration. For a noncompact manifold, an integral may diverge or receive boundary-at-infinity terms. For a fixed component with a nontrivial normal bundle, its equivariant Euler class contains ordinary characteristic classes in addition to the weights. If the normal representation has zero weights, the supposed fixed component was not the full fixed locus or the chosen torus parameter requires refinement.

There is no general permission to replace integration by counting fixed points. What localization permits is a precisely weighted pushforward after a specified algebraic localization. Once the tangent weights and degree conventions are visible, the formula becomes a tool for actual computations rather than a magic trick.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For a torus T acting on compact oriented M, and `α∈H_T^*(M)` over Q or R, the ABBV formula in localized equivariant cohomology reads

\[
\int_M\alpha=\sum_{F\subset M^T}\int_F\frac{i_F^*\alpha}{e_T(N_F)}.
\]

At an isolated fixed point with oriented complex tangent weights `w_1,...,w_n`, `e_T(T_pM)=(∏_j w_j)u^n` for S¹. For standard oriented `S²`, north and south weights are `+1,-1`. Thus `∫_{S²}1=1/u-1/u=0`; `∫_{S²}e_T(TS²)=1+1=2`.

The phrase “integral of 1” denotes the degree-lowering cohomological pushforward, not the area of the sphere. Area is the integral of a degree-two form. The distinction prevents a frequent false comparison.

### Exercises with answers

1. What is the equivariant Euler class of a weight-three complex line? **Answer:** `3u`.
2. What is it for two complex lines of weights two and minus three? **Answer:** `-6u²`.
3. Why do the two fixed-point contributions for `∫1` cancel on S²? **Answer:** their tangent weights have opposite signs.
4. What bundle supplies the denominator for a positive-dimensional fixed component F? **Answer:** the equivariant normal bundle `N_F`, not `TF`.

### Sources and further reading

- M. Atiyah and R. Bott, [The Moment Map and Equivariant Cohomology](https://doi.org/10.1016/0040-9383(84)90021-1) (1984).
- L. Jeffrey, [Equivariant Cohomology lecture notes](https://www.math.toronto.edu/~jeffrey/mat1312/lec10.eqcoh.pdf), the abelian localization theorem.
- [Atiyah–Bott localization theorem](https://en.wikipedia.org/wiki/Equivariant_cohomology).
