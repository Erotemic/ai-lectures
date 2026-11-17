# 007000 — Gauss's Lemma and a Complete Proof of Quadratic Reciprocity

**Track:** Number Theory from First Principles. **Background:** Euclid's algorithm, congruences, the Legendre symbol and Euler's criterion. **Theme:** turning a question about squares into a count of lattice points.

<!-- BEGIN SPOKEN LECTURE -->

# Gauss's Lemma and a Complete Proof of Quadratic Reciprocity

There is a theorem that compares two questions which seem to belong to different worlds. If p and q are distinct odd primes, is p a square modulo q? And is q a square modulo p? The two lists of squares have different sizes, and there is no obvious way to transport an answer from one list to the other. Yet quadratic reciprocity says that the answers agree unless both primes leave remainder three when divided by four. In that case the answers disagree.

We have already met the theorem as a statement. This time our job is to prove it. We will not appeal to a classification of finite fields or a theorem from advanced algebra. The proof uses multiplication on a clock, a parity calculation, and a rectangle full of integer points. Each step is something we can examine directly.

## Half a clock is enough

Fix an odd prime p. Call the integer half of p minus one n. The nonzero residue classes modulo p can be paired: one with negative one, two with negative two, and so on up to n with negative n. Every nonzero residue is in exactly one such pair.

Choose an integer a that is not divisible by p. Multiply the numbers one through n by a and reduce the results modulo p. The products cannot be zero. For each product, choose its least positive residue, between one and p minus one. If that residue is bigger than p divided by two, replace it by its negative representative: subtract p. The answer now lies among positive or negative one through positive or negative n.

Here is the crucial observation. The absolute values of these signed representatives are a rearrangement of one through n. For if the absolute values of a times i and a times j were equal modulo p, either a times i would equal a times j or it would equal negative a times j. Since a is invertible modulo p, this would say that i and j are equal, or that i plus j is divisible by p. But i and j are between one and n, so i plus j is positive and less than p. Only the equality i equals j is possible.

Let m be the number of products whose least positive residues fell in the upper half of the clock, so that we had to subtract p. When we multiply all our signed representatives, their absolute values give n factorial, and their signs give negative one to the power m. On the other hand, before the sign replacements, their product was a to the power n times n factorial, modulo p. Because none of the numbers one through n is divisible by p, n factorial has a multiplicative inverse modulo p. Cancel it.

The result is that a to the power n is congruent to negative one to the power m. Euler's criterion tells us that a to the power n is exactly the Legendre sign of a modulo p. Thus we have proved Gauss's lemma: **the Legendre sign is negative precisely when the number of upper-half residues is odd**.

For a small example, use p equal to seven and a equal to three. The first half of the clock is one, two, three. Multiplying by three gives least positive residues three, six, two. Only six lies above three and a half. The count m is one, so three is a nonsquare modulo seven. You can check independently that the nonzero squares are one, two and four.

With p equal to eleven and a equal to three, the five residues are three, six, nine, one and four. Two of them are above five and a half. The sign is positive. Indeed, five squared is three modulo eleven. The lemma has replaced the search for a square root by a parity count.

## A special law for two, proved rather than guessed

Before addressing the two-prime theorem, we can settle a question about the number two. For an odd prime p, when is two a square modulo p?

Apply Gauss's lemma with a equal to two. The least positive residues of two, four, six, and so on through twice n are exactly those even numbers. None reaches p. We must count how many of the integers k from one through n satisfy two k greater than p divided by two. Equivalently, how many satisfy k greater than p divided by four. That count is n minus the greatest integer not exceeding p divided by four.

Now inspect the four possible remainders of an odd prime modulo eight: one, three, five or seven. If p leaves remainder one or seven, that count is even. If it leaves remainder three or five, the count is odd. By Gauss's lemma, **two is a square modulo p exactly when p leaves remainder one or seven modulo eight**.

For seven, three squared is two modulo seven, and seven belongs to the favorable cases. For eleven, the count is odd and two is a nonsquare. This is the supplementary law for two. Its usual compact exponent involves p squared minus one divided by eight, but the proof is simply the count of even residues in the upper half of a clock.

The companion gives the four cases explicitly. Notice that we have proved the law by counting, not by claiming that an apparent pattern in small primes must continue.

## Another way to count the same sign

Gauss's lemma counts upper-half residues. To compare two different primes, we need to express that count using ordinary integer quotients, because quotients can be interpreted as points on a grid.

There is a useful parity identity. Suppose a is odd and coprime to our odd prime p. For each k from one through n, divide a times k by p. Record the integer quotient and the least positive remainder. Add up all those quotients. Then the parity of their sum equals the parity of the upper-half count m.

Why? Each product a k equals p times its quotient plus its remainder. A remainder in the lower half becomes its signed representative unchanged; a remainder in the upper half becomes its signed representative plus p. So when we sum all the remainders, we obtain the sum of the signed representatives plus m copies of p.

Now reduce this entire sum identity modulo two. Since p is odd, copies of p count just like copies of one. The signed representatives are, up to order and sign, exactly one through n. Signs make no difference modulo two. Thus their sum has the same parity as one plus two and so on through n. The left side is a times that same sum. Because a is odd, it too has the same parity. The two copies of the familiar sum cancel, leaving a simple conclusion: the sum of the integer quotients and m have the same parity.

We have therefore proved a convenient version of Gauss's criterion. For odd a, the Legendre sign of a modulo p is negative one raised to the sum of the integer parts of a divided by p, twice a divided by p, and so on through n times a divided by p.

Check this with p equal to eleven and a equal to three. The integer parts of three over eleven, six over eleven, nine over eleven, twelve over eleven, and fifteen over eleven are zero, zero, zero, one and one. Their sum is two, agreeing with the positive Legendre sign.

The hypothesis that a is odd matters to this particular floor-sum formula. We proved the special law for two separately; we must not substitute two into an identity whose proof explicitly uses an odd multiplier.

## A rectangle divided by a line

We can finally compare the two primes. Let p and q be distinct odd primes. Take a rectangle made of integer lattice points whose horizontal coordinates run from one through half of p minus one, and whose vertical coordinates run from one through half of q minus one. In other words, there are n times r points in all, where n is half of p minus one and r is half of q minus one.

Draw a line through the origin with slope q divided by p. The line has equation: vertical coordinate equals q times horizontal coordinate divided by p. It divides our rectangle into points strictly below the line and points strictly above it.

Could a point in our rectangle lie exactly on the line? If its coordinates are i and j, equality would give p times j equal to q times i. Since p and q are distinct primes, p would have to divide i. But i is positive and smaller than p. Impossible. So every point is on exactly one side.

Count the points below. Fix a horizontal coordinate i between one and n. The vertical integers below the line are one through the integer part of q times i divided by p. Because i is at most n, this quotient is less than half of q, so all of these values fit inside our rectangle. Summing those counts over i produces exactly the quotient sum from Gauss's criterion for q modulo p. Therefore the sign of q modulo p is negative one raised to the number of points below our line.

Now count the points above. Fix a vertical coordinate j between one and r. A point is above the line when its horizontal coordinate i is smaller than p times j divided by q. There are exactly the integer part of p times j divided by q such points. Their count is the quotient sum for p modulo q. Thus the Legendre sign of p modulo q is negative one raised to the number of points above the line.

Multiplying these two signs adds the two counts in the exponent. There are no points on the line, so their sum is the total number of lattice points: n times r. That is half of p minus one, multiplied by half of q minus one. We have arrived at the quadratic reciprocity formula.

Nothing is missing from the argument: Gauss's lemma was proved by cancellation, its quotient form was proved by parity, and the rectangle was partitioned without points on its diagonal. If at least one of p or q is one modulo four, one of n or r is even, so the two Legendre signs agree. If both primes are three modulo four, n and r are odd, so the signs disagree. This is exactly the theorem we set out to establish.

## Reading the result without losing the hypotheses

Try p equal to three and q equal to eleven. The rectangle has one vertical row and five horizontal positions. Two points lie below the diagonal and three above it. One sign is positive and the other negative. Directly, three is a square modulo eleven, while eleven, which is two modulo three, is not a square modulo three. Reciprocity explains their disagreement.

The theorem concerns **distinct odd primes**. It does not directly assert an identical formula for arbitrary composite denominators, though the Jacobi symbol provides a related computational extension. Its calculation also does not produce a square root; it tells us whether a square root exists. For the separate problem of finding roots, or lifting them to higher prime powers, other arguments are required.

Quadratic reciprocity is a good example of what a proof can accomplish beyond verifying a result. It converts two apparently unrelated modular questions into the same finite combinatorial picture. The signs are no longer mysterious. They record the parity of two complementary regions of a rectangle. The decisive new idea was not a longer calculation, but a better object to count.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

### Gauss's lemma with proof

Let p be an odd prime, \(n=(p-1)/2\), and \(p\nmid a\). For \(1\le k\le n\), let \(r_k\) be the least positive residue of \(ak\) modulo p. Define \(m=\#\{k:r_k>p/2\}\). The signed residues

\[
s_k=\begin{cases}r_k,&r_k<p/2,\\r_k-p,&r_k>p/2\end{cases}
\]

have absolute values \(1,\ldots,n\) exactly once. Thus

\[
a^n n!\equiv\prod_{k=1}^n s_k=(-1)^m n!\pmod p.
\]

Cancellation is valid because \(p\nmid n!\). Euler's criterion then gives

\[
\boxed{\left(\frac ap\right)=(-1)^m.}
\]

### The supplementary law for two

For \(a=2\), \(r_k=2k\) and \(m=n-\lfloor p/4\rfloor\). The residue classes give:

| \(p\bmod 8\) | \(n\) | \(\lfloor p/4\rfloor\) | \(m\) parity | \((2/p)\) |
|---|---|---|---|---|
| \(8t+1\) | \(4t\) | \(2t\) | even | +1 |
| \(8t+3\) | \(4t+1\) | \(2t\) | odd | -1 |
| \(8t+5\) | \(4t+2\) | \(2t+1\) | odd | -1 |
| \(8t+7\) | \(4t+3\) | \(2t+1\) | even | +1 |

Equivalently \(\left(\frac2p\right)=(-1)^{(p^2-1)/8}\).

### Floor-sum lemma for odd multipliers

For odd \(a\) with \(p\nmid a\), let \(h_k=\lfloor ak/p\rfloor\) and \(S=\sum_{k=1}^n h_k\). Since \(ak=ph_k+r_k\), and \(r_k=s_k+p\,1_{\{r_k>p/2\}}\), summing modulo two gives

\[
a\sum_{k=1}^n k\equiv S+\sum_{k=1}^n s_k+m\equiv S+\sum_{k=1}^n k+m\pmod2.
\]

The first and last sums of k have the same parity because a is odd. Hence \(S\equiv m\pmod2\), and

\[
\boxed{\left(\frac ap\right)=(-1)^{\sum_{k=1}^{(p-1)/2}\lfloor ak/p\rfloor}}
\qquad(a\text{ odd},\ \gcd(a,p)=1).
\]

### Quadratic reciprocity from the rectangle

For distinct odd primes \(p,q\), set \(n=(p-1)/2\), \(r=(q-1)/2\). Consider the \(nr\) lattice points \(1\le i\le n,1\le j\le r\). No point satisfies \(pj=qi\), since that would force \(p\mid i\) for \(0<i<p\).

Define the below-line count and above-line count:

\[
B=\sum_{i=1}^{n}\left\lfloor\frac{qi}{p}\right\rfloor,
\qquad
A=\sum_{j=1}^{r}\left\lfloor\frac{pj}{q}\right\rfloor.
\]

Both floor sums are valid counts *inside* the rectangle, since \(qi/p<q/2\) and \(pj/q<p/2\) in the respective ranges. Exactly one count contains each point, so \(A+B=nr\). Gauss's floor criterion applied separately to the odd integers q and p yields

\[
\boxed{\left(\frac qp\right)\left(\frac pq\right)
=(-1)^{A+B}=(-1)^{\frac{p-1}{2}\frac{q-1}{2}}.}
\]

**Proof status:** the lecture proves Gauss's lemma, the second supplementary law, the floor-sum identity (under its necessary oddness hypothesis), and quadratic reciprocity in full for distinct odd primes. It uses Euler's criterion from lecture 006000 and does not prove general Jacobi reciprocity or algorithms for finding square roots.

### Practice and reasoning checks

1. Apply Gauss's lemma with \(p=13\) and \(a=2\); list all six least positive residues and count those above \(13/2\).
2. Verify quadratic reciprocity for \(p=7,q=11\) by comparing the two Legendre symbols and the rectangle counts.
3. Identify the precise step where an odd multiplier is required for the floor-sum lemma; explain why using the formula with \(a=2\) may fail.
4. Prove that if two residue classes have the same absolute representative among \(1,\ldots,(p-1)/2\), their original multipliers agree.
5. For a prime \(p\equiv3\pmod4\), use the two supplementary laws to determine \(\left(\frac{-2}{p}\right)\) for both possible residues of p modulo eight.

### Sources and further reading

- MIT OpenCourseWare, [*18.781 Theory of Numbers*, quadratic residues and reciprocity lecture notes](https://ocw.mit.edu/courses/18-781-theory-of-numbers-spring-2012/resources/mit18_781s12_lec9/).
- Stanford pairing-based cryptography notes, [Quadratic Reciprocity](https://crypto.stanford.edu/pbc/notes/numbertheory/quadrecip.html): a Gauss criterion and Eisenstein rectangle proof.
- William Stein, [*Elementary Number Theory: Primes, Congruences, and Secrets*](https://www.wstein.org/ent/).
- Wikipedia orientation: [Gauss's lemma (number theory)](https://en.wikipedia.org/wiki/Gauss%27s_lemma_(number_theory)), [Quadratic reciprocity](https://en.wikipedia.org/wiki/Quadratic_reciprocity), [Legendre symbol](https://en.wikipedia.org/wiki/Legendre_symbol).
