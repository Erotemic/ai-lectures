# 008000 — Arithmetic Functions, Dirichlet Convolution, and Möbius Inversion

**Track:** Number Theory from First Principles. **Background:** divisibility, prime factorization, counting with finite sums, and Euler's totient. **Theme:** how to undo information that has been accumulated over all divisors.

<!-- BEGIN SPOKEN LECTURE -->

# Arithmetic Functions, Dirichlet Convolution, and Möbius Inversion

Imagine that you are given a report about every positive integer. For each number n, the report tells you the sum of an unknown quantity over every positive divisor of n. Could you recover the original quantity? At first this sounds like trying to reconstruct individual purchases from a collection of overlapping totals. But divisibility has enough structure to make the reconstruction exact.

This is the subject of Möbius inversion. The name may sound remote from elementary arithmetic, but the proof is a refinement of something familiar: inclusion and exclusion. We will build the idea from prime factors, discover a natural multiplication law for functions on positive integers, and use it to reverse divisor sums. Then we will count coprime integer pairs with the same tool.

## Numbers can have functions as well as factors

An arithmetic function assigns a number to each positive integer. That number could count something or measure something. For example, the divisor-counting function records how many positive divisors n has. The divisor-sum function adds those divisors instead. Euler's totient counts integers from one through n that are coprime to n. An arithmetic function is simply a sequence whose index happens to be an integer with useful factorization.

Consider twelve. Its positive divisors are one, two, three, four, six and twelve. So its divisor count is six, and its divisor sum is twenty-eight. Four of the integers between one and twelve are coprime to twelve: one, five, seven and eleven. Thus the totient of twelve is four.

One important adjective is **multiplicative**. An arithmetic function f is multiplicative when f of m times n equals f of m times f of n whenever m and n are coprime. This does not assert the same formula for arbitrary m and n. For the totient, the Chinese remainder theorem gives the coprime-product rule. And once you know a multiplicative function at every prime power, you know it at every positive integer: write n as a product of mutually coprime prime powers and multiply the separate values.

For example, twelve is four times three, with four and three coprime. The totient of four is two, and the totient of three is two, so the totient of twelve is four. But the totient of four times two is four, while the product of the totient of four and the totient of two is two. That attempted multiplication fails because four and two are not coprime. The hypothesis is part of the theorem, not a technicality to discard once examples look convincing.

## A sign that remembers squarefree divisors

We need a function with an especially useful pattern. Define the Möbius function, pronounced MUR-bee-us or MOH-bee-us in common usage, as follows. At one, its value is one. At an integer containing any squared prime factor, its value is zero. Otherwise the integer is a product of distinct primes; the function is one if the number of those primes is even, and negative one if that number is odd.

So the values at two, three and five are negative one. The value at six, a product of two distinct primes, is one. The value at thirty, a product of three distinct primes, is negative one. At twelve the value is zero, because two squared divides twelve.

What happens if we add the Möbius function over **all the divisors** of n? Take twelve. Its divisors have Möbius values one, negative one, negative one, zero, one and zero. Their sum is zero. At six the divisor values are one, negative one, negative one and one, again summing to zero. At one, the sum is one, because there is only one divisor.

This pattern holds for every positive integer. Suppose n has r distinct prime factors. Only its squarefree divisors can contribute, because the Möbius value of every other divisor is zero. Choosing a squarefree divisor amounts to choosing a subset of those r primes. Choosing a subset of size zero contributes one; size one contributes negative one; size two contributes one; and so forth. The alternating sum is the binomial expansion of one minus one, raised to the r-th power. If n is greater than one, r is positive, and the result is zero. For n equal to one, r is zero and the result is one.

This is inclusion-exclusion hiding inside prime factorization. Adding Möbius values across all divisors is a perfect cancellation device: it erases every positive integer except one.

## Multiplying functions by summing across factor pairs

Ordinary functions can be added pointwise. For arithmetic functions there is another multiplication operation that treats divisors as factor pairs. Given f and g, define their **Dirichlet convolution** at n by taking, for every positive divisor d of n, f of d times g of n divided by d, and adding those products.

The rule may sound formal. Try the constant function that assigns one to every positive integer. Convolving it with itself produces, at n, one contribution for each divisor d. So its convolution square is the divisor-counting function. If instead we convolve the identity-value function, the function that assigns n to n, with the constant-one function, we obtain the sum of all positive divisors. An apparently new multiplication is a compact way to describe old arithmetic quantities.

Dirichlet convolution is commutative. If you replace a divisor d with its complementary divisor n divided by d, the summands trade places. It is associative too. To see why, think of an ordered triple of positive integers whose product is n. Either way of bracketing a three-function convolution sums one contribution for each such triple. Both calculations enumerate the same factorizations.

The convolution has its own multiplicative identity. Let epsilon be one at n equal to one and zero everywhere else. Convolve epsilon with any function f. Only the term with d equal to one survives, giving f of n. So epsilon plays the role of the number one in this algebra of functions.

And now our cancellation identity becomes a remarkable equation: **the constant-one function convolved with the Möbius function equals epsilon**. In other words, Möbius is the convolution inverse of the constant-one function.

This is the underlying reason inversion works. We have constructed an arithmetic operation that sums over divisors, and a second operation that undoes the summing.

## The inversion theorem, proved step by step

Suppose f is an arithmetic function and you are given another function F defined by adding f over the positive divisors of n. We can say this in words: F of n equals the sum of f of d over every d dividing n. In convolution language, F is the constant-one function convolved with f.

Now convolve both sides with Möbius. Associativity allows us to pair Möbius with the constant-one function first. That pair becomes epsilon. Convolving epsilon with f returns f. Therefore f of n is the sum, over all divisors d of n, of Möbius of d times F of n divided by d.

This is Möbius inversion. It is exact and finite at every n. No convergence theorem is needed, because a positive integer has only finitely many divisors. The proof depends only on unique prime factorization, the cancellation identity we established, and the regrouping of finite sums.

Notice what the inverse does. It does not subtract an arbitrary correction guessed from data. It assigns a principled inclusion-exclusion sign to each divisor, so that contributions counted too many times cancel and the original value remains.

## Recovering the totient

Here is a concrete example where the input divisor sum already has a familiar meaning. For every n, the sum of the totients of all positive divisors of n equals n.

Why? Classify the integers one through n by their greatest common divisor with n. If that greatest common divisor is d, divide the integer and n by d. The resulting integer lies between one and n divided by d and is coprime to n divided by d. So there are exactly the totient of n divided by d such integers. Every integer from one through n belongs to exactly one class, and the classes together contain n integers. This proves the divisor-sum identity.

Apply Möbius inversion. We recover the totient of n as the sum, over divisors d, of Möbius of d times n divided by d. For twelve, only the squarefree divisors one, two, three and six contribute. We obtain twelve minus six minus four plus two, which is four, exactly as our direct count found.

There is an even more revealing way to reorganize that sum. Every contributing divisor is a subset of the distinct primes dividing n. Expanding a product with one factor of the form one minus one over p for each such prime gives exactly the same alternating terms. Consequently, the totient of n equals n multiplied by the product of one minus one over p, for each **distinct** prime p dividing n.

For thirty, remove the multiples of two, three and five, carefully restoring their overlaps. The formula gives thirty times one half, times two thirds, times four fifths, which is eight. This is the same inclusion-exclusion argument expressed in arithmetic-function language.

## Counting visible points on a square grid

Imagine drawing every integer point in a square grid from one through N on each axis. If you stand at the origin and look toward a point with coordinates a and b, you can see that point directly, without another integer point on the same ray in front of it, precisely when a and b are coprime. If they share a factor, divide both coordinates by it to find a closer integer point on the ray. Conversely, if they are coprime, no smaller positive integer multiple of the same primitive direction has integer coordinates.

We can count these visible points exactly by Möbius inversion. Remember the cancellation identity: the sum of Möbius over divisors of an integer is one if the integer is one and zero otherwise. Apply it to the greatest common divisor of a and b. It becomes an indicator: one if the pair is coprime and zero if not.

Now sum that indicator over all ordered pairs a and b from one through N. Swap the finite sums. For a fixed divisor d, how many pairs have both coordinates divisible by d? Exactly the square of the greatest integer not exceeding N divided by d. Therefore the count of coprime ordered pairs is the sum, for d from one through N, of Möbius of d times the square of that integer quotient.

Try N equal to five. The whole square contains twenty-five points. For d equal to two, subtract four. For three, subtract one. Four contributes zero, because its Möbius value is zero. Five subtracts one. The result is nineteen visible points. You can confirm that count by listing the pairs or drawing a five-by-five grid.

The formula is exact for every N. With analysis, one can go further and prove that the fraction of coprime pairs tends to six divided by pi squared as N grows. That limiting claim uses an infinite series and Euler's evaluation of its value, so it is a separate theorem, not a consequence we have proved merely by writing a finite counting formula.

## The broader idea

Möbius inversion is not confined to primes. Its real setting is a family of overlapping cumulative sums indexed by a partial order. Divisibility is one example of such an order; inclusion of sets is another. On subsets, the alternating correction from inclusion-exclusion plays the same role that our Möbius signs play on divisors.

In analytic number theory, divisor convolution also interacts with generating series. Under suitable convergence hypotheses, multiplying two Dirichlet series corresponds to convolving their coefficient functions. This connection eventually lets us translate between the arithmetic of divisors and the distribution of primes. The convergence hypotheses matter, and we will not quietly treat infinite rearrangements as if they were finite sums.

We began with the question of undoing a report of divisor totals. We now have a complete answer, its algebraic proof, and concrete applications to the totient and primitive lattice points. The key insight is that prime factorization makes inclusion-exclusion systematic. Once you recognize the underlying cumulative sum, Möbius inversion lets you recover exactly what was hidden inside it.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

### Definitions and examples

An arithmetic function is \(f:\mathbb N_{>0}\to\mathbb C\) (or another commutative coefficient ring). It is **multiplicative** when \(f(1)=1\) and \(f(mn)=f(m)f(n)\) for \(\gcd(m,n)=1\). It need not satisfy this identity when m and n are not coprime.

\[
\mu(n)=\begin{cases}
1,&n=1,\\
(-1)^r,&n=p_1\cdots p_r\text{ with distinct primes},\\
0,&\text{some }p^2\mid n.
\end{cases}
\]

For n with r distinct prime factors,

\[
\sum_{d\mid n}\mu(d)=\sum_{S\subseteq\{1,\ldots,r\}}(-1)^{|S|}
=(1-1)^r=\begin{cases}1,&n=1,\\0,&n>1.\end{cases}
\]

### Dirichlet convolution, associativity, and inversion

Let \({\bf1}(n)=1\), \(\varepsilon(n)=1_{\{n=1\}}\), and \(\mathrm{id}(n)=n\). Define

\[
(f*g)(n)=\sum_{d\mid n}f(d)g(n/d).
\]

Swapping d and n/d proves commutativity. Expanding either parenthesization proves associativity because both equal \(\sum_{abc=n} f(a)g(b)h(c)\), over **ordered positive factor triples**. The unit satisfies \(\varepsilon*f=f\), and \(\mu*{\bf1}=\varepsilon\).

If \(F(n)=\sum_{d\mid n} f(d)=({\bf1}*f)(n)\), then

\[
f=\mu*F,
\qquad
\boxed{f(n)=\sum_{d\mid n}\mu(d)F(n/d)=\sum_{d\mid n}\mu(n/d)F(d).}
\]

Useful cases: \(\tau={\bf1}*{\bf1}\), \(\sigma=\mathrm{id}*{\bf1}\), \(\mathrm{id}=\varphi*{\bf1}\), so

\[
\varphi(n)=\sum_{d\mid n}\mu(d)\frac nd
=n\prod_{p\mid n}\left(1-\frac1p\right).
\]

At \(n=12\), this gives \(12-6-4+2=4\).

### Coprime lattice points

For a positive integer g,
\(1_{\{g=1\}}=\sum_{d\mid g}\mu(d)\). Let \(C(N)\) count ordered pairs \((a,b)\in\{1,\ldots,N\}^2\) satisfying \(\gcd(a,b)=1\). Then, by reversing finite sums,

\[
\boxed{C(N)=\sum_{d=1}^N \mu(d)\left\lfloor\frac Nd\right\rfloor^2.}
\]

For \(N=5\), \(C(5)=25-4-1-1=19\). Under additional analytic arguments, \(C(N)/N^2\to1/\zeta(2)=6/\pi^2\); the limit and Euler's evaluation of \(\zeta(2)\) are **not** established by the finite identity alone.

### A carefully delimited analytic bridge

For real \(s>1\), absolute convergence permits the Dirichlet generating identity

\[
\sum_{n\ge1}\frac{(f*g)(n)}{n^s}=
\left(\sum_{n\ge1}\frac{f(n)}{n^s}\right)
\left(\sum_{n\ge1}\frac{g(n)}{n^s}\right)
\]

**provided both coefficient series converge absolutely**. In particular
\(\sum_{n\ge1}\mu(n)n^{-s}=1/\zeta(s)\) for \(s>1\). Extension to \(s=1\) is not automatic.

### Practice and reasoning checks

1. Compute \(\mu(n)\) for \(n=1,6,12,30,60,105\), then verify the cancellation sum for sixty.
2. Use the totient divisor-sum identity and Möbius inversion to find \(\varphi(18)\) and \(\varphi(45)\).
3. Prove \(\tau(p^e)=e+1\) and \(\sigma(p^e)=1+p+\cdots+p^e\), then use multiplicativity to compute \(\tau(72)\) and \(\sigma(72)\).
4. Show directly that Dirichlet convolution of multiplicative functions is multiplicative, by separating divisors of coprime factors.
5. Use the exact coprime-pair formula with N equal to six; check by an independent grid count.

### Sources and further reading

- MIT OpenCourseWare, [*18.781 Theory of Numbers*, arithmetic functions and Möbius inversion lectures](https://ocw.mit.edu/courses/18-781-theory-of-numbers-spring-2012/pages/lecture-notes/).
- Darij Grinberg, [*18.781: Floor and arithmetic functions*, sections 2.1–2.6](https://darijgrinberg.gitlab.io/floor.pdf): detailed proofs of convolution identities and inversion.
- William Stein, [*Elementary Number Theory*](https://www.wstein.org/ent/).
- Wikipedia orientation: [Möbius function](https://en.wikipedia.org/wiki/M%C3%B6bius_function), [Möbius inversion formula](https://en.wikipedia.org/wiki/M%C3%B6bius_inversion_formula), [Dirichlet convolution](https://en.wikipedia.org/wiki/Dirichlet_convolution), [Euler's totient function](https://en.wikipedia.org/wiki/Euler%27s_totient_function).
