# Step Inputs, Delays, and Impulses: Solving an Equation Across a Switch

<!-- BEGIN SPOKEN LECTURE -->

# Step Inputs, Delays, and Impulses

Imagine testing a thermostat. The room begins at its reference temperature. Two seconds into the experiment, a heater turns on. Three seconds later, it turns off. The temperature does not jump instantly to its new equilibrium: the heater changes the rate of warming, and the room takes time to respond. How do we write a single equation that records both switching events, rather than solve one time interval, then another, and hope we have matched them correctly?

We use a unit step, also called the Heaviside function. It is zero before the switching time and one after. A step is not an impulse. A step changes a force and then leaves it changed; an impulse delivers a finite amount of input in a vanishingly short interval. The distinction matters to both the mathematics and the physical prediction.

This lecture first handles switches that last a finite amount of time. Then we will let a narrow pulse shrink toward an ideal impulse and derive precisely which part of a system's state can jump.

## Describe a switch without breaking the time axis

Let u of t minus a mean the unit step that is zero when t is less than a and one when t is greater than a. The value at the single switching instant does not change any ordinary integral. We will assume a is positive so the event occurs after our initial time.

What is its Laplace transform? By definition, integrate the exponential weight times the step from zero to infinity. The integrand is zero before a. So the integral starts at a, and the result is the exponential of negative a s divided by s, for real s greater than zero.

This is the first place where the expression exponential of negative a s appears. It is a marker of time delay. A forcing that turns on later contributes the same algebraic shape as an immediate forcing, multiplied by a factor that records when it begins.

More generally, suppose g of t describes a signal beginning at time zero. Now wait until time a and play that same signal from its beginning. The delayed signal is u of t minus a, multiplied by g of t minus a. Substitute tau equal to t minus a in the defining transform integral. The result is the exponential of negative a s, multiplied by G of s, where G is the transform of g.

The argument shift inside g is indispensable. If a heater is programmed to ramp upward with elapsed time since it switched on, its input is the step at a times t minus a, not the step at a times t. The first starts its ramp from zero at the switch. The second begins immediately at height a.

For a concrete comparison, the delayed ramp u of t minus two times t minus two transforms to the exponential of negative two s divided by s squared. But u of t minus two times t equals the delayed ramp plus twice the delayed step. Its transform is the exponential of negative two s times the quantity one over s squared plus two over s. These are different physical inputs, so they must give different transforms.

## A heater that turns on once

Consider the simple response equation y prime plus y equals u of t minus two, with y at zero equal to zero. Before time two, the equation is y prime plus y equals zero. The initial value is zero, so the temperature deviation remains zero.

Transform the equation. The left-hand side becomes s Y plus Y, because the initial value vanishes. The forcing transforms to the exponential of negative two s divided by s. Thus Y equals the exponential of negative two s divided by s times s plus one.

Use partial fractions on the part without the delay: one over s times s plus one equals one over s minus one over s plus one. That inverts to one minus exponential of negative t. Apply the delay rule. The answer is zero before time two and, after time two, one minus the exponential of negative the elapsed time since two.

Check the behavior exactly. At the switch, the temperature is still zero, so y is continuous. Immediately after the switch, the right-hand side is one while y is zero, so y prime becomes one. At later times the temperature approaches one, the new equilibrium. The switch makes the derivative change, not the temperature itself.

Suppose the heater stays on only between time two and time five. The forcing becomes u of t minus two, minus u of t minus five. By linearity, the response is the delayed rise starting at two minus an identical delayed rise starting at five.

From time two to time five, we get one minus exponential of negative t minus two. At time five, the level has reached one minus exponential of negative three. After time five, the difference of the two delayed rises simplifies to one minus exponential of negative three, multiplied by the exponential of negative t minus five. That is the exact cooldown from the level reached when the heater turned off.

We did not have to glue two arbitrarily chosen formulas together. The two step terms automatically enforce continuity of the state. Still, it is wise to check the formula at the switching times and in each interval. A compact transform expression should never hide a physically incorrect jump.

## An impulse is an area, not a height

Now replace the sustained heat input with a short burst. Imagine a rectangular pulse with width epsilon and height three divided by epsilon, starting at time two. Its area is three, no matter how narrow it becomes. Let epsilon tend to zero. The height becomes unbounded and the width tends to zero, but the total delivered input remains three.

The idealized limit is written as three times delta of t minus two. Delta is the Dirac impulse. It is not an ordinary function that has a meaningful finite height at time two. It is best understood here by what it does under integration: when multiplied by a sufficiently nice test function and integrated across the event, it samples that function at the event time, multiplied by the impulse area.

For a positive event time a, the one-sided Laplace transform of delta of t minus a is exponential of negative a s. Compare this with the step transform, exponential of negative a s divided by s. The extra factor one over s records that a step persists; an impulse is a single idealized delivery.

Consider y prime plus y equals three delta of t minus two, with y at zero equal to zero. Transforming gives Y equal to three times exponential of negative two s divided by s plus one. In time, y is zero until two and equals three times exponential of negative elapsed time after two.

This time the state really does jump. Its value immediately before time two is zero, and its value immediately after is three. To verify the jump without invoking the transform, integrate the differential equation over a tiny interval enclosing time two. The integral of y prime gives the change in y. The integral of y is negligible in the limit if y remains locally bounded. The impulse contributes area three. The jump must therefore equal three.

A physical heating system has finite pulse width. The ideal impulse approximation is appropriate when the pulse is much shorter than the response time and its total effect is what matters. It does not mean that the room temperature becomes infinite.

## Position and velocity do not react the same way

What if the impulse acts on the acceleration of an ideal spring? Consider x double prime plus omega squared times x equals J times delta of t minus a, with zero initial displacement and velocity and positive omega.

Integrate through the impulse. The integral of x double prime equals the change in velocity. The spring term, involving displacement rather than a derivative, has a vanishing contribution over a shrinking interval if displacement stays bounded. The velocity jumps by J. Position remains continuous: the spring cannot teleport in response to a force impulse.

Once the impulse has ended, the spring oscillates freely from zero displacement with new velocity J. The solution after the event is J divided by omega times sine of omega times the elapsed time. Before the event it is zero. We can obtain exactly the same formula from the transform: the impulse contributes J times the delay factor, and the oscillator contributes one over s squared plus omega squared.

The difference between the first-order and second-order examples comes from where the input enters. A delta in a first-order state equation jumps the state. A delta force in a second-order position equation jumps velocity, while position stays continuous. In a larger system, impulse jump conditions follow from integrating the appropriate state equations, not from a rule that every variable must jump.

## What to verify at a switch

There are three separate checks. First, on each open interval between switching times, the formula must solve the ordinary differential equation with the correct forcing. Second, at an ordinary step, state variables that satisfy equations with locally integrable right-hand sides must have the appropriate continuity; their derivatives may jump. Third, at an impulse, integrate the equation across the event to determine the jump condition.

Remember too that the one-sided transform has a convention at time zero. We have put impulses at positive times to avoid mixing an impulse exactly at the initial boundary with a specified pre-impulse or post-impulse initial state. When a problem includes an event at zero, it must say which state convention it uses.

The broader story is that the factor exponential of negative a s is a faithful record of waiting. A delayed step changes the dynamics and leaves that change in place; a delayed impulse delivers an area at one instant. Both can be handled algebraically, but only if we preserve their meaning in time. Once we understand the response to one short pulse, we are ready to ask how the responses to an entire stream of tiny pulses accumulate. That accumulation is convolution.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

**Prerequisites:** 055000–056000, piecewise functions, exponentials and first-/second-order ODEs. **Conventions:** \(a>0\); \(u(t-a)\) is the Heaviside step (point value irrelevant); \(\delta(t-a)\) is the unit Dirac distribution supported at \(t=a\).

### Delay formulas

\[
\mathcal L\{u(t-a)\}(s)=\int_a^\infty e^{-st}\,dt=\frac{e^{-as}}s,
\qquad \mathcal L\{u(t-a)g(t-a)\}(s)=e^{-as}G(s).
\]
The second formula follows from \(\tau=t-a\). It is **not** generally true that \(\mathcal L\{u(t-a)g(t)\}=e^{-as}G(s)\). For instance,
\[
\mathcal L\{u(t-2)(t-2)\}=\frac{e^{-2s}}{s^2},\qquad
\mathcal L\{u(t-2)t\}=e^{-2s}\left(\frac1{s^2}+\frac2s\right).
\]

### On-off response

For \(y'+y=u(t-2)-u(t-5)\), \(y(0)=0\),
\[
Y(s)=\frac{e^{-2s}-e^{-5s}}{s(s+1)},
\]
\[
y(t)=u(t-2)\bigl(1-e^{-(t-2)}\bigr)-u(t-5)\bigl(1-e^{-(t-5)}\bigr).
\]
Piecewise this is \(0\) for \(t<2\), \(1-e^{-(t-2)}\) for \(2\le t<5\), and \((1-e^{-3})e^{-(t-5)}\) for \(t\ge5\). The state is continuous at both switches.

### Impulse jump conditions

For a test function \(\varphi\) continuous near \(a>0\), \(\int\delta(t-a)\varphi(t)\,dt=\varphi(a)\). Hence \(\mathcal L\{\delta(t-a)\}=e^{-as}\). Integrating \(y'+y=J\delta(t-a)\) across \(a\) gives \(y(a+)-y(a-)=J\), assuming \(y\) is locally bounded.

For a forced oscillator,
\[
x''+\omega^2x=J\delta(t-a),\quad x(0)=x'(0)=0
\quad\Longrightarrow\quad
x(t)=\frac J\omega u(t-a)\sin\bigl(\omega(t-a)\bigr).
\]
Here \(x\) is continuous and \(x'(a+)-x'(a-)=J\). In a distributional sense the second derivative contains the delta required by the forcing.

### Exercises with answers

1. Find \(\mathcal L\{u(t-4)e^{-2(t-4)}\}\). **Answer:** \(e^{-4s}/(s+2)\).
2. For \(y'+2y=u(t-1)\), \(y(0)=0\), give the exact solution. **Answer:** \(y(t)=\tfrac12u(t-1)(1-e^{-2(t-1)})\).
3. Express a pulse of height five over \([1,3)\) using steps. **Answer:** \(5[u(t-1)-u(t-3)]\); transform \(5(e^{-s}-e^{-3s})/s\).
4. If \(v'+4v=7\delta(t-3)\) and \(v(0)=0\), what happens at \(t=3\)? **Answer:** \(v\) jumps from zero to seven and then decays as \(7e^{-4(t-3)}\).
5. In the oscillator \(x''+9x=6\delta(t-2)\) with zero initial data, compute \(x'(2+)\). **Answer:** \(6\), while \(x(2+)=x(2-)=0\).

### Sources and further reading

- MIT OpenCourseWare, *18.03SC*, [Step and Delta Functions](https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/pages/unit-iii-fourier-series-and-laplace-transform/step-and-delta-functions-integrals-and-generalized-derivatives/).
- MIT OpenCourseWare, *18.03SC*, [Unit Step and Unit Impulse Response](https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/pages/unit-iii-fourier-series-and-laplace-transform/unit-step-and-unit-impulse-response/).
- Wikipedia: [Heaviside step function](https://en.wikipedia.org/wiki/Heaviside_step_function), [Dirac delta function](https://en.wikipedia.org/wiki/Dirac_delta_function).
