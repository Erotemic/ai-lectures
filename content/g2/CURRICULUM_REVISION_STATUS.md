# Curriculum revision coverage — 11 November 2026

This ledger records the scope of the concept-first and reference revisions in
the extracted `ai-lectures` snapshot. It is an editorial coverage note, not a
production pipeline or an additional test system.

## Inventory and migration

- The supplied archive contained an extracted Git repository at the expected
  `visualizations/` project root, with usable history and a clean starting tree.
  No further `git filter-repo` operation was performed.
- The G2 TTS collection now contains **156** numbered audio-first lectures,
  including two newly introduced prerequisite lectures.
- The shared source catalog has **151** entries, including **82** Wikipedia
  topic articles. The **1207** lecture-to-source associations validate against
  all 156 sidecars. Every lecture has at least one focused Wikipedia
  reading; other existing references are retained. Reading notes remain outside
  the spoken regions.
- Historical attribution anchors and formal declaration excerpts in existing
  companions were kept. No new unverified Lean declaration was introduced.

## Editorial coverage

**New standalone explanations (2):** `072500`, `080500`.

- `072500`: weak convergence of vectors, weak and strong operator convergence,
  operator-norm convergence, coordinate projection counterexamples, and
  graph-norm convergence on the domain of an unbounded diagonal operator.
- `080500`: approximate eigenvectors, absence of actual eigenvectors for a
  multiplication operator, continuous spectrum, dense range, and the resolvent
  distance formula for self-adjoint operators.

**Revised existing lecture narrations (69):** `013000`, `014000`, `015000`, `016000`, `017000`, `018000`, `019000`, `020000`, `022000`, `023000`, `024000`, `025000`, `026000`, `027000`, `028000`, `029000`, `030000`, `031000`, `032000`, `042000`, `044000`, `046000`, `047000`, `050000`, `051000`, `052000`, `054000`, `055000`, `056000`, `057000`, `058000`, `059000`, `060000`, `061000`, `063000`, `064000`, `065000`, `066000`, `069000`, `070000`, `071000`, `073000`, `076000`, `077000`, `079000`, `082000`, `096000`, `107000`, `108000`, `109000`, `111000`, `112000`, `113000`, `114000`, `115000`, `116000`, `117000`, `118000`, `119000`, `121000`, `129000`, `131000`, `136000`, `138000`, `139000`, `140000`, `145000`, `148000`, `149000`.

The major change is a concept-first opening in the foundational, singular-value,
Sylvester, subspace-angle and application groups, using one concrete geometric
or matrix problem to introduce the lecture's objects. The remainder of the
already-developed lecture bodies is retained where coherent. Selective
spoken-text corrections remove a formalization aside from `096000` and a
broken transition from `119000`.

**Worked mathematics added to display-only companions (24 lectures):**
`013000`, `014000`, `015000`, `017000`, `018000`, `019000`, `020000`,
`025000`, `029000`, `060000`, `065000`, `107000`, `108000`, `109000`,
`111000`, `112000`, `114000`, `115000`, `116000`, `117000`, `118000`,
`131000`, `140000`, `148000`.

These include explicit matrices, domain/codomain-sensitive embeddings, Gram
and frame computations, a residual/Sylvester calculation, double-angle
identities, and a Procrustes minimization formula. The two new lectures each
have their own mathematical appendix as well.

**Existing lectures retained without transcript edits (85):**
`000000`, `001000`, `002000`, `003000`, `004000`, `005000`, `006000`, `007000`, `008000`, `009000`, `010000`, `011000`, `012000`, `021000`, `033000`, `034000`, `035000`, `036000`, `037000`, `038000`, `039000`, `040000`, `041000`, `043000`, `045000`, `048000`, `049000`, `053000`, `062000`, `067000`, `068000`, `072000`, `074000`, `075000`, `078000`, `080000`, `081000`, `083000`, `084000`, `085000`, `086000`, `087000`, `088000`, `089000`, `090000`, `091000`, `091250`, `091500`, `092000`, `092250`, `093000`, `094000`, `095000`, `097000`, `098000`, `099000`, `099500`, `100000`, `101000`, `102000`, `103000`, `104000`, `105000`, `106000`, `110000`, `120000`, `122000`, `123000`, `124000`, `125000`, `126000`, `127000`, `128000`, `130000`, `132000`, `133000`, `134000`, `135000`, `137000`, `141000`, `142000`, `143000`, `144000`, `146000`, `147000`.

This group contains the earlier concept-first batches, together with older
lectures whose existing examples and proof development were retained after the
course structure and introductory coverage review. Retention does not mean
those scripts were recorded and listened to again. For a future deep edit,
start from a specific confusing transition or mathematical error rather than
rewriting a previously accepted lecture solely for stylistic uniformity.

## Structural observations

The new convergence lecture connects the finite-coordinate cutoff examples to
strong and norm-resolvent arguments. The approximate-eigenvector lecture
connects multiplication-operator spectral measures to the difference between
eigenvalue and spectrum. The curated topic graph includes both new G2 nodes and
their mathematical prerequisite links. Stable existing identifiers are
unchanged.

The reference catalog covers prerequisite topics such as Hilbert spaces,
projections, principal angles, weak convergence, closed operators, the
Courant min-max principle, Sylvester equations and Procrustes alignment.
The specialized Davis--Kahan sources and original papers were not displaced by
introductory references.

## Validation and outstanding work

- Narration extraction check: **156 lecture scripts passed**.
- Reference metadata: **156 sidecars, 51 historical claim anchors,
  1207 resource links validated**.
- Audio-library, graph and companion-export tests: **65 passed**.
- Mathematical companion/model tests: **16 passed**.
- Additional audio/preparation and continuity test batch: **32 passed,
  one unrelated FFmpeg timing assertion failed**, reporting an output of
  2.9 seconds against a minimum of 2.99 seconds. No rendering logic was
  changed as part of this content pass.

**Editorial limit:** This pass adds concept-first development across the
high-priority groups, introduces two missing foundations, and completes a
reference association pass through the entire G2 corpus. It does not claim
that every original lecture body has undergone a fresh line-by-line rewrite
or that all possible listener comprehension issues have been exhausted.
Remaining feedback-driven work should focus on specific proof transitions,
mathematical corrections and TTS passages identified by listening to the
new recordings, rather than adding administrative checks or producing media
as part of this revision.
