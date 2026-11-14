# Category Theory sixth arc: algebraic interpretation, indexed structure, and higher equality

**Status:** Four complete lectures, IDs `023000`–`026000`, with TTS manuscripts, display-only mathematical companions, exercises and answers, and reference sidecars. This is an additive extension of the existing Category Theory track.

| ID | Lecture question | Concrete entry point | Mathematical development | Critical distinction |
| --- | --- | --- | --- | --- |
| 023000 | What does it mean to interpret a monad coherently? | Adding or multiplying a list of prices | List-monad algebras, monoids, EM homomorphisms, free monoids, Lawvere theories | Finitary algebraic theories versus infinitary powerset algebras |
| 024000 | How can a category vary with a context? | Context-indexed role and document families | Slice pullbacks, cartesian arrows, Grothendieck construction, indexed categories | Strict reindexing versus pseudofunctorial reindexing |
| 025000 | Can different proofs of equality carry structure? | Transport between length-indexed vectors and multiple paths | Identity elimination, path induction, groupoid models, path objects | Intensional identity proof relevance versus Lean's proof-irrelevant `Prop` |
| 026000 | What if the comparisons between composites are mathematical data? | Functors and translations; witness-bearing spans | Strict 2-categories, horizontal and vertical 2-cell composition, bicategories, coherence | Strict associativity versus associativity up to coherent invertible 2-cells |

## Proof-bearing companions

The mathematical companions provide the typed algebra maps and unit/multiplication equations; construction and lifting property of cartesian arrows; identity eliminator and transport; and horizontal-composition, associator, and coherence calculations. The audio narration develops the motivating example before introducing each abstraction. All manuscripts are self-contained at the intended advanced-introduction level; they do not refer to previous recordings by number or chronology.

## Source policy

All bibliographic records are located in `draft-stages/tts-category-theory/metadata/sources.json`. Per-lecture resource choices and anchored historical or mathematical-scope statements are in `metadata/023000.json` through `026000.json`. Source URLs and proof details are outside the spoken lecture.

Principal references include Lawvere's *Functorial Semantics of Algebraic Theories* (1963), Eilenberg–Moore algebra treatments, Jacobs/fibration and indexed-category texts, Hofmann–Streicher's groupoid model, Awodey–Warren on path objects, the *Homotopy Type Theory* book, and Leinster's *Higher Operads, Higher Categories*.

## Subsequent possibilities

- Monadicity and Beck's theorem, including explicit examples where comparison functors fail to be equivalences.
- Descent and stacks, relating the Grothendieck construction back to sheaf gluing and groupoid-valued data.
- The theory of operads and compositional syntax; a compact introduction to higher categorical limits.
- A separate, carefully scoped thread on univalent and cubical foundations, distinguishing those from Lean's kernel.

## Acceptance criteria

- Audio manifest contains consecutive IDs `001000`–`026000` and accurate extracted word counts.
- New sources and local claim anchors resolve without modifying existing lecture contents.
- The four manuscripts have separate spoken and display-only regions with no URLs in the spoken audio.
- Exact explanations in companions match the conventions and mathematical hypotheses in the spoken manuscripts.
- Existing audio-reader registration and cache identity are preserved.
