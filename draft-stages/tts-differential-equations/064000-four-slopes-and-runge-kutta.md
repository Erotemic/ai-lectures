# Four Slopes and a Better Prediction: Runge–Kutta Methods from Scratch

<!-- BEGIN SPOKEN LECTURE -->

# Four Slopes and a Better Prediction

If a differential equation hands us the slope at any position, why not ask for the slope more than once before deciding where to go? Euler's method asks once, at the beginning of the interval. The midpoint method asks at the beginning and then halfway across. But those are just two choices in a much larger family. We can take several trial measurements of a changing rate, combine them carefully, and build a step that captures much more of the true solution's curvature.

This lecture develops the classical fourth-order Runge–Kutta method, often shortened to R K four. The name can make it sound like a black box. It is not. Its four intermediate slopes, with weights one, two, two, and one, are chosen to cancel several leading terms in the local error. We will carry out an entire step by hand, compare it to methods that use fewer evaluations, and then look at what a practical solver must do when it cannot know in advance how small a step should be.

## One equation, many possible algorithms

Start with an initial-value problem: y prime equals f of time and y, with a specified starting value. Let h be a step length. A numerical method that uses only the current time and state to construct the next state is called a one-step method. It may still make many internal trial evaluations of f during that step.

In explicit midpoint, we evaluate the slope at our starting state. That gives a provisional halfway state. We evaluate the slope there and use it to complete the step. This is already a two-stage Runge–Kutta method. A stage means one evaluation of the differential equation's right-hand side, at a chosen time and a chosen provisional state. A stage is not, by itself, an accepted point on the final solution trajectory.

One natural question is whether a more complicated method can be made arbitrarily accurate just by increasing the number of stages. There is a tradeoff. Different stages must be located and weighted so that the method's Taylor expansion agrees with the exact flow. Merely averaging any four slopes will not guarantee fourth-order accuracy. The classical four-stage formula is one successful choice, not a license to improvise weights.

## The four stages

Begin by evaluating the rate at the current state. Call that first slope k one. Use it to predict the state halfway forward. Evaluate the rate at this provisional midpoint; that is k two. Now make another midpoint prediction, but use k two instead of k one to reach it. Evaluate the rate again; that is k three. Finally, use k three to predict a state at the end of the full interval. Evaluate the rate there; that is k four.

We have sampled the rate at the beginning, at two successive estimates of the midpoint, and at an estimated endpoint. The final increment is h divided by six times k one plus twice k two plus twice k three plus k four.

Why give the midpoint slopes twice the weight? The method is designed so that when we expand the exact and numerical solutions in powers of h, the terms through the fourth power agree for smooth problems. The first four leading orders match; the local defect then begins at the fifth power. That statement can be proved by a systematic Taylor expansion or the algebra of Runge–Kutta order conditions. The simple weighted-average picture helps remember the formula, but it is not the proof of its order.

And the method is explicit: each temporary state can be calculated from earlier stages. No unknown future state appears in an equation that must be solved before the step can finish.

## Work through an entire step

Use the familiar equation y prime equals y, with y at time zero equal to one. The exact answer is exponential of t. Take one half as the step length. This is a moderately large step, so the differences will be visible.

The first slope is one. Use it to predict halfway: one plus one quarter times one gives one point two five. Thus the second slope is one point two five. Now use that second slope to predict halfway again: one plus a quarter times one point two five gives one point three one two five. That is the third slope. Finally, predict all the way to the end using the third slope: one plus a half times one point three one two five gives one point six five six two five. That is the fourth slope.

Now weight them. Add one, two times one point two five, two times one point three one two five, and one point six five six two five. The sum is seven point seven eight one two five. Multiply by one half divided by six, and add to the initial value one. The R K four result is one point six four eight four three seven five.

The exact exponential of one half is about one point six four eight seven two one three. We are off by roughly two point eight four ten-thousandths. The same interval with one Euler step gives one point five. Explicit midpoint gives one point six two five. R K four has made a substantially better prediction, although it used four rate evaluations rather than one or two.

An important caveat: for the equation y prime equals y, the R K four update happens to be the first five terms of the exponential series, through the fourth power of h. That is a satisfying check. Matching that one equation does not by itself prove fourth order for arbitrary nonlinear differential equations. The general theorem requires the appropriate order conditions for the stages.

## A system of equations needs the same four stages

Imagine a spring described by a position and a velocity. Position prime equals velocity; velocity prime equals negative position. Instead of computing four slopes of a scalar function, R K four computes four vectors of slopes. Each vector contains a proposed rate of position change and a proposed rate of velocity change. The formula and weights stay exactly the same.

This is one reason vector notation matters. We do not have to derive a different R K four algorithm for every physical system. We only have to supply the function f that evaluates the coupled rates. For a driven spring, f will depend on time. Each intermediate stage must use the stage's own time: halfway, halfway again, and the end of the interval. Mixing up the time arguments can ruin accuracy even if the state arithmetic is correct.

Classical R K four does not automatically preserve every physical feature of the underlying differential equation. For example, the exact undamped spring conserves an energy and traces a closed ellipse in phase space. Standard R K four can slowly alter the numerical energy over many steps. A high order of accuracy on fixed time intervals is not the same promise as exact energy conservation for unlimited time. Specialized geometric integrators address such questions, but ordinary R K four is a powerful baseline when the goal is accurate trajectories over a specified interval.

## The arithmetic of work and accuracy

Should we use one step of R K four, or four small steps of Euler? Both use four evaluations of f. Their errors are generally very different. The comparison is not just about how many times we call f; it is about how effectively those calls cancel the leading errors.

If a sufficiently smooth problem stays well behaved and we hold the final time fixed while shrinking h, Euler's global error typically decreases in proportion to h. Explicit midpoint's decreases proportionally to h squared. Classical R K four's decreases proportionally to h to the fourth power. These are asymptotic claims: they describe the pattern once the steps are small enough and numerical stability is under control. They do not say an R K four step of any size is trustworthy.

There is a practical twist. As a step becomes extremely small, floating-point rounding and the cost of additional function evaluations can matter. More steps do not always yield proportionally more useful digits. We should aim for enough accuracy, not infinitesimal steps as an end in themselves.

## Choosing the step while the solution is moving

A trajectory may vary slowly for a while and then bend sharply during a brief interval. Using one fixed step for the entire computation wastes effort in the calm region or misses detail in the rapidly changing region. An adaptive solver tries to estimate the error of a candidate step and decides whether to accept it, reject it, or adjust its next step size.

A simple idea is step doubling. Compare one step of length h with two steps of length h divided by two. If they agree closely, the method may be resolving the dynamics at that scale. If they disagree, it may need a smaller step. This comparison does not reveal the exact error automatically: both approximations can be wrong, and their difference has its own scaling. But with an established method order, the difference provides information that can guide step selection.

Modern explicit Runge–Kutta solvers often use an embedded pair. The same collection of intermediate slopes is combined with two different sets of weights to produce two estimates of different orders. Their difference is used as a local error indicator. The solver compares the estimated error with an absolute tolerance and a relative tolerance, adjusted for each state component's scale. It then chooses a new step rather than blindly keeping h fixed.

This is not a magical guarantee of global accuracy. A step controller monitors local error estimates, and it can still fail to detect a sharp event or use a method that is unstable for the dynamics. A model with discontinuous forcing, or a state variable that changes by orders of magnitude, requires care with event locations and error scales. And a stiff problem may demand a tiny explicit step for stability even when the trajectory is nearly motionless. We will return to that distinction.

## What to remember, not merely memorize

Euler, midpoint, and classical R K four all begin with the same information: a current state and a rule for computing its instantaneous derivative. They differ in how many provisional states they construct and how they combine the resulting slopes. Runge–Kutta methods turn local measurements of a changing rate into a carefully designed approximation to the flow of a differential equation.

The four-stage formula is worth knowing, but the reasoning is more transferable. A numerical method makes choices about where to sample, how to combine samples, how to estimate error, and how to set the time scale of a step. The accuracy order tells us how an error should decrease as the step size shrinks in a suitable regime. It does not tell us whether a huge step is stable, whether a conserved quantity is maintained forever, or whether our model has been formulated correctly.

The next mathematical challenge is to measure how one-step defects accumulate into a global discrepancy. Once we can distinguish consistency from error propagation, we will know what it actually means for a numerical trajectory to converge toward the solution we intended.

<!-- END SPOKEN LECTURE -->

## Mathematical companion: four-stage RK and order checks

For \(y'=f(t,y)\), classical explicit Runge–Kutta of order four is
\[
\begin{aligned}
k_1&=f(t_n,y_n),\\
k_2&=f(t_n+h/2,y_n+(h/2)k_1),\\
k_3&=f(t_n+h/2,y_n+(h/2)k_2),\\
k_4&=f(t_n+h,y_n+h k_3),\\
y_{n+1}&=y_n+\frac h6(k_1+2k_2+2k_3+k_4).
\end{aligned}
\]
The same scheme applies to vector-valued \(y\) without changing the coefficients.

### Worked example and local defect

For \(y'=y\), \(y_0=1\), \(h=1/2\), the slopes are \(k_1=1\), \(k_2=5/4\), \(k_3=21/16\), and \(k_4=53/32\). Therefore
\[
y_1=1+\frac{1/2}{6}\left(1+\frac{10}{4}+\frac{42}{16}+\frac{53}{32}\right)=\frac{211}{128}=1.6484375.
\]
The exact answer is \(e^{1/2}\approx1.6487212707\), so the one-step defect is approximately \(2.8377\times10^{-4}\). In general for this test equation, \(y_1=R(h)\) where
\[
R(z)=1+z+\frac{z^2}{2}+\frac{z^3}{6}+\frac{z^4}{24}.
\]
The match of \(R(z)\) with the exponential series through \(z^4\) confirms fifth-order local defect on this *particular* linear test; proving classical RK4 order four for general smooth nonlinear \(f\) requires the full Runge–Kutta order conditions.

### Why embedded estimates are informative, not exact

For a smooth, nonstiff IVP, a one-step method of order \(p\) started from the exact state has a local defect \(C(t,y)h^{p+1}+O(h^{p+2})\). Two approximations of different orders formed from shared stages can estimate a leading defect. A controller may use a formula involving \(\mathrm{tol}/\mathrm{err}\) raised to an exponent related to local order, with a safety factor and bounds on step-size changes. In general \(\mathrm{err}\) is an *estimate*; acceptance controls the estimated local error, not a rigorous global error bound.

### Exercises and answers

1. **Reproduce the four slopes.** For \(y'=y\), \(h=1/2\), find all stages. **Answer:** \((1,5/4,21/16,53/32)\).
2. **Compare simple methods.** Give one-step Euler and explicit midpoint for the same data. **Answer:** \(1.5\) and \(1.625\).
3. **Time-dependent forcing.** For \(y'=t\), \(y(0)=0\), \(h=1\), compute RK4. **Answer:** stages \(0,1/2,1/2,1\); output \((0+2(1/2)+2(1/2)+1)/6=1/2\), exactly the integral.
4. **Why is stage time relevant?** If \(f(t,y)=t\) and all stage evaluations mistakenly use \(t_n\), what happens? **Answer:** all rates are zero at the first step; the result is zero rather than \(1/2\).
5. **Order versus invariants.** Does fourth-order convergence on bounded time intervals imply exact oscillator energy conservation for arbitrarily long integrations? **Answer:** no; order and preservation of invariants are different properties.

### Sources and further reading

- Stuart Brorson, [*Numerically Solving Ordinary Differential Equations*, Chapter 4](https://math.libretexts.org/Bookshelves/Differential_Equations/Numerically_Solving_Ordinary_Differential_Equations_%28Brorson%29/04%3A_Predictor-corrector_methods_and_Runge-Kutta).
- Stuart Brorson, [Runge–Kutta methods](https://math.libretexts.org/Bookshelves/Differential_Equations/Numerically_Solving_Ordinary_Differential_Equations_%28Brorson%29/04%3A_Predictor-corrector_methods_and_Runge-Kutta/4.06%3A_Runge-Kutta_methods).
- SciPy developers, [solve_ivp reference: adaptive RK23, RK45, DOP853, and stiff methods](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html).
- Wikipedia: [Runge–Kutta methods](https://en.wikipedia.org/wiki/Runge%E2%80%93Kutta_methods), [Adaptive step size](https://en.wikipedia.org/wiki/Adaptive_step_size).
