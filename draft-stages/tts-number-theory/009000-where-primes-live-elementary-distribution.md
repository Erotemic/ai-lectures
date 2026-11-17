# 009000 — Where the Primes Live: Elementary Distribution Arguments

**Track:** Number Theory from First Principles. **Background:** unique factorization, congruences, quadratic residues, finite products, and introductory logarithms. **Theme:** the distance between proving infinitely many primes and understanding how many there are.

<!-- BEGIN SPOKEN LECTURE -->

# Where the Primes Live: Elementary Distribution Arguments

There are infinitely many prime numbers. Euclid's argument proves that with one striking construction: take a proposed complete list, multiply its members, and add one. But if you want to understand prime numbers as they become larger, infinity is only the beginning. How widely spaced are they? Do some remainders occur among primes forever? How rapidly does the count of primes below a large bound grow?

These questions have answers of different difficulty. Some can be settled by divisibility and congruences. Others require careful estimation of products and sums. Still others belong to deeper analytic number theory. Our aim is to learn what elementary arguments genuinely establish, and to see how their limits point toward stronger theorems.

## The prime-counting function

For a positive real number x, let pi of x denote the number of primes less than or equal to x. The notation pi here is a name for a counting function; it is not the circle constant, although both are conventionally written with the same Greek letter.

For x equal to ten, there are four primes: two, three, five and seven. So pi of ten is four. For twenty, the primes are two, three, five, seven, eleven, thirteen, seventeen and nineteen. So pi of twenty is eight. We can count small cases by a sieve: cross out the multiples of two, then three, then five, and continue through primes whose squares do not exceed the bound. The numbers left standing above one are exactly the primes.

Why is stopping at the square root enough? If a composite number n factors into two positive integers greater than one, at least one factor is no larger than the square root of n. That factor has a prime divisor no larger still. Thus a composite n not exceeding x has a prime divisor no larger than the square root of x. This is a correctness proof for the sieve cutoff, separate from its efficiency as an implementation.

Counting primes by this method is a finite computation. It does not by itself explain the asymptotic shape of the counting function. For that, we need proofs that work uniformly as the bound grows.

## Infinitely many primes of each kind modulo four

Euclid proves infinitely many primes in total, but that does not immediately prove infinitely many in a particular remainder class. We can nevertheless settle two complete cases using elementary ideas.

First consider primes leaving remainder three when divided by four. Suppose only finitely many exist, and multiply all of them to get P. Form four times P minus one. This number is positive and leaves remainder three modulo four. None of our listed primes divides it, because division by any prime dividing P leaves remainder negative one.

Now use the simple multiplication table modulo four. A product of integers each congruent to one modulo four is itself one modulo four. A positive odd number congruent to three modulo four therefore must have at least one prime factor congruent to three modulo four. Our new number has such a factor, yet that factor is not on the supposedly complete list. Contradiction. There are infinitely many primes congruent to three modulo four.

The primes congruent to one modulo four require a different trick. Suppose there are only finitely many, and let P be their product. Consider the number obtained by squaring twice P and adding one. It is odd and greater than one. Any prime q dividing it satisfies the congruence that the square of twice P is negative one modulo q. So negative one is a square modulo q.

We already proved that an odd prime has a square root of negative one exactly when it is congruent to one modulo four. Thus every prime factor of this new number is one modulo four. But none of the primes in our alleged complete list divides it, since the number leaves remainder one when divided by each of those primes. Again a contradiction. So there are infinitely many primes congruent to one modulo four as well.

Notice how the two constructions differ. For three modulo four, we used a product congruence and obtained **at least one** prime factor of the desired kind. For one modulo four, we built a number whose **every** prime factor has the desired kind, using our theorem about the residue negative one. In both cases the new number may be composite. The argument needs an appropriately classified prime factor, not a new prime number made to order.

One may now ask whether every remainder class that is coprime to its modulus contains infinitely many primes. Dirichlet's theorem answers yes. But the elementary proofs we have given only cover the two odd classes modulo four; they do not prove Dirichlet's general theorem.

## A product that remembers all integers

A different approach to primes starts with the harmonic sum: one plus a half plus a third, continuing through one over N. These partial sums grow without bound, though slowly. A useful way to see that is to group terms in blocks. The terms from one over two through one over three sum to at least a half; the next block, from one over four through one over seven, contributes at least another half; the next block from one over eight through one over fifteen contributes at least another half. Grouping successive powers of two gives an unlimited number of contributions bounded below by a positive constant.

Now return to prime factorization. Consider every prime p no larger than N, and for each take the infinite geometric sum one plus one over p plus one over p squared, and so on. Multiply all these geometric sums together. When you expand the product, you obtain the reciprocal of every positive integer built only from prime factors no larger than N, each appearing once by unique factorization.

Every integer from one through N has that property. Therefore this product is **at least** the harmonic sum through N. Each geometric series has value one divided by one minus one over p. We obtain a finite product inequality: the harmonic sum through N is no larger than the product, over primes no greater than N, of those reciprocal factors.

This is Euler's product idea in a form that avoids a dangerous shortcut. We are using finitely many prime factors and absolutely convergent geometric series. We have not substituted a divergent value into an infinite identity.

## Not just infinitely many: reciprocals of primes diverge

What can we deduce from the finite product inequality? Take natural logarithms. The logarithm of the harmonic sum is bounded above by the sum, over primes no greater than N, of the negative logarithm of one minus one over p.

For a number t between zero and one half, the negative logarithm of one minus t is at most t plus twice t squared. One can establish this by expanding the logarithm in a convergent power series, or by a short calculus argument. Every reciprocal of a prime lies in this interval, including one half.

So the logarithm of the harmonic sum is at most the sum of reciprocals of primes up to N, plus twice the sum of the reciprocals of their squares. The second sum stays bounded independently of N, because it is no larger than twice the convergent series of reciprocals of all integer squares greater than one.

Rearrange. The sum of reciprocals of primes up to N is at least the logarithm of the harmonic sum, minus a fixed constant. And the harmonic sum tends to infinity. Its logarithm also tends to infinity. Therefore **the series of reciprocal primes diverges**.

This says much more than the mere fact that there are infinitely many primes. The numbers two to the first power, two squared, two cubed, and so on are an infinite set, but their reciprocals form a convergent geometric series. The primes cannot be comparably sparse in this particular sense.

We have also obtained a rough quantitative lower bound. Since the harmonic sum grows at least like the logarithm of N, the sum of reciprocal primes up to N grows at least like the logarithm of the logarithm of N, apart from an additive constant. This is not an exact growth formula, but it demonstrates how an inequality can turn a qualitative proof of infinity into a quantitative statement.

## A surprisingly useful upper estimate

We can also use an elementary combinatorial number to bound how many primes lie in a large interval. Take the central binomial coefficient: the number of ways to choose n objects from a collection of two n objects. This integer equals the factorial of two n divided by n factorial squared.

Every prime strictly larger than n and at most two n divides that binomial coefficient. Why? Such a prime occurs in the numerator factorial, but it divides neither of the two copies of n factorial in the denominator. Thus the product of all primes in that interval is no larger than the binomial coefficient.

On the other hand, add all the binomial coefficients obtained by choosing zero objects, one object, and so on through two n objects. The sum is four to the power n, because each of the two n objects can independently be included or excluded. The central binomial coefficient is just one nonnegative term in this sum, so it is no larger than four to the power n.

Combine the two observations. If r primes lie strictly between n and two n, their product is greater than n to the power r. But that product is at most four to the power n. Taking logarithms gives r times the logarithm of n less than or equal to two n times the logarithm of two. So the number of primes in this doubling interval is at most two n times log two divided by log n, for n greater than one.

For the interval from ten to twenty, the primes are eleven, thirteen, seventeen and nineteen. We count four. Our bound is a little over six. It is not a sharp prediction, but it is valid without searching for the primes individually.

This shows how the scale of n divided by log n can enter an elementary argument. It is an upper bound for one interval, not an asymptotic equality, and it does not show that there actually are about n divided by log n primes in that interval. Proving matching lower and upper estimates takes more work.

## Three different claims about scarcity

Here are three claims that are easy to confuse. First, primes go on forever. Second, their proportion among positive integers tends to zero. Third, their count up to x is approximately x divided by log x in the strong sense that the ratio of the two quantities tends to one.

We have already proved the first claim. The second also follows from the elementary material, though it is worth seeing why. Pick a finite list of small primes. Any prime not on that list avoids divisibility by every prime on it. The fraction of positive integers that avoid all those divisors tends, by periodic counting and the Chinese remainder theorem, to the product of one minus one over p across the chosen list.

Because the reciprocal-prime series diverges, these avoidance products can be made as small as we wish by taking a sufficiently long list. The proportion of large integers that could still be prime is therefore arbitrarily small. Thus the primes have natural density zero.

The third claim is the **prime number theorem**. It gives the precise first-order asymptotic pi of x is equivalent to x divided by log x. We have not proved it. The binomial upper bound and the divergence argument illustrate some of the tools and scales behind its study, but neither is the prime number theorem.

The same care applies to Dirichlet's theorem on all coprime residue classes. Our explicit constructions settle two classes modulo four, but do not give a general theory of primes in arithmetic progressions. Advanced methods involve characters, series and estimates that this course can develop only after more preparation.

What have we learned? Congruence arguments can establish infinite families of primes with specified arithmetic properties. Unique factorization turns the harmonic sum into an inequality about a prime product. A little analysis upgrades infinity to divergence of reciprocal sums. Binomial coefficients supply estimates on the number of primes in large intervals. Each step answers a stronger and more quantitative question. Knowing which step proves which statement is the foundation for understanding the analytic theory of prime numbers.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

### Infinitely many primes in both odd residue classes modulo four

If the primes \(p\equiv3\pmod4\) were \(p_1,\ldots,p_k\), put \(P=\prod_i p_i\) and \(N=4P-1\). Then \(N\equiv3\pmod4\) and \(N\equiv-1\pmod{p_i}\). As N is odd and congruent to three modulo four, at least one prime factor q is congruent to three modulo four. That q is not on the list, a contradiction.

If the primes \(p\equiv1\pmod4\) were \(p_1,\ldots,p_k\), put \(P=\prod_i p_i\) and \(N=(2P)^2+1\). Every prime divisor q of the odd N satisfies \((2P)^2\equiv-1\pmod q\), hence \(q\equiv1\pmod4\) by lecture 006000. But \(N\equiv1\pmod{p_i}\). Contradiction.

### Euler's product at a convergent parameter

For real \(s>1\), absolute convergence and unique factorization justify

\[
\zeta(s)=\sum_{n=1}^{\infty}\frac1{n^s}=
\prod_{p\text{ prime}}\frac1{1-p^{-s}}.
\]

At \(s=1\), **the series is divergent and this equality must not be substituted into as an equality of finite numbers**. For each finite N, however,

\[
H_N:=\sum_{n=1}^{N}\frac1n
\le \prod_{p\le N}\left(1-\frac1p\right)^{-1}.
\]

For \(0<t\le1/2\), \(-\log(1-t)\le t+2t^2\). Thus

\[
\log H_N\le \sum_{p\le N}\frac1p
+2\sum_{p\le N}\frac1{p^2}
\le\sum_{p\le N}\frac1p+C,
\qquad C=2\sum_{n=2}^{\infty}\frac1{n^2}<\infty.
\]

Since \(H_N\to\infty\), \(\sum_p1/p\) diverges. Since \(H_N\ge \log(N+1)\), this also gives \(\sum_{p\le N}1/p\ge\log\log(N+1)-C\) for \(N\ge2\). This is a **lower bound**, not Mertens's asymptotic formula.

### An interval bound using a binomial coefficient

For integer \(n\ge2\), each prime \(n<p\le2n\) divides \(\binom{2n}{n}\). Thus, with \(r=\pi(2n)-\pi(n)\),

\[
n^r\le\prod_{n<p\le2n}p
\le\binom{2n}{n}\le4^n,
\qquad
\boxed{\pi(2n)-\pi(n)\le\frac{2n\log2}{\log n}.}
\]

The estimate has the right *order of magnitude as an upper bound* in a doubling interval but does not imply the prime number theorem. It also does not establish Bertrand's postulate, which is a **lower bound** asserting an interval contains at least one prime.

### Proof that the natural density of primes is zero

Fix \(p_1,\ldots,p_k\), with \(M=p_1\cdots p_k\). In each full block of M consecutive integers, exactly \(\varphi(M)=M\prod_i(1-1/p_i)\) integers are coprime to M. A prime exceeding \(p_k\) lies in these admissible classes, hence

\[
\limsup_{x\to\infty}\frac{\pi(x)}x\le\prod_{i=1}^{k}\left(1-\frac1{p_i}\right).
\]

As k increases, the product tends to zero because \(\sum_p1/p\) diverges. Therefore \(\lim_{x\to\infty}\pi(x)/x=0\).

**Proof status:** the lecture proves the two infinite-prime progression results, the divergence of prime reciprocals, the displayed binomial upper bound, and prime density zero. It **states without proof** Dirichlet's theorem for general coprime residue classes, Chebyshev's stronger two-sided bounds, Bertrand's postulate, and the prime number theorem \(\pi(x)\sim x/\log x\).

### Practice and reasoning checks

1. Explain why constructing \(4P-1\) does not prove that \(4P-1\) itself is prime. Find an explicit composite example if possible.
2. Use the negative-one test to explain why every prime divisor of \(x^2+1\) for even nonzero x is one modulo four.
3. Derive the inequality \(H_N\le\prod_{p\le N}(1-1/p)^{-1}\) from prime factorization without assigning a value to a divergent infinite product.
4. Estimate the number of primes in the interval from twenty to forty and compare with the central-binomial bound.
5. Explain why a set may be infinite and have density zero, or have density zero and a divergent reciprocal sum. Give an example of the former involving perfect squares.

### Sources and further reading

- MIT OpenCourseWare, [*18.781 Theory of Numbers*, lecture notes](https://ocw.mit.edu/courses/18-781-theory-of-numbers-spring-2012/pages/lecture-notes/), especially lectures on prime arithmetic and cyclotomic polynomials.
- University of Toronto course notes, [Elementary proof of divergence of the prime reciprocal series](https://www.math.toronto.edu/ebellah/CMU/21441Fall22/LectureNotes.pdf), section 1.3.4.
- Harvey Mudd College, [Sum of Prime Reciprocals](https://math.hmc.edu/funfacts/sum-of-prime-reciprocals/).
- Wikipedia orientation: [Prime-counting function](https://en.wikipedia.org/wiki/Prime-counting_function), [Euclid's theorem](https://en.wikipedia.org/wiki/Euclid%27s_theorem), [Dirichlet's theorem on arithmetic progressions](https://en.wikipedia.org/wiki/Dirichlet%27s_theorem_on_arithmetic_progressions), [Prime number theorem](https://en.wikipedia.org/wiki/Prime_number_theorem), [Euler product](https://en.wikipedia.org/wiki/Euler_product).
