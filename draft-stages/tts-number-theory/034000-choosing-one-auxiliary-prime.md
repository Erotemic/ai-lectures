# 034000 — The Auxiliary Prime: Matching Local Values with One Rational Number

**Track:** Number Theory from First Principles. **Background:** 002000 (CRT), 022000 (Dirichlet's theorem), 031250 (local square classes), 033750 (common-value lemma and all-but-one ternary principle). **Aim:** prove the exact rational square-class interpolation lemma used in Hasse–Minkowski, with no unaccounted extra primes.

<!-- BEGIN SPOKEN LECTURE -->

# The Auxiliary Prime: Matching Local Values with One Rational Number

Our next task sounds modest: we have chosen a nonzero number in Q-two, another in Q-three, perhaps a few more in other p-adic fields, and a positive or negative number over the reals. We want to replace this collection by one nonzero rational number. But not just any rational number will do. It must agree with each local target up to multiplication by a square, and its prime factorization must remain controlled.

This is a form of arithmetic approximation. We will not approximate the local numbers digit for digit. We will match something coarser but exactly suited to quadratic forms: their square classes. For a nonzero local number, multiplying by a square does not change whether a quadratic form represents it. If a form represents t, it represents t times any nonzero square, simply by scaling the representing vector.

The construction will use the Chinese remainder theorem and Dirichlet's theorem on primes in arithmetic progressions. Those results were proved earlier in this course for quite different reasons. Here they become the mechanism that joins local arithmetic to a global quadratic equation.

## The problem with a naive Chinese remainder solution

Suppose we have a finite set S of primes and, for each p in S, a nonzero local scalar t-sub-p. We could prescribe several p-adic digits of a rational integer and solve the resulting congruences by the Chinese remainder theorem. This would make a rational number close to the local targets. It could also introduce an arbitrary collection of prime divisors outside S.

That is dangerous. Later we will need to test a ternary form at primes not in S. At an odd prime where all its coefficients are units, that test is automatic. But if our chosen rational number is divisible by many new primes, we create many new places where the coefficient is not a unit. Ordinary Chinese remaindering does not prevent this.

We therefore give the new rational number a very special shape: a fixed product of primes already in S, times one new prime q, and perhaps a minus sign. The auxiliary prime q will be the only uncontrolled place. In the next lecture Hilbert reciprocity will dispose of that single missing condition.

## First fix the valuations

Recall the square-class structure of a p-adic field. Two nonzero elements of Q-p have the same square class if and only if their valuation difference is even and their unit parts differ by a unit square. At an odd prime, unit squareness is decided modulo p. At the prime two, it is decided modulo eight.

For every p in S, examine the integer valuation of t-sub-p and record its parity, either zero or one. Call that parity epsilon-sub-p. Form the rational integer A by multiplying all primes p in S raised to epsilon-sub-p. This uses only exponent zero or one. Its p-adic valuation has the same parity as the valuation of the desired t-sub-p.

We will choose the final rational number to have the form s times A times q, where s is a sign, plus or minus one, and q is a positive prime not belonging to S. Set s equal to the desired real sign. Then the final rational number automatically agrees with the prescribed real square class: a positive real number is a square times any other positive real number, and the same holds for the negative class.

At each p in S, q will be a unit because q is not p. Thus the valuation parity of our candidate at p is exactly epsilon-sub-p, as desired. We have reduced all remaining conditions to conditions on the residue of q.

## Odd primes in the set

Fix an odd p in S. Divide t-sub-p by the exact power of p in its valuation; call the result u-sub-p. It is a p-adic unit. Also divide A by p to the power epsilon-sub-p; call that remaining product A-sub-p. It is an ordinary integer not divisible by p.

The ratio of our candidate s A q to t-sub-p has even p-adic valuation. For the ratio to be a square, its unit part must be a quadratic residue modulo p. Equivalently, we can require the residue of s times A-sub-p times q to equal the residue of u-sub-p, up to a square.

We have complete freedom to make a stronger choice: require their unit residues to be exactly equal modulo p. Because s and A-sub-p are units, this specifies one nonzero residue class for q modulo p. It is a perfectly legitimate residue class for Dirichlet's theorem.

There is no hidden compatibility problem between different odd primes. Each condition is stated modulo a different prime, and the Chinese remainder theorem will combine them.

## The prime two

At two, unit square classes are not determined by reduction modulo two. Every odd unit reduces to one modulo two, but there are four distinct unit square classes. We must work modulo eight.

Let u-sub-two be the odd unit obtained by removing the exact power of two from t-sub-two. Let A-sub-two be A with its possible factor of two removed. Both A-sub-two and u-sub-two are odd. We require s times A-sub-two times q to be congruent to u-sub-two modulo eight.

This fixes one odd residue class for q modulo eight. By the two-adic square criterion from our earlier lecture, matching this residue makes the unit ratio a square in Q-two. Together with the even valuation difference, this gives the desired square-class equality at two.

The instruction to use modulo eight is indispensable. A modulo-two requirement would impose no constraint at all on an odd q and could leave the wrong square class.

## Combining the conditions into one prime

Form the modulus M by multiplying eight by every odd prime in S. For each odd prime in S we have selected a nonzero residue for q; modulo eight we have selected an odd residue. The Chinese remainder theorem supplies a unique class modulo M satisfying all these prescriptions.

That class is coprime to M. Dirichlet's theorem says that infinitely many positive primes lie in any residue class coprime to the modulus. Choose one such prime q outside S. In fact, because the primes in S all divide M, and the chosen residue is a unit modulo M, every prime in that class automatically lies outside S except for trivial possibilities that the congruence excludes.

Take t equal to s A q. Its sign is right. Its valuation parity is right at every p in S. Its unit square class is right at every p in S. And its prime factors outside S consist of just q.

This is the interpolation lemma we need. It is stronger than the simple assertion that rationals are dense in the product of finitely many local fields: it controls almost the entire prime factorization of the chosen rational number.

## A fully worked choice

Let's prescribe a positive real value, a two-adic value in the square class of five, and a three-adic value in the square class of six. Our set S is two and three.

The valuation of five at two is zero, while the valuation of six at three is one. Thus epsilon-sub-two is zero, epsilon-sub-three is one, and A is three. We seek t equal to three times an auxiliary prime q.

At two, we need three q congruent to five modulo eight. The inverse of three modulo eight is three, so q must be congruent to seven modulo eight.

At three, we need the unit part of t to be in the square class of the unit part of six, namely two. The unit part of three q is q; choose q congruent to two modulo three.

The Chinese remainder theorem combines these into q congruent to twenty-three modulo twenty-four. Twenty-three itself is prime, so we can take q equal to twenty-three and t equal to sixty-nine.

Check the result. Sixty-nine is congruent to five modulo eight, exactly the two-adic unit class we requested. At three it has valuation one, and after dividing by three its unit residue is twenty-three, congruent to two modulo three. The real sign is positive. The only prime factor outside our original set is twenty-three.

This numerical example captures the general construction. Nothing about the values five and six was special; all local targets reduce to valuation parity and a short unit residue condition.

## Why Dirichlet's theorem enters the global proof

We can now see why the number theory curriculum developed prime distributions before local quadratic forms. We need a new prime in a specified congruence class, not merely an integer in that class. A composite integer could have many different prime divisors, and each would threaten to add another local obstruction.

Dirichlet's theorem lets us store all that unwanted complexity at one auxiliary place. The all-but-one-place ternary theorem then says that a single unverified place cannot prevent the ternary equation from having a rational solution.

We should be precise about what we have, and what we do not have. The interpolation lemma does not say that the chosen number is close to each t-sub-p as a p-adic number. It says their ratio is a square, which is all the representation problem needs. It does not give a small prime q, and the proof is not designed as an efficient search algorithm. Its purpose is existence with controlled prime support.

In the next lecture the pieces will finally be assembled. We will split an n-variable quadratic form, choose the local common values, apply this interpolation lemma, solve a ternary equation globally, and use induction on the remaining dimension. That is the complete Hasse–Minkowski argument over the rationals.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

**Auxiliary-prime square-class interpolation.** Let \(S\) be a finite set of primes containing 2, and let \(t_p\in\mathbb Q_p^\times\) be specified for each \(p\in S\). Let \(s\in\{+1,-1\}\) be a prescribed real sign. There exists a rational \(t=sAq\), where \(A=\prod_{p\in S}p^{\epsilon_p}\), \(\epsilon_p\equiv v_p(t_p)\pmod2\) with \(\epsilon_p\in\{0,1\}\), and \(q\notin S\) is a positive prime, such that \(t/t_p\in\mathbb Q_p^{\times2}\) for every \(p\in S\).

**Proof:** Let \(u_p=t_p/p^{v_p(t_p)}\in\mathbb Z_p^\times\) and \(A_p=A/p^{\epsilon_p}\). At odd \(p\in S\), impose

\[
 q\equiv u_p(sA_p)^{-1}\pmod p.
\]

At \(p=2\) impose the analogous congruence modulo 8, using the odd unit residue of \(u_2\). These are unit congruence classes. CRT gives a unit residue class \(q\equiv r\pmod{M}\), where \(M=8\prod_{p\in S,\,p\text{ odd}}p\). Dirichlet's theorem produces a positive prime \(q\equiv r\pmod M\). By local square criteria, \(t/t_p\) has even valuation and square unit part at every \(p\in S\). Only \(q\) can divide \(t\) outside \(S\).

**Example:** \(S=\{2,3\}\), \(t_2=5\), \(t_3=6\), positive sign. Then \(A=3\), \(q\equiv7\pmod8\), \(q\equiv2\pmod3\), so choose \(q=23\), \(t=69\). The ratios \(69/5\in\mathbb Q_2^{\times2}\) and \(69/6\in\mathbb Q_3^{\times2}\).

### Exercises

1. Repeat the worked example for a prescribed negative real sign. Find a suitable prime \(q\).
2. Explain why \(q\equiv r\pmod M\), with \(r\) coprime to \(M\), excludes every prime divisor of \(M\).
3. Show that if a form \(Q\) represents \(t_p\) over \(\mathbb Q_p\), then it represents every scalar in \(t_p\mathbb Q_p^{\times2}\).
4. Explain why merely applying CRT to choose an integer with the local residues does not provide the single-exception property.

## Sources and reading

- John Voight, *Quaternion Algebras*, section 14.3 (auxiliary prime selected using Dirichlet's theorem): https://link.springer.com/chapter/10.1007/978-3-030-56694-4_14
- Dirichlet's theorem proof and notation: this course, lectures 015000–022000.
- Wikipedia: [Dirichlet's theorem on arithmetic progressions](https://en.wikipedia.org/wiki/Dirichlet%27s_theorem_on_arithmetic_progressions), [Chinese remainder theorem](https://en.wikipedia.org/wiki/Chinese_remainder_theorem), [p-adic number](https://en.wikipedia.org/wiki/P-adic_number).

**Proof scope:** Complete interpolation lemma for any finite set containing 2, based on the previously proved Dirichlet theorem. It constructs square-class matches and controls prime support, not numerical size or proximity.
