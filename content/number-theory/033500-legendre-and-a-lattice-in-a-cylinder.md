# 033500 — Legendre's Ternary Theorem: A Lattice Inside a Cylinder

**Track:** Number Theory from First Principles. **Background:** 001000 (divisibility), 007000 (quadratic residues), 027500 (Minkowski lattice arguments), 031000 (Hensel lifting). **Aim:** prove an elementary local-to-global criterion for nondegenerate ternary rational quadratic forms, with the lattice index and volume inequalities made explicit.

<!-- BEGIN SPOKEN LECTURE -->

# Legendre's Ternary Theorem: A Lattice Inside a Cylinder

A local solution is a solution seen through one kind of lens. Over the real numbers, an equation notices signs. Over Q-three, it notices divisibility by three. Over Q-five, it notices divisibility by five. A rational solution has to survive every one of these tests. It is easy to see why rational solvability implies all the local conditions. The hard question is whether the local tests can be satisfied separately while no single rational solution exists.

For homogeneous equations of degree two in three variables, the local tests are enough. We are going to prove this in the most concrete setting: a diagonal equation with three nonzero integer coefficients. The proof does not search for infinitely many triples. It builds a lattice on which the value of the quadratic form is forced to be a multiple of one large integer, and then uses geometry to find a lattice point whose value is too small to be any nonzero multiple.

The method is a good meeting point for algebra and geometry. The congruences build the lattice; the volume of a cylinder makes one of its points unavoidable.

## Simplifying the arithmetic without changing the problem

Begin with a nondegenerate ternary form. Completing the square over the rationals puts it in diagonal form: a times x squared, plus b times y squared, plus c times z squared. Multiply through by a common denominator to make the coefficients integers. None of the transformations affects whether there is a nonzero rational zero.

We can reduce further until a, b, and c are squarefree and pairwise coprime. Remove any square factor from one coefficient by absorbing it into that coordinate. If a prime divides two coefficients but not the third, substitute that prime times the third coordinate and divide the entire equation by the prime. After removing new square factors, the total size of the coefficients decreases. Repeating this process ends with coefficients having no shared prime factors. A prime dividing all three coefficients can simply be divided out. We will call this the reduced form.

If the original form has a nontrivial solution over each completion, then so does the reduced form: our substitutions are invertible over Q, hence also over every completion.

Now suppose the reduced form has a nonzero real solution. Because all three coefficients are nonzero, they cannot all have the same sign. Multiply the equation by minus one and permute the variables if necessary so that a and b are positive and c is negative.

The real condition has become a statement about the geometry of two positive squares balancing a negative one. The other local conditions will become instructions for constructing a lattice.

## What an odd prime dividing a coefficient tells us

Let p be an odd prime dividing a. Because a is squarefree and relatively prime to b and c, a is divisible by p exactly once, while b and c are units modulo p.

Assume the equation has a nontrivial solution over Q-p. Multiply that solution by a power of p so its coordinates lie in the p-adic integers and at least one coordinate is a unit. Reduce the equation modulo p. We obtain b times y squared plus c times z squared equals zero modulo p.

The two remaining coordinates cannot both vanish modulo p. If they did, the equation before reduction would have a term a times x squared of valuation one, while the other two terms would have valuation at least two; these could not cancel unless x were also divisible by p, contradicting the primitivity of our chosen vector.

Thus y and z are both units modulo p. Divide by z squared. We have found a number u modulo p such that b times u squared plus c equals zero. That is, negative b c is a quadratic residue modulo p. This is a necessary consequence of local solvability, not an extra assumption invented for our proof.

Exactly the same reasoning works for a prime dividing b or c, with the roles of the coordinates rotated. We have turned every relevant odd prime into one linear congruence between two coordinates.

## Congruences become a lattice

For each odd prime p dividing a, choose u with b u squared plus c divisible by p. Define a sublattice of integer triples by requiring y congruent to u z modulo p. This is an index-p sublattice of the full integer lattice. More importantly, the quadratic form is divisible by p at every point of it. Indeed, the a x squared term vanishes modulo p; replacing y by u z makes the remaining terms vanish as well.

For a prime dividing b or c, build the analogous index-p sublattice. We get one congruence for each odd prime dividing the product a b c.

We must handle the prime two. Here the lattice is simple enough to write down without a square-root test. If the product a b c is odd, require x plus y plus z to be even. This defines a lattice of index two. Because the three coefficients are all odd, the value of the form is even on that lattice.

If the product is even, exactly one coefficient, say a, is even; squarefreeness makes it twice an odd integer. We want the form divisible by four. If b plus c is divisible by four, require x even and y and z of the same parity. If b plus c is congruent to two modulo four, require x, y, and z all of the same parity. Either choice gives an index-four lattice, and the value of the quadratic form vanishes modulo four. You can check the first case by considering whether y and z are both odd or both even, and the second by considering whether all three are odd or all are even.

Intersect the lattices for all relevant primes. The Chinese remainder theorem tells us that these independent congruences multiply their indices. If D is the absolute value of a b c, the resulting lattice has index exactly two D in the full integer lattice. Every point of this lattice has a form value divisible by two D.

This is the arithmetic half of the proof. It does not yet give a point where the form is zero. A multiple of two D could be very large. We now use geometry to force it to be small.

## Why a large enough convex body cannot avoid a lattice

Here is the geometry-of-numbers principle we need. Let L be a full lattice in three-dimensional real space. A centrally symmetric convex body with volume strictly larger than eight times the volume of a fundamental lattice cell contains a nonzero lattice point. This is the three-dimensional form of Minkowski's convex body theorem.

The proof is worth recalling. Shrink the body by a factor of two in every direction; its volume becomes more than the volume of one fundamental cell. Translate the shrunken body's points back into that fundamental cell modulo the lattice. By a volume pigeonhole argument, two distinct points land at the same position. Their difference is a nonzero lattice vector. Because the original body was symmetric and convex, the difference belongs to it. There is the promised point.

For our constructed lattice the fundamental volume is two D. We therefore need a centrally symmetric convex body of volume greater than sixteen D. We should also arrange that the value of our quadratic form lies strictly between negative two D and positive two D throughout the body.

A ball is not the best choice. Instead take a cylinder with an elliptical cross-section. Require a times x squared plus b times y squared to be less than two D, and separately require the absolute value of c times z squared to be less than two D.

The area of the elliptical cross-section is two pi D divided by the square root of a b. The height of the cylinder is twice the square root of two D divided by the absolute value of c. Multiplying them gives four times the square root of two, times pi, times D.

That constant, four times the square root of two times pi, is greater than sixteen. The cylinder is therefore large enough for Minkowski's theorem to produce a nonzero point of our lattice inside it.

At this point, both halves of the proof meet. The lattice says the form value is an integer multiple of two D. The cylinder says its absolute value is smaller than two D: it is the difference between two quantities that are each nonnegative and smaller than two D. The only integer multiple of two D inside that open interval is zero.

So the nonzero lattice point is an exact integer zero of the quadratic form. We have proved a rational solution exists, because an integer solution is a rational one.

## What exactly have we proved?

The theorem can be stated without mentioning cylinders. A nondegenerate ternary quadratic form over the rationals has a nontrivial rational zero if and only if it has a nontrivial zero over the reals and over Q-p for every prime p. The easy direction is inclusion of the rationals in every completion. The difficult direction is the lattice proof we just gave after diagonalization and reduction.

Something stronger is hiding in the construction. We did not really need to test every possible prime separately. Away from the primes dividing twice the product of the three coefficients, the reduced ternary form has unit coefficients modulo p. A nonzero zero then exists automatically over the finite field and lifts by Hensel's lemma. So only finitely many primes need direct checking.

There is also an important limit. This argument is specific to quadratic forms. A random cubic equation need not obey such a local-to-global principle. We should not replace the theorem's precise scope by the slogan that local consistency always produces a global solution.

For the next lecture, we will translate this ternary theorem into the language of Hilbert symbols. Hilbert reciprocity then yields an even sharper statement: for a ternary form, one local condition is redundant. That fact will make the higher-dimensional proof possible, because we will deliberately concentrate all the uncontrolled arithmetic at one auxiliary prime.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Let \(q(x,y,z)=ax^2+by^2+cz^2\), with \(abc\ne0\), pairwise coprime squarefree integer coefficients, and assume \(a,b>0>c\). Put \(D=|abc|\).

For odd \(p\mid a\), the local condition gives \(u_p\) with \(bu_p^2+c\equiv0\pmod p\). Put \(\Lambda_p=\{(x,y,z)\in\mathbb Z^3:y\equiv u_p z\pmod p\}\). Similarly for \(p\mid b,c\). Then \([\mathbb Z^3:\Lambda_p]=p\) and \(q(\Lambda_p)\subseteq p\mathbb Z\).

At 2, when \(abc\) is odd set \(\Lambda_2=\{x+y+z\equiv0\pmod2\}\) of index 2, with \(q(\Lambda_2)\subseteq2\mathbb Z\). When \(a\) is even, use either \(\{x\equiv0\pmod2,\ y\equiv z\pmod2\}\) if \(b+c\equiv0\pmod4\), or \(\{x\equiv y\equiv z\pmod2\}\) if \(b+c\equiv2\pmod4\); each has index 4 and \(q(\Lambda_2)\subseteq4\mathbb Z\).

Set \(\Lambda=\bigcap_{p\mid 2D}\Lambda_p\). Chinese remainder independence yields

\[
[\mathbb Z^3:\Lambda]=2D,\qquad q(\Lambda)\subseteq 2D\mathbb Z.
\]

The symmetric convex cylinder

\[
C=\{(x,y,z)\in\mathbb R^3:ax^2+by^2<2D,\ |c|z^2<2D\}
\]

has volume \(\frac{2\pi D}{\sqrt{ab}}\cdot2\sqrt{\frac{2D}{|c|}}=4\sqrt2\pi D>16D=2^3\det\Lambda\). Minkowski yields \(0\ne v\in\Lambda\cap C\). Since \(|q(v)|<2D\) and \(q(v)\in2D\mathbb Z\), necessarily \(q(v)=0\).

**Scope:** This proves local-to-global isotropy for nondegenerate *ternary* forms over \(\mathbb Q\). It does not prove local-to-global for arbitrary degrees, integral representation of a specified integer, or forms over arbitrary number fields.

### Exercises

1. For \(q=x^2+y^2-5z^2\), write the necessary lattice congruences explicitly and find the solution \((1,2,1)\).
2. Verify both index-four lattices at the prime 2 by considering coordinate parities.
3. Recompute the cylinder volume without abbreviating \(D\), and verify that the final constant is greater than sixteen.
4. Give a proof of Minkowski's convex body theorem from a fundamental parallelepiped and the volume pigeonhole principle.
5. Show that a ternary form with all three coefficients units in \(\mathbb Z_p\), for odd \(p\), has a nonsingular nonzero zero modulo \(p\).

## Sources and reading

- Michael Stoll, *Introductory Number Theory*, sections 16–18, especially the Minkowski cylinder proof of Legendre's theorem: https://www.mathe2.uni-bayreuth.de/stoll/lecture-notes/IntroductoryNumberTheory.pdf
- John Voight, *Quaternion Algebras*, chapter 14.3, Legendre's theorem and Hasse–Minkowski: https://link.springer.com/chapter/10.1007/978-3-030-56694-4_14
- Wikipedia: [Minkowski's theorem](https://en.wikipedia.org/wiki/Minkowski%27s_theorem), [Hasse–Minkowski theorem](https://en.wikipedia.org/wiki/Hasse%E2%80%93Minkowski_theorem), [Quadratic form](https://en.wikipedia.org/wiki/Quadratic_form).

**Proof scope:** Complete lattice-and-volume proof of Legendre's local-to-global theorem for ternary quadratic forms over \(\mathbb Q\), including the prime-2 lattice and the exact determinant computation.
