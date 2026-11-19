# 031250 — Local Squares and the Limits of Local Solvability

**Track:** Number Theory from First Principles. **Background:** quadratic residues, finite-field cyclic groups, 031000 (Hensel), and rational squares. **Aim:** classify squares in Q_p including p=2, apply valuations to solvability, and distinguish local conditions from rational solutions.

<!-- BEGIN SPOKEN LECTURE -->

# Local Squares and the Limits of Local Solvability

A rational number can fail to be a square for more than one reason. Negative numbers cannot be squares in the real numbers. Three cannot be the square of a rational number because its prime factorization contains an odd exponent. And in a p-adic field, even when the valuation has the right parity, a unit may fail to be a square because of its residue modulo p.

The goal is to turn these observations into a complete test: given a nonzero p-adic number, can we decide whether it is a square? We will first handle odd primes, then the prime two. That distinction is not cosmetic. At odd primes, a root of x squared minus u is simple whenever u is a unit. At the prime two, its derivative is always divisible by two, so the simple-root theorem cannot be used in that form.

Along the way, this classification will explain familiar quadratic reciprocity phenomena and show why solving equations in every p-adic field is both powerful and, sometimes, insufficient to solve them over the rationals.

## First remove the valuation

Take a nonzero x in Q-p. It can be written uniquely as p to an integer power k times a p-adic unit u. If x equals y squared, then its valuation is twice the valuation of y, so k is even. That is a necessary condition for being a square, for every prime p.

If k is even, divide x by p to the k. Multiplication or division by the square p to the k does not change whether a square root exists. The whole question reduces to whether the *unit* u has a square root in Z-p.

That separates two obstructions. The first comes from the exponent of p. The second comes from the remaining unit. A complete answer needs both; checking only congruences for x without first separating its valuation can lead to confusion, especially for elements with negative valuation.

## At an odd prime, the first residue decides

Suppose p is odd and u is a p-adic unit. If u is a square in Q-p, then reducing a square root modulo p shows that the first residue of u must be a square in the finite field with p elements. That proves necessity.

For sufficiency, suppose a is a nonzero solution of a squared equals u modulo p. Consider f of X equals X squared minus u. Its derivative at a is two a. Because p is odd and a is nonzero modulo p, two a is a unit. Hensel's lemma lifts a uniquely to an exact p-adic square root of u.

So, for odd p, a nonzero p-adic number is a square precisely when its valuation is even and its unit part is a quadratic residue modulo p. This is the complete square criterion. It is often much easier to test than a direct search for p-adic roots.

For example, six has a square root in Q-five. Its five-adic valuation is zero, and six reduces to one modulo five, a nonzero square. Hensel lifts both residues one and negative one to roots of x squared equals six. But six is not a rational square. A solution in one completion is not a rational solution.

What about negative one? In a field of odd prime order, the nonzero elements form a cyclic group of order p minus one. Negative one is a square exactly when that order is divisible by four, so precisely when p is congruent to one modulo four. Thus negative one has a p-adic square root for odd p congruent to one modulo four, and has none for odd p congruent to three modulo four.

This is also an explanation of splitting for the Gaussian integers. For an odd prime p, the polynomial X squared plus one factors into distinct linear factors modulo p precisely when negative one is a square there. Those roots lift to Q-p, and the same criterion decides whether p splits into two prime ideals in the field Q of i. The local arithmetic is revealing the same distinction that global ideal factorization revealed earlier.

## The prime two requires an extra level of precision

For two-adic units, reduction modulo two cannot distinguish any odd unit from another: every unit has residue one. The derivative of X squared minus u at an odd x is two x, which is never a two-adic unit. So the first residue and the simple-root theorem give no answer.

But look modulo eight. The square of every odd integer is congruent to one modulo eight. To see this, write the odd integer as one plus two k. Its square is one plus four k times k plus one. Because k and k plus one are consecutive integers, their product is even, so the last term is divisible by eight. This proves that every odd two-adic square is congruent to one modulo eight.

A surprise is that the condition is also sufficient. Suppose u is an odd two-adic integer congruent to one modulo eight. Set f of X equal to X squared minus u, and start at a equal to one. The error f of one is divisible by eight, so its two-adic valuation is at least three. The derivative at one is two, of valuation one. The stronger Hensel condition asks that the error valuation be strictly greater than twice the derivative valuation. Three is greater than two. Therefore a genuine two-adic square root exists.

Thus an odd two-adic unit is a square if and only if it is congruent to one modulo eight. Combined with the valuation parity test, this classifies *all* nonzero squares in Q-two. No exception remains for negative valuations, because we already factored out an even power of two.

Seventeen is a two-adic square because seventeen is one modulo eight. Negative one is not, because negative one is seven modulo eight. Five is not, because five is five modulo eight. And nine is a two-adic square, as it should be, since it is literally three squared.

At this stage we can count square classes. For odd p, an element is determined up to a square by the parity of its valuation and by whether its unit residue is a square or nonsquare. That gives four classes. For p equal to two, the parity of the valuation gives two choices and the odd unit's residue modulo eight gives four choices. That gives eight classes. These finite square-class groups will become basic data for local quadratic forms and Hilbert symbols.

## A local obstruction to an equation in two variables

Consider the equation x squared plus y squared equals three, with x and y rational. It has no rational solution. The three-adic viewpoint gives a decisive obstruction without an exhaustive search over rational numerators and denominators.

Suppose x and y are three-adic numbers, not both zero. Let m be the smaller of their valuations. Factor three to the m out of x and y. At least one remaining number is a three-adic unit. Now reduce the squares of those remaining numbers modulo three. A unit square is one modulo three; a nonunit square is zero. Therefore their sum is either one or two modulo three, never zero. There can be no cancellation of the lowest valuation term.

It follows that the three-adic valuation of x squared plus y squared is exactly twice m, an even integer. But the valuation of three is one, which is odd. Contradiction. There is no solution even in Q-three, so there certainly cannot be one in the smaller field Q.

This reasoning still works if x or y has a power of three in its denominator. That is an important advantage of phrasing the obstruction in Q-three rather than testing only integer solutions modulo three.

We can reverse the perspective. If a rational equation has a rational solution, then the same coordinates give a solution over the real numbers and over every Q-p, because the rationals embed in all of these fields. So local solvability everywhere is a *necessary* condition for rational solvability. Finding even one obstructing place proves impossibility over Q.

## When is local solvability sufficient?

For a single rational number r, being a square at every place is sufficient. Suppose r is a square in the real numbers and in every Q-p. The real condition says r is positive. The p-adic condition says the valuation of r at every prime is even. In the prime factorizations of the numerator and denominator of r, every prime exponent is therefore even. Both numerator and denominator are perfect squares, so r is a rational square. We have proved this local-to-global statement directly, without a deep theorem.

The situation is richer for systems of quadratic equations or for higher-degree polynomials. A celebrated theorem of Hasse and Minkowski says that a homogeneous quadratic form with rational coefficients has a nontrivial rational zero if and only if it has a nontrivial zero over the reals and over Q-p for every prime. We are *not* proving that theorem here; it requires additional work on local quadratic forms and the relations among their invariants.

Nor can we replace the word quadratic with an arbitrary degree. Selmer established that the homogeneous cubic equation three x cubed plus four y cubed plus five z cubed equals zero has nontrivial real and p-adic solutions for every prime, yet no nontrivial rational solution. The proof of that fact is outside this lecture. Its lesson is that checking all completions can leave a genuine global obstruction unseen.

There is a hierarchy here. Congruence obstructions are relatively accessible. P-adic completion makes every level of prime-power congruence information available in a single field. Hensel lifting explains how simple solutions persist through those levels. Local-global theorems ask whether solutions from the various completions can be assembled into one rational solution. Sometimes they can, as for a single rational square and for quadratic forms. Sometimes they cannot, as the cubic example demonstrates.

We now have exact square tests and a method for detecting local impossibility. To connect these ideas more closely with prime splitting in number fields, the next natural step is to build finite extensions of Q-p and inspect their residue fields and ramification. There the single valuation of Q-p acquires new uniformizers and new finite residue fields, making the global behavior of primes visible locally.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For x∈Q_p^× write x=p^k u with k∈Z and u∈Z_p^×.

### Classification of squares

**Odd p:** \(x\in (Q_p^\times)^2\) iff \(k\) is even and \(\bar u\in\mathbb F_p^\times\) is a square. Necessity by valuation and reduction; sufficiency by the simple-root Hensel lemma applied to X²-u.

**p=2:** \(x\in(Q_2^\times)^2\) iff \(k\) is even and \(u\equiv1\pmod8\). Necessity: every odd square is 1 mod8. Sufficiency: apply strong Hensel to f(X)=X²-u at a=1: \(v_2(f(1))\ge3>2v_2(f'(1))=2\).

Square-class groups:

\[
|Q_p^\times/(Q_p^\times)^2|=\begin{cases}4,&p\text{ odd},\\8,&p=2.\end{cases}
\]

For odd p, representatives are 1, ε, p, pε where ε is a nonsquare unit. For p=2, representatives are 1,3,5,7,2,6,10,14.

### Local examples

- 6 is a square in Q_5 since v_5(6)=0 and 6≡1 mod5.
- -1 is a square in Q_p for odd p iff p≡1 mod4, by cyclicity of F_p^×; it is not a square in Q_2.
- 17 is a square in Q_2; 5 is not.
- In Q_3, \(v_3(x^2+y^2)=2\min(v_3(x),v_3(y))\) whenever (x,y)≠(0,0), because -1 is nonsquare modulo 3. Hence x²+y²=3 has no Q_3-solutions.

### Local-to-global distinctions

1. If r∈Q^× is a square in R and every Q_p, then r>0 and v_p(r) is even for every prime, so r∈Q². This particular statement is proved.
2. **Hasse–Minkowski:** A homogeneous rational quadratic form is isotropic over Q iff it is isotropic over R and over every Q_p. **Cited, not proved here.**
3. **Selmer's cubic:** 3X³+4Y³+5Z³=0 has nonzero points over R and every Q_p but none over Q. **Cited, not proved here.** Its projective interpretation matters: the zero vector is always a trivial solution to a homogeneous equation.

### Exercises

1. Classify all squares among 2, 3, 5, 6, 9, 17 in Q_2 and Q_5.
2. Prove the four square classes for odd p and the eight for p=2.
3. Derive the valuation obstruction for x²+y²=3 in Q_3, allowing nonintegral x and y.
4. Explain why -1 being a p-adic square for odd p is equivalent to p splitting in Q(i).
5. Prove the local-to-global result for a rational being a square without using quadratic reciprocity.

### Reading and source notes

- Keith Conrad, [Hensel's Lemma](https://kconrad.math.uconn.edu/blurbs/gradnumthy/hensel.pdf), square-root examples and strengthened lifting.
- Keith Conrad, [The Local-Global Principle](https://kconrad.math.uconn.edu/blurbs/gradnumthy/localglobal.pdf), local rational powers, Hasse–Minkowski context, Selmer counterexample.
- Wikipedia: [Quadratic residue](https://en.wikipedia.org/wiki/Quadratic_residue), [p-adic number](https://en.wikipedia.org/wiki/P-adic_number), [Hasse principle](https://en.wikipedia.org/wiki/Hasse_principle), [Hasse–Minkowski theorem](https://en.wikipedia.org/wiki/Hasse%E2%80%93Minkowski_theorem).
