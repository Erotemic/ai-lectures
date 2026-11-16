# 001000 — Open Sets and Continuity: Geometry Without a Ruler

**Track:** Topology and Geometry. **Background:** real-number intervals and elementary functions. **Question:** how can we speak about nearby points without assigning distances?

<!-- BEGIN SPOKEN LECTURE -->

# Open Sets and Continuity: Geometry Without a Ruler

Imagine a rubber sheet bearing a drawing. You stretch it gently, fold it, or pull it into a curved shape without tearing or joining points that were separate. Lengths change, angles change, and circles may become distorted. Yet there are aspects of the drawing that survive: which points can be reached by continuous paths, which parts are separated, and which points remain near which other points in a purely qualitative sense.

Topology begins by asking how much mathematics can be done with this qualitative structure alone. To answer, we need a way to say what a neighborhood is, even when we have no ruler.

## Open sets on the number line

Start with the real line. An open interval from a to b contains all numbers strictly between a and b, but not the endpoints. A set U of real numbers is open if every point x in U has some positive breathing room: there is a positive epsilon such that every real number within epsilon of x is also in U.

For example, the interval from zero to one is open. At a point x strictly between zero and one, choose a positive epsilon smaller than both the distance from x to zero and the distance from x to one. The epsilon neighborhood lies entirely inside the interval. By contrast, the half-open interval including zero but excluding one is not open in the real line: the point zero has no symmetric neighborhood contained in the set.

The empty set and the entire real line are open by convention and by the definition, respectively. The empty set satisfies the breathing-room condition vacuously because it contains no counterexample point.

There are two rules worth inspecting. The union of any collection of open sets is open. Why? A point in the union belongs to at least one of the member sets, and that member gives it the necessary breathing room. The intersection of finitely many open sets is also open. For each set choose some acceptable positive radius around the point, and take the smallest of these finitely many radii.

But infinite intersections can fail. Consider the open interval centered at zero with radius one, then radius one half, then one third, and so forth. The only point that belongs to all of them is zero. The one-point set containing zero is not open in the real line. We cannot take the minimum of infinitely many positive radii and assume that minimum is still positive.

This failure explains why topology singles out arbitrary unions but only finite intersections. It is not an arbitrary asymmetry; it captures the way ordinary neighborhoods actually behave.

## The abstraction

A topology on a set X is a selected family of subsets called open sets, satisfying three axioms. The empty set and X are open. Any union of open sets is open. Every finite intersection of open sets is open. That is the entire definition.

The points of X need not be numbers. They might be functions, geometric shapes, infinite sequences, or states of a system. If we can specify which subsets should count as open and verify the axioms, we have a topological space.

Every metric, or distance function, supplies a topology. Declare a set open if each point has a sufficiently small metric ball contained in the set. Different metrics can produce the same topology, because topology remembers which neighborhoods exist rather than their exact radii. And some topological spaces cannot be described by any metric at all.

Two extreme examples clarify how much freedom the definition allows. In the discrete topology, every subset is open. A point can be isolated from every other point by the one-element open set containing it. In the indiscrete topology, only the empty set and the whole set are open. It is impossible to distinguish individual points using nontrivial open sets.

These are not two different distance scales on the same space; the indiscrete topology on a set with more than one point cannot arise from a metric, because metric spaces can separate distinct points with disjoint small balls. The topology carries actual structural information.

## Continuity without epsilon and delta

For real functions, continuity is usually explained through nearby inputs producing nearby outputs. In a topological space, we can express the same idea with open sets. A function f from X to Y is continuous if, for every open set V in Y, the set of all inputs mapped into V is open in X. That input set is called the preimage of V.

It can be useful to think of this as an experimental test. Pick any open target region. Ask which source points land in that target. A continuous map requires that the resulting source region be open. This is a statement about all target neighborhoods at once.

On metric spaces, the preimage definition is equivalent to the familiar epsilon-delta definition. To sketch one direction, suppose f satisfies epsilon-delta continuity at every point. Take an open target region V. Every source point x whose image lies in V has an output ball around f of x contained in V. Epsilon-delta continuity then supplies a source ball around x mapping into that output ball. Hence the preimage of V is open.

For the reverse direction, take any source point x and any positive target radius. The ball centered at f of x with that radius is open. Its preimage is an open set containing x, so it contains a source ball around x. That source ball maps into the target ball. We have recovered epsilon-delta continuity.

Thus topology is not inventing a different notion for familiar real functions. It is exposing the part of continuity that does not depend on numerical distances.

## Images and preimages are not interchangeable

A tempting mistake is to say a continuous function sends every open set to an open set. That is false. Take the continuous function that squares real numbers. The image of the open interval from negative one to one is the interval from zero inclusive to one exclusive. That image is not open in the real line, because it includes zero without including nearby negative numbers.

The correct continuity test concerns preimages, not images. This matters because a preimage of a union is the union of preimages, and a preimage of an intersection is the intersection of preimages, for any function whatsoever. Those set-theoretic identities cooperate perfectly with the topology axioms.

If a continuous function is also a bijection and its inverse is continuous, it is called a homeomorphism. Homeomorphic spaces have the same topological structure up to a renaming of points. A continuous bijection alone may not be a homeomorphism, because the inverse need not be continuous. That distinction becomes important when compactness enters the picture.

## Closed sets and limiting behavior

A set is closed when its complement is open. On the real line, a closed interval including its endpoints is closed. The set of all integers is closed, even though it is not an interval. The entire real line and the empty set are both open and closed. “Open” and “closed” are not mutually exclusive categories: their definitions concern neighborhoods and complements, not an everyday door that must be one or the other.

A point x lies in the closure of a set A if every open neighborhood of x meets A. Thus zero lies in the closure of the open interval from zero to one, even though it is not a member of that interval. More generally, the closure consists of all points that cannot be separated from A by an open neighborhood.

In a metric space, this can be related to sequences: x is in the closure of A if some sequence of points of A converges to x. But in an arbitrary topological space, sequences need not detect every closure point. This is a first warning that many tools familiar from real analysis silently rely on properties of metric spaces. The open-set definition works at the wider level.

## What we have deliberately forgotten

Topology does not distinguish a circle of radius one from a circle of radius one hundred. It does distinguish an interval from a circle in ways we will later make precise, and it distinguishes a connected space from two separated pieces. The first step, however, is simpler: specify the open sets, preserve them under preimages, and recognize which conclusions need no measurement of distance.

The power of an abstraction is not that it says everything. It is that it says exactly the things we can carry from one setting into another. Open sets give us a portable definition of continuity; later they will give us portable definitions of compactness and connectedness. The geometry starts here, with neighborhoods instead of a ruler.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

A topology \(\tau\subseteq\mathcal P(X)\) contains \(\varnothing,X\), is closed under arbitrary unions, and is closed under finite intersections. A continuous map \(f:(X,\tau_X)\to(Y,\tau_Y)\) obeys
\[
V\in\tau_Y\implies f^{-1}(V)\in\tau_X.
\]
On metric spaces this is equivalent to pointwise \(\varepsilon\)-\(\delta\) continuity. The open interval example shows that
\[
\bigcap_{n=1}^{\infty}(-1/n,1/n)=\{0\}
\]
need not be open. Continuous functions need not map open sets to open sets: \(f(x)=x^2\) maps \((-1,1)\) to \([0,1)\).

**Closure:** \(x\in\overline A\iff U\cap A\neq\varnothing\) for every open neighborhood \(U\) of \(x\). Sequence-based characterization is valid for metric and first-countable spaces, not every topological space.

### Exercises with answers

1. Is \([0,1)\) open in \(\mathbb R\)? **Answer:** No; the point zero has no contained open ball.
2. Is every set continuous from a discrete domain? **Answer:** Every function from a discrete space is continuous, because every preimage is an open subset of the domain.
3. Does continuity require images of open sets to be open? **Answer:** No; squaring gives a counterexample.
4. Which subsets are simultaneously open and closed in a connected interval? **Answer:** Only the empty set and the whole interval.

### Reading

James R. Munkres, *Topology*, sections on topological spaces and continuous functions; MIT 18.901 Introduction to Topology course and reading syllabus.
