# 002000 — Phase Lines and Stability: Predicting Motion Without Solving an Equation

**Track:** Differential Equations and Dynamical Systems. **Background:** first-order differential equations and derivatives. **Question:** what can the signs of a rate law tell us about long-run behavior?

<!-- BEGIN SPOKEN LECTURE -->

# Phase Lines and Stability

Many differential equations cannot be solved in elementary functions. Even when a formula exists, the formula may obscure the behavior we care about. We might want to know whether a population approaches an equilibrium, whether a perturbation dies out, or whether a state is driven away from a seemingly steady configuration.

For a one-dimensional autonomous differential equation, much of that behavior can be read directly from a single function and its sign. This is the idea of the phase line: study the motion of the state rather than first searching for an explicit function of time.

## From slopes to arrows

An autonomous equation has the form the derivative of y equals f of y. The rate depends on the current state, not explicitly on the time. Where f is positive, a solution rises as time increases. Where f is negative, it falls. Where f equals zero, a constant solution is possible: the state remains at an equilibrium.

Draw a line representing all possible state values. Mark the zeros of f. Between consecutive zeros, if f is continuous, its sign cannot change without passing through another zero. So one arrow for each interval describes the direction of all trajectories while they remain there. We can inspect the qualitative pattern without integrating anything.

Consider the logistic equation, whose rate is y times one minus y. It has equilibria at zero and one. For y between zero and one, both factors are positive, so the arrow points upward. For y greater than one, the first factor is positive and the second negative, so the arrow points downward. For y below zero, the first factor is negative and the second is positive, so their product is negative; the arrow also points downward.

The resulting portrait is simple. States between zero and one rise toward one. States above one decrease toward one. Nearby positive states move toward one from either side. Near zero, positive states move away from zero, while negative states move farther negative. Thus zero is unstable and one is asymptotically stable with respect to nearby real states.

We have to interpret “population” carefully. Negative populations are physically meaningless in the ordinary model. The mathematical phase line includes them, but if the intended state space is nonnegative, we should state that restriction. For any positive starting population, the logistic solution exists for all future time and approaches one in our normalized units.

## Stability is a statement with quantifiers

An equilibrium y star is stable in the sense of Lyapunov if any sufficiently small initial disturbance remains small for all future time. More precisely, for every desired tolerance around the equilibrium, there must exist an initial tolerance such that starting within the initial tolerance keeps the trajectory within the desired tolerance forever.

Asymptotic stability requires more: the equilibrium is stable, and all trajectories starting sufficiently near it converge to it as time grows. An equilibrium may be stable without being attractive. For instance, when the rate is identically zero, every point is an equilibrium. Starting near a chosen equilibrium leaves the state at that nearby starting point forever. It never runs away, so the chosen equilibrium is stable, but trajectories do not generally converge to it.

The distinction matters when someone says that a numerical simulation has “settled.” A state can move slowly without converging to an equilibrium. Stability is a property of the mathematical flow and perturbations, not merely a visual impression of a flat plot.

## Linearization near an equilibrium

Suppose f is differentiable at an equilibrium y star. For a state just a little away, write y as y star plus a small perturbation z. Taylor's approximation gives f of y star plus z approximately f of y star plus f prime of y star times z. The first term is zero because y star is an equilibrium. So the perturbation approximately obeys z prime equals f prime of y star times z.

We already know the behavior of that linear equation. If the derivative f prime at the equilibrium is negative, small perturbations shrink exponentially in the linear approximation. If it is positive, some small perturbations grow. With the usual smoothness and well-posedness assumptions, a negative derivative proves local asymptotic stability in one dimension; a positive derivative proves instability.

For the logistic rate f of y equals y minus y squared, the derivative is one minus two y. At zero it equals one, confirming instability. At one it equals negative one, confirming local asymptotic stability. Our sign-chart argument already described the global behavior for positive initial states; linearization tells us about the local rate of return near one.

It is worth distinguishing the strength of these conclusions. A derivative sign at one equilibrium is local information. It does not by itself guarantee that every initial condition in the state space converges there. A global conclusion requires an argument about the whole relevant region, as the phase line provided for positive logistic states.

## When the linear term vanishes

What if f prime at the equilibrium is zero? Linearization then predicts z prime approximately zero and reveals nothing decisive. The neglected nonlinear terms can determine the entire stability picture.

Compare two equations at zero. In the first, the derivative of y equals negative y cubed. For positive y, the rate is negative and the state moves down toward zero. For negative y, the rate is positive and the state moves upward toward zero. The equilibrium at zero is asymptotically stable, though the return is slower than the exponential decay suggested by a strictly negative linear derivative.

In the second equation, the derivative of y equals positive y cubed. Positive states rise away from zero and negative states fall away. The equilibrium is unstable. In both equations, the derivative of the rate law at zero equals zero. The linear approximation is identical; the nonlinear behavior is opposite.

This is why a zero eigenvalue, or a zero derivative in one dimension, signals that a more careful analysis is required. Calling such an equilibrium stable because the linear model does not grow would be a mistake. A vanishing linear term is inconclusive.

## Solve the logistic equation as a check

We can verify our qualitative prediction with an explicit solution. For positive initial y zero, separation of variables leads to y of t equals y zero times the exponential of t divided by one plus y zero times the exponential of t minus one. Equivalently, y is one divided by one plus a constant times the exponential of negative t, with the constant determined by the starting value.

For positive y zero, the denominator stays positive for all nonnegative time. As time grows, the exponential of negative t tends to zero. Therefore y tends to one. If y zero is less than one, it increases; if y zero is greater than one, it decreases. These conclusions match the phase line.

At y zero equal to zero, the solution is the constant zero solution. For negative y zero, the formula can have a denominator that reaches zero in finite positive time, leading to blow-up toward negative infinity. The exact solution exposes a domain issue that the arrows alone do not resolve. Again, qualitative analysis and existence analysis complement each other.

## What changes in higher dimensions

In a system with several state variables, the phase line becomes a phase portrait in a plane or higher-dimensional space. Equilibria are states at which every component of the vector field vanishes. The linearization is a matrix, the Jacobian, and its eigenvalues help determine local behavior.

If every eigenvalue has strictly negative real part, a sufficiently smooth autonomous system has a locally asymptotically stable equilibrium. If at least one eigenvalue has strictly positive real part, the equilibrium is unstable. When eigenvalues have zero real part and none has positive real part, linearization can be inconclusive. These statements depend on the correct Jacobian and on local hypotheses; they are not a substitute for a global nonlinear analysis.

One-dimensional autonomous systems have an additional simplification under uniqueness: a nonconstant solution cannot cross an equilibrium, because doing so would conflict with the constant solution through that equilibrium. So the state remains in a region between equilibria. In higher dimensions, trajectories can move around equilibria, spiral, or cycle, and the geometry becomes richer.

## Prediction without a closed form

We began with a rate law and asked what it could tell us before solving. Zeros revealed equilibria. Signs gave directions. The derivative at an equilibrium gave a local linear test when nonzero. Explicit formulas then confirmed and sharpened the picture where they were available.

This approach is not a shortcut around mathematics. It separates questions: existence and uniqueness, local stability, domains of trajectories, and global attraction. A long exact formula may answer none of these transparently. A phase portrait, supported by theorems, can answer several of them at once. That is why dynamical systems is a subject in its own right, not merely a catalog of integration techniques.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For \(y'=f(y)\), equilibria satisfy \(f(y_*)=0\). If \(f\) is \(C^1\), then \(f'(y_*)<0\) implies local asymptotic stability and \(f'(y_*)>0\) implies instability in one dimension. A zero derivative is inconclusive.

**Logistic example:**
\[
y'=y(1-y),\quad f'(y)=1-2y,\quad y_*=0,1.
\]
For \(y_0>0\),
\[
y(t)=\frac{y_0e^t}{1+y_0(e^t-1)}\longrightarrow1
\qquad(t\to\infty).
\]
The sign of \(y(1-y)\) shows motion toward one for all positive states. Negative initial states need separate maximal-interval analysis.

**Nonhyperbolic counterexamples:** \(y'=-y^3\) is asymptotically stable at zero; \(y'=y^3\) is unstable, though both have \(f'(0)=0\).

**Higher-dimensional linearization:** For \(x'=F(x)\), \(J=DF(x_*)\). All eigenvalues \(\Re\lambda<0\) imply local asymptotic stability; an eigenvalue \(\Re\lambda>0\) implies instability, under usual \(C^1\) hypotheses. Eigenvalues on the imaginary axis require nonlinear analysis when no unstable eigenvalues are already present.

### Exercises with answers

1. Find equilibria of \(y'=y(2-y)\). **Answer:** Zero and two.
2. Which equilibrium in the preceding equation attracts nearby positive states? **Answer:** Two; the rate points toward it on both sides.
3. Does \(f'(y_*)=0\) prove stability? **Answer:** No; compare \(y'=\pm y^3\).
4. Can the logistic solution with \(y_0=1/2\) reach the equilibrium one at a finite positive time? **Answer:** No; its explicit formula stays below one for every finite time and converges to one only in the limit.

### Reading

MIT 18.03 Differential Equations, notes on autonomous equations, phase lines and stability; Arthur Mattuck, 18.03 notes on stability and graphical methods.
