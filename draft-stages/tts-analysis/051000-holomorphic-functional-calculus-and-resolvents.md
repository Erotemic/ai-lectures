# 051000 — Holomorphic Functional Calculus: Cauchy's Formula for Operators

**Track:** Analysis from First Principles. **Background:** Complex contour integrals, resolvents, spectra, and matrices. **Question:** How can contour integration define functions even of non-self-adjoint operators?

<!-- BEGIN SPOKEN LECTURE -->

# Holomorphic Functional Calculus: Cauchy's Formula for Operators

There is another road from scalar functions to operator functions, and it begins in complex analysis rather than in the spectral theorem for self-adjoint operators. The key idea is Cauchy's integral formula. An analytic function inside a closed contour can be reconstructed from its values along the contour, with a reciprocal factor that measures distance from the evaluation point.

If we replace the scalar point by a bounded operator, the reciprocal becomes the resolvent: the inverse of z times the identity minus the operator. Integrating that resolvent around a contour surrounding the spectrum defines a function of the operator.

This method matters because it works for general bounded operators, not just self-adjoint ones. Its price is a stronger requirement on the scalar function: it must be holomorphic on an open neighborhood of the spectrum.

## Recall the scalar formula

For a complex number a lying inside a positively oriented contour, Cauchy's formula expresses f of a as a contour integral of f of z divided by z minus a. The denominator becomes large near a, but the contour stays away from that point. The integral combines the function's boundary values into its interior value.

Now take a bounded operator T on a complex Banach space. For z outside the spectrum, the operator z times the identity minus T is invertible. Its inverse is the resolvent. As long as our contour stays in the resolvent set, the resolvent varies continuously along it and the operator-valued integral makes sense.

We define f of T by taking one over two pi i times the contour integral of f of z multiplied by the resolvent. The contour must surround the spectrum within a region where f is holomorphic. Different admissible contours give the same result by the operator-valued version of Cauchy's theorem.

This is called the holomorphic, or Riesz–Dunford, functional calculus.

## Why it agrees with polynomials

An unfamiliar definition should pass familiar tests. If f is the constant one, the integral gives the identity operator. If f of z equals z, it gives T. If f is a polynomial, it gives the polynomial evaluated at T in the usual algebraic way.

One way to see the polynomial case is to choose a sufficiently large circle and expand the resolvent as a geometric series in powers of T divided by z. Integrating term by term, all contour integrals vanish except the term matching the desired power. The result is precisely T to that power.

For an exponential, the same construction agrees with the usual norm-convergent power series for e to the T. For a general analytic function, the contour integral supplies the operator value even when no single power series centered at zero covers the whole spectrum.

## A Jordan block reveals the role of derivatives

Consider the two-by-two matrix N with zeros everywhere except a one above the diagonal. Its square is zero. It has only the eigenvalue zero, and only one independent eigenvector.

For a holomorphic scalar function f near zero, the functional calculus gives f of N equal to f of zero times the identity plus f prime of zero times N. The derivative matters because the matrix is not diagonalizable.

For example, the exponential of N is the identity plus N. If we tried to define a function of N using only its eigenvalue zero, we might incorrectly conclude that the exponential is just the identity. The missing derivative term captures the nilpotent part of the matrix.

This is an essential contrast with self-adjoint functional calculus. A self-adjoint matrix cannot have a nontrivial Jordan block; its perpendicular spectral decomposition uses only the values of f at eigenvalues. For a non-normal operator, derivatives of analytic functions may be required.

## Why continuous functions are not enough here

Suppose you know only the value of a continuous function at the spectrum of N, which is the singleton zero. That datum says nothing about its derivative at zero. Two analytic functions can have the same value at zero and different derivatives there, producing different operator values at N.

So for a general non-normal operator there cannot be a functional calculus for all continuous functions on its spectrum that preserves polynomial evaluation and depends only on function values in the self-adjoint manner. The holomorphic calculus solves the problem by requiring functions defined analytically on a neighborhood of the spectrum, so their derivatives are available.

The distinction also explains an important norm phenomenon. The spectrum of N contains only zero, but N itself is not zero. Therefore the norm of the polynomial function t evaluated at N cannot equal the maximum of its absolute value on the spectrum: that maximum is zero while the operator norm of N is positive. The exact norm formula of continuous self-adjoint calculus fails for non-normal operators.

## Spectral mapping survives

Despite these differences, holomorphic functional calculus preserves sums and products and satisfies spectral mapping: the spectrum of f of T is the image of the spectrum of T under f, for holomorphic f on an appropriate neighborhood.

It also provides spectral projections in a different guise. If part of the spectrum is separated from the rest by a contour, the integral of the resolvent around that part projects onto the corresponding invariant spectral subspace. These are called Riesz projections. For a non-normal operator they need not be orthogonal projections. That is another distinction between general analytic calculus and the projection-valued spectral theorem for self-adjoint operators.

## A map of the different calculi

We now have three broad settings. For bounded self-adjoint operators, continuous functions on the spectrum yield bounded operators, with exact norm control. Spectral measures extend that construction to bounded Borel functions and then to unbounded measurable functions with carefully specified domains. For general bounded operators on complex Banach spaces, holomorphic functions near the spectrum yield operator values through contour integration.

The calculi agree on their common ground. Polynomial evaluation means the same thing wherever it appears. For a bounded self-adjoint operator and a holomorphic function defined near its spectrum, the continuous and holomorphic constructions give the same bounded operator.

The different theories are therefore not competing notations. They are tools adapted to different combinations of assumptions and desired scalar functions. The central habit is to ask two questions before using f of A: what kind of operator is A, and what kind of function is f?

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For a complex unital Banach algebra B, \(a\in B\), and \(f\) holomorphic on a neighborhood \(U\supset\sigma(a)\), choose a positively oriented cycle \(\Gamma\subset U\cap\rho(a)\) surrounding the full spectrum. Then
\[
f(a)=\frac{1}{2\pi i}\int_\Gamma f(z)(z1-a)^{-1}\,dz.
\]
This is independent of admissible \(\Gamma\); it is a unital algebra homomorphism, agrees with polynomial evaluation, and satisfies \(\sigma(f(a))=f(\sigma(a))\). A large-circle Neumann expansion verifies the polynomial case.

For \(N=\begin{psmallmatrix}0&1\\0&0\end{psmallmatrix}\), \(N^2=0\), so \(f(N)=f(0)I+f'(0)N\). In particular \(e^N=I+N\), although \(\sigma(e^N)=\{1\}\). This demonstrates why \(\|f(N)\|=\sup_{\sigma(N)}|f|\) fails for nonnormal N.

For a spectral component enclosed by \(\Gamma\) disjoint from other components, the Riesz projection is \(P=(2\pi i)^{-1}\int_\Gamma(zI-T)^{-1}dz\). In general \(P^2=P\) but \(P\ne P^*\); orthogonality requires additional structure.

### Exercises with answers

1. **Nilpotent.** Compute \((I-N)^{-1}\) for \(N^2=0\). **Answer:** \(I+N\).
2. **Analytic function.** If \(f(z)=1/(1-z)\), what is \(f(N)\)? **Answer:** \(I+N\).
3. **Non-normal norm.** Why does \(\|N\|=\max_{z\in\sigma(N)}|z|\) fail? **Answer:** The right side is zero, while N is nonzero and has norm one in the Euclidean operator norm.
4. **Compare calculi.** For a self-adjoint bounded T and holomorphic f near its spectrum, do continuous and holomorphic calculi agree? **Answer:** Yes; both agree on polynomials, and the standard uniqueness/approximation arguments identify them.

### Reading and source notes

- [Michael Taylor, Lectures on Banach Algebras, Appendix A: Holomorphic Functional Calculus](https://mtaylor.web.unc.edu/wp-content/uploads/sites/16915/2018/04/banalg.pdf).
- [Foundations of von Neumann Algebras, Banach Algebras and Holomorphic Functional Calculus](https://openmaths.org/courses/foundations-of-von-neumann-algebras/banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.html).
