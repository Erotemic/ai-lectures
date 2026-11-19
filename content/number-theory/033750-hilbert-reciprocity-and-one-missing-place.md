# 033750 — A Local Condition You Can Leave Unchecked

**Track:** Number Theory from First Principles. **Background:** 032250–032500 (Hilbert symbols), 032750 (ternary isotropy), 033000 (Hilbert reciprocity), 033500 (Legendre's theorem). **Aim:** prove the all-but-one-place ternary principle and two elementary representation lemmas used in the full Hasse–Minkowski proof.

<!-- BEGIN SPOKEN LECTURE -->

# A Local Condition You Can Leave Unchecked

Imagine checking a quadratic equation in every p-adic field and over the real numbers. At first this sounds like an infinite program: there are infinitely many primes. We already know that, for ternary equations, most of the checks happen automatically. There is a stranger simplification. Once every local check except possibly one has succeeded, the last one is forced to succeed as well.

This principle is not an accident about three variables. It follows from a product law that we proved earlier, Hilbert reciprocity. But Hilbert reciprocity, by itself, never manufactures a rational point. To understand exactly how the pieces fit, we need to distinguish three statements: a formula for one local obstruction, a product relation between the obstructions, and the global existence theorem that clears all the obstructions at once.

In the preceding lecture we proved the global existence theorem for ternary forms by a lattice argument. We can now add the product relation to get a stronger, particularly useful version.

## The Hilbert symbol as a yes-or-no test

Start with a nondegenerate diagonal ternary form, a x squared plus b y squared plus c z squared, over a completion of the rationals. Multiply the equation by the nonzero coefficient a and rearrange it. We can write it as a norm equation: a square minus a suitable multiple of a second square equals a suitable multiple of a third square.

The result from our earlier local quadratic-form lecture says that this form is isotropic exactly when the Hilbert symbol with entries negative a b and negative a c equals plus one. If that symbol is minus one, the only local zero is the origin. This is an exact criterion. No search through three-variable vectors remains once the symbol can be computed.

A Hilbert symbol takes only the values plus one and minus one. Over the real numbers it is minus one precisely when both entries are negative. Over an odd p-adic field it can be calculated from valuation parity and Legendre symbols. At the prime two it can be calculated from the residues of odd units modulo eight. We developed all three calculations earlier, rather than reserving them as black boxes.

The displayed symbol depends on a choice of diagonal coefficients, but the underlying assertion is invariant. Changing coordinates cannot create or remove a nonzero zero. The symbol formula is simply a way to perform that coordinate-independent test in a chosen diagonal basis.

## The product over all places

Hilbert reciprocity says that if A and B are nonzero rational numbers, the product of their Hilbert symbols over every prime and the real place is plus one. Only finitely many factors differ from plus one, so the product is well-defined.

Apply this to A equal to negative a b and B equal to negative a c. The same two rational inputs determine the isotropy test of our ternary form at each place. Suppose the form is isotropic everywhere except possibly at one place, which we will call v-zero. Every symbol other than the v-zero symbol is plus one. Their product is plus one. Hilbert reciprocity therefore forces the remaining symbol to be plus one, too.

So there is no ternary form that is isotropic at every completion but exactly one. Its failing local places, if any, must occur in a pattern whose signs multiply to plus one. In particular the number of minus signs is even.

A familiar example helps. The equation x squared plus y squared equals three times z squared is isotropic over the real numbers, but fails over Q-three. We saw earlier that it also fails over Q-two. Those two failures are compatible with Hilbert reciprocity. One failure standing alone would not be.

Now bring in Legendre's theorem. We proved that a ternary rational quadratic form with a nontrivial zero in every completion has a nontrivial rational zero. Combining the two results gives the all-but-one-place theorem: if such a form is isotropic at every place except possibly one, it is isotropic over the rationals.

Notice the two separate logical jobs. Reciprocity forces the missing local check. Legendre's theorem supplies the rational point. If we dropped Legendre's theorem, the product formula would not be enough. This distinction will matter for higher-dimensional forms and even more for equations of degree three.

## Three unit coefficients at almost every prime

The all-but-one theorem becomes practical because most odd primes cannot obstruct a ternary form with integral coefficients. Suppose p is odd and does not divide a b c. Then all three diagonal coefficients are nonzero in the finite field with p elements.

Fix the third variable to one. As the first variable varies, a times its square takes p plus one over two distinct values. As the second variable varies, negative c minus b times its square also takes p plus one over two distinct values. Two subsets of a p-element set with more than half the elements each must intersect. Choose the corresponding variables. We have a zero modulo p with its third coordinate equal to one.

The derivative with respect to that coordinate is twice c, nonzero modulo p. Hensel's lemma lifts the finite-field point to a genuine p-adic point. Therefore a ternary form with three p-adic unit coefficients is automatically isotropic when p is odd.

For an arbitrary ternary form with nonzero integer coefficients, only the real place, the prime two, and primes dividing the product of its coefficients can need direct checks. This finite set is useful for deciding whether the form has a rational solution.

But there is a subtlety. We should not replace the statement with the false claim that a binary form with unit coefficients is always isotropic. Over a finite field, a binary form can be anisotropic. The finite-field counting argument used a third nonzero coefficient, and that third coordinate was essential.

## Isotropic forms represent every scalar

The global proof ahead asks us to match the value of one form with the value of another. To prepare for that, we need a small linear-algebra lemma.

Let F be a field of characteristic different from two, and let q be a nondegenerate quadratic form over F. Suppose q has a nonzero isotropic vector v. Nondegeneracy means we can choose another vector w whose associated bilinear product with v is nonzero. Replace w by w minus a suitable multiple of v. Since q of v is zero, this correction can make q of w zero while preserving the nonzero pairing with v.

On the plane spanned by these two isotropic vectors, the form has only a cross term. After scaling, its value at a vector with coordinates x and y is simply x times y. By taking x equal to one and y equal to any prescribed scalar, we can represent every element of F. In other words, an isotropic nondegenerate quadratic form is universal as a value-representing form.

This lemma looks elementary, but it will remove a nuisance in our induction. A solution of a larger form might arise from a smaller form's own zero rather than from the value we wanted it to represent. If that smaller form is isotropic, universality lets us recover the wanted value anyway.

## A shared nonzero value at a local place

Here is the second lemma. Suppose we split a nondegenerate quadratic form into two nondegenerate blocks, called A and minus B. If the whole form is isotropic over a field, then A and B represent a common nonzero value.

To see this, take a nonzero zero of the combined form. The A-block and B-block necessarily have equal values. If their common value is nonzero, we are done. If their common value is zero, at least one of the two nondegenerate blocks has a nonzero isotropic vector. That block therefore represents every scalar by the preceding lemma. The other block, being nondegenerate, represents at least one nonzero scalar. Choose such a scalar and use universality in the first block to match it.

This proof works over Q-p and over the real numbers. It is not asserting that the common value is rational. At a given completion we get some nonzero local scalar t-sub-p. The problem of finding one rational scalar that fits all these local choices is still ahead.

## Where the missing place goes

We can now describe the shape of the global argument before building it. Split a rational quadratic form into a binary block and the negative of the remaining block. At each troublesome prime, choose a nonzero local value represented by both blocks. Choose a rational number that matches those local values up to squares. Arrange for that rational number to introduce no new prime factors except one auxiliary prime.

Then the binary block, together with a new variable for the chosen scalar, gives a ternary form. At every place except perhaps that auxiliary prime, it will have a local zero. The all-but-one theorem makes it solvable over the rationals. The remaining block is handled by a second ternary application or by induction.

Every step we have proved in this lecture is needed to make that outline work. The Hilbert product formula closes the single missing place. Hensel lifting clears ordinary primes. The hyperbolic plane lemma supplies values, and the common-value lemma starts the matching process.

Next we will construct the auxiliary prime precisely. The earlier proof of Dirichlet's theorem on primes in arithmetic progressions will reappear in a new role: it will let us choose a prime in exactly the residue class needed to satisfy several p-adic square-class conditions simultaneously.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For a nondegenerate ternary diagonal form \(q=\langle a,b,c\rangle\) over \(\mathbb Q_v\),

\[
q\text{ isotropic over }\mathbb Q_v\quad\Longleftrightarrow\quad(-ab,-ac)_v=1.
\]

Hilbert reciprocity, proved in 033000, gives \(\prod_{v\le\infty}(A,B)_v=1\) for rational \(A,B\ne0\). Therefore, if a ternary form is isotropic at every place except perhaps one, it is isotropic at that place; Legendre's theorem from 033500 then yields a nonzero rational zero.

**Finite-field lemma:** For odd \(p\) and \(a,b,c\in\mathbb F_p^\times\), the sets \(\{ax^2:x\in\mathbb F_p\}\) and \(\{-c-by^2:y\in\mathbb F_p\}\) each have cardinality \((p+1)/2\); hence they intersect. Taking \(z=1\) gives a zero of \(ax^2+by^2+cz^2\) with \(\partial q/\partial z=2c\ne0\), which lifts by Hensel.

**Universality of isotropic forms:** If \(v\ne0\) and \(q(v)=0\), choose \(w\) with \(B(v,w)\ne0\), where \(B(x,y)=\frac12(q(x+y)-q(x)-q(y))\). Replacing \(w\) by \(w-q(w)v/(2B(v,w))\) makes \(q(w)=0\) while leaving \(B(v,w)\ne0\). Then \(q(xv+yw)=2xyB(v,w)\) represents any target scalar.

**Common local value:** If \(A\oplus(-B)\) is isotropic and \(A,B\) are nondegenerate, then \(A\) and \(B\) represent a common nonzero scalar. Either an isotropic vector immediately has nonzero shared value, or one block is isotropic and therefore universal.

### Exercises

1. For \(\langle1,1,-3\rangle\), calculate the Hilbert symbols at 2 and 3 and check that their product is plus one.
2. Prove that at an odd prime \(p\nmid abc\), the ternary form \(\langle a,b,c\rangle\) has a nonzero p-adic zero.
3. Prove the common-value lemma when only one block is binary and the other has arbitrary positive dimension.
4. Explain why the Hilbert product formula alone does not establish rational solvability for an arbitrary cubic equation.

## Sources and reading

- John Voight, *Quaternion Algebras*, section 14.3 (all-but-one-place ternary principle and rational Hasse–Minkowski induction): https://link.springer.com/chapter/10.1007/978-3-030-56694-4_14
- Michael Stoll, *Introductory Number Theory*, sections 18–20: https://www.mathe2.uni-bayreuth.de/stoll/lecture-notes/IntroductoryNumberTheory.pdf
- Wikipedia: [Hilbert symbol](https://en.wikipedia.org/wiki/Hilbert_symbol), [Hasse–Minkowski theorem](https://en.wikipedia.org/wiki/Hasse%E2%80%93Minkowski_theorem), [Quadratic form](https://en.wikipedia.org/wiki/Quadratic_form).

**Proof scope:** Includes the ternary all-but-one-place corollary and the nondegenerate common-value lemma. The rational auxiliary-prime construction and full induction are in subsequent lectures.
