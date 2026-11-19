# A Wave Grid That Keeps Its Energy: Leapfrog and the CFL Condition

<!-- BEGIN SPOKEN LECTURE -->

# A Wave Grid That Keeps Its Energy

A string stretched between two fixed supports behaves differently from a hot metal rod. If we pluck the string, it moves back and forth. Its shape changes, its velocity changes, but in an ideal model with no friction the total mechanical energy does not disappear. A numerical scheme that makes the string motion fade to zero has added dissipation that the equation did not contain. A scheme that makes the motion grow without bound has invented energy. We want a grid calculation that respects the oscillatory character of the wave equation.

Let the string occupy positions zero through one. Both endpoints are fixed at zero displacement. At any interior point, the acceleration is wave speed squared times the spatial second derivative of displacement. To model that equation, we place equally spaced grid points along the string. Each interior point has a displacement at a succession of times. The spatial curvature is approximated by the usual difference of its right neighbor, twice its center, and its left neighbor, divided by the spacing squared.

Time is different from the heat problem. The wave equation contains a second time derivative, not a first. So our numerical update naturally uses the displacement at three time levels: the previous, the present, and the next. Replace the time acceleration by next displacement minus twice present displacement plus previous displacement, divided by the time step squared. Equate that to wave speed squared times the present spatial second difference. Then solve for the next displacement.

The formula says that the new position is twice the present position minus the previous position, plus a correction from the curvature of the string. If a point is above its neighbors, its curvature is negative and the correction accelerates it downward. If it is below, the correction acts upward. This is a discrete version of how tension provides a restoring force.

## The time-step ratio that governs the wave

There is a natural dimensionless number in this update: the wave speed multiplied by the time step, divided by the grid spacing. Call it the wave Courant number. If it is one half, a wave travels half a grid cell during one time step. If it is one, it travels one cell. If it exceeds one, a physical wave can travel farther than one grid cell in the time that our three-point spatial stencil reaches only its immediate neighbors.

That observation suggests a time-step restriction. For this standard centered scheme on a uniform one-dimensional grid, a wave Courant number no larger than one gives the usual stability condition. The condition has a more precise derivation in terms of Fourier modes and numerical energy, which we will carry out shortly. The physical picture is helpful, but a stencil's domain of dependence alone is not a complete stability proof for every numerical method.

Let's compute a few values on a tiny string. Divide the unit interval into four subintervals, leaving three interior displacement values. Let the wave speed be one and choose a time step of one eighth. Then the Courant number is one half. Initially the interior displacements are zero, one, zero, and the initial velocity is zero everywhere. The endpoints remain fixed.

There is a small detail before we can use the three-level recurrence: at time zero, we do not yet have a preceding time level. A common mistake is to set that nonexistent level equal to the initial displacement and use the recurrence. That would correspond to the wrong initial velocity. Instead, use a second-order Taylor start. New displacement equals initial displacement plus time step times initial velocity plus half time step squared times initial acceleration. We can compute initial acceleration from the same spatial second difference.

The first interior displacement vector becomes one eighth, three quarters, one eighth. The center has begun to fall, and its neighbors have begun to rise. Now apply the three-level recurrence once more. The vector at the second time level is three eighths, three sixteenths, three eighths. The middle is still moving downward while the neighbors move upward. These numbers come from the same rule that can advance a string through thousands of steps, but each piece has a physical interpretation.

## A spring system is hiding inside the grid

After discretizing space, the wave equation becomes a coupled system of second-order ordinary differential equations. Every interior point is a mass connected by springs to its neighbors. The spatial difference matrix is symmetric, with negative eigenvalues when the endpoints are fixed. The string's displacement can be decomposed into discrete sine modes. Each mode satisfies an oscillator equation whose frequency depends on the grid spacing and the mode number.

The slowest mode bends gently across the whole string. The fastest modes alternate rapidly from one grid point to the next. Their frequencies can be much higher than the fundamental. If we choose a time step based only on the slow visible motion, a fast grid mode may become numerically unstable. It does not matter whether that mode starts with a large amplitude. Roundoff, boundary approximations, or the initial data can excite it.

For a discrete sine mode, insert a time dependence that oscillates with some numerical angle per step. The centered recurrence gives a precise relation: the sine of half that numerical angle equals the Courant number times the sine of half the spatial mode angle, up to the choice of sign and frequency branch. A real numerical oscillation angle exists for every grid mode when the Courant number is at most one. If that ratio is too large, the highest modes require an impossible real angle and instead have exponentially growing components.

This also shows numerical *dispersion*. Even when the scheme is stable, its numerical mode frequencies may differ from the actual frequencies of the continuous string. A waveform built from several modes can therefore change shape as its harmonics drift out of phase. A stable wave code can have the wrong wave speed at the shortest resolved wavelengths. Stability is not the same as accuracy.

## A discrete energy that does not change

The continuous wave equation has two kinds of energy. Kinetic energy depends on the square of velocity. Elastic energy depends on the square of the string's spatial slope. With fixed endpoints and no external forcing, their sum stays constant. As the string moves, energy shifts between kinetic and elastic forms, but the total remains the same.

We can derive a counterpart on the grid. Define the velocity over a time interval by next displacement minus present displacement divided by the time step. Define the spatial slope over an edge by the difference of displacements at its endpoints divided by grid spacing. Because the numerical update uses three time levels, the conserved quantity naturally lives between two adjacent time levels rather than at a single time.

Take the wave update and multiply it by next displacement minus previous displacement. Add over interior grid points, with the spacing as weight. On the time side, the cross terms collapse into the difference of two squares of interval velocities. On the spatial side, discrete integration by parts turns curvature into a product of neighboring spatial slopes at successive times. The fixed endpoints make the boundary contribution vanish.

The resulting energy consists of half the squared interval velocity, plus wave speed squared times half the product of the spatial slopes at the two neighboring times. Written that way, the potential term is not obviously positive, because it is a product of values from different times. But we can rewrite it as the square of their average minus a correction involving their difference. The difference of successive slopes is time step times the spatial difference of interval velocity.

Now use a basic inequality: on this grid, the squared norm of a first spatial difference is at most four divided by the spacing squared times the squared norm of the underlying grid vector. The correction is therefore controlled by the wave Courant number squared. When that number is less than one, the conserved energy is nonnegative and controls the velocity and an averaged spatial slope. The familiar stability condition has appeared again, this time from an energy argument.

This is a stronger explanation than 'the simulation looks fine'. It says which discrete quantity is conserved, why the condition on the time step matters, and why the fixed endpoints are part of the proof.

## Fixed, free, and absorbing boundaries are different models

For a fixed string, endpoint displacement is zero at all times. A free endpoint has zero spatial slope rather than zero displacement. That change alters the discrete modes and the boundary terms in the energy calculation. If we try to model a wave traveling out of a finite computational interval, we may prefer an absorbing boundary that lets energy leave rather than reflect. Then conservation of energy inside the interval is not the right requirement; an appropriate outward energy flux is.

A numerical scheme that correctly conserves energy for a fixed string can give the wrong physical picture if we apply the same endpoint rule to a string that should be free or to an open acoustic domain. The differential equation in the interior may be unchanged while the boundary physics is different.

Likewise, energy conservation does not mean the numerical trajectory is perfect. A phase error can accumulate over many oscillations even when total discrete energy remains exactly constant. Time-step refinement is still needed to study accuracy. The energy identity tells us that the method is not quietly generating or destroying the quantity it was designed to track.

We now have two related but distinct stories about grid stability. Heat diffusion should dissipate squared temperature and obey a maximum principle under the right scheme. Ideal waves should exchange kinetic and elastic energy without net loss. In both cases, the key is to start from the physical equation, derive a discrete identity, and determine the step-size conditions under which that identity gives control. The remaining question is whether that control, together with a good approximation of derivatives, is enough to guarantee that computed solutions converge to the actual PDE solution as we refine the grid.

<!-- END SPOKEN LECTURE -->

## Mathematical companion: leapfrog, dispersion, and conserved energy

Consider \(u_{tt}=c^2u_{xx}\) on \(0<x<L\), with \(u(0,t)=u(L,t)=0\). Let \(h=L/N\), \(t_n=n\Delta t\), and \(r=c\Delta t/h\). The centered wave scheme is
\[
 U_i^{n+1}=2U_i^n-U_i^{n-1}+r^2(U_{i-1}^n-2U_i^n+U_{i+1}^n),\qquad 1\le i<N.
\]
Use a second-order starter for velocity data \(v(x,0)=v_0(x)\):
\[
 U_i^1=U_i^0+\Delta t\,V_i^0+\frac{c^2\Delta t^2}{2}(D_{xx}U^0)_i.
\]
For \(N=4,h=1/4,c=1,\Delta t=1/8,r=1/2,\;U^0=(0,1,0),V^0=0\), this gives
\[
 U^1=(1/8,3/4,1/8),\qquad U^2=(3/8,3/16,3/8).
\]

For a Dirichlet sine mode \(U_j^n=\sin(j\theta_m)e^{in\Omega_m}\), \(\theta_m=m\pi/N\), substitution gives
\[
 \cos\Omega_m=1-2r^2\sin^2(\theta_m/2),\quad
 \sin^2(\Omega_m/2)=r^2\sin^2(\theta_m/2).
\]
A uniform sufficient stability bound is \(r\le1\). When \(r>1\), sufficiently fine meshes have modes whose recurrence roots are real and reciprocal with one larger than one in magnitude. Stable modes still exhibit dispersion because in general \(\Omega_m/\Delta t\ne cm\pi/L\).

Let \(\|W\|_h^2=h\sum_{i=1}^{N-1}W_i^2\), and for grid edges \(\|D_+U\|_h^2=h\sum_{i=0}^{N-1}((U_{i+1}-U_i)/h)^2\). Define \(V^{n+1/2}=(U^{n+1}-U^n)/\Delta t\). The discrete energy
\[
 E^{n+1/2}=\frac12\|V^{n+1/2}\|_h^2+
 \frac{c^2}{2}(D_+U^{n+1},D_+U^n)_h
\]
is invariant in \(n\). Multiply the scheme by \((U^{n+1}-U^{n-1})/(2\Delta t)\), sum over the grid, and use discrete integration by parts to prove \(E^{n+1/2}=E^{n-1/2}\).

With \(G=(D_+U^{n+1}+D_+U^n)/2\), the polarization identity gives
\[
 E^{n+1/2}=\frac12\|V\|_h^2+\frac{c^2}{2}\|G\|_h^2
 -\frac{c^2\Delta t^2}{8}\|D_+V\|_h^2.
\]
The elementary discrete inverse estimate \(\|D_+V\|_h\le (2/h)\|V\|_h\) therefore yields
\[
 E^{n+1/2}\ge\frac{1-r^2}{2}\|V\|_h^2+\frac{c^2}{2}\|G\|_h^2\qquad\text{for }r\le1.
\]
For \(r<1\), this is positive definite in the indicated variables and provides a stability estimate. The endpoint \(r=1\) is stable for the standard scheme but the lower bound degenerates, so proofs demanding uniform strict coercivity often assume \(r\le1-\epsilon\). Smooth-data second-order convergence also requires a consistent second-order initial step.

### Exercises with worked answers

1. If \(h=0.02\), \(c=4\), what is the standard one-dimensional centered-wave CFL restriction? **Answer:** \(\Delta t\le h/c=0.005\).
2. Given \(U^0=(0,1,0)\), \(V^0=0\), and \(r=1/2\) on three interior nodes, compute the first two numerical levels. **Answer:** \(U^1=(1/8,3/4,1/8)\), \(U^2=(3/8,3/16,3/8)\).
3. Why can \(U^{-1}=U^0\) be a bad initialization when the physical initial velocity is zero? **Answer:** it does not include the half-step acceleration correction and generally reduces the temporal accuracy of the initial condition.
4. A wave with fixed ends has continuous energy \(\int (u_t^2+c^2u_x^2)/2\,dx\). What boundary assumption removes the flux term after integration by parts? **Answer:** \(u=0\) at both ends for all times, hence \(u_t=0\) there.
5. Is the leapfrog energy the same as evaluating the continuum energy using \(U^n\) and a centered velocity at time \(n\)? **Answer:** not exactly; the preserved energy is staggered across adjacent time levels and includes the product of adjacent-time spatial slopes.

### Sources and further reading

- [Langtangen and Linge, *Finite Difference Computing with PDEs*, Wave Equations](https://link.springer.com/book/10.1007/978-3-319-55456-3).
- [MIT OpenCourseWare 18.086, lectures on the second-order wave equation and leapfrog](https://ocw.mit.edu/courses/18-086-mathematical-methods-for-engineers-ii-spring-2006/resources/lecture-videos/).
- [Interactive Educational Modules in Scientific Computing, wave-equation CFL condition](https://heath.cs.illinois.edu/iem/pde/wavecfl/).
