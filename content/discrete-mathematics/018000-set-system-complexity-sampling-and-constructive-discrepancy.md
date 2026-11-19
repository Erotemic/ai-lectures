# Set-system complexity, sampling, and constructive discrepancy

<!-- BEGIN SPOKEN LECTURE -->

# Set-system complexity, sampling, and constructive discrepancy

## Entropy as a Counting Tool: Shearer's Inequality

Suppose you are given an enormous family of possible configurations. Listing them is impossible, but perhaps you can look at the configurations through smaller windows: a few coordinates at a time, or a few overlapping subsets of variables. Can those limited views tell you how many full configurations there could be?

A powerful answer comes from information theory. Entropy measures uncertainty, and a uniform random choice from a finite family has entropy equal to the logarithm of the family's size. This turns a counting problem into an inequality about random variables. The surprising part is that overlapping partial views can be combined without counting the same information too many times.

### Why logarithms make counting easier

Take a finite set F of permitted binary strings, all of the same length. Choose one string uniformly at random, and call its coordinates X one through X n. Knowing the whole random string is equivalent to identifying one of the members of F. In base-two units, the uncertainty is the logarithm of the number of strings.

If the coordinates were independent fair bits, the entropy would simply be n. Constraints introduce dependence and can lower the entropy. For example, if every string must have its last bit equal to its first bit, those two coordinates contribute only one independent choice. The entropy of the complete string is not the sum of the entropies of its coordinates.

The chain rule tells us how to account for dependence. Reveal the coordinates one at a time. The entropy of the entire string is the entropy of the first bit, plus the additional uncertainty of the second bit after learning the first, and so on. Each term is a conditional entropy, and conditioning on more information cannot increase it.

This simple observation does much of the work in combinatorial entropy arguments.

### The covering inequality

Imagine selecting several subsets of the coordinate positions. For each subset, observe only the coordinates it contains. Assume that every coordinate position is included in at least r of these selected subsets. Shearer's inequality says that the entropy of the full vector, multiplied by r, cannot exceed the sum of the entropies of the observed subvectors.

The factor r prevents double-counting. If each coordinate is observed twice, the total entropy of all the partial observations must be at least twice the entropy of the original vector. Overlap is not a nuisance that invalidates the estimate; the proof uses the coverage multiplicity explicitly.

Here is the proof idea. Fix an order in which all coordinates will be revealed. For each chosen subset, expand the entropy of its projection using the chain rule. The conditional uncertainty of one coordinate given earlier coordinates inside the subset is at least the conditional uncertainty given all earlier coordinates in the full vector. A subset knows less history, so it cannot be more certain. Add the resulting lower bounds over all subsets. Every full-vector chain-rule term appears at least r times. That gives the claimed inequality.

There is nothing asymptotic about the result. It works for any finite collection of discrete random variables, and the subsets need not be the same size. The ordering of coordinates is arbitrary, yet the final inequality does not depend on it.

### From entropy back to counting

For a concrete combinatorial use, let F be the family of valid assignments and choose an assignment uniformly. The entropy of the full vector is log base two of the size of F. Each projected vector takes values in the projection of F onto its chosen coordinates, so its entropy cannot exceed the logarithm of the size of that projection.

Combining these statements gives a counting inequality. The size of F, raised to the power r, is at most the product of the sizes of all its selected coordinate projections. It is a bound on a high-dimensional collection using lower-dimensional shadows.

Consider a finite set S of points in a three-dimensional integer lattice. Project it onto the three coordinate planes. Every coordinate appears in exactly two of these three projections. Shearer's inequality says that the square of the number of points in S is at most the product of the numbers of points in its three shadows. This is the discrete Loomis–Whitney inequality.

For a rectangular box of grid points, equality holds. If there are a choices of first coordinate, b of second, and c of third, the whole box has a times b times c points. Its coordinate-plane projections have a times b, a times c, and b times c points. Their product is the square of the original count. Thus the inequality is tight, not merely a loose estimate with the right general shape.

### A four-string example

Take the four binary strings of length three having at most one coordinate equal to one. There are four possibilities: all zero, or a single one in one of three positions. Each projection onto a pair of coordinates has three possible values: zero-zero, one-zero, and zero-one. If we observe all three pairs of coordinates, every original coordinate is represented in two observations.

The counting inequality tells us that four squared cannot exceed three cubed. Sixteen is indeed no greater than twenty-seven. This particular example does not attain equality, but it lets us see exactly how a restriction on full configurations is reflected in limited views.

Notice what the method did not need. We did not derive a recurrence for the family, enumerate all allowed objects, or solve a generating function. The argument used only a random choice, projections, and an entropy inequality.

### When the method is useful and when it is not

Entropy bounds are particularly effective when a complicated combinatorial object has several overlapping descriptions, each of which is easy to count. They can control families of subsets, incidence structures, arrangements, and constrained configurations. Some sharp graph-theoretic counting theorems use considerably more sophisticated entropy decompositions, but this is the essential starting point.

The method does not produce an exact count by itself. If the projections are large or if their overlap structure is poorly chosen, the bound may be weak. Choosing the right coordinate subsets is a mathematical decision, not an automatic consequence of writing down an entropy expression.

It is also important not to confuse the entropy of a particular distribution with the logarithm of the entire possible support. Equality holds for a uniform distribution on the support; otherwise entropy is smaller. In counting proofs we often choose the uniform distribution precisely to make the two coincide.

The deeper lesson is that information cannot be manufactured by viewing the same system through several windows. Once we quantify how often each coordinate has been observed, we can turn this conservation of uncertainty into rigorous bounds on the number of combinatorial possibilities.

## Extremal Set Systems: Intersections, Sunflowers, and Forced Structure

Suppose we collect many different subsets of the same ground set. Some pairs may overlap, some may be disjoint, and some may share exactly the same intersection. When the collection becomes sufficiently large, can it still avoid every simple pattern we might ask for?

Extremal set theory studies such questions. Rather than asking how many subsets exist in total, it asks how many can exist under a restriction. The restriction might forbid disjoint pairs, forbid long inclusion chains, or forbid a group of sets whose pairwise intersections are identical.

Begin with a collection of k-element subsets of an n-element set. There are n choose k possible members. If we demand that every two chosen subsets intersect, we have thrown away many possibilities. A natural construction is a *star*: fix one element and take all k-element sets containing it. The star has n minus one choose k minus one members, and every pair intersects at the chosen element.

The Erdős–Ko–Rado theorem says that when n is at least twice k, no intersecting family of k-element subsets is larger than a star. For n greater than twice k, stars are the unique extremal families up to relabeling. At the boundary n equals twice k, other extremal configurations can also exist. The exact hypothesis is important: if n is smaller than twice k, *every* two k-element subsets already intersect, so the whole collection works.

### A small case we can see

Take k equals two. Our sets are edges of a graph, and pairwise intersection means any two edges share a vertex. A triangle has three edges and every pair meets. A star with n minus one edges also works. For at least five vertices, a star beats the triangle, and in fact any pairwise-intersecting family of two-element subsets is either contained in a star or is the three edges of a triangle.

Here is the argument. Choose two distinct edges, say a-b and a-c, sharing a. Any other edge avoiding a must meet both; therefore it must be b-c. Once b-c is present, another edge must meet all three. It can only be one of the triangle's edges. So the family is either centered at a or limited to a triangle.

This is extremal reasoning in miniature: identify a nearly forced structure, then show that one exceptional choice constrains everything else.

### Sunflowers: identical intersections

A different pattern is a sunflower. Its petals are sets whose pairwise intersections are all equal to one common core. If the core is empty, the petals are pairwise disjoint. If the core is nonempty, the petals share the core but are otherwise disjoint.

The classical sunflower lemma gives a threshold independent of the size of the ground set. Fix a petal size k and a desired number r of petals. If a family of distinct k-element sets has more than k factorial times r minus one to the kth power members, it must contain an r-petal sunflower. This bound is not generally sharp, but its proof is particularly instructive.

We use induction on k. For k equals one, if we have at least r distinct singleton sets, they are disjoint and form a sunflower. Now consider a large family of k-element sets. Choose a maximal collection of mutually disjoint members. If there are at least r, we already have a sunflower with empty core. Otherwise there are at most r minus one disjoint sets.

Their union contains at most k times r minus one elements. Because the disjoint collection was maximal, every set in our family meets this union. By averaging, some element of the union must belong to at least a fraction one over k times r minus one of the family.

Keep only sets containing that element, and remove the chosen element from each. These are distinct sets of size k minus one. If the original family exceeded the stated threshold, the smaller family exceeds the induction threshold. It therefore contains an r-petal sunflower. Put the removed element back into every petal. The common core grows by that element, and we have the required sunflower in the original family.

Notice what the proof did not need. It did not examine every possible intersection pattern. It used either a disjoint packing or a heavily represented element. Those are the only two branches of the argument, and together they force the structure.

### Why these theorems matter algorithmically

Sunflowers are useful in parameterized algorithms. If a family of small sets is too large, a sunflower identifies petals that behave redundantly for certain hitting-set decisions. With careful reduction rules, this leads to finite problem kernels: instances whose size is bounded by a function of the parameter rather than by the original number of sets.

But the reduction must be proved for the exact decision problem. Deleting arbitrary petals because they look similar need not preserve solutions. The sunflower gives combinatorial structure; an algorithm still needs a sound equivalence argument.

The more general lesson is a common one across discrete mathematics. Large collections cannot always remain unstructured. Extremal bounds translate forbidden configurations into numerical limits. Once the count exceeds the limit, the missing pattern is logically forced. The strongest results often come from finding a simple construction that meets a bound and a proof showing every larger construction fails.

## VC Dimension: How Many Patterns Can a Family Realize?

Imagine placing a finite set of points on the real number line. We want to label each point either selected or not selected. An unrestricted family of subsets can realize every one of the two-to-the-n possible labelings of n points. But suppose our allowed subsets are intervals. Then a selected set of ordered points must form one consecutive block. We can choose where that block begins and ends, but we cannot select the first and third points while omitting the second.

So intervals on the real line form an infinite family, yet their ability to express arbitrary labelings is limited. This observation leads to Vapnik–Chervonenkis dimension, usually called VC dimension. It is a combinatorial measurement of expressiveness, not a dimension in the sense of vector spaces.

A set system consists of a ground set X and a family of subsets of X. Given a finite sample S inside X, look at every intersection of a family member with S. Those intersections are the labelings the family can produce on that sample. If all subsets of S arise, we say the family shatters S.

The VC dimension is the largest size of a shattered set, when that maximum exists; otherwise it is infinite. A family can have many sets without shattering even three points. That distinction is useful in combinatorics, statistics, geometric range searching, and learning theory.

## Two concrete examples

Consider left half-lines on the real line: for a threshold a, select every point less than or equal to a. One point can be selected or not selected, so a single point is shattered. But two distinct ordered points cannot be labeled with only the larger one selected. Therefore the VC dimension is one.

Now consider all bounded intervals. Pick two ordered points. An interval can contain neither, only the first, only the second, or both. So the two-point set is shattered. Pick three ordered points. An interval cannot select the outer two while omitting the middle one. So three points are never shattered. The VC dimension of intervals is two.

A numerical observation now appears. On n ordered sample points, intervals create one labeling for the empty set and one labeling for each consecutive nonempty block. There are n choices for a one-point block, n minus one for a two-point block, and so on. The total is one plus n times n plus one divided by two. That grows quadratically, not exponentially.

## The Sauer–Shelah phenomenon

This polynomial-versus-exponential distinction generalizes. The Sauer–Shelah lemma says that if a family has VC dimension d, then on n sample points it realizes at most the sum of the binomial coefficients choosing zero through d elements from n.

When d is fixed, the sum grows on the order of n to the d-th power. So a prohibition against shattering one additional point dramatically restricts the number of traces a set system can create. There may still be infinitely many sets in the original family, but their behavior on any finite sample is controlled.

Why should that binomial sum appear? One extreme family gives a clue. Take all subsets with at most d elements. It cannot shatter d plus one points, because the labeling selecting all d plus one is missing. Yet every subset of at most d sample points is realized. Its number of traces is exactly the binomial sum. So the bound, if true, is sharp.

## An inductive proof that counts both branches

We can prove the lemma by induction on the size of the sample. Choose one distinguished point and split the family of traces into those that omit that point and those that contain it. Delete the distinguished point from both parts, obtaining two families on the remaining sample.

Some smaller subsets may appear in both families. Count the union of the two smaller families, then add the intersection. This exactly counts the original traces, because an overlapping smaller subset corresponds to two original traces, one with the distinguished point and one without.

The union cannot shatter more than d points. If it shattered d plus one, those same label patterns would already show that the original family shattered d plus one points. The intersection has an even stronger restriction: it cannot shatter d points. If it did, each labeling of those d points would appear both with and without the distinguished point, giving all labelings of d plus one points.

Therefore the union is bounded by the size-n-minus-one Sauer–Shelah expression with dimension d, and the intersection by the expression with dimension d minus one. Adding these bounds combines adjacent binomial coefficients, exactly as in Pascal's identity, to obtain the claimed bound for n points.

This proof illustrates a general combinatorial technique. Separate configurations according to a chosen element, identify what appears in one branch and what appears in both, then use an induction that reduces both the ground-set size and the complexity parameter.

## What this does and does not imply

VC dimension is useful for statistical learning because it controls the number of distinct classifications possible on a finite sample. Coupled with probability inequalities, this leads to uniform convergence bounds: empirical frequencies can approximate true frequencies simultaneously over all sets in a class, with sample requirements depending on VC dimension rather than the total number of sets.

But a low VC dimension does not magically guarantee a useful predictor. Learning guarantees also require assumptions about how data are sampled, what loss is measured, and whether the target class is appropriate. Likewise, the Sauer–Shelah lemma is a combinatorial statement: it controls trace counts, not directly the computational time required to find a good classifier.

The point to retain is that expressive power can be measured by how many patterns a family can realize, not merely by how many members the family contains. The same transition from arbitrary subsets to restricted patterns will appear again when we color set systems and ask how much imbalance is inevitable.

## Discrepancy: Balancing Many Sets at Once

Suppose a warehouse contains many items, and we must assign every item to one of two teams. We would like each team to receive approximately half of every category: heavy items, fragile items, expensive items, and items required for a particular job. An assignment that balances one category may produce a large imbalance in another.

Mathematically, we have a ground set of items and a family of distinguished subsets. We assign each element a sign, plus one or minus one. For each distinguished subset, add the signs of its elements. That signed sum is its imbalance. Discrepancy theory asks us to make the largest absolute imbalance as small as possible.

If there is only one subset containing an even number of elements, we can balance it perfectly by choosing equal numbers of plus and minus signs. But if the family includes many overlapping subsets, their requirements compete. The challenge is simultaneous balance.

## From a set family to a matrix

Write an incidence matrix whose rows correspond to the distinguished subsets and whose columns correspond to elements. Each entry is one when the element belongs to that subset, and zero otherwise. A coloring becomes a vector of plus and minus ones. The row sums of the matrix times that vector are exactly the discrepancies of the sets.

This matrix viewpoint is useful because it connects discrepancy to numerical linear algebra. The goal is to choose a sign vector whose image under the incidence matrix has small maximum absolute coordinate. Unlike least squares, we do not get to choose arbitrary real coefficients: each coordinate must be exactly plus or minus one.

For a path of four items with distinguished subsets consisting of consecutive pairs, alternating signs plus, minus, plus, minus produce discrepancy zero in every pair. But add a different collection of subsets, and a perfect assignment may cease to exist. We need upper bounds that work without discovering an exact zero-discrepancy solution.

## Random signs already give a bound

The first strategy is the same probabilistic idea we used in the earlier combinatorics lectures: assign each element an independent fair sign. For any particular subset containing r items, the expected signed sum is zero. A concentration bound says that large deviations from zero are exponentially unlikely in the square of the threshold divided by r.

If there are m distinguished subsets and each has at most r elements, we can take a union bound over all m possible failures. The probability that any subset has imbalance larger than a certain threshold is at most two m times an exponential term. Choose the threshold slightly larger than the square root of two r times the logarithm of two m. Then the upper bound drops below one.

A probability smaller than one for failure proves that some coloring succeeds. It also gives a useful randomized algorithm when the success probability is sufficiently high, or when a method of conditional expectation can derandomize the bound.

Notice what this result depends on. It grows with the size of the largest set and logarithmically with the number of constrained sets. It does not promise square-root-of-n discrepancy for every possible family of subsets: a family with exponentially many sets can defeat that expectation.

## The family of all subsets shows the limit

Take every subset of an n-element ground set as a constraint. Given any coloring, look at the set of all positively colored elements and the set of all negatively colored elements. One of those two sets has at least half the elements. Its signed sum has magnitude at least n over two.

Because both sets belong to the family, the discrepancy of the complete set system is at least n over two for every coloring. In fact it is exactly the larger of the number of plus and minus signs, so the optimum is the ceiling of n over two.

This example matters because it prevents us from overstating the power of random coloring. A guarantee must depend on structural information about the family. A low number of sets, small membership degrees, geometric structure, or limited combinatorial complexity can all help.

## Partial coloring: do not decide everything at once

A major advance in discrepancy theory is to avoid fixing every sign immediately. A partial coloring assigns plus or minus one to some elements and leaves others temporarily uncolored. We try to color a substantial fraction while keeping each constrained sum under control. Then we repeat on the remaining elements.

Why can this help? A fully colored sign vector lives at a vertex of a high-dimensional cube. A partial coloring can be found by moving through the cube while satisfying or approximately satisfying many linear constraints. Each round decreases the number of undecided coordinates. If the imbalance added at successive rounds is controlled, the total imbalance remains small.

This is the central strategy behind powerful partial-coloring theorems. Their proofs require more than the elementary union bound: dimension counting, entropy arguments, or randomized walks can locate colorings with many coordinates fixed and all constraints reasonably balanced.

A famous result says that when the number of sets is comparable to the number of elements, the discrepancy can be bounded on the order of the square root of the number of elements, with a universal constant. This is stronger than a direct union bound in that regime. But there are important hypotheses on the family size, and the proof is not simply 'color randomly and hope.'

## Membership degree and geometry

Another structural parameter is how many sets contain a single element. If each element appears in at most t distinguished subsets, one can obtain a discrepancy bound linear in t. This is the setting of the Beck–Fiala theorem. A dense family can have many sets, yet remain easy to balance when each element affects only a few constraints.

Geometric set systems offer a different form of structure. Intervals, rectangles, halfspaces, and other ranges have controlled pattern complexity, often described using VC dimension. But VC dimension and discrepancy are not the same invariant. Low VC dimension may support refined bounds under additional conditions; it does not imply a single universal discrepancy formula.

The broader idea is that constrained choices can become easier when we exploit how constraints overlap. Randomization gives a baseline. Partial coloring and geometric or algebraic structure improve the bound. For optimization, resource allocation, and computational geometry, the problem is not merely to split objects into two groups; it is to split them while respecting many measurements simultaneously.

## Epsilon-Nets: Hitting Every Large Geometric Range

Place twelve points in order along a straight line. Imagine that someone chooses an interval containing at least three of those points, but does not tell us which interval. We want to select a small set of sample points in advance so that every possible interval of this kind contains at least one selected point.

Here is a simple solution: select points three, six, nine, and twelve. Every run of three consecutive positions includes a multiple of three, so every interval containing at least three of our ordered points hits the sample. Four sample points have guaranteed coverage of all sufficiently large intervals, even though there are many possible intervals.

That is the idea of an epsilon-net. A net is not a collection that approximates every set in every detail. It is a sample guaranteed to hit every set occupying at least an epsilon fraction of the available mass.

The deeper question is why similarly small nets exist for large classes of geometric ranges, and why the answer depends on structure rather than on the total number of points.

## What is a range space?

A range space consists of a ground set and a chosen family of subsets called ranges. For points in the plane, the ranges might be subsets cut out by disks, axis-aligned rectangles, or half-planes. For points along a line, they might be intersections with intervals.

Equip the ground set with a probability measure. A range is called heavy if its measure is at least epsilon. An epsilon-net is a subset intersecting every heavy range. For a finite ground set with uniform measure, this means hitting every range that contains at least epsilon times the number of points.

If we let the ranges be every possible subset, there is no hope of a tiny net in general. An adversary could simply choose a large range disjoint from our sample. Geometry changes the story because geometric ranges cannot cut up small collections of points in completely arbitrary ways.

## VC dimension measures flexibility

Take an arrangement of points and ask what different patterns a range can select from them. A set of points is shattered if every subset of those points can be realized as the intersection with some range.

Intervals on the real line can shatter two distinct points. We can select neither point, the left point only, the right point only, or both, by choosing suitable intervals. But intervals cannot shatter three ordered points. To select the two endpoints without the middle one would require a disconnected interval.

Therefore intervals have VC dimension two. This is a finite numerical measure of how expressive the range family is. A family with a bounded VC dimension cannot realize all patterns on arbitrarily large samples.

The Sauer–Shelah lemma makes that statement quantitative: on m sample points, a family of VC dimension d realizes at most the sum of the binomial coefficients from zero through d, not all two to the m subsets.

## Why random samples work

Suppose a particular range occupies epsilon of the measure. If we sample m independent points, the chance of missing that range is at most one minus epsilon to the power m, which is at most the exponential of minus epsilon m.

For a finite family with M ranges, a union bound says the probability of missing at least one heavy range is at most M times that exponential. This already proves an epsilon-net exists with sample size on the order of log M divided by epsilon.

But this naive bound depends on how many ranges are listed. In geometry there may be infinitely many intervals or disks. The VC-dimension theorem replaces the raw count of ranges with a measure of how many distinct intersection patterns can appear on a finite sample.

The key technique is often called double sampling. We compare a random sample with an independent comparison sample. If some heavy range is missed by the first sample, it is likely to be visible in the second. Then we count the possible traces of ranges on the combined sample using Sauer–Shelah. The polynomial trace bound controls what would otherwise be an infinite union bound.

The result is that bounded-VC families have epsilon-nets of size on the order of d divided by epsilon, times the logarithm of one divided by epsilon. We can also incorporate a confidence parameter into the required random sample size.

## Nets are different from uniform convergence

An epsilon-net asks one-sided coverage: does our sample hit every range whose measure is at least epsilon? Uniform convergence asks a stronger numerical question: is the sample fraction inside every range close to that range's true measure?

A sample can be a good epsilon-net while giving poor estimates of some probabilities. The twelve-point sample with positions three, six, nine, and twelve certainly hits every interval of size three or more, but it is not designed to estimate the fraction in every interval precisely.

Uniform convergence typically needs an error tolerance squared in the denominator of the sample complexity. Epsilon-net coverage has a first power of epsilon. Conflating these two sampling problems hides their different goals and proof techniques.

## Why the theorem is algorithmically useful

In computational geometry, a small epsilon-net can serve as a representative set. Any range containing substantial mass is guaranteed to meet it. This allows algorithms to reduce a large search space to a much smaller sample while retaining specific coverage guarantees.

The guarantee is not free. It depends on the chosen range family and its VC dimension. If we change from intervals to an unrestricted family of arbitrary subsets, the sample theorem no longer gives the same small net. Nor does the existence theorem automatically mean that an efficient deterministic construction has been provided for every representation of the range space.

The essential result is a conversion from geometric limitations to probabilistic reliability: when a set family cannot shatter large configurations, a random sample can hit all of its large members at once.

## Constructive Discrepancy: From Random Signs to Partial Coloring

Suppose we have a collection of objects, and several different groups of objects that we care about. We must color every object red or blue. For each group, we count red as plus one and blue as minus one, and measure the absolute value of the sum. That number is the imbalance, or discrepancy, of the group.

If every group could be handled independently, we would just split each as evenly as possible. But the groups overlap. A color choice that balances one group may unbalance another. Discrepancy theory studies how much simultaneous imbalance is unavoidable, and how good a coloring we can construct.

There is a difference between proving that a coloring exists and finding one efficiently. The two tasks can use different mathematical ideas. Random signs give a simple existence argument; conditional expectation can turn that argument into a deterministic algorithm. More powerful bounds need more delicate algorithms, such as semidefinite rounding or constrained random walks.

## Start with four objects

Number four objects from one through four. Consider the sets consisting of the first two objects, the middle two, and the last two. Color them plus, minus, plus, minus. Each of the three sets has sum zero.

This shows perfect balancing is possible for this particular family. But if we also include every singleton set, no coloring can have discrepancy zero, because every singleton contains exactly one sign. Its absolute sum is one. The attainable discrepancy is controlled by the incidence structure, not just by our skill in choosing colors.

Represent a set system by a matrix with one row per set and one column per object. Put a one wherever an object belongs to a set and a zero elsewhere. A coloring is a vector of signs. Its discrepancies are the absolute values of the entries of the matrix times that sign vector.

The matrix viewpoint exposes the connection to rounding and optimization: we are trying to choose a vertex of the hypercube, with entries plus or minus one, while keeping many linear forms small.

## Random signs and a union bound

Give every object an independent random sign. For any fixed set, the expected sum is zero. If the set contains s elements, its sum is a collection of s independent centered signs. Hoeffding's inequality says the chance that its absolute sum exceeds t is at most two times the exponential of minus t squared divided by twice s.

If every set has size at most n and there are m sets, the probability that any set exceeds t is bounded by two m times the exponential of minus t squared divided by twice n. Choose t proportional to the square root of n times the logarithm of m. This makes the probability of failure smaller than one.

We have now proved that some coloring exists with discrepancy at most that threshold. But the proof as stated is existential. We could keep sampling colorings until one works, but that introduces randomness into our procedure and may not be the most efficient strategy.

## Making the random proof constructive

A standard derandomization technique is conditional expectation. Instead of assigning every sign at once, we choose signs one at a time. At each step, choose a sign so that the conditional expected value of a suitable potential does not increase.

A useful potential is the sum, over all rows, of two exponentials: one exponential of the positive weighted row sum, and the other of its negative. These exponentials penalize large absolute values. Initially, under random signs, their expectation can be bounded using a hyperbolic-cosine estimate. Once we choose a sign, we recompute the two possible conditional expectations and take the smaller one.

One of the two choices must have conditional expectation no larger than the current expectation, because the current value is their average. Repeating this yields a fully specified sign vector whose exponential potential is no larger than the initial bound. A large discrepancy would force one exponential term above that bound, so it cannot occur.

This method produces the same logarithmic style of discrepancy bound as the elementary random-sign argument. It is not yet the stronger bound that says, roughly, that n sets on n objects can all be balanced with discrepancy on the order of the square root of n.

## Why partial coloring is stronger

The remarkable idea behind the stronger bound is to avoid forcing every variable to a sign immediately. Start with entries allowed to vary continuously between minus one and plus one. Keep the important linear constraints under control while moving until a substantial fraction of the variables reach the boundary. Those variables are now permanently colored.

We call this a partial coloring. The uncolored variables remain available for another round. If the number of uncolored variables decreases geometrically, we can attempt to sum the discrepancy introduced in each round. Strong theorems show that, under the appropriate relation between the number of sets and objects, the total is much smaller than the naive random-sign union-bound estimate.

The proof and algorithm must control many correlated constraints at once. This is where the geometry of high-dimensional convex sets and random walks becomes useful. An algorithm can move within the face of a cube while respecting nearly tight constraints. At each stage enough coordinates reach their extreme values, and the process eventually produces a full coloring.

## Constructive does not mean effortless

Spencer's six-standard-deviations theorem gives a discrepancy bound of order square root n for n sets on n elements. The original theorem did not itself provide the later efficient algorithms that achieve comparable bounds. Algorithmic developments by Bansal, and then by Lovett and Meka, supplied constructive methods based on semidefinite programming or a carefully restricted random walk.

It is important not to claim that the simple conditional-expectation potential automatically proves Spencer's sharper result. It proves a weaker, logarithmic bound. The stronger bound uses genuinely different ideas to exploit the simultaneous structure of the constraints.

## Choosing the tool for the guarantee

We can now distinguish three levels of result. Independent random signs show that good balance is possible. Conditional expectation gives an explicit deterministic construction for the elementary bound. Partial-coloring algorithms reach stronger guarantees for important families, but with additional analysis and algorithmic machinery.

The matrix description makes all three levels comparable. The objects are columns, the demands are rows, and the signs are discrete decisions. Discrepancy measures how well the rounding preserves many linear constraints at once. This is why the subject appears in sampling, computational geometry, approximation algorithms, and numerical rounding.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Entropy as a Counting Tool: Shearer's Inequality

**Track:** Discrete Mathematics and Combinatorics. **Background:** elementary probability, set families, projections, conditional probability. **Central question:** how can uncertainty place sharp limits on how many combinatorial objects are possible?

#### Mathematical companion (not spoken)

For finite discrete random variables \(X=(X_1,\ldots,X_n)\), entropy in bits is \(H(X)=-\sum_x p(x)\log_2 p(x)\). The chain rule and monotonicity under conditioning give
\[H(X)=\sum_{i=1}^n H(X_i\mid X_1,\ldots,X_{i-1}),\quad H(Y\mid Z,W)\le H(Y\mid Z).\]
**Shearer's inequality:** let \(\mathcal A\) be a collection of subsets of \([n]\), counted with multiplicity if desired, such that each i belongs to at least r members. Then
\[r H(X)\le\sum_{A\in\mathcal A} H(X_A).\]
Proof: for each A use the chain rule in the global coordinate order and bound each \(H(X_i\mid X_{A\cap[i-1]})\ge H(X_i\mid X_{[i-1]})\); sum over A.

For a finite family \(F\subseteq\prod_i\Omega_i\), let X be uniform over F. Since \(H(X)=\log_2|F|\), and \(H(X_A)\le\log_2|\pi_A(F)|\), we conclude
\[|F|^r\le\prod_{A\in\mathcal A}|\pi_A(F)|.\]
**Discrete Loomis–Whitney:** if \(S\subseteq A\times B\times C\) is finite, then
\[|S|^2\le |\pi_{AB}(S)|\,|\pi_{AC}(S)|\,|\pi_{BC}(S)|.\]
Equality holds for Cartesian-product boxes. For \(F=\{000,100,010,001\}\), all three pair projections have size 3, yielding \(4^2\le3^3\).

##### Exercises with answers

1. Why is \(H(X)=\log_2|F|\) when X is uniform on F? **Answer:** each outcome has probability \(1/|F|\), so the sum gives log of the cardinality.
2. Explain why observing coordinates \(1,2\) and \(2,3\) alone does not permit r=2. **Answer:** coordinates 1 and 3 appear only once; r can be at most 1.
3. Verify equality for a box \(S=A\times B\times C\). **Answer:** the product of projection sizes is \((|A||B|)(|A||C|)(|B||C|)=|S|^2\).
4. Can the counting inequality prove an exact enumeration for an arbitrary family? **Answer:** not in general; it supplies bounds, with equality only under additional structural conditions.

##### Reading and source notes

- [*Entropy Methods in Combinatorics* (ICM 2026 survey)](https://epubs.siam.org/doi/full/10.1137/25M180874X), treatment of Shearer's inequality and its history.
- Jaikumar Radhakrishnan, [*Entropy and Counting*](https://bpb-us-e1.wpmucdn.com/sites.harvard.edu/dist/7/800/files/2024/10/spring2016-cs229r-radhakrishnan_survey.pdf), lecture notes on combinatorial entropy methods.
- [MIT OpenCourseWare, Mathematics for Computer Science](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/), probability and counting prerequisites.

### Extremal Set Systems: Intersections, Sunflowers, and Forced Structure

**Track:** Discrete Mathematics. **Background:** binomial coefficients, counting, graph extremal theory. **Central question:** when does a large collection of subsets have to contain a highly organized pattern?

#### Mathematical companion (not spoken)

For a k-uniform intersecting family `F subset binom([n],k)`, the Erdős–Ko–Rado theorem states, for `n >= 2k`,
\[
|F|\leq \binom{n-1}{k-1}.
\]
For `n>2k`, equality forces a star (up to relabeling); at `n=2k`, uniqueness fails. A full proof for arbitrary k uses more than the k=2 illustration in narration.

An r-sunflower is a family `S_1,...,S_r` with `S_i cap S_j=C` for all `i!=j`. Erdős–Rado's elementary sunflower lemma: any family of **distinct k-element sets** of size greater than `k!(r-1)^k` contains an r-sunflower.

Induction: let `D` be a maximal disjoint subfamily. If `|D|>=r`, done. Else its union `U` has size at most `k(r-1)` and intersects every set in `F`. Some `x in U` belongs to at least `|F|/[k(r-1)] > (k-1)!(r-1)^{k-1}` sets. Remove x from that subfamily, apply induction to its `(k-1)`-sets, and restore x.

For k=2, if edges ab and ac share a, an edge avoiding a must equal bc. Any edge meeting ab, ac and bc lies in the triangle, so pairwise-intersecting edge families are stars or subfamilies of triangles.

##### Exercises with answers

1. How many k-sets are in a star on an n-element ground set? **Answer:** `binom(n-1,k-1)`.
2. Give a three-petal sunflower with nonempty core. **Answer:** `{1,2},{1,3},{1,4}`, whose core is `{1}`.
3. What happens if the maximal disjoint family in the proof has at least r members? **Answer:** it is already an r-sunflower with empty core.
4. For `k=2,r=3`, what simple numerical threshold follows from the classical lemma? **Answer:** more than `2!*(2)^2=8` distinct edges, though the bound is not tight.

##### Reading and source notes

- [Erdős, Ko, and Rado, Intersection Theorems for Systems of Finite Sets](https://doi.org/10.1093/qmath/12.1.313), the classical intersecting-family theorem.
- [Alon and Spencer, The Probabilistic Method](https://www.wiley.com/en-us/The+Probabilistic+Method%2C+4th+Edition-p-9781119061953), sunflower arguments and extremal techniques.
- [Wikipedia, Sunflower Lemma](https://en.wikipedia.org/wiki/Sunflower_lemma), statement and elementary proof overview; use the primary treatments for sharp variants.

### VC Dimension: How Many Patterns Can a Family Realize?

**Track:** Discrete Mathematics. **Background:** set systems, combinatorial counting, binomial coefficients, and learning-theoretic examples. **Central question:** how can a family contain infinitely many sets yet have limited combinatorial complexity?

#### Mathematical companion (not spoken)

For a family `F subseteq P(X)` and finite `S subseteq X`, its trace is `F|S={A cap S:A in F}`. It **shatters** S if `F|S=P(S)`. Write `VCdim(F)=d` if d is the maximum size of a shattered finite S, and infinity if unbounded.

**Sauer–Shelah bound:** For `|S|=n`, if `VCdim(F)<=d`, then
\[
|\mathcal F|_S|\le\sum_{j=0}^{d}\binom nj,
\]
with the convention that the upper limit is capped at n. A family of all subsets of size at most d attains equality.

**Proof recurrence.** Given `F subseteq P([n])`, define `F_0={A subseteq [n-1]:A in F}`, `F_1={A subseteq [n-1]:A union {n} in F}`. Then
\[
|F|=|F_0\cup F_1|+|F_0\cap F_1|.
\]
`VCdim(F_0 union F_1)<=d`, while `VCdim(F_0 cap F_1)<=d-1`: shattering d points in the intersection would shatter those d plus the distinguished point in F. Induction and Pascal's identity give the result.

For intervals on n ordered real points, the trace family consists of the empty set and consecutive blocks, with size `1+n(n+1)/2 = sum_{j=0}^2 binom(n,j)` for n at least two. Threshold rays have VC dimension one, and intervals have VC dimension two.

##### Exercises with answers

1. Why do three ordered points fail to be shattered by intervals? **Answer:** the labeling choosing the outer two but omitting the middle one is impossible.
2. How many traces can a VC-dimension-three family realize on six points? **Answer:** at most `1+6+15+20=42`.
3. Which family attains the Sauer–Shelah bound? **Answer:** all subsets of size at most d of an n-point ground set.
4. Does VC dimension itself prove an algorithm runs in polynomial time? **Answer:** no; the theorem bounds distinct traces, not the cost of finding or optimizing a member.

##### Reading and source notes

- [ETH Zürich, Lecture Notes on VC Dimension](https://metaphor.ethz.ch/x/2025/hs/401-4627-00L/ex/Lecture06.pdf), VC shattering, growth functions and Sauer–Shelah bounds.
- [Vapnik and Chervonenkis, On the Uniform Convergence of Relative Frequencies](https://doi.org/10.1137/1116025), foundational uniform-convergence framework.
- [Chazelle, The Discrepancy Method](https://www.cs.princeton.edu/~chazelle/pubs/book.pdf), set systems, VC dimension and discrepancy links.

### Discrepancy: Balancing Many Sets at Once

**Track:** Discrete Mathematics. **Background:** set systems, concentration inequalities, randomized algorithms, and combinatorial bounds. **Central question:** can we color elements with plus and minus signs while keeping every relevant subset nearly balanced?

#### Mathematical companion (not spoken)

For set system `F subseteq P([n])` and a coloring `chi:[n]->{-1,+1}`, define
\[
\operatorname{disc}(\chi,\mathcal F)
=\max_{S\in\mathcal F}\left|\sum_{i\in S}\chi_i\right|,\qquad
\operatorname{disc}(\mathcal F)=\min_\chi\operatorname{disc}(\chi,\mathcal F).
\]
If A is the `m x n` incidence matrix, this is `min_{chi in {-1,+1}^n} ||A chi||_infinity`.

With independent Rademacher `chi_i`, Hoeffding's inequality gives for any set of size at most r:
\[
\Pr\left(\left|\sum_{i\in S}\chi_i\right|\ge t\right)
\le 2\exp\left(-\frac{t^2}{2|S|}\right)
\le 2\exp\left(-\frac{t^2}{2r}\right).
\]
Thus by a union bound `P(max_S |sum|>=t)<=2m exp(-t^2/(2r))`. Taking **strictly** `t>sqrt(2r log(2m))` proves the existence of a coloring with `max_S |sum|<t` (with the boundary interpreted appropriately for integer sums).

For the full power set `F=P([n])`, any coloring has `max_S |sum|=max(n_+,n_-)`. Therefore `disc(F)=ceil(n/2)`; this prevents a uniform `O(sqrt n)` bound over all families.

Classical stronger results include the Beck–Fiala bound `disc(F)<=2t-1` when every ground element lies in at most t sets (for positive integer t), and Spencer-type `O(sqrt n)` bounds for families with m on the order of n. These theorems require their respective hypotheses; the elementary random-sign proof above does not establish them.

##### Exercises with answers

1. A set system has 16 sets of size at most 9. Give a sufficient threshold from the union bound. **Answer:** any `t>sqrt(18 log 32)` is sufficient for existence.
2. Why does the complete power set require discrepancy at least `ceil(n/2)`? **Answer:** one of the positive and negative sign classes has at least that many elements and is a member of the family.
3. What does a partial coloring leave undecided? **Answer:** some coordinates retain value zero until later rounds.
4. Is low VC dimension identical to a bounded discrepancy guarantee? **Answer:** no; the two parameters measure different properties and additional assumptions enter specific bounds.

##### Reading and source notes

- [Chazelle, The Discrepancy Method](https://www.cs.princeton.edu/~chazelle/pubs/book.pdf), elementary, geometric and partial-coloring methods.
- [Lovett and Meka, Constructive Discrepancy Minimization by Walking on the Edges](https://arxiv.org/abs/1203.5747), randomized constructive partial-coloring methods.
- [Matoušek, Geometric Discrepancy](https://doi.org/10.1007/978-3-642-03942-3), geometric set systems and discrepancy bounds.

### Epsilon-Nets: Hitting Every Large Geometric Range

**Track:** Discrete Mathematics. **Background:** finite set systems, VC dimension, probability, and counting. **Central question:** how can a small sample be guaranteed to encounter every geometrically meaningful large subset?

#### Mathematical companion (not spoken)

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

##### Exercises with answers

1. Explain why three ordered points cannot be shattered by intervals. **Answer:** no interval can select the two endpoints while omitting the middle.
2. For X={1,...,20}, show that N={5,10,15,20} hits every interval containing at least five points. **Answer:** every five consecutive positions contain a multiple of five.
3. With epsilon=0.1 and m=30, bound the chance of missing one particular heavy range. **Answer:** at most `e^-3`.
4. Why is a union bound over all geometric disks not immediately useful? **Answer:** the disk family is infinite, and cardinality is not a finite value M; VC trace counting supplies the appropriate substitute.

##### Reading and source notes

- [The Epsilon-t-Net Problem (SoCG 2020)](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.SoCG.2020.5), the classical Haussler–Welzl epsilon-net theorem and later constructions.
- [Hardness of Discrepancy Computation and Epsilon-Net Verification](https://doi.org/10.1016/j.jco.2011.09.001), epsilon-nets, VC dimension and geometric range families.
- [MIT OpenCourseWare, Mathematics for Computer Science](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/pages/readings/), supporting probability, union bounds and combinatorial counting.

### Constructive Discrepancy: From Random Signs to Partial Coloring

**Track:** Discrete Mathematics. **Background:** probability inequalities, finite set systems, and linear algebra. **Central question:** how can we actually find a red-blue coloring whose imbalance is provably small across many overlapping sets?

#### Mathematical companion (not spoken)

Let A be the m-by-n incidence matrix of a set system. For sign vector `x in {-1,+1}^n`, discrepancy is `disc(A,x)=||Ax||_infty` and `disc(A)=min_x disc(A,x)`.

If X_j are independent Rademacher signs and row i has s_i nonzero incidence entries, Hoeffding yields
\[
\Pr\left(\left|\sum_j A_{ij}X_j\right|\ge t\right)
\le 2\exp(-t^2/(2s_i))\le2\exp(-t^2/(2n)).
\]
Hence `P(||AX||_infty >= t) <= 2m exp(-t^2/(2n))`. Taking `t=sqrt(2n log(4m))` makes this at most 1/2.

**Constructive exponential potential.** Define `Phi(x)=sum_i (exp(lambda (Ax)_i)+exp(-lambda (Ax)_i))`. Before signs are fixed,
\[
\mathbb E\Phi(X)=2\sum_i\prod_{j:A_{ij}=1}\cosh\lambda
\le 2m\exp(n\lambda^2/2).
\]
Set `lambda=sqrt(2log(4m)/n)` and `t=n lambda`. The initial expectation is at most `8m^2`, whereas a row discrepancy >= t implies `Phi >= exp(lambda t)=16m^2`. Fix signs sequentially so the conditional expectation never increases. This yields a deterministic coloring with `||Ax||_infty < t` (up to harmless boundary convention), assuming exact arithmetic in the idealized procedure.

The elementary bound is `O(sqrt(n log m))`; it is **not** Spencer's `O(sqrt n)` bound for m=n. Spencer's bound is existential, and constructive sharp-order methods are due to later work, including Bansal and Lovett–Meka.

##### Exercises with answers

1. For the set family `{1,2}`, `{2,3}`, `{3,4}`, show that `(1,-1,1,-1)` has discrepancy zero. **Answer:** each two-element sum is zero.
2. If singleton sets are included, can total discrepancy be zero? **Answer:** no; every singleton has absolute sum one.
3. Why does conditional expectation always offer a non-increasing choice for the next sign? **Answer:** the old conditional expectation is the mean of the two possible next conditional expectations.
4. Does Hoeffding plus a union bound alone prove Spencer's `O(sqrt n)` theorem for m=n? **Answer:** no; it yields an additional `sqrt(log n)` factor.

##### Reading and source notes

- [Lovett and Meka, Constructive Discrepancy Minimization by Walking on the Edges](https://doi.org/10.1137/130929400), a constructive partial-coloring method.
- [UC San Diego seminar summary of Spencer, Bansal and Lovett–Meka](https://www.math.ucsd.edu/seminar/constructive-discrepancy-minimization-walking-edges), attribution and comparison of existential and algorithmic results.
- [MIT OCW Mathematics for Computer Science](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/pages/readings/), concentration and conditional expectation background.
