# From Rate Laws to Initial-Value Problems: Reading an Equation Before Solving It

<!-- BEGIN SPOKEN LECTURE -->

# From Rate Laws to Initial-Value Problems

Imagine setting a cup of tea on a kitchen table. You can measure its temperature now, but how would you predict its temperature ten minutes from now? If you knew the temperature at every future moment, you would know the answer. A differential equation turns that task around. It proposes a rule for the rate of change and asks which future curves obey it.

This is a course in changing quantities, not a course in memorizing integrations. We will learn to read an equation, check the units, translate it into a picture, and make a numerical prediction even when no formula comes to mind. Along the way, we will distinguish three things that people sometimes collapse into one: a differential equation, a family of solutions, and a particular initial-value problem.

## A rate law is not yet a trajectory

Let T stand for the temperature of tea, measured in degrees, and t for time, measured in minutes. Suppose the room temperature remains twenty degrees. Newton's cooling model says that the rate at which the tea temperature changes is proportional to the difference between the tea and the room. In words, T prime equals negative k times T minus twenty, where k is a positive constant with units inverse minutes.

That negative sign is not decoration. When T is eighty degrees, T minus twenty is positive and the derivative is negative: cooling. When T is ten degrees, the difference is negative and the derivative is positive: warming toward the room. When T is exactly twenty degrees, the derivative is zero. Twenty is an equilibrium.

Now suppose k is one tenth per minute and the tea starts at eighty degrees. The rate at the initial instant is negative six degrees per minute. If we temporarily pretend that rate remains constant for one minute, we predict seventy-four degrees after the first minute. But the rate will not remain constant: at seventy-four degrees the model says the rate is negative five point four degrees per minute. The model constantly updates its own slope according to the current state.

Notice what we have specified. The differential equation tells us the slope at each possible pair of time and temperature. The initial condition says that at time zero the temperature is eighty degrees. Together they form the initial-value problem. Without the initial temperature, the model allows many trajectories approaching the same room temperature from different starting points.

The same structure occurs far beyond temperature. The population of an idealized organism might grow at a rate proportional to population. A bank balance might accumulate interest continuously. A chemical concentration might decay at a rate proportional to its current concentration. Different subjects, same mathematical task: find the function whose derivative follows the rule.

## Read the units before doing algebra

Consider the temperature equation once more. The derivative has units degrees per minute. The difference between the tea and the room has units degrees. Consequently k must have units inverse minutes. If someone reports k as six degrees per minute, the proposed equation has inconsistent units.

This test cannot prove the model is correct, but it can catch a faulty model before a page of algebra begins. If we rescale time from minutes to seconds, the numerical value of k must change by a factor of sixty. The physical cooling process should not change just because the clock label does.

What does the equation predict qualitatively? It predicts the direction of change, an equilibrium, and a characteristic timescale. Because the rate is proportional to the current temperature excess, the excess shrinks faster when it is large and more slowly when it is small. It does not decrease by the same six degrees each minute. A linear decrease in temperature would contradict the stated rate law.

## Slope fields: the equation as a picture

Imagine a graph with time running horizontally and temperature vertically. At each point, draw a tiny line segment whose slope equals the derivative prescribed by the equation. At a temperature of eighty, the segment slopes down steeply. At forty it slopes down more gently. At twenty it is horizontal. Below twenty it slopes upward. The collection of these little segments is called a direction field or slope field.

A solution curve follows those segments tangentially. Different initial temperatures give different curves through the same field. For an equation in which the rate depends only on the current state, not directly on the time, the slopes are the same across each horizontal row. Such an equation is called autonomous.

We can already describe the shape of a cooling curve without knowing its exact formula: it decreases when above room temperature, it flattens as it approaches room temperature, and it never changes direction unless it reaches an equilibrium or the model itself changes. These conclusions come from examining signs, not from guessing a function.

Direction fields are also a reality check. If a proposed formula climbs while the prescribed slopes point downward, no clever integration can rescue it. We have learned to test an answer against the problem before producing one.

## Predict with short steps: Euler's method

Suppose we have no symbolic solution, or the equation is complicated enough that solving by hand is inconvenient. We can still move forward from a known point. If the current value is y and the current slope is f of t and y, then over a short step of duration h we estimate the change in y as h times that slope.

That gives Euler's method: next value equals current value plus step size times current slope. It is the tangent-line approximation repeated over and over. The method produces a sequence of numbers rather than a closed formula.

For our tea model, start at eighty degrees, k one tenth per minute, and choose steps of one minute. The initial rate is negative six, so the first estimate is seventy-four. The next rate is negative five point four, so the second estimate is sixty-eight point six. A third step uses negative four point eight six and gives sixty-three point seven four.

The method is easy enough to do with a pencil, but it makes an approximation every step. The exact temperature after two minutes is twenty plus sixty times the exponential of negative zero point two. That is about sixty-nine point one two degrees. Euler gave sixty-eight point six. Its result is slightly too cool because it held each downward rate fixed throughout a step, although the rate became less negative as the tea cooled.

Take much smaller steps, and for this smooth model the approximation improves over any fixed time interval. But smaller steps are not a guarantee for every possible equation or every requested final time. Some equations become unstable under explicit Euler when the step is too large relative to a fast decay rate. A simple algorithm can fail numerically even when the underlying physical solution is calmly approaching equilibrium.

## What is a solution, exactly?

A solution is a differentiable function defined on some interval, with its derivative matching the rate law at each point in that interval. An initial condition selects a value at a specified time. We must also report the interval on which the formula actually solves the equation.

Consider y prime equals y squared, beginning at y equal to one at time zero. The function one divided by one minus t satisfies this equation. Check it: differentiating gives one divided by the square of one minus t, which equals the square of y. At time zero it equals one. But when t approaches one from below, the function grows without bound. The formula is not a solution through t equal to one, and it cannot be continued there as a finite differentiable trajectory.

This is a useful antidote to a common misconception. The right-hand side y squared is a perfectly smooth function of y. Local smoothness can ensure a trajectory exists near the initial time, yet still allow that trajectory to become infinite in finite time. A solution interval is a mathematical conclusion, not an optional footnote.

We should also separate a prediction from its model's assumptions. A cooling law may neglect evaporation, changing room temperature, or the cup's heat capacity. A population law may neglect food limits and random events. Solving the equation exactly does not make the model of reality exact. Mathematical rigor tells us what follows from our assumptions; experiment tells us whether those assumptions fit the situation.

## A second model: filling a tank

Imagine a well-mixed tank containing one hundred liters of liquid. Pure water enters at two liters per minute, and the mixed liquid leaves at two liters per minute, so the volume stays constant. Suppose ten grams of dissolved salt are present initially.

Let S be grams of salt. The incoming salt rate is zero. The outgoing salt concentration is S divided by one hundred grams per liter. Multiply by two liters per minute to obtain S divided by fifty grams per minute leaving. So the rate equation is S prime equals negative S divided by fifty.

This time a units check is especially helpful. S divided by fifty minutes is grams per minute, just what a time derivative of S should be. The equation predicts decreasing salt concentration. Its solution will be exponential, but even before solving it we know that if there is no salt, the output contains none; the zero state is an equilibrium.

This model exposes a subtlety in translation. The word 'well mixed' is mathematically essential: it allows the outgoing concentration to equal the current average concentration. If the incoming and outgoing volumes differed, the volume would change, and the denominator would have to change with it. A correct algebraic solution to the wrong tank model is still the wrong prediction.

## What to ask first

For any new first-order differential equation, start by asking: what quantity is changing, what are its units, and what assumptions determine the rate? Next: what are the equilibria, and which direction do nearby states move? Then: what initial data have been supplied? Finally: do we want a symbolic solution, a qualitative explanation, a numerical approximation, or all three?

These questions create a reliable habit. They also prepare us for equations that cannot be integrated in elementary functions. Differential equations are not defined by the availability of a tidy formula. They are defined by a local rule for change and the trajectories that obey it. Once that idea is clear, solving a particular first-order equation becomes meaningful rather than merely procedural.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

**Preparation:** Derivatives, exponentials, elementary function graphs, basic arithmetic. **Central objects:** direction fields, initial-value problems, units, Euler approximation, maximal solution interval.

For the cooling law, with temperature in degrees and time in minutes,
\[
T'(t)=-k(T-20),\quad k=0.1\,\mathrm{min}^{-1},\quad T(0)=80,
\quad T(t)=20+60e^{-0.1t}.
\]
This yields the exact two-minute value \(T(2)=20+60e^{-0.2}\approx69.12385\). Euler with \(h=1\) gives \(T_1=74\), \(T_2=68.6\), \(T_3=63.74\). The Euler error at \(t=2\) is \(-0.52385\) degrees. The method is applied to the **excess** temperature \(z=T-20\) by \(z_{n+1}=(1-kh)z_n\); it is stable for this scalar decay when \(|1-kh|<1\), i.e. \(0<kh<2\), though nonoscillatory decay requires \(0<kh\le1\).

For a tank with constant volume \(V=100\) liters and inflow/outflow \(q=2\) liters per minute, \(S'=-qS/V\), \(S(0)=10\), so \(S(t)=10e^{-t/50}\) grams. This model depends on instantaneous mixing and constant volume.

The equation \(y'=y^2\), \(y(0)=1\), has \(y=(1-t)^{-1}\) on its maximal interval \(( -\infty,1)\). A smooth right-hand side gives local well-posedness but not global boundedness.

### Exercises with answers

1. A reservoir loses \(3\%\) of its contents per hour *continuously*. Write its idealized rate law and solution for \(M(0)=200\). **Answer:** \(M'=-0.03M\) and \(M(t)=200e^{-0.03t}\); \(0.03\) has units per hour.
2. Perform two Euler steps of length \(1/2\) for \(y'=-2y,\; y(0)=3\). **Answer:** \(y_1=0,\;y_2=0\). The exact value at \(t=1\) is \(3e^{-2}>0\), showing the impact of too-large steps.
3. For \(y'=2-y\), locate equilibria and predict motion starting at \(y=5\). **Answer:** equilibrium \(y=2\); the solution initially decreases and tends toward 2.
4. Why does equal input and output volume matter in the tank model? **Answer:** It fixes the volume, making the concentration proportional to \(S/100\) rather than \(S/V(t)\).

### Reading and references

- MIT OpenCourseWare, *18.03 Differential Equations*, first-order direction fields and Euler's method: https://ocw.mit.edu/courses/18-03-differential-equations-spring-2010/pages/lecture-notes/
- OpenStax, *Calculus Volume 2*, Chapter 4, basic differential equations and direction fields: https://openstax.org/books/calculus-volume-2/pages/4-introduction
- Wikipedia: [Differential equation](https://en.wikipedia.org/wiki/Differential_equation), [Euler method](https://en.wikipedia.org/wiki/Euler_method), [Newton's law of cooling](https://en.wikipedia.org/wiki/Newton%27s_law_of_cooling).
