# Category Theory: third arc — sheaves and topoi (2026-11-14)

**Status:** Two complete standalone lectures, `013000` and `014000`, with mathematical companions, references, source metadata, and manifest entries. They extend the existing 12-lecture course without changing its reader registration.

| ID | Question | Concrete example | Key theorem or calculation |
| --- | --- | --- | --- |
| 013000 | When do local sections determine global data? | Continuous functions on overlapping intervals; two differently labeled disconnected components | A sheaf is a presheaf with unique compatible gluing, equivalently an equalizer condition |
| 014000 | What can truth mean when mathematical data vary across regions? | Sierpinski two-point space with opens empty, {p}, X | Truth values in Sh(X), open-set Heyting logic, failure of excluded middle |

## Mathematical boundaries

- For sheaves, differentiate compatibility, existence, and uniqueness. The constant presheaf of two labels on a disconnected space is not a sheaf, whereas locally constant functions are a sheaf. The sheaf property does not guarantee arbitrary locally solvable data possess a compatible global solution.
- Define stalks as germs, not mere values at a point. Explain when stalkwise checks determine an isomorphism.
- The elementary topos definition requires finite limits, exponentials, and a subobject classifier. A poset of opens is a Heyting algebra, not automatically an elementary topos.
- In Sh(X), the classifier Omega assigns to each open V the open subsets of V, with restriction by intersection. Subobjects of the terminal sheaf correspond to open sets of X.
- For the Sierpinski topology, neg {p} is empty and double-neg {p} is X. This is internal Heyting reasoning; external membership in ordinary sets remains classical.

## Next directions

Enriched categories and Lawvere metric spaces offer a distinct concrete continuation. Other options are sheafification and adjunctions in more detail, sites and Grothendieck topologies, or categorical models of dependent types. The course can continue without forcing all of these into the same arc.

## Validation

Check the source records, all spoken regions and word counts, the existing API `category-theory` listing and transcript endpoints, and the mathematical calculations in the small finite topology. Audio generation and listening review are separate follow-up steps.
