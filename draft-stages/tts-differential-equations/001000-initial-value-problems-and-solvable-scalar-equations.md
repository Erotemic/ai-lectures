# Initial-value problems and solvable scalar equations

<!-- BEGIN SPOKEN LECTURE -->

# Initial-value problems and solvable scalar equations

## Differential Equations: Rates, Initial Conditions, and Uniqueness

Suppose a temperature sensor reports that a room is cooling. Knowing its temperature at noon does not tell us what it will be at one o'clock. We need a law describing how the temperature changes. For instance, we might hypothesize that the rate of cooling is proportional to the difference between the room's temperature and the outside temperature.

Such a law relates a quantity to its derivative. It is a differential equation. Unlike an ordinary equation, its unknown is not a single number but an entire function of time. A solution is a trajectory whose rate of change agrees with the law at every point where the equation is asserted to hold.

The central questions are existence, uniqueness, and sensitivity. Does a trajectory satisfying the law exist? Is it determined by the initial state? And how much can nearby initial states or slightly inaccurate rate laws change the future?

### The simplest rate law

Suppose a population y grows at a rate proportional to its current size. Write the rule in words as: the derivative of y with respect to time equals k times y, where k is a fixed constant. The exponential function solves this equation because its derivative is proportional to itself. If y is initially y zero, the solution is y zero times the exponential of k times t, with time measured from the initial instant.

When k is positive and the initial population is positive, the population grows exponentially. When k is negative, it decays toward zero as time increases. When k equals zero, the population stays constant. The same mathematical model can describe a continuously compounded balance, an idealized decay process, or the early phase of a population process, depending on what assumptions connect the variables to the world.

We can check the solution rather than merely recognize its shape. Differentiate y zero times exponential of k t. By the chain rule we obtain k times the same expression. At time zero, the exponential is one, so the proposed trajectory has the required initial value. This is a complete verification for the initial value problem.

Why is the initial value needed? Without it, the equation has an entire family of solutions, one for each constant multiplier. The differential equation describes a family of admissible trajectories. An initial condition selects a member, when the law is sufficiently well behaved to make the selection unique.

### Direction fields and local prediction

For a general first-order equation, the derivative of y equals a function f of time and y. At a point in the time-state plane, f specifies a slope. Imagine drawing a tiny line segment with that slope at many points. The resulting direction field gives a qualitative picture of possible solution curves, even when no elementary formula exists.

For example, if the derivative equals y squared, slopes are nonnegative at every point and large when the magnitude of y is large. A trajectory starting at positive y rises. One starting at negative y also rises while remaining negative for as long as the formula applies, approaching zero in the future. The direction field reveals a qualitative rule, but it does not by itself guarantee that a solution exists everywhere or that curves never intersect.

A numerical approximation can follow the arrows. In Euler's method, start at a known time and value. Multiply the current slope by a small time step and add the result to the current value. Repeat. For the exponential growth equation with k equal to one, starting from one and taking steps of one tenth gives the sequence one, one point one, one point two one, and so on. After ten steps the Euler estimate is one point one raised to the tenth, about two point five nine, below the exact value e, about two point seven one eight.

Taking smaller steps typically improves the result for a smooth problem over a fixed finite time interval, but a method is not accurate merely because each step is small. Numerical convergence requires hypotheses and an error analysis, and finite precision eventually matters. The differential equation defines the target; the numerical method approximates that target.

### What existence and uniqueness require

Suppose the function f of time and state is continuous near a specified starting point. Standard existence theorems ensure that at least one local solution passes through that point. But continuity alone does not guarantee uniqueness. A commonly used sufficient condition for local uniqueness is that f be locally Lipschitz in the state variable, uniformly over a suitable local time neighborhood.

A Lipschitz condition means that changing the state from y one to y two changes the rate by at most a fixed constant times the distance between those states. It is a quantitative restriction on how violently the law can change with the state. If f has a continuous partial derivative with respect to y on a neighborhood, then it is locally Lipschitz there, so the familiar smooth rate laws fall within the theorem.

Why should Lipschitz control produce uniqueness? Imagine two trajectories beginning at the same point. Their instantaneous rates differ by at most L times their current separation. The accumulated separation therefore satisfies an integral inequality in which its growth is controlled by itself. Grönwall's inequality shows that a separation starting at zero must remain zero, at least while both trajectories remain in the common neighborhood. This is the mathematical form of the intuition that a well-behaved rate law cannot spontaneously split one initial state into two futures.

The existence theorem and the uniqueness theorem answer separate questions. Both are local statements under the standard hypotheses. A unique solution near the initial time is not automatically defined for all future time.

### Continuity without uniqueness

Consider a rate law that is twice the square root of the larger of y and zero, with the initial value y equal to zero. The right-hand side is continuous, but its dependence on y is not Lipschitz at zero.

One solution is to remain at zero forever. Another is to remain at zero until some chosen future time c, then follow the square of time minus c. After c, differentiating this square gives two times time minus c, exactly twice the square root of y. Before c, the derivative and the right-hand side are both zero. At c the derivatives from both sides agree at zero.

Every choice of waiting time gives a different solution of the same initial value problem. The differential equation permits a trajectory to sit still for an arbitrary interval and then depart. No numerical algorithm can recover a unique future from this initial condition without adding another selection principle, because the mathematical problem itself lacks uniqueness.

We should not misstate this example. It does not show that square roots are always troublesome, or that discontinuity is necessary for nonuniqueness. It shows that continuity is insufficient and that failure of a Lipschitz condition can matter. The Lipschitz hypothesis is sufficient for uniqueness, not necessary in every conceivable problem.

### Smoothness does not imply global existence

Consider another simple equation: the derivative of y equals y squared, with initial value one. Here the right-hand side is smooth everywhere. Local existence and uniqueness hold without difficulty. Separate variables or differentiate a proposed rational solution to find y equals one divided by one minus t.

As time approaches one from below, the solution grows without bound. It cannot be extended as a finite real-valued solution through time one while preserving the equation and the initial value. The rate law is perfectly smooth; the problem is that the state itself escapes to infinity in finite time.

This is finite-time blow-up. It distinguishes local existence from global existence. Smoothness controls what happens while a solution remains in a bounded region. To guarantee a trajectory for all future time, we need additional bounds that prevent escape or other obstructions.

The same equation also reveals an asymmetry in time. The solution beginning at one exists for all negative times but only until time one in the positive direction. A differential equation is often mathematically reversible as a local law, but its maximal solution interval need not extend infinitely in both directions.

### Models, conditions, and claims

When someone presents a differential equation as a model, several claims may be mixed together. The rate law may be an approximation of physical behavior. The initial state may be measured with error. The mathematical equation may have one solution, many solutions, or only a local solution. A computed curve may approximate a selected mathematical solution with an error that grows in time.

These are separate layers. We should not call a plot a prediction until we know which layer justifies it. A direction field clarifies how the rate depends on the state. An existence theorem tells us that a trajectory can satisfy the law. A uniqueness theorem tells us whether the initial data select exactly one trajectory. A numerical convergence theorem tells us when a discretized calculation tracks that trajectory.

The most valuable habit is to ask, whenever a differential equation appears: what is the state, what is the rate law, where is the initial condition, and which hypothesis supports the desired conclusion? Those questions turn a formula for change into a mathematically controlled account of evolution.

## Phase Lines and Stability: Predicting Motion Without Solving an Equation

Many differential equations cannot be solved in elementary functions. Even when a formula exists, the formula may obscure the behavior we care about. We might want to know whether a population approaches an equilibrium, whether a perturbation dies out, or whether a state is driven away from a seemingly steady configuration.

For a one-dimensional autonomous differential equation, much of that behavior can be read directly from a single function and its sign. This is the idea of the phase line: study the motion of the state rather than first searching for an explicit function of time.

### From slopes to arrows

An autonomous equation has the form the derivative of y equals f of y. The rate depends on the current state, not explicitly on the time. Where f is positive, a solution rises as time increases. Where f is negative, it falls. Where f equals zero, a constant solution is possible: the state remains at an equilibrium.

Draw a line representing all possible state values. Mark the zeros of f. Between consecutive zeros, if f is continuous, its sign cannot change without passing through another zero. So one arrow for each interval describes the direction of all trajectories while they remain there. We can inspect the qualitative pattern without integrating anything.

Consider the logistic equation, whose rate is y times one minus y. It has equilibria at zero and one. For y between zero and one, both factors are positive, so the arrow points upward. For y greater than one, the first factor is positive and the second negative, so the arrow points downward. For y below zero, the first factor is negative and the second is positive, so their product is negative; the arrow also points downward.

The resulting portrait is simple. States between zero and one rise toward one. States above one decrease toward one. Nearby positive states move toward one from either side. Near zero, positive states move away from zero, while negative states move farther negative. Thus zero is unstable and one is asymptotically stable with respect to nearby real states.

We have to interpret “population” carefully. Negative populations are physically meaningless in the ordinary model. The mathematical phase line includes them, but if the intended state space is nonnegative, we should state that restriction. For any positive starting population, the logistic solution exists for all future time and approaches one in our normalized units.

### Stability is a statement with quantifiers

An equilibrium y star is stable in the sense of Lyapunov if any sufficiently small initial disturbance remains small for all future time. More precisely, for every desired tolerance around the equilibrium, there must exist an initial tolerance such that starting within the initial tolerance keeps the trajectory within the desired tolerance forever.

Asymptotic stability requires more: the equilibrium is stable, and all trajectories starting sufficiently near it converge to it as time grows. An equilibrium may be stable without being attractive. For instance, when the rate is identically zero, every point is an equilibrium. Starting near a chosen equilibrium leaves the state at that nearby starting point forever. It never runs away, so the chosen equilibrium is stable, but trajectories do not generally converge to it.

The distinction matters when someone says that a numerical simulation has “settled.” A state can move slowly without converging to an equilibrium. Stability is a property of the mathematical flow and perturbations, not merely a visual impression of a flat plot.

### Linearization near an equilibrium

Suppose f is differentiable at an equilibrium y star. For a state just a little away, write y as y star plus a small perturbation z. Taylor's approximation gives f of y star plus z approximately f of y star plus f prime of y star times z. The first term is zero because y star is an equilibrium. So the perturbation approximately obeys z prime equals f prime of y star times z.

We already know the behavior of that linear equation. If the derivative f prime at the equilibrium is negative, small perturbations shrink exponentially in the linear approximation. If it is positive, some small perturbations grow. With the usual smoothness and well-posedness assumptions, a negative derivative proves local asymptotic stability in one dimension; a positive derivative proves instability.

For the logistic rate f of y equals y minus y squared, the derivative is one minus two y. At zero it equals one, confirming instability. At one it equals negative one, confirming local asymptotic stability. Our sign-chart argument already described the global behavior for positive initial states; linearization tells us about the local rate of return near one.

It is worth distinguishing the strength of these conclusions. A derivative sign at one equilibrium is local information. It does not by itself guarantee that every initial condition in the state space converges there. A global conclusion requires an argument about the whole relevant region, as the phase line provided for positive logistic states.

### When the linear term vanishes

What if f prime at the equilibrium is zero? Linearization then predicts z prime approximately zero and reveals nothing decisive. The neglected nonlinear terms can determine the entire stability picture.

Compare two equations at zero. In the first, the derivative of y equals negative y cubed. For positive y, the rate is negative and the state moves down toward zero. For negative y, the rate is positive and the state moves upward toward zero. The equilibrium at zero is asymptotically stable, though the return is slower than the exponential decay suggested by a strictly negative linear derivative.

In the second equation, the derivative of y equals positive y cubed. Positive states rise away from zero and negative states fall away. The equilibrium is unstable. In both equations, the derivative of the rate law at zero equals zero. The linear approximation is identical; the nonlinear behavior is opposite.

This is why a zero eigenvalue, or a zero derivative in one dimension, signals that a more careful analysis is required. Calling such an equilibrium stable because the linear model does not grow would be a mistake. A vanishing linear term is inconclusive.

### Solve the logistic equation as a check

We can verify our qualitative prediction with an explicit solution. For positive initial y zero, separation of variables leads to y of t equals y zero times the exponential of t divided by one plus y zero times the exponential of t minus one. Equivalently, y is one divided by one plus a constant times the exponential of negative t, with the constant determined by the starting value.

For positive y zero, the denominator stays positive for all nonnegative time. As time grows, the exponential of negative t tends to zero. Therefore y tends to one. If y zero is less than one, it increases; if y zero is greater than one, it decreases. These conclusions match the phase line.

At y zero equal to zero, the solution is the constant zero solution. For negative y zero, the formula can have a denominator that reaches zero in finite positive time, leading to blow-up toward negative infinity. The exact solution exposes a domain issue that the arrows alone do not resolve. Again, qualitative analysis and existence analysis complement each other.

### What changes in higher dimensions

In a system with several state variables, the phase line becomes a phase portrait in a plane or higher-dimensional space. Equilibria are states at which every component of the vector field vanishes. The linearization is a matrix, the Jacobian, and its eigenvalues help determine local behavior.

If every eigenvalue has strictly negative real part, a sufficiently smooth autonomous system has a locally asymptotically stable equilibrium. If at least one eigenvalue has strictly positive real part, the equilibrium is unstable. When eigenvalues have zero real part and none has positive real part, linearization can be inconclusive. These statements depend on the correct Jacobian and on local hypotheses; they are not a substitute for a global nonlinear analysis.

One-dimensional autonomous systems have an additional simplification under uniqueness: a nonconstant solution cannot cross an equilibrium, because doing so would conflict with the constant solution through that equilibrium. So the state remains in a region between equilibria. In higher dimensions, trajectories can move around equilibria, spiral, or cycle, and the geometry becomes richer.

### Prediction without a closed form

We began with a rate law and asked what it could tell us before solving. Zeros revealed equilibria. Signs gave directions. The derivative at an equilibrium gave a local linear test when nonzero. Explicit formulas then confirmed and sharpened the picture where they were available.

This approach is not a shortcut around mathematics. It separates questions: existence and uniqueness, local stability, domains of trajectories, and global attraction. A long exact formula may answer none of these transparently. A phase portrait, supported by theorems, can answer several of them at once. That is why dynamical systems is a subject in its own right, not merely a catalog of integration techniques.

## Separable and Linear First-Order Differential Equations

A differential equation tells us how a changing quantity responds to its current state and to time. Some equations can be solved by separating variables. Others yield to an integrating factor. These are often taught as algebraic recipes, but every transformation carries assumptions. Dividing by a function can discard a solution. Integrating can introduce constants that have to be determined. A formula may cease to exist even while the differential equation remains meaningful.

The useful question is not just how to produce a symbolic answer, but how to determine the interval on which that answer actually describes the initial-value problem.

### Separation as a change of perspective

Suppose a quantity y satisfies y-prime equals a function of time, g of t, multiplied by a function of state, h of y. In a region where h of y is nonzero, we can divide by it and write y-prime divided by h of y equals g of t. Since y-prime is the derivative of y with respect to t, the chain rule suggests integrating one divided by h with respect to y on one side and g with respect to t on the other.

This is what separation of variables means. It is a justified chain-rule calculation along a solution, not a magical rule for moving symbols d-y and d-t from one side of an equation to another. It can be written rigorously as the derivative of an antiderivative H of y equaling g of t, where H-prime equals one divided by h.

The warning is immediate. If h vanishes at some state, division by h cannot be performed there. Such zeros are equilibrium states of the autonomous equation when g is a nonzero constant, and they may supply constant solutions that the divided equation will not display. We should identify them before dividing.

### Exponential growth and decay

The equation y-prime equals k y, with constant k, is separable whenever y is nonzero. Dividing gives the derivative of the logarithm of the absolute value of y equal to k. Integrating gives logarithm of absolute y equal to k t plus a constant. Exponentiating yields y equals C times the exponential of k t. This formula also includes the zero solution when C is zero, even though the division step excluded it. We have recovered it by checking the original equation.

Given an initial value y at time zero equal to y-zero, the constant is y-zero. When k is positive, nonzero solutions increase in magnitude forward in time; when k is negative, they decay toward zero. These claims concern the mathematical model. Whether a physical population can grow indefinitely at a fixed proportional rate is a separate modeling question.

Notice that the equation was solved on the entire real time axis. That is not guaranteed for nonlinear equations, even when the right-hand side is a smooth function.

### Smooth equations can still blow up

Consider y-prime equals y squared with y at time zero equal to one. Separation gives negative one over y equals t plus a constant. Using the initial value yields y equal to one divided by one minus t.

The formula is valid on the interval from negative infinity to one that contains the initial time. As t approaches one from below, y becomes arbitrarily large. There is no finite value y of one that could continue this solution through the blow-up time. Yet the function y squared is smooth and locally Lipschitz for every finite y. Local existence and uniqueness do not imply that every solution exists for all time. The solution escapes every bounded region as its maximal interval ends.

The differential equation also has the constant solution y equals zero, which was excluded by dividing by y squared. It cannot be patched to the positive solution at any finite time because uniqueness prevents two distinct solutions from meeting at a point where the equation is regular.

### Logistic growth and its equilibria

A more constrained growth model is y-prime equals r y times one minus y divided by K, with positive constants r and K. The factor y drives initial exponential-like growth, while one minus y over K changes sign at the carrying capacity K.

There are two equilibrium solutions: y equals zero and y equals K. For values strictly between zero and K, the right-hand side is positive. Above K it is negative. We can understand that phase-line behavior before solving anything.

For y not equal to either equilibrium, separate using one over y times one minus y over K. The corresponding partial fractions produce the logarithm of the absolute value of y over K minus y equal to r t plus a constant. Solving for y yields K divided by one plus A times the exponential of negative r t. When the initial value lies strictly between zero and K, A is positive and the denominator never vanishes. The solution exists for all real t, approaches K as t increases, and approaches zero as t decreases.

For an initial value above K, A is negative. The solution is still valid forward in time and decreases toward K, but the same formula may have a denominator that vanishes at a finite negative time. Even a model with a stable forward equilibrium can have a finite backward-time blow-up for some initial conditions. The interval is part of the answer.

### Linear equations and integrating factors

Now consider a first-order linear equation: y-prime plus p of t times y equals q of t. Assume p and q are continuous on an interval containing the initial time. We want to make the left side the derivative of a product.

Choose a function mu whose derivative equals p times mu. One such function is the exponential of an antiderivative of p. Multiply the equation by mu. The left becomes mu times y-prime plus mu p y, which is exactly the derivative of mu times y by the product rule. Thus the equation reduces to a single integration: mu y equals the integral of mu q with respect to t plus a constant.

This method does not require division by y. It works equally well when the solution crosses zero. It is often safer than attempting to separate variables in an equation that is not separable.

Take y-prime plus two y equals t. The integrating factor is the exponential of two t. Integrating gives y equal to t over two minus one-quarter plus C times the exponential of negative two t. We can verify the result by differentiation: the constant-exponential terms cancel in y-prime plus two y, leaving exactly t. An initial condition such as y at zero equal to zero sets C to one-quarter.

This verification is worthwhile because an incorrect antiderivative or integration constant can easily produce a plausible but false formula.

### Why uniqueness matters to the method

For a linear first-order equation with continuous coefficients, every initial value determines a unique solution on the entire interval where the coefficients are defined. The integrating-factor formula makes this visible: the only free parameter is one constant, and the initial condition fixes it.

For a nonlinear separable equation, existence and uniqueness may still hold locally, but the explicit formula can reveal a finite maximal interval. If the right-hand side is not locally Lipschitz in the state, uniqueness itself may fail. For example, y-prime equals the square root of the absolute value of y, with initial value zero, permits the zero solution and solutions that remain zero for a while before becoming positive. One can verify that a solution beginning growth at time a is zero up to a and equals one-quarter times the square of t minus a thereafter. The derivative matches continuously at the start time, and both the derivative and the square root equal one-half times t minus a for later times. The model's lack of uniqueness is genuine, not an artifact of a bad integration trick.

The general lesson is that separation and integrating factors are tools for constructing and checking solutions. Equilibria, regularity, initial conditions, and maximal intervals determine whether the construction answers the intended question. An equation solved on paper is not yet an initial-value problem understood; we must also know where the solution exists and what makes it unique.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Differential Equations: Rates, Initial Conditions, and Uniqueness

**Track:** Differential Equations and Dynamical Systems. **Background:** derivatives and elementary algebra; exponential functions are reviewed. **Question:** when does a rule for change determine an actual trajectory?

#### Mathematical companion (not spoken)

An initial-value problem is \(y'(t)=f(t,y(t))\), \(y(t_0)=y_0\). A continuous \(f\) gives local existence (Peano, in standard finite-dimensional settings). Local Lipschitz continuity in \(y\), together with continuity in \(t\), gives local uniqueness (Picard–Lindelöf). These are sufficient hypotheses.

**Growth:** \(y'=ky,\;y(0)=y_0\implies y(t)=y_0e^{kt}\).

**Nonuniqueness:** \(y'=2\sqrt{\max(y,0)}\), \(y(0)=0\) permits
\[
y_c(t)=\begin{cases}0,&t\le c,\\(t-c)^2,&t>c,\end{cases}\qquad c\ge0,
\]
plus the identically zero solution. Each \(y_c\) is continuously differentiable and solves the ODE.

**Finite escape:** \(y'=y^2,\;y(0)=1\implies y(t)=1/(1-t)\) on its maximal interval \(( -\infty,1)\).

**Euler:** \(y_{j+1}=y_j+h f(t_j,y_j)\); smoothness and stability hypotheses are required for an error estimate.

##### Exercises with answers

1. Solve \(y'=3y\), \(y(0)=2\). **Answer:** \(y(t)=2e^{3t}\).
2. Is continuity of the rate law enough for uniqueness? **Answer:** No; the delayed-departure example has a continuous non-Lipschitz right-hand side.
3. Does smoothness guarantee global solutions? **Answer:** No; \(y'=y^2\), \(y(0)=1\) blows up at \(t=1\).
4. For \(y'=y\), \(y(0)=1\), what does two Euler steps of size \(h=1/2\) give? **Answer:** \((1+1/2)^2=2.25\), compared to \(e\) at time one.

##### Reading

MIT 18.03 Differential Equations, lecture notes on direction fields, existence and uniqueness, and Euler's method; Arthur Mattuck's 18.03 supplementary notes on graphical and numerical methods.

### Phase Lines and Stability: Predicting Motion Without Solving an Equation

**Track:** Differential Equations and Dynamical Systems. **Background:** first-order differential equations and derivatives. **Question:** what can the signs of a rate law tell us about long-run behavior?

#### Mathematical companion (not spoken)

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

##### Exercises with answers

1. Find equilibria of \(y'=y(2-y)\). **Answer:** Zero and two.
2. Which equilibrium in the preceding equation attracts nearby positive states? **Answer:** Two; the rate points toward it on both sides.
3. Does \(f'(y_*)=0\) prove stability? **Answer:** No; compare \(y'=\pm y^3\).
4. Can the logistic solution with \(y_0=1/2\) reach the equilibrium one at a finite positive time? **Answer:** No; its explicit formula stays below one for every finite time and converges to one only in the limit.

##### Reading

MIT 18.03 Differential Equations, notes on autonomous equations, phase lines and stability; Arthur Mattuck, 18.03 notes on stability and graphical methods.

### Separable and Linear First-Order Differential Equations

**Track:** Differential Equations and Dynamical Systems. **Background:** derivatives, integrals, and initial-value problems. **Question:** when is it legitimate to rearrange a differential equation as an integral, and what information can that step lose?

#### Mathematical companion (not spoken)

For \(y'=g(t)h(y)\), away from zeros of \(h\), choose \(H'(y)=1/h(y)\). Then \(H(y(t))=\int g(t)\,dt+C\); separately check states \(h(y)=0\).

**Finite-time blow-up:**
\[
y'=y^2,\quad y(0)=1\quad\Longrightarrow\quad y(t)=\frac1{1-t},\qquad t\in(-\infty,1).
\]

**Logistic:** \(y'=ry(1-y/K)\), \(r,K>0\):
\[
y(t)=\frac{K}{1+\bigl(K/y_0-1\bigr)e^{-rt}},\quad y_0\notin\{0,K\},
\]
with maximal interval determined by nonvanishing denominator, plus equilibria \(y=0\) and \(y=K\).

**Linear integrating factor:** if \(y'+p(t)y=q(t)\), let
\[
\mu(t)=\exp\left(\int_{t_0}^{t}p(s)\,ds\right),\qquad
(\mu y)'=\mu q.
\]
Then \(y(t)=\mu(t)^{-1}\bigl(y_0+\int_{t_0}^{t}\mu(s)q(s)\,ds\bigr)\).

**Nonunique example:** \(y'=\sqrt{|y|}\), \(y(0)=0\); for \(a\ge0\), \(y_a(t)=0\) for \(t\le a\), and \(y_a(t)=(t-a)^2/4\) for \(t>a\). The factor one-quarter is determined by direct substitution into the equation.

##### Exercises with answers

1. Solve \(y'=3y\), \(y(0)=2\). **Answer:** \(2e^{3t}\).
2. Solve \(y'+2y=t\), \(y(0)=0\). **Answer:** \(y=t/2-1/4+(1/4)e^{-2t}\).
3. Why must equilibria be checked before separation? **Answer:** dividing by \(h(y)\) excludes states where \(h(y)=0\), which can be constant solutions.
4. On what maximal interval through zero does \(y'=y^2\), \(y(0)=1\) exist? **Answer:** \((-\infty,1)\).

##### Reading

MIT OCW 18.03 *Differential Equations*, first-order ODEs and integrating factors; Arthur Mattuck, *18.03 Notes and Exercises*.
