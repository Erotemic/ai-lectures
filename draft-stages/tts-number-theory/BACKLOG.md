# Number theory foundations: coverage and next steps

**Status, 2026-11-16:** ten indexed and substantive spoken lectures. The first six establish elementary number theory; this continuation adds the four proofs and bridges below. The purpose is to supply tangible prerequisites for abstract algebra, algorithms, analytic methods and further integer equations, not to expand the course by repetition.

## Delivered foundation, lectures 001000–006000

1. Divisibility, Euclidean algorithm, Bézout identity, prime factorization.
2. Congruences, inverses, Chinese remainder theorem with noncoprime compatibility.
3. Unit groups, Euler's theorem, multiplicative order, pseudoprimes.
4. Diophantine equations, GCD solvability, modular obstructions, primitive Pythagorean triples.
5. Continued fractions, convergents, Pell examples, multiplicative norms.
6. Quadratic residues, Legendre symbol, Euler's criterion, negative-one law; reciprocity *stated* as motivation.

## Delivered in this continuation, lectures 007000–010000

7. **Complete quadratic reciprocity proof:** Gauss's lemma, odd-multiplier floor formula, lattice rectangle; supplementary law for two is also proved. The theorem for composite denominators is not asserted without qualification.
8. **Arithmetic functions and Möbius inversion:** finite convolution algebra, inversion proof, totient formula, visible lattice-point count; the density limit 6/pi-squared is labeled a later analytic result.
9. **Elementary prime distribution:** infinitely many primes in both odd classes modulo four; finite Euler products and divergence of prime reciprocals; binomial upper estimate; density zero. The prime number theorem and general Dirichlet theorem are carefully labeled *unproved*.
10. **Prime powers and Hensel lifting:** proof of the unique simple-root lift, worked 7-adic square-root corrections, unit-square-root classification for odd primes, derivative-zero counterexamples, CRT reduction.

## Priorities for the next continuation

- **011000 — The full Pell theorem and quadratic irrationality.** Prove periodicity of continued fractions for square roots and relate primitive solutions to fundamental units; distinguish constructing some solutions (005000) from classifying all positive solutions. This may be split if a complete proof needs it.
- **012000 — Sum of two squares and Gaussian integers.** Complete the converse of the negative-one test: odd prime p is a sum of two squares iff p is one modulo four; state and prove the role of Euclidean division in Z[i], then explain precisely where element factorization could fail in other quadratic rings.
- **013000 — Testing primality versus factoring.** Sieve, modular exponentiation, Miller–Rabin with correct witness guarantees, deterministic verification by certificates, computational complexity limits. The course needs proof of the algorithmic claim rather than a tool catalog.
- **014000 — Finite fields and primitive roots.** Develop polynomial root bounds, finite multiplicative groups, order, cyclicity for prime fields, and CRT for prime-power units, bridging to abstract algebra.
- **015000 — Estimation, series, and analytic number theory primer.** Develop logarithms, convergence, summation by parts, comparison estimates, and sufficient prerequisites for Dirichlet characters and deeper prime-distribution theorems.

## Integration notes and boundaries

Keep all content in `draft-stages/tts-number-theory/` and use unused stable six-digit IDs. Preserve one spoken region per source manuscript, display-only exact mathematical notation, claim-level references where consequential, relevant Wikipedia orientation links, and track-local metadata. Length is governed by mathematics and comprehension; descriptive word counts are not goals. No repository-wide refactor or testing is necessary for a source-only continuation. This pack owns its `track.json` and `metadata/sources.json` but does not change any other track.
