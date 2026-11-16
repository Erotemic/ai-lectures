# 007000 — Covering Spaces: Local Copies and Global Winding

**Track:** Topology and Geometry. **Background:** continuous maps, path homotopy, fundamental groups, and the circle's winding number. **Question:** how can a map look like separate copies of the same space locally while recording genuinely different topology globally?

<!-- BEGIN SPOKEN LECTURE -->

# Covering Spaces: Local Copies and Global Winding

A circle can be unwrapped onto a line. Map each real number to the point on the circle reached by turning through that many revolutions. Real numbers that differ by an integer map to the same point. Yet near any one point on the circle, we can select a small arc and find that its preimage is a disjoint collection of intervals, each of which maps perfectly onto the arc.

This is the defining idea of a covering space. Globally, the map may wrap one space around another many times. Locally, each small region downstairs has separate copies upstairs. Paths can be followed from one sheet to another, and the way they move between sheets records the global topology of the base space.

Let us call the map from the covering space E to the base space X by p. It is a covering map if every point of X has an open neighborhood U whose entire preimage is a disjoint union of open sets, each mapped homeomorphically onto U by p. We say U is evenly covered.

The requirement concerns the full preimage, not just a small neighborhood of one particular point upstairs. A map can be a local homeomorphism without satisfying the stronger global covering condition.

## Finite and infinite sheets

For a positive integer n, consider the map from the circle to itself that raises a complex number of unit magnitude to its nth power. Every point on the target has n preimages. Over a sufficiently small target arc, these preimages lie in n separate arcs, each mapped homeomorphically onto the chosen arc. We call this an n-sheeted covering.

If the starting circle winds once, its image winds n times. On fundamental groups, the induced map sends an integer k to n times k. The subgroup of winding numbers downstairs that come from closed loops upstairs is therefore the multiples of n.

The real line covering the circle has infinitely many sheets. A closed loop downstairs with winding number one lifts to a path upstairs whose endpoint is one unit away from its starting point. It does not lift to a closed loop. Only loops of winding number zero can lift to closed loops with that chosen starting point.

This gives a way to see subgroup information in a geometric picture. The circle covering itself n times corresponds to the subgroup of integers divisible by n. The real-line covering corresponds to the zero subgroup. The identity covering corresponds to all the integers.

## Uniqueness of a lifted path

Suppose a continuous path in X begins at a point x, and we choose one of the points upstairs lying over x. Can we find a path upstairs that projects to the given path and begins at our chosen point? For a covering map, yes, and the lift is unique.

Here is the argument. The path lives on a compact interval of time. Around each time, choose an evenly covered neighborhood containing the path's current position. Compactness allows us to divide the full time interval into finitely many smaller subintervals whose path images lie in such neighborhoods. Start with the chosen point upstairs. On the first subinterval, we use the unique inverse of p on its sheet. At the next endpoint, choose the sheet that contains where the previous lift arrived. Continue. The constructed segments agree at their boundaries. Local uniqueness of the inverse maps also proves that no other lift with the same initial point can diverge from it.

Now imagine continuously deforming one path into another while keeping their endpoints fixed. The covering-space homotopy-lifting property lets us lift that whole deformation once its initial lift has been selected. Because the fiber over a point is discrete, the endpoint of a lifted path cannot jump continuously from one sheet to another. Consequently homotopic based loops have lifts with the same endpoint.

This is exactly what made winding number invariant under homotopy in the previous circle calculation. Covering spaces generalize the mechanism.

## A lifting criterion

Take a continuous map from a path-connected, locally path-connected space Y into X, and choose a proposed lift of one base point. When can the whole map be lifted to E?

The answer is controlled by fundamental groups. A lift exists exactly when every loop in Y, after mapping into X, belongs to the subgroup represented by loops in E under p. In symbols, the induced image of the fundamental group of Y must be contained in the subgroup contributed by the covering map. We must use compatible base points; ignoring that choice can obscure a conjugation.

The necessity is clear. If we can lift the entire map, then the image of any closed loop in Y lifts to a closed loop in E. For sufficiency, choose a path in Y from the base point to a point y, map it into X, lift that path, and use its endpoint to define the lifted value at y. The fundamental-group condition ensures that choosing another path gives the same endpoint. Local path connectedness and the evenly covered neighborhoods then supply continuity.

For example, a continuous map from a simply connected domain into the circle has a continuous real-valued angle lift after we choose an initial angle. A map from the circle to itself of degree one cannot have such a global lift to the real line. Its fundamental group maps a generator to one, which does not belong to the zero subgroup coming from the real-line covering.

## Deck transformations

A deck transformation is a homeomorphism of the covering space to itself that leaves the projection p unchanged. For the real line over the circle, deck transformations include translations by integers. In fact those are all the deck transformations, and they form a group isomorphic to the integers.

For the n-fold circle cover, deck transformations are rotations by nth roots of unity, forming a cyclic group of order n. They permute the sheets without changing points downstairs. For more general coverings, the deck group need not act transitively on each fiber; coverings for which it does are often called regular or normal.

When X has a suitable universal cover, these symmetries are tightly connected to its fundamental group. With choices of base points, the deck group of the universal cover is naturally identifiable with the fundamental group, up to conventional choices about multiplication order. The universal cover is simply connected and serves as a reference from which other connected coverings can be constructed.

## Which subgroups correspond to coverings?

There is a beautiful classification theorem, but its hypotheses must be said aloud. If X is path-connected, locally path-connected, and semilocally simply connected, then it has a universal covering space. The connected covering spaces of X, considered up to equivalence, correspond to conjugacy classes of subgroups of its fundamental group. If we also choose base points upstairs, the correspondence becomes one with actual subgroups rather than conjugacy classes.

The subgroup records which loops downstairs close when lifted. A smaller subgroup corresponds to a covering with more sheets, where fewer loops close upstairs. For the circle, every subgroup of the integers has the form n times the integers, including the zero subgroup. We have already met all the resulting connected covering spaces: the finite-degree circle maps and the real line.

Not every topological space satisfies the local hypotheses. Spaces with loops accumulating at smaller and smaller scales can fail to admit the ordinary universal covering described here. The classification theorem is not a universal statement about arbitrary spaces.

Covering theory converts a global problem about paths into algebra about subgroups. It also illustrates a theme that will recur in geometry: local behavior can look completely standard while global gluing or winding produces structure that cannot be seen in any single small neighborhood.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

A covering \(p:E\to X\) has, for every \(x\in X\), an evenly covered open neighborhood \(U\) with
\[
p^{-1}(U)=\bigsqcup_{\alpha}V_\alpha,
\qquad p|_{V_\alpha}:V_\alpha\stackrel{\cong}{\longrightarrow}U.
\]

**Circle coverings.** For \(p_n:S^1\to S^1\), \(p_n(z)=z^n\) with \(n\ge1\), the induced homomorphism on \(\pi_1(S^1)\cong\mathbb Z\) is multiplication by \(n\), hence has image \(n\mathbb Z\). Its deck group is \(C_n\). For \(p_\infty:\mathbb R\to S^1\), \(p(t)=e^{2\pi it}\), the image of \(\pi_1(\mathbb R)\) is zero and the deck group consists of integer translations.

**Lifting criterion.** Let \(p:(E,e_0)\to(X,x_0)\) be a covering and \(f:(Y,y_0)\to(X,x_0)\) with \(Y\) path-connected and locally path-connected. A based lift \(\widetilde f:Y\to E\) exists iff
\[
f_*\pi_1(Y,y_0)\subseteq p_*\pi_1(E,e_0).
\]

**Classification.** If \(X\) is path-connected, locally path-connected, and semilocally simply connected, equivalence classes of connected pointed covers correspond to subgroups of \(\pi_1(X,x_0)\); forgetting the point upstairs quotients by conjugacy. Normal subgroups correspond to regular connected coverings; their deck groups are the corresponding quotient groups.

### Exercises with answers

1. Which subgroup of \(\mathbb Z\) corresponds to \(z\mapsto z^4\)? **Answer:** \(4\mathbb Z\).
2. Does \(z\mapsto z^2\) admit a continuous right inverse \(S^1\to S^1\)? **No.** On \(\pi_1\), multiplication by two cannot have a right inverse homomorphism \(\mathbb Z\to\mathbb Z\).
3. What is the deck group of the real-line covering of the circle? **Answer:** integer translations, isomorphic to \(\mathbb Z\).
4. Why are free homotopy classes and based homotopy classes treated differently in the classification? **Answer:** changing a chosen lift/basepoint acts by conjugation on the subgroup.

### Reading

Allen Hatcher, [Algebraic Topology](https://pi.math.cornell.edu/~hatcher/AT/ATchapters.html), Chapter 1, sections on covering spaces, path lifting, universal covers, and the classification theorem.
