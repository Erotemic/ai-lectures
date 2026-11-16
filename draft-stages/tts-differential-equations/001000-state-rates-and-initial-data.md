# 001000 — Differential Equations: Rates, Initial Conditions, and Uniqueness

**Track:** Differential Equations and Dynamical Systems. **Background:** derivatives and elementary algebra; exponential functions are reviewed. **Question:** when does a rule for change determine an actual trajectory?

<!-- BEGIN SPOKEN LECTURE -->

# Differential Equations: Rates, Initial Conditions, and Uniqueness

Suppose a temperature sensor reports that a room is cooling. Knowing its temperature at noon does not tell us what it will be at one o'clock. We need a law describing how the temperature changes. For instance, we might hypothesize that the rate of cooling is proportional to the difference between the room's temperature and the outside temperature.

Such a law relates a quantity to its derivative. It is a differential equation. Unlike an ordinary equation, its unknown is not a single number but an entire function of time. A solution is a trajectory whose rate of change agrees with the law at every point where the equation is asserted to hold.

The central questions are existence, uniqueness, and sensitivity. Does a trajectory satisfying the law exist? Is it determined by the initial state? And how much can nearby initial states or slightly inaccurate rate laws change the future?

## The simplest rate law

Suppose a population y grows at a rate proportional to its current size. Write the rule in words as: the derivative of y with respect to time equals k times y, where k is a fixed constant. The exponential function solves this equation because its derivative is proportional to itself. If y is initially y zero, the solution is y zero times the exponential of k times t, with time measured from the initial instant.

When k is positive and the initial population is positive, the population grows exponentially. When k is negative, it decays toward zero as time increases. When k equals zero, the population stays constant. The same mathematical model can describe a continuously compounded balance, an idealized decay process, or the early phase of a population process, depending on what assumptions connect the variables to the world.

We can check the solution rather than merely recognize its shape. Differentiate y zero times exponential of k t. By the chain rule we obtain k times the same expression. At time zero, the exponential is one, so the proposed trajectory has the required initial value. This is a complete verification for the initial value problem.

Why is the initial value needed? Without it, the equation has an entire family of solutions, one for each constant multiplier. The differential equation describes a family of admissible trajectories. An initial condition selects a member, when the law is sufficiently well behaved to make the selection unique.

## Direction fields and local prediction

For a general first-order equation, the derivative of y equals a function f of time and y. At a point in the time-state plane, f specifies a slope. Imagine drawing a tiny line segment with that slope at many points. The resulting direction field gives a qualitative picture of possible solution curves, even when no elementary formula exists.

For example, if the derivative equals y squared, slopes are nonnegative at every point and large when the magnitude of y is large. A trajectory starting at positive y rises. One starting at negative y also rises while remaining negative for as long as the formula applies, approaching zero in the future. The direction field reveals a qualitative rule, but it does not by itself guarantee that a solution exists everywhere or that curves never intersect.

A numerical approximation can follow the arrows. In Euler's method, start at a known time and value. Multiply the current slope by a small time step and add the result to the current value. Repeat. For the exponential growth equation with k equal to one, starting from one and taking steps of one tenth gives the sequence one, one point one, one point two one, and so on. After ten steps the Euler estimate is one point one raised to the tenth, about two point five nine, below the exact value e, about two point seven one eight.

Taking smaller steps typically improves the result for a smooth problem over a fixed finite time interval, but a method is not accurate merely because each step is small. Numerical convergence requires hypotheses and an error analysis, and finite precision eventually matters. The differential equation defines the target; the numerical method approximates that target.

## What existence and uniqueness require

Suppose the function f of time and state is continuous near a specified starting point. Standard existence theorems ensure that at least one local solution passes through that point. But continuity alone does not guarantee uniqueness. A commonly used sufficient condition for local uniqueness is that f be locally Lipschitz in the state variable, uniformly over a suitable local time neighborhood.

A Lipschitz condition means that changing the state from y one to y two changes the rate by at most a fixed constant times the distance between those states. It is a quantitative restriction on how violently the law can change with the state. If f has a continuous partial derivative with respect to y on a neighborhood, then it is locally Lipschitz there, so the familiar smooth rate laws fall within the theorem.

Why should Lipschitz control produce uniqueness? Imagine two trajectories beginning at the same point. Their instantaneous rates differ by at most L times their current separation. The accumulated separation therefore satisfies an integral inequality in which its growth is controlled by itself. Grönwall's inequality shows that a separation starting at zero must remain zero, at least while both trajectories remain in the common neighborhood. This is the mathematical form of the intuition that a well-behaved rate law cannot spontaneously split one initial state into two futures.

The existence theorem and the uniqueness theorem answer separate questions. Both are local statements under the standard hypotheses. A unique solution near the initial time is not automatically defined for all future time.

## Continuity without uniqueness

Consider a rate law that is twice the square root of the larger of y and zero, with the initial value y equal to zero. The right-hand side is continuous, but its dependence on y is not Lipschitz at zero.

One solution is to remain at zero forever. Another is to remain at zero until some chosen future time c, then follow the square of time minus c. After c, differentiating this square gives two times time minus c, exactly twice the square root of y. Before c, the derivative and the right-hand side are both zero. At c the derivatives from both sides agree at zero.

Every choice of waiting time gives a different solution of the same initial value problem. The differential equation permits a trajectory to sit still for an arbitrary interval and then depart. No numerical algorithm can recover a unique future from this initial condition without adding another selection principle, because the mathematical problem itself lacks uniqueness.

We should not misstate this example. It does not show that square roots are always troublesome, or that discontinuity is necessary for nonuniqueness. It shows that continuity is insufficient and that failure of a Lipschitz condition can matter. The Lipschitz hypothesis is sufficient for uniqueness, not necessary in every conceivable problem.

## Smoothness does not imply global existence

Consider another simple equation: the derivative of y equals y squared, with initial value one. Here the right-hand side is smooth everywhere. Local existence and uniqueness hold without difficulty. Separate variables or differentiate a proposed rational solution to find y equals one divided by one minus t.

As time approaches one from below, the solution grows without bound. It cannot be extended as a finite real-valued solution through time one while preserving the equation and the initial value. The rate law is perfectly smooth; the problem is that the state itself escapes to infinity in finite time.

This is finite-time blow-up. It distinguishes local existence from global existence. Smoothness controls what happens while a solution remains in a bounded region. To guarantee a trajectory for all future time, we need additional bounds that prevent escape or other obstructions.

The same equation also reveals an asymmetry in time. The solution beginning at one exists for all negative times but only until time one in the positive direction. A differential equation is often mathematically reversible as a local law, but its maximal solution interval need not extend infinitely in both directions.

## Models, conditions, and claims

When someone presents a differential equation as a model, several claims may be mixed together. The rate law may be an approximation of physical behavior. The initial state may be measured with error. The mathematical equation may have one solution, many solutions, or only a local solution. A computed curve may approximate a selected mathematical solution with an error that grows in time.

These are separate layers. We should not call a plot a prediction until we know which layer justifies it. A direction field clarifies how the rate depends on the state. An existence theorem tells us that a trajectory can satisfy the law. A uniqueness theorem tells us whether the initial data select exactly one trajectory. A numerical convergence theorem tells us when a discretized calculation tracks that trajectory.

The most valuable habit is to ask, whenever a differential equation appears: what is the state, what is the rate law, where is the initial condition, and which hypothesis supports the desired conclusion? Those questions turn a formula for change into a mathematically controlled account of evolution.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

An initial-value problem is \(y'(t)=f(t,y(t))\), \(y(t_0)=y_0\). A continuous \(f\) gives local existence (Peano, in standard finite-dimensional settings). Local Lipschitz continuity in \(y\), together with continuity in \(t\), gives local uniqueness (Picard–Lindelöf). These are sufficient hypotheses.

**Growth:** \(y'=ky,\;y(0)=y_0\implies y(t)=y_0e^{kt}\).

**Nonuniqueness:** \(y'=2\sqrt{\max(y,0)}\), \(y(0)=0\) permits
\[
y_c(t)=\begin{cases}0,&t\le c,\\(t-c)^2,&t>c,\end{cases}\qquad c\ge0,
\]
plus the identically zero solution. Each \(y_c\) is continuously differentiable and solves the ODE.

**Finite escape:** \(y'=y^2,\;y(0)=1\implies y(t)=1/(1-t)\) on its maximal interval \(( -\infty,1)\).

**Euler:** \(y_{j+1}=y_j+h f(t_j,y_j)\); smoothness and stability hypotheses are required for an error estimate.

### Exercises with answers

1. Solve \(y'=3y\), \(y(0)=2\). **Answer:** \(y(t)=2e^{3t}\).
2. Is continuity of the rate law enough for uniqueness? **Answer:** No; the delayed-departure example has a continuous non-Lipschitz right-hand side.
3. Does smoothness guarantee global solutions? **Answer:** No; \(y'=y^2\), \(y(0)=1\) blows up at \(t=1\).
4. For \(y'=y\), \(y(0)=1\), what does two Euler steps of size \(h=1/2\) give? **Answer:** \((1+1/2)^2=2.25\), compared to \(e\) at time one.

### Reading

MIT 18.03 Differential Equations, lecture notes on direction fields, existence and uniqueness, and Euler's method; Arthur Mattuck's 18.03 supplementary notes on graphical and numerical methods.
