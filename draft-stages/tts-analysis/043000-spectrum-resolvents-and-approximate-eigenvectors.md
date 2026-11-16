# 043000 — Spectra and Resolvents: What If an Operator Cannot Be Inverted?

**Track:** Analysis from First Principles. **Background:** Bounded operators, inverses, complex numbers, and inner products. **Question:** Why are eigenvalues insufficient to describe infinite-dimensional operators?

<!-- BEGIN SPOKEN LECTURE -->

# Spectra and Resolvents: What If an Operator Cannot Be Inverted?

Suppose a matrix has diagonal entries one and three. If you try to invert the matrix after subtracting one times the identity, the first diagonal entry becomes zero, and inversion fails. If you subtract three, the second entry becomes zero. At any other complex number, both diagonal entries remain nonzero and inversion works.

The values one and three are eigenvalues. But a more general question underlies the calculation: for which numbers z does A minus z times the identity have a bounded inverse defined on the entire space? The set where the answer is no is called the spectrum. For finite matrices, it is exactly the set of eigenvalues. For infinite-dimensional operators, that equality can fail.

## The resolvent is an inverse with a parameter

When A minus z times the identity has a bounded inverse, that inverse is called a resolvent operator. Thinking of z as a tunable parameter turns inversion into a family of problems. We can inspect where the inverse exists and how large its norm becomes as z approaches the spectrum.

For our diagonal matrix the inverse is also diagonal. Its entries are one divided by one minus z and one divided by three minus z. When z approaches one, the first factor becomes large. The inverse does not suddenly misbehave at a mysterious point: its failure is anticipated by increasingly severe amplification nearby.

If A is self-adjoint, the spectrum is real. For a complex parameter with a nonzero imaginary part, the inverse exists, and its norm is bounded by the reciprocal of the magnitude of that imaginary part. This estimate is a fundamental safeguard when working with self-adjoint differential operators.

## An operator with spectrum but no eigenvalues

Now use the space of square-integrable functions on the interval from zero to one. Let A multiply any function by the coordinate t.

To solve the equation A minus z times the identity, applied to f, equals g, the formal answer is to divide g by t minus z. If z lies outside the interval, that denominator stays safely away from zero. Division is bounded on L two. So z is outside the spectrum.

If z lies inside the interval, the denominator becomes arbitrarily small near the point t equals z. Dividing can amplify functions supported near that point by as much as we wish. There is no bounded inverse.

Thus the spectrum is the entire interval from zero to one. But this operator has no nonzero eigenvectors. An eigenvector associated with a value z would need to be supported only where t equals z, which is a set of measure zero.

This is the first decisive lesson: spectral values need not appear as eigenvalues. They can instead describe positions where an operator is arbitrarily close to failing an eigenvector equation on carefully chosen unit inputs.

## Approximate eigenvectors

Fix a number lambda between zero and one. Choose a small interval around lambda and build a function supported there, normalized so its L-two norm is one. On that support, t lies close to lambda. Therefore A applied to the function is close, in L-two norm, to lambda times the function.

As the support shrinks toward lambda, the discrepancy tends to zero. These functions are approximate eigenvectors. They do not converge to a genuine nonzero eigenvector; their shapes concentrate more and more tightly. Each one shows that the operator almost acts like multiplication by lambda on a particular unit vector.

For a bounded self-adjoint operator, every spectral value has such approximate eigenvectors. This fact replaces the finite-dimensional picture in which spectral values are always associated with actual eigenvectors.

There is another kind of infinite-dimensional spectral failure for general, non-self-adjoint operators. An operator can be one-to-one and bounded below while failing to be onto. The unilateral right shift is an example at the parameter zero. It has no nonzero kernel, but its range misses vectors with nonzero first coordinate. Its spectrum therefore contains zero even though zero is not an eigenvalue. Later, when we restrict ourselves to self-adjoint operators, the relationship between spectrum and approximate eigenvectors becomes cleaner.

## Why the distance to spectrum controls the inverse

For the multiplication operator, the inverse at a point z outside the interval is multiplication by one divided by t minus z. Its operator norm is the largest magnitude of that multiplier, interpreted in the essential-supremum sense. This is precisely one divided by the distance from z to the interval.

The same equality holds for any bounded normal operator, including every bounded self-adjoint one: the resolvent norm equals the reciprocal of the distance from z to its spectrum. This is an exceptionally rigid law. It says that the worst possible amplification of an attempted inverse can be read off directly from geometric distance in the complex plane.

Do not use that equality blindly for every matrix. A non-normal matrix can have a very large resolvent even when z is not particularly close to an eigenvalue. Such sensitivity underlies pseudospectra and transient growth in differential equations.

## A function of the operator should respect its spectrum

Take a polynomial p. We already know how to form p of A: replace the scalar variable by A, and use operator composition. For a self-adjoint A, its spectrum passes through the polynomial. In other words, the spectrum of p of A is the collection of values p takes on the spectrum of A.

For the multiplication operator, this is intuitive. If p is the square function, then p of A multiplies by t squared, and its spectrum ranges from zero to one. If p is t squared plus two, the spectrum ranges from two to three.

This is called spectral mapping. Functional calculus extends this relationship to more general functions. The spectrum supplies the domain on which those functions matter. If two scalar functions agree on the spectrum, they should describe the same function of A, even if they differ elsewhere.

The spectrum is therefore not just a list of special frequencies. It is the correct collection of scalar values against which we test an operator and through which we apply scalar functions to it. Eigenvalues are one way that spectral values show themselves, but they are not the whole story.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For bounded \(T\in\mathcal B(H)\), the resolvent set is \(\rho(T)=\{z\in\mathbb C:T-zI\text{ has a bounded everywhere-defined inverse}\}\); the spectrum is \(\sigma(T)=\mathbb C\setminus\rho(T)\). (Equivalently one may use \(zI-T\), changing the resolvent's sign.) In a nonzero complex Banach space, \(\sigma(T)\) is nonempty and compact.

For \(M_t\) on \(L^2[0,1]\):
\[
\sigma(M_t)=[0,1],\qquad \sigma_p(M_t)=\varnothing,\qquad
\|(M_t-zI)^{-1}\|=\frac1{\operatorname{dist}(z,[0,1])}
\quad(z\notin[0,1]).
\]
For real \(\lambda\in[0,1]\), normalized \(f_\epsilon=\mathbf1_{I_\epsilon}/\sqrt{|I_\epsilon|}\) with \(I_\epsilon=[0,1]\cap(\lambda-\epsilon,\lambda+\epsilon)\) satisfies \(\|(M_t-\lambda I)f_\epsilon\|\le\epsilon\). Hence the spectrum contains continuous-spectrum points without eigenvectors.

For normal \(T\), \(\|(T-zI)^{-1}\|=1/\operatorname{dist}(z,\sigma(T))\). For arbitrary operators, only the lower bound \(\|(T-zI)^{-1}\|\ge1/\operatorname{dist}(z,\sigma(T))\) is universally available. A Jordan block \(J=\begin{psmallmatrix}0&1\\0&0\end{psmallmatrix}\) has \(\sigma(J)=\{0\}\) but \(\|(zI-J)^{-1}\|\) grows on the order of \(|z|^{-2}\) near zero.

### Exercises with answers

1. **Matrix resolvent.** Find the spectrum of \(\operatorname{diag}(1,3)\). **Answer:** \(\{1,3\}\).
2. **Continuous spectrum.** Explain why \(M_t\) has no eigenvalue equal to one half. **Answer:** An eigenfunction would vanish almost everywhere except possibly at a singleton, hence be zero in \(L^2\).
3. **Shift range.** Is the unilateral right shift invertible? **Answer:** No. It has no preimage of \(e_1\), so zero belongs to its spectrum even though its kernel is zero.
4. **Mapping.** What is \(\sigma(M_t^2+2I)\)? **Answer:** \([2,3]\).

### Reading and source notes

- [MIT OpenCourseWare, Introduction to Functional Analysis, Lectures 20–22](https://ocw.mit.edu/courses/18-102-introduction-to-functional-analysis-spring-2021/pages/lecture-notes-and-readings/).
- [Michael Taylor, Lectures on Banach Algebras](https://mtaylor.web.unc.edu/wp-content/uploads/sites/16915/2018/04/banalg.pdf).
