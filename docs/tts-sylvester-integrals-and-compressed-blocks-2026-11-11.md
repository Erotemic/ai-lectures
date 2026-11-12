# G2 listening-first revision: Sylvester integrals through compressed blocks

11 November 2026. Incremental text-only overlay after
`ai-lectures-g2-schatten-ideals-sylvester-listening-polish-2026-11-11.zip`.

## Teaching thread

The recurring finite model uses A = diag(-2, 2), B = [0], C = (2, 4)^T,
and solution X = (-1, 2)^T. It has opposite-sign spectral differences,
gap 2, and equality in the constant-one square-norm estimate. Every lecture
reintroduces the example explicitly, so none depends on prior listening.
The final compressed-block lecture introduces its own two-dimensional
projection and Ritz examples because its unknown is geometric leakage.

## Changes by lecture

- `066000`: Explain relative unitary evolution before differentiating it;
  contrast decay from ordered spectra with two-sided oscillation from pairwise
  separation. Revisit the signed two-coordinate example in the Fourier
  reconstruction and distinguish the pi-over-two integral bound from the
  sharper Hilbert-Schmidt geometry.
- `067000`: Derive the resolvent cancellation in input/output order, use two
  circles to separate the left spectrum {-2,2} from the right spectrum {0},
  and evaluate an upper-triangular Jordan-block inverse. Keep the historical
  Rosenblum attribution, with its exact sidecar anchor updated for the new
  sentence.
- `068000`: Derive the bounded-inverse estimate through a contraction on
  cross-operators; distinguish an estimate for a given solution from the
  completeness required for a Neumann-series construction. Show why spectral
  distance alone does not control a nonnormal inverse norm.
- `069000`: Contrast one-column norm equality with the interlaced two-by-two
  operator-norm obstruction. Explain where Hilbert-Schmidt orthogonality
  enters, why the rank factor appears, and which hypotheses enable the
  ordered, interval/exterior, and general Fourier bounds.
- `070000`: Make the operator-on-operators picture explicit, including the
  rank-one Hilbert-Schmidt eigenbasis, spectral-block passage in infinite
  dimensions, and why ideal membership must be established before applying
  an ideal-norm estimate to a previously known bounded solution.
- `071000`: Derive the directed leakage identity with its domain and codomain,
  then work both the two-subspace perturbation and an independent Ritz
  example with projected residual 3/4, full residual sqrt(3)/2, and leakage
  1/2. Keep the unbounded-domain qualification separate.

All edits were confined to narration and display-only mathematical companions.
Existing Lean excerpts, reference-source IDs and lecture identifiers were
preserved. No production code, slide assets, audio, or binaries were changed.

## Validation

- All 156 numbered G2 and 27 numbered G3 transcripts extract through the
  repository narration extractor.
- Reference metadata validator: 156 sidecars, 51 historical anchors,
  1,207 source associations and 151 catalog sources.
- Focused regression suite: 70 passed, 1 skipped (Manim unavailable).
- Source-format extraction and reference-metadata unit tests: 8 passed.
- Independent numerical checks: opposite-sign diagonal solution, Jordan
  inverse, two-by-two norm obstruction, directed projection leakage and
  Ritz-residual identity.

## Possible continuation

The transition around `073000-082000` into functional calculus and unbounded
spectral integration remains a candidate for a similarly sustained
listening-first pass. Prioritize examples that bridge bounded step operators,
spectral measures and limiting arguments without burying the domain assumptions.
