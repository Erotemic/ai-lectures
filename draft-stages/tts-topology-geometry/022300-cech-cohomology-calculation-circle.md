# 022300 — Čech Cohomology by Calculation: Recovering the Circle's One Hole

**Track:** Topology and Geometry. **Background:** sheaf restrictions, open covers, linear algebra. **Central question:** how can a failure to glue local constants produce a cohomology class?

<!-- BEGIN SPOKEN LECTURE -->

# Čech Cohomology by Calculation: Recovering the Circle's One Hole

A sheaf gives us local sections and rules for matching them. Čech cohomology takes a further step: it organizes the disagreements on overlaps into a chain complex. The procedure resembles simplicial cohomology, but its entries are sections of a sheaf on intersections of open sets rather than numbers assigned to abstract simplices.

We will calculate the first cohomology of the circle with coefficients in the constant real sheaf. The answer will be one copy of the real numbers, but we will see exactly where that copy comes from.

## Cover a circle with two long arcs

Choose two open arcs U and V, each slightly longer than a semicircle, arranged so their union is the full circle. Each arc is connected and contractible. Their intersection is not connected: it has two disjoint short arcs, call them A and B, on opposite sides of the circle.

A section of the constant real sheaf on a connected arc is one constant real number. A section on the disconnected intersection consists of two numbers, one on A and one on B.

A zero-cochain is a choice of local section on each member of the cover. Therefore it is a pair of real numbers: a on U and b on V. A one-cochain assigns a section to their intersection. Because the intersection has two components, it is a pair of real numbers, which we may call c on A and d on B.

The Čech coboundary measures the difference between the two local constants. With a fixed sign convention, it sends the pair a,b to the pair b minus a, b minus a. The same difference appears on both components because each local section was constant on its entire connected arc.

## Compute the kernel and quotient

A zero-cochain is a cocycle when its coboundary vanishes. That happens exactly when a equals b. So degree-zero cohomology consists of the diagonal pairs, one real parameter, corresponding to a globally constant function on the connected circle.

In degree one, there are no nonempty triple intersections involving three distinct cover members because we have only two sets. With the usual alternating Čech complex, all one-cochains are cocycles. The first cohomology is therefore the two-dimensional vector space of pairs c,d, divided by the one-dimensional subspace of diagonal pairs produced by coboundaries.

The quotient has dimension one. A convenient coordinate on it is d minus c. That difference cannot be changed by adding the same number to both entries, which is precisely what a coboundary does.

We have just computed first Čech cohomology of the circle as one copy of the real numbers. The class is not simply a number attached to either overlap component. It is the *relative disagreement* between the two components, after accounting for arbitrary changes of local sections on U and V.

## What the one-dimensional answer means

Imagine choosing local primitives of a closed one-form on U and V. On each overlap component, their difference is a constant. We might have one constant on A and another on B. Changing the primitive on U by a constant and on V by another constant shifts both overlap differences by the same amount. Their difference survives these changes.

That surviving number is the period of the original closed one-form around the circle, up to orientation and normalization. It is the same information described by integration around a loop in de Rham cohomology.

For the angular one-form normalized to have period one, the corresponding Čech class can be represented by overlap differences zero and one. A different choice of local primitives may change both numbers, but it cannot change their difference. In that very concrete sense, the circle's cohomology is the obstruction to gluing the local primitives.

## Why the cover matters, and why it eventually does not

We used a particular cover with a disconnected overlap. If instead we choose a cover with many small arcs and connected intersections, there are more cochains and more differentials. The resulting cohomology should still describe the same global hole, provided the cover is sufficiently well behaved for the coefficients involved.

That qualification is important. For arbitrary sheaves and arbitrary covers, a single Čech complex does not always compute derived sheaf cohomology. A useful sufficient condition is that the higher cohomology of the sheaf vanish on every nonempty finite intersection of the chosen cover. Such a cover is called acyclic for the sheaf. Then the Čech computation agrees with sheaf cohomology.

Our arc cover is acyclic for the constant real sheaf because each nonempty intersection component is contractible, and its components have no higher constant-sheaf cohomology. It is a genuine computation of the sheaf's first cohomology, not just a calculation depending on an arbitrary drawing of two arcs.

## The algebraic pattern to retain

The first Čech cohomology group is the space of compatible overlap data, modulo overlap data that came from changing local sections. Higher cochains live on triple and larger intersections, and their coboundaries record alternating compatibility conditions. The entire pattern has the same kernel modulo image structure as any chain complex.

The circle computation is particularly memorable because every piece is elementary: two numbers for local sections, two for overlap sections, one diagonal coboundary direction, and one surviving direction. We have converted a geometric loop into a quotient of small vector spaces.

That method extends to line bundles, holomorphic functions, local systems, and obstructions in algebraic geometry. The formulas become richer, but the foundational question remains: which local disagreements can be removed by changing local data, and which survive every such change?

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Let U,V be connected contractible arcs covering S¹ with `U∩V=A⊔B`, two contractible components. For the constant real sheaf R, the two-set alternating Čech complex is

\[
C^0=R(U)\oplus R(V)\cong\mathbb R^2
\xrightarrow{\delta}
C^1=R(U\cap V)\cong\mathbb R^2,\quad
\delta(a,b)=(b-a,b-a).
\]

Thus `ker δ=diag(R)`, `im δ=diag(R)`, and `\check H^1≈R²/diag(R)≈R`, with class represented by the difference of the two overlap coordinates. Here intersections are disjoint unions of contractible sets, so the cover is acyclic for the constant sheaf and this computes `H^1(S¹;R)`. For a general sheaf or general open cover, Čech and derived sheaf cohomology need comparison; they are not simply synonymous.

### Exercises with answers

1. What are the dimensions of C-zero and C-one? **Answer:** both are two.
2. What is the rank of the coboundary map? **Answer:** one.
3. Why is the quotient dimension one? **Answer:** all one-cochains are cocycles and the image of δ has dimension one inside a two-dimensional space.
4. What is invariant when both overlap constants shift by the same amount? **Answer:** their difference, the Čech cohomology class.

### Sources and further reading

- The Stacks Project, [Čech Cohomology and Cohomology, Section 20.11](https://stacks.math.columbia.edu/tag/01EO), comparison theorem and acyclic covers.
- Allen Hatcher, [Algebraic Topology](https://pi.math.cornell.edu/~hatcher/AT/ATchapters.html), the circle's first cohomology.
- [Čech cohomology](https://en.wikipedia.org/wiki/%C4%8Cech_cohomology).
