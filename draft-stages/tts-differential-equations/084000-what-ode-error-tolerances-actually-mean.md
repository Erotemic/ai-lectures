# What ODE Error Tolerances Actually Mean: Scale, Units, and Accuracy

<!-- BEGIN SPOKEN LECTURE -->

# What ODE Error Tolerances Actually Mean

A differential-equation solver asks you for an absolute tolerance and a relative tolerance. You enter two small numbers, perhaps one millionth and one thousandth. It is tempting to treat them as promises: every answer is correct to six decimal places, or every computed value has only a tenth of a percent error. Neither interpretation is generally justified.

A numerical solver does not know the exact solution. Its tolerances define a *test on estimated local errors*, and the meaning of that test depends on the scale of each quantity being integrated. To use these settings responsibly, we need to understand how the test is assembled, what units it has, and what the solver is not promising.

## A trajectory with two very different quantities

Imagine a model that evolves a vehicle's position in meters and velocity in meters per second. The current position is about one thousand meters, while its velocity is close to zero: two thousandths of a meter per second. A proposed integration step produces estimated local errors of half a meter in position and three ten-thousandths of a meter per second in velocity.

Which error is worse? A half-meter position error may be completely acceptable when the vehicle is a kilometer from the origin. A three ten-thousandths velocity error looks numerically tiny, but it is fifteen percent of the current tiny velocity. More importantly, whether that error is acceptable depends on what the velocity means in the model. If we are locating a turning point, small velocities may be the central subject.

We cannot compare a number expressed in meters with a number expressed in meters per second using a single raw norm. Even changing meters to centimeters would change the result of that comparison without changing the underlying physics. The error test must first make each component dimensionless.

A common approach assigns each component a scale equal to its absolute tolerance plus its relative tolerance multiplied by a representative magnitude of the state component. The magnitude may be taken from the old state, new state, or the larger of the two; implementations differ in that detail. The estimated local error is divided by the corresponding scale. The result is a dimensionless error ratio.

Let's choose a relative tolerance of one thousandth for both components. For position, use an absolute tolerance of one hundredth of a meter. For velocity, use an absolute tolerance of one ten-thousandth of a meter per second. These absolute tolerances have different physical units, as they must.

At a position of one thousand meters, the relative part of its scale is one meter. Add one hundredth, giving roughly one point zero one meters. A half-meter estimated error is therefore about zero point four nine five times its allowed scale. This component passes individually.

At a velocity of zero point zero zero two meters per second, the relative part of the scale is only two millionths of a meter per second. Add the absolute tolerance of one ten-thousandth, giving zero point zero zero one zero two meters per second. Divide the error of zero point zero zero zero three by that scale. The ratio is about two point nine four. This component fails.

We can combine these dimensionless ratios into a single number. One common choice is their root-mean-square value: square them, average the squares, and take the square root. Our two ratios produce a score about two point one one. Since this is greater than one, the attempted step fails that particular test even though the position component looked fine.

A maximum norm would also reject the step, because at least one component exceeds one. The precise norm depends on the solver; the indispensable idea is scaling each component *before* combining them.

## Relative tolerance needs an absolute floor

Why not set the absolute tolerance to zero and request purely relative error? Because a solution component can pass through zero. At zero, the relative scale would be zero, and no finite nonzero estimated error could pass. Even near zero, relative error can become a poor measure of what we physically care about.

Consider a damped oscillator. Its position repeatedly crosses zero. That does not mean the solver should take infinitely small steps at every crossing. We usually care about the accuracy of the whole orbit, including its amplitude and phase, not about maintaining a fixed fractional position error exactly where the position vanishes. An absolute tolerance provides a nonzero scale for these crossings.

The absolute tolerance also encodes information about units and measurement. A sensor may reliably report position to a millimeter but not to a nanometer. Demanding a numerical error much smaller than the uncertainty in input data does not make the physical prediction more reliable. There are exceptions, such as numerical experiments investigating model sensitivity, but tighter arithmetic is not a substitute for better data.

In a chemical reaction model, concentrations of two species might differ by eight orders of magnitude. A single absolute tolerance applied uniformly can effectively ignore a species with tiny concentration, even when that species controls the reaction rate. An array of component-specific absolute tolerances is often appropriate. Better still, nondimensionalize the equations using meaningful characteristic scales, if the physical model permits it.

Nondimensionalization has another benefit. If we switch from seconds to milliseconds, derivatives and step lengths change numerically, but the underlying trajectory should not. A well-scaled numerical problem makes it easier to choose tolerances that reflect the actual desired resolution rather than an accident of chosen units.

## A test on the error estimate, not on the error itself

The solver's two approximations are not independent measurements of reality. They can share an error that their difference fails to reveal. They can also disagree for reasons other than the leading truncation term, such as roundoff, loss of smoothness, or a severe cancellation. The estimate is usually informative in the regime for which its mathematical derivation is valid. It is not a certificate for every conceivable problem.

Suppose a fifth-order Runge–Kutta method produces an accepted step based on a companion fourth-order estimate. The acceptance score tells us that the estimated *one-step* error is small relative to the chosen component scales. Over a thousand steps, the accumulated solution error depends on the stability and conditioning of the differential equation. The final state can be substantially less accurate than the per-step tolerance might suggest.

This distinction is particularly important for unstable or chaotic flows. If nearby exact trajectories separate exponentially, two integrations at different tolerances may eventually disagree in their detailed trajectories. That may be mathematically consistent with the model, not necessarily evidence of an implementation error. The right validation may concern short-time predictions, averaged quantities, invariant measures, or other specific observables.

Even in a stable problem, reducing relative tolerance by a factor of one hundred does not guarantee the error of every output will shrink by exactly that factor. The controller may change its step pattern, switch between limiting absolute and relative scales, or hit the floor of floating-point accuracy. A solver can also run out of feasible step size near a singularity or model breakdown.

## Output points are not integration steps

A further source of confusion arises when we ask for results at a neat grid of times: zero, one, two, three, and so on. Many modern solvers choose their own internal time steps and interpolate a continuous approximation to return the requested values. Asking for one output value each second does not necessarily mean the integrator took one-second steps.

This is usually a convenience. The solver can take many short steps near fast motion and longer ones when the solution is smooth, while still reporting the result on a regular schedule. But interpolation has error of its own, and a coarse requested output grid may miss a peak even if the underlying integrator followed the trajectory accurately. Event detection requires separate attention, which we will address in the next lecture.

A maximum-step setting is not the same as a tolerance. It deliberately prevents the solver from leaping across more than a given interval, perhaps because a forcing function changes abruptly or because the user needs adequately dense event searches. It can be useful, but it can also make the computation needlessly expensive. The choice should come from the model's behavior or the question being asked.

## Diagnosing a solver result

Here is a practical experiment. Take a model whose exact solution is unknown, and run it once with chosen tolerances. Record not just the final state, but also the solver's success status, number of function evaluations, rejected steps when exposed, and any warnings. Then tighten the tolerances and compare an actual quantity of interest: the time a chemical concentration reaches a threshold, the largest oscillator amplitude, or the final position.

If the quantity stabilizes as the requested error decreases, that is evidence of numerical convergence. It is not proof of physical model accuracy, but it is useful evidence. If it changes dramatically, inspect the equation: is it stiff, nearly singular, discontinuous, chaotic, or poorly scaled? Perhaps the solver should be implicit, an event should be handled explicitly, or the output quantity is inherently sensitive.

You can sometimes derive independent estimates. For a known exponentially decaying solution, compare against the exact exponential. For a conservative mechanical system, monitor energy and explain which numerical method should approximately or exactly conserve it. For a population model that should remain nonnegative, watch for negative values. Such checks are often more revealing than printing a long list of solver digits.

## What tolerances should communicate

An absolute tolerance sets a floor on the local error scale for each quantity. A relative tolerance sets a scale proportional to the magnitude of that quantity when it is large. The solver estimates a local error, normalizes it by those scales, and decides whether to accept a proposed step. That is the meaning of the controls.

It is a meaningful and powerful contract, but a narrower one than a promise of globally correct digits. To make good predictions, we must choose the scales deliberately, read the solver's status, compare solutions when uncertainty matters, and judge errors against the physical question. Accuracy is not one number entered in a settings box. It is an argument we assemble from numerical evidence and the mathematics of the model.

<!-- END SPOKEN LECTURE -->

## Mathematical companion: componentwise tolerance scales

Let \(e\in\mathbb R^m\) be the estimated local error vector. A representative scale (one common convention, not a universal solver contract) is
\[
 s_i = \mathrm{atol}_i + \mathrm{rtol}\max\{|y_{n,i}|,|y_{n+1,i}|\},
 \quad r_i=\frac{|e_i|}{s_i},\quad
 \mathrm{err}_{\mathrm{RMS}}=\sqrt{\frac1m\sum_{i=1}^m r_i^2}.
\]
Accepting a step when \(\mathrm{err}_{\mathrm{RMS}}\le1\) is a choice of norm/controller; other packages use other norms and magnitude conventions.

For \(y=(1000\ \mathrm{m},0.002\ \mathrm{m/s})\), \(e=(0.5\ \mathrm{m},0.0003\ \mathrm{m/s})\), \(\mathrm{rtol}=10^{-3}\), and \(\mathrm{atol}=(0.01\ \mathrm{m},10^{-4}\ \mathrm{m/s})\), assuming old and new magnitudes about the quoted values,
\[
 s_1=1.01\ \mathrm{m},\quad s_2=0.000102\ \mathrm{m/s},\quad
 r_1\approx0.49505,\quad r_2\approx2.94118,
\]
\[
 \mathrm{err}_{\mathrm{RMS}}\approx2.109\ (>1).
\]
The failure is driven by the small-scale velocity component. Dimensional consistency requires \(\mathrm{atol}_i\) to have the units of \(y_i\), while \(\mathrm{rtol}\) is dimensionless.

For a solution with a Lipschitz continuous right-hand side and a suitable convergent method, local truncation errors enter a recurrence that can be bounded via a discrete Gronwall argument. Neither the scaled acceptance test nor Gronwall's inequality alone turns \(\mathrm{rtol}\) into a final relative-error guarantee. To assess an observable \(Q(y)\), compare \(Q\) across tolerances, methods, and physically independent checks.

### Exercises and worked answers

1. For a state component near zero, which part of \(\mathrm{atol}+\mathrm{rtol}|y|\) dominates? **Answer:** the absolute tolerance, unless it was set negligibly small.
2. A model's length state is converted from meters to centimeters. What must happen to its absolute tolerance to preserve the same physical scale? **Answer:** multiply the numerical tolerance by one hundred; relative tolerance is unchanged.
3. Compute the normalized RMS error for \(r=(0.6,0.8)\). **Answer:** \(\sqrt{(0.36+0.64)/2}=\sqrt{1/2}\approx0.707\), so this RMS test passes.
4. Two solver runs agree on a final observable but disagree on individual internal steps. Is that contradictory? **Answer:** no. Adaptive meshes are algorithmic choices; compare quantities of interest and convergence, not internal step timestamps.
5. Why might a uniformly tiny absolute tolerance be inefficient or misleading in a multiscale model? **Answer:** it can overresolve irrelevant quantities while still representing meaningful small components poorly relative to their physical scales.

### Sources and further reading

- [SciPy `solve_ivp`: `rtol`, `atol`, output interpolation and solver status](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html).
- [SUNDIALS CVODE: numerical error weights and local error tests](https://sundials.readthedocs.io/en/develop/cvode/Mathematics_link.html).
- [SUNDIALS introduction to adaptive time stepping (Lawrence Livermore National Laboratory)](https://computing.llnl.gov/sites/default/files/2025-10/2025-SUNDIALS-Introduction-APPFPP.pdf).
