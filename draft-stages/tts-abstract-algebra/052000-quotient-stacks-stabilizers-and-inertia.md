# 052000 — Quotient Stacks: Spaces That Remember Symmetry

**Track:** Abstract Algebra. **Background:** algebraic group actions, schemes, moduli, descent and torsors. **Central question:** what is lost when we replace objects with their isomorphism classes?

<!-- BEGIN SPOKEN LECTURE -->

# When two points are equivalent

A group action lets us declare certain points equivalent. Rotating a shape produces a different description but perhaps not a different geometric object. The ordinary quotient attempts to identify all the points in each orbit. For many purposes this is sensible. Yet an orbit is more than a label: some points may have symmetries that others lack.

Imagine the plane rotating about the origin. A nonzero point moves around a circle, while the origin remains fixed under every rotation. If we reduce each orbit to a single point, we may forget that the origin has a much larger stabilizer group. In a moduli problem, forgetting stabilizers means forgetting automorphisms of the objects being classified.

A quotient stack is designed to retain this information. It does not merely record which points become equivalent. It records the ways they are equivalent, and the symmetries of those equivalences.

## A scaling example

Let the multiplicative group act on the affine line by scaling. Every nonzero geometric point can be moved to every other nonzero point; the origin cannot be moved at all. A coarse orbit description sees two kinds of orbits. But the ordinary affine invariant ring consists only of constants, so the categorical affine quotient is just one point. This is a warning: depending on the quotient construction, an orbit-space intuition can fail even to distinguish the origin from nonzero points.

Now examine automorphisms. At a nonzero point, the only scalar fixing it is one. Its stabilizer is trivial. At the origin, every scalar fixes it, so the stabilizer is the whole multiplicative group. A quotient stack distinguishes these situations even when the affine invariant quotient has forgotten them.

The symbol for the quotient stack is often written as X in square brackets divided by G. To understand what it means, we should resist describing it as simply a set of orbit labels. Over a test scheme S, an object is a principal G-bundle over S, together with a G-equivariant map from that bundle to X. An isomorphism is an isomorphism of bundles compatible with these maps.

Why introduce principal bundles instead of just taking maps from S to X? Because local choices of representatives need not glue globally into one representative. We may have local descriptions related by transition functions. A principal bundle records those transitions, and equivariance ensures that the geometric object is consistently defined.

## The simplest stack is not a space of points

Take X to be a single point. The quotient stack of that point by G is called B G, the classifying stack of G. Over a test scheme S, its objects are principal G-bundles on S. Its one geometric point carries automorphism group G.

Compare that with an ordinary one-point scheme. The scheme's unique point has no such attached family of principal bundles or automorphism groups. If all we need is a count of underlying isomorphism classes over an algebraically closed field, they might look similar. As moduli objects, they are not the same.

This difference becomes crucial in families. For a finite group, the classifying stack records finite torsors. For a connected algebraic group, it records more elaborate principal bundles. These may have nontrivial gluing even though each small piece looks trivial.

## Inertia remembers symmetries of objects

There is another construction called the inertia stack. An object of the inertia stack is an object of the original stack together with an automorphism of that object. For a quotient stack of X by G, one can picture its geometric points as pairs consisting of a point x of X and a group element g that fixes x, with a suitable quotient by conjugation and transport of x.

For the scaling action, at the origin we retain every scalar as an automorphism. At a nonzero point only the identity remains. The inertia stack therefore separates sectors of the quotient according to their stabilizer behavior.

This is not simply extra decorative metadata. Stabilizers affect deformation theories, intersection theories on stacks, and orbifold invariants. They also explain why counting objects in a moduli problem may require weighting by their automorphism groups rather than just counting labels.

## Why the quotient needs a groupoid

A groupoid is like a group where arrows can move between different objects, not only from an object to itself. The action groupoid has an arrow from x to g times x for every group element g. Composing arrows corresponds to multiplying group elements. Stabilizers are the arrows from an object back to itself.

A stack can be thought of as a groupoid-valued object satisfying a gluing condition. This makes it compatible with descent: objects and their isomorphisms can be assembled from local data, provided the compatibility conditions hold. A coarse quotient generally cannot reconstruct all that information after it has been forgotten.

There is no reason to replace every geometric space by a stack. If no automorphisms matter and a geometric quotient behaves well, ordinary spaces are often sufficient. But a moduli space of curves, bundles, or representations may contain objects with nontrivial symmetries. Treating each isomorphism class as an unadorned point can hide exactly the phenomenon we want to understand.

The general principle is straightforward. When mathematical objects can be equivalent in several ways, the equivalences are themselves mathematical data. Quotient stacks preserve those data. Stabilizers measure self-equivalences. Inertia organizes them. And descent ensures that the whole structure works in families, not just for individual points.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For an action of a group scheme G on X, a test scheme S-point of `[X/G]` consists of a G-torsor `P -> S` together with a G-equivariant map `P -> X`; arrows are equivariant torsor isomorphisms respecting the maps. For X a point, `[Spec(k)/G]=BG` classifies G-torsors.

For the action `G_m x A^1 -> A^1`, `(t,x) -> tx`, the invariant ring is `k[x]^{G_m}=k`, so the affine categorical quotient is `Spec k`. Geometrically, the stabilizer of `x=0` is `G_m`; for `x != 0` it is trivial. The two geometric orbit types are not captured by the invariant affine quotient.

For a quotient stack, the inertia stack can be presented by the quotient of the fixed-pair scheme:
\[
I([X/G]) \simeq [\{(x,g)\in X\times G: gx=x\}/G],
\]
where `h in G` acts on `(x,g)` by `(hx,hgh^{-1})` (with the scheme-theoretic fiber product construction underlying this formula). Over arbitrary base fields, twisting and torsors matter; a list of geometric fixed pairs is not a complete description of all S-points.

### Exercises with answers

1. What is an object of `BG` over S? **Answer:** a principal G-bundle on S.
2. What is the stabilizer of zero in the scaling action of `G_m`? **Answer:** all of `G_m`.
3. Why is a coarse invariant quotient inadequate for the scaling example? **Answer:** the invariant ring is only k, so it collapses all geometric points and loses the different stabilizers.
4. What extra datum does the inertia stack remember? **Answer:** a chosen automorphism of an object, up to the stack's equivalence relation.

### Reading and source notes

- [The Stacks Project, Algebraic Stacks](https://stacks.math.columbia.edu/download/algebraic.pdf), quotient stacks, groupoids and descent.
- [The Stacks Project, Groupoid Schemes](https://stacks.math.columbia.edu/download/groupoids.pdf), action groupoids and quotient presentations.
- [Edidin, Notes on the Construction of the Moduli Space of Curves](https://arxiv.org/abs/math/9805101), quotient stacks and moduli motivation.
