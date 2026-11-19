# Numerical Analysis and Reliable Computation

Floating-point arithmetic, conditioning, stability, approximation methods, error bounds, and certification.

The current pack contains **15 lecture manuscripts**. Short concept chapters have been consolidated where they develop one subject. Each numbered manuscript has one spoken region; its mathematical statements, exercises, sources, and inherited component notes remain in the non-spoken companion.

## Listening routes

`track.json` owns the current manuscripts and complete sequence. `navigation.json` selects the guided and deeper routes listed below.

- **Numerical Analysis · Reliable Computation Foundations** (Guided route): `001000`, `002000`, `003000`, `004000`, `005000`, `006000`, `007000`, `008000`, `009000`, `010000`, `011000`.
- **Numerical Analysis · Sparse Solvers and Preconditioning** (Deep dive): `006000`, `010000`, `014000`, `019000`.
- **Numerical Analysis · Validated Dynamics and Nonlinear Systems** (Deep dive): `005000`, `007000`, `011000`.
- **Numerical Analysis · Derivatives, Adjoint Methods, and Events** (Deep dive): `016000`.
- **Numerical Analysis · PDE Error Certificates** (Deep dive): `018000`.

## Current manuscripts

Durations are measured from the current spoken text at 145 words per minute, before synthesis; they are descriptions, not writing targets.

| ID | Lecture | Approximate minutes |
|---|---|---:|
| `001000` | [When to Trust a Computed Answer: Models, Data, Approximation, and Tolerances](001000-when-to-trust-a-computed-answer.md) | 13.8 |
| `002000` | [Small Errors, Large Consequences: Rounding and Error Propagation](002000-rounding-and-error-propagation.md) | 21.0 |
| `003000` | [Conditioning: When the Problem Amplifies Small Errors](003000-conditioning-and-sensitivity.md) | 11.9 |
| `004000` | [Backward Error: Which Nearby Problem Did the Algorithm Solve?](004000-backward-error-and-stability.md) | 11.5 |
| `005000` | [Finding Roots: Brackets, Newton's Method, and Honest Stopping Rules](005000-roots-brackets-and-newton.md) | 12.0 |
| `006000` | [Linear Algebra in Finite Precision: Pivoting, Conditioning, and Residuals](006000-linear-algebra-pivoting-and-residuals.md) | 10.8 |
| `007000` | [Convergence and Error Certificates: Knowing When to Stop](007000-error-budgets-convergence-certificates.md) | 12.7 |
| `008000` | [Interpolation: Why More Data Points Can Make an Approximation Worse](008000-interpolation-nodes-and-conditioning.md) | 11.2 |
| `009000` | [Quadrature and adaptive error control](009000-quadrature-and-adaptive-error-control.md) | 18.3 |
| `010000` | [Iterative Linear Solvers: Residuals, Spectra, and Conjugate Gradients](010000-iterative-linear-solvers-and-residuals.md) | 10.3 |
| `011000` | [Time stepping, verified enclosures, and validated dynamics](011000-time-stepping-verified-enclosures-and-validated-dynamics.md) | 48.5 |
| `014000` | [Krylov eigenproblems, implicit time steps, and preconditioning](014000-residuals-krylov-eigenproblems-and-implicit-solves-shared-core.md) | 17.6 |
| `016000` | [Differentiating algorithms, nonsmooth outputs, and event times](016000-differentiating-algorithms-nonsmooth-outputs-and-event-times.md) | 25.6 |
| `018000` | [Finite-element error bounds, equilibrated fluxes, and goal functionals](018000-finite-element-error-bounds-equilibrated-fluxes-and-goal-functionals.md) | 22.4 |
| `019000` | [Multigrid from near-nullspace to anisotropy](019000-multigrid-from-near-nullspace-to-anisotropy.md) | 21.2 |

## Sources and authoring

Per-lecture source records live in `metadata/`; the bibliography is in `metadata/sources.json` when present. Composition lineage and editorial revisions are recorded in per-lecture metadata and `provenance.yaml`. Original arguments and exact companions remain with their consolidated manuscript.

Read [the lecture style rules](../../LECTURE_STYLE_RULES.md) before changing narration. Use the spoken-region markers for extraction; keep raw mathematics, code, and source records in the non-spoken companion. Teaching preparation, proof dependencies, and historical influence are distinct.
