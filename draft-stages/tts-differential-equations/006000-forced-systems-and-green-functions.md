# 006000 — Forced Systems, Variation of Constants, and Green's Functions

**Track:** Differential Equations and Dynamical Systems. **Background:** scalar integrating factors and the matrix exponential. **Question:** how does a system combine its natural evolution with inputs arriving at different times?

<!-- BEGIN SPOKEN LECTURE -->

# Forced Systems, Variation of Constants, and Green's Functions

A vibrating instrument continues moving after the initial strike. It can also be driven while it moves: someone repeatedly plucks the string, pushes a mass, or changes an applied voltage. The first behavior comes from the state already present. The second comes from a continuing input. For a linear system, we can separate these effects exactly.

Write the state equation as x prime equals A x plus b of t, where A is a constant square matrix and b is a continuous forcing vector. The initial state is x zero at time zero. The solution has two pieces. The first is e to the A t times x zero, just as for the unforced system. The second is the integral, from zero to t, of e to the A times t minus s multiplied by b of s. This is the variation-of-constants formula, sometimes called variation of parameters or Duhamel's principle.

## Deriving the integral, not guessing it

First multiply the equation by e to the negative A t. Differentiate the product e to the negative A t times x of t. By the product rule, one contribution is negative A e to the negative A t times x. The other is e to the negative A t times x prime. Substitute x prime equals A x plus b. The A terms cancel because A commutes with its own exponential. We are left with e to the negative A t times b of t.

Integrate both sides from zero to t. At time zero, the exponential is the identity, so the initial value is x zero. Finally multiply by e to the A t. The result is precisely the two-part solution described above.

There is a physical interpretation behind each factor in the integral. At time s, the external input adds a small increment of state, proportional to b of s times the small time step. That increment then evolves freely for the remaining time t minus s, under the operator e to the A times t minus s. Adding up the contributions from all earlier input times produces the integral.

This explains causality in the formula. The state at time t depends only on inputs at earlier times, from zero through t. No future input is required to calculate it.

## A one-dimensional example

Take the scalar equation x prime equals negative a x plus f of t, with positive constant a. The unforced system decays at rate a. The solution is x zero times e to the negative a t plus the integral of e to the negative a times t minus s multiplied by f of s.

For a constant input F, the integral can be evaluated explicitly. The state approaches F divided by a, and the transient difference from that equilibrium decays exponentially. The exact solution is F divided by a plus the initial offset, x zero minus F divided by a, times e to the negative a t.

Now compare a constant input with a brief input concentrated near one moment. A brief impulse makes a quick change in the state followed by the usual natural decay. The effect of that impulse at later times is determined by the exponential decay kernel. When we model an idealized impulse using a Dirac delta distribution, its response is the same kernel, understood with the appropriate jump condition. We should not treat the delta as an ordinary continuous function; it is a useful idealization whose integral effect is precise.

## Green's functions and impulse responses

A Green's function is a kernel that translates forcing at one time or location into a response at another. For the scalar decay equation, the causal kernel is zero before the forcing time and e to the negative a times the elapsed time after it. The solution of the zero-initial-value problem is the integral of this kernel times the input.

For a vector system with an input matrix B and an input vector u of t, the corresponding kernel is e to the A times elapsed time multiplied by B for nonnegative elapsed time. The response is the convolution of that matrix-valued impulse response with u. Convolution means that all delayed copies of the impulse response are weighted by the past input and summed.

We can see superposition directly. If input u one produces a response x one from zero initial state, and input u two produces x two, then the sum of the inputs produces the sum of the responses. Scaling an input scales its response. These properties are not approximations; they follow from linearity and uniqueness.

But superposition does *not* say any nonlinear system can be decomposed in the same way. When the matrix A depends on the state, adding two solutions will generally not give another solution. When A depends on time rather than remaining constant, a time-dependent transition matrix replaces the simple exponential of a time difference; the convolution structure is no longer automatically time-translation invariant.

## Resonance and long-lived forcing

A stable system gradually forgets its initial state, but it can have a strong response to certain driving frequencies. Consider the undamped harmonic oscillator: x double prime plus omega zero squared times x equals a forcing F times cosine of omega times t. When the driving frequency differs from the natural frequency, one can seek a particular solution oscillating at the drive frequency, with amplitude proportional to one divided by omega zero squared minus omega squared.

As the driving frequency approaches the natural frequency, that denominator tends to zero. At exact resonance the simple sinusoidal trial fails. The correct particular solution includes a factor of time times sine of the natural frequency times t, showing linearly growing amplitude in the ideal undamped model. This does not require the system to have an unstable homogeneous solution; the undamped homogeneous motion remains bounded. Sustained resonant forcing injects energy so coherently that the forced response grows.

Damping changes the story. With positive damping, the steady periodic response has a finite amplitude at every fixed nonzero damping value. The largest response may still be substantial, but exact unbounded linear growth disappears in the standard damped oscillator. In applications, finite input duration, nonlinearities, and physical limits also constrain growth. The ideal linear equation isolates the mechanism.

## From time domain to frequency domain

For a stable linear system driven by a complex exponential input, try a response with the same frequency. If the input is B times a fixed vector times e to the imaginary frequency times t, substitute a solution of the same form. The unknown amplitude must satisfy the linear equation obtained by subtracting A from the imaginary-frequency multiple of the identity. When that matrix is invertible, its inverse times B is the frequency-response operator.

This is a compact way to predict which frequencies are amplified or attenuated without solving an integral anew each time. A pole or near-singularity of the frequency-response operator signals a strong interaction between forcing and the system's natural modes. For a stable matrix A, there are no poles on the imaginary axis, so the steady-state sinusoidal response is well-defined. If A has imaginary-axis eigenvalues, resonance and polynomial growth can reappear, and there may be no bounded steady state.

## Why this formula is more general than a trick

Variation of constants solves a broad class of linear forced initial-value problems. It makes the distinct roles of initial data, natural dynamics, and external forcing explicit. It also creates a bridge to numerical time-stepping, signals, control, and partial differential equations, where response kernels and operators appear in larger spaces.

Most importantly, the integral is not mysterious. Every forcing event contributes a little state, and every contribution follows the same evolution law afterward. A complex response is the cumulative sum of simple propagated contributions. That principle is the enduring content of Green's functions and linear superposition.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For \(x'(t)=Ax(t)+b(t)\), \(x(0)=x_0\), the **variation-of-constants formula** is
\[
x(t)=e^{At}x_0+\int_0^t e^{A(t-s)}b(s)\,ds.
\]
For \(b(t)=Bu(t)\), the causal impulse response is \(G(\tau)=e^{A\tau}B\) for \(\tau\ge0\) and zero for \(\tau<0\); from zero initial data, \(x=G*u\).

**Scalar decay:** \(x'=-ax+F\) for \(a>0\) has
\[
x(t)=\frac Fa+\left(x_0-\frac Fa\right)e^{-at}.
\]

**Undamped resonance:** for \(x''+\omega_0^2x=F\cos(\omega_0t)\), a particular solution is
\[
x_p(t)=\frac{F}{2\omega_0}t\sin(\omega_0t)\qquad(\omega_0\ne0).
\]
For stable \(A\), the steady complex frequency-response operator for \(x'=Ax+Bu\) is \((i\omega I-A)^{-1}B\).

### Exercises with answers

1. What remains of the formula if the forcing is zero? **Answer:** \(x(t)=e^{At}x_0\).
2. For \(x'=-2x+4\) and \(x(0)=1\), find \(x(t)\). **Answer:** \(x(t)=2-e^{-2t}\).
3. Why must the impulse-response kernel depend only on \(t-s\) here? **Answer:** constant A makes the dynamics time-translation invariant.
4. Why may resonance occur in an undamped but not an asymptotically stable oscillator? **Answer:** the undamped system has imaginary-axis eigenvalues; stable damping moves them into the left half-plane, preventing a pole at real driving frequency.

### Reading

MIT OpenCourseWare, [Differential Equations lecture notes](https://ocw.mit.edu/courses/18-03-differential-equations-spring-2010/pages/lecture-notes/), linear systems, transfer functions, and convolution.
