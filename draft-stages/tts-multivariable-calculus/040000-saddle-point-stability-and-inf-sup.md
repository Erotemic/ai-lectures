# Saddle-Point Stability: What the Inf–Sup Condition Measures

**Track:** Multivariable Calculus from First Principles. **Focus:** equality-constrained minimization, saddle-point equations, Schur complements, the inf–sup constant, kernel coercivity, and the Babuška–Brezzi framework.

<!-- BEGIN SPOKEN LECTURE -->

# Saddle-Point Stability: What the Inf–Sup Condition Measures

Imagine that two engineers are given the same linear system. One sees a symmetric matrix and reaches for a positive-definite solver. The other notices that the equations include a constraint enforced by a multiplier. The diagonal entry associated with that multiplier is zero. Before choosing a solver, the second engineer asks a different question: can the system tell one multiplier from another? If it cannot, no amount of numerical precision will supply information that the equations do not contain.

This is the central difficulty of a saddle-point problem. The issue is not merely that the combined matrix has positive and negative eigenvalues. Its stability depends on how the constrained directions couple to the original variables.

We will get to the inf–sup condition from an ordinary two-variable minimization problem. Every number will be available for checking. Then we will return to weak equations in function spaces and see why the same condition matters on every mesh.

## The smallest interesting constrained problem

Take two real variables, x one and x two. Minimize a quadratic energy: one half times the sum of two x one squared and x two squared, minus x one. Require their sum to be zero. Without the constraint, the energy prefers positive x one and zero x two. The constraint forces any increase in x one to be offset by a decrease in x two.

Attach a multiplier lambda to the equation x one plus x two equals zero. The Lagrangian is the energy plus lambda times the constraint. Stationarity with respect to x one says two x one plus lambda equals one. Stationarity with respect to x two says x two plus lambda equals zero. The constraint adds x one plus x two equals zero.

Solve these three equations. The second equation says lambda equals minus x two. Since x two equals minus x one, lambda equals x one. The first equation then gives three x one equals one. So x one is one third, x two is negative one third, and lambda is one third.

If we write these equations in matrix form, the upper-left block is the positive-definite diagonal matrix with entries two and one. The constraint is represented by the row with entries one and one. The full matrix consists of the energy block, the transpose of the constraint row, the constraint row itself, and a zero in the lower-right corner.

The zero is not an oversight. A multiplier does not have an independent quadratic penalty in this formulation. It enforces a relation among the original variables. The matrix is therefore symmetric but indefinite. In particular, an ordinary Cholesky factorization of the complete block matrix is not appropriate, even though the energy block has a perfectly good Cholesky factorization.

## Eliminate the variables, not the constraint

There is a clean way to understand solvability. From the first block equation, solve for x in terms of the forcing f and the multiplier: x equals the inverse of A applied to f minus B transpose times lambda. Here A is the energy matrix and B is the constraint row.

Substitute this expression into the constraint B x equals g. The resulting equation for the multiplier has the matrix B times A inverse times B transpose. This is a Schur complement, often denoted S. In our example, its value is one half plus one, or three halves. The forcing on the right is B A inverse f minus g, which is one half. Three halves times lambda equals one half, recovering lambda equal to one third.

Notice the identity hidden in this calculation. For any candidate multiplier value y, y times S times y is the squared A-inverse-weighted size of B transpose y. It cannot be negative. It is zero precisely when B transpose y is zero. So S is positive definite on the multiplier space exactly when no nonzero multiplier is invisible to the constraint coupling.

In finite dimensions, if A is positive definite and the constraint rows are independent, that conclusion is immediate. But two things can go wrong. Rows can be exactly dependent, leaving more multipliers than independent constraints. Or they can become almost dependent as a mesh changes, making the multiplier extremely sensitive even while the matrix remains invertible.

Both are captured by the smallest singular value of a suitably scaled constraint operator. We need a number that not only says the coupling is nonzero but measures how far it is from vanishing.

## The meaning of an infimum and a supremum

Call the original variable space V and the multiplier space Q. The coupling is a bilinear form b, taking a field v and a multiplier q and producing a number. In matrix form, the number is q transpose times B times v.

Fix a nonzero q. Ask: among all test fields v with unit size, how strongly can the coupling detect q? That is a supremum over v. If every allowed v gives zero, the multiplier is invisible. If some v detects it, the supremum is positive; if only enormously large v can detect it appreciably, the detection is weak after normalization by the size of v.

Now consider the worst nonzero multiplier, normalized to unit size. Take the infimum over q. The result is the inf–sup constant, usually called beta. A positive beta means that even the least detectable multiplier has a test field that reveals it at a controlled cost.

The norms matter. If we use the energy norm for v and the ordinary Euclidean norm for q, then beta squared is the smallest eigenvalue of the Schur complement B A inverse B transpose. For our two-variable example beta is the square root of three halves. That value exceeding one is not a problem; beta is not a probability. It depends on how we scale the variables and their norms.

For a different example, suppose the constraint rows are almost copies of each other. Take two variables and two constraints. The first row reads x one. The second reads x one plus a small number epsilon times x two. The difference between the two measured constraints is only epsilon times x two. A multiplier putting opposite weights on the two rows almost cancels in the field equation. As epsilon tends toward zero, the least detectable multiplier mode becomes harder to see. Beta tends toward zero.

When epsilon is exactly zero, the rows are identical, and infinitely many multiplier pairs can describe the same force on x. For nonzero epsilon, the solution is algebraically unique, but the multiplier can react enormously to a small incompatible change in the data. The exact size depends on how the constraints and norms are scaled. A tiny beta is a warning about stability, not a universal estimate of any physical observable without specifying those norms.

## From matrices to a theorem about functions

In a finite-element problem, matrices are only coordinate representations of bilinear forms on spaces of functions. The abstract saddle-point problem asks for a field u in V and a multiplier p in Q such that the energy form a applied to u and each test v, plus the coupling b applied to v and p, equals a prescribed functional; and the coupling b applied to u and each test q equals the constraint data.

There are two conditions to check. First, the energy form needs to control fields that satisfy the homogeneous constraint. Such fields lie in the kernel of b. We call this coercivity on the kernel. It need not control every direction in V by itself. Second, the coupling must satisfy an inf–sup condition with positive beta. Under the standard continuity and Hilbert-space assumptions, these two properties give existence, uniqueness, and continuous dependence on the data.

Why only coercivity on the kernel? Because the multiplier equation handles the directions outside the kernel. Requiring the energy to control every possible field would be stronger than necessary and would exclude important mixed formulations. In the mixed Poisson problem, for example, the flux energy measures the square-integrable flux. But the natural flux norm also includes the divergence. The energy alone does not control that divergence for arbitrary flux fields. On divergence-free fields the additional part of the norm vanishes, so coercivity on the kernel is exactly the right property.

For the Stokes problem, by contrast, the viscous energy controls the velocity in the zero-boundary H one norm, while the pressure is detected through divergence. The pressure is defined only up to an additive constant in a fully velocity-Dirichlet problem. We must account for that gauge freedom, typically by requiring the pressure to have mean zero. Otherwise beta would vanish because a constant pressure cannot be detected by divergence tests that vanish on the boundary.

## Stability must survive refinement

Suppose a continuous problem has a positive inf–sup constant. It is tempting to select any reasonable finite-dimensional subspaces and assume the same fact will hold after discretization. This is false. A pair of finite-element spaces can approximate smooth velocity and pressure functions separately yet admit a discrete pressure oscillation that the available velocity tests cannot detect.

The discrete inf–sup constant, beta sub h, measures precisely the coupling between the chosen discrete spaces. For each fixed mesh it might be positive, but if beta sub h tends to zero as the mesh gets finer, stability estimates deteriorate. Error bounds that appear to promise convergence may carry constants that blow up with refinement.

This explains why a good mixed method requires compatible spaces, not merely a large number of degrees of freedom or high polynomial order. More pressure degrees of freedom can actually make things worse if the velocity space has not acquired the means to detect them.

There is a conceptual difference between a solver that fails and a discretization that fails. A solver issue can sometimes be addressed by better elimination or preconditioning. A discrete inf–sup failure is already present in the equations we assembled. An exact direct solve may return one answer, or may report singularity, but it cannot restore the missing constraint information.

## The useful conclusion

The inf–sup test is a quantitative observability condition for constraints. It asks whether every possible multiplier mode pushes on some admissible field by an amount proportional to its own size. Coercivity on the kernel supplies control where the multiplier is silent. Together, the two conditions explain why certain saddle-point problems are well posed and why certain mixed discretizations remain stable under refinement.

The best way to see discrete failure is not to study an enormous finite-element mesh. It is to construct one nonzero pressure function that pairs to zero with every available discrete derivative. We can do that on an interval cut into just two cells. Then we will replace the pressure space and watch the coupling become exact.

<!-- END SPOKEN LECTURE -->

## Mathematical companion: a finite-dimensional calculation

Let \(A=\begin{bmatrix}2&0\\0&1\end{bmatrix}\), \(B=\begin{bmatrix}1&1\end{bmatrix}\), \(f=(1,0)^T\), \(g=0\). The constrained minimization

\[
\min_{Bx=g}\frac12x^TAx-f^Tx
\]

has KKT system

\[
\begin{bmatrix}2&0&1\\0&1&1\\1&1&0\end{bmatrix}
\begin{bmatrix}x_1\\x_2\\\lambda\end{bmatrix}=
\begin{bmatrix}1\\0\\0\end{bmatrix},\qquad
(x_1,x_2,\lambda)=\left(\frac13,-\frac13,\frac13\right).
\]

The Schur complement \(S=BA^{-1}B^T=\frac32\), hence \(S\lambda=BA^{-1}f-g=\frac12\). The quadratic form \(q^TSq=(B^Tq)^TA^{-1}(B^Tq)\) is strictly positive for \(q\ne0\) iff \(B^T\) is injective.

For the \(A\)-norm \(\|v\|_A=\sqrt{v^TAv}\) and \(Q=\mathbb R^m\) with Euclidean norm,

\[
\sup_{v\ne0}\frac{q^TBv}{\|v\|_A}=\sqrt{q^TBA^{-1}B^Tq},\qquad
\beta^2=\lambda_{\min}(BA^{-1}B^T).
\]

The supremum is attained at \(v=A^{-1}B^Tq\) up to a nonzero scalar.

### Abstract Hilbert-space statement

Let \(V,Q\) be Hilbert spaces; \(a:V\times V\to\mathbb R\), \(b:V\times Q\to\mathbb R\) bounded bilinear forms. Define

\[
V_0=\{v\in V:b(v,q)=0\ \forall q\in Q\}.
\]

Assume \(a(v,v)\ge\alpha\|v\|_V^2\) for all \(v\in V_0\), \(\alpha>0\), and

\[
\beta=\inf_{q\ne0}\sup_{v\ne0}
\frac{b(v,q)}{\|v\|_V\|q\|_Q}>0.
\]

(The supremum allows changing the sign of \(v\); equivalently use \(|b(v,q)|\).) Then the standard Brezzi saddle-point theorem gives well-posedness of

\[
a(u,v)+b(v,p)=F(v),\qquad b(u,q)=G(q),
\]

under these hypotheses. In a nonsymmetric generalization one must use the appropriate coercivity/invertibility assumptions on the kernel; here we use the standard coercive symmetric case. The discrete version requires bounds \(\alpha_h,\beta_h\) independent of mesh size for uniform stability and quasioptimal estimates.

A nearly dependent row family illustrates degeneration:

\[
B_\epsilon=\begin{bmatrix}1&0\\1&\epsilon\end{bmatrix},\qquad A=I,
\quad\det B_\epsilon=\epsilon.
\]

For \(\epsilon\ne0\), both constraints are independent. For \(\epsilon=0\), \(\ker B_\epsilon^T\) contains \((1,-1)^T\). As \(\epsilon\to0\), \(\beta_\epsilon=\sigma_{\min}(B_\epsilon)\to0\), in these fixed norms.

### Exercises with answers

1. **Schur arithmetic:** Compute \(BA^{-1}B^T\) for the worked example. **Answer:** \(1/2+1=3/2\).
2. **Why the zero block?** Differentiate the Lagrangian with respect to the multiplier. **Answer:** It gives \(Bx-g=0\) without a multiplier-square term.
3. **Row dependence:** For \(B=\begin{bmatrix}1&0\\2&0\end{bmatrix}\), find an invisible multiplier. **Answer:** \(q=(-2,1)^T\), because \(B^Tq=0\).
4. **Pressure gauge:** Explain why constant pressure cannot be detected in the Stokes weak equation with homogeneous velocity Dirichlet data. **Answer:** \(\int_\Omega\nabla\cdot v=\int_{\partial\Omega}v\cdot n=0\) for test velocities with zero trace.
5. **Kernel coercivity:** In mixed Poisson, what happens to the \(H(\mathrm{div})\)-norm when \(\nabla\cdot r=0\)? **Answer:** It reduces to the \(L^2\) flux norm, which is controlled by \((k^{-1}r,r)\) under positive bounded conductivity.

### Sources and further reading

- Franco Brezzi and Michel Fortin, [*Mixed and Hybrid Finite Element Methods* (1991)](https://link.springer.com/book/10.1007/978-1-4612-3172-1), chapters on saddle-point approximation and the inf–sup condition.
- Daniele Boffi, Franco Brezzi and Michel Fortin, [*Mixed Finite Element Methods and Applications* (2013)](https://link.springer.com/book/10.1007/978-3-642-36519-5), algebraic and Hilbert-space stability chapters.
- [Wikipedia: Ladyzhenskaya–Babuška–Brezzi condition](https://en.wikipedia.org/wiki/Ladyzhenskaya%E2%80%93Babu%C5%A1ka%E2%80%93Brezzi_condition) and [Uzawa iteration](https://en.wikipedia.org/wiki/Uzawa_iteration), for terminology and the Schur-complement viewpoint.

*Teaching connections:* `multivariable-calculus:029000` provides constrained Newton systems; `039000` supplies a PDE requiring precisely this kind of constraint coupling; `linear-algebra:024000` treats positive-definite factorizations, which apply to the energy block but not directly to the full saddle matrix.
