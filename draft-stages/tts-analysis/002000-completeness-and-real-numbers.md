# 002000 — The Number Line Without Gaps: Completeness and the Real Numbers

**Track:** Analysis from First Principles. **Background:** fractions, squares, inequalities, and the definition of a convergent sequence. **Theme:** why a sequence can get arbitrarily close to a destination that does not exist in its number system.

<!-- BEGIN SPOKEN LECTURE -->

# The Number Line Without Gaps: Completeness and the Real Numbers

A surveyor measures the side of a square as exactly one unit. How long is its diagonal? Pythagoras's theorem answers quickly: the square of the diagonal's length is two. But there is a problem. If our only permitted lengths are fractions—whole numbers divided by nonzero whole numbers—there is no length whose square is exactly two. A ruler can display increasingly convincing decimal approximations, yet no fraction will finish the job.

At first this sounds like a problem with our measuring equipment. A finer ruler seems to solve it. But better equipment cannot manufacture a missing rational number. We have found an exact geometric relationship that the rational number system cannot express as the square of one of its members. That gap is the starting point for completeness. It will tell us why some limits exist, why calculus works, and how to distinguish a proof of convergence from an impressively long computation.

## The failure occurs inside a remarkably crowded number line

Fractions are plentiful. Between any two distinct rational numbers lies another rational: their average. Between the first and the average lies another. We can keep inserting fractions indefinitely. The rational numbers are dense, meaning that every open interval contains a rational number.

Density might sound like the absence of gaps. But it gives the wrong guarantee. It says we can find fractions arbitrarily close to a target location if that location is specified by a larger number system or by geometry. It does not say the target itself is rational.

Let's prove that the square root of two is not rational. Suppose, for contradiction, it equals p divided by q, where p and q have no common factor and q is nonzero. Squaring gives p squared equal to twice q squared. So p squared is even, which forces p to be even. Write p as twice r. Substitution now gives four r squared equal to two q squared. Divide by two: q squared equals twice r squared. Then q is even too. Both numerator and denominator are divisible by two, contradicting our choice of a fraction in lowest terms.

There is no trick in the final step. If an integer's square is even, the integer is even: an odd integer has an odd square. What we proved is quite strong. No fraction, however complicated, solves that equation. Decimal digits cannot change it. So if we want the exact diagonal length to be a number, we need a number system larger than the rationals.

## A sequence that knows where it wants to go

Let's attempt to approach that missing length anyway. Start with one point four. Square it and obtain one point nine six, below two. Move to one point four one; its square is one point nine eight eight one. Move to one point four one four; its square is still below two. Move to one point four one four two, still below. Continue choosing the greatest terminating decimal at a given precision whose square does not exceed two.

Every entry is rational. Each approximation is no greater than the next. All remain below two, and indeed below two as a length once we restrict to positive entries with square below two. We are constructing an increasing bounded sequence of rationals. One might expect it to converge. But ask the important question: converge *where*?

If convergence is required to a rational number, the answer is no. Suppose its limit were a rational L. The squaring function preserves limits of convergent sequences. Because the squares of our approximations approach two, L squared would have to equal two. We have just proved that no rational L can satisfy that equation. Our rational sequence is getting indefinitely close to a perfectly coherent location, but that location is absent from the rationals.

There is an even more striking way to describe the same sequence. The later approximations become close to *each other*. Once two entries agree to ten decimal places, their difference is tiny, regardless of whether we know a destination. As precision increases, every sufficiently late pair can be made as close together as desired. That property has a name: Cauchy.

## Cauchy sequences ask for internal agreement

A sequence is Cauchy when, for every positive tolerance, there is a stage after which any two terms differ by less than that tolerance. Ordinary convergence asks for proximity to a fixed limiting value. The Cauchy condition asks only whether the late terms agree with one another.

Every convergent sequence in a metric space is Cauchy. If all late terms are within half a tolerance of a limit, then any two late terms are within the full tolerance of each other, by the triangle inequality. This argument is so direct that it works for rational numbers, real numbers, vectors, and many other settings.

The converse is where completeness enters. In the rationals, Cauchy need not imply convergence to a rational. The decimal approximations to the square root of two are the counterexample. In the real numbers, every Cauchy sequence does converge to a real number. That fact is one standard formulation of completeness.

Notice the subtle difference. The decimal approximations did not somehow change after we admitted irrational limits. The entries and differences were exactly the same. We changed the space in which a limiting value was allowed to live. A statement about the same sequence can be true in one mathematical environment and false in another.

This distinction is essential for numerical computing. A program may produce approximations that agree to many digits without telling us whether the underlying specification admits a solution in the space we chose. Conversely, rigorous error estimates can make the approximations meaningful because they identify a mathematical object and control the distance to it.

## The least upper bound: a second face of the same principle

Let's approach completeness from a different direction. Consider the set of all nonnegative rational numbers whose squares are less than two. It has members: one is in the set, and so is one point four. It is bounded above: two is certainly an upper bound. Could it have a *least rational upper bound*?

Suppose that rational bound were called b. If b squared is less than two, there is a slightly larger rational number whose square is still less than two. We can choose the increment small enough because squaring changes continuously as we move a short distance. That contradicts b being an upper bound. If b squared is greater than two, there is a slightly smaller rational upper bound, contradicting leastness. Equality is impossible by the proof we already gave. Therefore this bounded set has no supremum inside the rational numbers.

The real-number least-upper-bound property says that every nonempty set of reals that is bounded above has a least upper bound *in the reals*. We call it the supremum. If there are many upper bounds, the supremum is the smallest among them. It need not belong to the original set. The essential guarantee is existence.

This is another formulation of completeness. Under the usual ordered-field assumptions, the least-upper-bound property and Cauchy completeness express the same deep fact about the real numbers. There are technical hypotheses in the equivalence; in an arbitrary metric space there may not even be a meaningful order or a supremum to discuss. For the familiar real line, however, the two views fit together.

An ordered set can be densely populated and still lack least upper bounds. The rationals prove it. We need completeness in addition to density if we want the number line to have no such gaps.

## How Dedekind tried to build the missing points

Richard Dedekind developed a systematic way to turn this difficulty into the construction of numbers. His account appeared in 1872, though the underlying work had been developing for years. He began with the ordered rational numbers and imagined dividing them into a lower part and an upper part, with every element of the lower part smaller than every element of the upper part.

A rational number can define such a division. All fractions below three belong to the lower side; fractions at or above three belong to the upper side. But a division can also be made at the square root of two without using that irrational number as a preexisting member of the rationals. Put a positive rational on the lower side when its square is less than two, along with all negative rationals. Put the remaining rationals on the upper side. This produces a perfectly definite partition of the rational numbers, even though no rational lies precisely at its boundary.

Dedekind used cuts of this sort to account for numbers missing from the rational system. The important intellectual move is that we can define the boundary by relationships among objects we already know. Our missing diagonal length is represented by how it separates rational values, rather than by an endless string of unexplained digits.

Dedekind was working amid a nineteenth-century effort to make analysis less dependent on geometrical pictures and intuitive talk about infinitesimals. Georg Cantor published another approach in the same period, using equivalence classes of rational Cauchy sequences. Either construction requires careful definitions and proofs of arithmetic properties; simply giving new objects names does not suffice.

There is a human side to this shift. A mathematician teaching calculus could no longer treat every intuitive property of a continuous line as self-evident. Students and colleagues might agree about a diagram, yet the logical basis of the assertion still needed examination. The resulting constructions can feel abstract precisely because they make explicit what had previously been taken for granted.

## Completeness earns its keep: monotone convergence

We can now prove something a computational scientist will recognize. Imagine a process producing an increasing sequence of real numbers, with a known ceiling. Will the process settle toward a limit, even if we cannot write that limit in a familiar formula?

Let S be the set of all values attained by the sequence. Because the sequence is bounded above and nonempty, completeness supplies its supremum L. Pick any positive tolerance epsilon. Because L is the *least* upper bound, L minus epsilon cannot still be an upper bound. So some term exceeds L minus epsilon. Since the sequence is nondecreasing, every later term is at least as large, while no term exceeds L. The difference from L is therefore smaller than epsilon from that point onward.

We have proved that an increasing sequence bounded above converges. The decreasing, bounded-below version follows by reversing inequalities. The proof is short once completeness is available. Without it, the decimal sequence aiming toward the square root of two would spoil the claim if we insisted on a rational limit.

The argument also illustrates what a theorem actually says. It gives existence of a limiting real number. It doesn't give a fast algorithm for computing it, and it doesn't tell us how rapidly the sequence approaches it. For speed we need additional estimates. For an actual stopping rule we may need a bound that can be evaluated from finite data.

## How a gap appears in proofs about square roots

There is a deeper reason to study the irrational diagonal instead of treating it as a curiosity. Many arguments in analysis say that a quantity is bounded and then assume there is a best possible boundary. What guarantees that the boundary belongs to the number system? It is not an algebraic identity. If we stay with rational numbers, we can list all rational lengths whose squares remain below two, and their rational upper bounds; there is no least rational upper bound.

The same missing boundary can disrupt an apparently reasonable algorithm. Suppose a sequence of rational estimates gets closer and closer together. We can say, with proof, that the estimates will eventually be within any prescribed tolerance of each other. This makes them useful approximations. But if our program's *mathematical specification* requires returning an exact rational solution of x squared equals two, there is no possible correct output. We need to change the type of answer: perhaps a real number described by a construction, a sequence with an error guarantee, or an interval that encloses the desired root.

Here is a practical contrast. A rational interval with endpoints one point four one four and one point four one five contains the square root of two. We can verify that by squaring both endpoints and comparing with two. That is a finite certificate requiring rational arithmetic alone. The interval is informative even though neither endpoint is the exact root. An algorithm can keep producing certified intervals while the mathematical theory establishes that a unique real location lies inside all of them.

In formal mathematics this separation can be expressed through different types: a rational value, a real value, a rational interval with a proof, or a sequence accompanied by convergence data. Treating these as interchangeable would erase the property we are trying to understand. The proof of existence is often different from the computation of an approximation, and both are worth doing.

## Why boundedness alone fails

Suppose the sequence alternates between zero and one forever. It stays between two familiar bounds, but it has no limit. So boundedness is insufficient. Suppose instead it moves upward and then downward irregularly. Monotonicity is missing, so the supremum proof cannot guarantee that once the sequence approaches the top it will remain there.

There is a different theorem that is often more appropriate for arbitrary bounded sequences. Every bounded sequence of real numbers has a convergent *subsequence*. That is the Bolzano–Weierstrass theorem. We do not claim the whole sequence converges; we select indices that move farther and farther along and whose corresponding values approach a limit.

To picture the proof, put all terms in a closed interval. Split the interval in half. At least one half contains infinitely many sequence terms. Keep that half. Split it again and retain a half with infinitely many terms. Repeating this creates nested closed intervals whose lengths shrink toward zero. Completeness guarantees a common limiting point, and we can choose terms with increasing indices from the successive intervals. The selected terms converge.

This is another appearance of the same central theme. A finite interval, continually narrowed without contradiction, traps a real point. If we performed the same reasoning entirely in the rationals, the nested intervals could narrow toward an irrational boundary and leave us without a rational point to select.

## A practical example: finding a root by bisection

Suppose we need a positive solution of x squared equals two. Start with the interval from one to two. At the midpoint, one point five, the square is two point two five, so the solution lies in the left half. Now use the interval from one to one point five. Its midpoint, one point two five, squares below two, so keep the right half. Continue.

At each step the interval still encloses a solution location by the sign change of x squared minus two. Each interval has half the preceding width. After ten steps, its width is one divided by one thousand twenty-four. After twenty, one divided by about a million. The endpoints form nested rational brackets, but the point they enclose is irrational.

The bisection argument has two distinct ingredients. The intervals get narrower by arithmetic, which supplies a computable error bound. Their common point exists by completeness, and continuity ensures that the point solves the equation. If we ignore either ingredient, we have an incomplete story. Shrinking an interval around a missing point does not create that point in a deficient number system; and knowing that a point exists does not by itself tell us how accurate a finite approximation is.

In a computer, numbers are represented with finitely many bits. Real completeness does not transfer directly to that finite representation. We use proofs about ideal real quantities to justify the target, then separate arguments about rounding and error to show what the implemented algorithm can guarantee.

## Another guarantee: nested closed intervals

Take a sequence of closed real intervals, each inside its predecessor. Suppose their lengths tend to zero. Can they enclose one and only one point forever? On the real line, yes. The left endpoints form a bounded nondecreasing sequence, while the right endpoints form a bounded nonincreasing sequence. Completeness gives limits to both sequences. Since the interval lengths tend to zero, the two limits agree. That common point belongs to every closed interval.

Notice the hypotheses. The intervals must be nonempty and closed, and their lengths must tend to zero for uniqueness. If we remove the shrinking-length condition, the common intersection may be an entire interval. If we remove closedness, nested open intervals can converge toward a boundary point that is not in any of them. Changing one word in a theorem can change the conclusion.

This nested-interval principle also helps explain the difference between formal existence and finite computation. We can verify the endpoints of each rational bracket in finite time. Completeness tells us the entire infinite nesting defines a real point. To approximate that point within one thousandth, we need only continue until the bracket is shorter than one thousandth. We never need to write an infinite decimal on a screen.

## A limit of limits, and the danger of circular explanation

There is a temptation to define a real number as an infinite decimal and declare the problem solved. But what does an infinite decimal mean? If it is a limit of finite decimal approximations, we must explain why that limit exists. If we use an infinite sum, we must explain why the sum has a value. Completeness is the property that allows such constructions to be justified rather than merely pictured.

One familiar result is that zero point nine repeating equals one, as real numbers. The finite truncations are nine tenths, ninety-nine hundredths, and so on. The difference between each truncation and one is one divided by ten to an increasing power. For any positive tolerance, these differences eventually fall below it. By uniqueness of limits, the infinite decimal represents one. There isn't an extra real number hiding between them.

This is an excellent example of how mathematics separates a representation from what it represents. The notation zero point nine repeating is a description of a limit; it is not a different point merely because the symbols look different. Two descriptions may denote the same mathematical object. That insight will return whenever we study equivalence classes, measurement, and numerical representations.

## The question beneath the number line

We began with a square whose diagonal had a perfectly determinate geometrical length but no rational numerical expression. We found rational approximations, discovered that they agree ever more closely with one another, and still could not locate a rational limit. The issue was not lack of effort. It was lack of completeness.

The real number system supplies least upper bounds and limits for Cauchy sequences. Those guarantees let us prove monotone convergence, extract convergent subsequences, justify bisection, and make sense of infinite decimal representations. In more advanced spaces we will ask the same question again: when a sequence becomes internally consistent, does the space actually contain what it approaches?

That question is one of the foundations of analysis. It turns the image of a continuous line into a mathematical promise we can use, and it shows us exactly when that promise fails.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

**Rational gap.** If \(p^2=2q^2\) with \(\gcd(p,q)=1\), then \(p,q\) are both even, contradiction. Thus \(\sqrt2\notin\mathbb Q\).

**Cauchy condition.** \((x_n)\) is Cauchy in a metric space \((X,d)\) when \(\forall\varepsilon>0\ \exists N\ \forall m,n\ge N: d(x_m,x_n)<\varepsilon\). Completeness means every Cauchy sequence in \(X\) converges to a point of \(X\).

**A rational Cauchy sequence without rational limit.** Put \(k_n=\max\{k\in\mathbb N:k^2<2\cdot10^{2n}\}\) and \(q_n=k_n/10^n\in\mathbb Q\). Then \(q_n^2<2\le(q_n+10^{-n})^2\). For \(m\ge n\), \(q_n\le q_m<q_n+10^{-n}\), hence \((q_n)\) is rational Cauchy. Any rational limit \(L\) would satisfy \(L^2=2\), contradiction.

**Least-upper-bound property.** Every nonempty, bounded-above subset of \(\mathbb R\) admits a supremum in \(\mathbb R\). For a nondecreasing bounded sequence set \(L=\sup_n x_n\); for each \(\varepsilon>0\), some \(x_N>L-\varepsilon\), and \(L-\varepsilon<x_n\le L\) for \(n\ge N\).

**Bisection.** For continuous \(f\) on \([a,b]\) with \(f(a)f(b)<0\), the standard sign-preserving interval-halving procedure produces nested intervals \(I_n\) with length \((b-a)/2^n\) containing a zero; a midpoint approximates that zero with absolute error at most half the bracket width.

**Representations.** \(0.\overline9=\lim_{n\to\infty}(1-10^{-n})=1\).

### Exercises with answers

1. **Exercise:** Why is \((1+1/n)\) Cauchy? **Answer:** It converges to 1, so the triangle inequality guarantees it is Cauchy; directly, for large \(m,n\), \(|1/m-1/n|\le 1/m+1/n\).
2. **Exercise:** Name a bounded real sequence without a limit. **Answer:** \((-1)^n\). It has convergent even and odd subsequences with different limits.
3. **Exercise:** Where is the gap in rational completeness? **Answer:** A rational Cauchy sequence approximating \(\sqrt2\) has no limit in \(\mathbb Q\).
4. **Exercise:** Explain the role of the supremum in monotone convergence. **Answer:** Its minimality ensures the increasing sequence eventually enters every interval \((L-\varepsilon,L]\).

### References

- Richard Dedekind, *Continuity and Irrational Numbers* (1872), in English translation and historical commentary.
- Stanford Encyclopedia of Philosophy, “Dedekind's Contributions to the Foundations of Mathematics,” https://plato.stanford.edu/entries/dedekind-foundations/
- Stanford Encyclopedia of Philosophy, “Continuity and Infinitesimals,” https://plato.stanford.edu/entries/continuity/
- Stephen Abbott, *Understanding Analysis*, chapters on sequences and completeness.
- Terence Tao, *Analysis I*, constructions of the reals and Cauchy sequences.
- [MIT OpenCourseWare, 18.100B Real Analysis (Spring 2025)](https://ocw.mit.edu/courses/18-100b-real-analysis-spring-2025/pages/lecture-notes/) — MIT 18.100B, lectures 1–7: completeness and convergence of real sequences.
