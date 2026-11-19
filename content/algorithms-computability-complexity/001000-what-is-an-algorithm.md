# What Is an Algorithm, Really?

**Track:** Algorithms, Computability, and Complexity  
**Lecture:** 001000 — Foundations  
**Assumed background:** Whole numbers, elementary functions, and the idea of a computer program.  
**Companion:** Formal definitions, Euclidean algorithm, and source-to-claim map below the narration.

<!-- BEGIN SPOKEN LECTURE -->

Imagine that you are handed two numbers: two hundred fifty-two and one hundred five. Someone asks for the largest positive whole number that divides them both. You can test divisors one at a time, but there is a more revealing question. Could you give a finite set of instructions that works, not merely for these numbers, but for every admissible pair, no matter how large? Could you explain why the instructions give the right answer, and why they eventually stop?

That is the beginning of algorithmic thinking. We are not primarily asking a machine to perform a trick. We are asking for a general method whose meaning, correctness, and resource requirements can be investigated.

The word *algorithm* is often used casually to mean software, a recommendation system, or an inscrutable rule chosen by a company. But a mathematical algorithm is not identical to a software product. An algorithm describes a method of computation. A program is an implementation of a method in a particular language and execution environment. And a *problem* comes before both: it tells us what counts as a correct answer.

To make this distinction precise, suppose the problem is to compute a greatest common divisor. Its input is a pair of nonnegative whole numbers, with at least one positive. Its output is a positive whole number that divides both inputs, such that every other positive common divisor also divides that output. The definition says nothing about the route we take to find it. This is a specification. Many procedures can meet it.

Now I can describe one procedure. Begin with the two numbers, calling them a and b. As long as b is nonzero, replace the pair by b and the remainder obtained when a is divided by b. When b reaches zero, return a. For two hundred fifty-two and one hundred five, the first remainder is forty-two. The next remainder is twenty-one. The next is zero. The procedure returns twenty-one.

Why should we trust twenty-one? The answer is not that the calculation looked plausible. A positive whole number divides both a and b exactly when it divides both b and the remainder after division of a by b. A divisor of a and b divides their difference, and hence divides the remainder. Conversely, if it divides b and that remainder, it also divides a, because a is an integer multiple of b plus the remainder. The set of common divisors is unchanged at each replacement. Consequently the greatest common divisor is unchanged too.

This fact is the invariant of the algorithm. An invariant is a property that remains true as computation changes its state. Before the first step, the current pair has the same greatest common divisor as the input, obviously. If that is true before one step, it remains true afterward because the step preserves common divisors. When the second component becomes zero, the greatest common divisor of a and zero is a, provided a is positive. So the returned value satisfies the specification.

Notice what has and has not been proved. We have shown that *if* the procedure stops, its answer is right. But we have not yet shown that it stops. Correctness has a second dimension: termination.

When b is positive, the remainder of a divided by b is a nonnegative integer strictly smaller than b. After one iteration, that remainder becomes the new b. So, each time we continue, a nonnegative whole number decreases. It cannot strictly decrease forever. Therefore the procedure eventually reaches zero and returns. The preserved invariant plus a decreasing, well-founded measure gives a proof of total correctness for the stated inputs.

There is an ancient lineage here. Book Seven, Proposition Two of Euclid's *Elements* addresses the greatest common measure of two numbers. Euclid's presentation uses successive subtraction. Our version groups repeated subtractions into division with remainder. It is a modern formulation closely connected to the ancient construction, not a literal transcription of Euclid's pseudocode.

I want to emphasize something easy to miss. A single run has checked an instance. The proof covers an entire input domain. The gap between those two accomplishments is the gap between testing an answer and understanding an algorithm.

Now suppose the input is an empty list of numbers and the task is, 'Return its largest member.' What should the machine do? There is no largest element. A specification might reject empty inputs, return a designated absence value, or demand a separate error result. None of these decisions is an implementation detail. They change the problem being solved. Likewise, if the input consists of real numbers rather than machine integers, comparisons, equality, and representation require further thought. If a sorting procedure assumes its comparator is transitive and the actual comparator is not, a proof about ordered inputs does not automatically apply.

The honest unit of reasoning is therefore a relationship between admissible inputs and acceptable outputs. For deterministic, single-valued problems, that relationship may look like an ordinary mathematical function. But some problems admit many correct answers. If I ask for any shortest route between two vertices, ties may leave several acceptable routes. If I ask for any satisfying assignment of a logical formula, I may accept many different witnesses. A specification can be a relation rather than a single predetermined result.

The algorithm itself needs a sufficiently precise computational model. In everyday explanations we say 'compare two values' or 'look up an array element' as though each were one step. On a real machine, cost depends on representation, memory organization, and hardware. For correctness, those details may not always matter. For efficiency, they often do. A dictionary lookup may have expected constant-time behavior under suitable hashing assumptions; a balanced search tree has different guarantees. Neither is simply the abstract word 'lookup' made concrete.

The remarkable historical shift came when mathematicians asked whether the very notion of an effective, mechanical procedure could be described rigorously. In the nineteen thirties, several definitions appeared: Church's lambda calculus, recursive function systems developed by Gödel, Kleene, and others, and the machine models of Turing and Post. These frameworks looked quite different, yet their general-purpose versions characterize the same class of computable functions under the standard encodings. That equivalence is a theorem about the formal models.

Alan Turing's paper, written in nineteen thirty-six and published in nineteen thirty-seven, used an abstract machine with a finite control, a tape bearing symbols, and rules for changing state and moving along the tape. One should not confuse a Turing machine with the internal organization of a modern processor. The model strips away contingent engineering details to expose a notion of step-by-step symbolic computation.

The Church–Turing thesis says, in a common formulation, that every effectively calculable function can be computed by such a machine. It is important not to call this an ordinary theorem. The word *effectively* belongs to an informal notion of mechanically executable calculation, so the thesis connects an intuitive concept to a mathematical model. Formal equivalence among lambda calculus, recursive functions, and Turing machines supports the thesis, but those equivalence proofs are not themselves a proof of every possible informal interpretation of mechanical computation. Nor does the thesis assert that all computational tasks are practical, or that ordinary machines can solve every precisely stated problem.

The last point matters enormously. There exist perfectly precise questions for which there is no algorithm that always produces the requested answer. For example, the general halting problem asks for a method that, given an arbitrary program and its input, always determines whether that program eventually stops. Turing's work establishes the impossibility of a universal decision procedure of this kind. We will prove that fact separately. For now, keep the distinction: a problem can be meaningful and mathematically well-defined without having a total algorithmic solution.

Even when a problem is computable in principle, it may require a completely impractical quantity of work. Imagine an algorithm that enumerates every possible order of a thousand objects. It is a finite procedure, and it may even be correct. It is not therefore a usable procedure. That is why *computability* and *complexity* deserve separate study. Computability asks whether a procedure exists, subject to the chosen formal model and problem definition. Complexity asks what computational resources are required, and how those requirements grow with input size.

Return to the greatest common divisor. The mathematical description uses arithmetic on arbitrary integers. But a program running on bounded integers can overflow, and some languages define distinct behavior for negative division or remainder. Our proof requires nonnegative inputs and a particular meaning for remainder. If we compile the algorithm into a language with fixed-width unsigned integers, the correctness bridge needs to establish that each arithmetic operation stays within its permitted range. For the basic remainder version on nonnegative inputs, it can; for arbitrary code, one should not assume that.

There is also a difference between the number of iterations and the cost of an iteration. Dividing two integers with a million binary digits is not a single physical clock cycle. An algorithm analyzed by counting arithmetic operations may have a different bit-complexity once arithmetic is implemented. We must state the cost model before treating an operation count as a running-time theorem.

This leads to four questions worth asking of almost any claimed algorithm. What exactly is the problem? Which inputs are admissible, and what constitutes a correct output? Why does the proposed procedure preserve the required mathematical relationship and eventually stop? Under which computational assumptions is it fast enough, or even possible to run?

There is a fifth question, if we care about software rather than mathematical pseudocode: what connects the proof to the actual implementation? A proof about a mathematical sequence does not certify a piece of source code unless the relationship between the two is established. Tests can show that selected executions agree with expectations. A refinement argument, or a machine-checked correctness proof under a documented semantics, can establish a stronger connection.

Try a thought experiment. Someone offers a machine that returns the right answer on every example you test. Is that evidence of correctness? Certainly. Is it a universal proof? No. You can always write a procedure that behaves correctly for all inputs below a chosen size and fails on the next one. Conversely, a proof that an algorithm is correct under an assumption says nothing about inputs that violate the assumption. A good algorithm designer learns to search for the assumption, the invariant, and the progress measure before admiring the output.

Our greatest-common-divisor procedure is small enough that those ingredients fit in our heads. That is a useful place to begin. From this example we get a vocabulary that scales: problem, specification, state, invariant, termination, computational model, implementation, and cost. With those distinctions in place, the subject of algorithms is no longer a collection of recipes. It becomes a way to explain what a computation promises, why that promise should be believed, what it will cost, and where the promise stops.

<!-- END SPOKEN LECTURE -->

## Mathematical and implementation companion — not narrated

### Domain, specification, and code

For `a, b ∈ ℕ`, `a + b > 0`, define `gcd(a, b)` as the maximum positive common divisor. If `b > 0`, write `a = qb + r`, `0 ≤ r < b`. Then

\[
\gcd(a,b)=\gcd(b,r).
\]

The loop preserves `gcd(a,b)=gcd(a₀,b₀)`. It terminates because the positive second component strictly decreases whenever a loop iteration occurs. The case `(0,0)` is excluded to avoid treating the maximum positive common divisor as defined there; some computational libraries adopt the convenient convention `gcd(0,0)=0`.

```python
def gcd_nonzero_pair(a: int, b: int) -> int:
    assert a >= 0 and b >= 0 and (a or b)
    while b:
        a, b = b, a % b
    return a
```

**Trace:** `(252, 105) → (105, 42) → (42, 21) → (21, 0) → 21`.

### Source-to-claim notes

- **Euclid, *Elements*, VII.2.** Historical attribution to the greatest-common-measure construction. The remainder loop is a modern formulation, not a direct quotation from the source. [Clay Mathematics Institute translation](https://www.claymath.org/euclid_index/fundamentals-of-number-theory/?chapter=2).
- **Demaine, Ku, and Solomon, MIT 6.006 Spring 2020, Lecture 1.** Specification as relation from inputs to correct outputs; correctness and asymptotic cost are distinct obligations. [Lecture 1 notes](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/477c78e0af2df61fa205bcc6cb613ceb_MIT6_006S20_lec1.pdf).
- **Turing, A. M., “On Computable Numbers, with an Application to the Entscheidungsproblem.”** Published in *Proceedings of the London Mathematical Society* s2-42 (1937), 230–265; paper received in 1936. [Original publication record](https://doi.org/10.1112/plms/s2-42.1.230).
- **Jack Copeland and collaborators, “The Church–Turing Thesis,” Stanford Encyclopedia of Philosophy**, §§1, 4–6. Distinguishes formal equivalences and the informal effectiveness claim. [SEP](https://plato.stanford.edu/entries/church-turing/).
- **“Computability and Complexity,” Stanford Encyclopedia of Philosophy**, §§1–2. Background on equivalent formalisms and undecidability. [SEP](https://plato.stanford.edu/entries/computability/).

### Check your understanding

1. Why is `a` alone a valid answer when `b=0` and `a>0`?
2. Explain which hypothesis guarantees termination. Would it remain valid if the remainder operation could produce a negative number?
3. Distinguish a proof of equivalence between two formal computation models from the Church–Turing thesis.
4. What extra obligations arise when porting mathematical pseudocode to fixed-width arithmetic?
