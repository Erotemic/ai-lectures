# 061000 — Heights, Mordell–Weil, and Explicit Descent Algorithms

**Track:** Abstract Algebra. **Background:** elliptic curves, group laws, Galois cohomology, and Selmer groups. **Central question:** how can finite computations constrain an infinite group of rational points?

<!-- BEGIN SPOKEN LECTURE -->

# An infinite group, inspected with finite arithmetic

Take the equation y squared equals x cubed minus two. A rational solution is the point with coordinates three and five. Its reflected point, three and minus five, is another. The chord-and-tangent rule lets us combine these points and construct new rational points. We can even ask whether the first point has finite order, or whether repeated addition will produce infinitely many distinct points.

There is no obvious reason that such questions should be decided by finite calculations. Rational points have unbounded numerators and denominators. Checking a large box of possible fractions can find points, but failure to find another point is not proof that no such point exists. Explicit descent turns the infinite problem into controlled arithmetic in a finite collection of square classes, local fields, and covering curves.

The central achievement of the Mordell–Weil theorem is structural: for an elliptic curve over the rational numbers, the rational points form a finitely generated abelian group. Consequently there is a finite torsion subgroup and a free part with some nonnegative integer rank. The theorem does not hand us generators or the rank for a given curve. Descent helps produce the missing information.

# The tangent calculation is exact, not numerical evidence

On our example, consider the point three, five. The tangent slope is twenty-seven tenths. Doubling the point by the elliptic-curve group law gives a point whose x coordinate is one hundred twenty-nine over one hundred and whose y coordinate is negative three hundred eighty-three over one thousand.

Those denominators are an important feature, not a numerical inconvenience. They are the arithmetic footprint of repeated group operations on a curve. We can verify the resulting point by substitution into the cubic equation. What doubling does not tell us, on its own, is whether this process ever repeats.

For a curve with integral Weierstrass coefficients, the Nagell–Lutz theorem gives a powerful obstruction to an integral point being torsion. In this example the nonzero y coordinate is five, and its square does not divide the relevant discriminant quantity. Thus our point is not torsion. We have a concrete lower bound: the rank is at least one. But an infinite-order point does not prove the rank is exactly one; there might be other independent generators.

# The height measures arithmetic complexity

One way to avoid a fruitless search over fractions is to measure the size of a rational point. If the x coordinate is a reduced fraction with numerator a and denominator b, its logarithmic height is the logarithm of the larger of the absolute numerator and positive denominator. This simple function measures how complicated the rational coordinate has become.

On an elliptic curve, the naive height is corrected into the canonical height. The canonical height has the striking property that multiplying a point by an integer n multiplies its height by n squared. That quadratic rule makes the height into a positive-semidefinite quadratic form on rational points modulo torsion. It also allows a pairing of points, so independent points can be studied as an arithmetic lattice.

Height arguments help show finiteness when combined with a descent inequality. Roughly, if one knows the group modulo multiplication by two, every point can be represented as twice another point plus one of finitely many representatives. The height of the smaller point is approximately a quarter of the height of the original point, up to a controlled error. Iterating that reduction and invoking bounded-height finiteness is the mechanism behind the finite-generation proof.

# What two-descent actually computes

Now reduce the group modulo doubling. We are studying rational points up to the equivalence relation that two points differ by twice another rational point. The quotient is finite by Mordell–Weil, but finding it directly is difficult: we would have to know the rational points first.

The workaround is to pass through a cohomological group built from the two-torsion of the elliptic curve. Rational points determine cohomology classes through the Kummer map. To test whether a candidate class could arise from a rational point, examine it over the real numbers and over each p-adic field. The classes that pass all local tests form the two-Selmer group.

This is a computable finite group under standard algorithmic hypotheses. For an explicit model, local conditions reduce to solvability of associated covering curves in completions, supplemented by class-group and unit computations in number fields. Only finitely many primes require special treatment. The surviving Selmer classes yield an upper bound on the rational rank.

But there is a gap between locally soluble and globally soluble. A covering curve can have a point over every relevant completion and nevertheless have no rational point. The Tate–Shafarevich group records precisely this remaining obstruction in the exact sequence relating rational points modulo doubling to the two-Selmer group. Therefore a Selmer class is a candidate, not automatically a rational generator.

# A finite computation and its interpretation

Suppose a two-descent produces a Selmer group of dimension three as a vector space over the field of two elements, while the rational two-torsion has dimension one. Then the rank is at most two. To establish rank two, we still need two points proved independent, for example by a height pairing and a saturation argument. If we find only one independent point, the certified conclusion may remain that the rank is either one or two.

An upper bound from descent can become sharp after additional local tests, a four-descent, a Cassels–Tate pairing, or explicit investigation of covering curves. Rank lower bounds come from actual rational points. Rank upper bounds come from cohomological constraints. A complete answer must make the two meet and must also handle the index of the proposed generators.

This is why an algorithm may report a proven rank interval rather than one integer. The interval is honest mathematical information. A large point search alone, even with impressive computation, is not equivalent to a complete descent and saturation certificate.

# The constructive lesson

Explicit descent is a disciplined division of labor. Group laws construct examples. Heights control their complexity. Finite group computations constrain what classes are possible. Local solubility rules out impossible classes cheaply. Global rational points and height pairings give lower bounds and independence. Saturation addresses whether the points found generate the whole free group rather than a subgroup of finite index.

The curve y squared equals x cubed minus two makes this distinction vivid. We can write down one infinite-order point and its exact double immediately, but determining the entire Mordell–Weil group is a separate and deeper problem. Descent does not replace the infinite problem with a guess. It provides a chain of finite, checkable statements that progressively narrows the answer.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For `E: y^2=x^3-2`, `P=(3,5)` lies on E since `25=27-2`. With `a=0`, the tangent slope at P is `m=3x_P^2/(2y_P)=27/10`; hence
\[
x(2P)=m^2-2x_P=129/100,\qquad y(2P)=m(x_P-x(2P))-y_P=-383/1000.
\]
The integral short-Weierstrass discriminant is `Delta=-16(4a^3+27b^2)=-1728`. A nonzero integral torsion point on this model has `y^2 | (4a^3+27b^2)=108` by Nagell–Lutz; because `25` does not divide `108`, P has infinite order. This establishes `rank E(Q)>=1`, **not** an exact rank claim.

For an elliptic curve over Q, write `E(Q)=Z^r + E(Q)_tors` as an abstract group. The exact sequence for 2-descent is
\[
0\longrightarrow E(\mathbb Q)/2E(\mathbb Q)\longrightarrow \operatorname{Sel}^{(2)}(E/\mathbb Q)\longrightarrow \Sha(E/\mathbb Q)[2]\longrightarrow0.
\]
Thus `dim_F2 Sel2 = r + dim_F2 E(Q)[2] + dim_F2 Sha[2]`; in particular `r <= dim Sel2 - dim E(Q)[2]`. This is a *rank upper bound*, with no claim that every Selmer class is the image of a rational point. The logarithmic projective height of `x=a/b` in lowest terms is `h(x)=log max(|a|,|b|)`; the canonical height satisfies `hat h([n]P)=n^2 hat h(P)` and vanishes precisely on torsion over number fields.

### Exercises with answers

1. Verify that `2P` is on E. **Answer:** `(-383/1000)^2 = (129/100)^3-2 = 146689/1000000`.
2. What does a Selmer dimension of four and rational 2-torsion dimension two prove? **Answer:** `r<=2`; it does not by itself prove rank two.
3. Why are a height bound and finiteness of bounded-height rational points useful? **Answer:** descent reduces large points to smaller-height representatives, leaving only finitely many possibilities up to the finite quotient.
4. Why is an independent point search not a proof of rank maximality? **Answer:** it gives a lower bound but cannot exclude unseen generators or a nontrivial Tate–Shafarevich obstruction.

### Reading and source notes

- [Tom Fisher, Descent on elliptic curves](https://smf.emath.fr/node/152658), explicit Selmer groups and covering curves.
- [Magma Handbook, Mordell–Weil Groups and Descent Methods](https://docs.magma-maths.org/v2.30-1/ArithmeticGeometry/EllipticCurvesOverQAndNumberFields/mordell-weil.html), rank bounds, higher descents and generators.
- [J. S. Milne, Arithmetic Duality Theorems](https://www.jmilne.org/math/Books/ADTnot.pdf), cohomological background and local–global obstruction groups.
