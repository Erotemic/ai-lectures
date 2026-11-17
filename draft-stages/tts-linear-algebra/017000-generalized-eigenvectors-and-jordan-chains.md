# Beyond Ordinary Eigenvectors: Jordan Chains and Generalized Eigenspaces

**Track:** Linear Algebra from First Principles. **Background:** kernels, bases, eigenvalues, characteristic and minimal polynomials. **Purpose:** explain defective matrices from transformations rather than from a normal-form recipe.

<!-- BEGIN SPOKEN LECTURE -->

# Beyond Ordinary Eigenvectors: Jordan Chains and Generalized Eigenspaces

A diagonal matrix is easy to understand. Each coordinate evolves independently. We can raise the matrix to a power by raising each diagonal entry to that power, and we can solve a linear differential equation by treating each coordinate separately. The natural ambition is to find a basis in which every linear transformation looks diagonal.

That ambition is too strong. There are matrices with repeated eigenvalues but too few eigenvectors to make a basis. One response is to say that these matrices are defective and move on. A more useful response is to ask what an almost-eigenvector does. It turns out that the apparent failure of diagonalization contains a precise structure we can use.

## A shear with only one eigenvector

Consider the transformation of the plane with matrix whose first row is two, one, and whose second row is zero, two. It doubles both coordinates, but it also sends some of the second coordinate into the first. The horizontal unit vector is an eigenvector with eigenvalue two. What about a vector with nonzero second coordinate? When we double that vector, the transformation adds an extra horizontal component. So no vector pointing away from the horizontal axis is an eigenvector.

The characteristic polynomial is the square of x minus two. Its only eigenvalue is two, counted twice. But the eigenspace is only one-dimensional. There is no second independent eigenvector. A similarity transformation cannot manufacture one; changing coordinates changes the matrix representation, not the number of independent vectors satisfying the eigenvector equation.

Write A as twice the identity plus N, where N has one in the upper-right entry and zero everywhere else. The horizontal basis vector, call it v, is killed by N. The vertical basis vector, call it w, is not killed immediately; N sends w to v. Applying N once more kills v. Thus w does not satisfy the ordinary eigenvector equation, but it satisfies the equation obtained by applying A minus twice the identity twice.

This w is a generalized eigenvector. It reveals where the missing direction went: not into an independent eigenmode, but into a direction that feeds an eigenmode one step later.

## Chains rather than isolated directions

A Jordan chain for an eigenvalue lambda is an ordered set of vectors with a simple pattern. The first vector is an ordinary eigenvector. Subtract lambda times the identity from A and apply the resulting map: it kills the first vector, sends the second vector to the first, sends the third to the second, and so on.

The two-vector chain in our shear example is v followed by w. These two vectors form a basis even though only one is an ordinary eigenvector. In that basis, the matrix has lambda on the diagonal and a one directly above it. That is a Jordan block of size two.

For a chain of length three, the action goes from the third vector to the second, from the second to the first, and from the first to zero, after subtracting lambda times the identity. The corresponding Jordan block has three copies of lambda on its diagonal, ones directly above the diagonal, and zeros elsewhere. The extra ones record how directions feed one another.

Why are the vectors in a single chain independent? Suppose the last vector is killed by the k-th power of A minus lambda I, but not by its preceding power. Call that difference operator N. Then the vectors obtained by applying N repeatedly, from N to the k minus one power of the last vector down to the last vector itself, form a chain. If we had a linear relation among them, applying a suitable highest power of N would isolate the coefficient of the vector farthest along the chain. That coefficient must be zero. Repeat to remove the other coefficients. The whole chain is independent.

This is the first reason Jordan chains help: they produce actual bases where ordinary eigenvectors do not.

## Kernels that grow reveal the hidden structure

We already know how to find an ordinary eigenspace: compute the kernel of A minus lambda times the identity. To see generalized eigenvectors, compute kernels of successive powers of the same matrix. The first kernel contains ordinary eigenvectors. The second may contain vectors sent into the first kernel. The third may contain vectors sent into the second. These kernels form an increasing chain of subspaces.

Because our vector space has finite dimension, their dimensions cannot increase forever. Once two successive kernels have equal dimension, the chain stabilizes. To understand why, suppose the kernel of N to the k-th power equals the kernel of N to the k plus one power. If a vector is killed by N to the k plus two power, then N applied to that vector is killed by N to the k plus one power and therefore by N to the k power. That means the original vector is killed by N to the k plus one power, which by assumption is the same as the k-th kernel. No new vectors appear.

For our shear, the first kernel has dimension one, and the second kernel has dimension two. There is one Jordan chain of length two. Now imagine a four-dimensional transformation that contains one chain of length three and another independent chain of length one, both for the same eigenvalue. The first kernel has dimension two because each chain supplies its first vector. The second has dimension three. The third has dimension four. The successive dimension increases are two, one, one.

These increases count how many chains are at least that long. The first increase counts all blocks. The second counts blocks of size at least two. The third counts blocks of size at least three. In this way we can recover the sizes of all Jordan blocks without guessing a basis. It is a proof-relevant invariant, not just a pictorial trick.

## Algebraic and geometric multiplicity

There are two ways an eigenvalue can be counted. Its algebraic multiplicity is the number of times it appears as a root of the characteristic polynomial, counting repetitions. Its geometric multiplicity is the dimension of its ordinary eigenspace. For the shear, these are two and one. For twice the identity on the plane, they are both two.

Over the complex numbers, the generalized eigenspace for lambda eventually has dimension equal to its algebraic multiplicity. Inside that generalized eigenspace, A looks like lambda times the identity plus a nilpotent map. Nilpotent means that some power of the map is zero. The geometric multiplicity counts Jordan blocks, while the algebraic multiplicity counts all vectors in all those blocks.

The minimal polynomial supplies a third measurement: the exponent of x minus lambda in the minimal polynomial is the size of the largest Jordan block for lambda. Our shear has one block of size two, and therefore a squared factor. Twice the identity has two blocks of size one, and therefore only a first-power factor in its minimal polynomial.

Notice how these pieces of information are complementary. The characteristic polynomial tells us how much generalized space belongs to an eigenvalue. The eigenspace dimension tells us how many independent chains begin there. The minimal polynomial tells us how long the longest chain can be. The growth of the successive kernels fills in the remaining block sizes.

## What Jordan form actually asserts

The Jordan form theorem says that every linear operator on a finite-dimensional complex vector space has a basis built from Jordan chains. In that basis, its matrix is a block diagonal array of Jordan blocks. The blocks can appear in different orders, but the collection of block sizes for each eigenvalue is fixed.

Why do we insist on complex numbers here? A polynomial with real coefficients may have no real roots. A real ninety-degree rotation has no real eigenvector and no real Jordan basis made of one-dimensional eigenvalue chains. We can complexify the space and find a complex Jordan form, or keep real coordinates and use two-dimensional blocks for complex-conjugate pairs. We must say which field we are using.

A useful way to understand the theorem without memorizing a long construction is to separate its two tasks. First divide the vector space into invariant generalized eigenspaces belonging to distinct eigenvalues. Then, within each generalized eigenspace, study the nilpotent remainder and organize it into chains. The first task comes from polynomial factorization. The second comes from the growing kernels we just studied. Neither task needs an inner product or an orthonormal basis.

The proof's general machinery is described in the companion. For understanding, it is worth asking at each stage what the invariant subspaces mean and how they are detected.

## Jordan blocks predict powers and time dependence

Let A be lambda times the identity plus N, and suppose N squared is zero. When we square A, we obtain lambda squared times the identity plus twice lambda N. When we take the tenth power, the binomial theorem gives lambda to the tenth power times the identity plus ten times lambda to the ninth power times N. This is a binomial expansion of commuting matrices: the identity and N always commute, and all terms containing N squared vanish.

For a longer Jordan chain, more terms survive, but still only finitely many. A block of length three produces terms involving the binomial coefficients for the first and second powers of N. This is the algebraic origin of polynomial factors multiplying the usual eigenvalue powers.

Continuous time has a parallel behavior. If we solve a differential equation governed by A, a block with eigenvalue lambda produces terms that look like the ordinary exponential of lambda times time, multiplied by polynomials in time. With a chain of length two, a factor of time appears. With a chain of length three, a factor of time squared can appear. The chain records a coupling that diagonalization would have missed.

In particular, knowing that all eigenvalues are negative is enough to guarantee eventual decay for a fixed finite-dimensional constant-coefficient system. But a nonnormal matrix can temporarily amplify some inputs before that decay becomes visible. Jordan chains make one mechanism of that transient growth explicit.

## A warning about numerical Jordan forms

Jordan form is exact algebra, but it is often a poor floating-point target. Perturb the lower-right diagonal entry in our shear by a tiny nonzero amount. Now the two eigenvalues are different, so the perturbed matrix is diagonalizable. However, its eigenvectors can be nearly parallel, and the change-of-basis matrix can be terribly ill-conditioned. As the perturbation tends to zero, the diagonalizable matrices approach the defective one.

This is not a paradox. The exact question 'is there a Jordan block?' can have a discontinuous answer under perturbation. A numerical algorithm that must cope with rounded data should often use a Schur decomposition, invariant subspaces, or another stable representation instead of trying to decide the exact block structure of noisy inputs.

Jordan theory answers a structural question: what can every finite-dimensional linear transformation look like after a suitable change of basis? It gives us a language for failures of diagonalization, a method for understanding repeated eigenvalues, and a way to calculate powers and dynamics. It does not by itself provide a reliable numerical algorithm for detecting those structures from approximate coefficients.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Let \(N=A-\lambda I\). The **generalized eigenspace** is
\[
G_\lambda=\ker N^n=\bigcup_{k\ge1}\ker N^k
\]
for \(A\in M_n(\mathbb C)\). More economically, take the stabilized kernel. It is invariant under \(A\) because \(A\) commutes with \(N\).

A Jordan chain \(v_1,\ldots,v_r\) satisfies \(Nv_1=0\) and \(Nv_{j+1}=v_j\). Relative to this ordered basis, \(A\) is \(J_r(\lambda)=\lambda I+N_r\) with ones on the superdiagonal. These vectors are independent: applying \(N^{r-1}\) to a relation isolates the coefficient of \(v_r\), then apply \(N^{r-2}\), and continue.

**Kernel-growth formula.** Let \(d_k=\dim\ker N^k\), \(d_0=0\), for a nilpotent map \(N\). Then \(d_k-d_{k-1}\) equals the number of Jordan blocks of size at least \(k\). In particular, the number of blocks of size exactly \(k\) is \(2d_k-d_{k-1}-d_{k+1}\). Example: \(J_3(\lambda)\oplus J_1(\lambda)\) yields \((d_0,d_1,d_2,d_3,d_4)=(0,2,3,4,4)\); block counts are one of size three and one of size one.

**Three multiplicities.** For \(A\in M_n(\mathbb C)\), the algebraic multiplicity of \(\lambda\) equals \(\dim G_\lambda\). Its geometric multiplicity is \(\dim\ker(A-\lambda I)\), equal to the number of its Jordan blocks. The exponent of \((x-\lambda)\) in \(m_A(x)\) is the largest size among those blocks. The decomposition into \(G_\lambda\) can be derived from Bézout identities and coprime factors of the minimal polynomial, developed in the subsequent polynomial-projection lecture.

**Powers of a block:** for integer \(k\ge0\) and \(N^r=0\),
\[
(\lambda I+N)^k=\sum_{j=0}^{\min(k,r-1)}\binom{k}{j}\lambda^{k-j}N^j.
\]
The formula makes sense even when \(\lambda=0\), with the usual polynomial/binomial interpretation; avoid evaluating \(0^0\) as a floating-point operation.

For \(A_\varepsilon=\begin{pmatrix}2&1\\0&2+\varepsilon\end{pmatrix}\) with \(\varepsilon\ne0\), the eigenvectors can be \((1,0)^T\) and \((1,\varepsilon)^T\), and become parallel in the limit. Thus Jordan structure is not robust under perturbation.

### Problems with answers

1. Find a length-two Jordan chain for \(A=\begin{psmallmatrix}2&1\\0&2\end{psmallmatrix}\). **Answer:** \(v_1=(1,0)^T\), \(v_2=(0,1)^T\).
2. If a nilpotent four-by-four matrix has kernel dimensions \(1,2,3,4\) for its first four powers, how many Jordan blocks and of what size? **Answer:** one block of size four.
3. If a four-by-four matrix has characteristic polynomial \((x-1)^4\) and minimal polynomial \((x-1)^2\), can it have a single Jordan block of size four? **Answer:** no; the largest block size must be two.
4. Why is a real ninety-degree rotation not diagonally representable over the real numbers? **Answer:** it has no real eigenvalues or nonzero real eigenvectors.

### Source anchors and routes onward

- Sheldon Axler, [*Linear Algebra Done Right*](https://linear.axler.net/), treatment of generalized eigenvectors, nilpotent operators, decomposition, and Jordan form.
- Gilbert Strang, [MIT OCW: Similar Matrices and Jordan Form](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/resources/lecture-28-similar-matrices-and-jordan-form/index.html).
- [Jordan normal form](https://en.wikipedia.org/wiki/Jordan_normal_form), for terminology and further references.

`linear-algebra:016000` is the algebraic starting point. Polynomial spectral projectors make the decomposition into generalized eigenspaces explicit; `linear-algebra:019000` then uses chains to compute matrix exponentials. Infinite-dimensional operators need separate domain, boundedness, and spectral hypotheses.
