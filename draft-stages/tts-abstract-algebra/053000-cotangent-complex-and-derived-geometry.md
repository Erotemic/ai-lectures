# 053000 — The Cotangent Complex: Differentials That Remember Singularities

**Track:** Abstract Algebra. **Background:** Kahler differentials, modules, derived functors, deformations, and affine schemes. **Central question:** how can a tangent-space construction detect the equations and relations that ordinary differentials forget?

<!-- BEGIN SPOKEN LECTURE -->

# An equation can vanish without becoming irrelevant

At a smooth point of a curve, we expect one independent direction of motion. If a curve is given by one equation in the plane, its differential usually removes one of the two ambient directions. This is the familiar Jacobian picture of tangent spaces. At a singular point, however, the Jacobian can lose rank. We may then see too many apparent tangent directions. What has happened to the equation that was supposed to constrain them?

It has not disappeared. Its first derivative may have vanished, but the equation is still part of the way the space was constructed. The cotangent complex is a way of retaining both the infinitesimal directions and the relations among them. Ordinary Kähler differentials are only one part of that structure.

To see why the extra part matters, consider the algebra of dual numbers. Start with a polynomial variable x and impose x squared equals zero. The resulting ring contains a nonzero nilpotent element x. If we look only at geometric points over a field, this ring resembles a single point. But a function with a square-zero value carries a first-order direction. A reduced point and a dual-number point cannot be treated as the same infinitesimal object.

# How relations enter the differential calculation

Suppose an algebra B is presented as a polynomial algebra P modulo an ideal I. A variation of the generators belongs to the module of differentials of P. A variation must also respect the imposed relations. So there is a map from the relations, modulo relations multiplied by relations, into the differentials of P restricted to B. Each defining equation goes to its differential.

For a sufficiently well-behaved presentation, this gives a two-term model: relations in degree minus one, differentials of generators in degree zero. The map between them is the Jacobian of the defining equations. Its degree-zero homology is precisely the familiar module of Kähler differentials. Its degree-minus-one homology detects relations whose first derivatives vanish.

There is one qualification. For an arbitrary quotient, this two-term object describes the first stages of the cotangent complex, but higher syzygies may require a fuller resolution. We must not assume that every singular algebra has a two-term cotangent complex. Hypersurfaces and, more generally, suitable local complete intersections do admit the two-term model.

Return to the dual numbers over a field of characteristic different from two. There is one relation, x squared, and one generator, x. Differentiating the relation gives two x times d x. The cotangent complex is represented by a map multiplying by two x. Its degree-zero homology sees one infinitesimal direction supported at the origin. Its degree-minus-one homology is also nonzero: the relation has a nontrivial element killed by its own derivative.

If instead we worked with the reduced algebra of an ordinary point, both parts would vanish. So the cotangent complex distinguishes a thickened point from a reduced point even though the underlying set of geometric points is identical.

# Why use a complex rather than another module?

The answer becomes clearer when we change the presentation. One algebra may be described using many different generators and equations. A presentation-dependent list of Jacobian rows is not the invariant we want. We need a construction that behaves coherently under replacing an algebra by a free resolution. The result is an object of a derived category: a complex considered up to quasi-isomorphism.

This means that two computational models can have different numbers of generators, yet describe the same infinitesimal information. The cohomology groups, and more importantly the derived object that links them, are independent of the chosen resolution.

There is also a transitivity principle. If A maps to B and B maps to C, the cotangent information for C over A is related to that for B over A and C over B by an exact triangle. You can think of this as a derived version of the chain rule. Varying the final object includes variation inherited from its intermediate base and variation relative to that base.

# Lifting along a square-zero extension

The cotangent complex becomes especially useful when we try to lift a map through a small thickening. Imagine that a target ring has a square-zero ideal M, so multiplying any two elements of M gives zero. We have a map into the quotient and ask whether it lifts to the thickened ring.

A first-order deformation is not necessarily a unique answer. There can be several lifts, related by derivations. There can also be an obstruction that prevents any lift. The derived Hom groups of the cotangent complex organize these possibilities: degree zero describes infinitesimal variations, while the next Ext group can contain an obstruction. Which Ext degree appears depends on whether we are deforming a map, an algebra, or a more elaborate moduli object, so the deformation problem must always be specified.

This structure explains an important feature of singularities. Smooth objects allow infinitesimal lifts under appropriate hypotheses. Singular objects may fail the same lifting test. The extra terms of the cotangent complex provide a language in which that failure can be computed.

# The bridge to derived geometry

Ordinary algebraic geometry treats equations by taking their quotient ring. Derived algebraic geometry asks us also to retain higher homological information created by those equations, especially when constructions such as intersections are not transverse. The cotangent complex is the natural differential object in this enlarged setting.

It is tempting to call all negative-degree information an error term. That would miss the point. The extra data are not numerical artifacts to discard; they record geometric multiplicity, obstruction, and hidden relations. We need them because equations can constrain a space even when their first-order Jacobian data alone do not tell the whole story.

The practical lesson is this. If the problem involves smooth coordinate changes, ordinary differentials may be enough. If it involves singularities, deformation obstructions, or intersections with excess dimension, ask what the full cotangent complex remembers. That question leads directly to our next subject: derived intersections.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For a map of commutative rings `A -> B`, the cotangent complex `L_{B/A}` is an object of the derived category of B-modules. With cohomological indexing it is commonly represented in nonpositive degrees. Its zeroth cohomology is `Omega_{B/A}`.

For a **local complete intersection** quotient `B=P/I`, where P is smooth over A and I is locally generated by a regular sequence, a two-term model is
\[
L_{B/A}\simeq [I/I^2\xrightarrow{d}\Omega_{P/A}\otimes_P B],
\]
with `I/I^2` in degree `-1`. For a general quotient the same two-term expression gives the truncation through degree `-1`, not necessarily the full derived object.

**Dual-number calculation.** Let `k` be a field with `char(k) != 2` and `B=k[x]/(x^2)`. Then
\[
L_{B/k}\simeq [B\xrightarrow{2x}B],\quad
H^0(L)=B/(2x)\cong k,\quad H^{-1}(L)=\ker(2x)=(x)\cong k.
\]
By comparison, `L_{k/k}=0`. The singularity is detected by nonvanishing degree `-1` homology.

For composable `A -> B -> C`, the transitivity triangle is
\[
L_{B/A}\otimes_B^{\mathbf L} C\longrightarrow L_{C/A}\longrightarrow L_{C/B}\longrightarrow (L_{B/A}\otimes_B^{\mathbf L} C)[1].
\]
In an appropriate deformation/lifting problem, the obstruction to lifting a specified morphism against a square-zero extension lies in an `Ext^1` group of the relevant pulled-back cotangent complex; when it vanishes, lifts form a torsor under `Ext^0`, assuming the standard finiteness and setup hypotheses. For deformation of an **algebra** against a fixed base, the conventional degree indexing often appears as `Ext^2(L_{B/A},M)` for obstruction and `Ext^1` for isomorphism classes of deformations. The two settings must not be conflated.

### Exercises with answers

1. For `B=k[x]`, compute `L_{B/k}`. **Answer:** the free B-module `B dx` in degree zero; there is no negative-degree term.
2. For the dual numbers over characteristic zero, why is `H^{-1}` nonzero? **Answer:** multiplication by `2x` kills the nonzero element `x` in B.
3. Can two different free resolutions define different cotangent complexes? **Answer:** not up to the derived equivalence used in the construction.
4. What goes wrong if an arbitrary quotient is assumed to have only a two-term cotangent complex? **Answer:** higher syzygies and higher homology may be omitted.

### Reading and source notes

- [The Stacks Project, The Cotangent Complex](https://stacks.math.columbia.edu/download/cotangent.pdf), resolutions, transitivity and local complete intersections.
- [The Stacks Project, Deformation Theory](https://stacks.math.columbia.edu/download/defos.pdf), square-zero extensions, lifting and obstructions.
- [Toën, Higher and Derived Stacks: A Global Overview](https://arxiv.org/abs/math/0604504), why derived structures enter moduli geometry.
