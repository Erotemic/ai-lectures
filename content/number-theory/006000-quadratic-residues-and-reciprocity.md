# 006000 — Quadratic Residues and the Reciprocity Puzzle

**Track:** Number Theory from First Principles. **Background:** modular arithmetic, prime factorization, Fermat's little theorem. **Theme:** predicting which congruences have square roots.

<!-- BEGIN SPOKEN LECTURE -->

# Quadratic Residues and the Reciprocity Puzzle

Which numbers are perfect squares modulo seven? Squaring one gives one, squaring two gives four, and squaring three gives nine, or two modulo seven. Squaring four gives sixteen, again two; squaring five gives four; squaring six gives one. Among the nonzero classes modulo seven, precisely one, two, and four can be squares.

So the equation x squared congruent to three modulo seven has no solution. The equation x squared congruent to two modulo seven does have solutions: three and four both work. We have learned something exact about integers by exploring a tiny finite universe. The subject of quadratic residues asks how far these observations can be organized into a general theory.

The central mystery is not merely whether a class is a square modulo one prime. It is how to compare two different primes. When does a prime p behave like a square modulo another prime q, and what does that tell us about q modulo p? The quadratic reciprocity theorem gives a remarkably compact relationship. We will build the definitions, prove an important test, work through examples, and state clearly where the deeper reciprocity proof begins.

## The squares modulo an odd prime

Fix an odd prime p. Every nonzero residue modulo p has an inverse. When can two different nonzero numbers have the same square? If x squared equals y squared modulo p, subtract to obtain x minus y times x plus y congruent to zero. A prime dividing a product divides at least one factor. Therefore x is congruent to y or to negative y modulo p.

Thus each nonzero square is produced by exactly two inputs, x and negative x. They are distinct because p is odd and x is nonzero. There are p minus one nonzero inputs, paired into groups of two. So exactly half the nonzero residue classes are squares. The other half are nonsquares.

This counting argument is already a proof, not merely a pattern noticed in a table. For p equal to seven, the three nonzero square classes are one, two, and four. For p equal to eleven, they are one, three, four, five, and nine. The lists differ, but their sizes follow the same theorem.

A nonzero class that can be written as a square modulo p is called a quadratic residue. A nonzero class that cannot is a quadratic nonresidue. Zero is treated separately, because it is the square of zero but is not part of the multiplicative group of nonzero classes.

The language lets us turn an equation into a yes-or-no question. To ask whether x squared congruent to a modulo p is solvable is exactly to ask whether a is a quadratic residue or zero.

## A three-valued symbol

For an odd prime p, the Legendre symbol records this information. It is zero when p divides a, one when a is a nonzero square modulo p, and negative one when a is a nonsquare. The symbol is compact, but its definition is completely elementary.

For p equal to seven, the Legendre symbol for two is one, because three squared is two modulo seven. The symbol for three is negative one, because no nonzero square is congruent to three. The symbol for seven is zero, because seven is divisible by seven.

There is also a multiplication rule. If a and b are nonzero square classes, their product is a square. A square times a nonsquare is a nonsquare: otherwise multiplying by the inverse of the square would make the original nonsquare a square. And a nonsquare times a nonsquare is a square. The last fact follows because the squares form a subgroup of index two among the nonzero classes, or can be established by a counting argument using multiplication by one chosen nonsquare.

Consequently the Legendre symbol of a times b equals the product of their Legendre symbols. This makes the symbol useful for decomposing a complicated number into factors.

## A power test with a proof

Euler's criterion says that for a nonzero residue a modulo an odd prime p, raising a to the power p minus one divided by two gives one if a is a square, and negative one if it is a nonsquare.

First suppose a equals x squared modulo p for some nonzero x. Raise a to the half-exponent. The result is x raised to p minus one. Fermat's little theorem says that is one. So every nonzero square passes the positive test.

Now suppose we have a nonzero number whose half-exponent gives one. We want to show it is a square; otherwise the power test would be incomplete. Consider the polynomial whose value at t is t raised to the half-exponent minus one, working modulo p. A nonzero polynomial of degree d over a field has at most d distinct roots. The half-exponent is d equal to p minus one over two. But we have already found exactly d nonzero square classes, and each is a root. They exhaust the roots of that polynomial. Thus no nonsquare can give one.

Finally, Fermat's theorem says a raised to p minus one equals one, so the half-exponent result is a square root of one. In a field of odd characteristic, the only such roots are one and negative one: subtract one and factor. Since nonsquares cannot give one, they must give negative one. That completes Euler's criterion.

This proof brings several foundations together. The count of square classes uses unique factorization-like divisibility in a prime modulus. The root bound comes from polynomial division over a field. Fermat's theorem supplies the power constraint. We have not invoked mysterious machinery; every premise has an understandable job.

## A useful test for negative one

Does there exist a number whose square is negative one modulo p? Euler's criterion gives a complete answer for every odd prime. Apply it to a equal to negative one. Raising negative one to the half-exponent produces one exactly when that exponent is even, and negative one when it is odd. Therefore negative one is a quadratic residue modulo p precisely when p is congruent to one modulo four.

For example, modulo five, two squared is four, or negative one. Five is one modulo four. Modulo seven, negative one is six, and six is not a square; seven is three modulo four. This theorem explains a recurring distinction between primes that leave remainder one or three when divided by four.

The result will later help us study whether primes can be represented as sums of two squares. If an odd prime p equals a squared plus b squared, and p does not divide b, then the ratio a over b has square equal to negative one modulo p. Thus p must be one modulo four. Proving the converse—that every prime congruent to one modulo four is a sum of two integer squares—takes additional work. Our congruence argument establishes the necessary condition, not the complete theorem.

## Reciprocity: comparing two different primes

Now let p and q be distinct odd primes. There are two questions: is p a square modulo q, and is q a square modulo p? They look unrelated. Their square lists live in different arithmetic systems. Yet quadratic reciprocity says the answers agree unless both primes are congruent to three modulo four, in which case they are opposite.

In the language of Legendre symbols, the product of the symbol for p modulo q and the symbol for q modulo p equals negative one raised to the product of half of p minus one and half of q minus one. The exponent is odd exactly when both primes are three modulo four.

Take p equal to three and q equal to eleven. Modulo eleven, three is a square, since five squared is twenty-five, or three modulo eleven. So the symbol for three modulo eleven is one. Modulo three, eleven behaves like two, which is not a square, since the only nonzero square class is one. The other symbol is negative one. They are opposite, exactly as predicted because both primes are three modulo four.

For an example with agreement, take p equal to five and q equal to eleven. Five is a square modulo eleven, since four squared is sixteen, or five modulo eleven. Eleven behaves like one modulo five, which is a square. Both symbols are one. Since five is one modulo four, reciprocity predicts agreement.

These examples are checks, not proofs of the theorem. The general reciprocity law is a deeper result. One classical route uses Gauss's lemma, which turns a Legendre symbol into the parity of a count of negative representatives among certain multiples. Comparing lattice counts in a rectangle then yields the reciprocity sign. A full proof must establish Gauss's lemma and count carefully; we are not claiming to have proved the complete law from two examples.

## What the theorem makes computable

Suppose you want to decide whether an integer a is a square modulo a large odd prime p. You could test all possible squares, but that requires time proportional to p. Euler's criterion provides an exponentiation test. Quadratic reciprocity offers another kind of reduction: factor a, use multiplicativity of the Legendre symbol, switch two prime arguments when appropriate, and reduce to smaller residues. Together with special evaluations for negative one and two, this leads to fast symbolic calculations.

But there is a trap when the modulus is composite. The Jacobi symbol extends Legendre's notation to an odd positive composite denominator by multiplying symbols over its prime factorization. A Jacobi symbol equal to negative one proves that a is not a square modulo the composite modulus, but a Jacobi symbol equal to one does not ensure that it is a square.

For example, two has Legendre symbol negative one modulo three and also negative one modulo five. Their product is one, so the Jacobi symbol of two over fifteen is one. Yet two is not a square modulo three, and therefore cannot be a square modulo fifteen. This is a precise example of information lost when two signs are multiplied together.

The distinction matters in computational number theory. A compact symbol or a passing test can be useful without being a complete answer to a decision problem. Mathematical maturity includes learning what information a test certifies and what it leaves unresolved.

## Where the foundations lead

We started by listing the squares on a seven-hour arithmetic clock. That yielded a theorem counting exactly half the nonzero classes as quadratic residues. We then proved Euler's criterion from Fermat's theorem and a polynomial root bound, obtained a complete test for whether negative one is a square, and encountered quadratic reciprocity as a precise new relationship between different primes.

The next natural questions include a complete proof of reciprocity, the special law for two, prime representation by quadratic forms, and what changes when square roots are sought modulo prime powers rather than primes. They lead toward algebraic number theory, finite fields, and algorithms for finding modular square roots.

The foundational habit remains the same: ask exactly which arithmetic world we are in, state the hypothesis on the modulus, and distinguish testing a possible solution from proving that a solution exists. A very small question—can this number be a square on this clock?—has opened a path to one of the central theorems of classical number theory.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

### Core definitions and results

For an odd prime \(p\), let \(\left(\frac ap\right)\) denote the Legendre symbol, defined as \(0\) if \(p\mid a\), \(+1\) if \(a\not\equiv0\) is a square \(\pmod p\), and \(-1\) otherwise. Among the \(p-1\) nonzero classes, exactly \((p-1)/2\) are squares.

Euler's criterion is

\[
a^{(p-1)/2}\equiv\left(\frac ap\right)\pmod p
\qquad(p\nmid a).
\]

For nonzero \(a,b\), the symbol is multiplicative. The first supplementary law is

\[
\left(\frac{-1}{p}\right)=(-1)^{(p-1)/2}.
\]

For distinct odd primes \(p,q\), the quadratic reciprocity theorem is

\[
\left(\frac pq\right)\left(\frac qp\right)=(-1)^{\frac{p-1}{2}\frac{q-1}{2}}.
\]

**Proof status:** the spoken lecture proves the count, Euler's criterion, and the negative-one test. It **states but does not prove** full quadratic reciprocity. A proof via Gauss's lemma and lattice counts is a future deepening, not an implicit prerequisite silently assumed proved.

The Jacobi symbol \(\left(\frac a n\right)\) for odd composite \(n=\prod p_i^{e_i}\) is \(\prod_i\left(\frac a{p_i}\right)^{e_i}\). In particular \(\left(\frac{2}{15}\right)=(-1)(-1)=1\), although \(x^2\equiv2\pmod{15}\) is unsolvable.

### Practice and reasoning checks

1. List the nonzero square classes modulo thirteen. Verify there are six.
2. Prove that a quadratic residue times a nonresidue is a nonresidue, using inverses.
3. Use Euler's criterion to decide whether negative one is a square modulo seventeen and modulo nineteen.
4. Verify the reciprocity sign for primes three and seven, computing both Legendre symbols explicitly.
5. Explain why the Jacobi symbol example modulo fifteen is not a contradiction of quadratic reciprocity.

### Sources and further reading

- MIT OpenCourseWare, *18.781 Theory of Numbers*, lectures 9–11: quadratic residues, quadratic reciprocity, Jacobi symbols: https://ocw.mit.edu/courses/18-781-theory-of-numbers-spring-2012/pages/lecture-notes/
- William Stein, *Elementary Number Theory: Primes, Congruences, and Secrets*, chapter on quadratic reciprocity: https://www.wstein.org/ent/
- Wikipedia background: [Quadratic residue](https://en.wikipedia.org/wiki/Quadratic_residue), [Euler's criterion](https://en.wikipedia.org/wiki/Euler%27s_criterion), [Quadratic reciprocity](https://en.wikipedia.org/wiki/Quadratic_reciprocity), [Jacobi symbol](https://en.wikipedia.org/wiki/Jacobi_symbol).
