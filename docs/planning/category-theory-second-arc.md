# Category Theory: second arc (lectures 009000–012000)

**Status:** Four completed first-pass lecture manuscripts with display-only mathematical companions, exercises with answers, source sidecars, and manifest entries. Audio rendering and listening remain outstanding.

## Why a second arc

The first eight recordings establish categories, functors, natural transformations, universal properties, limits, adjunctions, Yoneda, and monads. The second arc asks what the foundational concepts let us *do*: recognize when two presentations capture the same mathematics, assemble processes in parallel, prove equations by manipulating typed diagrams, and describe logical rules using categorical universal properties.

These four recordings continue the category-theory track instead of creating a separate top-level category. They retain its audience: a listener comfortable with elementary algebra and functions who has worked through the categorical basics. Each lecture reminds listeners of its local prerequisites through examples, without a spoken “previous lecture” dependency.

| ID | Learning question | Concrete starting point | Main result | Critical limitation |
| --- | --- | --- | --- | --- |
| 009000 | When are two categories the same for structural purposes? | Finite sets and standard representatives | Equivalence via quasi-inverse; full + faithful + essentially surjective (classical setting) | Choice can be needed to choose a quasi-inverse; equivalence need not be strict isomorphism |
| 010000 | How do processes compose in parallel? | Product of two functions | Monoidal bifunctor, associator/unitor, coherence; symmetry when supplied | A tensor need not allow swaps, copying, deletion, or arbitrary regrouping without the relevant laws |
| 011000 | When can pictures prove equations? | Typed function wires and boxes | Diagram interpretation; interchange, naturality of symmetry, copy naturality in Set | Crossing, splitting, bending, and feedback require further structure |
| 012000 | Can logical inference be expressed categorically? | Predicates as subsets of a finite set | Subobjects, exponentials, subobject classifier, \(\exists_f\dashv f^*\dashv\forall_f\) in Set | Categories differ in available constructions; internal logic need not be Boolean |

## Teaching and mathematical review

The spoken text develops the problem before the abstract definition, with an audible calculation and a failure case. The companion records exact typed equations and exercises. Keep proofs of the highest-risk statements explicit:

- **Equivalence:** distinguish isomorphism of objects, strict isomorphism of categories, and equivalence of categories. Use the finite-set skeleton and automorphism-group obstruction. State the appropriate role of choice.
- **Monoidal:** check tensor is a bifunctor and identify the unit and coherence isomorphisms. Distinguish cartesian product and disjoint union on Set; do not assume every tensor is cartesian.
- **String diagrams:** specify top-to-bottom convention and left-to-right tensor order, and explain which graphical moves are legal in plain, braided, symmetric, rigid, or traced settings. Keep the linear-algebra verification of interchange.
- **Categorical logic:** keep the two semantics (types as objects and predicates as subobjects) distinct. In Set check the directions of the two adjunctions for inverse image; use the empty-fiber test for universal quantification. Treat the three-element Heyting algebra of open sets as an example of intuitionistic propositional logic, not as a topos by itself.

## Sources and provenance

The existing bibliography remains in `draft-stages/tts-category-theory/metadata/sources.json`. New records cover equivalences (nLab), graphical monoidal calculus (Peter Selinger), and categorical logic (Steve Awodey's course and notes). Existing textbooks by Leinster, Mac Lane, Riehl, and Fong–Spivak supply background and independent perspectives. Named historical/scholarly attribution in narration is anchored in the corresponding per-lecture sidecars.

Sources are reference material and are not fed to TTS. The teaching text is original narration, not a reproduction of source chapters. All mathematical companion notation and source URLs occur after the end-of-spoken marker.

## Production and review

1. Apply the new transcripts and metadata to a repository that already contains the first eight lectures and reader registration.
2. Check spoken-region extraction, recorded counts, source IDs and anchors, every manifest row, and retrieval through `/audio?track=category-theory`.
3. Run tests against the installed reader; these should cover twelve lectures and isolated TTS cache namespaces.
4. Before publication, generate audio and listen to difficult sections, especially equivalence versus isomorphism, associator/pentagon, crossings and duals, and the two directions of quantifier adjunction. Adjust pacing based on actual synthesis rather than estimated speech duration.

## Natural next topics

The most useful continuations are sheaves and local-to-global reasoning; topoi and their internal logic; enrichment and Lawvere metric spaces; categorical models of algebraic theories; and, only after concrete motivations are established, bicategories and Kan extensions. The next track design decision should be driven by how listeners handle the current abstract examples, not by a need to cover every categorical notion in a fixed number of episodes.
