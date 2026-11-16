# 077000 - Quadratic Chabauty and p-Adic Height Pairings

**Track:** Abstract Algebra. **Background:** Jacobians, Mordell–Weil rank, p-adic integration, height pairings, and classical Chabauty. **Central question:** how can a quadratic height constraint still isolate rational points when the Jacobian rank is too large for ordinary Chabauty?

<!-- BEGIN SPOKEN LECTURE -->

# A dimension argument reaches its limit

Suppose we have a smooth projective curve of genus two, and we want to list all its rational points. Its Jacobian is a two-dimensional abelian variety. If the rank of the group of rational points of the Jacobian is one, classical Chabauty has a useful dimension advantage: one can find a differential whose p-adic integral vanishes on the rational group. Zeros of that integral constrain rational points on the curve.

Now suppose the rank is two. The elementary dimension count has disappeared. There need not be a nonzero holomorphic differential annihilating the rational group. This does not prove that the rational points cannot be determined. It tells us that linear p-adic integrals, by themselves, may no longer cut out a finite set.

Quadratic Chabauty replaces some of that missing linear information with a height pairing. The crucial new constraint is quadratic rather than linear in the group coordinates. The price is more arithmetic: the height depends on local data at several primes and on geometric information about the Jacobian. We must be careful not to call every quadratic-looking analytic expression a certified rational-point sieve.

# What a height pairing remembers

An ordinary height measures the arithmetic complexity of a rational point. A canonical height on an abelian variety behaves quadratically under multiplication: multiplying a point by an integer n multiplies its canonical height by n squared. Polarization produces a bilinear pairing.

There are p-adic analogues. Their values live in a p-adic field rather than the real numbers, so they are not distances or measures of numerical size in the usual sense. Nevertheless, their algebraic behavior carries useful information. If a subgroup has basis points P and Q, an appropriate p-adic height can be expressed on their integer combinations by a quadratic polynomial in the two coefficients. Its mixed term records the pairing between P and Q.

The same height can be assembled from local contributions. The contribution at the chosen prime p is accessible through p-adic integration, while contributions at other primes reflect reduction, intersection behavior, and arithmetic geometry. Rational points impose global compatibility among these local terms. A p-adic point selected at random does not generally satisfy that compatibility.

# A new kind of zero condition

Embed the curve into its Jacobian using a rational base point. For each rational point of the curve, the associated Jacobian point belongs to the Mordell–Weil group. Its p-adic height can be calculated in two different ways: from group coordinates through the height pairing, and from local geometry through suitable p-adic functions on the curve.

Subtracting these descriptions produces locally analytic constraints. In explicit quadratic Chabauty, the non-p local height contributions often range over a finite computable set. Instead of asking for the zeros of one Coleman integral, one asks which p-adic points satisfy one of several equations involving p-adic heights and iterated integrals.

It is essential that the finite set of allowed local contributions be justified. If we simply choose a handful of constants that fit the rational points already found, we have constructed a pattern, not a proof. And finding p-adic solutions of the height equations does not immediately prove those solutions rational. The method supplies a finite candidate set containing rational points, and additional arithmetic information may be needed to eliminate the other candidates.

# The refined rank condition

There is an especially illuminating version of the dimension count. Let g be the genus of the curve, r the Mordell–Weil rank of its Jacobian, and rho the rank of the Néron–Severi group of that Jacobian over the rationals. In the setting of the Balakrishnan–Dogra quadratic Chabauty theorem, the inequality is that r is strictly smaller than g plus rho minus one.

Consider g equal to two, rho equal to two, and r equal to two. Classical Chabauty fails its familiar inequality r less than g: two is not smaller than two. But quadratic Chabauty meets its inequality: two is smaller than three. The extra divisor class supplies an additional source of arithmetic structure.

This numerical check is an illustration of the hypothesis, not a claim that every genus-two Jacobian has Néron–Severi rank two. For many Jacobians, the Néron–Severi rank is one, and the inequality gives no improvement over classical Chabauty. Even when it holds, further geometric and computational assumptions enter an effective implementation.

# A small algebraic model of the pairing

Take a rank-two free abelian group with basis P and Q. Imagine a symmetric bilinear p-adic height pairing with entries a, b, and c. The height of mP plus nQ is then a times m squared, plus twice b times mn, plus c times n squared. The mixed term matters: a quadratic constraint cannot be recovered by separately checking only the multiples of P and the multiples of Q.

If P and Q are replaced by another integral basis, the matrix of this pairing changes by congruence, but the quadratic value attached to a group element does not change. That is why the method is about arithmetic objects, not one preferred coordinate table. For an actual Jacobian, the pairing matrix and the local height functions must be computed, with normalization choices recorded consistently.

A p-adic quadratic form need not be positive. Calling its diagonal entries “energies” would be misleading. The crucial property is compatibility of its algebraic variation with the group law.

# From candidate points to a complete list

An effective calculation therefore has several layers. Certify the curve and its reduction data. Obtain a sufficiently controlled Mordell–Weil subgroup and rank information. Compute the relevant p-adic integrals and height pairings. Bound local contributions away from p. Isolate all p-adic solutions of the resulting finite family of equations with justified precision. Finally, test rational candidates and use sieves or additional constraints to exclude solutions that do not come from rational points.

At each stage, “we found no others” must become a verifiable statement about the entire remaining region. Root isolation is different from evaluating a function at a grid of p-adic approximations. A finite candidate set is different from a complete set of rational points. And an upper bound on the rank is different from a verified basis of the rational group.

Quadratic Chabauty teaches a general mathematical lesson. When a linear obstruction is too weak, a nonlinear arithmetic invariant may restore finiteness. But the strength of the conclusion depends on all of its ingredients: geometric classes, global heights, local analytic formulas, and proofs that no possible residue disk has been silently omitted.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Write `C/Q` for a smooth projective curve of genus `g>=2`, `J` for its Jacobian, `r=rank J(Q)`, and `rho=rank NS(J)`. The familiar Coleman dimension condition is `r<g`. An influential quadratic Chabauty finiteness criterion under the corresponding geometric hypotheses is
\[
r<g+\rho-1.
\]
For `(g,r,rho)=(2,2,2)`, `2<2+2-1=3` holds, while `r<g` does not. **Neither** condition alone identifies a rational point; a finite quadratic Chabauty locus may properly contain `C(Q)`.

A bilinear p-adic height pairing `h(.,.)` induces `q(mP+nQ)=m^2 h(P,P)+2mn h(P,Q)+n^2 h(Q,Q)` on a rank-two subgroup, subject to the chosen normalization. Global heights decompose into local contributions. In explicit implementations, possible contributions away from `p` must be calculated or bounded and p-adic analytic equations must be solved with certified error control. Such a pairing is not generally positive definite.

### Exercises with answers

1. For `g=2`, `rho=1`, `r=2`, does the displayed quadratic criterion hold? **Answer:** No; `2<2` is false.
2. For `q(m,n)=3m^2+2mn+5n^2`, find `q(1,2)`. **Answer:** `3+4+20=27`.
3. Does a finite set of p-adic candidate points imply all are rational? **Answer:** No; a candidate locus only contains the rational points.
4. What additional arithmetic data are needed to convert a p-adic root count into a rational-point census? **Answer:** Verified Mordell–Weil information and a justification that every remaining p-adic candidate is either rational and checked or excluded.

### Reading and source notes

- [Balakrishnan and Dogra, Quadratic Chabauty and rational points I: p-adic heights](https://arxiv.org/abs/1601.00388), original quadratic Chabauty setting and hypotheses.
- [Balakrishnan, Besser and Müller, Quadratic Chabauty: p-adic height pairings and integral points](https://arxiv.org/abs/1302.2944), explicit height computation and integral-point applications.
- [Chabauty and Beyond (ICM 2026)](https://epubs.siam.org/doi/10.1137/25M1805011), review of the rank condition and effective methods.
