# Semilinear Elliptic Equations: When the Source Depends on the Solution

**Track:** Multivariable Calculus from First Principles. **Focus:** nonlinear reaction terms, weak formulations, an energy functional, existence on an interval, and what linearization can and cannot tell us.

<!-- BEGIN SPOKEN LECTURE -->

# Semilinear Elliptic Equations: When the Source Depends on the Solution

A Poisson equation asks what shape a membrane takes when we specify the force acting on it. In the simplest one-dimensional version, we prescribe a function of position and solve for another function whose second derivative balances it. For example, if the load is a sine wave, the resulting displacement can be found by integrating twice or by using a Green function.

Now change one ingredient. Suppose the force depends on the displacement itself. If the membrane moves up, the force changes. The equation is no longer a linear inverse problem, even though its highest derivative appears linearly. This is a semilinear elliptic equation. The word semilinear says that the highest-order derivatives remain linear, while lower-order terms may depend nonlinearly on the unknown function.

We will use one equation throughout this lecture. On the interval from zero to pi, seek a function u that vanishes at both endpoints and satisfies: the negative second derivative of u equals lambda times u minus u cubed. Lambda is a real parameter. The linear part tries to amplify displacement when lambda is positive. The cubic term pushes back when the displacement becomes large. The competition creates something the linear Poisson equation cannot have: a threshold above which nonzero equilibrium shapes appear.

## Start by checking the obvious solution

The zero function is a solution for every value of lambda. That is easy, but it is not the whole story. A nonlinear equation can have several solutions for the same boundary data. Being able to solve the linearized equation does not tell us how many nonlinear solutions exist.

To see what the linearization says, imagine a tiny perturbation around zero. Cubing a tiny number makes it much smaller, so to first order the equation becomes negative u double prime equals lambda u. With zero endpoint values, nonzero solutions of this linear equation appear when lambda is the square of a positive integer. The first such value is one, and the associated shape is sine of x.

This observation suggests that something changes near lambda equal to one. But the linearized problem does not yet establish that a branch of nonlinear equilibria exists. To obtain that result, we will build an energy whose stationary points are exactly the solutions of our equation.

## Turn the equation into a weak statement

Multiply the equation by a smooth test function that also vanishes at the endpoints, and integrate. Integrating the second derivative by parts moves one derivative onto the test function. The boundary term disappears because the test function is zero at both ends.

The result says: the integral of u prime times test-function prime equals the integral of lambda u minus u cubed, multiplied by the test function. This is our weak equation. We can ask for solutions with square-integrable first derivatives rather than insisting from the outset on a continuous second derivative.

On this finite interval, a function in the usual zero-trace Sobolev space H one has a continuous representative and belongs to every finite L p space, so the cubic term is well-defined. In higher dimensions, the function spaces and permitted growth of the nonlinearity require more care. We are deliberately using the interval so the important issue is the nonlinear argument, not a hidden integrability restriction.

There is a natural energy: half the integral of the squared derivative, minus lambda over two times the integral of the squared function, plus one quarter the integral of the fourth power. Differentiate this energy in the direction of a test function. The three terms become, respectively, the derivative inner product, minus lambda times u, and plus u cubed. Setting that variation equal to zero recovers the weak equation.

This is the first important connection. The same object can be viewed as a stationary boundary-value problem or as a critical point of an energy. But a critical point need not be a minimum. Later, when we discuss bifurcation, we will distinguish minimizers, unstable equilibria, and directions where the second variation vanishes.

## Why a minimizer exists

An infinite-dimensional minimization problem is not settled by drawing an energy graph. We need compactness. The quartic term prevents the energy from dropping without bound when u becomes large. More precisely, at every point, one quarter u to the fourth minus lambda over two times u squared is at least minus lambda squared over four. Integrating shows that our energy controls half the total squared derivative, up to a fixed additive constant.

Because u is zero at both endpoints, controlling its derivative also controls its H one norm. Thus any sequence whose energies approach the infimum remains bounded in H one. We can take a weakly convergent subsequence. In one dimension, bounded H one sequences also have strongly convergent subsequences in ordinary L two and L four. The derivative energy is lower semicontinuous under weak convergence; the quadratic and quartic integrals pass to the limit using strong convergence. Hence the limiting function attains the minimum.

We have established that a minimum exists for every lambda. What we have not yet established is whether that minimizer is zero or nonzero.

## The exact threshold at lambda equal to one

Here the first Dirichlet eigenvalue supplies an elegant test. For every function vanishing at zero and pi, the integral of its squared derivative is at least the integral of its square. Equality is achieved by the first sine mode.

When lambda is at most one, insert that inequality into the energy. The quadratic part is nonnegative, and the quartic part is also nonnegative. The energy is therefore at least zero, with equality only for the zero function. Zero is the unique global minimizer. In fact, testing the equation against u shows there is no nonzero weak solution at all when lambda is at most one: the derivative energy equals lambda times the L two norm squared minus the integral of u to the fourth, which is incompatible with the eigenvalue inequality unless u vanishes.

When lambda exceeds one, we can demonstrate that the zero function is not a minimizer. Try a small multiple of sine of x. Its derivative energy and its squared-function integral are equal. The quadratic part of the energy is now negative, proportional to one minus lambda. The quartic part is positive but scales with the fourth power of the small amplitude. For a sufficiently small nonzero amplitude, the negative quadratic contribution wins. The energy is less than zero.

Since the true minimizer has energy no greater than that trial function, it cannot be zero. A nonzero equilibrium exists. This argument explains the threshold, and it does so without pretending that a single sine wave is an exact nonlinear solution.

## Why the sine-wave guess is not exact

Substitute a sine wave with amplitude a into the cubic term. Sine cubed is not just another multiple of sine. It also contains a third harmonic, sine of three x. A single sine mode cannot satisfy the differential equation point by point except when the amplitude vanishes.

Nevertheless, retaining only the first sine mode can be a useful approximation. Project the residual onto sine of x. The resulting scalar equation has a trivial solution a equal to zero and, when lambda is greater than one, two nonzero approximate amplitudes. Their squares equal four thirds times lambda minus one. This gives a first prediction of a pair of branches, one positive and one negative, emerging with square-root scaling.

The third harmonic is not an embarrassment to conceal. It tells us exactly why the finite-dimensional approximation is not a proof and what correction the full equation must supply. A later lecture will derive that correction systematically.

## The significance of positivity

The energy does not distinguish u from minus u: both have the same value. If u is a minimizer, its absolute value has the same energy and is also a minimizer. A nonzero nonnegative minimizer is actually positive at every interior point. One way to see this in our one-dimensional setting is to use regularity to recover the ordinary differential equation. At an interior zero of a nonnegative smooth solution, the derivative also vanishes. The initial-value uniqueness theorem would then force the solution to be identically zero, a contradiction.

Thus when lambda exceeds one, we obtain at least two distinct nonzero solutions, a positive solution and its negative. Zero remains a solution as well. In this example the positive solution is unique, but that requires an additional comparison argument. General semilinear equations can admit substantially more complicated solution sets.

## Equilibria and an evolution equation

The same energy gives a time-dependent interpretation. Let u evolve according to its second derivative plus lambda u minus u cubed, while the endpoint values stay fixed at zero. A stationary state of that evolution is precisely a solution of our semilinear elliptic boundary problem.

Along a sufficiently smooth evolving solution, the rate of change of the energy equals minus the integral of the squared time derivative. So the energy cannot increase. This makes the energy landscape relevant to stability, although energy decrease alone is not a complete stability theorem. Near the zero equilibrium, the first sine mode grows when lambda exceeds one and decays when lambda is below one. The threshold is therefore visible both in the stationary problem and in the evolution.

Notice the distinction between three claims. The energy argument establishes the existence of a nonzero minimizer. The linearization at zero identifies a loss of stability. A bifurcation theorem describes the local structure of the entire solution set near the threshold. They reinforce one another, but none is a substitute for the others.

We started with the familiar linear Poisson equation, changed the source into a function of the unknown, and discovered a qualitatively different problem. Integration by parts gives the weak formulation. Compactness gives a minimizer. The first eigenvalue predicts the point where a nontrivial equilibrium becomes energetically favorable. And the cubic term explains both the amplitude limitation and the appearance of new harmonics.

The next mathematical challenge is constructive: if we know a function that lies below a solution and another that lies above it, can we actually build a solution between them, even though the nonlinear reaction is not globally monotone? That question leads to subsolutions, supersolutions, and monotone iteration.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not narrated)

### Model problem and weak energy

On \(I=(0,\pi)\), with \(u(0)=u(\pi)=0\),
\[
-u''=f_\lambda(u)=\lambda u-u^3,
\quad
J_\lambda(u)=\frac12\int_I|u'|^2-\frac\lambda2\int_I u^2+\frac14\int_Iu^4.
\]
The Fréchet derivative for \(u,v\in H_0^1(I)\) is
\[
DJ_\lambda(u)[v]=\int_I u'v'-\int_I (\lambda u-u^3)v.
\]
One-dimensional Sobolev embedding makes these integrals well-defined. A weak critical point solves the displayed equation in distributions; standard one-dimensional bootstrap yields a classical \(C^2\) solution.

### Coercivity and the direct method

Since \(\frac14t^4-\frac\lambda2 t^2=\frac14(t^2-\lambda)^2-\frac{\lambda^2}{4}\),
\[
J_\lambda(u)\ge\tfrac12\|u'\|_{L^2}^2-\tfrac{\pi\lambda^2}{4}.
\]
A minimizing sequence is bounded in \(H_0^1\). Weak compactness and compact \(H_0^1(0,\pi)\hookrightarrow L^p(0,\pi)\) for every finite \(p\) allow passage to the limit in the quadratic and quartic terms. Weak lower semicontinuity of \(\|u'\|_2^2\) completes the proof.

The sharp interval Poincaré inequality is \(\int_I |u'|^2\ge\int_I u^2\). If \(u\) solves the equation,
\[
\int_I |u'|^2=\lambda\int_Iu^2-\int_Iu^4.
\]
Hence \(\lambda\le1\) forces \(u=0\). For \(\lambda>1\),
\[
J_\lambda(\varepsilon\sin x)
=\frac{\pi}{4}(1-\lambda)\varepsilon^2+\frac{3\pi}{32}\varepsilon^4<0
\]
for small \(\varepsilon>0\), proving the minimizer is nonzero. \(J_\lambda(|u|)=J_\lambda(u)\); smoothness and initial-value uniqueness imply a nonzero nonnegative solution is positive in the interior. By oddness, \(-u\) is also a solution.

### One-mode Galerkin approximation and the omitted mode

The identity \(\sin^3x=(3\sin x-\sin3x)/4\) yields, for \(u=a\sin x\),
\[
\langle -u''-\lambda u+u^3,\sin x\rangle
=\frac\pi2\big((1-\lambda)a+\tfrac34a^3\big).
\]
Thus the Galerkin branch obeys \(a^2=4(\lambda-1)/3\), but the full residual has a \(-a^3\sin3x/4\) component. This is a **projection formula**, not an exact nonlinear solution. The 062000 companion supplies the Lyapunov–Schmidt correction.

### Gradient evolution

For \(u_t=u''+\lambda u-u^3\) with zero Dirichlet data and sufficient smoothness,
\[
\frac{d}{dt}J_\lambda(u(t))
=DJ_\lambda(u)[u_t]=-\int_I |u_t|^2\,dx\le0.
\]
The linearized growth rates at zero are \(\lambda-n^2\) for the sine modes, \(n\ge1\).

### Exercises with answers

1. **Other interval.** What is the threshold on \((0,L)\)? **Answer:** \(\lambda_1=(\pi/L)^2\), from the first Dirichlet eigenvalue.
2. **Energy test.** Why does \(J_\lambda(a\sin x)<0\) for small \(a\ne0\) when \(\lambda>1\)? **Answer:** a negative quadratic term dominates the positive quartic term.
3. **Weak residual.** What is the test-function equation? **Answer:** \(\int u'v'=\int(\lambda u-u^3)v\) for all \(v\in H_0^1\).
4. **Symmetry.** Does finding \(u>0\) imply a negative solution? **Answer:** yes, since \(f_\lambda\) is odd.
5. **Modes.** Why is \(a\sin x\) not an exact solution for \(a\ne0\)? **Answer:** the cubic generates a third sine harmonic.
6. **Dimensions.** Why did we use an interval for the direct-method proof? **Answer:** its compact embedding into \(L^4\) has no higher-dimensional critical-exponent complication.

### Sources and further reading

- [Jean-Pierre Puel, *Semilinear elliptic equations* (2018)](https://pantheon.ufrj.br/items/d094491a-14db-450f-8508-0298c1366e0c), variational and monotone nonlinear elliptic equations.
- [A. Ambrosetti and A. Malchiodi, *Nonlinear Analysis and Semilinear Elliptic Problems*](https://assets.cambridge.org/97805218/63209/frontmatter/9780521863209_frontmatter.pdf), variational principles and bifurcation.
- [Wikipedia: Partial differential equation](https://en.wikipedia.org/wiki/Partial_differential_equation), terminology distinguishing nonlinearities in highest- and lower-order derivatives.
- [Wikipedia: Dirichlet eigenvalue](https://en.wikipedia.org/wiki/Dirichlet_eigenvalue), the spectral threshold; see also library lectures `multivariable-calculus:037000`, `047000`, `048000`.
