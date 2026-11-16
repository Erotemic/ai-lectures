# 024000 — Elliptic Index and the Atiyah-Singer Perspective

**Track:** Topology and Geometry. **Background:** Hodge theory, de Rham cohomology, elliptic operators, characteristic classes. **Central question:** why can the difference between dimensions of solution spaces be computed using topology?

<!-- BEGIN SPOKEN LECTURE -->

# The solutions that survive every deformation

A differential equation may have no solution, one solution, or a whole space of solutions. If we change the coefficients slightly, the number of solutions can jump. Yet certain differences between dimensions remain stable. The index of an elliptic operator is one of the most important of these stable quantities.

Take an operator between two spaces of sections of vector bundles on a compact manifold. Its kernel consists of solutions to the homogeneous equation. Its cokernel measures which right-hand sides cannot be achieved. When the operator is elliptic and we use suitable function spaces, both dimensions are finite. The index is the dimension of the kernel minus the dimension of the cokernel.

Why subtract the dimensions rather than count solutions alone? Because a perturbation can create or destroy matching pairs of kernel and cokernel directions while preserving the difference. The index captures a robust feature that does not depend on every analytic detail.

## Ellipticity as a condition on high frequencies

A differential operator has a principal symbol, obtained from its highest-order derivatives by replacing differentiation with multiplication by a frequency vector. For a first-order operator, the principal symbol is linear in that frequency. Ellipticity means the symbol is invertible at every nonzero cotangent vector for an operator of equal-rank bundles, or an appropriate exactness condition for elliptic complexes.

This requirement prevents solutions from oscillating arbitrarily in invisible directions. It supplies estimates that make the operator Fredholm on suitable Sobolev spaces when the manifold is compact without boundary. Boundary-value problems need boundary conditions of the proper elliptic type; we will not silently include arbitrary boundaries.

The index is insensitive to continuous deformations through Fredholm operators. That stability suggests a topological formula because homotopy-invariant data can be built from the operator's principal symbol.

## The de Rham operator as a test case

We can see the principle without invoking the full Atiyah-Singer theorem. On a closed oriented Riemannian manifold, take the exterior derivative and its formal adjoint. Combine them into an operator that maps even-degree differential forms to odd-degree forms. This is the even-to-odd part of d plus d adjoint.

Hodge theory says the harmonic forms represent de Rham cohomology. The kernel of the even-to-odd operator consists of even-degree harmonic forms. Its cokernel corresponds to the odd-degree harmonic forms. Therefore its index is the alternating sum of Betti numbers: the Euler characteristic.

On the two-sphere, the zero-degree and top-degree cohomology groups are one-dimensional and the first cohomology vanishes. The index is two. On the torus, the Betti numbers are one, two, and one; the index is zero. These are the same Euler characteristics we obtained from Morse critical points, now computed as an analytic index.

The equality reveals a deeper connection. Morse theory uses critical points and gradient flow. Hodge theory uses harmonic solutions of an elliptic equation. Both recover the Euler characteristic. They arrive by very different routes, but topology forces the same invariant to appear.

## The Atiyah-Singer theorem

The general Atiyah-Singer index theorem states that the analytic index of an elliptic operator on a closed smooth manifold equals a topological index determined by the symbol class. The topological side is expressed through K-theory and characteristic classes, with appropriate orientations and pushforwards.

The statement is broader than an equation involving only the Euler characteristic. Different operators lead to different indices. The signature operator on an oriented manifold of dimension divisible by four has index equal to the signature of the intersection pairing. On a spin manifold, the index of the spin Dirac operator is expressed by the A-hat genus.

The particular characteristic class depends on the operator. Replacing every index formula by the same Todd class would be wrong. Complex, spin, and signature orientations each carry their own structures.

A useful analogy is a balance sheet. Analysis counts actual solutions and constraints. Topology computes a net balance without solving the equations individually. The theorem says those two balances agree because they are descriptions of the same Fredholm class.

## What index theory does not tell us

A zero index does not mean the kernel is zero. It can mean kernel and cokernel have equal positive dimensions. A nonzero index gives a lower bound on at least one of those dimensions and can obstruct invertibility, but it does not list the solutions.

Similarly, index stability requires that we remain inside a Fredholm family. If ellipticity fails, the manifold becomes noncompact without control, or boundary conditions change improperly, finite-dimensional kernel and cokernel need not survive.

Index theory is therefore a theorem about robust analytic structure, not a substitute for checking hypotheses. It ties together the derived and K-theoretic ideas of algebra, the characteristic classes of geometry, and the PDE estimates of analysis. This synthesis is why an index can be computed without ever solving the operator's differential equation explicitly.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For a Fredholm operator `D:H_1->H_2` between Hilbert spaces, `ind(D)=dim ker(D)-dim coker(D)`. On a closed smooth manifold, an elliptic differential operator between smooth vector bundles gives a Fredholm map between appropriate Sobolev spaces. Its index depends only on its elliptic symbol class under continuous homotopy. The Atiyah-Singer theorem equates this analytic index with a topological pushforward in K-theory.

For a closed oriented Riemannian manifold M, define `D_even=(d+d^*)|_{Omega^even}:Omega^even->Omega^odd`. It is elliptic. Its adjoint is the odd-to-even restriction. By Hodge theory,
\[
\operatorname{ind}(D_{even})=\sum_{k=0}^{\dim M}(-1)^k\dim H^k_{dR}(M)=\chi(M).
\]
For `S^2` the Betti numbers are `(1,0,1)` and index is 2. For `T^2` they are `(1,2,1)` and index is 0. The standard self-adjoint scalar Laplacian, viewed as an operator from a Sobolev space to a lower-order Sobolev space, has index zero; it is not the even-to-odd de Rham operator.

The index of a spin Dirac operator on a closed spin manifold is the A-hat genus, while the signature operator gives the signature on closed oriented manifolds of dimension divisible by four. These require distinct geometric hypotheses and symbol classes. Index zero does not imply invertibility.

### Exercises with answers

1. An operator has a two-dimensional kernel and five-dimensional cokernel. What is its index? **Answer:** minus three.
2. What is the de Rham operator's index on a genus-g closed oriented surface? **Answer:** Euler characteristic `2-2g`.
3. Does an index-zero elliptic operator have to be invertible? **Answer:** no; both kernel and cokernel may be nonzero and equal-dimensional.
4. Why are boundary conditions relevant? **Answer:** ellipticity of the interior symbol alone does not guarantee a Fredholm boundary-value problem.

### Reading and source notes

- [Atiyah and Singer, The Index of Elliptic Operators I](https://doi.org/10.2307/1970715), original theorem.
- [Berline, Getzler and Vergne, Heat Kernels and Dirac Operators](https://link.springer.com/book/10.1007/978-3-642-58088-8), analytic index methods.
- [University of Cologne, Introduction to the Atiyah-Singer Index Theorem](https://www.mi.uni-koeln.de/~bxliu/Lecture2025IndexTheory/IndexTheory2025UzK.pdf), background on elliptic operators and K-theory.
