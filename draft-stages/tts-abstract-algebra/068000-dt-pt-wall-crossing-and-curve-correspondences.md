# 068000 — DT/PT Wall Crossing: Two Ways to Count Curves

**Track:** Abstract Algebra. **Background:** ideal sheaves, moduli spaces, stable pairs, virtual counting, and Calabi–Yau threefolds. **Central question:** why can changing the stability condition change the objects being counted while leaving a predictable relation among their generating functions?

<!-- BEGIN SPOKEN LECTURE -->

# What exactly counts as a curve?

Imagine drawing a curve inside a three-dimensional complex variety. If the curve is smooth and isolated, there may be little ambiguity about the geometric object. But moduli theory cannot restrict attention to that comfortable setting. Curves can become singular, nonreduced, or disconnected. Zero-dimensional pieces can appear. Families can degenerate to schemes that have the same underlying set of points but quite different algebraic structures.

To count curves in a deformation-invariant way, a theory must specify what objects are allowed and how they behave in families. Donaldson–Thomas theory and Pandharipande–Thomas theory make different choices. The surprise is that, under the appropriate threefold assumptions, the resulting generating functions are related by a precise factorization.

In Donaldson–Thomas theory, the main rank-one objects are ideal sheaves of one-dimensional subschemes. The ideal sheaf remembers equations of a subscheme, including nilpotent structure and embedded points. It places the curve in a Hilbert scheme and lets deformation theory assign a virtual count even when the geometric moduli space has the wrong ordinary dimension.

In stable-pair theory, the object is a pure one-dimensional sheaf together with a section from the structure sheaf, whose cokernel is zero-dimensional. Purity forbids a zero-dimensional subsheaf of the curve sheaf. The section singles out a generically surjective presentation. This removes a particular source of embedded-point behavior without reducing the count to only smooth embedded curves.

# The smooth-curve example is completely visible

Take a smooth connected curve C inside a smooth threefold. The ideal sheaf of C is an ordinary Donaldson–Thomas-type object. The pair consisting of the structure sheaf of C and its unit section is a stable pair: the map is surjective, so its cokernel is zero.

Now allow a finite collection of marked points on C. These points define an effective divisor D. We can form the line bundle associated with D and use the canonical section whose zeros are D. The resulting sheaf and section form a stable pair. The length of D increases the Euler characteristic of the sheaf by exactly that length.

For the projective line, every degree-d effective divisor is parametrized by a projective space of dimension d. Thus even this elementary curve has a rich family of stable pairs, and the generating variable recording Euler characteristic sees the points added along the curve.

There is an essential qualification. Those projective spaces describe a smooth-curve stratum and a simple choice of sheaves. The virtual invariant of the ambient threefold is not automatically just the ordinary number of points in such a projective space. Deformations normal to C, obstruction theories, and multiplicities affect the enumerative count.

# Why there is a degree-zero factor

Ideal sheaves can account for zero-dimensional subschemes that are not part of the one-dimensional curve class. Consequently, Donaldson–Thomas generating series have contributions from ideal sheaves of pure points, even when the curve class is zero.

Stable pairs package zero-dimensional modifications differently, through the cokernel of a section of a pure one-dimensional sheaf. When changing from ideal sheaves to stable pairs, a universal degree-zero contribution must be separated from the curve-dependent part.

For a smooth projective Calabi–Yau threefold and the conventional numerical generating series, the DT/PT correspondence says that the series for rank-one Donaldson–Thomas invariants in a fixed curve class equals the degree-zero Donaldson–Thomas series multiplied by the corresponding stable-pair series. Equivalently, reduced Donaldson–Thomas theory, after dividing out that degree-zero factor, agrees with stable-pair theory.

This is an equality of virtual-counting generating series, not a literal bijection between ideal sheaves and stable pairs of matching Euler characteristic. One side can contain embedded points that have no direct counterpart as objects on the other side. The equality is produced by a wall-crossing mechanism in a category of complexes.

# Walls come from the notion of stability

Why should a change of moduli problem yield a controlled formula? A stability condition determines which objects are regarded as stable and therefore counted. As the stability parameter varies, some objects become unstable and others become stable. At a wall, an object can decompose into pieces of equal phase or slope. The formula for how invariants jump is governed by the algebra of extensions among those pieces.

For DT/PT, an ideal sheaf and a stable pair can be placed inside a common derived-category framework. Hall-algebra identities, or their categorical descendants, organize how moduli stacks of extensions factor. Passing from those identities to numerical invariants produces the degree-zero factor that separates the theories.

There is a useful mental model: we are not changing the geometry of the underlying threefold, but we are changing the bookkeeping rules for how curve and point contributions can assemble into an object. The change has a predictable cost, expressed by another generating series.

# What a formula does and does not imply

The DT/PT correspondence has a large range of applications, but hypotheses matter. In a projective Calabi–Yau threefold, symmetric obstruction theories provide zero-dimensional virtual counts. On noncompact toric threefolds one often uses equivariant residues. For a general threefold or a different stability theory, the same numerical formula may need modifications or may not apply in the stated form.

Furthermore, multiplying generating series is not the same as multiplying individual invariant numbers. The coefficient for one Euler characteristic is a convolution: many degree-zero and stable-pair coefficients can contribute. That is why a wall-crossing identity naturally looks simple in generating-function form even though its term-by-term consequences are intricate.

It is tempting to hear the phrase counting curves and picture each curve contributing one. Virtual counts do not work that way. Signs, automorphisms, obstruction spaces, and degenerations all play roles. The moduli problem makes the count precise, and the obstruction theory makes it deformation robust.

# Two windows on one enumerative problem

Ideal sheaves are good at retaining the full scheme-theoretic curve, including embedded zero-dimensional structure. Stable pairs make the one-dimensional support pure and record zero-dimensional information through a section. Hall-algebra wall crossing relates their different assemblies. The degree-zero DT factor is not extraneous decoration; it is the price of changing what counts as an admissible object.

For a smooth curve with marked points, these ideas are accessible through line bundles and divisors. For a general Calabi–Yau threefold, they are statements about derived moduli, virtual classes, and generating functions. The underlying principle is the same: one can change a counting theory's objects without losing control of the resulting invariants, provided the change is governed by a sufficiently rich algebra of extensions.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For a smooth projective Calabi–Yau threefold X and curve class beta, write `I_n(X,beta)` for the Hilbert scheme of one-dimensional subschemes Z (possibly with zero-dimensional components) satisfying `[Z]=beta` and `chi(O_Z)=n`. A PT stable pair is `(F,s:O_X -> F)` where F is a pure one-dimensional coherent sheaf, the support has class beta, `chi(F)=n`, and `coker s` is zero-dimensional.

For a fixed smooth curve C and an effective divisor D of length d, the pair `(O_C(D), s_D)` has `coker s_D=O_D` and `chi(O_C(D))=1-g(C)+d`. When `C=P^1`, the effective divisors of degree d form `Sym^d(P^1) ~= P^d`. This is a moduli-stratum observation, **not** by itself a virtual invariant computation.

Define series `DT_beta(q)=sum_n DT_{n,beta}q^n`, `PT_beta(q)=sum_n PT_{n,beta}q^n` and `DT_0(q)=sum_{k>=0}DT_{k,0}q^k`. In the smooth projective Calabi–Yau threefold DT/PT correspondence, with consistent counting conventions,
\[
 DT_\beta(q)=DT_0(q)\,PT_\beta(q),\quad
 DT_{n,\beta}=\sum_{k\ge0}DT_{k,0}\,PT_{n-k,\beta}.
\]
This is **not** a coefficientwise equality `DT_{n,beta}=PT_{n,beta}`. The identity is a derived Hall-algebra wall-crossing result; it was conjectured by Pandharipande and Thomas and proved in numerical form through work including Bridgeland and Toda.

### Exercises with answers

1. For a smooth genus-two curve C and divisor D of length three, calculate `chi(O_C(D))`. **Answer:** `1-2+3=2`.
2. For a stable pair, can F contain a nonzero zero-dimensional subsheaf? **Answer:** no; purity rules it out.
3. If `DT_0(q)=1+aq+...` and `PT_beta(q)=b_0+b_1q+...`, what is the q coefficient of DT? **Answer:** `b_1+ab_0`.
4. Does DT/PT identify individual ideal sheaves with individual stable pairs? **Answer:** no; it identifies virtual-counting series through a wall-crossing formula.

### Reading and source notes

- [A. T. Ricolfi, The DT/PT correspondence for smooth curves](https://link.springer.com/article/10.1007/s00209-017-2037-2), local curve counting and the generating-series identity.
- [Pădurariu and Toda, Categorical DT/PT correspondence and quasi-BPS categories](https://www.cambridge.org/core/journals/moduli/article/categorical-dtpt-correspondence-and-quasibps-categories-for-local-surfaces/F9BEF205512AEB842BB3C2A313FA36D0), categorical wall-crossing perspective.
- [The local motivic DT/PT correspondence](https://pmc.ncbi.nlm.nih.gov/articles/PMC8596886/), definitions and a discussion of local counting formulas.
