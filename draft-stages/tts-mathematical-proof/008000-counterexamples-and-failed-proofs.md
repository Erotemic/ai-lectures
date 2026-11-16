# 008000 — Counterexamples: How One Example Defeats a General Claim

**Track:** Mathematical Reasoning and Proof from First Principles. **Background:** Universal statements and implication. **Purpose:** teach an actual proof obligation and the reasoning required to discharge it.

<!-- BEGIN SPOKEN LECTURE -->

# Counterexamples: How One Example Defeats a General Claim

Mathematical theorems often contain the word 'every.' That makes them powerful, but it also makes them vulnerable: one counterexample disproves a universal claim. The counterexample must satisfy the claim's hypotheses while violating its conclusion. Failing a hypothesis is not a refutation. Showing that a different theorem is false is not a refutation either.

Take the assertion that every prime number is odd. The number two is a prime and it is even. One example settles the matter. More complicated assertions may resist such quick searches because the dangerous cases lie at the boundary of the hypotheses: zero, empty sets, disconnected domains, repeated eigenvalues, or functions that behave badly at one point.

## Diagnosing a false converse

Recall that if an integer is divisible by six, it is divisible by three. The converse says that if it is divisible by three, it is divisible by six. The integer three refutes the converse. It meets the antecedent, divisibility by three, and violates the consequent, divisibility by six. Notice that our counterexample does not contradict the original theorem. It isolates a logical direction that was never promised.

Try a claim about functions: 'if a function has derivative zero at a point, it has a local maximum there.' Consider x cubed at zero. Its derivative is zero there, but values on one side are smaller and on the other larger. The claim confuses a necessary condition for a differentiable interior extremum with a sufficient one. The counterexample is not just an isolated fact; it tells us which missing hypothesis to examine. A negative second derivative can guarantee a strict local maximum under suitable smoothness assumptions, while a zero first derivative alone cannot.

## Boundary examples reveal missing assumptions

Suppose a theorem seems to say that every bounded sequence converges. The sequence alternating between one and minus one is bounded but does not converge. Yet it has convergent subsequences. This suggests a repair: boundedness on the real line guarantees at least one convergent subsequence, not convergence of the original sequence. The repaired theorem is the Bolzano–Weierstrass result, and its proof requires the completeness of the real numbers.

Consider another proposed theorem: a continuous function on a set attains its largest value. On the open interval from zero to one, the function f of x equal to x has no maximum. Every value can be exceeded by another point still inside the interval. The closed interval from zero to one does have a maximum for the same function. The boundary condition, expressed precisely through compactness, is not incidental.

## How to search responsibly

When testing a conjecture, first classify its logical form. If it claims all objects have a property, try the simplest and most degenerate admissible objects. If it claims an implication, seek an object where the hypothesis is true and the conclusion false. If it claims two sets are equal, try to find an element belonging to one but not the other. If it claims uniqueness, look for two distinct witnesses. If it claims an operation is well-defined, choose two representatives of the same object and see whether the operation produces incompatible answers.

Computations can help discover a counterexample, but a mathematical refutation still requires verifying it. A floating-point approximation showing a small negative value might be a rounding artifact. An alleged graph counterexample should have its edges and claimed properties checked. If a result depends on a subtle domain condition, write that condition down rather than trusting a picture.

## Repairing rather than merely rejecting

A good counterexample can become a guide to a true theorem. 'Every bounded function on an interval has a maximum' fails for discontinuous functions or open intervals. Continuity on a nonempty compact interval supplies the missing conditions. 'Every square matrix is diagonalizable' fails for a Jordan block, but real symmetric matrices are orthogonally diagonalizable. 'Every subset of a compact space is compact' fails, but every closed subset of a compact space is compact.

This is how much of mathematical understanding grows. A naive claim fails; the counterexample tells us what feature matters; a sharper statement emerges. We learn not just whether a theorem is true, but why each assumption belongs in it.

There is also a limitation to remember: an unsuccessful search for counterexamples does not prove a theorem. A million positive trials remain finite evidence unless a separate argument shows they exhaust all possibilities. By contrast, one correctly verified negative trial can settle a universal conjecture. Learn to use that asymmetry carefully. It is one of the fastest ways to become a better proof reader and a better theorem writer.

<!-- END SPOKEN LECTURE -->

---

## Mathematical companion (not spoken)

### Counterexamples and repaired claims

| False statement | Counterexample | Useful repair |
|---|---|---|
| Every bounded real sequence converges | \(a_n=(-1)^n\) | Every bounded real sequence has a convergent subsequence |
| Every critical point is a maximum | \(f(x)=x^3\) at \(0\) | A negative second derivative yields a strict local maximum under standard smoothness hypotheses |
| Every continuous function on an interval attains a maximum | \(f(x)=x\) on \((0,1)\) | Every continuous real function on a nonempty compact set attains its maximum and minimum |

### Exercises with answers

1. Refute 'every square of an integer is strictly positive.' **Answer:** \(0^2=0\).
2. Refute 'if \(f(A)=f(B)\), then \(A=B\)' for arbitrary functions. **Answer:** \(f(x)=x^2\), \(A=\{-1\}\), \(B=\{1\}\).
3. Explain the logical requirement for a counterexample to \(P\Rightarrow Q\). **Answer:** exhibit an admissible object with \(P\) true and \(Q\) false.

### Sources and further reading

- [Richard Hammack, Book of Proof, third edition (current online edition)](https://richardhammack.github.io/BookOfProof/).
- [Eric Lehman, F. Thomson Leighton and Albert R. Meyer, Mathematics for Computer Science, MIT OCW 6.042J](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/).
- [Wikipedia: Counterexample](https://en.wikipedia.org/wiki/Counterexample).
