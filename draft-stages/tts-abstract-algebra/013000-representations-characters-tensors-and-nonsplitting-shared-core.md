# Representations and characters

<!-- BEGIN SPOKEN LECTURE -->

# Representations and characters

## Representations: Making Symmetry Act on Vector Spaces

Think about the symmetries of an equilateral triangle. There are six: three rotations and three reflections. We can multiply those symmetries without ever writing coordinates, and group theory tells us what follows from that multiplication. But the triangle also lies in a plane. We can represent each symmetry by a two-by-two matrix and ask what it does to vectors. That extra choice of setting lets us use eigenvectors, projections, traces, and linear algebra. Representation theory studies exactly that passage from abstract multiplication to concrete linear action.

A representation of a group G on a vector space V over a field is a rule assigning to each group element an invertible linear transformation of V. The rule must preserve multiplication: the transformation assigned to the product of two group elements is the composition of their assigned transformations. It sends the identity to the identity linear map, and inverse group elements to inverse transformations. The dimension of V is the dimension of the representation.

Why invertibility? Because every group element has an inverse. If an assigned linear map failed to be invertible, there could not be a transformation representing the inverse group element. Representation theory is a stricter construction than simply assigning a matrix to each group element.

### Three ways a group can act

The triangle acts on its own plane by ordinary rotations and reflections. We obtain a two-dimensional real representation. A rotation by one third of a full turn has no nonzero real fixed vector, yet the reflection across an axis has one. The same group can therefore contain transformations with very different geometric behavior.

The group also acts on the three vertices by permuting them. Associate one coordinate to each vertex. A vertex permutation becomes a three-by-three permutation matrix, producing a different representation on three-dimensional space. The vector whose coordinates are all one is fixed by every permutation. Thus the line it spans is a one-dimensional invariant subspace. The plane of coordinate triples whose sum is zero is another invariant subspace. The three-dimensional permutation representation has separated into a fixed line and a two-dimensional part.

There is even a one-dimensional representation in which each rotation acts as multiplication by positive one and each reflection by negative one. This is the sign representation. It discards the geometric details but preserves whether a symmetry reverses orientation.

Notice that no representation is the group itself. A representation may forget distinctions between group elements: a trivial representation sends all of them to the identity. A faithful representation, by contrast, sends distinct group elements to distinct transformations. The three-vertex permutation representation of the triangle group is faithful, while the sign representation is not.

### Invariant subspaces are the first structural question

If W is a subspace of V that every group transformation maps into W, we call it invariant. We can restrict the representation to W. This is analogous to finding an invariant subspace for a single matrix, except that W must be invariant under an entire family of matrices at once.

A representation is irreducible if its only invariant subspaces are zero and the entire space. Otherwise it is reducible. For the triangle's three-coordinate permutation representation, the fixed line is an invariant proper subspace, so the representation is reducible. The two-dimensional sum-zero plane is in fact irreducible over the real numbers for the full triangle symmetry group: a line invariant under all of its rotations would need a real eigenvector for a rotation by one third of a turn, and none exists.

A direct sum of representations acts on pairs of vectors one component at a time. If we can write V as a direct sum of invariant subspaces, all representation matrices become block diagonal in a basis adapted to that decomposition. Complicated transformations can be analyzed one block at a time.

But finding one invariant subspace does not automatically yield an invariant complement. Every vector space admits a complement as a vector space. The stronger requirement is that the group preserve the complement too. In positive characteristic, even a representation of a finite group may fail to have such a complement.

### The averaging trick

There is a powerful theorem for finite groups over fields whose characteristic does not divide the number of group elements. It is commonly called Maschke's theorem: every invariant subspace has an invariant complement, and every finite-dimensional representation breaks into a direct sum of irreducible representations.

The proof explains why the assumption about the field matters. Begin with an invariant subspace W of V and choose any linear projection P from V onto W. We know P is the identity on W, but it may fail to commute with the group action. The group may carry a vector in the chosen complementary subspace to a vector outside it.

Repair that projection by averaging all its conjugates. For every group element g, first undo g, then apply P, then apply g; average those operators over the entire group. Call the result Q. Since W is invariant, each conjugated projection still acts as the identity on W and still maps V into W. So Q is a projection onto W.

Now take any group element h and conjugate Q by h. This just reorders the group elements appearing in the average. Because the sum runs over every element once, the operator does not change. Hence Q commutes with the representation of every h. Its kernel is therefore an invariant subspace. The image is W, the kernel is an invariant complement, and V is their direct sum.

The exact step that can fail is division by the number of group elements. If the field has characteristic p and the group order is divisible by p, that number becomes zero in the field. We cannot divide by it. The theorem does not promise a complement there.

### A small counterexample in characteristic two

Take the group of two elements and a two-dimensional vector space over the field with two elements. Let the nonidentity group element act by the matrix that adds the second coordinate to the first and leaves the second coordinate unchanged. In matrix notation this is an upper triangular matrix with ones on the diagonal and a one above the diagonal.

Applying the matrix twice gives the identity because two equals zero in this field. So it really is a representation of a group of order two. The line spanned by the first coordinate vector is invariant. But it has no invariant complementary line. The only nonzero eigenvectors for eigenvalue one lie on that same line; every invariant one-dimensional subspace is the line we already have. The representation is reducible but does not split into one-dimensional representations.

This is an important warning. The statement that finite-group representations split is not true without hypotheses. The field, not just the group, participates in the theorem.

### Why the new viewpoint is useful

A representation can turn a question about symmetry into a question about matrices. Invariant subspaces show which modes are independent. Averages over a group construct invariant inner products and projections. The action on functions, which sends each function to its pullback under a symmetry, lets us analyze symmetric signals. In a physical system with a symmetry, linearized modes often organize themselves into representations, constraining which couplings are possible.

The triangle's three-coordinate representation is a miniature example. One mode moves all coordinates together. Two other independent directions describe departures from their common value. The group acts trivially on the first part and nontrivially on the second. Splitting is not merely a way to make matrices smaller; it distinguishes what a symmetry can preserve from what it can transform.

The next tool is trace. In a finite-dimensional representation, the trace of the matrix representing a group element turns out to record enough information to tell complex representations apart and to count how many irreducible pieces occur. That function is called the character of the representation. It compresses all the matrix calculations into a surprisingly small amount of data.

## Characters: Traces, Orthogonality, and the Anatomy of a Representation

Suppose a finite group acts on a vector space of dimension one hundred. To understand that action, one could write down a hundred-by-hundred matrix for every group element. But changing the basis changes all of those matrices, and a collection of huge arrays may obscure the very symmetry we wanted to study. We would prefer a quantity that is independent of the basis and still remembers which irreducible representations are present.

Take the trace of each matrix. The resulting function on the group is called the character of the representation. The trace of a product of two matrices does not generally equal the product of their traces, so a character is not normally a group homomorphism. Nevertheless it has strong structure.

If two matrices are related by a change of basis, their traces agree. Thus equivalent representations have the same character. And because the trace of A B equals the trace of B A, conjugate group elements have the same character value. A character is a class function: it is constant on each conjugacy class.

A group with thousands of elements may have only a few conjugacy classes. Instead of recording a large matrix for every element, we can list one trace for each class. For finite-dimensional complex representations of a finite group, these values are enough to identify the representation up to equivalence.

### Read a character from the triangle

Consider the triangle symmetry group, the same group as permutations of three objects. Its conjugacy classes are the identity, the three reflections, and the two rotations by one third and two thirds of a full turn. There are three conjugacy classes.

For the trivial one-dimensional representation, every group element acts as the number one, so its character is one on all three classes.

For the sign representation, the identity and rotations have character one, while reflections have character negative one. This representation detects orientation reversal.

For the natural two-dimensional geometric representation, the identity has trace two. A reflection has one eigenvalue positive one along its mirror and one eigenvalue negative one across the mirror, so its trace is zero. A rotation by one third of a turn has trace twice the cosine of one hundred twenty degrees, which is negative one. The three character values are therefore two, zero, and negative one.

All six group elements can now be described with three short rows of numbers. The real gain comes when we learn how to compare those rows.

### An inner product on class functions

For complex-valued functions on a finite group, take the average of the first function times the complex conjugate of the second. This defines an inner product on the space of functions. If the functions are characters, remarkable orthogonality relations hold: characters of distinct irreducible complex representations have inner product zero, and an irreducible character has inner product one with itself.

Why should the traces be orthogonal? Start with two irreducible representations, V and W, and any linear map from V to W. Average that map over the group, conjugating on the left with W's action and undoing V's action on the right. The averaged map commutes with the group actions; it is an intertwining map.

Schur's lemma says an intertwining map between two irreducible complex representations is zero unless the representations are equivalent. For an irreducible representation mapped to itself, every intertwiner is a scalar multiple of the identity. The reason is linear algebra: a complex linear operator has an eigenvalue, its eigenspace is invariant under every group transformation when the operator commutes with the representation, and irreducibility forces that eigenspace to be the entire space.

Averaging matrix coefficients with this observation gives orthogonality. Taking traces produces orthogonality of characters. This is not merely a computational trick; it packages the consequences of irreducibility and averaging into one numerical test.

### Count the copies of an irreducible piece

If a representation is the direct sum of two others, its character is their sum because traces add across diagonal blocks. Maschke's theorem tells us that a complex representation of a finite group decomposes into irreducibles. Suppose its character is the sum of irreducible characters with certain nonnegative integer multiplicities.

Take the inner product of that character with any fixed irreducible character. Orthogonality kills all the other terms. The surviving number is exactly the multiplicity of that irreducible representation.

For example, the triangle's three-dimensional permutation representation has trace three at the identity, trace one at a reflection, and trace zero at a nontrivial rotation. Every fixed vertex contributes one to the trace of a permutation matrix, so these numbers are also the counts of fixed vertices.

Compare that character with the trivial character, which is one, one, one. Their inner product is the weighted average of three times one, three copies of one times one, and two copies of zero times one, all divided by six. The result is one. Thus the permutation representation contains one copy of the trivial representation.

Now compare with the two-dimensional character, two, zero, negative one. The weighted average is six from the identity, zero from reflections, and zero from rotations, divided by six: again one. Compare with sign and you get zero. We have proved that the three-dimensional permutation representation consists of one trivial line and one two-dimensional irreducible part, exactly the decomposition we found geometrically.

### The character table has numerical constraints

For a finite group over the complex numbers, the number of inequivalent irreducible representations equals the number of conjugacy classes. Their dimensions obey another striking identity: the sum of the squares of those dimensions equals the group order.

The easiest route to this identity uses the regular representation, where the group acts by left multiplication on basis vectors labeled by its own elements. It has dimension equal to the order of the group. Each irreducible of dimension d appears in it exactly d times. Therefore its dimension is the sum of d times d, taken over every irreducible representation.

For the triangle group, the three irreducible dimensions are one, one, and two. Their squares add to one plus one plus four, which is six, the group order. There is no room for a mysterious fourth irreducible.

These facts are special to finite-dimensional representations of finite groups over an appropriate splitting field, in particular the complex numbers. In modular representation theory the clean semisimple decomposition may fail; the character story requires care and can no longer be applied verbatim.

Characters compress a representation, but they do not discard its essential complex semisimple structure. They connect geometry, traces, and exact integer multiplicities. In later mathematics the same character perspective appears in harmonic analysis, Fourier transforms on finite groups, and the study of symmetries of equations.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Representations: Making Symmetry Act on Vector Spaces

**Track:** Abstract Algebra. **Background:** group actions, linear maps, finite-dimensional vector spaces, and quotients. **Question:** what becomes visible when an abstract group acts through matrices, and why does averaging allow representations of finite groups to split?

#### Mathematical companion (not spoken)

A representation is a homomorphism \(\rho:G\to \mathrm{GL}(V)\). A subrepresentation is a subspace \(W\subseteq V\) with \(\rho(g)W\subseteq W\) for all \(g\). For finite \(G\) and \(\mathrm{char}(k)\nmid |G|\), Maschke's theorem says every finite-dimensional \(kG\)-module is completely reducible.

**Proof of Maschke.** Take a linear retraction \(P:V\to W\) of the inclusion \(W\hookrightarrow V\) and form
\[
Q=\frac{1}{|G|}\sum_{g\in G}\rho(g)P\rho(g)^{-1}.
\]
Then \(\operatorname{im}Q\subseteq W\), \(Q|_W=\mathrm{id}_W\), and \(\rho(h)Q\rho(h)^{-1}=Q\) by reindexing. Therefore \(Q^2=Q\), and \(\ker Q\) is a \(G\)-stable complement: \(V=W\oplus\ker Q\).

**The triangle group.** The permutation representation of \(S_3\) on \(k^3\) decomposes, when \(\mathrm{char}(k)\nmid6\), as \(k(1,1,1)\oplus\{(a,b,c):a+b+c=0\}\). Over \(\mathbb R\), the second summand is irreducible for the natural geometric action.

**Modular counterexample.** Over \(\mathbb F_2\), let \(G=C_2=\langle g\rangle\) and
\[
\rho(g)=\begin{pmatrix}1&1\\0&1\end{pmatrix},\qquad \rho(g)^2=I.
\]
The invariant line \(\mathbb F_2e_1\) has no invariant complement because every nonzero eigenvector of \(\rho(g)\) lies in it.

##### Exercises with answers

1. Does \(g\mapsto I_V\) define a representation for any group? **Yes.** It is the trivial representation, generally not faithful.
2. Why does the kernel of an equivariant projection yield a subrepresentation? **Because** \(Q\rho(g)=\rho(g)Q\) implies \(Qv=0\Rightarrow Q\rho(g)v=0\).
3. Show the sum-zero plane is invariant under permutation of three coordinates. **Answer:** permuting entries preserves their sum.
4. Which field hypothesis is needed to average over a finite group? **Answer:** \(|G|\) must be invertible in the coefficient field.

##### Reading

Pavel Etingof and collaborators, [MIT 18.712 representation theory lecture notes](https://ocw.mit.edu/courses/18-712-introduction-to-representation-theory-fall-2010/pages/lecture-notes/), Chapter 3, on Maschke's theorem and representations of finite groups.

### Characters: Traces, Orthogonality, and the Anatomy of a Representation

**Track:** Abstract Algebra. **Background:** finite-dimensional complex vector spaces, group representations, and Maschke's theorem. **Question:** how can a few complex numbers reveal the irreducible components of a family of matrices?

#### Mathematical companion (not spoken)

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

##### Exercises with answers

1. Compute \(\langle\chi_{\mathrm{sgn}},\chi_{\mathrm{geo}}\rangle\) for \(S_3\). **Answer:** \((1\cdot2+3(-1)\cdot0+2(1)(-1))/6=0\).
2. How many copies of the trivial representation occur in the regular representation of \(S_3\)? **Answer:** one.
3. What is the trace of a permutation matrix? **Answer:** the number of fixed basis elements.
4. Why does \(\chi(g^{-1})=\overline{\chi(g)}\) for a finite complex representation? **Answer:** after averaging a Hermitian inner product, \(\rho(g)\) is unitary, and the trace of its inverse is the conjugate of its trace.

##### Reading

Pavel Etingof and collaborators, [MIT 18.712 lecture notes](https://ocw.mit.edu/courses/18-712-introduction-to-representation-theory-fall-2010/pages/lecture-notes/), Chapter 3, characters, orthogonality, and character tables.
