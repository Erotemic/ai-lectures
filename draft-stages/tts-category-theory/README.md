# An Introduction to Category Theory

A concept-first, proof-bearing mathematics track with **34 standalone lectures** and a separate display-only mathematical companion for each recording. The course begins with sets, functions, and universal properties, then develops structures used in geometry, logic, semantics, and higher category theory. Each lecture builds from a concrete example into precise definitions and proof arguments.

**Audience:** A listener comfortable with functions, basic algebra, and following short proofs. The later lectures introduce advanced concepts, but explain their specific examples and conventions rather than relying on the wording of earlier recordings. Recordings can be listened to individually.

**Audio reader:** `/audio?track=category-theory` (existing identifier unchanged).

## Course index

| ID | Lecture | Mathematical focus |
| --- | --- | --- |
| 001000 | Categories and Composition: What Can Arrows Tell Us? | Objects, arrows, identities, associativity, isomorphism |
| 002000 | Functors: Translating One Mathematical World into Another | Functoriality, covariant and contravariant maps, full and faithful functors |
| 003000 | Natural Transformations: What Does It Mean to Work the Same Way Everywhere? | Naturality squares, natural isomorphism, canonical choices |
| 004000 | Universal Properties: Defining an Object by What It Does | Terminal objects, products, coproducts, uniqueness |
| 005000 | Limits and Colimits: Solving an Entire Diagram | Equalizers, pullbacks, pushouts, cones, gluing |
| 006000 | Adjunctions: Why Free Constructions Fit Forgetful Ones | Free/forgetful adjunction, hom bijections, unit and counit |
| 007000 | The Yoneda Lemma: Knowing an Object by All Its Relationships | Representable functors, Yoneda lemma, Yoneda embedding |
| 008000 | Monads: Making Structured Computations Compose | List and Maybe monads, Kleisli composition, monad laws |
| 009000 | Equivalence of Categories: When Different Descriptions Mean the Same Mathematics | Full, faithful, essentially surjective, quasi-inverses |
| 010000 | Monoidal Categories: Composition Side by Side | Tensor, associators, unitors, coherence, symmetry |
| 011000 | String Diagrams: Proving Equations by Following Wires | Interchange, typed wires, symmetry, copying and duality |
| 012000 | Categorical Logic: When Maps Behave Like Proofs | Exponentials, subobjects, quantifiers as adjoints, Heyting logic |
| 013000 | Sheaves: When Local Answers Become a Global Answer | Sheaf gluing, stalks, sheafification, local-to-global |
| 014000 | Topoi: Mathematical Universes with Local Truth | Subobject classifier, Sierpiński opens, internal logic |
| 015000 | Enriched Categories: How Distance Can Be Composition | Lawvere metrics, nonexpansive maps, shortest paths |
| 016000 | Ends and Coends: Compatibility and Identification | Naturality as end; coend quotient and identification |
| 017000 | Kan Extensions: Extending a Diagram Without Guesswork | Kan universal properties, comma categories, pointwise formulas |
| 018000 | Categorical Semantics: Types, Programs, and Universal Laws | Typed lambda calculus, CCCs, beta and eta equations |
| 019000 | Profunctors: Relations That Know How to Compose | Profunctor composition, coends, bicategory laws |
| 020000 | Enriched Yoneda: Recovering Distance from Every Point of View | Asymmetric metric Yoneda, enriched representables |
| 021000 | Weighted Limits: When a Diagram Asks More Than One Question | Functorial weights, kernel pairs, enriched weighted limits |
| 022000 | Dependent Types: Contexts, Substitution, and Comprehension | Categories with families, substitution, Σ and Π |
| 023000 | Algebraic Theories: What Does It Mean to Interpret a Monad? | Eilenberg–Moore algebras, list fold, finitary algebraic theories |
| 024000 | Fibrations: How Categories Vary with Their Contexts | Indexed categories, cartesian lifts, Grothendieck construction |
| 025000 | Identity Types: When Equality Has Structure | Identity elimination, transport, groupoid models, path objects |
| 026000 | Higher Categories: When Compositions Have Their Own Comparisons | 2-categories, bicategories, spans, associators and coherence |
| 027000 | Beck's Monadicity Theorem: When Structure Can Be Recovered from a Monad | Comparison functor, split coequalizers, conservative right adjoints |
| 028000 | Descent: Reconstructing Global Objects from Local Data | Transition cocycles, effective descent and faithfully flat modules |
| 029000 | Stacks: Gluing Objects Without Forgetting Their Symmetries | Groupoids, principal bundles, classifying stacks, quotient stacks |
| 030000 | Operads: How Operations Compose Inside Operations | Many-input substitution, symmetric actions, little disks |
| 031000 | Infinity-Categories: When Composition Has More Than One Witness | Inner horn fillers, nerves, mapping spaces and coherent composition |
| 032000 | Homotopy Limits: Why a Pullback Can Contain Loops | Path-space pullbacks, loop spaces, homotopy fibers and invariant limits |
| 033000 | Infinity-Operads: Algebraic Laws with Room to Deform | Little disks, E_n algebras, coherence and finite-pointed-set structure |
| 034000 | Derived and Higher Stacks: What an Intersection Can Remember | Derived tensor products, Tor, higher descent and deformation information |

## Authoring conventions

- Spoken manuscripts are marked with `BEGIN SPOKEN LECTURE` and `END SPOKEN LECTURE`. Exact formulas, exercises, and bibliography sit in a display-only mathematical companion after the spoken region.
- Each lecture supplies its own setting, notation, and hypotheses at the point they are used. It does not direct listeners to an earlier recording or to prompt-related authoring instructions.
- Begin with a specific mathematical construction; use small examples and work through at least one characteristic calculation or proof. State limitations when a general theorem needs hypotheses.
- Universal properties and constructions are not automatically preserved by all functors. Equality, equivalence, isomorphism, and coherent comparison are kept distinct.
- Metadata lives in `metadata/sources.json` and `metadata/<id>.json`; source URLs do not appear in speech.
- The course intentionally distinguishes homotopy-theoretic identity proofs from Lean's proof-irrelevant equality in `Prop`.

## Planning documents

- `docs/planning/category-theory-intro-track.md`
- `docs/planning/category-theory-second-arc.md`
- `docs/planning/category-theory-third-arc.md`
- `docs/planning/category-theory-fourth-arc.md`
- `docs/planning/category-theory-fifth-arc.md`
- `docs/planning/category-theory-sixth-arc.md`
- `docs/planning/category-theory-seventh-arc.md`
- `docs/planning/category-theory-eighth-arc.md`

## Further directions

Further directions include stable infinity-categories, the Dold–Kan correspondence, bar and cobar constructions, cotangent complexes, and carefully scoped treatments of cubical and univalent foundations. This track is extensible rather than intended to be an exhaustive treatment of category theory.
