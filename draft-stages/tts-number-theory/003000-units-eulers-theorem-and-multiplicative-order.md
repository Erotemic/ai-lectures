# 003000 — Units, Euler's Theorem, and Multiplicative Order

**Track:** Number Theory from First Principles. **Background:** modular arithmetic, GCDs, and modular inverses. **Theme:** why powers repeat and when repeating powers prove anything.

<!-- BEGIN SPOKEN LECTURE -->

# Units, Euler's Theorem, and Multiplicative Order

What happens if we keep multiplying by the same number on a clock? Modulo seven, powers of two begin with two, four, one, and then repeat: two, four, one. Modulo fifteen, the powers of two go two, four, eight, one and repeat. How can we know that a repeating cycle must appear, and how long might we need to wait before reaching one?

The answer depends on which residue classes can be undone by multiplication. These are called units. Their behavior connects basic arithmetic to finite groups, gives us Euler's theorem and Fermat's little theorem, and explains both the power and the limits of elementary primality tests.

## Which remainders can be multiplied backwards?

Take arithmetic modulo ten. The classes one, three, seven, and nine have multiplicative inverses. The classes zero, two, four, five, six, and eight do not. Why this division? Exactly the first four are coprime with ten. Any number sharing a factor with ten cannot multiply to a remainder of one, because that common factor would then divide one.

The invertible classes modulo n form a finite set closed under multiplication, containing one, with an inverse for each element. This set is often denoted by a star over the integers modulo n. Multiplication is associative because ordinary integer multiplication is. These properties make the set a group, though we do not need abstract group theory to calculate with it.

Euler's totient function, pronounced phi, counts these units. Phi of ten is four. Phi of seven is six because every nonzero class modulo a prime is invertible. Phi of twelve is four, with units one, five, seven, and eleven.

Can we compute phi without inspecting each remainder? Start with a prime power. A number fails to be coprime with p to the k exactly when it is divisible by p. Among the p to the k residue classes, one in every p is divisible by p. Thus phi of p to the k is p to the k minus p to the k minus one. For a general positive integer n, unique factorization and the Chinese remainder theorem tell us that a class is a unit modulo n precisely when it is a unit modulo each of its prime-power factors. Therefore phi of n is n multiplied by one minus one over p for every distinct prime p dividing n.

For example, fifteen has the two prime factors three and five. Phi of fifteen is fifteen times two-thirds times four-fifths, which is eight. The units are one, two, four, seven, eight, eleven, thirteen, and fourteen.

## Euler's theorem from a permutation

Suppose a is coprime with n. Multiply every unit modulo n by a. Since a has an inverse, this multiplication sends units to units and never maps two distinct units to the same output. In a finite set, a one-to-one self-map is a permutation. It merely rearranges the list.

Now multiply all the units together in two ways: once in the original list, and once after every unit has been multiplied by a. Because the second list is a permutation of the first, the two products are congruent modulo n. But the second product is the first product times a raised to the number of units, which is phi of n.

We may cancel the product of all the units, because that product is itself a unit. What remains is the congruence that a raised to phi of n equals one modulo n. This is Euler's theorem.

Listen for the hypotheses: n is a positive modulus and a is coprime to n. Without the coprimality assumption, multiplication by a need not permute the unit classes, and the cancellation argument breaks. Try a equal to three modulo nine. Phi of nine is six, but three to the sixth is divisible by nine rather than congruent to one.

For a prime p, phi of p is p minus one. Euler's theorem becomes Fermat's little theorem: if p does not divide a, then a raised to p minus one is congruent to one modulo p. There is also a form that works for every integer a: a raised to p is congruent to a modulo p. When p divides a, both sides are zero. Otherwise multiply Fermat's congruence by a.

These statements do not require advanced abstract algebra. The essential observation was a finite permutation, and the proof came from multiplying the same collection in two orders.

## The exact length of a power cycle

Euler's theorem tells us a power returns to one eventually. It does not tell us the first time. The multiplicative order of a modulo n, when a is a unit, is the smallest positive exponent r for which a raised to r is congruent to one.

Modulo seven, the order of two is three: two squared is four, two cubed is one. Modulo fifteen, the order of two is four. By contrast, the order of fourteen modulo fifteen is two, because fourteen squared is one. Different units in the same arithmetic system can have different cycle lengths.

The order always divides phi of n. Here is why. Let r be the first return exponent. Divide phi of n by r, obtaining a quotient q and a remainder s between zero and r minus one. Euler's theorem says a raised to phi of n is one. Since a raised to r is one, the same equality says a raised to s is one. If s were positive, it would contradict minimality of r. Therefore s is zero. The order divides phi of n.

This proof works more generally: if a power of a unit equals one, its order divides that exponent. So testing divisors of phi is often more efficient than testing every possible exponent. Order is a precise mathematical version of the period of a repeating multiplication process.

## Why a passing test need not mean prime

Fermat's little theorem gives a necessary condition for primality. If n is prime and coprime to a, then a raised to n minus one is one modulo n. It is tempting to reverse this and say that a number passing the test is prime. That reversal is false.

Consider three hundred forty-one. It equals eleven times thirty-one, so it is composite. Yet two raised to the tenth is one thousand twenty-four, which is three times three hundred forty-one plus one. Thus two raised to the tenth is congruent to one modulo three hundred forty-one. Raise both sides to the thirty-fourth power: two raised to three hundred forty is also congruent to one. Our composite number passes the base-two Fermat test.

We call such a number a pseudoprime to the chosen base. This is a lesson in the logical direction of an implication. Every prime satisfying the coprimality condition passes Fermat's test; passing the test does not establish primality. More sophisticated primality tests use additional conditions or different mathematical arguments. Compositeness can also be certified directly, as we did by exhibiting two nontrivial factors.

Conversely, if n greater than one is coprime with a and the power test fails, n definitely is composite. One-sided evidence is still useful evidence, provided we remember which side is justified.

## A calculation behind public-key arithmetic

The same periodicity idea explains a basic ingredient of R S A arithmetic. Choose two distinct primes p and q, and let n be their product. Choose positive exponents e and d whose product is congruent to one modulo phi of n. For any message represented by a residue class coprime with n, Euler's theorem implies that raising first to e and then to d returns the original class.

Why? Their exponent product has the form one plus k times phi of n. So the resulting power is the original message times a power of the Euler quantity that equals one. The computation happens modulo n. This establishes the algebraic round trip for units.

For squarefree n equal to two distinct primes, a stronger statement handles messages that are not units: check the power separately modulo p and q. If a message is zero modulo one of these primes, both the original and the powered version are zero there. If not, Fermat's theorem applies, because e times d is one modulo p minus one and modulo q minus one. The Chinese remainder theorem then recombines the equalities. This is a proof about modular exponentiation, not a proof that a particular cryptographic configuration is secure.

Security requires much more: parameter choices, padding, a precise adversary model, and implementation discipline. The mathematical calculation gives correctness under specified hypotheses. It does not, by itself, give secrecy or authentication.

## A group idea hiding inside arithmetic

We have moved from remainders to invertible remainders, from finite permutations to a general power theorem, and from a theorem about powers to questions of order and primality. The underlying group idea is already visible: multiplication is an operation with an identity and inverses, and repeated applications of the operation trace a finite cycle.

This matters because number theory repeatedly uses algebra without making algebra feel like an extra layer of vocabulary. One can first discover that the units modulo n behave in a structured way, then recognize the general pattern in matrix multiplication, symmetries, and transformations. Concrete modular arithmetic is one place where group theory earns its keep.

The central conclusion is simple to say but rich in consequences: invertible remainders form a finite world, and multiplication by one of them only permutes that world. Euler's theorem captures that finiteness. Multiplicative order measures the precise cycle. Their counterexamples teach us which inferences are licensed—and which are not.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

### Definitions and derivations

The unit group and Euler totient are

\[
(\mathbb Z/n\mathbb Z)^\times=\{[a]:\gcd(a,n)=1\},\qquad
\varphi(n)=\#(\mathbb Z/n\mathbb Z)^\times.
\]

For \(n=\prod_{i=1}^k p_i^{e_i}\),

\[
\varphi(n)=\prod_i(p_i^{e_i}-p_i^{e_i-1})=n\prod_{p\mid n}(1-1/p).
\]

Euler's theorem: \(\gcd(a,n)=1\Rightarrow a^{\varphi(n)}\equiv 1\pmod n\). For prime \(p\), this reduces to \(a^{p-1}\equiv1\pmod p\) if \(p\nmid a\), hence \(a^p\equiv a\pmod p\) for all \(a\).

If \(r=\operatorname{ord}_n(a)\), and \(a^k\equiv1\pmod n\), division of \(k=qr+s\), \(0\le s<r\), gives \(a^s\equiv1\), hence \(s=0\). Thus \(r\mid k\) and in particular \(r\mid\varphi(n)\).

The pseudoprime calculation is \(341=11\cdot31\), \(2^{10}=1024=3\cdot341+1\), so \(2^{340}=(2^{10})^{34}\equiv1\pmod{341}\).

### Practice and reasoning checks

1. Find the units modulo twelve and their inverses. Show directly that Euler's theorem works for each.
2. Compute phi of thirty-six from its prime factors, then count directly as a check.
3. Find the order of three modulo seven, and compare it with phi of seven.
4. Explain why Fermat's test is a sound *compositeness witness* when it fails but not a sound *primality certificate* when it passes.
5. State which RSA round-trip steps rely on Euler's theorem, which rely on Fermat's theorem, and which rely on the Chinese remainder theorem.

### Sources and further reading

- MIT OpenCourseWare, *18.781 Theory of Numbers*, lectures 4 and 6–8: Fermat, Euler, units, orders, and primitive roots: https://ocw.mit.edu/courses/18-781-theory-of-numbers-spring-2012/pages/lecture-notes/
- William Stein, *Elementary Number Theory: Primes, Congruences, and Secrets*, chapters on modular integers and public-key arithmetic: https://www.wstein.org/ent/
- Wikipedia background: [Euler's theorem](https://en.wikipedia.org/wiki/Euler%27s_theorem), [Euler's totient function](https://en.wikipedia.org/wiki/Euler%27s_totient_function), [Multiplicative order](https://en.wikipedia.org/wiki/Multiplicative_order), [Fermat pseudoprime](https://en.wikipedia.org/wiki/Fermat_pseudoprime).
