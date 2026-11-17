# First Variation: Optimizing a Function Instead of a Vector

**Track:** Multivariable Calculus from First Principles. **Focus:** directional derivatives of functionals, admissible perturbations, second variations, and when an energy minimizer really follows from stationarity.

<!-- BEGIN SPOKEN LECTURE -->

# First Variation: Optimizing a Function Instead of a Vector

Suppose you want to find a number that minimizes a formula. Calculus tells you to differentiate. Suppose you want to find a vector that minimizes a formula. Multivariable calculus tells you to set a gradient to zero, perhaps subject to constraints. Now suppose the unknown is an entire curve. Every point of the curve can move, but those movements are linked by smoothness and boundary conditions. What does it mean to differentiate with respect to a function?

That is the starting question of the calculus of variations. It is a direct continuation of finite-dimensional optimization, not a different kind of mathematical magic. The central idea is familiar: replace a full problem by its response to a small change. The difference is that a small change is now a function of position, and the derivative must tell us what happens for every allowed change, not just along a few coordinate directions.

Think of a flexible string stretched across a gap. It can bend in infinitely many ways. We might prefer a shape that does not stretch or bend too sharply, but also need it to respond to a distributed force. Or imagine reconstructing a spatial field from measurements: we want the field to agree with data while avoiding excessive variation between neighboring locations. Both problems optimize an entire function.

## What is a functional?

A functional takes a function as input and returns a number. For example, consider functions defined from zero to one that vanish at both ends. Assign each candidate curve the energy equal to one half the integral of its squared slope, minus the integral of its height. The first term penalizes rapid changes; the second represents the work of a uniform upward load, using a particular sign convention. Call this energy E of u.

The condition that u vanish at zero and one is important. We are not choosing arbitrary graphs. We are choosing graphs with their endpoints pinned. In the optimization language from our constraint lectures, the boundary values define the feasible set. When we perturb a feasible curve, we must not pull its endpoints away from their pins.

Take any sufficiently smooth function eta that also vanishes at both ends. For a small real number t, consider u plus t times eta. That family gives a line through the space of functions, in exactly the same way that x plus t times d gives a line through ordinary Euclidean space. The first variation of E at u in the direction eta is the ordinary derivative with respect to t, evaluated at zero.

In our example, the slope of u plus t eta is u prime plus t eta prime. Square it, integrate, subtract the load term, and collect powers of t. The coefficient of the first power of t is the integral of u prime times eta prime, minus the integral of eta. That number is the first variation in direction eta. The coefficient of one half t squared is the integral of eta prime squared. We have not guessed an infinite-dimensional gradient. We have differentiated a one-variable expression exactly.

This is called a directional derivative, or in an appropriate setting a Gâteaux derivative. A Fréchet derivative asks for a stronger statement: one bounded linear functional must approximate the change uniformly across small perturbations in a specified norm. For the quadratic energy on the usual one-dimensional energy space, that stronger property does hold. But directional derivatives and Fréchet derivatives are not interchangeable by definition. Which function space and which norm we use can matter.

## From one direction to all directions

At a local minimizer, moving a little in either direction along every admissible line must not lower the energy. So the first variation must vanish for every eta that vanishes at the endpoints. Notice the force of the word every. If we test only a few trial perturbations, we may find a curve that looks stationary within our small family but is still improvable by a perturbation we never considered.

Our stationarity condition is thus: the integral of u prime eta prime equals the integral of eta, for every allowed eta. This already looks different from an ordinary derivative equal to zero. It is an identity involving two functions. Later we will call it a weak equation. For now, it is simply the exact first-order condition produced by optimization.

If u is twice differentiable, we can integrate the left side by parts. The boundary term vanishes because eta is zero at both endpoints. What remains says that the integral of negative u double prime minus one, multiplied by eta, is zero for every smooth test perturbation. The fundamental lemma of the calculus of variations then says the coefficient must vanish pointwise, under the continuity assumptions we are using. We recover the differential equation: negative u double prime equals one.

Solve it. Integrate twice. The general solution is a downward-opening quadratic, and the pinned endpoint values select u of x equal to one half times x times one minus x. That curve is not a guess based on its visual shape. It is the solution of the stationarity equation obtained by testing every allowed direction.

## An exact small trial family

We can discover the same curve by an unusually fortunate shortcut. Restrict attention to trial functions of the form a times x times one minus x, with a an ordinary real coefficient. Now we are back in finite-dimensional optimization, although with only one coordinate.

The slope of this trial curve is a times one minus two x. Integrating its squared slope gives a squared divided by three. Integrating its height gives a divided by six. Consequently the energy is a squared divided by six, minus a divided by six. Differentiate with respect to a and set the answer to zero. We obtain a equal to one half.

This time the one-parameter family happened to contain the exact solution of the full variational problem. That is not typical. Change the forcing from a constant to something varying with position, and this particular quadratic family generally cannot reproduce the exact solution. Minimizing over a chosen collection of functions is an approximation unless we prove that its minimizer also satisfies the condition for all admissible perturbations.

The distinction is fundamental in numerical methods. A finite-element method will eventually replace an infinite-dimensional problem by a finite-dimensional one. It will then solve exactly, or nearly exactly, within the chosen finite-dimensional space. The remaining error is not necessarily a failure of the linear solver. It may be the limitation of the functions we allowed it to choose.

## Stationary is not the same as minimizing

In our string energy, we can go further. Let u star denote the solution we just found, and compare it with any other feasible u star plus eta. Expand the energy exactly. The linear term disappears because u star satisfies the first-variation identity. What remains is one half the integral of eta prime squared. It cannot be negative. It vanishes only if eta is constant almost everywhere, and the zero boundary values then force that constant to be zero.

Therefore u star is the unique global minimizer in the appropriate energy space. We obtained much more than stationarity. We obtained a certificate of global optimality and uniqueness, analogous to a positive-definite Hessian in finite-dimensional optimization.

The second variation here sends a pair of directions eta and zeta to the integral of eta prime times zeta prime. Evaluating both directions at eta gives the nonnegative quadratic form that certifies convexity. In fact it is positive for every nonzero admissible direction. The boundary pins remove the constant direction that otherwise would have zero slope and zero energy penalty.

This is a useful place to remember the role of constraints. If the endpoints were not pinned and we had no additional term controlling the average height, adding a constant to u would not change the squared-slope term. With a nonzero uniform load, the negative height term could then drive the energy downward without bound. The same formula can define a well-behaved optimization problem on one feasible space and an ill-posed problem on another.

What if the energy has a negative quadratic term? Consider a different functional: one half the integral of squared slope minus squared height over an interval of length L, again with pinned endpoints. The zero curve is stationary because every first-order term vanishes there. But test it in the direction of a sine arch that is zero at both ends. The energy change is proportional to pi squared minus L squared. If the interval is longer than pi, that change is negative. The zero curve is not even a local minimum. A vanishing first variation is only a necessary condition at an interior minimizer, not an unconditional certificate that a minimum exists.

This example also foreshadows a phenomenon from spectral theory. Whether the derivative penalty beats the negative height term depends on the lowest eigenvalue of a boundary-value problem. The spectrum of an operator can decide the sign of the second variation, just as the eigenvalues of a Hessian decide local curvature in finite dimensions.

## Why the norm matters

A candidate function is not merely a table of values. In an energy containing a squared derivative, we need a class where the derivative can be interpreted and integrated. Smooth functions are convenient for the initial calculation, but they are not complete under the natural energy norm: a sequence of smooth curves can converge to a curve with corners that still has square-integrable slope.

The corresponding complete space is called a Sobolev space. For zero endpoint values on an interval we write H naught one, or H one with zero boundary trace. In that space, the derivative is understood weakly, and the energy is still meaningful. Poincaré's inequality tells us that for functions pinned at the ends, the size of the function can be controlled by the size of its derivative. This turns the derivative penalty into genuine control of the whole candidate, not just its wiggliness.

There is one further subtlety about gradients. The first variation is a linear functional of eta. Calling it a gradient requires an inner product that turns such functionals into vectors or functions. With the usual L two inner product, a smooth candidate's formal gradient looks like negative u double prime minus one. With an H one inner product, the gradient is a different function obtained by solving another equation. The first variation itself is the invariant object; a particular gradient depends on the geometry we put on the space of functions.

This is why numerical optimization of fields can be sensitive to how it measures a step. The same physical energy can generate very different algorithms under different inner products or preconditioners. The choice is not cosmetic.

## Where the variational viewpoint takes us

We began with a scalar energy assigned to a whole curve. We perturbed the curve in an admissible direction, differentiated a one-parameter family, and demanded stationarity in every direction. For a smooth solution, integration by parts turned that condition into a differential equation. The second variation and the boundary constraints then told us why its solution was a true minimum in this particular example.

The important bridge is already built. A differential equation can emerge as the optimality condition of a functional; the corresponding integral identity can remain meaningful even when classical second derivatives do not. Next, the boundary terms we discarded will become part of the story, rather than a nuisance to hide.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not narrated)

### First and second variations

Let

\[
V=H_0^1(0,1),\qquad
E(u)=\frac12\int_0^1 |u'(x)|^2\,dx-\int_0^1 f(x)u(x)\,dx,
\]

with \(f\in L^2(0,1)\). The weak derivative is used in \(H_0^1\). For \(v,w\in V\),

\[
\begin{aligned}
DE(u)[v]&=\left.\frac{d}{dt}E(u+tv)\right|_{t=0}
=\int_0^1 u'v'\,dx-\int_0^1 fv\,dx,\\
D^2E(u)[v,w]&=\int_0^1 v'w'\,dx,\\
E(u+v)-E(u)&=DE(u)[v]+\tfrac12\int_0^1 |v'|^2\,dx.
\end{aligned}
\]

These are Fréchet derivatives on \(H_0^1\) endowed with its standard norm, by boundedness and the exact quadratic expansion. A condition \(DE(u)[v]=0\) for all \(v\in V\) is the *weak equation*. Smoothness is only needed to turn the weak identity into the pointwise equation \(-u''=f\).

For \(f=1\), the minimizer is \(u_*(x)=x(1-x)/2\), and the energy gap is exactly

\[
E(u_*+v)-E(u_*)=\tfrac12\|v'\|_{L^2}^2.
\]

Poincaré's inequality implies the gap controls \(\|v\|_{H^1}\) up to a domain-dependent constant. Thus \(u_*\) is the unique global minimizer.

### One-dimensional Ritz restriction

For \(u_a(x)=a x(1-x)\), and \(f=1\),

\[
\int_0^1|u_a'|^2\,dx=\frac{a^2}{3},\quad
\int_0^1u_a\,dx=\frac a6,\quad
E(u_a)=\frac{a^2-a}{6},\quad a_*=\frac12.
\]

For the *different* load \(f(x)=x\), the same trial family yields

\[
E(u_a)=\frac{a^2}{6}-\frac{a}{12},\qquad a_{\rm Ritz}=\frac14,
\]

whereas the exact solution is \(u_*(x)=(x-x^3)/6\). The Ritz solution is optimal in the trial subspace, not the entire admissible space.

### Counterexample: stationary but unstable

On \((0,L)\), define \(J(u)=\frac12\int_0^L(|u'|^2-|u|^2)\,dx\). The zero function is stationary. Taking \(v(x)=\sin(\pi x/L)\),

\[
J(tv)-J(0)=\frac{t^2}{4L}(\pi^2-L^2).
\]

For \(L>\pi\), every nonzero sufficiently small \(t\) decreases the energy, so zero is not a local minimizer. At \(L=\pi\) this direction is flat; the second variation is not positive definite.

### Exercises with answers

1. **Perturbation:** For \(E(u)=\frac12\int_0^1 a(x)|u'|^2-\int_0^1fu\), show \(DE(u)[v]=\int a u'v'-fv\). **Answer:** Differentiate \(a(u'+tv')^2/2\) at \(t=0\); no derivatives of \(a\) appear until integration by parts.
2. **Pinned endpoints:** Why can a nonzero constant not belong to \(H_0^1(0,1)\)? **Answer:** Its endpoint traces are nonzero, violating the essential boundary condition.
3. **Subspace trap:** Compute the best quadratic trial coefficient for \(f=x\). **Answer:** \(a=1/4\), not the coefficient of an exact solution in that family.
4. **Curvature:** What makes \(J(u)=\frac12\int(|u'|^2-|u|^2)\) different from the positive energy? **Answer:** The second variation is indefinite if the domain is long enough; zero first variation need not give minimum.

### Sources and further reading

- L. C. Evans, [*Mathematical Methods for Optimization* / calculus-of-variations notes](https://math.berkeley.edu/~evans/math%20195%20notes.pdf), for first variations, Euler–Lagrange equations, and endpoint assumptions.
- Luca Heltai, [*Model Problems and the Ritz–Galerkin Method*](https://luca-heltai.github.io/nmpde/lectures/lecture-01/), for a variational Poisson problem, coercivity, and the passage from a function space to a discrete one.
- [Wikipedia: Calculus of variations](https://en.wikipedia.org/wiki/Calculus_of_variations) and [First variation](https://en.wikipedia.org/wiki/First_variation), for terms and historical orientation.

*Teaching connections:* `multivariable-calculus:027000` supplies the analogous second variation along finite-dimensional constraints; `differential-equations:010000` surveys the weak Poisson formulation; the later lectures in this route develop boundary conditions, existence, and discretization explicitly.
