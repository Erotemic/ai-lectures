# 048000 — Deformation-Obstruction Complexes in Moduli Problems

**Track:** Abstract Algebra. **Background:** Ext groups, cotangent complexes, line bundles, families, deformation theory. **Central question:** why can a space of mathematical objects have tangent directions, symmetries, and obstructions all at once?

<!-- BEGIN SPOKEN LECTURE -->

# A space whose points are themselves mathematical objects

A moduli problem asks us to organize mathematical objects into a family. Each point is meant to represent something: a curve, a vector bundle, a surface, or perhaps a representation. We can then ask whether nearby points correspond to nearby objects, how many independent ways an object can vary, and whether a first-order variation extends to an actual family.

For an ordinary smooth curve, tangent vectors at a point describe possible directions of motion. In a moduli problem, a tangent direction is often a deformation of the object over the dual numbers, a ring with one infinitesimal parameter whose square is zero. This lets us study first-order changes without claiming they extend indefinitely.

A second question appears immediately: what if the object has automorphisms? Two descriptions of a deformation can be equivalent through a symmetry. A third question is whether a first-order deformation can be lifted from a small infinitesimal thickening to a larger one. An obstruction may prevent that lift.

These three phenomena lead naturally to a complex rather than to a single tangent vector space.

## Ext groups as a deformation dictionary

Fix a smooth projective variety X and a coherent sheaf E on it, in a setting where the standard deformation theory applies. The vector space Ext one of E with itself governs first-order deformations of E. Ext two receives obstruction classes for lifting deformations. Ext zero records infinitesimal automorphisms.

The numbers zero, one, and two are not ranks of three arbitrary matrices. They arise from the cohomological degrees of a derived endomorphism object. A deformation problem is controlled by how a mathematical object maps to itself, including higher extension data.

It is important not to overstate the dictionary. An obstruction group may be nonzero even when a particular deformation problem is unobstructed. The obstruction is a class in that group, and the class may vanish. Likewise, a tangent space of positive dimension does not by itself prove that a smooth family of that dimension exists.

Consider a line bundle L on a smooth projective curve C of genus g. Its derived endomorphism groups simplify because its endomorphism sheaf is the structure sheaf. Ext one of L with itself is therefore the first cohomology of the structure sheaf. That vector space has dimension g. Ext two vanishes on a smooth curve, so the standard obstruction group for line-bundle deformations vanishes. This explains the smooth g-dimensional local behavior of the Picard variety.

For a genus-one curve, that tangent space is one-dimensional. We can change the line bundle infinitesimally in one independent direction. The calculation is not just counting coefficients in an equation; it is measuring cohomology of the underlying curve.

## Deforming the space instead of a sheaf

Now let the geometric space X itself vary. For a smooth proper scheme, its infinitesimal automorphisms are measured by the global sections of the tangent sheaf, while first-order deformations are measured by its first cohomology and potential obstructions by second cohomology. This is the familiar smooth-case pattern.

When X has singularities, the tangent sheaf alone misses information. The cotangent complex replaces the sheaf of differentials as the object that correctly remembers equations and relations among equations. Derived Hom from that cotangent complex to the structure sheaf organizes the tangent, deformation, and obstruction groups. The precise degree conventions depend on whether we are deforming the space, a map, or a sheaf.

Here is a concrete way to see why relations matter. Suppose a space is cut out by polynomial equations. Perturb the coordinates by a first-order epsilon. The linearized equations say which directions are initially allowed. But if the equations satisfy dependencies, the linearized conditions can also satisfy dependencies. On attempting a second-order lift, a quadratic error can survive that cannot be corrected by changing the next coefficient. That residual error is the obstruction.

## Why moduli spaces can be singular

A naive picture of moduli would be a smooth manifold with as many coordinates as deformation parameters. In reality, automorphisms may lead to stack-like quotients, and obstruction equations may cut out singular loci. A space of first-order possibilities may be much larger than the space of genuine nearby solutions.

Derived deformation theory supplies a systematic record of these features. It does not magically turn every moduli problem smooth. Instead, it keeps track of the reason smoothness may fail, while preserving the data needed for virtual dimensions and intersection invariants.

Think of a coarse moduli point, for example, as a label for an isomorphism class. That label can conceal a symmetry group. A moduli stack retains the symmetry information. A derived enhancement can also retain higher deformation-obstruction information. Each layer adds structure that a set of labels cannot express.

The broad principle is that moving objects create more than coordinates. They create automorphisms, first-order possibilities, and possible barriers to realizing those possibilities. Complexes and Ext groups provide the language in which all three can be calculated and compared.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For a coherent sheaf E on a fixed smooth projective X, the standard deformation-obstruction complex is `RHom_X(E,E)` (with the customary shifts in the derived moduli formalism). In classical deformation theory:
\[
\operatorname{Ext}^0_X(E,E)\;\text{(infinitesimal automorphisms)},\quad
\operatorname{Ext}^1_X(E,E)\;\text{(first-order deformations)},\quad
\operatorname{Ext}^2_X(E,E)\;\text{(obstruction space)}.
\]
An obstruction is an actual class in `Ext^2`; a nonzero obstruction *space* does not guarantee obstruction for a given deformation.

For an invertible sheaf L on a smooth projective curve C, `RHom(L,L)=R Gamma(O_C)`, so `Ext^i(L,L)=H^i(C,O_C)`. Thus `dim Ext^1=g`, `Ext^2=0` and `Ext^0=k` for a geometrically connected curve over an algebraically closed field. This matches the tangent dimension of `Pic(C)`; the scalar automorphisms of L still matter if one studies the moduli *stack* rather than the Picard *scheme*.

For the deformation of a smooth proper scheme X, the classical groups are `H^i(X,T_X)` in degrees `i=0,1,2`. More generally, cotangent-complex expressions `Ext^i_X(L_{X/k},O_X)` encode deformations and obstructions (with indexing dependent on the exact deformation functor). Smoothness and properness are not optional assumptions when using the simplest tangent-sheaf formula.

### Exercises with answers

1. What is the infinitesimal deformation dimension of a line bundle on a smooth genus-two curve? **Answer:** two, since `dim H^1(O_C)=2`.
2. Does `Ext^2(E,E) != 0` prove every deformation is obstructed? **Answer:** no; obstruction classes can vanish.
3. Why can a coarse moduli point conceal information? **Answer:** it records an isomorphism class but not necessarily its automorphism group.
4. What replaces the ordinary sheaf of differentials in singular deformation theory? **Answer:** the cotangent complex.

### Reading and source notes

- [Stacks Project, Deformation Theory](https://stacks.math.columbia.edu/download/defos.pdf), deformations of modules, schemes, and complexes.
- [Stacks Project, Key example in Artin's axioms](https://stacks.math.columbia.edu/tag/07YI), explicit obstruction maps from equations.
- [Stacks Project, Cotangent complex](https://stacks.math.columbia.edu/tag/08P5), derived control of infinitesimal deformations.
