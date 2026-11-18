# Upwind Steps and the CFL Limit: Following Information Across a Grid

<!-- BEGIN SPOKEN LECTURE -->

# Upwind Steps and the CFL Limit

A mathematical pulse can shift three tenths of a meter to the right without changing shape. A computer grid cannot move one of its stored values three tenths of a cell. It has a list of numbers, one at each grid location or one average in each cell, and it must calculate a new list after each time step. How should it decide which numbers to mix?

We will begin with the simplest transport equation: concentration moves to the right at a positive constant speed a. We will derive an update rule from the direction of the flow and also from the amount crossing each cell face. Then we will calculate a whole time step on six cells, discover an exact special case, and see both the usefulness and the limits of the Courant–Friedrichs–Lewy condition.

## A derivative that looks toward the source

Let the grid spacing be h and the time step be delta t. The advection equation says the time derivative of q equals negative a times its spatial derivative. We know how to approximate the time derivative: the change from the current time to the next, divided by delta t.

For the spatial derivative, which neighboring value should we use? If a is positive, information at position x has arrived from a point to its left. We should therefore approximate the spatial derivative by the current value minus the value at the point immediately to the left, divided by h. This is a backward spatial difference. It does not mean we are integrating backward in time. It means we sample upstream in space.

Substituting those two differences into the equation gives a simple rule. The new concentration in cell i equals its current concentration minus the speed times the time step divided by h, multiplied by the difference between its concentration and that of the cell on the left.

Let C denote that ratio: speed times delta t divided by h. Reorganizing the update, the new value is one minus C times the old value in the cell, plus C times the old value in the cell to the left. It is a weighted average. The upstream neighbor donates a fraction C of what moves into the cell; the cell retains the fraction one minus C of its prior value.

This formula is the first-order upwind method, also called the donor-cell method. We can derive exactly the same rule by treating each stored number as the average amount in a cell. During a short time interval, fluid travels a distance a times delta t. If that distance is less than one cell width, a fraction C of one cell's contents passes through its right face. The new average is the part retained from the present cell plus the part arriving from upstream. This finite-volume interpretation explains why the weights are what they are rather than merely presenting them as an algebraic trick.

## The Courant number has a physical meaning

The number C has no units. It is a distance traveled during one time step divided by the spatial cell width. If C equals one quarter, a characteristic moves one quarter of a cell width during one step. If C equals one, a characteristic moves exactly one full cell width. If C equals two, the physical solution moves across two cells during the time in which our numerical stencil consults only the immediate neighbor.

The classical CFL requirement arises from this mismatch between a continuous domain of dependence and a discrete one. For this explicit one-cell upwind scheme, the safe range is C between zero and one. In that range, one minus C and C are nonnegative and sum to one. Every updated value is therefore between the two old values it mixes. A nonnegative concentration cannot become negative because of the update, and the method cannot invent a new value larger than the maximum already present.

The conclusion depends on the scheme. The CFL idea is that the numerical domain of dependence must be wide enough to contain the physical one as the grid is refined. It is a necessary design principle for an explicit local scheme, not a general promise that every scheme satisfying an inequality is stable. We will see a centered spatial discretization fail for any positive time step, even while the same Courant number looks perfectly acceptable for upwind.

## Six cells and one transported pulse

Take six equal cells on a periodic channel. Imagine their concentration averages are zero, zero, one, one, zero, zero. There are two units of cell-width-weighted concentration in this pulse. Choose C equal to one half.

The first cell sees a zero to its left, so it remains zero. The second also remains zero. The third initially holds one and receives from a zero neighbor; half its amount remains, so its new value is one half. The fourth initially holds one and receives from the third cell, which also held one, so its new value stays one. The fifth initially holds zero, but its upstream neighbor held one, so it becomes one half. The sixth remains zero.

The new list is zero, zero, one half, one, one half, zero. The sum is still two. The shape has spread over three cells, but the total is preserved. If we take another half-cell step, the central values mix again and the front spreads further. That spreading is a real numerical error—pure transport does not physically smear the pulse—but the calculation has kept the concentration nonnegative and has not created or destroyed any mass.

There is a revealing special case. Set C equal to one. Then the weight on the old value in the present cell vanishes and the weight on the upstream value becomes one. The new value in cell i is exactly the old value in cell i minus one. On a periodic uniform grid, this is an exact shift by one cell per time step for the stored cell averages. Although the upwind method is generally first-order accurate, here its movement exactly matches the grid geometry and there is no extra smoothing of the represented profile.

Now try C equal to one point two. This means the physical pulse travels farther than one cell width during a single update, but our formula still looks back only one cell. On the same initial pulse, the third cell becomes negative point two, the fourth stays one, and the fifth becomes one point two. The total is still two, yet the method has produced a negative concentration and an overshoot above the original maximum.

Conservation, by itself, did not prevent a bad answer. The update had exchanged some mass in a way that preserved its sum while violating the expected bounds. This is why a solver needs several distinct checks: conservation, stability, and accuracy.

## What if the speed is negative?

Now reverse the direction of the flow. A negative speed means a point at x receives its information from positions to the right. The appropriate spatial difference uses the value on the right minus the current value, divided by h. Define a nonnegative Courant number using the absolute value of the speed. The new value is one minus this number times the old value in the cell, plus the number times the value in the cell to the right.

The stable interval is again between zero and one. The change is which side donates information. A robust implementation must choose its upstream side from the sign of the velocity, not from the order in which the grid happens to be stored in memory.

On an open domain, boundary values matter only on the inflow side. For positive speed, the first cell receives contributions from a prescribed left boundary concentration. The value leaving the last cell is determined by its interior state. On a periodic grid, the first cell reads the last cell as its left neighbor. In either case, the rule must handle the boundary consistently with characteristic direction.

## Why using a centered difference can fail

A centered spatial difference looks attractive because it estimates a spatial derivative more accurately for smooth functions. It uses the value on the right minus the value on the left, divided by twice h. Combined with forward Euler in time, the transport update becomes the old value minus half the Courant number times the right-left difference.

At first glance, symmetric neighbors seem fairer than a one-sided neighbor. But pure transport is not symmetric in space. It has a direction. For the six-cell pulse and Courant number one half, the centered update immediately produces a negative point two five in the cell just before the left front and one point two five at the cell just after it. Values below zero and above one have appeared. Total mass is still preserved on the periodic grid because the centered differences telescope, but these new extrema are unphysical for exact constant-speed translation.

A small overshoot does not by itself establish that repeated steps will become unstable. To prove that, we can investigate a single oscillatory grid pattern. Imagine a Fourier mode whose value from one cell to the next rotates by a fixed phase angle. The centered spatial difference produces an imaginary multiple of that mode. Forward Euler then multiplies its amplitude by a complex number whose real part is one and whose imaginary part is proportional to the Courant number times the sine of the phase angle.

For any nonzero Courant number and any mode with nonzero sine of its phase angle, the magnitude of that multiplier is strictly greater than one. Repeated steps amplify the mode. The forward-time centered-space scheme for constant-speed advection is therefore unstable under grid refinement; simply taking the time step smaller while retaining the scheme does not give it the stable weighted-average structure of upwind. On some particular tiny grids a few exceptional modes may not reveal the problem, but the method has no stable all-wavelength limit.

The lesson is not that centered spatial derivatives are always bad. We used them successfully for the heat equation, where the second derivative produces diffusive damping. Here the combination of a centered first derivative with forward Euler gives oscillations without a counteracting damping mechanism. The direction and type of the underlying differential equation matter.

## A stability proof we can understand without Fourier transforms

Let us return to upwind with C between zero and one. Suppose two different initial grid profiles differ by a small error in each cell. Evolve both with the same scheme. Their difference obeys exactly the same weighted-average update.

At each cell, the absolute error after a step is no larger than one minus C times the previous absolute error in that cell plus C times the previous absolute error in its upstream neighbor. Sum these inequalities over a periodic grid. Because every cell appears once in each sum, the total absolute error cannot increase. This is an ell-one contraction: a measurement of total cellwise discrepancy that is natural for conservation laws.

The proof also shows why an error cannot spontaneously become huge under stable donor-cell advection. It does not say the error is zero. A sharp front is smeared by repeated averaging; the method can be stable and conservative while still having visible truncation error. That distinction is essential for evaluating numerical results.

On a periodic grid the sum of the updated concentrations equals the sum of the old concentrations, because the upstream contributions are just a rearrangement of the same cell values. With a nonperiodic boundary, the sum changes by the net inflow minus outflow. Neither calculation requires the solution to be smooth. These are structural properties of the numerical rule.

## What a good grid experiment should show

If you implement this scheme, begin with a smooth wave and with a rectangular pulse. Try Courant numbers one quarter, one half, one, and one point two. For the smooth wave, measure how much the shape changes after one trip around a periodic domain. For the pulse, check the minimum and maximum values and the total sum times the cell width.

You should find a tradeoff. In the stable range, the upwind method carries information in the correct direction and conserves the total. Except at the special one-cell-shift case, it tends to smooth the profile. Above the stable range, it may overshoot and eventually amplify oscillations. The centered Euler scheme preserves the sum but lacks the stability required to be useful.

These observations lead to a deeper question. If the original PDE contains no physical diffusion, why does a stable upwind scheme smooth the profile? It is not merely a visual artifact. Taylor expansion shows that the discrete method behaves, to leading order, like a transport equation with an additional diffusion term. Deriving that hidden diffusion will give us a quantitative measure of how much accuracy the robust update has purchased at the price of smoothing.

<!-- END SPOKEN LECTURE -->

## Mathematical companion: donor-cell stability and centered instability

For \(q_t+a q_x=0\), with \(a>0\), set \(C=a\Delta t/h\). The upwind update is
\[
Q_i^{n+1}=Q_i^n-C(Q_i^n-Q_{i-1}^n)=(1-C)Q_i^n+C Q_{i-1}^n.
\]
For \(a<0\), write \(C=|a|\Delta t/h\) and use \(Q_i^{n+1}=(1-C)Q_i^n+C Q_{i+1}^n\). If \(0\le C\le1\), both are convex combinations, preserve positivity, and contract periodic \(\ell^\infty\) and \(\ell^1\) differences.

On a periodic mesh with \(Q^0=(0,0,1,1,0,0)\),
\[
\begin{array}{c|c}
C&Q^1\\\hline
1/2&(0,0,1/2,1,1/2,0)\\
1&(0,0,0,1,1,0)\\
6/5&(0,0,-1/5,1,6/5,0)
\end{array}
\]
In each row \(\sum_i Q_i^1=\sum_i Q_i^0=2\). This is conservation, not a proof of stability.

For forward Euler with a centered first difference,
\[
Q_i^{n+1}=Q_i^n-\frac C2(Q_{i+1}^n-Q_{i-1}^n).
\]
Insert \(Q_i^n=G^n e^{\mathrm{i} i\theta}\). Then
\[
G(\theta)=1-\mathrm{i}C\sin\theta,\qquad |G(\theta)|^2=1+C^2\sin^2\theta>1
\]
for \(C\ne0\) and \(\sin\theta\ne0\). By contrast, upwind has
\[
G_{\rm up}(\theta)=(1-C)+C e^{-\mathrm{i}\theta},\quad
|G_{\rm up}|^2=1-2C(1-C)(1-\cos\theta)\le1
\]
for \(0\le C\le1\). On a six-cell periodic grid, centered Euler with \(C=1/2\) and the same pulse yields \((0,-1/4,3/4,5/4,1/4,0)\).

For two upwind solutions \(U,V\), writing \(E_i=U_i-V_i\) gives
\[
\sum_i|E_i^{n+1}|\le(1-C)\sum_i|E_i^n|+C\sum_i|E_{i-1}^n|=\sum_i|E_i^n|.
\]
The result is periodic, or applies with matching boundary data and an appropriate domain boundary-error accounting.

### Exercises with worked answers

1. With \(a=2\), \(h=0.1\) and \(\Delta t=0.03\), compute \(C\). **Answer:** \(0.6\), within the donor-cell stable range.
2. Repeat with \(\Delta t=0.06\). **Answer:** \(C=1.2\); positivity and monotonicity no longer follow, and some modes grow.
3. For positive speed and periodic \(Q^0=(2,0,0,0)\), what is one upwind step with \(C=1/4\)? **Answer:** \((1.5,0.5,0,0)\).
4. Why is mass conservation not enough to guarantee a reliable scheme? **Answer:** centered Euler conserves the sum on a periodic mesh but amplifies Fourier modes and creates undershoots/overshoots.
5. Show that upwind at \(C=1\) exactly shifts the represented cell averages by one cell. **Answer:** the coefficient of \(Q_i\) becomes zero and the update is \(Q_i^{n+1}=Q_{i-1}^n\).

### Sources and further reading

- [LeVeque, *Finite Volume Methods for Hyperbolic Problems*, Cambridge University Press (2002)](https://www.cambridge.org/core/books/abs/finite-volume-methods-for-hyperbolic-problems/finite-volume-methods/CB7B0A27A6D37AE3B906D4AE7C60A87E).
- [Berkeley Math 228B, Finite Difference Methods for PDEs](https://persson.berkeley.edu/math228b/html/finite_difference_methods_for_PDEs.html).
- [Berkeley Math 228B, Finite Difference Methods for PDEs](https://persson.berkeley.edu/math228b/html/finite_difference_methods_for_PDEs.html).
