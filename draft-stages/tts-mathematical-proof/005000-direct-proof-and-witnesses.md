# 005000 — Direct Proof: Turning a Hypothesis into a Conclusion

**Track:** Mathematical Reasoning and Proof from First Principles. **Background:** Definitions of integers and divisibility. **Purpose:** teach an actual proof obligation and the reasoning required to discharge it.

<!-- BEGIN SPOKEN LECTURE -->

# Direct Proof: Turning a Hypothesis into a Conclusion

The most straightforward kind of proof begins where a theorem begins. You assume its hypotheses and move, by justified steps, toward its conclusion. This is called a direct proof. Its power is easy to overlook because it may not involve a named trick. It does involve a reliable discipline: use the exact information given, introduce witnesses when definitions promise them, and keep track of what sort of object each symbol denotes.

Take the claim: if an integer is divisible by six, then it is divisible by three. Let n be an arbitrary integer divisible by six. That means there is an integer k with n equal to six times k. Rewrite six times k as three times two k. Since two k is an integer, n satisfies the definition of divisibility by three. The entire proof is the movement from one witness to another.

## Witnesses make existential conclusions concrete

To prove that an integer is divisible by d, exhibit an integer quotient. To prove a set is nonempty, identify an element. To prove a function is not injective, find two distinct inputs with the same output. These are existential obligations. They cannot be met merely by restating the desired property. A useful question while writing is: what object is the theorem asking me to build?

Consider two integers a and b each divisible by five. Then a equals five r and b equals five s for integers r and s. Their sum equals five times r plus s. Thus it is divisible by five. The witness for the conclusion is r plus s. We did not need to know the numerical values of a or b. We needed only the representations supplied by divisibility.

The same reasoning proves that multiples of five are closed under subtraction, because r minus s remains an integer. The word 'closed' here means the operation stays within the set under discussion. Later, a subspace or subgroup proof will repeat this pattern: take arbitrary elements of the candidate set, apply an operation, and demonstrate that the result still satisfies the defining property.

## Direct proof with inequalities

Suppose we want to prove: if x and y are nonnegative real numbers, then x plus y is nonnegative. This follows from the compatibility of the order on the real numbers with addition. Starting with zero less than or equal to x, add y to both sides. We get y less than or equal to x plus y. Combining zero less than or equal to y with that inequality gives zero less than or equal to x plus y. The conclusion is now derived from declared assumptions and order rules.

It is important to notice which operations preserve inequalities. Adding the same real number does. Multiplying by a nonnegative number does; multiplying by a negative number reverses the inequality. A proof that divides by a variable without establishing its sign may be invalid. The same kind of audit applies to algebraic cancellation: canceling a factor requires that factor to be nonzero.

## Generalizing an example

Take the numerical identity that three times five minus three times two equals three times three. One may see a pattern and conjecture the distributive law. A general proof works with arbitrary real numbers a, b, and c and uses the field axiom a times b minus a times c equals a times the difference b minus c. This may itself be an axiom or an earlier derived theorem, depending on how algebra has been developed. A proof is always relative to accepted starting rules. It is not required to rebuild arithmetic from set theory in every lecture.

A useful technique is to transform the expression appearing in the hypothesis until it resembles the target. For claims about divisibility, factor out the needed integer. For claims about functions, start from the definition at an arbitrary input. For claims about subset inclusion, pick an arbitrary element of the left-hand set and show it belongs to the right-hand set. The action changes with the conclusion's logical form.

## A complete set inclusion proof

Let A, B, and C be sets. We want to show that if A is contained in B and B is contained in C, then A is contained in C. Start with an arbitrary element x of A. Since A is a subset of B, x is in B. Since B is a subset of C, x is in C. Therefore every element of A belongs to C, which is exactly the definition of A being a subset of C.

Notice that this argument does not require A to contain any element. If A is empty, the universal claim has no counterexample. Nothing goes wrong. The proof does not rely on choosing an actual element in advance; 'take an arbitrary element' introduces a hypothetical element for a conditional argument.

Direct proofs teach the central skill of all proof writing: matching a conclusion to the data that would establish it. Later techniques, such as induction or contradiction, will change the route. They do not change the need to know exactly what has been proved.

<!-- END SPOKEN LECTURE -->

---

## Mathematical companion (not spoken)

### Witness-based divisibility proof

For \(d\neq0\), \(d\mid a\) means \(\exists k\in\mathbb Z\;(a=dk)\). If \(5\mid a\) and \(5\mid b\), choose \(r,s\) with \(a=5r\), \(b=5s\); then \(a-b=5(r-s)\), so \(5\mid(a-b)\).

For subset transitivity,
\[
A\subseteq B\land B\subseteq C\Rightarrow A\subseteq C,
\]
fix arbitrary \(x\in A\), use each hypothesis to obtain \(x\in B\) then \(x\in C\). This works for \(A=\varnothing\).

### Exercises with answers

1. Show that if \(3\mid a\) and \(3\mid b\), then \(3\mid(2a-5b)\). **Answer:** writing \(a=3r,b=3s\) gives \(2a-5b=3(2r-5s)\).
2. Prove that the sum of two nonnegative reals is nonnegative. **Answer:** add the two inequalities \(0\leq x\) and \(0\leq y\).
3. Which step is invalid when multiplying an inequality by an unknown real \(t\)? **Answer:** preserving its direction before establishing \(t\geq0\).

### Sources and further reading

- [Richard Hammack, Book of Proof, third edition (current online edition)](https://richardhammack.github.io/BookOfProof/).
- [Eric Lehman, F. Thomson Leighton and Albert R. Meyer, Mathematics for Computer Science, MIT OCW 6.042J](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/).
- [Wikipedia: Direct proof](https://en.wikipedia.org/wiki/Direct_proof).
