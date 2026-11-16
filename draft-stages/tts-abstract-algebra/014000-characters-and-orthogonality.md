# 014000 — Characters: Traces, Orthogonality, and the Anatomy of a Representation

**Track:** Abstract Algebra. **Background:** finite-dimensional complex vector spaces, group representations, and Maschke's theorem. **Question:** how can a few complex numbers reveal the irreducible components of a family of matrices?

<!-- BEGIN SPOKEN LECTURE -->

# Characters: Traces, Orthogonality, and the Anatomy of a Representation

Suppose a finite group acts on a vector space of dimension one hundred. To understand that action, one could write down a hundred-by-hundred matrix for every group element. But changing the basis changes all of those matrices, and a collection of huge arrays may obscure the very symmetry we wanted to study. We would prefer a quantity that is independent of the basis and still remembers which irreducible representations are present.

Take the trace of each matrix. The resulting function on the group is called the character of the representation. The trace of a product of two matrices does not generally equal the product of their traces, so a character is not normally a group homomorphism. Nevertheless it has strong structure.

If two matrices are related by a change of basis, their traces agree. Thus equivalent representations have the same character. And because the trace of A B equals the trace of B A, conjugate group elements have the same character value. A character is a class function: it is constant on each conjugacy class.

A group with thousands of elements may have only a few conjugacy classes. Instead of recording a large matrix for every element, we can list one trace for each class. For finite-dimensional complex representations of a finite group, these values are enough to identify the representation up to equivalence.

## Read a character from the triangle

Consider the triangle symmetry group, the same group as permutations of three objects. Its conjugacy classes are the identity, the three reflections, and the two rotations by one third and two thirds of a full turn. There are three conjugacy classes.

For the trivial one-dimensional representation, every group element acts as the number one, so its character is one on all three classes.

For the sign representation, the identity and rotations have character one, while reflections have character negative one. This representation detects orientation reversal.

For the natural two-dimensional geometric representation, the identity has trace two. A reflection has one eigenvalue positive one along its mirror and one eigenvalue negative one across the mirror, so its trace is zero. A rotation by one third of a turn has trace twice the cosine of one hundred twenty degrees, which is negative one. The three character values are therefore two, zero, and negative one.

All six group elements can now be described with three short rows of numbers. The real gain comes when we learn how to compare those rows.

## An inner product on class functions

For complex-valued functions on a finite group, take the average of the first function times the complex conjugate of the second. This defines an inner product on the space of functions. If the functions are characters, remarkable orthogonality relations hold: characters of distinct irreducible complex representations have inner product zero, and an irreducible character has inner product one with itself.

Why should the traces be orthogonal? Start with two irreducible representations, V and W, and any linear map from V to W. Average that map over the group, conjugating on the left with W's action and undoing V's action on the right. The averaged map commutes with the group actions; it is an intertwining map.

Schur's lemma says an intertwining map between two irreducible complex representations is zero unless the representations are equivalent. For an irreducible representation mapped to itself, every intertwiner is a scalar multiple of the identity. The reason is linear algebra: a complex linear operator has an eigenvalue, its eigenspace is invariant under every group transformation when the operator commutes with the representation, and irreducibility forces that eigenspace to be the entire space.

Averaging matrix coefficients with this observation gives orthogonality. Taking traces produces orthogonality of characters. This is not merely a computational trick; it packages the consequences of irreducibility and averaging into one numerical test.

## Count the copies of an irreducible piece

If a representation is the direct sum of two others, its character is their sum because traces add across diagonal blocks. Maschke's theorem tells us that a complex representation of a finite group decomposes into irreducibles. Suppose its character is the sum of irreducible characters with certain nonnegative integer multiplicities.

Take the inner product of that character with any fixed irreducible character. Orthogonality kills all the other terms. The surviving number is exactly the multiplicity of that irreducible representation.

For example, the triangle's three-dimensional permutation representation has trace three at the identity, trace one at a reflection, and trace zero at a nontrivial rotation. Every fixed vertex contributes one to the trace of a permutation matrix, so these numbers are also the counts of fixed vertices.

Compare that character with the trivial character, which is one, one, one. Their inner product is the weighted average of three times one, three copies of one times one, and two copies of zero times one, all divided by six. The result is one. Thus the permutation representation contains one copy of the trivial representation.

Now compare with the two-dimensional character, two, zero, negative one. The weighted average is six from the identity, zero from reflections, and zero from rotations, divided by six: again one. Compare with sign and you get zero. We have proved that the three-dimensional permutation representation consists of one trivial line and one two-dimensional irreducible part, exactly the decomposition we found geometrically.

## The character table has numerical constraints

For a finite group over the complex numbers, the number of inequivalent irreducible representations equals the number of conjugacy classes. Their dimensions obey another striking identity: the sum of the squares of those dimensions equals the group order.

The easiest route to this identity uses the regular representation, where the group acts by left multiplication on basis vectors labeled by its own elements. It has dimension equal to the order of the group. Each irreducible of dimension d appears in it exactly d times. Therefore its dimension is the sum of d times d, taken over every irreducible representation.

For the triangle group, the three irreducible dimensions are one, one, and two. Their squares add to one plus one plus four, which is six, the group order. There is no room for a mysterious fourth irreducible.

These facts are special to finite-dimensional representations of finite groups over an appropriate splitting field, in particular the complex numbers. In modular representation theory the clean semisimple decomposition may fail; the character story requires care and can no longer be applied verbatim.

Characters compress a representation, but they do not discard its essential complex semisimple structure. They connect geometry, traces, and exact integer multiplicities. In later mathematics the same character perspective appears in harmonic analysis, Fourier transforms on finite groups, and the study of symmetries of equations.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For a finite group \(G\) and \(\rho:G\to\mathrm{GL}(V)\) a complex representation, define \(\chi_\rho(g)=\operatorname{tr}\rho(g)\). Its values are constant on conjugacy classes. For class functions,
\[
\langle f,h\rangle_G=\frac1{|G|}\sum_{g\in G}f(g)\overline{h(g)}.
\]
The irreducible characters \(\chi_i\) form an orthonormal basis of the space of class functions. If \(\chi_V=\sum_i m_i\chi_i\), then \(m_i=\langle\chi_V,\chi_i\rangle_G\in\mathbb Z_{\ge0}\).

**\(S_3\) character table.** Columns are identity (size 1), transpositions (size 3), and 3-cycles (size 2):

| Irreducible | \(e\) | \((12)\) | \((123)\) |
|---|---:|---:|---:|
| trivial | 1 | 1 | 1 |
| sign | 1 | -1 | 1 |
| geometric plane | 2 | 0 | -1 |

The permutation representation on \(\mathbb C^3\) has \(\chi_{\mathrm{perm}}=(3,1,0)\) and decomposes as trivial \(\oplus\) geometric plane.

**Regular representation proof.** The character \(\chi_{\mathrm{reg}}(e)=|G|\) and \(\chi_{\mathrm{reg}}(g)=0\) for \(g\ne e\). Thus \(\langle\chi_{\mathrm{reg}},\chi_i\rangle=\chi_i(e)=\dim V_i\). Taking dimensions gives \(|G|=\sum_i(\dim V_i)^2\).

**Schur's lemma.** If \(V,W\) are irreducible finite-dimensional complex representations and \(T:V\to W\) intertwines the actions, then \(T=0\) or an isomorphism; if \(V=W\) then \(T=\lambda I\). Matrix-coefficient orthogonality follows by averaging rank-one maps \(V\to W\) and applying the lemma.

### Exercises with answers

1. Compute \(\langle\chi_{\mathrm{sgn}},\chi_{\mathrm{geo}}\rangle\) for \(S_3\). **Answer:** \((1\cdot2+3(-1)\cdot0+2(1)(-1))/6=0\).
2. How many copies of the trivial representation occur in the regular representation of \(S_3\)? **Answer:** one.
3. What is the trace of a permutation matrix? **Answer:** the number of fixed basis elements.
4. Why does \(\chi(g^{-1})=\overline{\chi(g)}\) for a finite complex representation? **Answer:** after averaging a Hermitian inner product, \(\rho(g)\) is unitary, and the trace of its inverse is the conjugate of its trace.

### Reading

Pavel Etingof and collaborators, [MIT 18.712 lecture notes](https://ocw.mit.edu/courses/18-712-introduction-to-representation-theory-fall-2010/pages/lecture-notes/), Chapter 3, characters, orthogonality, and character tables.
