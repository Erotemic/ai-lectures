# 005000 — Linear Systems, Eigenvalues, and Matrix Exponentials

**Track:** Differential Equations and Dynamical Systems. **Background:** first-order ODEs, matrices, eigenvalues. **Question:** how can a matrix determine an entire family of trajectories, including when it cannot be diagonalized?

<!-- BEGIN SPOKEN LECTURE -->

# Linear Systems, Eigenvalues, and Matrix Exponentials

One differential equation describes the evolution of one quantity. Many real systems have several quantities influencing one another: two populations, coupled masses, a collection of chemical concentrations, or an electrical network. A linear system writes their rates of change as a matrix times the state vector. Even with constant coefficients, the coordinates may be coupled so that we cannot solve them one at a time.

There is a single object that solves every constant-coefficient linear initial-value problem of this kind: the matrix exponential. Understanding it also clarifies what eigenvalues reveal about stability, and what they do not.

## From a scalar exponential to a matrix exponential

For a scalar equation saying y prime equals a times y, with constant a, the solution is y at time zero multiplied by e to the a t. Replace the scalar a with a square matrix A and the scalar state with a vector x. We hope that an expression called e to the A t will solve x prime equals A x.

Define the matrix exponential by the same infinite power series as the ordinary exponential: identity matrix plus A t plus one half A squared t squared, and so on, with the k-th term being A to the k-th power times t to the k-th power divided by k factorial. This series converges for every finite matrix and every real t. Because each term is a power of the same matrix A, term-by-term differentiation works and gives A times the original series. At time zero the sum is the identity matrix.

Thus x of t equals e to the A t times the initial state x zero is a solution. Standard uniqueness for linear differential equations says it is the only one with that initial state. We call the matrix exponential the state-transition operator: it maps an initial state to its later value.

There is a group law in time. Evolving for time s and then for time t is the same as evolving for time s plus t. The matrix identity is e to the A s times e to the A t equals e to the A times s plus t. The two factors commute because they are functions of the same matrix. We must not generalize this blindly to two unrelated matrices: e to the A times e to the B need not equal e to the A plus B if A and B do not commute.

## Eigenvectors are the normal modes

Suppose A has an eigenvector v with eigenvalue lambda. Starting on the line through v, the solution is e to the lambda t times v. The direction remains the same; only its scale changes. Such a direction is a mode. If a real matrix can be diagonalized over the reals, a general initial state is a sum of eigenmodes, each evolving at its own exponential rate.

Take a two-dimensional system with rates x one prime equals negative x one and x two prime equals negative three times x two. Its matrix is diagonal. The solution is x one at zero times e to the negative t, and x two at zero times e to the negative three t. Both modes decay, but the second does so faster. A trajectory tends to the origin, and after sufficient time its direction is typically dominated by the slowest decaying mode.

Now consider the matrix with entries negative one and one in the first row, and zero and negative two in the second. It is upper triangular. The second state decays as e to the negative two t. That second state also drives the first. Starting from first coordinate zero and second coordinate one, the solution becomes first coordinate e to the negative t minus e to the negative two t, and second coordinate e to the negative two t. Even though both eigenvalues are negative, the first coordinate initially increases from zero before eventually decaying. Stability concerns long-run behavior; it does not imply every coordinate decreases at every instant.

## Complex modes and rotations

A real matrix may have complex eigenvalues. In a two-dimensional example, let A rotate every vector counterclockwise at unit angular speed: its first row is zero, negative one, and its second row is one, zero. The eigenvalues are plus and minus the imaginary unit. The matrix exponential is the ordinary rotation matrix through angle t. The solution goes around a circle, never approaching the origin and never escaping to infinity.

If we subtract a small positive multiple of the identity matrix from this rotation generator, each trajectory spirals inward while rotating. The eigenvalues then have negative real parts. If instead we add a positive multiple of the identity, they spiral outward. This is why real parts of eigenvalues control exponential growth or decay and imaginary parts describe oscillatory behavior, at least at the level of linear modes.

But there is another issue: a matrix might not have enough eigenvectors to form a basis.

## Defective matrices and polynomial factors

Take a matrix whose diagonal entries are both negative one, whose upper-right entry is one, and whose lower-left entry is zero. It has only one independent eigenvector. Write the matrix as negative identity plus N, where N is nonzero but N squared equals zero. The exponential factors because the identity and N commute. We obtain e to the negative t multiplied by identity plus t times N.

Starting from a vector with second coordinate one, the first coordinate is t times e to the negative t. The factor t is not an exponential mode. It arises from a generalized eigenvector and is characteristic of a Jordan block. Nevertheless, t times e to the negative t still tends to zero. Negative exponential decay eventually dominates any fixed polynomial factor.

In general, finite-dimensional constant-coefficient systems are asymptotically stable if and only if every eigenvalue of A has strictly negative real part. Even if A is not diagonalizable, any Jordan polynomial factors are overwhelmed by those negative exponentials.

If some eigenvalue has positive real part, the equilibrium is unstable. If the largest real part is exactly zero, no single conclusion follows from eigenvalues alone without looking at Jordan blocks. A pure rotation is stable in the Lyapunov sense but not asymptotically stable. A nontrivial Jordan block attached to an imaginary-axis eigenvalue can produce unbounded polynomial growth and is unstable.

## Non-normal growth despite stable eigenvalues

Even a diagonalizable stable matrix can show large transient amplification if its eigenvectors are nearly parallel. This is common for non-normal matrices, where the matrix does not commute with its transpose in the appropriate real inner product. A concrete family is the upper-triangular matrix with negative one and negative two on the diagonal and a large positive number K in the upper-right position. Starting from the second coordinate one and the first zero, the first coordinate becomes K times the difference between e to the negative t and e to the negative two t. The amplitude can be as large as K divided by four at time log two, despite both eigenvalues being strictly negative.

So eigenvalues correctly predict eventual decay, but they do not bound intermediate amplification without additional information about eigenvector geometry or the matrix exponential norm. This distinction matters in numerical simulation and control. If disturbances are amplified a thousandfold before decaying, the eventual stability statement may be inadequate for design.

## What the exponential actually buys us

The matrix exponential solves the complete homogeneous system, with diagonalizable, defective, real, or complex eigenvalues. It also tells us exactly how perturbations to initial data propagate: the difference between two trajectories is the matrix exponential applied to the initial difference.

From there we can ask a new question. What happens when the system is continuously pushed by a time-dependent external force rather than merely starting away from equilibrium? The answer will integrate the matrix exponential against the forcing, revealing the principle of superposition in its most useful form.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For constant \(A\in\mathbb R^{n\times n}\), define
\[
e^{At}=\sum_{k=0}^\infty\frac{A^k t^k}{k!},\quad \frac d{dt}e^{At}=Ae^{At},\quad e^{A(t+s)}=e^{At}e^{As}.
\]
The unique solution to \(x'=Ax\), \(x(0)=x_0\), is \(x(t)=e^{At}x_0\). The identity \(e^{A+B}=e^Ae^B\) requires \(AB=BA\) in general.

**Jordan block:** \(A=\begin{pmatrix}-1&1\\0&-1\end{pmatrix}=-I+N\), \(N^2=0\), so
\[
e^{At}=e^{-t}\begin{pmatrix}1&t\\0&1\end{pmatrix}.
\]

**Non-normal transient:** for \(A=\begin{pmatrix}-1&K\\0&-2\end{pmatrix}\), \(x_0=(0,1)^T\),
\[
x(t)=\begin{pmatrix}K(e^{-t}-e^{-2t})\\e^{-2t}\end{pmatrix},\quad \max_{t\ge0}x_1(t)=K/4\ \text{at }t=\log2\text{ for }K>0.
\]
All eigenvalues have negative real parts, but transient amplification may be arbitrarily large as \(K\to\infty\).

### Exercises with answers

1. What is \(e^{At}\) when \(A=\operatorname{diag}(-2,3)\)? **Answer:** \(\operatorname{diag}(e^{-2t},e^{3t})\).
2. Is the origin asymptotically stable for pure planar rotation? **Answer:** no; trajectories retain their radius.
3. Can a matrix with only negative-real-part eigenvalues amplify a state transiently? **Answer:** yes; the triangular example above does so.
4. What invalid shortcut is tempting for noncommuting matrices? **Answer:** replacing \(e^Ae^B\) by \(e^{A+B}\) without checking commutativity.

### Reading

MIT OpenCourseWare, [Differential Equations lecture notes](https://ocw.mit.edu/courses/18-03-differential-equations-spring-2010/pages/lecture-notes/), sessions on eigenvalues, phase portraits and matrix exponentials.
