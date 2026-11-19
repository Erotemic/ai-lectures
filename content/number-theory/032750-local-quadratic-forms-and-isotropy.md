# 032750 — Quadratic Forms over Local Fields: From Diagonalization to Isotropy

**Track:** Number Theory from First Principles. **Background:** 031250 (local squares), 032250–032500 (Hilbert symbols), 025000 (finite fields). **Aim:** connect Hilbert symbols to quadratic forms, prove an exact ternary isotropy test and a five-variable theorem for odd p, and distinguish local results from the global Hasse–Minkowski theorem.

<!-- BEGIN SPOKEN LECTURE -->

# Quadratic Forms over Local Fields: From Diagonalization to Isotropy

An equation with a single square is usually easy to recognize. An equation involving several squares can hide much more structure. Consider x squared plus y squared equals three times z squared. It has real nonzero solutions; over the rational numbers, however, there is no nontrivial solution. Is the obstacle arithmetic or geometric? And can we detect it by looking at one prime at a time?

Quadratic forms give us a systematic language for such problems. A quadratic form is a homogeneous polynomial of degree two. It may have terms like x squared, two x y, and five y squared, or it may involve many variables. A form is called isotropic over a field if it takes the value zero at a nonzero vector. Otherwise it is anisotropic.

The word isotropic does not say that all coefficients are small or that the form represents many numbers. It asks one very precise question: does the cone defined by the equation q equals zero contain anything besides its vertex?

We will study this over Q-p. We already know how to solve one related problem: the Hilbert symbol tells us when a binary norm expression can equal a prescribed number. That turns out to settle all nondegenerate ternary forms. It also gives a way to understand why five variables are enough to force a p-adic zero, at least when p is odd.

## Removing cross terms without losing the question

A quadratic form in n variables can be written as a symmetric matrix expression. Over any field of characteristic different from two, there is an invertible linear change of variables making it diagonal: a-one times X-one squared, plus a-two times X-two squared, and so on. This is the quadratic-form version of completing the square.

Why can we always start the process? If the form is nonzero, some vector v has q of v nonzero. Use v as the first basis vector. The associated bilinear form, obtained by polarizing q, lets us subtract suitable multiples of v from the other basis vectors so that they become orthogonal to v. Now split off the one-dimensional term and repeat. The field Q-p has characteristic zero, so division by two causes no problem.

An invertible change of variables preserves whether there is a nonzero zero. Multiplying the form by any nonzero scalar preserves it as well. So for isotropy questions we can work with diagonal forms without pretending that their coefficients are canonical.

A two-variable form a x squared plus b y squared is isotropic precisely when negative a b is a square. Indeed, a nontrivial solution cannot have only one nonzero coordinate; dividing the equation gives a square ratio equal to negative b over a, which differs from negative a b by the square a squared. This is the elementary first case.

## Three variables: the Hilbert symbol is exact

Now take a diagonal ternary form a x squared plus b y squared plus c z squared, where all coefficients are nonzero. Divide the equation by a and rearrange it as x squared minus negative b over a times y squared equals negative c over a times z squared.

That is precisely a norm-form equation. Therefore the ternary form is isotropic if and only if the Hilbert symbol of negative a b and negative a c is plus one. We multiplied both inputs by the square a squared to avoid fractions, so the symbol did not change. This is an if-and-only-if statement, not merely a necessary condition. Every nondegenerate ternary local isotropy problem reduces to one explicit Hilbert symbol.

Let's work through the equation x squared plus y squared equals three z squared. Its coefficients are one, one, and negative three. Our test asks for the symbol of negative one and three. At p equal to three, the odd-prime formula gives the Legendre symbol of negative one modulo three. That is minus one. Therefore the equation has no nontrivial solution over Q-three, and hence no nontrivial rational solution.

At p equal to two, the Hilbert symbol of negative one and three is also minus one: both are odd units congruent to three modulo four. So this one rational equation has local obstructions at two different primes. A rational solution cannot exist because it would give a solution in every completion. Notice that the converse, local solutions everywhere implying a rational solution, is a much deeper question and has not been used in this argument.

Change the coefficient three to five. Now x squared plus y squared equals five z squared has the familiar rational solution one squared plus two squared equals five. The corresponding local symbols are all positive. In this easy case we have a global solution in hand; we did not need a local-global theorem to produce it.

## What changes in four variables?

When we reach four variables, the situation becomes more subtle. There exist anisotropic forms of dimension four over every Q-p. We can construct one using the unramified quadratic extension from the earlier lectures.

Choose a unit u that is not a square and such that adjoining its square root is unramified. For odd p, any nonsquare residue unit will do. For p equal to two, take u equal to five. Consider the four-variable form x squared minus u y squared minus p z squared plus p u w squared.

Rewrite it as one quadratic norm minus p times another quadratic norm. If it were zero, the norm of x plus y square-root-u would equal p times the norm of z plus w square-root-u. In an unramified quadratic extension, the p-adic valuation of a nonzero norm is always even. The left side would have even valuation, the right side odd valuation. They cannot be equal unless both norms vanish. But a norm of a nonzero field element cannot vanish, so x and y, then z and w, must all be zero.

Thus this four-variable form is anisotropic. It proves that local isotropy cannot be forced merely by having four variables, even though many particular four-variable forms do have nontrivial zeros.

This example also shows why we developed local norm theory before studying quadratic forms. The valuation parity of a norm creates an obstruction in four dimensions without any elaborate search for solutions.

## Five variables at an odd prime

Now suppose p is odd, and consider a nondegenerate diagonal quadratic form in at least five variables. We can prove that it must be isotropic over Q-p.

First scale each variable independently by an integer power of p. Because each coefficient changes by a square, we can make the valuation of each nonzero coefficient either zero or one. These two possibilities are its parity class. With five coefficients and only two parity classes, at least three coefficients belong to the same class.

Set all the other variables equal to zero. If the three selected coefficients have valuation one, divide this ternary equation by p. Either way we obtain a ternary form whose three coefficients are p-adic units. We only need to prove that a ternary quadratic form with three unit coefficients has a nontrivial p-adic zero.

Reduce modulo p. Let the coefficients be A, B, and C, all nonzero in the field with p elements. Seek a solution with the third variable equal to one. We need A x squared equal to negative C minus B y squared. As x varies, the left side takes exactly p plus one over two values, because a nonzero square has two square roots. As y varies, the right side also takes p plus one over two values. Two subsets of a p-element set, each larger than half the set, must intersect. So a solution with the third variable one exists modulo p.

This solution is automatically nonsingular: the partial derivative with respect to the third variable is twice C, which is nonzero modulo the odd prime p. Hensel's lemma therefore lifts the finite-field solution to a genuine zero over Q-p. That proves the five-variable assertion for every odd prime.

For p equal to two, that particular derivative vanishes, and the argument breaks. The conclusion that five variables force isotropy remains true over Q-two, but proving it takes a different argument. We are not silently extending the odd-prime proof to two.

## Dimension, discriminant, and the Hasse invariant

The full classification of nondegenerate quadratic forms over Q-p uses three pieces of data: the dimension, the determinant modulo squares, and a product of Hilbert symbols called the Hasse invariant. For a diagonal form with coefficients a-one through a-n, the Hasse invariant is the product of the Hilbert symbols of a-i and a-j over all pairs with i smaller than j.

A change of diagonal coordinates does not leave each individual coefficient unchanged. What is striking, and requires a separate invariance argument, is that the product survives as an invariant of the quadratic form. Together with dimension and determinant square class, it classifies nondegenerate local quadratic forms. We state that classification here to orient the subject; we have not yet proved the full classification theorem or the two-adic five-variable bound.

There is a second boundary, between local and global arithmetic. The Hasse–Minkowski theorem says that a quadratic form over the rational numbers has a nontrivial rational zero if and only if it has a nontrivial zero over the real numbers and over Q-p for every prime p. We have proved several local criteria and one half of that implication: a rational zero produces local zeros. We have not yet proved the converse, which is the heart of Hasse–Minkowski.

The local tools are nevertheless substantial. We can diagonalize a form, calculate ternary isotropy exactly with Hilbert symbols, construct anisotropic four-variable forms, and prove isotropy in five variables for odd primes. The next bridge will show how the different completions constrain each other. That bridge begins not with an existence theorem, but with a product identity: the local Hilbert symbols of rational numbers multiply to one across all primes and the real place.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Let \(K=\mathbb Q_p\), \(\operatorname{char}K\neq2\), and q a nondegenerate diagonal quadratic form.

### Low dimensions

\[
\langle a,b\rangle\text{ isotropic}\iff -ab\in K^{\times2}.
\]
For a ternary form,
\[
\boxed{\langle a,b,c\rangle\text{ isotropic}\iff(-ab,-ac)_p=1.}
\]
Indeed \(ax^2+by^2+cz^2=0\) becomes \(x^2-(-b/a)y^2=(-c/a)z^2\); multiplication of each argument by \(a^2\) does not change the Hilbert symbol. The homogeneous norm criterion handles solutions with a zero coordinate as well.

Examples:
\[
\langle1,1,-3\rangle: (-1,3)_3=-1,\quad (-1,3)_2=-1;
\]
\[
\langle1,1,-5\rangle: (1,2,1)\text{ is a rational zero}. 
\]

### Dimension four can be anisotropic

Choose a unit \(u\in\mathbb Q_p^\times\) defining the unramified quadratic extension \(E=\mathbb Q_p(\sqrt u)\). For odd p take a nonsquare residue unit; at p=2 take u=5. The form
\[
q(x,y,z,w)=x^2-u y^2-pz^2+puw^2=N_{E/K}(x+y\sqrt u)-pN_{E/K}(z+w\sqrt u)
\]
is anisotropic: any nonzero norm has even p-adic valuation, so equality of the two terms is impossible unless both norms, and hence both arguments, are zero.

### Five variables, p odd: elementary proof

Scale each of five nonzero diagonal coefficients to valuation 0 or 1. Three share the same parity; restricting to these three variables and removing a common factor p gives a ternary form with unit coefficients. Over \(\mathbb F_p\), for unit \(A,B,C\), the two sets
\[
S_1=\{Ax^2:x\in\mathbb F_p\},\quad S_2=\{-C-By^2:y\in\mathbb F_p\}
\]
each have cardinality \((p+1)/2\). Their intersection is nonempty. Taking z=1 gives a solution of \(Ax^2+By^2+Cz^2=0\pmod p\), with derivative \(2Cz\neq0\); lift by Hensel. Thus every form of dimension at least five over \(\mathbb Q_p\), with p odd, is isotropic.

**Boundaries:** The five-variable theorem for Q_2, Hasse-invariant independence from diagonalization, complete local classification, and the global Hasse–Minkowski converse are stated/reference results, not proved by this manuscript.

### Exercises

1. Diagonalize \(x^2+2xy+3y^2\) over Q_3 and test isotropy.
2. Check \((-1,3)_2=(-1,3)_3=-1\), and show why either obstruction rules out a rational zero of \(x^2+y^2-3z^2\).
3. Explain why the norm parity argument gives an anisotropic four-variable form even over Q_2.
4. Verify the finite-field pigeonhole proof for p=3 by listing the sets of squares.
5. Identify exactly where the five-variable proof fails when p=2 and what sort of new idea would be required.

### Reading and source notes

- Cindy Zhang, University of Chicago REU, [p-adic numbers, quadratic forms, and the Hasse–Minkowski theorem](https://math.uchicago.edu/~may/REU2021/REUPapers/Zhang,Cindy.pdf), finite-field ternary isotropy and quadratic-form context.
- Wikipedia: [Quadratic form](https://en.wikipedia.org/wiki/Quadratic_form), [Hasse invariant of a quadratic form](https://en.wikipedia.org/wiki/Hasse_invariant_of_a_quadratic_form), [Hasse–Minkowski theorem](https://en.wikipedia.org/wiki/Hasse%E2%80%93Minkowski_theorem), [Isotropic quadratic form](https://en.wikipedia.org/wiki/Isotropic_quadratic_form).
