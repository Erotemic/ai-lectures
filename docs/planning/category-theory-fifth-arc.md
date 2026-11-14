# Category Theory fifth arc — profunctors, enriched Yoneda, weighted limits, dependent types

**Status:** Four complete manuscripts numbered `019000`–`022000`, each with a spoken narration, non-spoken mathematical companion, examples, exercises, and research records. This overlay leaves the existing audio reader unchanged.

| ID | Central question | Running example | Formal result |
| --- | --- | --- | --- |
| 019000 | How can witness-bearing relationships compose? | Discrete catalog matches and a walking-arrow quotient | Profunctor composition via coends, hom identity, bicategory laws |
| 020000 | Can an object be reconstructed from its distance relations? | Three-point metric and two-point directed network | Metric/enriched Yoneda evaluation and isometric embedding |
| 021000 | How can one diagram answer different compatibility questions? | Employees and departments | Set-weighted limits, category of elements, explicit kernel pair |
| 022000 | How can a type depend on a term in a changing context? | Person-indexed access levels | Categories with families, reindexing, context comprehension; Σ/Π structure |

## Editorial and mathematical conventions

Each spoken lecture restates the definitions it needs, without referring the listener to another lecture. Concrete examples precede formal definitions and companions keep exact notation separate from the synthesized narration. No binary or generated image assets are included.

- The profunctor convention is `P:C^op × D -> Set` for a generalized arrow `C -> D`; the direction of each coend action is documented. Composition is associative and unital up to coherent natural isomorphism.
- The enriched Yoneda calculation compares **directed** profiles using Lawvere residuation; symmetric sup norms are marked as a special case. Infinite arithmetic is handled by residuation rather than undefined subtraction.
- The weighted-limit convention is **covariant weights** `W:J -> Set` for limits. The employee example uses a two-to-one weight; the result is the exact five-element kernel pair. A parallel-arrow example explains why compatible equalizer elements must also share the prescribed image.
- The categories-with-families lecture presents the *strict* substitution laws and distinguishes bare CwF structure from extra dependent sum, dependent product, identity-type and universe structures. It does not claim that the finite Set-family model validates every rule of Lean.

## Source and validation policy

Bibliographic records live in `draft-stages/tts-category-theory/metadata/sources.json`; per-lecture reading selections and anchored attributions in `metadata/019000.json`–`022000.json`. Validate spoken-marker extraction, manifest counts, source existence, audio reader retrieval, and the numeric examples. The mathematical companions are explanatory and do not claim to be Lean-checked formal proofs.

## Further extensions

- Algebraic theories, Eilenberg–Moore algebras, monad morphisms, and relations to proof-relevant computations.
- Fibrations, Grothendieck construction, indexed categories, and the connection between CwFs and comprehension categories.
- Categorical models of identity types and higher categories, with careful separation of extensional and intensional equality.
- Applicative interpretations: databases, lenses, enriched search and compositional program verification.
