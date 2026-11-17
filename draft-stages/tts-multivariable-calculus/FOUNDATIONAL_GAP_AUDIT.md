# Mathematics curriculum gap audit — foundation-first expansion

Date: 2026-11-17. Scope: the supplied `ai-lectures` source snapshot, the latest delivered multivariable-calculus pack through `062000`, and the separately delivered linear-algebra pack through `027000`. This is an editorial *coverage-and-pacing* audit, not a replacement of any source and not a claim to know concurrent unpublished work in other packs.

## Decision

**Yes: recent expansion has become too specialized relative to the amount of separately navigable introductory material.** Complete the promised mountain-pass/Palais–Smale/critical-scaling route (`063000`–`066000`) and **pause further advanced elliptic PDE expansion**. The next additions should be approachable, single-subject foundation lectures with concrete worked examples, explanations of notation and mistakes, and appropriate exercises.

No fixed lecture duration, word count, or forced topic quota is recommended. The issue is the relationship between assumed prerequisites and what a first-time listener can reasonably learn from the entry path.

## Evidence from the current source materials

| Pack/route | Observed structure | Gap indicated by the structure | What is already covered |
|---|---|---|---|
| `multivariable-calculus` | Before this batch, 47 indexed manuscripts; the introductory `survey` contains just `001000`, `008000`, `015000`; afterward 51 indexed, still three in the survey | Many foundational transitions occur inside lengthy, combined lectures while 12 later four-lecture routes develop specialist material | Total derivatives, inverse/implicit maps, multiple integrals, Jacobians, vector calculus, and integral theorems *are present*. They should not be described as absent. |
| `multivariable-calculus:001000` | One combined lecture contains seven parts, from limits through implicit functions | Separately guided worked development of differential maps, Jacobian composition and local solvability | Each subject receives an introduction and companion in the consolidated survey. |
| `multivariable-calculus:008000` | One combined lecture runs from Hessians and extrema through iterated integrals and change of variables | The connection between coordinate transformations, bounds and integration could use its own problem sequence | Multiple-integral change of variables is already introduced. |
| `multivariable-calculus:015000` | One combined lecture treats line/surface integration plus Green, Stokes and divergence | Orientation, flux signs and the cancellation of internal boundaries warrant slower examples | All four topics are explicitly present in the survey. |
| `differential-equations` (source snapshot) | 13 consolidated manuscripts; the initial `001000`, `004000`, `007000`, `010000` move from IVPs to PDE evolution | Standalone worked ODE techniques and elementary Fourier PDE boundary problems would make a gentler path to weak formulations | Separation, linear ODEs, oscillation, forcing, phase portraits and PDE evolution appear in the consolidated material. |
| `linear-algebra` | The source snapshot has 3 consolidated introductory manuscripts; the separate latest delivered operator/numerics pack has 15 | Strengthen small-matrix worked examples and projection before expecting spectral algorithms, KKT operators and weak PDEs | Elimination, maps, spectral methods and numerical factorizations are already represented. Do not overwrite the separate pack with the older snapshot. |
| `analysis` (source snapshot) | 44 manuscripts; `001000`–`012000` introduce convergence, continuity, differentiation, integration, compactness and uniform convergence in relatively granular units | Less urgent need for new abstract foundation lectures; stronger *application bridges* to function spaces may help | Basic real analysis and Lebesgue, L-p, Hilbert, weak/operator theory are substantially covered. |
| `numerical-analysis` (source snapshot) | 15 manuscripts, including initial error, conditioning, root-finding, linear algebra and interpolation | Coordinate numerical PDE examples with fundamentals rather than further abstract estimate refinements | Basic numerical error reasoning is already independently taught. |

These are findings about **accessibility and depth distribution**, not merely counts: the headings in the actual introduction manuscripts were inspected. Lecture counts alone cannot establish teaching quality. Any proposed new lecture should first review the relevant existing prose and companion examples to avoid duplicate treatment.

## Prioritized next writing work

### 1. Multivariable calculus: slower entry-to-advanced path

Preferred immediate next sequence, within this same pack only after checking other agents' edits:

- **Differentiation as a linear map:** compute real Jacobians of two- and three-variable maps, use directional increments to distinguish partial derivatives from differentiability, and compose maps using the chain rule.
- **Implicit and inverse functions:** a complete small nonlinear system, parameter dependence, local-versus-global invertibility, and why a singular Jacobian changes the question.
- **Multiple integration and coordinate change:** draw the region in words, choose integration order, derive polar/spherical Jacobians, use the determinant as local volume distortion, and verify a nontrivial example two ways.
- **Vector fields, flux and orientation:** gradients versus fluxes, line and surface parameterizations, normals, exact Green/Stokes/divergence examples, sign mistakes and conditions on the domain.

These are **new practice routes**, not a plan to replace `001000`, `008000`, or `015000` or to reintroduce legacy IDs as live manuscripts. They address the bridge from introductory calculus to the many deep-dive routes.

### 2. Differential equations: worked first course before nonlinear PDEs

Coordinate with the owner of `tts-differential-equations` and inspect the current pack before reserving IDs:

- Separable, linear and exact first-order equations, together with initial conditions and failure of uniqueness.
- Constant-coefficient second-order systems, oscillation, forcing, resonance, and interpretation of eigenmodes.
- Fourier sine/cosine series and separation of variables for a fixed-endpoint string and a heat equation, including why boundary conditions choose modes.
- Heat versus wave energy estimates, physical interpretation, and the precise step from classical to weak form.

These already appear in broad survey form. The goal is an *independent construction-level route* with calculations that can be followed before listening to `multivariable-calculus:033000` and later PDE analysis.

### 3. Function-space prerequisites: applications, not duplicated definitions

The Analysis track introduces L-p/Hilbert spaces and operators, and Multivariable `033000`–`036000` introduces weak solutions, weak convergence, and Sobolev compactness. An effective supplement would be a set of concrete practice problems connecting them: piecewise-smooth weak derivatives, integration by parts, orthogonal projection, energy norms, bounded oscillating sequences, and the exact point where a nonlinear weak limit requires strong convergence. Inspect both packs first.

### 4. Linear algebra: strengthen introductory stepping stones

The latest separately delivered linear-algebra bridge introduces substantial operator and numerical machinery. Before extending it further, consider slower examples of coordinate maps, change of basis, rank and nullity, orthogonal projection, least squares, eigenvectors and diagonalization. Do not duplicate the existing numerical-matrix route merely to increase lecture count.

## Subjects explicitly deferred for now

- Full concentration–compactness proofs and profile decompositions.
- Critical semilinear elliptic existence, energy quantization and bubble-tree arguments.
- Further elliptic boundary, potential, nonlinear regularity and geometric PDE theory.
- More advanced bifurcation and critical-point multiplicity without a demonstrated prerequisite need.

The existing specialist manuscripts remain useful to advanced listeners. They can sit behind clearly declared prerequisites while introductory routes become more navigable.

## Review rule for subsequent batches

1. Inspect the *actual manuscript*, not just a tag, title or cross-route link.
2. Identify one missing conceptual or worked transition that blocks an existing advanced lecture.
3. Write enough derivation and examples to make that transition understandable from declared prerequisites; no duration rule.
4. Put exact equations in non-spoken companions and keep audible narration self-contained.
5. Maintain source attribution, Wikipedia links where relevant, stable IDs, pack-local metadata and ordinary text-only ZIP handoffs.

## Follow-through: worked foundations added, 2026-11-17

The immediate multivariable-calculus recommendation was implemented as `067000`–`070000` and the `worked-multivariable-foundations-bridge` route. This is a **status update**, not a revision to the original dated source coverage observations above. The original three survey manuscripts were preserved. The four new manuscripts deliberately use simple examples and explicit calculation checks; no advanced PDE prerequisites are assumed. Further work should now shift toward the audited introductory differential-equations and concrete function-space gaps rather than resume critical-point PDE expansion.
