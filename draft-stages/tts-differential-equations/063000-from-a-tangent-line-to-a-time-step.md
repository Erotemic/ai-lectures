# From a Tangent Line to a Time Step: Euler, Midpoint, and Numerical Trajectories

<!-- BEGIN SPOKEN LECTURE -->

# From a Tangent Line to a Time Step

Suppose we know how fast a population is changing at every possible population size, but we do not know a formula for the population at noon tomorrow. That is a normal situation. The differential equation tells us the instantaneous rate, not necessarily a closed-form solution. A numerical method turns this local information into a sequence of predictions. The central question is not whether a computer can repeat an arithmetic rule. It is which arithmetic rule makes a reliable approximation to the continuous trajectory.

We will construct three rules directly from calculus. First, Euler's method follows the tangent line. Then the midpoint method estimates the slope partway through the next step. Finally, the improved Euler method averages a starting slope and an estimated ending slope. We will calculate their answers on a problem whose true solution is known. That lets us see what each method gains and, just as importantly, what each one still gets wrong.

## An initial-value problem is a promise about a slope

Write the rate law as y prime of t equals f of t and y of t, with y at time zero given. The input f takes a time and a state and returns a rate. If y measures temperature in degrees and t measures seconds, f must have units of degrees per second. We need this distinction because a method for stepping forward must multiply a rate by a time interval before adding it to a state.

Choose a sequence of times separated by a positive step length h. At the first time we know the exact initial value. After that, we store estimates, not the true values. Call the estimate at the n-th time y sub n. It is tempting to write an equals sign between the stored number and the true solution. Avoid that: the difference between those two quantities will be the subject of our error analysis.

If the slope barely changed during one short interval, the next state would be approximately the current state plus h times the current slope. That sentence is Euler's method. Evaluate f at the current time and current estimate; multiply by h; add the result. No future value is needed. This is an explicit method: every new value is computable directly from numbers already in hand.

The rule is a moving tangent line. At the current point, we know the direction the exact solution would initially take. We pretend it keeps that direction for an entire interval, then draw a new tangent at our new approximate position. The true solution may bend between these points. Each time we ignore that bending, we incur an error.

## A complete Euler calculation

Take the differential equation y prime equals y squared, with initial value one. It is deliberately simple enough that we can compare a numerical step to an exact answer. Separating variables gives the exact solution one divided by one minus t. It exists for times strictly less than one. The denominator warns us that no numerical method should be expected to sail through time one as if the smooth solution continued.

Let our first step be one fifth of a time unit. At time zero, the state is one and its rate is one squared, or one. Euler says add one fifth times one. The prediction at time one fifth is one point two. The exact solution at the same time is one divided by point eight, or one point two five. We are low by point zero five, a four percent error relative to the exact value.

This is not a failed calculation. It is a faithful calculation for a low-accuracy approximation. The method used the initial slope of one throughout the whole interval, even though the true rate grows as y grows. For a convex increasing solution, the tangent line lies below the curve. The sign of the error has a geometric explanation.

Try dividing the interval into two Euler steps of length one tenth. The first value is one point one. Its new rate is one point one squared, or one point two one. The next value is one point one plus one tenth times one point two one, which is one point two two one. That is closer to one point two five than the single long step, but it is still low. Two steps involve two slope evaluations instead of one. Smaller steps often buy accuracy by spending more work.

We have just compared the answer at a fixed final time, not merely the error made during one isolated step. The distinction will matter later: errors from earlier steps alter the slopes used in all subsequent steps.

## Sampling a slope halfway through

Can we do better without taking many tiny steps? The most obvious weakness of Euler is that it uses only the starting slope. The explicit midpoint method asks what the slope might be halfway across the interval. We do not know the halfway state, so we first predict it with a half-length Euler step. We evaluate f at that predicted midpoint. Then we use this middle slope over the full interval.

For our example, start again at y equals one and take h equal to one fifth. The starting slope is one. A half step is one tenth, so our estimated midpoint state is one point one. At the midpoint the rate estimate is one point one squared, or one point two one. Multiply that by the full interval, point two, and add to one. The explicit midpoint answer is one point two four two.

Compare the results: Euler gives one point two, midpoint gives one point two four two, and the exact solution gives one point two five. The midpoint error is point zero zero eight. That is far smaller for this particular step. We must not conclude from a single example that midpoint always has an eight-thousandth error, or that it always lies below the true value. The behavior depends on the differential equation, the step size, and the current state.

There is a subtle point in the construction. The midpoint prediction does not have to be an accurate final answer. It only has to locate the slope well enough that using it across the whole step cancels the leading error. Calculus gives us a precedent: the midpoint rule for definite integration usually improves on using a rectangle of the starting height. Numerical ODE methods adapt that idea, but the height being sampled is now a derivative that depends on the evolving state.

## Another second-order idea: average two slopes

The improved Euler method, also called Heun's explicit trapezoidal method, makes a different prediction. Start with an Euler step all the way to the end, solely to estimate the ending slope. Average that predicted ending slope with the starting slope. Use the average to update the actual state.

In the same example, Euler's provisional endpoint is one point two, whose square is one point four four. The starting slope was one. Their average is one point two two. Multiplying by point two gives point two four four, so the improved Euler answer is one point two four four. It is also close to the exact one point two five, with error point zero zero six.

Do not confuse explicit trapezoidal Heun with the implicit trapezoidal method. The implicit version evaluates the end slope at the unknown new state and requires an equation to be solved. Heun uses the provisional Euler value instead. The distinction is important when we later ask which methods remain stable for very fast decay.

Midpoint and Heun use two evaluations of f per step, but choose different places at which to sample. Both are called second-order methods. That term does not mean they use second derivatives, nor does it guarantee that the second one wins on every problem. It describes how global error generally scales when we make the step smaller over a fixed time interval, under suitable smoothness and stability assumptions.

## What the computer actually repeats

A scalar equation fits on a notepad. Real models often contain several coupled states: position and velocity, concentrations in different compartments, or currents and temperatures. Put these into a vector and let f return a vector of rates. Exactly the same Euler and midpoint formulas work, replacing scalar addition and multiplication with vector arithmetic. A system of ten ordinary differential equations does not require ten different integration methods.

What does require care is the meaning of the step. A step of point two seconds may be small for an object moving slowly but enormous for an electrical circuit whose fastest transient lasts one thousandth of a second. The differential equation determines the relevant time scales. Units and physical interpretation are not optional decorations on the algorithm.

To implement any of these rules, keep the current pair of time and state, evaluate f at precisely the locations prescribed by the rule, and update both time and state. The intermediate predictions are temporary, not new accepted solution points. If f depends explicitly on time, its time argument must advance for the midpoint or end slope. Accidentally evaluating all slopes at the starting time silently changes the method and, often, its order of accuracy.

As a diagnostic, substitute the computed state back into the original equation conceptually. Does a positive growth rate cause an increase? Is a conserved quantity drifting? Does the numerical solution cross a boundary that the true model cannot cross? None of these checks proves accuracy, but they can expose a mistaken step, an inappropriate step size, or even a flawed model.

## A method is more than its first answer

Return one last time to y prime equals y squared. Its exact solution blows up at time one. For small steps and times safely before one, Euler, midpoint, and Heun can approximate it with improving accuracy as h decreases. Close to time one, the rate becomes very large and the same fixed step no longer resolves the change well. A method that worked acceptably at time point two may fail badly near point nine. Numerical accuracy is a statement about an interval and its hypotheses, not a permanent badge earned by an algorithm.

There are two distinct decisions in numerical integration: how to approximate one step, and how large that step should be. Euler is cheap but crude. Midpoint and Heun spend an additional slope evaluation to cancel a leading error. We have built each from an ordinary calculus idea and checked it against a solvable initial-value problem.

Next in the mathematics, without needing to change the model itself, we can sample four carefully chosen slopes to obtain a much more accurate Runge–Kutta step. But the larger question remains: even a sophisticated single step is only useful if accumulated errors and numerical stability are understood. We now have the concrete update rules needed to study both.

<!-- END SPOKEN LECTURE -->

## Mathematical companion: exact update rules and worked verification

For an IVP \(y'=f(t,y)\), \(y(t_0)=y_0\), set \(t_n=t_0+nh\) and denote an approximation to \(y(t_n)\) by \(y_n\). For a vector state, all formulas are interpreted componentwise.

**Forward Euler:**
\[
y_{n+1}=y_n+h f(t_n,y_n).
\]

**Explicit midpoint (two evaluations):**
\[
k_1=f(t_n,y_n),\qquad k_2=f(t_n+h/2,y_n+(h/2)k_1),\qquad y_{n+1}=y_n+h k_2.
\]

**Heun, or explicit trapezoidal (two evaluations):**
\[
k_1=f(t_n,y_n),\quad k_2=f(t_n+h,y_n+h k_1),\quad y_{n+1}=y_n+\frac h2(k_1+k_2).
\]

### Worked IVP: \(y'=y^2\), \(y(0)=1\), \(h=1/5\)

The exact solution is \(y(t)=1/(1-t)\) for \(t<1\). Its value at \(h\) is \(5/4=1.25\). The three updates are
\[
\begin{aligned}
\text{Euler: }&1+\tfrac15=1.2,\\
\text{Midpoint: }&1+\tfrac15(1+\tfrac1{10})^2=1.242,\\
\text{Heun: }&1+\tfrac1{10}\bigl(1+(1+\tfrac15)^2\bigr)=1.244.
\end{aligned}
\]
Their one-step absolute errors are \(0.05\), \(0.008\), and \(0.006\), respectively. Two Euler steps of length \(h/2=0.1\) yield \(1.1\) and \(1.1+0.1(1.1)^2=1.221\).

### Why the midpoint formula is second order

For a sufficiently smooth scalar solution, \(y(t+h)=y(t)+h f+(h^2/2)(f_t+f_yf)+O(h^3)\), with derivatives of \(f\) evaluated at \((t,y(t))\). The midpoint slope is
\[
f(t+h/2,y+(h/2)f)=f+(h/2)(f_t+f_yf)+O(h^2).
\]
Multiplying by \(h\) matches the exact Taylor expansion through \(h^2\); the one-step defect from an exact starting value is \(O(h^3)\). Under stability and smoothness assumptions, fixed-time global error is \(O(h^2)\). The stronger global statement requires an error-propagation argument, not just this expansion.

### Exercises with answers

1. **Euler with a time-dependent rate.** Let \(y'=t+y\), \(y(0)=1\), \(h=0.2\). Find one Euler step. **Answer:** \(1+0.2(0+1)=1.2\).
2. **Midpoint on the same problem.** **Answer:** estimate \(y(0.1)=1.1\), evaluate \(f(0.1,1.1)=1.2\), return \(1+0.2(1.2)=1.24\).
3. **Check the y-squared example.** Compute the error in a single midpoint step. **Answer:** \(|1.25-1.242|=0.008\).
4. **Use a vector state.** For \(\mathbf z'=(-x,-2v)\), initial \((x,v)=(1,1)\) and \(h=0.1\), compute Euler. **Answer:** \((0.9,0.8)\).
5. **Know the domain.** Why does \(y'=y^2\), \(y(0)=1\) not have a finite continuous solution through \(t=1\)? **Answer:** \(y(t)=1/(1-t)\) diverges as \(t\uparrow1\); reducing a numerical step cannot remove this genuine singularity.

### Sources and further reading

- Stuart Brorson, [*Numerically Solving Ordinary Differential Equations*, Chapters 1, 2 and 4](https://math.libretexts.org/Bookshelves/Differential_Equations/Numerically_Solving_Ordinary_Differential_Equations_%28Brorson%29).
- Stuart Brorson, [Midpoint method](https://math.libretexts.org/Bookshelves/Differential_Equations/Numerically_Solving_Ordinary_Differential_Equations_%28Brorson%29/04%3A_Predictor-corrector_methods_and_Runge-Kutta/4.04%3A_Midpoint_method).
- Wikipedia: [Euler method](https://en.wikipedia.org/wiki/Euler_method), [Midpoint method](https://en.wikipedia.org/wiki/Midpoint_method), [Heun's method](https://en.wikipedia.org/wiki/Heun%27s_method).
