# A Heat Solver Should Cool: Discrete Maximum Principles and Energy

<!-- BEGIN SPOKEN LECTURE -->

# A Heat Solver Should Cool

Place a single hot spot in the middle of a rod whose ends are held at zero temperature. In the real heat equation, the maximum temperature cannot climb above that initial hot spot without a heater or some other source. Heat spreads, extremes become less extreme, and the temperature profile gradually flattens. That is not merely an impression of what a graph should look like. It follows from the heat equation's maximum principle and its dissipation of energy.

A numerical scheme should respect as much of this behavior as its design allows. We are going to discover that an update can be algebraically consistent with the heat equation and still turn one positive hot spot into negative temperatures and an oscillation that grows. The problem is the time step, not the physical model. Then we will see how to make the numerical version of the maximum principle visible, how to measure dissipation through a discrete energy, and why implicit steps solve a different tradeoff.

We work on a rod between zero and one, with zero temperature at both ends. Put three unknown temperatures at positions one quarter, one half, and three quarters. The spatial spacing is one quarter. Let the thermal diffusivity be one. This is the same small grid used in our boundary calculations, but now both ends are held cold, so there is no boundary forcing.

## Why averaging is a stability proof

Recall the explicit Euler heat update. The new temperature at an interior grid point equals the old center temperature multiplied by one minus twice the diffusion ratio, plus each immediate neighbor multiplied by that ratio. The diffusion ratio is diffusivity times the time step divided by the square of the spatial spacing. Call it r.

If r is between zero and one half, all three coefficients are nonnegative and their sum is one. This makes the next value a weighted average of the old center and its two neighbors. A weighted average cannot exceed the largest input and cannot fall below the smallest. Include the fixed endpoint values in that statement, and the maximum temperature cannot increase while the minimum cannot decrease. For our source-free, zero-endpoint problem, the scheme also preserves nonnegativity of initially nonnegative data.

This simple observation is a proof of stability in the maximum norm. We did not need to diagonalize a matrix. If a perturbation has maximum absolute size epsilon at some time, a single averaging step cannot make that maximum larger. Apply the reasoning repeatedly, and the error introduced by an initial perturbation remains bounded by epsilon, provided the boundary data of the two compared solutions agree.

Try the calculation. Initially the middle temperature is one and its neighbors are zero. Choose r equal to one quarter. After one step, the temperatures are one quarter, one half, one quarter. After another, they are one quarter, three eighths, one quarter. The peak fell from one to one half to three eighths; the profile spread. Every new entry lies between the previous minimum and maximum.

Now choose r equal to three quarters, keeping exactly the same grid and initial values. The first step produces three quarters, negative one half, three quarters. A rod that began at nonnegative temperature has acquired a negative center. The center coefficient, one minus twice r, is now negative. It is no longer a weighted average. For sufficiently fine grids, such large diffusion ratios also amplify high-frequency errors from one time step to the next, causing growing oscillations.

The ordinary heat equation never makes that move. The grid rule did. This distinction is central to numerical modeling: a solution violating a physical bound may be signaling a numerical instability rather than a surprising physical phenomenon.

## Energy without calculus tricks

There is another way to see the dissipative nature of the heat equation. If we square the temperature and integrate along a rod with zero-temperature ends, the total squared temperature decreases. This quantity is not the total amount of heat. It is a mathematical energy measuring the size of temperature variations. Different quantities answer different questions: total heat can flow out through the cold boundaries, while squared temperature measures the overall amplitude of the evolving field.

The continuum calculation multiplies the heat equation by temperature and integrates. Integration by parts moves one spatial derivative onto temperature itself, and the endpoint contribution vanishes because temperature is zero at both ends. The result says: the rate of change of half the integrated temperature squared equals negative diffusivity times the integrated squared temperature gradient.

We can perform the same reasoning on the grid. Multiply each interior temperature rate by that temperature, add the terms with spacing as a weight, and rearrange the neighbor differences. Every interior edge appears twice with opposite cross terms. What remains is minus the sum of squared temperature differences between neighbors, divided by the grid spacing and multiplied by diffusivity. Those squares are never negative. The semidiscrete heat system therefore dissipates this discrete energy exactly.

Notice what this proves and what it does not prove. It tells us that the system obtained after discretizing space but before discretizing time is dissipative. A numerical time integrator may fail to preserve that property. The explicit scheme with too large a step does exactly that. We must analyze the *combined* spatial and temporal discretization.

For our three-temperature example, let the discrete energy measure be the spacing times the sum of the three squared temperatures. Initially it is one quarter. After the stable first step it is three thirty-seconds; after the second step it decreases again. The numbers give a separate check beyond merely looking for negative values. A scheme could remain nonnegative and still have poor accuracy; satisfying an energy inequality is a useful necessary design signal, not an accuracy certificate.

## What backward Euler changes

A straightforward response to the explicit stability restriction is to evaluate the spatial second differences at the *new* time rather than the old one. This is backward Euler. The future temperatures now depend on one another, so each time step requires solving a tridiagonal linear system. We exchange a simple explicit update for an implicit solve.

Why does this help? A discrete heat mode decays exponentially in the semidiscrete system. Its associated eigenvalue is negative. Explicit Euler multiplies that mode by one plus the time step times the eigenvalue. If the step is too long, the multiplier crosses below negative one, and the mode grows while flipping sign. Backward Euler multiplies by one divided by one minus the time step times the eigenvalue. For a negative eigenvalue, this factor is positive and strictly smaller than one for every positive step length.

The effect can be seen without calculating any eigenvectors. Multiply the backward Euler equation by the new temperature vector. Use the discrete integration-by-parts identity, and a simple algebraic identity for the difference of two squared norms. The result says the energy at the new time, plus some nonnegative terms, is bounded by the old energy. No explicit diffusion ratio appears in the inequality.

For the same three interior grid points, start from zero, one, zero and choose a time step whose diffusion ratio is one. Explicit Euler would be unstable. Backward Euler instead gives interior values one seventh, three sevenths, one seventh. Every value is positive and the largest is below the initial maximum. The central temperature is lower, as expected after heat has had time to spread toward cold endpoints.

Implicit does not mean magically exact. A very large backward Euler step may erase a physical transient too aggressively. The solution might remain stable and nonnegative while looking overly smoothed. If the question concerns the timing of a rapid heating event, the method may require a smaller step for accuracy even when stability imposes no such restriction.

## Crank–Nicolson and the cost of better time accuracy

There is a middle choice. Average the spatial derivative from the old and new times. That is the Crank–Nicolson or trapezoidal method. For sufficiently smooth evolution it is second-order in time, while Euler methods are first-order. Its energy analysis is attractive: multiply the update by the average of old and new temperatures, and the grid integration-by-parts formula again gives a nonpositive energy change.

But a subtle point matters. Energy stability and pointwise positivity are not the same. For a very large step, Crank–Nicolson can give a negative amplification factor for a high-frequency heat mode. The discrete energy may decrease while that mode changes sign. On some initial data, a negative temperature can appear even though the starting values were nonnegative. The weighted-average argument that guaranteed the explicit method's maximum principle for small steps is not automatically available here.

We therefore have a family of questions rather than a single verdict of 'stable'. Does the method keep a perturbation bounded? Does it preserve positivity? Does it dissipate a discrete energy? Does it approximate the true decay rate? Does it preserve total heat under insulating boundaries? And what does it cost to advance one step? Forward Euler, backward Euler, and Crank–Nicolson answer these questions differently.

## A route from a physical statement to a numerical certificate

The strongest lesson is the style of reasoning. Start with a physical or mathematical identity of the differential equation. Write down its precise boundary assumptions. Choose a grid and boundary treatment. Derive a discrete version of the identity. Then see whether the *time-stepping rule* preserves it under a stated restriction.

The heat equation has a maximum principle and a dissipation law. A carefully designed numerical heat solver can inherit both, but not automatically, and not always under the same hypotheses. Knowing the exact role of r, the discrete Laplacian, and the boundary terms tells us where a solver's trustworthy behavior comes from. Next we will turn to waves, where energy is not supposed to disappear at all. The corresponding numerical problem has an equally sharp time-step restriction but a different physical demand: preserve oscillation rather than erase it.

<!-- END SPOKEN LECTURE -->

## Mathematical companion: stability and dissipation

Use zero Dirichlet values \(U_0=U_N=0\), the difference \(D_{xx}\), and \(\|U\|_h^2=h\sum_{i=1}^{N-1}U_i^2\). Summation by parts gives
\[
 (U,D_{xx}U)_h=-\frac1h\sum_{i=0}^{N-1}(U_{i+1}-U_i)^2=-\|D_+U\|_h^2.
\]
For the semidiscrete heat equation \(\dot U=\kappa D_{xx}U\),
\[
 \frac{d}{dt}\frac12\|U\|_h^2=-\kappa\|D_+U\|_h^2\le0.
\]
Here \(\|D_+U\|_h^2=h\sum_{i=0}^{N-1}[(U_{i+1}-U_i)/h]^2\).

Forward Euler has the pointwise update
\[
 U_i^{n+1}=rU_{i-1}^n+(1-2r)U_i^n+rU_{i+1}^n,\qquad r=\kappa\Delta t/h^2.
\]
For \(0\le r\le1/2\), all coefficients are nonnegative, and their sum is one, so \(\|U^{n+1}\|_\infty\le\max(\|U^n\|_\infty,\|g\|_\infty)\), with fixed boundary values included. For homogeneous boundaries the propagator is also a contraction in the discrete \(L^2\) norm. On a uniform Dirichlet mesh with \(N\) subintervals, the \(m\)-th discrete Laplacian eigenvalue is
\[
 \lambda_m=-\frac{4}{h^2}\sin^2\left(\frac{m\pi}{2N}\right),\quad m=1,\ldots,N-1.
\]
The explicit amplification is \(1+\kappa\Delta t\lambda_m\). The uniform sufficient bound \(r\le1/2\) is also sharp in the limit of large \(N\). For a fixed small Dirichlet grid the exact spectral limit is slightly larger.

For \(N=4\), \(U^0=(0,1,0)\):
\[
\begin{array}{c|cc}
 r &U^1 &U^2\\\hline
 1/4 &(1/4,1/2,1/4)&(1/4,3/8,1/4)\\
 3/4 &(3/4,-1/2,3/4)&\text{positivity already violated}
\end{array}
\]
The stable first-step discrete squared norm is \(h(1/16+1/4+1/16)=3/32\), compared with initial \(1/4\).

For backward Euler, \((U^{n+1}-U^n)/\Delta t=\kappa D_{xx}U^{n+1}\). Taking the \(h\)-inner product with \(U^{n+1}\),
\[
 \frac{\|U^{n+1}\|_h^2-\|U^n\|_h^2+\|U^{n+1}-U^n\|_h^2}{2\Delta t}
 =-\kappa\|D_+U^{n+1}\|_h^2.
\]
For \(N=4,r=1,U^n=(0,1,0)\), the tridiagonal system has diagonal 3, off-diagonal \(-1\), and the exact solution is \(U^{n+1}=(1/7,3/7,1/7)\). Its matrix is an \(M\)-matrix, giving nonnegativity and an appropriate maximum principle for \(r>0\) with this standard Dirichlet grid.

For Crank–Nicolson, set \(\bar U=(U^{n+1}+U^n)/2\). Then
\[
 \frac{U^{n+1}-U^n}{\Delta t}=\kappa D_{xx}\bar U,\qquad
 \frac{\|U^{n+1}\|_h^2-\|U^n\|_h^2}{2\Delta t}
 =-\kappa\|D_+\bar U\|_h^2.
\]
For an eigenvalue \(\lambda<0\), the amplification factor is \(G=(1+\kappa\Delta t\lambda/2)/(1-\kappa\Delta t\lambda/2)\), whose absolute value is at most one, but it becomes negative when \(\kappa\Delta t|\lambda|>2\). Therefore \(L^2\)-stability does not imply positivity.

### Exercises with worked answers

1. A rod has \(h=0.05\) and \(\kappa=0.25\). What is the uniform explicit Euler heat restriction? **Answer:** \(\Delta t\le h^2/(2\kappa)=0.005\).
2. For \(U^n=(0,1,0)\) and \(r=1/4\), compute the first two updates. **Answer:** \(U^{n+1}=(1/4,1/2,1/4)\), and then \((1/4,3/8,1/4)\).
3. Why does a nonnegative weighted average prove more than spectral boundedness? **Answer:** it gives a pointwise maximum principle and preserves positivity, while a bounded negative amplification factor may create sign changes.
4. What is the discrete energy dissipation term? **Answer:** \(\kappa h\sum_i[(U_{i+1}-U_i)/h]^2\), the sum of squared neighbor gradients times diffusivity.
5. If backward Euler is stable with \(r=10\), is it necessarily accurate? **Answer:** no; it strongly damps modes and may distort their transient time scales.

### Sources and further reading

- [Langtangen and Linge, *Finite Difference Computing with PDEs*, Diffusion Equations](https://link.springer.com/book/10.1007/978-3-319-55456-3).
- [MIT OpenCourseWare 18.086: finite differences, accuracy, stability, convergence, and heat equation](https://ocw.mit.edu/courses/18-086-mathematical-methods-for-engineers-ii-spring-2006/resources/lecture-videos/).
- [Wikipedia: Crank–Nicolson method](https://en.wikipedia.org/wiki/Crank%E2%80%93Nicolson_method).
