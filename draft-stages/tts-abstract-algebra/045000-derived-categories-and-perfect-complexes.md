# 045000 — Derived Categories and Perfect Complexes on Schemes

**Track:** Abstract Algebra. **Background:** chain complexes, exact sequences, Tor, projective modules, coherent sheaves. **Central question:** what must we preserve when two complexes give the same cohomology, and which complexes behave like finite-dimensional vector bundles?

<!-- BEGIN SPOKEN LECTURE -->

# When the object is an entire complex

In ordinary linear algebra an object is a vector space, and a map is a linear transformation. In homological algebra an object can be a sequence of modules with maps between them. Each map is followed by another, and the composition of consecutive maps is zero. We call this a chain complex. It contains the data of cycles, boundaries, and cohomology, but often much more data than those groups alone reveal.

A simple example comes from multiplication by an integer n. Put a copy of the integers in one position, another copy in the next, and connect them by multiplication by n. When n is nonzero the only cohomology is the integers modulo n in degree zero. The complex is a resolution of that quotient module. It is not the quotient module written in a more complicated font: it is a concrete way to compute operations that are not exact.

Why not simply replace every complex with its cohomology groups? Because those groups do not always determine how the complex interacts with other complexes. Extensions can be encoded in the placement and attachment of pieces. We need a notion of equivalence that forgets irrelevant choices of resolutions but retains information needed for derived operations.

## Quasi-isomorphisms and the derived category

A map of complexes is called a quasi-isomorphism if it induces an isomorphism on every cohomology group. In the derived category we formally allow such maps to be inverted. The point is not that every chain map acquires a literal inverse. Rather, objects are compared by chains of maps whose induced cohomology maps are isomorphisms, and we construct a category in which those comparisons become genuine isomorphisms.

This is why projective resolutions are useful. A module and any projective resolution of it represent the same object of the derived category. We can choose a resolution suited to calculation, without pretending that a particular choice is part of the underlying mathematical object.

What survives the passage to the derived category is more than just a table of cohomology dimensions. For instance, the derived tensor product keeps track of higher Tor groups. Tensoring the two-term resolution of integers modulo n with integers modulo n turns the multiplication-by-n differential into zero. Now there is cohomology in two adjacent degrees. One copy is the ordinary tensor product; the second records Tor. If we had applied ordinary tensor product without resolving, we would have missed that second contribution.

## Cones and exact triangles

In ordinary homological algebra a short exact sequence leads to a long exact sequence in cohomology. The derived category packages this phenomenon using a mapping cone. Given a map from complex A to complex B, its cone measures how far that map is from being an equivalence. A map is a quasi-isomorphism precisely when its cone has zero cohomology.

The cone fits into a distinguished triangle: A goes to B, B goes to the cone, and the cone goes to the shifted complex A. The word triangle does not mean a diagram of three ordinary short exact sequences. It describes a structure with a shift operation and axioms designed to encode long exact cohomology sequences.

One useful mental model is that an ordinary quotient works when a subobject is embedded cleanly, while the mapping cone provides a homological quotient even when the original map is not injective. This analogy is suggestive, not a substitute for the construction.

## Perfect complexes as finite objects

On an affine scheme built from a ring R, a perfect complex is an object equivalent to a bounded complex of finitely generated projective R-modules. The terms can occupy several degrees, but there are only finitely many, and each behaves like a finite vector bundle. On a general scheme, perfection is a local condition: locally, the complex must have a bounded finite-rank vector-bundle resolution.

The adjective perfect signals strong finiteness. Perfect complexes survive derived tensor products well. They have duals and support traces and determinants under appropriate constructions. They provide the correct language for K-theory and for pushforward theorems in algebraic geometry.

It is tempting to claim every coherent sheaf is perfect. That is true on a regular Noetherian scheme, but not in general. On a singular affine scheme a finite module may require an infinite projective resolution. The dual numbers provide a compact example: over the ring of dual numbers, the residue field has a repeating free resolution. It is coherent but not perfect.

This failure tells us that singularities can be detected homologically. A module that looks finite from the outside may have infinite projective complexity when seen over a singular ring.

## Why this is geometry, not bookkeeping

Suppose we study a family of algebraic varieties and a complex of sheaves on that family. Fibers may gain or lose individual cohomology dimensions, while an alternating Euler characteristic remains stable under suitable proper and flat hypotheses. Perfect complexes make this variation manageable. They are the natural input for determinant lines, K-theoretic classes, and derived deformation theory.

The central distinction is between an arbitrary presentation and an invariant object. The derived category discards the choice of resolution but retains the higher interactions that resolutions expose. Perfect complexes then identify the finite objects for which those interactions are especially well controlled. That prepares us to understand why Riemann-Roch theorems and deformation calculations use complexes rather than only vector bundles or dimensions.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Let a cochain complex have differential `d^i:C^i -> C^{i+1}` with `d^{i+1}d^i=0`, and `H^i(C)=ker(d^i)/im(d^{i-1})`. A quasi-isomorphism induces isomorphisms on all `H^i`. The derived category `D(R)` is obtained from complexes of R-modules by localizing at quasi-isomorphisms. A triangle `A -> B -> Cone(f) -> A[1]` gives a long exact cohomology sequence.

For an integer `n >= 2`, the complex `P^{-1}=Z --n--> P^0=Z` is a projective resolution of `Z/n`. Derived tensoring with `Z/n` yields `P tensor_Z Z/n` with zero differential. Thus
\[
H^0(P\otimes\mathbf Z/n)=\mathbf Z/n,\qquad H^{-1}(P\otimes\mathbf Z/n)=\mathbf Z/n;
\]
under the homological convention these are `Tor_0^Z(Z/n,Z/n)` and `Tor_1^Z(Z/n,Z/n)`. Quasi-isomorphic complexes need not remain quasi-isomorphic after *ordinary* tensoring with a nonflat module; derived tensor corrects that defect.

For a ring R, perfect means quasi-isomorphic to a bounded complex of finitely generated projective modules. For a scheme X, perfect means locally quasi-isomorphic to a bounded complex of finite-rank locally free sheaves. Regular Noetherian schemes have `D^b_coh(X)=Perf(X)`; on singular schemes containment may be strict. For `R=k[epsilon]/(epsilon^2)`, the residue field k has the infinite periodic resolution `... -> R --epsilon--> R --epsilon--> R -> k -> 0`, so k is not perfect as an R-complex.

### Exercises with answers

1. What does a mapping cone detect? **Answer:** `Cone(f)` is acyclic exactly when f is a quasi-isomorphism.
2. Compute `Tor_1^Z(Z/6,Z/6)`. **Answer:** `Z/6`, using the two-term free resolution and reduction modulo 6.
3. Is every coherent sheaf on a singular Noetherian scheme perfect? **Answer:** no; the residue field over the ring of dual numbers is a counterexample.
4. Why is derived tensor used before reduction modulo n? **Answer:** ordinary tensor can destroy exactness and miss higher Tor groups.

### Reading and source notes

- [Stacks Project, Perfect complexes](https://stacks.math.columbia.edu/tag/0656), definitions and finite projective resolutions.
- [Stacks Project, Characterizing perfect complexes](https://stacks.math.columbia.edu/tag/07LQ), compact objects and finite construction from R.
- [Stacks Project, Derived categories of schemes](https://stacks.math.columbia.edu/tag/08E0), sheaf-theoretic context.
