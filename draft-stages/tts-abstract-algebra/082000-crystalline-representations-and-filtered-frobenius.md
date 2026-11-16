# 082000 — Crystalline Representations and Filtered Frobenius Modules

**Track:** Abstract Algebra. **Background:** p-adic fields, Hodge–Tate weights, linear algebra over valued fields. **Central question:** when can a complicated Galois action be reconstructed from a finite-dimensional filtered space and Frobenius?

<!-- BEGIN SPOKEN LECTURE -->

# More than a list of weights

A Hodge–Tate weight is a useful measurement of a p-adic Galois representation, but it does not determine the representation. Two objects can have identical weight lists and different arithmetic behavior. The next step in p-adic Hodge theory seeks a stronger form of compression: replace an infinite Galois action with a finite-dimensional space that carries both a filtration and a Frobenius operator.

Crystalline representations permit precisely this move. The adjective does not mean that the representation is made of literal crystals. It comes from crystalline cohomology, a cohomology theory in characteristic p that records infinitesimal thickening data. Comparison with that cohomology explains why Frobenius, the operation of raising to the p-th power in characteristic p, becomes central in the description of arithmetic representations.

A period ring, called B crystalline, is built to carry both the Galois action and Frobenius. Take the tensor product of this ring with the representation, and then take Galois invariants. The resulting space is called D crystalline of the representation.

The representation is crystalline when the invariant space has the expected dimension. This dimension condition matters. If the period ring fails to produce enough invariants, the proposed linear-algebra model has lost information.

# The rank-one experiment

Consider the trivial one-dimensional representation. Its crystalline invariant is one-dimensional. Frobenius acts as the identity on a suitable basis, and the filtration is concentrated at weight zero. This is the baseline.

Now take the cyclotomic Tate twist. A distinguished period, traditionally called t, transforms under Galois by the cyclotomic character. If e is a basis of the Tate twist, then t inverse times e is invariant. Frobenius sends t to p times t, so it sends that invariant basis vector to one over p times itself.

Notice the two independent measurements. The filtration says that the Tate twist has Hodge–Tate weight negative one, in our convention. The Frobenius action carries a p-adic slope of negative one. Their numerical agreement is an example of the compatibility condition called weak admissibility.

There is an easy sign trap here. A power of p greater than one has positive valuation, while the inverse of p has negative valuation. Likewise, the weight of the Tate twist depends on the chosen Hodge–Tate sign convention. Mixing conventions makes a valid comparison look false. We keep the convention in which the cyclotomic twist has weight negative one, and with that choice both quantities are negative one in this example.

# Comparing Hodge and Newton numbers

A filtered Frobenius module has two kinds of numerical data. The filtration determines a Hodge number by summing the filtration degrees with their multiplicities. The Frobenius determinant determines a Newton number through its valuation.

Weak admissibility requires those total numbers to agree. It also requires an inequality for every Frobenius-stable subobject: the Hodge number of that subobject must not exceed its Newton number, under the conventions we are using.

The subobject condition is essential. A two-dimensional object can have the right total number by cancellation while hiding an impossible one-dimensional subobject. Matching determinants is therefore necessary but insufficient.

In suitable local-field settings, the filtered Frobenius modules that satisfy weak admissibility are precisely those arising from crystalline representations. That is an equivalence theorem, not merely a recipe to attach a representation to an arbitrary filtration. One must specify the base field and the semilinearity of Frobenius, and use the corresponding admissibility theorem.

# An explicit failed candidate

Suppose we have a two-dimensional space with Frobenius acting diagonally with eigenvalues one and p. Its Newton slopes are zero and one. Give the space a filtration whose Hodge weights are also zero and one, so the total numbers agree.

If the Frobenius eigenline of slope zero is assigned the Hodge weight one, that line violates the subobject inequality: its Hodge number is one, but its Newton number is zero. The total determinant passed the test; the invariant line failed it. This filtered module is not weakly admissible.

The example shows why geometry must pay attention not only to totals but to alignment. The eigenlines and filtration must fit together. Rearranging the same two weights can alter whether a filtered Frobenius module corresponds to a crystalline representation.

# Where the comparison stops

Crystalline representations capture important forms of good reduction, but they are not a synonym for all geometric p-adic representations. Semistable representations can require a monodromy operator in addition to Frobenius and filtration. General de Rham representations form a larger class still. An object may have well-defined Hodge–Tate weights without being crystalline.

The gain from crystalline theory is that an infinite symmetry group becomes a finite-dimensional linear-algebra problem with sharply stated constraints. The rank-one Tate twist displays the dictionary. The two-dimensional failed candidate shows why a dictionary needs syntax, not just matched vocabulary. Filtration and Frobenius must agree on every stable piece, not only on the object as a whole.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For `K=Q_p`, define `D_{cris}(V)=(B_{cris}\otimes_{Q_p}V)^{G_K}`. If `dim_{Q_p}V=n`, then `dim_{Q_p}D_{cris}(V)\le n`; equality characterizes crystalline representations in this setting. The filtered `\varphi`-module has `\varphi` semilinear over the maximal unramified subfield in the general case; here for `Q_p` it is linear.

For `V=Q_p(1)` with generator `e` and Fontaine period `t`, `g(t)=\chi_p(g)t`, `\varphi(t)=pt`. The invariant basis `b=t^{-1}\otimes e` satisfies `\varphi(b)=p^{-1}b`, `\mathrm{Fil}^{-1}D_{dR}=D`, `\mathrm{Fil}^{0}D_{dR}=0`. With `v_p(p)=1`, both `t_N=v_p(\det\varphi)` and `t_H=\sum_i i\dim \mathrm{gr}^i` equal `-1`.

For a filtered `\varphi`-module `D`, weak admissibility demands `t_H(D)=t_N(D)` and `t_H(D')\le t_N(D')` for every `\varphi`-stable subobject `D'` with induced filtration. Example: `D=Q_p e_1\oplus Q_p e_2`, `\varphi(e_1)=e_1`, `\varphi(e_2)=pe_2`; filtration `\mathrm{Fil}^1 D=Q_p e_1`, `\mathrm{Fil}^0D=D`, `\mathrm{Fil}^2=0`. Then totals equal `1`, but `D'=Q_p e_1` has `t_H(D')=1>0=t_N(D')`: not weakly admissible.

### Exercises with answers

1. Compute `t_N` for the matrix `diag(1,p^2)`. **Answer:** `2`.
2. Explain why the two-dimensional candidate fails weak admissibility although totals agree. **Answer:** the slope-zero eigenline inherits filtration weight one, violating `t_H\le t_N`.
3. What extra operator appears in the semistable comparison setting? **Answer:** monodromy `N`, with compatibility to Frobenius.
4. Is an arbitrary Hodge–Tate representation automatically crystalline? **Answer:** No.

### Reading and source notes

- [Laurent Berger, An Introduction to the Theory of p-adic Representations](https://arxiv.org/abs/math/0210184), crystalline and semistable period-module descriptions.
- [Colmez and Fontaine, Construction des représentations p-adiques semi-stables](https://doi.org/10.1007/s002220000042), equivalence between admissible filtered modules and semistable representations (consult theorem and base-field hypotheses).
