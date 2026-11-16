# 015000 — Spectral Methods for PDEs: Boundary Eigenproblems and Mode Evolution

**Track:** Differential Equations and Dynamical Systems. **Background:** heat and wave equations, linear algebra, Fourier series, boundary conditions. **Central question:** why can a PDE often be solved by following infinitely many uncoupled ordinary differential equations?

<!-- BEGIN SPOKEN LECTURE -->

# Spectral Methods for PDEs: Boundary Eigenproblems and Mode Evolution

Imagine a metal rod heated unevenly. Its ends are held at zero temperature, and its interior begins with a complicated temperature profile. Over time the temperature smooths out. Small alternating hot and cold regions vanish quickly, while broad patterns persist much longer.

The heat equation explains this behavior quantitatively. But there is a particularly revealing way to solve it: decompose the initial temperature into spatial modes, let each mode evolve according to its own simple ordinary differential equation, and then add them back together.

The method is called an eigenfunction expansion. It connects partial differential equations to spectral theory, and it also leads naturally to numerical spectral methods.

## The spatial operator comes first

Consider a rod of length L, with temperature zero at both ends. Let u of x and t be its temperature at position x and time t. The heat equation says its time derivative equals a positive diffusivity times its second spatial derivative.

Try a solution whose space and time dependence separate: a product of a spatial shape X of x and an amplitude T of t. Substitution into the equation leaves a spatial differential equation on one side and a temporal differential equation on the other. Since they depend on different variables, they must both equal the same constant, with the sign chosen conveniently.

The spatial problem becomes minus the second derivative of X equals lambda times X, with X zero at both endpoints. This is an eigenvalue problem for the negative second-derivative operator. Its eigenfunctions are sine waves that fit the interval exactly. The first mode makes half an oscillation along the rod; the second makes two half oscillations; the nth has n half oscillations. Their eigenvalues grow like n squared.

Each mode respects the endpoint conditions. That is essential. A Fourier basis chosen without regard for the boundary can produce the wrong physical problem, even if the algebra looks familiar.

## Time evolution of each mode

Once the spatial eigenfunction is fixed, the corresponding time amplitude satisfies a first-order ordinary differential equation. Its decay rate is the diffusivity multiplied by the spatial eigenvalue. So the nth sine mode decays exponentially, with an exponent proportional to negative n squared times time.

This is the precise reason fine-scale temperature variations fade rapidly. A tenth mode decays one hundred times as fast in its exponential rate as the first mode. Give the initial rod a broad single hump and a small ripple that oscillates ten times faster. After even a modest period, the ripple may have nearly vanished while the broad hump remains.

An arbitrary square-integrable initial profile can be expanded as a sine series. The coefficients are obtained by taking its inner products with the normalized spatial modes. The heat solution is the sum of those same modes multiplied by their respective decaying exponentials.

The meaning of convergence changes with the regularity of the initial data. For an arbitrary square-integrable profile, the series makes sense in an appropriate square-integrable sense at initial time. At positive time the heat equation smooths the profile, and the rapidly decaying coefficients make the series much better behaved.

## Energy provides an independent check

We can verify the direction of the dynamics without solving the series. Multiply the heat equation by u and integrate over the rod. Integration by parts, together with the zero endpoint conditions, says the time derivative of the squared temperature norm is negative two times the diffusivity times the squared spatial-gradient norm.

Thus the total squared temperature cannot increase. The Poincaré inequality gives an explicit lower bound on the gradient energy in terms of the temperature energy. Together they imply exponential decay at least at the rate associated with the lowest spatial eigenvalue.

The spectral solution and the energy estimate describe the same mechanism from different angles. One diagonalizes the operator; the other proves a monotonicity law directly. Comparing the two is a powerful guard against a misplaced sign or an incorrect boundary condition.

## The wave equation uses the same modes differently

Now replace the heat equation with the wave equation for a string fixed at both ends. Its second time derivative equals a positive wave-speed squared times its second spatial derivative.

The spatial sine eigenfunctions are unchanged because the boundary operator is unchanged. But each temporal coefficient now satisfies an oscillator equation, not a decay equation. Its frequency is the wave speed multiplied by the square root of the spatial eigenvalue.

If the initial displacement and velocity are expanded in sine modes, each mode oscillates with its own frequency. Their superposition gives the motion of the string. Smoothness does not suddenly improve the way it does for the heat equation; hyperbolic wave evolution transports and oscillates energy rather than diffusing it away.

This comparison teaches something important. The same spatial operator can participate in very different dynamics. Its eigenfunctions describe the geometry of allowed shapes. The PDE's time derivative determines whether those shapes decay, oscillate, or grow.

## From an infinite series to a numerical method

An exact expansion has infinitely many modes. A numerical spectral method retains only finitely many. Choose the first N eigenfunctions and approximate the solution as a linear combination with time-dependent coefficients. Substitute that approximation into the PDE and require the residual to be orthogonal to the retained subspace. This is a Galerkin method.

For a constant-coefficient linear problem with matching boundary eigenfunctions, the resulting system is diagonal and particularly simple. For variable coefficients or nonlinear terms, the modes interact, producing a coupled system of ordinary differential equations. The finite-dimensional problem can then be integrated by the time-stepping methods used in numerical analysis.

High regularity often leads to rapidly decaying spectral coefficients and therefore very accurate approximations with relatively few modes. However, discontinuities and sharp gradients can ruin that advantage. A truncated Fourier representation of a jump can exhibit oscillations near the discontinuity, including the Gibbs phenomenon. Spectral accuracy is conditional on the smoothness of what is being approximated and the suitability of the chosen basis.

## Beyond an interval

On more complicated regions, the analogous spatial problem involves the Laplacian with specified boundary conditions. Under suitable self-adjointness and compactness conditions, there is a discrete sequence of eigenvalues and an orthonormal family of eigenfunctions. These modes can expand square-integrable data and reduce linear PDE evolution to scalar equations.

On unbounded domains the spectrum may be continuous, and sums can be replaced or augmented by integrals. For non-self-adjoint operators, orthogonality can fail, eigenvectors may be incomplete, and spectral expansions require additional care.

So the spectral method is not the claim that every PDE is a Fourier series. It is a strategy: find a spatial operator adapted to the domain and its boundary conditions, understand its spectral structure, and use that structure to simplify time evolution. The resulting connection between PDEs and linear algebra is one of the most productive ideas in mathematical physics and scientific computation.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For \(0<x<L\), \(u_t=\kappa u_{xx}\), \(u(0,t)=u(L,t)=0\), and \(u(x,0)=f(x)\in L^2(0,L)\), the Dirichlet operator \(-\partial_{xx}\) has eigenpairs
\[\phi_n(x)=\sqrt{2/L}\sin(n\pi x/L),\qquad\lambda_n=(n\pi/L)^2,\quad n\ge1.\]
The mild solution is
\[u(t,x)=\sum_{n=1}^\infty\langle f,\phi_n\rangle_{L^2}\,e^{-\kappa\lambda_nt}\phi_n(x).\]
For sufficient smoothness, integration by parts gives \(\frac{d}{dt}\|u(t)\|_{L^2}^2=-2\kappa\|u_x(t)\|_{L^2}^2\le-2\kappa\lambda_1\|u(t)\|_{L^2}^2\). Thus \(\|u(t)\|_{L^2}\le e^{-\kappa\lambda_1t}\|f\|_{L^2}\).

For the Dirichlet wave equation \(u_{tt}=c^2u_{xx}\), each coefficient satisfies \(a_n''(t)+c^2\lambda_na_n(t)=0\), so \(a_n=A_n\cos(c\sqrt{\lambda_n}t)+B_n\sin(c\sqrt{\lambda_n}t)\), with \(B_n\) determined by initial velocity. A truncated Galerkin expansion \(u_N=\sum_{n=1}^Na_n(t)\phi_n(x)\) approximates the PDE while preserving the chosen boundary conditions.

### Exercises with answers

1. How much faster does the tenth heat mode decay than the first? **Answer:** its exponential decay rate is \(\lambda_{10}/\lambda_1=100\) times larger.
2. If the initial data equal \(\phi_3\), which modes appear later in the linear heat equation? **Answer:** only \(\phi_3\), multiplied by \(e^{-\kappa\lambda_3t}\).
3. Why do the sine modes fail for nonzero fixed endpoint values without modification? **Answer:** they vanish at endpoints; first subtract a function satisfying the nonhomogeneous boundary data.
4. Does Fourier truncation near a discontinuity automatically produce small maximum error? **No:** Gibbs oscillations persist in amplitude near jumps, although convergence holds in appropriate integral senses.

### Reading and source notes

- Lawrence C. Evans, [*Partial Differential Equations* (AMS textbook information)](https://www.ams.org/books/gsm/019/), separation, weak formulations, and spectral operators.
- [MIT 18.303 Linear Partial Differential Equations](https://ocw.mit.edu/courses/18-303-linear-partial-differential-equations-fall-2006/), boundary eigenfunctions and mode expansions.
- [MIT 18.330 Introduction to Numerical Analysis](https://ocw.mit.edu/courses/18-330-introduction-to-numerical-analysis-spring-2012/), numerical approximation and spectral discretizations.
