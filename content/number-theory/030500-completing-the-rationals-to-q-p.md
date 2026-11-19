# 030500 — Completing the Rationals: Constructing the Field Q_p

**Track:** Number Theory from First Principles. **Background:** 030250 (ultrametric, Cauchy sequences), rational arithmetic. **Aim:** construct Q_p as a completion rather than using an unexplained symbol, prove it is a field, and derive canonical p-adic digit expansions.

<!-- BEGIN SPOKEN LECTURE -->

# Completing the Rationals: Constructing the Field Q-p

There is a philosophical choice hidden in an innocent-looking equation: a sequence has a limit. A limit is not always present in the number system where the sequence began. Decimal approximations to the square root of two are rational numbers, but their limit is not rational. The real numbers are the system obtained by filling in the missing limits for the ordinary absolute value.

We have given the rational numbers a different distance, one determined by divisibility by a fixed prime p. Now we are going to fill in the missing limits for *that* distance. The resulting field is written Q with a subscript p, read as the p-adic numbers. We will construct it carefully enough to see why addition, multiplication, and division still work.

First recall the definition. A sequence of rationals is Cauchy p-adically if, for each positive precision threshold, all sufficiently late pairs of terms are that close. A convenient choice of thresholds is the sequence one, one over p, one over p squared, and so on. Requiring later differences to be divisible by arbitrarily high powers of p is exactly the same condition.

Two Cauchy sequences should represent the same new number when the distance between their corresponding terms tends to zero. For example, the constant sequence minus one half and the geometric partial sums one, one plus p, one plus p plus p squared, and so on represent the same number, because their difference tends to zero p-adically. This equivalence relation is crucial: we are not declaring every distinct sequence to be a distinct number.

## Numbers made of Cauchy sequences

Define a p-adic number to be an equivalence class of rational Cauchy sequences. Embed each rational r as the class of the constant sequence r, r, r, and so on. Two different rationals remain different because a fixed nonzero difference has a fixed positive p-adic absolute value; it cannot tend to zero. Thus the original rationals sit faithfully inside the new structure.

To add two classes, add representative sequences term by term. To multiply them, multiply representative sequences term by term. Why is this well-defined? The sum of two Cauchy sequences is Cauchy by the ultrametric inequality. For products, first observe that a Cauchy sequence is bounded in p-adic absolute value. Once all its tail terms are within distance one of some fixed term, their absolute values are bounded by the greater of one and that term's absolute value. A finite initial segment is also bounded. Then the difference of two products splits into two terms, each a small difference multiplied by a bounded factor. It tends to zero.

The same estimate shows that replacing either sequence by an equivalent one does not change the sum or product class. Zero is the class of sequences tending to zero. One is the class of the constant sequence one. These are the familiar ring operations, extended to new limits.

But a *field* must permit division by every nonzero element. That needs a separate argument. Let x be represented by a Cauchy sequence of rationals x one, x two, and so forth, and suppose this class is not zero. Then the terms cannot approach zero. There must be a positive lower bound, valid eventually, for their p-adic absolute values.

Why? Choose a sufficiently late term whose absolute value is positive and larger than the Cauchy error for all later terms. The strong triangle inequality, together with its unequal-valuation refinement, says that every sufficiently late term then has exactly the same absolute value as that chosen term. In other words, a nonzero Cauchy sequence eventually stabilizes at a *valuation*, even though its numerical terms continue changing.

All these late terms are nonzero. Take their ordinary rational reciprocals. The distance between the reciprocals of x at stages n and m is the distance between those x terms divided by the product of their p-adic absolute values. The denominator has eventually constant nonzero size; the numerator tends to zero. Therefore the reciprocals form another Cauchy sequence. Its class multiplies with the original class to give one. This proves that the completion is a field, not merely a ring.

## Do Cauchy sequences of the new numbers converge?

We have constructed new numbers as equivalence classes, but a construction deserves its name only if it really solves the completeness problem. Suppose X one, X two, X three, and so forth are p-adic numbers forming a Cauchy sequence. Each X lies in a class represented by rational numbers. Choose a rational q at stage n that approximates X at least as accurately as one over p to the n. We can always do so: any member of the completion is represented by rationals getting arbitrarily close to it.

The rational sequence q one, q two, and so on is Cauchy. Its difference at two late stages is bounded by three terms: the error in approximating the first p-adic number, the small difference between the two p-adic numbers, and the error in approximating the second. The ultrametric bound makes the combined error small.

Let X be the class defined by those rational q's. Then the original Cauchy sequence of p-adic numbers converges to X, since the approximation errors tend to zero. So the new field is complete. Furthermore, it has the *same* p-adic distances between original rationals, and the original rationals are dense in it: every new number can be approximated arbitrarily closely by rationals.

Completeness is a genuine theorem about the construction, not an extra axiom we have simply announced. Up to a unique isomorphism that fixes the rational numbers and respects their distances, the completion is determined by these properties.

## The valuation survives the limit

We can extend the p-adic absolute value from the rationals to a completed number X by taking the ordinary real limit of the absolute values of a rational sequence representing X. For a nonzero X there is a simpler description: after enough terms, every representative has the same valuation, so the absolute values eventually agree exactly. For zero, they tend to zero.

The completed field still satisfies both the multiplicative law and the strong triangle inequality. Its possible nonzero absolute values are the powers of p with arbitrary integer exponents. So every nonzero p-adic number has a valuation that is an integer; the valuation of zero remains infinity. The field is complete, but its valuation remains discrete.

Call a p-adic number *integral* when its p-adic absolute value is at most one. These numbers form a subring, denoted Z with a subscript p. The ones with absolute value exactly one are its units; the others are divisible by p. We will study this ring from the perspective of coherent residues in the next lecture.

## Digits run toward greater powers of p

An ordinary real decimal expansion uses more negative powers of ten to increase precision. Here we use more *positive* powers of p. Start with a p-adic integer x. Reduce x modulo p and choose a digit a zero between zero and p minus one. The difference x minus a zero is divisible by p. Divide that difference by p, reduce again, and choose digit a one. Continue. The successive digits yield an expansion of x as a zero, plus a one times p, plus a two times p squared, and so on.

At each stage the difference between x and the partial digit sum is divisible by the next power of p. That difference tends to zero in the p-adic distance. Every x therefore equals the limit of its digit partial sums. The digits are unique because if two expansions first differ at power p to the k, their difference has valuation exactly k and cannot be zero.

For a general nonzero element of Q-p, its valuation may be negative. Factor out the corresponding power of p and apply the construction to the remaining p-adic unit. Its expansion begins at some integer exponent, perhaps negative two or negative ten, but it has only finitely many negative powers. No infinitely long negative tail is needed.

Consider negative one in the two-adic numbers. Its digits are all ones: one plus two plus four plus eight and onward. The finite partial sum through two to the n minus one is two to the n minus one, which approaches negative one two-adically. The usual sum of positive powers of two diverges in the real numbers; the two-adic equality is a limit statement for a different metric.

For a less symmetric example, consider one third in the five-adic numbers. Three is a unit modulo five, so one third is a five-adic integer. Modulo five, the inverse of three is two. Modulo twenty-five, it is seventeen. Modulo one hundred and twenty-five, it is forty-two. Modulo six hundred and twenty-five, it is four hundred seventeen. The corresponding low-order base-five digits begin two, three, one, three, one, three, and continue with that repeating pair. Each new digit is chosen to satisfy one more power of five, and all earlier digits remain fixed.

This is more than a new notation. It says that infinite compatible modular information can form an actual field element, with well-defined arithmetic and limits.

## How large is the new field?

No finite list of rational fractions can account for all p-adic numbers. In fact the completion is uncountable. To see it without measure theory, choose each base-p digit independently from zero and one. Every infinite sequence of these digits defines a p-adic integer because its partial sums are Cauchy. Two such sequences define different numbers if their first differing digits occur at some finite position. There are uncountably many infinite binary sequences by the diagonal argument, so there are uncountably many p-adic integers.

Yet the ordinary rationals are countable. Therefore the completion genuinely added many numbers; it is not a disguised renaming of a rational field. And because all digit partial sums are ordinary integers, the rationals are still dense in the p-adic numbers.

The p-adic field is built by a familiar completion process, but it encodes a different notion of precision. When an equation has compatible solutions modulo higher and higher powers of p, the completion gives us a place to take their limit. Our next task is to show that the compatible residues themselves form a concrete ring, and that this ring is exactly the p-adic integers.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Let C be the set of p-adically Cauchy sequences in Q, and identify (x_n)~(y_n) iff |x_n-y_n|_p ->0. Set Q_p=C/~.

### Proof details

1. **Cauchy boundedness:** for large n, |x_n-x_N|_p<=1, hence |x_n|_p<=max(1,|x_N|_p); the finite prefix is bounded too.
2. **Nonzero valuation stabilization:** if (x_n) is not equivalent to 0, there are epsilon>0 and arbitrarily late n with |x_n|>=epsilon. Choose a Cauchy tail with pairwise distances <epsilon, then select one such term x_N on that tail. For all m late, |x_m-x_N|<|x_N|, so |x_m|=|x_N|.
3. **Inverses:** for late n,m, |1/x_n-1/x_m|_p=|x_m-x_n|_p/(|x_n|_p|x_m|_p) ->0. This supplies inverses for nonzero classes.
4. **Completeness:** given Cauchy (X_n) in Q_p, choose q_n∈Q with |X_n-q_n|_p<=p^{-n}. Then (q_n) is Cauchy in Q; the class X=[(q_n)] is its limit and X_n->X.
5. **Digits:** for x∈Z_p there are unique a_j∈{0,...,p-1} with x=∑_{j>=0} a_j p^j. For x∈Q_p^× with v_p(x)=k, write x=∑_{j>=k} a_j p^j, a_k != 0. Uniqueness by taking the first differing digit.
6. **Density and cardinality:** integer digit truncations approach each x∈Z_p; their rational p-power shifts approach any x∈Q_p. Binary digit sequences inject into Z_p and are uncountable.

### Worked checks

- In Q_2, ∑_{j=0}^∞2^j = 1/(1-2)=-1.
- The inverse of 3 mod 5^n is 2,17,42,417,1042 for n=1,...,5; first five base-five digits are (2,3,1,3,1).
- The infinite base-five expansion for 1/3 is 2+3·5+∑_{m>=1}(5^{2m}+3·5^{2m+1}) = 17+16·25/(1-25) = 1/3.

### Exercises

1. Fill in the missing estimate establishing well-defined multiplication on equivalence classes.
2. Prove a nonzero p-adic number has a valuation in Z even though Q_p is uncountable.
3. Find the first five base-three digits of minus one, and prove the pattern.
4. Explain why every class in Q_p contains rational approximations arbitrarily close to it.
5. Prove directly that the valuation ring Z_p is closed under addition and multiplication.

### Reading and source notes

- Andrew V. Sutherland, MIT 18.785, [Lecture 8: Complete Fields and Valuation Rings](https://math.mit.edu/classes/18.785/2021fa/LectureNotes8.pdf), metric completion and the valuation ring.
- Keith Conrad, [The p-adic expansion of rational numbers](https://kconrad.math.uconn.edu/blurbs/gradnumthy/rationalsinQp.pdf), examples of expansions and digit conventions.
- Wikipedia: [p-adic number](https://en.wikipedia.org/wiki/P-adic_number), [Completion (metric space)](https://en.wikipedia.org/wiki/Complete_metric_space), [Cauchy sequence](https://en.wikipedia.org/wiki/Cauchy_sequence).
