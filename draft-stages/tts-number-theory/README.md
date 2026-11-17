# Number Theory from First Principles

A proof-driven course connecting integer arithmetic with algorithms, algebraic structure, and analytic number theory. It starts with gcds, congruences, integer equations, reciprocity, and finite fields, and develops the analytic machinery required for a **complete proof of Dirichlet's theorem** and elementary **Chebyshev prime-counting bounds**. The course currently contains **27 substantive lectures**.

The opening lectures assume only integer arithmetic, fractions, elementary algebra, and a willingness to follow proofs. Later lectures build their own analysis and character foundations rather than presupposing advanced number theory. Each manuscript has one extractable spoken lecture and a display-only mathematical companion with worked equations, exercises, claim-level reading records, and Wikipedia references. Length and word counts describe the manuscripts; they are not duration targets.

## Listening sequence

| ID | Lecture | Spoken words (measured) |
|---|---|---:|
| `001000` | [Divisibility, Euclid's Algorithm, and the Architecture of Prime Factorization](001000-divisibility-euclid-and-unique-factorization.md) | 1,942 |
| `002000` | [Congruences, Inverses, and the Chinese Remainder Theorem](002000-congruences-inverses-and-the-chinese-remainder-theorem.md) | 1,770 |
| `003000` | [Units, Euler's Theorem, and Multiplicative Order](003000-units-eulers-theorem-and-multiplicative-order.md) | 1,603 |
| `004000` | [Integer Equations, Rational Points, and Pythagorean Triples](004000-diophantine-equations-and-pythagorean-triples.md) | 1,899 |
| `005000` | [Continued Fractions, Rational Approximation, and Pell Equations](005000-continued-fractions-and-pell-equations.md) | 1,763 |
| `006000` | [Quadratic Residues and the Reciprocity Puzzle](006000-quadratic-residues-and-reciprocity.md) | 1,885 |
| `007000` | [Gauss's Lemma and a Complete Proof of Quadratic Reciprocity](007000-gauss-lemma-and-proof-of-quadratic-reciprocity.md) | 1,975 |
| `008000` | [Arithmetic Functions, Dirichlet Convolution, and Möbius Inversion](008000-arithmetic-functions-and-mobius-inversion.md) | 2,049 |
| `009000` | [Where the Primes Live: Elementary Distribution Arguments](009000-where-primes-live-elementary-distribution.md) | 2,102 |
| `010000` | [Prime Powers, Simple Roots, and Hensel Lifting](010000-prime-powers-and-hensel-lifting.md) | 2,127 |
| `011000` | [Periodic Continued Fractions and the Complete Pell Theorem](011000-periodic-continued-fractions-and-the-pell-theorem.md) | 2,150 |
| `012000` | [Gaussian Integers and the Two-Squares Theorem](012000-gaussian-integers-and-two-squares.md) | 2,170 |
| `013000` | [Primality Tests, Compositeness Witnesses, and Certificates](013000-primality-witnesses-and-certificates.md) | 2,291 |
| `014000` | [Finite Fields, Primitive Roots, and Unit Groups](014000-finite-fields-and-primitive-roots.md) | 2,398 |
| `015000` | [Series, Logarithms, and Summation by Parts](015000-series-logarithms-and-summation-by-parts.md) | 2,340 |
| `016000` | [Dirichlet Characters and Arithmetic Fourier Filters](016000-dirichlet-characters-and-orthogonality.md) | 2,103 |
| `017000` | [Euler Products, the Zeta Function, and Prime Weights](017000-euler-products-zeta-and-prime-weights.md) | 2,085 |
| `018000` | [Dirichlet L-Series and the Boundary of the Progression Theorem](018000-dirichlet-l-series-and-primes-in-progressions.md) | 2,202 |
| `019000` | [Crossing the Line One: Analytic Functions, Zeta, and Character Series](019000-analytic-continuation-at-the-line-one.md) | 1,670 |
| `020000` | [Complex Characters and the Positive Euler-Product Inequality](020000-complex-characters-and-nonvanishing.md) | 1,523 |
| `021000` | [Landau's Positivity Principle and the Real-Character Case](021000-landau-positivity-and-real-characters.md) | 1,658 |
| `022000` | [A Complete Proof of Dirichlet's Theorem on Primes in Progressions](022000-proof-of-dirichlets-theorem.md) | 1,877 |
| `023000` | [Chebyshev Functions and the First Serious Bounds on Prime Counts](023000-chebyshev-functions-and-prime-counting.md) | 2,284 |
| `024000` | [How Many Ways Can an Integer Be Two Squares?](024000-counting-sums-of-two-squares.md) | 1,928 |
| `024500` | [Counting Lattice Points in a Growing Circle](024500-lattice-points-and-the-gauss-circle-problem.md) | 1,887 |
| `025000` | [Constructing Finite Fields, and Proving They Are Unique](025000-constructing-and-classifying-finite-fields.md) | 2,503 |
| `025500` | [Frobenius, Subfields, and Testing Irreducibility](025500-frobenius-subfields-and-irreducibility.md) | 2,607 |

**Total:** 27 indexed lectures, **54,791 spoken words**. 

## Proven theorems and open boundaries

- **001000–006000:** Euclidean algorithm and prime factorization; CRT, order and Euler's theorem; Diophantine equations and Pythagorean triples; continued fractions; quadratic residues.
- **007000–010000:** quadratic reciprocity proved by Gauss's lemma, Dirichlet convolution and Möbius inversion, elementary prime-distribution arguments, and simple-root Hensel lifting.
- **011000–014000:** Pell equation existence and classification for positive norm-one solutions, Gaussian integers and the two-squares criterion, primality witnesses/certificates, and finite-field multiplicative groups including primitive roots.
- **015000–018000:** series and summation by parts, character construction and orthogonality, Euler products and von Mangoldt weights, and the character projection argument for primes in progressions. Lecture 018000 deliberately identifies the then-unproved general nonvanishing theorem; the gap is filled by the new sequence below.
- **019000–023000, Continuation 5:** partial-summation continuation of zeta and nonprincipal L-series to the right half-plane; full nonvanishing for nonreal characters via a trigonometric square; full nonvanishing and positivity for real characters via an explicitly proved Landau disk lemma; **unconditional proof of Dirichlet's theorem for every coprime residue and modulus**, including divergent prime reciprocals and equal Dirichlet densities; and elementary \(\psi(x)=\Theta(x)\), \(\pi(x)=\Theta(x/\log x)\) estimates using binomial coefficients.

- **024000–025500, Continuation 6:** exact signed, ordered representation count for sums of two squares and its \(r_2/4=\mathbf1*\chi_4\) formula; elementary Gauss circle lattice-point estimate \(N(R)=\pi R^2+O(R)\); existence and uniqueness of finite fields of every prime-power order; Frobenius orbits, subfield structure, exact irreducible counts, Rabin irreducibility test, and trace/norm. The refined Gauss circle error problem and the prime number theorem remain outside this proof sequence.

**Not claimed as proved:** the prime number theorem \(\pi(x)\sim x/\log x\), the prime number theorem in arithmetic progressions, zero-free vertical-line estimates for zeta and L-functions, the refined Gauss circle error problem, and the deferred topics listed in `BACKLOG.md`. A standalone complex analysis course can deepen the power-series framework used in lectures 019000–021000; their companion supplies a direct integral-expansion justification sufficient for the Landau application.

## Related tracks and attribution

The course now supplies prerequisites for abstract algebra, functional analysis, computational number theory, and further analytic number theory. Only files under this content pack are changed. Scholarly references, formal proof developments, and Wikipedia background are recorded in the pack-local `metadata/` directory, with authorship history in `provenance.yaml`. Source records distinguish citation and independent exposition from any claim of copying a proof.
