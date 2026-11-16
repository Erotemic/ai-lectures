# 010000 — Transport and Diffusion: Two Ways a Field Evolves

**Track:** Differential Equations and Dynamical Systems. **Background:** derivatives in space and time, conservation laws, and Fourier modes. **Central question:** why does advection preserve shapes while diffusion smooths them out?

<!-- BEGIN SPOKEN LECTURE -->

# Transport and Diffusion: Two Ways a Field Evolves

An ordinary differential equation describes the evolution of finitely many quantities, perhaps the position of a mass or the amount of a chemical species. But temperature and concentration are fields: their values depend on position as well as time. To describe how an entire field evolves, derivatives in both space and time become part of the equation. These are partial differential equations.

Two basic mechanisms appear almost everywhere: transport and diffusion. Transport moves a pattern from one place to another. Diffusion spreads a pattern, smoothing sharp variations. Their equations look similar at first glance, but the behavior they predict is fundamentally different.

## Transport carries profiles

Consider a scalar field u depending on position x and time t. Suppose the field is carried along the line at constant speed c without changing shape. If the initial profile is a bump, after time t the bump has moved a distance c times t.

The exact expression says: to find u at x and t, look at the initial profile at x minus c times t. Differentiate this expression. The time derivative is negative c times the derivative of the initial profile, and the spatial derivative is that same profile derivative. Consequently u satisfies an equation that says the time derivative plus c times the spatial derivative equals zero.

This is the linear transport equation. Its solutions are constant along characteristic lines that move at speed c. A disturbance has a definite propagation direction. On the whole line, an initial bump simply translates. It does not become broader or shorter by the transport law alone.

If we work on a bounded interval, boundary conditions matter. For positive c, information flows into the interval through the left boundary, so prescribing data there is natural. Imposing arbitrary conditions independently at both ends would generally overdetermine the first-order transport problem. The direction of information flow is part of the mathematics.

## Diffusion follows gradients

Now imagine a concentration field where material moves from regions of high concentration toward regions of low concentration. In a simple homogeneous model, the flux is proportional to the negative spatial gradient of the concentration. This is Fick's law. A positive gradient sends flux toward the negative x direction, and a negative gradient sends flux toward positive x.

Conservation says the rate of change in a short interval equals the net flux entering it. In differential form, the time derivative of concentration is minus the spatial derivative of flux. Substitute the gradient law, assume the diffusivity D is constant, and obtain the heat equation: the time derivative equals D times the second spatial derivative.

The second derivative measures local curvature. At a sharp local maximum, curvature is negative, and diffusion tends to lower the peak. At a local minimum, curvature is positive, and diffusion tends to raise the trough. Over time, a rough initial profile becomes smoother.

## Understand smoothing one Fourier mode at a time

A sine wave is a useful test. Suppose u is initially a sine wave of spatial frequency k, and we look for a solution with the same spatial shape but a changing amplitude. Taking two spatial derivatives of that sine wave produces negative k squared times the original sine wave. The heat equation therefore tells us the amplitude decays exponentially at rate D times k squared.

Higher frequencies have larger k squared, so their amplitudes decay more rapidly. Very short-wavelength oscillations disappear faster than long-wavelength ones. This is the mathematical source of the familiar smoothing action of diffusion.

Compare transport. A sinusoidal wave under constant-speed transport has its phase shifted, but its amplitude remains the same. Transport changes position; diffusion changes the amplitudes of spatial modes. The distinction becomes central when both mechanisms appear together, as in advection-diffusion equations for heat or chemical species moving through a flow.

## Boundary conditions change the answer

On a finite rod of length L, suppose the ends are held at zero temperature relative to a reference level. Those are Dirichlet boundary conditions. Sine waves that vanish at both endpoints fit the boundary. Their spatial frequencies are integer multiples of pi divided by L. Each mode decays at a rate proportional to the square of its mode number.

If instead the ends are insulated, the heat flux at each boundary is zero. Since flux is minus D times the gradient, this means the spatial derivative vanishes at the endpoints. These are Neumann boundary conditions. In that setting the spatially constant mode does not decay: total heat is conserved because nothing escapes through either endpoint.

Both are heat equations, but they describe different physical systems. An initial condition alone does not generally determine the evolution on a bounded domain without appropriate boundary conditions. Which conditions are appropriate depends on what the surroundings do to the field.

## Energy provides a uniqueness argument

There is a useful proof that the heat equation is stable in a broad sense. Work on a finite interval with homogeneous zero-temperature boundary conditions. Multiply the heat equation by u and integrate over the interval. The time derivative of half the integral of u squared equals D times the integral of u times its second derivative.

Integrate by parts. The boundary term vanishes because u is zero at the ends. The remainder is minus D times the integral of the square of the spatial derivative. This quantity cannot be positive. Therefore the squared-size, or energy, of the temperature profile cannot increase.

Apply the same argument to the difference between any two solutions with the same initial and boundary data. That difference has zero initial energy and cannot gain energy, so it remains zero. This proves uniqueness within the regularity class in which the calculation is valid. Similar energy methods extend to weaker notions of solution with careful functional-analytic definitions.

Transport has a different conservation property. With periodic boundaries, constant-speed transport preserves the integral of u squared rather than dissipating it. Its profiles travel; diffusion loses spatial variation.

## A warning about numerical time steps

Diffusion is especially demanding for explicit numerical solvers. On a uniform spatial grid, approximate the second derivative by comparing each value with its two neighbors. If the time step is too large relative to the square of the spatial spacing, the explicit update can become unstable. In one dimension, a standard forward-Euler centered-difference scheme is stable in its usual maximum-principle sense when the dimensionless ratio D times the time step divided by the spacing squared does not exceed one half.

Refine the spatial grid by a factor of two, and the stable explicit time step becomes at most one quarter as large. This resembles stiffness: very fast decay of high spatial frequencies creates stringent numerical restrictions even when the visible temperature profile changes slowly. Implicit methods can relax the restriction, though their accuracy still needs attention.

## Two models, two kinds of information

For transport, a solution follows characteristics and preserves the profile along them. For diffusion, the solution smooths and dissipates variations; its mathematical model can spread an initially localized effect beyond any fixed distance at every positive time. That last feature is a property of the ideal heat equation, not a claim that physical thermal signals transmit infinitely fast at arbitrary microscopic scales. The diffusion equation is a continuum approximation with a domain of validity.

These equations establish two basic modes of PDE thinking. We can track information along paths, or we can understand how gradients and curvature reorganize a field. Their analysis combines differential equations, conservation laws, boundary conditions, and numerical stability. From here we can study waves, nonlinear conservation laws, weak solutions, and the geometries of higher-dimensional fields.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

**Transport.** On \(\mathbb R\), for sufficiently regular \(u_0\),
\[
u_t+c u_x=0,\quad u(x,0)=u_0(x)
\quad\Longrightarrow\quad u(x,t)=u_0(x-ct).
\]
Characteristics obey \(x(t)=x_0+ct\); \(u\) is constant along each characteristic.

**Diffusion.** Conservation \(u_t+F_x=0\) and Fick's law \(F=-D u_x\), for constant \(D>0\), give
\[
u_t=D u_{xx}.
\]
Fourier mode \(e^{ikx}\) decays as \(e^{-Dk^2t}e^{ikx}\). On \([0,L]\) with \(u(0,t)=u(L,t)=0\), separated solutions are \(\sin(n\pi x/L)e^{-D(n\pi/L)^2 t}\), \(n\ge1\).

**Energy identity** under homogeneous Dirichlet boundaries:
\[
\frac{d}{dt}\frac12\int_0^L u^2\,dx
=D\int_0^L u u_{xx}\,dx=-D\int_0^L (u_x)^2\,dx\le0.
\]
For two solutions with identical data, apply this to their difference to prove uniqueness for sufficiently regular solutions. For zero-flux Neumann conditions, \(\frac{d}{dt}\int_0^L u\,dx=D[u_x]_0^L=0\).

**Explicit finite differences.** For \(r=D\Delta t/(\Delta x)^2\),
\[
u_j^{n+1}=(1-2r)u_j^n+r u_{j-1}^n+r u_{j+1}^n.
\]
When \(0\le r\le1/2\), the update is a convex combination, ensuring a discrete maximum principle. This is the standard 1-D explicit diffusion restriction, not a universal CFL condition for every PDE discretization.

### Exercises with answers

1. Where is an initial peak \(u_0(x)=e^{-x^2}\) centered after time \(t\) under \(u_t+3u_x=0\)? **Answer:** at \(x=3t\).
2. Which diffusion Fourier mode decays faster: frequency one or frequency four? **Answer:** frequency four, with decay rate sixteen times as large.
3. With no-flux boundaries, is total mass conserved? **Yes:** the net boundary flux is zero.
4. If \(\Delta x\) halves, what happens to the forward-Euler diffusion stability limit on \(\Delta t\)? **Answer:** it decreases by a factor of four.

### Reading and source notes

- MIT OCW [Linear Partial Differential Equations](https://ocw.mit.edu/courses/18-303-linear-partial-differential-equations-fall-2006/pages/syllabus/), heat equation, separation of variables, Fourier series, and characteristics.
- University of Illinois [Stiff ODEs](https://heath.cs.illinois.edu/iem/ode/stiff/), numerical stability motivation.
