# 071000 - Quantum Connections, Monodromy, and Stokes Matrices

**Track:** Abstract Algebra. **Background:** quantum cohomology, differential equations with regular and irregular singularities, and analytic continuation. **Central question:** what extra structure appears when quantum multiplication is treated as a differential equation?

<!-- BEGIN SPOKEN LECTURE -->

# Multiplication becomes transport

Ordinary cohomology gives a ring of topological classes. Quantum cohomology modifies that multiplication by counting curves. One might think the story ends once all multiplication tables are known. But a ring that varies with parameters can be regarded as a family, and a family invites us to ask how vectors change as the parameters move.

This leads to the quantum connection. It is a differential equation built from quantum multiplication. Its flat sections record how cohomology classes are transported through the parameter space. Around a closed loop, a flat section need not return unchanged; its transformation is called monodromy. At an irregular singularity, even the asymptotic series used to represent a solution can change when we cross certain rays. These jumps are encoded by Stokes matrices.

We will see all three ideas in the quantum cohomology of the projective line. That example is small enough to calculate by hand, but rich enough to display the distinction between classical monodromy and irregular Stokes behavior.

# The projective line has a two-dimensional cohomology

The complex projective line has a unit class and a degree-two class, conventionally called H. In ordinary cohomology, multiplying H by itself gives zero because there is no degree-four cohomology. Quantum cohomology changes this: multiplying H by H gives a parameter q times the unit. The parameter records a degree-one rational curve contribution.

In the basis consisting of the unit and H, multiplication by H is a two-by-two matrix. It sends the unit to H and sends H to q times the unit. As q changes, this matrix changes. A quantum differential equation asks for a vector-valued function whose logarithmic derivative in q is given, up to a scale z, by this multiplication matrix.

The new variable z has an important role. It controls the semiclassical or asymptotic regime of the connection. Holding q away from zero and letting z approach zero makes the equation rapidly varying. Holding z fixed and moving q around zero instead reveals ordinary local monodromy. Confusing these two limits is a common source of mistaken statements about the singularities.

# A scalar equation hides inside the matrix equation

Write a flat section as a(q) times the unit plus b(q) times H. Quantum multiplication gives two coupled differential equations. The logarithmic derivative of a is proportional to q times b, and the logarithmic derivative of b is proportional to a. Eliminate a. Then b satisfies a second-order scalar equation in which the square of the logarithmic derivative is multiplication by q, with z-squared as the scale.

A power-series solution can be found without any general theory. Suppose b is a sum of coefficients times successive powers of q. Applying the logarithmic derivative twice multiplies the coefficient of q to the d by d squared. Consequently the recurrence says the coefficient at degree d is the preceding coefficient divided by z squared times d squared.

Starting at one, we obtain the series one plus q over z squared plus q squared over four z to the fourth, and so on. In general the coefficient is one divided by the square of d factorial and by z to the power two d. This is a familiar Bessel-type hypergeometric series. Its appearance is not a numerical accident: enumerative curve counting has produced a differential equation whose solutions are special functions.

# Walking once around q equal to zero

At q equal to zero, the scalar equation has a regular singular point with repeated exponent zero. One solution is the power series we just derived. A second linearly independent local solution has a logarithm of q times the first solution plus a regular series.

Move q once counterclockwise around the origin. The ordinary power-series solution returns to itself. The logarithm, however, gains two pi times the imaginary unit. Thus the logarithmic solution is shifted by a constant multiple of the analytic solution. Relative to a suitable basis, the monodromy is unipotent: its diagonal entries are one, and one off-diagonal entry is nonzero.

This is monodromy in the parameter q, and it follows from analytic continuation around a regular singularity. We have not yet encountered a Stokes matrix. The distinction matters because not every nontrivial continuation of a solution is a Stokes phenomenon.

# What changes when z is small

Now keep q nonzero. Quantum multiplication by H has two eigenvalues: plus and minus the square root of q. In the small-z regime, the associated exponential factors have leading behavior involving plus and minus two square roots of q divided by z. They grow or decay at dramatically different rates in different angular sectors of the z-plane.

Asymptotic solutions built around these exponentials generally have divergent formal expansions. Within a sector, a suitable analytic solution matches one chosen asymptotic expansion. Rotate the sector across a Stokes ray and the preferred analytic basis may jump by a triangular matrix. That matrix records how exponentially small contributions become visible relative to dominant ones.

The underlying flat connection did not suddenly become discontinuous. Rather, the sectorial bases adapted to asymptotic growth changed. Stokes matrices relate those bases. Their entries depend on the normalization and ordering of the eigenvalue sectors, so quoting a numerical Stokes matrix without specifying conventions is incomplete.

# Why geometry determines analytic data

In the semisimple regime of a Frobenius manifold, quantum multiplication is diagonalizable at a generic parameter value. Its eigenvalues provide local canonical coordinates. The corresponding quantum connection has rich asymptotic structure, with Stokes matrices, central connection matrices, and monodromy data.

In favorable geometric examples, those analytic invariants can be related to intersection pairings and derived-category data. Such correspondences are powerful, but they require hypotheses, choices of exceptional collections, and normalization conventions. It would be wrong to claim that every quantum cohomology ring automatically carries the same fixed Stokes matrix.

The projective line makes the principle concrete. A relation in a tiny quantum ring leads to a Bessel-type differential equation. Its logarithmic solution creates unipotent monodromy around a parameter singularity. Its distinct small-z exponential scales create Stokes jumps. Thus the same multiplication law has algebraic, topological, and asymptotic interpretations.

# What a connection knows beyond a ring

A ring gives rules for multiplying elements at a specified parameter. A flat connection gives a rule for transporting them, for comparing solutions along paths, and for extracting global analytic information from local equations. Once curve counts enter quantum multiplication, those counts control differential equations, and the differential equations generate monodromy and Stokes data.

This provides one of the cleanest examples of a theme running through modern geometry: enumerative information can be translated into differential equations, and the singularities of those equations can reveal structure not visible from a single multiplication table.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For `QH^*(P^1)=C[H,q]/(H^2-q)` in basis `(1,H)`, `H*` has matrix
\[
M(q)=\begin{pmatrix}0&q\\1&0\end{pmatrix}.
\]
Using the convention `z D s=M(q)s`, `D=q d/dq` and `s=a(q)1+b(q)H`, we obtain `z D a=q b`, `z D b=a` and hence
\[
 (zD)^2 b=q b,\qquad b_0(q,z)=\sum_{d\ge0}\frac{q^d}{(d!)^2z^{2d}}.
\]
The recurrence is `z^2 d^2 c_d=c_(d-1)`. At q=0 the repeated exponent zero yields a logarithmic second solution, so monodromy around q=0 is unipotent. With q nonzero, the eigenvalues of M are `+sqrt(q)` and `-sqrt(q)`; their WKB exponentials, after integrating `d log(q)`, are locally `exp(+/- 2 sqrt(q)/z)` to leading order. Stokes matrices arise from sectorial asymptotics as `z->0`, not from the mere existence of regular-singular monodromy at q=0.

The sign convention for the connection and direction of analytic continuation changes certain matrices. State conventions before asserting particular Stokes matrix entries.

### Exercises with answers

1. Find the eigenvalues of multiplication by H. **Answer:** `+sqrt(q)` and `-sqrt(q)`.
2. Compute the coefficient of `q^3` in the normalized power-series solution. **Answer:** `1/(36 z^6)`.
3. What happens to `log(q)` after one positive loop around q=0? **Answer:** it increases by `2*pi*i`.
4. Why is this logarithmic monodromy not itself a Stokes jump? **Answer:** it is analytic continuation around a regular singularity in q, rather than sectorial asymptotic switching in the small-z irregular problem.

### Reading and source notes

- [Dubrovin, Geometry of 2D Topological Field Theories](https://arxiv.org/abs/hep-th/9407018), Frobenius manifolds, quantum connections, monodromy and Stokes data.
- [Givental, A Mirror Theorem for Toric Complete Intersections](https://arxiv.org/abs/alg-geom/9701016), hypergeometric solutions and enumerative geometry.
- [Givental, Equivariant Gromov-Witten Invariants](https://arxiv.org/abs/alg-geom/9603021), quantum differential equations and asymptotic structure.
