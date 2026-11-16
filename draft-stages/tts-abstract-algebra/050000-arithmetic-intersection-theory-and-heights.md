# 050000 — Arithmetic Intersection Theory: Heights and the Size of Rational Points

**Track:** Abstract Algebra. **Background:** number fields, divisors, line bundles, algebraic curves, intersection theory. **Central question:** what replaces a geometric intersection number when rational points have arithmetic size?

<!-- BEGIN SPOKEN LECTURE -->

# Coordinates have more than one kind of size

A rational point on a projective line can be written as a pair of integers, not both zero. But multiplying both entries by the same nonzero number does not change the point. So if we want to measure how complicated a rational point is, we need a size that does not depend on an arbitrary choice of coordinates.

Take a point represented by two relatively prime integers a and b. A natural answer is the logarithm of the larger absolute value. The point one over three has height log three. So does the projective point represented by two and six, because after dividing by their common factor it represents one and three. The height measures the arithmetic cost of specifying the point, not its distance from a chosen location in Euclidean space.

This elementary measure becomes a bridge to geometry. Divisors and line bundles let us define height functions on general projective varieties. Arithmetic intersection theory provides a way of understanding how those heights transform and how they behave in families.

## Why every absolute value matters

At first, rational numbers seem to have one absolute value: their usual magnitude. But number theory also has p-adic absolute values, one for each prime p. A rational number can be small in the ordinary sense and large with respect to a p-adic valuation, or conversely.

The product formula says that when we multiply the appropriately normalized absolute values of a nonzero rational number over all places, the answer is one. In logarithms, the sum is zero. This is exactly what makes a properly normalized projective height independent of multiplying the coordinates by a common rational scalar.

For a projective point with rational coordinates, we sum the logarithm of the largest coordinate absolute value at each place. For primitive integer coordinates, all the non-Archimedean contributions vanish, leaving our familiar logarithm of the largest integer magnitude. For a point over a number field, the same idea works with local weights and a normalization by field degree.

This definition may look like bookkeeping until we ask an arithmetic question: how many algebraic points can have bounded height? Northcott's finiteness theorem says that once we bound both height and degree over the rational numbers, only finitely many algebraic points remain. The degree restriction matters. Infinitely many roots of unity have bounded height, but their degrees can grow.

## From heights to line bundles

On an ordinary projective curve, a divisor records zeros and poles, with multiplicity. A line bundle turns this local information into a geometric object that can be pulled back and tensored. The degree of a line bundle measures the net divisor contribution.

In arithmetic geometry, a line bundle alone is not quite enough. We must also specify how to measure sections at the complex embeddings. This additional measurement is a metric. A line bundle equipped with suitable metrics is called a metrized line bundle. Its arithmetic degree combines contributions from finite primes and from the Archimedean places.

The need for both sorts of contributions is not an aesthetic choice. If we change a trivialization by multiplying by a rational function, its valuations shift at finite places and its ordinary absolute values shift at infinity. The product formula is what makes the total arithmetic degree invariant.

Consider a rational point on the projective line. It defines a section of the projection from the arithmetic projective line over the integers to its base. Pulling back the metrized hyperplane bundle gives an arithmetic degree. With standard normalizations, this degree recovers the logarithmic height of the point. The familiar quantity log three is therefore an arithmetic degree of a geometric line bundle.

## Intersection over an arithmetic base

On a surface over a field, intersecting two divisors produces a number. Over the spectrum of the integers, the geometric situation has an extra dimension. Intersections of horizontal and vertical divisors at finite primes contribute discrete terms, while complex embeddings contribute analytic corrections involving metrics and Green functions.

The full Arakelov intersection pairing combines these pieces. We should not picture it merely as counting where two curves meet. At infinity, an intersection has an analytic component. This allows arithmetic intersections to remain compatible with changes of rational sections and with the global product formula.

A good use of the theory is to compare arithmetic and geometric positivity. A line bundle may be ample in the geometric sense, but the heights it produces also depend on the chosen metrics, up to bounded changes in many common constructions. This gives a quantitative language for studying rational and integral points.

## A small calculation and a large principle

Compute the height of the rational projective point represented by twelve and eighteen. Divide by the greatest common divisor, six. We obtain two and three, so the logarithmic height is log three. The original coordinates had larger numbers, but their redundancy should not count. Now consider the squaring map on the projective line. It sends the point two to three to four to nine, so the height doubles: log nine equals twice log three. More generally, the standard height on the projective line scales approximately, and for this monomial example exactly, by the degree of the map.

That scaling is one reason heights are useful in arithmetic dynamics. If a rational map repeatedly raises arithmetic complexity, the height lets us quantify the growth. Arithmetic intersection theory gives the geometric infrastructure behind this apparently elementary observation.

The deeper lesson is that number theory has a geometry spanning all its places. A rational point has ordinary magnitude, p-adic information, and a projective equivalence relation. Height gathers those ingredients into one invariant. Arithmetic intersections explain why the invariant behaves like a geometric degree and why it can constrain the distribution of rational points.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For primitive `(a,b) in Z^2 \ {(0,0)}` define `h([a:b])=log max(|a|,|b|)`. Then `h([12:18])=h([2:3])=log 3`. Under `[a:b] -> [a^d:b^d]`, primitiveness is preserved and `h` becomes `d h` for positive integer `d`.

The absolute logarithmic Weil height on `P^n(K)` is
\[
h([x_0:\cdots:x_n])=\frac{1}{[K:\mathbb Q]}\sum_{v\in M_K} n_v\log\max_i |x_i|_v,
\]
for normalized local absolute values, local degrees `n_v`, and the product formula `sum_v n_v log|lambda|_v=0` for `lambda != 0`. The height does not depend on the choice of homogeneous coordinates or of field of definition. There are infinitely many degree-unbounded roots of unity of height zero, so Northcott finiteness requires a bound on field degree.

A metrized line bundle on an arithmetic curve has an arithmetic degree combining valuations of rational sections at finite places with negative logarithms of their metric norms at infinite places. For the standard metrized `O(1)` on `P^1_Z`, the arithmetic degree along a rational section agrees with the Weil height, subject to the stated metric convention.

The arithmetic intersection product on arithmetic surfaces also needs Green-current or metric contributions at Archimedean places. Do not conflate a literal number of intersection points with the full arithmetic pairing, and do not claim all heights on a fixed variety coincide exactly: changes of metrics and models can alter them by bounded terms under standard hypotheses.

### Exercises with answers

1. Find `h([35:14])`. **Answer:** `log 5`, since the primitive pair is `[5:2]`.
2. What is the standard height of `[2^4:3^4]`? **Answer:** `4 log 3`.
3. Why is degree boundedness required in Northcott's theorem? **Answer:** infinitely many roots of unity have height zero but increasing algebraic degrees.
4. Which principle cancels the effect of rescaling projective coordinates across places? **Answer:** the product formula.

### Reading and source notes

- [Bombieri and Gubler, Heights in Diophantine Geometry](https://doi.org/10.1017/CBO9780511542879), Weil heights, local contributions and height finiteness.
- [Arakelov Theory, Encyclopedia of Mathematics](https://encyclopediaofmath.org/wiki/Arakelov_theory), arithmetic intersections and Archimedean metrics.
- [The Stacks Project, Divisors](https://stacks.math.columbia.edu/download/divisors.pdf), geometric divisor and line-bundle background.
