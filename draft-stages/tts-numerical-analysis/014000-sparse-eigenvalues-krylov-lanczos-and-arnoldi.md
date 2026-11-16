# 014000 — Sparse Eigenvalue Problems: Krylov Spaces, Lanczos, and Arnoldi

**Track:** Numerical Analysis and Reliable Computation. **Background:** matrix-vector products, eigenvalues, orthogonal projections, iterative linear solvers. **Central question:** how can we approximate important eigenvalues of a matrix too large to diagonalize, and what makes an approximation trustworthy?

<!-- BEGIN SPOKEN LECTURE -->

# Sparse Eigenvalue Problems: Krylov Spaces, Lanczos, and Arnoldi

Many scientific matrices are enormous. A grid with millions of points, a large graph, or a discretized partial differential equation may produce a matrix with millions of rows. But each row can contain only a few nonzero entries, because each point interacts directly with a small neighborhood.

Computing a complete dense eigenvalue decomposition would destroy that advantage. It could require far too much memory and arithmetic. Often we need only a handful of eigenvalues: perhaps the largest eigenvalue, a small cluster near zero, or the modes responsible for instability. Krylov subspace algorithms approach this task using matrix-vector products rather than the full dense matrix.

## Start with the power method

Take a matrix A and a starting vector v. Multiply by A, normalize, and repeat. Under appropriate assumptions, the direction of the iterates approaches an eigenvector corresponding to an eigenvalue of largest magnitude.

For example, let A be diagonal with entries nine, four, and one, and start with a vector whose three components are all one. After one multiplication the components become nine, four, and one. After another they become eighty-one, sixteen, and one. The direction increasingly favors the first coordinate. The ratio between the dominant and next-largest magnitudes controls how quickly this happens.

The method has limitations. If the starting vector has no component in the dominant eigendirection, it cannot discover it in exact arithmetic. If eigenvalues of equal maximal magnitude compete, the normalized sequence may not converge to one direction. And the power method preferentially finds large-magnitude eigenvalues, not whichever eigenvalue happens to be scientifically interesting.

## Keep the subspace instead of one vector

Rather than discard previous information after each multiplication, collect the vectors v, A times v, A squared times v, and so on. Their span after k terms is the k-th Krylov subspace.

Every vector in this subspace is a polynomial in A applied to the starting vector, with polynomial degree less than k. This observation connects the eigenvalue problem to polynomial approximation. By choosing different polynomials implicitly, the algorithm can emphasize useful parts of the spectrum and suppress others.

But the raw powers are a poor numerical basis. The columns quickly become nearly parallel when one spectral component dominates. The resulting basis can be extremely ill-conditioned. We therefore orthogonalize as we construct the subspace.

## Arnoldi orthogonalization

Arnoldi's method constructs an orthonormal basis q one through q k for the Krylov subspace. At each step it multiplies the newest basis vector by A, subtracts components in all the current basis directions, and normalizes the remaining component if it is nonzero.

The inner products used in those subtractions form a small upper-Hessenberg matrix H. It represents the action of A after projecting back into the current subspace. Instead of solving a huge eigenvalue problem, we solve a small one involving H.

The approximate eigenvalues of H are called Ritz values. If y is an eigenvector of H with Ritz value theta, multiply the Arnoldi basis matrix Q by y. The result is a candidate eigenvector of A. The hope is that A acting on that candidate approximately multiplies it by theta.

This is a projection method, not a mysterious transformation of the original matrix. It chooses a restricted subspace, demands that the residual be orthogonal to that subspace, and solves the resulting small problem.

## Why symmetry makes Lanczos cheaper

If A is real symmetric, or complex Hermitian, the orthogonality structure becomes simpler. The Hessenberg matrix collapses to a symmetric tridiagonal matrix. In exact arithmetic, each new Lanczos basis vector can be generated using only the current and previous basis vectors, together with a new multiplication by A.

That short recurrence saves work and makes Lanczos especially attractive for large sparse Hermitian eigenproblems. But its ideal behavior assumes exact orthogonality. In floating-point arithmetic, the computed vectors can lose orthogonality, producing repeated or ghost Ritz values. Reorthogonalization, selective orthogonalization, and restarted variants are practical responses.

Arnoldi is more general and handles nonsymmetric matrices, including cases with complex eigenvalues, but maintaining an orthonormal basis generally costs more storage and inner products as the subspace grows. This is an important algorithmic tradeoff, not simply a preference between two implementations.

## An exact small example

Take the two-by-two diagonal matrix with eigenvalues two and five. Start with the unit vector whose components are equal. Restrict to the one-dimensional subspace spanned by that vector. The Rayleigh quotient, its estimated eigenvalue, is the average of two and five: three and one-half.

Apply the original matrix to the vector and subtract three and one-half times the vector. The residual has magnitude one and one-half. That is not a small error, because our single trial direction mixes both eigenspaces equally.

Expand the Krylov subspace to include the matrix applied to the starting vector. These two vectors are linearly independent, so their span is the entire two-dimensional space. With exact arithmetic, the second Ritz calculation recovers the eigenvalues two and five exactly.

This toy example captures the mechanism. As the Krylov subspace expands, it gains directions that resolve the action of A. The small projected problem becomes more informative about the actual spectrum.

## Residuals are the first credibility check

An approximate eigenpair consists of a scalar theta and a nonzero vector v. Its residual is A times v minus theta times v. A small residual says the pair almost satisfies the eigenvalue equation.

For a symmetric or Hermitian A, there is a particularly clear theorem: if v has unit norm, at least one true eigenvalue of A lies within the residual norm of theta. The proof follows by expanding v in an orthonormal eigenbasis. If every eigenvalue were farther from theta than that residual norm, the squared residual would have to be larger than it actually is.

This is a rigorous absolute eigenvalue enclosure when the residual norm is itself computed or enclosed reliably. But it does not necessarily identify *which* eigenvalue is nearby, and it does not certify that the corresponding eigenvector is accurate. Eigenvector error bounds need additional information, such as a spectral gap. For nonsymmetric matrices, nonnormality can make a small residual much less informative about the spectrum.

For Arnoldi, the residual can be estimated cheaply from the last recurrence coefficient and the final component of the Ritz vector in the projected basis. In finite precision, it remains sensible to evaluate a candidate's residual directly against the original matrix, especially when orthogonality has degraded.

## Finding eigenvalues near a chosen location

Standard Krylov iterations often favor extremal parts of the spectrum. To find an interior eigenvalue near a target sigma, a common technique is shift-and-invert. Instead of multiplying by A, apply the inverse of A minus sigma times the identity. Eigenvalues near sigma are transformed into eigenvalues of large magnitude, making them easier for power-like methods to capture.

The price is that every iteration now requires solving a linear system. If the matrix is sparse and a factorization can be reused, this may be worthwhile. But a difficult or poorly conditioned shifted solve can dominate the computation. The method is not a free shortcut, and the chosen shift must avoid a singular system or be handled with appropriate methods.

## When the computation is finished

A reliable sparse eigensolver should report what it actually established: the Ritz value, an approximate eigenvector, residual information, and assumptions under which residuals imply spectral error. It should also distinguish matrix approximation error from discretization error. If A came from a PDE, a certified eigenvalue of A is not automatically a certified eigenvalue of the continuous differential operator.

Krylov algorithms are powerful because they use the matrix in the form we can afford: as an operation on vectors. Arnoldi builds a general projected problem; Lanczos exploits Hermitian symmetry for a shorter recurrence; Rayleigh–Ritz turns the projection into candidate eigenpairs. Residual analysis turns those candidates into defensible numerical claims.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For \(A\in\mathbb C^{n\times n}\), \(v\ne0\), the \(k\)-th Krylov subspace is
\[\mathcal K_k(A,v)=\operatorname{span}\{v,Av,\ldots,A^{k-1}v\}.\]
Arnoldi constructs an orthonormal \(Q_k\) and Hessenberg \(H_k=Q_k^*AQ_k\) with the recurrence
\[AQ_k=Q_kH_k+h_{k+1,k}q_{k+1}e_k^*.\]
For an eigenpair \(H_ky=\theta y\), \(\|y\|=1\), the Ritz vector \(z=Q_ky\) has residual
\[r=Az-\theta z=h_{k+1,k}(e_k^*y)q_{k+1},\qquad \|r\|=|h_{k+1,k}e_k^*y|\]
in exact arithmetic. For Hermitian \(A\), Lanczos produces a real symmetric tridiagonal \(H_k\); finite precision may require reorthogonalization.

**Hermitian residual theorem:** \(\operatorname{dist}(\theta,\sigma(A))\le\|Az-\theta z\|/\|z\|\). Proof: if \(A=U\operatorname{diag}(\lambda_i)U^*\), then \(\|r\|^2=\sum_i|\lambda_i-\theta|^2|\langle u_i,z\rangle|^2\ge \operatorname{dist}(\theta,\sigma(A))^2\|z\|^2\).

**Two-dimensional example:** \(A=\operatorname{diag}(2,5)\), \(q_1=(1,1)/\sqrt2\), \(\theta=q_1^*Aq_1=7/2\), \(\|Aq_1-\theta q_1\|=3/2\). At \(k=2\), the Krylov subspace is all \(\mathbb R^2\), so both Ritz values are exact. For shift-and-invert, \(B=(A-\sigma I)^{-1}\) (when invertible) has eigenvalues \((\lambda_i-\sigma)^{-1}\); each action of \(B\) requires a solve.

### Exercises with answers

1. What operation must an efficient sparse Arnoldi iteration support? **Answer:** repeated matrix-vector products with \(A\), plus orthogonalization.
2. Why is the unorthogonalized power basis often numerically bad? **Answer:** repeated powers can become nearly linearly dependent as dominant modes overwhelm others.
3. For Hermitian \(A\) and a unit Ritz vector with residual norm \(10^{-6}\), what is certified in exact residual arithmetic? **Answer:** at least one eigenvalue lies within \(10^{-6}\) of the Ritz value, not necessarily a specified indexed eigenvalue.
4. What new work does shift-and-invert introduce? **Answer:** repeated linear solves involving \(A-\sigma I\); a sparse matrix-vector product alone no longer suffices.

### Reading and source notes

- David Bindel, [Cornell CS 6210: Lanczos and Arnoldi](https://www.cs.cornell.edu/courses/cs6210/2025fa/lec/2025-11-17.html), Krylov subspaces and recurrences.
- David Bindel, [Cornell CS 6210: Large-scale eigensolvers](https://www.cs.cornell.edu/courses/cs6210/2025fa/lec/2025-12-01.html), Rayleigh–Ritz and residuals.
- ETH Zurich, [Lecture Notes on Solving Large Scale Eigenvalue Problems](https://people.inf.ethz.ch/arbenz/ewp/Lnotes/lsevp.pdf), Arnoldi and Lanczos algorithms.
