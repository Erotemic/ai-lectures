# 050000 — Unbounded Functional Calculus: A Formula with an Input Test

**Track:** Analysis from First Principles. **Background:** Spectral projections, scalar spectral measures, and domains of closed operators. **Question:** How can a self-adjoint operator act through an unbounded scalar function without losing control of its domain?

<!-- BEGIN SPOKEN LECTURE -->

# Unbounded Functional Calculus: A Formula with an Input Test

Suppose a self-adjoint operator A acts like multiplication by a spectral variable. A bounded scalar function of that variable causes no difficulty: it changes the size of each spectral component by at most a fixed factor. But what if the scalar function grows without bound? Then some inputs may accumulate more squared output magnitude than the Hilbert space allows.

The unbounded spectral calculus answers two questions at once. It tells us what f of A should do, and it tells us exactly which inputs may be given to that operator. The second answer is as important as the first.

## A weighted sum as a model

Start with square-summable sequences and a diagonal operator whose N-th eigenvalue is N. A scalar function f acts on this diagonal by multiplying the N-th coordinate by f of N. To remain in square-summable sequences, the sum of the squared magnitude of f of N times the squared magnitude of the input coordinate must be finite.

If f is bounded, that weighted sum is automatically finite for every square-summable input. If f grows, different vectors behave differently. A vector supported on finitely many coordinates is always allowed, even for a rapidly growing f. Another vector may be square summable but become too large after the spectral multipliers are applied.

For instance, f of N equals N squared gives the square of the original diagonal operator. An input whose N-th coordinate is one divided by N squared belongs to the domain of A, but applying N squared produces the sequence of ones. So it is not in the domain of A squared.

The operator expression f of A therefore includes a hidden integrability condition. Making that condition explicit turns the apparently dangerous unbounded operation into a precise mathematical object.

## Replace sums by spectral measures

The general self-adjoint operator need not have an eigenbasis. It has a projection-valued spectral measure. Every vector x gives an ordinary finite measure, called the scalar spectral measure of x. It records how much squared magnitude the vector places in each spectral region.

To decide whether f of A can act on x, integrate the squared absolute value of f against that measure. If the integral is finite, x belongs to the domain. If the integral is infinite, the operation is not defined on that vector as a Hilbert-space vector.

For an allowed x, the squared norm of the output is exactly that integral. This is the general version of summing weighted squared coordinates.

The construction can be made without guessing. Truncate the scalar function by cutting its magnitude off at a large bound. Each truncation defines a bounded operator by Borel functional calculus. Apply these bounded operators to x. If the weighted integral of the full function is finite, their outputs form a Cauchy sequence in Hilbert-space norm. Define f of A applied to x to be the limit.

That explains the existence of the output. It also explains the domain: outside the weighted-integrability class, the truncated outputs cannot converge to a finite Hilbert-space vector.

## Reconstruct the operator itself

Choose f of lambda equal to lambda. Then f of A is the original self-adjoint operator A. Its domain consists of vectors for which the integral of lambda squared against their scalar spectral measures is finite.

Choose f of lambda equal to lambda squared. Then f of A is A squared with its appropriate domain, often strictly smaller. Choose f of lambda equal to the absolute value of lambda, and obtain the positive operator absolute A. All these constructions use the same spectral measure.

For a positive A, choose the square-root function. The result A to the power one half is a positive self-adjoint operator. Its domain is typically larger than that of A: the square-root weight grows more slowly than the full spectral variable. This is why an energy norm involving one derivative can make sense for functions lacking two derivatives.

The effect is visible in the diagonal model. If the eigenvalue at coordinate N is N squared, then the square-root operator multiplies by N. Some vectors survive multiplication by N but not multiplication by N squared. Fractional powers let us describe intermediate levels of regularity between the ordinary Hilbert-space norm and the stronger domain norms.

## Bounded functions of an unbounded operator

Now take f of lambda equal to one divided by one plus lambda squared. This function is bounded by one on the entire real line. So even when A is unbounded, f of A is bounded and defined on every vector.

The same is true of the complex phase function e to the imaginary t times lambda. Its magnitude is one, so e to the imaginary t A is unitary on all of H. An unbounded self-adjoint generator can thus create an everywhere-defined family of length-preserving transformations.

This is one of the most useful consequences of functional calculus. We may be unable to apply A itself to an arbitrary vector, yet can apply many important functions of A without difficulty.

## Inverses, zero, and domain traps

Suppose A is multiplication by t on L two of the real line. The scalar function one divided by t is unbounded near zero. It defines an operator only on functions whose quotient by t is still square integrable.

There is no genuine contradiction in this statement even though the number zero is not an eigenvalue of A. Inversion may fail because zero lies in the continuous spectrum: there are approximate eigenvectors concentrated near zero on which A becomes arbitrarily small.

A subtle complication arises when multiplying unbounded functions of operators. For bounded functions, f of A followed by g of A equals the function f times g of A on all vectors. For unbounded functions we must check the domain of the composition. Algebraic simplification may produce a bounded scalar function while the two-stage composition is only defined on a proper subspace.

For the multiplication operator on the real line, multiplying by one over t and then by t gives the identity on every input for which division by t was legal. But it does not define the identity on all of L two, because the first step may fail. The single function that equals one almost everywhere, by contrast, does define the identity everywhere. The formulas agree where both are defined, but their operator domains need not be identical.

This is why the spectral calculus is powerful: it tells us when familiar scalar algebra transfers safely to operators and when domain questions remain.

## Functional calculus as a language of regularity

In partial differential equations, positive self-adjoint operators frequently encode derivatives. Applying a square root, a fractional power, or a resolvent changes the regularity demanded of an input. Spectral calculus turns these changes into precise weighted-integrability conditions.

It also gives a common framework for very different physical equations. Heat evolution uses a decaying exponential of a positive operator. Wave evolution uses cosine and sine functions of a square root. Quantum evolution uses unit-modulus complex exponentials.

The reason these constructions coexist is that they are all scalar functions of a spectral variable, interpreted through one operator and its spectral measure. The operator can be unbounded; the function may still be bounded. If the function itself is unbounded, the weighted integral supplies the domain.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Let A be self-adjoint, possibly unbounded, with spectral PVM \(E_A\). For any Borel measurable \(f:\mathbb R\to\mathbb C\) finite everywhere (or finite \(E_A\)-almost everywhere), define
\[
\mathcal D(f(A))=\{x\in H:\int_{\mathbb R}|f(\lambda)|^2\,d\mu_x(\lambda)<\infty\},
\qquad\|f(A)x\|^2=\int|f|^2d\mu_x.
\]
One constructs \(f(A)x\) as the limit of \(f_n(A)x\) for bounded truncations \(f_n=f\,\mathbf1_{\{|f|\le n\}}\), or magnitude clipping. The resulting operator is closed and normal; it is self-adjoint when f is real-valued \(E_A\)-almost everywhere.

For \(A=\operatorname{diag}(1,2,3,\ldots)\) on \(\ell^2\), \(\mathcal D(A^s)=\{x:\sum n^{2s}|x_n|^2<\infty\}\) for \(s>0\). On \(L^2(\mathbb R)\) with \(A=M_t\), \(f(t)=t^{-1}\) for \(t\ne0\) and \(f(0)=0\), \(f(A)\) is multiplication by \(1/t\) on \(\{x:x/t\in L^2\}\). The product \(A f(A)\) equals I on this proper domain, whereas \((t f(t))(A)=I\) on all of H, since \(t f(t)=1\) almost everywhere relative to the PVM. Product identities for unbounded symbols are domain-sensitive.

### Exercises with answers

1. **Domain hierarchy.** For \(A=\operatorname{diag}(n)\), is \(\mathcal D(A^2)\subseteq\mathcal D(A)\)? **Answer:** Yes; \(n^4\ge n^2\) for all \(n\ge1\).
2. **Unitary.** If A is self-adjoint, what is the norm of \(e^{itA}x\)? **Answer:** \(\|x\|\), by the weighted-integral formula and \(|e^{it\lambda}|=1\).
3. **Fractional power.** If \(A=\operatorname{diag}(n^2)\), which is more restrictive: \(\mathcal D(A^{1/2})\) or \(\mathcal D(A)\)? **Answer:** \(\mathcal D(A)\subseteq\mathcal D(A^{1/2})\), typically strictly.
4. **Domain trap.** Why need \(A(1/A)\) not be the everywhere-defined identity? **Answer:** The first unbounded inverse may have a proper domain even if the scalar product equals one almost everywhere.

### Reading and source notes

- [University of Potsdam, Functional Analysis II, spectral theorem for unbounded operators](https://www.math.uni-potsdam.de/fileadmin/user_upload/Prof-Math-Phy/Rosenberger/Skripte/Funktionalanalysis_2.pdf).
- [Johns Hopkins University, Functional Analysis lecture notes, unbounded operators and calculus](https://math.jhu.edu/~js/Math637/eth.functionalanalysis.pdf).
