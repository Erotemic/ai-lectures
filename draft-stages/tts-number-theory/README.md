# Number Theory from First Principles

A proof-driven introduction to integer arithmetic and its deepening tools: prime factorization, congruences, Diophantine equations, rational approximation, quadratic reciprocity, divisor functions, prime distribution and lifting solutions modulo prime powers. The course now contains ten substantive lectures.

The course starts from integer arithmetic and basic algebra. Each manuscript is comprehensible at its declared background level; the sequence is useful because the proofs deliberately supply prerequisites for later entries. There is exactly one delimited TTS narration region per lecture, with the formal mathematics and practice prompts retained in display-only companions.

## Main listening sequence

| ID | Lecture | Spoken words (measured) |
| --- | --- | ---: |
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

Total: **10 lectures**, **19,115 spoken words** (measured descriptively; no length target).

## Proven results versus forward references

Lecture 006000 *states* quadratic reciprocity and proves Euler's criterion and the law for -1. Lecture 007000 **completes** the proof of quadratic reciprocity with Gauss's lemma, an odd-multiplier floor-sum identity, and an exact partition of a lattice rectangle. It also proves the supplementary law for 2. Lecture 008000 proves Möbius inversion using finite divisor sums, then derives the totient formula and an exact count of coprime lattice points. Lecture 009000 proves special cases of infinite primes in progressions, divergence of the sum of prime reciprocals, a binomial upper bound, and zero density of primes. It expressly does not prove Dirichlet's theorem or the prime number theorem. Lecture 010000 proves simple-root Hensel lifting and unit-square-root counts modulo odd prime powers, with singular and even-prime counterexamples.

## Connection to the existing library

This course complements `draft-stages/tts-abstract-algebra/004000-*`, which introduces divisibility in the language of rings. It also provides concrete prerequisites for `discrete-mathematics`, `algorithms-computability-complexity`, `logic-types`, and higher algebra/analysis courses. None of those packs is modified by this overlay.

## References and attribution

The two main open university/textbook references are [MIT OpenCourseWare 18.781](https://ocw.mit.edu/courses/18-781-theory-of-numbers-spring-2012/pages/lecture-notes/) and [William Stein, *Elementary Number Theory*](https://www.wstein.org/ent/). Newer lecture references include [Stanford's quadratic-reciprocity proof notes](https://crypto.stanford.edu/pbc/notes/numbertheory/quadrecip.html), [Darij Grinberg's arithmetic functions notes](https://darijgrinberg.gitlab.io/floor.pdf), and [MIT's p-adic Hensel lemma notes](https://math.mit.edu/classes/18.782/2013fa/LectureNotes8.pdf). Every transcript has relevant Wikipedia background links, and each has a source sidecar under `metadata/`. A recorded source is a reading reference, not a claim of verbatim quotation or a line-by-line external proof audit.

Future coverage and explicitly deferred proofs appear in [BACKLOG.md](BACKLOG.md).
