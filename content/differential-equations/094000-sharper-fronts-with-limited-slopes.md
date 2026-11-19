# Sharper Fronts without New Oscillations: MUSCL and Slope Limiters

<!-- BEGIN SPOKEN LECTURE -->

# Sharper Fronts without New Oscillations

Take a row of cell averages representing a smooth rising profile. A first-order finite-volume scheme imagines each cell is flat. The reconstructed picture looks like a staircase even if the underlying function is nearly a straight line. That staircase supplies jumps at every cell face, and a numerical solver spends part of its effort smoothing jumps that were artifacts of the representation.

A natural fix is to reconstruct a sloping line inside each cell. Neighboring averages tell us whether the profile is rising or falling and roughly how steeply. We can then compute the left and right values at each shared face and solve the same Riemann problem as before. The conservation update remains unchanged: one face, one flux, equal and opposite contributions to the adjacent cells.

But imagine doing this at the top of a steep pulse. An unconstrained line fitted across neighboring averages can extend above the highest observed value or below the lowest. That artificial excess may then propagate and grow into an oscillation. A sharp method needs both ambition and restraint: use slope where the data justify it, and reduce slope where they do not.

This is the reason for slope limiters and MUSCL reconstruction. The acronym refers to a monotonic upstream-centered scheme for conservation laws. The important mathematics is more transparent than the name: replace piecewise constants by limited piecewise lines, predict their evolution consistently in time, and continue using conservative interface fluxes.

## One line per cell, with its average preserved

Let the average in a cell be Q. Suppose its reconstructed line has a left-edge value below Q and a right-edge value equally far above Q. The average of that line across the cell is still Q. This matters: reconstruction is not allowed to change how much material the cell represents. It only changes how that stored amount is distributed inside the cell for the purpose of calculating interface fluxes.

We will measure slopes by the total change across one cell, rather than change per unit distance. If the reconstructed change is sigma, the left edge has value Q minus one half sigma, and the right edge has value Q plus one half sigma. The physical slope is sigma divided by cell width.

There are two simple candidate changes for a cell. The backward change is the cell's average minus its left neighbor's average. The forward change is its right neighbor's average minus its own. On a smoothly rising straight line with equally spaced samples, these changes agree. Using that common value gives a reconstruction that matches the line exactly inside each cell.

Suppose the neighboring averages are zero, one, and two. The middle cell has backward and forward changes both equal to one. It is natural to reconstruct left and right edges at one half and one and a half. At the interface with the next cell, whose reconstructed line also has slope one, the two edge values meet. There is no artificial jump in the reconstruction of this straight ramp.

Now try a less cooperative sequence of four averages: zero, one, two, and ten. Look at the cell with average two. Its backward change is one, but its forward change is eight. The centered average of those changes is four and a half. A line with total change four and a half would begin at negative one quarter, below both the cell's value two and its left neighbor's value one. The reconstruction has invented an undershoot while trying to fit the steep change toward ten.

This is exactly what a limiter should prevent.

## The minmod decision

One of the simplest slope limiters is called minmod, short for minimum modulus. Give it the backward and forward changes. If both have the same sign, it returns the one with smaller absolute magnitude. If their signs disagree, or one is zero, it returns zero.

For a smooth ramp, both differences equal one, so minmod returns one. The slope is retained. For our sequence zero, one, two, ten, the differences at the cell with average two are one and eight. Minmod selects one, not four and a half. Its reconstructed edge values become one and a half and two and a half. These lie within the bounds set by the neighboring averages.

At the top of a pulse, the backward difference is positive and the forward difference negative. Minmod returns zero, so the cell is reconstructed as flat. That sounds conservative in the everyday sense, and it is: there is insufficient local evidence for a slope that would not produce a new overshoot. Near an extremum, first-order behavior is often the price of avoiding spurious oscillations.

Minmod is not the only possible limiter. The monotonized central limiter, often abbreviated M C, considers a centered slope but clips it using bounds based on twice the one-sided differences. It can retain a somewhat steeper slope than minmod on smooth data while still preventing certain new extrema. Van Leer and superbee are other well-known choices, each with a different tradeoff between resolving sharp features and suppressing oscillations.

A limiter is not a universal spell that makes every numerical computation safe. Its guarantees depend on the equation, numerical flux, time integrator, and time step. We should understand the one-dimensional scalar setting before trusting a similar name in a nonlinear multidimensional or multi-equation simulation.

## From reconstructed lines to a time step

Reconstruction alone improves where we evaluate the spatial flux; it does not automatically improve time accuracy. If we compute a face flux from the initial reconstructed lines and then use only a first-order time update, the overall method need not be second order.

One approach is called MUSCL–Hancock. Start by reconstructing a limited line in each cell. Use the PDE to predict that cell's data forward by half a time step. Take the predicted left and right edge values at each face. Solve the local Riemann problem between those predicted states. Finally use the resulting fluxes to update the cell averages over the full time step.

Let's walk through the prediction for positive-speed linear advection, where the physical flux equals speed times state. Use speed one, cell width one, and time step one half. Then the Courant number is one half. In a region with cell averages increasing by exactly one from cell to cell, the limited change across each cell is one.

Consider a cell whose average is one. Its initial reconstructed edge values are one half and one and a half. Over half a time step, the profile translates to the right by one quarter of a cell width. The predicted cell-center value becomes three quarters. Its predicted right edge becomes one and a quarter. That is the state transported through the cell's right face at the midpoint of the time step.

The preceding cell on the same straight ramp has predicted right-edge value one quarter. The difference between the two successive face states remains exactly one. The conservative update subtracts the time-step factor one half times that flux difference. The average one becomes one half, precisely what translation of a unit-slope line by half a cell should produce.

This worked example does not prove second-order convergence for every profile; in fact first-order upwind also happens to translate a perfectly linear ramp exactly at its cell centers. But it shows the logic of reconstructing, predicting, and using a single shared flux. For curved smooth profiles, the benefit appears in higher-order error terms. For discontinuities, the limiter must keep the reconstructed states controlled.

For nonlinear Burgers flow, a similar half-step prediction uses the physical flux difference between the two reconstructed edges in a cell. The predicted states at a face then become the left and right data for our exact Burgers Riemann flux. The face can again contain a shock or rarefaction. The key difference from first-order Godunov is that the Riemann data reflect limited variation inside each cell, not just constant cell averages.

## A second route to accurate time integration

Rather than using a half-step Hancock predictor, we can use a semidiscrete finite-volume operator with the reconstructed Godunov flux and apply a suitable second-order Runge–Kutta method. One common choice computes a forward-Euler stage, recomputes all limited slopes and face fluxes at that stage, takes a second Euler-like stage, and averages it with the original state.

This is often called strong-stability-preserving Runge–Kutta of order two. The point is not that averaging two wrong answers magically repairs everything. Under the relevant forward-Euler stability property and a suitable time-step restriction, the staged method can inherit that property. We must recompute the nonlinear flux and limiter at each stage. Using the same frozen face flux twice would not amount to a genuine second-order evolution method.

Whichever time discretization we choose, the conservative part remains simple. For every face, calculate the flux once and use its negative contribution on one side and positive contribution on the other. Reconstructing a line changes the inputs to the flux but not the balance law.

## Measuring what the limiter is protecting

For a sequence of cell averages, total variation means adding the absolute differences between successive averages. A jagged sequence with repeated overshoots and undershoots has more variation than a single clean jump of the same height. A numerical method is called total-variation diminishing, or T V D, if that discrete sum does not increase from one accepted time level to the next, under the stated boundary and time-step conditions.

The simplest first-order monotone scalar schemes have this property under familiar CFL bounds. Properly designed limited high-resolution schemes can retain it while resolving smooth features more accurately. There is a limit to what a method can do: a globally linear monotone method cannot be higher than first order for general transport data, so high-resolution TVD methods become nonlinear through their limiters. Near sharp extrema they typically reduce order.

In a test, do not merely look at a picture and announce that the method is good. Check the sum of cell amounts for conservation. Track maximum and minimum values for spurious new extrema. Measure total variation where the TVD theory applies. For a smooth profile with known solution, refine the grid and estimate an error rate. For a discontinuity, watch how many cells the numerical front occupies and whether an overshoot appears. A method that passes one of these checks may still fail another.

The CFL number also needs attention. Our first-order Burgers Godunov flux used constant data in each cell. A MUSCL method uses reconstructed interface states that can reach somewhat different values. The characteristic speed for Burgers is the state itself, so a solver should estimate the allowable time step using appropriate evolved or reconstructed states and the restriction established for its temporal scheme. The formula for a positive constant advection speed is not a blanket theorem for every higher-order nonlinear method.

## Why this is a useful stopping point

We now have a complete ladder of ideas. Characteristic curves explain how smooth nonlinear transport steepens. Weak conservation laws permit jumps. Entropy selects a shock rather than a fictitious expansion shock. A Riemann problem turns two constant states into a meaningful interface flux. A first-order Godunov method uses that flux to update cell averages conservatively. Limited piecewise-linear reconstruction gives us a way to represent smooth variation without blindly creating oscillations near a front.

More sophisticated numerical conservation laws involve coupled fields, nonconvex fluxes, multidimensional geometry, and source terms. Those topics deserve their own foundations. But none changes the lesson of this scalar construction: mathematical information about wave direction and entropy must be built into the numerical interface rule, and higher accuracy must be checked against conservation and stability rather than assumed from a higher-degree formula.

The next time a numerical simulation shows a sharply moving front, we can ask informed questions. Is the front created by the PDE or by the grid? Does the method conserve the right quantity? Has it selected the entropy solution? Is the front smeared, oscillatory, or well resolved? And are we seeing a time-stepping error, a reconstruction error, or both? Those are practical questions rooted in the very first principles of the equation.

<!-- END SPOKEN LECTURE -->

## Mathematical companion: MUSCL reconstruction, limiting, and half-step evolution

For uniform cells of width \(h\) and average \(Q_i\), a piecewise-linear reconstruction is
\[
q_i(x)=Q_i+\sigma_i\frac{x-x_i}{h},\qquad
q_{i,L}=Q_i-\frac{\sigma_i}2,\quad q_{i,R}=Q_i+\frac{\sigma_i}2.
\]
The line has cell average \(Q_i\). Let \(\delta_-Q_i=Q_i-Q_{i-1}\) and \(\delta_+Q_i=Q_{i+1}-Q_i\). Define
\[
\minmod(a,b)=\begin{cases}\operatorname{sign}(a)\min(|a|,|b|),&ab>0,\\0,&ab\le0.\end{cases}
\quad\text{and}\quad \sigma_i=\minmod(\delta_-Q_i,\delta_+Q_i).
\]
For local averages \((0,1,2,10)\), the cell with average two has \((\delta_-,\delta_+)=(1,8)\). Centered slope \(\sigma=4.5\) gives reconstructed edges \((-0.25,4.25)\), while minmod gives \(\sigma=1\), edges \((1.5,2.5)\). For \((0,1,3,1,0)\), at the peak \(3\) the differences are \((2,-2)\), so \(\sigma=0\).

The monotonized-central (MC) option is
\[
\sigma_i^{\mathrm{MC}}=\minmod\left(2\delta_-Q_i,\frac{\delta_-Q_i+\delta_+Q_i}2,2\delta_+Q_i\right),
\]
where the three-argument minmod returns the smallest magnitude if all signs agree, and zero otherwise.

A scalar MUSCL–Hancock half-step predictor based on reconstructed edge fluxes takes
\[
Q_i^*=Q_i-\frac{\Delta t}{2h}\left[f(Q_i+\sigma_i/2)-f(Q_i-\sigma_i/2)\right].
\]
Then the predicted face states are \(Q_{i+1/2}^{L,*}=Q_i^*+\sigma_i/2\), \(Q_{i+1/2}^{R,*}=Q_{i+1}^*-\sigma_{i+1}/2\); compute \(\widehat F_{i+1/2}=G(Q_{i+1/2}^{L,*},Q_{i+1/2}^{R,*})\) with an entropy-consistent Riemann flux, and update \(Q_i^{n+1}=Q_i^n-(\Delta t/h)(\widehat F_{i+1/2}-\widehat F_{i-1/2})\). For linear advection \(f(q)=a q\), the predictor simplifies to \(Q_i^*=Q_i-(a\Delta t/(2h))\sigma_i\).

For \(a=1,h=1,\Delta t=1/2\) and a locally linear ramp \(Q_i=i\), we have \(\sigma_i=1\), \(Q_i^*=i-1/4\), and the predicted right face state \(i+1/4\). Consecutive positive-speed face fluxes differ by one; the conservative update gives \(Q_i^{n+1}=i-1/2\), consistent with exact translation of the linear profile.

An alternative semidiscrete approach sets \(L_i(Q)=-[\widehat F_{i+1/2}(Q)-\widehat F_{i-1/2}(Q)]/h\) and applies SSP RK2:
\[
Q^{(1)}=Q^n+\Delta t L(Q^n),\qquad
Q^{n+1}=\frac12Q^n+\frac12\bigl(Q^{(1)}+\Delta t L(Q^{(1)})\bigr).
\]
Recalculate slopes and fluxes at each stage. TVD and maximum-principle guarantees require suitable scalar fluxes, limiters, time discretizations, and CFL conditions; neither formula alone guarantees them for arbitrary systems.

### Exercises with worked answers

1. For averages \((0,1,2)\), reconstruct the middle cell with minmod. **Answer:** slope change one and edge values \(1/2\) and \(3/2\).
2. For averages \((0,1,2,10)\), why is the centered slope dangerous at the cell with average two? **Answer:** its reconstructed left edge is \(-1/4\), below neighboring values.
3. For averages \((1,4,2)\), what does minmod do in the middle cell? **Answer:** it returns zero at this local maximum.
4. For constant-speed advection with \(a=1\), \(h=1\), \(\Delta t=1/2\), \(Q_i=1\), and \(\sigma_i=1\), compute the MUSCL–Hancock predicted center and right edge. **Answer:** \(Q_i^*=3/4\), predicted right edge \(5/4\).
5. How can a limited scheme preserve total mass while adjusting slopes? **Answer:** each reconstructed cell line has the original cell average, and the update still uses a single shared flux on every interface.
6. What does TVD measure? **Answer:** the discrete sum of magnitudes of adjacent differences, not local truncation error or physical entropy.
7. Is a limiter alone sufficient to guarantee a stable high-order Burgers solver? **Answer:** no. The numerical flux, time discretization, boundary treatment, and CFL condition also matter.

### Sources and further reading

- [Ammar Hakim, *The MUSCL–Hancock Scheme for Solution of Hyperbolic Equations*](https://www.ammar-hakim.org/_static/files/1010-muscl-hancock.pdf).
- [Clawpack limiter documentation: minmod, MC, van Leer and superbee](https://www.clawpack.org/v5.13.x/pyclaw/evolve/limiters.html).
- [LeVeque, *Finite Volume Methods for Hyperbolic Problems*, Cambridge University Press](https://www.cambridge.org/core/books/abs/finite-volume-methods-for-hyperbolic-problems/finite-volume-methods/CB7B0A27A6D37AE3B906D4AE7C60A87E).
- [Wikipedia: MUSCL scheme](https://en.wikipedia.org/wiki/MUSCL_scheme).
