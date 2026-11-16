# 009000 — Stiff Systems: Fast Transients and Slow Motion

**Track:** Differential Equations and Dynamical Systems. **Background:** linear systems, eigenvalues, phase planes, and numerical ODE stability. **Central question:** why can a solution evolve slowly while the equations contain a very fast timescale that cannot be ignored numerically?

<!-- BEGIN SPOKEN LECTURE -->

# Stiff Systems: Fast Transients and Slow Motion

Imagine a physical system that reaches a near-equilibrium state in a fraction of a second but then changes noticeably only over many minutes. A chemical reaction may contain a species that adjusts almost instantly to the concentration of another. An electrical circuit can contain a tiny capacitance whose transient dies away while the overall signal varies slowly. Such systems are natural examples of multiple timescales.

There is a numerical puzzle here. A time-stepping method may need to take extraordinarily small steps, even after the solution has become smooth and slowly varying. Increasing the step size makes the computed values oscillate or explode, although the actual physical motion is perfectly stable. This is a principal symptom of stiffness.

## A two-variable model

Let u decay at rate one. Let v rapidly adjust toward u, at rate one thousand. In words, u-prime is negative u, and v-prime is minus one thousand times the difference between v and u.

The u equation is easy: u decays as e to the negative t. The v equation is a linear forced equation. It has one component that follows the slow decay and another that decays at rate one thousand. With initial values u and v both equal to one, the exact v equals one thousand over nine hundred ninety-nine times e to the negative t, minus one over nine hundred ninety-nine times e to the negative one thousand t.

The rapidly decaying second term nearly disappears after a few thousandths of a time unit. Afterwards v follows the slow component, remaining very close to u. A scientist interested in the trajectory over several seconds would naturally choose a step size based on the slow variation, perhaps tenths of a second. Why might that fail?

## The eigenvalues explain the step restriction

Write the system as a matrix equation. Its two eigenvalues are negative one and negative one thousand. Both indicate stable decay. The slow eigenvalue governs long-term behavior; the fast eigenvalue governs how rapidly deviations toward the slow behavior disappear.

Apply explicit Euler. For a scalar decay with rate one thousand, one step multiplies the value by one minus one thousand times h, where h is the step size. For repeated steps to decay in magnitude, this multiplier must lie strictly between negative one and one. Thus h must be smaller than two thousandths.

A step of one tenth is fifty times too large for this fast component. The numerical method may amplify an error in the fast direction even though the true fast mode decays almost instantly. The actual solution's smooth appearance does not remove the unstable numerical mode. Floating-point rounding, inaccurate starting values, or coupling to the slow component can excite it.

In systems with eigenvalues spread over many orders of magnitude, an explicit stability restriction may therefore be far more severe than the step size required to resolve the behavior of interest. This is not a universal definition that fits every nonlinear problem, but it gives the central intuition of stiffness.

## Solve the new state implicitly

Backward Euler handles the scalar decay equation differently. Instead of evaluating the derivative at the old value, it evaluates the derivative at the unknown new value. For a decay rate of one thousand, the new value equals the old value divided by one plus one thousand h. This multiplier remains between zero and one for every positive h.

For a linear system with matrix A, backward Euler solves a linear system with coefficient matrix identity minus h times A. The new value is determined by an equation, not by a direct evaluation. That requires more work per step, especially for large problems. But when the fast mode would force thousands of explicit steps, a stable implicit step can be economical.

This illustrates a distinction between two words often confused in numerical simulation. Stability asks whether numerical perturbations are suppressed or amplified. Accuracy asks whether the numerical result is close to the desired solution. Backward Euler can be stable for a huge step and still inaccurate. A method may safely damp the fast transient while distorting the slow dynamics if the step is too large.

An implicit method is not automatically adequate for every stiff problem. Backward Euler is A-stable, meaning its linear stability region includes the entire left half of the complex plane. It is also L-stable, meaning its stability multiplier tends to zero for extremely fast decaying modes. The trapezoidal rule is A-stable but not L-stable; for very negative test-equation arguments its multiplier approaches negative one, so fast numerical components can persist as alternating artifacts. This is why the shape of a stability region, and not just the order of the method, matters.

## Fast and slow geometry

There is also a dynamical-systems interpretation. Write the second equation with a small parameter epsilon: epsilon times v-prime equals u minus v. When epsilon is small, v changes quickly whenever it differs from u. On the slower timescale, v stays near a relation determined by the other variables. Setting epsilon equal to zero suggests v equals u, a limiting algebraic constraint rather than a differential equation for v.

But the limiting relation is only a first approximation. For the actual model, the slow solution is v equals one thousand over nine hundred ninety-nine times u, so it differs slightly from u. The tiny difference compensates for the fact that u is itself moving. If we want a more accurate reduced model, we need to account for that drift.

This is the opening idea of singular perturbation and slow-manifold theory. A small parameter multiplying a derivative can change the type of the governing equation when set to zero. Initial conditions may create a thin, fast adjustment period called an initial layer, followed by motion near a lower-dimensional slow set.

Such reductions need hypotheses. Fast dynamics must genuinely attract nearby states in the relevant region, and a proposed slow manifold may lose validity near bifurcations or where timescale separation disappears. Simply deleting a fast variable because it seems unimportant can change the solution qualitatively.

## A numerical experiment worth reasoning through

Suppose we only wish to predict u after one unit of time. The exact answer is e to negative one. In this triangular model, u is unaffected by v, so an explicit solver could integrate u alone without caring about the fast mode. But if we integrate the full coupled system with a naive explicit fixed-step method, the fast eigenvalue still constrains its stable step size. This detail prevents a common overstatement: a stiff subsystem may be irrelevant to a selected output in a special decoupled model, even though it causes trouble for a straightforward full-state integration.

In real models, coupling may make the fast variables essential for the slow evolution, and eliminating them may require more care than it does here. The point of the example is to isolate the stability mechanism, not to claim every stiff system forces the same computational choice.

Stiffness sits at the intersection of mathematical modeling, dynamical systems, and numerical analysis. The equations contain fast decaying directions and slowly evolving behavior. An integrator must respect both the geometry of those directions and the region in which its numerical updates are stable. Good solvers do not simply take smaller steps forever; they choose methods and tolerances that match the structure of the dynamics.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Consider
\[
u'=-u,\qquad v'=-1000(v-u),\qquad u(0)=v(0)=1.
\]
Then \(u(t)=e^{-t}\) and
\[
v(t)=\frac{1000}{999}e^{-t}-\frac1{999}e^{-1000t}.
\]
The coefficient matrix \(A=\begin{psmallmatrix}-1&0\\1000&-1000\end{psmallmatrix}\) has eigenvalues \(-1,-1000\).

**Absolute stability for \(y'=\lambda y\).** Explicit Euler has multiplier \(R_E(z)=1+z\); for \(\lambda=-1000\), stability requires \(0<h<0.002\). Backward Euler has \(R_B(z)=1/(1-z)\) and \(|R_B(z)|\le1\) for \(\Re z\le0\). The trapezoidal rule has \(R_T(z)=(1+z/2)/(1-z/2)\); as \(z\to-\infty\), \(R_T(z)\to-1\), so it is A-stable but not L-stable.

**Fast-slow form.** Setting \(\varepsilon=0.001\) gives \(\varepsilon v'=u-v\), \(u'=-u\). The formal \(\varepsilon\to0\) limit imposes \(v=u\), but the exact attracting slow solution for fixed \(\varepsilon\) satisfies \(v=u/(1-\varepsilon)\) for this model. The initial layer carries the fast exponential term. This reduction should not be confused with an exact identity \(v=u\) at positive epsilon.

### Exercises with answers

1. What is the explicit-Euler stability bound for \(y'=-500y\)? **Answer:** \(0<h<0.004\).
2. Why does backward Euler not guarantee high accuracy at arbitrary step size? **Answer:** absolute stability bounds amplification, not truncation error.
3. Which fast eigenvalue drives the step restriction in the two-variable example? **Answer:** \(-1000\).
4. What happens to \(R_T(z)\) for large negative real \(z\)? **Answer:** it tends to \(-1\), leaving slowly damped alternating numerical transients.

### Reading and source notes

- Michael T. Heath, University of Illinois, [Stiff ODEs](https://heath.cs.illinois.edu/iem/ode/stiff/), explicit and implicit stability comparison.
- MIT OCW [Introduction to Numerical Analysis](https://ocw.mit.edu/courses/18-330-introduction-to-numerical-analysis-spring-2004/pages/lecture-notes/), numerical ODE stability.
