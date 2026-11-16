# 029000 — Epsilon-Nets: Hitting Every Large Geometric Range

**Track:** Discrete Mathematics. **Background:** finite set systems, VC dimension, probability, and counting. **Central question:** how can a small sample be guaranteed to encounter every geometrically meaningful large subset?

<!-- BEGIN SPOKEN LECTURE -->

# A sample that cannot miss a large interval

Place twelve points in order along a straight line. Imagine that someone chooses an interval containing at least three of those points, but does not tell us which interval. We want to select a small set of sample points in advance so that every possible interval of this kind contains at least one selected point.

Here is a simple solution: select points three, six, nine, and twelve. Every run of three consecutive positions includes a multiple of three, so every interval containing at least three of our ordered points hits the sample. Four sample points have guaranteed coverage of all sufficiently large intervals, even though there are many possible intervals.

That is the idea of an epsilon-net. A net is not a collection that approximates every set in every detail. It is a sample guaranteed to hit every set occupying at least an epsilon fraction of the available mass.

The deeper question is why similarly small nets exist for large classes of geometric ranges, and why the answer depends on structure rather than on the total number of points.

# What is a range space?

A range space consists of a ground set and a chosen family of subsets called ranges. For points in the plane, the ranges might be subsets cut out by disks, axis-aligned rectangles, or half-planes. For points along a line, they might be intersections with intervals.

Equip the ground set with a probability measure. A range is called heavy if its measure is at least epsilon. An epsilon-net is a subset intersecting every heavy range. For a finite ground set with uniform measure, this means hitting every range that contains at least epsilon times the number of points.

If we let the ranges be every possible subset, there is no hope of a tiny net in general. An adversary could simply choose a large range disjoint from our sample. Geometry changes the story because geometric ranges cannot cut up small collections of points in completely arbitrary ways.

# VC dimension measures flexibility

Take an arrangement of points and ask what different patterns a range can select from them. A set of points is shattered if every subset of those points can be realized as the intersection with some range.

Intervals on the real line can shatter two distinct points. We can select neither point, the left point only, the right point only, or both, by choosing suitable intervals. But intervals cannot shatter three ordered points. To select the two endpoints without the middle one would require a disconnected interval.

Therefore intervals have VC dimension two. This is a finite numerical measure of how expressive the range family is. A family with a bounded VC dimension cannot realize all patterns on arbitrarily large samples.

The Sauer–Shelah lemma makes that statement quantitative: on m sample points, a family of VC dimension d realizes at most the sum of the binomial coefficients from zero through d, not all two to the m subsets.

# Why random samples work

Suppose a particular range occupies epsilon of the measure. If we sample m independent points, the chance of missing that range is at most one minus epsilon to the power m, which is at most the exponential of minus epsilon m.

For a finite family with M ranges, a union bound says the probability of missing at least one heavy range is at most M times that exponential. This already proves an epsilon-net exists with sample size on the order of log M divided by epsilon.

But this naive bound depends on how many ranges are listed. In geometry there may be infinitely many intervals or disks. The VC-dimension theorem replaces the raw count of ranges with a measure of how many distinct intersection patterns can appear on a finite sample.

The key technique is often called double sampling. We compare a random sample with an independent comparison sample. If some heavy range is missed by the first sample, it is likely to be visible in the second. Then we count the possible traces of ranges on the combined sample using Sauer–Shelah. The polynomial trace bound controls what would otherwise be an infinite union bound.

The result is that bounded-VC families have epsilon-nets of size on the order of d divided by epsilon, times the logarithm of one divided by epsilon. We can also incorporate a confidence parameter into the required random sample size.

# Nets are different from uniform convergence

An epsilon-net asks one-sided coverage: does our sample hit every range whose measure is at least epsilon? Uniform convergence asks a stronger numerical question: is the sample fraction inside every range close to that range's true measure?

A sample can be a good epsilon-net while giving poor estimates of some probabilities. The twelve-point sample with positions three, six, nine, and twelve certainly hits every interval of size three or more, but it is not designed to estimate the fraction in every interval precisely.

Uniform convergence typically needs an error tolerance squared in the denominator of the sample complexity. Epsilon-net coverage has a first power of epsilon. Conflating these two sampling problems hides their different goals and proof techniques.

# Why the theorem is algorithmically useful

In computational geometry, a small epsilon-net can serve as a representative set. Any range containing substantial mass is guaranteed to meet it. This allows algorithms to reduce a large search space to a much smaller sample while retaining specific coverage guarantees.

The guarantee is not free. It depends on the chosen range family and its VC dimension. If we change from intervals to an unrestricted family of arbitrary subsets, the sample theorem no longer gives the same small net. Nor does the existence theorem automatically mean that an efficient deterministic construction has been provided for every representation of the range space.

The essential result is a conversion from geometric limitations to probabilistic reliability: when a set family cannot shatter large configurations, a random sample can hit all of its large members at once.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For a range space `(X,R)` with probability measure mu, an epsilon-net `N subset X` satisfies `N intersect R != empty` for every R with `mu(R)>=epsilon`. With a finite uniform ground set of n points, this means `|R|>=epsilon*n`.

**Finite interval example.** For X={1,...,12}, ranges are contiguous intervals and epsilon=1/4. The sample N={3,6,9,12} intersects every interval of cardinality >=3: any run of 3 integers includes a multiple of 3. Intervals on the line have VC dimension exactly 2.

For a fixed heavy R, independent sampling of m points with replacement gives
\[
\Pr[N\cap R=\varnothing]=(1-\mu(R))^m\le e^{-\epsilon m}.
\]
For a finite range family with M elements, the union bound is `P(any heavy range missed)<=M e^(-epsilon*m)`. This is inadequate for infinite range families; it is *not* the proof of the VC-dimension epsilon-net theorem.

**Epsilon-net theorem (standard form).** For VC dimension d >= 1 and epsilon in (0,1/2), an iid sample of size
\[
m\ge C\left[\frac d\epsilon\log\frac1\epsilon+\frac1\epsilon\log\frac1\delta\right]
\]
forms an epsilon-net with probability at least `1-delta`, for an absolute constant C, under standard measurability conventions. This is a sampling bound, not a claim about a specific optimal deterministic algorithm.

For comparison, a safe standard VC uniform-convergence sample upper bound for error eta and confidence 1-delta has order `O((d log(1/eta)+log(1/delta))/eta^2)`. The two guarantees are different.

### Exercises with answers

1. Explain why three ordered points cannot be shattered by intervals. **Answer:** no interval can select the two endpoints while omitting the middle.
2. For X={1,...,20}, show that N={5,10,15,20} hits every interval containing at least five points. **Answer:** every five consecutive positions contain a multiple of five.
3. With epsilon=0.1 and m=30, bound the chance of missing one particular heavy range. **Answer:** at most `e^-3`.
4. Why is a union bound over all geometric disks not immediately useful? **Answer:** the disk family is infinite, and cardinality is not a finite value M; VC trace counting supplies the appropriate substitute.

### Reading and source notes

- [The Epsilon-t-Net Problem (SoCG 2020)](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.SoCG.2020.5), the classical Haussler–Welzl epsilon-net theorem and later constructions.
- [Hardness of Discrepancy Computation and Epsilon-Net Verification](https://doi.org/10.1016/j.jco.2011.09.001), epsilon-nets, VC dimension and geometric range families.
- [MIT OpenCourseWare, Mathematics for Computer Science](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/pages/readings/), supporting probability, union bounds and combinatorial counting.
