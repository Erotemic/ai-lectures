# 004000 — Separation Axioms: When Can Points and Sets Be Told Apart?

**Track:** Topology and Geometry. **Background:** open sets, compactness, continuity, and quotient topology. **Question:** why does a continuous bijection sometimes fail to be a homeomorphism?

<!-- BEGIN SPOKEN LECTURE -->

# Separation Axioms: When Can Points and Sets Be Told Apart?

A topological space tells us which collections of points count as open. That alone does not guarantee that individual points can be distinguished by open neighborhoods. A topology can be so coarse that two different points have exactly the same neighborhoods. A quotient construction can make distinct points impossible to separate, as happens on the line with two origins.

Separation axioms organize the different ways a space can distinguish its points and closed sets. They are not simply a ladder of increasingly abstract definitions. Each one supports concrete theorems about limits, compactness, and the existence of continuous functions.

## The first distinctions

A space is T-zero if, given two distinct points, there is some open set containing one but not the other. This is the weakest of the standard point-separation conditions. It permits one point to lie in every neighborhood of another, so the distinction may work only in one direction.

A space is T-one if, for two different points, each has an open neighborhood excluding the other. Equivalently, every singleton is a closed set. A proof of that equivalence is short. If the singleton containing x is closed, its complement is open and contains every other point. Conversely, if every other point has an open neighborhood avoiding x, their union is the complement of the singleton, which is therefore open.

A space is Hausdorff, or T-two, if any two distinct points have *disjoint* open neighborhoods. This is stronger than merely finding different neighborhoods. Ordinary metric spaces are Hausdorff: given points at positive distance d, open balls of radius less than half d around each point do not intersect.

To see that the distinctions matter, consider an infinite set with the cofinite topology, where the open sets are the empty set and all sets whose complements are finite. Every singleton is closed, so the space is T-one. But any two nonempty open sets intersect, because the complement of their intersection is the union of two finite sets and cannot exhaust an infinite set. Thus the space is not Hausdorff.

## Why Hausdorff spaces matter for limits

Suppose a sequence converges to x and also to y in a Hausdorff space. If x and y were different, choose disjoint neighborhoods U of x and V of y. Eventually the sequence would have to lie in U, and eventually it would have to lie in V. Beyond the later of those two points in the sequence, it would have to lie in their empty intersection. That is impossible. Therefore a sequence in a Hausdorff space has at most one limit.

The same argument applies to nets, which generalize sequences to spaces where ordinary sequences do not detect all topological behavior. Hausdorffness is the condition needed for uniqueness of limits in that general setting.

Hausdorffness also interacts decisively with compactness. If K is a compact subset of a Hausdorff space X, then K is closed. To prove it, take any point x outside K. For each y in K, find disjoint neighborhoods U-y of y and V-y of x. The U-y cover K. Compactness provides finitely many of them. Intersect the corresponding finitely many V-y neighborhoods of x to obtain one neighborhood V disjoint from K. Every point outside K has such a neighborhood; the complement of K is open.

This proof explains a result used when we glued an interval into a circle. A continuous bijection from a compact space to a Hausdorff space must be a homeomorphism. Indeed, it sends closed subsets of the compact domain to compact subsets of the Hausdorff codomain, hence to closed subsets. So it is a closed map, and the inverse is continuous.

## Points versus closed sets

Hausdorffness separates two points. Sometimes we want to separate a point from an entire closed set. A space is regular if, given a point x outside a closed set F, there are disjoint open neighborhoods of x and F. By a common convention, T-three means regular together with T-one. Some books build T-one into the word regular, so the convention must be checked when reading a theorem.

The next condition is normality. A space is normal if two disjoint closed sets can be placed in disjoint open neighborhoods. Under the usual convention, T-four means normal together with T-one.

Every metric space is normal. One can see this without constructing disjoint balls of a fixed radius, which may not exist. Let A and B be disjoint nonempty closed sets in a metric space. Define the distance from x to A as the infimum of distances from x to points of A, and similarly for B. Because A and B are closed and disjoint, their distances from any particular point cannot both be zero. The ratio distance to A divided by the sum of distance to A and distance to B is therefore a well-defined continuous function. It equals zero on A and one on B. The sets where this ratio is less than one-third and greater than two-thirds are disjoint open neighborhoods of A and B.

The formula shows something stronger than open-set separation: a continuous real-valued function can distinguish the two closed sets. In general topology, the Urysohn lemma guarantees such functions in normal T-one spaces. It is an important bridge from topology back to analysis.

## When a topology comes from a metric

If every familiar example were metrizable, we might wonder why not simply define distances from the beginning. But not every topology arises from a metric. The cofinite topology on an infinite set is not Hausdorff and so cannot be metrizable. There are also Hausdorff topologies that do not come from any metric.

A countable base is one useful condition. A space is second countable if there is a countable family of open sets such that every open set is a union of members of that family. The real line is second countable: intervals with rational endpoints form a countable base. A discrete space with uncountably many points is not second countable, because each singleton must appear in any base, although it is metrizable using the distance zero for identical points and one for distinct points.

There is a deep theorem that links these ideas: a regular T-one space with a countable base is metrizable. This is one form of the Urysohn metrization theorem. We will not prove it from scratch here; the construction is much longer than the preceding separation arguments. Its content is that a sufficiently rich supply of separations, together with countable control of the topology, permits a metric description.

That theorem does not assert that every Hausdorff space is metrizable, or that second countability is necessary for metrizability. Our uncountable discrete space already disproves the second claim.

## Applying the tests to constructions

When we form a quotient, compactness and connectedness survive continuous images under their usual hypotheses. Hausdorffness can fail. When we want to identify a geometric quotient with a familiar metric object, the compact-to-Hausdorff theorem can restore control, provided we have an actual continuous bijection to the proposed target.

Separation axioms therefore function as proof tools. Before using unique limits, ask for Hausdorffness. Before treating compact subsets as closed, ask the same. Before separating closed sets by a continuous function, ask for normality and the appropriate point-separation convention. These conditions mark which steps in familiar Euclidean proofs remain valid when we work in a space built abstractly from open sets.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Standard conventions used here:

- **T0:** distinct points are distinguished by an open set in at least one direction.
- **T1:** all singletons are closed.
- **T2 / Hausdorff:** distinct points admit disjoint open neighborhoods.
- **Regular:** every point and disjoint closed set have disjoint open neighborhoods; **T3** adds T1.
- **Normal:** every two disjoint closed sets admit disjoint open neighborhoods; **T4** adds T1.

**Compact-to-Hausdorff theorem:** a continuous bijection \(f:K\to H\) with \(K\) compact and \(H\) Hausdorff is a homeomorphism. Its inverse is continuous because \(f\) sends closed sets to closed sets.

**Metric normality witness:** for disjoint nonempty closed sets \(A,B\),
\[
h(x)=\frac{d(x,A)}{d(x,A)+d(x,B)}
\]
is continuous, \(h|_A=0\), \(h|_B=1\).

**Urysohn metrization theorem (one standard form):** every regular T1 second-countable space is metrizable. This theorem is recorded here, not proved in the spoken lecture.

### Exercises with answers

1. Is an infinite set with the cofinite topology T1? **Answer:** yes, every singleton is closed.
2. Is that topology Hausdorff? **Answer:** no, any two nonempty open sets intersect.
3. Why are compact subsets of Hausdorff spaces closed? **Answer:** separate an external point from each compact-set point and take a finite subcover.
4. Does metrizability imply second countability? **Answer:** no; an uncountable discrete metric space is a counterexample.

### Reading

Munkres, *Topology*, second edition, countability and separation axioms; MIT OCW 18.901, notes on Hausdorff spaces, regularity, normality, and metrization.
