# G2 listening-first polish: Schatten ideals and Sylvester estimates

11 November 2026. Incremental editorial pass after `ai-lectures-g2-g3-listening-polish-2026-11-11.zip`.

## Revised lecture narrations

- `057000`: Carry finite singular-value measurements into the compact diagonal example \(D e_k=e_k/k\); distinguish operator-norm, Hilbert–Schmidt, and trace-class membership using actual truncations. Unpack the Ky Fan / gauge / Minkowski triangle-inequality steps.
- `058000`: Compare ordered lists \((3,2,1)\) and \((4,1,1)\) to distinguish weak majorization from coordinatewise domination. Explain two-sided ideal compatibility separately from unitary invariance of a fixed matrix size.
- `059000`: Use one rectangular map with stretches four and two throughout; distinguish source versus output Gram zero multiplicities and mere padding versus compression. Correct the opening's earlier mistaken implication that adding an output row necessarily lengthens the source-indexed singular-value list.
- `060000`: Use the same real symmetric matrix throughout the pinching argument. Its singular values \((7,1)\) become \((3,3)\), so the second individual singular value grows while both Ky Fan prefix sums decrease. Relate reflection averaging to direct-sum formulas without conflating the operations.
- `061000`: Explain why Loewner comparison is a vectorwise hypothesis, why source Gram operators remain comparable for maps with different codomains, and why noncommutative squaring is invalid.
- `062000`: Distinguish the spaces acted on by the two Sylvester coefficients. Explain why entrywise gap division proves a Frobenius bound but does not, by itself, prove the corresponding sharp operator-norm claim.
- `063000`: Align the opening denominators with the same two-by-two example used in the full calculation and show one signed entry before doing the others.
- `064000`: Align the introductory eigenvalue lists with its diagonal vectorization example. Distinguish the order of denominators before and after column-stacking and separate invertibility from conditioning.
- `065000`: Describe the left/right exponential flow before the integral, clarify cancellation of the arbitrary spectral cut, and motivate the dimension-free constant.
- `068000`: Improve the bounded-inverse mental model, remove an implicit previous-lecture reference, and distinguish bounded-operator Neumann-series convergence from convergence in a complete ideal norm.

Six companions (`057000` through `061000`, plus `063000`) gained explicit displayed calculations. Other existing companions and Lean excerpts were retained.

## Reference sidecar repairs

Thirteen existing historical attribution anchors had drifted from earlier narration revisions. Reanchored `068000` and `124000`, `127000`, `130000`, `132000`–`135000`, `137000`, `142000`–`144000`, and `146000` to exact excerpts of the current extracted narration. Source IDs, locators, historical claims and audit statuses are unchanged. This restores the shared reference validator without reintroducing production or provenance narration.

## Validation

- G2 source narration extractor: all 156 numbered transcripts parsed; the 27 numbered G3 narrations also extract.
- Shared reference validator: 156 sidecars, 51 claim anchors, 1,207 related-resource associations, 151 catalog sources.
- Focused tests: 96 passed in the final relevant regression pass.
- Algebraic/numerical examples were checked: infinite diagonal truncations, weak majorization, rectangular Gram padding, pinching singular values, noncommutative Loewner squaring, and the two-by-two Sylvester solution.
- No audio synthesis, slides, or runtime production code changed.

## Further listening-first priorities

The adjacent `066000`–`071000` lectures connect exponential representations, Rosenblum theory, norm dependence, and cross-block Sylvester identities. Their main remaining opportunity is to carry one chosen spectral example through multiple estimates, making the norm and gap hypotheses audible. The spectral-calculus transition in `073000`–`082000` is a further candidate for a sustained argument-level review.
