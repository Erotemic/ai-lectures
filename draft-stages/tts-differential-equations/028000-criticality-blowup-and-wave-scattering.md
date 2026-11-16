# 028000 — Critical Waves: Scaling, Blow-Up, and Scattering

**Track:** Differential Equations. **Background:** semilinear wave equations, conserved energy, Sobolev norms, dispersive inequalities and scaling. **Central question:** why do the same equations behave differently at different powers and in different dimensions?

<!-- BEGIN SPOKEN LECTURE -->

# A change of scale can reveal the difficult exponent

Some wave equations have no preferred length scale. If we zoom into a solution in space and time, multiplying its amplitude by the right factor produces another solution of the same mathematical form. This scaling symmetry is valuable because it tells us which norms can distinguish small structures from large ones.

Take a semilinear wave equation with a power nonlinearity. If we speed up both time and space by the same factor, the second derivatives pick up two powers of the scale factor. For the nonlinear term to scale the same way, the amplitude must be multiplied by the scale factor raised to two divided by p minus one, where p is the power of the nonlinearity.

Now ask what happens to energy. The gradient part of energy involves two derivatives in total, while integration over d-dimensional space introduces d powers from volume scaling. At one particular value of p, those effects balance exactly. That power is called energy critical.

In spatial dimension three, the energy-critical power is five: the nonlinear force is quintic in the amplitude. In dimension four, it is cubic. In dimensions one and two, no finite positive power has the same energy-critical scaling under the usual energy norm.

# Subcritical, critical, and supercritical

When an equation is energy subcritical, the conserved energy scales favorably relative to the local control norms, at least in the heuristic sense relevant to local theory. Energy-critical equations sit at the borderline: the energy is invariant under the natural scaling. Energy-supercritical equations allow concentration at smaller and smaller scales without a corresponding increase in the energy that would control those concentrations.

These names describe scaling, not an automatic verdict about existence. A subcritical equation may blow up with a focusing sign. A critical equation may have global solutions under suitable conditions. A supercritical equation is not guaranteed to blow up for every datum. The scaling classification tells us which estimates are plausible and which difficulties should be expected.

A critical theorem is often harder precisely because rescaling can preserve the quantity we hoped would control the solution. Compactness arguments can fail by concentration: a sequence of solutions can focus into smaller regions without its critical norm becoming large. This is one reason concentration-compactness and profile decompositions appear in advanced nonlinear wave analysis.

# Scattering is more than not blowing up

Suppose a solution exists for all positive time. That alone is not scattering. We say it scatters forward when it approaches some solution of the free linear wave equation in an appropriate norm as time goes to infinity.

The difference is important. A solution might survive forever while oscillating, retaining a bound state, or interacting nonlinearly in a persistent way. It need not approach a linear wave. Scattering requires that the nonlinear influence becomes asymptotically negligible in a precise sense.

Dispersive decay helps make scattering possible. A localized linear wave spreads its energy across space as time passes. Under suitable geometric conditions and appropriate norms, this reduces the strength of nonlinear interactions. But energy conservation alone does not imply a pointwise decay rate, and dispersive bounds can depend strongly on dimension and geometry.

# A small-data argument in outline

Imagine we have a norm that measures space-time dispersion, not merely energy at each time. Suppose the linear wave propagator maps small initial data to a small value of this norm. Suppose further that Duhamel's nonlinear forcing term obeys an estimate that is a higher power of the size of the solution.

Then a contraction mapping can close on a ball of small radius. The nonlinear correction remains smaller than the linear part, and the integral of the forcing over the entire time axis converges in the space needed to define an asymptotic free wave. This gives both global existence and scattering for sufficiently small data, under the theorem's exact admissibility assumptions.

Such an argument uses a precise collection of Strichartz or related estimates. It does not apply automatically on arbitrary manifolds, for arbitrary powers, or with arbitrary initial regularity. The details of the norm are part of the proof, not optional decoration.

# Focusing dynamics and threshold phenomena

For focusing nonlinearities, the potential energy has a negative sign. Special stationary or traveling profiles may exist, and they can separate different kinds of dynamics. Below a ground-state threshold, some equations admit strong global results under additional sign or variational conditions. Above or across such thresholds, blow-up or non-scattering behavior may occur.

The idea of a threshold is not that energy alone always divides the phase space into two simple regions. One may also need to control a gradient norm, a virial functional, or the sign of a quantity related to the ground state. The energy landscape has more structure than a single number.

This is especially vivid at the critical power. The scaling symmetry makes the shape and concentration of solutions central, and threshold theorems often compare solutions with a distinguished stationary profile that saturates a sharp inequality.

# What changes when the domain changes

On a compact spatial domain, linear waves do not disperse to infinity. The geometry can reflect and refocus them repeatedly. As a result, a scattering theorem that makes sense on Euclidean space may have no direct analogue on a compact manifold. Similarly, boundaries, trapping, and external potentials can interfere with the dispersive estimates used on free space.

This is a recurring theme across our Differential Equations course. Linearization and energy give local structural information, but global dynamics depend on the surrounding geometry and on how the system transports information.

Scaling, meanwhile, provides a diagnostic before we attempt a proof. It identifies invariant quantities and indicates when a norm can remain blind to small-scale concentration. That is why criticality is such a useful bridge between local existence, blow-up mechanisms, and long-time scattering theory.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

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

### Exercises with answers

1. Compute the energy-critical p in dimension six. **Answer:** `p=1+4/(6-2)=2`.
2. What is invariant at the critical exponent? **Answer:** the homogeneous energy scaling of the equation.
3. Is a global solution necessarily scattering? **Answer:** no; it may remain nonlinear or bound instead of approaching a free wave.
4. Why does a compact spatial domain complicate Euclidean scattering arguments? **Answer:** waves cannot disperse to spatial infinity in the same way.

### Reading and source notes

- [Tao, Nonlinear Dispersive Equations: Local and Global Analysis](https://www.math.ucla.edu/~tao/preprints/chapter.pdf), scaling and scattering methods.
- [Duyckaerts, Dynamics of Semilinear Wave Equations](https://www.math.univ-paris13.fr/~duyckaer/enseignement/CoursOndes2025_02_04.pdf), nonlinear wave dynamics and energy-critical analysis.
- [Shatah and Struwe, Geometric Wave Equations](https://www.ams.org/books/cln/002/), critical wave models and nonlinear energy arguments.
