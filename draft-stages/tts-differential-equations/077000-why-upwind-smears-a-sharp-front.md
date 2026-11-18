# Why Upwind Smears a Sharp Front: Numerical Diffusion and Accuracy

<!-- BEGIN SPOKEN LECTURE -->

# Why Upwind Smears a Sharp Front

A stable numerical solution can still be wrong in a systematic way. Consider a sharp concentration front transported to the right. The exact solution has the same front, just farther downstream. But the donor-cell method replaces each cell value with an average of itself and its upstream neighbor. After many steps the abrupt transition becomes a broad ramp.

The method has not violated conservation. It may not have violated positivity or the stable time-step limit either. Its error comes from something more subtle: the repeated averaging acts as though we secretly added diffusion to an equation that only describes transport.

We can go beyond noticing that the plot looks blurry. Taylor series let us find the size of the extra diffusion. Then we can understand why one high-order alternative removes much of the smearing but can make new, negative concentrations appear near jumps. Finally, we will see why robust high-resolution methods often have to choose their behavior according to the solution itself.

## Error from a grid step, not from a physical process

Recall our basic transport equation. The time derivative of concentration plus a times the spatial derivative is zero, with positive constant speed a. The upwind update says the new concentration equals the old concentration minus C times the backward difference, where C is a times the time step divided by h.

Let us pretend, for a moment, that the stored grid values come from a very smooth function q of position and time. Expand the value one time step ahead with a Taylor series. It is the current value, plus the time step times the first time derivative, plus half the time step squared times the second time derivative, plus higher terms.

Do the same for the value one grid position to the left. That value is the current q minus h times the first spatial derivative plus half h squared times the second spatial derivative, and higher terms. Insert both expansions into the difference equation and divide by the time step.

The leading terms reproduce the advection equation, as they should. The next terms tell us how the grid equation deviates from the exact equation. They involve half the time step times the second time derivative and minus half a h times the second spatial derivative.

We can simplify because the exact advection equation tells us how derivatives are related. Differentiate the equation in time, and use the equation again for the spatial derivative of the time derivative. For a constant a, the second time derivative equals a squared times the second spatial derivative.

After substitution, the leading correction on the right-hand side is a h times one minus C, divided by two, multiplied by the second spatial derivative. That is precisely the form of a diffusion term. The number in front acts like an artificial diffusivity.

This is called a modified-equation calculation: instead of asking only how accurately one step approximates the intended PDE, we ask which nearby differential equation the numerical scheme follows to leading order. We must be clear about the approximation. It is a formal expansion for sufficiently smooth functions as h and the time step shrink together at a fixed Courant number. It is not an exact PDE satisfied by a discontinuous numerical profile. Nevertheless, it predicts the smearing that we observe.

## Measure the hidden diffusion

Suppose the speed is one meter per second, the cells are one tenth of a meter wide, and the Courant number is one half. Then the artificial diffusion coefficient is one times point one times point five, divided by two: point zero two five square meters per second.

There is no physical diffusion in the equation we meant to solve. A grid computation has supplied its own. If we halve the cell width while keeping the Courant number fixed, the artificial diffusivity halves. This is one reason a finer grid keeps a transported front sharper. It also shows a precise difference from heat-equation discretization, where the diffusion coefficient comes from the physical model and should not vanish under mesh refinement.

What does a diffusion coefficient do to a narrow profile? On the whole line, pure heat diffusion turns a concentrated pulse into a Gaussian whose variance grows at twice the diffusivity times elapsed time. The modified equation predicts a related broadening of a transported pulse as it moves. The center travels at speed a while the edges spread out.

There is also a discrete way to see the same number. With one upwind step and Courant number C, the update moves a fraction C of each cell's value one grid position to the right, leaving one minus C behind. As a distribution of grid-cell positions, each step resembles a random jump of one cell with probability C and no jump with probability one minus C. After many independent steps, the mean displacement is the number of steps times C h, exactly a times elapsed time. The positional variance is the number of steps times h squared times C times one minus C.

Divide that variance by the elapsed time. We get a h times one minus C, which is twice the artificial diffusivity found with Taylor series. The two calculations agree. We have measured the same spreading phenomenon from local derivative expansions and from repeated averaging.

The random-walk comparison is a mathematical representation of the update coefficients, not a claim that dye molecules are truly taking random one-cell jumps. The real model deliberately excluded diffusion. This is computational spreading, generated by how we represent continuous movement on a fixed grid.

## Why the Courant number one case looks special

Our artificial diffusion coefficient contains the factor one minus C. At C equal to one, that coefficient vanishes. We saw why: every cell's concentration simply shifts into the next cell. On a periodic uniform grid with constant speed, the numerical translation then agrees exactly with the exact translation at the sampled times.

At C equal to one half, each step mixes two cells. Repeating the operation produces binomial weights spreading across a growing range of cells. At very small Courant numbers, each update only moves a tiny fraction, but we must take many more steps to cover the same physical time. The total spreading does not vanish by taking delta t toward zero at fixed h. The modified-equation diffusivity approaches a h divided by two. Only reducing the spatial grid width removes the leading artificial diffusion.

These are useful design facts. A time-step refinement experiment at fixed spatial resolution is not necessarily a test of spatial transport accuracy. Once the time-integration error is small, the grid itself can be the main source of blur.

## Can a more accurate formula preserve sharp fronts?

There is a natural way to try to improve the method. Instead of using only the value behind a cell, take more nearby points and use Taylor's formula in time. The advection equation converts time derivatives into spatial derivatives. A second-order time expansion uses both the first spatial derivative and the second spatial derivative.

Approximate the first spatial derivative with a centered difference and the second derivative with the usual three-point centered difference. This gives the Lax–Wendroff method for constant-speed advection. On a smooth solution, its local truncation error is higher order than basic upwind. It transports smooth waves with less leading-order diffusion.

But now return to our six-cell pulse: zero, zero, one, one, zero, zero. With Courant number one half, a single Lax–Wendroff step gives zero, negative point one two five, point six two five, one point one two five, point three seven five, zero. Add them and the total remains two. But notice the negative dip ahead of one front and the overshoot above one at the other.

The method has improved its formal accuracy for smooth profiles at the expense of new extrema near this jump. Those extrema are not physical for exact passive transport of a profile constrained between zero and one. They are oscillatory approximation errors associated with representing a discontinuity using a higher-order linear stencil.

Does this make Lax–Wendroff unstable? No. For constant-speed linear advection on a periodic grid, its Fourier amplification factors have magnitude at most one in the standard Courant range between negative one and one. Stability in a norm does not imply positivity or a bound on local overshoots. We must keep those concepts separate. Lax–Wendroff can be stable and second-order accurate on smooth data while still ringing near discontinuities.

## Monotonicity, total variation, and the limitation of linear schemes

We need vocabulary for the visual problem. A numerical update is monotone if increasing its input values cannot decrease any of the updated values, with the usual componentwise interpretation. The stable donor-cell update is monotone because its coefficients are nonnegative. A monotone conservative update cannot invent new extremes from bounded input data.

Another measure is total variation: add the absolute change in concentration from each cell to the next. A rectangular pulse has variation concentrated at its two edges. A scheme that generates alternating overshoots and undershoots creates extra variation. The stable first-order upwind scheme does not increase total variation on a periodic grid.

There is a fundamental obstacle, often called Godunov's order barrier. For a linear, translation-invariant scheme for scalar advection, monotonicity under the appropriate assumptions rules out achieving more than first-order accuracy in general. A linear high-order rule cannot simultaneously remain monotone for every possible profile. We should not expect a clever fixed set of weights to provide a universal solution.

This theorem does not say that all accurate methods must produce terrible ringing. It says that if we want high accuracy in smooth regions and robust behavior near fronts, we generally need a scheme whose coefficients adapt to the data. High-resolution methods use nonlinear reconstructions or flux limiters to reduce risky corrections near steep changes while retaining more accuracy where the solution is smooth.

One elementary idea is to estimate the slope in a cell from the neighboring differences. If both differences have the same sign, their smaller magnitude can serve as a cautious slope. If the signs disagree, set the slope to zero. This is called a minmod limiter. It prevents a reconstructed line from introducing a new peak inside a cell when the data already look like a local extremum.

Combining reconstruction, interface fluxes, and a suitable time integrator can produce a method that is more accurate in smooth monotone regions while controlling oscillations. The details matter: merely adding a limiter to an arbitrary forward-Euler update is not enough to guarantee all desired properties. The stability conditions depend on the full space-and-time method.

## What accuracy means for a moving discontinuity

For a smooth wave, we can measure error by comparing the numerical values to an exact translated sine wave and watch how the error decreases as the grid is refined. A second-order scheme can show faster convergence than a first-order one in this setting, provided its hypotheses hold and the time step is refined consistently.

For a step, there is no smooth derivative at the front. A Taylor expansion based on derivatives at that point cannot justify the same convergence rate. Instead, compare the integral difference of the profiles, the location of the main transition, and the total mass. Different error norms respond differently to a narrow layer of smearing or a small overshoot.

This is why a scheme's formal order is not the full story. It is useful information about smooth solutions, not a certificate that a discontinuity will be reproduced without artifacts. The physical model may actually contain a shock, a contact discontinuity, or a boundary layer. Then we need discrete conservation and an appropriate admissibility property in addition to smooth-data accuracy.

We can now diagnose three distinct outcomes for numerical transport. A scheme that changes the total amount has a conservation error. A scheme that amplifies oscillations on refinement has a stability problem. A conservative stable scheme that broadens a sharp front has numerical diffusion. A method that avoids that broadening but overshoots near the front may have a monotonicity problem even when it is stable.

The next computational step is to derive the update directly from conservation over individual cells. That viewpoint makes mass bookkeeping exact by construction and gives us a natural place—each cell face—to choose an upwind flux, a high-resolution flux, or eventually a flux for nonlinear waves. Instead of treating conservation as a property we hope our finite differences happen to possess, we can make it the organizing principle of the algorithm.

<!-- END SPOKEN LECTURE -->

## Mathematical companion: modified equation and high-order tradeoff

For \(a>0\), the upwind difference equation is
\[
\frac{Q_i^{n+1}-Q_i^n}{\Delta t}+a\frac{Q_i^n-Q_{i-1}^n}{h}=0,\quad C=\frac{a\Delta t}{h}.
\]
Insert a smooth exact \(q(x,t)\):
\[
q_t+\frac{\Delta t}{2}q_{tt}+a q_x-\frac{a h}{2}q_{xx}
   +O(\Delta t^2+h^2)=0.
\]
Using \(q_{tt}=a^2q_{xx}\) at leading order gives the modified equation
\[
q_t+a q_x=D_{\mathrm{num}}q_{xx}+O(h^2),\qquad
D_{\mathrm{num}}=\frac{a h}{2}(1-C),\qquad \Delta t=O(h).
\]
At \(a=1\,\mathrm{m/s},h=0.1\,\mathrm m,C=0.5\), \(D_{\mathrm{num}}=0.025\,\mathrm{m^2/s}\). This leading-order expansion applies to smooth solutions under fixed-C refinement, not as an exact identity at discontinuities.

Binomial averaging provides a second derivation: an upwind update acts as a shift of \(h\) with weight \(C\) and a shift of \(0\) with weight \(1-C\). After \(n\) steps the mean is \(n Ch=a n\Delta t\) and the variance is \(n h^2 C(1-C)\). Hence
\[
\frac{\mathrm{Var}}{n\Delta t}=a h(1-C)=2D_{\mathrm{num}}.
\]

For smooth functions, the Lax–Wendroff update is
\[
Q_i^{n+1}=Q_i^n-\frac C2(Q_{i+1}^n-Q_{i-1}^n)
+\frac{C^2}{2}(Q_{i+1}^n-2Q_i^n+Q_{i-1}^n).
\]
Its Fourier amplification factor is \(G=1-\mathrm{i}C\sin\theta+C^2(\cos\theta-1)\), and
\[
|G|^2=1-4C^2(1-C^2)\sin^4(\theta/2)\le1\quad (|C|\le1).
\]
At \(C=1/2\) and periodic \((0,0,1,1,0,0)\), the step is \((0,-1/8,5/8,9/8,3/8,0)\): conservative and stable but non-monotone.

Minmod for two real arguments is
\[
\operatorname{minmod}(r,s)=\begin{cases}
\min(r,s),& r,s>0,\\
\max(r,s),&r,s<0,\\
0,&rs\le0.
\end{cases}
\]
A slope \(\sigma_i=\operatorname{minmod}((Q_i-Q_{i-1})/h,(Q_{i+1}-Q_i)/h)\) is zero at a discrete extremum; higher-resolution finite-volume methods combine such reconstruction with appropriate numerical fluxes and time integration.

### Exercises with worked answers

1. If \(a=2\), \(h=0.04\), \(C=0.75\), what is \(D_{\mathrm{num}}\)? **Answer:** \(D=2(0.04)(0.25)/2=0.01\).
2. At fixed \(C\) and smooth data, how does \(D_{\mathrm{num}}\) change when \(h\) is halved? **Answer:** it halves.
3. Explain why taking \(\Delta t\to0\) at fixed \(h\) does not remove all upwind smearing. **Answer:** \(C\to0\) and \(D_{\mathrm{num}}\to ah/2\); the spatial upwind error remains.
4. Compute the Lax–Wendroff step for the six-cell pulse at \(C=1/2\). **Answer:** \((0,-1/8,5/8,9/8,3/8,0)\), sum \(2\), with negative and over-one values.
5. Does \(|G|\le1\) for all Fourier modes imply positivity? **Answer:** no; Lax–Wendroff provides a counterexample near a jump.

### Sources and further reading

- [Randall J. LeVeque, *Finite Volume Methods for Hyperbolic Problems* (2002)](https://www.cambridge.org/core/books/abs/finite-volume-methods-for-hyperbolic-problems/finite-volume-methods/CB7B0A27A6D37AE3B906D4AE7C60A87E).
- [Berkeley Math 228B, Finite Difference Methods for PDEs](https://persson.berkeley.edu/math228b/html/finite_difference_methods_for_PDEs.html).
- [Berkeley Math 228B, Finite Difference Methods for PDEs](https://persson.berkeley.edu/math228b/html/finite_difference_methods_for_PDEs.html).
