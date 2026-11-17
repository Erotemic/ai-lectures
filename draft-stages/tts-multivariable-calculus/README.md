# Multivariable Calculus from First Principles

A calculation-first and proof-aware bridge from single-variable calculus and basic linear algebra to smooth manifolds, PDEs, optimization and vector calculus. The three existing consolidated manuscripts give the guided survey; four new quantitative deep dives explain Taylor errors, Hessian geometry and Newton methods with proofs.

## Listening routes

- **Foundations survey** (`multivariable-calculus:survey`): `001000`, `008000`, `015000`; this preserves the three-manuscript entry path.
- **Local Models and Newton Methods** (`multivariable-calculus:taylor-newton-bridge`): `019000`, `020000`, `021000`, `022000`; a worked continuation from second-order calculus to convergence proofs.
- **Full source sequence** (`multivariable-calculus:main`): all indexed manuscripts in `track.json` order.

The optional `navigation.json` separates introductory listening from depth; it does not replace the full source inventory or imply any proof prerequisites by itself. These are declared separately in each new lecture's `metadata/` sidecar.

## Current manuscripts

Durations below are descriptive measurements of spoken text at 145 words per minute, before synthesis; they are not composition targets.

| ID | Lecture | Approximate minutes | Route |
|---|---|---:|---|
| `001000` | [Local geometry and the total derivative](001000-local-geometry-and-the-total-derivative.md) | 44.9 | Foundations survey |
| `008000` | [Curvature, constrained extrema, and volume integration](008000-curvature-constrained-extrema-and-volume-integration.md) | 43.1 | Foundations survey |
| `015000` | [Integrating over curves, surfaces, and boundaries](015000-integrating-over-curves-surfaces-and-boundaries.md) | 27.4 | Foundations survey |
| `019000` | [Multivariable Taylor Remainders: From a Line to a Reliable Bound](019000-taylor-remainders-from-lines-to-bounds.md) | 12.7 | New local-model bridge |
| `020000` | [Hessian Geometry: Curvature, Convexity, and Conditioning](020000-hessian-geometry-convexity-and-conditioning.md) | 13.3 | New local-model bridge |
| `021000` | [Newton's Method for Systems and Optimization: Building the Step](021000-newton-method-for-systems-and-optimization.md) | 14.0 | New local-model bridge |
| `022000` | [Why Newton Converges: Remainders, Basins, and Safeguards](022000-newton-convergence-bounds-and-globalization.md) | 16.5 | New local-model bridge |

## Editorial boundaries and evidence

The old combined `001000`, `008000`, and `015000` manuscripts remain unchanged, including their inherited mathematical companions and consolidation provenance. The new manuscripts add quantitative material beyond the original Hessian survey: integral remainder estimates, strong-convexity bounds, a full nonlinear-system iteration, and a local quadratic-convergence proof. Worked examples, derivations and exercises appear in each non-spoken mathematical companion.

`track.json` is the authoritative inventory. Source records live in `metadata/sources.json`; per-lecture citation links, original authorship and teaching prerequisites live in `metadata/*.json`; authorship lineage and editorial changes live in `provenance.yaml`. Consult [`LECTURE_STYLE_RULES.md`](../../LECTURE_STYLE_RULES.md) before further authoring. No runtime pack build or audio synthesis is required for content handoff.
