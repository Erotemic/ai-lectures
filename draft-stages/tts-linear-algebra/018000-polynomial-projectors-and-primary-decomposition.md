# Separating Mixed Modes: Polynomial Spectral Projectors and Primary Decomposition

**Track:** Linear Algebra from First Principles. **Background:** polynomial evaluation at matrices, minimal polynomials, kernels, generalized eigenvectors, and polynomial division. **Purpose:** make invariant subspace decomposition and finite-dimensional functional calculus constructive.

<!-- BEGIN SPOKEN LECTURE -->

# Separating Mixed Modes

Suppose a matrix acts on a vector, mixing several kinds of behavior. One part of the vector grows by a factor near two every step. Another part grows by a factor near three. A third part might shear inside the first component. We want to separate those behaviors without having to guess a basis of eigenvectors, especially because the matrix may not have enough ordinary eigenvectors for such a basis.

The solution is to build special transformations from the original matrix itself. Each transformation keeps one class of modes and removes the others. These are spectral projectors. For the first encounter, we will construct them using nothing more than polynomials and the Euclidean algorithm, the same tools used to solve elementary divisibility problems.

## Projection does not have to mean perpendicular

A projection is a linear map P satisfying P squared equals P. Applying it once selects some component; applying it again changes nothing. Every vector can be written as P applied to the vector plus identity minus P applied to the vector. The first piece lies in the image of P, and the second lies in its kernel.

In Euclidean geometry we often imagine projection as dropping a perpendicular onto a line. But a general algebraic projection can move parallel to a slanted complementary direction instead. Its image and kernel need not be perpendicular. This distinction becomes essential for matrices that are not symmetric or normal. We will construct algebraic projectors first, without assuming an inner product.

A projector onto an invariant part of a linear transformation should also commute with that transformation. In other words, selecting the component and then applying A must produce the same result as first applying A and then selecting. A polynomial in A automatically has this property because all powers of A commute with A. This makes polynomials natural candidates for projectors.

## The easy case: distinct eigenvalues

Take the diagonal matrix with entries two and three. The operation A minus three times the identity is zero on the second coordinate and minus one on the first coordinate. Its negative, three times the identity minus A, therefore keeps the first coordinate and kills the second. Call it P two. Similarly, A minus two times the identity keeps the second coordinate and kills the first. Call it P three.

Notice what we have achieved. Both projectors are polynomials in the original matrix. We never needed a separately named coordinate selector. The projectors add up to the identity. Multiplying them gives zero. Squaring either one leaves it unchanged. And A itself is two times the first projector plus three times the second.

If the eigenvalues are distinct and a matrix is diagonalizable, this idea generalizes. For each eigenvalue, make a polynomial that equals one at that eigenvalue and zero at all the others. Such polynomials are produced by Lagrange interpolation. Evaluated at A, they select the corresponding eigenspaces. The resulting operators are independent of the choice of eigenvectors used to describe them.

But that construction seems to stumble when an eigenvalue is repeated. Matching a polynomial's value at a repeated eigenvalue is not always enough to eliminate the shear inside a generalized eigenspace. We need information about the polynomial's derivatives as well as its values.

## Repeated eigenvalues ask for stronger divisibility

Consider a three-dimensional matrix. On its first two coordinates, it acts like the two-by-two shear with eigenvalue two: its top-left block has rows two, one and zero, two. On the third coordinate, it multiplies by three. These are two distinct modes, but one of them is internally coupled.

The minimal polynomial is the square of x minus two, multiplied by x minus three. To remove the two-mode entirely, it is not enough to use a polynomial that vanishes at two. Its value and first derivative must both vanish there, because a two-step Jordan chain is present. The polynomial x minus two squared does exactly that. On the two-by-two block it becomes zero. On the one-dimensional three-mode it becomes one, because three minus two squared is one.

Therefore the square of A minus twice the identity is exactly the projector onto the third coordinate. The projector onto the two-mode is the identity minus that square. We can verify these claims by direct matrix multiplication. The two projectors square to themselves, their product is zero, and their sum is the identity.

This example carries the whole philosophy. The polynomial does not merely recognize numerical eigenvalues. It recognizes how many steps of generalized-eigenvector behavior must be killed inside each mode.

## The polynomial Chinese remainder theorem

Here is the general construction. Work over the complex numbers for now, so that every polynomial factors into linear factors. Factor the minimal polynomial of A into powers of distinct linear factors: one factor for each eigenvalue, raised to an exponent large enough to kill the associated generalized eigenspace.

These factors are pairwise coprime: no two share a root. The polynomial Chinese remainder theorem tells us that we can prescribe a polynomial's remainders separately modulo each of these factors. In particular, for one selected eigenvalue we can build a polynomial whose remainder is one modulo that eigenvalue's factor and zero modulo all the others.

Why does the word 'modulo' matter? Saying that the polynomial equals one at an eigenvalue only concerns its value. Saying that its difference from one is divisible by a whole power of x minus lambda also controls enough derivatives to respect the generalized eigenspace. The congruence is precisely the stronger condition we need.

Now evaluate the polynomial at A. On the generalized eigenspace we selected, the difference between this operator and the identity contains a factor that annihilates the whole eigenspace. On every other generalized eigenspace, the operator itself contains that annihilating factor. Thus it acts as identity on one component and as zero on the others.

There is no hidden appeal to a diagonalizing matrix. Indeed, this construction is one way to prove that the whole space splits as a direct sum of generalized eigenspaces. Because the polynomials that select the pieces add to one modulo the minimal polynomial, their matrix evaluations add to the identity. Because different selector polynomials multiply to zero modulo the minimal polynomial, their projectors have zero pairwise products. Every vector splits into its selected pieces, and no nonzero vector belongs to two different pieces.

The written companion gives the Bézout argument behind this result. The important point for a listener is that a decomposition of polynomial factors becomes a decomposition of the vector space on which A acts.

## What exactly is independent of coordinates?

Suppose we replace A by a similar matrix, representing the same linear transformation in a different basis. A polynomial of the similar matrix is similar to the same polynomial of A. So the projector constructed by this method describes the same invariant subspace; only its coordinate entries change.

There is another benefit. The projectors commute with every polynomial in A. We can split a polynomial calculation into separate problems on the different generalized eigenspaces. For instance, powers of A can be computed by taking powers on each Jordan block and then recombining the pieces with the projectors. A large system with several eigenvalues becomes a collection of smaller systems.

This is not yet the orthogonal spectral theorem. For a self-adjoint matrix, eigenspaces for different eigenvalues are perpendicular, and the spectral projections are orthogonal. For a general matrix, the complementary generalized eigenspaces need not be perpendicular. A projection onto a slanted subspace can have norm much greater than one. Consequently, two nearby eigenvalues do not necessarily imply that their corresponding spectral projectors vary gently under a perturbation. The geometry of the eigenspaces matters.

## From a polynomial of A to a function of A

Imagine wanting to apply a function, not merely a polynomial, to a matrix. For a diagonal matrix with diagonal entries two and three, the intuitive rule is to apply the function separately to those entries. But what should the function mean for a shear block that cannot be diagonalized?

For functions with suitable derivatives, finite-dimensional Jordan theory provides a definition. On a block equal to lambda times the identity plus N, where a power of N is zero, we can form a finite Taylor expression: the value of the function at lambda times the identity, plus its first derivative there times N, plus its second derivative there divided by two times N squared, and so on until the nilpotent terms stop.

This is not merely a convenient approximation. For a polynomial, the formula is an exact identity, because all higher powers of N vanish. For a holomorphic function, it agrees with the analytic matrix functional calculus. And because there are only finitely many eigenvalues and finitely many derivatives needed, a polynomial can be constructed that matches the required Taylor data at each eigenvalue. That is Hermite interpolation.

In our two-by-two shear, a function evaluated at A has the function's value at two on the diagonal and its derivative at two in the upper-right entry. This is a revealing answer. Knowing only the values of a function on the spectrum would not determine what it does to a defective matrix. Derivative information is essential.

This is also why the self-adjoint case becomes simpler. A self-adjoint matrix has no nontrivial Jordan chains, so only the function values on its real eigenvalues are needed. The continuous functional calculus for bounded self-adjoint operators in infinite-dimensional Hilbert spaces extends this simpler idea by limits; its full proof requires new analytic tools, not just the finite polynomial construction.

## The scope of the method

The polynomial projection construction assumes a finite-dimensional linear operator and a minimal polynomial that splits into the appropriate factors. Over the real numbers, some irreducible factors may be quadratic rather than linear; the same coprime-factor method still gives real invariant subspaces, but they need not be one-dimensional real eigenspaces.

For infinite-dimensional operators, a polynomial that annihilates the whole operator may not exist. Even when a spectrum can be defined, it can contain infinitely many points or continuous intervals. Some operator functional calculi rely on integration, contour integrals, or approximation, and unbounded operators require special care with domains.

We should therefore keep two conclusions separate. The first, established here, is algebraic: every finite-dimensional transformation over a splitting field decomposes into generalized eigenspaces, and polynomial selectors can recover the pieces. The second is a bridge forward: the language of spectral projections and functions of operators has a meaning beyond matrices, but the proofs and hypotheses change.

A spectral projector is not a mysterious black box that extracts an eigenmode. In finite dimensions it can be built from ordinary polynomial arithmetic. That construction explains both why distinct modes can be separated and why repeated eigenvalues require more information than a list of roots.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Let \(A\in M_n(\mathbb C)\) with minimal polynomial
\[
m_A(t)=\prod_{j=1}^s q_j(t),\qquad q_j(t)=(t-\lambda_j)^{r_j},\quad \lambda_i\ne\lambda_j\ (i\ne j).
\]
Because \(q_j\) are pairwise coprime, the polynomial Chinese remainder theorem gives unique residue classes \([e_j]\in\mathbb C[t]/(m_A)\) with
\[
e_j\equiv 1\pmod{q_j},\qquad e_j\equiv0\pmod{q_i}\quad(i\ne j).
\]
Set \(P_j=e_j(A)\). The congruences show
\[
\sum_jP_j=I,\quad P_j^2=P_j,\quad P_iP_j=0\ (i\ne j),\quad AP_j=P_jA.
\]
Moreover \(\operatorname{im}P_j=\ker q_j(A)=\ker(A-\lambda_j I)^{r_j}\). For the inclusion from left to right, use \(q_jP_j=0\) modulo \(m_A\). For the opposite inclusion, \(e_j=1+q_jh\), so \(e_j(A)v=v\) when \(q_j(A)v=0\). Hence
\[
V=\bigoplus_{j=1}^s \ker(A-\lambda_jI)^{r_j}.
\]
A constructive Bézout recipe takes \(M_j=m_A/q_j\), finds \(u_jM_j\equiv1\pmod{q_j}\) by the extended Euclidean algorithm, and sets \(e_j=u_jM_j\) modulo \(m_A\).

**Exact example.** For
\[
A=\begin{pmatrix}2&1&0\\0&2&0\\0&0&3\end{pmatrix},\quad m_A(t)=(t-2)^2(t-3),
\]
set \(P_3=(A-2I)^2=\operatorname{diag}(0,0,1)\) and \(P_2=I-P_3=\operatorname{diag}(1,1,0)\). The labels denote the eigenvalues, not the matrix sizes.

**Hermite polynomial calculus.** On \(J_r(\lambda)=\lambda I+N\), \(N^r=0\), and for a polynomial \(f\),
\[
f(J_r(\lambda))=\sum_{k=0}^{r-1}\frac{f^{(k)}(\lambda)}{k!}N^k.
\]
For several eigenvalues, Hermite interpolation produces a polynomial matching these derivatives modulo each \((t-\lambda_j)^{r_j}\). For a function holomorphic in neighborhoods of the spectrum, this equals the usual analytic matrix calculus. Values alone suffice for diagonalizable matrices, but not for defective matrices. Do **not** infer a general continuous functional calculus for nonnormal matrices from values on the spectrum alone.

### Problems with answers

1. For \(A=\operatorname{diag}(2,3)\), find polynomial projectors. **Answer:** \(P_2=3I-A\) and \(P_3=A-2I\).
2. Why does \(P^2=P\) imply \(\operatorname{im}P\cap\ker P=\{0\}\)? **Answer:** if \(x=Py\) and \(Px=0\), then \(x=P^2y=Px=0\).
3. For \(A=\begin{psmallmatrix}2&1\\0&2\end{psmallmatrix}\), what is \(f(A)\) when \(f(t)=t^3\)? **Answer:** \(\begin{psmallmatrix}8&12\\0&8\end{psmallmatrix}\), from \(f(2)=8\), \(f'(2)=12\).
4. Are polynomial spectral projections always orthogonal? **Answer:** no; that conclusion requires additional normal/self-adjoint structure and an inner product.

### Source anchors and routes onward

- Sheldon Axler, [*Linear Algebra Done Right*](https://linear.axler.net/), generalized eigenspace decomposition, characteristic and minimal polynomials.
- Jim Hefferon, [*Linear Algebra*](https://hefferon.net/linearalgebra/), similarity and eigenspace constructions.
- [Primary decomposition theorem](https://en.wikipedia.org/wiki/Primary_decomposition_theorem), [Chinese remainder theorem](https://en.wikipedia.org/wiki/Chinese_remainder_theorem), and [spectral projection](https://en.wikipedia.org/wiki/Spectral_projection), for supplementary terminology.

For subsequent study: `analysis:046000` treats continuous/Borel and holomorphic calculi with operator hypotheses; `g3:004500` treats two projections geometrically. These are different constructions, even when the language overlaps.
