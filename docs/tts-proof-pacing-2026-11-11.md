# TTS proof-body revision — 11 November 2026

This pass follows the [lecture-opening audit](tts-introduction-audit-2026-11-11.md).
It is a proof-pacing revision of seven recordings, using the snapshot after the
November 11 concept-first openings overlay. The focus is the inference that
connects an example to a theorem, not another introduction rewrite.

| Track/ID | Specific explanatory gap addressed | Revised derivation |
| --- | --- | --- |
| G2 `125000` | The frame factor appeared as abstract polar-decomposition algebra | Two-column frame on R3 with Gram spectrum 4, 1/16; explicit raw cross block, normalized sine and equality in the δ ε bound |
| G2 `126000` | The role of the squared norm was explained without exhibiting the multiplier's four denominators | Interlaced 2-by-2 spectra, entrywise gap calculation, Hilbert–Schmidt energy 28 vs 36, and failing operator-norm comparison |
| G2 `127000` | The Ritz principal-vector argument jumped from an inner product to a cosine | Explicit P_Z w=s z identity, residual pairing, projected test-vector norm c; corrected the opening's conflation of residual component with full residual norm |
| G2 `128000` | Cutoff convergence and leakage bound were stated more quickly than their mechanisms | Identity-versus-compact diagonal cutoff comparison; orthogonal square-energy splitting and exact deficit inequality; source rank hypotheses located |
| G3 `014000` | Graph normalization and the scalar Riccati equation needed a common numerical anchor | 3/4 slope producing sine 3/5 and cosine 4/5; exact small Riccati root for a 2-by-2 symmetric matrix |
| G3 `020000` | The Sylvester multiplier and the distinction between arbitrary and Ritz residuals remained implicit | Diagonal entry division, a 30-degree equality calculation, and a separate Ritz calculation with its own gap |
| G3 `021000` | The extra cosine in the tangent estimate was identified but not calculated explicitly | Residual and corrected projection vectors in the plane, with equality in the Cauchy–Schwarz step; why Ky Fan prefixes require a separate proof |

The display-only companions include the actual matrices and formulas. The G3
word counts in `draft-stages/tts-paper/track.json` are synchronized with the
canonical narration extractor. All original mathematical source declaration
excerpts and reference sidecars are retained.

## Further proof-body priorities

- G2 `129000`: inspect the direct-sum/Ky Fan step that assembles *two* crossed
  residual equations into an ambient projection bound. The constant-one step
  deserves a worked finite example and a careful block-to-prefix explanation.
- G2 `130000–131000`: explain the singular-value min–max argument for restricted
  displacement and where it stops applying to whole-space displacement.
- G2 `141000–144000`: audit the stated open questions and operator-functional
  calculus estimates for hypothesis fidelity and independent listening.

Validation is recorded in the overlay delivery. No changes to audio synthesis,
slides, visualizations, UI, or source formalization were made.
