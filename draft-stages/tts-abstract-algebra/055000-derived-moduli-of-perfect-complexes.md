# 055000 — Deforming a Complex: Ext Groups as Tangents and Obstructions

**Track:** Abstract Algebra. **Background:** derived categories, perfect complexes, Ext, sheaf cohomology, and deformation theory. **Central question:** if our objects are complexes rather than points or bundles, what counts as an infinitesimal motion?

<!-- BEGIN SPOKEN LECTURE -->

# A moduli problem need not classify points

Many geometric classification problems begin with points, curves, or vector bundles. But sometimes the natural object is a complex of sheaves: a sequence of bundles and maps, considered up to quasi-isomorphism. Such complexes may encode solutions of linear differential equations, coherent sheaves, or geometric objects resolved by bundles.

A moduli problem asks us to organize all these objects into families. For an ordinary moduli space, one hopes to describe its tangent directions. For a moduli stack, we must also remember automorphisms. And for a derived moduli object, we should retain the higher obstruction data that explains why a proposed family cannot always be extended.

The bridge between these three levels is remarkably concrete. For a perfect complex E, the derived endomorphism complex of E controls its infinitesimal deformation theory. Its cohomology consists of the Ext groups from E to itself.

# The three neighboring Ext groups

Begin with Ext in degree zero. This describes endomorphisms of the object in the derived category. Invertible elements give automorphisms. A moduli stack that forgets these automorphisms can misrepresent the classification problem.

Ext in degree one describes first-order deformation classes in the standard deformation theory of a perfect complex with suitable conditions. Intuitively, we have a family depending on a tiny parameter whose square is zero. The degree-one Ext group contains the ways to vary E over that first-order thickening.

Ext in degree two is where the primary obstructions to extending a chosen deformation can live. For example, we might have lifted the complex over first-order dual numbers, and now try to lift it to a thicker ring where the parameter cubed vanishes. There can be an obstruction class in Ext two. If that class is nonzero, the specified lift cannot be extended in the way requested.

This does not mean every nonzero Ext-two group guarantees an obstruction. The group is the space where an obstruction may land. The particular obstruction class must still be calculated. Conversely, vanishing Ext two is a useful sufficient condition for unobstructedness in many standard setups, but it is not a universal shortcut for every moduli problem.

# A line bundle on a curve

Consider a smooth projective connected curve C over an algebraically closed field, and a line bundle L on C. Because L is locally free of rank one, the derived endomorphisms reduce to cohomology of the structure sheaf. The zeroth Ext group is the global functions on the curve, usually just the field. The first Ext group is the first cohomology of the structure sheaf, of dimension equal to the genus. And Ext two vanishes because a smooth curve has coherent cohomological dimension one.

So the family of line bundles has genus-many infinitesimal directions, while the obstruction group vanishes. This is why the Picard variety of a smooth projective curve is smooth of dimension equal to its genus. But the moduli stack of line bundles still has scalar automorphisms; the Picard variety and the stack do not contain exactly the same information.

On the projective line, the genus is zero. A fixed-degree line bundle has no infinitesimal deformations. On an elliptic curve, the genus is one, and a degree-zero line bundle has one infinitesimal deformation direction. This example lets us see a whole derived deformation story through three familiar cohomology groups.

# Why the shift matters

For the derived moduli stack of perfect complexes, the tangent complex at E is represented, with a common cohomological convention, by the derived endomorphisms shifted by one. This shift places infinitesimal automorphisms in degree minus one, first-order deformation classes in degree zero, and obstructions in degree one.

A single tangent vector space would see only the middle term. A derived tangent complex explains how the middle term is related to automorphisms below it and obstructions above it. That is the value of derived enhancement: we are not adding arbitrary layers of abstraction, but keeping the deformation problem's natural chain of homological information intact.

# When finite presentation matters

There is an important restriction. Not every unbounded complex behaves well in families. The perfect complexes, which locally have bounded resolutions by finite-rank projective modules, provide an especially useful class. They support duality and good base-change behavior under appropriate hypotheses. On reasonable geometric bases, they form a moduli problem that can be given a derived stack structure.

If we abandon boundedness or finite-generation conditions, the moduli problem can become too large or fail to have the desired geometric finiteness. The word perfect is therefore doing real mathematical work. It is not just a more flattering name for a complex.

# From deformation groups to geometric counts

Suppose a moduli problem has too many actual directions because some conditions fail to cut transversely. Its tangent and obstruction groups may nevertheless predict an expected dimension. The difference between the dimensions of deformation and obstruction spaces is the starting point for a virtual dimension calculation, after accounting correctly for automorphisms and the specific obstruction theory.

That is why the Ext groups are more than labels attached to a classification problem. They can determine whether the moduli space is locally smooth, how many parameters we should expect, and what additional structure is needed to define meaningful counts. An obstruction theory can sometimes turn this expected-dimensional information into a virtual fundamental class even when the ordinary space has the wrong dimension.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For a perfect complex E on an appropriate scheme X, the derived endomorphism complex is `RHom_X(E,E)`. Under standard conventions for the derived moduli of perfect complexes,
\[
T_E\mathcal{P}erf(X)\simeq \operatorname{RHom}_X(E,E)[1],\qquad
H^{-1}(T_E)=\operatorname{Ext}^0(E,E),\quad
H^0(T_E)=\operatorname{Ext}^1(E,E),\quad
H^1(T_E)=\operatorname{Ext}^2(E,E).
\]
The `Ext^0` group is an infinitesimal automorphism space, not automatically the full automorphism group; invertibility is an additional condition. `Ext^2` is a possible obstruction **space**, not a proof of an actual obstruction.

For a line bundle L on a smooth projective geometrically connected curve C over an algebraically closed field,
\[
\operatorname{RHom}(L,L)\simeq R\Gamma(C,L^\vee\otimes L)=R\Gamma(C,\mathcal O_C).
\]
Hence `Ext^0(L,L)=k`, `dim Ext^1(L,L)=g`, and `Ext^i(L,L)=0` for `i>=2`. On `P^1`, `g=0`; on an elliptic curve `g=1`. The Picard **stack** still has `G_m` automorphisms, while the fixed-degree Picard **scheme** has tangent dimension g.

The local perfectness requirement means E is locally quasi-isomorphic to a bounded complex of finite-rank vector bundles. Obstruction theories for other objects or for complexes over singular bases may require additional hypotheses. The expected dimension of a derived moduli stack must treat negative-degree tangent terms (automorphisms) appropriately; it is not generally `dim Ext^1 - dim Ext^2` without qualification.

### Exercises with answers

1. What is the first-order deformation space of a perfect complex in the standard setup? **Answer:** `Ext^1(E,E)`.
2. Does nonzero `Ext^2(E,E)` imply every deformation is obstructed? **Answer:** no; the actual obstruction class may vanish.
3. For a line bundle on a genus-two smooth projective curve, what are the dimensions of `Ext^1` and `Ext^2`? **Answer:** two and zero, respectively.
4. Why do we retain `Ext^0` in a moduli stack? **Answer:** it records infinitesimal self-equivalences, which an ordinary set of isomorphism classes forgets.

### Reading and source notes

- [The Stacks Project, Derived Categories](https://stacks.math.columbia.edu/download/derived.pdf), derived Hom and perfect complexes.
- [Toën and Vaquié, Moduli of Objects in dg-Categories](https://arxiv.org/abs/math/0503269), derived moduli and tangent complexes.
- [The Stacks Project, Cohomology of Schemes](https://stacks.math.columbia.edu/download/coherent.pdf), coherent cohomology and geometric examples.
