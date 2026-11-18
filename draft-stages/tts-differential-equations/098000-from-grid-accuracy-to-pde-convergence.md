# From Grid Accuracy to PDE Convergence: Consistency, Stability, and Refinement

<!-- BEGIN SPOKEN LECTURE -->

# From Grid Accuracy to PDE Convergence

You have written a heat solver and a wave solver. Both produce smooth-looking animations. Both respect their boundary conditions. The heat calculation cools, and the wave calculation oscillates. But here is the question that separates an appealing simulation from a numerical result: when you make the grid finer and the time step smaller, do the computed values actually approach the solution of the differential equation?

It is tempting to answer by saying that finite differences become exact as the spacing goes to zero. That statement skips the central difficulty. A formula may approximate a derivative very accurately at one point, yet repeated use of the formula can amplify tiny errors until the final calculation is completely wrong. We have already seen that happen with explicit heat stepping beyond its stability limit. Accuracy of the local formula and control of the complete computation are different requirements.

The standard language separates them into consistency, stability, and convergence. We are going to connect those words to a calculation with exact numbers. Then we will do something similar for waves and see why a time step can be harmless for one spatial mode but disastrous for another.

## Consistency: put the exact solution into the wrong equation

Begin with a smooth exact solution of the heat equation on a finite rod with zero-temperature ends. Sample that exact function on the spatial grid and at each numerical time. Now pretend that those samples are the numbers our numerical method produced. Apply a single explicit heat update to them. In general the exact samples will not satisfy that discrete update perfectly. The mismatch is the local defect, also called a residual or truncation error.

Taylor expansion tells us where it comes from. The difference between next exact temperature and current exact temperature, divided by time step, approximates the time derivative with first-order error in the time step. The centered spatial second difference approximates the second spatial derivative with second-order error in the spatial spacing. Because the exact function satisfies the heat equation, their leading terms cancel. The remaining residual is bounded by a constant times time step plus spatial spacing squared, provided the necessary time and spatial derivatives exist and remain bounded.

Notice the assumptions. The initial temperature might contain a jump, or the boundary data might not agree smoothly with the initial data. Then the high derivatives used in this Taylor argument may not be bounded near the initial time or boundary. The method may still converge, but this particular simple error proof no longer applies with its stated constant and order.

Also notice that the local residual is an error in the *discrete differential equation*. A single-step temperature defect is the residual multiplied by the time step. That extra time-step factor matters when we add up errors over many steps. Mixing up these two conventions is a frequent source of mistaken convergence estimates.

## Stability: why the small defects stay small

Let the computed grid temperature differ from the exact sampled temperature by an error vector. Subtract the update equation for the exact samples from the update equation for the computed values. The result has a simple form: next error equals the heat update applied to current error, minus time step times the residual.

When the diffusion ratio is no larger than one half, the heat update is a nonnegative weighted average. It cannot increase the maximum absolute size of a grid vector with zero endpoint values. So the next error is at most the previous maximum error plus time step times the largest residual. Repeat that inequality through the whole computation. If we start with exact sampled initial values, then at a fixed final time the total maximum error is at most that time multiplied by the maximum residual encountered up to then.

That is the promised connection. Taylor expansion made the residual small. The maximum principle prevented each step from amplifying previous error. Together they imply convergence, with an error bound proportional to time step plus spatial spacing squared for sufficiently smooth compatible solutions. Either ingredient alone is insufficient: a consistent but unstable scheme can blow up, and a stable scheme that approximates the wrong differential equation can settle into a perfectly stable wrong answer.

The reasoning is strikingly practical. We did not need an explicit formula for every possible temperature profile. We needed a local approximation bound and a global estimate that prevents accumulation from getting out of hand. This is why energy estimates and maximum principles play such a large role in numerical analysis.

## A numerical experiment with an exact answer

Let's make the abstract estimate visible. Take the unit rod, cold at both ends, and begin with temperature equal to the sine of pi times position. This is a spatial mode whose exact heat evolution is especially simple. Its shape stays a sine wave, while its amplitude decays exponentially at a rate given by pi squared, when the diffusivity is one.

On a spatial grid with N equal subintervals, the sampled sine wave is also an eigenvector of the centered difference matrix. But the grid eigenvalue is not quite the continuum value negative pi squared. It is negative four divided by squared grid spacing times the square of the sine of pi divided by twice N. This difference is the spatial error. Forward Euler then replaces the exact exponential decay of that discrete mode by repeated multiplication by one plus time step times its grid eigenvalue. This creates the time error.

Choose the diffusion ratio equal to one quarter and measure the temperature after one sixteenth of a time unit. With four subintervals there are four time steps, and the computed amplitude is approximately zero point five three zero eight. The exact amplitude is about zero point five three nine six. The error is approximately eight point eight five thousandths.

Double the spatial resolution to eight subintervals, and reduce the time step by a factor of four to keep the same diffusion ratio. We now need sixteen time steps to reach the same final time. The amplitude error falls to about two point one six thousandths. Double the resolution again, to sixteen subintervals, and the error is roughly five point three six ten-thousandths. Each doubling divides the leading error by close to four. That is what second-order convergence with respect to grid spacing looks like in actual arithmetic.

Why four and not two? Because the spatial truncation error scales like the square of spacing. And because we held the diffusion ratio fixed, the time step also scales like the square of spacing. Its first-order time error is therefore of the same overall order as the second-order spatial error. The two contributions shrink together.

There is an important warning hidden in this convenient experiment. On an unstable choice of time step, this low-frequency sine mode might still decay and look plausible. The highest grid modes can be unstable even when the first mode is not. To establish stability of the scheme, we analyze its full spectrum or prove a maximum principle; we cannot infer stability by looking at one successful initial condition.

## Wave convergence needs a different stability argument

For the centered wave scheme, the local derivative residual is second-order both in time step and in spatial spacing, under enough smoothness. But its update has a previous time level as well as the current one, and it does not form a nonnegative average. That is appropriate: waves are not supposed to obey a heat-style maximum principle. Their amplitudes can overshoot neighboring values as energy travels and interferes.

Instead, use the conserved discrete wave energy. For a Courant number strictly below one, the energy controls the staggered velocity and an averaged spatial slope. When we apply the same discrete energy argument to the *error equation*, the residual acts as a small forcing. Over a fixed time interval, a bound on that forcing and a consistent second-order initial step give an error estimate. Under the usual smoothness and compatibility hypotheses, the energy-scale error is of order time step squared plus spatial spacing squared. The precise norm and treatment of the first step matter to the theorem.

We can check the predicted order with another standing-wave solution. Begin with the sine of pi times position as the initial string displacement, with zero initial velocity and fixed endpoints. The exact displacement keeps the sine shape while multiplying by cosine of pi times time, for wave speed one. On the grid, the centered scheme has its own discrete oscillation angle per time step. The solution is the same sampled sine shape multiplied by the cosine of that numerical angle times the step number, provided we start it with the second-order Taylor formula.

Choose a Courant number of one half and inspect the amplitude at time one half, when the exact first mode passes through zero. With four subintervals the numerical amplitude is about positive zero point zero three zero six. With eight it is about zero point zero zero seven five nine. With sixteen, about zero point zero zero one eight nine. Once again, halving the spacing shrinks the leading error by roughly four. This time the two terms are both second-order, and our fixed Courant number makes the time step proportional to the spacing, not to its square.

This wave example shows why the initial step matters. If we choose a first step that is only first-order accurate, that initial defect can dominate the final error even when the recurrence itself is second-order. A method's advertised order belongs to the whole algorithm, including how it begins and how its boundaries are handled.

## How to run a refinement study that tells the truth

When the exact solution is unavailable, we can compare numerical resolutions with each other. But a finer-grid solution is not automatically the truth. Compare quantities at matching physical times and positions, use an appropriate interpolation or restriction when grids differ, and check whether observed differences shrink at the expected rate. Distinguish maximum errors, energy errors, and errors in integral quantities. A method might conserve total mass exactly while placing a moving front a little too far to the right.

For heat diffusion, track positivity and the squared-temperature energy alongside numerical error. For waves, track the discrete energy, the positions of peaks, and phase errors over many cycles. If a boundary condition is approximated at lower order, that error may dominate the interior stencil. If the initial data are rough, the smooth-data error law may not appear until the solution has regularized or the grid becomes fine enough. If you change the physical model, no amount of numerical refinement can tell you whether that model itself describes your experiment correctly.

Finally, separate verification from validation. Verification asks whether the code actually solves the numerical equations we intended and whether those equations converge to the stated PDE. Validation asks whether the PDE and its boundary conditions represent the physical world well enough for the purpose at hand. An exact manufactured solution is excellent for verification, but it is not evidence that a model of a real steel beam or an actual heated wall has the right material constants.

We can now make a defensible claim about a numerical boundary-value solver. We know what its interior and boundary equations are. We know which physical balance it should preserve. We have a consistency calculation, a stability estimate, and a refinement test against an exact or independently checked answer. That is a substantial step beyond drawing a plausible simulation: it is a chain of reasons explaining why the approximation can be trusted, where the chain relies on smoothness or step-size restrictions, and what to test when one of those assumptions fails.

<!-- END SPOKEN LECTURE -->

## Mathematical companion: two complete convergence benchmarks

### Heat: a maximum-norm error recursion

For \(u_t=\kappa u_{xx}\) with homogeneous Dirichlet data, forward Euler uses
\[
 U_i^{n+1}=U_i^n+\kappa\Delta t(D_{xx}U^n)_i.
\]
For a sufficiently smooth exact solution define the residual of the sampled solution by
\[
 \tau_i^n=\frac{u(x_i,t_{n+1})-u(x_i,t_n)}{\Delta t}-\kappa(D_{xx}u(\cdot,t_n))_i.
\]
Taylor expansions give \(\|\tau\|_\infty\le C(\Delta t+h^2)\) on a fixed time interval, assuming suitable bounded temporal and spatial derivatives. If \(e_i^n=U_i^n-u(x_i,t_n)\), the recursion is
\[
 e^{n+1}=(I+\kappa\Delta t D_{xx})e^n-\Delta t\tau^n.
\]
For \(0\le r=\kappa\Delta t/h^2\le1/2\), the update is a maximum-norm contraction for homogeneous error boundary data, hence
\[
 \|e^n\|_\infty\le \|e^0\|_\infty+t_n C(\Delta t+h^2).
\]
This result requires a correct, compatible boundary treatment and sufficiently smooth data; it is not a theorem for arbitrarily rough solutions under the same derivative-based constant.

For \(\kappa=1\), the exact mode \(u(x,t)=e^{-\pi^2t}\sin(\pi x)\) yields numerical amplitude
\[
 a_h(T)=\left(1-4r\sin^2\frac{\pi}{2N}\right)^{T/\Delta t},\qquad h=1/N.
\]
Set \(r=1/4\), \(T=1/16\), \(\Delta t=h^2/4\), so \(T/\Delta t=N^2/4\) is an integer for the listed \(N\). The exact amplitude is \(e^{-\pi^2/16}\approx0.539641486\):

| Subintervals \(N\) | Steps | Numerical amplitude | Absolute amplitude error |
|---:|---:|---:|---:|
| 4 | 4 | 0.530790043 | 0.008851443 |
| 8 | 16 | 0.537484642 | 0.002156844 |
| 16 | 64 | 0.539105645 | 0.000535841 |
| 32 | 256 | 0.539507734 | 0.000133752 |

Each refinement approximately divides the error by four, consistent with \(O(h^2+\Delta t)=O(h^2)\) when \(\Delta t=h^2/4\).

### Wave: energy stability and phase convergence

For \(u_{tt}=c^2u_{xx}\), the leapfrog scheme with a second-order Taylor starter has local PDE residual \(O(\Delta t^2+h^2)\) for smooth solutions. Under \(r=c\Delta t/h\le1-\epsilon\), \(\epsilon>0\), the discrete wave energy controls the numerical error forced by that residual, yielding the corresponding fixed-time order in appropriate discrete energy norms, assuming compatible initial and boundary data.

The exact mode \(u(x,t)=\sin(\pi x)\cos(\pi ct)\) has sampled grid mode \(\sin(i\pi/N)\). Its discrete frequency satisfies
\[
 \Omega_h=2\arcsin\left[r\sin\left(\frac{\pi}{2N}\right)\right],\qquad U_i^n=\sin(i\pi/N)\cos(n\Omega_h)
\]
when the initial velocity is zero and the second-order starter is used. For \(c=1\), \(r=1/2\), \(T=1/2\) and \(n=T/\Delta t=N\), the exact amplitude is zero:

| Subintervals \(N\) | Discrete amplitude \(\cos(N\Omega_h)\) | Absolute amplitude error |
|---:|---:|---:|
| 4 | 0.030560064 | 0.030560064 |
| 8 | 0.007587959 | 0.007587959 |
| 16 | 0.001893610 | 0.001893610 |
| 32 | 0.000473189 | 0.000473189 |

The order is again approximately two in \(h\), but now \(\Delta t\propto h\) because the wave CFL number, not the diffusion ratio, is fixed.

### Exercises with worked answers

1. A heat scheme has \(h=0.1\), \(\kappa=1\), \(\Delta t=0.01\). Is its usual explicit stability restriction met? **Answer:** no; \(r=1\), exceeding the uniform bound \(1/2\).
2. If a heat solver has an error of \(0.008\) and is second-order under a refinement path \(\Delta t\propto h^2\), what error would you predict after halving \(h\)? **Answer:** about \(0.002\) when the asymptotic error term dominates.
3. Why is \(O(\Delta t+h^2)\) the local *residual* order for FTCS rather than the one-step temperature-defect order? **Answer:** the residual has divided a step difference by \(\Delta t\); the one-step defect is \(\Delta t\) times the residual.
4. A leapfrog wave scheme uses \(r=1/2\). If the spacing is halved and \(c\) fixed, how should \(\Delta t\) change to keep \(r\) fixed? **Answer:** halve the time step, unlike diffusion where it must be quartered to keep \(r_{\rm heat}\) fixed.
5. Why can a scheme pass an exact first-sine-mode test but still be unstable? **Answer:** higher discrete modes can have amplification factors outside the stability region even if the tested low mode decays.
6. What is a manufactured solution? **Answer:** a function chosen in advance; substitute it into the PDE to calculate a forcing term and compatible boundary/initial data, then compare the numerical solver against that exact solution.

### Sources and further reading

- [Langtangen and Linge, *Finite Difference Computing with PDEs*, Wave and Diffusion Equations](https://link.springer.com/book/10.1007/978-3-319-55456-3).
- [MIT OpenCourseWare 18.086, Finite Differences: Accuracy, Stability, Convergence](https://ocw.mit.edu/courses/18-086-mathematical-methods-for-engineers-ii-spring-2006/resources/lecture-videos/).
- [Wikipedia: Lax equivalence theorem](https://en.wikipedia.org/wiki/Lax_equivalence_theorem) (related linear initial-value principle; not a substitute for the specific stability proofs used here).
