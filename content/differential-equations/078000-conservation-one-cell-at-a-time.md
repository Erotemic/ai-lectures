# Conservation One Cell at a Time: Finite-Volume Methods from Scratch

<!-- BEGIN SPOKEN LECTURE -->

# Conservation One Cell at a Time

Suppose our numerical solution represents the concentration of a substance flowing through a pipe. The pipe is divided into cells. Each cell keeps track of how much substance is inside it. Every time we update the simulation, substance can cross the faces between neighboring cells. There is one accounting rule we should be able to demand without qualification: if a certain amount leaves one cell through a shared face, the same amount must enter the cell on the other side.

That sounds almost too obvious to be a mathematical design principle. Yet it gives us one of the most useful ways to construct numerical methods for transport, fluid flow, and other conservation laws. Rather than guessing a spatial derivative and then asking whether it conserves mass, we start with the exact balance of mass in each cell and only afterward choose how to approximate the flux crossing a face.

The result is a finite-volume method. We will derive it from an integral, calculate a full open-boundary time step, prove global conservation by cancellation, and see what changes when cells have unequal widths or flux depends nonlinearly on the state. Along the way we will separate conservation from accuracy, positivity, and the choice of time step.

## A cell stores an average, not a point measurement

Begin with a conservation law: the time derivative of q plus the spatial derivative of a flux f of q equals zero. This is the general form that includes constant-speed transport, for which f of q equals a times q.

Divide an interval into cells. Cell i extends from its left face to its right face. Define Q sub i as the average concentration in that whole cell, not the value of the exact solution at one special point. To compute the amount stored there, multiply Q sub i by the cell width.

Integrate the conservation equation over the cell. The integral of the time derivative becomes the rate of change of the stored amount. The integral of the spatial flux derivative becomes the flux at the right face minus the flux at the left face. Rearranging, the rate of stored amount equals flux entering through the left face minus flux leaving through the right face.

So far we have made no spatial approximation. The equation is an exact consequence of the conservation law, as long as the physical flux and boundary traces make sense. We could even interpret it as the starting point for a weak solution with discontinuities.

To turn it into a computation, we must estimate the face flux from information in the nearby cells. Denote the approximate flux through the right face of cell i by F sub i plus one half. A forward time step changes the cell average by the time step divided by cell width times the incoming flux minus the outgoing flux.

This is the entire structural pattern of a finite-volume method. Each cell's value changes by a difference of fluxes. The physics and numerical accuracy enter through the formula chosen for the common face flux, and through how we advance the resulting time-dependent equations.

## Why shared faces produce exact conservation

Consider two adjacent cells. Cell i loses an amount proportional to the flux through its right face. Cell i plus one gains exactly that same amount through its left face, because it is the same face and the same flux number. Add the two cell balances and the internal flux cancels.

Now add the balances for every cell in a row. Every interior flux appears once as an outgoing term and once as an incoming term, with opposite signs. All cancel. What remains is the flux entering at the far left minus the flux exiting at the far right.

This is a telescoping sum. The total amount represented by the cell averages changes by exactly the net boundary flux used by the numerical method. On a periodic domain, the outer faces connect, so all face fluxes cancel and the discrete total is conserved to roundoff, assuming each shared flux is used consistently.

The result holds even if the individual flux estimates are not accurate. Conservation is a structural property. That is both its power and its limitation. A conservative scheme can still smear a front, oscillate around a shock, or use a catastrophically large time step. It will merely account for mass consistently while doing those other things poorly.

Nevertheless, the structural guarantee is valuable because it does not depend on a smooth solution, a fine grid, or a special choice of initial data. A numerical derivative built through flux differences automatically respects the same integral balance from which the physical equation was derived.

## Recovering upwind from a face flux

For constant positive transport speed a, the physical flux is a times concentration. Which cell's concentration should we use at a face? Since the material moves from left to right, take the concentration in the cell on the left. This is the upwind flux.

At the face between cells i and i plus one, the flux estimate is a times Q sub i. At the left face of cell i, it is a times Q sub i minus one. Substitute those into the balance update. We obtain the same donor-cell formula developed from one-sided finite differences: the new cell average is one minus C times its old value plus C times the upstream neighbor's old value.

This agreement is not accidental. For constant-speed advection on a uniform grid, a first-order upwind finite difference and a first-order upwind finite volume can have identical update equations. But their explanations differ. The finite-volume viewpoint begins with cell averages and the flux through a common face. It remains natural when we use unequal cell sizes, when the solution has jumps, or when fluxes come from nonlinear physics.

There is a useful subtlety here. If the initial data are exactly constant inside each cell and a positive-speed wave moves less than one cell width in a single step, donor-cell averaging reproduces the exact new cell averages for that one step. After the step, however, the exact translated profile generally varies within cells. The method throws away that within-cell detail and again treats each cell as constant. Repeating this reconstruction and averaging is where the numerical diffusion arises.

So finite-volume conservation is exact in its balance, but the reconstructed profile and the face flux are approximations. We should never conflate those two statements.

## An open channel calculated by hand

Let us compute an example with five equal-width cells. Their initial average concentrations are zero, two, one, zero, zero. The total of the five averages is three, so the represented amount is three times the cell width.

Flow moves right at positive speed a. At the inlet on the left, a reservoir supplies concentration one. At the outlet on the right, material simply leaves according to the last cell's concentration. Choose the Courant number one half.

The flux through any interior face is the speed times the concentration in the cell immediately to its left. The inlet flux is speed times one. The outlet flux is speed times the last cell concentration, which is currently zero. The update is the same weighted averaging rule as before, except the first cell receives half of the inlet concentration rather than an upstream grid-cell value.

Calculate the new cells in order. The first becomes one half. The second begins at two and has a zero upstream neighbor, so it becomes one. The third begins at one and receives from the cell holding two, so it becomes one point five. The fourth starts at zero and receives from the cell holding one, so it becomes one half. The fifth remains zero.

The new list is one half, one, one point five, one half, zero. Its sum is three point five. The total has increased by one half of one cell-width unit. That is exactly the amount the inlet contributed during this step. The outlet initially carried away nothing.

No amount has appeared mysteriously in the interior. For example, the increase in the third cell is balanced by the part of the second cell's decrease that crossed their shared face. The interior changes are transfers, not creation. If we now change the inlet concentration or introduce a nonzero outlet flux, the net change will be computed from those boundary values alone.

Compare this with our periodic six-cell pulse. There the total cannot change because any substance leaving through the right side reenters on the left. The same face-flux bookkeeping handles both situations; only the boundary model changes.

## Unequal widths and more than one dimension

Now allow cell widths to vary. A narrow cell holds less substance than a wide cell at the same average concentration. We must therefore sum width times concentration, not simply add the cell averages, to obtain total mass.

The finite-volume update divides the difference of face fluxes by the actual cell width. A single shared flux still cancels in the mass-weighted sum, even though adjacent cells can have different widths and therefore different changes in concentration. This property is particularly useful on meshes refined near an interesting front or boundary.

The local time-step restriction also depends on width. For constant positive velocity and a first-order upwind explicit update, the local Courant number is a times delta t divided by that cell's width. The narrowest cell can therefore impose the most restrictive time step if we insist on a single global explicit step. Refinement improves spatial resolution but can increase the cost of advancing a simulation.

In two dimensions, a cell has several faces. For each face we multiply the normal component of the transported flux by the face length and subtract outgoing from incoming amounts. In three dimensions we use face areas. Interior faces still come in equal and opposite pairs in the sums of cell balances. The bookkeeping principle is unchanged; only the geometry and the choice of face flux become more involved.

We have just described the reason finite-volume schemes are attractive for conservation laws on complicated meshes. They do not require us to invent a global coordinate derivative at each cell. They work from the flux passing through each part of the boundary of a control volume.

## What changes when the flux is nonlinear?

Suppose the flux is not simply a constant speed times concentration. It may instead depend nonlinearly on q. Consider the scalar flux one half q squared. In a smooth part of the solution, disturbances travel at speed q, so the direction of information can vary with the state.

At a face between two cells, the left and right states can be different. We can no longer blindly take the left state for every case. We need a numerical flux that depends on both neighboring states and represents the behavior of the underlying wave problem at the interface.

A basic consistency requirement is that if the left and right states are equal to the same q, then the numerical flux must equal the physical flux f of q. If that condition fails, even a constant solution may evolve incorrectly. But consistency is not enough: stability and the selection of physically appropriate weak solutions also matter.

For the quadratic flux, imagine a state of two to the left of an interface and zero to the right. The jump propagates as a shock at speed one, obtained from the change in flux divided by the change in state. It moves right. A finite-volume method can use the corresponding interface solution to decide the flux. In more general nonlinear problems, resolving the interface wave pattern is called solving a Riemann problem, exactly or approximately.

This is a preview, not an assumption needed for our foundation route. The important point is architectural: the same discrete conservation balance survives when we replace the simple upwind flux with a numerical flux appropriate for nonlinear waves. We change the rule at the interface, not the principle that a shared face must have one flux value.

## The four checks a transport computation deserves

After deriving a finite-volume scheme, what should we test first? Start with conservation. Sum every cell average multiplied by its width and compare the change to the prescribed net boundary flux. If they disagree beyond rounding and known source terms, there is an implementation or bookkeeping error.

Next check the direction of information. A positive-speed flow should use an inlet state on the left and let the right outlet export information. Reverse the velocity and those roles reverse. On a periodic mesh, a pulse should wrap around without losing total mass.

Then check bounds and stability. For the first-order positive-speed upwind method, a Courant number between zero and one makes the update a convex combination, so nonnegative data remain nonnegative. Above one, even a conservative update can produce undershoots and growing modes.

Finally check accuracy. Use a smooth translated wave whose exact solution is known. Refine the grid and measure error after the same physical time. Then use a pulse with a sharp front and examine how many cells it takes to represent the transition, whether the mass remains correct, and whether any overshoot develops. Conservation and convergence are not the same question.

Notice how the ideas fit together. Characteristics tell us where information originates. Conservation tells us what can change in a cell. The CFL limit tells us how far information may travel during an explicit local update. Modified-equation analysis tells us what extra smoothing the grid has introduced. A numerical flux ties these ideas together at each shared face.

We have reached a practical foundation for numerical transport. The equations are simple enough to compute with pencil and paper, but the principles scale to scientific simulations with millions of cells: represent an amount in each volume, use one flux per shared face, enforce the boundary balance, and choose numerical approximations that respect the physics of information flow. The next essential tools are not more sophisticated differential equations; they are ways to check, measure, and improve the behavior of these basic approximations.

<!-- END SPOKEN LECTURE -->

## Mathematical companion: telescoping fluxes and an open-boundary update

For \(q_t+f(q)_x=0\), cell \(I_i=(x_{i-1/2},x_{i+1/2})\), width \(h_i\), and average \(Q_i(t)=h_i^{-1}\int_{I_i}q(x,t)\,dx\),
\[
\frac{d}{dt}(h_i Q_i)=f(q(x_{i-1/2},t))-f(q(x_{i+1/2},t)).
\]
A forward-Euler finite-volume discretization with a single shared numerical flux \(\widehat F_{i+1/2}\) is
\[
h_iQ_i^{n+1}=h_iQ_i^n+\Delta t(\widehat F_{i-1/2}^n-\widehat F_{i+1/2}^n).
\]
Summing over cells \(i=1,\dots,N\) telescopes:
\[
\sum_{i=1}^N h_i(Q_i^{n+1}-Q_i^n)
=\Delta t(\widehat F_{1/2}^n-\widehat F_{N+1/2}^n).
\]
With periodic boundaries, the two boundary fluxes coincide and total represented mass is exactly conserved algebraically. Equal fluxes should be computed once or used consistently at every shared face.

For \(f(q)=a q\), \(a>0\), choose \(\widehat F_{i+1/2}=aQ_i\), including \(\widehat F_{1/2}=a g\) for an inlet value \(g\). Then for uniform \(h\), with \(C=a\Delta t/h\),
\[
Q_i^{n+1}=(1-C)Q_i^n+C Q_{i-1}^n,
\]
where \(Q_0=g\) for the left inlet. At the last face use \(\widehat F_{N+1/2}=a Q_N\) for an outflow with \(a>0\).

Worked five-cell case: \(Q^0=(0,2,1,0,0)\), \(g=1\), \(C=1/2\). The new state is
\[
Q^1=(1/2,1,3/2,1/2,0),\qquad
\sum Q_i^1-\sum Q_i^0=1/2.
\]
The boundary balance gives \(C(g-Q_5^0)=1/2(1-0)=1/2\), agreeing exactly.

For a general consistent numerical flux, \(\widehat F(q,q)=f(q)\). For Burgers' flux \(f(q)=q^2/2\), a shock between constant states \(q_L=2\) and \(q_R=0\) has Rankine–Hugoniot speed \(s=(f(2)-f(0))/(2-0)=1\). Selecting an admissible numerical interface flux for nonlinear conservation laws requires additional information about the wave and entropy behavior; consistency and telescoping alone do not ensure convergence to the entropy solution.

### Exercises with worked answers

1. Why sum \(h_iQ_i\), not \(Q_i\), on a nonuniform grid? **Answer:** \(Q_i\) is an average; multiplying by width yields amount stored in the cell.
2. Reproduce the five-cell open-channel update with \(C=1/2\). **Answer:** \((0.5,1,1.5,0.5,0)\) and total \(3.5\).
3. For that example, replace the inlet value by zero. What is the one-step total? **Answer:** \(3\), because the initial outflow is also zero and the net boundary flux vanishes in that step.
4. If a periodic scheme uses one shared flux per face, can its total amount change merely because an interior flux was inaccurate? **Answer:** no; internal errors change the distribution, but opposite contributions cancel in the mass sum.
5. At positive constant speed, why can a very narrow cell restrict a global explicit time step? **Answer:** its local Courant number \(a\Delta t/h_i\) must remain no greater than one for the basic positive upwind update.
6. For \(f(q)=q^2/2\), calculate the shock speed between states \(q_L=2,q_R=0\). **Answer:** \(s=1\); an admissible shock connection must also be checked against entropy criteria.

### Sources and further reading

- [Randall J. LeVeque, *Finite Volume Methods for Hyperbolic Problems* (2002)](https://www.cambridge.org/core/books/abs/finite-volume-methods-for-hyperbolic-problems/finite-volume-methods/CB7B0A27A6D37AE3B906D4AE7C60A87E).
- [LeVeque, Cambridge University Press, Chapter 4: Finite Volume Methods](https://www.cambridge.org/core/books/abs/finite-volume-methods-for-hyperbolic-problems/finite-volume-methods/CB7B0A27A6D37AE3B906D4AE7C60A87E).
- [Stanford Math 220A, Conservation Laws lecture notes](https://web.stanford.edu/class/math220a/lecturenotes.html).
