# 030250 — The p-adic Distance: When Divisibility Means Closeness

**Track:** Number Theory from First Principles. **Background:** divisibility, prime factorization, congruences, rational numbers, and the elementary valuation in 027875. **Aim:** construct the p-adic absolute value, prove the ultrametric inequality, and develop enough topology and series to make completion a natural question.

<!-- BEGIN SPOKEN LECTURE -->

# The p-adic Distance: When Divisibility Means Closeness

Consider two integers, one and a million and one. In ordinary arithmetic, their distance is a million. But if the million is divisible by a high power of five, those two integers look almost identical when viewed through successively finer congruences modulo five, twenty-five, one hundred and twenty-five, and so on. The usual real-number distance cares about the numerical size of the difference. A new distance could instead care about its *divisibility*.

To make that precise, fix a prime number p. For a nonzero integer, count the copies of p in its prime factorization. Call the count its p-adic valuation. For a nonzero fraction a divided by b, subtract the p-adic valuation of b from that of a. Thus the valuation of nine is two when p is three; the valuation of one ninth is negative two; and the valuation of ten is zero when p is three. Set the valuation of zero to infinity, meaning that zero is divisible by every power of p.

This is a measurement of arithmetic information. It is not a measure of numerical magnitude. A denominator can contribute a negative valuation, and that is why we need rational numbers, not only integers, from the start.

Define the p-adic absolute value of a nonzero rational x to be p raised to the *negative* of its valuation. Define the absolute value of zero to be zero. If x is divisible by many copies of p, its p-adic absolute value is small. If x contains p in its denominator, its p-adic absolute value is large. For p equal to three, nine has absolute value one ninth, while one ninth has absolute value nine. Ten has absolute value one.

Finally, define the distance between two rational numbers x and y as the p-adic absolute value of x minus y. The central idea is now exact: a small distance means a difference divisible by a large power of p.

## Why the triangle is stronger here

The ordinary triangle inequality says that the length of one side of a triangle is no greater than the sum of the other two. Our new distance obeys a stronger rule: the p-adic absolute value of a sum is at most the *larger* of the two absolute values of its summands.

Here is the proof. Suppose the valuation of x is r and that of y is s. Let m be the smaller of r and s. Both x and y have at least m powers of p, in the rational sense; after factoring out p to the m, the remaining terms have denominators not divisible by p. Adding them cannot introduce a p into the denominator. Therefore the valuation of x plus y is at least m. Because a larger valuation means a smaller p-adic absolute value, the strong inequality follows.

There is a useful refinement. If the two valuations are different, then the valuation of their sum is *exactly* the smaller one. To see why, factor out that lower power of p. One remaining term is a p-adic unit, meaning a rational with numerator and denominator both indivisible by p; the other is divisible by p. A unit plus a multiple of p is still a unit. Equal valuations are the only situation where cancellation can make the sum much smaller.

This is called the ultrametric inequality. It has consequences that are easy to prove and hard to picture using Euclidean geometry. If the three distances in a triangle are considered, the largest occurs at least twice. Suppose one side were strictly longer than both others. The ultrametric inequality would say that this supposedly longest side was no longer than the longer of the two shorter sides, a contradiction.

The language of balls is particularly useful. Fix a center a and an integer n. All rational numbers differing from a by a multiple of p to the n are inside the closed ball of radius p to the minus n. If b lies in that ball, the ball centered at b with the same radius is exactly the same set. Membership, not the choice of center, determines the ball. Any two balls of this kind are either disjoint or one sits inside the other.

A ball is also open as well as closed in the p-adic metric. For each point inside a ball there is a sufficiently small neighborhood remaining inside it. For each point outside the ball there is a small neighborhood remaining outside. The rational p-adic line is made of nested, separated neighborhoods, rather than connected intervals. The proof does not require a picture; it follows directly from the strong triangle inequality.

## A concrete calculation with three

Let p equal three, and compare four with thirty-one. Their difference is twenty-seven, equal to three cubed. Their p-adic distance is one twenty-seventh. Compare four with five. Their difference is one and the distance is one. The pair whose ordinary numerical difference is larger is the pair that is closer three-adically.

Now consider a succession of ordinary integers: one; one plus three; one plus three plus nine; and so on, each time adding the next power of three. Consecutive terms differ by a power of three with ever larger valuation. More importantly, two terms far enough along differ by a sum beginning with a very high power of three. Factoring out that power makes their distance small. This sequence is Cauchy for the three-adic distance.

Its familiar geometric-series identity is illuminating. The partial sum through three to the n minus one is the fraction three to the n minus one, divided by two. Equivalently, it is negative one half plus three to the n divided by two. Since three to the n has p-adic absolute value three to the negative n, the partial sums approach negative one half in this distance.

So the infinite series one plus three plus nine plus twenty-seven and so on converges to negative one half, *three-adically*. It does not converge in the real numbers. Both statements are correct, because convergence always refers to a choice of distance. We have not changed the ordinary finite sum or the laws of algebra. We have changed which sequences count as convergent.

Notice why this geometric example is not a trick. The ordinary identity relating a finite geometric sum to its final power holds in the rationals. Only the assertion that the final power tends to zero is new, and that assertion follows immediately from the p-adic metric.

## Limits and a rule for infinite series

An infinite series converges if its sequence of partial sums converges. In a complete ultrametric space, there is a particularly simple criterion: a series converges exactly when its individual terms tend to zero. Necessity is true for every metric field, because each term is the difference of two consecutive partial sums. For sufficiency, look at the difference between two partial sums. It is a finite sum of late terms. Its absolute value is no larger than the greatest absolute value among those terms. If every late term is small, then every tail is small, no matter how many terms it contains. That makes the partial sums Cauchy; completeness then gives a limit.

We must not skip a subtlety. At this point we have defined the metric on the rational numbers, and we have *not* proved that those rationals are complete. We can conclude that terms tending to zero produce Cauchy partial sums in the rationals; we can only guarantee a limit after passing to their completion. The familiar geometric series already converges to a rational, but arbitrary p-adic Cauchy sequences need not.

This distinction is the reason to construct a new field. A rational Cauchy sequence in the usual distance can converge to the square root of two, which does not lie in the rationals. The real numbers repair that missing-limit problem. For the p-adic distance we will make an analogous repair, but its elements and geometry will be different.

## Congruences as approximations

Return to an integer x. Knowing x modulo p specifies the first level of p-adic approximation. Knowing x modulo p squared refines it. Knowing x modulo p cubed refines it again, and the residue at every finer level must reduce to the residue at the previous level.

That is the reason high powers of p feel like increasing precision. Ordinary decimals refine an approximation by fixing more digits after the decimal point. A p-adic integer is approximated by fixing more *low-order* base-p digits. We read the powers of p in the opposite direction from the usual real-number intuition. In the three-adic series for negative one half, we kept adding terms with ever larger positive powers of three, and therefore ever smaller p-adic magnitude.

Some rational numbers cannot be reduced modulo p in the obvious way. One third, when p is three, has a denominator divisible by p and a negative valuation. It is not p-adically integral. That does not remove it from our metric field; it means that, to represent it, a p-adic expansion must allow finitely many negative powers of p. This is the same reason the final field will be larger than the ring of p-adic integers.

There are now three distinct operations worth keeping apart. Reducing modulo p to the n forgets information. Localizing at p permits denominators that are not divisible by p, but it does not add any limits. Completing the rationals for the p-adic distance fills in the limits of Cauchy sequences. These operations interact, but they are not synonyms.

The distance we have made from prime divisibility is a genuine metric. It respects addition and multiplication, and it turns modular accuracy into geometric closeness. In the next construction, every Cauchy sequence will acquire a limit, and the field of those limits will be called the p-adic numbers.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Fix a prime p. For x in Q nonzero write x=p^k a/b with p not dividing ab. Set v_p(x)=k, v_p(0)=+infinity, |x|_p=p^{-v_p(x)}, and |0|_p=0.

1. **Valuation rules:** v_p(xy)=v_p(x)+v_p(y); v_p(x+y)>=min(v_p(x),v_p(y)). If v_p(x) differs from v_p(y), equality holds. Proof of the sum inequality: factor out p^m, where m is the minimum, and observe both remaining summands lie in Z_(p), the rationals with denominators prime to p.
2. **Ultrametric:** |x+y|_p<=max(|x|_p,|y|_p), so d_p(x,z)<=max(d_p(x,y),d_p(y,z)). Equality occurs when summand norms differ.
3. **Congruence balls:** for integers a,b and n>=0, d_p(a,b)<=p^{-n} iff a≡b mod p^n. More generally this is true for a,b in Z_(p) with congruences defined there.
4. **Balls:** B(a,p^{-n}) for closed ball convention equals a+p^n Z_(p) inside Q. Every ball is clopen, because a point outside a closed ball has a small ball separated from it.
5. **Geometric series:** S_N=sum_{k=0}^{N-1}p^k=(p^N-1)/(p-1) -> 1/(1-p) in Q_p, once Q_p is constructed. The limit is already rational.
6. **Series caution:** For a general ultrametric field K, a_n ->0 makes partial sums Cauchy. Convergence is then guaranteed only if K is complete.

### Worked checks

- v_3(4-31)=v_3(-27)=3, hence d_3(4,31)=1/27; d_3(4,5)=1.
- In Q_3, 1+3+9+...=-1/2, because S_N+1/2=3^N/2.
- |1/p|_p=p, not 1/p: the reciprocal of p is **outside** the p-adic unit ball.

### Exercises

1. Show the largest of three pairwise distances in an ultrametric triangle must occur at least twice.
2. Prove every p-adic closed ball is both open and closed.
3. Find d_5(6,631) and compare it with the ordinary distance.
4. Check that a series with terms tending to zero produces Cauchy partial sums in an ultrametric field. Identify exactly where completeness enters.
5. Explain why adding arbitrarily many terms with p-adic absolute value at most p^{-N} still gives a sum with absolute value at most p^{-N}.

### Reading and source notes

- Andrew V. Sutherland, MIT 18.785, [Lecture 8: Complete Fields and Valuation Rings](https://math.mit.edu/classes/18.785/2021fa/LectureNotes8.pdf), §§8.1–8.3; source for standard completion and valuation framework.
- Keith Conrad, [p-adic number expositions and course handouts](https://kconrad.math.uconn.edu/math3094f16/), introductory arithmetic perspective.
- Wikipedia: [p-adic number](https://en.wikipedia.org/wiki/P-adic_number), [Ultrametric space](https://en.wikipedia.org/wiki/Ultrametric_space), [p-adic valuation](https://en.wikipedia.org/wiki/P-adic_valuation).
