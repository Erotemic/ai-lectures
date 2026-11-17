# 024000 — How Many Ways Can an Integer Be Two Squares?

**Track:** Number Theory from First Principles. **Background:** Gaussian integers, prime factorization, Dirichlet characters and convolution. **Aim:** prove the exact count of ordered, signed representations and its divisor-sum formula.

<!-- BEGIN SPOKEN LECTURE -->

# How Many Ways Can an Integer Be Two Squares?

Thirteen is a sum of two squares: two squared plus three squared. So is sixty-five, and sixty-five has two visibly different decompositions: one squared plus eight squared, and four squared plus seven squared. What makes sixty-five more generous? And can we count its solutions without looking through every possible pair of integers?

The existence theorem answers a different question. A positive integer can be expressed as a sum of two integer squares exactly when each prime congruent to three modulo four occurs with an even exponent in its prime factorization. That theorem is a gate: it tells us whether any solutions exist. It does not tell us how many lie beyond the gate.

We will establish an exact formula. Its proof has two languages, and both matter. Gaussian integer factorization explains why the count has its particular multiplicative shape. Dirichlet convolution transforms that shape into a surprising formula involving ordinary divisors, and connects a geometry problem to a character modulo four.

## Decide what a representation counts

Start by making a small accounting decision. We count **ordered integer pairs**, and we distinguish signs. If a pair is two and three, its companions include three and two, negative two and three, and every other independent choice of sign. As long as neither entry is zero and their absolute values differ, a single picture of two perpendicular side lengths creates eight ordered signed pairs.

For thirteen, those eight are all the solutions. For five, one and two also produces eight. For one, things are different: one squared plus zero squared gives four ordered pairs, not eight, because changing the sign of zero does nothing. And the solution zero, zero, is reserved for the integer zero; it is the only solution there.

Denote the number of ordered signed pairs satisfying a squared plus b squared equals the positive integer n by r two of n. Our formula will hold for positive n. We will define r two of zero as one, separately, when we discuss generating series. That small distinction keeps a later constant term correct.

Try sixty-five now. The representations using one and eight give eight ordered signed pairs. Those using four and seven give eight more. Therefore r two of sixty-five is sixteen. The exact formula must produce sixteen without having to find the pairs first.

## A pair is a Gaussian integer with a prescribed norm

Replace the pair a, b by the Gaussian integer a plus b times i. Its norm is a squared plus b squared. So r two of n counts exactly the Gaussian integers whose norm is n.

Why is that useful? In the Gaussian integers we have unique factorization, up to order and multiplication by a unit. There are four units: one, negative one, i, and negative i. Multiplying by any unit preserves the norm, and gives four distinct Gaussian integers whenever the norm is positive.

We also know how ordinary rational primes behave there. Two is ramified. It is a unit times the square of one plus i, whose norm is two. Every ordinary prime congruent to one modulo four splits into two nonassociate conjugate Gaussian primes, each of norm p. Every ordinary prime congruent to three modulo four stays irreducible as a Gaussian integer, and its Gaussian norm is p squared.

The last claim deserves a reminder. If a rational prime p congruent to three modulo four factored nontrivially in Gaussian integers, the norms of its factors would both have to equal p. That would represent p as two squares, which the existence theorem forbids. So it remains Gaussian-prime.

Now write the positive integer n as a product of a power of two, powers of primes of the first splitting type, and powers of primes of the second type. The interesting bookkeeping happens at the split primes.

Suppose p is congruent to one modulo four and occurs in n to exponent e. In Gaussian integers p factors as pi times pi-bar, with pi and pi-bar nonassociate. A Gaussian integer of norm n can receive k copies of pi and e minus k copies of pi-bar. Every integer choice of k from zero through e gives a different Gaussian factorization. That is e plus one choices for p.

For a prime congruent to three modulo four, something more restrictive happens. A Gaussian integer can contain that ordinary prime to some exponent t, but its norm then contains p to exponent two t. So an odd exponent of p in n makes the entire problem impossible. An even exponent forces t exactly; there is no choice to count.

For two, the exponent in the Gaussian integer is also determined, because one plus i has norm two and the conjugate one minus i differs from it only by a Gaussian unit. We do not get a second independent choice by pretending those two associates are different primes.

Finally we multiply by four, one for each Gaussian unit. The result is our counting theorem. If any prime congruent to three modulo four has an odd exponent, r two of n is zero. Otherwise, r two of n equals four times the product of e plus one over all primes congruent to one modulo four, where e is that prime's exponent in n. An empty product is one.

Let's put the formula to work. Sixty-five is five times thirteen. Both primes split, each with exponent one. We get four times two times two, which is sixteen, as expected. Twenty-five is five squared. We get four times three, or twelve. Eight of those pairs use three and four; four more use five and zero. Forty-five is five times three squared. The factor three is inert, but its exponent is even, so it contributes no choice. The factor five contributes two choices; four times two is eight. All eight come from the pair three and six with signs and order.

What about eighteen? It is two times three squared. There are no primes congruent to one modulo four, and the exponent of three is even. We get four representations: three squared plus three squared, with the two signs chosen independently. This is a useful warning that the geometry of a representation can affect its symmetry without requiring an adjustment to the Gaussian count. The four units already account for it.

## The divisor formula hidden in the answer

There is a second way to describe exactly the same function, without mentioning Gaussian prime factors explicitly.

Define a character modulo four, conventionally called chi four. On positive odd integers it is one for numbers congruent to one modulo four, and negative one for numbers congruent to three modulo four. On even integers it is zero. This is a completely multiplicative function: chi four of a product equals the product of the two chi four values.

Form the divisor sum: add chi four of d over every positive divisor d of n. Let's calculate its contribution one prime power at a time.

At a power of two, every divisor except one is even, so the sum is one. At a power of a prime congruent to one modulo four, chi four is one on every power, so the sum is e plus one. At a power of a prime congruent to three modulo four, the terms alternate: one, negative one, one, negative one, and so on. Their sum is one if e is even and zero if e is odd.

These are exactly the local factors we just counted in Gaussian integers. Because a divisor of a product of coprime integers is built by choosing a divisor of each factor independently, the divisor sum is multiplicative. Therefore, for every positive integer n, **r two of n is four times the sum of chi four of d over the divisors d of n**.

This is sometimes called Jacobi's two-square identity. It may also be written as four times the number of divisors congruent to one modulo four minus four times the number congruent to three modulo four. Even divisors contribute zero.

For sixty-five, the divisors are one, five, thirteen, and sixty-five. Every one of them is congruent to one modulo four. Their four character values add to four, and multiplying by four gives sixteen. For twenty-one, the divisors are one, three, seven, and twenty-one. Their character values are one, negative one, negative one, and one. They cancel, leaving zero representations. The cancellation is not an accident; it encodes the odd exponents of primes that cannot split in Gaussian integers.

We can express this economically using Dirichlet convolution. Let the constant-one arithmetic function give one at every positive integer. Convolve it with chi four: the value at n is the divisor sum we just calculated. Hence r two divided by four equals one convolved with chi four, as arithmetic functions on positive integers.

Why care about the convolution phrasing? It makes a multiplicative identity into an algebraic one, so the same tools from Möbius inversion and Euler products become available. On the half-plane where the relevant series converge absolutely, the Dirichlet series whose coefficients are r two of n divided by four factors as the Riemann zeta function times the Dirichlet L-function for chi four.

This statement does not assert that a count of lattice points has magically become a distribution theorem for primes. It says that the arithmetic of representations and the analytic behavior of an Euler product are linked by an exact coefficient identity. Later, summing the representation counts through a large cutoff will give a geometric interpretation of the analytic singularity near one.

## One formula, several kinds of information

Compare the existence criterion with the counting formula. The existence criterion is just the statement that the count is positive. But the actual value tells us more: each prime congruent to one modulo four contributes its exponent plus one independent options. The inert primes do not increase the count. Powers of two affect which solutions appear, but not the total number, provided the other conditions hold.

This also shows why a naive rule such as "every new prime doubles the number of pairs" fails. If the same splitting prime appears repeatedly, its exponent e contributes e plus one, not two to the e. Twenty-five has twelve solutions, not sixteen. We are distributing copies of a prime between a Gaussian factor and its conjugate, not independently switching each indistinguishable copy.

There is a useful computational shortcut. Suppose n is five squared times thirteen times three to the fourth. Its factorization already tells us the answer. There are three choices at the five factor, two at thirteen, and one forced choice at three. Multiply by the four units and obtain twenty-four ordered signed representations. We have counted them without extracting a single square root.

It is important not to confuse this with counting positive unordered pairs. That version treats exchanges and signs as equivalent; pairs on the axes and on the diagonal have smaller symmetry orbits. To count that version you must correct for those special cases. Our signed, ordered count is deliberate: it is the one that respects Gaussian multiplication cleanly.

We began with a geometric puzzle about how many points sit on a circle of squared radius n. Unique factorization in a different integer ring gave us an exact answer. Then a character modulo four, which arose earlier as a Fourier-like filter for congruence classes, recovered that answer as a divisor sum. These are not competing explanations. One exposes the geometry of prime splitting. The other exposes the arithmetic function hidden in the geometry.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

### Counting convention and theorem

For positive integer \(n\), define
\[
r_2(n)=\#\{(a,b)\in\mathbb Z^2:a^2+b^2=n\}.
\]
Ordered pairs and independent signs count separately; zero counts once. Define \(r_2(0)=1\) separately when forming generating functions. If
\[
n=2^a\prod_{p\equiv1\ (4)}p^{e_p}\prod_{q\equiv3\ (4)}q^{f_q},
\]
then unique factorization of \(\mathbb Z[i]\) gives
\[
\boxed{r_2(n)=\begin{cases}
4\prod_{p\equiv1\ (4)}(e_p+1),&\text{if every }f_q\text{ is even},\\
0,&\text{otherwise}.
\end{cases}}
\]
A Gaussian integer of norm \(n\) contains exactly \(a\) copies of \(1+i\) (up to associates), exactly \(f_q/2\) copies of each inert rational prime \(q\), and for each \(p=\pi\bar\pi\) a choice of exponents \((k,e_p-k)\). Four Gaussian units multiply the count by 4. The separate \(\pi,\bar\pi\) are not associates for \(p\equiv1\pmod4\).

### Divisor identity, proved by prime powers

\[
\chi_4(m)=\begin{cases}0&m\equiv0,2\pmod4,\\1&m\equiv1\pmod4,\\-1&m\equiv3\pmod4.\end{cases}
\quad \chi_4(ab)=\chi_4(a)\chi_4(b).
\]
The multiplicative function \(S(n)=\sum_{d\mid n}\chi_4(d)=(\mathbf1*\chi_4)(n)\) has prime-power values
\[
S(2^a)=1,\qquad
S(p^e)=e+1\ (p\equiv1\bmod4),\qquad
S(q^f)=\frac{1-(-1)^{f+1}}2\ (q\equiv3\bmod4).
\]
Consequently
\[
\boxed{r_2(n)=4(\mathbf1*\chi_4)(n)=4\sum_{d\mid n}\chi_4(d)=4(d_1(n)-d_3(n)),\ n\ge1.}
\]
For \(\Re(s)>1\), absolute convergence and Dirichlet-series multiplication give
\[
\boxed{\sum_{n\ge1}\frac{r_2(n)}{n^s}=4\zeta(s)L(s,\chi_4).}
\]
This is not a statement about \(n=0\), which is omitted from Dirichlet series.

### Worked cases

| \(n\) | Factorization | \(r_2(n)\) | Geometry |
|---|---|---:|---|
| 1 | \(1\) | 4 | \((\pm1,0),(0,\pm1)\) |
| 5 | \(5\) | 8 | \((\pm1,\pm2)\), exchanged |
| 13 | \(13\) | 8 | \((\pm2,\pm3)\), exchanged |
| 18 | \(2\cdot3^2\) | 4 | \((\pm3,\pm3)\) |
| 25 | \(5^2\) | 12 | \((\pm5,0),(0,\pm5)\) and \((\pm3,\pm4)\), exchanged |
| 45 | \(3^2\cdot5\) | 8 | \((\pm3,\pm6)\), exchanged |
| 65 | \(5\cdot13\) | 16 | \((\pm1,\pm8)\), \((\pm4,\pm7)\), exchanged |

### Exercises

1. Count \(r_2(50)\), then list the solutions and check that the two counts agree.
2. Prove that \(r_2(5^e)=4(e+1)\) and explain why this is not \(4\cdot2^e\).
3. Establish \(r_2(mn)/4=(r_2(m)/4)(r_2(n)/4)\) for coprime positive \(m,n\), and provide a counterexample when coprimality fails.
4. Compute \(r_2(325)\) without solving any quadratic equations.
5. Explain precisely why \(\pi\) and \(\bar\pi\) are nonassociate when \(p\equiv1\bmod4\), whereas \(1+i\) and \(1-i\) are associates.

### Reading and source notes

- Eric W. Weisstein, [Sum of Squares Function, MathWorld](https://mathworld.wolfram.com/SumofSquaresFunction.html), counting conventions, divisor identity and prime-exponent formula.
- Wikipedia: [Sum of two squares theorem](https://en.wikipedia.org/wiki/Sum_of_two_squares_theorem), [Gaussian integer](https://en.wikipedia.org/wiki/Gaussian_integer), [Dirichlet convolution](https://en.wikipedia.org/wiki/Dirichlet_convolution), [Dirichlet character](https://en.wikipedia.org/wiki/Dirichlet_character).
- The preceding course lectures 008000, 012000, and 016000 supply the independent proofs of convolution, Gaussian factorization, and the character laws used here.
