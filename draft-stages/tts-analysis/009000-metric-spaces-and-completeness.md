# 009000 — Distance Without Coordinates: Metric Spaces and Completeness

**Track:** Analysis from First Principles. **Background:** real-number limits, Cauchy sequences, continuity. **Theme:** keep the structure needed for rigorous limits while discarding the accidental details of the number line.

<!-- BEGIN SPOKEN LECTURE -->

# Distance Without Coordinates: Metric Spaces and Completeness

Suppose a sequence of approximations is meant to settle down to a single answer. In the real numbers, we can ask whether the difference between an approximation and its proposed limit becomes arbitrarily small. But what if an approximation is not a number? It might be a pair of coordinates, a vector with a thousand entries, a continuous curve, or an entire function. We still want to ask whether the approximations are approaching one another, and whether the approach actually produces an object of the kind we started with.

One response would be to invent a separate theory of limits for each collection of objects. A better response is to identify what the existing proofs use. Many proofs care about distances, not about multiplication, ordering, or even the existence of a coordinate system. That observation leads to a metric space: a set together with a rule for measuring the distance between any two of its points.

The idea is economical, but it comes with a warning. Changing the meaning of distance can change what counts as convergence and continuity. The word distance is not merely descriptive here. It is part of the mathematics.

## What a distance must do

A metric begins with a set of objects, which we will call points, even when they are functions or sequences. For every pair of points, it assigns a nonnegative real number as their distance.

We impose three conditions. The distance between two points is zero exactly when they are the same point. The distance from the first point to the second equals the distance in the reverse direction. And the direct distance from one point to another cannot exceed the distance of a route that passes through an intermediate point. That last condition is the triangle inequality.

Consider ordinary numbers first. The absolute value of their difference is a metric. Two different numbers have positive distance, exchanging their order changes nothing, and the absolute value triangle inequality tells us that going by way of a third number does not provide a shorter upper bound than the sum of the two legs.

On the plane, straight-line distance gives another metric. We can also use the sum of the absolute horizontal and vertical changes. Both satisfy the rules, but they measure the geometry differently. For a move three units horizontally and four vertically, straight-line distance is five while the sum distance is seven. The numbers differ, yet a sequence converges in one of these two distances exactly when it converges in the other. In this finite-dimensional example, inequalities compare the two distances above and below by fixed multiples.

There is a more surprising possibility. On any set at all, declare the distance between distinct points to be one, while the distance from a point to itself is zero. This is the discrete metric. The triangle inequality holds, because a direct jump has length at most one and any route connecting distinct points must include at least one jump. It ignores any finer notion of nearness the points might have possessed.

We can now see why the metric belongs in the specification of the problem. On the real numbers with ordinary distance, a sequence such as one over n approaches zero. With the discrete metric on exactly the same underlying set, that sequence does not approach zero. Every term remains distance one from zero.

## Open balls replace intervals

Once we can measure distance, we can describe a neighborhood without referring to left or right. Fix a point and a positive radius. The open ball around that point contains every point whose distance from the center is strictly less than the radius.

For ordinary numbers, an open ball is just an open interval centered at the chosen point. In the plane with straight-line distance, it is the interior of a circle. Under the sum distance, it becomes the interior of a diamond. Under the discrete metric, a ball of radius one-half contains only its center.

An open set is one that contains a sufficiently small open ball around each of its points. The ball need not have the same radius at every point. These are the local regions in which limit and continuity arguments take place. We have reconstructed a language of neighborhoods without ever asking which point is larger than another.

A sequence converges to a point when, for every positive tolerance, all sufficiently late terms lie inside the open ball of that radius centered at the point. The quantifiers are exactly the familiar epsilon and N quantifiers from numerical sequences. Only the absolute difference has been replaced by a metric.

The triangle inequality immediately proves that a sequence cannot converge to two different points. Suppose it approached both a and b. The distance between a and b is no larger than the distance from a to a late term plus the distance from that term to b. Both pieces can be made smaller than any chosen half-tolerance. Therefore the distance between a and b must be zero, and a equals b.

This proof is valuable because it never mentions coordinates. Wherever the metric axioms hold, uniqueness of limits follows.

## The internal test: Cauchy sequences

There is a second way to describe a sequence settling down. Instead of comparing its terms to a proposed limit, compare late terms to one another. A sequence is Cauchy if, for every positive tolerance, there comes a time after which any two terms are closer than that tolerance.

Every convergent sequence is Cauchy. If both late terms are close to the limit, the triangle inequality says they are close to each other. More precisely, give each term half the permitted error, add the two distances, and obtain the required bound.

The converse is a deeper issue. A Cauchy sequence can look internally settled while its intended limit is not present in the space. Consider rational approximations to the square root of two. Their rational terms become arbitrarily close to one another, but no rational number is their limit. The rationals, with ordinary distance, are not complete.

A metric space is complete if every Cauchy sequence in that space converges to a point belonging to that space. The real numbers have this property. The rational numbers do not. Notice what completeness does not say: it does not assert that every sequence converges. A sequence that alternates forever between zero and one is not Cauchy. Completeness promises a limit only after the internal Cauchy test has been passed.

The discrete metric offers a strikingly different complete space. Take a Cauchy sequence and request an error smaller than one. Any two sufficiently late terms must have distance zero, so they must actually be the same point. The sequence is eventually constant and therefore converges. Even an infinite set becomes complete under the discrete metric.

## Completeness is not just about the set

The real numbers with their ordinary metric are complete. Can we keep the same points but pick a metric that loses completeness? Yes. For two real numbers, measure the absolute difference between their arctangents. Arctangent is strictly increasing, so this really is a metric.

Now look at the sequence of positive integers. Their arctangents approach a right angle, so the differences between late arctangents become very small. In our new metric, the integer sequence is Cauchy. But there is no real number whose arctangent is exactly a right angle. The sequence has no limit inside the real numbers with this metric.

No points were removed from the underlying set. We changed the distances, and completeness changed with them. The example also shows why a theorem about the ordinary real line should not automatically be exported to an arbitrary metric imposed on the same collection of points.

## Continuity without a coordinate system

A function between metric spaces is continuous at a point if sufficiently small changes of input distance force arbitrarily small changes of output distance. The desired output tolerance is chosen first. The input tolerance may depend on that output tolerance and on the point where continuity is being tested.

For real-valued functions on intervals, this is the epsilon-delta definition we already know. But the domain could now be a space of curves, and the output could be another space of curves. The form of the definition does not change.

There is also a sequential test. A function between metric spaces is continuous at a point precisely when it sends every sequence converging to that point to a sequence converging to the function value there.

One direction is immediate. Given an output tolerance, continuity supplies an input tolerance; convergence eventually keeps the sequence inside that input ball. For the reverse direction, suppose continuity fails. Then one can choose inputs arbitrarily close to the point whose outputs all stay at least some fixed positive distance away from the claimed output. Choosing an input within one over n of the point constructs a convergent sequence whose images fail to converge correctly. That contradiction proves continuity.

The ability to build this counterexample sequence depends on having a metric. In more general settings, sequences do not always capture every form of continuity. For metric spaces, they do.

## When the points themselves are functions

Imagine approximating a continuous curve on the interval from zero to one. The approximation is now a function, so it is not enough to ask for a single numerical error. We must decide how to compare whole functions.

A natural choice is the largest absolute difference between their values over the interval. If two curves differ by at most one hundredth at every input, their distance in this metric is at most one hundredth. This is called the uniform, or supremum, metric.

It is stronger than checking convergence at each input separately. Two approximating curves could become accurate at each fixed input eventually, while the location of their largest error keeps moving around. Under the uniform metric, one common accuracy bound must work for every input at once.

Even better, the space of continuous functions on a closed real interval is complete under this metric. To see the mechanism, start with a Cauchy sequence of continuous functions. At each fixed input, their numerical values form a Cauchy sequence of real numbers, so they have a real limit. Call the resulting pointwise limit function f. The original uniform Cauchy condition passes to that limit and shows that the approximation error is small simultaneously at all inputs. Consequently the convergence to f is uniform.

Why is f continuous? Fix an input point and a small requested output error. First choose a single sufficiently late continuous approximation that differs from f by less than one third of the error everywhere. Then use the continuity of that approximation to control its change near the input point. Two approximation errors and one local change combine, by the triangle inequality, to keep f within the required output tolerance. Thus f belongs to the same space of continuous functions.

This is a compact example of the larger method: construct a candidate limit point by point, use a uniform estimate to control the entire object, and prove the resulting object remains in the intended space.

## The question to carry forward

We have learned to say that objects are near without choosing coordinates, to recognize limits using open balls, and to distinguish internal Cauchy coherence from actual convergence in the chosen space. Completeness tells us when a Cauchy approximation process has somewhere to land.

But completeness alone does not force every sequence to have a useful convergent subsequence. The real-number sequence one, two, three, and so on is not even bounded; and an infinite discrete space is complete while its distinct-point sequence can never approach anything. To extract convergent subsequences, and to transfer powerful continuity theorems beyond closed intervals, we need a stronger form of finiteness. That is the idea of compactness.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

### Definitions and core proofs

A **metric** on a set \(X\) is \(d:X\times X\to[0,\infty)\) with
\[
 d(x,y)=0\iff x=y,\quad d(x,y)=d(y,x),\quad d(x,z)\le d(x,y)+d(y,z).
\]
The open ball is \(B_d(x,r)=\{y\in X:d(x,y)<r\}\). The sequence \(x_n\to x\) means \(\forall\varepsilon>0\;\exists N\;\forall n\ge N:d(x_n,x)<\varepsilon\). A sequence is Cauchy if \(\forall\varepsilon>0\;\exists N\;\forall m,n\ge N:d(x_m,x_n)<\varepsilon\). The space is complete if every Cauchy sequence converges in \(X\).

**Uniqueness:** If \(x_n\to x\) and \(x_n\to y\), then \(d(x,y)\le d(x,x_n)+d(x_n,y)<\varepsilon\), so \(x=y\). **Convergence implies Cauchy:** choose \(N\) giving each term distance \(<\varepsilon/2\) from the limit.

**Discrete metric:** \(d(x,y)=\mathbf 1_{x\ne y}\). Every Cauchy sequence is eventually constant; every infinite sequence of distinct points has no convergent subsequence.

**Noncomplete metric on \(\mathbb R\):** \(d(x,y)=|\arctan x-\arctan y|\). The sequence \(n\) is \(d\)-Cauchy and has no \(d\)-limit in \(\mathbb R\).

**Sequential continuity:** \(f:X\to Y\) is continuous at \(x\) iff \(x_n\to x\implies f(x_n)\to f(x)\) for all sequences. Contrapositive: if continuity fails at \(x\), there is an \(\varepsilon_0>0\) and \(x_n\) with \(d_X(x_n,x)<1/n\) but \(d_Y(f(x_n),f(x))\ge\varepsilon_0\).

**Complete function space:** For \(C([a,b])\), \(d_\infty(f,g)=\sup_{x\in[a,b]}|f(x)-g(x)|\). A Cauchy sequence \(f_n\) converges pointwise in \(\mathbb R\) to \(f\); passing \(m\to\infty\) through \(|f_n(x)-f_m(x)|<\varepsilon\) establishes the uniform bound \(|f_n(x)-f(x)|\le\varepsilon\). An epsilon-thirds continuity argument shows \(f\in C([a,b])\).

### Exercises with worked answers

1. **Two geometries.** For \(p=(0,0)\), \(q=(3,4)\), calculate the Euclidean metric and Manhattan metric. **Answer:** \(5\) and \(7\), respectively.
2. **Eventual constancy.** Let \(X\) carry the discrete metric. If \(x_n\to a\), prove \(x_n=a\) for all sufficiently large \(n\). **Answer:** take \(\varepsilon=1/2\).
3. **Incomplete without deleting points.** Why does the sequence \(x_n=n\) fail to have a limit in \((\mathbb R,d)\) with \(d(x,y)=|\arctan x-\arctan y|\)? **Answer:** a limit \(x\) would require \(\arctan x=\pi/2\), impossible for finite real \(x\).
4. **Continuity in a discrete domain.** Prove every function \(f:(X,d_{\rm disc})\to Y\) is continuous. **Answer:** the input ball of radius \(1/2\) contains only the base point, so its image has distance zero from \(f(x)\).
5. **Cauchy functions.** Suppose \(f_n\in C([0,1])\) and \(\sup_x|f_m(x)-f_n(x)|\le 1/\min(m,n)\). What uniform bound can you prove for \(f_n-f\), where \(f\) is the pointwise limit? **Answer:** \(\sup_x|f_n(x)-f(x)|\le 1/n\), by fixing \(n\) and passing \(m\to\infty\).

### Focused references

- [Wikipedia: Metric space](https://en.wikipedia.org/wiki/Metric_space) — definitions, examples, total boundedness and completeness.
- [Wikipedia: Complete metric space](https://en.wikipedia.org/wiki/Complete_metric_space) — Cauchy sequences and function-space completeness.
- Stephen Abbott, *Understanding Analysis*, chapters on sequences, continuity, and uniform convergence.
- Terence Tao, *Analysis I*, metric-space limit ideas and Cauchy reasoning.
- [MIT OpenCourseWare, 18.S190 Introduction to Metric Spaces (2023)](https://ocw.mit.edu/courses/18-s190-introduction-to-metric-spaces-january-iap-2023/pages/lecture-notes/) — MIT 18.S190, lectures 1, 2 and 5: metrics and completeness.
