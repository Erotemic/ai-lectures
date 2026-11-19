# p-Adic refinements and representation-theoretic information

<!-- BEGIN SPOKEN LECTURE -->

# p-Adic refinements and representation-theoretic information

## Quadratic Chabauty and p-Adic Height Pairings

Suppose we have a smooth projective curve of genus two, and we want to list all its rational points. Its Jacobian is a two-dimensional abelian variety. If the rank of the group of rational points of the Jacobian is one, classical Chabauty has a useful dimension advantage: one can find a differential whose p-adic integral vanishes on the rational group. Zeros of that integral constrain rational points on the curve.

Now suppose the rank is two. The elementary dimension count has disappeared. There need not be a nonzero holomorphic differential annihilating the rational group. This does not prove that the rational points cannot be determined. It tells us that linear p-adic integrals, by themselves, may no longer cut out a finite set.

Quadratic Chabauty replaces some of that missing linear information with a height pairing. The crucial new constraint is quadratic rather than linear in the group coordinates. The price is more arithmetic: the height depends on local data at several primes and on geometric information about the Jacobian. We must be careful not to call every quadratic-looking analytic expression a certified rational-point sieve.

## What a height pairing remembers

An ordinary height measures the arithmetic complexity of a rational point. A canonical height on an abelian variety behaves quadratically under multiplication: multiplying a point by an integer n multiplies its canonical height by n squared. Polarization produces a bilinear pairing.

There are p-adic analogues. Their values live in a p-adic field rather than the real numbers, so they are not distances or measures of numerical size in the usual sense. Nevertheless, their algebraic behavior carries useful information. If a subgroup has basis points P and Q, an appropriate p-adic height can be expressed on their integer combinations by a quadratic polynomial in the two coefficients. Its mixed term records the pairing between P and Q.

The same height can be assembled from local contributions. The contribution at the chosen prime p is accessible through p-adic integration, while contributions at other primes reflect reduction, intersection behavior, and arithmetic geometry. Rational points impose global compatibility among these local terms. A p-adic point selected at random does not generally satisfy that compatibility.

## A new kind of zero condition

Embed the curve into its Jacobian using a rational base point. For each rational point of the curve, the associated Jacobian point belongs to the Mordell–Weil group. Its p-adic height can be calculated in two different ways: from group coordinates through the height pairing, and from local geometry through suitable p-adic functions on the curve.

Subtracting these descriptions produces locally analytic constraints. In explicit quadratic Chabauty, the non-p local height contributions often range over a finite computable set. Instead of asking for the zeros of one Coleman integral, one asks which p-adic points satisfy one of several equations involving p-adic heights and iterated integrals.

It is essential that the finite set of allowed local contributions be justified. If we simply choose a handful of constants that fit the rational points already found, we have constructed a pattern, not a proof. And finding p-adic solutions of the height equations does not immediately prove those solutions rational. The method supplies a finite candidate set containing rational points, and additional arithmetic information may be needed to eliminate the other candidates.

## The refined rank condition

There is an especially illuminating version of the dimension count. Let g be the genus of the curve, r the Mordell–Weil rank of its Jacobian, and rho the rank of the Néron–Severi group of that Jacobian over the rationals. In the setting of the Balakrishnan–Dogra quadratic Chabauty theorem, the inequality is that r is strictly smaller than g plus rho minus one.

Consider g equal to two, rho equal to two, and r equal to two. Classical Chabauty fails its familiar inequality r less than g: two is not smaller than two. But quadratic Chabauty meets its inequality: two is smaller than three. The extra divisor class supplies an additional source of arithmetic structure.

This numerical check is an illustration of the hypothesis, not a claim that every genus-two Jacobian has Néron–Severi rank two. For many Jacobians, the Néron–Severi rank is one, and the inequality gives no improvement over classical Chabauty. Even when it holds, further geometric and computational assumptions enter an effective implementation.

## A small algebraic model of the pairing

Take a rank-two free abelian group with basis P and Q. Imagine a symmetric bilinear p-adic height pairing with entries a, b, and c. The height of mP plus nQ is then a times m squared, plus twice b times mn, plus c times n squared. The mixed term matters: a quadratic constraint cannot be recovered by separately checking only the multiples of P and the multiples of Q.

If P and Q are replaced by another integral basis, the matrix of this pairing changes by congruence, but the quadratic value attached to a group element does not change. That is why the method is about arithmetic objects, not one preferred coordinate table. For an actual Jacobian, the pairing matrix and the local height functions must be computed, with normalization choices recorded consistently.

A p-adic quadratic form need not be positive. Calling its diagonal entries “energies” would be misleading. The crucial property is compatibility of its algebraic variation with the group law.

## From candidate points to a complete list

An effective calculation therefore has several layers. Certify the curve and its reduction data. Obtain a sufficiently controlled Mordell–Weil subgroup and rank information. Compute the relevant p-adic integrals and height pairings. Bound local contributions away from p. Isolate all p-adic solutions of the resulting finite family of equations with justified precision. Finally, test rational candidates and use sieves or additional constraints to exclude solutions that do not come from rational points.

At each stage, “we found no others” must become a verifiable statement about the entire remaining region. Root isolation is different from evaluating a function at a grid of p-adic approximations. A finite candidate set is different from a complete set of rational points. And an upper bound on the rank is different from a verified basis of the rational group.

Quadratic Chabauty teaches a general mathematical lesson. When a linear obstruction is too weak, a nonlinear arithmetic invariant may restore finiteness. But the strength of the conclusion depends on all of its ingredients: geometric classes, global heights, local analytic formulas, and proofs that no possible residue disk has been silently omitted.

## p-Adic Galois Representations and Hodge-Tate Weights

A Galois representation is a rule for letting field symmetries act on a vector space. Over the complex numbers, familiar representation theory asks for characters, invariant subspaces, and decomposition into simple pieces. Over the p-adic numbers a new possibility appears: the field of coefficients carries its own arithmetic topology. Continuity of the representation matters, and the symmetry group of a local number field is enormous.

Let K be a finite extension of the p-adic rational field. Its absolute Galois group consists of all field automorphisms of an algebraic closure fixing K. A p-adic representation is a finite-dimensional vector space over the p-adic rationals, equipped with a continuous action of that group. The simplest representation is trivial: every field automorphism acts as the identity. The next example is already rich enough to reveal Hodge theory.

Take all compatible p-power roots of unity. A Galois automorphism permutes these roots, and it must do so by raising them to a unit exponent. Recording those exponents gives the cyclotomic character. The one-dimensional representation on which Galois acts through this character is called the first Tate twist.

That character is not merely a formal decoration. It measures the action on a compatible system of roots, and twists of geometric cohomology by this character change the filtration weights that p-adic Hodge theory detects.

## Ordinary eigenvalues are not enough

An infinite profinite group need not admit a simple decomposition into ordinary eigenspaces over the original coefficient field. Even a one-dimensional character can take values in infinitely many p-adic units. To uncover structure, p-adic Hodge theory enlarges the scalars to a much bigger complete field, usually denoted C sub p. This is the completion of an algebraic closure of K.

Over that bigger field, certain representations split into graded pieces made from integer powers of the cyclotomic character. These graded pieces are described by Hodge–Tate weights. The convention is important: in the convention used here the cyclotomic Tate twist has weight negative one. The trivial representation has weight zero. Their tensor product has weight negative one, because twists add weights.

A representation is called Hodge–Tate when the appropriate scalar extension decomposes into these weight pieces. This condition does not hold for every continuous p-adic representation. Nor should Hodge–Tate decomposability be confused with splitting the original representation into one-dimensional Galois characters. The decomposition takes place after a carefully chosen extension of scalars.

## Where the weights come from

Imagine a smooth proper geometric object over K. Its p-adic étale cohomology is a finite-dimensional p-adic vector space equipped with Galois action. The same geometric object has algebraic differential forms and a de Rham cohomology equipped with a descending filtration. On good geometric examples, a comparison theorem relates those otherwise different objects.

The Hodge–Tate decomposition reads the graded pieces of the de Rham filtration from the Galois representation after extending scalars to C sub p. A differential one-form contributes in a different weight from an ordinary function. Thus a representation that initially looks like a collection of matrices carries information about the degrees of differential forms on the geometric object that produced it.

One can understand the simplest case on the projective line. Its first cohomology vanishes, but its second étale cohomology is one-dimensional and is a negative Tate twist. With our convention the inverse Tate twist has weight positive one. The important point is not a memorized sign; it is that projective geometry supplies a nontrivial character even when the underlying cohomology group is one-dimensional.

## The arithmetic information a weight does not provide

A list of Hodge–Tate weights is informative but incomplete. Two representations may have the same weights and nevertheless differ in ramification, extension classes, or Frobenius data. A weight records part of a comparison between Galois action and differential geometry, not a complete classification of all continuous actions.

This limitation motivates richer categories: de Rham representations, semistable representations, and crystalline representations. Their relationships require additional period rings, in which Galois invariants become linear algebra together with filtrations, Frobenius maps, and sometimes monodromy operators.

The hierarchy also helps guard against a tempting shortcut. Every p-adic representation is continuous by definition, but continuity alone does not grant it a geometric origin. Saying that a representation comes from cohomology is a substantive arithmetic assertion.

## A new language between number theory and geometry

The remarkable move is to change which object we look at. Instead of staring at infinitely many Galois automorphisms one by one, we ask whether an extended representation admits a finite collection of integer weights. In geometric cases, those integers recover how differential forms are arranged in a filtered cohomology group. They allow arithmetic symmetries and algebraic geometry to speak through a common vocabulary.

The trivial representation and the cyclotomic character already show the mechanism. One has weight zero; the other carries a twist. Tensor powers add those weights. Geometric cohomology organizes them into graded pieces. The remaining task, which is deeper than this first comparison, is to retain not only weights but the additional structure needed to distinguish representations with the same weight data.

## Crystalline Representations and Filtered Frobenius Modules

A Hodge–Tate weight is a useful measurement of a p-adic Galois representation, but it does not determine the representation. Two objects can have identical weight lists and different arithmetic behavior. The next step in p-adic Hodge theory seeks a stronger form of compression: replace an infinite Galois action with a finite-dimensional space that carries both a filtration and a Frobenius operator.

Crystalline representations permit precisely this move. The adjective does not mean that the representation is made of literal crystals. It comes from crystalline cohomology, a cohomology theory in characteristic p that records infinitesimal thickening data. Comparison with that cohomology explains why Frobenius, the operation of raising to the p-th power in characteristic p, becomes central in the description of arithmetic representations.

A period ring, called B crystalline, is built to carry both the Galois action and Frobenius. Take the tensor product of this ring with the representation, and then take Galois invariants. The resulting space is called D crystalline of the representation.

The representation is crystalline when the invariant space has the expected dimension. This dimension condition matters. If the period ring fails to produce enough invariants, the proposed linear-algebra model has lost information.

## The rank-one experiment

Consider the trivial one-dimensional representation. Its crystalline invariant is one-dimensional. Frobenius acts as the identity on a suitable basis, and the filtration is concentrated at weight zero. This is the baseline.

Now take the cyclotomic Tate twist. A distinguished period, traditionally called t, transforms under Galois by the cyclotomic character. If e is a basis of the Tate twist, then t inverse times e is invariant. Frobenius sends t to p times t, so it sends that invariant basis vector to one over p times itself.

Notice the two independent measurements. The filtration says that the Tate twist has Hodge–Tate weight negative one, in our convention. The Frobenius action carries a p-adic slope of negative one. Their numerical agreement is an example of the compatibility condition called weak admissibility.

There is an easy sign trap here. A power of p greater than one has positive valuation, while the inverse of p has negative valuation. Likewise, the weight of the Tate twist depends on the chosen Hodge–Tate sign convention. Mixing conventions makes a valid comparison look false. We keep the convention in which the cyclotomic twist has weight negative one, and with that choice both quantities are negative one in this example.

## Comparing Hodge and Newton numbers

A filtered Frobenius module has two kinds of numerical data. The filtration determines a Hodge number by summing the filtration degrees with their multiplicities. The Frobenius determinant determines a Newton number through its valuation.

Weak admissibility requires those total numbers to agree. It also requires an inequality for every Frobenius-stable subobject: the Hodge number of that subobject must not exceed its Newton number, under the conventions we are using.

The subobject condition is essential. A two-dimensional object can have the right total number by cancellation while hiding an impossible one-dimensional subobject. Matching determinants is therefore necessary but insufficient.

In suitable local-field settings, the filtered Frobenius modules that satisfy weak admissibility are precisely those arising from crystalline representations. That is an equivalence theorem, not merely a recipe to attach a representation to an arbitrary filtration. One must specify the base field and the semilinearity of Frobenius, and use the corresponding admissibility theorem.

## An explicit failed candidate

Suppose we have a two-dimensional space with Frobenius acting diagonally with eigenvalues one and p. Its Newton slopes are zero and one. Give the space a filtration whose Hodge weights are also zero and one, so the total numbers agree.

If the Frobenius eigenline of slope zero is assigned the Hodge weight one, that line violates the subobject inequality: its Hodge number is one, but its Newton number is zero. The total determinant passed the test; the invariant line failed it. This filtered module is not weakly admissible.

The example shows why geometry must pay attention not only to totals but to alignment. The eigenlines and filtration must fit together. Rearranging the same two weights can alter whether a filtered Frobenius module corresponds to a crystalline representation.

## Where the comparison stops

Crystalline representations capture important forms of good reduction, but they are not a synonym for all geometric p-adic representations. Semistable representations can require a monodromy operator in addition to Frobenius and filtration. General de Rham representations form a larger class still. An object may have well-defined Hodge–Tate weights without being crystalline.

The gain from crystalline theory is that an infinite symmetry group becomes a finite-dimensional linear-algebra problem with sharply stated constraints. The rank-one Tate twist displays the dictionary. The two-dimensional failed candidate shows why a dictionary needs syntax, not just matched vocabulary. Filtration and Frobenius must agree on every stable piece, not only on the object as a whole.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Quadratic Chabauty and p-Adic Height Pairings

**Track:** Abstract Algebra. **Background:** Jacobians, Mordell–Weil rank, p-adic integration, height pairings, and classical Chabauty. **Central question:** how can a quadratic height constraint still isolate rational points when the Jacobian rank is too large for ordinary Chabauty?

#### Mathematical companion (not spoken)

Write `C/Q` for a smooth projective curve of genus `g>=2`, `J` for its Jacobian, `r=rank J(Q)`, and `rho=rank NS(J)`. The familiar Coleman dimension condition is `r<g`. An influential quadratic Chabauty finiteness criterion under the corresponding geometric hypotheses is
\[
r<g+\rho-1.
\]
For `(g,r,rho)=(2,2,2)`, `2<2+2-1=3` holds, while `r<g` does not. **Neither** condition alone identifies a rational point; a finite quadratic Chabauty locus may properly contain `C(Q)`.

A bilinear p-adic height pairing `h(.,.)` induces `q(mP+nQ)=m^2 h(P,P)+2mn h(P,Q)+n^2 h(Q,Q)` on a rank-two subgroup, subject to the chosen normalization. Global heights decompose into local contributions. In explicit implementations, possible contributions away from `p` must be calculated or bounded and p-adic analytic equations must be solved with certified error control. Such a pairing is not generally positive definite.

##### Exercises with answers

1. For `g=2`, `rho=1`, `r=2`, does the displayed quadratic criterion hold? **Answer:** No; `2<2` is false.
2. For `q(m,n)=3m^2+2mn+5n^2`, find `q(1,2)`. **Answer:** `3+4+20=27`.
3. Does a finite set of p-adic candidate points imply all are rational? **Answer:** No; a candidate locus only contains the rational points.
4. What additional arithmetic data are needed to convert a p-adic root count into a rational-point census? **Answer:** Verified Mordell–Weil information and a justification that every remaining p-adic candidate is either rational and checked or excluded.

##### Reading and source notes

- [Balakrishnan and Dogra, Quadratic Chabauty and rational points I: p-adic heights](https://arxiv.org/abs/1601.00388), original quadratic Chabauty setting and hypotheses.
- [Balakrishnan, Besser and Müller, Quadratic Chabauty: p-adic height pairings and integral points](https://arxiv.org/abs/1302.2944), explicit height computation and integral-point applications.
- [Chabauty and Beyond (ICM 2026)](https://epubs.siam.org/doi/10.1137/25M1805011), review of the rank condition and effective methods.

### p-Adic Galois Representations and Hodge-Tate Weights

**Track:** Abstract Algebra. **Background:** local fields, Galois groups, finite-dimensional representations, and valuations. **Central question:** how can a Galois action on a p-adic vector space retain geometric information about differential forms?

#### Mathematical companion (not spoken)

Let `K/Q_p` be finite, `G_K=Gal(\bar K/K)` and `V` a finite-dimensional continuous `Q_p`-representation. The cyclotomic character `\chi_p:G_K\to\mathbb Z_p^\times` is characterized by `g(\zeta_{p^n})=\zeta_{p^n}^{\chi_p(g)\bmod p^n}` for a compatible choice of roots. Define `Q_p(1)=Q_p e_1`, `g(e_1)=\chi_p(g)e_1`. We adopt the conventional Hodge–Tate weight `-1` for `Q_p(1)` and `+1` for `Q_p(-1)`. Some authors reverse signs; every quoted weight must state its convention.

For `K=Q_p` an admissible description of a Hodge–Tate representation is a `G_K`-equivariant `C_p`-linear decomposition
\[
C_p\otimes_{\mathbb Q_p}V\cong\bigoplus_{j\in\mathbb Z} C_p(-j)^{h_j},
\]
with only finitely many nonzero multiplicities; the notation here labels the weight `j` by `C_p(-j)`. The relationship to `\operatorname{gr}^j D_{\rm dR}` is convention-dependent. Do not assert the splitting for arbitrary `V`.

For a smooth proper `X/K`, the Hodge–Tate comparison takes a form such as
\[
H^n_{\acute et}(X_{\bar K},\mathbb Q_p)\otimes_{\mathbb Q_p}C_p
\cong \bigoplus_{i+j=n} H^i(X,\Omega^j_{X/K})\otimes_K C_p(-j)
\]
with compatibility, assumptions and index conventions as in the comparison theorem. For `X=\mathbb P^1`, `H^2_{et}(X_{\bar K},Q_p)\cong Q_p(-1)`; its weight is `+1`, consistent with `H^1(\mathbb P^1,\Omega^1)`.

##### Exercises with answers

1. What weight has `Q_p(1)^{\otimes 3}` under our sign convention? **Answer:** `-3`.
2. If `V` has weights `0` and `2`, what weights does `V(1)` have? **Answer:** `-1` and `1`.
3. Must two representations with equal Hodge–Tate weights be isomorphic? **Answer:** No; weights do not classify extensions or Frobenius/ramification data.
4. Is every continuous p-adic representation Hodge–Tate? **Answer:** No; it is a restrictive condition.

##### Reading and source notes

- [Laurent Berger, An Introduction to the Theory of p-adic Representations](https://arxiv.org/abs/math/0210184), period-ring and representation-theoretic foundations.
- [Bhatt, Morrow, and Scholze, Integral p-adic Hodge Theory](https://arxiv.org/abs/1602.03148), modern geometric comparison in a substantially broader setting.

### Crystalline Representations and Filtered Frobenius Modules

**Track:** Abstract Algebra. **Background:** p-adic fields, Hodge–Tate weights, linear algebra over valued fields. **Central question:** when can a complicated Galois action be reconstructed from a finite-dimensional filtered space and Frobenius?

#### Mathematical companion (not spoken)

For `K=Q_p`, define `D_{cris}(V)=(B_{cris}\otimes_{Q_p}V)^{G_K}`. If `dim_{Q_p}V=n`, then `dim_{Q_p}D_{cris}(V)\le n`; equality characterizes crystalline representations in this setting. The filtered `\varphi`-module has `\varphi` semilinear over the maximal unramified subfield in the general case; here for `Q_p` it is linear.

For `V=Q_p(1)` with generator `e` and Fontaine period `t`, `g(t)=\chi_p(g)t`, `\varphi(t)=pt`. The invariant basis `b=t^{-1}\otimes e` satisfies `\varphi(b)=p^{-1}b`, `\mathrm{Fil}^{-1}D_{dR}=D`, `\mathrm{Fil}^{0}D_{dR}=0`. With `v_p(p)=1`, both `t_N=v_p(\det\varphi)` and `t_H=\sum_i i\dim \mathrm{gr}^i` equal `-1`.

For a filtered `\varphi`-module `D`, weak admissibility demands `t_H(D)=t_N(D)` and `t_H(D')\le t_N(D')` for every `\varphi`-stable subobject `D'` with induced filtration. Example: `D=Q_p e_1\oplus Q_p e_2`, `\varphi(e_1)=e_1`, `\varphi(e_2)=pe_2`; filtration `\mathrm{Fil}^1 D=Q_p e_1`, `\mathrm{Fil}^0D=D`, `\mathrm{Fil}^2=0`. Then totals equal `1`, but `D'=Q_p e_1` has `t_H(D')=1>0=t_N(D')`: not weakly admissible.

##### Exercises with answers

1. Compute `t_N` for the matrix `diag(1,p^2)`. **Answer:** `2`.
2. Explain why the two-dimensional candidate fails weak admissibility although totals agree. **Answer:** the slope-zero eigenline inherits filtration weight one, violating `t_H\le t_N`.
3. What extra operator appears in the semistable comparison setting? **Answer:** monodromy `N`, with compatibility to Frobenius.
4. Is an arbitrary Hodge–Tate representation automatically crystalline? **Answer:** No.

##### Reading and source notes

- [Laurent Berger, An Introduction to the Theory of p-adic Representations](https://arxiv.org/abs/math/0210184), crystalline and semistable period-module descriptions.
- [Colmez and Fontaine, Construction des représentations p-adiques semi-stables](https://doi.org/10.1007/s002220000042), equivalence between admissible filtered modules and semistable representations (consult theorem and base-field hypotheses).
