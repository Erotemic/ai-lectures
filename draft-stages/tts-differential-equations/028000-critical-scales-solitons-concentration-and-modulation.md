# Critical scales, solitons, concentration, and modulation

<!-- BEGIN SPOKEN LECTURE -->

# Critical scales, solitons, concentration, and modulation

## Critical Waves: Scaling, Blow-Up, and Scattering

Some wave equations have no preferred length scale. If we zoom into a solution in space and time, multiplying its amplitude by the right factor produces another solution of the same mathematical form. This scaling symmetry is valuable because it tells us which norms can distinguish small structures from large ones.

Take a semilinear wave equation with a power nonlinearity. If we speed up both time and space by the same factor, the second derivatives pick up two powers of the scale factor. For the nonlinear term to scale the same way, the amplitude must be multiplied by the scale factor raised to two divided by p minus one, where p is the power of the nonlinearity.

Now ask what happens to energy. The gradient part of energy involves two derivatives in total, while integration over d-dimensional space introduces d powers from volume scaling. At one particular value of p, those effects balance exactly. That power is called energy critical.

In spatial dimension three, the energy-critical power is five: the nonlinear force is quintic in the amplitude. In dimension four, it is cubic. In dimensions one and two, no finite positive power has the same energy-critical scaling under the usual energy norm.

## Subcritical, critical, and supercritical

When an equation is energy subcritical, the conserved energy scales favorably relative to the local control norms, at least in the heuristic sense relevant to local theory. Energy-critical equations sit at the borderline: the energy is invariant under the natural scaling. Energy-supercritical equations allow concentration at smaller and smaller scales without a corresponding increase in the energy that would control those concentrations.

These names describe scaling, not an automatic verdict about existence. A subcritical equation may blow up with a focusing sign. A critical equation may have global solutions under suitable conditions. A supercritical equation is not guaranteed to blow up for every datum. The scaling classification tells us which estimates are plausible and which difficulties should be expected.

A critical theorem is often harder precisely because rescaling can preserve the quantity we hoped would control the solution. Compactness arguments can fail by concentration: a sequence of solutions can focus into smaller regions without its critical norm becoming large. This is one reason concentration-compactness and profile decompositions appear in advanced nonlinear wave analysis.

## Scattering is more than not blowing up

Suppose a solution exists for all positive time. That alone is not scattering. We say it scatters forward when it approaches some solution of the free linear wave equation in an appropriate norm as time goes to infinity.

The difference is important. A solution might survive forever while oscillating, retaining a bound state, or interacting nonlinearly in a persistent way. It need not approach a linear wave. Scattering requires that the nonlinear influence becomes asymptotically negligible in a precise sense.

Dispersive decay helps make scattering possible. A localized linear wave spreads its energy across space as time passes. Under suitable geometric conditions and appropriate norms, this reduces the strength of nonlinear interactions. But energy conservation alone does not imply a pointwise decay rate, and dispersive bounds can depend strongly on dimension and geometry.

## A small-data argument in outline

Imagine we have a norm that measures space-time dispersion, not merely energy at each time. Suppose the linear wave propagator maps small initial data to a small value of this norm. Suppose further that Duhamel's nonlinear forcing term obeys an estimate that is a higher power of the size of the solution.

Then a contraction mapping can close on a ball of small radius. The nonlinear correction remains smaller than the linear part, and the integral of the forcing over the entire time axis converges in the space needed to define an asymptotic free wave. This gives both global existence and scattering for sufficiently small data, under the theorem's exact admissibility assumptions.

Such an argument uses a precise collection of Strichartz or related estimates. It does not apply automatically on arbitrary manifolds, for arbitrary powers, or with arbitrary initial regularity. The details of the norm are part of the proof, not optional decoration.

## Focusing dynamics and threshold phenomena

For focusing nonlinearities, the potential energy has a negative sign. Special stationary or traveling profiles may exist, and they can separate different kinds of dynamics. Below a ground-state threshold, some equations admit strong global results under additional sign or variational conditions. Above or across such thresholds, blow-up or non-scattering behavior may occur.

The idea of a threshold is not that energy alone always divides the phase space into two simple regions. One may also need to control a gradient norm, a virial functional, or the sign of a quantity related to the ground state. The energy landscape has more structure than a single number.

This is especially vivid at the critical power. The scaling symmetry makes the shape and concentration of solutions central, and threshold theorems often compare solutions with a distinguished stationary profile that saturates a sharp inequality.

## What changes when the domain changes

On a compact spatial domain, linear waves do not disperse to infinity. The geometry can reflect and refocus them repeatedly. As a result, a scattering theorem that makes sense on Euclidean space may have no direct analogue on a compact manifold. Similarly, boundaries, trapping, and external potentials can interfere with the dispersive estimates used on free space.

This is a recurring theme across our Differential Equations course. Linearization and energy give local structural information, but global dynamics depend on the surrounding geometry and on how the system transports information.

Scaling, meanwhile, provides a diagnostic before we attempt a proof. It identifies invariant quantities and indicates when a norm can remain blind to small-scale concentration. That is why criticality is such a useful bridge between local existence, blow-up mechanisms, and long-time scattering theory.

## Solitons and Modulation: A Klein–Gordon Wave that Can Become Unstable

Many wave equations spread disturbances across space. But some nonlinear equations admit localized shapes that persist without dispersing. These structures are called solitary waves. They can travel at a constant speed or remain stationary in a suitable reference frame.

The existence of an exact localized shape does not automatically mean that the shape is stable. A pencil balanced on its tip is an exact equilibrium, but small perturbations can move it away. Nonlinear waves can have the same distinction between existence and stability, and their geometry is often more subtle because shifts in position create a whole family of equivalent solutions.

We will study an explicit example from a one-dimensional focusing cubic Klein–Gordon equation. The special feature is that we can write down its stationary wave, its linearized operator, and even an exponentially growing perturbation mode using elementary functions.

## A nonlinear Klein–Gordon equation

The equation has a second time derivative, a negative second spatial derivative, a linear restoring term, and a cubic focusing term. The cubic term has the sign that competes with the linear restoring force rather than strengthening it.

To find a stationary wave, set the time derivatives to zero. We obtain an ordinary differential equation for the spatial profile. We want a smooth function that approaches zero as the spatial coordinate tends to either positive or negative infinity.

A remarkable solution is the square root of two times the hyperbolic secant of the spatial coordinate. The hyperbolic secant is the reciprocal of the hyperbolic cosine, so it has a bell shape. It is largest at zero and decays exponentially in both directions.

Substitute this profile into the stationary differential equation, differentiate twice, and the terms cancel exactly. Thus this wave is not a numerical approximation or a perturbative guess. It is an exact nonlinear stationary solution on the whole real line.

## Translation produces a neutral direction

The equation is unchanged if we shift the spatial coordinate. If the bell-shaped profile centered at zero is a stationary solution, then the same profile centered at any other position is also a stationary solution.

Differentiate this family with respect to the center position. The result is proportional to the spatial derivative of the profile. It turns out to lie in the kernel of the linearized spatial operator.

This zero eigenvalue is geometrically necessary. A tiny shift of the center does not represent the same kind of departure as a deformation that changes the shape. It simply moves us along a family of exact solutions. Any stability analysis should recognize that neutral symmetry direction rather than treating it as a decay failure.

## Linearize the equation

Now perturb the stationary solution by adding a small function of time and space. Expand the cubic nonlinearity and retain only terms linear in that perturbation. We get a second-order evolution equation with a spatial Schrödinger-type operator.

That operator is minus the second spatial derivative plus one, minus three times the square of our stationary profile. Because the profile is the square root of two times the hyperbolic secant, the potential is one minus six times the square of the hyperbolic secant.

One eigenfunction is the spatial derivative of the profile, with eigenvalue zero. But there is another important eigenfunction: the square of the hyperbolic secant. Substitution shows that its eigenvalue is negative three.

A negative spatial eigenvalue produces a very different time behavior. Along that eigenfunction, the linearized wave amplitude satisfies an ordinary differential equation whose second derivative is three times the amplitude. Its solutions include an exponential growing like the exponential of the square root of three times time.

This is a genuine linear instability mode. Small perturbations with a component in that direction grow rather than disperse. The existence of the stationary wave does not protect it from that growth.

## Why simply tracking the center is not enough

A common way to study solitary waves is called modulation. We allow the center of the profile to depend slowly on time and write the actual solution as a shifted profile plus a remainder. We then impose an orthogonality condition on the remainder so that the decomposition selects a unique center, at least while the solution remains close to the family.

For our example, we can require the remainder to be orthogonal to the translation mode, the spatial derivative of the profile. This removes the ambiguity of whether a small difference came from an actual shape change or just a slight shift.

But the orthogonality condition does not remove the unstable eigenfunction. The unstable mode is distinct from the translation mode. Therefore modulation of the center alone is insufficient to prove that every nearby solution remains near the solitary wave forever.

A full dynamical analysis may require restricting initial data to a stable or center-stable manifold, accounting for the unstable direction, and controlling the nonlinear remainder. Different nonlinear equations can have solitary waves with very different spectral structures.

## Energy is conserved but instability remains

This Klein–Gordon equation has a conserved energy combining kinetic energy, spatial-gradient energy, a positive quadratic potential term, and a negative quartic potential term.

The negative quartic contribution is characteristic of the focusing case. It means that the energy is not globally a positive quadratic measure of distance from the origin or from the solitary wave. Conservation of this energy does not imply that every perturbation is controlled by a positive norm.

Near a stationary solution, the second variation of the energy is related to the linearized operator. A negative direction in this quadratic form is an indication of a potential instability, and in this explicit example the negative eigenvalue produces an actual exponentially growing linear mode.

## What the example teaches

This single model separates several statements that are often compressed into the word stable. A solitary wave exists exactly. Translation symmetry supplies a zero mode. The linearized operator supplies a negative mode. Modulation can account for the neutral shift without eliminating the unstable growth.

The resulting picture is more informative than simply saying nonlinear waves can form solitons. It tells us what must be examined to predict their behavior: conserved quantities, the spectrum of the linearized operator, the symmetry modes, and the nonlinear coupling among them. An exact coherent shape is only the beginning of the stability question.

## Concentration–Compactness and Nonlinear Scattering

Consider a wave packet evolving under a dispersive equation. The linear theory allows waves of different frequencies to spread at different speeds. At large times, a nonlinear solution may become close to some linear solution, even though nonlinear interactions influenced its earlier evolution. When this happens in a specified function-space norm, we say the nonlinear solution scatters.

Scattering is stronger than simply existing for all time. A global solution might oscillate forever, concentrate into a localized solitary wave, or undergo repeated interactions that never become negligible. A proof of global existence is not automatically a proof of scattering.

One important setting is the energy-critical nonlinear Schrödinger equation in three spatial dimensions. Its nonlinearity is the fifth power in amplitude: the equation contains the magnitude of the solution to the fourth power multiplied by the solution. The word critical means the scaling symmetry leaves the natural homogeneous energy norm unchanged.

This scaling creates the difficulty. A solution can concentrate into a smaller spatial region while maintaining the same critical norm. Ordinary compactness arguments that work at a fixed scale no longer rule out concentration. A sequence of solutions may shift, spread, or change scale rather than approach a limit in the usual sense.

## Why small data is easier

If the initial data is sufficiently small in the critical norm, dispersive estimates make nonlinear interactions perturbative. A fixed-point argument controls the solution in a spacetime norm, and the nonlinear correction remains integrable enough for the solution to approach a linear evolution.

For large data, the perturbative argument cannot be applied to the entire evolution in one step. The nonlinearity might be large over some time intervals. A standard approach is to partition the time axis into regions where suitable spacetime norms are small, but to prove scattering one must first show that the total relevant norm is finite.

One could hope to derive that finiteness directly from conserved energy. Sometimes monotonicity or interaction-Morawetz estimates accomplish much of the job. In critical problems, however, energy control alone often does not prevent a hypothetical solution from concentrating repeatedly.

Concentration–compactness attacks the obstruction indirectly. Rather than estimate every solution at once, suppose scattering fails and study the smallest possible counterexample.

## Decompose the escaping sequence

Imagine a sequence of initial data whose energies approach the lowest energy at which scattering can fail. The data may not converge strongly. One packet might move far away, another might concentrate on a tiny scale, and a third might disperse.

A profile decomposition separates these effects. After passing to a subsequence, the data can be expressed as a sum of profiles whose scales, locations, and sometimes time translations become asymptotically separated, plus a remainder that is small in a suitable dispersive sense.

Because separated profiles interact weakly, nonlinear perturbation theory can often approximate the evolution by the sum of their individual nonlinear evolutions. If every profile were safely below the supposed failure threshold, each would scatter, and the original solution would also scatter. That would contradict how the sequence was chosen.

The contradiction forces nearly all of the critical energy or norm to concentrate into one essential profile. One obtains a minimal nonscattering solution, sometimes called a critical element, whose orbit is precompact after allowing the symmetries of the equation.

## Compactness modulo symmetry is not ordinary compactness

For the energy-critical Schrödinger equation, translations and scalings act on solutions. A critical element need not stay in one fixed ball at one fixed physical scale. Instead, at each time it can be recentred and rescaled so that the resulting family lies in a compact subset of the critical function space.

The phrase almost periodic modulo symmetries describes that property. It does not mean the solution repeats with some time period. It means its energy remains concentrated near a moving center and a changing frequency scale, with uniform control of the tails after normalization.

This is a remarkable simplification. We began by imagining a vast class of bad evolutions. Now any failure of scattering would force a highly organized solution that maintains a coherent packet of critical-size energy. The proof has converted a global question into a rigidity question about a special compact orbit.

## The rigidity step must use the equation

The concentration–compactness step is not enough to prove scattering. It constructs a possible obstruction. A separate rigidity theorem must rule that obstruction out.

Depending on the equation, the rigidity argument may use a localized virial identity, a Morawetz inequality, finite-speed propagation, or another monotonicity mechanism. One typically shows that a nonzero almost-periodic solution would cause some positive quantity to accumulate or move in a way incompatible with the conservation laws and localization.

The details are not interchangeable. Radial symmetry may simplify spatial localization. Focusing and defocusing nonlinearities have different signs. Some equations admit stationary or solitary waves, so a rigidity theorem cannot forbid every compact orbit without restricting energy, norms, or symmetry classes.

For the focusing energy-critical Schrödinger equation, the stationary ground state establishes a natural threshold. Below its energy, the behavior can depend on whether the gradient norm lies below or above that of the ground state. A sharp scattering theorem under stated hypotheses must reflect that distinction. Declaring that all finite-energy focusing solutions scatter would be false.

## The ground state marks the obstruction

A concrete ground-state profile in three dimensions is the function one over the square root of one plus the radial coordinate squared divided by three. It solves a stationary elliptic equation associated with the focusing energy-critical Schrödinger dynamics.

This profile sits at a borderline scale. It is not a free dispersive wave and cannot scatter to one. It also shows why the concentrating critical element is a meaningful object rather than merely a nuisance of the proof method. The equation has coherent nonlinear structures that can block scattering.

In a defocusing problem the energy has a positive nonlinear term and no such stationary finite-energy ground state of the same type. A rigidity argument can exploit that sign. In a focusing problem the threshold geometry must be incorporated, often with variational inequalities comparing initial data to the ground state.

## The logical architecture

The full proof strategy has four moving parts. First, local well-posedness and perturbation estimates permit controlled approximate solutions. Second, a profile decomposition explains how bounded data can fail to converge because of symmetries. Third, a minimal-counterexample argument concentrates any failure of scattering into an almost-periodic critical element. Fourth, a rigidity theorem proves that the alleged critical element cannot exist under the theorem's hypotheses.

None of those steps alone implies the final result. A profile decomposition is a statement about sequences. A compact orbit may be possible for a different equation. A monotonicity identity is useful only if the quantities it controls are finite and its error terms can be estimated.

What concentration–compactness contributes is a way to transform a large-data question, beyond direct perturbation theory, into an exclusion problem for one highly constrained class of solutions. That pattern now appears across dispersive wave and Schrödinger equations, nonlinear elliptic problems, and other critical phenomena. It is not a formula for a solution. It is a proof strategy that explains why there can be no counterexample.

## Whitham Modulation and Dispersive Limits

Imagine a train of nearly periodic waves crossing a long channel. Individual crests move, but the broad envelope of the waves may move at a different speed. If wavelength and amplitude vary slowly, tracking each crest is not the most informative description. We want equations for the slowly varying pattern itself.

Whitham modulation theory is built for this situation. It starts with a family of periodic traveling-wave solutions to a partial differential equation, then allows the parameters of that family to change on a much larger spatial and temporal scale. Instead of solving the fast oscillation at every point, we derive effective equations for local wavelength, frequency, amplitude, and sometimes mean value.

The word “slowly” is not a metaphor. It is an assumption involving a small parameter and a separation between the oscillation scale and the modulation scale. If the scales cease to separate, the effective equations can fail even though the original PDE remains meaningful.

## Phase compatibility gives the first equation

Write the wave approximately as a periodic profile evaluated at a rapidly varying phase. Define the local wave number as the spatial derivative of that phase and the local frequency as minus its temporal derivative.

Now differentiate these definitions in the opposite order. Since mixed partial derivatives of a sufficiently smooth phase commute, the time derivative of the wave number plus the spatial derivative of the frequency is zero.

This is conservation of waves. It is not a conservation law obtained by integrating mass or energy. It is a compatibility identity saying that the local phase is a genuine function of space and time. A proposed modulation model that violates this identity cannot arise from one smooth phase field in the assumed regime.

A dispersion relation connects frequency to wave number and other slowly varying parameters. Substituting that relation turns phase compatibility into a transport-like PDE for the local wave number.

## Check the dispersion relation in KdV

Consider the Korteweg–de Vries equation, with a nonlinear transport term and a third spatial derivative. Linearize it around a constant background value. A small sinusoidal disturbance has a frequency equal to six times the background times wave number, minus wave number cubed.

The phase speed is frequency divided by wave number, whereas the group speed is the derivative of frequency with respect to wave number. For the linearized KdV equation, the group speed is six times the background minus three times wave number squared.

Those speeds differ except in special cases. A crest and a modulated wave packet do not generally travel together. This is why a large-scale modulation equation cannot be inferred just by following one crest at a fixed phase.

For slowly varying wave number on a fixed background, phase conservation gives an equation whose characteristic speed is the group speed. This is the linear, small-amplitude shadow of Whitham theory. The full nonlinear periodic-wave problem requires more parameters and more averaged equations.

## Average over one rapid oscillation

Suppose the original PDE has conservation laws. Evaluate them on a periodic traveling wave, then average the conserved density and flux over one period. Those averages depend on the wave's parameters. Allow the parameters to vary slowly and impose conservation of the averages.

Together with phase compatibility, these equations form the Whitham modulation system. Its unknowns are not every value of the original rapidly oscillating field; they are quantities such as local mean, amplitude, and wave number.

Averaging does not mean that the fast wave has disappeared. It means the fast shape is assumed to remain close to a member of the periodic-wave family as the parameters evolve. The approximate reconstruction from the modulation parameters and phase is part of the asymptotic claim.

For nonlinear KdV wavetrains, the full Whitham equations can be expressed using parameters related to the roots of a traveling-wave polynomial. In an appropriate regime they form a diagonalizable system whose characteristic speeds depend on elliptic integrals. A few words about group velocity do not replace that nonlinear calculation.

## What hyperbolicity tells us

Modulation equations are typically first-order PDEs. Their characteristic speeds may be real, in which case the system is hyperbolic, or may develop complex eigenvalues, indicating a different and potentially unstable modulation behavior.

The relation to spectral stability is subtle. A modulational instability often appears as small-frequency perturbations of the underlying periodic wave, but one must compare the modulation system with the Bloch spectrum of the full linearized PDE to make a theorem. Hyperbolicity can be a necessary or informative condition in particular models without being a universal guarantee of nonlinear stability.

Characteristic speeds can also coincide. Near degeneracy, higher-order dispersion or different slow scales can become important. A first-order Whitham approximation that worked far from the degeneracy can miss the leading dynamics there.

## From waves to dispersive shocks

An ordinary conservation law can develop a discontinuity when characteristics cross. A dispersive PDE does not necessarily form a classical shock. Instead, a region of rapid oscillations may appear, often called a dispersive shock wave.

Whitham modulation can describe the slowly varying envelope of that oscillatory region. At its edges, the periodic-wave family may degenerate into a small-amplitude wave or a solitary-wave limit. Matching those limiting behaviors helps determine the propagation of the edges.

This is different from a viscous shock, whose internal layer is shaped by dissipation. Dispersion spreads oscillations; viscosity smooths a transition. Both may regularize a steepening profile, but through different mechanisms and with different effective equations.

## What a modulation result needs

A controlled modulation approximation requires a family of periodic profiles, an appropriate nondegeneracy condition, slow initial data, and estimates that keep the solution near the modulated family over a stated time interval. Formal averaging is valuable, but it is not by itself a proof that errors remain small.

The simplest exact part is phase compatibility. It follows from mixed derivatives. The more demanding part is establishing that the averaged conservation laws provide an accurate evolution of the parameters. Spectral information, energy estimates, and sometimes integrability of the underlying PDE help.

Whitham theory turns a visibly complicated field of oscillations into a smaller geometry of parameters. A crest, an envelope, and a modulated wave train each have their own proper description. The theory works by keeping these levels of motion distinct while deriving equations that connect them.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Critical Waves: Scaling, Blow-Up, and Scattering

**Track:** Differential Equations. **Background:** semilinear wave equations, conserved energy, Sobolev norms, dispersive inequalities and scaling. **Central question:** why do the same equations behave differently at different powers and in different dimensions?

#### Mathematical companion (not spoken)

Consider `u_tt-Delta u + sigma |u|^{p-1}u=0` on `R^{1+d}`, p>1. Its scaling symmetry is
\[
u_\lambda(t,x)=\lambda^{2/(p-1)}u(\lambda t,\lambda x).
\]
The homogeneous energy norm scales as
\[
\|\nabla u_\lambda(0)\|_{L^2}^2
=\lambda^{\frac4{p-1}+2-d}\|\nabla u(0)\|_{L^2}^2.
\]
For `d>=3`, the critical power satisfies `4/(p-1)+2-d=0`, hence
\[
p_{\mathrm{crit}}=1+\frac4{d-2}=\frac{d+2}{d-2}.
\]
In three dimensions `p_crit=5`; in four `p_crit=3`. These values refer to the exponent in `|u|^{p-1}u` and not the exponent of its potential energy.

Let `S_L(t)` be the free wave evolution on energy data. Forward energy scattering means there exist `(v_0^+,v_1^+)` such that
\[
\|(u(t),u_t(t))-S_L(t)(v_0^+,v_1^+)\|_{\dot H^1\times L^2}
\longrightarrow0\qquad(t\to+\infty).
\]
A solution can be global without satisfying this limit. Scattering theorems require assumptions about the nonlinearity's sign, exponent, spatial domain and data class; Strichartz admissibility and endpoint issues cannot be ignored.

For focusing equations, negative potential energy makes the full conserved energy noncoercive. Threshold results based on a ground state typically require *additional* conditions; energy alone need not decide blow-up versus global dynamics.

##### Exercises with answers

1. Compute the energy-critical p in dimension six. **Answer:** `p=1+4/(6-2)=2`.
2. What is invariant at the critical exponent? **Answer:** the homogeneous energy scaling of the equation.
3. Is a global solution necessarily scattering? **Answer:** no; it may remain nonlinear or bound instead of approaching a free wave.
4. Why does a compact spatial domain complicate Euclidean scattering arguments? **Answer:** waves cannot disperse to spatial infinity in the same way.

##### Reading and source notes

- [Tao, Nonlinear Dispersive Equations: Local and Global Analysis](https://www.math.ucla.edu/~tao/preprints/chapter.pdf), scaling and scattering methods.
- [Duyckaerts, Dynamics of Semilinear Wave Equations](https://www.math.univ-paris13.fr/~duyckaer/enseignement/CoursOndes2025_02_04.pdf), nonlinear wave dynamics and energy-critical analysis.
- [Shatah and Struwe, Geometric Wave Equations](https://www.ams.org/books/cln/002/), critical wave models and nonlinear energy arguments.

### Solitons and Modulation: A Klein–Gordon Wave that Can Become Unstable

**Track:** Differential Equations. **Background:** semilinear wave equations, conserved energies, Sturm–Liouville theory, and linearization. **Central question:** how can a localized stationary wave be both an exact nonlinear solution and unstable under small perturbations?

#### Mathematical companion (not spoken)

Consider the focusing cubic Klein–Gordon equation on R:
\[
u_{tt}-u_{xx}+u-u^3=0.
\]
Its stationary profile `Q(x)=sqrt(2) sech(x)` satisfies `-Q''+Q-Q^3=0`, or equivalently `Q''=Q-Q^3`. The translated profiles `Q(x-y)` are also stationary.

Write `u=Q+eta`. Linearization yields `eta_tt+L eta = nonlinear higher-order terms`, where
\[
L=-\partial_x^2+1-3Q^2=-\partial_x^2+1-6\operatorname{sech}^2 x.
\]
Differentiating the stationary equation gives `L Q'=0`. Direct differentiation also gives
\[
L(\operatorname{sech}^2 x)=-3\operatorname{sech}^2 x.
\]
Thus a linear perturbation `eta(t,x)=a(t)sech^2(x)` obeys `a''-3a=0` and has a growing solution `a(t)=exp(sqrt(3)*t)`. The negative eigenvalue is a *linear instability*, not a theorem that every small nonlinear perturbation blows up.

The conserved energy for sufficiently regular decaying solutions is
\[
\mathcal E(u,u_t)=\int_\mathbb R\left[\tfrac12 u_t^2+\tfrac12 u_x^2+
\tfrac12 u^2-\tfrac14 u^4\right]dx.
\]
A modulated decomposition is `u(t,x)=Q(x-y(t))+eta(t,x)` with orthogonality `int eta(t,x) Q'(x-y(t)) dx=0`. Fixing the translation coordinate does not remove the negative eigendirection. For this explicit operator the unique negative discrete eigenvalue is -3, the zero eigenvalue corresponds to translation, and the continuous spectrum starts at 1, under the usual L2 realization.

##### Exercises with answers

1. Verify the stationary equation from `Q''=Q-Q^3`. **Answer:** substitute to obtain `-Q''+Q-Q^3=0`.
2. Why is `Q'` a zero eigenfunction? **Answer:** differentiate the stationary profile equation with respect to x.
3. Solve `a''-3a=0`. **Answer:** `a(t)=A e^(sqrt(3)t)+B e^(-sqrt(3)t)`.
4. Does an orthogonality condition against Q' remove an unstable sech-squared mode? **Answer:** no; the two modes correspond to different eigenvalues and the negative mode must be controlled separately.

##### Reading and source notes

- [The Cubic Klein–Gordon Equation with Damping (lecture notes)](https://lmv.math.cnrs.fr/wp-content/uploads/2025/02/M2_2025.pdf), explicit profile, linearized spectral structure and modulation estimates.
- [Terence Tao, PDE preprints on wave and dispersive equations](https://www.math.ucla.edu/~tao/preprints/pde.html), nonlinear Klein–Gordon dynamics and stability contexts.
- [Keel and Tao, Endpoint Strichartz Estimates](https://doi.org/10.1353/ajm.1998.0039), tools for perturbative dispersive analysis beyond the elementary spectral model.

### Concentration–Compactness and Nonlinear Scattering

**Track:** Differential Equations and Dynamical Systems. **Background:** dispersive PDEs, Sobolev spaces, nonlinear Schrödinger equations, and Strichartz estimates. **Central question:** how can one rule out every possible failure of scattering without explicitly solving each initial-value problem?

#### Mathematical companion (not spoken)

For the defocusing energy-critical NLS in `R^3`, use `i u_t+Delta u=|u|^4u`. The scaling `u_lambda(t,x)=lambda^(1/2)u(lambda^2 t,lambda x)` leaves `||grad u||_{L^2(R^3)}` invariant, and energy is
\[
E(u)=\frac12\int_{\mathbb R^3}|\nabla u|^2\,dx+\frac16\int_{\mathbb R^3}|u|^6\,dx.
\]
Scattering in the homogeneous H1 class means there exist `u_+` such that `||u(t)-e^{it Delta}u_+||_{dot H^1}->0` as `t->+infty` (with the prescribed solution class and conventions).

For focusing sign `i u_t+Delta u=-|u|^4u`, the energy uses a negative nonlinear term and `W(x)=(1+|x|^2/3)^(-1/2)` satisfies `Delta W+W^5=0`. Classical Kenig–Merle radial results for dimensions 3,4,5 distinguish scattering and blow-up below the ground-state energy using the gradient-norm threshold, along with regularity hypotheses. A minimal-blowup/critical-element proof has distinct **compactness** and **rigidity** steps; neither can be omitted.

##### Exercises with answers

1. Show the gradient L2 norm is scaling-invariant in three dimensions. **Answer:** `grad u_lambda=lambda^(3/2)grad u(lambda^2t,lambda x)`, and spatial change of variables contributes `lambda^-3` to its square integral.
2. Why can a bounded sequence fail to converge strongly? **Answer:** it may translate or concentrate at changing scales.
3. Does a critical element have to be periodic in time? **Answer:** no; almost periodic modulo symmetries is a compactness condition, not temporal periodicity.
4. Can every focusing energy-critical solution scatter? **Answer:** no; the ground state and blow-up regimes obstruct such a claim.

##### Reading and source notes

- [Kenig and Merle, Global well-posedness, scattering and blow-up for the focusing energy-critical NLS](https://arxiv.org/abs/math/0610266), critical-element and rigidity proof.
- [Duyckaerts, Kenig, and Merle, Profiles for bounded solutions of dispersive equations](https://www.aimsciences.org/article/doi/10.3934/cpaa.2015.14.1275), profile decompositions and critical dynamics.
- [W. Schlag, Long-term dynamics of nonlinear wave equations](https://math.mit.edu/events/kenig/assets/schlag.pdf), accessible concentration–compactness blueprint.

### Whitham Modulation and Dispersive Limits

**Track:** Differential Equations. **Background:** periodic traveling waves, conservation laws, linear dispersion, and nonlinear stability. **Central question:** what equations govern a wave train whose amplitude, wavelength, and speed vary slowly in space and time?

#### Mathematical companion (not spoken)

For a smooth phase `theta(x,t)`, define `k=theta_x`, `omega=-theta_t`; then `k_t+omega_x=0`. If a dispersion relation `omega=omega(k,a,...)` holds with slowly varying parameters, this is one modulation equation.

For `u_t+6uu_x+u_{xxx}=0`, linearize at constant `u_0`: `v_t+6u_0 v_x+v_{xxx}=0`. Insert `v=e^{i(kx-omega t)}` to obtain
\[
\omega(k)=6u_0 k-k^3,
\quad c_{\rm ph}=6u_0-k^2,
\quad c_{\rm gr}=\frac{d\omega}{dk}=6u_0-3k^2.
\]
For a slowly modulated linear wavetrain with fixed background, phase conservation gives `k_t+ (6u_0 k-k^3)_x=0`. Full nonlinear Whitham theory averages sufficient independent conservation laws on an actual periodic-wave family. This linear expression is not the complete nonlinear KdV system. Hyperbolicity of the modulation system and nonlinear stability of the original PDE are not interchangeable statements.

##### Exercises with answers

1. For `u_0=0`, `k=2`, calculate phase speed and group speed. **Answer:** `-4` and `-12`.
2. Why is `k_t+omega_x=0` independent of mass conservation? **Answer:** it follows from equality of mixed derivatives of a phase.
3. What mechanism distinguishes a dispersive shock from a viscous shock? **Answer:** rapidly oscillatory dispersive regularization versus dissipative smoothing.
4. Is a formal averaged equation automatically a proven approximation for all times? **Answer:** No; it requires an error analysis and an interval of validity.

##### Reading and source notes

- [Whitham, Linear and Nonlinear Waves](https://onlinelibrary.wiley.com/doi/book/10.1002/9781118032954), classical modulation theory.
- [Bridges, Breakdown of Whitham Modulation Theory and Emergence of Dispersion](https://doi.org/10.1111/sapm.12086), modulation degeneracy and new scales.
- [El and Hoefer, Dispersive Shock Waves and Modulation Theory](https://arxiv.org/abs/1602.06163), dispersive shock applications.
