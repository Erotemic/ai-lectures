# Differential Equations and Dynamical Systems — Foundation-First Backlog

The pack now has **57 lecture manuscripts**: 13 inherited consolidated manuscripts and 44 worked foundations spanning `047000`–`090000` (2026-11-17). Existing consolidated and advanced manuscript prose remains unchanged. Lecture length is driven by teaching needs, not a fixed duration.

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

## Highest-priority remaining foundational gaps

1. **Nonlinear transport and finite-volume reconstruction.** A worked limiter/MUSCL comparison and a single nonlinear scalar Riemann problem, without jumping to advanced shock-stability theory.
2. **Elementary boundary numerical methods.** Accuracy and stability of fixed-boundary wave/heat discretizations, using the previously constructed Fourier modes and method of lines.
3. **Introductory probability for stochastic modeling.** Random variables, expectation, variance, covariance and Monte Carlo sampling, presented separately from the spectral-estimation applications.

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
