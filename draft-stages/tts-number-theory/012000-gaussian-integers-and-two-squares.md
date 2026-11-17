# 012000 — Gaussian Integers and the Two-Squares Theorem

**Track:** Number Theory from First Principles. **Background:** unique prime factorization, Bézout's identity, congruences and the quadratic-residue test for negative one. **Theme:** solving an equation about ordinary integers by enlarging the set of numbers we allow ourselves to divide.

<!-- BEGIN SPOKEN LECTURE -->

# Gaussian Integers and the Two-Squares Theorem

Thirteen is the sum of two squares: two squared plus three squared. Seventeen is one squared plus four squared. But eleven is not the sum of two integer squares. There is a simple modular hint: squares leave remainder zero or one when divided by four, so the sum of two squares can never leave remainder three. This rules out eleven immediately.

It does not explain why every prime leaving remainder one modulo four **must** be a sum of two squares. A congruence can obstruct a solution without constructing one. To get the converse, we will briefly enlarge our number system. The enlargement has its own division algorithm, and that algorithm makes the arithmetic problem tractable.

## A grid of numbers, not a mysterious new species

A Gaussian integer is a complex number of the form a plus b times i, where a and b are ordinary integers and i squared equals negative one. You can draw such a number as the lattice point with horizontal coordinate a and vertical coordinate b. Adding Gaussian integers adds coordinates. Multiplying them uses the usual distributive law together with i squared equals negative one.

For example, two plus i times three plus two i equals four plus seven i. The real part is six minus two, and the imaginary part is four plus three. This multiplication looks less immediately intuitive than addition, so we attach a measurement to it.

Define the norm of a plus b i to be a squared plus b squared. The norm is a nonnegative ordinary integer, and is zero only for the zero Gaussian integer. Most importantly, the norm of a product is the product of the norms. You can verify this by expanding both sides, or geometrically by remembering that complex multiplication multiplies distances from the origin. We use the squared distance so the norm remains an integer.

Our original question is now asking: which ordinary integers are norms of Gaussian integers? Thirteen is the norm of two plus three i. Eleven is not the norm of any Gaussian integer, as the simple remainder argument showed.

This change of vocabulary does not solve the problem by itself, but it gives us multiplication as a tool. If two numbers are sums of two squares, so is their product. Indeed, multiplying a plus b i by c plus d i produces the sum-of-squares identity: the product of a squared plus b squared and c squared plus d squared is the sum of the squares of a c minus b d and a d plus b c.

For instance, five is two squared plus one squared, and thirteen is three squared plus two squared. Their product, sixty-five, is both four squared plus seven squared and eight squared plus one squared. The two representations come from multiplying two plus i by three plus two i or by three minus two i. The norm tells us why both constructions work.

## Division with a smaller remainder

In ordinary integer arithmetic, Euclid's algorithm depends on one fact: when we divide by a nonzero integer, we can choose a remainder smaller in absolute value than the divisor. Is there anything analogous on our two-dimensional lattice?

Yes, and here the geometry gives the proof. Suppose we wish to divide one Gaussian integer alpha by a nonzero Gaussian integer beta. First form the ordinary complex quotient alpha over beta. Its real and imaginary coordinates need not be integers. Round each coordinate to a nearest integer. That gives another Gaussian integer, q, close to the quotient.

The distance from an arbitrary real number to its nearest integer is at most one half. Therefore the squared distance between alpha over beta and q is at most one quarter plus one quarter, or one half. Let the remainder r be alpha minus beta times q. Multiplying our distance inequality by the norm of beta gives the norm of r at most half the norm of beta. In particular, its norm is strictly smaller than the norm of beta.

We have proved a Euclidean division algorithm for Gaussian integers. It is not a metaphor: it is an explicit way to find a quotient and a remainder, and the remainder's positive integer norm strictly decreases at every nonzero step.

Now the familiar integer argument can be repeated. Apply this division until the remainder is zero. The last nonzero remainder is a greatest common divisor, up to multiplication by a unit. Work backward through the divisions to express the greatest common divisor as a Gaussian-integer combination of the original two numbers. This is Bézout's identity on the grid.

The units, meaning the Gaussian integers with multiplicative inverses that are also Gaussian integers, are exactly one, negative one, i and negative i. Their norms are one. They account for why greatest common divisors and prime factorizations are determined only up to multiplication by a unit.

## Why the division algorithm gives unique factorization

Here is the structural step we must not hide. In a number system, an irreducible is a nonunit that cannot be split into two nonunits. A prime element is one that, whenever it divides a product, divides at least one factor. For ordinary integers those notions coincide, but in a general number system they need not.

They do coincide here. Suppose a Gaussian irreducible pi divides a product alpha times beta. If pi does not divide alpha, then pi and alpha have no nonunit common divisor, by irreducibility. Their greatest common divisor is therefore a unit, and Bézout's identity gives a combination of pi and alpha equal to one. Multiply that combination by beta. Since pi divides alpha times beta and also divides pi times beta, it divides beta. That proves the prime-divides-product property.

Factorizations also exist. Take any nonzero Gaussian nonunit. If it can be split into two nonunits, their positive integer norms are both greater than one and strictly less than the original norm. If either factor can be split, repeat. The norm cannot decrease forever through positive integers, so the process ends at irreducibles.

Once every irreducible is prime, the usual cancellation argument proves uniqueness: an irreducible from one factorization must divide an irreducible in the other, so the two differ by a unit; remove the pair and repeat. **Gaussian integers have unique factorization**, and we have derived the needed facts from their Euclidean algorithm rather than importing a general classification of rings.

We are ready to return to the ordinary primes.

## Split a prime by finding a square root of negative one

Let p be an odd prime that leaves remainder one modulo four. The earlier quadratic-residue result tells us that negative one is a square modulo p. So some ordinary integer t satisfies t squared congruent to negative one modulo p.

Regard p as a Gaussian integer on the real axis. The congruence says p divides t squared plus one, and now we can factor that expression as t plus i times t minus i. Thus p divides a product of two Gaussian integers.

But p does not divide either factor in the Gaussian integers. To divide t plus i by p with a Gaussian-integer quotient would require the imaginary coefficient one to be divisible by p in the ordinary integers. It is not. The same is true for t minus i.

If p were irreducible as a Gaussian integer, the prime-divides-product property we proved would force it to divide one of those factors. Contradiction. So p is reducible in the Gaussian integers: p equals alpha times beta, with neither factor a unit.

Take norms. The norm of the ordinary integer p is p squared. So the two positive integer norms multiply to p squared. Neither norm can be one, since the factors are nonunits. The primality of p leaves only one possibility: both norms are p. In particular, alpha has norm p. Write alpha as a plus b i. We have constructed a squared plus b squared equals p.

That completes the difficult direction. If p leaves remainder three modulo four, it cannot be a sum of two squares because two square residues never add to three. Two itself is one squared plus one squared. We have therefore proved the **two-squares theorem for primes**: an odd prime is a sum of two integer squares if and only if it leaves remainder one modulo four.

Try p equal to thirteen. Five squared is twenty-five, which is negative one modulo thirteen. In the Gaussian integers, thirteen divides five plus i times five minus i. The nontrivial Gaussian factor two plus three i has norm thirteen. Its conjugate has the same norm, and thirteen is the product of those two Gaussian factors. What first looked like a lucky pair of small squares is forced by a factorization argument.

## Classifying all positive integers that are sums of two squares

The prime case leads to a stronger theorem for composite numbers. Factor a positive integer n into ordinary primes. Then n is a sum of two integer squares **if and only if every prime leaving remainder three modulo four occurs with an even exponent**.

First, why is the condition necessary? Suppose a squared plus b squared is divisible by an odd prime p that leaves remainder three modulo four. If p did not divide b, we could divide by b squared modulo p and conclude that negative one is a square modulo p. That is impossible. So p divides b. The same equation then shows that p divides a as well. It follows that p squared divides a squared plus b squared.

Now remove that factor of p squared and repeat the argument on the smaller representation. Each time p occurs, it must occur in a pair. Therefore its exponent in n is even. The argument even handles a or b equal to zero, because the congruence still forces both divisible by p whenever p divides their sum of squares.

For sufficiency, start with the ordinary prime factorization of n. Every prime leaving remainder one modulo four is already a sum of two squares, as we proved. The prime two is also a sum of two squares. Every prime leaving remainder three modulo four appears with an even exponent, so its whole contribution is a perfect square, which is a square plus zero squared. Finally use the multiplicativity of the Gaussian norm to multiply all those representations together. Their product is n, and it is again a sum of two squares.

For example, forty-five factors as five times three squared. The prime three occurs twice, so forty-five can be represented as three squared plus six squared. In contrast, twenty-one factors as three times seven. Each of those primes leaves remainder three modulo four and appears an odd number of times. No pair of integer squares sums to twenty-one.

The theorem classifies existence, not the number of distinct representations. Counting representations with signs and order becomes a second, interesting problem. Unique Gaussian factorization allows that count as well, but we will not pretend it has been proved merely by knowing that a representation exists.

## What can go wrong in a different quadratic ring?

It is tempting to think that adjoining any square root to the integers will make another pleasant Euclidean grid. That is false. Consider the numbers a plus b square root of negative five, with a and b integers. There is still a multiplicative norm, a squared plus five times b squared. But six now has two visibly different factorizations: two times three, and one plus square root of negative five times one minus square root of negative five.

These are genuinely different factorizations into irreducibles. None of the four factors can be split into nonunits: a split would force a factor with norm two or three, but the expression a squared plus five b squared never equals two or three for integers a and b. This also shows why the ordinary division argument cannot simply be recycled. A multiplicative norm does not by itself guarantee Euclidean division, Bézout's identity, or unique factorization.

There are sophisticated repairs, including factoring ideals rather than elements, but those belong to algebraic number theory. For now we have a precise lesson: in the Gaussian integers the lattice is close enough to round in every division, and that geometric fact makes the algebraic proof work.

## Why a larger number system helped

We began with a question about ordinary integer pairs. By allowing the symbol i, the sum of two squares became a norm. The norm multiplied cleanly. The lattice admitted a division algorithm. That proved unique factorization. And unique factorization turned a modular square root of negative one into an actual representation of a prime as two squares.

One chain of arguments connects a simple clock calculation with a geometric lattice and a full classification of positive integers. Every link matters. This is one of the clearest examples of the payoff from abstract algebra: it supplies a new language in which an elementary question finally has enough structure to be solved.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

### Gaussian arithmetic and Euclidean division

\[
\mathbb Z[i]=\{a+bi:a,b\in\mathbb Z\},\quad
N(a+bi)=(a+bi)(a-bi)=a^2+b^2,\quad N(zw)=N(z)N(w).
\]

For \(\alpha,\beta\in\mathbb Z[i]\) with \(\beta\ne0\), choose \(q\in\mathbb Z[i]\) by rounding the real and imaginary parts of \(\alpha/\beta\) to nearest integers, and let \(r=\alpha-\beta q\). Then
\[
N(r)=N(\beta)\,N(\alpha/\beta-q)\le \frac12N(\beta)<N(\beta).
\]

Euclidean descent gives gcd and Bézout identities. If \(\pi\) is irreducible and divides \(\alpha\beta\) but not \(\alpha\), then \(\gcd(\pi,\alpha)\) is a unit; Bézout proves \(\pi\mid\beta\). Norm descent gives existence of irreducible factorizations, and Euclid's lemma yields uniqueness up to order and multiplication by one of \(\{\pm1,\pm i\}\).

### Fermat's theorem on two squares

For an odd rational prime \(p\):
\[
\boxed{p=a^2+b^2\ (a,b\in\mathbb Z)\iff p\equiv1\pmod4.}
\]

For \(p\equiv1\pmod4\), choose \(t\in\mathbb Z\) with \(t^2\equiv-1\pmod p\) (quadratic-residue criterion). In \(\mathbb Z[i]\),
\[
p\mid(t+i)(t-i),\qquad p\nmid(t+i),\quad p\nmid(t-i).
\]
Since irreducibles in \(\mathbb Z[i]\) are prime, the rational integer \(p\) is reducible: \(p=uv\), with \(N(u),N(v)>1\). Because \(p^2=N(p)=N(u)N(v)\), primality forces \(N(u)=N(v)=p\).

Example: \(13=(2+3i)(2-3i)\), with \(5^2\equiv-1\pmod{13}\) and \(5+i=(2+3i)(1-i)\).

### Complete criterion for any positive integer

If \(n=\prod p^{e_p}>0\), then
\[
\boxed{n=a^2+b^2\iff e_p\text{ is even for every prime }p\equiv3\pmod4.}
\]

**Necessity:** for \(p\equiv3\pmod4\), \(p\mid(a^2+b^2)\) implies \(p\mid a,b\), since \(-1\) is a quadratic nonresidue. Divide the representation by \(p^2\) and iterate. **Sufficiency:** primes \(2\) and \(1\pmod4\) are Gaussian norms, and \(p^{2k}=N(p^k)\) for every remaining prime. Multiply these norms:
\[
(a^2+b^2)(c^2+d^2)=(ac-bd)^2+(ad+bc)^2.
\]

Examples: \(45=3^2+6^2\); \(65=1^2+8^2=4^2+7^2\); \(21\) is not representable.

### Counterexample to naive factorization in quadratic rings

In \(\mathbb Z[\sqrt{-5}]\),
\[
6=2\cdot3=(1+\sqrt{-5})(1-\sqrt{-5}).
\]
The norm \(a^2+5b^2\) takes neither value 2 nor 3 for integer \((a,b)\). Hence \(2,3,1\pm\sqrt{-5}\) are irreducible and pairwise nonassociated; unique factorization into elements fails. **This does not contradict unique factorization of ideals in the full ring of integers**, a later theorem not proved here.

### Practice and reasoning checks

1. Carry out Gaussian Euclidean division of \(13\) by \(5+i\) and find a nonunit gcd.
2. Use the norm product to construct both representations of \(65\) from the representations of \(5\) and \(13\).
3. Decide whether \(18\), \(75\), \(90\), and \(325\) can each be written as sums of two squares; justify from prime exponents.
4. Explain why \(p\mid(t+i)(t-i)\) and \(p\nmid t+i,t-i\) contradict *irreducibility* of \(p\) only **after** Euclid's lemma has been established.
5. Check why the norm in \(\mathbb Z[\sqrt{-5}]\) cannot take the values 2 or 3.

### Sources and further reading

- Stanford, [Gaussian integers and sums of two squares](https://crypto.stanford.edu/pbc/notes/numberfield/sumsquares.html).
- Darij Grinberg, [Number Theory Lecture 17](https://www.cip.ifi.lmu.de/~grinberg/t/23wa/lec17.pdf), Gaussian norms and Fermat's two-squares theorem.
- University of Tennessee, [Fermat's two-square theorem](https://web.math.utk.edu/~dcartwr1/iaawa/domains-5.html), complete integer criterion.
- Wikipedia background: [Gaussian integer](https://en.wikipedia.org/wiki/Gaussian_integer), [Fermat's theorem on sums of two squares](https://en.wikipedia.org/wiki/Fermat%27s_theorem_on_sums_of_two_squares), [Euclidean domain](https://en.wikipedia.org/wiki/Euclidean_domain), [Brahmagupta–Fibonacci identity](https://en.wikipedia.org/wiki/Brahmagupta%E2%80%93Fibonacci_identity).
