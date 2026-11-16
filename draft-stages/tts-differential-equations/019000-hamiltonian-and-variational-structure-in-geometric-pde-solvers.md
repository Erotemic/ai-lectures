# Hamiltonian and variational structure in geometric PDE solvers

<!-- BEGIN SPOKEN LECTURE -->

# Hamiltonian and variational structure in geometric PDE solvers

## Hamiltonian Systems and Symplectic Flows

Watch a pendulum swinging in a nearly frictionless room. It trades kinetic energy for potential energy and back again. In the simplest mathematical model, the total energy stays constant. That conservation law is familiar. What is less obvious is that the motion also preserves a geometric structure in the space of all possible positions and momenta.

Hamiltonian mechanics organizes a state using two kinds of coordinates. Position tells us where the system is; momentum tells us how it is moving. Together they form phase space. For one moving particle on a line, phase space is a plane with one position axis and one momentum axis. A whole trajectory draws a curve in that plane.

Instead of deriving the motion directly from forces, we begin with a function H of position and momentum, called the Hamiltonian. For familiar conservative mechanical systems it is total energy: kinetic plus potential. Hamilton's equations say that the time derivative of position is the derivative of H with respect to momentum, while the time derivative of momentum is minus the derivative of H with respect to position.

The minus sign is essential. It turns the gradient of H sideways in phase space. Rather than following the gradient downhill, a state moves along a level set of H when the Hamiltonian has no explicit time dependence.

### The oscillator as a phase-space curve

Take a mass attached to an ideal spring. Its Hamiltonian is momentum squared divided by twice the mass, plus spring stiffness times position squared divided by two. Hamilton's equations reproduce the familiar harmonic-oscillator equation.

In phase space, the conserved energy curves are ellipses. The moving state travels around one of them. There is no spiral toward the center, because the ideal model has no friction. If we add a velocity-dependent damping force, the trajectory can spiral inward, but we have changed the dynamical class. That damped flow is not the autonomous Hamiltonian flow of the original two-dimensional canonical phase space.

A conserved energy function already restricts the motion, but there is more. Consider a small region of initial states, a patch rather than one point. Follow every state in the patch forward by the same amount of time. Its shape may shear and stretch. Yet its area in canonical position-momentum coordinates is preserved.

This is Liouville's theorem in one degree of freedom. In several degrees of freedom it becomes preservation of phase-space volume. The reason is visible in the equations: the divergence of the Hamiltonian vector field is zero, since two mixed second derivatives of H cancel.

### Symplectic structure, not just area

A two-form called the symplectic form captures the oriented areas of position-momentum planes. In canonical coordinates, it is the sum of each position differential wedged with its matching momentum differential. Hamiltonian flow preserves that two-form, not merely its top-dimensional volume.

Volume preservation alone would be weaker. In a high-dimensional phase space, a map can keep overall volume constant while distorting the pairwise position-momentum geometry in ways a symplectic map cannot. Symplecticity is the stronger invariant that makes Hamiltonian dynamics a special branch of differential equations.

The preservation law has a concise proof. The Hamiltonian vector field is defined so that contracting it with the symplectic form gives the differential of H, up to the chosen sign convention. Taking an exterior derivative yields zero, since the exterior derivative applied twice vanishes. Cartan's formula for the Lie derivative then shows that the flow leaves the symplectic form unchanged.

This geometric argument works even in coordinates where the phase portrait is hard to draw. It also explains why symplectic numerical integrators are worth studying: an algorithm that respects the form can preserve qualitative phase-space behavior over long times better than a method chosen only for low local error.

### What is conserved, and what is not

For an autonomous Hamiltonian, energy remains constant along exact solutions. For a time-dependent Hamiltonian, the flow can remain symplectic while energy changes. Likewise, a symplectic numerical integrator does not generally preserve the exact Hamiltonian at every step. It preserves a discrete version of the geometric structure, often with favorable long-time energy behavior under additional hypotheses.

Nor does phase-volume preservation forbid every kind of complicated motion. Hamiltonian systems with enough degrees of freedom can exhibit chaotic trajectories. Symplecticity limits how volume can contract, but it does not require every orbit to be periodic or easy to predict.

We have now separated three facts that are often merged. A system can have a conserved energy. It can have an invariant symplectic form. It can preserve phase volume. In autonomous canonical Hamiltonian mechanics, all three occur, but they are logically different statements with different assumptions.

The main gain is structural. Hamilton's equations are not merely another notation for Newton's laws. They reveal which patterns remain intact while trajectories twist through phase space, and they give us a language for preserving those patterns in analysis and computation.

The same structural question survives discretization: which variational, symplectic, or conservation identity should the numerical update preserve?

## Hamiltonian and variational structure through discretization

### Variational PDEs and Noether-Type Conservation Identities

A wave equation can be written as a differential relation between time derivatives and spatial derivatives. But some wave equations also arise from a variational principle: among nearby fields with fixed boundary data, the physical field makes an action stationary. This second description exposes connections that are difficult to see from the equation alone.

For a vibrating string, the action accumulates a Lagrangian density through space and time. The density contains positive kinetic energy from time variation and a negative contribution from spatial gradients. If we add a potential energy term, the variational equation becomes a nonlinear wave equation.

The Euler-Lagrange calculation is a systematic way to derive that PDE. Perturb the field by a small test function, differentiate the action with respect to the perturbation, and integrate derivative terms by parts. When the first variation vanishes for all compactly supported perturbations, the coefficient of the test function must vanish. That coefficient is the Euler-Lagrange expression.

#### Stationarity produces the wave equation

Take a real field u depending on time and one spatial coordinate. Let the Lagrangian density be one half of the time derivative squared, minus one half of the wave-speed squared times the spatial derivative squared, minus a potential V of u.

Differentiate with respect to the field and its derivatives. After integrating by parts, the stationarity condition says that the second time derivative minus wave-speed squared times the second spatial derivative plus the derivative of the potential is zero.

If the potential is zero, we obtain the ordinary linear wave equation. If the potential is nonlinear, the wave still has a variational structure, but its dynamics can include complex oscillations, traveling structures, and nonlinear instabilities.

The calculation reveals what must be assumed. We need enough smoothness to justify the variation, or a weak formulation where the same statement has a precise meaning. Boundary terms vanish if perturbations are compactly supported or if the boundary conditions are chosen appropriately. Ignoring them can change the conserved quantity.

#### Time translation and energy

The Lagrangian density just described has no explicit time dependence. We can shift a solution forward in time without changing the rule that defines the action. Noether's theorem links that continuous symmetry to a conserved current.

For this wave equation, the energy density is one half of the time derivative squared plus one half of the wave-speed squared times the spatial derivative squared plus the potential V of u. The first two terms are kinetic and elastic energy. Multiply the PDE by the time derivative and rearrange derivatives. The result is a local energy balance: the time derivative of energy density plus the spatial derivative of an energy flux is zero.

Integrate over a spatial interval. The change of total energy equals the flux through the endpoints. If the domain is periodic, or the solution decays sufficiently fast on the whole line, there is no net boundary flux, so total energy is conserved.

A wave on a bounded interval with a driven boundary can gain energy from the driver. Noether's local identity still describes the transfer, but the total energy of the interior is not conserved by itself. That distinction between a local conservation law and an integrated global constant matters in every application.

#### Spatial translation and momentum

Now shift the spatial coordinate. If the Lagrangian has no explicit dependence on position, this is another symmetry. It leads to momentum conservation under appropriate boundary conditions. For the simple scalar wave, a momentum-like density is the product of the time derivative and the spatial derivative, up to a sign convention.

The local identity has the same pattern: a time derivative of momentum density equals a spatial derivative of a stress-like expression. Integrating removes the flux when boundary conditions permit. The resulting conserved quantity is not the same as energy. Its origin is a different symmetry.

This gives a powerful diagnostic. If a PDE is supposed to represent a spatially uniform medium but its computed dynamics do not respect the corresponding momentum balance, we should ask whether the discrepancy comes from forcing, boundaries, discretization, or an actual error in the model.

#### Field shifts and other symmetries

For the free wave equation, adding a constant to u leaves the gradient-based Lagrangian unchanged. This field-shift symmetry yields another conserved current, whose time component is the time derivative of u. If we add a potential that depends on u, the shift symmetry normally disappears. Correspondingly, the associated conservation law no longer holds.

A symmetry is not just any transformation that makes a picture look similar. Noether's theorem concerns differentiable one-parameter transformations of the action, possibly changing the Lagrangian by a total divergence. The transformation must be a genuine variational symmetry under the appropriate hypotheses.

#### Why weak solutions complicate the story

Smooth solutions permit direct differentiation and integration by parts. Weak solutions may contain sharp fronts, shocks, or insufficient regularity for products of derivatives to be defined pointwise. Then a formal conservation law may hold only in a distributional sense, or an admissible solution may satisfy an energy inequality instead of equality.

For example, entropy-admissible shocks in conservation laws can dissipate an entropy-like quantity even though the inviscid PDE has a formal smooth conservation identity. A numerical method can also break exact conservation if it does not respect the relevant discrete structure.

The takeaway is not that every PDE has an action or that every conserved quantity is guaranteed by a symmetry. It is that whenever a suitable variational symmetry exists, the Euler-Lagrange framework gives an organized way to derive a local current. That current connects analysis, mechanics, geometry, and computational verification.

### Structure-Preserving PDE Integrators: Discretizing Without Losing Geometry

Suppose we simulate a vibrating string for many thousands of oscillations. The numerical solution does not explode, and the time step is small. Yet the amplitude slowly grows or fades, and the oscillation phase drifts until the animation tells a different story from the physical string.

A small local truncation error does not guarantee that the right qualitative behavior survives over long times. A numerical integrator may approximate each short step well and still corrupt conservation laws, symmetries, or the geometry of the underlying flow.

Structure-preserving integration begins by identifying what the equation preserves and constructing the discrete method to respect an appropriate analogue. That structure might be a symplectic form, a quadratic energy, a mass integral, a momentum map, or a discrete multisymplectic conservation law. There is no universal method that exactly preserves all of them for every nonlinear equation. The task is to choose the right structure for the problem.

### Turning the wave equation into oscillators

Take the one-dimensional wave equation on a periodic interval, with unit wave speed for simplicity. Its second time derivative equals its second spatial derivative. The continuous energy is the integral of one half the squared velocity plus one half the squared spatial gradient. Differentiate it in time, integrate the spatial derivative by parts, and periodicity cancels the boundary terms. The energy is constant.

Now discretize space first, leaving time continuous. Let q be the vector of grid displacements and p the vector of momenta. A symmetric stiffness matrix records the coupling between neighboring grid values. The semidiscrete system has the form that the time derivative of q equals an inverse mass matrix times p, while the time derivative of p equals minus the stiffness matrix times q.

This is a finite-dimensional Hamiltonian system. Its energy is a quadratic form: kinetic energy in p plus potential energy in q. Eigenvectors of the stiffness operator provide independent oscillatory modes. A numerical time method must act on those modes without introducing artificial amplification or damping if it claims to conserve the semidiscrete energy.

### The midpoint rule and an exact algebraic identity

The implicit midpoint method evaluates the vector field at the average of the old and new states. For a linear Hamiltonian system with constant mass and stiffness matrices, it has a remarkable property: it preserves the quadratic Hamiltonian exactly in exact arithmetic.

Here is the calculation without hiding it behind a theorem. The difference of two squares equals the difference times the sum. Apply that identity to the kinetic term and the potential term. The change of kinetic energy is the average momentum paired with the momentum increment. The change of potential energy is the average displacement paired with the displacement increment, weighted by the stiffness matrix.

The midpoint update says the displacement increment is the time step times the inverse mass matrix applied to the average momentum. It also says the momentum increment is minus the time step times stiffness applied to the average displacement. Substitute both. The two energy changes cancel exactly.

This is not merely saying the method has small energy error. For the linear semidiscrete wave equation with the stated matrices and boundary treatment, the discrete energy after each step equals the energy before it, apart from floating-point solution error.

### What is preserved for nonlinear Hamiltonians?

A common misunderstanding is that implicit midpoint preserves the exact energy of every nonlinear Hamiltonian system. It does not. It is symplectic, which means it preserves the canonical symplectic two-form for Hamiltonian ODEs under the standard conditions. For quadratic Hamiltonians, symplecticity and midpoint's algebra also give exact energy conservation. For a general nonlinear Hamiltonian, exact energy is not guaranteed by symplecticity alone.

Why use a symplectic method if the original energy can vary slightly? Backward-error analysis often shows that, under smoothness, small step size, and suitable nonresonance assumptions, the numerical trajectory follows the flow of a nearby modified Hamiltonian over long intervals. Its energy error can remain bounded and oscillatory rather than systematically drifting. The quantitative time scale depends on the equation and the theorem's hypotheses.

This is a geometric rather than pointwise guarantee. It helps explain why symplectic integrators are valuable for long-duration Hamiltonian simulations even when their per-step accuracy is no better than that of a non-symplectic method of the same order.

### The explicit alternative: Störmer–Verlet

The leapfrog or Störmer–Verlet method is popular for wave equations because it separates updates of positions and momenta into simple half- and full-steps. For separable Hamiltonians it is symplectic and time-reversible. It does not require solving an implicit nonlinear system at each time step.

But it is conditionally stable. Consider one harmonic oscillator with frequency omega. The discrete recurrence has bounded oscillations only when the product of omega and the time step is less than two, with the boundary case requiring separate care. For a spatially discretized wave equation, the highest resolved frequency grows as the grid is refined, creating a Courant-type time-step restriction.

The implicit midpoint method avoids this particular linear stability restriction on purely imaginary eigenvalues, but its phases are still distorted: a discrete oscillation angle is related to the true angle by an arctangent. Energy conservation alone does not imply exact phase accuracy.

### What about multisymplectic PDEs?

Space and time can sometimes be treated more symmetrically. For suitable first-order Hamiltonian PDEs, one can write an equation involving skew-symmetric matrices multiplying space and time derivatives of a state vector. Solutions satisfy a local multisymplectic conservation law, not just a global energy balance.

Multisymplectic integrators attempt to preserve a discrete counterpart of that local law. This approach is useful for wave propagation and nonlinear field equations where a time-only Hamiltonian formulation hides some of the geometric structure.

Yet a discretization may preserve a discrete multisymplectic form and still have numerical dispersion or parasitic oscillation modes. Structure preservation needs to be combined with consistency, stability and resolution analysis. No preserved two-form compensates for a grid too coarse to resolve the physics of interest.

### Conservation claims must name the boundary

A periodic string and a string with fixed endpoints conserve energy when the boundary does no work. A string driven at one endpoint generally does not have constant interior energy, because energy flows through the boundary. A method that forces constant interior energy in that setting would be wrong.

The same is true for PDE systems with damping, forcing or shocks. A correct discrete method may need to preserve a balance law with fluxes and dissipation rather than an invariant. For compressible fluids, exact energy balance can coexist with entropy production at shocks. Preserving the wrong invariant is not a sign of quality.

There are also numerical qualifications. An implicit update solved only approximately may violate exact conservation by the nonlinear or linear solver residual. Floating-point arithmetic introduces small deviations. A theorem about the algebraic method in exact arithmetic must not be advertised as a computer-verified equality unless those implementation effects are bounded.

### Designing for the invariant rather than discovering drift later

Structure-preserving methods are not a promise of perfect simulation. They are a design strategy: identify the geometric or physical law, derive its discrete analogue, prove the method respects that analogue under explicit assumptions, and separately check stability, consistency, resolution, and solver error.

For the semidiscrete linear wave equation, implicit midpoint offers a clean example. The energy is quadratic, the midpoint identity makes the energy changes cancel, and the proof works for every step size in exact arithmetic. For nonlinear dynamics the story becomes subtler, and symplecticity is often the more robust long-time principle. Preserving the right structure can make a numerical model much more faithful than a method selected only for low short-time truncation error.

### Multisymplectic Variational Integrators for Wave Equations

A numerical solution of a wave equation may look convincing for a few periods and then gradually drift. Its phase shifts. Its energy changes. A wave that should remain bounded may grow for no physical reason. Small truncation errors are inevitable, but their long-term organization depends strongly on the numerical method.

One response is to use smaller time steps. Another is to design the scheme around the geometry of the original differential equation. Variational integrators take the second route. Instead of discretizing the differential equation directly, we discretize the action and demand stationarity of the discrete action. For field equations, this can yield a discrete multisymplectic conservation law.

The claim is not that such a method makes all physical invariants exactly constant. Symplectic and multisymplectic structures are particular geometric quantities. They constrain how errors accumulate, but stability and accurate energy behavior still depend on the mesh, the timestep, the boundary conditions and the particular discretization.

### The wave equation comes from an action

Consider a one-dimensional vibrating field u of position and time. Its kinetic energy density is one half times the square of its time derivative. Its elastic energy density is one half times a wave-speed constant squared times the square of its spatial derivative. We may also add a potential energy density depending on u.

The Lagrangian density is kinetic energy minus elastic and potential energy. Integrate this density over a space-time region. The result is the action. A physical solution makes the action stationary under variations that vanish at the prescribed boundary.

Perform the variation and integrate by parts. The resulting Euler-Lagrange equation is the wave equation with a potential force: the second time derivative of u, minus wave speed squared times the second spatial derivative, plus the derivative of the potential, equals zero.

This derivation already links dynamics to geometry. The field equation is not just a formula we decide to approximate. It is the condition that a functional be stationary. Boundary terms from the variation carry information about momentum and symplectic structure.

### Two variations produce a conserved current

Take two small variations around a solution, call them v and w. Both satisfy the linearized wave equation, whose potential term contains the second derivative of the potential evaluated along the background solution.

Multiply the linearized equation for w by v, multiply the equation for v by w, and subtract. The potential terms cancel because they involve the same scalar coefficient. The remaining terms form a divergence: a time derivative of one antisymmetric expression minus a spatial derivative of another.

Thus there is a local conservation law for a two-form current built from pairs of variations. It is called multisymplectic because space and time both contribute boundary fluxes of symplectic type. Integrating over a space-time rectangle shows that the flux through the boundary vanishes under the appropriate orientation conventions.

This is not simply the statement that total physical energy is conserved. Energy comes from time-translation symmetry and Noether's theorem. The multisymplectic conservation law comes from the antisymmetry of the second variation of the action. Both arise from variational structure, but they are different invariants.

### Discretize the action, not merely the acceleration

Now replace the continuum by a grid of space-time cells. On each cell, approximate the action using values at its corners or edges, together with quadrature weights. Sum the cell actions. Take partial derivatives of this discrete action with respect to every interior grid value. Setting those derivatives to zero gives the discrete field equations.

Because the equations arise as stationarity conditions, the discrete first and second variations retain an exact algebraic identity. Boundary contributions from neighboring cells cancel when assembled consistently. The result is a discrete multisymplectic form formula: an oriented sum of boundary two-form contributions vanishes for variations satisfying the linearized discrete equations.

This exact identity is the geometric advantage. It does not depend on pretending the grid has no truncation error. It follows algebraically from the fact that mixed second derivatives of the discrete action commute and boundary terms are organized consistently.

### A familiar wave stencil appears

In the simplest linear case, set the potential to zero and use centered differences in space and time. The resulting equation advances the field at a grid point using its values at the two neighboring time levels and the two neighboring spatial points.

Written as an update, the next field value equals twice the current field value minus the previous one, plus a factor proportional to the wave speed squared and the time-step squared over the space-step squared, multiplying the discrete spatial second derivative.

This is the standard leapfrog or centered scheme for a linear wave equation. It also arises from a suitable discrete variational principle. The example shows that structure preservation does not necessarily require exotic formulas. A familiar stencil can have a geometric interpretation that explains some of its long-time properties.

### Stability is still a separate calculation

Take a Fourier mode on a periodic spatial grid. The centered spatial second difference multiplies that mode by a negative number proportional to the square of the sine of half the grid frequency. Each Fourier mode therefore behaves like a harmonic oscillator with a mesh-dependent frequency.

The leapfrog recurrence for that oscillator is stable when the product of the timestep and the oscillator frequency is at most two, with marginal cases needing care. The largest mesh frequency gives the familiar one-dimensional Courant condition: wave speed times timestep divided by spatial step must not exceed one.

Notice the logic. The variational construction gave a discrete geometric conservation law. Fourier analysis supplied a stability restriction. A method can be variational and still become unstable if the timestep violates that restriction. Symplecticity never replaces the Courant analysis.

### Energy oscillation versus energy explosion

Even within the stable range, the discrete scheme does not generally preserve the exact continuum Hamiltonian at every step. For a harmonic oscillator, leapfrog exactly preserves a modified quadratic invariant and a symplectic area form. The physical energy oscillates around its correct value. This is very different from a slow monotone drift that accumulates over many periods.

For a nonlinear wave, backward error analysis can sometimes explain long-time near-conservation under additional smoothness, nonresonance and step-size assumptions. But one cannot infer global error bounds for every nonlinear field equation just from the label variational.

Boundary conditions matter as well. A periodic grid permits boundary flux cancellation. At an open boundary, physical energy and multisymplectic current can flow out. The correct discrete law must include that boundary contribution rather than declaring every integral constant.

### Why more than one symplectic form?

In finite-dimensional mechanics, symplectic structure concerns time evolution of positions and momenta. A field theory has infinitely many interacting spatial points, and its action is integrated over both space and time. The multisymplectic viewpoint treats the conservation law locally in space-time rather than only after integrating over the whole spatial slice.

This supports discretizations where temporal and spatial directions are treated more symmetrically. It also clarifies why some schemes preserve a global symplectic form after spatial discretization while others directly preserve a local multi-directional flux law. The two approaches overlap but are not logically identical.

The practical design principle is to begin with the structure one wants to preserve. If a field equation is variational, one can approximate its action and derive a scheme. If a numerical method must handle dissipation, shocks, irregular meshes or moving boundaries, the discrete action and boundary terms need corresponding modifications. For strongly dissipative or entropy-producing solutions, preserving a conservative symplectic form may not be the dominant requirement.

The broader lesson is that numerical approximation should respect more than pointwise differential identities when possible. A wave equation carries an action, symmetries, boundary terms and local geometric conservation laws. A discrete method can inherit some of those relationships exactly while still approximating the wave only up to finite resolution. Understanding both statements is the basis of reliable structure-preserving simulation.

### Moving-Boundary PDEs and the Geometric Conservation Law

Consider a fluid whose density is perfectly uniform. The physical solution is constant in space and time. Now let a computational grid move through the fluid, with cells expanding and contracting. A careless numerical method can report changing density even though the physical field has not changed.

That failure is not a subtle turbulence phenomenon. It is a bookkeeping error: the scheme did not account consistently for how the volume of each moving cell changes. The geometric conservation law is designed to prevent precisely this artifact.

Moving-grid methods are useful when a physical boundary moves, when a structure deforms, or when the mesh is adapted to follow interesting features of a flow. They introduce a new geometric velocity: the speed of the grid faces. That velocity need not equal the fluid velocity. Mixing them up gives incorrect fluxes.

### Conservation on a fixed interval

Begin with a scalar conservation law in one dimension. The time derivative of a conserved density plus the spatial derivative of its flux is zero. On a fixed interval, the rate of change of the total conserved quantity equals the incoming flux at the left boundary minus the outgoing flux at the right.

This formula reflects something physical. The amount of material changes because material crosses the boundary. If no flux crosses, the total remains fixed.

But when the interval's endpoints move, a second effect appears. The region over which we integrate changes, even for a perfectly constant field. The total in the region can increase simply because the region gets larger.

### The transport theorem supplies the missing terms

Let the left boundary be a function a of time and the right boundary a function b. Differentiate the integral of the density between those boundaries. Besides the integral of the local time derivative, we gain a boundary term at the right endpoint proportional to its speed, and subtract a boundary term at the left endpoint proportional to its speed.

Insert the conservation law. The result has the same incoming-minus-outgoing structure as before, but the appropriate flux at each moving face is the physical flux minus the face velocity times the conserved density.

This is the arbitrary Lagrangian–Eulerian viewpoint. Eulerian coordinates are fixed in space; Lagrangian coordinates move with material; an ALE grid may move according to an independent mesh design. The conservative balance uses the flux relative to that moving grid.

The formula follows from calculus and conservation. A discrete geometric conservation law is then an additional requirement on a numerical method: its approximations of face motion and cell-volume change must agree sufficiently to preserve constants.

### A complete numerical sanity check

Suppose the physical flux is zero and the density is constantly five. Let the left grid face move to the right at speed one, and the right grid face move right at speed two. Start with a cell whose left endpoint is zero and right endpoint is two.

After time t, the left endpoint is t and the right endpoint is two plus two t. The width is two plus t. Its total conserved quantity is five times two plus t, so its rate of change is five.

Now compute through moving-face fluxes. At the right face, physical flux minus face speed times density is minus ten. At the left face, it is minus five. Incoming minus outgoing relative flux equals minus five minus minus ten, which is plus five. The two calculations agree.

If we had used the physical flux zero at both faces and ignored their motion, we would have predicted zero change in the cell total. That would contradict its explicitly growing volume. A code that then divides the wrong total by the new cell volume would produce a fake decline in the density.

### The free-stream preservation test

Take any constant state compatible with the physical PDE. A numerical scheme on a moving mesh should preserve it exactly, up to the intended arithmetic behavior of the implementation. This is often called free-stream preservation.

The test sounds elementary, but it catches substantial bugs in geometric discretization. Cell volumes may be updated with one temporal quadrature while swept-face fluxes use another. Coordinate transformations may be differentiated inconsistently. Face normals or mesh velocities may be evaluated at incompatible times.

The discrete geometric conservation law demands a consistent relationship among these geometric quantities. On a fixed mesh it is nearly invisible. On a strongly moving mesh it can determine whether a physically steady field remains steady at all.

### Moving boundaries and boundary conditions

A moving computational face is not necessarily a physical wall. For a physical moving impermeable boundary, fluid and wall normal velocities must satisfy an appropriate no-penetration condition. For a computational face moving through the fluid, relative flux need not vanish.

This distinction matters especially in fluid–structure interaction. A structural surface imposes physical boundary conditions. Interior mesh motion merely changes coordinates and cells. The numerical method must correctly represent both effects and not substitute a grid kinematic condition for a physical one.

Remapping adds another challenge. An ALE algorithm may move a mesh with the solution for part of a step, then interpolate onto a new mesh. That interpolation can change mass or create oscillations unless constructed conservatively. Even if each moving-grid step respects its volume balance, a careless remap can undo the result.

### Geometry in several dimensions

In higher dimensions, cell boundaries are surfaces with outward normals. The transport theorem states that the rate of change of the integral over a moving domain equals the integral of the local time derivative plus a boundary integral of density times normal boundary velocity.

For a conservation law, this produces physical flux minus density times mesh velocity at every face. In a finite-volume method, the discrete volume change must equal the signed swept volumes of the faces. Under this identity, the update of a constant field is consistent with the update of the cell geometry.

A high-order method must make the consistency hold at its actual quadrature and time-integration level, not merely in a continuous derivation printed in the documentation.

### Why this is a geometric invariant of the algorithm

The geometric conservation law does not add a new physical conservation quantity. It enforces that changing the grid's geometry does not invent a change in the solution. It is a consistency principle between the mesh's motion and the PDE's conservative flux balance.

That principle can be tested before attempting realistic flow simulations. Prescribe a constant state, move and deform a mesh, and check that the numerical field remains constant. Then verify mass balance when the physical flux is nonzero. The tests are simple enough to isolate geometry bugs from flux-solver bugs.

The broader lesson is that a numerical coordinate system has its own dynamics. When the coordinates move, the scheme must transport the geometry as accurately as it transports the solution. Otherwise a perfectly constant physical world can become an artificial numerical wave.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Hamiltonian Systems and Symplectic Flows

**Track:** Differential Equations and Dynamical Systems. **Background:** first-order systems, gradients, differential forms, energy conservation. **Central question:** what dynamical structure survives in systems without dissipation?

#### Mathematical companion (not spoken)

For \(q,p\in\mathbf R^n\) and a smooth autonomous \(H(q,p)\), Hamilton's equations are
\[\dot q_i=\partial H/\partial p_i,\qquad \dot p_i=-\partial H/\partial q_i.\]
With \(\omega=\sum_i dq_i\wedge dp_i\), the convention \(\iota_{X_H}\omega=dH\) yields these equations. Since \(d\omega=0\), Cartan's formula gives \(\mathcal L_{X_H}\omega=d(\iota_{X_H}\omega)=d(dH)=0\), so \(\Phi_t^*\omega=\omega\). For autonomous H, \(dH/dt=dH(X_H)=\omega(X_H,X_H)=0\). For H depending explicitly on t, \(dH/dt=\partial_t H\) along the flow.

**Harmonic oscillator:** \(H=p^2/(2m)+kq^2/2\), so \(q'=p/m\), \(p'=-kq\), and \(q''+(k/m)q=0\). Energy shells are ellipses. The phase-space divergence equals \(\sum_i\partial_{q_i}\partial_{p_i}H-\partial_{p_i}\partial_{q_i}H=0\), yielding Liouville volume preservation for smooth canonical Hamiltonian flows.

**Caution:** volume preservation does not imply symplecticity in dimensions four and higher; exact energy conservation need not hold for time-dependent H, and a symplectic numerical map need not exactly conserve H.

##### Exercises with answers

1. For H=(q²+p²)/2, find the trajectories. **Answer:** \(q'=p\), \(p'=-q\); circles oriented clockwise in the (q,p) plane, with fixed q²+p².
2. Why cannot an autonomous planar Hamiltonian flow have an asymptotically attracting equilibrium surrounded by a neighborhood of positive area? **Answer:** the flow preserves area and cannot contract the whole neighborhood to zero area.
3. Is \(H(q,p,t)=p^2/2+tq\) constant along a trajectory? **Answer:** generally no; \(dH/dt=\partial_tH=q\).
4. What is stronger than phase-volume preservation? **Answer:** preservation of the symplectic two-form, including oriented areas of canonical two-planes.

##### Reading and source notes

- [MIT OpenCourseWare, Symplectic Geometry lecture 4](https://ocw.mit.edu/courses/18-966-geometry-of-manifolds-spring-2007/864a8cbd55d8d9696a717db38f8668a9_lect04.pdf), Hamiltonian vector fields and symplectic flows.
- [MIT Classical Mechanics II, Hamiltonian Mechanics](https://ocw.mit.edu/courses/8-223-classical-mechanics-ii-january-iap-2017/09ab68ae8e7987debc025892e00c0f1f_MIT8_223IAP17_Lec15.pdf), coordinates and energy.
- [MIT Classical Mechanics: A Computational Approach](https://ocw.mit.edu/courses/12-620j-classical-mechanics-a-computational-approach-fall-2008/pages/readings/), Liouville theorem and symplectic maps.

### Hamiltonian and variational structure through discretization

### Hamiltonian and variational structure through discretization

#### Companions, sources, and study material (not spoken)

##### Variational PDEs and Noether-Type Conservation Identities

**Track:** Differential Equations and Dynamical Systems. **Background:** Euler-Lagrange equations, wave equations, symmetries, weak solutions. **Central question:** when does a symmetry of an action force a quantity to be conserved by a PDE?

###### Mathematical companion (not spoken)

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

##### Exercises with answers

1. Derive the Euler-Lagrange PDE when `V(u)=m^2u^2/2`. **Answer:** `u_tt-c^2u_xx+m^2u=0`.
2. What is the energy-flux term for the free wave? **Answer:** `j=-c^2u_tu_x`.
3. When does spatial integration yield constant total energy? **Answer:** when boundary energy flux vanishes or cancels, as in periodic conditions.
4. Does a nonconstant potential preserve constant field-shift symmetry? **Answer:** generally no.

##### Reading and source notes

- [Peter Olver, Applications of Lie Groups to Differential Equations](https://link.springer.com/book/10.1007/978-1-4684-0274-2), Noether symmetries and conservation laws.
- [University of Cambridge, Mathematical Methods of Classical Mechanics notes](https://www.damtp.cam.ac.uk/user/tong/dynamics.html), variational and Noether background.
- [Lawrence Evans, Partial Differential Equations](https://bookstore.ams.org/gsm-19-r), weak formulations and energy estimates.

##### Structure-Preserving PDE Integrators: Discretizing Without Losing Geometry

**Track:** Differential Equations and Dynamical Systems. **Background:** wave equations, semidiscrete systems, Hamiltonian mechanics, and numerical time integration. **Central question:** when can a discrete evolution reproduce the conservation laws and geometry of a PDE?

###### Mathematical companion (not spoken)

Let `M=M^T>0`, `K=K^T>=0` and the semidiscrete wave equation be `qdot=M^{-1}p`, `pdot=-Kq`. Define
\[
H(q,p)=\tfrac12p^TM^{-1}p+\tfrac12q^TKq.
\]
The implicit midpoint equations, with `bar q=(q_{n+1}+q_n)/2` and similarly `bar p`, are
\[
q_{n+1}-q_n=hM^{-1}\bar p,\qquad p_{n+1}-p_n=-hK\bar q.
\]
Using difference-of-squares,
\[
H_{n+1}-H_n=\bar p^TM^{-1}(p_{n+1}-p_n)+\bar q^TK(q_{n+1}-q_n)=0.
\]
This is exact for linear constant-coefficient semidiscrete systems and exact solves. For general nonlinear Hamiltonians, midpoint is symplectic but not necessarily energy preserving.

For the oscillator `q''+omega^2 q=0`, Störmer–Verlet yields `q_{n+1}-2q_n+q_{n-1}=-(h omega)^2 q_n`. The roots lie on the unit circle for `0<h omega<2`. At `h omega=2` there is a repeated root -1 with possible linear growth for general initial data; do not claim unconditional boundedness at equality. The implicit midpoint rotation satisfies `theta=2 arctan(h omega/2)`, displaying phase error despite exact quadratic energy.

##### Exercises with answers

1. What assumption permits the midpoint energy cancellation? **Answer:** a constant quadratic Hamiltonian with symmetric mass and stiffness matrices, using an exact implicit solve.
2. Is a symplectic method necessarily exactly energy-preserving for a nonlinear potential? **Answer:** no.
3. What is the open stability interval for Verlet on a single harmonic oscillator? **Answer:** `0<h omega<2`.
4. Can energy flow through a driven boundary? **Answer:** yes; the correct PDE law is an energy balance with boundary flux.

##### Reading and source notes

- [Hairer, Lubich and Wanner, Geometric Numerical Integration](https://link.springer.com/book/10.1007/3-540-30666-8), symplectic methods and backward-error analysis.
- [Frank, Moore and Reich, Linear PDEs and Numerical Methods That Preserve a Multisymplectic Conservation Law](https://doi.org/10.1137/050628271), multisymplectic methods and numerical dispersion.
- [Marsden, Patrick and Shkoller, Multisymplectic Geometry, Variational Integrators and Nonlinear PDEs](https://arxiv.org/abs/math/9807080), variational PDE discretization.

##### Multisymplectic Variational Integrators for Wave Equations

**Track:** Differential Equations and Dynamical Systems. **Background:** Lagrangian mechanics, wave equations, numerical time stepping, and symplectic geometry. **Central question:** can a discrete wave solver preserve the geometric conservation law inherited from an action principle?

###### Mathematical companion (not spoken)

For a scalar field, take
\[
\mathcal L(u,u_t,u_x)=\tfrac12u_t^2-\tfrac{c^2}{2}u_x^2-V(u).
\]
The Euler-Lagrange equation is `u_tt-c^2 u_xx+V'(u)=0`. Variations v,w satisfy `v_tt-c^2 v_xx+V''(u)v=0` and the same for w. Subtracting the equations after cross multiplication yields
\[
\partial_t(v w_t-w v_t)-c^2\partial_x(v w_x-w v_x)=0.
\]
This is a local multisymplectic conservation identity. A discrete action assembled from space-time cell Lagrangians yields a discrete analogue through its second variation, subject to compatible boundary orientations and discrete Euler-Lagrange equations.

For the linear wave and centered differences,
\[
\frac{u_j^{n+1}-2u_j^n+u_j^{n-1}}{\Delta t^2}
=c^2\frac{u_{j+1}^n-2u_j^n+u_{j-1}^n}{\Delta x^2}.
\]
The spatial Fourier frequency is `omega_k=(2c/Delta x)|sin(k Delta x/2)|`; leapfrog oscillator stability `Delta t omega_k<=2` for all modes requires `c Delta t/Delta x<=1` in one dimension, with endpoint marginality handled separately. Symplectic/multisymplectic conservation does not guarantee exact conservation of continuum energy or unconditional stability.

##### Exercises with answers

1. What equation follows from the stated Lagrangian when `V(u)=m^2 u^2/2`? **Answer:** `u_tt-c^2u_xx+m^2u=0`.
2. What becomes of the local multisymplectic current integrated over a periodic spatial domain? **Answer:** its net spatial flux cancels, yielding a conserved temporal two-form for linearized variations.
3. If `c=2` and `Delta x=0.1`, what is the one-dimensional linear CFL timestep limit? **Answer:** `Delta t<=0.05`.
4. Does the variational derivation make leapfrog stable for `c Delta t/Delta x=2`? **Answer:** no; the highest-frequency modes are unstable.

##### Reading and source notes

- [Marsden and West, Discrete Mechanics and Variational Integrators](https://doi.org/10.1017/S096249290100006X), action-based integrators and discrete symplectic structure.
- [Bridges and Reich, Multi-Symplectic Integrators](https://www.sciencedirect.com/science/article/abs/pii/S0375960101002948), space-time geometry and multi-symplectic schemes.
- [Marsden, Patrick and Shkoller, Multisymplectic Geometry, Variational Integrators, and Nonlinear PDEs](https://arxiv.org/abs/math/9807080), field-theoretic multisymplectic conservation and discretization.

##### Moving-Boundary PDEs and the Geometric Conservation Law

**Track:** Differential Equations. **Background:** conservation laws, finite-volume methods, transport theorems, and moving meshes. **Central question:** how can numerical mesh motion preserve a physically constant solution?

###### Mathematical companion (not spoken)

For `u_t+F(u)_x=0` on moving cell `[a(t),b(t)]`, Leibniz/Reynolds transport gives
\[
\frac{d}{dt}\int_{a(t)}^{b(t)}u\,dx
=\big[F(u)-a'(t)u\big]_{x=a(t)}-\big[F(u)-b'(t)u\big]_{x=b(t)}.
\]
Equivalently the right face has outward relative flux `F(u)-b'u`, the left face `-(F(u)-a'u)`. With `u=5`, `F=0`, `a(t)=t`, `b(t)=2+2t`, the mass is `M=5(2+t)` and `M'=5`. Right relative flux `-10`, left relative flux `-5`, so incoming minus outgoing is `-5-(-10)=5`. A fixed-state-preserving ALE discretization needs the discrete cell-volume change to match the signed swept-face volumes (geometric conservation law).

In higher dimensions for `u_t+div F(u)=0`, domain boundary velocity `w` gives
\[
\frac{d}{dt}\int_{\Omega(t)}u\,dx
=-\int_{\partial\Omega(t)}\big(F(u)-u w\big)\cdot n\,dS.
\]
A moving physical boundary and a moving interior mesh face impose different physical conditions; no-penetration is not automatic on arbitrary ALE mesh faces.

##### Exercises with answers

1. If both faces translate at the same speed and `u` is uniform with zero flux, does cell mass change? **Answer:** No; cell width is constant.
2. If a one-dimensional cell expands at width rate three and constant density is four, what is its mass rate? **Answer:** twelve.
3. Why is `F-uw` the correct moving-face flux? **Answer:** it subtracts transport caused by motion of the control-volume boundary.
4. What does free-stream preservation detect? **Answer:** inconsistent discrete geometry and moving-face flux updates.

##### Reading and source notes

- [Thomas and Lombard, Geometric Conservation Law and Its Application to Flow Computations on Moving Grids](https://doi.org/10.2514/3.61273), classic geometric conservation law analysis.
- [Donea, Huerta, Ponthot and Rodríguez-Ferran, Arbitrary Lagrangian–Eulerian Methods](https://doi.org/10.1002/0470091355.ecm009), transport formulas and ALE formulations.
- [Farhat, Geuzaine and Grandmont, Discrete Geometric Conservation Law and Stability of Nonlinear ALE Schemes](https://doi.org/10.1006/jcph.2001.6932), discrete consistency and stability.
