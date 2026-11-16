# 004000 — Recurrences, Rational Generating Functions, and Growth

**Track:** Discrete Mathematics and Combinatorics. **Background:** ordinary generating functions, coefficient extraction, elementary algebra. **Question:** how can a local recurrence predict an entire infinite sequence and its rate of growth?

<!-- BEGIN SPOKEN LECTURE -->

# Recurrences, Rational Generating Functions, and Growth

Some sequences are defined not by a formula for their n-th term but by a rule that looks backward. A population count depends on previous populations. The number of tilings of a board depends on tilings of shorter boards. An algorithm's workload can depend on smaller subproblems. Such rules are recurrences, and they often seem to require laborious step-by-step computation.

A generating function can turn the recurrence into a single algebraic equation. Solving that equation may give an exact formula for every term and, just as importantly, a clear description of how the terms grow.

## Tilings give a recurrence

Imagine a row of n unit cells to be tiled using one-cell squares and two-cell dominoes. Let t-n count the tilings. An empty row has one tiling, so t-zero is one. A one-cell row also has one tiling. For a longer row, inspect the first tile. If it is a square, the remainder is a row of n minus one cells. If it is a domino, the remainder is a row of n minus two cells. These cases are disjoint and exhaustive. Therefore t-n equals t at n minus one plus t at n minus two for n at least two.

The first values are one, one, two, three, five, eight. The same recurrence produces the Fibonacci numbers, but with a shifted index. Calling a sequence Fibonacci-like does not supply a proof; the first-tile argument supplies a combinatorial reason for the recurrence.

## Encode the rule in one equation

Let T of x be the sum of t-n times x to the n, beginning at n equals zero. Multiply the recurrence by x to the n and sum over n at least two. The left side becomes T minus t-zero minus t-one x. The first shifted sum on the right becomes x times T minus x times t-zero. The second becomes x squared times T.

Substituting the initial values gives T minus one minus x equals x T minus x plus x squared T. The x terms cancel, leaving T times one minus x minus x squared equal to one. Therefore T equals one divided by one minus x minus x squared.

That rational function encodes every tiling count. The denominator records the recurrence coefficients. The numerator records the initial conditions. This separation is especially useful when we change the starting values without changing the recurrence rule.

The Fibonacci sequence itself, conventionally beginning with F-zero equals zero and F-one equals one, has generating function x divided by one minus x minus x squared. The two sequences differ by one index, exactly as their initial conditions suggest.

## Solving the recurrence with roots

Try a solution of the form r to the n for the recurrence a-n equals a at n minus one plus a at n minus two. Substitution gives r squared equals r plus one. There are two roots, phi equal to one plus square root of five over two, and psi equal to one minus square root of five over two. Any linear combination of phi to the n and psi to the n obeys the recurrence. The two initial conditions determine the coefficients.

For Fibonacci numbers, the result is F-n equals phi to the n minus psi to the n, divided by square root of five. This is an exact identity, often called Binet's formula. It looks surprising because it produces integers from irrational powers. The recurrence and starting values ensure that exact cancellation occurs.

The expression also shows the growth. Phi is about one point six one eight, while the absolute value of psi is less than one. As n increases, psi to the n approaches zero. So F-n is asymptotic to phi to the n divided by square root of five. The ratio of successive nonzero terms approaches phi. The recurrence, the rational generating function, and the growth estimate are three views of the same structure.

## General linear recurrences

Suppose a-n equals c-one times a at n minus one, through c-k times a at n minus k, with constant coefficients, once n is at least k. The same summation strategy gives a rational generating function whose denominator is one minus c-one x minus c-two x squared and so on through c-k x to the k. Its numerator is a polynomial determined by the initial values.

The roots of the characteristic polynomial explain the solutions. Distinct characteristic roots produce terms proportional to their n-th powers. Repeated roots require extra factors that are polynomials in n. For instance, the recurrence a-n equals two a at n minus one minus a at n minus two has characteristic polynomial r minus one squared. The general solution is A plus B times n. Check it directly: the second finite difference of a linear function of n vanishes.

This matters when analyzing growth. A repeated dominant root can introduce factors such as n times r to the n. Merely identifying the largest root without checking multiplicities may miss the correct asymptotic factor.

## A different kind of recurrence: branching structure

Not every recurrence is linear. Let C-n count rooted full binary tree shapes with n internal nodes, where each internal node has an ordered left and right subtree. There is one empty tree, so C-zero is one. A nonempty tree has a root, a left subtree with k internal nodes, and a right subtree with n minus one minus k internal nodes. Summing over k gives C-n equals the convolution of C-k and C at n minus one minus k.

The generating function C of x therefore satisfies C equals one plus x times C squared. Rearranging gives a quadratic equation for C. Its formal-power-series solution with constant term one is the quantity one minus the square root of one minus four x, divided by two x. The other algebraic root does not have a formal power-series expansion with the required constant term.

Extracting coefficients yields the Catalan numbers: C-n equals one over n plus one times the binomial coefficient two n choose n. Their initial values are one, one, two, five, fourteen. A Catalan sequence grows on the scale of four to the n divided by n to the power three halves, with a constant factor. The contrast with Fibonacci's phi to the n is instructive: the branching tree recurrence creates a different functional equation, a different singularity, and a different growth rate.

The exact asymptotic claim is more advanced than the coefficient calculation. It follows from a standard estimate for the central binomial coefficient. We do not need to pretend it follows just by looking at the first few terms.

## When the technique is appropriate

A recurrence can be a constructive counting proof, a computational procedure, or an algebraic identity. Generating functions connect those roles. Rational generating functions are characteristic of constant-coefficient linear recurrences. Nonlinear structural recurrences may produce algebraic generating functions instead. Neither type requires analytic convergence merely to justify coefficient manipulations.

When we do want growth estimates, however, it becomes useful to treat the series as analytic functions and study where they become singular. That is a separate analytical step, and its hypotheses matter. For now, the central lesson is that an infinite collection of local equations can be turned into a finite algebraic relation. A recurrence tells us how a sequence is assembled; its generating function lets us reason about the whole assembly at once.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For \(t_0=t_1=1\), \(t_n=t_{n-1}+t_{n-2}\) for \(n\ge2\),
\[
T(x)=\sum_{n\ge0}t_nx^n=\frac1{1-x-x^2}.
\]
For Fibonacci numbers \(F_0=0,F_1=1\):
\[
F(x)=\frac{x}{1-x-x^2},\qquad
F_n=\frac{\varphi^n-\psi^n}{\sqrt5},
\quad \varphi=\frac{1+\sqrt5}{2},\quad \psi=\frac{1-\sqrt5}{2}.
\]

The recurrence \(a_n=\sum_{j=1}^kc_j a_{n-j}\) yields a rational generating function with denominator \(1-\sum_{j=1}^kc_jx^j\).

For Catalan numbers,
\[
C_0=1,\quad C_n=\sum_{k=0}^{n-1}C_kC_{n-1-k},\quad
C(x)=1+xC(x)^2,\quad C_n=\frac1{n+1}{2n\choose n}.
\]
A standard Stirling approximation gives \(C_n\sim 4^n/(\sqrt\pi\,n^{3/2})\).

### Exercises with answers

1. Count tilings of a length-four board by squares and dominoes. **Answer:** five.
2. What are the first four Fibonacci numbers? **Answer:** \(0,1,1,2\) with the chosen indexing.
3. Solve \(a_n=2a_{n-1}-a_{n-2}\), \(a_0=2\), \(a_1=5\). **Answer:** \(a_n=2+3n\).
4. Compute \(C_3\) from its recurrence. **Answer:** \(C_0C_2+C_1C_1+C_2C_0=2+1+2=5\).

### Reading

MIT 6.042J, *Mathematics for Computer Science*, recurrences and generating functions; Herbert S. Wilf, *generatingfunctionology*, rational generating functions and recurrences.
