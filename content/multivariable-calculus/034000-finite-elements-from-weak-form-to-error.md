# Finite Elements: From a Weak Equation to a Matrix and an Error Bound

**Track:** Multivariable Calculus from First Principles. **Focus:** piecewise-linear trial spaces, stiffness assembly, Ritz–Galerkin orthogonality, exact energy errors, and numerical limitations.

<!-- BEGIN SPOKEN LECTURE -->

# Finite Elements: From a Weak Equation to a Matrix and an Error Bound

We have reached a practical question. A weak equation asks an unknown function to satisfy an integral identity for every admissible test function. A computer cannot hold an arbitrary function or check infinitely many tests. Yet it can solve a finite system of linear equations, often very efficiently. How do we turn one problem into the other without discarding the mathematics that made the weak equation reliable?

The finite-element method answers by choosing a finite-dimensional space of functions and requiring the weak equation to hold for every test function in that space. The basis functions are local: each is nonzero only on a few neighboring pieces of a mesh. This locality produces sparse matrices. More importantly, the relationship between the continuous and discrete weak equations gives us a way to measure error that is not just trial and error.

We will assemble a complete example by hand: a string or one-dimensional Poisson problem on the interval from zero to one, under uniform load, with both endpoint values fixed at zero. Then we will compare the computed piecewise-linear solution with the exact curved solution and calculate the energy error exactly.

## A weak equation a computer can approach

The continuous problem is negative u double prime equals one, with u at both endpoints equal to zero. Its weak form says the integral of u prime times v prime equals the integral of v for every zero-endpoint test function v. We know the exact solution: u of x equals one half times x times one minus x. It is a parabola. Our numerical method will deliberately use only straight segments, so we should expect some approximation error between its nodes.

Divide the unit interval into three equal elements. There are four mesh nodes: zero, one third, two thirds, and one. We will build continuous functions that are linear separately on each element. The boundary values at zero and one are fixed, so only the heights at the two interior nodes are unknown. Call them U one and U two.

For each interior node, construct a hat function. The first hat is one at x equal to one third, zero at all other nodes, and linear on each element. It rises from zero to one over the first element, falls back to zero over the second, and stays zero on the third. The second hat is its shifted counterpart, supported on the last two elements. Both vanish at the prescribed boundary nodes, so every linear combination satisfies the endpoint constraints.

Our approximate function u sub h is U one times the first hat plus U two times the second. We have replaced infinitely many possible shapes by a two-dimensional family. That restriction is the approximation decision. We are not changing the physical source or the weak equation's basic integral form.

We now demand the weak identity only for test functions in this two-dimensional space. It is enough to demand it separately for each hat. Any other test in the space is a linear combination of them, and the weak equation is linear in the test function. Thus two scalar equations determine the two unknown coefficients.

## Assemble the stiffness matrix

Take one element, of length h, with a linear function whose values at its ends are A and B. Its slope is constant, equal to B minus A divided by h. On that element, the squared-slope energy becomes one half times the square of B minus A divided by h. This simple local expression is the foundation of the stiffness matrix.

Equivalently, the two local hat derivatives are negative one divided by h and positive one divided by h. Integrating their pairwise products gives a two-by-two local matrix. Its diagonal entries are one divided by h, and its off-diagonal entries are negative one divided by h. The matrix penalizes differences between neighboring nodal values, which is precisely what squared slope means for a straight segment.

To assemble the global matrix, add each element's contributions to the entries associated with its endpoints. A node shared by two elements receives contributions from both. The prescribed boundary nodes do not become unknown coordinates; their known values would be moved to the right-hand side if they were nonzero.

Here h is one third, so one divided by h is three. Each interior node belongs to two elements, giving a diagonal entry of six. The two interior hats overlap on the middle element, giving an off-diagonal entry of negative three. The stiffness matrix therefore has six, negative three in its first row, and negative three, six in its second row.

The right-hand side comes from the applied source. Since the source is the constant one, each load entry is simply the integral of one interior hat over the interval. A hat is two triangles of width one third and height one; together their area is one third. Both load entries are one third.

Our full two-by-two system is now easy to state. Six U one minus three U two equals one third. Negative three U one plus six U two equals one third. By symmetry the coefficients are equal, and either equation gives three times that common value equals one third. Thus U one and U two are both one ninth.

The finite-element solution is a straight line rising to one ninth at x equal to one third, level between the two interior nodes, and descending to zero at x equal to one. It is a trapezoid with a flat top, not the smooth parabola we began with. Its second derivative is zero inside each element, so it certainly does not satisfy negative u double prime equals one pointwise there.

That observation is not a contradiction. We asked it to satisfy the weak equation against the two hat functions, not the original strong equation at every point. In fact the pointwise strong residual on each element does not even tell the full story, because the slope jumps at the nodes. The discrete weak residual vanishes on the chosen test space, which is exactly what the method was designed to achieve.

## A fortunate property of this example

Evaluate the exact parabola at the interior nodes. At one third, one half times one third times two thirds is one ninth. At two thirds, the same calculation again gives one ninth. Our finite-element solution happens to match the exact solution at all the nodes. It is therefore the piecewise-linear interpolant of the exact solution on this particular mesh.

This is a special property of this one-dimensional constant-load problem. It does not mean finite-element nodal values are generally exact. Change the equation, the basis, the geometry, or the assumptions, and the numerical nodal values may differ from the true solution. The right interpretation is that we have an exactly soluble example in which approximation error is isolated between the nodes, making it especially good for understanding the method.

We can now compute that error rather than just sketch it.

## Galerkin orthogonality and best approximation

Call the exact solution u and the finite-element solution u sub h. Because u satisfies the weak equation for every admissible test, it satisfies it for both hats. Because u sub h satisfies the discrete equation, it also satisfies it for both hats. Subtracting the two equations gives a precise identity: the integral of the derivative of u minus u sub h times the derivative of any finite-element test function is zero.

This is Galerkin orthogonality. The error is orthogonal to the discrete trial space, but not under the ordinary dot product of its nodal values. Orthogonality here is measured by the integral of the product of derivatives. That is the energy inner product determined by our variational problem.

The geometric meaning is the same as orthogonal projection in linear algebra. If a vector is projected onto a subspace, the error is perpendicular to the subspace, and the projection is the closest point in the relevant norm. Here functions play the role of vectors and the derivative-energy inner product plays the role of the dot product. The finite-element solution is the best approximation to the exact solution among our continuous piecewise-linear, zero-boundary functions, measured by the square root of the integrated squared error in slope.

This best-approximation statement depends on the form being symmetric and coercive, so that it genuinely defines an energy inner product. For a more general bounded and coercive, possibly nonsymmetric bilinear form, an analogous result is Céa's lemma: the error is bounded by a stability constant times the best error available in the discrete space. A familiar bound uses the continuity constant divided by the coercivity constant. That constant matters; not every stable problem yields an exact orthogonal projection in its original norm.

The key separation is between approximation and solution. The finite-dimensional space limits the accuracy we can hope for, even with perfect arithmetic. Solving the matrix equation inaccurately introduces a second, algebraic error. An implementation may introduce further errors from numerical integration or imperfect representation of a curved domain. These have different causes and should not be conflated.

## Calculate the energy error exactly

For our parabola, the derivative is one half minus x. Our piecewise-linear solution has constant slope one third on the first element, zero on the second, and negative one third on the third. On every element, the finite-element slope equals the average slope of the exact parabola over that element.

Think about one element of length h. The difference between the exact slope, which decreases linearly, and its average slope is simply minus the distance from the element's midpoint. The integral of the square of that difference over the element is h cubed divided by twelve. There are three elements, each of length one third. Adding their contributions gives three times one twenty-seventh divided by twelve, or one divided by one hundred eight.

Thus the squared energy-norm error is exactly one over one hundred eight. The energy-norm error itself is one divided by the square root of one hundred eight. We can also write the squared error as h squared divided by twelve for this uniform-mesh example. Halving h would halve the energy-norm error, because the error scales linearly with element width for this specific smooth quadratic solution.

That calculation makes a convergence claim concrete. It is not proof that every finite-element problem converges at the same rate. Error orders depend on the regularity of the exact solution, polynomial degree, mesh quality, and formulation. A solution with a corner at a material interface can behave differently if the mesh fails to align with the interface. A higher-order basis can do better on smooth problems, but it also changes the discrete space and its numerical costs.

## How the same assembly handles an interface

Recall the two-material example: stiffness one on the left half, two on the right, with u equal to zero at the left and one at the right, and no distributed load. Use a mesh consisting of exactly those two halves. There is one interior unknown at the material interface.

The stiffness contributed by the left element is material stiffness divided by element length: one divided by one half, or two. The right element contributes two divided by one half, or four. Together the diagonal stiffness for the interface node is six. Because the right boundary value is one, its known contribution supplies a right-hand side of four. The interior equation gives six times the unknown interface height equals four, so the height is two thirds.

That is exactly the weak solution from the previous lecture. The first element's slope is four thirds and the second's is two thirds. Once again the weighted flux is continuous, while the ordinary slope is not. Local element matrices and the shared node enforce the transmission condition through assembly. We did not need to insert an artificial equality of slopes.

In two and three dimensions, the geometric elements are typically triangles or tetrahedra, or other mesh cells selected for the problem. Basis functions have gradients on each cell; stiffness entries integrate dot products of those gradients, weighted by material coefficients when appropriate. Their overlap pattern creates the sparse matrix. Boundary values, sources, and fluxes enter through the variational formulation and its load terms. The simple two-by-two example contains the essential algebra of the larger method.

## Accuracy and conditioning are separate questions

As a mesh becomes finer, its function space can approximate more detailed behavior. But the stiffness matrix also changes. For the one-dimensional uniform mesh with piecewise-linear hats, its condition number in the ordinary Euclidean coefficient norm grows on the order of the inverse square of the mesh width. A smaller discretization error does not automatically mean an easier linear system.

This is why finite-element software needs both approximation theory and numerical linear algebra. One asks how closely a trial space can represent a smooth or singular solution. The other asks how accurately and economically the resulting matrix system can be solved. Cholesky factorization, conjugate gradients, and preconditioning from the linear-algebra bridge are useful here, when their assumptions hold. In larger systems, the mesh geometry and coefficient contrasts affect solver design.

The method also inherits the original mathematical problem's limitations. If the weak problem is not coercive, a positive-definite stiffness solve may not be available. If constraints leave an undetermined constant, the matrix can be singular. If boundary or interface terms are mishandled, the discrete equations may represent the wrong physical model no matter how accurately the linear solver runs.

## From an energy to an algorithm

We started with an infinite-dimensional minimization problem. We chose a discrete space, assembled a matrix from local derivative interactions, solved for nodal coefficients, and proved an exact energy-error formula in a case where the continuous solution was known. Galerkin orthogonality explains why the discrete solution is the best energy approximation in its space; coercivity explains why the underlying problem and discrete system are well posed.

This is the bridge from variational calculus to numerical PDEs: not merely replacing derivatives by differences, but preserving an integral balance and its energy geometry while restricting the number of degrees of freedom. From here, the natural extensions are higher-dimensional meshes, richer element spaces, adaptive refinement, and the distinction between a small residual and a reliable error estimate.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not narrated)

### Hat functions and the full two-by-two system

For \(-u''=1\) on \((0,1)\), with \(u(0)=u(1)=0\), let nodes be \(x_j=jh\), \(j=0,1,2,3\), \(h=1/3\). For \(i=1,2\), let \(\phi_i\) be the continuous piecewise-linear hat with \(\phi_i(x_j)=\delta_{ij}\) for interior nodes and zero endpoint values. Seek

\[
u_h=U_1\phi_1+U_2\phi_2,\qquad
\int_0^1u_h'\phi_i'\,dx=\int_0^1\phi_i\,dx.
\]

The element stiffness for an interval of length \(h\) is

\[
K^{(e)}=\frac1h\begin{bmatrix}1&-1\\-1&1\end{bmatrix}.
\]

After assembly and elimination of the zero Dirichlet endpoint variables,

\[
K=\begin{bmatrix}6&-3\\-3&6\end{bmatrix},\quad
b=\begin{bmatrix}1/3\\1/3\end{bmatrix},\quad
U=K^{-1}b=\begin{bmatrix}1/9\\1/9\end{bmatrix}.
\]

The eigenvalues of \(K\) are \(3\) and \(9\), so its spectral condition number is \(3\).

### Exact Galerkin error and special nodal coincidence

The classical solution \(u(x)=x(1-x)/2\) satisfies \(u(1/3)=u(2/3)=1/9\), so in this particular example \(u_h=I_hu\), its piecewise-linear nodal interpolant. On each uniform element \(I_j\) of length \(h\) with midpoint \(m_j\),

\[
u'(x)=\frac12-x,\qquad u_h'|_{I_j}=\frac1h\int_{I_j}u'(x)\,dx=\frac12-m_j.
\]

Thus \(u'-u_h'=-(x-m_j)\) on \(I_j\). Therefore,

\[
\|u-u_h\|_a^2=\int_0^1|u'-u_h'|^2\,dx
=\sum_{j=1}^3\frac{h^3}{12}
=\frac{h^2}{12}=\frac1{108},
\qquad \|u-u_h\|_a=\frac1{\sqrt{108}}.
\]

Here \(a(w,v)=\int_0^1w'v'\,dx\). This nodal coincidence does **not** hold for general equations or meshes; the energy error remains nonzero despite exact nodal values.

### Galerkin orthogonality, energy best approximation, and Céa

If \(a(u,v)=\ell(v)\) for all \(v\in V\), and \(a(u_h,v_h)=\ell(v_h)\) for all \(v_h\in V_h\subset V\), then

\[
a(u-u_h,v_h)=0\quad\forall v_h\in V_h.
\]

For symmetric positive definite \(a\), Pythagoras in the energy inner product gives

\[
\|u-v_h\|_a^2=\|u-u_h\|_a^2+\|u_h-v_h\|_a^2
\quad\forall v_h\in V_h,
\]

so \(u_h\) is the best energy-norm approximation. For a general bounded coercive bilinear form on \(V\), with continuity constant \(M\) and coercivity constant \(\alpha\), Céa's lemma yields

\[
\|u-u_h\|_V\le\frac M\alpha\inf_{v_h\in V_h}\|u-v_h\|_V.
\]

Approximation rates require additional interpolation and regularity estimates; no universal rate follows solely from Céa.

### One interface unknown

Let the interval have two elements of length \(1/2\), with stiffnesses \(a_1=1\) and \(a_2=2\), zero source, and prescribed endpoint values \(U_0=0,U_2=1\). The one interior equation is

\[
\left(\frac{a_1}{h}+\frac{a_2}{h}\right)U_1
=\frac{a_1}{h}U_0+\frac{a_2}{h}U_2
\quad\Rightarrow\quad6U_1=4\quad\Rightarrow\quad U_1=\frac23.
\]

This exactly reproduces the piecewise-affine weak solution with slopes \(4/3\) and \(2/3\), and continuous flux \(a u'=4/3\).

### Exercises with answers

1. **Coarser mesh:** With two elements of length \(1/2\), what is the single interior nodal value for \(-u''=1\)? **Answer:** stiffness \(4\), load \(1/2\), so value \(1/8\).
2. **Error:** Prove \(\int_{-h/2}^{h/2}x^2\,dx=h^3/12\). **Answer:** The antiderivative is \(x^3/3\); evaluate at both ends.
3. **Source variation:** Why need the load vector no longer be hat areas for \(f(x)=x\)? **Answer:** It becomes \(b_i=\int_0^1x\phi_i(x)\,dx\), which weights each hat differently.
4. **Solver versus approximation:** Does solving \(KU=b\) to machine precision make \(\|u-u_h\|_a=0\)? **Answer:** No. The exact discrete solution still has positive approximation error \(1/\sqrt{108}\) on this mesh.

### Sources and further reading

- Frans van der Meer, [*Finite Element Method*, MUDE textbook](https://mude.citg.tudelft.nl/book/2025/fem/intro.html), for the complete journey from 1D and 2D Poisson models to discrete matrices.
- [*A primer on finite element methods*](https://www.math.ntnu.no/emner/MA8502/2024h/lectures/html/chapter_02/galerkin_methods.html), for Galerkin orthogonality and Céa's lemma.
- Luca Heltai, [*Model Problems and the Ritz–Galerkin Method*](https://luca-heltai.github.io/nmpde/lectures/lecture-01/), for abstract stability and the discrete projection argument.
- [Wikipedia: Finite element method](https://en.wikipedia.org/wiki/Finite_element_method) and [Galerkin method](https://en.wikipedia.org/wiki/Galerkin_method), for broader orientation.

*Teaching connections:* `linear-algebra:024000`–`025000` develop Cholesky and conjugate gradients for the resulting positive-definite systems; `numerical-analysis:018000` extends this introduction to a posteriori and goal-oriented error bounds; `differential-equations:010000` provides the PDE survey.
