# 034500 — What Hasse–Minkowski Gives Us, and What It Does Not

**Track:** Number Theory from First Principles. **Background:** 029500–029750 (ideal classes and forms), 033750 (isotropic forms represent every scalar), 034250 (Hasse–Minkowski). **Aim:** derive rational value representation and rational isometry from the theorem, prove one-dimensional Witt cancellation, and exhibit an explicit failure of integral local-to-global representation.

<!-- BEGIN SPOKEN LECTURE -->

# What Hasse–Minkowski Gives Us, and What It Does Not

We have proved that a rational quadratic form has a nonzero rational zero exactly when it has a nonzero zero over every completion. This is a strong result, but the word zero hides some useful consequences. We often care about representing a number other than zero. We may want to know whether two forms are the same after a rational change of variables. And we may care about integer coordinates, not rational ones.

These questions sound close together. Over the rationals, the first two are governed by the same local-to-global principle. Over the integers, the analogous statement can fail, even for a positive definite binary form. Today's aim is to extract the positive conclusions and then identify the exact boundary.

## Representing a specified rational value

Let q be a nondegenerate rational quadratic form, and let m be a nonzero rational number. Suppose q represents m over the reals and over Q-p for every prime p. Can we conclude that it represents m over the rationals?

Add one new variable z and form the homogeneous equation q of x minus m z squared equals zero. Every local representation of m becomes a nonzero local zero by taking z equal to one. The Hasse–Minkowski theorem therefore gives a nonzero rational zero of the enlarged form.

There are two possibilities. If z is nonzero, divide the old coordinates by z. The resulting vector represents m under q. If z is zero, q itself has a nonzero rational zero. But we proved that a nondegenerate isotropic form over a field represents every scalar, using a hyperbolic plane. In particular, it represents m. Either way we obtain a rational representation of m.

Thus the local-to-global principle extends from isotropy to representing any nonzero rational value. In fact zero is covered directly by the theorem. We have not introduced a new deep theorem; we have reduced the representation problem to the theorem we already proved.

## A finite number of local checks

There is a practical feature of this conclusion. Suppose the form q has at least three variables and has been diagonalized with nonzero integer coefficients. At an odd prime dividing none of those coefficients, any three of the coefficients are units. The finite-field square-counting argument provides a nonsingular zero of that three-variable subform, which lifts to a p-adic zero. Therefore at such a prime, isotropy is automatic.

Only the real place, the prime two, and primes dividing the product of the diagonal coefficients need to be examined individually. This turns an apparently infinite local list into a finite procedure, at least once the coefficients have been factored.

For representing a fixed m by a form with at least two variables, apply the same observation to the augmented form q minus m times a square. The relevant finite set consists of the real place, two, and primes dividing the coefficients or m after denominators are cleared.

We should not use this shortcut for an arbitrary binary form's isotropy. Binary unit forms may be anisotropic at infinitely many primes. The automatic argument requires at least three variables.

## From existence to parameterization

Once a rational point on a conic is known, it typically unlocks many more rational points. Consider the affine circle x squared plus y squared equals five. We already know the rational point one, two.

Draw a line of rational slope through that point. Algebraically, write y equal to two plus t times x minus one, where t is rational. Substitute into the circle equation. One root of the resulting quadratic equation gives the known point. The other root is also rational, because the coefficients and the first root are rational.

As t varies through the rationals, we obtain a family of rational solutions. A single rational point turns the conic into something we can parameterize with lines. This does not mean every equation of degree two can be solved with a pleasing small formula; it means that the rational-point existence problem and the rational-point generation problem are closely connected.

It also explains why Hasse–Minkowski is especially consequential for conics. The theorem tells us when a rational point must exist. Elementary geometry tells us what we can do after finding one.

## When are two forms the same over the rationals?

Now consider two nondegenerate quadratic forms in the same number of variables. They are called isometric over Q if an invertible rational linear change of coordinates carries one to the other. A rational isometry certainly remains an isometry over every completion. Is the converse true?

Yes. Local isometry at every completion implies rational isometry. We can derive this from the existence theorem, together with a cancellation principle for quadratic forms.

Here is the strategy. Suppose two forms are locally isometric everywhere. Choose a nonzero rational value a represented by the first form; a nondegenerate form always represents some nonzero value. Its local isometries show that the second form represents a over every completion. The value-representation consequence just proved shows that the second form represents a rationally.

We can now split off an a times x squared term from both forms by rational orthogonal changes of coordinates. What remains are two forms of one lower dimension. Their local isometry follows from canceling the common one-dimensional summand. Repeat by induction.

The only step requiring explanation is that cancellation. Let's prove it in the one-dimensional case rather than invoking a theorem without showing what happens.

## How to cancel one common line

Work over any field of characteristic different from two. Suppose a quadratic space contains a vector e of nonzero value a, and an isometry sends e to another vector x of the same value. We want an isometry of the target space carrying x back to e, so that the orthogonal complements can be compared.

Consider the difference x minus e. If this vector has nonzero quadratic value, reflection in the hyperplane perpendicular to x minus e sends x to e. This is a direct computation from the reflection formula: subtract from a vector twice its projection onto the normal direction, using the associated symmetric bilinear form.

If x minus e has zero value, use x plus e instead. Because both x and e have the same nonzero value a, the sum x plus e then has value four a, which is nonzero. Reflection in this second vector sends x to negative e. A final reflection in e changes negative e into e.

Thus we can always adjust the original isometry so that it fixes e. An isometry fixing e carries the orthogonal complement of e onto the orthogonal complement of e. This is one-dimensional Witt cancellation. Applied at each completion, it says that after splitting off the same nonzero coefficient, the two remaining forms are locally isometric.

Induction now proves that the original two forms were isometric over Q. Again, the subtle global step was existence of a rational representation. The cancellation itself is linear algebra over a field.

## Why replacing rationals by integers breaks the statement

It is tempting to conclude something even stronger: if a form represents an integer over the real numbers and over the p-adic integers for every prime, then it represents that integer with ordinary integer coordinates. That is false.

Consider the positive definite form x squared plus x y plus six y squared. Ask whether it represents two by ordinary integers. Complete the square after multiplying by four. The equation becomes the square of two x plus y, plus twenty-three y squared, equals eight.

If y is nonzero, the second term alone is at least twenty-three, already too large. If y is zero, the first term would have to be eight, which is not a square. So there is no integer solution.

Yet there is a solution over the p-adic integers for every prime. For every odd prime, take x and y both equal to one-half. Their form value is two, and one-half belongs to the p-adic integers whenever p is odd. At the prime two, set y equal to one. Then we need x squared plus x plus four to equal zero. Modulo two, x equal to zero is a root; its derivative, two x plus one, is odd. Hensel's lemma lifts it to a solution in the two-adic integers. The equation has real solutions as well, for example x and y both one-half.

There is even a rational solution: one-half, one-half. So Hasse–Minkowski has done exactly what it promised. The failure is the extra demand that both coordinates be ordinary integers. The p-adic integer solutions need not come from the same integer pair. This example also connects to our earlier discussion of forms of discriminant negative twenty-three and nontrivial ideal classes.

## The boundary at higher degrees

A different boundary appears when we change the degree of the equation. The famous cubic three x cubed plus four y cubed plus five z cubed equals zero has a nonzero solution over the reals and over every Q-p, but no nonzero rational solution. This is Selmer's example. Its local solutions and global obstruction require arguments beyond our current quadratic theory, and we cite those arguments rather than pretending to have reproved them here.

The contrast is important. Degree two has a particularly effective linear-algebra structure, Hilbert-symbol tests, and an induction that can isolate a single troublesome prime. There is no automatic extension of that mechanism to arbitrary cubic curves or higher-degree varieties.

Our course has now established three global facts with sharply different scopes. A rational quadratic form has a nonzero rational zero exactly when all its completions do. A nondegenerate rational quadratic form represents a rational value exactly when it does so locally everywhere. And two nondegenerate rational quadratic forms are isometric exactly when they are locally isometric everywhere. But insisting on integral coordinates, or abandoning quadratic equations, changes the problem.

The next algebraic direction is already visible in the background. Our p-adic extension lectures gave a trace lattice, a ring of integers, valuations, and ramification indices. We can now build the different and discriminant as tools for measuring ramification, especially at the prime two, without confusing these with the local-to-global principle we have just proved.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

**Representation corollary:** For nondegenerate \(q/\mathbb Q\) and \(m\in\mathbb Q\), \(m\in q(\mathbb Q^n)\) if and only if \(m\in q(\mathbb Q_v^n)\) for all \(v\), by Hasse–Minkowski applied to \(q\perp\langle-m\rangle\) and universality of isotropic spaces.

**Local-to-global isometry:** If two nondegenerate forms of the same dimension are isometric over every \(\mathbb Q_v\), choose \(a\in\mathbb Q^\times\) represented by one. The other represents \(a\) everywhere locally and therefore over \(\mathbb Q\). Split a common \(\langle a\rangle\). One-dimensional Witt cancellation at each completion permits induction on the remaining summands.

**Reflection proof of cancellation:** Let \(q(x)=q(e)=a\ne0\), and let \(B\) be the polarized bilinear form. For anisotropic \(v\), the reflection \(r_v(z)=z-2B(z,v)v/q(v)\) preserves \(q\). If \(q(x-e)\ne0\), then \(r_{x-e}(x)=e\). If \(q(x-e)=0\), then \(q(x+e)=4a\ne0\) and \(r_{x+e}(x)=-e\); composing with \(r_e\) sends \(x\) to \(e\). Thus an isometry can be modified to fix the common line and restrict to its orthogonal complement.

**Conic parameterization:** The line \(y=2+t(x-1)\) through \((1,2)\) meets \(x^2+y^2=5\) again at

\[
 x=\frac{t^2-4t-1}{1+t^2},\qquad y=\frac{2-2t-2t^2}{1+t^2}\quad(t\in\mathbb Q).
\]

**Explicit failure of *integral* local-global representation:** Let \(q(x,y)=x^2+xy+6y^2\). Then \(q(\frac12,\frac12)=2\). This is an integral point over every \(\mathbb Z_p\) for odd \(p\); for \(p=2\), use \(y=1\) and lift the simple root \(x\equiv0\pmod2\) of \(x^2+x+4\). Yet no ordinary integer solution exists, since \((2x+y)^2+23y^2=8\) has none.

### Exercises

1. Prove the value-representation corollary including the case when the newly added variable in \(q\perp\langle-m\rangle\) is zero.
2. Verify the reflection formulas and the conic parameterization.
3. Check local integral solvability of \(x^2+xy+6y^2=2\) at \(p=2\) using the simple-root Hensel criterion and explain why the rational solution fails to be 2-adically integral.
4. Compare rational isometry, integral equivalence, and belonging to the same genus of integral quadratic forms.

## Sources and reading

- John Voight, *Quaternion Algebras*, section 14.3, the local-to-global isometry corollary: https://link.springer.com/chapter/10.1007/978-3-030-56694-4_14
- Keith Conrad, *Selmer's Example*, complete source for the cubic counterexample: https://kconrad.math.uconn.edu/blurbs/gradnumthy/selmerexample.pdf
- Wikipedia: [Witt's theorem](https://en.wikipedia.org/wiki/Witt%27s_theorem), [Hasse–Minkowski theorem](https://en.wikipedia.org/wiki/Hasse%E2%80%93Minkowski_theorem), [Genus of a quadratic form](https://en.wikipedia.org/wiki/Genus_of_a_quadratic_form).

**Proof scope:** Proves the rational value and local-isometry consequences and one-dimensional cancellation. The integral counterexample is proved directly; Selmer's cubic is cited, not reproved.
