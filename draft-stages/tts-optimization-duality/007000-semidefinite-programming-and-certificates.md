# 007000 — Semidefinite Programming: Optimizing over Positive Matrices

**Track:** Optimization, Convexity, and Duality. **Background:** convexity, linear-programming duality, symmetric matrices. **Question:** how can a matrix inequality express infinitely many quadratic inequalities, and how does a dual matrix certify an optimum?

<!-- BEGIN SPOKEN LECTURE -->

# Semidefinite Programming: Optimizing over Positive Matrices

Linear programming optimizes a linear function under linear inequalities. Quadratic functions and geometric constraints seem to demand a different theory. Yet many such problems can be written as a linear optimization over matrices, with the constraint that a symmetric matrix be positive semidefinite. This is semidefinite programming, often abbreviated SDP.

The central move is to replace a list of scalar nonnegativity conditions with a stronger matrix condition. A symmetric matrix X is positive semidefinite if v transpose X v is nonnegative for every vector v. A single finite matrix inequality therefore encodes infinitely many scalar inequalities, one for each direction v. The constraint looks complicated, but it defines a convex set, so much of convex duality becomes available.

## What positive semidefinite means

For a symmetric real matrix, positive semidefiniteness is equivalent to having only nonnegative eigenvalues. To see the relationship, use an orthonormal eigenbasis. A quadratic form evaluated on any vector is then a sum of eigenvalues multiplied by squares of coordinates. If every eigenvalue is nonnegative, every term is nonnegative. If one eigenvalue were negative, the quadratic form evaluated on its eigenvector would be negative.

A two-by-two symmetric matrix with diagonal entries a and b and off-diagonal entry c is positive semidefinite exactly when a and b are nonnegative and a times b is at least c squared. This is not the same as requiring every matrix entry to be nonnegative. For example, a matrix with diagonal entries one and off-diagonal entries negative one is positive semidefinite: it has one eigenvalue zero and one eigenvalue two, even though some entries are negative.

The set of all positive semidefinite symmetric matrices is a convex cone. If X and Y are positive semidefinite and the coefficients used to combine them are nonnegative, every quadratic form of the combination is a nonnegative combination of quadratic forms. The result stays positive semidefinite.

That convexity is what makes this a tractable class of optimization problems, although practical computational costs can still be substantial for very large matrices.

## A standard semidefinite program

A common standard form minimizes a linear matrix inner product between a given symmetric cost matrix C and an unknown symmetric matrix X. The matrix inner product is the trace of the product, or equivalently the sum of corresponding entries when both matrices are symmetric. We impose linear equalities saying that the inner product of given matrices A one through A m with X equals specified scalars b one through b m. We also require X to be positive semidefinite.

Everything except the positive-semidefinite constraint is linear in the entries of X. In a linear program, requiring each coordinate to be nonnegative gives the nonnegative orthant. In an SDP, requiring an entire matrix to be positive semidefinite gives a richer cone. Linear programming itself can be represented as a special case, by placing ordinary nonnegative variables on the diagonal of a matrix.

The semidefinite constraint allows us to express relationships among variables. A two-by-two positive-semidefinite condition with a fixed off-diagonal entry one says that two diagonal variables a and b must be nonnegative and satisfy a times b at least one. That is nonlinear as a scalar constraint, but it is convex when expressed as a matrix inequality.

## The dual problem and weak duality

To obtain a lower bound on a minimization problem, choose one multiplier for each linear equality. Combine the given constraint matrices using those multipliers and subtract the combination from C. Call the remaining matrix S. If S is positive semidefinite, it is a dual-feasible slack matrix.

For any primal-feasible positive-semidefinite X, the difference between the primal cost and the proposed dual value is the trace of S times X. That quantity is nonnegative when S and X are both positive semidefinite. The reason is not that individual matrix entries are nonnegative; they need not be. Instead, take a positive-semidefinite square root of one matrix and use the cyclic trace identity. The trace becomes the trace of another positive-semidefinite matrix, so it is nonnegative.

Thus every feasible dual multiplier produces a certified lower bound on the primal cost. This is weak duality. The primal problem searches for the smallest achievable cost, while the dual searches for the strongest such lower bound under the matrix slack constraint.

## A complete two-by-two calculation

Let X have diagonal entries a and b and both off-diagonal entries equal to one. Minimize its trace, a plus b, subject to X being positive semidefinite.

Positive semidefiniteness requires a and b to be nonnegative and their product to be at least one. By the arithmetic-geometric mean inequality, a plus b is at least twice the square root of a b, hence at least two. We can achieve two by taking a and b both equal to one. The optimal matrix has every entry equal to one and has rank one.

Now give an independent dual certificate. Encode the off-diagonal constraint as the inner product of X with the symmetric matrix whose off-diagonal entries are one half and whose diagonal entries are zero; this inner product equals one. The cost matrix is the identity. Choose dual multiplier y equal to two. The dual slack becomes the matrix with diagonal entries one and off-diagonal entries negative one. This slack is positive semidefinite. The proposed dual value is two. Weak duality then proves that no feasible primal matrix can have trace less than two. Since our candidate reaches two, primal and dual objectives agree and both are optimal.

We did not need to run an optimizer to certify this answer. The primal matrix and the dual multiplier are independently checkable mathematical witnesses. Their agreement rules out any better feasible solution.

## Complementary slackness as orthogonality

At an optimum where primal and dual objectives agree, the trace of the primal matrix times the dual slack is zero. For positive-semidefinite matrices this forces their product to be zero. In geometric terms, their ranges occupy orthogonal directions after accounting for the positive-semidefinite structure. In the worked example, the optimal primal matrix is supported along the vector with two equal coordinates, while the optimal dual slack is supported along the vector with opposite coordinates.

This is semidefinite complementary slackness. It parallels the familiar linear-programming statement that a positive primal variable requires a zero corresponding dual slack, except that now entire subspaces, not just coordinates, interact.

Strong duality does not follow from convexity alone without qualifications. A standard sufficient condition is Slater's constraint qualification: one side has a strictly feasible point and the appropriate finite optimal-value and feasibility hypotheses hold. In our example, the primal constraint has a strictly positive-definite feasible matrix, such as diagonal entries two and off-diagonal entries one. So we are not relying on an unexplained assumption that every SDP always has zero duality gap or an attained optimum.

## Relaxing discrete geometry into a matrix

Why do semidefinite programs appear in combinatorial optimization? Suppose discrete variables are required to be either plus one or negative one. Form a matrix X from all pairwise products of those variables. Then X is positive semidefinite, its diagonal entries are all one, and it has rank one. Many quadratic objectives in the original variables become *linear* in X.

The rank-one condition is difficult and nonconvex. If we drop it but retain positive semidefiniteness and unit diagonal, we obtain a convex relaxation. Its feasible set is larger, so for a maximization problem it gives an upper bound on the discrete optimum; for a minimization problem, it gives a lower bound. The relaxed solution need not correspond to any original plus-or-minus-one assignment, but it can be used to construct approximations or prove bounds.

This is a common mathematical strategy: lift nonlinear expressions into a larger space in which the objective and constraints become linear, relax a difficult structural condition, and then use convex optimization to obtain a verifiable bound.

## The boundary of the method

SDPs are expressive, but positive-semidefinite constraints can be expensive in memory and time. Floating-point solvers also require residual checks for equality constraints, cone feasibility, and primal-dual gap before a numerical answer should be regarded as certified to a requested tolerance. A solver's success message is not itself a mathematical proof of exact feasibility, especially near singular matrices.

The enduring idea is the dual certificate. A seemingly nonlinear collection of quadratic inequalities can be represented by a positive-semidefinite matrix, and its objective can be bounded with another positive-semidefinite matrix. When the primal construction and dual bound meet, the optimization problem has an explanation, not merely a number.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

The **positive-semidefinite cone** \(\mathbb S_+^n=\{X=X^T:v^TXv\ge0\;\forall v\in\mathbb R^n\}\) is closed and convex. For \(X=\begin{pmatrix}a&c\\c&b\end{pmatrix}\), \(X\succeq0\) iff \(a\ge0\), \(b\ge0\), \(ab\ge c^2\).

**Primal standard form:**
\[
\min_{X\succeq0}\;\langle C,X\rangle\quad\text{subject to }\langle A_i,X\rangle=b_i,\ i=1,\dots,m.
\]
**Dual:**
\[
\max_y\;b^Ty\quad\text{subject to }S=C-\sum_i y_iA_i\succeq0.
\]
For feasible \(X,y\), weak duality follows from
\[
\langle C,X\rangle-b^Ty=\langle S,X\rangle\ge0.
\]
For \(S,X\succeq0\), \(\operatorname{tr}(SX)\ge0\). If \(\operatorname{tr}(SX)=0\), then \(SX=0\).

**Worked certificate:** \(C=I_2\), \(A_1=\begin{pmatrix}0&1/2\\1/2&0\end{pmatrix}\), \(b_1=1\). Primal \(X_*=\begin{pmatrix}1&1\\1&1\end{pmatrix}\) has objective 2. Dual \(y_*=2\) gives \(S_*=\begin{pmatrix}1&-1\\-1&1\end{pmatrix}\succeq0\) with objective 2. Hence both are optimal. Moreover \(S_*X_*=0\).

**Boolean lifting:** for \(x\in\{-1,+1\}^n\), \(X=xx^T\) has \(X\succeq0\), \(X_{ii}=1\), and rank one. Dropping rank one creates a convex relaxation. Preserve the direction of the resulting bound: for minimization it is a lower bound, and for maximization an upper bound.

### Exercises with answers

1. Is \(\begin{pmatrix}1&-2\\-2&1\end{pmatrix}\) positive semidefinite? **Answer:** no; its eigenvalues are three and negative one.
2. Is entrywise nonnegativity necessary for positive semidefiniteness? **Answer:** no; \(\begin{pmatrix}1&-1\\-1&1\end{pmatrix}\succeq0\).
3. Explain the duality gap in the worked example. **Answer:** the primal and dual objectives both equal two, so the gap is zero.
4. Why does dropping the rank-one constraint enlarge the lifted Boolean feasible set? **Answer:** positive semidefiniteness and unit diagonal also allow Gram matrices of higher-dimensional unit vectors.

### Reading

Stephen Boyd and Lieven Vandenberghe, [Convex Optimization](https://web.stanford.edu/~boyd/cvxbook/), semidefinite programming and duality; Lieven Vandenberghe and Stephen Boyd, [Semidefinite Programming](https://web.stanford.edu/~boyd/papers/sdp), *SIAM Review* 38(1), 1996.
