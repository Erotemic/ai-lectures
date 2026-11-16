# 022200 — Sheaves: Local Information That Knows How to Glue

**Track:** Topology and Geometry. **Background:** topological spaces, functions on open sets, vector bundles. **Central question:** what extra structure turns local formulas into globally consistent objects?

<!-- BEGIN SPOKEN LECTURE -->

# Sheaves: Local Information That Knows How to Glue

Suppose we want to solve a differential equation on a circle. On every short arc we may find a solution. But these local solutions may disagree on overlapping arcs. Even if they agree locally in pairs, the global problem can have an obstruction when we return to the starting point. What language can express local existence, agreement on overlaps, and failure to construct a global object?

A sheaf does this in a remarkably economical way. It assigns a collection of objects to each open set, lets us restrict them to smaller open sets, and specifies when compatible local objects glue uniquely into one on a union.

## Assign information to an open set

Take a smooth manifold. For every open region U, let F of U be the set of smooth real-valued functions defined on U. If V lies inside U, restricting a smooth function from U to V gives a function on V. Restriction from U to itself does nothing, and a sequence of restrictions agrees with direct restriction.

This is a presheaf: a systematic assignment of data to open regions with restriction maps that compose correctly. The word may sound technical, but the operation is as familiar as cropping a map to a smaller neighborhood.

A sheaf is a presheaf that also satisfies two gluing principles. First, if two global objects have the same restrictions on every member of an open cover, they are equal. Second, if we have an object on every member of a cover and all the objects agree on overlaps, there is one global object restricting to each of them.

For smooth functions both principles hold. Agreement on overlaps lets us define a function on the union point by point, and smoothness is a local property. The same logic works for continuous functions, smooth differential forms, and sections of a fixed vector bundle.

## A presheaf that is not a sheaf

Consider an assignment that gives the real numbers to every nonempty open set, interpreted as one globally constant number, with identity restriction maps wherever possible. Take an open set consisting of two disconnected intervals. On the first interval choose the number one. On the second choose the number two. The overlap is empty, so compatibility imposes no relation. But the original assignment permits only one number for the whole disconnected union.

The gluing axiom fails. The associated sheaf repairs this defect by allowing locally constant functions, which can take different values on different connected components. This example separates the words constant and locally constant in a way that becomes important when we compute cohomology.

For a connected circle, a locally constant real function is constant everywhere. On a disconnected union it need not be. The sheaf remembers this difference without changing the definition of restriction.

## Look at germs near a point

Sometimes we care only about a function's behavior arbitrarily close to one point. Two functions defined on possibly different neighborhoods have the same germ at p if they agree on some smaller neighborhood of p. The set of all such germs is the stalk of the sheaf at p.

For the sheaf of smooth functions, a stalk is the collection of smooth-function germs, not merely numerical values at p. The functions x and x squared have the same value zero at the origin but different germs. Their derivatives and higher local behavior distinguish them.

A stalk is assembled as a direct limit over shrinking neighborhoods. This construction turns the restriction maps into a precise notion of infinitesimal local information. A morphism of sheaves is an isomorphism if and only if it is an isomorphism on every stalk. Exactness of sequences of sheaves can also be tested on stalks.

## Sections of a line bundle

Take a nontrivial complex line bundle over the sphere. On two disks it has local frames, and a section can be described by one function on each disk. On their overlap, the functions are related by the line bundle's transition function. The sheaf of sections packages these local descriptions without demanding one global frame.

This connects sheaves to the earlier bundle-gluing lectures. The transition function tells us how local coordinates compare. The sheaf tells us which local sections exist and whether compatible sections glue. A line bundle and its sheaf of sections carry closely related information, but it is useful to distinguish them: the sheaf tracks sections on every open set, not just the bundle's fibers.

## Local solutions may not become global solutions

Consider the differential equation df equals a closed one-form alpha. On a small enough contractible neighborhood, the Poincaré lemma supplies a local primitive f. On overlaps, two primitives differ by a constant. Their constants may fail to fit into a globally consistent collection.

On a circle, the one-form d theta has local primitives, but no single-valued global primitive. If there were one, integrating its derivative around the circle would be zero, whereas the integral of d theta is one full turn. The difference between local solvability and global solvability is not a minor exception: it is a central reason cohomology exists.

Sheaf cohomology generalizes this situation. It records obstructions to gluing and higher relations among local pieces. But before introducing higher cohomology, the sheaf axioms tell us exactly what the basic objects and their local behavior are.

A sheaf is neither merely a collection of functions nor a synonym for a bundle. It is a disciplined account of what can be known locally, how that information restricts, and what it takes to make a consistent global object. That is the missing language behind many constructions in geometry, analysis, and algebraic topology.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

A presheaf F assigns to each open U a set/group/module F(U) and to V⊂U a restriction `ρ_{UV}:F(U)→F(V)` with `ρ_{UU}=id` and `ρ_{VW}ρ_{UV}=ρ_{UW}`. A sheaf additionally satisfies uniqueness and existence of glued sections from matching families on an open cover. The stalk `F_p=colim_{p∈U}F(U)` consists of germs.

For smooth M, `U↦C∞(U)` and `U↦Ω^k(U)` are sheaves. The constant presheaf `U↦R` fails gluing over disconnected unions; its sheafification is the constant sheaf `R_M` of locally constant functions. A short exact sequence of sheaves is exact at stalks; it need not yield a short exact sequence of global sections.

### Exercises with answers

1. Why is the presheaf of one constant number per open set not a sheaf on disconnected opens? **Answer:** compatible different constants on disjoint components cannot glue to one constant.
2. Are a function's value and its germ at a point the same? **Answer:** no, distinct local functions can agree at the point yet have distinct germs.
3. What makes a section over two overlapping bundle charts global? **Answer:** the local coordinate sections agree after applying the bundle transition function on the overlap.
4. Why can a closed one-form have local primitives but no global primitive? **Answer:** local primitives may differ by constants that fail a global compatibility condition, detected by a nonzero period.

### Sources and further reading

- Ravi Vakil, [The Rising Sea: Foundations of Algebraic Geometry](https://math.stanford.edu/~vakil/preprints.html), Chapter 2, on sheaves and stalks.
- [Sheaf (mathematics)](https://en.wikipedia.org/wiki/Sheaf_(mathematics)); [Stalk (sheaf)](https://en.wikipedia.org/wiki/Stalk_(sheaf)).
