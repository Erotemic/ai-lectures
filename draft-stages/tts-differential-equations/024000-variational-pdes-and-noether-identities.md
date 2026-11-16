# 024000 — Variational PDEs and Noether-Type Conservation Identities

**Track:** Differential Equations and Dynamical Systems. **Background:** Euler-Lagrange equations, wave equations, symmetries, weak solutions. **Central question:** when does a symmetry of an action force a quantity to be conserved by a PDE?

<!-- BEGIN SPOKEN LECTURE -->

# Why an equation has an energy law

A wave equation can be written as a differential relation between time derivatives and spatial derivatives. But some wave equations also arise from a variational principle: among nearby fields with fixed boundary data, the physical field makes an action stationary. This second description exposes connections that are difficult to see from the equation alone.

For a vibrating string, the action accumulates a Lagrangian density through space and time. The density contains positive kinetic energy from time variation and a negative contribution from spatial gradients. If we add a potential energy term, the variational equation becomes a nonlinear wave equation.

The Euler-Lagrange calculation is a systematic way to derive that PDE. Perturb the field by a small test function, differentiate the action with respect to the perturbation, and integrate derivative terms by parts. When the first variation vanishes for all compactly supported perturbations, the coefficient of the test function must vanish. That coefficient is the Euler-Lagrange expression.

## Stationarity produces the wave equation

Take a real field u depending on time and one spatial coordinate. Let the Lagrangian density be one half of the time derivative squared, minus one half of the wave-speed squared times the spatial derivative squared, minus a potential V of u.

Differentiate with respect to the field and its derivatives. After integrating by parts, the stationarity condition says that the second time derivative minus wave-speed squared times the second spatial derivative plus the derivative of the potential is zero.

If the potential is zero, we obtain the ordinary linear wave equation. If the potential is nonlinear, the wave still has a variational structure, but its dynamics can include complex oscillations, traveling structures, and nonlinear instabilities.

The calculation reveals what must be assumed. We need enough smoothness to justify the variation, or a weak formulation where the same statement has a precise meaning. Boundary terms vanish if perturbations are compactly supported or if the boundary conditions are chosen appropriately. Ignoring them can change the conserved quantity.

## Time translation and energy

The Lagrangian density just described has no explicit time dependence. We can shift a solution forward in time without changing the rule that defines the action. Noether's theorem links that continuous symmetry to a conserved current.

For this wave equation, the energy density is one half of the time derivative squared plus one half of the wave-speed squared times the spatial derivative squared plus the potential V of u. The first two terms are kinetic and elastic energy. Multiply the PDE by the time derivative and rearrange derivatives. The result is a local energy balance: the time derivative of energy density plus the spatial derivative of an energy flux is zero.

Integrate over a spatial interval. The change of total energy equals the flux through the endpoints. If the domain is periodic, or the solution decays sufficiently fast on the whole line, there is no net boundary flux, so total energy is conserved.

A wave on a bounded interval with a driven boundary can gain energy from the driver. Noether's local identity still describes the transfer, but the total energy of the interior is not conserved by itself. That distinction between a local conservation law and an integrated global constant matters in every application.

## Spatial translation and momentum

Now shift the spatial coordinate. If the Lagrangian has no explicit dependence on position, this is another symmetry. It leads to momentum conservation under appropriate boundary conditions. For the simple scalar wave, a momentum-like density is the product of the time derivative and the spatial derivative, up to a sign convention.

The local identity has the same pattern: a time derivative of momentum density equals a spatial derivative of a stress-like expression. Integrating removes the flux when boundary conditions permit. The resulting conserved quantity is not the same as energy. Its origin is a different symmetry.

This gives a powerful diagnostic. If a PDE is supposed to represent a spatially uniform medium but its computed dynamics do not respect the corresponding momentum balance, we should ask whether the discrepancy comes from forcing, boundaries, discretization, or an actual error in the model.

## Field shifts and other symmetries

For the free wave equation, adding a constant to u leaves the gradient-based Lagrangian unchanged. This field-shift symmetry yields another conserved current, whose time component is the time derivative of u. If we add a potential that depends on u, the shift symmetry normally disappears. Correspondingly, the associated conservation law no longer holds.

A symmetry is not just any transformation that makes a picture look similar. Noether's theorem concerns differentiable one-parameter transformations of the action, possibly changing the Lagrangian by a total divergence. The transformation must be a genuine variational symmetry under the appropriate hypotheses.

## Why weak solutions complicate the story

Smooth solutions permit direct differentiation and integration by parts. Weak solutions may contain sharp fronts, shocks, or insufficient regularity for products of derivatives to be defined pointwise. Then a formal conservation law may hold only in a distributional sense, or an admissible solution may satisfy an energy inequality instead of equality.

For example, entropy-admissible shocks in conservation laws can dissipate an entropy-like quantity even though the inviscid PDE has a formal smooth conservation identity. A numerical method can also break exact conservation if it does not respect the relevant discrete structure.

The takeaway is not that every PDE has an action or that every conserved quantity is guaranteed by a symmetry. It is that whenever a suitable variational symmetry exists, the Euler-Lagrange framework gives an organized way to derive a local current. That current connects analysis, mechanics, geometry, and computational verification.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For a real field `u(t,x)` and Lagrangian
\[
\mathcal L(u,u_t,u_x)=\tfrac12u_t^2-\tfrac{c^2}{2}u_x^2-V(u),
\]
variation of `S[u]=integral L dt dx` with compactly supported variations gives
\[
u_{tt}-c^2u_{xx}+V'(u)=0.
\]
The local energy density `e=(1/2)u_t^2+(c^2/2)u_x^2+V(u)` and flux `j=-c^2u_t u_x` obey `partial_t e + partial_x j=0` for smooth solutions. Indeed `partial_t e=u_t(u_tt-c^2u_xx+V')+c^2 partial_x(u_t u_x)=c^2 partial_x(u_t u_x)`. Integration over `[a,b]` gives `dE/dt=j(a)-j(b)`; periodic or zero-flux boundaries yield conservation.

For translation-invariant x-dependence, define `p=u_t u_x`. Then using the PDE,
\[
\partial_t p=\partial_x\left(\tfrac12u_t^2+\tfrac{c^2}{2}u_x^2-V(u)\right).
\]
The sign of the physical momentum depends on the convention for canonical stress-energy. If `V=0`, constant field shifts give `partial_t u_t - c^2 partial_x u_x=0`, so `integral u_t dx` is conserved on a periodic domain. Adding a nonconstant potential breaks this shift symmetry.

Weak/entropy solutions require distributional or inequality formulations. Smooth formal identities are not automatically valid pointwise across shocks.

### Exercises with answers

1. Derive the Euler-Lagrange PDE when `V(u)=m^2u^2/2`. **Answer:** `u_tt-c^2u_xx+m^2u=0`.
2. What is the energy-flux term for the free wave? **Answer:** `j=-c^2u_tu_x`.
3. When does spatial integration yield constant total energy? **Answer:** when boundary energy flux vanishes or cancels, as in periodic conditions.
4. Does a nonconstant potential preserve constant field-shift symmetry? **Answer:** generally no.

### Reading and source notes

- [Peter Olver, Applications of Lie Groups to Differential Equations](https://link.springer.com/book/10.1007/978-1-4684-0274-2), Noether symmetries and conservation laws.
- [University of Cambridge, Mathematical Methods of Classical Mechanics notes](https://www.damtp.cam.ac.uk/user/tong/dynamics.html), variational and Noether background.
- [Lawrence Evans, Partial Differential Equations](https://bookstore.ams.org/gsm-19-r), weak formulations and energy estimates.
