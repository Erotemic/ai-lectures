# Number theory foundations: coverage and next steps

**This continuation:** launch a standalone, undergraduate-entry course with six complete lectures. The goal is to make arithmetic arguments transparent to listeners who know basic algebra but have not studied abstract algebra. The course also supplies specific prerequisites for `abstract-algebra`, `discrete-mathematics`, `algorithms-computability-complexity`, `logic-types`, and computational mathematics.

## Delivered in the current pack

1. Divisibility, Euclidean algorithm, Bézout's identity, Euclid's lemma, unique prime factorization and infinitude of primes.
2. Congruence, modular inverse, linear congruences and the Chinese remainder theorem, including noncoprime compatibility.
3. Multiplicative units, totient, Euler/Fermat, order, pseudoprimes and the correctness (not security) of modular exponentiation used by RSA.
4. Integer equations, GCD solvability, modular obstructions, primitive Pythagorean triples and rational parametrization.
5. Continued fractions as a Euclidean algorithm, convergents, approximation error, Pell's equation for D=2 and multiplicative norms.
6. Quadratic residues, Legendre symbol, Euler's criterion, the -1 supplementary law and a worked introduction to quadratic reciprocity (which is explicitly **stated, not yet proved**).

## Prioritized next content

- **007000. A complete proof of quadratic reciprocity.** Build Gauss's lemma with an example, count lattice points and carry out the sign argument. Add the complementary law for 2 with its proof, not only its statement. This is the most important proof debt from 006000.
- **008000. Arithmetic functions and Möbius inversion.** Multiplicative functions, divisor sums, Dirichlet convolution, inversion proof, counting coprime pairs, link to inclusion-exclusion and generating functions.
- **009000. Prime distribution from elementary arguments.** Infinite primes in congruence classes in tractable cases, Euler product intuition with convergence qualifications, Chebyshev-type estimates, what the prime number theorem adds, and what is not being proved.
- **010000. Prime powers and lifting.** Units modulo prime powers, lifting solutions and Hensel's lemma with exact derivative conditions, modular square roots.
- **011000. The full Pell theorem and quadratic forms.** Periodicity of quadratic-irrational continued fractions, fundamental solutions, classification of positive solutions, Gaussian integers and a rigorous two-squares theorem.
- **012000. Primality and factorization algorithms.** Sieve, modular exponentiation, Miller–Rabin assumptions and guarantees, certificates, complexity comparisons. Keep probability and adversary assumptions explicit.

## Boundaries and overlap

`abstract-algebra/004000` already introduces integer divisibility together with rings, polynomial factorization and fields. This number-theory course develops divisibility as a standalone proof chain and continues toward integer equations and rational approximation. It does not replace the ring-theoretic lectures. Existing algorithms and complexity courses can use these examples without duplicating their formal machine models. These are teaching links, not formal proof dependencies.

For all new lectures, preserve one canonical spoken region, readable display-only mathematics, per-lecture source metadata, Wikipedia orientation links, and no fixed word or runtime target. A theorem named in a lecture is not thereby proved; keep exact proof status explicit.
