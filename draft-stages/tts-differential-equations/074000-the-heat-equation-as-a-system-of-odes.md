# The Heat Equation as a System of ODEs: Method of Lines, Stability, and Error

<!-- BEGIN SPOKEN LECTURE -->

# The Heat Equation as a System of ODEs

A differential equation describing temperature depends on both position and time. We have already learned one way to solve it: express the temperature as a sum of spatial sine modes, with a separate exponential decay for each mode. We have also learned numerical ways to solve ordinary differential equations when no exact formula is available. Can we combine those two sets of tools?

Yes. Instead of approximating the entire space-time surface at once, first place a finite number of grid points along the rod. Approximate the spatial derivatives, but leave time continuous. Each grid temperature becomes a function of time. The partial differential equation has turned into a system of ordinary differential equations. This approach is called the method of lines.

We will use the simplest model that still exhibits the central difficulty: one-dimensional heat diffusion with fixed zero temperatures at the ends. We will compute an explicit time step by hand, derive a stability limit using both convex averages and discrete Fourier modes, and see why refining the spatial mesh forces an explicit solver to take smaller time steps. Then we will try an implicit step and compare the two sources of approximation error.

## A grid of temperatures that changes in time

Let the rod occupy the interval from zero to one, and let the diffusion coefficient be kappa, a positive number. The heat equation says that the time derivative of temperature equals kappa times its second spatial derivative. Fix the temperatures at both ends to zero. Choose a grid spacing h equal to one quarter. There are three unknown interior temperatures, located at one quarter, one half, and three quarters.

Call the three unknowns U one, U two, and U three. Each is now a function of time. The second derivative at an interior grid point is approximated by the temperature to the left minus twice the temperature at the point plus the temperature to the right, divided by h squared. At the endpoints, the neighboring values are the prescribed zeros.

In vector form, our system says U prime equals kappa times A sub h times U, where A sub h is the tridiagonal matrix derived from centered second differences. We know how to solve such a system exactly in principle: U of t equals the matrix exponential of kappa A sub h t applied to the initial vector. In a larger problem, we need not actually compute that exponential. We can apply an ODE integrator to the vector system.

This is an important modeling boundary. The unknowns are still approximate temperatures at positions along a continuous rod. Solving the vector ODE exactly would remove time-integration error but not the error from replacing spatial derivatives by finite differences. We have two approximations that should be evaluated separately.

## Forward Euler gives an averaging rule

Apply forward Euler with time step delta t. Take the current temperature vector, evaluate kappa A sub h times that vector, and multiply by delta t to predict the next vector. At a single interior grid point, the formula uses three current values: left neighbor, center, and right neighbor.

Define r to be kappa times delta t divided by h squared. The next temperature equals r times the current left value, plus one minus two r times the current center value, plus r times the current right value. This is called forward in time, centered in space. The abbreviation is sometimes F T C S.

Here is the first stability insight, and it does not require eigenvalues. When r lies between zero and one half, all three weights are nonnegative and add to one. The next temperature is then a convex average of the neighboring and current values. It cannot be higher than the largest of those three values or lower than the smallest. With boundary values zero, this also gives a discrete maximum principle relative to the temperatures and boundaries already present.

Choose kappa equal to one, h equal to one quarter, and delta t equal to point zero two. Then h squared is one sixteenth, so r is point three two. Suppose the initial interior temperatures are zero, one, zero: only the center sensor reports a unit temperature. After one Euler step, the vector is point three two, point three six, point three two. The central temperature has fallen, and its neighbors have warmed. The pattern is exactly what we expect diffusion to do.

Take another step using those new values. The two outer temperatures become point two three zero four, and the center becomes point three three four four. Heat has spread toward the boundaries, where energy can leave because those temperatures are held at zero. Even this three-variable calculation shows the mechanism of diffusion, the role of boundary conditions, and the influence of the time-step parameter.

## What goes wrong when the time step is too large?

Keep the same spatial grid and diffusion coefficient, but increase delta t to point zero four. Then r becomes point six four. The center weight, one minus two r, is now negative. Starting again from zero, one, zero, the first Euler step gives point six four, negative point two eight, point six four.

The exact heat equation cannot make a nonnegative initial temperature negative under these boundary conditions. The numerical method has produced an artificial negative temperature at the center. A second step produces roughly negative point three five eight four, point eight nine seven six, negative point three five eight four. The grid has begun to alternate wildly, even though the true solution is smoothing out.

One pathological step does not by itself prove a numerical sequence diverges forever; we should identify the unstable mode. The discrete second-derivative matrix has negative eigenvalues. Applying Euler to an eigenvector with eigenvalue lambda multiplies its amplitude by one plus kappa delta t times lambda. An exact heat mode instead multiplies by e to the kappa lambda delta t, which lies between zero and one for negative lambda and positive time.

Euler's multiplier can cross below negative one if delta t is too large relative to the magnitude of the most negative eigenvalue. Then that mode alternates sign and grows in magnitude from step to step. On our three-interior-point grid, delta t equal to point zero four is large enough to make the highest discrete sine mode unstable. Because the initial center pulse excites that mode, the numerical oscillation does not disappear on its own.

The commonly used mesh-independent sufficient condition for this one-dimensional explicit heat scheme is r less than or equal to one half. The convex-average argument already established a strong positivity and maximum-preserving property under that condition. The discrete frequency analysis confirms stability for every wavelength on an arbitrarily fine uniform grid when r stays in that range. For one fixed, finite Dirichlet grid, the exact spectral threshold can be slightly above one half, but one half is a clean safe bound that remains valid under refinement.

## Why finer spatial resolution can make the solver slower

Suppose we keep the physical rod and diffusion constant unchanged but halve h. The centered second derivative now has a denominator h squared that is four times smaller. To keep r at the same safe value, the time step must also be divided by four. In one spatial dimension, halving h roughly doubles the number of interior unknowns and requires about four times as many explicit time steps to reach the same final time. The total work can therefore grow by about a factor of eight, even before considering overhead.

This scaling sometimes surprises students. Better spatial resolution sounds as though it should simply improve an answer. It does improve the ability to resolve spatial features, but it also introduces high-frequency grid modes that decay extremely rapidly. An explicit integrator must avoid numerically amplifying those modes. The restriction comes from stability, not necessarily from the rate at which the physically interesting, smooth solution is changing.

The same difficulty appeared earlier in stiff ordinary differential equations. Here stiffness emerges naturally when a PDE is discretized in space. That connects two subjects we have been studying separately: the negative eigenvalues of the discrete Laplacian and the stability region of an ODE solver.

## Backward Euler trades a restriction for a solve

Try backward Euler instead. Rather than evaluating the spatial second difference at the current time, evaluate it at the next time. In the vector equation, this gives next U minus current U divided by delta t equal to kappa A sub h times next U. Rearrange the terms. We must solve a linear system with matrix identity minus kappa delta t A sub h to obtain the new temperature vector.

The matrix is tridiagonal and, with zero Dirichlet boundary values, symmetric positive definite. Its solve is computational work, but the payoff is a better stability property. On a discrete eigenmode with negative eigenvalue lambda, backward Euler multiplies by one divided by one minus kappa delta t lambda. That is positive and no greater than one for every positive delta t. There is no counterpart of forward Euler's diffusion stability restriction.

Do not mistake unconditional linear stability for unconditional accuracy. If the exact decay factor over a step is e to the negative ten, backward Euler gives one over eleven. Both decrease the amplitude, but their numerical values are very different. Backward Euler avoids exploding on a stiff decay mode; that does not mean it resolves the mode's exact history with a giant step.

For the three-temperature example, choosing r equal to one solves a tridiagonal system at each step. The new central value does not come from a single weighted average using only current temperatures. It depends on the unknown new neighbor values as well. This simultaneous coupling is the computational price of the implicit method. Efficient linear algebra—sparse factorization, iterative solvers, and preconditioning—becomes important for large grids and multiple spatial dimensions.

## Spatial and temporal error are different questions

Return to the smooth heat equation. The centered second-difference approximation of the spatial second derivative has error proportional to h squared. Forward Euler's time difference has leading local derivative error proportional to delta t. Put them into the original PDE and, for a sufficiently smooth solution, the residual in the discrete equation is of order delta t plus h squared.

This is a consistency statement. It tells us that the numerical equation approaches the differential equation as h and delta t go to zero. It does not, by itself, guarantee the computed solution will approach the true solution. We also need a stability estimate preventing small local defects from being amplified without bound. Under the forward Euler restriction and appropriate regularity and compatibility assumptions, the heat scheme has a fixed-time global error bounded by a constant times delta t plus h squared in the maximum norm.

A useful way to understand the error proof is to insert the exact solution sampled on the grid into one numerical step. The mismatch is a small local defect, of size about delta t times the sum of delta t and h squared. The next step transports the previous error through a stable averaging matrix and adds one more defect. After roughly final time divided by delta t steps, those defects accumulate to a global error of order delta t plus h squared. This is the same local-versus-global distinction we learned in numerical ODEs, now with a spatial error added.

If we keep r constant while refining the grid, then delta t is proportional to h squared. Both error contributions are consequently of order h squared. In that regime, halving h should make the leading error about one quarter as large on a sufficiently smooth test problem, after reaching the asymptotic range. A much rougher initial profile or an unresolved boundary layer may show a different observed rate until the mesh is fine enough.

It is worth verifying the two components separately. Hold h fixed and reduce delta t to test time integration against the exact semidiscrete matrix solution. Hold delta t sufficiently small and refine h to test the spatial approximation against a known PDE solution. If we change both at once without recording their relation, an observed error reduction does not tell us which approximation was responsible.

## One exact mode as a benchmark

A particularly convenient benchmark is the initial temperature sin of pi x on the unit interval, with zero endpoint temperatures. The exact PDE solution is that same sine profile multiplied by e to the negative kappa pi squared t. Every time step should preserve the shape of that first sine mode on the grid, changing only its amplitude.

The discrete second-derivative matrix also has the sampled first sine profile as an eigenvector, but its eigenvalue is not exactly negative pi squared. Forward Euler multiplies that vector by one plus kappa delta t times the discrete eigenvalue at each step. This shows the two errors plainly: the discrete eigenvalue differs from the continuous eigenvalue because of spatial approximation, and the Euler factor differs from the exponential of the discrete eigenvalue because of time approximation.

A trustworthy solver can be checked against this one-mode calculation before we feed it more complicated initial conditions. It provides a numerical answer, a known exact PDE answer, and a predicted effect of refining both the spatial and temporal grids. It also makes clear why a smooth low-frequency solution may look reasonable even with a time step that is dangerous for high-frequency grid noise. Stability is a property of the method across the modes it may encounter, not merely a flattering plot of one initial condition.

We now have a complete bridge from continuous PDE mathematics to numerical integration. A spatial derivative becomes a sparse matrix. A PDE becomes a vector ODE. An ODE time step becomes an update rule for temperatures. Matrix eigenvalues explain time-step restrictions; an energy or maximum principle helps control errors; and refinement reveals how closely the numerical solution approaches the physical model. The advanced algorithms for diffusion, fluids, and waves differ in important ways, but they build on these same decisions: what to approximate in space, what to advance in time, which properties to preserve, and how to separate consistency from stability.

<!-- END SPOKEN LECTURE -->

## Mathematical companion: method of lines and stability

For \(u_t=\kappa u_{xx}\) on \((0,1)\), homogeneous Dirichlet boundary data and a uniform grid \(x_i=ih\), the semidiscrete method of lines is
\[
\frac{d\mathbf U}{dt}=\kappa A_h\mathbf U,\qquad
(A_hU)_i=\frac{U_{i-1}-2U_i+U_{i+1}}{h^2}.
\]
For inhomogeneous boundary values, add their known contributions to a forcing vector. Forward Euler is
\[
U_i^{n+1}=rU_{i-1}^n+(1-2r)U_i^n+rU_{i+1}^n,
\qquad r=\frac{\kappa\Delta t}{h^2}.
\]
For \(0\le r\le1/2\), the update coefficients are nonnegative and sum to one (including boundary values), implying a maximum-principle bound.

On a periodic or infinite uniform grid, a Fourier mode \(e^{ikih}\) has Euler amplification factor
\[
G(k)=1-4r\sin^2(kh/2).
\]
The condition \(|G(k)|\le1\) for all modes is equivalent to \(r\le1/2\). On an \(N\)-subinterval homogeneous Dirichlet mesh, the exact condition for spectral stability is \(r\le [2\sin^2((N-1)\pi/(2N))]^{-1}\), slightly larger than \(1/2\), while \(r\le1/2\) is the standard uniform bound.

At \(h=1/4,\kappa=1,\mathbf U^0=(0,1,0)^T\),
\[
\begin{array}{c|c|c|c}
\Delta t&r&\mathbf U^1&\mathbf U^2\\\hline
0.02&0.32&(0.32,0.36,0.32)&(0.2304,0.3344,0.2304)\\
0.04&0.64&(0.64,-0.28,0.64)&(-0.3584,0.8976,-0.3584)
\end{array}
\]
The second sequence violates positivity. The most negative grid eigenvalue is \(\lambda_{h,3}=-64\sin^2(3\pi/8)\approx-54.6274\), giving Euler amplification \(1+0.04\lambda_{h,3}\approx-1.1851\).

Backward Euler is the solve
\[
(I-\kappa\Delta t A_h)\mathbf U^{n+1}=\mathbf U^n,
\]
with eigenmode multiplier \((1-\kappa\Delta t\lambda_{h,m})^{-1}\in(0,1)\) for each negative eigenvalue \(\lambda_{h,m}\) and \(\Delta t>0\).

For sufficiently smooth compatible solutions, the FTCS residual has local operator truncation error \(O(\Delta t+h^2)\); under its stability condition the global grid error over fixed time is \(O(\Delta t+h^2)\), with constants depending on the smooth solution and interval. If \(\Delta t\sim h^2\), the combined leading order is \(O(h^2)\).

### Exercises with worked answers

1. With \(h=0.1\), \(\kappa=0.5\), what is the largest time step permitted by the uniform forward-Euler heat stability bound? **Answer:** \(\Delta t\le h^2/(2\kappa)=0.01\).
2. If the spatial mesh width is halved and you keep \(r\) fixed, how must \(\Delta t\) change? **Answer:** divide by four.
3. For \(\mathbf U^0=(0,1,0)^T\), \(h=1/4\), \(\kappa=1\), \(r=1/4\), compute the next vector. **Answer:** \((1/4,1/2,1/4)^T\).
4. Why can a backward Euler method remain stable when it is inaccurate? **Answer:** its negative-real-axis amplification has magnitude at most one for every positive step, but \((1-z)^{-1}\) need not closely approximate \(e^z\) for a large negative \(z\).
5. Give a one-mode exact PDE benchmark for zero Dirichlet heat diffusion. **Answer:** \(u(x,t)=e^{-\kappa\pi^2t}\sin(\pi x)\) on \((0,1)\).

### Sources and further reading

- [MIT OpenCourseWare, 18.086, Gilbert Strang: Finite Differences for the Heat Equation](https://ocw.mit.edu/courses/18-086-mathematical-methods-for-engineers-ii-spring-2006/pages/video-lectures/).
- [TU Delft, MUDE Numerical Methods for PDEs, Diffusion Equation](https://mude.citg.tudelft.nl/book/2025/numerical_methods_for_PDEs/diffusion_equation.html).
- [MIT OpenCourseWare, 18.085 Computational Science and Engineering I](https://ocw.mit.edu/courses/18-085-computational-science-and-engineering-i-summer-2020/).
