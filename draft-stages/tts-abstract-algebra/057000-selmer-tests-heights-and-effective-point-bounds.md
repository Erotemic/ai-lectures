# Selmer tests, heights, and effective point bounds

<!-- BEGIN SPOKEN LECTURE -->

# Selmer tests, heights, and effective point bounds

## Selmer Groups: Global Points, Local Tests, and Arithmetic Duality

Suppose we are trying to find a rational point on a curve. An obvious first question is whether it has a real point. Then we can ask whether it has a solution modulo two, modulo three, or modulo any other prime. We can even ask for solutions in the p-adic numbers, which retain all powers of a fixed prime at once. If an equation has no solution in one of these places, it cannot have a rational solution.

But the converse is a much deeper question. Passing every local test does not always guarantee a global rational point. Arithmetic geometry turns that gap into an object we can study. The Selmer group collects certain locally permissible cohomology classes, while the Tate–Shafarevich group records a particular failure of the local-to-global principle for torsors under an elliptic curve.

We will build the idea rather than treat either group as a black box. Along the way, we will discover why exact sequences are more useful than an isolated count of rational points.

## From doubling points to a cohomology class

Let E be an elliptic curve over a number field K. Its rational points form an abelian group, with the point at infinity as identity. Fix a positive integer n. Multiplication by n takes a point P and adds it to itself n times. Over an algebraic closure, the points killed by multiplication by n form the finite group E[n]. In characteristic zero this group has n squared elements, although they need not all be defined over K.

There is an exact sequence of Galois modules: n-torsion points include into all algebraic points, followed by multiplication by n. When we take Galois cohomology, a rational point P determines a class measuring the obstruction to choosing an n-th division point over K. Choose Q over an algebraic closure with n Q equal to P. Every Galois automorphism sends Q to another division point; the difference between its image and Q is n-torsion. These differences form a cocycle.

Changing Q changes the cocycle by a coboundary. Thus P defines a well-defined cohomology class, and two rational points differing by an n-fold multiple define the same class. This gives an injection of E(K) modulo n E(K) into the first cohomology group with coefficients in E[n].

The construction has an important interpretation. A rational point supplies a global certificate that its cohomological class comes from division on E. A general cohomology class need not have that certificate.

## The local condition

Now repeat the construction over every completion of K. For the rational numbers, there is the real completion and a p-adic completion for each prime p. Any global rational point yields a division class that looks legitimate in all these local settings.

The n-Selmer group is formed by taking those global first-cohomology classes whose restriction at every place lies in the image of the corresponding local Kummer map. Membership therefore consists of two demands: the class must be global cohomological data, and it must pass each local point-lifting test.

The Selmer group is finite for an elliptic curve over a number field and fixed n. That makes it a usable approximation to the quotient of rational points by n-fold multiples. But it may be larger than that quotient, because local validity need not imply the existence of a global point.

There is a canonical exact sequence whose first term is rational points modulo n, whose middle term is the Selmer group, and whose last term is the n-torsion subgroup of the Tate–Shafarevich group. This single sequence identifies exactly what the Selmer computation knows and what it has not proved.

## A simpler model: square classes

Before working with an elliptic curve, look at the multiplicative group. The Kummer sequence for square roots identifies first cohomology with square classes of nonzero rational numbers. Two numbers represent the same class when their quotient is a rational square.

Take the class of minus one. It is not a square in the real numbers, so its failure is already visible at the real place. Take the class of five. It is not a square in the three-adic numbers: a three-adic square that is a unit has square residue modulo three, but five has residue two. Both examples show how a local obstruction detects that a global square root cannot exist.

These are not examples of a Tate–Shafarevich obstruction. In each case, a local test actually fails. The interesting arithmetic failures arise when every local test passes but the required global object is still missing. For an elliptic curve that missing object is often best understood as a torsor: a curve on which E acts transitively but with no chosen rational origin.

## What duality contributes

Arithmetic duality relates local and global Galois cohomology. Local Tate duality supplies pairings between cohomology groups for a finite Galois module and its dual, subject to the correct degree shifts and dualizing twists. Global Poitou–Tate duality organizes these pairings into exact sequences with contributions from every place.

This framework provides more than a test for membership. It tells us that local conditions and their orthogonal complements interact through a global pairing. A Selmer structure for one Galois module has a dual Selmer structure for the dual module. Under appropriate hypotheses, the relevant finite groups and kernels can be compared through these pairings.

The Tate–Shafarevich group of an elliptic curve carries the Cassels–Tate pairing, with qualifications about divisibility and nondegeneracy. Its finiteness is not known in general. Thus one must not silently replace a Selmer-group computation by an unconditional statement that all globally missing rational points have been counted.

## A calculation is a bound, not an answer to everything

Suppose an n-Selmer group has four elements. What can we conclude? The quotient E(K) by n E(K) injects into a group of order four. This may constrain the Mordell–Weil rank, once we also account for rational n-torsion. It does not prove that there are four independent rational points, and it does not tell us which Selmer classes are represented by rational points.

This is the useful way to read arithmetic descent. A cohomology group packages candidate division data. Local conditions make that group finite and computable. Exactness explains how actual rational points sit inside the candidates. Arithmetic duality examines the missing classes and their compatibility across all places.

The resulting architecture is a precise response to a deceptively simple question: if an equation can be solved everywhere we know how to look locally, what is still missing from a global solution?

## Heights, Mordell–Weil, and Explicit Descent Algorithms

Take the equation y squared equals x cubed minus two. A rational solution is the point with coordinates three and five. Its reflected point, three and minus five, is another. The chord-and-tangent rule lets us combine these points and construct new rational points. We can even ask whether the first point has finite order, or whether repeated addition will produce infinitely many distinct points.

There is no obvious reason that such questions should be decided by finite calculations. Rational points have unbounded numerators and denominators. Checking a large box of possible fractions can find points, but failure to find another point is not proof that no such point exists. Explicit descent turns the infinite problem into controlled arithmetic in a finite collection of square classes, local fields, and covering curves.

The central achievement of the Mordell–Weil theorem is structural: for an elliptic curve over the rational numbers, the rational points form a finitely generated abelian group. Consequently there is a finite torsion subgroup and a free part with some nonnegative integer rank. The theorem does not hand us generators or the rank for a given curve. Descent helps produce the missing information.

## The tangent calculation is exact, not numerical evidence

On our example, consider the point three, five. The tangent slope is twenty-seven tenths. Doubling the point by the elliptic-curve group law gives a point whose x coordinate is one hundred twenty-nine over one hundred and whose y coordinate is negative three hundred eighty-three over one thousand.

Those denominators are an important feature, not a numerical inconvenience. They are the arithmetic footprint of repeated group operations on a curve. We can verify the resulting point by substitution into the cubic equation. What doubling does not tell us, on its own, is whether this process ever repeats.

For a curve with integral Weierstrass coefficients, the Nagell–Lutz theorem gives a powerful obstruction to an integral point being torsion. In this example the nonzero y coordinate is five, and its square does not divide the relevant discriminant quantity. Thus our point is not torsion. We have a concrete lower bound: the rank is at least one. But an infinite-order point does not prove the rank is exactly one; there might be other independent generators.

## The height measures arithmetic complexity

One way to avoid a fruitless search over fractions is to measure the size of a rational point. If the x coordinate is a reduced fraction with numerator a and denominator b, its logarithmic height is the logarithm of the larger of the absolute numerator and positive denominator. This simple function measures how complicated the rational coordinate has become.

On an elliptic curve, the naive height is corrected into the canonical height. The canonical height has the striking property that multiplying a point by an integer n multiplies its height by n squared. That quadratic rule makes the height into a positive-semidefinite quadratic form on rational points modulo torsion. It also allows a pairing of points, so independent points can be studied as an arithmetic lattice.

Height arguments help show finiteness when combined with a descent inequality. Roughly, if one knows the group modulo multiplication by two, every point can be represented as twice another point plus one of finitely many representatives. The height of the smaller point is approximately a quarter of the height of the original point, up to a controlled error. Iterating that reduction and invoking bounded-height finiteness is the mechanism behind the finite-generation proof.

## What two-descent actually computes

Now reduce the group modulo doubling. We are studying rational points up to the equivalence relation that two points differ by twice another rational point. The quotient is finite by Mordell–Weil, but finding it directly is difficult: we would have to know the rational points first.

The workaround is to pass through a cohomological group built from the two-torsion of the elliptic curve. Rational points determine cohomology classes through the Kummer map. To test whether a candidate class could arise from a rational point, examine it over the real numbers and over each p-adic field. The classes that pass all local tests form the two-Selmer group.

This is a computable finite group under standard algorithmic hypotheses. For an explicit model, local conditions reduce to solvability of associated covering curves in completions, supplemented by class-group and unit computations in number fields. Only finitely many primes require special treatment. The surviving Selmer classes yield an upper bound on the rational rank.

But there is a gap between locally soluble and globally soluble. A covering curve can have a point over every relevant completion and nevertheless have no rational point. The Tate–Shafarevich group records precisely this remaining obstruction in the exact sequence relating rational points modulo doubling to the two-Selmer group. Therefore a Selmer class is a candidate, not automatically a rational generator.

## A finite computation and its interpretation

Suppose a two-descent produces a Selmer group of dimension three as a vector space over the field of two elements, while the rational two-torsion has dimension one. Then the rank is at most two. To establish rank two, we still need two points proved independent, for example by a height pairing and a saturation argument. If we find only one independent point, the certified conclusion may remain that the rank is either one or two.

An upper bound from descent can become sharp after additional local tests, a four-descent, a Cassels–Tate pairing, or explicit investigation of covering curves. Rank lower bounds come from actual rational points. Rank upper bounds come from cohomological constraints. A complete answer must make the two meet and must also handle the index of the proposed generators.

This is why an algorithm may report a proven rank interval rather than one integer. The interval is honest mathematical information. A large point search alone, even with impressive computation, is not equivalent to a complete descent and saturation certificate.

## The constructive lesson

Explicit descent is a disciplined division of labor. Group laws construct examples. Heights control their complexity. Finite group computations constrain what classes are possible. Local solubility rules out impossible classes cheaply. Global rational points and height pairings give lower bounds and independence. Saturation addresses whether the points found generate the whole free group rather than a subgroup of finite index.

The curve y squared equals x cubed minus two makes this distinction vivid. We can write down one infinite-order point and its exact double immediately, but determining the entire Mordell–Weil group is a separate and deeper problem. Descent does not replace the infinite problem with a guess. It provides a chain of finite, checkable statements that progressively narrows the answer.

## Mordell–Weil Saturation and Height Pairings

Consider a curve given by y squared equals x cubed minus two. The point with coordinates three and five is rational, and its elliptic-curve double is the point with x coordinate one hundred twenty-nine over one hundred and y coordinate negative three hundred eighty-three over one thousand. Both points have infinite order. But they do not provide the same information about generators. The subgroup generated by the double misses the original point. It has index two in the subgroup generated by the original point.

This is a simple illustration of a serious problem in arithmetic geometry. An algorithm may prove that an elliptic curve has rank one and produce an infinite-order point. Even then, the point might be twice another rational point, or five times another, or a more complicated linear combination of undiscovered points. The rank is a dimension. Generating the whole Mordell–Weil group is a lattice problem.

A finite-index gap is not a technical annoyance. It changes the answer to a question such as, Can every rational point be written using these proposed generators and torsion? A correct result must distinguish three claims: we know some independent points, we know the rank, and we know a complete set of generators. The third claim requires saturation.

## Heights turn the group into a lattice

The Mordell–Weil theorem says that the rational points form a finitely generated abelian group. Once torsion is removed, it looks like integer lattice points in an r-dimensional space. Canonical height provides a geometry on that lattice.

The canonical height of n times a point is n squared times its height. This quadratic behavior makes it possible to define a symmetric height pairing. Given independent points P one through P r, we form a matrix whose entries are their pairwise height pairings. Its diagonal entries are individual canonical heights. Its off-diagonal entries measure how the points interact under addition.

If the determinant of this matrix is positive, the points are independent modulo torsion. For instance, the abstract matrix with rows two, one and one, three has determinant five. It is positive definite, so those two basis directions are independent. But such a determinant does not certify that the lattice they generate is the full lattice of rational points.

Suppose we replace a genuine generator Q by twice Q. Its canonical height is multiplied by four. In rank one, the height regulator therefore multiplies by four. In higher rank, replacing one lattice basis by an integer matrix of determinant d multiplies the regulator by d squared. The regulator detects index once both lattices are known. Without a certified full regulator, an observed determinant alone cannot tell us what index is missing.

## Prime-by-prime saturation

Now fix a prime number p. A proposed full-rank subgroup is p-saturated if there is no rational point outside that subgroup whose p-fold multiple lies inside it, after accounting correctly for torsion. Another way to say this is that the quotient by the subgroup has no p-torsion.

To test this, take linear combinations of the proposed generators with coefficients between zero and p minus one, not all zero modulo p. Ask whether any such combination is p times a rational point. If it is, a new rational point has been found. Replacing an appropriate generator enlarges the subgroup by index p. If no such division is possible, the subgroup is p-saturated.

In rank one the picture is clear. Start with the doubled point on our cubic curve. Testing p equal to two immediately finds its rational half, the point three, five. The original subgroup was not two-saturated. Enlarging it fixes that particular defect. But we have not proved that the new point generates all rational points on the curve. A further prime could still divide the remaining index.

For rank two, there are more combinations to inspect. Testing the divisibility of each generator separately is not enough. A combination such as P plus Q might be divisible by p even though neither P nor Q is. The search is over nonzero projective coefficient vectors modulo p. This is exactly the kind of finite computation that the word saturation is meant to organize.

## Local reduction gives finite obstructions

A direct attempt to divide a point by p amounts to solving polynomial equations with rational coordinates. That can be expensive. Instead, reduce the curve and the known points modulo carefully chosen good primes. The finite groups of points on the reduced curves reveal congruence obstructions to divisibility back over the rational numbers.

A crucial logical asymmetry appears. A failed congruence test can prove that no rational division exists. A congruence test that succeeds does not automatically construct the rational divisor. It may only leave a candidate alive. Combining reductions at several primes can often eliminate every candidate coefficient vector, proving p-saturation without a massive rational search.

The test depends on good reduction, the structure of the finite group, and the choice of auxiliary primes. Computational packages make these choices but a mathematical certificate should still say which part is proved: saturation at one prime, at all primes below a bound, or at every possible prime.

## How can finitely many primes suffice?

There are infinitely many primes. Testing the first hundred does not prove saturation at every prime. To make a final claim, an algorithm needs an independent argument bounding primes that could divide the index.

Canonical-height lower bounds for non-torsion points, together with height estimates for the current subgroup and lattice geometry, can provide such a bound. If there were an overlooked p-division for a sufficiently large p, its canonical height would become too small relative to those estimates. In practice the bound may be conservative. More refined arithmetic information can improve it.

An especially effective proof strategy has three distinct pieces. Establish the rank so the proposed generators have full rank. Compute a bound on possible prime divisors of the remaining finite index. Then certify saturation at each prime in that finite range. Torsion must be handled as well. Only after all three are complete does the phrase full Mordell–Weil group have its strongest meaning.

## A regulator can be evidence or a certificate

Imagine two independent points with a height pairing matrix whose determinant is twenty. We might suspect they generate a sublattice of index two in a full lattice whose regulator is five, because index two squares to four. But that suspicion requires an independent proof that five is the full regulator. It cannot be deduced simply because five is a pleasant number.

Conversely, if we have already established the full group by saturation, the resulting regulator is a meaningful invariant, suitable for arithmetic comparisons and conjectures. The process is not circular: height calculations help control possible indices; modular tests eliminate those indices; only then can the final regulator be certified.

The broader lesson is that an exact point and an exact group are different outputs. Rational coordinates certify membership. A nonsingular height pairing certifies independence. Descent certifies a rank bound. Saturation certifies that the lattice is complete. Each answers a different mathematical question, and none should be silently substituted for the others.

## Cassels-Tate Pairings: How an Obstruction Sharpens a Rank Bound

An elliptic curve may have rational points that we can write down explicitly, and still resist our attempts to determine its complete group of rational points. The group is finitely generated, so in principle it consists of finitely many free generators together with torsion. But the theorem that tells us this does not hand us the generators. Descent is one of the main ways to make progress.

Here is the difficulty. A descent calculation can list classes that pass every local test. Each class can be represented over every completion of the number field. Yet being possible over every completion does not guarantee coming from a rational point. The missing distinction is precisely where the Tate-Shafarevich group enters. And the Cassels-Tate pairing can sometimes prove that some of those locally possible classes cannot represent new free generators.

We will keep two claims separate throughout. A Selmer computation supplies an upper bound on rank. A Mordell-Weil search supplies a lower bound by constructing independent rational points. A pairing can improve the upper bound, but it does not automatically find the missing rational points, and it does not automatically resolve every obstruction.

## The exact sequence behind the mystery

Fix an elliptic curve over a number field and a prime p. Consider multiplication by p on the elliptic curve. On rational points, this map takes a point to its p-fold sum. Its cokernel measures which points cannot be obtained by multiplying another rational point by p. After modding out by p, the free rank and rational p-torsion appear as dimensions of a finite vector space over the field with p elements.

Now do the analogous construction not only over the number field, but over every local completion. The p-Selmer group consists of global cohomology classes satisfying appropriate local conditions. It is finite and computable in many explicit cases. Rational points modulo p inject into this group, but need not fill it. The quotient is the p-torsion in the Tate-Shafarevich group, traditionally abbreviated Sha.

Sha measures torsors that look soluble locally but have no rational point. This is why a Selmer class can survive every congruence and local test and yet fail to correspond to a rational point. The two obstructions are related, but they are not the same problem: local solubility belongs in the Selmer definition; global solubility belongs in the exact sequence connecting Selmer, rational points, and Sha.

Suppose, to make the count transparent, that the curve has no rational p-torsion. If the p-Selmer group has dimension four, the rank is at most four. That bound could be exact, or there could be nonzero Sha contributions. To make it smaller we need more information than the dimension alone.

## Pairing the surviving classes

The Cassels-Tate pairing assigns a value in the rationals modulo the integers to pairs of obstruction classes. Its construction uses global duality and local invariants. Very roughly, one lifts a class through a cohomological sequence, compares it with local choices, and sums local pairings. The global reciprocity law ensures the resulting answer is independent of choices under the theorem's hypotheses.

For an elliptic curve, the pairing is alternating in the usual formulation. An element pairs trivially with itself. When restricted to appropriate p-primary obstruction data, its finite matrix looks like a skew-symmetric bilinear form. Such a matrix has even rank over a field of odd characteristic. This parity becomes arithmetic information.

We should be careful with the domain. The canonical Cassels-Tate pairing lives on Sha, and its degeneracy properties require qualifications involving divisible subgroups. Computational descent methods also construct a related pairing directly on p-Selmer groups. In common p-descent settings, the radical of that Selmer pairing is the image of the p-squared Selmer group. These formulations fit together, but they should not be collapsed into the assertion that the first Selmer group is itself Sha.

## A four-dimensional calculation

Imagine that a three-Selmer computation yields four independent classes, represented by basis vectors one through four. Suppose the computed pairing has only one nontrivial block: the pairing of basis vector one with basis vector two is one modulo three, and reversing their order gives negative one modulo three. Every pairing involving the last two vectors vanishes.

The matrix then has rank two. Its radical is the two-dimensional span of vectors three and four. So not all four Selmer directions survive into the next descent stage. Under the standard Cassels pairing theorem, the image of the nine-Selmer group has dimension two, and the image of rational points modulo three must lie inside that image.

If the curve has no rational three-torsion, the rank is therefore at most two, instead of at most four. We have improved the bound by two without discovering a single new rational point. If, separately, we know two independent rational points, then rank two is proved. If we know only one, the pairing has not found a second point and the exact rank remains unresolved.

This example is an abstract pairing matrix, not a claim about a particular elliptic curve. Constructing the matrix for an actual curve requires arithmetic geometry: covering curves, local points, and precise local invariant calculations. The linear algebra at the end is simple; making its entries rigorous is the hard part.

## Why the pairing can have a radical

A student of elementary linear algebra might expect a perfect alternating pairing, with zero radical. But the arithmetic pairing can have a radical because divisible classes can pair trivially with everything. On the quotient of Sha by its maximal divisible subgroup, the relevant Cassels-Tate pairing is nondegenerate in an appropriate sense. To conclude a finite, perfect pairing on all of Sha, one usually needs an additional finiteness assumption.

This matters when presenting a rank certificate. A nonzero pairing value is decisive: it witnesses a genuine obstruction. Zero pairings are not always decisive. The radical may contain rational-point classes, higher-descent classes, or elements hidden by the chosen level of descent. One cannot infer that every class in the radical comes from a rational point.

Likewise, a computation of a pairing on a finite subgroup is not automatically a computation of the entire Tate-Shafarevich group. It can prove that particular obstruction classes are nontrivial, and it can reduce a bound, without settling whether Sha is finite or whether it contains further elements of higher prime-power order.

## A certificate has several layers

How should a complete rank proof be organized? Start with explicit rational points and prove that they are independent, perhaps with a height pairing. That establishes a lower bound. Next compute a Selmer group with rigorous local conditions. That establishes an initial upper bound. Then evaluate a Cassels-type pairing, if available, to shrink the allowable space of rational-point classes. Finally compare the resulting upper bound with the known lower bound.

When the bounds meet, the rank is certified. Yet there remains a separate question about generators: the known independent points might span a subgroup of finite index. A saturation computation, together with torsion determination and an index bound, addresses that problem. This is why a certified rank and a certified full Mordell-Weil group are different outputs.

The deeper picture is that local arithmetic creates a finite space of possibilities, global duality pairs those possibilities, and linear algebra rules out some combinations. A rank bound ceases to be a raw count of locally soluble coverings. It becomes a count corrected by a measurable obstruction to global solubility.

## Effective Chabauty-Coleman Bounds on Rational Points

A computer can search through thousands of rational coordinates on an algebraic curve. It can report solutions of small height, and it may discover patterns that suggest no more solutions exist. But the word “all” asks for a theorem. A bound on the search box is not a bound on the height of every possible rational point. Some rational points can hide at astonishingly large heights.

For a curve of genus at least two, a fundamental finiteness theorem says that there are only finitely many rational points. The theorem does not, by itself, hand us a list. The Chabauty–Coleman method provides a way to turn certain arithmetic information into an explicit upper bound, and sometimes into a complete list.

The method joins three geometries that look different at first: the geometry of the curve, the arithmetic of its Jacobian, and the geometry seen under a p-adic microscope. Its key restriction is just as important as its power. The rank of the Jacobian's rational points must be strictly smaller than the genus for the classical form of the method to operate.

## Put the curve inside its Jacobian

Choose a rational base point on a smooth projective curve. To any other point, assign the divisor class represented by the new point minus the base point. This maps the curve into its Jacobian, an abelian variety whose dimension equals the curve's genus.

Why is that useful? Because rational points on an abelian variety form a finitely generated group. Its free rank measures the number of independent non-torsion directions. The curve itself is a one-dimensional geometric object sitting inside the Jacobian, while the rational points on the Jacobian generate an arithmetic lattice.

This is not an ordinary Euclidean lattice-intersection problem. The Jacobian is algebraic, and we need to take its points into a p-adic completion. Yet the dimension comparison survives. If the genus is two and the rank is one, there is at least one independent differential direction that annihilates the p-adic closure of the rational group. Restricting that differential to the curve creates a function whose rational zeros can be counted locally.

The mere inequality between rank and genus does not identify the rational points. It gives us room to construct analytic constraints that every rational point must satisfy.

## Why a prime helps rather than hides information

Pick a prime at which the curve has good reduction. Reduce its defining equations modulo that prime. The resulting finite-field curve has only finitely many points, and those points divide the p-adic curve into residue disks.

Each rational point reduces into one of these disks. We are not claiming that reducing a rational point determines it uniquely. Usually infinitely many p-adic points lie above a single finite-field point. Instead, reduction gives us an organized finite collection of local regions on which analytic expansions can be controlled.

The p-adic numbers behave differently from the real numbers. A sequence is close when its difference is divisible by a high power of the prime. Power-series expansions can converge on entire residue disks, making the number of zeros accessible to arithmetic estimates. Coleman integration builds p-adic analytic functions by integrating differentials along the curve in a way compatible with the Jacobian's group structure.

Now take a differential whose Coleman integral vanishes on the relevant Mordell–Weil subgroup. Every rational point of the curve must then be a zero of the corresponding Coleman function, with the base point chosen to normalize the integral. A theorem about how many zeros can occur in each residue disk turns this into an arithmetic bound.

## The clean global bound

For a smooth projective curve of genus at least two over the rational numbers, assume its Jacobian has Mordell–Weil rank smaller than the genus. Choose a prime of good reduction larger than twice the genus. Under precisely these conditions, Coleman's theorem bounds the number of rational points by the number of points on the reduced curve, plus twice the genus minus two.

This formula has a remarkably concrete character. The finite-field count can be calculated by enumerating residues and checking which right-hand sides are squares. The genus comes from the geometry. The difficult part is establishing the rank hypothesis; it cannot be supplied by wishful thinking or by a small numerical search.

Even after the global bound is known, a list found by search is complete only if the number of known distinct points meets that bound, or if sharper disk-by-disk analysis excludes the remaining possibilities. A bound of eight combined with a list of five does not prove that the list is complete. It leaves space for three more points, perhaps at heights far beyond the original search.

## A six-point reduction count

Consider a genus-two hyperelliptic curve defined by the square of y equal to the fifth power of x, plus x, plus one. Work modulo five. The derivative of that polynomial is one modulo five, so the polynomial has no repeated roots there. The reduction is smooth, and five is larger than twice the genus.

For each of the five possible x-coordinates, evaluate the polynomial modulo five. The results are one, three, zero, two, and four. One and four each have two square roots. Zero has one. Two and three have none. That produces five affine points over the field with five elements. An odd-degree hyperelliptic model has one additional point at infinity. The finite-field curve therefore has six points.

If the Jacobian of this particular rational curve had rank strictly less than two, Coleman's bound would give at most eight rational points. Notice the conditional. We have checked smooth reduction and counted finite-field points, but we have not established the rank. It would be mathematically incorrect to announce an eight-point bound for this curve without that separate arithmetic certificate.

This example shows how a valid computation is assembled from independent claims. A point count may be elementary. A rank computation can involve descent, heights, and saturation. The p-adic zero counting then combines them.

## From a bound to an effective census

An effective Chabauty calculation works more finely than the global count. It computes expansions of annihilating Coleman integrals on individual residue disks, often using a chosen basis of regular differentials. Zeros are isolated with controlled p-adic precision. Rational candidates are lifted and checked in the original equations.

One also needs proof that the group information is complete enough. If we work with an unverified finite-index subgroup of the Jacobian, missing cosets can invalidate the annihilator construction or the claim that all rational points have been covered. Saturation tests and explicit rank bounds belong in the proof record, not merely in a software log.

Sometimes Coleman integration leaves several candidates in a disk. A Mordell–Weil sieve can impose congruence conditions at additional primes and eliminate residue classes that cannot correspond to rational points. The two methods complement each other: p-adic analysis controls local zeros, and the sieve enforces global group compatibility.

There are also important limits. If the rank is at least the genus, the classical dimension argument no longer guarantees a nonzero annihilating differential. Bad reduction requires modified analysis. For more general curves or higher-rank situations, nonabelian Chabauty and related methods enlarge the collection of constraints, but they do not erase the need to certify hypotheses.

## What a rigorous answer looks like

A finished point census should record the curve and its smooth model; the chosen prime and proof of good reduction; the exact finite-field count; a certified Mordell–Weil rank bound and subgroup information; the Coleman integrals and precision bounds; and a list of rational points checked in the original equations. It must explicitly explain why every possible residue disk has been exhausted.

That is the conceptual achievement of effective Chabauty–Coleman theory. It transforms an open-ended search into a finite collection of analytic and arithmetic obligations. The curve supplies geometry, the Jacobian supplies group structure, reduction supplies finitely many local neighborhoods, and p-adic integration supplies constraints. When those ingredients meet their hypotheses, “we found these points” can become “these are all the points.”

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Selmer Groups: Global Points, Local Tests, and Arithmetic Duality

**Track:** Abstract Algebra. **Background:** elliptic curves, Galois cohomology, short exact sequences, and completions of number fields. **Central question:** why can an equation have solutions in every completion of a number field without having a global rational solution?

#### Mathematical companion (not spoken)

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

##### Exercises with answers

1. Why does the cocycle `sigma(Q)-Q` lie in E[n]? **Answer:** multiplying by n gives `sigma(P)-P=0` because P is K-rational.
2. If E(K) has rank 2 and no rational n-torsion, what is `|E(K)/nE(K)|`? **Answer:** `n^2`.
3. If `|Sel^(2)(E/K)|=8` and E(K)[2] has 2 elements, what rank bound follows? **Answer:** `2^r * 2 <= 8`, hence `r <= 2`; a matching lower bound requires further information.
4. Does local solubility of every torsor force Sha to vanish? **Answer:** no; the kernel is precisely the obstruction group, and it need not be trivial.

##### Reading and source notes

- [Bjorn Poonen, arithmetic geometry reading course and Selmer group notes](https://math.mit.edu/~poonen/reading.html), descent and the distinction between Selmer and Tate–Shafarevich groups.
- [Stanford Number Theory Seminar, duality and Birch–Swinnerton-Dyer references](https://math.stanford.edu/~conrad/BSDseminar/), local/global Galois duality and arithmetic descent.
- [J. S. Milne, Arithmetic Duality Theorems](https://www.jmilne.org/math/Books/ADTnot.pdf), cohomological duality for local and global fields.

### Heights, Mordell–Weil, and Explicit Descent Algorithms

**Track:** Abstract Algebra. **Background:** elliptic curves, group laws, Galois cohomology, and Selmer groups. **Central question:** how can finite computations constrain an infinite group of rational points?

#### Mathematical companion (not spoken)

For `E: y^2=x^3-2`, `P=(3,5)` lies on E since `25=27-2`. With `a=0`, the tangent slope at P is `m=3x_P^2/(2y_P)=27/10`; hence
\[
x(2P)=m^2-2x_P=129/100,\qquad y(2P)=m(x_P-x(2P))-y_P=-383/1000.
\]
The integral short-Weierstrass discriminant is `Delta=-16(4a^3+27b^2)=-1728`. A nonzero integral torsion point on this model has `y^2 | (4a^3+27b^2)=108` by Nagell–Lutz; because `25` does not divide `108`, P has infinite order. This establishes `rank E(Q)>=1`, **not** an exact rank claim.

For an elliptic curve over Q, write `E(Q)=Z^r + E(Q)_tors` as an abstract group. The exact sequence for 2-descent is
\[
0\longrightarrow E(\mathbb Q)/2E(\mathbb Q)\longrightarrow \operatorname{Sel}^{(2)}(E/\mathbb Q)\longrightarrow \Sha(E/\mathbb Q)[2]\longrightarrow0.
\]
Thus `dim_F2 Sel2 = r + dim_F2 E(Q)[2] + dim_F2 Sha[2]`; in particular `r <= dim Sel2 - dim E(Q)[2]`. This is a *rank upper bound*, with no claim that every Selmer class is the image of a rational point. The logarithmic projective height of `x=a/b` in lowest terms is `h(x)=log max(|a|,|b|)`; the canonical height satisfies `hat h([n]P)=n^2 hat h(P)` and vanishes precisely on torsion over number fields.

##### Exercises with answers

1. Verify that `2P` is on E. **Answer:** `(-383/1000)^2 = (129/100)^3-2 = 146689/1000000`.
2. What does a Selmer dimension of four and rational 2-torsion dimension two prove? **Answer:** `r<=2`; it does not by itself prove rank two.
3. Why are a height bound and finiteness of bounded-height rational points useful? **Answer:** descent reduces large points to smaller-height representatives, leaving only finitely many possibilities up to the finite quotient.
4. Why is an independent point search not a proof of rank maximality? **Answer:** it gives a lower bound but cannot exclude unseen generators or a nontrivial Tate–Shafarevich obstruction.

##### Reading and source notes

- [Tom Fisher, Descent on elliptic curves](https://smf.emath.fr/node/152658), explicit Selmer groups and covering curves.
- [Magma Handbook, Mordell–Weil Groups and Descent Methods](https://docs.magma-maths.org/v2.30-1/ArithmeticGeometry/EllipticCurvesOverQAndNumberFields/mordell-weil.html), rank bounds, higher descents and generators.
- [J. S. Milne, Arithmetic Duality Theorems](https://www.jmilne.org/math/Books/ADTnot.pdf), cohomological background and local–global obstruction groups.

### Mordell–Weil Saturation and Height Pairings

**Track:** Abstract Algebra. **Background:** elliptic-curve group laws, Mordell–Weil finite generation, canonical heights, and descent. **Central question:** when do rational points we have found generate the entire group, rather than a subgroup of finite index?

#### Mathematical companion (not spoken)

On `E: y^2=x^3-2`, let `Q=(3,5)` and `P=2Q=(129/100,-383/1000)`. The subgroup `<P>` is a proper index-two subgroup of `<Q>` because Q has infinite order. **This does not assert** that `<Q>=E(Q)/E(Q)_tors`.

Write `G=E(K)/E(K)_tors`, assumed free of rank r, and let `L=<P_1,...,P_r>\subseteq G` have finite index d. The Néron–Tate pairing is
\[
\langle P,Q\rangle=\tfrac12(\widehat h(P+Q)-\widehat h(P)-\widehat h(Q)),\quad H_L=(\langle P_i,P_j\rangle)_{ij}.
\]
For a change-of-basis integer matrix A with determinant d, `H_L=A^T H_G A`, hence `det H_L=d^2 det H_G`. In rank one `\widehat h(2Q)=4\widehat h(Q)`.

For a full-rank subgroup L of G, p-saturation is equivalent to `G/L` having no element of order p, or `pG\cap L=pL`. To test it, inspect nonzero classes in `L/pL`; the projective coefficient classes number `(p^r-1)/(p-1)`. Torsion is treated separately in an actual elliptic-curve computation. Good-reduction maps to finite groups supply necessary congruence conditions for rational divisibility.

A full certificate is: proven rank r; explicit independent points; full torsion; a theorem-backed finite bound for possible prime divisors of `[G:L]`; and p-saturation checks for every prime up to that bound. Numerical approximations to heights need rigorous error control if used to prove inequalities.

##### Exercises with answers

1. Why does knowing the rank equal one not prove that a discovered non-torsion P is a generator? **Answer:** `P=mQ` may hold for an integer m greater than one.
2. A lattice change has determinant three. What happens to its height regulator? **Answer:** it is multiplied by nine.
3. Why must rank-two p-saturation test combinations of points? **Answer:** `P_1+P_2` may be divisible by p even if neither summand is.
4. What does verifying p-saturation for every prime up to 31 prove without an index bound? **Answer:** only that the remaining index, if nontrivial, has no prime divisor at most 31.

##### Reading and source notes

- [Sage reference: Saturation of Mordell–Weil groups](https://doc-gitlab.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/elliptic_curves/saturation.html), finite-field sieves, height bounds, and full saturation.
- [Magma Handbook: Mordell–Weil Groups and Descent Methods](https://docs.magma-maths.org/v2.30-1/ArithmeticGeometry/EllipticCurvesOverQAndNumberFields/mordell-weil.html), distinction between rank proofs and full generators.
- [J. S. Milne, Arithmetic Duality Theorems](https://www.jmilne.org/math/Books/ADTnot.pdf), cohomological background for descent and arithmetic local-global arguments.

### Cassels-Tate Pairings: How an Obstruction Sharpens a Rank Bound

**Track:** Abstract Algebra. **Background:** elliptic curves, Mordell-Weil groups, Selmer groups, local fields, and descent. **Central question:** when a Selmer computation gives too many possible rational points, how can a pairing detect the excess?

#### Mathematical companion (not spoken)

Let `E/K` be an elliptic curve and `p` a prime. The Kummer sequence supplies
\[
0\longrightarrow E(K)/pE(K)\longrightarrow \operatorname{Sel}^{(p)}(E/K)
\longrightarrow \Sha(E/K)[p]\longrightarrow 0.
\]
If `t=dim_Fp E(K)[p]`, then `dim_Fp E(K)/pE(K)=rank E(K)+t`. Thus `rank E(K)<=dim Sel_p-t`.

For odd p, in the conventional Cassels pairing on `Sel_p`, the radical is `im(Sel_{p^2}->Sel_p)` in the hypotheses of the descent pairing theorem (see Fisher-Newton). As `E(K)/pE(K)` lies inside that image, `rank E(K)<=dim rad-t`. The canonical Cassels-Tate pairing on Sha and the induced pairing on Selmer groups are related but have different domains. Do not assert perfection on the full Sha without addressing its maximal divisible subgroup or assuming finiteness.

For p=3, let
\[
B=\begin{pmatrix}0&1&0&0\\-1&0&0&0\\0&0&0&0\\0&0&0&0\end{pmatrix}
\quad\text{over }\mathbf F_3.
\]
Then `rank(B)=2`, `dim ker(B)=2`; if `E(K)[3]=0` and this is the actual descent pairing, the three-Selmer dimension-four bound improves to `rank E(K)<=2`. A lower bound of two from independent rational points establishes equality, **not** saturation of those points.

##### Exercises with answers

1. If `dim Sel_5=5` and `dim E(K)[5]=1`, what is the initial rank bound? **Answer:** at most four.
2. If the corresponding Selmer pairing has radical dimension three, what is the refined rank bound? **Answer:** at most two, assuming the standard radical theorem applies.
3. Does a zero Cassels pairing imply its arguments come from rational points? **Answer:** no; higher-Selmer images and divisible obstructions can lie in the radical.
4. Why can an alternating pairing improve a rank bound by an even number for odd p? **Answer:** the skew-symmetric pairing matrix has even rank.

##### Reading and source notes

- [Fisher and Newton, Computing the Cassels-Tate Pairing on the 3-Selmer Group](https://www.dpmms.cam.ac.uk/~taf1000/papers/ctp3.pdf), explicit pairing construction and its use in improved rank bounds.
- [J. S. Milne, Arithmetic Duality Theorems](https://www.jmilne.org/math/Books/ADTnot.pdf), global duality and the pairing on Tate-Shafarevich groups.
- [Magma Handbook, Mordell-Weil groups and descent](https://docs.magma-maths.org/v2.30-1/ArithmeticGeometry/EllipticCurvesOverQAndNumberFields/mordell-weil.html), distinction between rank bounds, generators, and saturation.

### Effective Chabauty-Coleman Bounds on Rational Points

**Track:** Abstract Algebra. **Background:** algebraic curves, Jacobians, Mordell–Weil groups, reduction modulo primes, and p-adic analysis. **Central question:** when can one certify that a search has found every rational point on a curve?

#### Mathematical companion (not spoken)

Let `C/Q` be smooth, projective, genus `g>=2`, with rational base point `b`, Jacobian `J`, and rank `r=rank J(Q)<g`. The Abel–Jacobi map `i_b:C -> J`, `P |-> [P-b]`, makes Coleman integrals of annihilating holomorphic differentials vanish on `C(Q)` after normalization. For a prime of good reduction `p>2g`, Coleman's bound is
\[
\#C(\mathbb Q)\leq \#C(\mathbb F_p)+2g-2.
\]
The rank inequality and good reduction are **hypotheses**, not consequences of the point count. An explicit effective result also requires certified group information and disk-by-disk root isolation, possibly with a Mordell–Weil sieve.

Worked count: `C:y^2=x^5+x+1` has `g=2`. Modulo `5`, `f'(x)=5x^4+1=1`, hence squarefree. For `x=0,1,2,3,4`, values `f(x) mod 5` are `(1,3,0,2,4)`. These contribute `(2,0,1,0,2)` affine points, plus one at infinity: `#C(F_5)=6`. **Only if** `rank J(Q)<2`, the bound would be `#C(Q)<=8`. No claim about the actual rank or exhaustive rational-point set is made here.

##### Exercises with answers

1. Why does one rational point not determine the residue disk above its reduction? **Answer:** infinitely many p-adic points generally reduce to that finite-field point.
2. In genus three, what rank condition is required for classical Chabauty? **Answer:** rank at most two.
3. If `#C(F_p)=10`, `g=3`, and all hypotheses hold, what is Coleman's upper bound? **Answer:** fourteen.
4. Why is a bound of eight and a list of five points not a complete census? **Answer:** the bound allows up to three additional rational points.

##### Reading and source notes

- [Coleman–Chabauty bounds and rank hypotheses](https://doi.org/10.1016/S0764-4442(00)80041-5), discussion of the rank condition and bounds.
- [Chabauty and Beyond: Explicit p-adic Methods for Rational Points](https://doi.org/10.1137/25M1805011), detailed modern account of computations, sieves, and certified bounds.
