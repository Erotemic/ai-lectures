# 052000 — Functional Calculus in Motion: Heat, Waves, and Quantum Evolution

**Track:** Analysis from First Principles. **Background:** Positive self-adjoint operators, bounded Borel functional calculus, and energy norms. **Question:** How do scalar functions of spectral values solve evolution equations?

<!-- BEGIN SPOKEN LECTURE -->

# Functional Calculus in Motion: Heat, Waves, and Quantum Evolution

A hot object cools. A plucked string vibrates. A quantum wave function changes phase. These are different physical processes, but their mathematical solutions share a common mechanism: apply a scalar function to an operator that encodes spatial structure.

The scalar function depends on time. The spatial operator supplies spectral values. Functional calculus combines them, turning an ordinary scalar multiplier for each frequency into a transformation on a whole function space.

The advantage is that we do not need to solve a new equation for every initial condition. Once the operator is understood, the same operator-valued function evolves every allowed initial state.

## The heat equation as spectral damping

Begin with a nonnegative self-adjoint operator A. Imagine it as a measure of spatial roughness. For a vibrating string with fixed ends, one example is minus the second derivative, equipped with appropriate boundary conditions. Its eigenfunctions are sine waves. Higher frequencies have larger eigenvalues, growing like the square of the frequency.

The heat equation can be written in the form: the time derivative of u plus A applied to u equals zero. If u begins in a single eigenvector direction, then A acts by multiplication by an eigenvalue lambda, and the equation becomes an ordinary differential equation. Its solution is the initial amplitude multiplied by e to the negative t lambda.

Every eigenmode therefore decays exponentially, with a rate controlled by its eigenvalue. High-frequency roughness decays faster than low-frequency variation. This is why heat flow smooths a signal.

Functional calculus turns this scalar solution into an operator solution: apply the function lambda maps to e to the negative t lambda to A. We write this as e to the negative t A. Because A is nonnegative, the scalar multiplier lies between zero and one for nonnegative time. The resulting operator is a contraction: it cannot increase the Hilbert-space norm of the input.

Even if the initial condition is outside the domain of A, the bounded exponential still acts on it. For positive times, the decay of large spectral values often gives additional regularity. This is why a rough initial temperature profile can immediately become smoother under heat flow.

## Fixed-end strings give a concrete spectrum

For a string of length one with both endpoints fixed, consider the functions sine of n pi x, for positive integers n. After normalization they form an orthonormal basis of L two on the interval. The operator minus the second derivative sends the N-th mode to N squared pi squared times that mode.

Suppose the initial temperature is a sum of the first two modes. The first component decays like e to the negative pi squared times time. The second decays like e to the negative four pi squared times time. At the same positive time, the second mode is suppressed more strongly.

This calculation can be understood without an abstract spectral theorem, because the sine basis is explicit. The spectral theorem generalizes it to settings where the spatial operator cannot be diagonalized by such a familiar formula.

## Quantum motion rotates instead of damping

Now change the scalar exponential. Instead of e to the negative t lambda, use e to the negative imaginary t lambda. Its absolute value is one for every real lambda. If A is self-adjoint, functional calculus makes the resulting operator unitary.

So an initial state keeps its Hilbert-space norm exactly, while each spectral component rotates in complex phase at a rate determined by its spectral value. This is the mechanism behind the abstract Schrödinger evolution.

The contrast with heat is instructive. The same positive operator A may generate a contraction semigroup through a real negative exponential and a unitary group through an imaginary exponential. The difference comes from the scalar function, not from changing the spectral decomposition.

In the quantum case, the equation is expressed with an imaginary unit multiplying the time derivative. In suitable units, the resulting solution is e to the negative imaginary t A applied to the initial vector. For inputs in the domain of A, the derivative in Hilbert-space norm exists and satisfies the equation in the usual strong sense. For arbitrary Hilbert-space vectors, the unitary family still defines a continuous evolution, even when that derivative need not exist.

## Wave motion uses a square root

A wave equation has two time derivatives. In abstract form it is the second time derivative of u plus A u equals zero, with A nonnegative and self-adjoint.

In a single spectral direction with value lambda, the scalar equation describes an oscillator with frequency equal to the square root of lambda. Its solution combines cosine of t times that frequency with sine divided by that frequency. If lambda is zero, the sine-over-frequency expression is interpreted by its continuous limit, which is t.

Functional calculus gives the same solution for the whole operator. The initial displacement is multiplied by cosine of t times square root A. The initial velocity is multiplied by sine of t times square root A divided by square root A, with the zero-frequency value defined by continuity.

The cosine multiplier is bounded by one. The sine-over-square-root multiplier is bounded for every fixed time, because its absolute value is at most the magnitude of t. Thus the operator formula makes sense on the full Hilbert space for fixed time.

For a physically meaningful finite-energy wave solution, more regularity is needed: the initial displacement should lie in the domain of square root A, and the initial velocity in the Hilbert space. Then an energy combining squared velocity and the squared norm of square root A applied to displacement is conserved.

That distinction illustrates the value of domain-aware functional calculus. The operator-valued formula can define a continuous motion on broad input classes; different claims about derivatives and energy require the appropriate domains.

## A computational perspective

In numerical analysis, the same reasoning explains spectral filtering and matrix functions. If a discretization produces a positive self-adjoint matrix, its heat propagator damps high eigenvalue components. Its wave propagator oscillates them. Approximating these operator functions becomes a computational problem: polynomials, rational approximations, Krylov methods, or contour methods can evaluate the action without explicitly forming every eigenvector.

The underlying accuracy question is not just whether a scalar approximation is good on paper. It is whether it is good over the relevant spectrum, in the operator norm or in the state-dependent norm appropriate to the task.

So functional calculus is not an abstract detour from applied mathematics. It is the common language behind smoothing, oscillation, propagation, spectral regularization, and many simulation algorithms.

## What we have gained

We began by asking what it means to apply a function to something that is not a number. For self-adjoint operators, spectral calculus provides the answer by representing an operator through its spectral values and applying the scalar function there. If the scalar function is bounded, the result acts on every vector. If it is unbounded, a weighted-integrability condition specifies the domain.

For non-self-adjoint bounded operators, complex contour integration provides a different but compatible construction for holomorphic functions. Each version preserves the ordinary scalar manipulations that remain valid under its assumptions.

And now the abstractions return to concrete phenomena. Heat decays. Waves oscillate. Quantum states preserve norm. These behaviors emerge from elementary scalar functions evaluated on a spectrum. The achievement of functional calculus is to make that reasoning correct even when the spectrum is infinite, continuous, or hidden from any explicit eigenvector basis.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For \(A\ge0\) self-adjoint on H, spectral calculus defines the heat semigroup \(S(t)=e^{-tA}\) for \(t\ge0\), with \(\|S(t)\|\le1\), \(S(t+s)=S(t)S(s)\), and strong continuity at \(t=0\). For \(x\in\mathcal D(A)\), \(\frac d{dt}S(t)x=-AS(t)x\). The Schrödinger unitary group \(U(t)=e^{-itA}\) obeys \(\|U(t)x\|=\|x\|\) and for \(x\in\mathcal D(A)\) satisfies \(i\partial_t U(t)x=AU(t)x\).

The abstract wave equation \(u_{tt}+Au=0\) has formula
\[
u(t)=\cos(t\sqrt A)u_0 + g_t(A)v_0,\quad
 g_t(\lambda)=\begin{cases}\sin(t\sqrt\lambda)/\sqrt\lambda,&\lambda>0,\\t,&\lambda=0.\end{cases}
\]
For fixed real t, \(|g_t(\lambda)|\le|t|\), so both terms define bounded operators on H. Finite-energy data \(u_0\in\mathcal D(A^{1/2})\), \(v_0\in H\) yield energy conservation \(E(t)=\tfrac12(\|u_t(t)\|^2+\|A^{1/2}u(t)\|^2)=E(0)\), understood at the appropriate solution regularity.

For the Dirichlet Laplacian \(A=-\partial_x^2\) on \((0,1)\), \(\phi_n(x)=\sqrt2\sin(n\pi x)\), \(A\phi_n=n^2\pi^2\phi_n\), and \(e^{-tA}\phi_n=e^{-tn^2\pi^2}\phi_n\). This directly illustrates high-frequency damping.

### Exercises with answers

1. **Two heat modes.** Which decays faster under heat flow, \(\phi_1\) or \(\phi_2\)? **Answer:** \(\phi_2\), with exponent \(-4\pi^2t\) rather than \(-\pi^2t\).
2. **Norm preservation.** Why is \(e^{-itA}\) unitary for self-adjoint A? **Answer:** Its scalar spectral multiplier has modulus one for real \(t\).
3. **Zero frequency.** What is \(\lim_{\lambda\downarrow0}\sin(t\sqrt\lambda)/\sqrt\lambda\)? **Answer:** t.
4. **Initial domain.** May \(e^{-tA}u_0\) be defined when \(u_0\notin\mathcal D(A)\)? **Answer:** Yes; for \(t\ge0\) the exponential is bounded. Differentiability at zero is a separate matter.

### Reading and source notes

- [MIT OpenCourseWare, Introduction to Functional Analysis](https://ocw.mit.edu/courses/18-102-introduction-to-functional-analysis-spring-2021/pages/lecture-notes-and-readings/).
- [University of Potsdam, Functional Analysis II, unbounded spectral theorem](https://www.math.uni-potsdam.de/fileadmin/user_upload/Prof-Math-Phy/Rosenberger/Skripte/Funktionalanalysis_2.pdf).
- [Sheldon Axler, Measure, Integration & Real Analysis](https://measure.axler.net/).
