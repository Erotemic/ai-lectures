# History track: Hermann Weyl long-form promotion

**Scope:** `005000` is promoted from the archived short portrait to a researched
long-form History recording. Its original six-digit ID is retained. The other
23 drafts remain excluded from the playable track.

**Spoken narration:** 5,035 extracted words; approximately 34.7 minutes at
145 words per minute. This is a duration estimate, not synthesized audio.
The narration builds from a two-by-two matrix counterexample into Weyl's
Hermitian eigenvalue inequalities, min–max and subspace gaps, high-frequency
spectral counting, essential spectrum, equidistribution, and group/gauge
symmetry. Equations and full references appear only in the companion and
metadata. No neighboring lecture is required for the narration to make sense
at its intended prerequisite level.

**Mathematical checks:** the companion derives the matrix-sum inequality,
validates the exact two-by-two eigenvalues and principal-vector rotation,
separates spectrum from essential spectrum using a diagonal compact operator,
computes the one-dimensional Weyl counting law, and distinguishes the 1918
length-gauge proposal from its quantum phase reinterpretation.

**Historical sources:** MacTutor and the Institute for Advanced Study for
biographical events; the Stanford Encyclopedia of Philosophy for the
broader mathematical and philosophical context; William Fulton's Bourbaki
survey for the 1912 matrix inequality; a centennial review of Weyl's law
for the original 1911 spectral asymptotic; accessible encyclopedia articles
for further reading. Their links and specific reading notes are in
`draft-stages/tts-history/metadata/005000.json` and the shared source catalog.

**Promotion mechanics:** the overlay creates the root lecture and its active
sidecar and removes `005000` from the deferred manifest. When applying to an
existing checkout, remove only the two obsolete archived copies with
`git rm` after extracting the ZIP. Preserve all other stubs.

**Out of scope:** rendering, TTS synthesis, slide redesign, or modification of
G2/G3 mathematics.
