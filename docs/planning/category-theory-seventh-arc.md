# Category Theory, seventh arc — Reconstruction and multivariable composition

This arc adds four independent but related lectures, `027000`–`030000`, to the existing `category-theory` track. It preserves the audio URL, previous manuscripts, and IDs. Each lesson has its own prerequisites, spoken region, mathematical companion, exercises, and source metadata.

## The sequence

| ID | Lecture | Learning outcome | Worked anchor |
| --- | --- | --- | --- |
| 027000 | Beck's Monadicity Theorem | Decide when a right adjoint is monadic; distinguish conservativity and creation of U-split coequalizers | Free-monoid comparison, failure for Set → 1, free-algebra coequalizer |
| 028000 | Descent | Build descent data and distinguish cocycle consistency from effectiveness | Möbius sign transitions, three-chart matrix cocycle, faithful-flat module reconstruction |
| 029000 | Stacks | Explain why isomorphism classes lose gluing information and formulate stack descent | Classifying stack of Z/2, circle's two bundle classes and automorphisms |
| 030000 | Operads | Compose many-input operations, distinguish symmetry from commutativity, and recognize operadic algebras | Tree substitution, associative and commutative operads, little disks |

## Review priorities

- **Monadicity:** `F ⊣ U`, induced monad `UF`, comparison `D → C^T`, and `U`-split coequalizers must keep their types and direction. Do not claim that monadic functors create every ordinary underlying coequalizer. The comparison uses an *equivalence*, with strict versions requiring stronger choices.
- **Descent:** retain the difference between local objects, actual transition isomorphisms, cocycle conditions, and proof of effective descent; distinguish a global object from a global trivialization. Faithfully flat module descent depends on the flatness and faithfulness hypotheses.
- **Stacks:** preserve automorphism groups; distinguish descent for morphisms and objects, groupoids versus isomorphism-class sets, and ordinary stacks versus algebraic or higher stacks.
- **Operads:** preserve the order of inputs, distinction between symmetric and commutative, and differences between strict equations and homotopy-coherent operations. Colored operads must type-check substitution.

## Further development

A future arc could explore derived/higher stacks, ∞-operads, bar and cobar constructions, operadic Koszul duality, or the interaction of dependent type theory with higher-categorical semantics. Those subjects should retain separate mathematical witnesses and concrete prerequisites rather than relying on naming them in succession.

## Source discipline

The bibliography records theorem sources and original foundational works. Historical or scope claims are anchored to exact spoken passages. External references are not spoken or presented as invented firsthand testimony. The core sources are Riehl's *Category Theory in Context*, the Stacks Project, Vistoli's descent notes, Beck's theorem sources, May's *Geometry of Iterated Loop Spaces*, and Loday–Vallette's *Algebraic Operads*.

## Validation

Use `tests/test_category_theory_track.py` for IDs, source anchors, speech extraction, and reader retrieval; also run the existing audio-course and course-graph tests. Audio synthesis and an actual listening pass are separate acceptance steps.
