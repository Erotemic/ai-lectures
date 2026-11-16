# 003000 — Separable and Linear First-Order Differential Equations

**Track:** Differential Equations and Dynamical Systems. **Background:** derivatives, integrals, and initial-value problems. **Question:** when is it legitimate to rearrange a differential equation as an integral, and what information can that step lose?

<!-- BEGIN SPOKEN LECTURE -->

# Separable and Linear First-Order Differential Equations

A differential equation tells us how a changing quantity responds to its current state and to time. Some equations can be solved by separating variables. Others yield to an integrating factor. These are often taught as algebraic recipes, but every transformation carries assumptions. Dividing by a function can discard a solution. Integrating can introduce constants that have to be determined. A formula may cease to exist even while the differential equation remains meaningful.

The useful question is not just how to produce a symbolic answer, but how to determine the interval on which that answer actually describes the initial-value problem.

## Separation as a change of perspective

Suppose a quantity y satisfies y-prime equals a function of time, g of t, multiplied by a function of state, h of y. In a region where h of y is nonzero, we can divide by it and write y-prime divided by h of y equals g of t. Since y-prime is the derivative of y with respect to t, the chain rule suggests integrating one divided by h with respect to y on one side and g with respect to t on the other.

This is what separation of variables means. It is a justified chain-rule calculation along a solution, not a magical rule for moving symbols d-y and d-t from one side of an equation to another. It can be written rigorously as the derivative of an antiderivative H of y equaling g of t, where H-prime equals one divided by h.

The warning is immediate. If h vanishes at some state, division by h cannot be performed there. Such zeros are equilibrium states of the autonomous equation when g is a nonzero constant, and they may supply constant solutions that the divided equation will not display. We should identify them before dividing.

## Exponential growth and decay

The equation y-prime equals k y, with constant k, is separable whenever y is nonzero. Dividing gives the derivative of the logarithm of the absolute value of y equal to k. Integrating gives logarithm of absolute y equal to k t plus a constant. Exponentiating yields y equals C times the exponential of k t. This formula also includes the zero solution when C is zero, even though the division step excluded it. We have recovered it by checking the original equation.

Given an initial value y at time zero equal to y-zero, the constant is y-zero. When k is positive, nonzero solutions increase in magnitude forward in time; when k is negative, they decay toward zero. These claims concern the mathematical model. Whether a physical population can grow indefinitely at a fixed proportional rate is a separate modeling question.

Notice that the equation was solved on the entire real time axis. That is not guaranteed for nonlinear equations, even when the right-hand side is a smooth function.

## Smooth equations can still blow up

Consider y-prime equals y squared with y at time zero equal to one. Separation gives negative one over y equals t plus a constant. Using the initial value yields y equal to one divided by one minus t.

The formula is valid on the interval from negative infinity to one that contains the initial time. As t approaches one from below, y becomes arbitrarily large. There is no finite value y of one that could continue this solution through the blow-up time. Yet the function y squared is smooth and locally Lipschitz for every finite y. Local existence and uniqueness do not imply that every solution exists for all time. The solution escapes every bounded region as its maximal interval ends.

The differential equation also has the constant solution y equals zero, which was excluded by dividing by y squared. It cannot be patched to the positive solution at any finite time because uniqueness prevents two distinct solutions from meeting at a point where the equation is regular.

## Logistic growth and its equilibria

A more constrained growth model is y-prime equals r y times one minus y divided by K, with positive constants r and K. The factor y drives initial exponential-like growth, while one minus y over K changes sign at the carrying capacity K.

There are two equilibrium solutions: y equals zero and y equals K. For values strictly between zero and K, the right-hand side is positive. Above K it is negative. We can understand that phase-line behavior before solving anything.

For y not equal to either equilibrium, separate using one over y times one minus y over K. The corresponding partial fractions produce the logarithm of the absolute value of y over K minus y equal to r t plus a constant. Solving for y yields K divided by one plus A times the exponential of negative r t. When the initial value lies strictly between zero and K, A is positive and the denominator never vanishes. The solution exists for all real t, approaches K as t increases, and approaches zero as t decreases.

For an initial value above K, A is negative. The solution is still valid forward in time and decreases toward K, but the same formula may have a denominator that vanishes at a finite negative time. Even a model with a stable forward equilibrium can have a finite backward-time blow-up for some initial conditions. The interval is part of the answer.

## Linear equations and integrating factors

Now consider a first-order linear equation: y-prime plus p of t times y equals q of t. Assume p and q are continuous on an interval containing the initial time. We want to make the left side the derivative of a product.

Choose a function mu whose derivative equals p times mu. One such function is the exponential of an antiderivative of p. Multiply the equation by mu. The left becomes mu times y-prime plus mu p y, which is exactly the derivative of mu times y by the product rule. Thus the equation reduces to a single integration: mu y equals the integral of mu q with respect to t plus a constant.

This method does not require division by y. It works equally well when the solution crosses zero. It is often safer than attempting to separate variables in an equation that is not separable.

Take y-prime plus two y equals t. The integrating factor is the exponential of two t. Integrating gives y equal to t over two minus one-quarter plus C times the exponential of negative two t. We can verify the result by differentiation: the constant-exponential terms cancel in y-prime plus two y, leaving exactly t. An initial condition such as y at zero equal to zero sets C to one-quarter.

This verification is worthwhile because an incorrect antiderivative or integration constant can easily produce a plausible but false formula.

## Why uniqueness matters to the method

For a linear first-order equation with continuous coefficients, every initial value determines a unique solution on the entire interval where the coefficients are defined. The integrating-factor formula makes this visible: the only free parameter is one constant, and the initial condition fixes it.

For a nonlinear separable equation, existence and uniqueness may still hold locally, but the explicit formula can reveal a finite maximal interval. If the right-hand side is not locally Lipschitz in the state, uniqueness itself may fail. For example, y-prime equals the square root of the absolute value of y, with initial value zero, permits the zero solution and solutions that remain zero for a while before becoming positive. One can verify that a solution beginning growth at time a is zero up to a and equals one-quarter times the square of t minus a thereafter. The derivative matches continuously at the start time, and both the derivative and the square root equal one-half times t minus a for later times. The model's lack of uniqueness is genuine, not an artifact of a bad integration trick.

The general lesson is that separation and integrating factors are tools for constructing and checking solutions. Equilibria, regularity, initial conditions, and maximal intervals determine whether the construction answers the intended question. An equation solved on paper is not yet an initial-value problem understood; we must also know where the solution exists and what makes it unique.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

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

### Exercises with answers

1. Solve \(y'=3y\), \(y(0)=2\). **Answer:** \(2e^{3t}\).
2. Solve \(y'+2y=t\), \(y(0)=0\). **Answer:** \(y=t/2-1/4+(1/4)e^{-2t}\).
3. Why must equilibria be checked before separation? **Answer:** dividing by \(h(y)\) excludes states where \(h(y)=0\), which can be constant solutions.
4. On what maximal interval through zero does \(y'=y^2\), \(y(0)=1\) exist? **Answer:** \((-\infty,1)\).

### Reading

MIT OCW 18.03 *Differential Equations*, first-order ODEs and integrating factors; Arthur Mattuck, *18.03 Notes and Exercises*.
