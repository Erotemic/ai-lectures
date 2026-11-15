# Agent C: analysis track — opening sequence and future boundary

**Ownership:** `draft-stages/tts-analysis/**`, `docs/planning/agent-c-analysis/**`, and optionally `tests/agent-c-analysis/**`. Everything else is read-only. This deliverable is a text-only ZIP overlay for the shared baseline.

## Completed opening sequence

| ID | Topic | Central mathematical result |
| --- | --- | --- |
| 001000 | Sequence convergence | Epsilon-N definition, limit uniqueness, boundedness, squeeze and counterexample to the 'small step implies convergence' fallacy |
| 002000 | Completeness and real numbers | Rational gap at sqrt(2), Cauchy convergence, least-upper-bound principle and its applications (retained existing source manuscript) |
| 003000 | Limits and continuity | Epsilon-delta estimates, relative-domain continuity, sequential criterion and limit algebra |
| 004000 | Consequences of continuity | IVT and bisection, Bolzano–Weierstrass subsequences, and EVT with proof of attained extrema |

These lectures constitute one coherent real-analysis opening. The track also covers complex analysis in its intended broader scope, but the first four recordings establish the real-number techniques used for later complex-variable reasoning. No premature complex analysis claims were inserted into the beginner sequence.

## Planned continuation (not indexed as available)

A sensible next sequence is 005000 differentiability and the linear approximation, 006000 the mean value theorem and rigorous error estimates, 007000 the Riemann integral and criteria for integrability, 008000 the fundamental theorem of calculus, and then finite-dimensional norms, metric spaces, uniform convergence, power series, and the complex plane. Introduce holomorphicity, Cauchy integrals, residues, and analytic continuation after the relevant real-analysis prerequisites. These are proposed topics, **not** empty files or manifest entries.

## Existing shared-test integration request

The snapshot's `tests/test_foundational_expansion_tracks.py` hardcodes exactly two lecture IDs and at least 3,000 spoken words for each lecture in every foundational track. The shared baseline was reportedly altered to expect only the previously available 002000 lecture, but either hardcoded count necessarily becomes stale as soon as Agent C adds manuscripts. This is a **shared-test defect**, not a reason to pad lecture prose to meet a count or edit the shared test from the Agent C fork. A separate baseline maintainer should change that global test to read the full list of expected IDs from the track manifest and check appropriate content and spoken-region quality rather than enforcing an arbitrary uniform transcript length. This request is recorded here; Agent C does not modify shared tests or reader code.

The overlay retains `002000-completeness-and-real-numbers.md` unchanged; it must already be present on the shared baseline. It introduces three new manuscripts and updates the per-track manifest to list all four actual lecture files. The real index is validated against the numbered files in the track directory, not by fabricating missing entries.
