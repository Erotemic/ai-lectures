# 017000 — Epsilon-Delta Proofs: Controlling a Function Near a Point

**Track:** Mathematical Reasoning and Proof from First Principles. **Background:** Sequences and basic algebra. **Purpose:** teach an actual proof obligation and the reasoning required to discharge it.

<!-- BEGIN SPOKEN LECTURE -->

# Epsilon-Delta Proofs: Controlling a Function Near a Point

A function has a limit L as x approaches a when its outputs become arbitrarily close to L whenever its inputs are sufficiently close to a, excluding the point a itself. Continuity adds the requirement that the function's value at a exists and agrees with that limit. The difference matters: a removable hole can have a limit even when the function is undefined at the hole.

The epsilon-delta language encodes the relation. Given any positive desired output error epsilon, we must supply a positive input radius delta. Every point x of the domain satisfying zero less than the distance from x to a and less than delta must have output within epsilon of L. The order is crucial. Delta is allowed to depend on epsilon and a, but not on the particular x selected after delta has been fixed.

## The easiest exact proof

Consider f of x equals three x plus one and a fixed real base point a. We claim the function is continuous at a. Given epsilon greater than zero, choose delta equal to epsilon divided by three. If the distance from x to a is less than delta, the distance from f of x to f of a is three times the distance from x to a, which is less than epsilon. This is a complete epsilon-delta proof. It does not merely evaluate the algebraic expression at a; it shows how to choose an input tolerance that guarantees an output tolerance.

A proof does not require the smallest possible delta. Any positive choice that works is enough. Sometimes a convenient conservative estimate is easier to derive than an optimal one.

## When an extra bound is needed

Now consider f of x equals x squared. At a fixed real number a, the difference between x squared and a squared factors as x minus a times x plus a. We can directly make the first factor small by choosing x near a. But the second factor also depends on x. Control it by first requiring x to be within one of a. Then the absolute value of x plus a is at most two times the absolute value of a plus one. For any requested epsilon, choose delta to be the smaller of one and epsilon divided by two absolute a plus one. When x is within delta of a, the product estimate is less than epsilon. We have proved continuity at every real a.

This is a typical two-stage estimate. First restrict to a convenient neighborhood so the uncontrolled-looking factor becomes bounded. Then choose a smaller neighborhood that delivers the requested accuracy. The same idea appears in products of convergent sequences, continuity of products, and error bounds for polynomials.

## Why order of quantifiers distinguishes uniform continuity

For ordinary continuity, delta may depend on the base point a. For uniform continuity on a domain, one delta must work simultaneously for every pair of points in that domain once epsilon is specified. The function x squared is continuous at every real number but not uniformly continuous on the entire real line. Take two large nearby points n and n plus one over n. Their input distance is one over n, tending to zero, while their squared outputs differ by two plus one over n squared. No single delta works for output accuracy one at every point of the real line.

On a bounded closed interval, x squared is uniformly continuous. The factor x plus a is then bounded uniformly across the interval. This is an early example of how compactness turns local control into global control.

## Reading a proof of discontinuity

To prove a function is discontinuous at a, we must exhibit a positive epsilon such that every positive delta admits a point x within delta of a whose output remains at least epsilon away from f of a. The point x may depend on delta. For the function that equals zero at zero and one everywhere else, choose epsilon equal to one half. No matter how small delta is, there is a nonzero x closer than delta to zero, but its output differs from f of zero by one. So the function is discontinuous at zero.

A plot may show the jump, but the epsilon-delta argument identifies exactly why no input tolerance can guarantee the required output tolerance. Conversely, a single path approaching a with a wrong output limit can refute a proposed multivariable limit, though confirming a limit requires control of all approaches.

## Use the definition as a design tool

When a proof asks for continuity, start by writing the desired inequality on outputs. Manipulate it until you find a sufficient condition on inputs. Take note of where the proposed delta depends on the point a. Check that delta is positive and that it works for every admissible x, not only for a convenient sequence. This is proof writing as quantitative design: decide how accurate the answer must be, then work backwards to the input control needed to guarantee it.

<!-- END SPOKEN LECTURE -->

---

## Mathematical companion (not spoken)

### Epsilon–delta continuity

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

### Exercises with answers

1. Prove \(f(x)=7x-2\) is continuous everywhere. **Answer:** use \(\delta=\varepsilon/7\).
2. Why is \(x^2\) not uniformly continuous on all \(\mathbb R\)? **Answer:** choose \(x=n,y=n+1/n\); their distance tends to zero but the output difference tends to two.
3. State the negation of continuity at \(a\). **Answer:** \(\exists\varepsilon>0\,\forall\delta>0\,\exists x\in D\) with \(|x-a|<\delta\) and \(|f(x)-f(a)|\ge\varepsilon\).

### Sources and further reading

- [Richard Hammack, Book of Proof, third edition (current online edition)](https://richardhammack.github.io/BookOfProof/).
- [Eric Lehman, F. Thomson Leighton and Albert R. Meyer, Mathematics for Computer Science, MIT OCW 6.042J](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/).
- [OpenStax, Calculus Volume 1, Rice University](https://openstax.org/books/calculus-volume-1/pages/preface).
- [Wikipedia: Limit of a function](https://en.wikipedia.org/wiki/Limit_of_a_function).
