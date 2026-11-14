# Introduction to Category Theory — curriculum and review plan

**Status:** Eight complete first-pass manuscript drafts with mathematical companions, source sidecars, and reader integration. Editorial listening and audio synthesis have not been completed.

## Why this track

Category theory offers a precise language for how mathematical structures relate, how constructions behave under maps, and why universal solutions are unique up to canonical isomorphism. Its introduction should not assume that abstraction itself is sufficient motivation. The course uses functions, small posets, finite lists, groups, vector spaces, and compatible records to build the need for each new notion.

## Teaching arc

1. **Composition and identity:** Which kinds of arrows form a category? Why do source/target typing and associativity matter?
2. **Functoriality:** How do translations carry both objects and arrows? Which information is preserved or forgotten?
3. **Naturality:** What makes a family of comparison maps coherent across every arrow? Why do arbitrary choices interfere?
4. **Universal properties:** Can a construction be specified by a unique factorization requirement rather than a representation?
5. **Limits and colimits:** How do we impose compatibility constraints or glue along a shared source?
6. **Adjunctions:** How can two kinds of mapping problems express the same choices? What do units/counits record?
7. **Yoneda:** How does the identity arrow determine natural transformations out of a representable functor? Why are objects recoverable up to isomorphism from their hom functors?
8. **Monads:** How do functors, natural transformations, and adjunctions provide associative composition for structured outputs?

These titles form a coherent **introductory core**, not a complete survey of contemporary category theory. An advanced successor could cover equivalences and skeletons, monoidal categories, enriched categories, sheaves, and topoi. The primary challenge for a future expansion is selecting examples that justify each abstraction at a listening pace.

## Mathematical review checklist

- In every statement, identify domain, codomain, variance, and size hypotheses when relevant.
- For a candidate functor verify preservation of identities and composition; do not confuse full, faithful, and reflecting isomorphisms.
- For a natural transformation verify the naturality square for a general arrow, not a single object.
- For a universal construction separately verify existence and unique factorization; identify the category in which it lives.
- For adjuncts verify the direction of \(F\dashv U\), naturality of the hom bijection, and both triangle identities.
- For Yoneda verify variance and the formula determined by the identity arrow.
- For monads verify naturality, both unit equations, and associativity; distinguish pure mathematical models from programming-language operational semantics.

## Production validation and remaining work

- Validate the exact spoken marker extraction and word-count agreement with track metadata.
- Validate source IDs, related-resource visibility, and anchors for any historical claims.
- Validate all eight lectures are retrievable under the isolated audio track, including their transcript text.
- Run the project's existing audio/track integration tests against the new registration.
- After generating audio, listen to the opening, proof-heavy middle, and conclusion of every episode for pronunciation, pacing, and awkward page boundaries. Revise the narration as necessary before treating these drafts as published audio.

The manuscripts, companions, and source metadata are independently reviewable.
