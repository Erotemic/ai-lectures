# 060000 — Equivariant Localization: A Global Count from Fixed Points

**Track:** Abstract Algebra. **Background:** torus actions, characteristic classes, intersection theory, and virtual fundamental classes. **Central question:** how can a geometric integral over a large space be computed using only its fixed-point locus?

<!-- BEGIN SPOKEN LECTURE -->

# The economy of symmetry

Imagine integrating a geometric quantity over an entire projective variety. Now imagine that a circle or multiplicative group acts on that variety in a way that preserves the object we are measuring. Under the right hypotheses, the global integral can be reconstructed from contributions concentrated at points or subspaces left fixed by the symmetry.

The statement is called localization. It does not assert that the original geometric space has shrunk. Rather, after we enlarge the coefficient ring by allowing certain weights to be inverted, its equivariant cohomology or intersection theory carries the same information as its fixed locus.

The algebra behind this sounds formal until we calculate the projective line. That example shows both the power of localization and the importance of keeping the weights straight.

# The projective line under a torus action

Represent a point of the complex projective line by two homogeneous coordinates. Let a nonzero complex number t act by multiplying the first coordinate by t and leaving the second coordinate unchanged.

There are exactly two fixed points. One is the first coordinate axis; the other is the second coordinate axis. Every other point moves when we vary t.

To each fixed point we associate the weight with which the torus acts on its tangent line. Near the first axis, a local coordinate is the ratio of second coordinate to first. This ratio is multiplied by the reciprocal of t, so the tangent weight is negative one. Near the second axis the local coordinate is first over second, and its tangent weight is positive one.

Localization will divide each fixed-point contribution by the corresponding tangent weight. This division takes place in the equivariant coefficient ring after we invert the weight parameter, not in ordinary integer cohomology.

# A calculation with a line bundle

Consider the hyperplane line bundle on the projective line. Choose the torus action on it induced by the standard action on the two-dimensional coordinate space. The fiber weight at the first fixed point is negative one, and at the second it is zero, with this choice of linearization.

We want to integrate the first Chern class of that line bundle over the projective line. Ordinary intersection theory says the answer is one, because the bundle has degree one.

The localization formula gives the same result almost immediately. At the first fixed point, divide the first Chern weight, negative one, by the tangent weight, also negative one. The ratio is one. At the second fixed point, the numerator is zero and the tangent weight is positive one, so its contribution is zero. Adding them gives one.

The calculation is tiny, but the lesson is large. A global intersection number is reconstructed from local linear algebra at fixed points. The choice of equivariant lift determines individual weights, while the final nonequivariant integral is independent of that auxiliary choice.

# What if the fixed locus has components?

In general the fixed locus need not consist of isolated points. It may contain curves or higher-dimensional subspaces. Then the localization formula integrates over each fixed component, dividing by the equivariant Euler class of its normal bundle.

The normal bundle records the directions that move away from the fixed locus. Its torus weights are nonzero along the moving directions, which makes the Euler class invertible after localization. Tangent directions within the fixed component remain in the ordinary integration on that component.

There is a useful separation here. Geometry of the fixed component stays geometric. Geometry transverse to it is compressed into a bundle and its characteristic classes. Localization can simplify a high-dimensional integral dramatically when the fixed pieces are small.

# When the space is singular or obstructed

Moduli spaces of curves and maps are rarely smooth. The ordinary tangent bundle may not capture their deformation theory. If the moduli space has an equivariant perfect obstruction theory, its tangent and obstruction directions form a virtual tangent class.

The virtual localization theorem replaces the ordinary normal bundle by a virtual normal object made from the moving parts of that obstruction theory. Fixed components carry their own virtual fundamental classes. The global virtual class can be expressed as a sum of contributions from these fixed components, divided by the equivariant Euler classes of the virtual normal terms.

The theorem has hypotheses. One needs compatible torus actions and obstruction theories, and one works in an appropriate localized equivariant intersection theory. Properness is relevant for obtaining global numerical integrals. In some formulations additional embedding conditions are imposed. The formula is not permission to write down fractions for any singular space whatsoever.

# Graphs appear inside geometry

For the torus action on projective space, a fixed stable map may have components mapped to fixed points, connected by components that cover torus-invariant lines. Such a map can often be encoded by a decorated graph. Vertices carry fixed-point and genus information; edges carry degrees of coverings.

Virtual localization then expresses a complicated invariant as a sum over graphs. The denominator records moving deformation and obstruction directions. The numerator includes tautological intersection data on the fixed components.

This is a striking bridge between algebraic geometry and combinatorics. The graph is not a new definition of a curve. It is a bookkeeping device made valid by fixed-point geometry and the virtual localization theorem.

# Interpreting the result correctly

The fixed-point contributions can be rational functions of the equivariant weight parameter, even when the final ordinary invariant is an integer or rational number independent of that parameter. Different terms may contain apparent poles that cancel after summation. Discarding individual terms because they look singular would destroy the invariant.

Localization says a great deal, but not that fixed points are the only geometric objects that exist or that every answer is an ordinary count of curves. It offers a mathematically controlled reduction of an intersection calculation.

The projective-line example is the smallest complete model: identify fixed points, calculate tangent and bundle weights, divide, and sum. Virtual localization applies this recipe to spaces where the notion of dimension itself must be corrected by deformation and obstruction data.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Let `T=G_m` act on `P^1` by `t.[x:y]=[t x:y]`. Write `u=c_1^T` of the weight-one representation in `A_T^*(pt)~=Z[u]`. The fixed points are `p_x=[1:0]` and `p_y=[0:1]`; tangent weights are `-u` at p_x and `+u` at p_y. For O(1) with the linearization dual to the tautological O(-1), the fiber weights are `-u` at p_x and `0` at p_y. Therefore the equivariant localization formula gives
\[
\int_{\mathbf P^1} c_1^T(\mathcal O(1))
=\frac{-u}{-u}+\frac0u=1.
\]
The fractions live in the localized equivariant Chow ring `Q(u)` (or an appropriate localized coefficient ring). They are not divisions by ordinary cohomology classes before localization.

For a smooth proper T-space X and fixed connected components F,
\[
\int_X \alpha=\sum_{F\subseteq X^T}\int_F\frac{i_F^*\alpha}{e_T(N_F)}
\]
under the standard hypotheses. For a T-equivariant perfect obstruction theory, **virtual** localization schematically replaces `[F]` by `[F]^vir` and `N_F` by the virtual normal class assembled from moving tangent-obstruction terms. The fixed locus may be stacky and some contributions may be rational.

### Exercises with answers

1. Why is the tangent weight at `[1:0]` negative? **Answer:** `y/x` transforms as `t^-1(y/x)`.
2. What is the nonequivariant degree of O(1) on P^1? **Answer:** one.
3. If a fixed component is a curve, does localization replace its contribution with a single number before integrating? **Answer:** no; one integrates a characteristic-class expression over the fixed component.
4. What replaces the ordinary normal bundle in virtual localization? **Answer:** the moving part of the equivariant virtual tangent/obstruction complex, expressed as a virtual normal bundle.

### Reading and source notes

- [Graber and Pandharipande, Localization of Virtual Classes](https://arxiv.org/abs/alg-geom/9708001), the virtual localization theorem and stable-map graph sums.
- [The Stacks Project, Intersection Theory](https://stacks.math.columbia.edu/download/intersection.pdf), Gysin maps and intersection-theoretic foundations.
- [Atiyah and Bott, The Moment Map and Equivariant Cohomology](https://doi.org/10.1016/0040-9383(84)90021-1), fixed-point methods in equivariant topology.
