# Conic optimization: matrix inequalities, barriers, and verified witnesses

<!-- BEGIN SPOKEN LECTURE -->

# Conic optimization: matrix inequalities, barriers, and verified witnesses

## Semidefinite Programming: Optimizing over Positive Matrices

Linear programming optimizes a linear function under linear inequalities. Quadratic functions and geometric constraints seem to demand a different theory. Yet many such problems can be written as a linear optimization over matrices, with the constraint that a symmetric matrix be positive semidefinite. This is semidefinite programming, often abbreviated SDP.

The central move is to replace a list of scalar nonnegativity conditions with a stronger matrix condition. A symmetric matrix X is positive semidefinite if v transpose X v is nonnegative for every vector v. A single finite matrix inequality therefore encodes infinitely many scalar inequalities, one for each direction v. The constraint looks complicated, but it defines a convex set, so much of convex duality becomes available.

### What positive semidefinite means

For a symmetric real matrix, positive semidefiniteness is equivalent to having only nonnegative eigenvalues. To see the relationship, use an orthonormal eigenbasis. A quadratic form evaluated on any vector is then a sum of eigenvalues multiplied by squares of coordinates. If every eigenvalue is nonnegative, every term is nonnegative. If one eigenvalue were negative, the quadratic form evaluated on its eigenvector would be negative.

A two-by-two symmetric matrix with diagonal entries a and b and off-diagonal entry c is positive semidefinite exactly when a and b are nonnegative and a times b is at least c squared. This is not the same as requiring every matrix entry to be nonnegative. For example, a matrix with diagonal entries one and off-diagonal entries negative one is positive semidefinite: it has one eigenvalue zero and one eigenvalue two, even though some entries are negative.

The set of all positive semidefinite symmetric matrices is a convex cone. If X and Y are positive semidefinite and the coefficients used to combine them are nonnegative, every quadratic form of the combination is a nonnegative combination of quadratic forms. The result stays positive semidefinite.

That convexity is what makes this a tractable class of optimization problems, although practical computational costs can still be substantial for very large matrices.

### A standard semidefinite program

A common standard form minimizes a linear matrix inner product between a given symmetric cost matrix C and an unknown symmetric matrix X. The matrix inner product is the trace of the product, or equivalently the sum of corresponding entries when both matrices are symmetric. We impose linear equalities saying that the inner product of given matrices A one through A m with X equals specified scalars b one through b m. We also require X to be positive semidefinite.

Everything except the positive-semidefinite constraint is linear in the entries of X. In a linear program, requiring each coordinate to be nonnegative gives the nonnegative orthant. In an SDP, requiring an entire matrix to be positive semidefinite gives a richer cone. Linear programming itself can be represented as a special case, by placing ordinary nonnegative variables on the diagonal of a matrix.

The semidefinite constraint allows us to express relationships among variables. A two-by-two positive-semidefinite condition with a fixed off-diagonal entry one says that two diagonal variables a and b must be nonnegative and satisfy a times b at least one. That is nonlinear as a scalar constraint, but it is convex when expressed as a matrix inequality.

### The dual problem and weak duality

To obtain a lower bound on a minimization problem, choose one multiplier for each linear equality. Combine the given constraint matrices using those multipliers and subtract the combination from C. Call the remaining matrix S. If S is positive semidefinite, it is a dual-feasible slack matrix.

For any primal-feasible positive-semidefinite X, the difference between the primal cost and the proposed dual value is the trace of S times X. That quantity is nonnegative when S and X are both positive semidefinite. The reason is not that individual matrix entries are nonnegative; they need not be. Instead, take a positive-semidefinite square root of one matrix and use the cyclic trace identity. The trace becomes the trace of another positive-semidefinite matrix, so it is nonnegative.

Thus every feasible dual multiplier produces a certified lower bound on the primal cost. This is weak duality. The primal problem searches for the smallest achievable cost, while the dual searches for the strongest such lower bound under the matrix slack constraint.

### A complete two-by-two calculation

Let X have diagonal entries a and b and both off-diagonal entries equal to one. Minimize its trace, a plus b, subject to X being positive semidefinite.

Positive semidefiniteness requires a and b to be nonnegative and their product to be at least one. By the arithmetic-geometric mean inequality, a plus b is at least twice the square root of a b, hence at least two. We can achieve two by taking a and b both equal to one. The optimal matrix has every entry equal to one and has rank one.

Now give an independent dual certificate. Encode the off-diagonal constraint as the inner product of X with the symmetric matrix whose off-diagonal entries are one half and whose diagonal entries are zero; this inner product equals one. The cost matrix is the identity. Choose dual multiplier y equal to two. The dual slack becomes the matrix with diagonal entries one and off-diagonal entries negative one. This slack is positive semidefinite. The proposed dual value is two. Weak duality then proves that no feasible primal matrix can have trace less than two. Since our candidate reaches two, primal and dual objectives agree and both are optimal.

We did not need to run an optimizer to certify this answer. The primal matrix and the dual multiplier are independently checkable mathematical witnesses. Their agreement rules out any better feasible solution.

### Complementary slackness as orthogonality

At an optimum where primal and dual objectives agree, the trace of the primal matrix times the dual slack is zero. For positive-semidefinite matrices this forces their product to be zero. In geometric terms, their ranges occupy orthogonal directions after accounting for the positive-semidefinite structure. In the worked example, the optimal primal matrix is supported along the vector with two equal coordinates, while the optimal dual slack is supported along the vector with opposite coordinates.

This is semidefinite complementary slackness. It parallels the familiar linear-programming statement that a positive primal variable requires a zero corresponding dual slack, except that now entire subspaces, not just coordinates, interact.

Strong duality does not follow from convexity alone without qualifications. A standard sufficient condition is Slater's constraint qualification: one side has a strictly feasible point and the appropriate finite optimal-value and feasibility hypotheses hold. In our example, the primal constraint has a strictly positive-definite feasible matrix, such as diagonal entries two and off-diagonal entries one. So we are not relying on an unexplained assumption that every SDP always has zero duality gap or an attained optimum.

### Relaxing discrete geometry into a matrix

Why do semidefinite programs appear in combinatorial optimization? Suppose discrete variables are required to be either plus one or negative one. Form a matrix X from all pairwise products of those variables. Then X is positive semidefinite, its diagonal entries are all one, and it has rank one. Many quadratic objectives in the original variables become *linear* in X.

The rank-one condition is difficult and nonconvex. If we drop it but retain positive semidefiniteness and unit diagonal, we obtain a convex relaxation. Its feasible set is larger, so for a maximization problem it gives an upper bound on the discrete optimum; for a minimization problem, it gives a lower bound. The relaxed solution need not correspond to any original plus-or-minus-one assignment, but it can be used to construct approximations or prove bounds.

This is a common mathematical strategy: lift nonlinear expressions into a larger space in which the objective and constraints become linear, relax a difficult structural condition, and then use convex optimization to obtain a verifiable bound.

### The boundary of the method

SDPs are expressive, but positive-semidefinite constraints can be expensive in memory and time. Floating-point solvers also require residual checks for equality constraints, cone feasibility, and primal-dual gap before a numerical answer should be regarded as certified to a requested tolerance. A solver's success message is not itself a mathematical proof of exact feasibility, especially near singular matrices.

The enduring idea is the dual certificate. A seemingly nonlinear collection of quadratic inequalities can be represented by a positive-semidefinite matrix, and its objective can be bounded with another positive-semidefinite matrix. When the primal construction and dual bound meet, the optimization problem has an explanation, not merely a number.

Positive semidefinite matrices give one particular cone. A primal-dual certificate can be formulated for a general cone, letting us compare matrix inequalities, linear programs, and second-order constraints in one language.

## Conic Duality: One Language for Linear, Quadratic, and Matrix Inequalities

Linear programming constrains variables to lie in half-spaces. Semidefinite programming constrains matrices to be positive semidefinite. Second-order cone programming constrains the length of a vector to be no greater than a scalar. These look like different mathematical worlds, but they share an organizing structure: an affine subspace intersected with a convex cone.

Conic optimization expresses that structure directly. Once it does, weak duality, complementarity, and conditions for strong duality can be derived in one framework rather than as separate tricks for every problem class.

### What a cone contributes

A cone contains the nonnegative scalar multiples of its elements. A convex cone is also closed under addition, and we usually work with closed convex cones for standard finite-dimensional conic optimization.

The nonnegative orthant is the cone behind ordinary linear programming. The cone of positive semidefinite symmetric matrices gives semidefinite programming. The second-order, or Lorentz, cone consists of pairs of a scalar t and a vector u satisfying t at least the Euclidean norm of u. Convexity follows from the triangle inequality.

A conic problem can minimize a linear objective over variables x constrained by a linear equation A x equals b and membership x in a cone K. Many convex problems admit a formulation of this type after introducing auxiliary variables or slack variables.

But representation matters. Different equivalent mathematical models can have very different sizes, numerical conditioning, or constraint qualifications. A conic formulation is a common language, not a promise that every formulation is computationally equally good.

### The dual cone and weak duality

Every cone K has a dual cone K star. It contains all vectors s whose inner product with every vector in K is nonnegative. Think of a dual-cone element as a linear functional that can never assign a negative value to a feasible cone direction.

Introduce a multiplier y for the equation A x equals b. The Lagrangian takes the linear objective c dot x and subtracts y dot the constraint residual A x minus b. Collect the terms involving x: its coefficient is c minus A transpose y.

When that coefficient belongs to K star, its inner product with every x in K is nonnegative. Therefore the Lagrangian is bounded below by b dot y. This leads to the conic dual: maximize b dot y subject to c minus A transpose y belonging to K star.

The proof of weak duality now fits on one line of algebra. For primal feasible x and dual feasible y, subtract the dual objective from the primal objective. The result is the inner product of x with c minus A transpose y. One vector lies in K, the other in K star, so the difference is nonnegative.

That conclusion needs no Slater condition and no numerical algorithm. Any pair of exactly feasible points gives a rigorous lower and upper bound on the optimum.

### Three self-dual examples

The nonnegative orthant is self-dual: a vector has nonnegative dot product with every nonnegative vector exactly when its coordinates are nonnegative. That gives the usual sign restrictions in LP duality.

The second-order cone is also self-dual under the standard Euclidean inner product. Its defining inequality, t at least the norm of u, is a familiar norm bound. The self-duality can be understood using Cauchy–Schwarz: the worst direction opposing u has the same magnitude and opposite direction.

The positive semidefinite cone is self-dual under the trace inner product. If X and S are positive semidefinite, the trace of their product is nonnegative. Conversely, a symmetric matrix with a negative eigenvalue has negative trace inner product with a suitable rank-one positive semidefinite matrix. This recovers the dual constraints used in semidefinite programming.

Not every convex cone is self-dual. The cone and its dual may require different descriptions. The conic-duality framework works because it names the two separately rather than assuming they coincide.

### A norm as an optimization problem

Fix a vector a. What is its Euclidean norm? We can express it as the smallest scalar t such that the pair t and a belongs to the second-order cone. The primal answer is the norm of a by definition.

The corresponding dual viewpoint maximizes the inner product of a with a vector y constrained to have norm at most one. Cauchy–Schwarz says the inner product can never exceed the norm of a. If a is nonzero, choose y in the direction of a with unit length, and equality holds.

Thus the equality between a norm and the support function of the unit ball is a concrete case of conic duality. The primal chooses the smallest enclosing magnitude. The dual chooses the direction that certifies that magnitude cannot be smaller.

This example illustrates what a certificate does: instead of trusting a solver's claim that t is minimal, produce a feasible dual vector whose objective matches t.

### When do the bounds coincide?

Weak duality only says the dual value cannot exceed the primal value. Strong duality says their optimal values are equal. For finite-dimensional convex conic problems, a standard sufficient condition is strict feasibility, often called Slater's condition.

In the simple primal form with equality constraints, strict feasibility means there is an x satisfying A x equals b that lies in the interior of K. Together with suitable finiteness assumptions, this provides strong duality and attainment of a dual optimum. There are refinements for cones with empty interior in an ambient representation, where relative interior and facial reduction enter.

The condition is sufficient, not necessary. Strong duality can hold even if no strictly feasible point exists. Conversely, without appropriate constraint qualifications, a conic problem may have a positive duality gap, an unattained optimum, or delicate feasibility behavior. Semidefinite optimization in particular admits weak infeasibility, where an affine space has zero distance to the cone without intersecting it.

Slater's condition is a theorem hypothesis, not a setting in a software interface. A solver can report numerical feasibility without proving that the exact mathematical problem meets the required condition.

### Complementarity and certificates

Suppose primal and dual optima are both attained and the gap is zero. The inner product between the primal cone variable and the dual slack must vanish. This is complementarity. For the nonnegative orthant, it reduces to coordinatewise products of primal and dual slack variables being zero. For semidefinite optimization, it becomes orthogonality of positive semidefinite matrices in the trace inner product.

To verify a candidate solution, check the linear equalities, cone membership, and the objective gap. Approximate solutions require an additional numerical error analysis. A tiny floating-point residual is evidence of a good answer, not by itself a mathematical proof of exact feasibility or zero gap.

The unifying benefit of conic duality is clear. LP, second-order cone programs, and SDP share the same weak-duality algebra. Their cones differ, but the language of dual cones and complementary slackness does not. Theorems about strong duality then become precise statements about geometry: whether the feasible affine space reaches the cone's interior, and whether separating functionals can be used without a gap.

## Interior-Point Methods: Central Paths, Barriers, and Newton Systems

Imagine optimizing a linear objective over a polygon. If you could only walk along the edges, you might travel from corner to corner until reaching the best one. But there is another strategy: move through the interior, guided by a function that becomes increasingly costly as you approach the boundary. Gradually reduce that artificial boundary penalty, and the path of minimizers approaches an optimum of the original constrained problem.

This is the central idea behind barrier and interior-point methods. Their importance is not that they always produce fewer arithmetic operations than every alternative algorithm. It is that they turn constraints into a sequence of smooth problems, provide a powerful primal-dual interpretation, and, with suitable barrier geometry, support polynomial-time complexity guarantees.

### A one-dimensional barrier calculation

Minimize x subject to x being at least one. The optimum is plainly x equals one, right on the boundary. For a logarithmic barrier, keep x strictly greater than one and minimize t times x minus the logarithm of x minus one. Here t is a positive parameter controlling how strongly we care about the original objective relative to the barrier.

Differentiate. The derivative is t minus one divided by x minus one. Setting it equal to zero gives x equal to one plus one divided by t. The minimizer remains strictly feasible and approaches one as t grows. Its objective value exceeds the true optimum by exactly one divided by t.

We have obtained a central path explicitly. Each value of t defines an interior point. The path is not a sequence of arbitrary guesses near the optimum; it is a family of minimizers of well-defined smooth problems.

There is a price for remaining interior. The second derivative of the logarithmic barrier is one divided by the square of x minus one. It grows rapidly near the boundary. Newton's method can exploit the curvature, but careless undamped steps may leave the feasible region. Practical interior-point methods control step lengths and use a suitable measure of distance from the central path.

### The barrier for many inequalities

Suppose we want to minimize a convex differentiable function subject to inequality constraints. A logarithmic barrier adds a negative logarithm of each positive slack to the objective. It is defined only in the strict interior, where all slacks are positive. As a slack approaches zero from above, the penalty diverges to positive infinity.

For a problem with m inequality constraints, under standard convexity and constraint-qualification assumptions, the objective gap along a central path can be related to m divided by t. This is a duality-based statement, not a claim that all barrier approximations have the same actual primal error. The bound is derived from constructed dual variables and weak duality.

Increasing t pushes the barrier minimizers closer to constrained optima, but it also changes the conditioning of the Newton system. The art of an interior-point implementation is to advance the parameter at a rate the Newton corrections can track.

### Linear programming in primal-dual form

Consider a standard-form linear program: minimize c dotted with x, subject to A x equals b and x componentwise nonnegative. Its dual maximizes b dotted with y, subject to A transpose y being at most c. Define dual slack s as c minus A transpose y. Dual feasibility requires s to be nonnegative.

At an exact optimum, primal-dual complementarity says x sub i times s sub i equals zero for every coordinate, provided the usual optimality hypotheses hold. A central-path point instead has strictly positive x and s, and replaces each zero product by the same positive parameter mu. In other words, x sub i times s sub i equals mu.

The central-path equations are A x equals b, A transpose y plus s equals c, and x times s equals mu times the all-ones vector, with x and s strictly positive. As mu tends to zero, these equations approach the KKT complementarity conditions. They offer a different view of barrier minimization: it is a continuously perturbed primal-dual optimality system.

The duality gap along such a primal-dual feasible central path is n times mu, where n is the number of nonnegative coordinates. This follows by subtracting the dual objective from the primal objective and using the primal and dual equalities. The gap is the sum of all the x sub i times s sub i products.

That gives an explicit certificate of progress. Because the dual objective is a lower bound on the primal optimum, the gap bounds primal suboptimality. It does not, however, certify feasibility or numerical accuracy by itself unless the equalities and inequalities are actually satisfied to verified tolerances.

### Newton steps for the perturbed KKT system

We rarely solve the central-path equations exactly at each mu. Instead, we linearize them around the current approximate iterate and compute a Newton correction. The linear equations involve the primal residual A x minus b, the dual residual A transpose y plus s minus c, and the complementarity residual consisting of the products x sub i s sub i minus mu.

Solving the Newton system produces directions for x, y, and s. A line search or fraction-to-the-boundary rule chooses a step short enough to keep x and s positive. The algorithm also updates mu to encourage complementarity to shrink. Predictor-corrector variants use information about how the current path might change to improve practical performance.

The main numerical cost is often solving sparse linear systems derived from these Newton equations. Choosing whether to factor a normal-equations matrix or an augmented KKT matrix affects fill-in, conditioning, and stability. A mathematical iteration bound says little by itself about memory use or numerical reliability on a specific problem.

### Self-concordance and predictable steps

Why do logarithmic barriers work so reliably in theory? Their third derivatives are controlled by their second derivatives in a sense called self-concordance. This provides quantitative bounds on how fast the local Hessian geometry can change, so a Newton step that is safe in the current local norm stays meaningful nearby.

For suitable self-concordant barriers and regularity assumptions, path-following algorithms can reach a desired duality gap in a number of Newton iterations scaling with the square root of a barrier parameter times the logarithm of the accuracy requirement. The exact theorem depends on the feasible set, barrier, initialization and arithmetic model. It should not be interpreted as a universal running-time guarantee for every numerical implementation.

This is one of the striking achievements of convex optimization: geometry of the barrier supplies a bridge from local Newton steps to global algorithmic complexity.

### What an optimality report must include

An optimizer may report success because its primal residual, dual residual, and complementarity measure are small. Whether those values prove a claimed mathematical tolerance depends on scaling, conditioning, and the accuracy of the arithmetic. In ill-conditioned problems, small residuals can coexist with large errors in some variables. If strict certification is required, externally checkable primal and dual bounds, possibly supported by interval or rational arithmetic, are a separate stage from the floating-point solver's stopping criterion.

Interior-point methods do not remove the boundary. They organize the approach to it. Logarithmic penalties define a smooth interior geometry, the central path connects that geometry to exact KKT conditions, and primal-dual gaps explain why the iterates are improving. The method's theoretical strength comes from keeping those three layers together: optimization geometry, numerical linear algebra, and a verifiable statement about the remaining gap.

## Verifiable Optimization Certificates: From Solver Output to Proof

An optimization solver can print the word optimal next to a number with many decimal digits. That tells us something about what the solver computed under its tolerances and assumptions. It does not, by itself, provide a proof that no feasible point has a better objective value.

A stronger result is a certificate: a collection of objects that a separate, relatively simple checker can inspect and use to establish a mathematical bound. Convex duality provides a natural source of certificates. Numerical analysis tells us when their verification must account for rounding, constraint residuals, and the conditioning of the problem.

### Upper and lower bounds meet

Consider a minimization problem. Any feasible candidate gives an upper bound on the optimum, because the optimum cannot be worse than a candidate. A valid dual-feasible point gives a lower bound by weak duality. Put the two together, and the true optimum lies in an interval.

If the bounds coincide, the candidate is optimal. If they differ by a small amount, we have a quantitative optimality gap. This conclusion does not require us to trust the internal iteration history of a solver. We need only verify feasibility of the candidate, feasibility of the dual object, and the objective values.

For linear programming, this can become an exact arithmetic proof. Suppose the objective is to minimize x plus y, where both variables are nonnegative, and x plus twice y must be at least four. The feasible point x equals zero, y equals two has cost two.

Now multiply the constraint x plus twice y at least four by one half. We obtain half x plus y at least two. Since x is nonnegative, x plus y is at least half x plus y. Therefore every feasible objective is at least two. We have a lower bound of two and a feasible point with objective two. The optimum is exactly two.

This proof is tiny, but it contains the essence of dual certification. The half is a nonnegative multiplier on the inequality. Its combination of constraints is dominated by the objective coefficients. The resulting weighted constraint supplies a lower bound equal to the candidate's cost.

### Separate discovery from verification

A numerical optimizer might discover the candidate and its dual multiplier using thousands of iterations, matrix factorizations, or heuristic choices. The checker only needs to verify a handful of inequalities. The process that finds a certificate can be complex; the process that validates it can be simple.

For an exact rational linear program, we can represent the proposed primal and dual variables as rational numbers, then check the linear inequalities and equalities with exact integer arithmetic after clearing denominators. If those checks pass, weak duality gives an exact interval for the optimum. This is the useful distinction between a numerical guess and a proof-carrying result.

But many solvers return floating-point numbers. A reported zero residual may mean a quantity was smaller than a tolerance, not that it was mathematically zero. A variable printed as zero may actually be slightly negative. And a dual inequality evaluated with rounding may have the opposite sign from its exact mathematical value.

A numerical certificate is therefore not complete until we understand how feasibility is checked. We can sometimes round solver output to rational numbers and verify those numbers exactly. In other problems we use interval arithmetic with outward rounding to enclose every relevant expression. If the enclosure proves an inequality has the required sign, the certificate is established. If the interval crosses zero, the checker must report uncertainty, refine the computation, or find a different certificate. It must not quietly assume the sign.

### Infeasibility can also be certified

Optimality is not the only claim worth checking. Suppose a system of linear equations asks for a nonnegative vector x satisfying A times x equals b. An appropriate vector y can prove that no such x exists.

Specifically, if every component of A transposed times y is nonnegative but the dot product of b with y is negative, then any feasible nonnegative x would give a contradiction. On one hand, the dot product b with y equals x dotted with A transposed y, which would be nonnegative. On the other hand, the proposed certificate says it is negative.

For the simplest example, suppose x must be nonnegative but also equal negative one. Take the single equation x equals negative one and the multiplier y equal one. The coefficient side is nonnegative while the right-hand side multiplier is negative, so infeasibility follows immediately.

Such a witness is an instance of Farkas' lemma. The general lesson is that a solver may report no solution, but a certificate makes the absence of solutions a verifiable algebraic statement.

### Positive semidefinite certificates

Semidefinite programming replaces scalar inequalities with constraints that matrices are positive semidefinite. The duality principle is similar, but a checker must verify that certain symmetric matrices really have no negative quadratic directions.

For instance, the matrix with diagonal entries one and off-diagonal entries negative one is positive semidefinite. We can verify it exactly by observing that its quadratic form on a vector with coordinates a and b equals the square of a minus b. Every real square is nonnegative. This is a proof, not a floating-point eigenvalue estimate.

For larger matrices, one might verify an exact factorization or use carefully bounded spectral estimates. Positive definiteness, where all eigenvalues are strictly positive, can be numerically easier to certify when there is a known gap above zero. Semidefiniteness on the boundary is harder: an eigenvalue very close to zero may be slightly positive or slightly negative, and ordinary floating-point rounding can conceal the distinction.

Conic duality also requires proper attention to primal and dual feasibility. A tiny reported duality gap does not establish an optimum if either proposed point violates its constraints. A solver may use scaled residuals and stopping tolerances, while a mathematical claim concerns the original unscaled problem. Verification must return to that original formulation.

### Does a narrow objective gap locate the optimizer?

Even a rigorous objective-value interval does not always imply that the optimizer's coordinates are accurately determined. A nearly flat objective may have many widely separated points with almost identical cost. Strong convexity is one condition that connects objective error to distance.

If a differentiable objective is strongly convex with positive parameter mu, then a feasible candidate whose objective value is at most delta above the optimum lies within a distance proportional to the square root of delta divided by mu from the unique optimizer, under the standard convex-feasible-set hypotheses. A small mu makes this bound weak. Without an appropriate curvature or error-bound assumption, a tiny duality gap alone gives no comparable distance guarantee.

This distinction echoes condition numbers in numerical linear algebra. One must ask what has actually been certified: the value of the optimum, feasibility of the point, a distance to a minimizer, or sensitivity to perturbations in the problem data. Those are different mathematical conclusions.

### A trustworthy workflow

The strongest practical pattern separates the roles of discovery and proof. First use an effective numerical solver to find promising primal and dual candidates. Then export a well-specified certificate containing the original problem data, candidate variables, constraints, objective values, and precision assumptions. Finally run an independent checker that verifies the relevant inequalities in exact arithmetic or with justified enclosures.

If verification fails, that does not always mean the proposed solution is poor. It may mean that the reported precision is insufficient or that the certificate needs repair. Conversely, successful verification certifies the stated mathematical model, not automatically the accuracy of the model relative to the physical or economic system it represents.

Optimization becomes much more reliable when we ask not merely what number a solver printed, but what mathematical evidence the number came with. A certificate converts a complicated computation into a simple claim another system can check. The boundary between heuristic numerical confidence and proof is where feasible bounds and justified arithmetic meet.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Semidefinite Programming: Optimizing over Positive Matrices

**Track:** Optimization, Convexity, and Duality. **Background:** convexity, linear-programming duality, symmetric matrices. **Question:** how can a matrix inequality express infinitely many quadratic inequalities, and how does a dual matrix certify an optimum?

#### Mathematical companion (not spoken)

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

##### Exercises with answers

1. Is \(\begin{pmatrix}1&-2\\-2&1\end{pmatrix}\) positive semidefinite? **Answer:** no; its eigenvalues are three and negative one.
2. Is entrywise nonnegativity necessary for positive semidefiniteness? **Answer:** no; \(\begin{pmatrix}1&-1\\-1&1\end{pmatrix}\succeq0\).
3. Explain the duality gap in the worked example. **Answer:** the primal and dual objectives both equal two, so the gap is zero.
4. Why does dropping the rank-one constraint enlarge the lifted Boolean feasible set? **Answer:** positive semidefiniteness and unit diagonal also allow Gram matrices of higher-dimensional unit vectors.

##### Reading

Stephen Boyd and Lieven Vandenberghe, [Convex Optimization](https://web.stanford.edu/~boyd/cvxbook/), semidefinite programming and duality; Lieven Vandenberghe and Stephen Boyd, [Semidefinite Programming](https://web.stanford.edu/~boyd/papers/sdp), *SIAM Review* 38(1), 1996.

### Conic Duality: One Language for Linear, Quadratic, and Matrix Inequalities

**Track:** Optimization and Duality. **Background:** convex cones, linear programming, Lagrangians, KKT conditions, semidefinite programming. **Central question:** how can different kinds of convex constraints share one duality theorem and one style of optimality certificate?

#### Mathematical companion (not spoken)

Let \(K\subset\mathbb R^n\) be a nonempty closed convex cone with \(K^*=\{s:\langle s,x\rangle\ge0\ \forall x\in K\}\). In a standard equality-form convention,
\[\text{(P)}\quad\inf\{c^Tx:Ax=b,\ x\in K\},\qquad\text{(D)}\quad\sup\{b^Ty:c-A^Ty\in K^*\}.\]
For feasible \(x,y\), \(c^Tx-b^Ty=\langle x,c-A^Ty\rangle\ge0\): weak duality. When both attain a common value, \(\langle x,c-A^Ty\rangle=0\) (complementarity). A standard sufficient strong-duality qualification is primal strict feasibility \(Ax=b\) with \(x\in\operatorname{int}K\), together with finite primal optimal value; then the dual optimum is attained and values coincide (nondegenerate finite-dimensional setting).

**Three cones:**
\[\mathbb R_+^n=(\mathbb R_+^n)^*,\quad\mathcal Q_{m+1}=\{(t,u):t\ge\|u\|_2\}=\mathcal Q_{m+1}^*,\quad\mathbb S_+^m=(\mathbb S_+^m)^*\ \text{under}\ \langle X,S\rangle=\operatorname{tr}(XS).\]
**Norm duality example:** \(\|a\|_2=\min\{t:(t,a)\in\mathcal Q_{m+1}\}=\max\{a^Ty:\|y\|_2\le1\}\). The upper bound is Cauchy–Schwarz; for \(a\ne0\), \(y=a/\|a\|\) attains it.

**Certificate caution:** small numerical residuals are not exact feasibility certificates. A primal–dual feasible pair yields upper/lower bounds, while strict feasibility is a sufficient theorem hypothesis, not a necessary one. Nonclosed conic images can produce duality gaps or weak infeasibility even for a closed cone.

##### Exercises with answers

1. Derive weak duality for equality-form conic programs. **Answer:** use \(Ax=b\) to rewrite the gap as \(\langle x,c-A^Ty\rangle\ge0\).
2. Why is the Lorentz cone self-dual? **Answer:** Cauchy–Schwarz shows \((t,u)\cdot(s,v)\ge ts-\|u\|\|v\|\ge0\) for cone members; testing extremal unit directions proves the converse.
3. If a primal and dual feasible pair has equal objectives, what follows even without Slater? **Answer:** both are globally optimal, because weak duality sandwiches every feasible objective.
4. Is Slater necessary for a zero duality gap? **No:** strict feasibility is sufficient under stated finiteness conditions, not necessary.

##### Reading and source notes

- Stephen Boyd and Lieven Vandenberghe, [*Convex Optimization*](https://web.stanford.edu/~boyd/cvxbook/), dual cones, constraint qualifications, and Slater's condition.
- Lieven Vandenberghe and Stephen Boyd, [*Semidefinite Programming*](https://web.stanford.edu/~boyd/papers/sdp), self-dual PSD cone and primal-dual conditions.
- [Boyd et al., *Conic Optimization via Operator Splitting and Homogeneous Self-Dual Embedding*](https://web.stanford.edu/~boyd/papers/pdf/scs.pdf), conic standard forms and numerical feasibility/optimality residuals.

### Interior-Point Methods: Central Paths, Barriers, and Newton Systems

**Track:** Optimization, Convexity, and Duality. **Background:** convexity, linear-programming duality, Newton's method, KKT conditions. **Central question:** how can a constrained optimizer approach the boundary of a feasible region while staying strictly inside it?

#### Mathematical companion (not spoken)

For \(x>1\), the barrier objective \(\phi_t(x)=t x-\log(x-1)\) has derivative \(t-1/(x-1)\) and minimizer \(x_t=1+1/t\). The original optimum is \(1\), with barrier primal gap \(1/t\).

For standard-form LP
\[
\begin{aligned}
\text{(P)}\quad &\min c^\top x &&\text{s.t. }Ax=b,\ x\ge0,\\
\text{(D)}\quad &\max b^\top y &&\text{s.t. }A^\top y+s=c,\ s\ge0,
\end{aligned}
\]
central-path equations at \(\mu>0\) are
\[
Ax=b,\quad A^\top y+s=c,\quad Xs=\mu\mathbf1,\quad x>0,s>0,
\]
with diagonal \(X=\operatorname{diag}(x)\). If these equations hold, the feasible primal-dual gap is
\[
c^\top x-b^\top y=x^\top s=n\mu.
\]
The Newton linearization for residuals \(r_p=Ax-b\), \(r_d=A^\top y+s-c\), \(r_c=Xs-\mu\mathbf1\) is
\[
A\Delta x=-r_p,\quad A^\top\Delta y+\Delta s=-r_d,\quad
S\Delta x+X\Delta s=-r_c.
\]
A damped step must preserve \(x+\alpha\Delta x>0\) and \(s+\alpha\Delta s>0\). Under suitable self-concordant barrier and feasibility hypotheses, path-following iteration complexity scales as \(O(\sqrt\nu\log(\nu/\varepsilon))\), with \(\nu\) the barrier parameter; this is not a generic floating-point runtime bound.

##### Exercises with answers

1. Find the one-dimensional central-path point when \(t=10\). **Answer:** \(x=1.1\), with objective gap \(0.1\).
2. For a central-path LP with four nonnegative coordinates and \(\mu=0.01\), what is its duality gap? **Answer:** \(n\mu=0.04\), assuming exact primal and dual feasibility.
3. Why can a full Newton step be unacceptable? **Answer:** it may violate strict positivity of primal or dual slacks.
4. Does a small numerical duality gap alone certify an exact solution? **No:** independently controlled feasibility, rounding, and conditioning also matter.

##### Reading and source notes

- Stephen Boyd and Lieven Vandenberghe, [*Convex Optimization*](https://web.stanford.edu/~boyd/cvxbook/), Chapter 11: Interior-point methods.
- Boyd and Vandenberghe, [Convex Optimization lecture slides](https://web.stanford.edu/~boyd/cvxbook/bv_cvxslides.pdf), central path and Newton equations.

### Verifiable Optimization Certificates: From Solver Output to Proof

**Track:** Optimization, Convexity, and Duality. **Background:** linear and semidefinite programming, weak duality, and numerical conditioning. **Central question:** when does a numerical optimum become an independently checkable mathematical claim?

#### Mathematical companion (not spoken)

**Primal and dual LP.** Consider
\[
\begin{aligned}
(P)\quad &\min_{x\ge0} c^Tx\quad\text{subject to }Ax\ge b,\\
(D)\quad &\max_{\lambda\ge0} b^T\lambda\quad\text{subject to }A^T\lambda\le c.
\end{aligned}
\]
For any primal-feasible \(x\) and dual-feasible \(\lambda\),
\[
b^T\lambda\le\lambda^TAx=x^TA^T\lambda\le c^Tx.
\]
Thus \(b^T\lambda\le p^*\le c^Tx\), with a certified gap \(c^Tx-b^T\lambda\) when all feasibility and arithmetic checks are rigorous.

**Exact worked certificate.** Let \(c=(1,1)\), \(A=(1,2)\), \(b=4\), \(x=(0,2)\), \(\lambda=1/2\). Then \(Ax=4\), \(x\ge0\); \(A^T\lambda=(1/2,1)\le c\), \(\lambda\ge0\); both objectives are \(2\). The optimum is exactly \(2\).

**Farkas-type infeasibility.** If \(Ax=b\), \(x\ge0\) and some \(y\) satisfies \(A^Ty\ge0\) and \(b^Ty<0\), then feasibility is impossible, since \(b^Ty=x^TA^Ty\ge0\). Example: \(A=(1)\), \(b=-1\), \(y=1\).

**PSD witness.** \(S=\begin{psmallmatrix}1&-1\\-1&1\end{psmallmatrix}\succeq0\) because \((a,b)S(a,b)^T=(a-b)^2\ge0\). This is an exact nonnegativity certificate without approximate eigenvalues.

**Objective vs solution error.** If \(f\) is \(\mu\)-strongly convex on a convex feasible domain, \(\mu>0\), with minimizer \(x^*\), then \(f(x)-f(x^*)\ge\frac\mu2\|x-x^*\|^2\). A rigorous gap bound \(f(x)-f(x^*)\le\delta\) gives \(\|x-x^*\|\le\sqrt{2\delta/\mu}\). Without suitable curvature, objective accuracy need not imply location accuracy.

##### Exercises with answers

1. Verify \(x=(0,2)\), \(\lambda=1/2\) in the worked LP. **Answer:** all sign and linear constraints hold exactly, both objective values equal two.
2. If a duality gap is numerically tiny but the dual multiplier violates feasibility, is it a proof of optimality? **No:** weak duality applies to feasible certificates.
3. What proves a PSD matrix \(S\succeq0\) exactly? **Answer:** for example, a verified decomposition \(S=B^TB\) over exact arithmetic, or another justified positivity argument.
4. Does a gap of \(10^{-6}\) guarantee the optimizer is within \(10^{-6}\) in Euclidean distance? **No:** that requires additional quantitative assumptions, such as strong convexity with known parameter.

##### Reading and source notes

- Stephen Boyd and Lieven Vandenberghe, [Convex Optimization](https://web.stanford.edu/~boyd/cvxbook/), Chapter 5 on dual lower bounds, certificates, and suboptimality gaps.
- JuMP documentation, [Tolerances and numerical issues](https://jump.dev/JuMP.jl/stable/tutorials/getting_started/tolerances/), solver feasibility tolerances and reporting.
