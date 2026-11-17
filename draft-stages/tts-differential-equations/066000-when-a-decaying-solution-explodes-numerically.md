# When a Decaying Solution Explodes Numerically: Stability, Stiffness, and Implicit Steps

<!-- BEGIN SPOKEN LECTURE -->

# When a Decaying Solution Explodes Numerically

Consider a differential equation whose exact solution shrinks rapidly toward zero. It is one of the least threatening-looking motions imaginable. Yet a numerical calculation may alternate between huge positive and huge negative values, growing larger at every step. The equation is stable; the computation is not.

This is the distinction we need to complete our foundation in numerical time stepping. Accuracy describes how closely a numerical method follows the true solution at a given resolution. Numerical stability asks whether small disturbances are controlled or amplified by repeated application of the update rule. A method can have high order of accuracy when its steps are sufficiently small and still behave disastrously at a step size that seems modest compared with the time interval we are studying.

We will derive the stability condition of forward Euler, compare it with backward Euler, and use a simple two-component model to explain stiffness. The point is not to recommend an implicit algorithm for every problem. It is to see exactly what a time integrator must respect when a system contains both fast and slow dynamics.

## The easiest stable equation

Take y prime equals negative fifteen times y, starting at one. The rate is always negative while y is positive. The exact solution is exponential of negative fifteen t. After a fifth of a time unit, it is exponential of negative three, about point zero four nine eight. The state is already close to zero. After more time it becomes smaller still. A small perturbation in the initial value also shrinks exponentially.

Now use Euler's formula: new y equals old y plus h times the rate at old y. Substituting negative fifteen y gives new y equals one minus fifteen h, times old y. This multiplication factor completely determines the numerical trajectory. It is not an approximation we have to guess about; it is the exact formula of the discretized method on this equation.

With h equal to point two, one minus fifteen h is one minus three, or negative two. Euler's numerical values are one, negative two, four, negative eight, sixteen, and so on. They alternate signs and double in magnitude. The true solution is racing toward zero while the numerical solution races away from it.

This is not caused by a bug in the arithmetic. The algorithm is faithfully carrying out its own update equation. The issue is that one tangent-line extrapolation spans too much of the fast decay. It overshoots zero, and the next tangent based on the overshoot reverses direction. Repeated overshoots amplify rather than cancel.

## Derive the stability interval

For a decay equation y prime equals negative lambda times y, with lambda positive, forward Euler multiplies by one minus h lambda. The numerical values approach zero as the number of steps increases exactly when the absolute value of this multiplier is less than one.

This requirement gives a simple condition: h lambda must lie strictly between zero and two. If h lambda is smaller than one, each numerical value stays positive and decays. If h lambda lies between one and two, the signs alternate but the magnitudes shrink. At h lambda equal to two, the multiplier is negative one, so values alternate without decay. Above two, their magnitudes grow. The exact solution, by contrast, decays for every positive lambda and every positive time.

For lambda fifteen, the Euler step must therefore be smaller than two fifteenths, about point one three three, for asymptotic numerical decay. At h equal to point one the multiplier is negative point five: stable but alternating. At h equal to point zero five, the multiplier is positive point two five: stable without sign reversal. Even the latter is not especially accurate during the very rapid first transient. Stability is necessary for a meaningful long calculation, but it is not by itself a guarantee of small error.

The example shows why an adaptive controller that monitors only apparent smoothness may be misleading. A trajectory can be nearly stationary after its fast transient while an explicit method still has to respect a short stability-limited step. That restriction may persist long after the fast component has become physically negligible.

## The same idea with complex growth rates

In a linear system, modes are often associated with eigenvalues. We can understand the stability of a one-step method by first applying it to the scalar test equation y prime equals lambda y, where lambda may be complex. The exact mode decays when the real part of lambda is negative.

For forward Euler the multiplication factor is one plus h lambda. The method damps the numerical mode only when the magnitude of that complex factor is less than one. In the complex plane, the admissible values of h lambda lie inside a disk of radius one centered at negative one. This is called Euler's region of absolute stability.

Why is the region a disk rather than a half-plane? Because Euler approximates the exponential evolution by a first-degree polynomial. Far into the left half-plane, the exact exponential is extremely small, but one plus h lambda may be enormous. A more accurate polynomial for small steps can have a larger region, yet every explicit Runge–Kutta method with finitely many stages has a polynomial stability function. No such polynomial stays bounded throughout the entire left half-plane. This limitation becomes important for stiff equations.

The scalar test is informative but not a complete analysis of every nonlinear or strongly nonnormal system. Interactions among modes, transient amplification, variable coefficients, and nonlinear effects require further work. We are using it to diagnose a real failure mechanism, not to certify all possible problems.

## Turn the slope around: backward Euler

Forward Euler uses the derivative at the start of a step. Backward Euler uses the derivative at its end. Its rule says new y equals old y plus h times f evaluated at the new time and the unknown new state. That makes it an implicit method: the update is an equation to solve, not merely an expression to evaluate.

On the decay equation, new y equals old y minus h lambda times new y. Gather the new y terms on one side. The result is new y equals old y divided by one plus h lambda. Instead of multiplying by one minus h lambda, we divide by one plus h lambda.

For the earlier choice lambda fifteen and h point two, the factor is one quarter. The numerical sequence is one, one quarter, one sixteenth, and so on. It is positive and decaying for every positive h. On the complex test equation the factor is one divided by one minus h lambda; for every lambda with negative real part, its magnitude is less than one regardless of step size. Backward Euler is called A-stable because its absolute stability region contains the entire open left half-plane, and also its boundary in the usual nonamplifying sense where the formula is defined.

There is a price. One backward Euler step of length point two estimates the true value at that time as point two five, while the exact value is only about point zero four nine eight. The numerical solution is stable, but its estimate of the initial fast decay is coarse. If we care about resolving that brief transient precisely, we still need small steps. Implicit stability does not repeal accuracy requirements.

On a nonlinear equation, backward Euler may demand solving a nonlinear algebraic equation at every step, often using Newton's method. The computational work per step is higher, and a solution of the algebraic equation may not be unique without further assumptions. The benefit is the possibility of taking much larger stable steps in problems where explicit stability would impose severe restrictions.

## Two time scales in the same system

Now consider a model with two independent decaying quantities. Let x prime equal negative x and z prime equal negative one thousand z. Start both at one. The slow variable x changes on a time scale of roughly one unit. The fast variable z changes on a time scale of roughly one thousandth of a unit. After a very short interval, z is effectively gone, while x continues to evolve slowly.

Forward Euler must keep h smaller than two thousandths to damp the fast mode, even if our main interest is the slow variable over ten whole time units. That means more than five thousand steps to traverse the slow interval, simply to keep the rapidly decaying z component from exploding numerically. The slow equation alone would not need such a fine time grid for comparable accuracy.

This is the basic difficulty of stiffness. The system contains dynamics that force a small explicit stability step, although the behavior we want to follow may occur on a much longer scale. Stiffness is not synonymous with a large derivative, a difficult formula, or merely a large coefficient. It describes a mismatch between the step required for explicit stability and the step justified by accuracy for the behavior of interest.

Using backward Euler at h equal to one tenth, the slow component multiplies by one divided by one point one, about point nine zero nine. The fast component multiplies by one divided by one hundred and one, about point zero zero nine nine. Both decay. The fast component's numerical value at the end of that first large step is much larger than its exact, almost vanished value. So we have sacrificed accuracy in the fast transient. But once the fast part no longer matters to our chosen outputs, the method can follow the slow motion without an explicit stability restriction set by one thousand.

This example is diagonal, so we can see every component. Coupled stiff systems are harder, and whether a fast mode can safely be ignored depends on coupling, initial data, and the quantities we need to predict. A stability interval derived from a single scalar mode cannot answer every such question. It is still a valuable first test.

## Choosing an integrator is part of modeling

A numerical solution should be judged against the task. If we need precise oscillation phases, damping rates, or rapid transients, we must resolve them. If we need slow evolution after a brief relaxation, a stiffly stable implicit solver may be more efficient. If we care about long-term energy or symplectic geometry, another class of integrators may be better. The mathematically right method depends on what must be accurate and which qualitative properties matter.

Widely used ODE software reflects this choice. Explicit adaptive Runge–Kutta methods are usually sensible starting points for nonstiff initial-value problems. Implicit Runge–Kutta or backward-differentiation methods are common choices for stiff problems. That is an algorithmic distinction, not a claim that any particular solver is perfect or that one option is universally faster.

We now have a coherent way to assess a time-step calculation. Begin with the ODE and its time scales. Derive or inspect the update rule. Check the local approximation error and its propagation over the time interval. Examine the method's stability on relevant modes, and distinguish damping of numerical disturbances from the true motion's stability. Finally, refine the time grid and inspect physically meaningful observables, rather than trusting a single successful run.

A solution that should decay toward zero must not explode merely because we selected a convenient step size. Understanding why that can happen, and how an implicit step changes the answer, is the bridge from elementary differential equations to the numerical methods used in scientific computing.

<!-- END SPOKEN LECTURE -->

## Mathematical companion: absolute stability and a stiff two-mode test

For the scalar test equation \(y'=\lambda y\) with \(\Re\lambda<0\) and \(z=h\lambda\), a one-step method has an amplification factor \(R(z)\). **Absolute stability** on the test problem means \(|R(z)|\le1\) (strict \(<1\) for decay).

| Method | Amplification factor \(R(z)\) | Real-negative-axis stability |
|---|---|---|
| Forward Euler | \(1+z\) | \(-2<z<0\) for strict decay |
| Explicit midpoint | \(1+z+z^2/2\) | \(-2<z<0\) for strict decay |
| Backward Euler | \(1/(1-z)\) | every \(z<0\) |

For forward Euler, the complex stability region is \(|1+z|\le1\), a disk centered at \(-1\) with radius one. For backward Euler, if \(\Re z\le0\), then \(|1-z|\ge1\), so \(|R(z)|\le1\). Thus backward Euler is A-stable on the scalar test equation. In addition \(R(z)\to0\) as real \(z\to-\infty\), a strong-damping property useful for stiff decay.

### A single rapidly decaying mode

For \(y'=-15y\), \(y(0)=1\), \(h=0.2\):
\[
\begin{array}{ll}
\text{Exact: }&y(h)=e^{-3}\approx0.0497870684,\\
\text{Forward Euler: }&y_1=(1-15h)y_0=-2,\\
\text{Backward Euler: }&y_1=y_0/(1+15h)=1/4.
\end{array}
\]
Both discrete approximations are inaccurate on this large first step; only backward Euler produces a decaying sequence. For the forward method, strict damping requires \(0<h<2/15\). At \(h=0.1\), the factor \(-0.5\) decays but alternates sign.

### The two-scale system

\[
\begin{pmatrix}x'\\z'\end{pmatrix}=
\begin{pmatrix}-1&0\\0&-1000\end{pmatrix}
\begin{pmatrix}x\\z\end{pmatrix},\quad (x(0),z(0))=(1,1).
\]
Forward Euler must have \(h<0.002\) to damp both modes. Backward Euler at \(h=0.1\) gives \((x_1,z_1)=(1/1.1,1/101)\); the exact values are \((e^{-0.1},e^{-100})\). Its stiff component is stable but not accurately resolved at \(t=0.1\).

### An implicit nonlinear step

For \(y'=-y^2\) with \(y_n>0\), backward Euler requires solving
\[
y_{n+1}=y_n-hy_{n+1}^2
\quad\Longleftrightarrow\quad
hy_{n+1}^2+y_{n+1}-y_n=0.
\]
The positive root is \(y_{n+1}=\bigl(\sqrt{1+4hy_n}-1\bigr)/(2h)\), which may be evaluated more stably as \(2y_n/(1+\sqrt{1+4hy_n})\). In general an implicit step can need a nonlinear solve; its existence, uniqueness, and numerical solution must not be assumed without checking.

### Exercises and answers

1. **Explicit stability.** For \(y'=-4y\), what positive Euler steps give strict numerical decay? **Answer:** \(0<h<1/2\).
2. **Oscillation without blow-up.** What happens at \(h=0.4\) for this same equation? **Answer:** amplification \(1-4(0.4)=-0.6\), alternating signs with shrinking magnitude.
3. **Implicit stability.** Compute the backward Euler factor for \(y'=-4y\), \(h=1\). **Answer:** \(1/(1+4)=1/5\), stable though not equal to \(e^{-4}\).
4. **Fast and slow.** For eigenvalues \(-2\) and \(-200\), what Euler restriction arises from the fast mode? **Answer:** \(h<2/200=0.01\).
5. **Stability versus accuracy.** Is the backward Euler value \(1/4\) for \(y'=-15y\) at \(t=0.2\) accurate merely because it decays? **Answer:** no; the exact value is approximately \(0.0498\), so the first-step absolute error is about \(0.2002\).

### Sources and further reading

- Stuart Brorson, [Forward Euler stability](https://math.libretexts.org/Bookshelves/Differential_Equations/Numerically_Solving_Ordinary_Differential_Equations_%28Brorson%29/02%3A_Forward_Euler_method/2.09%3A_Stability) and [stiff ODEs](https://math.libretexts.org/Bookshelves/Differential_Equations/Numerically_Solving_Ordinary_Differential_Equations_%28Brorson%29/05%3A_Adaptive_stepping/5.03%3A_Stiff_ODEs).
- SciPy developers, [solve_ivp reference: explicit RK versus implicit Radau and BDF](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html).
- Wikipedia: [Stiff equation](https://en.wikipedia.org/wiki/Stiff_equation), [A-stability](https://en.wikipedia.org/wiki/A-stability), [Backward Euler method](https://en.wikipedia.org/wiki/Backward_Euler_method).
