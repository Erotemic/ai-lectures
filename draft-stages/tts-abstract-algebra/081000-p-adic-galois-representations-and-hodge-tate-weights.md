# 081000 — p-Adic Galois Representations and Hodge–Tate Weights

**Track:** Abstract Algebra. **Background:** local fields, Galois groups, finite-dimensional representations, and valuations. **Central question:** how can a Galois action on a p-adic vector space retain geometric information about differential forms?

<!-- BEGIN SPOKEN LECTURE -->

# A representation whose coefficients remember arithmetic

A Galois representation is a rule for letting field symmetries act on a vector space. Over the complex numbers, familiar representation theory asks for characters, invariant subspaces, and decomposition into simple pieces. Over the p-adic numbers a new possibility appears: the field of coefficients carries its own arithmetic topology. Continuity of the representation matters, and the symmetry group of a local number field is enormous.

Let K be a finite extension of the p-adic rational field. Its absolute Galois group consists of all field automorphisms of an algebraic closure fixing K. A p-adic representation is a finite-dimensional vector space over the p-adic rationals, equipped with a continuous action of that group. The simplest representation is trivial: every field automorphism acts as the identity. The next example is already rich enough to reveal Hodge theory.

Take all compatible p-power roots of unity. A Galois automorphism permutes these roots, and it must do so by raising them to a unit exponent. Recording those exponents gives the cyclotomic character. The one-dimensional representation on which Galois acts through this character is called the first Tate twist.

That character is not merely a formal decoration. It measures the action on a compatible system of roots, and twists of geometric cohomology by this character change the filtration weights that p-adic Hodge theory detects.

# Ordinary eigenvalues are not enough

An infinite profinite group need not admit a simple decomposition into ordinary eigenspaces over the original coefficient field. Even a one-dimensional character can take values in infinitely many p-adic units. To uncover structure, p-adic Hodge theory enlarges the scalars to a much bigger complete field, usually denoted C sub p. This is the completion of an algebraic closure of K.

Over that bigger field, certain representations split into graded pieces made from integer powers of the cyclotomic character. These graded pieces are described by Hodge–Tate weights. The convention is important: in the convention used here the cyclotomic Tate twist has weight negative one. The trivial representation has weight zero. Their tensor product has weight negative one, because twists add weights.

A representation is called Hodge–Tate when the appropriate scalar extension decomposes into these weight pieces. This condition does not hold for every continuous p-adic representation. Nor should Hodge–Tate decomposability be confused with splitting the original representation into one-dimensional Galois characters. The decomposition takes place after a carefully chosen extension of scalars.

# Where the weights come from

Imagine a smooth proper geometric object over K. Its p-adic étale cohomology is a finite-dimensional p-adic vector space equipped with Galois action. The same geometric object has algebraic differential forms and a de Rham cohomology equipped with a descending filtration. On good geometric examples, a comparison theorem relates those otherwise different objects.

The Hodge–Tate decomposition reads the graded pieces of the de Rham filtration from the Galois representation after extending scalars to C sub p. A differential one-form contributes in a different weight from an ordinary function. Thus a representation that initially looks like a collection of matrices carries information about the degrees of differential forms on the geometric object that produced it.

One can understand the simplest case on the projective line. Its first cohomology vanishes, but its second étale cohomology is one-dimensional and is a negative Tate twist. With our convention the inverse Tate twist has weight positive one. The important point is not a memorized sign; it is that projective geometry supplies a nontrivial character even when the underlying cohomology group is one-dimensional.

# The arithmetic information a weight does not provide

A list of Hodge–Tate weights is informative but incomplete. Two representations may have the same weights and nevertheless differ in ramification, extension classes, or Frobenius data. A weight records part of a comparison between Galois action and differential geometry, not a complete classification of all continuous actions.

This limitation motivates richer categories: de Rham representations, semistable representations, and crystalline representations. Their relationships require additional period rings, in which Galois invariants become linear algebra together with filtrations, Frobenius maps, and sometimes monodromy operators.

The hierarchy also helps guard against a tempting shortcut. Every p-adic representation is continuous by definition, but continuity alone does not grant it a geometric origin. Saying that a representation comes from cohomology is a substantive arithmetic assertion.

# A new language between number theory and geometry

The remarkable move is to change which object we look at. Instead of staring at infinitely many Galois automorphisms one by one, we ask whether an extended representation admits a finite collection of integer weights. In geometric cases, those integers recover how differential forms are arranged in a filtered cohomology group. They allow arithmetic symmetries and algebraic geometry to speak through a common vocabulary.

The trivial representation and the cyclotomic character already show the mechanism. One has weight zero; the other carries a twist. Tensor powers add those weights. Geometric cohomology organizes them into graded pieces. The remaining task, which is deeper than this first comparison, is to retain not only weights but the additional structure needed to distinguish representations with the same weight data.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

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

### Exercises with answers

1. What weight has `Q_p(1)^{\otimes 3}` under our sign convention? **Answer:** `-3`.
2. If `V` has weights `0` and `2`, what weights does `V(1)` have? **Answer:** `-1` and `1`.
3. Must two representations with equal Hodge–Tate weights be isomorphic? **Answer:** No; weights do not classify extensions or Frobenius/ramification data.
4. Is every continuous p-adic representation Hodge–Tate? **Answer:** No; it is a restrictive condition.

### Reading and source notes

- [Laurent Berger, An Introduction to the Theory of p-adic Representations](https://arxiv.org/abs/math/0210184), period-ring and representation-theoretic foundations.
- [Bhatt, Morrow, and Scholze, Integral p-adic Hodge Theory](https://arxiv.org/abs/1602.03148), modern geometric comparison in a substantially broader setting.
