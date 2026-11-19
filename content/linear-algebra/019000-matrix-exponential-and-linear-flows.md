# From Repeated Steps to Continuous Motion: The Matrix Exponential

**Track:** Linear Algebra from First Principles. **Background:** matrix powers, ordinary exponential and its power series, eigenvalues, and a first derivative. **Purpose:** connect finite-dimensional operator algebra to linear differential equations and semigroups.

<!-- BEGIN SPOKEN LECTURE -->

# From Repeated Steps to Continuous Motion

A matrix can describe one discrete step of a process. A population moves from one age group to another, a vector is transformed by a graphics operation, or a state is updated by a numerical algorithm. Repeating the process means taking powers of the matrix.

But many physical systems change continuously. A temperature distribution evolves every instant. A spring oscillates without waiting for a clock tick. A chemical reaction proceeds at a rate determined by its current state. In the simplest linear model, the rate of change of a vector is a fixed matrix applied to that vector. We write this as the derivative of x with respect to time equals A times x.

For a single scalar equation, the solution is an exponential. Does a matrix have an exponential? And if so, can it still work when the matrix cannot be diagonalized?

## Rebuild the scalar exponential from what it does

Start with the scalar differential equation: the rate of change of x equals a times x. If we start at x zero, the solution at time t is x zero times the exponential of a times t. The exponential has three properties worth remembering. At time zero it is one. Its derivative is itself multiplied by a. And evolving for time s and then for time t is the same as evolving once for time s plus t.

We want a matrix-valued function with the same properties, except that the identity matrix replaces the number one. A natural guess comes from the familiar power series for the exponential. Replace the scalar quantity a times t with the matrix A times t. Begin with the identity matrix, add t times A, add t squared times A squared divided by two, and continue with all higher powers divided by factorials.

Why should that infinite series make sense? For any fixed finite matrix A, choose a compatible matrix norm. The norm of A to the k-th power is at most the norm of A raised to the k-th power. So the norms of the matrix-series terms are bounded by the corresponding scalar exponential series with argument the absolute value of t times the norm of A. That scalar series converges. Hence the matrix series converges absolutely, uniformly on bounded time intervals, and we may differentiate it term by term.

The derivative is A times the same series. At time zero all terms except the identity vanish. We call this function the matrix exponential, written as the exponential of t times A.

This definition has not used any eigenvectors. It works equally well for diagonal, triangular, defective, real, and complex matrices.

## Why it really solves the differential equation

Take any initial vector x zero and multiply it by the matrix exponential. Differentiate with respect to time. Since the derivative of the exponential is A times the exponential, the resulting vector's derivative equals A times the vector itself. At time zero, the exponential is the identity, so the starting condition is satisfied. We have constructed a solution.

But is it the only solution? There is a short argument that explains the special role of the exponential. Suppose x of t is any differentiable solution of the same equation. Multiply it by the exponential of minus t times A and call the result y of t. Differentiate using the product rule. One term gives minus A times the inverse exponential applied to x. The other gives the inverse exponential applied to A times x. These cancel because A commutes with every power of itself, and hence with its exponential. Therefore y has derivative zero. It stays equal to the original initial vector. Multiply back, and x must be the exponential of tA applied to x zero.

The same reasoning proves that evolution over adjacent time intervals composes. The exponential of sA times the exponential of tA equals the exponential of their sum, s plus t, times A. One proof multiplies the two power series and uses the binomial theorem; it works because both series involve the same matrix. The inverse of the exponential of tA is the exponential of minus tA.

These properties describe a one-parameter group of invertible linear maps. In more general evolution problems, especially irreversible ones such as diffusion on function spaces, the forward-time maps may form a semigroup rather than a group of bounded invertible operators. The finite-dimensional matrix case is a starting model, not the whole theory.

## Diagonal matrices are easy; Jordan blocks explain the rest

For a diagonal matrix, each power remains diagonal, so the exponential simply applies the scalar exponential to every diagonal entry. This gives independent growth or decay in the separate coordinate directions. If A has a basis of eigenvectors, we may change to that basis, exponentiate the diagonal matrix, and change back.

For the two-by-two shear with both diagonal entries equal to two and one in the upper-right corner, diagonalization is impossible. Write A as twice the identity plus N, with N squared equal to zero. The identity and N commute, so we can separate their exponentials. The exponential of twice t times the identity is just the scalar exponential of two t times the identity. The exponential of tN is only the identity plus tN, because every higher power of N vanishes.

The answer is therefore the scalar exponential of two t multiplied by a matrix with ones on the diagonal and t in the upper-right corner. Applying it to an initial vertical vector produces a horizontal component proportional to time times that exponential. That factor of time is the signature of a length-two Jordan chain.

For a chain of length three, we also get a term involving time squared divided by two. More generally, a Jordan block of length r contributes the exponential of its eigenvalue times time multiplied by a polynomial in time of degree at most r minus one. This is a complete description of the finite-dimensional constant-coefficient case over the complex numbers.

Notice a conceptual distinction. The eigenvalue determines the principal exponential growth or decay rate. The nilpotent part describes coupling between generalized eigenvectors and contributes the polynomial factors. Both are needed to predict the actual motion.

## Rotation and oscillation without real eigenvectors

Take the two-by-two matrix with first row zero, minus omega and second row omega, zero. This is the infinitesimal generator of rotation in the plane. Its square is minus omega squared times the identity. Consequently its even powers contribute the cosine series, while its odd powers contribute the sine series.

When we regroup the matrix exponential into those even and odd terms, we obtain a rotation matrix through angle omega times t. Its entries are cosine, minus sine, sine, cosine. If omega is positive, increasing time rotates counterclockwise; if omega is negative, it rotates clockwise.

This example is important because the real matrix has no real eigenvectors when omega is nonzero. Yet its exponential is perfectly real, and the calculation is straightforward. Complex eigenvalues can be useful bookkeeping for oscillation, but the real dynamics do not depend on pretending that complex eigenvectors are physical directions in the real plane.

We can now solve linear oscillators in two equivalent ways. We may write a second-order scalar equation as a first-order system and calculate its matrix exponential. Or we may use the familiar sine and cosine solutions. The matrix formulation packages both position and velocity, and the same method extends to coupled oscillators.

## Stable eigenvalues do not forbid transient growth

Consider a matrix with minus one on both diagonal entries and ten in its upper-right entry. Its only eigenvalue is minus one. One might guess that every initial state immediately shrinks, since the corresponding scalar exponential decays.

But the matrix has a strong shear. Its exponential is the scalar exponential of minus t times a matrix whose diagonal entries are one and whose upper-right entry is ten t. Start with the vertical unit vector. At time one, its image has first coordinate ten divided by e and second coordinate one divided by e. Its Euclidean length is greater than three, even though its length at time zero was one.

Eventually the exponential decay wins over the linear factor of time, and every solution tends to zero. There is no contradiction. 'The solution tends to zero as time grows' and 'the solution's norm decreases at every instant' are different claims.

In finite dimensions with constant coefficients, all eigenvalues having strictly negative real parts implies eventual decay of every solution. For normal matrices measured in the Euclidean norm, the geometry is much simpler: orthogonal eigenmodes eliminate this kind of shear-driven transient amplification. For nonnormal matrices, eigenvalues alone do not give a sharp bound on the intermediate growth of the evolution operator.

This matters in control theory, hydrodynamic stability, numerical discretizations, and any problem where a large temporary amplification can cause failure before the asymptotic regime arrives.

## Forces that vary with time

So far the differential equation was homogeneous: the derivative equals A times the state. Add an external forcing term b of t. The equation becomes the derivative of x equals A times x plus b of t.

The solution separates the effect of the initial condition from the accumulated effect of the forcing. The initial condition evolves under the matrix exponential. Each small impulse applied at an earlier time s is carried forward to the present time t by the exponential of A times the elapsed interval, t minus s. Integrate these transported impulses from the initial time to the present. This is the variation-of-constants formula, also called Duhamel's formula in many settings.

We can verify it by differentiating. The upper endpoint contributes the current forcing. Differentiating the exponential inside the integral contributes A times the accumulated response. Together with the homogeneous part, we recover the original differential equation.

This perspective extends beyond a neat formula. It tells us that the matrix exponential is a propagator: the operator that transports information from an earlier time to a later one. When we later study partial differential equations, semigroups of operators will play an analogous role, although their generators may be unbounded and require domain analysis.

## Why matrix exponentials cannot always be combined

Scalar exponentials satisfy the rule that the exponential of a plus b is the exponential of a times the exponential of b. For matrices, the analogous identity is generally false when the matrices do not commute. The product of two different matrix exponentials need not equal the exponential of their sum.

Imagine first evolving under one matrix for one unit of time and then under a second matrix for one unit. The resulting transformation is the exponential of the second matrix multiplied by the exponential of the first. Reverse the order, and the result may change. We can construct this explicitly with two matrices, each of which squares to zero: one sends the vertical direction horizontally, and the other sends the horizontal direction vertically. Each exponential is just the identity plus that matrix, but their two products differ because their cross-products differ.

This warning becomes crucial if the governing matrix itself changes over time. Writing the exponential of the integral of the matrix usually misses the order in which the transformations act. Such a formula works under suitable commutativity conditions, not automatically. General time-dependent systems need a time-ordered evolution construction.

## Exact formulas and reliable computation are separate tasks

The infinite series defines the matrix exponential and proves its fundamental properties, but summing many terms naively is not always the best numerical procedure. For real computations, algorithms may use scaling and squaring together with rational approximations, or exploit sparse structure and Krylov subspaces when only the action on a vector is needed. Eigenvector formulas may be ill-conditioned near defective matrices even when the exponential itself changes smoothly with the entries.

We have moved from repeated discrete steps to continuous motion without abandoning finite-dimensional algebra. Matrix powers, annihilating polynomials, Jordan chains, and spectral projectors all feed into a single construction. The exponential is a precise bridge: on one side stand ordinary matrices and eigenvectors; on the other stand differential equations, operator semigroups, stability analysis, and functional calculus.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For \(A\in M_n(\mathbb C)\) and \(t\in\mathbb R\),
\[
e^{tA}=\sum_{k=0}^{\infty}\frac{t^kA^k}{k!},\qquad \|t^kA^k/k!\|\le |t|^k\|A\|^k/k!.
\]
Uniform convergence of the series of derivatives on compact time intervals yields
\[
\frac{d}{dt}e^{tA}=Ae^{tA}=e^{tA}A,\quad e^{0A}=I,\quad e^{sA}e^{tA}=e^{(s+t)A},\quad(e^{tA})^{-1}=e^{-tA}.
\]
Uniqueness for \(x'(t)=Ax(t)\) follows by differentiating \(e^{-tA}x(t)\). In the inhomogeneous system \(x'=Ax+b(t)\), with continuous \(b\),
\[
x(t)=e^{tA}x_0+\int_0^t e^{(t-s)A}b(s)\,ds.
\]
For a Jordan block \(J_r(\lambda)=\lambda I+N\), \(N^r=0\),
\[
e^{tJ_r(\lambda)}=e^{\lambda t}\sum_{k=0}^{r-1}\frac{t^kN^k}{k!}.
\]
For \(A=\begin{pmatrix}-1&10\\0&-1\end{pmatrix}\),
\[
e^{tA}=e^{-t}\begin{pmatrix}1&10t\\0&1\end{pmatrix},\qquad \|e^Ae_2\|_2=e^{-1}\sqrt{101}>3.
\]
Yet \(e^{tA}\to0\) as \(t\to\infty\). For constant matrices in finite dimensions, \(e^{tA}\to0\) iff every eigenvalue has negative real part.

A real rotation generator \(R=\begin{pmatrix}0&-\omega\\\omega&0\end{pmatrix}\), \(R^2=-\omega^2I\), gives
\[
e^{tR}=\begin{pmatrix}\cos\omega t&-\sin\omega t\\\sin\omega t&\cos\omega t\end{pmatrix}.
\]

**Noncommuting example.** With \(B=\begin{pmatrix}0&1\\0&0\end{pmatrix}\), \(C=\begin{pmatrix}0&0\\1&0\end{pmatrix}\), both square to zero, so \(e^B=I+B\), \(e^C=I+C\), but \(e^Ce^B=I+B+C+CB\ne I+B+C+BC=e^Be^C\). The relation \(e^{B+C}=e^Be^C\) is valid when \(B\) and \(C\) commute, but not generally.

### Problems with answers

1. Find \(e^{tA}\) for \(A=\operatorname{diag}(2,-1)\). **Answer:** \(\operatorname{diag}(e^{2t},e^{-t})\).
2. Find \(e^{tN}\) when \(N^3=0\). **Answer:** \(I+tN+(t^2/2)N^2\).
3. Verify \(x(t)=e^{tA}x_0\) has the given initial condition. **Answer:** \(e^{0A}=I\), hence \(x(0)=x_0\).
4. Does negative real part of every eigenvalue force \(\|e^{tA}x_0\|_2\) to decrease for every \(t>0\)? **Answer:** no; the shear with minus-one eigenvalues gives transient amplification.
5. What condition makes \(e^{B+C}=e^Be^C\) safe? **Answer:** \(BC=CB\) is sufficient (though not necessary in every special instance).

### Source anchors and routes onward

- Gilbert Strang, [MIT OCW: Differential Equations and exp(At)](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/resources/lecture-23-differential-equations-and-exp-at/).
- MIT OpenCourseWare, [18.06SC Differential Equations and exp(At)](https://www.ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/pages/least-squares-determinants-and-eigenvalues/differential-equations-and-exp-at/).
- Sheldon Axler, [*Linear Algebra Done Right*](https://linear.axler.net/), finite-dimensional operator theory, generalized eigenspaces and nilpotent blocks.
- [Matrix exponential](https://en.wikipedia.org/wiki/Matrix_exponential) and [one-parameter group](https://en.wikipedia.org/wiki/One-parameter_group).

The finite-dimensional generator \(A\) is automatically bounded. In an infinite-dimensional PDE setting, general \(C_0\)-semigroups and unbounded generators require the distinct hypotheses in `analysis:064000` and related foundations; the same symbols alone do not prove their existence.
