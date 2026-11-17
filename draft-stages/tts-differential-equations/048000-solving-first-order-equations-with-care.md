# Solving First-Order Equations with Care: Separation and Integrating Factors

<!-- BEGIN SPOKEN LECTURE -->

# Solving First-Order Equations with Care

A differential equation gives us a rule for the slope of a curve. Sometimes we can turn that rule into an exact formula. The two most useful introductory techniques are separation of variables and the integrating factor. Both are powerful. Both are also easy to misuse if we treat the algebra as a ritual without checking where divisions and formulas are valid.

We'll practice two things at once: finding solutions and verifying that they solve the intended initial-value problem. The verification matters as much as the construction. A correct differential equation can lead to an incorrect answer if we lose an equilibrium, choose the wrong integration constant, or use a formula outside its interval of validity.

## Separation begins with a product

Suppose y prime equals one plus t, multiplied by one minus y. The time dependence and the state dependence have been factored: one plus t is a function of time alone, and one minus y is a function of y alone. Such an equation is separable.

Before dividing, ask where the state factor vanishes. At y equal to one, the derivative is zero for every t, so y identically one is a solution. If we divide by one minus y, we exclude that constant solution from our algebra. We'll remember it.

For a solution with y different from one, divide by one minus y. The derivative of negative logarithm of the absolute value of one minus y is y prime divided by one minus y. The equation therefore says that this logarithmic derivative equals one plus t. Integrating gives negative logarithm of absolute one minus y equals t plus one-half t squared plus a constant.

Rearrange to obtain one minus y equal to a constant times the exponential of negative t minus one-half t squared. If y at time zero equals zero, the constant equals one. The solution is y equals one minus the exponential of negative t minus one-half t squared. We can check it without trusting a memory of integration rules: differentiating yields the exponential factor times one plus t, while one minus y is exactly that exponential factor. The equation holds.

This calculation also illustrates the purpose of the initial condition. Integrating introduced one free constant. The condition at t equal to zero fixed it. Without the initial condition, we would have a family of curves.

There is a practical catch: for t less than negative one, the coefficient one plus t changes sign. A solution that rises toward one when t is increasing beyond negative one can behave differently farther in the past. The derivative's sign depends on both factors. 'The equilibrium is attracting' is a claim that needs a time direction and a region, not an automatic consequence of one factor looking familiar.

## The logistic equation, without the mystery

Consider a population law y prime equals y times one minus y divided by three. The states zero and three are equilibria. At y between zero and three, both factors are positive: population grows. Above three, the second factor is negative: population decreases. We know the phase-line picture before any calculation.

Now suppose the initial population is one. Separation gives one over y times one minus y over three, integrated with respect to y, equal to time plus a constant. Partial fractions turn the left side into a difference of logarithms. Solving for y gives three divided by one plus two times the exponential of negative t.

Check time zero: three divided by three is one. Check long times: the exponential tends to zero, so the population approaches three. Check the derivative: it is positive for every finite positive time, which agrees with the phase-line picture. These independent checks reinforce each other. If the constant had come out negative for initial population one, we would have reason to suspect a mistake.

The formula is not a claim that real populations have perfectly fixed carrying capacities. It is a deduction from a simplified model. Its main mathematical lesson is how two equilibrium values and a nonlinear rate rule constrain a whole family of solution curves.

## When division loses information

Try y prime equals y squared, starting at zero. If we divide by y squared, we have already ruled out y equal to zero. But the identically zero function is a perfectly good solution. The separated formula would instead produce functions of the form one divided by a shifted time, none of which passes through zero at a finite time. An uncritical calculation could falsely conclude that the initial-value problem has no solution.

The right method is to identify constant solutions first and then divide only on regions where the divisor is nonzero. The same warning applies to equations involving products such as y times one minus y or functions like sine of y. At every zero of the state factor, ask whether a constant curve solves the original equation.

Sometimes the difficulty goes deeper. The equation y prime equals the square root of y for nonnegative y has solutions that wait at zero before growing. One is identically zero. Another remains zero until time one and then grows as one quarter times the square of t minus one. More generally, growth can begin at any nonnegative time. Separation away from zero does not tell us which waiting time to choose. This is genuine nonuniqueness, not merely a forgotten integration constant. We will return to why it happens.

## Integrating factors come from the product rule

Separation works when the rate can be written as a product of a time-only factor and a state-only factor. What if the equation is y prime plus two y equals six? The time derivative and y appear in a sum. There is no reason to force them into a separated product.

Instead, multiply by the exponential of two t. The derivative of the exponential times y is exactly the exponential times y prime plus two times the exponential times y. We have manufactured the product rule. The new equation says that derivative equals six times the exponential.

Integrate once. The exponential times y equals three times the exponential plus a constant. Hence y equals three plus a constant times the exponential of negative two t. If y initially equals one, the constant is negative two. So the solution is three minus two times the exponential of negative two t.

We can explain the same result without algebra. Three is the equilibrium: there y prime equals zero. The difference from equilibrium decays exponentially, because its rate is negative twice itself. The formula makes the qualitative reasoning exact.

An integrating factor is not a trick to memorize. It solves a specific design problem: find a multiplier that turns the left side into one derivative. For the general equation y prime plus p of t times y equals q of t, choose the multiplier to have logarithmic derivative p. That multiplier is the exponential of an antiderivative of p. Once multiplied, the equation can be integrated. On any interval where p and q are continuous, this process gives a solution for every initial value.

## A variable forcing term

Consider y prime plus y equals t, and y at zero equals two. Here the input depends on time. Multiply by the exponential of t. The derivative of the exponential times y equals t times the exponential. Integrating the right side gives the exponential times t minus one, plus a constant. Divide by the exponential to obtain y equals t minus one plus C times the exponential of negative t.

At time zero, y equals negative one plus C, so C must be three. The answer is y equals t minus one plus three times the exponential of negative t.

Verify: the derivative is one minus three times the exponential of negative t. Add y itself. The exponential terms cancel, and the constant one cancels negative one; only t remains. The initial value is two. This is a complete solution, not just an antiderivative scribbled on paper.

The solution also separates two effects. The exponential term remembers the initial condition but decays. The term t minus one follows the growing input. This distinction between a transient and a particular response becomes essential when we study forced oscillators and linear systems.

## Why the coefficient's interval matters

Consider y prime plus one over t times y equals t, with an initial value at t equal to one. The coefficient one over t is continuous on positive times but not at zero. We can multiply by t on the positive interval, because there the integrating factor is t. Then the equation becomes the derivative of t times y equals t squared.

Integrating gives y equals one-third t squared plus C divided by t. If y at one equals one, C equals two-thirds. This formula solves the initial-value problem for all positive t. But the equation itself is not defined at t equal to zero, so we cannot demand it solve that same equation across zero. A formula can be well behaved near a point while the differential equation's coefficients are not, or vice versa. Always state the interval where the claimed equation is meaningful.

## How to recognize the method

Start by looking at the form, not by moving symbols. If y prime equals a time factor times a state factor, consider separation. If y prime plus p of t times y equals q of t, consider an integrating factor. Some equations fit both patterns. The simple decay equation y prime equals negative two y, for example, is separable and linear.

Other equations fit neither. The equation y prime equals t y plus y squared is not generally separable and is not linear in y. Failing to force it into a known template is not failure to solve; it is accurate recognition of the limits of a method. We might analyze its signs, look for a transformation, or use a numerical method.

One final rule is worth keeping. After deriving a candidate, substitute it into the original differential equation, verify the initial condition, and identify its interval. That three-part check catches most elementary errors and builds habits that remain useful when the formulas become far more complicated.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

**Preparation:** Single-variable differentiation and integration, logarithms and exponentials, partial fractions. **Question:** which algebraic transformations are legal, and how do we check a proposed solution?

### Separation

For \(y'=g(t)h(y)\), on an interval where \(h(y(t))\ne0\), define \(H'(y)=1/h(y)\). Then
\[
H(y(t))=\int g(t)\,dt+C.
\]
**Before dividing**, test \(h(c)=0\): \(y(t)\equiv c\) is an equilibrium solution (as long as the equation is defined).

For \(y'=(1+t)(1-y)\), \(y(0)=0\), set \(z=1-y\), giving \(z'=-(1+t)z\) and
\[
y(t)=1-e^{-t-t^2/2},\qquad y'(t)=(1+t)e^{-t-t^2/2}.
\]
For \(y'=y(1-y/3)\), \(y(0)=1\), partial fractions yield
\[
\frac{1}{y(1-y/3)}=\frac1y+\frac1{3-y},\quad
\ln\left|\frac{y}{3-y}\right|=t+C,\quad
 y(t)=\frac3{1+2e^{-t}}.
\]

### Integrating factor

For \(y'+p(t)y=q(t)\) on an interval \(I\) of continuity, define
\[
\mu(t)=\exp\left(\int_{t_0}^t p(s)\,ds\right),\qquad
 y(t)=\mu(t)^{-1}\left[y_0+\int_{t_0}^t\mu(s)q(s)\,ds\right].
\]
For \(y'+2y=6\), \(y(0)=1\): \(y=3-2e^{-2t}\). For \(y'+y=t\), \(y(0)=2\): \(y=t-1+3e^{-t}\). For \(y'+y/t=t\), \(t>0\), \(y(1)=1\): \(y=t^2/3+2/(3t)\). That last equation is not defined at \(t=0\).

### Exercises with answers

1. Solve \(y'=3t y\), \(y(0)=4\). **Answer:** \(y=4e^{3t^2/2}\).
2. Solve \(y'+3y=9\), \(y(0)=0\). **Answer:** \(y=3(1-e^{-3t})\).
3. Find all nonnegative solutions of \(y'=\sqrt{y}\), \(y(0)=0\) on \(t\ge0\) that never decrease. **Answer:** \(y(t)=0\) for \(t\le a\) and \((t-a)^2/4\) for \(t\ge a\), with any \(a\ge0\); also the zero solution. The right-hand side is not locally Lipschitz at zero.
4. Why is the formula \(y=t^2/3+2/(3t)\) not a solution to an initial-value problem on \((-1,1)\) for \(y'+y/t=t\)? **Answer:** the equation and formula are not defined at \(t=0\); an initial-value interval crossing zero is not available.

### Reading and references

- OpenStax, *Calculus Volume 2*, [Separable Equations](https://openstax.org/books/calculus-volume-2/pages/4-3-separable-equations) and [First-Order Linear Equations](https://openstax.org/books/calculus-volume-2/pages/4-5-first-order-linear-equations).
- MIT OCW 18.03SC, *Basic Differential Equations and Separable Equations*: https://ocw-preview.odl.mit.edu/courses/18-03sc-differential-equations-fall-2011/pages/unit-i-first-order-differential-equations/basic-de-and-separable-equations/
- Wikipedia: [Separation of variables](https://en.wikipedia.org/wiki/Separation_of_variables), [Integrating factor](https://en.wikipedia.org/wiki/Integrating_factor), [Logistic function](https://en.wikipedia.org/wiki/Logistic_function).
