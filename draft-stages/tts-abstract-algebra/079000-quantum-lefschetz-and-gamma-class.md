# 079000 - Quantum Lefschetz, Hypergeometric Periods, and Gamma Classes

**Track:** Abstract Algebra. **Background:** projective hypersurfaces, Gromov–Witten theory, quantum connections, and characteristic classes. **Central question:** how does the curve-counting theory of a hypersurface relate to the ambient projective space?

<!-- BEGIN SPOKEN LECTURE -->

# What happens to curves when we impose an equation?

Projective space contains many algebraic curves. Now cut out a hypersurface by setting a homogeneous polynomial equal to zero. Which of those curves lie in the hypersurface, and how many should be counted after allowing curves to degenerate?

Ordinary Lefschetz theorems compare the cohomology of a smooth hypersurface with that of its ambient space. Quantum Lefschetz asks for an analogous comparison of curve-counting invariants. It is much subtler. Curves must carry stable-map data, and the equation defining the hypersurface imposes conditions on sections along each map.

One consequence is a striking hypergeometric expression. The factorial patterns that arise from imposing the hypersurface equation become coefficients of solutions to quantum differential equations. For the quintic threefold in projective four-space, the first such coefficients are one hundred and twenty and one hundred and thirteen thousand four hundred. These numbers are not, by themselves, counts of rational curves. They are period coefficients that must be transformed before extracting enumerative information.

# Why a degree-five equation produces five factors

Take a smooth degree-five hypersurface in projective four-space. Its defining polynomial is a section of the line bundle called O of five. A stable map from a rational curve to projective space pulls that bundle back to a line bundle of degree five times the curve degree.

In a favorable genus-zero situation, imposing that the map land in the hypersurface amounts to the vanishing of the pulled-back defining section. Virtual intersection theory packages this constraint through an Euler class. In torus-equivariant or hypergeometric language, the Euler class introduces a product of factors indexed through five times the curve degree. The ambient projective-space contribution gives denominator factors repeated five times.

This contrast—five times the degree upstairs, five ambient coordinates downstairs—is visible in the quintic I-function. It is the source of the factorial ratios in the simplest coefficient calculation.

# Two coefficients that can be checked by hand

Ignore the cohomology variable for a moment and look only at the scalar hypergeometric period. The coefficient in degree d is the factorial of five d, divided by the fifth power of d factorial.

For degree one, that is five factorial, or one hundred and twenty. For degree two, it is ten factorial divided by two factorial raised to the fifth power, giving one hundred and thirteen thousand four hundred. The resulting series begins with one, then one hundred and twenty times q, then one hundred and thirteen thousand four hundred times q squared.

A power series with such large integer coefficients is not automatically an enumerative generating function. The mirror coordinate is not generally the naive q. A mirror map and a normalization relate the hypergeometric expression to the quantum connection and the actual Gromov–Witten invariants. One must also distinguish primary invariants, descendants, and the integrality transformations that appear when discussing counts of curves.

This is a place where casual exposition easily overclaims. One hundred and twenty is a period coefficient; it is not the number of lines on a generic quintic. The latter is a different, classical enumerative calculation.

# The Gamma class carries a different correction

The quantum connection does not only have formal power-series solutions. One can ask for a preferred integral structure on its solutions, linked to K-theory. Here the Gamma class appears.

For a vector bundle with formal Chern roots, its Gamma class is formed by multiplying values of the Gamma function at one plus each root, with the customary normalization choices understood. This construction mixes characteristic-class information with special values of the Riemann zeta function when expanded in cohomology.

For the quintic threefold, the tangent-bundle exact sequence comes from subtracting the normal bundle O of five from the ambient tangent bundle. In the resulting formal characteristic-class computation, the Gamma class has a ratio with five copies of Gamma at one plus the hyperplane class in the numerator, and Gamma at one plus five times that class in the denominator.

These are two related but distinct stories. Quantum Lefschetz modifies the ambient curve-counting series by the hypersurface constraint. The Gamma class corrects the comparison between quantum flat sections and integral K-theory data. Their coexistence matters in mirror symmetry, but they should not be merged into one unexplained factor.

# A warning about genus and positivity

The cleanest hypergeometric quantum Lefschetz picture concerns genus-zero theories under positivity or convexity assumptions suited to the chosen target and twisting bundle. In higher genus, a naive rule that simply inserts the same Euler factors generally fails. The virtual geometry of maps contains additional obstruction contributions.

Even in genus zero, saying that the I-function equals the J-function without qualification can miss a mirror change of variables and scalar normalization. A rigorous calculation records which twisting and equivariant conventions are used and what transformation identifies the hypergeometric series with the target's quantum data.

This distinction is not pedantic. A wrong identification can produce plausible-looking series with wrong coefficients or wrong enumerative interpretations. The method is powerful precisely because it provides a controlled way to transport information from the ambient space into the hypersurface.

# Three ways to read one formula

The same quintic hypergeometric series can be read geometrically, analytically, and arithmetically. Geometrically, the numerator encodes the hypersurface condition imposed along stable maps. Analytically, the resulting series solves a differential equation coming from periods and quantum connections. Arithmetically, its coefficients are explicit integers with strong divisibility properties.

The Gamma class adds a fourth reading, connecting characteristic classes and special functions to integral structures. None of these readings replaces the others. A good proof tracks the exact object being transported at each step: an Euler class, a cohomology-valued series, a flat section, or a K-theory class.

Quantum Lefschetz is therefore not simply a slogan that hypersurface invariants come from projective space. It is a disciplined method for imposing equations on families of maps while preserving the virtual multiplicities they carry. The hypergeometric products are the visible computational reward for doing that geometry carefully.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For the quintic `X_5 subset P^4`, a conventional genus-zero hypergeometric I-function has the form
\[
I(q,z)=e^{H\log q/z}\sum_{d\ge0}q^d\frac{\prod_{m=1}^{5d}(5H+mz)}{\prod_{m=1}^d(H+mz)^5},
\]
with `H` the ambient hyperplane class restricted to `X_5` and the usual empty-product convention. Setting `H=0,z=1` gives
\[
\Phi(q)=\sum_{d\ge0}\frac{(5d)!}{(d!)^5}q^d=1+120q+113400q^2+\cdots.
\]
The scalar series is **not** a direct curve count; mirror-map and normalization data intervene when matching I- and J-functions. Via `0 -> TX -> TP^4|_X -> O_X(5) -> 0`, the formal Gamma characteristic class is
\[
\widehat\Gamma(TX)=\frac{\Gamma(1+H)^5}{\Gamma(1+5H)}
\]
modulo the standard normalization/convention for Chern roots. Quantum Lefschetz and the Gamma integral structure are related but not identical constructions.

### Exercises with answers

1. Compute the scalar degree-one coefficient of the quintic period. **Answer:** `5! = 120`.
2. Compute the degree-two coefficient. **Answer:** `10!/(2!)^5=113400`.
3. Why does the degree-five hypersurface impose `5d` in the numerator? **Answer:** the pulled-back normal line bundle has degree `5d` on a degree-`d` genus-zero map.
4. Are scalar I-function coefficients counts of rational curves? **Answer:** Not directly; normalization, mirror coordinates, and enumerative transformations must be specified.

### Reading and source notes

- [Pandharipande, Rational Curves on Hypersurfaces (after Givental)](https://arxiv.org/abs/math/9806133), genus-zero hypergeometric construction.
- [Fan and Lee, Towards a Quantum Lefschetz Hyperplane Theorem in All Genera](https://doi.org/10.2140/gt.2019.23.493), limits of naive higher-genus transfer.
- [Iritani, Gamma Classes and Quantum Cohomology](https://arxiv.org/abs/2307.15938), quantum integral structures.
