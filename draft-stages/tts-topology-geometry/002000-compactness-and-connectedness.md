# 002000 — Compactness and Connectedness: Two Global Consequences of Open Sets

**Track:** Topology and Geometry. **Background:** open sets, continuity, elementary real analysis. **Question:** how can local neighborhood conditions guarantee global results?

<!-- BEGIN SPOKEN LECTURE -->

# Compactness and Connectedness

An open set is local information. It tells us that each included point comes with some neighborhood. Yet collections of open sets can encode remarkable global facts. One fact says that an infinite collection of local observations can sometimes be reduced to a finite collection without losing coverage. Another says that a space cannot be split cleanly into two nonempty open pieces.

The first is compactness. The second is connectedness. Together they explain why continuous functions on closed intervals behave so well, and why that behavior can fail when an endpoint is missing.

## Cover a space with neighborhoods

An open cover of a space X is a collection of open subsets whose union contains every point of X. The collection may be infinite. A finite subcover is a finite selection from the collection that still covers all of X.

A space is compact if every open cover has a finite subcover. Notice the quantifiers: we require this property for *every* possible open cover, not merely for a convenient family. Compactness is not a synonym for being small. It is a theorem about the way infinitely many local neighborhoods can cover the space.

Take the closed interval from zero to one with its ordinary real-line topology. It is compact. One way to see the underlying reason is through the completeness of the real numbers. Given an arbitrary open cover, consider how far to the right we can cover the interval using finitely many selected open sets. There is at least a little progress starting at zero, because some open set contains zero. Let s be the least upper bound of all the right endpoints reached by such finite coverage.

If s were less than one, choose an open set containing s. That set contains points a little to the left and a little to the right of s. A finite cover reaching sufficiently close to s, together with this one additional open set, would extend the covered interval past s. That contradicts the definition of s. Therefore the supremum must be one. A final open set containing one lets us extend finite coverage to the endpoint itself. We have produced a finite subcover of the entire interval.

The proof is a sketch of the Heine–Borel phenomenon in one dimension. It depends on the least-upper-bound property of the real numbers. In Euclidean space, a set is compact exactly when it is closed and bounded. That equivalence is special to Euclidean space and certain related settings; in a general topological space, the open-cover definition is the fundamental one.

## Missing an endpoint changes everything

Consider the interval greater than zero and at most one. We can cover it by the open sets that, for each positive integer n, contain all real numbers greater than one over n and less than two. Every positive point eventually lies in one of these sets. But any finite selection has a smallest included left threshold, so it misses points sufficiently close to zero. There is no finite subcover. The interval is not compact.

It is tempting to say the failure has no practical effect because the set is bounded and almost closed. Yet compactness is not approximate. Its consequences can disappear completely when one endpoint is removed.

Consider the function one divided by x on this half-open interval. The function is continuous everywhere in its domain, but it is unbounded as x approaches zero. On a compact interval a real-valued continuous function must be bounded and must attain its maximum and minimum. On the noncompact half-open interval, the corresponding claim fails. The topology explains why a missing point can matter more than its negligible size.

## Continuous images of compact spaces

Suppose f is continuous from a compact space X into a space Y. We claim the image f of X is compact, with the subspace topology inherited from Y. Take any open cover of f of X. Each covering open set has an open preimage in X because f is continuous. These preimages cover X. Compactness of X supplies a finite subcover, and taking the corresponding target open sets gives a finite cover of f of X.

We proved a global preservation theorem from one line of local information: preimages of open sets remain open. Nothing in the proof requires Y to have a distance function. This is why open-cover compactness is a successful topological definition.

In the real numbers, compact sets are closed and bounded. So if f maps a compact X continuously into the real line, its image is compact and therefore bounded, with maximum and minimum attained. The familiar extreme value theorem is one consequence of a broader theorem about continuous images.

There is a useful related result. A continuous bijection from a compact space X onto a Hausdorff space Y is automatically a homeomorphism. Hausdorff means distinct points can be separated by disjoint open neighborhoods; every metric space is Hausdorff. The proof uses the fact that a compact subset of a Hausdorff space is closed: the continuous bijection sends closed subsets of compact X to compact, hence closed, subsets of Y. That makes the inverse continuous.

Without compactness, the conclusion can fail. The map that sends each angle t in the half-open interval from zero inclusive to two pi exclusive to its point on the unit circle, using cosine and sine, is continuous and bijective. But the inverse cannot be continuous near the point corresponding to angle zero, because nearby points on the circle approached from one direction have angles approaching two pi rather than zero. The interval and the circle are not homeomorphic. Compactness catches the obstruction: the circle is compact and the half-open interval is not.

## Connectedness prevents a split

A topological space X is disconnected if it can be written as a union of two nonempty, disjoint open sets. Otherwise it is connected. The definition says the space cannot be separated into two pieces that are both open within the space. We do not require that two arbitrary points can be joined by a path; path connectedness is stronger in general.

Every interval in the real line is connected. To understand why, imagine an interval split into two disjoint nonempty open pieces. Pick a point in one piece and a point in the other. Travel along the numerical order between them. At some boundary between the pieces, neither side can maintain its supposed openness: the least-upper-bound property forces a point that cannot be assigned an open neighborhood staying entirely in its designated piece. A rigorous proof uses a supremum argument similar in spirit to the compactness proof.

Connectedness explains the intermediate value theorem. A continuous map sends connected spaces to connected spaces. The proof is by contradiction. If the image could be separated into disjoint nonempty open pieces, the preimages of those pieces would be disjoint, nonempty, open sets separating the domain. But a connected domain admits no such separation.

A connected subset of the real line must be an interval: if it contains two values a and b but misses some value c strictly between them, it splits into the part below c and the part above c. Therefore a continuous real-valued function on an interval takes every intermediate value between any two values it attains. This is the intermediate value theorem as a statement about connected images.

## Connected does not mean path connected

Consider the closure in the plane of the graph of sine of one over x for positive x near zero. The oscillating graph is connected, and its closure includes a vertical line segment at x equal to zero. The whole set remains connected because the closure of a connected set is connected. Yet it is not path connected: there is no continuous path inside that set from a point on the vertical segment to a point on the oscillating graph.

The point of the example is not to make the topology needlessly strange. It shows that “cannot be separated by open sets” and “can be traversed along a continuous path” are distinct claims. They coincide in many familiar regions, but they are not equivalent for arbitrary spaces.

A related distinction is local connectedness: having small connected neighborhoods. A space can be connected without being locally connected. When a theorem needs paths, neighborhoods, or differentiable curves, the precise hypothesis matters.

## Two powerful kinds of global control

Compactness says any open cover admits a finite subcover. Connectedness says no separation into two nonempty open pieces is possible. Under continuous maps, both properties survive. Their consequences are different: compactness helps guarantee extrema and finite control; connectedness helps guarantee intermediate values and the impossibility of certain partitions.

Together they illustrate why topology is more than a vocabulary for deforming pictures. Local openness produces global mathematical theorems. The conditions state exactly what is preserved, and examples with missing endpoints or oscillating curves tell us where seemingly obvious conclusions stop being valid.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

**Compactness:** Every open cover \(\{U_i\}_{i\in I}\) of \(X\) has a finite subcover. **Heine–Borel in \(\mathbb R^n\):** \(K\subseteq\mathbb R^n\) is compact iff closed and bounded. Outside this setting, closed and bounded need not characterize compactness.

**Continuous preservation:** If \(f:X\to Y\) is continuous and \(X\) compact, then \(f(X)\) is compact. If \(X\) connected, then \(f(X)\) is connected. In a Hausdorff space, compact subsets are closed; hence continuous bijections from compact spaces to Hausdorff spaces have continuous inverses.

**Counterexamples:** \((0,1]\) has the open cover \(\{(1/n,2)\cap(0,1]\}_{n\ge1}\) with no finite subcover. The mapping
\[
f:[0,2\pi)\to S^1,\quad f(t)=(\cos t,\sin t)
\]
is a continuous bijection but not a homeomorphism. The closure of \(\{(x,\sin(1/x)):0<x\le1\}\) is connected but not path connected.

### Exercises with answers

1. Is the open interval \((0,1)\) compact in \(\mathbb R\)? **Answer:** No; it is not closed, and one can exhibit covers with no finite subcover.
2. Why does a continuous real function on \([0,1]\) achieve its maximum? **Answer:** The image is compact in \(\mathbb R\), so it is closed and bounded and contains its supremum.
3. Is every continuous bijection a homeomorphism? **Answer:** No; the half-open angle interval mapping to the circle is a counterexample.
4. Does connectedness always imply path connectedness? **Answer:** No; the closed topologist's sine curve is a standard counterexample.

### Reading

Munkres, *Topology*, sections on connectedness, compactness, and quotient topology; MIT 18.901, course notes and syllabus.
