# 030500 - Computing the Spin-C Dirac Index on a Four-Manifold

**Track:** Topology and Geometry. **Background:** characteristic classes, signature, spin-C determinant line, chiral Dirac operator, analytic index. **Central question:** how can a spinor equation's analytic index be computed from topology before solving the equation?

<!-- BEGIN SPOKEN LECTURE -->

# Computing the Spin-C Dirac Index on a Four-Manifold

A Dirac equation on a closed manifold may have an unknown number of solutions. But when the manifold is even-dimensional, the positive-to-negative chirality Dirac operator has an index: the dimension of its kernel minus the dimension of the kernel of its formal adjoint. That difference is stable under smooth deformations of the operator's coefficients and can often be computed without solving the equation.

In four dimensions, the spin-C Dirac index has a strikingly compact formula. It depends on the first Chern class of the determinant line and the signature of the four-manifold. Understanding what those two quantities mean is more valuable than memorizing a fraction with an eight in the denominator.

## The determinant line records the twist

A spin-C structure comes with a determinant line bundle. Its first Chern class is an integral second cohomology class. Geometrically, that class can be measured by integrating the line's curvature over oriented two-dimensional cycles, with the correct normalization.

On a four-manifold, a second cohomology class can be multiplied with itself using the cup product. Evaluating the resulting fourth-degree class on the fundamental cycle gives an integer: the self-intersection number of the class. This is the square of the determinant line's first Chern class.

That square is not an ordinary square of a number obtained by integrating over one particular surface. It is the intersection pairing on second cohomology. The pairing also has a signature: the number of positive directions minus the number of negative directions after extending the form to the real numbers and ignoring zero directions as appropriate. For a closed oriented four-manifold, this signature is a topological invariant.

## How the index theorem combines them

The Atiyah-Singer theorem for a spin-C Dirac operator says that its index is obtained by integrating a characteristic-class expression, the A-hat class multiplied by the exponential of half the determinant first Chern class.

In real dimension four, only degree-four terms contribute to the integral. The exponential contributes one eighth of the Chern-class square. The A-hat class contributes minus one twenty-fourth of the first Pontryagin class. The signature theorem identifies the Pontryagin number with three times the signature. Substituting gives the answer: the determinant Chern-class square minus the signature, all divided by eight.

This gives a consistency test. The result must be an integer, because it is an analytic Fredholm index. The parity condition on the determinant line, inherited from the spin-C structure, is precisely what makes the numerator divisible by eight in the required topological setting.

## Calculate the complex projective plane

The complex projective plane has a second cohomology generator conventionally called h. Its self-intersection is one. The signature is one. The complex tangent bundle has first Chern class three times h, and the canonical spin-C structure associated with the complex structure has determinant line with that same first Chern class.

Square three times h using the intersection pairing and obtain nine. Subtract the signature, one, to get eight. Divide by eight. The index is one.

That integer can also be understood through complex geometry. For the canonical complex spin-C structure, the Dirac operator is related to the Dolbeault operator and its adjoint. Its index is the holomorphic Euler characteristic. For the complex projective plane, this is one. Two very different languages agree on the same answer.

## Twisting changes the index predictably

Suppose we twist a spin-C structure by a complex line bundle with first Chern class q. The determinant first Chern class changes by twice q, not just q. This reflects the square in the determinant character of the spin-C group.

Substitute the new first Chern class into the formula. The index change is a combination of the original Chern class paired with q and the self-intersection of q, divided by two in the resulting expansion. The point is that changing the line twist changes the index by a calculable integer. We can check the change entirely in cohomology.

## An index does not count every solution

If the index is one, it does not mean there is exactly one Dirac zero mode. The kernel might have dimension five and the cokernel four, or the kernel one and the cokernel zero. The index records their difference, not their individual values.

For a nonlinear monopole equation, the expected dimension of the solution moduli space includes more than the chiral Dirac index. We must also account for the curvature equation, the gauge group, and real versus complex dimensions. That is why a Fredholm index calculation is a component of moduli-space analysis, not the final answer about solutions.

This lecture's payoff is a repeatable method: specify the correct elliptic operator, identify its bundle and topological twisting, expand the index characteristic class to the manifold's dimension, and calculate the relevant intersection numbers. We will next return to the other half of moduli-space theory: linearized equations and gauge symmetries.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Let \(X\) be a closed oriented smooth four-manifold with spin-C structure \(\mathfrak s\), determinant line \(L\), and \(c=c_1(L)\in H^2(X;\mathbb Z)\). The chiral Dirac index is
\[\operatorname{ind}_{\mathbb C}(D_A^+)=\langle e^{c/2}\,\widehat A(TX),[X]\rangle
=\frac{\langle c^2,[X]\rangle-\sigma(X)}8.\]
Here \(\widehat A=1-\tfrac1{24}p_1+\cdots\), and the Hirzebruch signature theorem gives \(\langle p_1,[X]\rangle=3\sigma(X)\). The class \(c\) is characteristic: \(c\bmod2=w_2(TX)\); its characteristic congruence implies \(c^2\equiv\sigma(X)\pmod8\).

For \(X=\mathbb{CP}^2\), write \(h\in H^2(X;\mathbb Z)\), \(\langle h^2,[X]\rangle=1\), \(\sigma(X)=1\), and the canonical complex spin-C determinant \(c=3h\). Then \(\operatorname{ind}_\mathbb C D_A^+=(9-1)/8=1\). Twisting by \(Q\) with \(q=c_1(Q)\) sends \(c\mapsto c+2q\) and changes the index by \(\langle cq+q^2,[X]\rangle/2\), obtained by expanding \(((c+2q)^2-c^2)/8\). This is an integer because the characteristic-class congruence implies \(cq\equiv q^2\pmod 2\). This is the spin-C Dirac index, not the de Rham parity index \(\chi(X)\).

### Exercises with answers

1. **Four-dimensional term.** Which terms of \(e^{c/2}\widehat A\) contribute to the index integral on a four-manifold? **Answer:** the degree-four terms \(c^2/8-p_1/24\).
2. **Projective plane.** For \(c=3h\), \(h^2=1\), and \(\sigma=1\), compute the index. **Answer:** one.
3. **Kernel.** Does index one force a one-dimensional kernel? **Answer:** no; kernel dimension minus cokernel dimension equals one.
4. **Twist.** If a spin-C structure is twisted by a line bundle with class \(q\), what happens to the determinant class? **Answer:** \(c\) becomes \(c+2q\).

### Sources and further reading

- Tim Perutz, [Basics of Seiberg-Witten Theory](https://www.imperial.ac.uk/media/imperial-college/research-centres-and-groups/geometry/junior-geometry-seminar/Seiberg-Witten-theory.pdf).
- Liviu Nicolaescu, [Notes on Seiberg-Witten Theory](https://www3.nd.edu/~lnicolae/new1.pdf), Dirac index and characteristic classes.
- Overviews: [Atiyah-Singer index theorem](https://en.wikipedia.org/wiki/Atiyah%E2%80%93Singer_index_theorem), [Signature (topology)](https://en.wikipedia.org/wiki/Signature_(topology)), [Spin-C structure](https://en.wikipedia.org/wiki/Spinc_structure).
