# 030000 — Building Lebesgue Measure: Coverings, Null Sets, and a Necessary Boundary

**Track:** Analysis from First Principles. **Background:** countable additivity, sigma-algebras, intervals, infima and countable limits. **Question:** How can the ordinary length of an interval be extended to a much larger family of sets, and why not to every set?

<!-- BEGIN SPOKEN LECTURE -->

# Building Lebesgue Measure: Coverings, Null Sets, and a Necessary Boundary

Imagine measuring the amount of paint on a wall. If the paint covers one rectangular patch, the area is easy. If it covers an intricate collection of dots and thin streaks, measuring each connected piece may not be realistic. You might instead put a collection of simple shapes *over* the painted region, add the areas of those shapes, and try to make the total covering area as small as possible.

There is a useful asymmetry here. Covering a messy region with simple shapes is easy. Finding an exact disjoint partition of that region into simple shapes is not. We will use coverings to construct an upper estimate for size, and then take the best possible such estimate. In one dimension the simple shapes will be intervals, and the resulting construction is called Lebesgue outer measure.

The remarkable part is not just that outer measure assigns a number to every subset of the line. The remarkable part is discovering which subsets can be treated consistently as measurable, and why the apparently natural demand to measure *all* subsets must be rejected.

## A length estimate made from coverings

Start with a set E on the real line. Cover every point of E by countably many open intervals. Add the lengths of those intervals. Any particular choice of intervals gives one candidate estimate for the size of E. It might be wasteful: the intervals could overlap or extend far beyond E. So take the infimum over all such countable coverings.

This number is the outer measure of E. It may be infinite. We use the convention that an empty set needs no intervals and has outer measure zero.

For a concrete example, consider a single point at one third. For any positive tolerance, cover it by an interval of length smaller than that tolerance. Because we can make the interval arbitrarily short, the outer measure of one point is zero.

Now consider the rational numbers between zero and one. There are infinitely many, and they are dense: every nonempty interval contains a rational. Would that force their total length to be one? No. List the rationals as the first, second, third, and so on. Give the first rational a tiny covering interval, the second one half as much length, the third half as much again, and continue. Choose the initial scale so the sum of all those lengths is less than any tolerance you please. Every rational is covered, yet the total covering length is arbitrarily small. Therefore this dense countable set has outer measure zero.

Density and length are answering different questions. Density says there is a rational point in every open interval. Measure asks how much total length is needed to cover all the points with countably many intervals. A set can be everywhere dense and still have measure zero.

For an actual interval from a to b, the outer measure is its familiar length, b minus a. Covering from above proves that the outer measure is at most this number. The reverse inequality requires an argument: any countable open cover of a closed subinterval has a finite subcover, and the sum of the lengths of finitely many covering intervals cannot be shorter than the interval being covered. Move the endpoints of the closed subinterval toward the desired endpoints, and we obtain the lower bound. This compactness argument is where familiar real-analysis foundations enter the construction.

## What outer measure can promise for every set

Outer measure is defined for every subset, without first asking whether the set is measurable. It has three immediate properties. The empty set has outer measure zero. A subset cannot have larger outer measure than the set containing it, because any cover of the larger set also covers the smaller one. And the outer measure of a countable union is no greater than the sum of the individual outer measures.

The last statement is countable *subadditivity*, not necessarily additivity. To understand the proof, choose for each set a covering whose total length is very close to that set's outer measure. Combine all those covers into one countable family of intervals. The sum of their lengths is very close to the sum of the outer measures. Because the combined intervals cover the union, its outer measure is no greater. Finally let the small covering errors approach zero. If any individual outer measure is infinite, the inequality is immediate.

Why not assert equality whenever the sets are disjoint? Because the infimum over coverings is not automatically an additive measurement. We have not imposed enough conditions to ensure that cutting a set along a boundary preserves its outer measure exactly.

That observation leads to the definition of a Lebesgue measurable set. A set A is measurable when it cuts every possible test set E without losing or creating outer measure: the outer measure of E must equal the outer measure of the portion inside A plus the outer measure of the portion outside A.

This is called Carathéodory's criterion. One direction of the equality follows from subadditivity for every A and every E, since E is the union of its two pieces. The significant requirement is the reverse direction: no covering can exploit the cut to make a combined measurement smaller than the separate measurements.

An interval satisfies this criterion. Intuitively, when a covering interval crosses a fixed endpoint, split that covering interval at the endpoint. The total length does not change, and the two pieces cover the appropriate portions. A careful proof handles endpoints and open covers with arbitrarily small extra length. Once intervals are measurable, the sigma-algebra operations produce all Borel sets as measurable too.

The general Carathéodory theorem establishes that the sets satisfying this criterion form a sigma-algebra, and that outer measure restricted to this sigma-algebra is countably additive. The proof is a useful model for turning an approximate quantity into an exact mathematical object. You begin with a subadditive upper bound on every set, isolate the cuts across which it behaves additively, and prove that all such cuts are compatible with one another and with countable limits.

## A measure more forgiving than the Borel sets

We have now constructed Lebesgue measure on the line: outer measure restricted to the Lebesgue measurable sets. It agrees with ordinary interval length, is translation invariant, and is countably additive over disjoint measurable sets.

The Lebesgue sigma-algebra is larger than the Borel sigma-algebra. The extra freedom is associated with null sets, sets having measure zero. Every subset of a Lebesgue null set is itself Lebesgue measurable, even if the subset is not Borel.

Why should a subset of a null set be measurable? Let N have outer measure zero and let A be any subset of N. By monotonicity, A also has outer measure zero. For any test set E, the inside portion E intersect A has outer measure zero. The outside portion is at most the outer measure of E. Subadditivity says the two portions together have outer measure at least that of E. Both inequalities force equality. Thus A passes the Carathéodory test.

This property is called *completeness* of the measure: every subset of every measurable null set belongs to the sigma-algebra. A Borel measure considered only on Borel sets is not complete in this sense, even though every singleton is Borel and has measure zero. Its completion is the Lebesgue measure space.

This is a different use of the word completeness from Cauchy completeness in metric spaces. Metric completeness ensures that Cauchy sequences converge. Measure completeness ensures that changing a measurable object on a sufficiently small null set does not create a nonmeasurable exception. The shared word should not obscure the different definitions.

Consider the standard middle-thirds Cantor set. At the first stage we remove the open middle third of the unit interval. At the second stage we remove the middle thirds of the two remaining intervals, and continue. After N stages, the remaining pieces have total length two thirds raised to the Nth power. The final Cantor set is contained in every one of these stages, so its outer measure is at most all those shrinking lengths. The limit is zero. Yet the Cantor set is uncountable. Measure zero is not the same as countability.

A subset of this Cantor set is Lebesgue measurable, whether or not it is Borel. There are in fact subsets that are not Borel: the collection of Borel subsets of the real line has the cardinality of the continuum, while the power set of the uncountable Cantor set has strictly larger cardinality. We do not need to construct one explicitly to understand the conclusion. The measurable sets have outgrown the original Borel construction.

## Why no satisfactory measure covers every subset

It is tempting to ask why we do not simply include every subset of the real line in our sigma-algebra. Perhaps outer measure already gives every set a number, so why insist on Carathéodory's criterion at all?

The reason is a contradiction involving translation, countable additivity, and the axiom of choice. On the interval from zero to one, declare two real numbers equivalent when their difference is rational. Choose exactly one representative from each equivalence class that intersects the interval. Call the resulting set V.

Now translate V by rational numbers between minus one and one. The translated sets are pairwise disjoint: if one point belonged to two such translates, the corresponding representatives of V would differ by a rational number, contradicting our selection of one representative per equivalence class. Their union contains the entire interval from zero to one and is contained in a bounded interval, from minus one to two.

Suppose every subset were measurable, that the length of the unit interval were one, and that translating a set never changed its measure. Every rational translate of V would have the same measure, say c. If c were zero, the countable union of translates would also have measure zero, yet it contains the unit interval and must have measure at least one. If c were positive, the countably many disjoint translates would have infinite total measure, yet they lie in a bounded interval of finite measure. Either choice is impossible.

The conclusion is not that outer measure is inconsistent. Outer measure is well defined on every subset. The conclusion is that we cannot have the stronger countably additive, translation-invariant extension of ordinary length *on every subset*, assuming the relevant form of choice. Some sets must fail the measurability criterion. V is a Vitali set, the standard example of this obstruction.

Note what the contradiction does and does not say. It does not give a practical procedure for finding a nonmeasurable piece of dust. The selection uses a strong existence principle. And it does not make typical geometric regions mysterious. Every open interval, closed set, Borel set, and subset of a null set is measurable. The issue concerns the outer edge of what can be consistently required of all subsets.

## Why this is enough for integration

We have achieved the basic properties of length without insisting that all sets are measurable. Every interval has its expected length. Rational points, despite being dense, take up no length. The Cantor set is uncountable but has measure zero. Subsets of null sets stay measurable. Increasing measurable sets have measures that converge to the measure of their union, and decreasing sets enjoy the analogous statement when the first measure is finite.

What does any of this have to do with integrating a function? Imagine measuring the area under a graph by asking how much of the input domain lies where the function exceeds a given height. That question involves a set of inputs. Before we can assign meaningful sizes to such sets, we must know that they are measurable. The Lebesgue construction provides the domain-side notion of size; the next step is to identify which functions expose measurable sets when we ask about their values.

Once we have measurable functions, we can build an integral by adding height times measure, starting with very simple functions and then passing to limits. The surprising strength of Lebesgue integration is that it follows the measure of sets through limits, rather than requiring a single interval partition to approximate every oscillation at once.

For now the key contrast is between *outer measure*, defined for every subset but only guaranteed to be subadditive, and *Lebesgue measure*, defined on the Carathéodory sigma-algebra and genuinely countably additive. The latter is not smaller because the construction failed. It is smaller because countable additivity has content. That content is what makes the integral to come useful.

<!-- END SPOKEN LECTURE -->

## Mathematical companion — display only

### Outer measure and Carathéodory measurability

For \(E\subseteq\mathbb R\) define
\[
m^*(E)=\inf\left\{\sum_{n=1}^{\infty}(b_n-a_n):E\subseteq\bigcup_{n=1}^{\infty}(a_n,b_n)\right\}.
\]
The empty cover has sum zero. The family of Lebesgue measurable sets is
\[
\mathcal L=\bigl\{A\subseteq\mathbb R:\ \forall E\subseteq\mathbb R,\quad m^*(E)=m^*(E\cap A)+m^*(E\setminus A)\bigr\}.
\]
Carathéodory's theorem: \(\mathcal L\) is a sigma-algebra; \(m=m^*|_{\mathcal L}\) is a complete countably additive measure. \(\mathcal B(\mathbb R)\subsetneq\mathcal L\). The proper inclusion uses the existence of non-Borel subsets of a null Cantor set.

### Countable coverings of countable sets

If \(E=\{x_1,x_2,\ldots\}\) and \(\varepsilon>0\), cover \(x_n\) by an interval of length \(\varepsilon 2^{-n}\). Then \(m^*(E)\le\varepsilon\), hence \(m(E)=0\).

For the middle-thirds Cantor set \(C\), the \(n\)th stage consists of \(2^n\) closed intervals each of length \(3^{-n}\), so \(m(C)\le(2/3)^n\) for all \(n\). Thus \(m(C)=0\).

### Vitali obstruction, with exact scope

Let \(V\subseteq[0,1]\) contain one representative from each equivalence class of \(x\sim y\iff x-y\in\mathbb Q\). The family \(\{V+q:q\in\mathbb Q\cap[-1,1]\}\) is pairwise disjoint. Its union covers \([0,1]\), because each \(x\in[0,1]\) differs from its chosen \(v\in V\) by \(q=x-v\in\mathbb Q\cap[-1,1]\). Its union lies in \([-1,2]\). If every such translate were measurable and translation invariance and countable additivity held, a common measure \(c=0\) would contradict \(m([0,1])=1\), while \(c>0\) would contradict \(m([-1,2])=3\). The selection of representatives uses choice.

### Exercises and answers

1. **Dense but null.** Construct a dense subset of \([0,1]\) of measure zero. **Answer:** \(\mathbb Q\cap[0,1]\), covered by geometrically shrinking intervals.
2. **Singleton subsets.** Explain why every subset of a null measurable set is Lebesgue measurable. **Answer:** Outer-measure monotonicity makes it null, and subadditivity plus \(m^*(E\cap A)=0\) proves Carathéodory's equality for every \(E\).
3. **Cantor set.** Why does the Cantor set having measure zero not imply it is countable? **Answer:** The left/right choices at each retained third encode all infinite binary sequences, producing uncountably many points, while stage-cover lengths tend to zero.
4. **Outer measure versus measure.** Must \(m^*(A\cup B)=m^*(A)+m^*(B)\) for disjoint arbitrary subsets? **Answer:** No. Countable subadditivity is universal; additivity is guaranteed when the cutting sets are Lebesgue measurable.

### Sources

- Sheldon Axler, *Measure, Integration & Real Analysis*, chapters on outer measure, Lebesgue measure, and Borel sets.
- MIT OpenCourseWare, *18.125 Measure and Integration*, lectures 6–9 (outer measure, Carathéodory's criterion, invariance and Vitali sets).
