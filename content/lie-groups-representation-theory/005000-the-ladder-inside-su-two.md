# 005000 — The Ladder Inside SU(2)

**Track:** Lie Groups, Lie Algebras, and Representations. **Preparation:** two-by-two matrices, Lie brackets, invariant subspaces, polynomial differentiation. **Theme:** three commutator relations classify all finite-dimensional complex representations of the complex Lie algebra sl two.

<!-- BEGIN SPOKEN LECTURE -->

# The Ladder Inside SU(2)

The group SU two consists of complex two-by-two unitary matrices with determinant one. It has only three real dimensions as a smooth group, but its representations occur in dimensions one, two, three, four, and every larger positive integer. How can such a small family of matrices have so many different ways to act on vector spaces?

The answer is that the original two-dimensional action can generate entire families of higher-dimensional actions. We will construct them from homogeneous polynomials, then prove that their structure is forced by three elementary commutator relations.

There is one technical change of viewpoint. The Lie algebra of SU two consists of traceless skew-Hermitian matrices, and is a *real* Lie algebra. When studying finite-dimensional complex representations, it is useful to extend scalars from real to complex. Its complexification is the Lie algebra of all complex traceless two-by-two matrices, called sl two over the complex numbers. We will work with that complex Lie algebra. It retains the infinitesimal representation theory we need while making eigenvalues and eigenspaces easier to use.

## Three small matrices

Let H be the diagonal matrix with entries one and negative one. Let E be the matrix with a one in the upper-right corner and zeros elsewhere. Let F be its lower-left counterpart. All three have trace zero, and together they form a basis of the complex traceless two-by-two matrices.

Multiply the matrices and compute the brackets. H with E gives two E. H with F gives negative two F. E with F gives H. Three relations, each only one line long, encode the whole Lie algebra.

The names E and F are suggestive. E raises a certain eigenvalue by two, and F lowers it by two. We can see why without writing down any complicated representation. Let a representation assign operators, again called H, E, and F, satisfying those same brackets. Suppose v is an eigenvector of H with eigenvalue lambda. Then H applied to E v equals E applied to H v plus two E v. That is lambda plus two times E v. Unless E v is zero, it is another eigenvector with eigenvalue lambda plus two.

Similarly, F v, when nonzero, has eigenvalue lambda minus two. A representation decomposes into a ladder of weight spaces, where weights are eigenvalues of H. E climbs the ladder, F descends it.

## A representation you can hold in your hands

Take the ordinary two-dimensional complex vector space with basis vectors we will call x and y. Instead of stopping there, consider homogeneous polynomials of total degree n in two formal variables x and y. A basis consists of x to the n, x to the n minus one times y, and so on, ending with y to the n. There are exactly n plus one basis monomials, so this space has dimension n plus one.

A two-by-two matrix acts on the underlying two-dimensional vector space. By applying that transformation to each factor of a symmetric tensor, it induces an action on homogeneous degree-n polynomials. For SU two this is an honest representation of the group. At the infinitesimal level the action of E is x times differentiation with respect to y; the action of F is y times differentiation with respect to x; and H is x times differentiation with respect to x minus y times differentiation with respect to y.

We can test these formulas on a basis monomial x to the n minus k times y to the k. H multiplies it by n minus twice k. E multiplies it by k and replaces one y with an x. F multiplies it by n minus k and replaces one x with a y. Each operation stays in the degree-n polynomial space.

Thus the weights are n, n minus two, n minus four, continuing down to negative n. Each weight occurs once. E annihilates x to the n, because that polynomial contains no y. F applied repeatedly to x to the n produces every other basis monomial, with nonzero coefficients until the bottom of the ladder is reached.

For n equals two, the basis is x squared, x y, y squared. H has eigenvalues two, zero, negative two. E sends y squared to two x y, and x y to x squared. F sends x squared to two x y, and x y to y squared. We have constructed a three-dimensional representation using only two-by-two matrix algebra and polynomial differentiation.

For n equals three, the space has dimension four, with weights three, one, negative one, negative three. Nothing in the size of the original group prevents it from acting on an arbitrarily large polynomial space.

## Why these representations are irreducible

A representation is irreducible if it has no nontrivial proper invariant subspace. For our polynomial representation, suppose W is a nonzero invariant subspace. Since W is preserved by H and H has distinct eigenvalues on the monomial basis, W contains a nonzero H-eigenvector. One can justify this by applying a polynomial in H that projects a chosen nonzero vector onto one of its nonzero weight components.

Every weight space here is one-dimensional, so that eigenvector is a scalar multiple of one of the monomials. Apply E repeatedly. The raising coefficients are nonzero until we reach x to the n. Therefore W contains the highest-weight vector x to the n. Now apply F repeatedly. Every lower monomial appears, so W contains the entire basis. Thus W was the whole representation space.

This proof is illuminating because it uses only the ladder. We did not appeal to geometric pictures of rotation or to character orthogonality. The irreducibility follows from an eigenvalue calculation and the fact that E and F connect the successive weight spaces.

## Why every finite-dimensional irreducible has this shape

Now turn the construction around. Take any nonzero finite-dimensional complex irreducible representation of sl two. Because H is a complex linear operator, it has an eigenvector. Among its finitely many weights along a raising chain, select a vector v such that E v is zero. It is a highest-weight vector. Let H v equal lambda times v.

Apply F repeatedly. The commutator relations imply a useful identity: E applied to F to the k times v equals k times lambda minus k plus one, multiplied by F to the k minus one times v. The identity follows by induction, moving E past one F at a time using the bracket of E with F equals H, and then moving H past the remaining F operators using its bracket with F.

Because the representation is finite-dimensional, this descending chain eventually terminates. Suppose F to the n times v is nonzero, but F to the n plus one times v is zero. Apply E to that zero vector. The identity gives n plus one times lambda minus n times F to the n v equals zero. Since the last vector is nonzero, lambda must equal n, a nonnegative integer.

Thus the highest weight is constrained to be a nonnegative integer, not an arbitrary complex number. The ladder then has weights n, n minus two, and so on down to negative n, and it contains n plus one nonzero vectors. They span an invariant subspace. Irreducibility forces that span to be the whole representation.

We have sketched the classification: every finite-dimensional irreducible complex representation of sl two is isomorphic to precisely one of these homogeneous-polynomial representations, indexed by a nonnegative integer n. The proof is the systematic version of the concrete calculations we made first.

This is an example of a highest-weight method. Find a vector that cannot be raised, read its weight, then reconstruct the entire representation by lowering operators. More complicated semisimple Lie algebras have several independent raising directions, but this central strategy survives.

## From two dimensions to three and one

Take two copies of the defining two-dimensional representation. Their tensor product has dimension four. Exchange the two factors. The symmetric tensors form a three-dimensional invariant subspace, while the antisymmetric tensors form a one-dimensional invariant subspace. So two tensor two decomposes as three plus one.

This is not merely dimension bookkeeping. The three-dimensional component is the degree-two polynomial representation we constructed, while the one-dimensional antisymmetric component is trivial for SU two because every group matrix has determinant one. In terms of highest weights, the weights one and one combine into highest weights two and zero.

This decomposition is the simplest instance of the Clebsch–Gordan rule. More generally, the tensor product of the representations with highest weights m and n splits into representations with highest weights m plus n, m plus n minus two, and so on down to the absolute value of m minus n. Each occurs once.

We can verify the dimension of the smallest case immediately: two times two equals four, while three plus one also equals four. For the next case, a dimension-three representation tensored with a dimension-two representation gives dimension six, and the rule predicts a dimension-four piece plus a dimension-two piece. Again it works. The full rule can be developed by comparing weight multiplicities and then using complete reducibility for SU two.

## Why the global group changes the answer

There is an important distinction between SU two and SO three. The former is a double cover of the latter. Its central matrix negative I lies in the kernel of the map to SO three. On the homogeneous degree-n polynomial representation, negative I acts by multiplication by negative one to the n-th power.

For even n, that action is the identity, so the representation descends to SO three. For odd n, negative I acts by negative identity, so the representation does **not** define an ordinary representation of SO three through the quotient. The Lie algebra sees the same ladder in either case; the global group decides which ladders are allowed as single-valued representations.

Physicists often label these representations by spin j equal to n divided by two. Even n correspond to integer j, while odd n correspond to half-integer j. The vocabulary comes from angular momentum, but the mathematical source is simple: polynomial degree and the action of a two-element center.

This is the promised return to our first distinction between the local and global. An infinitesimal commutator classification gives all the sl two modules. Passing back to a particular group can impose an additional condition about closed loops and central elements.

A three-dimensional real rotation group, a two-dimensional complex matrix group, and a complex Lie algebra of traceless matrices are now related by explicit calculations rather than by mysterious analogies. Three generators create a ladder. The ladder constrains the possible eigenvalues. Polynomial representations realize every permitted ladder. Tensor products combine the ladders, and the global group determines which ones are genuinely its representations.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

\[
H=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\quad
E=\begin{pmatrix}0&1\\0&0\end{pmatrix},\quad
F=\begin{pmatrix}0&0\\1&0\end{pmatrix},
\quad [H,E]=2E,\ [H,F]=-2F,\ [E,F]=H.
\]
For \(V_n=\operatorname{Sym}^n(\mathbb C^2)\) (homogeneous degree-n polynomials), let \(v_k=x^{n-k}y^k\), \(0\le k\le n\):
\[
H v_k=(n-2k)v_k,\quad E v_k=k v_{k-1},\quad F v_k=(n-k)v_{k+1}
\]
with absent endpoint vectors taken as zero. For highest-weight \(v\) with \(Ev=0\), \(Hv=\lambda v\):
\[
E F^k v=k(\lambda-k+1)F^{k-1}v.
\]
If \(F^n v\ne0\) and \(F^{n+1}v=0\), then \(\lambda=n\). For \(SU(2)\), the irreducible modules \(V_n\) have dimension \(n+1\) and \(-I\) acts by \((-1)^n\); exactly those with even \(n\) descend to \(SO(3)\).

\[
V_m\otimes V_n\cong\bigoplus_{k=0}^{\min(m,n)}V_{m+n-2k}.
\]

**Exercises and solutions.** (1) List the weights of \(V_4\). *4, 2, 0, -2, -4.* (2) Compute \(E(xy^2)\). *\(2x^2y\).* (3) Decompose \(V_1\otimes V_2\). *\(V_3\oplus V_1\), dimensions 4 + 2 = 6.* (4) Does \(V_3\) descend to \(SO(3)\)? *No; \(-I\) acts by \(-1\).* (5) Why is the complexification step worth stating? *The real Lie algebra \(\mathfrak{su}_2\) is not literally the complex vector space \(\mathfrak{sl}_2(\mathbb C)\); the latter is its complexification.*

### Sources and further reading

- MIT OCW 18.745 (2020), lecture 11 on representations of sl two: https://ocw.mit.edu/courses/18-745-lie-groups-and-lie-algebras-i-fall-2020/resources/lecture-notes/
- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations*, 2nd ed., basic representations and semisimple theory: https://doi.org/10.1007/978-3-319-13467-3
- Pavel Etingof et al., *Introduction to Representation Theory*, sections on Lie algebras and sl two: https://math.mit.edu/~etingof/replect.pdf
