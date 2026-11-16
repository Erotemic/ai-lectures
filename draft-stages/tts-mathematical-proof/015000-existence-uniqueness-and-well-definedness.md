# 015000 — Existence, Uniqueness, and Constructive Descriptions

**Track:** Mathematical Reasoning and Proof from First Principles. **Background:** Quantifiers, functions, and direct proofs. **Purpose:** teach an actual proof obligation and the reasoning required to discharge it.

<!-- BEGIN SPOKEN LECTURE -->

# Existence, Uniqueness, and Constructive Descriptions

Many theorems say that an object exists. A stronger theorem may say that there is exactly one such object. These are two separate responsibilities. To prove existence, supply a construction or an argument that rules out nonexistence. To prove uniqueness, suppose there are two admissible objects and show they must be equal. An existence proof does not establish uniqueness, and a uniqueness proof can be valid even when nothing exists.

## A simple equation with a unique solution

Take the equation two x plus three equals eleven, with x required to be a real number. We produce x equals four, and direct substitution verifies that it works. This is existence. For uniqueness, suppose x and y both solve the equation. Then two x plus three and two y plus three both equal eleven, so two x equals two y. Dividing by two gives x equals y. There is at most one solution. Combining both parts shows there is exactly one.

Notice the two different logical structures. Existence states 'there is some x with the property.' Uniqueness states 'for all x and y with the property, x equals y.' A writer who says 'the solution' before establishing either requirement may be silently assuming what needs proof.

## Nonconstructive existence and explicit construction

Some existence proofs identify a witness. Others derive existence without a formula for the witness. The intermediate value theorem states that a continuous real function on a closed interval takes every value between its endpoint values. Under its hypotheses, if f at a is negative and f at b is positive, a root exists somewhere in the interval. The theorem does not by itself tell us a finite exact expression for that root.

The bisection method builds nested intervals containing a root and can approximate it to any prescribed accuracy when the sign and continuity assumptions are satisfied. An approximation procedure is extra information beyond the bare existence theorem. Separating the claim that an object exists from the claim that we can calculate it efficiently becomes essential in optimization, numerical analysis, and computability.

## Well-definedness is a third obligation

Suppose we define a function on rational numbers by taking a fraction p over q and sending it to p plus q. This does not define a function of the rational number: one half can be written one over two or two over four, producing outputs three and six. The rule depends on a choice of representation. To construct a function on equivalence classes, prove that different representatives always give the same output. Only then is there a well-defined object to discuss.

A proof may therefore have several stages: define a candidate, show it is well-defined, show it has the required property, and show it is unique. Textbooks sometimes compress these into a single paragraph. When learning the argument, it helps to separate them so no obligation is lost.

## Uniqueness in linear algebra

Suppose v one through v k is a basis of a vector space. By spanning, every vector can be written as a linear combination of the basis vectors: existence of coordinates. By linear independence, those coordinates are unique. If two coefficient lists represented the same vector, subtract the expansions to obtain a linear combination equal to zero. Independence forces each coefficient difference to vanish. The proof of a coordinate system is therefore an existence-and-uniqueness theorem in disguise.

The same structure appears in differential equations. A theorem may guarantee that an initial-value problem has a solution and that no two distinct solutions satisfy the same initial condition. But without hypotheses such as appropriate regularity of the vector field, uniqueness may fail. For example, the equation y prime equals the square root of the absolute value of y, with initial value y of zero equal to zero, allows a zero solution and delayed-start solutions. Continuous right-hand sides alone need not guarantee uniqueness.

## Reading a theorem with an existential conclusion

Ask whether the theorem claims one witness, at least one, at most one, or exactly one. Ask which assumptions are used for each part. If a proof defines something by a choice of representative, ask whether the result is independent of that choice. If it defines an object as a limit, ask whether the limit exists and is independent of the approximating sequence. If it defines a map as 'the unique' solution of an equation, check the uniqueness argument rather than trusting the definite article.

These questions may sound elementary, but they reappear at every level: the uniqueness of a derivative, existence and uniqueness for differential equations, the construction of a completed metric space, the definition of an integral, and the classification of algebraic structures. A reliable proof tells us what exists, why it exists, and whether other choices could change the answer.

<!-- END SPOKEN LECTURE -->

---

## Mathematical companion (not spoken)

### Existence versus uniqueness

To prove \(\exists!x\,P(x)\), give a witness \(x_0\) satisfying \(P\) and prove
\[
\forall x,y\;(P(x)\land P(y)\Rightarrow x=y).
\]
For \(2x+3=11\), existence comes from \(x=4\); uniqueness from \(2x+3=2y+3\Rightarrow x=y\).

The initial value problem \(y'=\sqrt{|y|}\), \(y(0)=0\) has nonunique differentiable solutions on \(t\geq0\): \(y(t)\equiv0\), and for each \(c\geq0\),
\[
y_c(t)=\begin{cases}
0,&t\leq c\\
(t-c)^2/4,&t>c.
\end{cases}
\]
Each satisfies the same initial condition and differential equation. This motivates additional hypotheses in uniqueness theorems.

### Exercises with answers

1. Prove that a vector has at most one coordinate list relative to a linearly independent family. **Answer:** subtract two representations; independence makes every coefficient difference zero.
2. Why does 'at most one solution' not imply 'there is a solution'? **Answer:** a problem may have none.
3. Is \([p/q]\mapsto p+q\) a well-defined map on rational numbers? **Answer:** no; \(1/2=2/4\) but the proposed outputs differ.

### Sources and further reading

- [Richard Hammack, Book of Proof, third edition (current online edition)](https://richardhammack.github.io/BookOfProof/).
- [Eric Lehman, F. Thomson Leighton and Albert R. Meyer, Mathematics for Computer Science, MIT OCW 6.042J](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/).
- [Wikipedia: Uniqueness theorem](https://en.wikipedia.org/wiki/Uniqueness_theorem).
