# 011000 — Euler and Runge–Kutta Methods: Accuracy Is Not Stability

**Track:** Numerical Analysis. **Background:** derivatives, initial-value problems, Taylor expansion, and elementary error bounds. **Question:** how can a sequence of discrete updates approximate a continuous trajectory, and why can small steps still give unstable or misleading answers?

<!-- BEGIN SPOKEN LECTURE -->

# Euler and Runge–Kutta Methods: Accuracy Is Not Stability

A differential equation tells us the velocity of a system at each moment. A numerical solver turns that local information into a sequence of states, each separated by a chosen time step. The simplest method looks at the current derivative and moves along its direction for one step. It is called Euler's method.

Suppose y-prime equals f of time and y, with an initial value y at time zero. Choose a step size h. Euler's rule says: the next value equals the current value plus h times the derivative evaluated at the current time and value. Geometrically, we follow the tangent line from the current point rather than the unknown curved solution.

For a linear function with constant slope, this is exact. For a curved trajectory it introduces error. Understanding that error requires distinguishing what happens in one step from what accumulates over many steps.

## A test equation we can solve exactly

Take y-prime equals negative two times y, starting at y equals one. The exact solution decays exponentially: at time t it equals e raised to negative two t. Euler's method instead multiplies the current value by one minus two h at every step.

If h is one quarter and we take four steps to reach time one, the numerical values are one, one half, one quarter, one eighth, and one sixteenth. The final approximation is 0.0625. The true value is approximately 0.1353. We have underestimated it substantially.

Decrease h and the approximation improves. But simply taking a positive step size does not guarantee reasonable behavior. If h is larger than one, the factor one minus two h has magnitude greater than one. Successive Euler values grow in magnitude while changing sign, even though the true solution decays monotonically to zero. The numerical method can be unstable on a mathematically stable problem.

This simple example tells us that the behavior of the discretization is not identical to the behavior of the differential equation.

## Local error and global error

Imagine starting a numerical step from the exact value of the solution. Compare the output of the numerical step with the true solution at the next time. That difference is the one-step local error, also called the local truncation defect. It isolates the error of a single update without allowing earlier numerical mistakes to contaminate the experiment.

For Euler's method, Taylor's theorem gives the exact next value as the current value plus h times the derivative plus a term proportional to h squared, assuming suitable smoothness. Euler keeps the first two terms and discards the rest. Therefore its local error is of order h squared.

But to simulate a fixed interval of length T, we take roughly T divided by h steps. Earlier errors are propagated by later updates, and each step contributes another new defect. Under a Lipschitz condition and suitable regularity, those effects accumulate so that the global error at a fixed final time is of order h, not h squared.

There is a useful way to derive the bound. Let e be the difference between the numerical approximation and the true value at a time step. Lipschitz continuity of f says the difference between two evaluated derivatives is at most L times the difference in their states. Euler therefore amplifies the prior error by at most one plus h L, then adds the new local error of order h squared. Repeat this inequality over N steps. The geometric sum of the amplification factors remains bounded by an exponential in L T, while the accumulated local errors are proportional to h. This is a discrete version of Grönwall's inequality.

The constant can be large when the dynamics strongly amplify perturbations. Convergence order describes what happens as h shrinks with the final time fixed and assumptions satisfied; it does not promise a small error at a particular coarse step size.

## Improve the step by sampling more intelligently

Euler uses only the slope at the beginning of the interval. One improvement is the explicit midpoint method. First predict where the solution would be halfway through the interval using a half Euler step. Evaluate the derivative at that predicted midpoint. Then use that midpoint slope for the full step.

For a smooth differential equation, this scheme has local error of order h cubed and global error of order h squared. It is often substantially more accurate than Euler for the same step size, though each step needs an extra derivative evaluation.

The classical fourth-order Runge–Kutta method, often called RK four, takes four slopes: at the beginning, at two intermediate predicted states near the midpoint, and at a predicted endpoint. It combines those slopes with weights one, two, two, and one, divided by six. The weighting is chosen so that its Taylor expansion matches the exact solution through fourth order.

Under sufficient smoothness, RK four has local error of order h to the fifth power and global error of order h to the fourth power on a fixed interval. It uses more derivative evaluations per step, but can be far more accurate at a given step size.

This tradeoff suggests an important practical question: how many evaluations are needed to reach a desired accuracy, not simply how accurate one step is in isolation?

## Return to the decay equation and test stability

Write the linear test equation as y-prime equals lambda times y, where lambda can be a complex number. Its exact solution multiplies by e to the lambda h after one step. Euler instead multiplies by one plus lambda h. For a decaying exact solution, the real part of lambda is negative. The numerical values decay only if the magnitude of one plus lambda h is less than one.

For a real negative lambda, this means the step size must be small enough that lambda h lies strictly between negative two and zero. If lambda is negative one hundred, h must be smaller than 0.02 for Euler's iterates to decay. A simulation over a long interval using h equals 0.03 may produce alternating values whose magnitude grows, although the real solution decays extremely rapidly.

Classical RK four has its own stability multiplier, a fourth-degree polynomial in lambda h obtained by truncating the exponential series after the fourth power. On the negative real axis it remains stable over a larger interval than Euler, but that interval is still finite. Higher order does not make an explicit method stable for every possible step size.

This is one motivation for implicit methods. A backward Euler step evaluates the derivative at the new unknown state. Applied to the linear test equation it gives a multiplier equal to one divided by one minus lambda h. For real negative lambda, its magnitude is less than one for every positive h. More generally backward Euler is stable for the whole left half of the complex plane, a property called A-stability.

Implicit steps require solving equations. That additional cost can be justified when the dynamics include fast-decaying components that force explicit methods to take tiny steps for stability even though the behavior of interest evolves slowly. Such systems are called stiff.

## Accuracy, stability, and conditioning are different questions

An accurate method can still use an unstable step size. A stable step may still be too inaccurate to resolve the quantity we care about. And even if a numerical method is stable, the original differential equation may be sensitive to perturbations in its initial conditions or parameters.

For linear test problems we can analyze the stability multiplier exactly. For nonlinear problems we combine local error estimates, stability analysis, adaptive step-size control, and sometimes conservation laws or qualitative checks. If a physical pendulum is supposed to conserve energy in the absence of friction, long-time numerical energy drift is a warning about the integrator, not automatically evidence of real damping or energy input.

The central numerical lesson is that consistency, stability, and convergence play distinct roles. The solver must approximate the differential equation locally; errors must not be amplified uncontrollably; and the cumulative approximation must approach the true solution as the step is refined. Euler and Runge–Kutta make those distinctions visible with formulas simple enough to analyze by hand.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For \(y'=f(t,y)\), explicit Euler is \(y_{n+1}=y_n+h f(t_n,y_n)\). Explicit midpoint is
\[
k_1=f(t_n,y_n),\quad k_2=f(t_n+h/2,y_n+hk_1/2),\quad y_{n+1}=y_n+h k_2.
\]
Classical RK4 is
\[
\begin{aligned}
k_1&=f(t_n,y_n),\\
k_2&=f(t_n+h/2,y_n+hk_1/2),\\
k_3&=f(t_n+h/2,y_n+hk_2/2),\\
k_4&=f(t_n+h,y_n+hk_3),\\
y_{n+1}&=y_n+\frac h6(k_1+2k_2+2k_3+k_4).
\end{aligned}
\]
Under sufficient smoothness and a Lipschitz bound, Euler local defect is \(O(h^2)\), global error \(O(h)\); explicit midpoint \(O(h^3)\) and \(O(h^2)\); RK4 \(O(h^5)\) and \(O(h^4)\). These are fixed-time asymptotic statements, not uniform guarantees for arbitrarily stiff equations.

**Discrete Grönwall.** If \(\|e_{n+1}\|\le(1+hL)\|e_n\|+Ch^{p+1}\) and \(e_0=0\), then for \(t_n\le T\) and \(L>0\),
\[
\|e_n\|\le Ch^p\frac{(1+hL)^n-1}{L}\le Ch^p\frac{e^{LT}-1}{L}.
\]
For \(L=0\), the bound is \(CT h^p\).

**Absolute stability for \(y'=\lambda y\).** Euler: \(R(z)=1+z\). RK4: \(R(z)=1+z+z^2/2+z^3/6+z^4/24\). Backward Euler: \(R(z)=(1-z)^{-1}\). The linear test iterates decay when \(|R(h\lambda)|<1\). Backward Euler satisfies \(|R(z)|\le1\) for \(\Re z\le0\), where the denominator is nonzero.

**Worked step.** \(y'=-2y\), \(y(0)=1\), \(h=1/4\): Euler \(y_4=(1-2h)^4=(1/2)^4=0.0625\), while \(y(1)=e^{-2}\approx0.135335\).

### Exercises with answers

1. For \(y'=-10y\), what is Euler's absolute-stability requirement? **Answer:** \(0<h<0.2\).
2. How many derivative evaluations does classical RK4 require per step? **Answer:** four.
3. Does \(O(h^2)\) local defect imply \(O(h^2)\) global accuracy for Euler? **No.** Under the stated conditions its global accuracy is first order.
4. Is backward Euler explicit? **No.** Its update generally requires solving for the new state.

### Reading

MIT 18.330, [Introduction to Numerical Analysis lecture notes](https://ocw.mit.edu/courses/18-330-introduction-to-numerical-analysis-spring-2004/pages/lecture-notes/), ODE integration and error; MIT 18.330, [initial-value problem notes](https://math.mit.edu/icg/resources/teaching/18.330/18.330-Feb23.pdf), local and global order and linear stability.
