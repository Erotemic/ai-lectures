# 046000 — Continuous Functional Calculus: Build the Operator by Approximation

**Track:** Analysis from First Principles. **Background:** Self-adjoint operators, spectrum, polynomials, and uniform convergence. **Question:** How can a continuous scalar function act on an operator without an eigenbasis?

<!-- BEGIN SPOKEN LECTURE -->

# Continuous Functional Calculus: Build the Operator by Approximation

Suppose A is a bounded self-adjoint operator with spectrum between zero and one. We know how to form A squared. We know how to form three A plus the identity. But what should the square root of A mean if A has no eigenvectors?

There are two ideas in the answer. First, every polynomial has an unambiguous meaning when the scalar variable is replaced by an operator. Second, we can approximate a continuous scalar function by polynomials, and the operator norm behaves well enough to carry that approximation into the operator world.

The second idea requires care. It is not enough that the scalar polynomials converge pointwise. We need one error bound controlling every possible input vector. That is what uniform convergence on the spectrum provides.

## Start from a polynomial

Let p of t be t squared minus two t plus three. Define p of A as A composed with A minus two A plus three times the identity. This uses only addition, scalar multiplication, and composition of bounded operators.

Polynomial evaluation preserves sums and products of polynomials. It also preserves complex conjugation in the form of taking adjoints when A is self-adjoint. At this stage we are doing algebra, not analysis.

The analytic question is how the size of p of A compares with the largest size of p on the spectrum of A. For bounded self-adjoint operators, the answer is exact: the operator norm of p of A equals the maximum of the absolute value of p over the spectrum. This is the crucial norm formula.

Where does it come from? The operator p of A is normal, meaning it commutes with its adjoint. For a normal operator, the operator norm equals the largest magnitude in its spectrum. Polynomial spectral mapping says that the spectrum of p of A consists exactly of values of p on the spectrum of A. Combine the two statements and the norm formula follows.

This is where the self-adjoint hypothesis earns its keep. General non-normal matrices do not satisfy the same norm formula. Their polynomial values can be much larger than the polynomial is on the spectrum.

## Approximate a continuous function

Take a continuous function f on the spectrum of A. Since the spectrum is a compact subset of the real line, we can approximate f uniformly by polynomials. This is a consequence of the Weierstrass approximation theorem, applied to a containing interval if necessary.

Uniformly means that a single small tolerance controls the difference between f and the chosen polynomial at every spectral value. Choose a sequence of polynomials whose maximum approximation errors approach zero.

Now compare two of their operator evaluations. The norm formula says their operator-norm distance is exactly the maximum difference between the two polynomials on the spectrum. So the operators form a Cauchy sequence in operator norm.

The space of bounded operators is complete. The sequence therefore converges to a bounded operator. We define that limit to be f of A. If we had picked a different approximating polynomial sequence, the same estimate would force the same limit. So the definition does not depend on our approximation method.

This is functional calculus constructed from first principles: an approximation theorem for scalar functions, an exact operator norm formula, and completeness.

## What the construction guarantees

The resulting rule from f to f of A preserves sums, products, constants, and complex conjugation. A real-valued continuous function gives a self-adjoint operator. A nonnegative continuous function gives a positive operator.

It is isometric: the norm of f of A is the maximum absolute value of f on the spectrum. This is a much stronger assertion than merely being bounded by a constant times that maximum. It means the functional calculus retains the full uniform size of the scalar function, as seen through the spectrum.

For the square-root function on the nonnegative spectrum of a positive A, we obtain a positive square root. For a real-valued exponential we obtain a positive operator. For the complex-valued function whose value at t is e to the imaginary t, we obtain a unitary operator.

It also satisfies spectral mapping: the spectrum of f of A is the image of the spectrum of A under f. This follows from invertibility. A scalar number lies outside the range of f on the spectrum exactly when one divided by f minus that number is another continuous function there. Functional calculus turns this reciprocal into a bounded inverse.

## A concrete multiplication example

Let A multiply square-integrable functions on the unit interval by t. It has no eigenvectors, but we can evaluate polynomials in it: p of A simply multiplies by p of t.

When we pass to uniformly approximating polynomials, the limit must multiply by f of t. So continuous functional calculus agrees with the obvious answer for this model.

For example, the square root of A multiplies by the square root of t. The exponential of negative A multiplies by e to the negative t. If two continuous functions agree on the interval, they yield the same operator. Nothing requires an eigenbasis.

The general spectral theorem says every bounded self-adjoint operator can be represented, in an appropriate sense, by multiplication. But the polynomial approximation construction allows us to define the continuous calculus before proving the full representation theorem.

## The boundary of the method

What about a function that is one on the left half of the spectrum and zero on the right half? Such a function is discontinuous at the dividing point. Unless that point is isolated from the rest of the spectrum, continuous functions cannot uniformly approximate it. Any continuous approximant must transition somewhere, and the maximum error near the jump cannot be made arbitrarily small.

Yet selecting part of the spectrum is a natural operation. For a matrix, we simply sum the projections corresponding to eigenvalues in the selected region. We want an analogous spectral filter in infinite dimensions.

The missing ingredient is a different notion of approximation. Rather than demand a uniform operator-norm error, we can require convergence when the operators act on each fixed vector. For bounded pointwise approximations, the spectral theorem makes this possible, using measures and dominated convergence. This extension leads to bounded Borel functional calculus.

The important distinction is not just continuous versus discontinuous functions. It is norm convergence versus strong convergence, and the information carried by the spectral measure of each vector. The continuous construction teaches us what functions of operators should do. Spectral measures let us go further without pretending that every scalar approximation is uniform.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For a bounded self-adjoint \(A\) on a nonzero complex Hilbert space with \(K=\sigma(A)\subset\mathbb R\), there exists a unique unital isometric \(*\)-homomorphism
\[
\Phi_A:C(K)\to\mathcal B(H),\qquad \Phi_A(t\mapsto t)=A,
\]
with \(\|\Phi_A(f)\|=\max_{\lambda\in K}|f(\lambda)|\). For polynomials, this follows from spectral mapping and the spectral-radius formula for normal operators; then extend via uniform polynomial approximation and completeness.

The continuous calculus satisfies \(\sigma(f(A))=f(\sigma(A))\), \(f\ge0\implies f(A)\ge0\), and \(f(A)^*=\overline f(A)\). The notation \(f(A)\) here is defined for continuous \(f\) on \(K\); bounded Borel symbols require a later extension.

A useful limit comparison: if continuous \(f_n\to f\) uniformly on \(K\), then \(\|f_n(A)-f(A)\|\to0\). Pointwise convergence alone does not imply norm convergence: with \(A=M_t\) and \(f_n(t)=t^n\) on \([0,1]\), \(f_n(t)\to0\) for \(t<1\) but \(\|f_n(A)\|=1\) for every n. In fact \(f_n(A)x\to0\) for each \(x\in L^2[0,1]\) by dominated convergence, showing strong but not norm convergence.

### Exercises with answers

1. **Same on spectrum.** If \(\sigma(A)=[0,1]\), can different continuous functions on \(\mathbb R\) define the same operator? **Answer:** Yes, provided their restrictions to \([0,1]\) agree.
2. **Root.** For \(A\ge0\), why is \((\sqrt\cdot(A))^2=A\)? **Answer:** The calculus is multiplicative, and \((\sqrt t)^2=t\) on \(\sigma(A)\).
3. **Norm.** If \(\sigma(A)=\{-2,3\}\), what is \(\|A^2\|\)? **Answer:** \(\max(4,9)=9\).
4. **Pointwise.** Explain why \(t^n\) gives strong but not operator-norm convergence to zero for multiplication on \(L^2[0,1]\). **Answer:** Dominated convergence applies to each fixed vector, but the essential supremum of \(t^n\) is one.

### Reading and source notes

- [Sheldon Axler, Measure, Integration & Real Analysis](https://measure.axler.net/).
- [Kelly Davis, Spectral Theorem for Bounded Self-Adjoint Operators](https://kellyjdavis.github.io/functional-analysis/spectral-theorems/).
- [MIT OpenCourseWare, Introduction to Functional Analysis](https://ocw.mit.edu/courses/18-102-introduction-to-functional-analysis-spring-2021/pages/lecture-notes-and-readings/).
