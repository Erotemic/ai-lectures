# 018400 — The Chern Character: Why Exponentials Connect Bundles to Cohomology

**Track:** Topology and Geometry. **Background:** Chern classes, tensor products, rational cohomology. **Central question:** how do multiplicative bundle data become additive cohomology classes?

<!-- BEGIN SPOKEN LECTURE -->

# The Chern Character: Why Exponentials Connect Bundles to Cohomology

There are two natural ways to combine complex vector bundles. We can take a direct sum, which adds ranks, or a tensor product, which multiplies ranks. Characteristic classes are especially effective at recognizing the global twisting, but their formulas for these two operations do not always look simple. The Chern character is designed to make both operations behave naturally.

To see its construction, we begin with line bundles. For a complex line bundle L, its first Chern class is an integral class of degree two. Tensoring lines adds that class. If we want tensor product to become multiplication, we should look for a function that turns sums into products. The exponential function does precisely that.

## The exponential of a two-dimensional class

Write x for the first Chern class of L. Define the Chern character of L as the formal exponential of x: one plus x plus one-half x squared plus one-sixth x cubed, and so on. On any finite-dimensional manifold, only finitely many terms can survive because powers in degrees above the dimension vanish.

Suppose M is another line with first Chern class y. The tensor product has first Chern class x plus y. Therefore its Chern character is the exponential of x plus y, equal to the exponential of x times the exponential of y. Tensor products of lines have become ordinary multiplication of cohomology classes.

What about direct sums? We declare the Chern character of a direct sum to be the sum of the characters. For a general bundle, the splitting principle allows us to work formally as if the bundle decomposed into line bundles after pulling back to a suitable space. If x one through x r are its formal Chern roots, the character is the sum of their exponentials.

The degree-zero component is the rank. The degree-two component is the first Chern class. The degree-four component is one-half the square of the first Chern class minus twice the second Chern class. Already at this stage, rational coefficients appear. The Chern character does not usually land in integral cohomology.

## A calculation on the sphere

Take the complex projective line, which is a two-sphere, with positive generator h in second cohomology. The degree-positive line L has first Chern class h. Since the sphere has no degree-four cohomology, h squared vanishes. Its Chern character is just one plus h.

Now subtract the trivial line in K-theory. The reduced class beta equals L minus one. The Chern character of beta is h. Thus the rank-zero K-theory generator maps to the degree-two cohomology generator. This explains why our sphere computation looked so much like ordinary cohomology.

On more complicated spaces, Chern character is still an isomorphism after tensoring K-theory with the rational numbers, with the appropriate even or odd grading. This is a deep structural fact. It does not mean integral K-theory and integral cohomology are identical: torsion information can be lost when rationalizing.

## A calculation on the projective plane

The complex projective plane has a degree-two cohomology class h whose square is nonzero and integrates to one. For the line L with first Chern class h, the character is one plus h plus one-half h squared. The fraction is not a defect in the calculation; it is built into the exponential.

Now form the reduced K class L minus one. Its character is h plus one-half h squared. The square of that reduced class has character h squared, because all higher terms are too high in degree. There is no contradiction with the sphere relation beta squared equals zero: on the complex projective plane, a degree-four cohomology class actually exists.

The exponential creates a bridge between the algebra of bundles and the cup-product structure of cohomology, but the bridge has rational coefficients. This will matter when calculating indices, which must come out as integers even though intermediate characteristic-class expressions contain fractions.

## Curvature and normalizations

If a Hermitian vector bundle carries a unitary connection with curvature F, Chern–Weil theory represents the Chern character in differential forms using the matrix exponential of a normalized curvature matrix. The precise factor of the imaginary unit and two pi depends on whether one writes the curvature as a skew-Hermitian matrix or a real-valued two-form for a line bundle.

For a line bundle of first Chern number one over a sphere, the normalized curvature integrates to one. Its exponential contains a constant term and a degree-two term. On the sphere, only the degree-two term contributes to the integral. This is the same Chern character we calculated topologically.

Yet a curvature form cannot detect torsion Chern classes after passing to real cohomology. Differential forms and rational characteristic classes give a powerful part of the story, not every integral detail.

## Why the index formula needs another factor

A tempting guess is that the index of a Dolbeault operator twisted by L equals the integral of the Chern character of L. But on a complex curve, integrating just the first Chern class would give the degree k for a line of degree k. The actual holomorphic Euler characteristic of a line on the projective line is k plus one.

The missing one comes from the geometry of the tangent bundle and is encoded by the Todd class. The general Riemann–Roch formula contains Chern character times Todd class. We can already see why a correction is necessary: a bundle does not live alone; the elliptic operator also depends on the manifold and its tangent directions.

The Chern character is therefore not simply a new notation for Chern classes. It is the map that carries stable vector-bundle arithmetic into cohomological arithmetic in the form suited to index theory, while exposing exactly where rational coefficients and tangent-bundle correction terms enter.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For a complex bundle E with formal Chern roots `x_i`,

\[
\operatorname{ch}(E)=\sum_i e^{x_i}
=\operatorname{rank}(E)+c_1(E)
+\tfrac12(c_1(E)^2-2c_2(E))+\cdots.
\]

Extend by `ch([E]-[F])=ch(E)-ch(F)`. It satisfies `ch(E⊕F)=ch(E)+ch(F)` and `ch(E⊗F)=ch(E)ch(F)`. On `CP²` with `h=c_1(O(1))`, `∫h²=1`, the truncation is `ch(O(1))=1+h+h²/2`. The Chern character induces a natural isomorphism `K^0(X)⊗Q ≅ H^{even}(X;Q)` for finite CW complexes (and `K^{-1}(X)⊗Q ≅ H^{odd}(X;Q)`). Rationalization may annihilate torsion.

### Exercises with answers

1. Compute `ch(O(2))` on `CP¹`. **Answer:** `1+2h`.
2. Compute `ch([O(1)]-[1])` on `CP²`. **Answer:** `h+h²/2`.
3. Can a torsion K-theory class have nonzero rational Chern character? **Answer:** no.
4. Does the integral of `ch(O(k))` alone always equal the holomorphic Euler characteristic on `CP¹`? **Answer:** no; the Todd class contributes the extra one.

### Sources and further reading

- Allen Hatcher, [Vector Bundles and K-Theory](https://pi.math.cornell.edu/~hatcher/VBKT/VBpage.html), Sections on Chern classes and K-theory.
- [Chern character](https://en.wikipedia.org/wiki/Chern_character); [Splitting principle](https://en.wikipedia.org/wiki/Splitting_principle).
