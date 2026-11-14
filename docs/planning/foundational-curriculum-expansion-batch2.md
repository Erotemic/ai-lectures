# Foundational curriculum: second lectures (2026-11-14)

**Status:** Four complete narration manuscripts, display-only companions, track manifests, source sidecars, and reader regression tests. Continue the existing four tracks; no new audio reader endpoint or binary media is needed.

| Track | ID | Lecture | Main worked result | Next lecture |
| --- | --- | --- | --- | --- |
| The Making of the Modern World | 002000 | Across the Atlantic: The Columbian Exchange and Its Human Consequences | Compare biological transfer, institutional coercion, and unequal local outcomes | Reformations, scientific communities, and the early modern state |
| The Physical World | 002000 | Where Does the Energy Go? Conservation, Work, and Heat | Work-energy theorem and ideal falling-weight calorimetry | Entropy and the direction of heat flow |
| Analysis from First Principles | 002000 | The Number Line Without Gaps: Completeness and the Real Numbers | Rational gap at sqrt(2), Cauchy condition, supremum and monotone convergence | Epsilon-delta limits and continuity of functions |
| Numerical Analysis and Reliable Computation | 002000 | Small Errors, Large Consequences: Rounding and Error Propagation | Binary64 nonassociativity, gamma-n bound, stable radical evaluation | Conditioning and backward stability in linear systems |

## Teaching requirements

- Every lecture explains its basic objects and central question within the recording; no audible reference to a previous lecture is required.
- Keep mathematical formulas and proof details in the display-only companion when spoken notation would be hard to follow. A spoken calculation still explains the variables, scale, assumptions, and conclusion.
- The historical lecture separates global ecological consequences from the agency and suffering of particular communities. Avoid unsupported universal mortality rates and overly tidy causal narratives.
- The physical lecture distinguishes mechanical energy conservation from the first law for a defined system and anticipates the second law without claiming the first law determines thermodynamic direction.
- The analysis lecture specifies when a limit lies in Q versus R, and does not conflate existence of a real root with an exact rational output of a numerical algorithm.
- The numerical lecture explicitly distinguishes floating-point arithmetic, input uncertainty, and problem conditioning. Any error bound states the hypotheses under which it applies.

## Implementation notes

The track IDs remain `modern-world`, `physical-world`, `analysis`, and `numerical-analysis`; new lecture IDs are `002000` in each track. Existing audio-reader registration uses manifest/discovery and needs no additional runtime changes. Source catalog entries and claim anchors are per-track. New text is original narration and no binary assets are included.

## Validation checklist

1. Spoken-region extraction matches stored word counts and excludes URLs and appendices.
2. All source IDs resolve and each recorded historical anchor occurs in speech.
3. Exact arithmetic checks confirm the stated floating-point counterexamples and energy calculation; check completeness counterexamples and proof hypotheses.
4. API listing and transcript routes work for both lectures of each track, and cache paths stay isolated by track.
5. Exercise and companion text remain display-only; no voice synthesis is claimed without generating audio.
