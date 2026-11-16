# 040000 - Moving-Boundary PDEs and the Geometric Conservation Law

**Track:** Differential Equations. **Background:** conservation laws, finite-volume methods, transport theorems, and moving meshes. **Central question:** how can numerical mesh motion preserve a physically constant solution?

<!-- BEGIN SPOKEN LECTURE -->

# A moving grid can create a fictitious wave

Consider a fluid whose density is perfectly uniform. The physical solution is constant in space and time. Now let a computational grid move through the fluid, with cells expanding and contracting. A careless numerical method can report changing density even though the physical field has not changed.

That failure is not a subtle turbulence phenomenon. It is a bookkeeping error: the scheme did not account consistently for how the volume of each moving cell changes. The geometric conservation law is designed to prevent precisely this artifact.

Moving-grid methods are useful when a physical boundary moves, when a structure deforms, or when the mesh is adapted to follow interesting features of a flow. They introduce a new geometric velocity: the speed of the grid faces. That velocity need not equal the fluid velocity. Mixing them up gives incorrect fluxes.

# Conservation on a fixed interval

Begin with a scalar conservation law in one dimension. The time derivative of a conserved density plus the spatial derivative of its flux is zero. On a fixed interval, the rate of change of the total conserved quantity equals the incoming flux at the left boundary minus the outgoing flux at the right.

This formula reflects something physical. The amount of material changes because material crosses the boundary. If no flux crosses, the total remains fixed.

But when the interval's endpoints move, a second effect appears. The region over which we integrate changes, even for a perfectly constant field. The total in the region can increase simply because the region gets larger.

# The transport theorem supplies the missing terms

Let the left boundary be a function a of time and the right boundary a function b. Differentiate the integral of the density between those boundaries. Besides the integral of the local time derivative, we gain a boundary term at the right endpoint proportional to its speed, and subtract a boundary term at the left endpoint proportional to its speed.

Insert the conservation law. The result has the same incoming-minus-outgoing structure as before, but the appropriate flux at each moving face is the physical flux minus the face velocity times the conserved density.

This is the arbitrary Lagrangian–Eulerian viewpoint. Eulerian coordinates are fixed in space; Lagrangian coordinates move with material; an ALE grid may move according to an independent mesh design. The conservative balance uses the flux relative to that moving grid.

The formula follows from calculus and conservation. A discrete geometric conservation law is then an additional requirement on a numerical method: its approximations of face motion and cell-volume change must agree sufficiently to preserve constants.

# A complete numerical sanity check

Suppose the physical flux is zero and the density is constantly five. Let the left grid face move to the right at speed one, and the right grid face move right at speed two. Start with a cell whose left endpoint is zero and right endpoint is two.

After time t, the left endpoint is t and the right endpoint is two plus two t. The width is two plus t. Its total conserved quantity is five times two plus t, so its rate of change is five.

Now compute through moving-face fluxes. At the right face, physical flux minus face speed times density is minus ten. At the left face, it is minus five. Incoming minus outgoing relative flux equals minus five minus minus ten, which is plus five. The two calculations agree.

If we had used the physical flux zero at both faces and ignored their motion, we would have predicted zero change in the cell total. That would contradict its explicitly growing volume. A code that then divides the wrong total by the new cell volume would produce a fake decline in the density.

# The free-stream preservation test

Take any constant state compatible with the physical PDE. A numerical scheme on a moving mesh should preserve it exactly, up to the intended arithmetic behavior of the implementation. This is often called free-stream preservation.

The test sounds elementary, but it catches substantial bugs in geometric discretization. Cell volumes may be updated with one temporal quadrature while swept-face fluxes use another. Coordinate transformations may be differentiated inconsistently. Face normals or mesh velocities may be evaluated at incompatible times.

The discrete geometric conservation law demands a consistent relationship among these geometric quantities. On a fixed mesh it is nearly invisible. On a strongly moving mesh it can determine whether a physically steady field remains steady at all.

# Moving boundaries and boundary conditions

A moving computational face is not necessarily a physical wall. For a physical moving impermeable boundary, fluid and wall normal velocities must satisfy an appropriate no-penetration condition. For a computational face moving through the fluid, relative flux need not vanish.

This distinction matters especially in fluid–structure interaction. A structural surface imposes physical boundary conditions. Interior mesh motion merely changes coordinates and cells. The numerical method must correctly represent both effects and not substitute a grid kinematic condition for a physical one.

Remapping adds another challenge. An ALE algorithm may move a mesh with the solution for part of a step, then interpolate onto a new mesh. That interpolation can change mass or create oscillations unless constructed conservatively. Even if each moving-grid step respects its volume balance, a careless remap can undo the result.

# Geometry in several dimensions

In higher dimensions, cell boundaries are surfaces with outward normals. The transport theorem states that the rate of change of the integral over a moving domain equals the integral of the local time derivative plus a boundary integral of density times normal boundary velocity.

For a conservation law, this produces physical flux minus density times mesh velocity at every face. In a finite-volume method, the discrete volume change must equal the signed swept volumes of the faces. Under this identity, the update of a constant field is consistent with the update of the cell geometry.

A high-order method must make the consistency hold at its actual quadrature and time-integration level, not merely in a continuous derivation printed in the documentation.

# Why this is a geometric invariant of the algorithm

The geometric conservation law does not add a new physical conservation quantity. It enforces that changing the grid's geometry does not invent a change in the solution. It is a consistency principle between the mesh's motion and the PDE's conservative flux balance.

That principle can be tested before attempting realistic flow simulations. Prescribe a constant state, move and deform a mesh, and check that the numerical field remains constant. Then verify mass balance when the physical flux is nonzero. The tests are simple enough to isolate geometry bugs from flux-solver bugs.

The broader lesson is that a numerical coordinate system has its own dynamics. When the coordinates move, the scheme must transport the geometry as accurately as it transports the solution. Otherwise a perfectly constant physical world can become an artificial numerical wave.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

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

### Exercises with answers

1. If both faces translate at the same speed and `u` is uniform with zero flux, does cell mass change? **Answer:** No; cell width is constant.
2. If a one-dimensional cell expands at width rate three and constant density is four, what is its mass rate? **Answer:** twelve.
3. Why is `F-uw` the correct moving-face flux? **Answer:** it subtracts transport caused by motion of the control-volume boundary.
4. What does free-stream preservation detect? **Answer:** inconsistent discrete geometry and moving-face flux updates.

### Reading and source notes

- [Thomas and Lombard, Geometric Conservation Law and Its Application to Flow Computations on Moving Grids](https://doi.org/10.2514/3.61273), classic geometric conservation law analysis.
- [Donea, Huerta, Ponthot and Rodríguez-Ferran, Arbitrary Lagrangian–Eulerian Methods](https://doi.org/10.1002/0470091355.ecm009), transport formulas and ALE formulations.
- [Farhat, Geuzaine and Grandmont, Discrete Geometric Conservation Law and Stability of Nonlinear ALE Schemes](https://doi.org/10.1006/jcph.2001.6932), discrete consistency and stability.
