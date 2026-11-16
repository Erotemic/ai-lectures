# 069000 - Cassels-Tate Pairings: How an Obstruction Sharpens a Rank Bound

**Track:** Abstract Algebra. **Background:** elliptic curves, Mordell-Weil groups, Selmer groups, local fields, and descent. **Central question:** when a Selmer computation gives too many possible rational points, how can a pairing detect the excess?

<!-- BEGIN SPOKEN LECTURE -->

# A rank bound that is too generous

An elliptic curve may have rational points that we can write down explicitly, and still resist our attempts to determine its complete group of rational points. The group is finitely generated, so in principle it consists of finitely many free generators together with torsion. But the theorem that tells us this does not hand us the generators. Descent is one of the main ways to make progress.

Here is the difficulty. A descent calculation can list classes that pass every local test. Each class can be represented over every completion of the number field. Yet being possible over every completion does not guarantee coming from a rational point. The missing distinction is precisely where the Tate-Shafarevich group enters. And the Cassels-Tate pairing can sometimes prove that some of those locally possible classes cannot represent new free generators.

We will keep two claims separate throughout. A Selmer computation supplies an upper bound on rank. A Mordell-Weil search supplies a lower bound by constructing independent rational points. A pairing can improve the upper bound, but it does not automatically find the missing rational points, and it does not automatically resolve every obstruction.

# The exact sequence behind the mystery

Fix an elliptic curve over a number field and a prime p. Consider multiplication by p on the elliptic curve. On rational points, this map takes a point to its p-fold sum. Its cokernel measures which points cannot be obtained by multiplying another rational point by p. After modding out by p, the free rank and rational p-torsion appear as dimensions of a finite vector space over the field with p elements.

Now do the analogous construction not only over the number field, but over every local completion. The p-Selmer group consists of global cohomology classes satisfying appropriate local conditions. It is finite and computable in many explicit cases. Rational points modulo p inject into this group, but need not fill it. The quotient is the p-torsion in the Tate-Shafarevich group, traditionally abbreviated Sha.

Sha measures torsors that look soluble locally but have no rational point. This is why a Selmer class can survive every congruence and local test and yet fail to correspond to a rational point. The two obstructions are related, but they are not the same problem: local solubility belongs in the Selmer definition; global solubility belongs in the exact sequence connecting Selmer, rational points, and Sha.

Suppose, to make the count transparent, that the curve has no rational p-torsion. If the p-Selmer group has dimension four, the rank is at most four. That bound could be exact, or there could be nonzero Sha contributions. To make it smaller we need more information than the dimension alone.

# Pairing the surviving classes

The Cassels-Tate pairing assigns a value in the rationals modulo the integers to pairs of obstruction classes. Its construction uses global duality and local invariants. Very roughly, one lifts a class through a cohomological sequence, compares it with local choices, and sums local pairings. The global reciprocity law ensures the resulting answer is independent of choices under the theorem's hypotheses.

For an elliptic curve, the pairing is alternating in the usual formulation. An element pairs trivially with itself. When restricted to appropriate p-primary obstruction data, its finite matrix looks like a skew-symmetric bilinear form. Such a matrix has even rank over a field of odd characteristic. This parity becomes arithmetic information.

We should be careful with the domain. The canonical Cassels-Tate pairing lives on Sha, and its degeneracy properties require qualifications involving divisible subgroups. Computational descent methods also construct a related pairing directly on p-Selmer groups. In common p-descent settings, the radical of that Selmer pairing is the image of the p-squared Selmer group. These formulations fit together, but they should not be collapsed into the assertion that the first Selmer group is itself Sha.

# A four-dimensional calculation

Imagine that a three-Selmer computation yields four independent classes, represented by basis vectors one through four. Suppose the computed pairing has only one nontrivial block: the pairing of basis vector one with basis vector two is one modulo three, and reversing their order gives negative one modulo three. Every pairing involving the last two vectors vanishes.

The matrix then has rank two. Its radical is the two-dimensional span of vectors three and four. So not all four Selmer directions survive into the next descent stage. Under the standard Cassels pairing theorem, the image of the nine-Selmer group has dimension two, and the image of rational points modulo three must lie inside that image.

If the curve has no rational three-torsion, the rank is therefore at most two, instead of at most four. We have improved the bound by two without discovering a single new rational point. If, separately, we know two independent rational points, then rank two is proved. If we know only one, the pairing has not found a second point and the exact rank remains unresolved.

This example is an abstract pairing matrix, not a claim about a particular elliptic curve. Constructing the matrix for an actual curve requires arithmetic geometry: covering curves, local points, and precise local invariant calculations. The linear algebra at the end is simple; making its entries rigorous is the hard part.

# Why the pairing can have a radical

A student of elementary linear algebra might expect a perfect alternating pairing, with zero radical. But the arithmetic pairing can have a radical because divisible classes can pair trivially with everything. On the quotient of Sha by its maximal divisible subgroup, the relevant Cassels-Tate pairing is nondegenerate in an appropriate sense. To conclude a finite, perfect pairing on all of Sha, one usually needs an additional finiteness assumption.

This matters when presenting a rank certificate. A nonzero pairing value is decisive: it witnesses a genuine obstruction. Zero pairings are not always decisive. The radical may contain rational-point classes, higher-descent classes, or elements hidden by the chosen level of descent. One cannot infer that every class in the radical comes from a rational point.

Likewise, a computation of a pairing on a finite subgroup is not automatically a computation of the entire Tate-Shafarevich group. It can prove that particular obstruction classes are nontrivial, and it can reduce a bound, without settling whether Sha is finite or whether it contains further elements of higher prime-power order.

# A certificate has several layers

How should a complete rank proof be organized? Start with explicit rational points and prove that they are independent, perhaps with a height pairing. That establishes a lower bound. Next compute a Selmer group with rigorous local conditions. That establishes an initial upper bound. Then evaluate a Cassels-type pairing, if available, to shrink the allowable space of rational-point classes. Finally compare the resulting upper bound with the known lower bound.

When the bounds meet, the rank is certified. Yet there remains a separate question about generators: the known independent points might span a subgroup of finite index. A saturation computation, together with torsion determination and an index bound, addresses that problem. This is why a certified rank and a certified full Mordell-Weil group are different outputs.

The deeper picture is that local arithmetic creates a finite space of possibilities, global duality pairs those possibilities, and linear algebra rules out some combinations. A rank bound ceases to be a raw count of locally soluble coverings. It becomes a count corrected by a measurable obstruction to global solubility.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

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

### Exercises with answers

1. If `dim Sel_5=5` and `dim E(K)[5]=1`, what is the initial rank bound? **Answer:** at most four.
2. If the corresponding Selmer pairing has radical dimension three, what is the refined rank bound? **Answer:** at most two, assuming the standard radical theorem applies.
3. Does a zero Cassels pairing imply its arguments come from rational points? **Answer:** no; higher-Selmer images and divisible obstructions can lie in the radical.
4. Why can an alternating pairing improve a rank bound by an even number for odd p? **Answer:** the skew-symmetric pairing matrix has even rank.

### Reading and source notes

- [Fisher and Newton, Computing the Cassels-Tate Pairing on the 3-Selmer Group](https://www.dpmms.cam.ac.uk/~taf1000/papers/ctp3.pdf), explicit pairing construction and its use in improved rank bounds.
- [J. S. Milne, Arithmetic Duality Theorems](https://www.jmilne.org/math/Books/ADTnot.pdf), global duality and the pairing on Tate-Shafarevich groups.
- [Magma Handbook, Mordell-Weil groups and descent](https://docs.magma-maths.org/v2.30-1/ArithmeticGeometry/EllipticCurvesOverQAndNumberFields/mordell-weil.html), distinction between rank bounds, generators, and saturation.
