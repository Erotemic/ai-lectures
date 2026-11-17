# Harmonic Measure: Which Part of the Boundary Matters?

**Track:** Multivariable Calculus from First Principles. **Focus:** representing harmonic solutions by boundary probability measures, Poisson kernels, Brownian exit laws, and limits of boundary regularity.

<!-- BEGIN SPOKEN LECTURE -->

# Harmonic Measure: Which Part of the Boundary Matters?

Suppose a room is in thermal equilibrium. Part of its boundary is held hot, and the rest is held cold. How much does the hot portion affect the temperature at one specified point in the interior?

One answer is to solve the entire boundary-value problem. A more revealing answer is to assign the hot portion a number between zero and one. That number tells us its influence at the observation point, independent of the actual hot and cold temperatures. The number is called the harmonic measure of that boundary portion, as seen from that interior point.

The same quantity has a probabilistic interpretation. Release a Brownian particle at the observation point and stop it the first time it reaches the boundary. Harmonic measure is the probability that its exit point lies in the selected portion of the wall. This is not a metaphor. The probability distribution and the elliptic boundary-value problem determine the same mathematical object.

Our earlier lecture on the Poisson kernel gave an explicit formula for a disk. We will now understand what the formula measures, derive a testable example, and see why the right generalization to irregular domains is a measure rather than always a neat density.

## The easiest exit problem is one dimensional

Start with a particle moving randomly on the interval from zero to one. Its position fluctuates with no drift, and we stop it upon hitting either endpoint. Let h of x be the probability that it hits the endpoint one before endpoint zero, starting at position x.

The boundary conditions are immediate. Starting at zero, the chance is zero. Starting at one, the chance is one. In the interior, the probability has no preferred local direction; its second derivative is zero. The unique solution is h of x equals x.

At position one quarter, there is a one-quarter chance of escaping at the right endpoint. At position three quarters, the chance is three quarters. We can also read this from a classical harmonic boundary-value problem: for arbitrary endpoint temperatures a and b, the equilibrium temperature is a times one minus x, plus b times x. The two coefficients are the exit probabilities for the two endpoints.

Notice a conceptual advantage. We can solve the two probability problems once and then reuse the results for every pair of endpoint values. Harmonic measure turns an infinite family of boundary conditions into a single reusable rule for how boundary information reaches an interior point.

## A measure rather than a list of weights

In a higher-dimensional domain the boundary contains infinitely many points. There is no finite list of endpoint probabilities. Instead, for each interior point x, harmonic measure assigns a probability to suitable subsets of the boundary. The whole boundary has measure one, disjoint portions add their probabilities, and no portion has negative probability.

We write this object as harmonic measure with pole x, because the observation point is fixed while the boundary location varies. For continuous boundary temperatures g, on a bounded domain whose boundary points are regular for the Dirichlet problem, the harmonic solution at x is the average of g against that probability measure.

In ordinary speech: to find the temperature at x, weight each boundary temperature by the chance that a Brownian particle launched from x first reaches that part of the boundary. What looks like an elliptic equation with infinitely many boundary values becomes an expectation.

Why should random motion know anything about the Laplacian? Brownian motion has infinitesimal generator one half of the Laplacian. If u is harmonic, then applying the generator to u gives zero. Along Brownian paths, the value of u behaves as a martingale until the path is stopped. Under the usual boundedness and stopping assumptions, the expected value at the stopping point equals the starting value. Thus u of x equals the expected boundary value at exit.

Conversely, the expectation of a continuous boundary payoff defines a harmonic function inside the domain. At a sufficiently regular boundary point it approaches the prescribed payoff as the starting point moves there. For a rough boundary, there can be exceptional points where this limiting statement fails. The probabilistic definition still makes sense even though solving the continuous Dirichlet problem in the classical boundary sense needs care.

## Read the disk's exit probabilities from the Poisson kernel

In the unit disk, put the observation point at distance r from the center on the positive horizontal axis. Label a boundary point by its angle t from that axis. The Poisson kernel says that its relative weight is one minus r squared divided by one minus twice r times cosine t, plus r squared. Integrate against boundary angle divided by two pi to obtain a probability.

At the center, r is zero, so the weight is one. Exit angles are uniformly distributed. An arc occupying one tenth of the circle has harmonic measure one tenth from the center. Away from the center, the weights are not uniform. Nearby boundary locations become more likely exit locations than distant ones.

Let's make that precise. Take the boundary arc consisting of angles from negative a to positive a, centered on the point one on the real axis. Here a is between zero and pi. The harmonic measure of that arc, as seen from the point at radius r on the positive axis, is the integral of the Poisson kernel over that angular interval.

The integral has a compact exact answer. It is two over pi times the arctangent of the product of two factors: one plus r divided by one minus r, and the tangent of half the arc angle a. At the center this becomes a divided by pi, exactly the fraction of the circumference covered by the arc.

For a quarter-circle arc centered on the nearest boundary point, a equals pi over four. The center sees probability one quarter. Now move to radius one half toward that arc. The multiplier one plus r over one minus r becomes three, so the probability is two over pi times the arctangent of three times the tangent of pi over eight. That is about fifty-seven percent. Being closer to the selected wall has made that arc far more influential.

As the starting point approaches the middle of the arc from the interior, the probability approaches one. The particle is increasingly likely to exit near that nearby boundary point. If instead the starting point approaches a smooth boundary point strictly outside the arc, its probability of exiting within the selected arc tends to zero.

An indicator function for an arc is discontinuous at its endpoints. The formula still defines a harmonic function in the open disk, but we should not claim continuous boundary agreement at those two jump points. On a smooth disk the value approached from certain directions at an endpoint can differ from either side's assigned indicator value; the boundary interpretation is almost-everywhere or through suitable limits.

## The Green function and the Poisson kernel are related

We have met two ways to reconstruct an elliptic solution. A Green function gives the interior response to distributed forcing. A Poisson kernel gives the interior response to boundary values. For the Dirichlet Laplacian on a smooth bounded domain, they are not independent constructions.

Fix the observation point x. Let the Green function vanish at the boundary and solve the negative-Laplacian equation for a unit point source at x. Now differentiate that Green function at a boundary location in the outward normal direction. Take its negative. This normal derivative, where the required smoothness holds, is the Poisson kernel at that boundary point.

The sign is instructive. A positive Dirichlet Green function falls to zero at the boundary, so its outward derivative is generally nonpositive. Hopf's boundary point lemma often tells us the derivative is strictly negative. Negating it gives a positive boundary weight, exactly what a probability density requires.

In one dimension, the connection becomes almost embarrassingly concrete. The interval Dirichlet Green function is the smaller of x and y times one minus the larger. Its outward-normal derivative, negated at the left endpoint, is one minus x. At the right endpoint, it is x. These are the very exit probabilities we derived from the equation h double prime equals zero.

This is why boundary point principles and harmonic measure sit naturally next to Green functions. One estimates how a positive function leaves zero at the boundary; the other uses those boundary fluxes as weights in a representation formula. The connection is exact under appropriate hypotheses, not merely visual.

## A trap: area on the boundary is not always the probability

In the unit disk we described harmonic measure with a density against ordinary angular length. A smooth domain often has a Poisson kernel against surface area as well, though its formula is rarely as simple. But this behavior is not guaranteed for every domain.

A boundary may be rough enough that harmonic measure concentrates on sets whose ordinary surface-area behavior is complicated. In some settings a density with respect to surface measure does not exist. The harmonic measure remains a probability measure; what fails is the assumption that it must be represented by a familiar geometric density.

Even in a perfectly smooth disk, uniform arc length is the correct exit distribution only when starting at the center. At other points the Poisson weight is essential. Two boundary arcs with equal length may have very different harmonic measures from a fixed off-center starting point.

This distinction matters in inverse problems and boundary control. A large piece of the boundary can have surprisingly little influence at a selected interior point, while a smaller but nearby piece can dominate. What matters to that point is harmonic measure, not a simple percentage of perimeter.

## What happens when the equation changes?

Standard Brownian motion corresponds to the Laplace operator. For a diffusion with anisotropic or spatially varying behavior, the generator changes. Under appropriate conditions, the exit distribution of that new diffusion represents a corresponding elliptic equation. The weights need not be those of standard Brownian motion.

Adding a source term also changes the representation. A Poisson equation has a contribution from forcing accumulated before exit, in addition to the expected boundary payoff. In our sign convention, solving negative Laplacian of u equals f involves an interior Green-function term. The pure harmonic measure average appears when the interior source is zero.

Harmonic measure gives the correct language for a boundary influence question. Green functions answer a source response question. Hopf's lemma describes strict boundary growth. Harnack's inequality compares positive values inside. These are related methods but not interchangeable conclusions.

The most important change of viewpoint is that we no longer need an explicit formula to ask a precise question about the boundary. At an observation point, harmonic measure itself is the mathematical object that records how the boundary is seen. On the disk we can compute it exactly. On a complicated domain we may approximate it numerically or probabilistically. The boundary-value problem gives it meaning either way.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not narrated)

### Harmonic measure as a linear functional and as an exit law

For a bounded domain \(D\subset\mathbb R^n\) regular for the continuous Dirichlet problem, the map \(g\mapsto u_g(x)\) on \(C(\partial D)\) is positive and sends the constant function 1 to 1. The Riesz representation theorem gives a probability measure \(\omega_D^x\) on \(\partial D\) such that
\[
u_g(x)=\int_{\partial D}g(y)\,d\omega_D^x(y).
\]
For standard Brownian motion \(B_t\) started at \(x\), with exit time \(\tau_D=\inf\{t\ge0:B_t\notin D\}\),
\[
\omega_D^x(E)=\mathbb P^x(B_{\tau_D}\in E),\quad
u_g(x)=\mathbb E^x[g(B_{\tau_D})].
\]
The usual Brownian generator is \(\tfrac12\Delta\). For \(u\in C^2(D)\cap C(\bar D)\) harmonic and bounded, Itô's formula and bounded stopping justify the representation. In rough domains, the expectation is harmonic in \(D\), but boundary continuity may fail at irregular boundary points.

### Disk Poisson kernel and a symmetric arc

For \(z=re^{i\theta}\in\mathbb D\) and \(e^{it}\in\partial\mathbb D\),
\[
P_r(\theta-t)=\frac{1-r^2}{1-2r\cos(\theta-t)+r^2},\qquad
 d\omega_{\mathbb D}^z(e^{it})=P_r(\theta-t)\frac{dt}{2\pi}.
\]
For \(z=r\in[0,1)\) and \(A_a=\{e^{it}:-a<t<a\}\), \(0<a<\pi\), substitute \(s=\tan(t/2)\):
\[
\begin{aligned}
\omega_{\mathbb D}^r(A_a)
&=\frac1{2\pi}\int_{-a}^a\frac{1-r^2}{(1-r)^2+4r\sin^2(t/2)}\,dt\\
&=\frac2\pi\arctan\!\left(\frac{1+r}{1-r}\tan\frac a2\right).
\end{aligned}
\]
For \(a=\pi/4\), \(r=1/2\), this is \(\frac2\pi\arctan(3(\sqrt2-1))\approx0.5686\); at \(r=0\) it is \(1/4\).

### Poisson kernel from the Dirichlet Green function

With \(-\Delta_yG_D(x,y)=\delta_x(y)\), \(G_D(x,y)=0\) at \(y\in\partial D\), for sufficiently smooth \(D\), Green's identity gives
\[
 u(x)=\int_{\partial D}\left[-\frac{\partial G_D(x,y)}{\partial\nu_y}\right]g(y)\,dS(y),\quad \Delta u=0,\ u|_{\partial D}=g.
\]
The bracketed density is \(P_D(x,y)\). On \(D=(0,1)\),
\[
G(x,y)=\min(x,y)(1-\max(x,y)),\quad
 P_D(x,0)=1-x,\quad P_D(x,1)=x.
\]
Boundary surface measure in one dimension counts the two endpoint atoms.

### Exercises and worked answers

1. **Two endpoints.** If \(g(0)=8\), \(g(1)=20\), what is \(u(1/4)\)? **Answer:** \((3/4)8+(1/4)20=11\).
2. **Arc at center.** What is the harmonic measure of an arc of opening angle \(\pi/3\), seen from the disk center? **Answer:** \((\pi/3)/(2\pi)=1/6\).
3. **Why not uniform off center?** Examine \(P_r(0)\) and \(P_r(\pi)\). **Answer:** They are \((1+r)/(1-r)\) and \((1-r)/(1+r)\), respectively.
4. **Normal sign.** Compute \(-\partial_{\nu_y}G(x,y)\) at both interval endpoints. **Answer:** \(1-x\) at \(y=0\), \(x\) at \(y=1\).
5. **Forcing.** If \(-\Delta u=f\ne0\), why does the boundary average not suffice? **Answer:** Green's representation adds \(\int_DG_D(x,y)f(y)\,dy\).

### Sources and further reading

- [Gregory Lawler, *Harmonic Measure* lecture notes](https://www.math.uchicago.edu/~lawler/harmonic.pdf), Brownian exit laws and planar harmonic measure.
- [University of Washington, lecture on Brownian motion and the Dirichlet problem](https://homes.cs.washington.edu/~jrl/teaching/cse599Isp21/notes/lecture7.pdf), Poisson integral and stochastic representation on a disk.
- [MIT OpenCourseWare, *Introduction to PDE*, lecture notes](https://ocw.mit.edu/courses/18-152-introduction-to-partial-differential-equations-fall-2005/pages/lecture-notes/), harmonicity and the Dirichlet problem.
- [Wikipedia: Harmonic measure](https://en.wikipedia.org/wiki/Harmonic_measure), general definition and Brownian interpretation.
- Library connections: `multivariable-calculus:048000` (Green functions), `multivariable-calculus:050000` (Poisson kernel), and `multivariable-calculus:051000` (Hopf).
