# 029000 — Sigma-Algebras: What Does It Mean to Measure a Set?

**Track:** Analysis from First Principles. **Background:** countable unions and intersections, real-number intervals, sequences and limits. **Question:** Why must the sets we can measure form a carefully chosen collection rather than simply every conceivable subset?

<!-- BEGIN SPOKEN LECTURE -->

# Sigma-Algebras: What Does It Mean to Measure a Set?

Imagine that you are designing an instrument that measures length. A solid metal rod is easy: mark its endpoints and subtract. A collection of separate rods is almost as easy: if they do not overlap, add their lengths. Now start breaking the rods into more and more pieces. Suppose there are infinitely many disjoint pieces, and you want the total length to be the sum of the lengths of all the pieces. Suppose you also want a region left over after cutting pieces out to have a meaningful length. You have moved from measuring intervals to measuring *sets*.

At first, one might declare that every subset of the real line has a length. That ambition will eventually collide with a rigorous obstruction. It is possible to insist on a consistent, translation-invariant notion of length that adds over countably many disjoint sets, but not while assigning such a length to every imaginable subset. Before seeing that obstruction, we need to understand the structure that a workable notion of measurement demands.

The surprise is that the first mathematical object is not a formula for length. It is a collection of sets: a declaration of which questions about membership our instrument can answer.

## From a finite partition to a countable one

Start with a single unit interval, from zero to one. Split it into its left and right halves. If our only information is which half contains a point, then the events we can distinguish are: neither half, the left half, the right half, or the entire interval. We cannot distinguish a tiny interval deep inside the left half. Our information is too coarse.

Split both halves again. We obtain four quarters. A set that is the union of any selection of these quarters is now distinguishable. Every new refinement gives a richer collection of sets, but it still need not include all subsets of the interval.

There are three operations that information about sets should survive. First, the whole space is a possible event: wherever the point is, it lies in the space we are discussing. Second, if we can decide whether the point is in a particular set, we can also decide whether it lies outside that set. Third, if we have a countable list of decidable membership questions, we can ask whether *at least one* of them has a yes answer. We should remain within our collection of measurable questions.

These three requirements define a sigma-algebra. The word sigma signals the countable operation. A sigma-algebra on a set X is a collection of subsets containing X, closed under complements relative to X, and closed under countable unions.

The word countable matters. Closure under finite unions alone gives an algebra of sets, but may not be sufficient when we take limits of approximations. Closure under *arbitrary* unions would be stronger than needed and, in the concrete case of the Borel sets, would usually be false. Every subset of the real line is a union of singleton sets, possibly an uncountable union. Singletons are Borel. Yet not every subset of the real line is Borel. That distinction would vanish if we demanded arbitrary unions.

A few useful consequences follow immediately. The empty set belongs to every sigma-algebra because it is the complement of the whole space. Countable intersections belong too: to be in all sets is to be outside the union of all their complements. The difference of two measurable sets is measurable because it is the first set intersected with the complement of the second. We are not adding independent axioms for these operations; we derive them from the three defining properties.

## Why the countable condition matches the limits we actually take

Return to our refinements of the interval. Consider a decreasing sequence of sets. We keep all points in the first set, remove some to form the second, then remove more to form the third, and continue indefinitely. The points that survive every stage form the intersection of the sequence. A sigma-algebra ensures that this limiting survivor set is still measurable.

Or suppose sets grow through successive approximations. Each stage adds new points, and the eventual union consists of everything admitted at some finite stage. Again the limit is a countable union, so it stays measurable.

The connection to sequences is more than an analogy. Many notions from analysis can be written using countably many set operations. For example, the set of points where a sequence of real-valued functions converges can be expressed using unions and intersections of sets defined by inequalities. Provided those inequality sets are measurable, the convergence set is measurable. We will make that assertion precise when we study measurable functions.

One subtlety is easy to overlook: an uncountable family of questions cannot necessarily be combined into a single measurable question. But sequences are indexed by natural numbers. The mathematical operations that encode sequential limits fit the sigma-algebra axioms exactly.

## Three examples that behave differently

The smallest possible sigma-algebra on X consists only of the empty set and all of X. It can tell us whether the point is somewhere in the space, but nothing finer. The largest is the power set: every subset of X is admitted. Both meet the axioms. Choosing a sigma-algebra is therefore about the purpose and the available structure, not about identifying a unique collection that every set must belong to.

A third example is more instructive. On an uncountable set X, consider every subset that is countable, together with every subset whose complement is countable. This is the countable-cocountable sigma-algebra. The complement operation switches the two categories. A countable union of countable sets is countable. If at least one set in a union has countable complement, then the complement of the union is contained in that countable complement and is itself countable. The three axioms hold.

This example admits each individual point as a measurable singleton, and it admits any countable collection of points. Yet it may exclude a large set whose complement is also uncountable. Knowing how to measure every point separately does not imply knowing how to measure every union of points. We can form countable unions, not arbitrary ones.

On the real line, a sigma-algebra especially well matched to geometry is the Borel sigma-algebra. Start with every open interval, and take the smallest sigma-algebra containing all of them. The word *smallest* means the intersection of all sigma-algebras containing those intervals; that intersection is itself a sigma-algebra. The resulting Borel sets include all open sets, all closed sets, countable sets, and many much more complicated sets formed by countable set operations.

Why does an open interval generate all open sets? Every open set on the real line can be written as a countable union of intervals with rational endpoints. The rational endpoints provide a countable menu of building blocks. That countability connects topology to the sigma-algebra operations. It is not true that every arbitrary union of Borel sets is Borel.

## A sigma-algebra is not yet a measure

We have described which sets are eligible to have sizes, but we have not assigned the sizes. A *measure* takes each set in our sigma-algebra to a nonnegative extended real number, allowing infinity. It assigns zero to the empty set. And it is countably additive: when a sequence of measurable sets is pairwise disjoint, the measure of their union equals the sum of their measures.

Countable additivity is the operational demand that made the rod-breaking thought experiment interesting. It is stronger than the rule for just two disjoint pieces. It also produces estimates. If A is contained in B, then B can be decomposed into A and the part of B left over. The two parts are disjoint, so B has measure at least as large as A. This is monotonicity. If sets overlap, we can still bound the measure of their union by the sum of their measures. That is countable subadditivity, obtained by stripping overlaps away one set at a time.

Take the counting measure on a set X. It assigns to a finite set the number of points in it, and to an infinite set the value infinity. On the power set, this is a legitimate measure. A singleton has measure one; two distinct points have measure two; the nonnegative sum over countably many disjoint pieces works as expected. Nothing about a measure requires the measure of a singleton to be zero.

At the opposite extreme, choose a distinguished point x. Define the Dirac measure at x: a measurable set has measure one if it contains x, and zero if it does not. A countable collection of disjoint sets can contain x in at most one member, so countable additivity follows. The same underlying collection of sets may support radically different measures, each answering a different question.

If the measure of the entire space is one, we call it a probability measure. Probability theory is measure theory with total mass one, together with interpretations of the sets as events. In that language, the complement rule says the probability of the opposite event is one minus the probability of the event, and countable additivity handles infinitely many mutually exclusive events.

## How countable additivity controls a limiting process

Consider an increasing sequence of measurable sets, each contained in the next. We want to know the measure of their union. Countable additivity says that the measures of the approximations approach the measure of the union.

Here is the idea of the proof. The first approximation contributes its whole measure. The second contributes only the new points it adds. The third contributes only the new points that were absent from the second. Continue. These incremental pieces are disjoint, and together they make the final union. Adding their measures through the first N steps gives exactly the measure of the Nth approximation. Adding every increment gives the measure of the union. Therefore the sequence of approximate measures converges upward to the final measure. This is continuity from below.

There is a companion result for decreasing sets, but with an important condition. If the first set has finite measure, then the measures decrease to the measure of the intersection. We obtain it by applying continuity from below to the pieces removed from that first set. The finiteness condition permits subtraction from the first measure. Without it the conclusion can fail.

A concrete counterexample lives on the integers with counting measure. Let the Nth set be all integers at least N. Each set is infinite, so each has infinite counting measure. The sets decrease, and no integer belongs to all of them. Their intersection is empty and has measure zero. Thus the measure of the intersection is not the limit of the measures. The missing finite-measure assumption is doing real work.

These continuity properties tell us why countable additivity deserves its place as an axiom. It is the part of set measurement that cooperates with sequential limits.

## What comes next

We still have not constructed a notion of length for scattered subsets of the real line. We have only built the abstract framework in which such a notion could exist. In the next step, we will cover a set by countably many intervals, try to make those coverings as short as possible, and turn the resulting *outer measure* into an actual measure on a well-defined sigma-algebra. We will also discover why a good measurement theory refuses to measure some sets at all.

That refusal is not a defect in the construction. It is the price of keeping a powerful combination of geometrical meaning, countable additivity, and compatibility with limits. The sigma-algebra tells us which sets live inside that combination. The measure tells us their sizes. Keeping those two roles distinct is the first conceptual step toward Lebesgue integration, probability, and modern real analysis.

<!-- END SPOKEN LECTURE -->

## Mathematical companion — display only

### Sigma-algebras and measures

For a set \(X\), a family \(\Sigma\subseteq\mathcal P(X)\) is a sigma-algebra when
\[
X\in\Sigma,\qquad A\in\Sigma\Rightarrow X\setminus A\in\Sigma,\qquad (A_n)_{n\ge1}\subseteq\Sigma\Rightarrow\bigcup_{n=1}^\infty A_n\in\Sigma.
\]
A measure is \(\mu:\Sigma\to[0,\infty]\) with \(\mu(\varnothing)=0\) and, for pairwise disjoint \(A_n\in\Sigma\),
\[
\mu\left(\bigcup_{n=1}^\infty A_n\right)=\sum_{n=1}^\infty\mu(A_n).
\]
The *generated sigma-algebra* \(\sigma(\mathcal G)\) is the intersection of all sigma-algebras containing \(\mathcal G\). The Borel sigma-algebra on \(\mathbb R\) is \(\mathcal B(\mathbb R)=\sigma(\{(a,b):a<b\})\).

### Consequences with proof details

- **Subadditivity:** set \(B_1=A_1\) and \(B_n=A_n\setminus\bigcup_{k<n}A_k\); the \(B_n\) are disjoint, \(B_n\subseteq A_n\), and \(\cup_nB_n=\cup_nA_n\). Thus \(\mu(\cup A_n)\le\sum\mu(A_n)\).
- **Continuity from below:** if \(A_n\uparrow A\), the increments \(A_1, A_2\setminus A_1,\ldots\) are disjoint. Therefore \(\mu(A)=\lim_n\mu(A_n)\) even when the limit is infinite.
- **Continuity from above:** if \(A_n\downarrow A\) and \(\mu(A_1)<\infty\), then \(\mu(A_1\setminus A_n)\uparrow\mu(A_1\setminus A)\), giving \(\mu(A_n)\downarrow\mu(A)\). Counterexample: \(A_n=\{n,n+1,\ldots\}\subseteq\mathbb Z\) with counting measure has \(\mu(A_n)=\infty\) and \(\cap_nA_n=\varnothing\).
- **Borel generation:** each open \(U\subset\mathbb R\) equals \(\bigcup\{(p,q):p,q\in\mathbb Q,\ (p,q)\subset U\}\), a countable union.

### Exercises with answers

1. **Countable-cocountable measure.** Let \(X\) be uncountable, and \(\Sigma\) consist of countable and cocountable subsets. Set \(\mu(A)=0\) if \(A\) is countable, \(1\) if \(A\) is cocountable. Is this a probability measure? **Answer:** Yes. Two disjoint cocountable sets cannot exist. If a disjoint union is cocountable, precisely one of its members must be cocountable; otherwise a countable union of countable sets is countable.
2. **Generating closed sets.** Why does the sigma-algebra generated by open intervals contain every closed set? **Answer:** It contains all open sets by countable rational-interval unions, and is closed under complements.
3. **Infinite-measure pitfall.** Produce decreasing sets with empty intersection and infinite measure at every stage. **Answer:** The tails \(A_n=\{k\in\mathbb N:k\ge n\}\) with counting measure.
4. **Different meanings of size.** Under counting measure and Dirac measure at 0, compare \(\mu(\{0,2,4\})\). **Answer:** Counting measure gives 3; Dirac at 0 gives 1.

### Sources

- Sheldon Axler, *Measure, Integration & Real Analysis*, chapters 1–2 (open-access textbook). See `metadata/029000.json` and `metadata/sources.json`.
- MIT OpenCourseWare, *18.125 Measure and Integration*, lecture 1 (sigma-algebras, Borel sets, measurable functions).
