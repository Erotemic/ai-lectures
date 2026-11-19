# When a Solver Chooses Its Own Time Steps: Adaptive ODE Integration

<!-- BEGIN SPOKEN LECTURE -->

# When a Solver Chooses Its Own Time Steps

An ordinary differential equation describes change continuously, but a numerical method moves forward in jumps. We learned how Euler's method uses one slope, how midpoint and Runge–Kutta methods use several, and why a smaller step can improve accuracy. That leaves an awkward practical question. How small should the step be?

For a slowly changing solution, taking ten thousand tiny steps wastes time. When a solution turns sharply, those same steps might not be small enough. Choosing one fixed step for the entire interval asks us to predict the hardest part of a problem before we have solved it. Adaptive integration replaces that guess with a local question, asked repeatedly: do we have enough evidence to trust this proposed step?

The answer is never perfect. The solver does not know the exact future trajectory, which is precisely why we need it. It constructs an estimate from two related approximations, compares that estimate with a requested error scale, and accepts or rejects the attempted move. The important word is *attempted*. A proposed step is not a commitment.

## Two approximations from the same starting point

Consider the initial-value problem whose rate of change is the negative of the current value, and whose initial value is one. Its exact solution is the exponential decay function. We know that answer, but imagine that we do not. We'll use it afterward to check the numerical reasoning.

Start at time zero with value one and propose a step of length one. Euler uses the initial slope, negative one, all the way across. Its prediction is zero. Heun's method, sometimes called the explicit trapezoidal method, first makes that same Euler prediction, measures the slope at the predicted endpoint, and averages the two slopes. At the predicted endpoint zero, the slope is zero. The average of negative one and zero is negative one half, so Heun predicts one half.

We now have two proposed values, zero and one half, for the same future time. Their difference is one half. That difference warns us that a whole unit of time is too ambitious. But what exactly does it estimate?

Euler's error over a single step, starting from exact data, is typically proportional to the square of the step length. Heun's corresponding error is typically proportional to the cube. The difference between the two approximations is therefore mainly measuring Euler's lower-order error, not exactly measuring the smaller error of the higher-order approximation. A controller using the higher-order result should treat the difference as a conservative or indirect error indicator, not as a certified numerical bound.

For this particular decay equation we can compute the two formulas without knowing the exact exponential. Starting from a general positive value, Euler multiplies it by one minus the step length. Heun multiplies it by one minus the step length plus half the square of the step length. Their difference is the starting value times half the square of the step length.

With starting value one and proposed length one, the difference is one half. With length one tenth, Euler predicts zero point nine and Heun predicts zero point nine zero five. Their difference is only zero point zero zero five. If the acceptable one-step discrepancy in this simple illustration is one hundredth, the first attempt fails and the second passes. The exact exponential at one tenth is about zero point nine zero four eight four; Heun's actual one-step error is about one point six ten-thousandths, substantially smaller than the estimated difference. We have learned why a discrepancy is useful without mistaking it for the exact error.

## Rejecting a step is normal work

Imagine a control rule that asks for a discrepancy no larger than one hundredth. At step length one, our estimate is fifty times too large. Since the difference scales like the square of the step in this example, dividing the step by the square root of fifty would bring the estimate near the target. A cautious controller applies a safety factor as well. It may try a length close to one tenth rather than exactly the predicted boundary.

The failed attempt has not advanced time. We do not record its inaccurate endpoint as the next state. We return to the same initial state, evaluate the equation on a shorter interval, and only then commit the accepted approximation. A solver that rejects a step is not necessarily broken. It is performing a normal part of error control.

Once a step is accepted, it is also not compulsory to keep its length. If the estimated discrepancy is much smaller than the requested amount, the next step can grow. Conversely, an approaching rapid transition can make the next proposal shrink. A practical controller limits how much the step may grow or shrink, because highly aggressive changes can cause a cycle of overconfident proposals and rejections. It also checks for step sizes too small to advance floating-point time meaningfully.

Notice the tradeoff: every rejection costs derivative evaluations, but an accepted step that is needlessly small also costs evaluations. Adaptive integration is an attempt to spend computational work where the evolving solution needs it.

## Why real solvers use embedded Runge–Kutta pairs

Our Euler–Heun comparison is easy to derive by hand, but efficient software does not usually calculate two entirely unrelated methods at every step. An *embedded Runge–Kutta pair* shares the intermediate slope evaluations. It combines those slopes using one set of weights to produce one approximation, and another set to produce a companion approximation of a different order. Subtracting the two gives an error indicator at relatively little extra cost.

The widely used Runge–Kutta five-four pair is named for its fifth- and fourth-order formulas. Its difference behaves, in the usual smooth regime, like the leading one-step error term of the fourth-order member: the fifth power of the step length. That is why a simple controller for this estimated quantity uses a fifth root when adjusting the next step. An Euler–Heun difference is quadratic in the step, so its corresponding power was a square root instead. The exponent is derived from how the estimate scales, not from a rule that all adaptive methods share one favorite power.

For a system of equations, the candidate state contains several numbers. We do not compare each raw difference to a single physical tolerance measured in unspecified units. The next lecture will construct the scaled error test used for vector-valued states. For now, think of an error score: below one means that the proposed step passes the local test, and above one means it fails. The controller tries to make that score neither wildly below nor above one.

## Local error is not the final answer's error

A crucial warning: the solver's acceptance test concerns an estimate for one step, conditional on its starting state. The starting state itself is already approximate. The discrepancy between two formulas is not the same as the discrepancy between the computed state and the unknown exact trajectory at the final time.

If errors introduced at each step are amplified by the differential equation, a long trajectory can accumulate a substantial global error even though every local test passed. Near a stable equilibrium, errors may shrink; along an unstable trajectory, they may grow. Both behaviors are properties of the differential equation as well as of the integrator.

For example, suppose a system has one direction in which perturbations double over each unit of time. Even a small error made early may become important much later. Tightening a local tolerance can reduce that seed, but it cannot abolish the mathematical amplification. In chaotic systems, close individual trajectories can diverge while ensemble or statistical features remain meaningful. Error control helps, but it does not create unlimited predictive time.

We therefore distinguish three checks. An accepted step has passed the solver's *estimated local* error test. A convergence experiment solves the same problem at tighter tolerances and compares the resulting trajectories or quantities of interest. An independent mathematical check asks whether the solution respects properties such as conservation, positivity, or known asymptotic behavior. These checks answer different questions.

## Smoothness, discontinuities, and workload

Adaptive formulas are derived using Taylor expansions or comparable smoothness assumptions. They work best when the right-hand side behaves smoothly over a proposed step. Suppose a heater turns on at exactly two seconds. If the solver evaluates a derivative both before and after that switch without being told about the discontinuity, an adaptive error estimate may detect something wrong and shorten the step. But it is generally better to represent the switch as a known boundary between integration segments, or ensure the solver explicitly handles the change. Step adjustment is not a reliable substitute for specifying the model's discontinuities.

Likewise, if a system oscillates rapidly with a small amplitude, an error test might allow steps that are inaccurate for locating individual peaks even if the total state error passes its criteria. If the purpose is to measure peak times, we must use a method and output resolution appropriate to that purpose. An acceptable state tolerance is not automatically an acceptable event-time tolerance.

And if a rapidly decaying component forces a tiny explicit step for stability, simply requesting looser error may not rescue efficiency. That is stiffness, which we discussed with implicit Euler. Error control and stability control interact, but they are not the same thing. Some problems warrant an implicit solver instead of indefinitely shrinking explicit steps.

## A useful mental model

Imagine walking through an unfamiliar canyon with a map drawn from local slope measurements. You propose a stride, make two predictions of where that stride would land, and compare them. If they disagree too much, you do not pretend to have walked there. You shrink the stride and calculate again. If they agree extremely closely, you may lengthen the next stride. But the map may have a long-term navigational bias, and a cliff marked by an abrupt change still requires attention beyond ordinary slope comparison.

An adaptive ODE solver works in roughly that way. It makes trial predictions, measures disagreement, accepts or rejects the step, and chooses the next amount of work. The mathematics of the controller comes from the order of the numerical approximation; its limitations come from the difference between local numerical evidence and global dynamical truth. Knowing both makes adaptive integration a tool we can reason about rather than a black box labeled accurate.

<!-- END SPOKEN LECTURE -->

## Mathematical companion: a two-level local error controller

For the scalar test equation \(y'=-y\), a proposed step from exact input \(y_n\) gives
\[
Y_E=y_n(1-h),\qquad Y_H=y_n(1-h+h^2/2),\qquad
E=Y_H-Y_E=y_nh^2/2.
\]
At \(y_n=1,h=1\), \(Y_E=0\), \(Y_H=1/2\), and \(E=1/2\). At \(h=0.1\), \(Y_E=0.9\), \(Y_H=0.905\), and \(E=0.005\). The exact value is \(e^{-0.1}=0.904837418\ldots\); the Heun local error is \(0.000162582\ldots\). The pair difference primarily estimates the lower-order Euler local error, whose leading term has size \(h^2/2\).

If an error indicator obeys \(\|E(h)\|\approx C h^{p+1}\), the naive next step to target normalized error \(\eta\) is
\[
 h_{\mathrm{new}} = h\left(\frac{\eta}{\|E(h)\|}\right)^{1/(p+1)}.
\]
In practice multiply by a safety factor below one and clamp growth/shrinkage; if the estimate is based on the lower-order member of an embedded \(p+1,p\) pair, the usual exponent is \(1/(p+1)\). Estimates can lose their asymptotic scaling near discontinuities or cancellation.

Local error starting from exact data is not the global error. For a method of global order \(p\) applied on a bounded interval under suitable smoothness and stability assumptions, the global error is typically \(O(h^p)\) for fixed step \(h\). This statement alone is not a guarantee that a user-prescribed adaptive tolerance equals the final absolute error.

### Exercises and worked answers

1. Starting from \(y_n=2\) with \(h=0.2\), compute Euler, Heun, and their difference for \(y'=-y\). **Answer:** \(Y_E=1.6\), \(Y_H=1.64\), \(E=0.04\).
2. A quadratic error indicator is eight times the target. What multiplicative step change would bring it to the target without a safety factor? **Answer:** \(1/\sqrt{8}\approx0.3536\).
3. An embedded four-five pair's estimator scales as \(h^5\). Estimate the new step if normalized error is thirty-two and the target is one. **Answer:** multiply by \(32^{-1/5}=1/2\), before safety factors.
4. Why isn't a rejected trial point part of the numerical trajectory? **Answer:** the accepted trajectory advances only after the local test passes; the failed point was a tentative estimate from the previous accepted state.
5. Can every locally accepted step guarantee a globally accurate final value? **Answer:** no. Accumulation and dynamical amplification of earlier errors are not controlled by a single-step test.

### Sources and further reading

- [SciPy `solve_ivp`: adaptive Runge–Kutta pairs, tolerances, and step controls](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html).
- [SUNDIALS CVODE Mathematical Considerations: local error tests and adaptive steps](https://sundials.readthedocs.io/en/develop/cvode/Mathematics_link.html).
- [Wikipedia: Embedded Runge–Kutta methods](https://en.wikipedia.org/wiki/Runge%E2%80%93Kutta_methods#Adaptive_Runge%E2%80%93Kutta_methods).
