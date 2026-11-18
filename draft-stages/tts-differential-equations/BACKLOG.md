# Differential Equations and Dynamical Systems — Foundation-First Backlog

The pack now has **65 lecture manuscripts**: 13 inherited consolidated manuscripts and 52 worked foundations spanning `047000`–`098000` (2026-11-18). Existing consolidated and advanced manuscript prose remains unchanged. Lecture length is driven by teaching needs, not a fixed duration.

## Foundation-first additions completed

- `047000`–`050000`: rate laws, first-order solution methods, existence/uniqueness, and oscillators.
- `051000`–`054000`: Fourier coefficients and convergence, periodic forcing and resonance.
- `055000`–`058000`: Laplace transform construction, IVPs, switched forcing, convolution and transfer functions.
- `059000`–`062000`: coupled linear systems, nodes, saddles, spirals, generalized eigenvectors and matrix exponentials.
- `063000`–`066000`: Euler, midpoint and Heun updates; classical RK4; local versus global errors; stability regions, backward Euler and stiff decay.
- `067000`–`070000`: boundary versus initial data; Dirichlet, Neumann and Robin conditions; Sturm-Liouville eigenfunctions; heat and wave mode solutions with exact examples.
- `071000`–`074000`: Fourier transform as a continuum of series frequencies; Gaussian heat kernel and convolution; finite differences, spatial matrices, and diffusion method-of-lines stability.
- `075000`–`078000`: characteristics and conservation; upwind differences and CFL; modified-equation numerical diffusion, Lax–Wendroff and monotonicity; finite-volume flux balances.
- `079000`–`082000`: sampling, Nyquist and aliases; four-point DFT, inverse and Parseval; leakage, windows and circular convolution; radix-two FFT and periodic finite-difference heat modes.
- `083000`–`086000`: embedded/adaptive local error tests, componentwise tolerances, event roots and impact jumps, and symplectic/energy-aware oscillator stepping.
- `087000`–`090000`: short-time Fourier transform, time–frequency uncertainty, chirps/impacts and spectrogram interpretation, noise PSD normalization and Welch averaging.
- `091000`–`094000`: Burgers shock formation, entropy-admissible Riemann problems, Godunov fluxes, MUSCL reconstruction, and slope limiting.
- `095000`–`098000`: endpoint forcing and ghost nodes, heat maximum principle and discrete energy, centered wave leapfrog energy and CFL, and consistency-stability-convergence with refinement tables.

## Highest-priority remaining foundational gaps

1. **Introductory probability for stochastic modeling.** Random variables, expectation, variance, covariance and Monte Carlo sampling, presented separately from the spectral-estimation applications.
2. **Foundational statistics and uncertainty.** Sampling distributions, bias, confidence intervals and stochastic simulation error, rather than only spectral-noise applications.

## Already covered but compressed

- `001000`: introductory ODE models, uniqueness, and scalar solution methods.
- `004000`: oscillators, linear systems, and sinusoidal forcing.
- `007000`: nonlinear phase portraits, bifurcation, and stiffness.
- `019000`: geometric PDE solvers and Hamiltonian integrators (advanced).

These are not missing topics; the new lectures provide accessible constructions and worked verification before listeners encounter the advanced surveys. The existing Fourier and Laplace routes remain independently listenable.

## Deprioritized advanced proposals

- `043000` — Slow Manifolds and Pattern Formation
- `044000` — Stefan Free-Boundary Problems
- `045000` — Multiphysics Energy-Stable Coupling
- `046000` — Quasilinear Waves and Weak Null Conditions

These IDs are placeholders for proposed work, not published manuscripts. No audio was generated in this source-only batch.

## Time–frequency and spectral-estimation foundation bridge

The `087000`–`090000` route builds the short-time Fourier transform and exact four-point frames from the sampling/DFT route, then proves the Gaussian variance-based uncertainty inequality. It distinguishes hop density, physical window duration, FFT spacing and actual resolution; reads chirps and impulses with phase and plotting caveats; and derives the correct window-normalized white-noise PSD and Welch averaging. Noise statistics are introduced using elementary means and variances instead of assumed probability theory. All 53 preceding manuscripts and their metadata are unchanged.

## Nonlinear scalar conservation and limited reconstruction foundation bridge

The `091000`–`094000` route shows characteristic crossing and finite-time slope blow-up, then distinguishes conserved weak shocks from entropy-admissible shocks and rarefactions. It derives the exact scalar Godunov flux, checks all face fluxes of a four-cell periodic grid, and constructs minmod/MUSCL–Hancock updates. The lessons are confined to their scalar hypotheses; they do not claim that conservation alone implies admissibility or that slope limiting alone guarantees nonlinear multidimensional TVD. All 57 earlier manuscripts and metadata remain unchanged.

## Finite-difference boundary methods and PDE convergence foundation bridge

The `095000`–`098000` route supplies the missing construction-level boundary treatment for heat and wave grids, with explicit Dirichlet boundary rows, mass-preserving Neumann ghost nodes, maximum principles, summation by parts, staggered leapfrog energy, and CFL-dependent stability. A discrete error recursion proves fixed-time heat convergence under smooth compatible data; exact heat and wave mode refinement tables check second-order observed accuracy. The 61 earlier manuscripts and metadata remain unchanged.
