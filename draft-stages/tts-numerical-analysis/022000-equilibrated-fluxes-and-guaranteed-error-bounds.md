# 022000 — Equilibrated Fluxes: A Computable Upper Bound on PDE Error

**Track:** Numerical Analysis. **Background:** weak formulations of Poisson problems, finite elements, and integration by parts. **Central question:** how can a numerical approximation carry a mathematically guaranteed bound on the error in its gradient?

<!-- BEGIN SPOKEN LECTURE -->

# A numerical picture is not an error bound

Imagine solving a boundary-value problem using finite elements. The resulting function looks smooth enough, and refinement changes the plotted solution only slightly. Does that mean the approximation is accurate? Perhaps, but visual stability is not a mathematical bound.

To certify an approximation, we want an inequality involving a quantity we can compute and the actual, unknown error. Ideally the inequality should be an upper bound with a known constant, rather than an estimate whose scale depends on an unspecified factor.

For elliptic partial differential equations, equilibrated flux reconstruction provides one route to such a certificate. Its central trick is to reconstruct a vector field satisfying the differential equation's balance law exactly, or with a separately controlled residual. We can then compare that reconstructed flux with the gradient of the computed solution.

The resulting error estimate is not just a heuristic based on how rough the mesh looks. It follows from the weak equation and a single use of the Cauchy–Schwarz inequality.

# The model problem

Consider Poisson's equation on a bounded domain. We seek a function whose negative Laplacian equals a given source, with zero values on the boundary. The finite-element approximation also vanishes on the boundary, but typically satisfies the differential equation only in a weak, projected sense.

The natural error norm for this problem is the energy norm: the square root of the integral of the squared gradient of the difference between the exact solution and the finite-element approximation.

Why the gradient? Because the weak equation pairs gradients, and because the zero boundary condition allows the gradient norm to control the solution itself through a Poincaré inequality.

If we already knew the exact solution, we could integrate the error directly. But that would defeat the purpose of numerical solution. We need a certificate derived from the computed approximation, the source, and a reconstruction that can be found without solving the entire original problem exactly.

# Reconstruct a flux that balances the source

The exact gradient of the solution has a divergence equal to the negative source. We therefore look for another vector field, call it the reconstructed flux, with the same divergence.

A flux can be represented by piecewise polynomials that have continuous normal components across mesh faces. The natural space for such fields is called H-divergence: vector fields whose components and divergence are square-integrable. This is not merely a function space chosen for elegance. Its continuity properties allow integration by parts without fictitious source terms appearing at interior faces.

In practice, equilibrated fluxes can be built using local mixed finite-element solves on element patches. They are designed to satisfy the required balance constraints while remaining close to the gradient of the computed finite-element solution.

# The energy estimate

Let the error be the exact solution minus the computed solution. The weak form says that the gradient of the exact solution, paired with the gradient of any boundary-vanishing test function, equals the source paired with that test function.

The equilibrated flux has the same weak pairing because its divergence is the negative source. Subtract these equalities and take the error itself as test function. The gradient error squared becomes the inner product of the reconstructed flux minus the computed gradient with the gradient error.

Now use Cauchy–Schwarz. The error norm squared is at most the norm of the flux difference times the error norm. Cancel the nonzero error norm. We obtain an error bound with constant one: the energy norm of the true error is no greater than the ordinary square-integrable norm of the equilibrated flux minus the computed gradient.

This is an upper bound, not merely an empirical indicator. It follows from the source-balance condition. If that condition is only approximate, the residual must be included as an additional term; it cannot be ignored.

# A one-dimensional example with an exact number

Solve the equation in which the negative second derivative equals two on the interval from zero to one, with the solution zero at both endpoints.

The exact solution is x times one minus x, a downward-opening parabola. Its derivative is one minus two x. But pretend we do not use that solution directly. Instead, approximate it by the piecewise-linear function that is zero at the ends and has value one quarter at the midpoint. Its slope is plus one half on the left half and minus one half on the right.

An equilibrated one-dimensional flux must have derivative negative two. So it has the form a constant minus two x. To make it as close as possible in the square-integrable norm to our piecewise-constant computed gradient, choose the constant equal to one.

The reconstructed flux is one minus two x. The difference between this flux and the computed gradient has squared integral equal to one twelfth. Thus the estimator is the square root of one twelfth.

In this particular example the reconstructed flux coincides with the exact derivative, so the bound is actually an equality. In a general multidimensional problem the flux reconstruction will not be exact, but the same inequality remains valid if the balance condition holds.

# What real implementations must check

The phrase guaranteed upper bound has prerequisites. The weak problem must be well posed in the stated space. The finite-element approximation must satisfy the required boundary conditions. The reconstructed flux must belong to the appropriate H-divergence space and satisfy the balance equation to the claimed precision.

If we replace the source by a finite-element projection, there is a data-oscillation term. If the source, flux, or quadrature is computed in floating-point arithmetic, roundoff and integration error can affect whether the claimed numerical value is truly an outward bound.

There is a distinction between an inequality proved for exact reconstructed functions and a software output that certifies the inequality with rigorous numerical arithmetic. Fully verified computation requires both parts.

# Guaranteed does not mean efficient by itself

A very large upper bound can be correct but unhelpful. We also want efficiency: the reconstructed estimator should be comparable to the actual error, possibly up to controlled oscillation terms. Good equilibrated flux constructions can provide local estimates on elements or patches, making them useful for adaptive mesh refinement.

A typical adaptive workflow computes an approximate solution, reconstructs the flux, evaluates local error contributions, and refines the regions that contribute most. The global theorem guarantees reliability; local efficiency explains why the estimator tends to identify worthwhile refinement regions.

The broader idea extends beyond the Poisson equation. For diffusion and reaction–diffusion problems, and for some time-dependent discretizations, flux equilibration can support reliable error control. Each extension requires its own assumptions and sometimes additional residual terms.

An accurate-looking picture is not a proof. An equilibrated balance law plus an explicit energy identity can turn a computed finite-element field into one.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For the homogeneous Dirichlet Poisson problem on a bounded Lipschitz domain `Omega`, let `u in H_0^1(Omega)` satisfy
\[
\int_\Omega\nabla u\cdot\nabla v=\int_\Omega fv
\quad\forall v\in H_0^1(\Omega).
\]
Let `u_h in H_0^1(Omega)` be any conforming approximation and `sigma in H(div;Omega)` satisfy `div sigma=-f` in the distributional sense. Then for `e=u-u_h`, integration by parts gives
\[
\|\nabla e\|_{L^2}^2=\int_\Omega(\sigma-\nabla u_h)\cdot\nabla e
\le\|\sigma-\nabla u_h\|_{L^2}\|\nabla e\|_{L^2}.
\]
Therefore
\[
\boxed{\|\nabla(u-u_h)\|_{L^2}\le\|\sigma-\nabla u_h\|_{L^2}.}
\]
If the flux balances only an approximation `f_h`, i.e. `div sigma=-f_h`, the estimate has an extra residual `||f-f_h||_{H^-1}` (or an upper bound such as `C_P ||f-f_h||_{L^2}`). No unknown estimator constant appears in the ideal exact-balance inequality.

**One-dimensional exact check.** For `-u''=2` on (0,1), u(0)=u(1)=0, use `u_h(0)=0`, `u_h(1/2)=1/4`, `u_h(1)=0` with piecewise-linear interpolation. Its derivative is `+1/2` on (0,1/2) and `-1/2` on (1/2,1). Choose equilibrated `sigma(x)=1-2x`, since `sigma'=-2`. Direct integration gives
\[
\int_0^1 |\sigma-u_h'|^2\,dx=\frac1{12},\qquad
\|u'-u_h'\|_{L^2}=\frac1{\sqrt{12}}.
\]
The equality is special to this example. In actual computer-assisted certification, flux equilibrium, quadrature and floating-point bounds must themselves be verified.

### Exercises with answers

1. What divergence must an equilibrated flux satisfy for `-Delta u=f`? **Answer:** `div sigma=-f`.
2. Why must the flux have compatible normal components across interior faces? **Answer:** otherwise interior face jumps introduce distributional divergence terms and invalidate exact equilibrium.
3. Evaluate the estimator in the one-dimensional example. **Answer:** `1/sqrt(12)`, about 0.288675.
4. If `div sigma=-f_h` rather than `-f`, can the mismatch be dropped? **Answer:** no; an additional source-residual or oscillation term is required.

### Reading and source notes

- [Ern and Vohralík, Polynomial-Degree-Robust A Posteriori Estimates](https://doi.org/10.1137/130950100), equilibrated flux reconstructions and guaranteed elliptic bounds.
- [Smears and Vohralík, Equilibrated Flux Estimates for Reaction–Diffusion](https://archive.numdam.org/articles/10.1051/m2an/2020034/), robust explicit upper estimates beyond Poisson.
- [Goal-Oriented A Posteriori Error Estimation with Inexact Solvers](https://doi.org/10.1016/j.cam.2019.112367), separating discretization and algebraic errors in certificates.
