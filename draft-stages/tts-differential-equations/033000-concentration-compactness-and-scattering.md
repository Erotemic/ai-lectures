# 033000 — Concentration–Compactness and Nonlinear Scattering

**Track:** Differential Equations and Dynamical Systems. **Background:** dispersive PDEs, Sobolev spaces, nonlinear Schrödinger equations, and Strichartz estimates. **Central question:** how can one rule out every possible failure of scattering without explicitly solving each initial-value problem?

<!-- BEGIN SPOKEN LECTURE -->

# Scattering is a long-time comparison

Consider a wave packet evolving under a dispersive equation. The linear theory allows waves of different frequencies to spread at different speeds. At large times, a nonlinear solution may become close to some linear solution, even though nonlinear interactions influenced its earlier evolution. When this happens in a specified function-space norm, we say the nonlinear solution scatters.

Scattering is stronger than simply existing for all time. A global solution might oscillate forever, concentrate into a localized solitary wave, or undergo repeated interactions that never become negligible. A proof of global existence is not automatically a proof of scattering.

One important setting is the energy-critical nonlinear Schrödinger equation in three spatial dimensions. Its nonlinearity is the fifth power in amplitude: the equation contains the magnitude of the solution to the fourth power multiplied by the solution. The word critical means the scaling symmetry leaves the natural homogeneous energy norm unchanged.

This scaling creates the difficulty. A solution can concentrate into a smaller spatial region while maintaining the same critical norm. Ordinary compactness arguments that work at a fixed scale no longer rule out concentration. A sequence of solutions may shift, spread, or change scale rather than approach a limit in the usual sense.

# Why small data is easier

If the initial data is sufficiently small in the critical norm, dispersive estimates make nonlinear interactions perturbative. A fixed-point argument controls the solution in a spacetime norm, and the nonlinear correction remains integrable enough for the solution to approach a linear evolution.

For large data, the perturbative argument cannot be applied to the entire evolution in one step. The nonlinearity might be large over some time intervals. A standard approach is to partition the time axis into regions where suitable spacetime norms are small, but to prove scattering one must first show that the total relevant norm is finite.

One could hope to derive that finiteness directly from conserved energy. Sometimes monotonicity or interaction-Morawetz estimates accomplish much of the job. In critical problems, however, energy control alone often does not prevent a hypothetical solution from concentrating repeatedly.

Concentration–compactness attacks the obstruction indirectly. Rather than estimate every solution at once, suppose scattering fails and study the smallest possible counterexample.

# Decompose the escaping sequence

Imagine a sequence of initial data whose energies approach the lowest energy at which scattering can fail. The data may not converge strongly. One packet might move far away, another might concentrate on a tiny scale, and a third might disperse.

A profile decomposition separates these effects. After passing to a subsequence, the data can be expressed as a sum of profiles whose scales, locations, and sometimes time translations become asymptotically separated, plus a remainder that is small in a suitable dispersive sense.

Because separated profiles interact weakly, nonlinear perturbation theory can often approximate the evolution by the sum of their individual nonlinear evolutions. If every profile were safely below the supposed failure threshold, each would scatter, and the original solution would also scatter. That would contradict how the sequence was chosen.

The contradiction forces nearly all of the critical energy or norm to concentrate into one essential profile. One obtains a minimal nonscattering solution, sometimes called a critical element, whose orbit is precompact after allowing the symmetries of the equation.

# Compactness modulo symmetry is not ordinary compactness

For the energy-critical Schrödinger equation, translations and scalings act on solutions. A critical element need not stay in one fixed ball at one fixed physical scale. Instead, at each time it can be recentred and rescaled so that the resulting family lies in a compact subset of the critical function space.

The phrase almost periodic modulo symmetries describes that property. It does not mean the solution repeats with some time period. It means its energy remains concentrated near a moving center and a changing frequency scale, with uniform control of the tails after normalization.

This is a remarkable simplification. We began by imagining a vast class of bad evolutions. Now any failure of scattering would force a highly organized solution that maintains a coherent packet of critical-size energy. The proof has converted a global question into a rigidity question about a special compact orbit.

# The rigidity step must use the equation

The concentration–compactness step is not enough to prove scattering. It constructs a possible obstruction. A separate rigidity theorem must rule that obstruction out.

Depending on the equation, the rigidity argument may use a localized virial identity, a Morawetz inequality, finite-speed propagation, or another monotonicity mechanism. One typically shows that a nonzero almost-periodic solution would cause some positive quantity to accumulate or move in a way incompatible with the conservation laws and localization.

The details are not interchangeable. Radial symmetry may simplify spatial localization. Focusing and defocusing nonlinearities have different signs. Some equations admit stationary or solitary waves, so a rigidity theorem cannot forbid every compact orbit without restricting energy, norms, or symmetry classes.

For the focusing energy-critical Schrödinger equation, the stationary ground state establishes a natural threshold. Below its energy, the behavior can depend on whether the gradient norm lies below or above that of the ground state. A sharp scattering theorem under stated hypotheses must reflect that distinction. Declaring that all finite-energy focusing solutions scatter would be false.

# The ground state marks the obstruction

A concrete ground-state profile in three dimensions is the function one over the square root of one plus the radial coordinate squared divided by three. It solves a stationary elliptic equation associated with the focusing energy-critical Schrödinger dynamics.

This profile sits at a borderline scale. It is not a free dispersive wave and cannot scatter to one. It also shows why the concentrating critical element is a meaningful object rather than merely a nuisance of the proof method. The equation has coherent nonlinear structures that can block scattering.

In a defocusing problem the energy has a positive nonlinear term and no such stationary finite-energy ground state of the same type. A rigidity argument can exploit that sign. In a focusing problem the threshold geometry must be incorporated, often with variational inequalities comparing initial data to the ground state.

# The logical architecture

The full proof strategy has four moving parts. First, local well-posedness and perturbation estimates permit controlled approximate solutions. Second, a profile decomposition explains how bounded data can fail to converge because of symmetries. Third, a minimal-counterexample argument concentrates any failure of scattering into an almost-periodic critical element. Fourth, a rigidity theorem proves that the alleged critical element cannot exist under the theorem's hypotheses.

None of those steps alone implies the final result. A profile decomposition is a statement about sequences. A compact orbit may be possible for a different equation. A monotonicity identity is useful only if the quantities it controls are finite and its error terms can be estimated.

What concentration–compactness contributes is a way to transform a large-data question, beyond direct perturbation theory, into an exclusion problem for one highly constrained class of solutions. That pattern now appears across dispersive wave and Schrödinger equations, nonlinear elliptic problems, and other critical phenomena. It is not a formula for a solution. It is a proof strategy that explains why there can be no counterexample.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For the defocusing energy-critical NLS in `R^3`, use `i u_t+Delta u=|u|^4u`. The scaling `u_lambda(t,x)=lambda^(1/2)u(lambda^2 t,lambda x)` leaves `||grad u||_{L^2(R^3)}` invariant, and energy is
\[
E(u)=\frac12\int_{\mathbb R^3}|\nabla u|^2\,dx+\frac16\int_{\mathbb R^3}|u|^6\,dx.
\]
Scattering in the homogeneous H1 class means there exist `u_+` such that `||u(t)-e^{it Delta}u_+||_{dot H^1}->0` as `t->+infty` (with the prescribed solution class and conventions).

For focusing sign `i u_t+Delta u=-|u|^4u`, the energy uses a negative nonlinear term and `W(x)=(1+|x|^2/3)^(-1/2)` satisfies `Delta W+W^5=0`. Classical Kenig–Merle radial results for dimensions 3,4,5 distinguish scattering and blow-up below the ground-state energy using the gradient-norm threshold, along with regularity hypotheses. A minimal-blowup/critical-element proof has distinct **compactness** and **rigidity** steps; neither can be omitted.

### Exercises with answers

1. Show the gradient L2 norm is scaling-invariant in three dimensions. **Answer:** `grad u_lambda=lambda^(3/2)grad u(lambda^2t,lambda x)`, and spatial change of variables contributes `lambda^-3` to its square integral.
2. Why can a bounded sequence fail to converge strongly? **Answer:** it may translate or concentrate at changing scales.
3. Does a critical element have to be periodic in time? **Answer:** no; almost periodic modulo symmetries is a compactness condition, not temporal periodicity.
4. Can every focusing energy-critical solution scatter? **Answer:** no; the ground state and blow-up regimes obstruct such a claim.

### Reading and source notes

- [Kenig and Merle, Global well-posedness, scattering and blow-up for the focusing energy-critical NLS](https://arxiv.org/abs/math/0610266), critical-element and rigidity proof.
- [Duyckaerts, Kenig, and Merle, Profiles for bounded solutions of dispersive equations](https://www.aimsciences.org/article/doi/10.3934/cpaa.2015.14.1275), profile decompositions and critical dynamics.
- [W. Schlag, Long-term dynamics of nonlinear wave equations](https://math.mit.edu/events/kenig/assets/schlag.pdf), accessible concentration–compactness blueprint.
