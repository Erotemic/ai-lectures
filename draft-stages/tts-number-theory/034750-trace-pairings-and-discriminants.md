# 034750 — Trace Pairings, Dual Lattices, and Discriminants

**Track:** Number Theory from First Principles. **Background:** 027000, 027625, 027875 (quadratic integers, trace lattices, ideal norms); 029250 (the index trap); 031750 (finite local extensions). **Aim:** construct the discriminant from the trace pairing, derive the basis-change and index formulas, and explain why an integral basis matters.

<!-- BEGIN SPOKEN LECTURE -->

# Trace Pairings, Dual Lattices, and Discriminants

Two people hand you the same quadratic number field in two different descriptions. One says it is the rationals together with the square root of five. The other says it is the rationals together with the number one plus the square root of five, divided by two. Their fields agree. Their polynomial discriminants do not. The first calculation gives twenty; the second gives five. Which number tells us where primes ramify?

Five is the field discriminant. Twenty is the discriminant of a smaller ring inside the full ring of integers. The discrepancy is not a nuisance in a formula. It is the mathematical reason the polynomial X squared minus five can give a false prediction about the prime two. We will understand it through a pairing, a dual lattice, and a determinant.

## A pairing with values back in the ground field

Let L be a number field of degree n over the rationals. Every element x of L acts on L by multiplication: send y to xy. The trace of this rational linear map is called the field trace of x. If the conjugates of x are x-one through x-n, counted through the n embeddings of L into the complex numbers, then its trace is their sum.

There is a natural two-input operation: take x and y, multiply them, and take the trace of their product. This is the trace pairing. It is symmetric and rational-bilinear. Symmetric means changing the order does nothing. Bilinear means it respects adding either input and multiplying either input by rational scalars.

Why use a two-input operation instead of merely taking traces of individual elements? Because a pairing measures how well one set of coordinates can detect another. In ordinary Euclidean geometry, a dot product with each vector of a basis determines an unknown vector. Here, traces against basis elements can do the same job, even though the pairing need not be positive. In an imaginary quadratic field it can be negative on some nonzero squares.

Separability is what makes the trace pairing nondegenerate. A nonzero x cannot have trace of xy equal to zero for every y. To see the structure, choose a rational basis b-one through b-n and list the n embeddings sigma-one through sigma-n. Make a square matrix whose entry in row i, column j is sigma-i of b-j. Call it the embedding matrix. The matrix of the trace pairing in our basis is the transpose of that embedding matrix times the embedding matrix itself. Its determinant is therefore the square of the embedding matrix's determinant.

The embeddings are distinct, and their evaluations on a basis are linearly independent; this is the separability fact already underlying the trace lattice argument in our treatment of Dedekind domains. Consequently that determinant is not zero. The pairing does detect every nonzero vector.

## The Gram matrix, and why a square appears

Now insist that our basis elements are algebraic integers. Their pairwise products are algebraic integers, and the trace of an algebraic integer is an ordinary integer. So the Gram matrix, the matrix of traces of b-i times b-j, has integer entries.

Define the discriminant of the basis to be the determinant of this Gram matrix. It is an integer, not merely a rational number. It can be negative. To understand the sign, observe that real embeddings contribute real rows and the complex embeddings come in conjugate pairs. Pairing each nonreal row with its conjugate contributes one negative sign to the square of the determinant. If there are r-two pairs of complex embeddings, the sign is negative one to the power r-two.

The basis is not arbitrary bookkeeping: a different basis changes the Gram matrix. Suppose the new basis is obtained from the old one by a rational change-of-basis matrix C. The Gram matrix changes to C-transpose times the old Gram matrix times C. Taking determinants multiplies the discriminant by the square of the determinant of C.

If both lists are bases of the same lattice of algebraic integers, C is an integer matrix with an integer inverse. Its determinant is plus or minus one. Its square is one, so the discriminant does not change. That is why the discriminant of a number field, defined from a complete integral basis, is a field invariant.

If one list spans only a sublattice, however, its determinant may differ by a nontrivial integer factor. This is the index formula: the discriminant of a finite-index sublattice is the discriminant of the full lattice times the square of the index. We can prove it in one sentence of linear algebra. An integral basis of the smaller lattice has a coordinate matrix in a basis of the larger; the absolute determinant of that integer matrix is exactly the index, and the pairing makes its determinant appear twice.

## The square root of five, twice

Let L be the rationals with the square root of five. Put omega equal to one plus the square root of five, divided by two. We know from the classification of quadratic integer rings that the full ring of integers has basis one and omega. Omega satisfies omega squared equals omega plus one.

The trace of one is two. The trace of omega is one, because its conjugate is one minus the square root of five, divided by two. The trace of omega squared is three: substitute omega squared equals omega plus one and take traces. Thus our trace Gram matrix has first row two, one and second row one, three. Its determinant is six minus one, or five.

Now use the smaller ring generated by the square root of five. Its basis is one and the square root of five. The trace Gram matrix has diagonal entries two and ten, with zeros off the diagonal. Its determinant is twenty. But the smaller ring has index two in the ring generated by omega. Twenty is four times five, exactly the square-index law.

Notice the arithmetic consequence. The polynomial X squared minus five has a repeated root modulo two. But its ring is not maximal at two. The repeated root is detecting the failure of that chosen order to be well behaved, not ramification in the actual field. In contrast, omega has polynomial X squared minus X minus one. Modulo two, that becomes X squared plus X plus one, which is irreducible and separable. The local extension at two is unramified of residue degree two.

That example has a second interpretation: two different embeddings of one field, one true ring of integers. A polynomial equation is a presentation. An integral basis is an arithmetic object.

## Dual coordinates as algebraic numbers

The trace pairing gives something more than a determinant. Given an integral basis b-one through b-n, there is a unique dual rational basis b-star-one through b-star-n with trace of b-star-i times b-j equal to one if i equals j, and zero otherwise.

These dual vectors lie in L. Their integer combinations form the trace-dual lattice. More intrinsically, the trace-dual of the full ring of integers consists of all x in L such that the trace of xy is an integer for every algebraic integer y. That definition makes no reference to a chosen basis.

The full ring is contained in its trace dual, because products of algebraic integers have integer trace. The containment may be strict. Think of it as a failure of the integer lattice to be self-dual under this particular pairing. The discriminant measures the size of that failure: the finite quotient of the dual lattice by the original ring has exactly the absolute value of the field discriminant many elements.

For our field with square root of five, the inverse of the Gram matrix is one fifth times the matrix whose rows are three, minus one and minus one, two. So the dual basis contains fifths even though our original basis contained no denominators. The index of the original lattice in the trace dual is five.

We now have three manifestations of the same integer. Five is a determinant of traces. It is an index of one lattice inside another. And it identifies a prime where the trace pairing stops being perfect after reduction modulo that prime. We have not yet proved that this last event is precisely ramification, but we can already see why a discriminant should have something to say about primes.

## What a discriminant does not tell us

A discriminant is not itself a full factorization of primes. Knowing that a prime does not divide the field discriminant says it is unramified, but does not say whether it splits or remains inert. In our square-root-of-five example, two is unramified and inert, whereas eleven is unramified and splits. Both are invisible to the discriminant as ramified primes.

Nor may we take the discriminant of whichever polynomial happens to define a field and declare it the field discriminant. The square-index correction must be checked. Over a more general base number field, there may not even be a global integral basis for the extension as a module over the base integers; one uses a discriminant ideal instead. The trace pairing remains the organizing idea in either case.

Next we can turn that failure of self-duality into an actual ideal, living in the extension ring rather than in the ordinary integers. That ideal is the different. Its name is less transparent than its construction, but the construction now has a clear purpose: isolate exactly which algebraic integers account for imperfect trace duality, and measure their contributions prime by prime.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Let `K/Q` be separable of degree `n`, `B=O_K` and `b=(b_1,...,b_n)` an integral basis. With embeddings `sigma_i`, write `E=(sigma_i(b_j))` and `G=(Tr(b_i b_j))=E^T E`.

\[
\operatorname{disc}(b)=\det G=(\det E)^2,
\qquad\operatorname{disc}(bC)=(\det C)^2\operatorname{disc}(b).
\]

For any order `R subseteq B` of finite index `m`,
\[
\operatorname{disc}(R)=m^2\operatorname{disc}(B).
\]

The trace dual is `B^vee={x in K: Tr(xB) subseteq Z}`. If `b_i^vee` is the trace-dual basis, then
\[
|B^\vee/B|=|\operatorname{disc}(B)|.
\]

For `K=Q(sqrt 5)`, `omega=(1+sqrt 5)/2`:
\[
G_{(1,\omega)}=\begin{pmatrix}2&1\\1&3\end{pmatrix},\quad\det G=5,
\qquad
G_{(1,\sqrt5)}=\begin{pmatrix}2&0\\0&10\end{pmatrix},\quad\det G=20.
\]

The dual basis of `(1,omega)` is `((3-omega)/5,(-1+2omega)/5)`.

### Exercises

1. Compute the trace matrix, discriminant, and trace-dual basis for `Z[i]`. Explain its negative sign.
2. Derive the square-index formula by writing the sublattice basis in terms of the full integral basis.
3. Check directly that `X^2-X-1` is separable and irreducible modulo two, whereas `X^2-5` reduces to a repeated root.
4. Explain why the discriminant cannot distinguish an inert prime from a split prime when neither ramifies.

## Sources and reading

- Andrew V. Sutherland, *18.785 Number Theory I*, Lecture 12, “The Different and the Discriminant,” pp. 2–5: https://ocw.mit.edu/courses/18-785-number-theory-i-fall-2021/mit18_785f21_lec12.pdf
- Wikipedia: [Discriminant of an algebraic number field](https://en.wikipedia.org/wiki/Discriminant_of_an_algebraic_number_field), [Different ideal](https://en.wikipedia.org/wiki/Different_ideal), [Quadratic field](https://en.wikipedia.org/wiki/Quadratic_field).

**Proof scope:** Derives the Gram-matrix, embedding, basis-change, square-index and trace-dual index formulas. The general separability/nondegeneracy theorem and classification of quadratic integer rings were established previously in this course.
