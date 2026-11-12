# G3 coverage of the journal paper, and a proposed syllabus

Draft for review, 12 November 2026. All 32 lectures in §3 were rewritten the same day; see §6.

**Goal of G3:** a reader who works through the track masters everything in the
journal paper (`aiq-dkps-formalization/papers/dk_formalization_journal/`):
its background constructions, the sine-theta theorem with its exact hypotheses,
the 29 Davis–Kahan results in the appendix, the Proposition 4.4
counterexample and Q-norm repair, and the real trace-norm matching theorem.

G3 is written for its own audience, which knows linear algebra, singular values,
Hilbert-space notation and elementary measure theory. Topics overlap with G2,
but G3 lectures are written fresh rather than adapted from G2. The current 27
files are adapted G2 lectures (`source_g2` in `track.json`); they serve as raw
material and as a check on examples, not as the text to edit.

## 1. What the paper contains

The paper sections and appendix results, each with the place it would be
taught in the proposed syllabus (§3). IDs such as `DK-3.1-prop` are the
paper's appendix IDs.

| Paper content | Taught in |
| --- | --- |
| §2.1 Principal angles: overlap singular values are cosines; principal vectors and planes; canonical correlations; CS decomposition; Jordan, Hotelling, Björck–Golub, Stewart | G3-1 |
| §2.2 Rayleigh quotient, Ritz values, residual; Courant–Fischer; Weyl's inequality; the 2×2 swap example (eigenvalues stable, eigenvectors not; gap equal to perturbation) | G3-0, G3-8 |
| §2.3 Compression PQP, angle operators Θ0, Θ1, Θ; meaning of Θ ≤ c; right angles from unmatched directions; Halmos block form; four intersection spaces; defect spaces D0, D1; intertwining | G3-2, G3-3 |
| §2.4 Sz.-Nagy–Kato intertwiner T = QP + (I−Q)(I−P); T*T = I − (P−Q)²; acuteness ‖P−Q‖ < 1; polar factor as direct rotation; displacement I − W | G3-4 |
| §2.5 Spectral theorem and PVMs; Borel spectral projections; Hellinger–Toeplitz; domains; resolvent and Riesz contour projection; half-infinite spectral sets; residual R = ÂE0 − E0A0; sinΘ0 = (I − E0*PE0)^½; modulus of S equals sinΘ0 | G3-6, G3-7, G3-8, G3-2 |
| §2.6 Sylvester equation; scalar prototype; Λ1X − XA0 = F1*R; constant one needs ordered or interval/exterior positions; interlaced spectra need another constant | G3-12 to G3-15 |
| §2.7 Singular values; Schatten norms; operator ideals and membership; trace, Hilbert–Schmidt, operator norm rank transporters differently; the three Section-4 objectives; Davis 1958 extremality; Example 4.2; Bolotnikov–Li–Rodman; Grassmannian metrics | G3-10, G3-11, G3-24 |
| §2.8–2.9 The angle-estimate chain δN(sinΘ0) = δN(X) ≤ N(F1*R) ≤ N(R); Wedin, Björck–Golub, Stewart, Paige–Wei; Yu–Wang–Samworth and statistical use | G3-16, G3-H |
| §3 Sine-theta setup: E0, A0, F0, F1, Λ1; IsTrialResidual and IsExactSpectralDecomposition; interval/exterior and ordered (form) separation; both blocks unbounded (diag(n+δ), diag(−n)); common dense domain; normalized symmetric ideal norm, Ky Fan dominance; Rayleigh residual figure (diag(1.9, 0.7), θ = 40°); theorem and proof; sharpness | G3-16 |
| §4.1 Direct rotation: existence/uniqueness, square-root characterization, commutation, reversal, defect criteria, compact angle sequences | G3-4, G3-5, G3-3 |
| §4.1 Branch selection, Thm 8.1: ordered reference gap, off-diagonal H, gap survives, Θ ≤ π/4 iff block ordering, existence and uniqueness, repulsion inequality with cos Θ1 | G3-21 |
| §4.1 Smallness, Thm 8.2: central interval, ‖H‖ or ‖R‖ < δ/2 gives Θ < π/4, sin 2Θ bounds, equal defect dimensions | G3-22 |
| §4.2 Approximation numbers; symmetric norming functions; Ky Fan sums; restricted displacement singular-value minimality; Prop 4.3 | G3-10, G3-11, G3-24 to G3-26 |
| §4.3 Unbounded Sylvester: domain conditions; spectral cutoffs; convergence of approximation numbers; reflection pinching; direct-sum comparison; generalized theorems 6.1–6.3 | G3-15, G3-17, G3-20 |
| §4.4 Real and complex Hilbert spaces: complexification transfer | G3-18 |
| §5 Counterexample: construction; trace norms 4 sin θ < 8 sin(θ/2); operator norm reverses the order; global trace minimum via ‖P−Q‖₁ ≤ ‖I−W‖₁; failure of comparison (4.3) with shared output plane; Q-norms; realification of Example 4.2; Bolotnikov–Li–Rodman, Qiu, Zhang | G3-27 |
| §6 Matching theorem: costs e_ij, s_i; matching as maximum weight; 30°/45°/75° example; six-step proof (compactness, stationarity, spectral gradient, two-phase blocks, block costs, p → 1 limit) | G3-28 to G3-30 |
| Appendix A Notation | Reference only; used throughout |
| Appendix B: 29 results with hypotheses (table below) | Distributed |
| Appendix C Reading Lean signatures | Visual versions (decision 3) |

### The 29 appendix results

| ID | Result | Current G3 | Proposed |
| --- | --- | --- | --- |
| S2-sin-theta | Sine theorem | 020 (hypotheses stated by pointer) | G3-16 |
| S2-tan-theta | Tangent theorem | 021 | G3-20 |
| S2-sin-two-theta | Double-angle sine | 022 | G3-22 |
| S2-tan-two-theta | Double-angle tangent | 023 | G3-23 |
| DK-3.1-prop | Acute direct rotation existence/uniqueness | 005 | G3-4 |
| DK-3.2-prop | Nonacute existence iff dim D0 = dim D1 | not covered | G3-5 |
| DK-3.3-prop | Square-root characterization R² = (2Q−I)(2P−I) | 005, partly | G3-4 |
| DK-3.4-prop | Square as a direct rotation | not covered | G3-5 |
| DK-3.1-thm | Classification of pairs of subspaces | not covered | G3-3 |
| DK-3.1-cor | Compact classification by angle eigenvalues | not covered | G3-3 |
| DK-3.5-prop | Angle commutation, eigenspace geometry | not covered | G3-4 |
| DK-3.2-cor | Reversal symmetry | 005 | G3-4 |
| DK-4.1-prop | Restricted displacement, singular-value extremality | 017 | G3-24 |
| DK-4.1-cor | Unitarily invariant norm minimality, restricted | 017 | G3-24 |
| DK-4.2-prop | Basis-angle square sums | 018 | G3-25 |
| DK-4.3-prop | Squared full displacement minimality | 018500 | G3-26 |
| DK-4.4-prop | Printed full-displacement claim (refuted) | 019, 024 | G3-27 |
| DK-5.1-thm | Banach-space Sylvester bound | 010, partly | G3-12 |
| DK-5.2-thm | Semibounded self-adjoint Sylvester theorem | 009 | G3-13 |
| DK-5.1-lem | Strong-cutoff convergence of singular values | 012/013, partly | G3-11, G3-15 |
| DK-6.1-lem | Direct-sum norm comparison and converse | not identified | G3-17 |
| DK-6.2-lem | Reflection-pinch contraction | 007, partly | G3-17 |
| DK-6.1-prop | Symmetric sine theorem, δN(sinΘ) ≤ N(H) | not covered | G3-17 |
| DK-6.1-thm | Generalized sine (ε frames, unequal dimensions) | 020, briefly | G3-17 |
| DK-6.2-thm | Pairwise gap: Hilbert–Schmidt and √rank bounds | 010 | G3-14 |
| DK-6.3-thm | Generalized tangent | 021, partly | G3-20 |
| DK-6.3-lem | Finite-rank near-maximizer leakage estimate | not covered | G3-20 |
| DK-8.1-thm | Branch selection and repulsion | 016 | G3-21 |
| DK-8.2-thm | Smallness selects the acute branch | not identified | G3-22 |

"Current G3" is from section headings and a keyword screen of the extracted
narration. Each lecture is read in full when it is rewritten.

## 2. What is missing from the current G3

- **Two-subspace theory beyond the acute direct rotation:** Halmos's block
  form, the four intersection spaces, classification of pairs (3.1 theorem
  and corollary), nonacute existence (3.2), the square of a direct rotation
  (3.4), and angle commutation (3.5).
- **Eigenvalue versus subspace stability:** Weyl's inequality and the 2×2
  swap example, which motivates the whole theory and fixes why δ is compared
  with the perturbation.
- **Spectral projections in operator language:** the Riesz contour projection,
  resolvents, and Hellinger–Toeplitz (why self-adjoint and unbounded forces a
  proper domain).
- **Generalized sine results:** the symmetric sine theorem (6.1 proposition),
  the direct-sum and reflection-pinch lemmas, and the finite-rank
  near-maximizer lemma.
- **Smallness theorem 8.2:** how a small ‖H‖ or ‖R‖ selects the branch with
  Θ < π/4.
- **Real versus complex:** why spectral arguments go through
  complexification, and what transfers back.
- **The paper's own framing:** the lineage of each construction, related
  work (Bolotnikov–Li–Rodman, Qiu, Zhang, Wedin, YWS), and what the paper
  claims as new.
- **The matching proof at the paper's level of detail:** the current lecture
  compresses six steps into one recording.

The sine-theta lecture states its gap hypothesis by pointer ("one of the
supported separation conditions") and uses U, V, E rather than the paper's
E0, F0, F1, Λ1.

## 3. Proposed syllabus

Order follows mathematical dependency, not paper order. Since some
chronology is now allowed, later lectures can build on earlier ones and
share running examples, while each recording still states the data it uses.
IDs are placeholders; existing IDs would be reused where the topic matches.

**Orientation**

- **G3-0 The problem and the paper.** When a self-adjoint operator changes,
  what can still be trusted? Weyl and the 2×2 swap example. The residual
  form, the perturbation form Â = A + H and why ‖R‖ ≤ ‖H‖. The four angle
  theorems at a glance. The paper's three contributions: formalization,
  correction, matching. Rewrite last, once the rest exists.
- **G3-H The lineage of the constructions** (decision 2). Jordan → Dixmier,
  Davis → Halmos; Rayleigh → Ritz → Weyl; Rellich → Sz.-Nagy → Kato;
  Sylvester → Rosenblum; von Neumann → Schatten → Ky Fan; Davis and Kahan;
  then Wedin, Stewart, Bolotnikov–Li–Rodman, YWS.

**I. Geometry of two subspaces**

- **G3-1 Principal angles.** Overlap matrix, its SVD, principal vectors and
  planes; canonical correlations; CS decomposition. Introduces the 4D
  equal-angle pair used again in G3-27.
- **G3-2 Angle operators.** PQP, cos Θ0, sin Θ0, the full Θ; unmatched
  directions give right angles; S = (I − P)E0; modulus and polar
  decomposition give |S| = sin Θ0.
- **G3-3 Two projections and the classification of pairs.** Halmos's form,
  intersection and defect spaces, classification (DK-3.1 theorem and
  corollary).
- **G3-4 The direct rotation.** Sz.-Nagy–Kato intertwiner, acuteness,
  polar factor; existence/uniqueness, square-root characterization,
  commutation, reversal (3.1, 3.3, 3.5, 3.2 corollary).
- **G3-5 Nonacute pairs.** Defect spaces, existence iff equal dimensions,
  R² = −I on D0 ⊕ D1, nonuniqueness; square of a direct rotation (3.2, 3.4).

**II. The spectral side**

- **G3-6 Spectral subspaces and exact decompositions.** Finite picture,
  PVMs and Borel sets, half-infinite intervals, Riesz contour projection;
  reducing subspaces, blocks, F0, F1, Λ1.
- **G3-7 Unbounded self-adjoint operators.** Hellinger–Toeplitz, domains,
  form bounds on a domain, the ℓ² example where both blocks are unbounded.
- **G3-8 Trial subspaces and residuals.** Rayleigh quotient, Ritz values,
  R = ÂE0 − E0A0, invariance when R = 0, Galerkin orthogonality,
  perturbation form, unbounded trial data; the paper's 40° residual
  triangle.
- **G3-9 Gap geometry.** Interval/exterior, ordered, and distance-only
  separation; which one each later theorem needs.

**III. Norms**

- **G3-10 Unitarily invariant norms.** Singular values, symmetric gauges,
  Ky Fan norms, majorization, Ky Fan dominance; Q-norms defined here.
- **G3-11 Operator ideals.** Approximation numbers, Schatten ideals,
  membership, normalization, N(BT) ≤ ‖B‖N(T); strong-cutoff convergence
  (5.1 lemma).

**IV. Sylvester estimates**

- **G3-12 The Sylvester equation.** Scalar prototype, eigenvector
  denominators, Banach-space theorem (5.1 theorem).
- **G3-13 Ordered separation.** Semibounded self-adjoint theorem (5.2) and
  its integral proof.
- **G3-14 Interval/exterior and distance-only gaps.** Constant one where it
  holds; the 2×2 obstruction; Hilbert–Schmidt and √rank bounds (6.2
  theorem).
- **G3-15 Unbounded Sylvester identities.** Domains, filled cutoffs, passing
  the estimate to the limit.

**V. The sine-theta theorem**

- **G3-16 The sine-theta theorem.** Full statement with every hypothesis
  stated in content; proof chain; sharpness; reading the theorem's
  ingredients as the paper presents them.
- **G3-17 Generalizations of the sine theorem.** ε-frames and unequal
  dimensions (6.1 theorem); symmetric sine theorem (6.1 proposition);
  direct-sum and reflection-pinch lemmas.
- **G3-18 Real and complex scalars.** Complexification and transfer of the
  theorems.

**VI. Tangent and double-angle theorems**

- **G3-19 Graph subspaces and tangents.**
- **G3-20 The tangent theorem.** S2-tan-theta, generalized tangent (6.3
  theorem), near-maximizer lemma (6.3 lemma).
- **G3-21 Off-diagonal perturbations, branch selection and repulsion**
  (8.1).
- **G3-22 The doubled-sine theorem and smallness** (S2-sin-two-theta, 8.2).
- **G3-23 The doubled-tangent theorem.**

**VII. Transport, correction and matching**

- **G3-24 The transport problem and restricted displacement** (4.1
  proposition and corollary).
- **G3-25 Basis square sums** (4.2).
- **G3-26 Squared full displacement and the Q-norm repair** (4.3,
  Q-norm proposition).
- **G3-27 Proposition 4.4 and its counterexample.** The claim; the 4D
  family; operator norm reverses the order; global trace minimum; the failed
  Ky Fan comparison and the shared output plane; realification of Example
  4.2; related literature.
- **G3-28 The matching theorem: statement and meaning.** Costs, matchings as
  maximum weight, the 30°/45°/75° and paired 30° examples.
- **G3-29 The matching proof, I.** Compactness, stationarity along
  source-preserving rotations, the spectral gradient, two-phase blocks.
- **G3-30 The matching proof, II.** One- and two-angle block costs, the
  four-dimensional minimum, assembly into a matching, the limit p → 1.

That is 32 recordings. Several cover more than an old lecture did; none has a
length target.

### Running examples

Recurring examples, each restated where used:

- the plane with Â = diag(1.9, 0.7) and a 40° trial line (paper figure 1);
- the swap pair diag(0, ε) and diag(ε, 0);
- the 4D pair with two equal principal angles θ (the counterexample);
- the ℓ² operators diag(n + δ) and diag(−n);
- the three angles 30°, 45°, 75° in ℝ⁶ (paper figure 3).

## 4. Decisions for Jon

1. **Order.** Dependency order as above, or the paper's order (background,
   sine-theta, foundations, counterexample, matching)?
2. **History.** A dedicated lineage lecture (G3-H), short historical context
   inside each lecture, or both?
3. **Lean in G3 audio.** Keep Lean only in companions and visual versions,
   or add one spoken lecture on how the paper's formal statements encode
   hypotheses (partial maps for domains, ideal membership, bundled
   predicates)?
4. **Where to start.** Writing in order from G3-1 lets later lectures build
   on earlier ones. G3-0 is best rewritten last.

## 5. Mechanics to update when the track changes

`track.json` is the source of order. `tests/test_audio_course_tracks.py`
asserts exactly 27 lectures and the IDs and `source_g2` values of the last
six; those assertions change with the syllabus. Fresh lectures set
`source_g2` to null.

## 6. ID assignment and progress

Defaults taken when the revision started (12 November 2026), pending Jon's
review: dependency order; short history inside each lecture plus a lineage
lecture; Lean only in display companions; start at G3-1.

| Syllabus | ID | Replaces | Status |
| --- | --- | --- | --- |
| G3-0 orientation | 000000 | 000000 | rewritten |
| G3-H lineage | 000500 | new | rewritten |
| G3-1 principal angles | 003900 | new | rewritten |
| G3-2 angle operators | 004000 | 004000 | rewritten |
| G3-3 two projections, classification | 004500 | new | rewritten |
| G3-4 direct rotation | 005000 | 005000 | rewritten |
| G3-5 nonacute pairs | 005500 | new | rewritten |
| G3-6 spectral subspaces | 001000 | 001000, 007000 | rewritten |
| G3-7 unbounded self-adjoint | 011000 | 011000 | rewritten |
| G3-8 trial subspaces, residuals | 003000 | 003000 | rewritten |
| G3-9 gap geometry | 002000 | 002000 | rewritten |
| G3-10 unitarily invariant norms | 006000 | 006000 | rewritten |
| G3-11 operator ideals | 013000 | 013000 | rewritten |
| G3-12 Sylvester equation | 008000 | 008000 | rewritten |
| G3-13 ordered separation | 009000 | 009000 | rewritten |
| G3-14 distance gaps | 010000 | 010000 | rewritten |
| G3-15 unbounded Sylvester | 012000 | 012000 | rewritten |
| G3-16 sine-theta | 020000 | 020000 | rewritten |
| G3-17 generalized sine | 020500 | new | rewritten |
| G3-18 real and complex | 020700 | new | rewritten |
| G3-19 graph subspaces | 014000 | 014000 | rewritten |
| G3-20 tangent | 021000 | 021000 | rewritten |
| G3-21 branch selection | 016000 | 015000, 016000 | rewritten |
| G3-22 doubled sine, smallness | 022000 | 022000 | rewritten |
| G3-23 doubled tangent | 023000 | 023000 | rewritten |
| G3-24 restricted displacement | 017000 | 017000 | rewritten |
| G3-25 basis square sums | 018000 | 018000 | rewritten |
| G3-26 squared displacement, Q-norms | 018500 | 018500 | rewritten |
| G3-27 Proposition 4.4 | 024000 | 019000, 024000 | rewritten |
| G3-28 matching statement | 025000 | 025000 | rewritten |
| G3-29 matching proof I | 025500 | new | rewritten |
| G3-30 matching proof II | 025700 | new | rewritten |

`track.json` order follows the syllabus as lectures are rewritten; unrevised
lectures keep their old position until replaced. Rewritten lectures have
`draft_status: g3_rewrite` and `source_g2: null`.

The source reconstruction
`aiq-dkps-formalization/prose/distilled_literature/DavisKahan1970_part_III.tex`
is the primary reference for the 1970 statements; Lean anchors are checked
against the pinned Tau Ceti revision and the Davis–Kahan library.

### Findings for primary-source review

- **Section 7 doubled-sine factor.** Resolved: the original Section 7 residual
  line drops a factor 2 (proof-line slip); the stated theorem is correct and the
  lecture is unchanged. Noted as a LaTeX comment in the journal paper only.
- **Example 6.1.** The tangent-theorem lecture uses a 3×3 instance with the
  numbers the reconstruction reports for Example 6.1 (gap 1, tangent 1,
  residual 1/√2); compare with the printed example.

## 7. Second-pass review log

Each lecture re-read in full, in track order, as extracted narration (audio-first
test). This is the author's self-review; Jon's listening review is still pending
for every lecture.

| ID | Second pass | Changes |
| --- | --- | --- |
| 000000 | done | Interlaced-gap sentence now says "constant one in the operator norm". |
| 000500 | done | Björck–Golub: "numerical" not "stable" methods; Weyl 1912 described as the source of inequalities whose modern matrix form is stated. |
| 003900 | done | No changes; all numbers and claims re-checked. |
| 004000 | done | "Acute" now distinguishes the journal paper's convention (norm of P minus Q below one) from Davis–Kahan's defect condition. |
| 004500 | done | No changes; Halmos derivation, classification, shift example and compact case re-checked. |
| 005000 | done | Kato formula sentence no longer calls T unitary. |
| 005500 | done | Planar case: G is plus or minus one; the resulting maps are the plus and minus ninety degree rotations. |
| 001000 | done | Lambda zero: the theorem's hypotheses omit it, the paper does name it; stability claim narrowed to "comes with an estimate". |
| 011000 | done | Cutoff-pattern attribution narrowed to the paper's Section 6 appendix. |
| 003000 | done | No changes; Figure 1 numbers, Rayleigh–Ritz decomposition, Weyl and swap example re-checked. |
| 002000 | done | Theorem 8.2 hypothesis corrected (interval on the perturbed block Lambda zero, with A zero within delta over two of it). |
| 006000 | done | No changes; dominance sketch, Q-norm list and notation warning re-checked. |
| 013000 | done | No changes; membership discussion re-checked. |
| 008000 | done | Theorem 5.2 method no longer attributed to the source's own proof. |
| 009000 | done | Integral proof described as the course's proof, not necessarily Davis–Kahan's. |
| 010000 | done | No changes; Hilbert–Schmidt spectral argument and the 2x2 obstruction re-checked. |
| 020500 | done | No changes; ambient-limitation example, Lemmas 6.1–6.2 and Proposition 6.1 block bookkeeping re-checked. |
| 012000 | done | No changes; duality test, filled truncation and limit argument re-checked. |
| 020000 | done | No changes; statement re-checked against the journal paper's Theorem 1. |
| 016000 | done | Theorem 8.1 equivalence now states the equal-defect hypothesis. |
| 022000 | done | No changes; reflection argument (both gap conditions reduce to the Lambda zero / Lambda one window) and homotopy re-checked. |
| 021000 | done | No changes; identity (6.5), principal-vector inequality, Example 6.1 numbers and beam refinement re-checked. |
| 014000 | done | No changes; graph characterization and tangent singular values re-checked. |
| 023000 | done | No changes; Jacobi formula and beam bound re-verified numerically. |
| 020700 | done | Complexification multiplicity passages already corrected; transport costs re-verified numerically. |
| 017000 | done | Min-max step corrected: for every removed subspace some remaining unit vector has angle at least theta k. |
| 018500 | done | No changes; pinching proof, Q-norm consequence and square-root counterexamples re-checked. |
| 018000 | done | No changes; per-vector cosine bound (valid past ninety degrees) and trace argument re-checked. |
| 024000 | done | No changes; construction, lower bound and failed comparison re-checked against numerical verification. |
| 025000 | done | No changes; example costs and weights re-verified numerically. |
| 025500 | done | No changes; stationarity, complex-structure and kernel steps re-checked against the journal proof. |
| 025700 | done | No changes; block-cost reduction re-verified by brute force at p = 1.5 and p = 1. |
