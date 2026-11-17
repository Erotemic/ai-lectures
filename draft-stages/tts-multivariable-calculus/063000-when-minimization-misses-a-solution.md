# When Minimization Misses a Solution: From Critical Points to Mountain Passes

**Track:** Multivariable Calculus from First Principles. **Focus:** accessible energy landscapes, non-minimizing critical points, path minimax, and the transition from scalar calculus to a function-valued unknown.

<!-- BEGIN SPOKEN LECTURE -->

# When Minimization Misses a Solution: From Critical Points to Mountain Passes

Imagine looking for the lowest point of a landscape. That is the optimization problem most of us first learn. We differentiate, find where the derivative vanishes, and check which candidates are minima. In several variables we also learn about saddle points, where the slope vanishes even though the landscape rises in one direction and falls in another.

But suppose our unknown is not a number or a vector. It is a whole function, such as the shape of a stretched membrane. An energy assigns one number to each possible shape. We want shapes where the first variation of the energy is zero. It is tempting to find those shapes by minimizing the energy. Sometimes that works beautifully. Sometimes the energy has no lowest value at all, yet a nonzero stationary shape still exists. This lecture develops a method for seeing where such a shape might be hiding.

We will begin with a polynomial of one variable. We can solve everything exactly. Then we will add a second coordinate and see a genuine saddle. Only then will we return to differential equations. The same reasoning survives, but it takes an additional compactness argument to turn a geometric prediction into a theorem.

## A minimum and two other stationary points

Consider a function of a real number x. Its value is one half x squared minus one quarter x to the fourth power. Near zero the positive quadratic term dominates, so zero is a local minimum. Far away, the negative fourth power dominates, and the value falls without bound.

Differentiate. The result is x minus x cubed, or x times one minus x squared. It vanishes at negative one, zero, and positive one. The second derivative is one minus three x squared. At zero it is positive, so we really have a strict local minimum. At positive one and negative one it is negative, so those two stationary points are local maxima.

Evaluate the energy. At zero it is zero. At either positive or negative one it is one quarter. At two it is negative two. We have a very concrete puzzle. Starting at the local minimum zero, we can eventually reach a point of lower energy at two, but we cannot get there without first climbing above zero. Along the real number line, every continuous journey from zero to two crosses one. Consequently, the highest energy encountered on any such journey is at least one quarter. The direct path from zero to two encounters no value higher than one quarter, so that bound is exact.

Notice what we did not do. We did not minimize the energy over every possible x. That would fail because the energy tends to negative infinity. We minimized the greatest energy encountered along a path. The resulting number, one quarter, is a *minimax value*: first take the maximum along a particular path, then take the minimum of those maxima over all allowed paths.

This is already a useful shift in viewpoint. An energy can have interesting stationary points even if it has no global minimum. The structure of the available paths can force us to encounter a critical height.

## Why the mountain pass becomes a saddle

A one-dimensional local maximum looks like the top of a hill, not a pass between mountains. Add a second coordinate y and consider the original polynomial plus y squared. Now the landscape rises whenever we move away from y equals zero. In the x direction, however, it falls on either side of x equals one. At the point with x equal to one and y equal to zero, the second derivative in the x direction is negative, and the second derivative in the y direction is positive. This point is a saddle.

We can check that the minimax calculation has not changed. Take any continuous path from the origin to the point with x equal to two and y equal to zero. The x coordinate of the path must pass through one. When it does, the polynomial contributes one quarter, while y squared contributes a nonnegative amount. So every path has a highest energy of at least one quarter. Following the x axis achieves precisely one quarter. The pass is forced, even though the path is free to wander across the entire plane.

The geometry, not an explicit derivative calculation, identified the important level. This matters in higher dimensions, where solving all stationary equations directly may be very difficult. We do not need to guess the precise saddle before we know that the landscape forces a path to climb.

There is one subtlety. A minimax value is just a number until we prove that it is attained at a stationary point. In the plane, the usual compactness arguments let us complete that step under suitable assumptions. In a space of functions, minimizing paths can stretch, oscillate, or concentrate. Their high points may have no convergent subsequence. A picture of a mountain pass is therefore not yet an existence theorem.

## Replacing a vector by an entire function

Now take a string fixed at both ends, with positions running from zero to pi. Its displacement is a function u of position. Suppose its energy is one half of the integral of the square of its slope, minus one quarter of the integral of the fourth power of its displacement.

The first term penalizes rapid changes in the string. The negative fourth-power term rewards large displacement, enough that the total energy can become very negative. This is a mathematical model, not a claim that a physical string always has such a potential. It is useful precisely because the competition between the terms is easy to describe.

To differentiate this energy, perturb the shape by a small multiple of another function v that also vanishes at the endpoints. Differentiate with respect to the perturbation parameter at zero. The result is the integral of u prime times v prime, minus the integral of u cubed times v. Setting this expression to zero for every test function v is the weak form of the equation: negative u double prime equals u cubed, with zero displacement at the endpoints.

The zero function plainly satisfies the equation. But is it the only solution? Look at energy near zero. On this fixed interval, the size of a function can be controlled by the square-integral of its derivative. In particular, the integral of u to the fourth power is bounded by a constant times the fourth power of the slope norm. The positive quadratic term therefore dominates for small nonzero shapes. The zero shape is a strict local minimum in the energy norm.

Now choose any smooth nonzero shape that vanishes at both endpoints. Multiply it by a large positive number t. The slope energy grows like t squared, while the negative displacement term grows like t to the fourth. For large t, the energy becomes negative. Just as in the polynomial, we can begin at the local minimum and travel to a shape with lower energy. Somewhere along any continuous route in the function space, the energy must pass a positive barrier.

The analogy is exact at the level of the energy's geometry. It is not yet exact at the level of existence. We must still know whether a sequence of nearly optimal routes has high points that settle down to a genuine stationary function.

## What makes a function space different

In a finite-dimensional space, a bounded sequence always has a convergent subsequence. We use this fact so often that it can become invisible. In a space of functions it fails dramatically.

Imagine a sequence of increasingly narrow spikes. A spike can become taller as it becomes narrower, while selected integrals of its size remain controlled. Or imagine functions whose oscillations become faster and faster. Their values may average out when tested against smooth probes, but they do not necessarily approach one fixed function in a strong norm.

This is why variational analysis distinguishes weak convergence from strong convergence. A sequence of functions may converge weakly, meaning that every continuous linear measurement settles to a limit, without the functions becoming close in norm. If an energy involves a nonlinear power of the function, weak convergence alone may not allow us to pass to the limit.

For this particular string problem, one-dimensional Sobolev compactness rescues the argument. A bounded sequence of functions with controlled slope and fixed endpoints has a subsequence that converges uniformly. Uniform convergence is more than enough to control the fourth-power term. That compactness will be the key to a rigorous existence proof.

The important lesson is not that every nonlinear energy behaves this way. Some energies are convex and can be minimized directly. Others have barriers but fail the compactness needed for a mountain-pass theorem. Still others have many competing passes and numerous critical points. We have to verify the geometry and the convergence mechanism separately.

## What to remember before the theorem

Let us collect the ingredients without hiding their logic. First, our objective is a stationary point, not necessarily the lowest value. Second, a local minimum can be surrounded by an energy barrier even when the energy eventually drops below its starting value. Third, we look at continuous paths joining two low-energy configurations, and consider the least possible maximum energy along such paths. Fourth, we need an argument that this critical height corresponds to an actual critical function, rather than to a sequence that disappears through the infinite dimensions.

In elementary calculus, the derivative test tells us where a stationary point is once we have a candidate. The mountain-pass idea works in the opposite direction: geometry and compactness together can guarantee the presence of a stationary point before we have an explicit formula.

This is the first conceptual step from minimizing energies to discovering nonlinear states that a minimization algorithm would miss.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not narrated)

### Exact finite-dimensional model

Let
\[
 f(x)=\tfrac12 x^2-\tfrac14 x^4,\qquad F(x,y)=f(x)+y^2.
\]
Then
\[
 f'(x)=x-x^3,\quad f''(x)=1-3x^2,\quad
 \nabla^2F(1,0)=\operatorname{diag}(-2,2).
\]
Moreover \(f(0)=0\), \(f(\pm1)=1/4\), \(f(2)=-2\). For any continuous \(\gamma:[0,1]\to\mathbb R^2\) from \((0,0)\) to \((2,0)\), the intermediate value theorem gives \(t_0\) with \(\gamma_1(t_0)=1\). Hence
\[
 \max_tF(\gamma(t))\geq F(1,\gamma_2(t_0))=\tfrac14+\gamma_2(t_0)^2\geq\tfrac14.
\]
The straight path \(\gamma(t)=(2t,0)\) attains equality, so \(c=1/4\).

### A function-valued energy

Take \(H=H_0^1(0,\pi)\) with norm \(\|u\|_H=\|u'\|_{L^2}\), and define
\[
 J(u)=\frac12\int_0^\pi |u'|^2\,dx-\frac14\int_0^\pi u^4\,dx.
\]
The derivative is
\[
 J'(u)[v]=\int_0^\pi u'v'\,dx-\int_0^\pi u^3v\,dx,
\]
so \(J'(u)=0\) is the weak Dirichlet problem \(-u''=u^3\).

For \(u\in H\), the fundamental theorem of calculus for the absolutely continuous representative and Cauchy–Schwarz imply
\[
 |u(x)|\leq\sqrt\pi\,\|u'\|_2,
 \qquad \int_0^\pi u^4\,dx\leq\pi^3\,\|u'\|_2^4.
\]
Thus \(J(u)\geq \frac12t^2-\frac{\pi^3}4t^4\), where \(t=\|u'\|_2\). In particular \(J\) is positive on a sufficiently small sphere in \(H\), whereas \(J(s\phi)\to-\infty\) for any fixed nonzero \(\phi\in H\) as \(s\to+\infty\).

### Exercises with answers

1. **Critical points.** Find all critical points of \(f\). **Answer:** \(-1,0,1\); the outer two are local maxima and zero a strict local minimum.
2. **Why paths matter.** Could a path in the plane avoid the critical energy \(1/4\) by going around the saddle? **Answer:** No. Every path must reach \(x=1\), where \(F\geq1/4\).
3. **Energy scaling.** Show that \(J(t\phi)\to-\infty\). **Answer:** \(J(t\phi)=t^2\|\phi'\|_2^2/2-t^4\|\phi\|_4^4/4\), and the quartic coefficient is strictly positive before its minus sign.
4. **Stationarity.** Why does \(J'(u)=0\) not by itself imply an energy minimum? **Answer:** The derivative detects first-order stationarity only; a Hessian or separate comparison is needed to classify a critical point.

### Sources and further reading

- [Ambrosetti and Rabinowitz (1973), *Dual variational methods in critical point theory and applications*](https://doi.org/10.1016/0022-1236(73)90051-7), original source of the mountain-pass framework.
- [Variational Methods lecture notes, University of Pisa, §7](https://poisson.phc.dm.unipi.it/~fpmaiale/notes/MetodiVariazionali.pdf), path minimax and deformation argument.
- [Wikipedia: Mountain pass theorem](https://en.wikipedia.org/wiki/Mountain_pass_theorem), overview and terminology.
- Library preparation: `multivariable-calculus:031000`, `033000`, `035000`, `036000`, `037000`.
