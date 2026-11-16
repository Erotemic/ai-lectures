# 073000 - Effective Chabauty–Coleman Bounds on Rational Points

**Track:** Abstract Algebra. **Background:** algebraic curves, Jacobians, Mordell–Weil groups, reduction modulo primes, and p-adic analysis. **Central question:** when can one certify that a search has found every rational point on a curve?

<!-- BEGIN SPOKEN LECTURE -->

# Finding points is easier than proving completeness

A computer can search through thousands of rational coordinates on an algebraic curve. It can report solutions of small height, and it may discover patterns that suggest no more solutions exist. But the word “all” asks for a theorem. A bound on the search box is not a bound on the height of every possible rational point. Some rational points can hide at astonishingly large heights.

For a curve of genus at least two, a fundamental finiteness theorem says that there are only finitely many rational points. The theorem does not, by itself, hand us a list. The Chabauty–Coleman method provides a way to turn certain arithmetic information into an explicit upper bound, and sometimes into a complete list.

The method joins three geometries that look different at first: the geometry of the curve, the arithmetic of its Jacobian, and the geometry seen under a p-adic microscope. Its key restriction is just as important as its power. The rank of the Jacobian's rational points must be strictly smaller than the genus for the classical form of the method to operate.

# Put the curve inside its Jacobian

Choose a rational base point on a smooth projective curve. To any other point, assign the divisor class represented by the new point minus the base point. This maps the curve into its Jacobian, an abelian variety whose dimension equals the curve's genus.

Why is that useful? Because rational points on an abelian variety form a finitely generated group. Its free rank measures the number of independent non-torsion directions. The curve itself is a one-dimensional geometric object sitting inside the Jacobian, while the rational points on the Jacobian generate an arithmetic lattice.

This is not an ordinary Euclidean lattice-intersection problem. The Jacobian is algebraic, and we need to take its points into a p-adic completion. Yet the dimension comparison survives. If the genus is two and the rank is one, there is at least one independent differential direction that annihilates the p-adic closure of the rational group. Restricting that differential to the curve creates a function whose rational zeros can be counted locally.

The mere inequality between rank and genus does not identify the rational points. It gives us room to construct analytic constraints that every rational point must satisfy.

# Why a prime helps rather than hides information

Pick a prime at which the curve has good reduction. Reduce its defining equations modulo that prime. The resulting finite-field curve has only finitely many points, and those points divide the p-adic curve into residue disks.

Each rational point reduces into one of these disks. We are not claiming that reducing a rational point determines it uniquely. Usually infinitely many p-adic points lie above a single finite-field point. Instead, reduction gives us an organized finite collection of local regions on which analytic expansions can be controlled.

The p-adic numbers behave differently from the real numbers. A sequence is close when its difference is divisible by a high power of the prime. Power-series expansions can converge on entire residue disks, making the number of zeros accessible to arithmetic estimates. Coleman integration builds p-adic analytic functions by integrating differentials along the curve in a way compatible with the Jacobian's group structure.

Now take a differential whose Coleman integral vanishes on the relevant Mordell–Weil subgroup. Every rational point of the curve must then be a zero of the corresponding Coleman function, with the base point chosen to normalize the integral. A theorem about how many zeros can occur in each residue disk turns this into an arithmetic bound.

# The clean global bound

For a smooth projective curve of genus at least two over the rational numbers, assume its Jacobian has Mordell–Weil rank smaller than the genus. Choose a prime of good reduction larger than twice the genus. Under precisely these conditions, Coleman's theorem bounds the number of rational points by the number of points on the reduced curve, plus twice the genus minus two.

This formula has a remarkably concrete character. The finite-field count can be calculated by enumerating residues and checking which right-hand sides are squares. The genus comes from the geometry. The difficult part is establishing the rank hypothesis; it cannot be supplied by wishful thinking or by a small numerical search.

Even after the global bound is known, a list found by search is complete only if the number of known distinct points meets that bound, or if sharper disk-by-disk analysis excludes the remaining possibilities. A bound of eight combined with a list of five does not prove that the list is complete. It leaves space for three more points, perhaps at heights far beyond the original search.

# A six-point reduction count

Consider a genus-two hyperelliptic curve defined by the square of y equal to the fifth power of x, plus x, plus one. Work modulo five. The derivative of that polynomial is one modulo five, so the polynomial has no repeated roots there. The reduction is smooth, and five is larger than twice the genus.

For each of the five possible x-coordinates, evaluate the polynomial modulo five. The results are one, three, zero, two, and four. One and four each have two square roots. Zero has one. Two and three have none. That produces five affine points over the field with five elements. An odd-degree hyperelliptic model has one additional point at infinity. The finite-field curve therefore has six points.

If the Jacobian of this particular rational curve had rank strictly less than two, Coleman's bound would give at most eight rational points. Notice the conditional. We have checked smooth reduction and counted finite-field points, but we have not established the rank. It would be mathematically incorrect to announce an eight-point bound for this curve without that separate arithmetic certificate.

This example shows how a valid computation is assembled from independent claims. A point count may be elementary. A rank computation can involve descent, heights, and saturation. The p-adic zero counting then combines them.

# From a bound to an effective census

An effective Chabauty calculation works more finely than the global count. It computes expansions of annihilating Coleman integrals on individual residue disks, often using a chosen basis of regular differentials. Zeros are isolated with controlled p-adic precision. Rational candidates are lifted and checked in the original equations.

One also needs proof that the group information is complete enough. If we work with an unverified finite-index subgroup of the Jacobian, missing cosets can invalidate the annihilator construction or the claim that all rational points have been covered. Saturation tests and explicit rank bounds belong in the proof record, not merely in a software log.

Sometimes Coleman integration leaves several candidates in a disk. A Mordell–Weil sieve can impose congruence conditions at additional primes and eliminate residue classes that cannot correspond to rational points. The two methods complement each other: p-adic analysis controls local zeros, and the sieve enforces global group compatibility.

There are also important limits. If the rank is at least the genus, the classical dimension argument no longer guarantees a nonzero annihilating differential. Bad reduction requires modified analysis. For more general curves or higher-rank situations, nonabelian Chabauty and related methods enlarge the collection of constraints, but they do not erase the need to certify hypotheses.

# What a rigorous answer looks like

A finished point census should record the curve and its smooth model; the chosen prime and proof of good reduction; the exact finite-field count; a certified Mordell–Weil rank bound and subgroup information; the Coleman integrals and precision bounds; and a list of rational points checked in the original equations. It must explicitly explain why every possible residue disk has been exhausted.

That is the conceptual achievement of effective Chabauty–Coleman theory. It transforms an open-ended search into a finite collection of analytic and arithmetic obligations. The curve supplies geometry, the Jacobian supplies group structure, reduction supplies finitely many local neighborhoods, and p-adic integration supplies constraints. When those ingredients meet their hypotheses, “we found these points” can become “these are all the points.”

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Let `C/Q` be smooth, projective, genus `g>=2`, with rational base point `b`, Jacobian `J`, and rank `r=rank J(Q)<g`. The Abel–Jacobi map `i_b:C -> J`, `P |-> [P-b]`, makes Coleman integrals of annihilating holomorphic differentials vanish on `C(Q)` after normalization. For a prime of good reduction `p>2g`, Coleman's bound is
\[
\#C(\mathbb Q)\leq \#C(\mathbb F_p)+2g-2.
\]
The rank inequality and good reduction are **hypotheses**, not consequences of the point count. An explicit effective result also requires certified group information and disk-by-disk root isolation, possibly with a Mordell–Weil sieve.

Worked count: `C:y^2=x^5+x+1` has `g=2`. Modulo `5`, `f'(x)=5x^4+1=1`, hence squarefree. For `x=0,1,2,3,4`, values `f(x) mod 5` are `(1,3,0,2,4)`. These contribute `(2,0,1,0,2)` affine points, plus one at infinity: `#C(F_5)=6`. **Only if** `rank J(Q)<2`, the bound would be `#C(Q)<=8`. No claim about the actual rank or exhaustive rational-point set is made here.

### Exercises with answers

1. Why does one rational point not determine the residue disk above its reduction? **Answer:** infinitely many p-adic points generally reduce to that finite-field point.
2. In genus three, what rank condition is required for classical Chabauty? **Answer:** rank at most two.
3. If `#C(F_p)=10`, `g=3`, and all hypotheses hold, what is Coleman's upper bound? **Answer:** fourteen.
4. Why is a bound of eight and a list of five points not a complete census? **Answer:** the bound allows up to three additional rational points.

### Reading and source notes

- [Coleman–Chabauty bounds and rank hypotheses](https://doi.org/10.1016/S0764-4442(00)80041-5), discussion of the rank condition and bounds.
- [Chabauty and Beyond: Explicit p-adic Methods for Rational Points](https://doi.org/10.1137/25M1805011), detailed modern account of computations, sieves, and certified bounds.
