# 011100 - Integration over Cycles and the de Rham Map

**Track:** Topology and Geometry. **Background:** smooth singular chains, boundaries, exterior derivatives, Stokes' theorem. **Question:** how does a differential form detect topological cycles?

<!-- BEGIN SPOKEN LECTURE -->

# Integration over Cycles and the de Rham Map

Suppose you are given a smooth closed curve on a manifold. One question is whether the curve encloses a region inside that manifold. Another question is whether a closed one-form accumulates a nonzero integral when evaluated along the curve. These questions turn out to be linked by Stokes' theorem.

Homology studies cycles modulo boundaries. De Rham cohomology studies closed differential forms modulo exact forms. Integration provides a natural way for the two theories to speak to each other. We will build that relationship carefully, beginning with actual parametrized pieces rather than treating a cycle as a picture of a hole.

## Chains are formal sums of parametrized pieces

A smooth singular one-simplex is a smooth map from a standard interval into the manifold. It can trace an edge, a curved route, or a constant path. A one-chain is a finite formal linear combination of such maps with coefficients, often integers or real numbers. Its boundary is a signed sum of endpoints. When the signed endpoints cancel, the chain is a cycle.

A two-simplex is a map from a filled triangle. Its boundary is the alternating sum of its three oriented edges. A two-chain is a formal sum of these parametrized triangles. Its boundary is a one-chain. The algebraic rule that the boundary of a boundary is zero is a consequence of pairwise cancellation of oriented faces.

A closed path is a basic one-cycle, but not every cycle is presented as one simple loop. A cycle may have many pieces, self-intersections, and coefficients. This algebraic flexibility is useful: it lets homology behave well under subdivision and gluing.

## Integrating a form over a chain

Let omega be a one-form, and let sigma be a smooth parametrized one-simplex. Pull omega back along sigma to the interval and integrate there. For a chain consisting of several simplexes, multiply each integral by its coefficient and add them. A k-form can be integrated in the same way over a smooth k-chain, by pulling it back to each standard k-simplex.

This definition needs the form to have the same degree as the dimension of the chain. Integrating a two-form over a curve is not a standard differential-form integral: there are not enough independent tangent directions. To pair a two-form with a two-cycle, use a surface-like chain.

The result is linear in both the form and the chain. If you double a cycle with its coefficient, you double the integral. If you reverse orientation, you change the sign. The construction is a pairing, not yet a pairing on homology and cohomology classes. For it to descend to classes, we need to check what happens when we change a chain by a boundary or a form by an exact form.

## Why closed forms ignore boundaries

Let omega be a closed k-form, meaning d omega equals zero. Suppose a k-cycle z is the boundary of a k-plus-one-chain C. Integrating omega over z gives, by Stokes, the integral of d omega over C. Because d omega is zero, the result is zero. Thus closed forms have zero integral on boundaries, and their integrals depend only on the homology class of the cycle.

Now suppose the form is exact: omega equals d eta. Integrate over any k-cycle z. Stokes converts the integral to that of eta over the boundary of z, which is zero by the definition of cycle. So exact forms contribute zero to every cycle integral. The integral therefore depends only on the de Rham cohomology class of the form.

Together these statements show that integration gives a well-defined number from a cohomology class and a homology class of matching degree. This is the de Rham pairing.

## A calculation on the circle

Write the unit circle using an angle coordinate that increases once around the circle. There is a globally defined angular one-form, even though there is no global real-valued angle function. Normalize the form by dividing it by two pi. Its integral around one counterclockwise circuit is one. Around a path that winds twice it is two. Around the same circuit clockwise it is negative one.

This tells us something that neither a local derivative nor a single chart makes visible. The one-form measures the homology class of the loop, and indeed its integer winding number for loops of the circle. Although the form itself has real coefficients, these particular normalized periods on integral one-cycles are integers.

If we change the form by adding the differential of a globally defined smooth function, its integral around a closed loop is unchanged. And if we alter the cycle by adding the boundary of a two-chain, its integral is unchanged. The number belongs to the pair of classes, not to arbitrary representatives.

## Detecting a two-dimensional cycle

Consider the two-dimensional torus formed by identifying opposite edges of a square. There is a closed two-form representing oriented area. Normalize it so its integral over the torus is one. Because the torus is a closed oriented surface, it has a fundamental two-cycle. The integral of the normalized area form over that cycle is one.

The two-form cannot be exact. If it were the derivative of a one-form, Stokes on the entire torus, which has no boundary, would force its integral to vanish. This is a concrete way to exhibit a nonzero second de Rham cohomology class. The calculation depends on orientation and normalization, but the nonvanishing is a topological fact.

## What the de Rham map asserts

Integration is more than a source of examples. It assigns to a closed k-form a real-valued functional on k-dimensional singular homology. Under the standard comparison between smooth singular homology and ordinary singular homology, this produces a singular cohomology class with real coefficients. The de Rham theorem says this map from de Rham cohomology to singular cohomology over the real numbers is an isomorphism for smooth manifolds.

This is a strong result. It says that every real singular cohomology class comes from a closed differential form, and that a closed form whose class has zero integrals against all real homology classes represents zero de Rham cohomology. The statement does not say that every integer cohomology class is the de Rham class of an arbitrary differential form with some preferred integer coefficients. Real forms do not directly encode torsion classes, because torsion vanishes upon passage to real coefficients.

We have justified why integration descends to cohomology and homology. The full proof of the isomorphism needs more machinery, such as local exactness and a method for gluing local comparisons. The Poincare lemma and partitions of unity supply precisely those ingredients. It is valuable to distinguish constructing the map from proving that the map is an isomorphism.

## Why this bridge matters

A topological cycle may be difficult to see geometrically in a complicated manifold. A differential form can give a quantitative witness that the cycle is not a boundary: if a closed form integrates to a nonzero number over it, the cycle cannot bound. Conversely, differential forms allow us to describe classes using derivatives, coordinates and integrals rather than only combinatorial chains.

This is the deeper reason the theories fit together. The boundary operator on chains and the exterior derivative on forms are dual through integration. Stokes is the compatibility relation. Once we pass to classes, calculus and topology become two descriptions of the same real-valued invariants.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For a smooth singular \(k\)-simplex \(\sigma:\Delta^k\to M\), define \(I_\omega(\sigma)=\int_{\Delta^k}\sigma^*\omega\), and extend linearly over finite chains. Stokes gives
\[I_{d\eta}(c)=I_\eta(\partial c).\]
If \(d\omega=0\), then \(I_\omega(\partial b)=0\); if \(c\) is a cycle, then \(I_{d\eta}(c)=0\). Thus
\[H^k_{\mathrm{dR}}(M)\times H_k(M;\mathbb R)\longrightarrow\mathbb R,\quad([\omega],[c])\mapsto\int_c\omega.\]
The de Rham isomorphism is \(H^k_{\mathrm{dR}}(M)\cong H^k_{\mathrm{sing}}(M;\mathbb R)\) for smooth manifolds; its construction uses the smooth-chain comparison. Over real coefficients, the universal coefficient theorem identifies singular cohomology with \(\operatorname{Hom}_{\mathbb R}(H_k(M;\mathbb R),\mathbb R)\).

On \(S^1\) with \(\eta=\frac1{2\pi}d\theta\) understood as a global one-form, \(\int_{S^1}\eta=1\). On \(T^2\) with angular coordinates modulo \(2\pi\), \(\omega=(2\pi)^{-2}d\theta\wedge d\phi\) integrates to one over the positively oriented fundamental cycle.

### Check your understanding

1. If \(d\omega=0\) and \(z=\partial C\), what is \(\int_z\omega\)? **Answer:** zero.
2. If \(\omega=d\eta\) and \(\partial z=0\), what is \(\int_z\omega\)? **Answer:** zero.
3. Can an ordinary real-valued de Rham pairing detect torsion homology classes? **No:** torsion classes vanish after tensoring with \(\mathbb R\).

### Reading and sources

- Allen Hatcher, [Algebraic Topology](https://pi.math.cornell.edu/~hatcher/AT/ATchapters.html), singular chains, homology and cohomology.
- Dietmar Salamon, [Differential Topology](https://people.math.ethz.ch/~salamon/PREPRINTS/difftop.pdf), de Rham theorem and cycle pairings.
- Overview: [De Rham theorem](https://en.wikipedia.org/wiki/De_Rham_cohomology#De_Rham%27s_theorem).
