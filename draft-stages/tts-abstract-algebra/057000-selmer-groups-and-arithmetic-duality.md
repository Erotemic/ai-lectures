# 057000 — Selmer Groups: Global Points, Local Tests, and Arithmetic Duality

**Track:** Abstract Algebra. **Background:** elliptic curves, Galois cohomology, short exact sequences, and completions of number fields. **Central question:** why can an equation have solutions in every completion of a number field without having a global rational solution?

<!-- BEGIN SPOKEN LECTURE -->

# A puzzle about solving equations everywhere

Suppose we are trying to find a rational point on a curve. An obvious first question is whether it has a real point. Then we can ask whether it has a solution modulo two, modulo three, or modulo any other prime. We can even ask for solutions in the p-adic numbers, which retain all powers of a fixed prime at once. If an equation has no solution in one of these places, it cannot have a rational solution.

But the converse is a much deeper question. Passing every local test does not always guarantee a global rational point. Arithmetic geometry turns that gap into an object we can study. The Selmer group collects certain locally permissible cohomology classes, while the Tate–Shafarevich group records a particular failure of the local-to-global principle for torsors under an elliptic curve.

We will build the idea rather than treat either group as a black box. Along the way, we will discover why exact sequences are more useful than an isolated count of rational points.

# From doubling points to a cohomology class

Let E be an elliptic curve over a number field K. Its rational points form an abelian group, with the point at infinity as identity. Fix a positive integer n. Multiplication by n takes a point P and adds it to itself n times. Over an algebraic closure, the points killed by multiplication by n form the finite group E[n]. In characteristic zero this group has n squared elements, although they need not all be defined over K.

There is an exact sequence of Galois modules: n-torsion points include into all algebraic points, followed by multiplication by n. When we take Galois cohomology, a rational point P determines a class measuring the obstruction to choosing an n-th division point over K. Choose Q over an algebraic closure with n Q equal to P. Every Galois automorphism sends Q to another division point; the difference between its image and Q is n-torsion. These differences form a cocycle.

Changing Q changes the cocycle by a coboundary. Thus P defines a well-defined cohomology class, and two rational points differing by an n-fold multiple define the same class. This gives an injection of E(K) modulo n E(K) into the first cohomology group with coefficients in E[n].

The construction has an important interpretation. A rational point supplies a global certificate that its cohomological class comes from division on E. A general cohomology class need not have that certificate.

# The local condition

Now repeat the construction over every completion of K. For the rational numbers, there is the real completion and a p-adic completion for each prime p. Any global rational point yields a division class that looks legitimate in all these local settings.

The n-Selmer group is formed by taking those global first-cohomology classes whose restriction at every place lies in the image of the corresponding local Kummer map. Membership therefore consists of two demands: the class must be global cohomological data, and it must pass each local point-lifting test.

The Selmer group is finite for an elliptic curve over a number field and fixed n. That makes it a usable approximation to the quotient of rational points by n-fold multiples. But it may be larger than that quotient, because local validity need not imply the existence of a global point.

There is a canonical exact sequence whose first term is rational points modulo n, whose middle term is the Selmer group, and whose last term is the n-torsion subgroup of the Tate–Shafarevich group. This single sequence identifies exactly what the Selmer computation knows and what it has not proved.

# A simpler model: square classes

Before working with an elliptic curve, look at the multiplicative group. The Kummer sequence for square roots identifies first cohomology with square classes of nonzero rational numbers. Two numbers represent the same class when their quotient is a rational square.

Take the class of minus one. It is not a square in the real numbers, so its failure is already visible at the real place. Take the class of five. It is not a square in the three-adic numbers: a three-adic square that is a unit has square residue modulo three, but five has residue two. Both examples show how a local obstruction detects that a global square root cannot exist.

These are not examples of a Tate–Shafarevich obstruction. In each case, a local test actually fails. The interesting arithmetic failures arise when every local test passes but the required global object is still missing. For an elliptic curve that missing object is often best understood as a torsor: a curve on which E acts transitively but with no chosen rational origin.

# What duality contributes

Arithmetic duality relates local and global Galois cohomology. Local Tate duality supplies pairings between cohomology groups for a finite Galois module and its dual, subject to the correct degree shifts and dualizing twists. Global Poitou–Tate duality organizes these pairings into exact sequences with contributions from every place.

This framework provides more than a test for membership. It tells us that local conditions and their orthogonal complements interact through a global pairing. A Selmer structure for one Galois module has a dual Selmer structure for the dual module. Under appropriate hypotheses, the relevant finite groups and kernels can be compared through these pairings.

The Tate–Shafarevich group of an elliptic curve carries the Cassels–Tate pairing, with qualifications about divisibility and nondegeneracy. Its finiteness is not known in general. Thus one must not silently replace a Selmer-group computation by an unconditional statement that all globally missing rational points have been counted.

# A calculation is a bound, not an answer to everything

Suppose an n-Selmer group has four elements. What can we conclude? The quotient E(K) by n E(K) injects into a group of order four. This may constrain the Mordell–Weil rank, once we also account for rational n-torsion. It does not prove that there are four independent rational points, and it does not tell us which Selmer classes are represented by rational points.

This is the useful way to read arithmetic descent. A cohomology group packages candidate division data. Local conditions make that group finite and computable. Exactness explains how actual rational points sit inside the candidates. Arithmetic duality examines the missing classes and their compatibility across all places.

The resulting architecture is a precise response to a deceptively simple question: if an equation can be solved everywhere we know how to look locally, what is still missing from a global solution?

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Let K be a number field and E/K an elliptic curve. The Kummer exact sequence for n >= 2 is `0 -> E[n] -> E(Kbar) --[n]--> E(Kbar) -> 0` as Galois modules. Its connecting map gives
\[
\delta_K:E(K)/nE(K)\hookrightarrow H^1(K,E[n]).
\]
For `P in E(K)`, choose `Q in E(Kbar)` with `[n]Q=P`; the cocycle `sigma |-> sigma(Q)-Q` is E[n]-valued. At each place v let `delta_v` denote the analogous local map and `res_v` restriction. Then
\[
\operatorname{Sel}^{(n)}(E/K)=\{c\in H^1(K,E[n]):\operatorname{res}_v(c)\in\operatorname{im}\delta_v\ \forall v\}.
\]
The standard exact sequence is
\[
0\to E(K)/nE(K)\to \operatorname{Sel}^{(n)}(E/K)
\to \Sha(E/K)[n]\to 0.
\]
Here `Sha(E/K)=ker(H^1(K,E)->prod_v H^1(K_v,E))`. This identifies torsors that are trivial over every completion. It does *not* assert that Sha is finite.

If `E(K) ~= Z^r direct-sum T` by Mordell–Weil, then `|E(K)/nE(K)| = n^r |T/nT| = n^r |T[n]|`. In particular a finite n-Selmer calculation bounds the rank and does not by itself identify the rank unless Sha[n] is controlled.

For the multiplicative group, the Kummer sequence identifies `H^1(Q,mu_2)=Q^*/(Q^*)^2`. The class of `-1` fails over R, and the class of `5` fails over Q_3, since 5 mod 3 is the nonsquare class 2 among the nonzero residues modulo 3. Neither is a local-everywhere/global-nowhere example.

### Exercises with answers

1. Why does the cocycle `sigma(Q)-Q` lie in E[n]? **Answer:** multiplying by n gives `sigma(P)-P=0` because P is K-rational.
2. If E(K) has rank 2 and no rational n-torsion, what is `|E(K)/nE(K)|`? **Answer:** `n^2`.
3. If `|Sel^(2)(E/K)|=8` and E(K)[2] has 2 elements, what rank bound follows? **Answer:** `2^r * 2 <= 8`, hence `r <= 2`; a matching lower bound requires further information.
4. Does local solubility of every torsor force Sha to vanish? **Answer:** no; the kernel is precisely the obstruction group, and it need not be trivial.

### Reading and source notes

- [Bjorn Poonen, arithmetic geometry reading course and Selmer group notes](https://math.mit.edu/~poonen/reading.html), descent and the distinction between Selmer and Tate–Shafarevich groups.
- [Stanford Number Theory Seminar, duality and Birch–Swinnerton-Dyer references](https://math.stanford.edu/~conrad/BSDseminar/), local/global Galois duality and arithmetic descent.
- [J. S. Milne, Arithmetic Duality Theorems](https://www.jmilne.org/math/Books/ADTnot.pdf), cohomological duality for local and global fields.
