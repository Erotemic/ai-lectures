# 030750 — The p-adic Integers as Compatible Residues

**Track:** Number Theory from First Principles. **Background:** 030250–030500, modular arithmetic and the Chinese remainder theorem. **Aim:** prove Z_p is the inverse limit of prime-power residue rings, identify its ideals and units, and prove compactness and local compactness.

<!-- BEGIN SPOKEN LECTURE -->

# The p-adic Integers as Compatible Residues

Imagine you have solved a congruence modulo five, then modulo twenty-five, then modulo one hundred and twenty-five, and so on. A solution at one stage does not automatically determine a solution at the next. But suppose you have chosen a solution at *every* stage, and that each new solution reduces to the one previously chosen. Do these infinitely many pieces of finite arithmetic assemble into a single number?

For the p-adic integers, the answer is yes. The result is not merely a useful metaphor. It is an isomorphism between a ring of completed numbers and a ring built entirely out of compatible finite residue systems.

Let us recall that Z-p is the set of p-adic numbers with absolute value at most one. These numbers have no negative powers of p in their canonical digit expansions. Every x in Z-p can be reduced modulo p to the n by taking its first n base-p digits and interpreting them as an ordinary integer between zero and p to the n minus one. When we reduce that representative further modulo p to the n minus one, we get exactly the representative from the previous stage.

So each p-adic integer determines a sequence: a residue modulo p, a residue modulo p squared, a residue modulo p cubed, and onward, with a compatibility condition. Our task is to prove the converse, then study the ring through that description.

## What compatibility means

For each positive integer n, take a residue r n modulo p to the n. We require r at level n plus one to reduce to r at level n. This means that if we use integer representatives, their difference is divisible by p to the n. Such sequences can be added and multiplied coordinate by coordinate: reduce the sums or products at each level. Compatibility is preserved, since reduction is a ring homomorphism.

The set of all compatible sequences is called the inverse limit of the rings of integers modulo p to the n. The name emphasizes that information flows backward from a finer modulus to a coarser modulus. No abstract category theory is needed to use the construction; one only needs the collection of finite rings and the reduction maps connecting them.

Given compatible residues, choose for each n an integer representative a n. Compatibility says that a n plus one minus a n is divisible by p to the n. More generally, for every later m, a m minus a n is divisible by p to the n. Therefore the integer representatives form a p-adic Cauchy sequence. Its limit exists in Q-p, and because the representatives are ordinary integers with p-adic absolute value at most one, their limit also has absolute value at most one. Thus it lies in Z-p.

Different choices of representatives differ by multiples of p to the corresponding powers, so they give the same limit. Conversely, the limit recovers the original residue at every level. We have proved that Z-p is exactly the ring of all compatible residues. Every coherent infinite system defines one p-adic integer, and every p-adic integer gives one coherent system.

This is much stronger than saying a solution exists modulo every p to the n, without any relation among the chosen solutions. A compatible sequence must be selected. Later, compactness will tell us when compatible choices can be extracted from the mere existence of solutions at all finite levels.

## A familiar negative number with infinitely many digits

Consider negative one. Modulo p it is represented by p minus one. Modulo p squared it is represented by p squared minus one. The representatives continue with p cubed minus one and so on. Their base-p expansions have every digit equal to p minus one.

At first this may appear to create a strange new number. It does not: the resulting p-adic integer is the ordinary rational number negative one, embedded in the completion. The partial digit sum is p to the n minus one, and the difference between this sum and negative one is p to the n, whose p-adic absolute value tends to zero. An infinite string of maximal digits is therefore a perfectly ordinary negative integer in p-adic notation.

Likewise, the inverse of three in Z-five begins with the compatible residues two, seventeen, forty-two, four hundred seventeen, and so on. The inverse exists because three is not divisible by five. In the infinite residue system, multiplying each coordinate by three yields the residue one at every level. The resulting p-adic integer is precisely the rational one third.

## Which elements can be inverted?

An element x of Z-p is a unit if and only if its first digit is nonzero, or equivalently if its residue modulo p is not zero. One direction is immediate: if x times y equals one, then their first residues multiply to one in the field of p elements, so neither can be zero.

For the other direction, suppose x has nonzero residue modulo p. Its p-adic valuation is zero. Because x is nonzero in the field Q-p it has a reciprocal. The reciprocal has valuation zero as well, so it belongs to Z-p. In the inverse-limit picture, its coordinates are simply the inverses of x modulo each p to the n. Those inverses exist because x is coprime to p.

Every nonunit of Z-p is divisible by p, and every multiple of p is a nonunit. Thus the nonunits form one ideal, p times Z-p. It is the unique maximal ideal, because the quotient Z-p modulo p is the field with p elements. This makes Z-p a *local ring* in the algebraic sense: there is just one maximal ideal.

More is true. A nonzero p-adic integer has a finite nonnegative valuation k, so it equals p to the k times a unit. Let I be any nonzero ideal in Z-p. Among the valuations of its nonzero elements, choose the smallest; that is possible because nonnegative integers are well ordered. Let x in I have that smallest valuation, say k. Since x is a unit times p to the k, the ideal I contains p to the k. Every element of I has valuation at least k, so I is contained in the ideal generated by p to the k. Therefore I is exactly p to the k times Z-p.

Every nonzero ideal is a power of the maximal ideal. In particular, Z-p is a discrete valuation ring, and its fraction field is Q-p. To see the fraction-field claim, take a nonzero p-adic number x with possibly negative valuation. Multiply it by a large enough power of p to obtain a p-adic integer. Then x is a fraction of two p-adic integers.

This is the completed counterpart of the local discrete valuation rings built by localization in the earlier algebraic lectures. They share the exponent arithmetic, but only Z-p comes with all its p-adic Cauchy limits.

## Why Z-p is compact

The inverse-limit description gives us a useful finiteness theorem inside an infinite ring. Take any sequence of p-adic integers. Modulo p there are only p possible residues. At least one residue occurs infinitely often; keep that infinite subsequence. Within that subsequence there are only p squared possible residues modulo p squared, so again choose a residue occurring infinitely often and keep a further subsequence. Continue for all powers of p.

Choose one term sufficiently far along from each nested infinite subsequence, with indices increasing. The selected diagonal subsequence has the property that, for every fixed n, all sufficiently late selected terms agree modulo p to the n. In the p-adic metric, it is Cauchy. Z-p is complete as a closed subset of the complete field Q-p, so it converges to a p-adic integer.

We have shown that every sequence in Z-p has a convergent subsequence. For metric spaces, this is equivalent to compactness. Thus Z-p is compact. If that theorem about metric spaces is unfamiliar, the practical conclusion is already substantial: every infinite sequence of p-adic integers has some subsequence that converges p-adically.

A closed ball in Q-p is a translate of p to the k times Z-p for some integer k, once its radius is adjusted to an attainable value. Translation and multiplication by a nonzero p-adic number are homeomorphisms, so these balls are compact too. This is why Q-p is called a *local field*: it is a topological field with a compact neighborhood around each point. It is not compact as a whole, because the powers p to negative n escape every bounded ball.

Compactness also bridges finite congruences and exact equations. Suppose an equation f of x equals zero has at least one solution modulo every power of p, with no compatibility specified. For a polynomial in one variable, choose representatives of solutions in Z-p. By compactness, a subsequence converges to some x. Given a fixed power p to the n, the late chosen representatives need not all solve a *fixed* congruence at that level unless their original moduli are large enough; choose them with increasing modulus. They then satisfy the congruence modulo p to the n, and continuity of f shows the limit does as well. Since this works for every n, f of x equals zero. For polynomial equations in finitely many variables, the same argument works in the compact product Z-p to the d.

Notice the limit of this assertion: it is about solutions in Z-p, not necessarily integer solutions in Z. Compatibility or compactness may deliver a genuinely p-adic number rather than an ordinary rational or integer.

## Why the prime matters

What would happen if we tried the same construction with powers of ten? The Chinese remainder theorem identifies integers modulo ten to the n with pairs of residues, one modulo two to the n and one modulo five to the n. Taking compatible systems produces a product ring, Z-two times Z-five. This ring has zero divisors: the nonzero pairs one comma zero and zero comma one multiply to zero. It is not a discrete valuation ring and has no single fraction field analogous to Q-p.

That contrast is why this course fixed a *prime* at the beginning. Powers of a prime form one indivisible chain of arithmetic precision. Their inverse limit is a local integral domain with a single maximal ideal. Composites with several different prime factors split into several independent local directions.

We have now arrived at the same ring by three routes: completion of the rational integers, infinite base-p digits, and compatible residues modulo powers of p. The agreement is a theorem, not an analogy. It allows us to trade among geometric convergence, finite modular calculations, and ring theory, choosing whichever language makes an argument simplest.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Write A_n=Z/p^n Z and let A_{n+1}->A_n be reduction. Then

\[
\mathbb Z_p\cong\varprojlim_n A_n
=\{(r_n)_{n\ge1}:r_{n+1}\bmod p^n=r_n\}.
\]

### Proof map

1. **Surjectivity:** choose representatives a_n∈{0,...,p^n-1}. For m>=n, a_m≡a_n mod p^n, hence |a_m-a_n|_p<=p^{-n}. Their Cauchy limit lies in Z_p.
2. **Injectivity:** if every residue of x is zero, |x|_p<=p^{-n} for all n, so x=0. Reductions respect ring operations.
3. **Units:** Z_p^×={x:v_p(x)=0}={x:x modp ≠0}. Maximal ideal pZ_p, quotient F_p.
4. **All ideals:** for nonzero I⊆Z_p, k=min{v_p(x):x∈I\{0}}. Then p^k∈I because a minimal-valuation element is p^k times a unit, and I⊆p^k Z_p. So I=p^k Z_p.
5. **Compactness:** nested infinite subsequences fixed successively mod p^n give a Cauchy diagonal; completeness yields a convergent subsequence. In metric spaces sequential compactness implies compactness.
6. **Compactness and solvability:** let f∈Z_p[X_1,...,X_d] and suppose it has a solution in (Z/p^n Z)^d for every n. Choose Z_p representatives z_n of such solutions, and a convergent subsequence z_{n_j}->z with n_j increasing. For every fixed m and all sufficiently large j, f(z_{n_j})∈p^m Z_p. By continuity f(z)=0. This does *not* assert existence in Z^d.
7. **Composite base:** lim Z/10^n Z≅Z_2×Z_5 by the Chinese remainder theorem, so the ring has zero divisors.

### Examples

- In Z_5, -1 has digit sequence (4,4,4,...).
- In Z_5, 1/3 has residues 2 mod5, 17 mod25, 42 mod125, 417 mod625.
- The only ideals in Z_3 are (0), Z_3, 3Z_3, 9Z_3, 27Z_3, and so on.
- A compactness consequence: a polynomial in finitely many variables with integral p-adic coefficients is solvable in Z_p iff it is solvable modulo p^n for every n. (The reverse implication follows by reduction.)

### Exercises

1. Verify that coordinatewise multiplication on coherent residues is well-defined.
2. Show the first digit being nonzero characterizes a unit in the inverse limit.
3. Prove directly, without invoking Noetherianity, that every nonzero ideal of Z_p is generated by p to a power.
4. Explain the diagonal compactness construction using p=2 and the first three levels.
5. Use CRT to exhibit two nonzero zero divisors in the ten-adic inverse limit.

### Reading and source notes

- Andrew V. Sutherland, MIT 18.785, [Lecture 8](https://math.mit.edu/classes/18.785/2021fa/LectureNotes8.pdf), inverse limits, valuations and completions.
- Andrew V. Sutherland, MIT 18.785, [Lecture 9](https://math.mit.edu/classes/18.785/2021fa/LectureNotes9.pdf), local fields and compact balls.
- Wikipedia: [p-adic integer](https://en.wikipedia.org/wiki/P-adic_number), [Inverse limit](https://en.wikipedia.org/wiki/Inverse_limit), [Profinite group](https://en.wikipedia.org/wiki/Profinite_group), [Local field](https://en.wikipedia.org/wiki/Local_field).
