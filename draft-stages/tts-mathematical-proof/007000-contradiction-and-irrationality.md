# 007000 — Contradiction: Proving Something Cannot Happen

**Track:** Mathematical Reasoning and Proof from First Principles. **Background:** Even and odd integers; direct proof. **Purpose:** teach an actual proof obligation and the reasoning required to discharge it.

<!-- BEGIN SPOKEN LECTURE -->

# Contradiction: Proving Something Cannot Happen

There is a way to prove a claim by examining what would happen if it were false. Assume the denial of the desired conclusion. Reason carefully from that assumption together with the standing hypotheses. If the result is impossible, the denial cannot hold. In ordinary classical mathematics, this is proof by contradiction.

One of the first famous examples says that the square root of two is irrational. Irrational does not mean mysterious or unknowable. It means the number cannot be expressed as a fraction of two integers with nonzero denominator. A proof must rule out every such fraction at once.

## A complete irrationality proof

Suppose, seeking a contradiction, that the square root of two equals a fraction p over q in lowest terms, where p and q are integers and q is nonzero. Lowest terms means p and q share no common positive divisor greater than one. Square the equation. It says p squared equals twice q squared. Therefore p squared is even. The parity result established earlier tells us p itself must be even. Write p as two times r.

Substitute that into the squared equation. Four r squared equals twice q squared. Dividing by two gives q squared equals twice r squared. Hence q squared is even, and so q is even. But now both p and q are divisible by two, contradicting that the fraction was in lowest terms. No such representation exists, so the square root of two is irrational.

Where exactly is the contradiction? It is the simultaneous claim that p and q have no common factor greater than one and that both have the factor two. We did not derive a numerical impossibility such as zero equals one. We derived two incompatible statements under the same assumptions.

## Assumptions that make the argument work

The proof uses the fact that a rational number can be expressed as a fraction in lowest terms. That fact comes from elementary properties of the integers, such as division by a greatest common divisor or well-ordering. If we omit it, learning only that p and q are even is not itself contradictory: many fractions have even numerator and denominator. The choice of reduced fraction is the piece that closes the loop.

Likewise, when we square an equality, the resulting equation follows from the original. But squaring is not always reversible without additional sign information. From x squared equals four we get x equals two or minus two, not only two. Contradiction arguments often contain algebraic transformations; they must be checked just as carefully as any direct proof.

## Refuting an existence claim

Suppose someone claims that there exists a greatest integer. Assume there is one, call it M. The integer M plus one is larger. This contradicts the assumed maximality. Therefore no greatest integer exists. In this proof the negation of the existential statement is the desired universal negative: every candidate fails to be greatest.

We can also prove a universal negative by showing any hypothetical counterexample produces a contradiction. For example, no integer is both even and odd. If n equals twice a and also twice b plus one, subtraction gives twice the difference between a and b equals one. The left side is even, and the right side is odd, impossible by parity. The proof is simply the direct incompatibility of the two definitions.

## Classical reasoning and a useful distinction

In classical logic, to establish P by contradiction we may assume not P, reach an impossibility, and conclude P. Constructive logic distinguishes that from proving not P by assuming P and reaching an impossibility. The latter pattern is valid constructively; the unrestricted step from 'not not P' to P is a classical principle. The advanced constructive-logic course develops this distinction further. For elementary proof writing, what matters is that we identify which proposition was negated and what actually caused the contradiction.

Do not treat contradiction as a license for circular reasoning. If the supposed contradiction relies on the very theorem being proved, we have gained nothing. Likewise, an unfamiliar or surprising conclusion is not a contradiction. The conclusion must violate a known fact, a definition, an assumption, or an earlier proved theorem.

A good contradiction proof identifies its incompatible statements explicitly. If you cannot point to both sides of the conflict, the argument may still be missing its final step. With that discipline, contradiction becomes a precise tool rather than a rhetorical flourish.

<!-- END SPOKEN LECTURE -->

---

## Mathematical companion (not spoken)

### Reduced-fraction contradiction

Assume \(\sqrt2=p/q\) with \(p,q\in\mathbb Z\), \(q\neq0\), and \(\gcd(|p|,|q|)=1\). Then \(p^2=2q^2\). Since an odd integer has odd square, \(p\) must be even: \(p=2r\). Hence \(q^2=2r^2\), making \(q\) even. Now \(2\mid p\) and \(2\mid q\), contrary to coprimality.

### Exercises with answers

1. Prove there is no greatest integer. **Answer:** if \(M\) were greatest, \(M+1\) would be an integer greater than \(M\).
2. Does learning that both numerator and denominator are even contradict an arbitrary fractional representation? **Answer:** no; it contradicts a *reduced* representation.
3. Distinguish contradiction proving \(\neg P\) from classical contradiction proving \(P\). **Answer:** the first assumes \(P\) and derives falsehood; the second assumes \(\neg P\), derives falsehood, and uses double-negation elimination.

### Sources and further reading

- [Richard Hammack, Book of Proof, third edition (current online edition)](https://richardhammack.github.io/BookOfProof/).
- [Eric Lehman, F. Thomson Leighton and Albert R. Meyer, Mathematics for Computer Science, MIT OCW 6.042J](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/).
- [forall x: Calgary, A Free and Open Introduction to Formal Logic (Open Logic Project)](https://forallx.openlogicproject.org/).
- [Wikipedia: Proof by contradiction](https://en.wikipedia.org/wiki/Proof_by_contradiction).
