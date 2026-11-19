# First epsilon and compactness arguments

<!-- BEGIN SPOKEN LECTURE -->

# First epsilon and compactness arguments

## Epsilon Proofs for Sequences: Making Eventually Precise

A sequence converges to a real number L when its terms eventually remain as close to L as we demand. The word 'eventually' is not a vague promise. It has a precise meaning: for every positive tolerance epsilon, there is an integer N such that every index n at least N has the term within epsilon of L. The threshold N may depend on epsilon. Once N is chosen, however, it must work for all later terms, not just one convenient term.

We will use the sequence one over n, for positive integers n. Its terms approach zero. To prove this, begin with an arbitrary positive epsilon. Choose a positive integer N larger than one divided by epsilon. Such an integer exists by the Archimedean property of the real numbers. For every n at least N, one over n is no greater than one over N, which is strictly less than epsilon. Since the absolute distance from one over n to zero is one over n, the convergence condition holds.

### Follow the quantifiers in order

The proof is a small game. Someone asks for accuracy epsilon. We respond with N. Then they may choose any n beyond that threshold. We must show the inequality for that n. If we instead checked only n equals N, the argument could fail for an oscillating sequence that later wanders away. If we chose one N without looking at epsilon, we might accidentally be demanding eventual exact equality with L.

Sometimes the threshold appears as a formula. For a sequence of the form three over n, choosing N larger than three divided by epsilon works. For one over n squared, any N larger than one over the square root of epsilon works. Exact ceiling details are not the point; the proof must establish an integer threshold that exists and makes every later term satisfy the requested bound.

### Sums of convergent sequences

Suppose a sequence a n converges to A and a sequence b n converges to B. To prove their sum converges to A plus B, take a desired tolerance epsilon. Convergence of a gives a threshold after which its error is less than epsilon over two. Convergence of b gives another threshold for the same half-error. Choose N to be the larger of the two thresholds. For every n at least N, both estimates hold. The triangle inequality bounds the error of the sum by the sum of the errors, which is less than epsilon.

The trick of splitting an error budget is a reusable proof method. We allocate room for two independent sources of error, choose one stage where both bounds apply, and combine them with a triangle inequality. In analysis this pattern recurs in continuity of compositions, approximation by dense subsets, and estimates for differential equations.

### Uniqueness of the limit

Could one sequence converge to two different real limits L and M? Suppose it did. If the limits were distinct, their distance d would be positive. Choose epsilon smaller than half of d, say one third of d. Eventually the sequence would be within epsilon of L and, after another threshold, within epsilon of M. Beyond the larger threshold, the triangle inequality would force the distance from L to M to be less than two epsilon, smaller than d. Contradiction. Therefore the limits coincide.

Notice how the proof uses both limits at a common late index. Two different thresholds need not be equal; taking their maximum is enough. This tiny step often separates a valid epsilon proof from a merely suggestive one.

### A sequence that does not converge

Let a n equal one when n is even and minus one when n is odd. Suppose it converged to L. Every sufficiently late even term would force L to be near one, while every sufficiently late odd term would force L to be near minus one. Choosing an error tolerance less than one makes those requirements incompatible. Alternatively, extract the even subsequence, which is constantly one, and the odd subsequence, constantly minus one. Any subsequence of a convergent sequence must converge to the same limit. The two different subsequence limits refute convergence.

This is an example of proving a negative statement about a quantified definition. To disprove convergence to a proposed L, we find one tolerance for which no matter how late a threshold is chosen, a later term lies too far away. To disprove convergence to any L, we need an argument valid for every possible candidate L; the two-subsequence method supplies one clean way.

The language of epsilon and N initially feels more complicated than saying 'the terms get close.' But it lets us combine limits, prove uniqueness, and identify exactly how approximations depend on requested accuracy. These are the tools on which rigorous calculus is built.

## Epsilon-Delta Proofs: Controlling a Function Near a Point

A function has a limit L as x approaches a when its outputs become arbitrarily close to L whenever its inputs are sufficiently close to a, excluding the point a itself. Continuity adds the requirement that the function's value at a exists and agrees with that limit. A removable hole can have a limit even when the function is undefined there.

The epsilon-delta language encodes the relation. Given any positive desired output error epsilon, we must supply a positive input radius delta. Every point x of the domain satisfying zero less than the distance from x to a and less than delta must have output within epsilon of L. The order is crucial. Delta is allowed to depend on epsilon and a, but not on the particular x selected after delta has been fixed.

### The easiest exact proof

Consider f of x equals three x plus one and a fixed real base point a. We claim the function is continuous at a. Given epsilon greater than zero, choose delta equal to epsilon divided by three. If the distance from x to a is less than delta, the distance from f of x to f of a is three times the distance from x to a, which is less than epsilon. This is a complete epsilon-delta proof. It does not merely evaluate the algebraic expression at a; it shows how to choose an input tolerance that guarantees an output tolerance.

A proof does not require the smallest possible delta. Any positive choice that works is enough. Sometimes a convenient conservative estimate is easier to derive than an optimal one.

### When an extra bound is needed

Now consider f of x equals x squared. At a fixed real number a, the difference between x squared and a squared factors as x minus a times x plus a. We can directly make the first factor small by choosing x near a. But the second factor also depends on x. Control it by first requiring x to be within one of a. Then the absolute value of x plus a is at most two times the absolute value of a plus one. For any requested epsilon, choose delta to be the smaller of one and epsilon divided by two absolute a plus one. When x is within delta of a, the product estimate is less than epsilon. We have proved continuity at every real a.

This is a typical two-stage estimate. First restrict to a convenient neighborhood so the uncontrolled-looking factor becomes bounded. Then choose a smaller neighborhood that delivers the requested accuracy. The same idea appears in products of convergent sequences, continuity of products, and error bounds for polynomials.

### Why order of quantifiers distinguishes uniform continuity

For ordinary continuity, delta may depend on the base point a. For uniform continuity on a domain, one delta must work simultaneously for every pair of points in that domain once epsilon is specified. The function x squared is continuous at every real number but not uniformly continuous on the entire real line. Take two large nearby points n and n plus one over n. Their input distance is one over n, tending to zero, while their squared outputs differ by two plus one over n squared. No single delta works for output accuracy one at every point of the real line.

On a bounded closed interval, x squared is uniformly continuous. The factor x plus a is then bounded uniformly across the interval. This is an early example of how compactness turns local control into global control.

### Reading a proof of discontinuity

To prove a function is discontinuous at a, we must exhibit a positive epsilon such that every positive delta admits a point x within delta of a whose output remains at least epsilon away from f of a. The point x may depend on delta. For the function that equals zero at zero and one everywhere else, choose epsilon equal to one half. No matter how small delta is, there is a nonzero x closer than delta to zero, but its output differs from f of zero by one. So the function is discontinuous at zero.

A plot may show the jump, but the epsilon-delta argument identifies exactly why no input tolerance can guarantee the required output tolerance. Conversely, a single path approaching a with a wrong output limit can refute a proposed multivariable limit, though confirming a limit requires control of all approaches.

### Use the definition as a design tool

When a proof asks for continuity, start by writing the desired inequality on outputs. Manipulate it until you find a sufficient condition on inputs. Take note of where the proposed delta depends on the point a. Check that delta is positive and that it works for every admissible x, not only for a convenient sequence. This is proof writing as quantitative design: decide how accurate the answer must be, then work backwards to the input control needed to guarantee it.

## Compactness and Subsequence Proofs: From Infinity to Finite Control

In analysis and topology, many important conclusions come from a principle of finite control. An infinite collection of possibilities may be too large to inspect one by one, but compactness often lets us pass to finitely many pieces or extract a convergent subsequence. These two descriptions are closely related in Euclidean space. Understanding their proofs shows how definitions and completeness work together.

### An open-cover version of compactness

A collection of open sets is an open cover of a set K if every point of K lies in at least one member of the collection. A set is compact if every such cover has a finite subcollection that still covers K. The statement does not say that the original cover is finite. It says no matter how many open sets are offered, enough of them can be chosen finitely to cover the whole set.

Why is the closed interval from zero to one compact? The standard proof uses the completeness of the real numbers. Given an arbitrary open cover, define S to be the collection of points t in the interval such that the subinterval from zero through t is already covered by finitely many members of the original cover. Since some open set contains zero, a short initial interval has a finite cover, so S is nonempty. Since S is bounded above by one, let s be its supremum.

Choose an open set from the cover containing s. Because it is open, it contains a small interval around s. From the definition of supremum, some point t in S lies inside that neighborhood just to the left of s, unless s is the left endpoint, which has already been handled. A finite cover of zero through t, supplemented by the one open set containing s, extends beyond s. This contradicts maximality unless s is one. The same neighborhood argument at one then ensures the entire interval has a finite subcover. The details matter: openness is what permits extension, and completeness is what supplies the supremum.

### A bounded sequence and nested intervals

A related theorem says every bounded sequence of real numbers has a convergent subsequence. Put the sequence in some closed bounded interval. Split the interval into two halves. At least one half contains infinitely many terms of the sequence; choose it. Split that half again and choose a half containing infinitely many terms. Continue, obtaining nested closed intervals with lengths tending to zero.

Choose indices in increasing order, one from each chosen interval, using the fact that the intervals contain infinitely many terms. Completeness gives a unique point in all the nested intervals, and the selected subsequence approaches that point because its terms lie in intervals of shrinking length. The conclusion is a convergent subsequence, not convergence of the entire original sequence. Alternating one and minus one provides the distinction.

### Compactness controls continuous functions

A continuous function maps compact sets to compact sets. Here is the open-cover proof. Suppose an open cover of the image is given. Take the inverse image of each covering open set. Continuity makes these inverse images open in the domain, and together they cover the compact source set. Choose finitely many. Their corresponding image-cover members then cover the entire image. The proof is a composition of two definitions: continuity preserves openness of inverse images, and compactness supplies finiteness.

A nonempty compact subset of the real line is closed and bounded, so a continuous real-valued function on a compact set attains a maximum and a minimum. This is the extreme value theorem. The word 'attains' is stronger than merely having a finite supremum. On the open interval from zero to one, f of x equal to x has supremum one but never reaches it. Compactness closes that gap.

### Sequential and open-cover language have limits

In metric spaces, compactness and the property that every sequence has a convergent subsequence are equivalent. In arbitrary topological spaces the two notions can differ; not every topological space is characterized by sequences alone. It is therefore unsafe to transplant a sequential proof to a general topology problem without checking the space's hypotheses. This is precisely the kind of hidden prerequisite that a foundational proof course should make visible.

We now have a bridge from elementary logical form to some of the strongest statements in introductory analysis. A proof of compactness begins with an arbitrary open cover and constructs a finite subcover. A proof using subsequences begins with an arbitrary sequence and constructs a convergent subsequence. A continuity argument takes an arbitrary target cover and pulls it back. These are different objects, but they share the same discipline: read the quantifiers, produce the objects the definition requires, and justify the step where infinite data becomes finite or convergent. That discipline is what makes advanced mathematics readable.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Epsilon Proofs for Sequences: Making Eventually Precise

**Track:** Mathematical Reasoning and Proof from First Principles. **Background:** Real numbers, inequalities, quantifiers. **Purpose:** teach an actual proof obligation and the reasoning required to discharge it.

---

#### Mathematical companion (not spoken)

##### Sequence limit definition and error budgets

\[
a_n\longrightarrow L\iff
\forall\varepsilon>0\,\exists N\,\forall n\geq N:\ |a_n-L|<\varepsilon.
\]
For \(a_n=1/n\), let \(N>1/\varepsilon\). Then \(n\ge N\Rightarrow 1/n\le1/N<\varepsilon\).

If \(a_n\to A\) and \(b_n\to B\), given \(\varepsilon>0\) select \(N_a,N_b\) for errors below \(\varepsilon/2\). For \(n\ge\max(N_a,N_b)\),
\[
|(a_n+b_n)-(A+B)|\le|a_n-A|+|b_n-B|<\varepsilon.
\]
To prove uniqueness, take distinct limits \(A,B\), let \(d=|A-B|>0\), and use \(\varepsilon=d/3\) for both. Eventually \(d\le|A-a_n|+|a_n-B|<2d/3\), a contradiction.

##### Exercises with answers

1. Show \(5/n\to0\). **Answer:** take \(N>5/\varepsilon\).
2. Prove \((-1)^n\) does not converge. **Answer:** even and odd subsequences have limits \(1\) and \(-1\), respectively.
3. Why choose \(\max(N_a,N_b)\)? **Answer:** it ensures both error estimates hold at the same index.

##### Sources and further reading

- [Richard Hammack, Book of Proof, third edition (current online edition)](https://richardhammack.github.io/BookOfProof/).
- [Eric Lehman, F. Thomson Leighton and Albert R. Meyer, Mathematics for Computer Science, MIT OCW 6.042J](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/).
- [OpenStax, Calculus Volume 1, Rice University](https://openstax.org/books/calculus-volume-1/pages/preface).
- [Wikipedia: Limit of a sequence](https://en.wikipedia.org/wiki/Limit_of_a_sequence).

### Epsilon-Delta Proofs: Controlling a Function Near a Point

**Track:** Mathematical Reasoning and Proof from First Principles. **Background:** Sequences and basic algebra. **Purpose:** teach an actual proof obligation and the reasoning required to discharge it.

---

#### Mathematical companion (not spoken)

##### Epsilon–delta continuity

A function \(f:D\to\mathbb R\) is continuous at \(a\in D\) when
\[
\forall\varepsilon>0\,\exists\delta>0\,\forall x\in D:\ |x-a|<\delta\Rightarrow |f(x)-f(a)|<\varepsilon.
\]
For a function limit at a possible hole, require \(0<|x-a|<\delta\) and replace \(f(a)\) by \(L\).

For \(f(x)=x^2\) and fixed \(a\), let
\[
\delta=\min\left\{1,\frac{\varepsilon}{2|a|+1}\right\}.
\]
Then \(|x-a|<\delta\) implies \(|x+a|<2|a|+1\), hence
\[
|x^2-a^2|=|x-a|\,|x+a|<\varepsilon.
\]

##### Exercises with answers

1. Prove \(f(x)=7x-2\) is continuous everywhere. **Answer:** use \(\delta=\varepsilon/7\).
2. Why is \(x^2\) not uniformly continuous on all \(\mathbb R\)? **Answer:** choose \(x=n,y=n+1/n\); their distance tends to zero but the output difference tends to two.
3. State the negation of continuity at \(a\). **Answer:** \(\exists\varepsilon>0\,\forall\delta>0\,\exists x\in D\) with \(|x-a|<\delta\) and \(|f(x)-f(a)|\ge\varepsilon\).

##### Sources and further reading

- [Richard Hammack, Book of Proof, third edition (current online edition)](https://richardhammack.github.io/BookOfProof/).
- [Eric Lehman, F. Thomson Leighton and Albert R. Meyer, Mathematics for Computer Science, MIT OCW 6.042J](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/).
- [OpenStax, Calculus Volume 1, Rice University](https://openstax.org/books/calculus-volume-1/pages/preface).
- [Wikipedia: Limit of a function](https://en.wikipedia.org/wiki/Limit_of_a_function).

### Compactness and Subsequence Proofs: From Infinity to Finite Control

**Track:** Mathematical Reasoning and Proof from First Principles. **Background:** Sequence limits, completeness, and elementary sets. **Purpose:** teach an actual proof obligation and the reasoning required to discharge it.

---

#### Mathematical companion (not spoken)

##### Compactness and subsequence principles

A set \(K\) is compact if every open cover \(\{U_i\}_{i\in I}\) of \(K\) contains finitely many members still covering \(K\). In \(\mathbb R^n\), Heine–Borel says compact \(\iff\) closed and bounded. In metric spaces, compact \(\iff\) every sequence has a convergent subsequence with limit in the space.

If \(f:K\to Y\) is continuous and \(\{V_i\}\) is an open cover of \(f(K)\), then the preimages \(\{f^{-1}(V_i)\}\) form an open cover of \(K\). Finite reduction on \(K\) supplies a finite subcover of \(f(K)\). Thus continuous images of compact spaces are compact.

##### Exercises with answers

1. Show \((0,1)\) is not compact. **Answer:** the open sets \(U_n=(1/n,1)\) for integers \(n\ge2\) cover \((0,1)\) but no finite subfamily covers it.
2. Find a convergent subsequence of \((-1)^n\). **Answer:** choose even indices to obtain the constant subsequence \(1\).
3. Why does a continuous real function on \([0,1]\) attain a maximum? **Answer:** its image is nonempty compact in \(\mathbb R\), hence closed and bounded and contains its supremum.

##### Sources and further reading

- [Richard Hammack, Book of Proof, third edition (current online edition)](https://richardhammack.github.io/BookOfProof/).
- [Eric Lehman, F. Thomson Leighton and Albert R. Meyer, Mathematics for Computer Science, MIT OCW 6.042J](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/).
- [OpenStax, Calculus Volume 1, Rice University](https://openstax.org/books/calculus-volume-1/pages/preface).
- [Wikipedia: Heine%E2%80%93Borel theorem](https://en.wikipedia.org/wiki/Heine%E2%80%93Borel_theorem).
