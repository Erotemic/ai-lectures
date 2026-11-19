# Beyond Eigenvalue Lists: Nonnormality, Resolvents, and Pseudospectra

**Track:** Linear Algebra from First Principles. **Background:** eigenvalues, singular values, matrix inverses, matrix exponential, Schur form. **Purpose:** distinguish spectral location from sensitivity, derive pseudospectra from smallest singular values and perturbed eigenproblems, and explain transient growth in nonnormal dynamics.

<!-- BEGIN SPOKEN LECTURE -->

# Beyond Eigenvalue Lists: Nonnormality, Resolvents, and Pseudospectra

Suppose two matrices have exactly the same eigenvalues. Should we expect them to behave similarly? In some circumstances, yes. For normal matrices, an orthonormal eigenvector basis makes the answer remarkably clean. But for a nonnormal matrix, the eigenvalues may tell us much less about how vectors are stretched, how solutions to differential equations evolve over finite times, or how a small perturbation moves the spectrum.

This is more than a pathology of eigenvalue software. Many linearized dynamical systems and discretized differential operators are nonnormal. A triangular matrix with a large entry above the diagonal is enough to see the central issue. We will develop a way of describing not only where the eigenvalues are, but also where they could move under small changes to the matrix.

## Normality is a geometric condition

A complex matrix A is normal if A times its conjugate transpose equals its conjugate transpose times A. Real symmetric and complex Hermitian matrices are normal, and so are unitary matrices. The spectral theorem says that a normal matrix has an orthonormal eigenvector basis. In a suitable unitary basis, its action is just multiplication of independent coordinates by eigenvalues.

That orthogonality gives strong control. If A is normal and z is not an eigenvalue, then the norm of the inverse of z times the identity minus A is exactly the reciprocal of the distance from z to the nearest eigenvalue. Here norm means the Euclidean operator norm. The formula follows by expressing everything in the orthonormal eigenvector basis: the inverse simply divides each coordinate by z minus an eigenvalue.

For an arbitrary matrix, the distance to the spectrum need not control the inverse so precisely. It can be much larger. This is the first sign that the eigenvalue locations are insufficient.

## A matrix with no eigenvalues away from zero

Let A have first row zero, one hundred, and second row zero, zero. Its characteristic polynomial is lambda squared. Both eigenvalues are zero. Indeed, A squared is zero, so its only eigenvalue is zero and it has just one linearly independent eigenvector.

Nevertheless, A sends the second coordinate basis vector to one hundred times the first. Its Euclidean operator norm is one hundred, even though both eigenvalues vanish. Contrast it with the zero matrix, which has exactly the same eigenvalues but sends every vector to zero. A list of eigenvalues cannot distinguish these two actions.

This triangular matrix is nonnormal. Its one hundred in the upper-right position encodes a strong coupling between coordinate directions. The coupling cannot be removed by a unitary diagonalization. When we examined Schur form, we saw that an upper triangular matrix can retain entries above the diagonal. Now we see why those entries may have immediate quantitative consequences.

## A tiny change can move an eigenvalue surprisingly far

Perturb A by placing a tiny positive number, one ten-thousandth, in the lower-left position. Call this perturbation E. Its Euclidean operator norm is exactly one ten-thousandth. The new matrix has an upper-right entry of one hundred and a lower-left entry of one ten-thousandth.

Compute its characteristic polynomial. It is lambda squared minus one hundred times one ten-thousandth, or lambda squared minus one hundredth. The eigenvalues of A plus E are therefore positive one tenth and negative one tenth. A change in a matrix entry of size one ten-thousandth has moved both eigenvalues a distance of one tenth away from zero.

Compare this with the zero matrix. If we perturb zero by a matrix of norm one ten-thousandth, every new eigenvalue has magnitude at most one ten-thousandth. That follows because an eigenvalue cannot exceed the operator norm in magnitude. The difference is not that our arithmetic was poor. It is that the original triangular matrix has a highly sensitive spectrum.

This square-root relationship is characteristic of perturbing a defective two-by-two Jordan block. In our example, if the lower-left perturbation is delta and the upper-right entry is K, the new eigenvalues are positive and negative the square root of K times delta, for positive K and delta. That dependence is not linear in delta near zero. So we should not expect every eigenvalue of a defective matrix to vary with a small, uniformly bounded derivative under perturbation.

## The resolvent measures more than spectral distance

Introduce a complex number z that is not an eigenvalue of A. The inverse of z times the identity minus A is called the resolvent at z. It tells us how a response to the linear system z times x minus A x equals b changes with the forcing b. If the resolvent has a large norm, there is some forcing of unit size that produces a large response.

For our triangular example, the inverse can be written explicitly. Its diagonal entries are one divided by z. Its upper-right entry is one hundred divided by z squared. The lower-left entry remains zero. That second-order denominator is the algebraic signature of the nontrivial Jordan coupling.

Take z equal to one tenth. This is a full tenth of a unit away from the sole eigenvalue, zero. Yet the upper-right entry of the resolvent is ten thousand. A unit input along the second coordinate produces a response with a first component of ten thousand. Distance to eigenvalues alone did not warn us about that amplification.

The inverse becomes undefined at an eigenvalue, of course. But this example shows that large inverse norms are not restricted to points immediately next to the spectrum in the ordinary geometric sense. There can be a much wider region in the complex plane where the matrix behaves as if it were nearly singular.

## Define the pseudospectrum by singular values

We need a quantitative definition of 'nearly singular.' For a positive tolerance epsilon, the epsilon-pseudospectrum of A consists of all complex numbers z for which the smallest singular value of z times the identity minus A is less than epsilon. This includes the true eigenvalues, where the smallest singular value is zero.

Why singular values? The smallest singular value measures the least possible output norm when we feed a unit vector into a matrix. If that value is tiny, there is a unit direction almost annihilated by z times the identity minus A. In other words, there is a vector that behaves almost like an eigenvector with eigenvalue z, even if z is not actually an eigenvalue.

There is an equivalent perturbation interpretation. A number z belongs to the epsilon-pseudospectrum exactly when it is an eigenvalue of some matrix A plus E with E of operator norm less than epsilon. One direction is easy: if a nearby matrix has an eigenvector at z, then the corresponding vector for A has a small residual. For the other direction, take a unit singular vector that nearly vanishes under z times the identity minus A. A rank-one perturbation of size equal to that small singular value makes the residual vanish exactly.

Thus the pseudospectrum describes the eigenvalues that nearby matrices are capable of having. It does not say that every such eigenvalue will appear in a random perturbation, nor does it prescribe how a physical perturbation is distributed. It gives a worst-case sensitivity region at a stated perturbation scale.

Away from the exact spectrum, there is one more equivalent description. The smallest singular value of z times the identity minus A is the reciprocal of the resolvent norm. Therefore z is in the epsilon-pseudospectrum precisely when the resolvent norm exceeds one divided by epsilon. A large resolvent and a nearby perturbable eigenvalue are two views of the same phenomenon.

## How the normal and nonnormal pictures differ

For a normal matrix, the epsilon-pseudospectrum is exactly the union of open disks of radius epsilon around the eigenvalues. The orthonormal eigenvector basis prevents a small perturbation from moving the eigenvalues farther than its own norm. Here geometric distance, resolvent amplification, and spectral perturbation tolerance agree neatly.

For the nonnormal triangular example, the pseudospectrum bulges much farther from zero. A perturbation of norm one ten-thousandth can create eigenvalues at positive and negative one tenth. If we choose epsilon slightly larger than one ten-thousandth, both new values lie in that pseudospectrum, even though their distance to the original spectrum is one thousand times the size of the perturbation.

One way to understand the difference is eigenvector geometry. If A is diagonalizable, write it as V times a diagonal eigenvalue matrix times V inverse. Then the movement of eigenvalues under a perturbation can be bounded by a condition number of V multiplied by the perturbation norm. When V is unitary, this condition number is one. When its eigenvectors are nearly parallel, V can be poorly conditioned, and the bound becomes weak. A defective matrix does not even possess the required full eigenvector matrix, so this diagonalizable-matrix argument cannot apply.

The precise name for that perturbation estimate is the Bauer–Fike theorem. It illustrates how an assumption about eigenvectors, not merely eigenvalues, enters a reliable error guarantee.

## A small eigenpair residual proves something, but not everything

Suppose an algorithm returns a scalar mu and a unit vector v, claiming that A v is approximately mu v. We can compute the residual r equal to A v minus mu v. If that residual is small, we know the pair nearly satisfies the eigenvalue equation.

We can make that statement exact by defining a rank-one perturbation E that sends v to negative r and vanishes on vectors perpendicular to v. Then the norm of E equals the norm of r, and A plus E has v as an exact eigenvector with eigenvalue mu. So a small eigenpair residual is a backward-error certificate: it proves that the pair solves a nearby eigenvalue problem.

But it does not automatically prove that mu lies within the residual norm of the original spectrum. That stronger conclusion holds for normal matrices, because their pseudospectra are simple disks. For a strongly nonnormal matrix the original eigenvalues may be much farther away. A numerically computed eigenvalue can have an excellent backward error while its forward error, measured against a selected exact eigenvalue, is much larger.

This is why the norms of residuals, condition numbers of eigenspaces, and separation of eigenvalue clusters must be considered alongside a spectral plot. The residual certifies the problem the algorithm actually solved; sensitivity tells us how that nearby problem relates to the original one.

## Why eigenvalues can predict long-time decay but miss transient growth

Now shift our triangular example so both eigenvalues become negative one. Take the matrix with diagonal entries negative one and an upper-right entry of one hundred. Both eigenvalues are negative. The linear differential equation x prime equals A x is asymptotically stable: every solution tends to zero as time grows.

Yet the matrix exponential tells a richer story. Because the nilpotent upper-right part squares to zero and commutes with the negative identity, the exponential is e to the negative t times the matrix with diagonal entries one and upper-right entry one hundred t. At time one, a unit vector initially in the second coordinate has become e to the negative one times the vector one hundred, one. Its length is more than thirty-six, although it began with length one and the eigenvalues both predict eventual decay.

There is no contradiction. Eigenvalues describe the exponential rates of asymptotic modes, but a nonnormal matrix can combine modes in a way that causes substantial temporary amplification. After enough time, the decaying exponential overwhelms the linear factor and the solution tends to zero. A bound based only on the real parts of eigenvalues misses the amplitude of that transient.

Such transient amplification matters when disturbances, nonlinear effects, or numerical errors are large enough to activate behavior that an asymptotic eigenvalue calculation alone might overlook. The precise application requires its own model; the finite-dimensional calculation already explains the mathematical possibility.

## The bridge toward advanced spectral theory

We now have three different objects to keep distinct. The spectrum is the exact set of eigenvalues. Schur form is a stable representation of a matrix that exposes invariant subspaces without requiring a fragile Jordan classification. The pseudospectrum records where eigenvalues can appear under norm-bounded perturbations, equivalently where resolvents are large.

For Hermitian and other normal matrices, these descriptions fit together particularly well. This is part of why self-adjoint spectral theory has strong perturbation bounds and clean orthogonal projection geometry. For nonnormal operators, the off-diagonal structure and resolvent behavior cannot be omitted. And when we move from matrices to infinite-dimensional operators, domain questions, continuous spectrum, and different notions of resolvent require new care.

Eigenvalues remain essential. They are simply not the whole story. Knowing when they are sufficient, and when they are not, is one of the foundational skills needed to approach numerical spectral theory and operator perturbation results with confidence.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

### Spectrum, resolvent and pseudospectrum

For \(A\in\mathbb C^{n\times n}\), \(z\notin\sigma(A)\), and \(\varepsilon>0\):
\[
R(z,A)=(zI-A)^{-1},\qquad
\sigma_\varepsilon(A)=\{z\in\mathbb C:\sigma_{\min}(zI-A)<\varepsilon\}.
\]
Equivalent, with a strict threshold:
\[
\sigma_\varepsilon(A)=\{z:\text{there is }E\text{ with }\|E\|_2<\varepsilon
\text{ and }z\in\sigma(A+E)\}.
\]
For \(z\notin\sigma(A)\), \(\sigma_{\min}(zI-A)=1/\|R(z,A)\|_2\), so \(z\in\sigma_\varepsilon(A)\) iff \(\|R(z,A)\|_2>1/\varepsilon\). For a normal A, \(\sigma_\varepsilon(A)=\bigcup_{\lambda\in\sigma(A)}\{z:|z-\lambda|<\varepsilon\}\).

**Proof of the perturbation equivalence.** Choose unit right and left singular vectors \(v,u\) of \(zI-A\) with \((zI-A)v=s u\), \(s=\sigma_{\min}(zI-A)\). Put \(E=suv^*\). Then \(\|E\|_2=s\), and \((A+E)v=zv\). Conversely, if \((A+E)v=zv\), \(\|v\|=1\), then \(\|(zI-A)v\|=\|Ev\|\le\|E\|_2\), hence \(\sigma_{\min}\le\|E\|_2\).

### A defective example with square-root eigenvalue motion

\[
A=\begin{bmatrix}0&K\\0&0\end{bmatrix},\quad
E=\begin{bmatrix}0&0\\\delta&0\end{bmatrix},\quad
\|E\|_2=|\delta|,\quad
\sigma(A+E)=\{\pm\sqrt{K\delta}\}\quad(K,\delta>0).
\]
With \(K=100\), \(\delta=10^{-4}\): original eigenvalues \(0,0\); perturbed eigenvalues \(\pm0.1\). For \(z\ne0\),
\[
(zI-A)^{-1}=\begin{bmatrix}1/z&K/z^2\\0&1/z\end{bmatrix},
\qquad \|(zI-A)^{-1}\|_2\ge |K/z^2|.
\]
At \(z=0.1\), the resolvent norm is at least \(10^4\) though \(\operatorname{dist}(z,\sigma(A))=0.1\).

### Eigenpair residuals and Bauer–Fike

For \(\|v\|_2=1\), \(r=Av-\mu v\), define \(E=-rv^*\). Then \((A+E)v=\mu v\) and \(\|E\|_2=\|r\|_2\). Thus a residual is a backward-error certificate. It need not imply \(\operatorname{dist}(\mu,\sigma(A))\le\|r\|_2\) for a nonnormal A.

If \(A=V\Lambda V^{-1}\) is diagonalizable, **Bauer–Fike** states for every eigenvalue \(\mu\in\sigma(A+E)\),
\[
\min_{\lambda\in\sigma(A)}|\mu-\lambda|\le \kappa_2(V)\|E\|_2.
\]
The factor \(\kappa_2(V)\) is exactly 1 for unitary V (normal A). This inequality alone does not provide a unique matching between perturbed and unperturbed eigenvalues when disks overlap.

### Transient growth with stable eigenvalues

For \(B=-I+N\), \(N=\begin{bmatrix}0&K\\0&0\end{bmatrix}\), \(N^2=0\):
\[
e^{tB}=e^{-t}(I+tN)=e^{-t}\begin{bmatrix}1&Kt\\0&1\end{bmatrix}.
\]
Both eigenvalues of B equal \(-1\), yet \(\|e^Be_2\|_2=e^{-1}\sqrt{K^2+1}\), which exceeds 36 for \(K=100\). The solution still decays as \(t\to\infty\), since \(t e^{-t}\to0\).

### Exercises with answers

1. **Normal matrix:** For \(D=\operatorname{diag}(1,4)\), give \(\sigma_{0.2}(D)\). **Answer:** open disks of radius 0.2 centered at 1 and 4 in the complex plane.
2. **Resolvent:** Compute \(R(z,A)\) for \(A=\begin{bmatrix}0&K\\0&0\end{bmatrix}\). **Answer:** \(\begin{bmatrix}1/z&K/z^2\\0&1/z\end{bmatrix}\) for \(z\ne0\).
3. **Sensitivity:** If \(K=9\) and \(\delta=10^{-4}\), what are the perturbed eigenvalues? **Answer:** \(\pm0.03\).
4. **Residual certificate:** Show the rank-one E constructed from \(r=Av-\mu v\) has norm \(\|r\|_2\). **Answer:** \(\|rv^*\|_2=\|r\|_2\|v\|_2=\|r\|_2\).
5. **Transient:** How can \(e^{tB}\) initially amplify a vector if its eigenvalues all have negative real part? **Answer:** nonorthogonal/nilpotent coupling produces a polynomial transient factor \(t\) before the exponential decay dominates.

### Sources and reading

- Lloyd N. Trefethen and Mark Embree, [*Spectra and Pseudospectra: The Behavior of Nonnormal Matrices and Operators*](https://press.princeton.edu/books/hardcover/9780691119465/spectra-and-pseudospectra), Princeton University Press (2005), for resolvent norms, eigenvalue sensitivity, and transient effects.
- Lloyd N. Trefethen and David Bau III, [*Numerical Linear Algebra*](https://people.maths.ox.ac.uk/trefethen/text.html), for eigenvalue conditioning, Schur form and numerical residuals.
- Nicholas J. Higham, [*Accuracy and Stability of Numerical Algorithms*](https://nhigham.com/accuracy-and-stability-of-numerical-algorithms/), for backward-error interpretation.
- Wikipedia topic pointers: [Pseudospectrum](https://en.wikipedia.org/wiki/Pseudospectrum), [Normal matrix](https://en.wikipedia.org/wiki/Normal_matrix), [Resolvent formalism](https://en.wikipedia.org/wiki/Resolvent_formalism), [Bauer–Fike theorem](https://en.wikipedia.org/wiki/Bauer%E2%80%93Fike_theorem).

Read `linear-algebra:018000` for exact spectral projectors, `linear-algebra:019000` for matrix exponentials, and `linear-algebra:026000` for Schur form. The advanced spectral-perturbation results for self-adjoint operators require their own hypotheses; these finite-dimensional examples do not extend them unqualified to arbitrary bounded or unbounded operators.
