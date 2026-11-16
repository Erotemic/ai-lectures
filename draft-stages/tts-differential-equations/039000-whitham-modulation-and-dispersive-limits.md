# 039000 - Whitham Modulation and Dispersive Limits

**Track:** Differential Equations. **Background:** periodic traveling waves, conservation laws, linear dispersion, and nonlinear stability. **Central question:** what equations govern a wave train whose amplitude, wavelength, and speed vary slowly in space and time?

<!-- BEGIN SPOKEN LECTURE -->

# A wave can have two distinct speeds

Imagine a train of nearly periodic waves crossing a long channel. Individual crests move, but the broad envelope of the waves may move at a different speed. If wavelength and amplitude vary slowly, tracking each crest is not the most informative description. We want equations for the slowly varying pattern itself.

Whitham modulation theory is built for this situation. It starts with a family of periodic traveling-wave solutions to a partial differential equation, then allows the parameters of that family to change on a much larger spatial and temporal scale. Instead of solving the fast oscillation at every point, we derive effective equations for local wavelength, frequency, amplitude, and sometimes mean value.

The word “slowly” is not a metaphor. It is an assumption involving a small parameter and a separation between the oscillation scale and the modulation scale. If the scales cease to separate, the effective equations can fail even though the original PDE remains meaningful.

# Phase compatibility gives the first equation

Write the wave approximately as a periodic profile evaluated at a rapidly varying phase. Define the local wave number as the spatial derivative of that phase and the local frequency as minus its temporal derivative.

Now differentiate these definitions in the opposite order. Since mixed partial derivatives of a sufficiently smooth phase commute, the time derivative of the wave number plus the spatial derivative of the frequency is zero.

This is conservation of waves. It is not a conservation law obtained by integrating mass or energy. It is a compatibility identity saying that the local phase is a genuine function of space and time. A proposed modulation model that violates this identity cannot arise from one smooth phase field in the assumed regime.

A dispersion relation connects frequency to wave number and other slowly varying parameters. Substituting that relation turns phase compatibility into a transport-like PDE for the local wave number.

# Check the dispersion relation in KdV

Consider the Korteweg–de Vries equation, with a nonlinear transport term and a third spatial derivative. Linearize it around a constant background value. A small sinusoidal disturbance has a frequency equal to six times the background times wave number, minus wave number cubed.

The phase speed is frequency divided by wave number, whereas the group speed is the derivative of frequency with respect to wave number. For the linearized KdV equation, the group speed is six times the background minus three times wave number squared.

Those speeds differ except in special cases. A crest and a modulated wave packet do not generally travel together. This is why a large-scale modulation equation cannot be inferred just by following one crest at a fixed phase.

For slowly varying wave number on a fixed background, phase conservation gives an equation whose characteristic speed is the group speed. This is the linear, small-amplitude shadow of Whitham theory. The full nonlinear periodic-wave problem requires more parameters and more averaged equations.

# Average over one rapid oscillation

Suppose the original PDE has conservation laws. Evaluate them on a periodic traveling wave, then average the conserved density and flux over one period. Those averages depend on the wave's parameters. Allow the parameters to vary slowly and impose conservation of the averages.

Together with phase compatibility, these equations form the Whitham modulation system. Its unknowns are not every value of the original rapidly oscillating field; they are quantities such as local mean, amplitude, and wave number.

Averaging does not mean that the fast wave has disappeared. It means the fast shape is assumed to remain close to a member of the periodic-wave family as the parameters evolve. The approximate reconstruction from the modulation parameters and phase is part of the asymptotic claim.

For nonlinear KdV wavetrains, the full Whitham equations can be expressed using parameters related to the roots of a traveling-wave polynomial. In an appropriate regime they form a diagonalizable system whose characteristic speeds depend on elliptic integrals. A few words about group velocity do not replace that nonlinear calculation.

# What hyperbolicity tells us

Modulation equations are typically first-order PDEs. Their characteristic speeds may be real, in which case the system is hyperbolic, or may develop complex eigenvalues, indicating a different and potentially unstable modulation behavior.

The relation to spectral stability is subtle. A modulational instability often appears as small-frequency perturbations of the underlying periodic wave, but one must compare the modulation system with the Bloch spectrum of the full linearized PDE to make a theorem. Hyperbolicity can be a necessary or informative condition in particular models without being a universal guarantee of nonlinear stability.

Characteristic speeds can also coincide. Near degeneracy, higher-order dispersion or different slow scales can become important. A first-order Whitham approximation that worked far from the degeneracy can miss the leading dynamics there.

# From waves to dispersive shocks

An ordinary conservation law can develop a discontinuity when characteristics cross. A dispersive PDE does not necessarily form a classical shock. Instead, a region of rapid oscillations may appear, often called a dispersive shock wave.

Whitham modulation can describe the slowly varying envelope of that oscillatory region. At its edges, the periodic-wave family may degenerate into a small-amplitude wave or a solitary-wave limit. Matching those limiting behaviors helps determine the propagation of the edges.

This is different from a viscous shock, whose internal layer is shaped by dissipation. Dispersion spreads oscillations; viscosity smooths a transition. Both may regularize a steepening profile, but through different mechanisms and with different effective equations.

# What a modulation result needs

A controlled modulation approximation requires a family of periodic profiles, an appropriate nondegeneracy condition, slow initial data, and estimates that keep the solution near the modulated family over a stated time interval. Formal averaging is valuable, but it is not by itself a proof that errors remain small.

The simplest exact part is phase compatibility. It follows from mixed derivatives. The more demanding part is establishing that the averaged conservation laws provide an accurate evolution of the parameters. Spectral information, energy estimates, and sometimes integrability of the underlying PDE help.

Whitham theory turns a visibly complicated field of oscillations into a smaller geometry of parameters. A crest, an envelope, and a modulated wave train each have their own proper description. The theory works by keeping these levels of motion distinct while deriving equations that connect them.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For a smooth phase `theta(x,t)`, define `k=theta_x`, `omega=-theta_t`; then `k_t+omega_x=0`. If a dispersion relation `omega=omega(k,a,...)` holds with slowly varying parameters, this is one modulation equation.

For `u_t+6uu_x+u_{xxx}=0`, linearize at constant `u_0`: `v_t+6u_0 v_x+v_{xxx}=0`. Insert `v=e^{i(kx-omega t)}` to obtain
\[
\omega(k)=6u_0 k-k^3,
\quad c_{\rm ph}=6u_0-k^2,
\quad c_{\rm gr}=\frac{d\omega}{dk}=6u_0-3k^2.
\]
For a slowly modulated linear wavetrain with fixed background, phase conservation gives `k_t+ (6u_0 k-k^3)_x=0`. Full nonlinear Whitham theory averages sufficient independent conservation laws on an actual periodic-wave family. This linear expression is not the complete nonlinear KdV system. Hyperbolicity of the modulation system and nonlinear stability of the original PDE are not interchangeable statements.

### Exercises with answers

1. For `u_0=0`, `k=2`, calculate phase speed and group speed. **Answer:** `-4` and `-12`.
2. Why is `k_t+omega_x=0` independent of mass conservation? **Answer:** it follows from equality of mixed derivatives of a phase.
3. What mechanism distinguishes a dispersive shock from a viscous shock? **Answer:** rapidly oscillatory dispersive regularization versus dissipative smoothing.
4. Is a formal averaged equation automatically a proven approximation for all times? **Answer:** No; it requires an error analysis and an interval of validity.

### Reading and source notes

- [Whitham, Linear and Nonlinear Waves](https://onlinelibrary.wiley.com/doi/book/10.1002/9781118032954), classical modulation theory.
- [Bridges, Breakdown of Whitham Modulation Theory and Emergence of Dispersion](https://doi.org/10.1111/sapm.12086), modulation degeneracy and new scales.
- [El and Hoefer, Dispersive Shock Waves and Modulation Theory](https://arxiv.org/abs/1602.06163), dispersive shock applications.
