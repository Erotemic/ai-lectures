# 046000 — Grothendieck-Riemann-Roch and Pushforwards

**Track:** Abstract Algebra. **Background:** Riemann-Roch on curves and surfaces, K-theory, Chern classes, sheaf cohomology. **Central question:** how can pushforward of vector bundles be reconciled with pushforward of geometric cycles?

<!-- BEGIN SPOKEN LECTURE -->

# Counting sections as an operation of pushing forward

Riemann-Roch on a curve predicts an Euler characteristic from degree and genus. On a surface it predicts an Euler characteristic from divisor intersections. Grothendieck-Riemann-Roch puts these calculations into a single statement about maps between spaces. It asks not only how many sections live on a variety, but how a family of geometric objects behaves when we send it to another variety.

Take a proper map from X to Y. A vector bundle on X contains local linear data. When we push it forward along the map, the fibers over points of Y collect the sections that live above them. But ordinary pushforward is not generally exact. Some data moves into higher direct images. This is exactly the setting where derived categories become necessary rather than decorative.

The correct pushforward class is an alternating combination of the higher direct images. In K-theory it is the class of the derived pushforward. A second kind of pushforward acts on geometric cycles and characteristic classes. Grothendieck-Riemann-Roch relates the two, but a correction factor appears.

## Why a correction factor is needed

The Chern character turns a vector bundle into a sum of rational characteristic classes. It behaves well with direct sums and tensor products, so it translates questions about bundles into calculations in a cohomology or Chow ring. One might hope that the Chern character commutes with pushforward without adjustment.

It does not. The discrepancy is measured by the Todd class of the tangent bundle. For a proper morphism between smooth varieties, the theorem says that pushing forward the Chern character multiplied by the Todd class of X gives the Chern character of the K-theoretic pushforward multiplied by the Todd class of Y.

That extra factor is not an arbitrary normalization. Integration along fibers changes dimensions, and the tangent bundles carry information about that change. The Todd class compensates for it. In the formulation using the virtual relative tangent bundle, the correction is the Todd class of the relative tangent data.

The theorem takes place after passing to rational coefficients, because characteristic-class formulas involve denominators. In the general form, one also needs appropriate hypotheses ensuring that the pushforward is defined. We will work with a smooth proper map between smooth quasi-projective varieties over a field, where the familiar formula is available.

## The projective line as a test

Let X be the projective line and Y a point. Choose the line bundle O of d. Its Euler characteristic is the number of independent global sections minus the dimension of the first cohomology group. Grothendieck-Riemann-Roch now says that this alternating dimension is the degree-one component of the Chern character of O of d multiplied by the Todd class of the tangent bundle of the projective line.

Write H for the class of a point. In the Chow ring, H squared is zero. The Chern character of O of d is one plus d times H. The Todd class of the tangent bundle is one plus H, since the tangent bundle has degree two. Multiply and keep the coefficient of H. The answer is d plus one.

For nonnegative d this is the familiar dimension of homogeneous polynomials of degree d in two variables. But the same Euler characteristic formula remains true for negative d. When d is minus two, there are no global sections, while first cohomology has dimension one, so the Euler characteristic is minus one. The calculation and the cohomology agree.

This is an important difference between an index and a count. The theorem computes an alternating sum robustly even when individual cohomology dimensions change.

## Pushforward through a family

Now imagine Y is not a point. Over each y in Y, the fiber X over y may have a space of sections. Some fibers can have more sections than others; higher cohomology can also jump. If the higher direct images are bundles under suitable base-change hypotheses, we can work with their alternating K-theory class. Its Chern character lives on Y. The theorem predicts that class using characteristic data on X and geometric pushforward along the map.

We are not claiming every higher direct image is automatically a vector bundle or that cohomology commutes with every base change. Those conclusions need additional assumptions. The derived pushforward remains the right object even when the naive vector-bundle picture breaks down.

## Where this leads

The result links algebraic geometry to topology and differential geometry. A curvature calculation may represent a characteristic class; an intersection calculation may evaluate that class; an algebraic cohomology calculation may produce the same integer by an alternating sum. Grothendieck-Riemann-Roch explains why these answers belong to the same structure.

Notice how the previous ideas line up. Perfect complexes give finite derived objects. K-theory records their additive classes. The Chern character converts those classes into intersection-theoretic data. The Todd class corrects pushforward. Riemann-Roch is not merely a formula to memorize; it is a compatibility theorem connecting several kinds of mathematical measurement.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For a proper morphism `f:X -> Y` of smooth quasi-projective varieties over a field, with the relevant K-theory pushforward defined,
\[
\operatorname{ch}(f_![E])\operatorname{Td}(T_Y)
=f_*(\operatorname{ch}(E)\operatorname{Td}(T_X))
\quad\text{in }A^*(Y)_\mathbf Q,
\]
where `f_![E]=sum_i (-1)^i [R^if_*E]` in K-theory. A formulation using the virtual relative tangent bundle is `ch(f_!E)=f_*(ch(E) Td(T_f))` with the appropriate projection formula and orientations. Stating `ch(f_!E)=f_* ch(E)` alone is generally false.

For `X=P^1_k`, `H^2=0`, `integral_{P^1} H=1`, `c_1(T_{P^1})=2H`, and `Td(T_{P^1})=1+H`. Also `ch(O(d))=exp(dH)=1+dH`. Therefore
\[
\chi(\mathbf P^1,\mathcal O(d))=\int_{\mathbf P^1}(1+dH)(1+H)=d+1.
\]
For `d=-2`, `H^0=0`, `H^1` has dimension one, so `chi=-1`. Cohomology vanishing, not the GRR formula alone, converts an index into `h^0`.

The compact form presumes compatibility between the cycle-theoretic pushforward and K-theory pushforward; if using general schemes, perfectness, finite Tor dimension, and properness must be handled with the appropriate version of GRR.

### Exercises with answers

1. Evaluate `chi(P^1,O(3))`. **Answer:** four, because `d+1=4`.
2. Evaluate `chi(P^1,O(-4))`. **Answer:** minus three; it is not a negative dimension of global sections.
3. What is missing from a naive formula that commutes Chern character with pushforward? **Answer:** the Todd-class correction.
4. Why is derived pushforward used? **Answer:** pushforward of sheaves is not exact; higher direct images contribute to the K-theory index.

### Reading and source notes

- [Stacks Project, Grothendieck-Riemann-Roch](https://stacks.math.columbia.edu/tag/02UO), formula in a smooth proper setting.
- [Grothendieck, SGA 6, Expose 0](https://grothendiecksga.com/read/sga6/en/0.html), intersection-theoretic framework and pushforward.
- [Stacks Project, Perfect complexes](https://stacks.math.columbia.edu/tag/0656), relevant finite derived objects.
