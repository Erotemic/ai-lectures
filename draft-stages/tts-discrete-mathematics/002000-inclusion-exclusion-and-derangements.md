# 002000 — Inclusion–Exclusion: Counting When Cases Overlap

**Track:** Discrete Mathematics and Combinatorics. **Background:** basic set operations, factorials, binomial coefficients. **Question:** how can we count objects that violate several conditions without counting some objects twice?

<!-- BEGIN SPOKEN LECTURE -->

# Inclusion–Exclusion: Counting When Cases Overlap

Imagine a conference registration list. Some attendees requested vegetarian meals. Some requested a seat near the front. We want to count people who made at least one of those requests. If we add the two request counts, someone who made both requests gets counted twice. Subtract the overlap, and the problem is solved.

With two conditions, this correction is familiar. With ten conditions, the overlaps form a complicated web: pairwise intersections, triple intersections, and so on. Inclusion–exclusion gives a systematic way to untangle that web. It also leads to a celebrated answer to a different question: if n letters are randomly placed into n addressed envelopes, how many arrangements have no letter in its own envelope?

## One overlap, then three

Let A be the set of people requesting vegetarian meals and B the set requesting front seating. Each person in only A or only B is counted once by the sum of the sizes of A and B. Each person in both is counted twice. Therefore the size of their union equals the size of A plus the size of B minus the size of their intersection.

With three conditions, begin by adding the sizes of A, B, and C. An object satisfying exactly two conditions is counted twice; subtract the three pairwise overlaps and it is counted once. But an object satisfying all three conditions was counted three times initially and subtracted three times, leaving zero. It needs to be added back once. The correct formula adds the three individual sizes, subtracts all three pairwise intersection sizes, and adds the size of the triple intersection.

The alternating pattern continues. For any finite family of conditions, sum the counts for single conditions, subtract the counts for pairs, add the counts for triples, and continue with alternating signs. If there are many conditions, writing every term may be impractical, but the principle is exact.

## Why alternation works

Consider a particular object that satisfies exactly r of the conditions, with r positive. In the alternating sum, it is counted r times at the first stage, subtracted once for each pair of satisfied conditions, added once for each triple, and so on. Its total coefficient is r choose one, minus r choose two, plus r choose three, continuing through r.

The binomial theorem says the alternating sum of all the binomial coefficients from zero through r is zero when r is positive. Because the zero-th coefficient is one, removing it and changing the sign shows that the alternating sum starting at one equals one. So our object is counted exactly once, regardless of how many conditions it satisfies.

An object satisfying none of the conditions appears in no intersection and is counted zero times. That is precisely what we want for a union. This argument is a proof of inclusion–exclusion for any finite number of sets. It is also a warning about infinite families: extending the same alternating expression to infinitely many sets requires separate convergence and measure-theoretic justification. Our theorem is a finite counting statement.

## The envelope problem

Suppose n different letters need to be placed into n distinct addressed envelopes, one letter per envelope. There are n factorial permutations of the letters. Let A sub i be the set of permutations that place letter i into its correct envelope. We want to count permutations outside every A sub i. Such permutations are called derangements.

For a fixed letter i, the number of permutations fixing i is n minus one factorial: arrange the other letters freely. For two specified letters, the count is n minus two factorial. For any chosen collection of k letters that must all remain in the correct envelopes, we can permute the remaining n minus k letters in n minus k factorial ways. There are n choose k ways to choose which k letters are prescribed to stay fixed.

Inclusion–exclusion first counts all permutations, subtracts those fixing at least one letter, adds back those fixing two specified letters, and so forth. The resulting count of derangements is n factorial times the alternating sum of one, minus one, plus one over two factorial, minus one over three factorial, continuing through the term at n.

For three letters this is six times the quantity one minus one plus one half minus one sixth, which is two. You can check the two surviving permutations directly: both are three-cycles. For four letters, the calculation gives nine derangements.

The formula is a pleasing example of why inclusion–exclusion is needed. We cannot count arrangements without fixed points by simply saying “each letter has n minus one choices.” Those choices are coupled: sending a letter into someone else's envelope removes a destination for all the others. The result must remain a permutation. Inclusion–exclusion respects that global constraint.

## A surprising limiting fraction

Divide the derangement count by n factorial. We obtain the probability that a uniformly random permutation has no fixed points. As n grows, the finite alternating sum approaches the infinite series for the exponential function evaluated at negative one. Its limit is one divided by the mathematical constant e, approximately zero point three six eight.

The probability of no fixed points does not approach zero, even though there are more and more letters. Each additional letter provides a new opportunity to be correct, but the dependencies among destinations are balanced so the chance of avoiding all correct placements approaches a positive constant.

We can also bound the approximation error. The alternating-series theorem gives an error smaller than the magnitude of the first omitted term. Therefore the probability differs from one over e by at most one over n plus one factorial. Multiplying back by n factorial shows that the derangement count differs from n factorial divided by e by less than one over n plus one. For n at least one, that is at most one half, with strict inequality when n is positive. Hence the number of derangements is the nearest integer to n factorial divided by e. We reached an exact integer-counting formula by combining finite combinatorics with a controlled infinite-series estimate.

## Counting surjections

The same method answers a different problem. How many functions from a set of n labeled inputs onto a set of m labeled outputs use every output at least once? Begin with all m to the n functions. For each target label, define the bad condition that this label is never used. To exclude one specified label, there are m minus one choices for every input; to exclude two, m minus two choices; and so on.

Inclusion–exclusion gives the alternating sum over k from zero to m of m choose k times m minus k to the n, with a sign that is negative for odd k and positive for even k. This counts onto functions, also called surjections.

For three inputs and two outputs, there are eight possible functions total. Two fail to be onto because all three inputs go to the first output or all three to the second. Thus there are six surjections. The formula gives eight minus two, agreeing with our direct count.

This result connects to set partitions. Every surjection onto m labeled boxes partitions the inputs into m nonempty fibers. If we erase the labels on the boxes, each partition has m factorial different labelings. So dividing the surjection count by m factorial gives the number of partitions of an n-element set into exactly m nonempty blocks, known as a Stirling number of the second kind. Here the division is justified because the output labels can be permuted freely and each resulting labeled arrangement is distinct.

## Where inclusion–exclusion ends and judgment begins

The formula is exact, but using it efficiently depends on the problem. With many unrelated conditions, there can be exponentially many intersections to evaluate. In some problems those intersections have a simple form, as they did for fixed points of a permutation. In others, a recurrence, a generating function, a dynamic program, or a probabilistic bound may be preferable.

Another important distinction: inclusion–exclusion counts a finite union exactly, while the union bound in probability merely says the probability of at least one event is no greater than the sum of the event probabilities. The union bound drops all the overlap corrections. It may be coarse, but it remains useful when we cannot compute the intersections. A less precise theorem can be more computationally accessible.

The central lesson is that overlapping cases are not an obstacle to counting, provided we name the overlaps. Inclusion–exclusion is a disciplined accounting identity. Every object that satisfies r conditions receives an alternating coefficient of exactly one, and every object that satisfies none receives zero. Once we understand that, the envelope problem and the surjection formula cease to be isolated puzzles. They are applications of one mechanism.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For finite subsets \(A_1,\ldots,A_m\) of a finite universe,
\[
\left|\bigcup_{i=1}^m A_i\right|
=\sum_{\varnothing\ne S\subseteq\{1,\ldots,m\}}
(-1)^{|S|+1}\left|\bigcap_{i\in S} A_i\right|.
\]
An object in exactly \(r\ge1\) sets receives coefficient
\(\sum_{j=1}^r(-1)^{j+1}\binom rj=1\).

Derangements of \(n\) labeled objects:
\[
D_n=n!\sum_{k=0}^n\frac{(-1)^k}{k!},
\qquad D_3=2,\ D_4=9,\quad
\left|D_n-\frac{n!}{e}\right|<\frac1{n+1}.
\]
Surjections from an \(n\)-set to an \(m\)-set:
\[
\#\mathrm{Surj}(n,m)=\sum_{k=0}^m(-1)^k\binom mk(m-k)^n=m!S(n,m).
\]
The \(0^0\) convention may matter for empty-domain edge cases; lectures above assume \(n,m\ge1\) where appropriate.

### Exercises with answers

1. How many derangements of two letters exist? **Answer:** One: they swap positions.
2. How many onto functions go from a four-element domain to two labeled values? **Answer:** \(2^4-2=14\).
3. Why can't we multiply \((n-1)^n\) to count derangements? **Answer:** The individual destination choices are not independent under the permutation constraint.
4. What would double counting do to an item in three overlapping sets if we only subtracted pairwise intersections? **Answer:** It would be counted zero times; add the triple intersection back once.

### Reading

MIT 6.042J, *Mathematics for Computer Science*, chapter on inclusion–exclusion and counting techniques; standard results on permutations and surjections.
