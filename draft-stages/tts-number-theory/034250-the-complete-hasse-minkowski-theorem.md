# 034250 — Hasse–Minkowski: From Every Completion to One Rational Zero

**Track:** Number Theory from First Principles. **Background:** 033250 (two-adic isotropy), 033500 (Legendre's theorem), 033750 (all-but-one and common-value lemmas), 034000 (auxiliary-prime interpolation), 022000 (Dirichlet's theorem). **Aim:** give a complete induction proof of the Hasse–Minkowski local-to-global theorem for isotropy of quadratic forms over the rational numbers.

<!-- BEGIN SPOKEN LECTURE -->

# Hasse–Minkowski: From Every Completion to One Rational Zero

There is a recurring difficulty in number theory. We can solve an equation modulo each power of a prime, sometimes even in every p-adic field, and still have no obvious way to put those solutions together. Each prime sees a different part of the arithmetic. The real numbers add a sign condition. A solution in one completion need not resemble a solution in another.

For quadratic forms over the rational numbers, this apparent fragmentation is deceptive. If a homogeneous quadratic equation has a nonzero solution over the reals and over Q-p for every prime p, then it has a nonzero rational solution. This is the Hasse–Minkowski theorem.

Today we will prove it. The argument is not a single trick. It is a chain, developed across the preceding lectures: finite-field zeros and Hensel lifting, a lattice proof for ternary forms, Hilbert reciprocity, local square classes, Dirichlet's theorem, and induction on the number of variables. Each part has a distinct job. We will keep those jobs visible rather than compressing the proof into the phrase local-global principle.

## The exact theorem and the easy direction

Let q be a quadratic form with rational coefficients. It is called isotropic over a field if some nonzero vector over that field makes q equal zero. The theorem states that q is isotropic over Q exactly when it is isotropic over R and over every Q-p.

If q has a nonzero rational zero, it also has that same zero in each completion. So one direction is immediate.

There is also an easy degenerate case. If the form has a nontrivial radical, then a nonzero vector in the radical has quadratic value zero over Q. We may therefore concentrate on nondegenerate forms. Completing the square diagonalizes a nondegenerate form over Q, and multiplying by a rational square or scaling the whole equation does not change isotropy. We can work with a diagonal form whose coefficients are nonzero integers.

The task is to prove the other implication: if all completions admit a nonzero zero, then so do the rationals.

## One and two variables

In one variable a nondegenerate form is a times x squared, with a nonzero. It has no nonzero zero over any field, so there is no case to prove.

In two variables, divide by the first coefficient and write the equation as x squared minus d times y squared equals zero, for a nonzero rational d. A nonzero solution exists over a field exactly when d is a square in that field.

Suppose d is a square in Q-p for every prime and a square over the reals. At every prime its valuation must be even. Therefore every prime occurs to an even exponent in the rational factorization of d. The real condition says d is positive. Together these statements force d to be a square of a positive rational number. Thus the binary equation has a rational zero.

This is the first local-to-global step. It uses only unique factorization, the sign at infinity, and the easiest part of local square theory.

## The three-variable case

For a nondegenerate ternary form, we have already done the difficult work. Legendre's theorem, proved with a lattice and a cylinder, says that local solutions everywhere yield a nonzero rational zero. Hilbert reciprocity further says that we can omit one place from the local checks: if a ternary form is locally isotropic everywhere except possibly at one completion, that missing condition is automatically satisfied.

This all-but-one form of the ternary theorem is the hinge of the induction. We will intentionally introduce one new prime at which we do not know whether a ternary equation is solvable. The theorem will allow us to ignore that remaining uncertainty.

## Splitting a larger form in two

Now assume there are at least four variables, and suppose the theorem has been proved for all smaller dimensions. Write the form as a binary block A minus a remaining block B. The block A has two nonzero diagonal coefficients, a and b. The block B has the other n minus two nonzero diagonal coefficients, c-one through c-n-minus-two. All these coefficients can be chosen to be integers.

At every completion, the original form is isotropic by hypothesis. Therefore, at every completion, A and B represent some common nonzero local value. We proved that in the common-value lemma. If an isotropic vector makes their shared value nonzero, take that value. If the shared value is zero, one block is isotropic; a nondegenerate isotropic block represents every scalar, so choose a nonzero value represented by the other block and match it.

At each place we now know such a local value exists. But these values may differ. We cannot simply declare them to be one rational number. This is the heart of the global problem.

## Decide which places matter

Form the integer d by multiplying two, a, b, and all the coefficients of B. Let S be the finite set of primes dividing d. In particular S contains the prime two and every prime that divides any coefficient of the original diagonal form.

For each p in S, choose a nonzero local value t-sub-p represented by both A and B. At the real place choose a nonzero common value t-infinity and record its sign.

Apply the auxiliary-prime lemma from the preceding lecture. It gives a nonzero rational number t with three properties. At every p in S, t and t-sub-p lie in the same p-adic square class. At infinity, t has the sign of t-infinity. And outside S, the prime divisors of t consist of at most one positive prime q.

The square-class matching has a direct consequence. Every time A or B represents t-sub-p, it represents t as well: scale the representing vector by a square root of t divided by t-sub-p. So A and B both represent t at every place in S and over the reals.

The prime q is the only place where the extra factor t might spoil a simple unit-coefficient argument. All other primes outside S see all our coefficients, including t, as units.

## First make the binary block represent t globally

Consider the ternary form obtained by taking A and subtracting t times a new variable squared. Over the real numbers it is isotropic, because A represents t there. It is isotropic over Q-p for every p in S, because A represents t at those places.

Let p be any odd prime outside S and different from q. None of the three coefficients a, b, and t is divisible by p. A ternary form with three unit coefficients has a nonsingular zero modulo p, as we proved using the finite-field square-counting argument. Hensel lifting gives a p-adic zero. Therefore this ternary form is isotropic at every place except possibly q.

The all-but-one-place ternary theorem now says it has a nonzero rational zero. What does that imply about A?

If the new variable is nonzero, divide the original binary coordinates by that variable. This shows A represents t over Q. If the new variable is zero, then A itself has a nonzero rational zero. An isotropic nondegenerate form represents every rational scalar, so A represents t in this case as well.

We have achieved the first half of our goal: one rational value t is represented by the binary block A.

## The remaining block when there are four variables

Suppose n equals four. Then B is binary. Consider the ternary form consisting of B and the negative of t times a new square. At the real place and at all p in S, it is isotropic because B represents t locally. At every odd prime outside S different from q, its three coefficients are units, so it is isotropic by the same finite-field and Hensel argument.

It may be obstructed at q, but there is only one missing place. The ternary all-but-one theorem yields a nonzero rational zero. As before, either B represents t directly or B is isotropic and therefore universal. Thus B represents t over Q.

Both A and B now represent the same nonzero rational scalar. Choose representing vectors and put them together. Their values cancel in A minus B. The resulting vector is nonzero and rational. Our original four-variable form is isotropic.

No separate classification of four-variable forms was required. We transformed their rational isotropy problem into two ternary problems and let reciprocity handle the single auxiliary prime in each.

## The remaining block in five or more variables

Now suppose n is at least five. The form B has at least three variables. We again consider the form B minus t times a new square, but this time it has n minus one variables. We want to apply the induction hypothesis to it. For that, we must check that it is isotropic over every completion, including q.

The real place and all primes in S are covered by our choice of t. At an odd prime outside S different from q, every coefficient of the new form is a unit. Since this new form has at least four variables, we may select three of them; the three-unit finite-field argument supplies a nonzero p-adic zero.

What happens at q? The coefficient t might be divisible by q, so we do not use it. Instead examine B alone. It has at least three variables, and all its coefficients are q-adic units because q lies outside S. A ternary unit subform of B is isotropic over Q-q by the finite-field argument. Therefore B is already isotropic over Q-q, and so the enlarged form B minus t times a square is isotropic there as well, using zero for the added variable.

All local conditions for this n-minus-one-variable form are now satisfied. By the induction hypothesis, it has a nonzero rational zero. If the added variable is nonzero, B represents t. If the added variable is zero, B is isotropic over Q and thus represents every rational scalar, including t. Either way, B represents t.

The binary block A also represents t, as established earlier. Their representing vectors combine into a nonzero rational zero of the original form. This closes the induction.

## What made the proof work

We have proved the theorem for one and two variables, for three variables by Legendre's theorem, and for every higher dimension by induction. Thus a rational quadratic form is isotropic if and only if it is isotropic over the reals and at every p-adic completion.

The most delicate part was not Hensel lifting or matrix diagonalization. It was the passage from many unrelated local values to one rational value. Dirichlet's theorem provided a prime in a carefully chosen arithmetic progression, concentrating the uncontrolled factorization at one place. Hilbert reciprocity and the ternary theorem disposed of that one place. Induction then reduced the dimension of the remaining problem.

There is no assertion here that rational solutions of arbitrary polynomial equations exist whenever all local solutions exist. The degree two hypothesis and the nondegenerate quadratic structure are essential. We have also proved existence, not an efficient bound on the size of a solution. The auxiliary prime obtained from Dirichlet's theorem may be very large.

We can now use Hasse–Minkowski as a theorem we have established within the course, rather than a result cited just beyond its boundary. In the following lecture we will extract two consequences: local criteria for when a quadratic form represents a specified rational number, and a local-to-global classification of rational quadratic forms up to isometry. We will also mark the important difference between rational quadratic equations and integral representation problems.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

**Hasse–Minkowski over \(\mathbb Q\).** A quadratic form \(q/\mathbb Q\) has a nonzero rational zero if and only if \(q\otimes\mathbb R\) and \(q\otimes\mathbb Q_p\) have nonzero zeros for every prime \(p\).

**Induction:** Assume \(q\) nondegenerate and diagonal integral. For \(n\ge4\), write \(q=A\perp(-B)\), with \(A=\langle a,b\rangle\), \(B=\langle c_1,\ldots,c_{n-2}\rangle\), and \(S=\{p:p\mid 2ab\prod_i c_i\}\). At each \(p\in S\) and at \(\infty\), choose \(t_v\ne0\) represented by both A and B (033750). Choose \(t=sA_0q_0\in\mathbb Q^\times\) using the auxiliary-prime lemma (034000), where \(q_0\notin S\) is prime and \(t/t_p\in\mathbb Q_p^{\times2}\), with the correct real sign.

- \(A\perp\langle-t\rangle\) is a ternary form isotropic at every place except perhaps \(q_0\): at \(\infty,S\) by construction, and at each odd \(p\notin S\cup\{q_0\}\) by the unit-coefficient finite-field lemma and Hensel. The all-but-one ternary theorem (033750) implies rational isotropy, and hence \(t\in A(\mathbb Q^2)\).
- If \(n=4\), the same proof with \(B\perp\langle-t\rangle\) shows \(t\in B(\mathbb Q^2)\).
- If \(n\ge5\), \(B\perp\langle-t\rangle\) has dimension \(n-1\) and is isotropic everywhere: at \(\infty,S\) by construction; at odd \(p\notin S\cup\{q_0\}\) by unit coefficients; at \(q_0\) because \(B\) has at least three unit coefficients, so \(B\) itself is isotropic there. Apply induction to \(B\perp\langle-t\rangle\) to obtain \(t\in B(\mathbb Q^{n-2})\).

The observation used in the final step is that if \(C\perp\langle-t\rangle\) is isotropic then either \(C\) represents \(t\) (new coordinate nonzero) or \(C\) is isotropic and hence represents all scalars (new coordinate zero). Since both \(A\) and \(B\) represent \(t\), their difference \(A\perp(-B)\) is isotropic.

**Base dimensions:** \(n=1\) vacuous for nondegenerate forms; \(n=2\) equivalent to a rational number being a square (even valuations everywhere and positive sign); \(n=3\) proved by Legendre's theorem (033500) and strengthened by Hilbert reciprocity (033750).

### Exercises

1. Prove carefully that if \(q\) has nonzero radical over \(\mathbb Q\), it has a nonzero rational zero.
2. In the proof for \(n\ge5\), explain why \(q_0\notin S\) ensures all coefficients of \(B\) are units over \(\mathbb Z_{q_0}\).
3. Identify the separate applications of Dirichlet's theorem, Legendre's theorem, Hilbert reciprocity, and the induction hypothesis.
4. Show that a rational quadratic form of dimension at least five which has a nonzero real zero must have a nonzero rational zero. (Use the five-variable local results at every p.)
5. Explain why the argument proves existence but does not directly bound the height of a smallest rational zero.

## Sources and reading

- John Voight, *Quaternion Algebras*, section 14.3, Hasse–Minkowski over the rationals, proof by induction following Serre: https://link.springer.com/chapter/10.1007/978-3-030-56694-4_14
- Michael Stoll, *Introductory Number Theory*, section 18, ternary Legendre theorem: https://www.mathe2.uni-bayreuth.de/stoll/lecture-notes/IntroductoryNumberTheory.pdf
- Wikipedia: [Hasse–Minkowski theorem](https://en.wikipedia.org/wiki/Hasse%E2%80%93Minkowski_theorem), [Quadratic form](https://en.wikipedia.org/wiki/Quadratic_form), [Local-global principle](https://en.wikipedia.org/wiki/Local%E2%80%93global_principle).

**Proof scope:** Complete existence proof for isotropy of rational quadratic forms in all dimensions, relying on the separately proved ternary and reciprocity lemmas. The extension to arbitrary number fields is not proved here.
