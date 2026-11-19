# Linear measurements and constructions beyond vectors

<!-- BEGIN SPOKEN LECTURE -->

# Linear measurements and constructions beyond vectors

## Dual Spaces and Covectors: The Objects That Measure Vectors

A direction in space tells us how we might move. A thermometer reading, a height difference, or the derivative of a function tells us a number associated with that movement. The first is a vector; the second is a linear measurement of vectors. Linear algebra calls such measurements covectors, or linear functionals, and collects them into the dual space.

### Linear functionals as measurements

Take the plane with coordinates x and y. Define f of a vector to be two times x minus y. If we add two vectors, their readings add. If we scale a vector, its reading scales by the same amount. So f is a linear map from the plane to the real numbers.

A functional is not itself a direction on the plane. We can represent it by a row of coefficients, but that row is meaningful as an instruction to take a weighted sum. A column of coordinates is meaningful as a description of a vector. Their product is a scalar: evaluation. Without an inner product, there is no canonical way to turn one kind of object into the other.

The set of all linear functionals on a vector space V is itself a vector space, called V dual. We add functionals by adding their readings and scale them by scaling their readings. If V is finite-dimensional, its dual has the same dimension. But equal dimension does not mean a canonical identification of individual vectors with individual covectors.

### The dual basis is designed to evaluate coordinates

Suppose a vector space has a basis e one, e two, and so forth. There is a corresponding dual basis of functionals. The first returns the coefficient of e one; the second returns the coefficient of e two; and so forth. Applying dual basis functional i to basis vector j gives one when the indices match and zero otherwise.

The dual basis exists because any vector has a unique coordinate representation. If we know the coefficients, we can extract them linearly. Every functional can be expressed as a linear combination of these coordinate-extraction functionals.

In standard coordinates, our measurement two x minus y is the row two, minus one. If the vector is four, two, the reading is six. Now change the basis of vectors to u equal to one, one and v equal to one, minus one. The same physical vector has coefficients three and one. Evaluate f on u: the result is one. Evaluate f on v: the result is three. So f has the row one, three in this new basis, and its reading is one times three plus three times one, again six.

Vectors and covectors have changed coordinates in complementary ways. The vector coordinates changed from four, two to three, one. The covector coefficients changed from two, minus one to one, three. Their pairing did not change. This is why tensor calculus uses different coordinate-transformation rules for upper and lower indices.

### The transpose is the map on measurements

Suppose T maps one vector space V to another W. A functional on W can measure T of v. Compose that functional with T and you have a functional on V. This construction sends W dual back to V dual; it is called the dual map, or pullback. In coordinates, its matrix is the transpose of T, once the relevant dual bases are chosen.

Notice the reversal of direction. The original map goes from V to W, but measurements pull back from W dual to V dual. This is not a contradiction: a measurement on the output gives a measurement on the input by asking what output the input would produce. Differential forms are built from this same contravariant behavior.

### A derivative is a covector

Let h be a smooth real function on the plane, perhaps h of x and y equals x squared plus three y. A small displacement v with components a, b changes h to first order by two x times a plus three b. At each point, the derivative is a linear functional on tangent vectors, recorded as the differential d h. It takes a direction and returns a rate of change.

We often draw the gradient of h as a vector. Where did that vector come from if the derivative is naturally a covector? The inner product supplies the conversion: the gradient is the unique vector whose inner product with every direction reproduces the differential's value. In Euclidean coordinates they happen to share components. On a curved manifold or in nonorthogonal coordinates they transform differently. Confusing them leads to mistakes in geometry and optimization.

### Tangent and cotangent spaces

At a point of a smooth manifold, tangent vectors represent velocities of curves through that point. Covectors in the cotangent space are linear measurements of those velocities. Differentials of coordinate functions, like d x and d y, form a local basis of cotangent vectors. They evaluate tangent-coordinate directions just as the dual basis should.

A differential one-form assigns a covector smoothly to every point. Integrating one-forms along curves becomes possible because a one-form evaluates the curve's velocity to produce an ordinary scalar function of time. Two-forms and higher forms are multilinear alternating versions of the same measurement idea.

One last useful fact: any finite-dimensional vector space V maps canonically into its double dual. A vector v defines the functional on V dual that evaluates any covector at v. This map is an isomorphism in finite dimensions, but the construction is meaningful because it uses evaluation, not an arbitrary chosen basis. In infinite-dimensional functional analysis, continuous duals and double duals require extra hypotheses, and the canonical map may fail to be onto.

A vector is a possible direction. A covector is a way to read a number from a direction. The difference may seem formal in flat Cartesian coordinates, but it becomes indispensable when coordinates curve, metrics vary, and geometric objects must make sense independently of a chosen chart.

## Bilinear and Quadratic Forms: Curvature, Energy, and Signature

A linear functional takes one vector and returns a number. A bilinear form takes two vectors and returns a number, linearly in each argument. It can measure lengths and angles, as an inner product does, but it can also measure signed area, energy interactions, or mixed second derivatives. The resulting quadratic forms are the language of local optimization, Riemannian metrics, and much of mathematical physics.

### Start with two inputs

Consider the rule that takes two plane vectors, multiplies their first coordinates and adds their second coordinates multiplied together. That is the dot product, an example of a symmetric bilinear form. Another rule takes the first coordinate of the first vector times the second coordinate of the second, then subtracts the second coordinate of the first times the first coordinate of the second. That is the determinant of the two vectors, an alternating bilinear form. Swapping its inputs reverses the sign.

Both rules are linear in either input when the other is held fixed, yet they describe different geometry. The dot product of a nonzero vector with itself is positive. The determinant of any vector with itself is zero. Symmetry and alternation are different structural properties; one cannot infer them from the word bilinear alone.

Choose a basis. Any bilinear form B has a matrix M whose entry in row i and column j is B of basis vector i with basis vector j. On coordinate columns x and y, the form is x transpose times M times y. Symmetry of the form corresponds to a symmetric matrix. If we change coordinates using a matrix P, the new matrix is P transpose times M times P. This is congruence, not the similarity change used for linear operators. A bilinear form eats two vectors whereas an operator sends one vector to another, so their matrices transform by different rules.

### A quadratic form measures a vector against itself

Define Q of v to be B of v with itself. If B is symmetric, Q records its diagonal behavior. For example, take Q of x, y equal to the square of x minus y. This is always nonnegative, but it vanishes for every vector along the line x equals y. The corresponding symmetric matrix has rows one, minus one and minus one, one. It has rank one. This quadratic form is positive semidefinite, not positive definite.

Now consider Q of x, y equal to x squared minus y squared. Along the horizontal axis it is positive except at the origin; along the vertical axis it is negative. The matrix has one positive and one negative eigenvalue. This form is indefinite. The origin is not a local minimum or maximum of Q; arbitrarily close points have both positive and negative values.

The signature records how many positive, negative, and zero directions remain after diagonalizing a real symmetric form by a suitable change of coordinates. Sylvester's law of inertia says these counts do not depend on which basis we used. Individual matrix entries may change dramatically, but the numbers of intrinsically positive and negative directions do not.

### From quadratic forms to a second derivative test

At a critical point of a smooth function of several variables, the first derivative vanishes. The leading correction to the function's value is often a quadratic expression involving its Hessian: the matrix of second partial derivatives. When the Hessian is positive definite, every sufficiently small nonzero displacement raises the function value, yielding a strict local minimum. A negative-definite Hessian gives a strict local maximum. An indefinite Hessian produces a saddle point.

But a zero eigenvalue makes the second derivative test inconclusive. Consider the function x to the fourth power at zero. Its second derivative vanishes there, yet zero is a strict local minimum. Consider minus x to the fourth power: the same second derivative, but a strict local maximum. The quadratic approximation does not contain enough information. We must examine higher-order terms.

This example is a valuable warning: a sufficient condition is not a necessary one. Positive definite Hessian proves a strict local minimum, but failure of positive definiteness does not disprove one.

### How a metric differs from a general form

A Riemannian metric assigns a positive-definite symmetric bilinear form to the tangent space at every point, smoothly varying with the point. It measures squared lengths of tangent vectors and angles between them. At one point, an appropriate basis can make its matrix the identity. Across a curved manifold, however, no single coordinate system need make the metric constant everywhere. Curvature measures part of the obstruction to such a global simplification.

Indefinite nondegenerate forms also play an important role. In spacetime geometry, a Lorentzian metric has one time-like direction and space-like directions with opposite sign, under a chosen convention. It does not give a positive squared length to every nonzero tangent vector. Nevertheless it is a symmetric nondegenerate bilinear form, so much of the same algebra applies with different geometric consequences.

### Polarization reconstructs cross terms

If B is symmetric over the real numbers, we can recover B of u and v from Q. Evaluate Q on u plus v and subtract Q on u and Q on v. The difference is twice B of u and v. So knowledge of the quadratic form on every vector determines the symmetric bilinear form. We call this polarization.

Alternating forms cannot be recovered by evaluating a vector twice, because B of v with v always vanishes. Their information lives in how distinct directions interact. This is the distinction between the metric geometry of inner products and the area geometry of symplectic forms.

Bilinear forms are a common language for phenomena that can look unrelated: a Hessian in optimization, the dot product in Euclidean space, a Lorentzian spacetime interval, or an alternating two-form on a symplectic manifold. Learning their transformations and positivity conditions gives us a reliable way to move between these subjects without confusing the different kinds of structure.

## Tensor Products and Exterior Algebra: How Measurements Combine

A length measurement depends on one vector. An inner product depends on two. A determinant in three dimensions depends on three. Advanced geometry studies fields that assign such multilinear measurements at each point of a manifold. The algebraic machinery is called tensors, and its alternating part is exterior algebra. We can build the ideas from familiar operations rather than starting with index notation.

### A measurement of two vectors

A bilinear map takes a vector u from one space and a vector v from another and returns an output that depends linearly on each input separately. For example, from two coordinate vectors with components u one, u two and v one, v two, we can make four products: u one times v one, u one times v two, u two times v one, and u two times v two. Every bilinear scalar expression is a linear combination of those four products.

This suggests a construction. Instead of treating a bilinear map as something requiring two separate inputs, encode the pair of vectors in a single object u tensor v, with rules forcing linearity in each slot. A bilinear map can then be handled as an ordinary linear map out of the tensor product space. This is the universal property of the tensor product.

The symbol u tensor v represents a pure tensor. Sums of pure tensors make the general elements. Not every tensor can be expressed as one pure tensor: a general two-by-two matrix need not have rank one. This is important in applications because tensor decomposition can be a nontrivial mathematical or numerical problem.

If the spaces have dimensions m and n, their tensor product has dimension m times n. A basis is formed from every pair of basis elements, one from each space. For two-dimensional spaces, four such basis tensors appear. This explains the number of entries in a matrix of a bilinear form and the coordinate array for a rank-two tensor.

### Contravariant and covariant slots

A vector lives in a space V. A covector lives in its dual V star and evaluates vectors. A tensor can have slots that transform as vectors, as covectors, or both. A bilinear form on V is naturally an element of V star tensor V star in finite dimensions. A linear operator from V to V can be identified with an element of V tensor V star. These identifications explain why changing coordinates produces different index rules in different positions.

An abstract tensor does not depend on a chosen basis. Its coordinate array does, and the transformation law ensures that a complete contraction gives the same scalar in every chart. For example, a covector evaluating a vector is a contraction. The row and column components transform oppositely so their pairing remains unchanged.

### Antisymmetry means oriented area

Now consider two covectors alpha and beta. Form the alternating bilinear expression alpha of u times beta of v minus alpha of v times beta of u. This is alpha wedge beta evaluated on u and v. It changes sign when we exchange u and v, and vanishes when they point along the same line.

For the standard coordinate covectors d x and d y, the wedge d x wedge d y on vectors u and v is precisely the determinant of the matrix with columns u and v. It measures their signed parallelogram area. The wedge product is not just a symbol inserted between differential letters; it is an antisymmetrized tensor product that produces geometric quantities independent of coordinates.

For higher-degree alternating tensors, wedge products combine oriented measurements. If alpha is a one-form and beta a two-form, alpha wedge beta is a three-form. Swapping a p-form and a q-form introduces a sign of minus one to the power p times q. This graded sign rule makes differentials and Stokes' theorem work consistently.

At a point of an n-dimensional vector space, alternating k-forms are zero when k exceeds n, because we cannot supply more than n independent directions. The dimension of the space of k-forms is the number of ways to choose k basis directions from n, written n choose k. In particular, the top-degree alternating forms form a one-dimensional space. A nonzero top-degree form gives an orientation and a way to measure signed volume after a normalization is chosen.

### Why differential forms are tensors that can be integrated

On a smooth manifold, tangent spaces vary from point to point. A differential k-form assigns an alternating k-linear functional to each tangent space in a smooth way. A one-form can be integrated along a path because it evaluates each tangent velocity. A two-form can be integrated over a parameterized surface because it evaluates the two tangent directions induced by the surface coordinates. The wedge product combines forms to build higher-dimensional volume elements.

The exterior derivative is a further operation, depending on how a form varies from point to point. It raises degree by one and satisfies a graded product rule. A form is not the same as its exterior derivative; the latter captures how the original measurement changes across space. The generalized Stokes theorem relates integrating an exterior derivative over a region to integrating the original form over the boundary.

### One concrete pullback calculation

Let a coordinate transformation take parameters s, t to the plane by x equals two s and y equals s plus three t. The pullbacks of the coordinate one-forms are d x equals two d s and d y equals d s plus three d t. Wedge them. The d s wedge d s term vanishes, leaving six times d s wedge d t. The factor six is the determinant of the coordinate transformation. Exterior algebra has recovered the Jacobian formula from the transformation of one-forms.

This example is the bridge between linear algebra, multivariable calculus, and geometry. A change of variables in an integral is not a separate trick: it follows from how alternating multilinear measurements behave under linear maps.

Tensor products organize several-input linearity. Exterior products organize oriented measurements. Once these constructions are comfortable, coordinates in differential geometry stop looking like a maze of superscripts and subscripts, and start looking like a systematic way to keep track of which kinds of objects are being measured.

## Quotient Spaces and Exact Sequences: Forgetting Information on Purpose

Sometimes a measurement tells us only part of a state. If we know the sum of two coordinates, we cannot distinguish one, zero from zero, one. We might regard them as equivalent because their difference makes no change to the observed sum. The quotient space formalizes this decision: keep what survives after we declare a subspace of differences to be invisible.

### Equivalence by an invisible direction

Let V be the plane and let U be the line generated by one, minus one. Two vectors are equivalent modulo U if their difference lies in U. For example, one, zero and zero, one are equivalent, because their difference is one, minus one. So are five, minus three and two, zero, because both have coordinate sum two and their difference lies in U.

An equivalence class contains every point obtained by sliding along U. We write the class of v as v plus U. The quotient V modulo U is the set of those classes. We can add classes and scale them by using representatives, because changing a representative by an element of U changes the resulting answer only by another element of U. This independence of representative is what makes the quotient operations well defined.

The quotient is itself a vector space. In our example, each class is determined by the sum x plus y, so V modulo U is one-dimensional. We began with two input coordinates and deliberately identified all movement along a one-dimensional line. One independent direction survived.

### The first isomorphism theorem

Consider the linear measurement T of x, y equal to x plus y. Its kernel is exactly U. The map is surjective onto the real line. If we identify vectors that differ by elements of its kernel, the resulting quotient has precisely the distinctions the measurement actually detects. There is a natural map from V modulo kernel T to the image of T, sending the class of v to T of v.

Why is this well defined? If two representatives differ by something in the kernel, their images are equal. Why is it injective? If their images are equal, their difference is in the kernel, so they are the same class. Why is it surjective? Every point in the image is the image of some input. Thus the quotient by the kernel is naturally isomorphic to the image.

This is the first isomorphism theorem for vector spaces. Rank–nullity counted dimensions; the isomorphism theorem identifies the surviving space itself. It is a stronger structural statement.

### Dimension and choosing representatives

For finite-dimensional V, the quotient has dimension equal to dimension V minus dimension U. To see this, choose a basis of U and extend it to a basis of V. The extra basis vectors determine a basis of the quotient. Their images span all classes, and none of their nontrivial combinations belongs to U. So the dimensions subtract.

If we choose a complementary subspace W with V equal to U plus W and intersection only zero, every quotient class has exactly one representative in W. That choice identifies V modulo U with W. But the complement is generally not unique, so that identification is not canonical. The quotient is defined without selecting one convenient set of representatives.

### Exact sequences report where information went

Now place linear maps in a row: a space U maps into V, then V maps into W. The sequence is exact at V if the image of the first map equals the kernel of the second. In words, the elements arriving from U are exactly those that the next map sends to zero.

For our example, let U be the real line, map its number t to the plane vector t, minus t, and then map the plane vector x, y to x plus y. The image of the first map is precisely the kernel of the second. The first map is injective, the second is surjective. This is a short exact sequence: zero to the real line, to the plane, to the real line, to zero.

The zero spaces at the ends encode the injectivity and surjectivity conditions. They are not decorative punctuation. Exactness is a precise way of saying that every lost direction at one stage has been accounted for by the preceding stage, with no unexplained leftovers.

### When exactness fails, homology appears

Imagine a chain of linear maps whose consecutive compositions are zero. Then every vector produced by one map is sent to zero by the next. That means every boundary is a cycle, in the terminology of chain complexes. But there may be cycles that do not arise as boundaries. The quotient of cycles by boundaries measures the failure of the sequence to be exact. That quotient is homology.

This connection is central in algebraic topology. A closed loop in a triangulated space has zero boundary, but it may not be the boundary of a filled-in surface. The algebra says it lies in the kernel of one boundary map but not in the image of the previous one. Its homology class is the surviving obstruction.

The same language appears in differential equations. A differential operator may have a nontrivial kernel of solutions and an image of permissible source terms. In gauge theory, a chain complex separates genuine deformations from changes produced by symmetry. In cohomology, exact sequences record what local or global information survives a gluing operation.

There is a useful caution about splitting. Every short exact sequence of vector spaces over a field splits, because we can choose a basis and a complement. That need not hold for modules over a general ring or for vector bundles globally, at least not as a splitting respecting the additional structures under discussion. Algebraic statements must retain the category in which they are claimed.

A quotient does not throw away mathematics carelessly. It records which distinctions we intentionally no longer observe. An exact sequence reports precisely which directions are accounted for. Together they offer a common grammar for linear algebra, topology, and many advanced theories built from kernels and images.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Dual Spaces and Covectors: The Objects That Measure Vectors

**Track:** Linear Algebra from First Principles. **Background:** linear maps, coordinates and basis changes. **Question:** why is a linear measurement not the same mathematical object as a direction?

#### Mathematical companion (not spoken)

The algebraic dual \(V^*=\operatorname{Hom}_{\mathbb F}(V,\mathbb F)\). Given a basis \((e_i)\), the dual basis satisfies \(e^i(e_j)=\delta^i_j\). For \(v\in V\) and \(\varphi\in V^*\), the pairing \(\varphi(v)\) is basis-independent. If \([v]_{\mathrm{old}}=P[v]_{\mathrm{new}}\), then \([\varphi]_{\mathrm{new}}=[\varphi]_{\mathrm{old}}P\) as row coordinates, preserving \(\varphi(v)\). For \(T:V\to W\), \(T^*:W^*\to V^*\), \(T^*\psi=\psi\circ T\), has transpose matrix in dual bases; here \(T^*\) denotes the **algebraic dual map**, distinct from the Hilbert adjoint, although their matrices are related after inner-product identifications.

For \(h(x,y)=x^2+3y\), \(dh_{(x,y)}(a,b)=2xa+3b\). A Riemannian metric \(g\) identifies \(dh\) with a gradient vector through \(g(\nabla h,v)=dh(v)\).

##### Exercises with answers

1. Evaluate \(f(x,y)=2x-y\) on \((4,2)\). **Answer:** six.
2. What are its coefficients on the basis \((1,1),(1,-1)\)? **Answer:** \((1,3)\).
3. What direction does the dual map \(T^*\) go when \(T:V\to W\)? **Answer:** \(W^*\to V^*\).
4. Is the differential of a function naturally a vector? **Answer:** no; it is a covector, convertible to a gradient with a metric.

##### Sources and further reading

- Sheldon Axler, [Linear Algebra Done Right](https://linear.axler.net/), dual spaces and linear functionals.
- Jim Hefferon, [Linear Algebra](https://hefferon.net/linearalgebra/), dual spaces.
- [Dual space](https://en.wikipedia.org/wiki/Dual_space).

### Bilinear and Quadratic Forms: Curvature, Energy, and Signature

**Track:** Linear Algebra from First Principles. **Background:** matrices, duals, inner products and eigenvalues. **Question:** what does a measurement involving two directions tell us about geometric shape?

#### Mathematical companion (not spoken)

A bilinear form \(B:V\times V\to\mathbb R\) has coordinate form \(B(u,v)=u^TMv\); under \([u]_{\rm old}=P[u]_{\rm new}\), its matrix becomes \(M_{\rm new}=P^TM_{\rm old}P\). A symmetric form has quadratic form \(Q(v)=B(v,v)\) and polarization \(B(u,v)=\tfrac12(Q(u+v)-Q(u)-Q(v))\). Sylvester inertia theorem asserts invariance of the counts of positive, negative and zero entries under real congruence diagonalization. For \(Q(x,y)=(x-y)^2\), \(M=\begin{psmallmatrix}1&-1\\-1&1\end{psmallmatrix}\), with eigenvalues two and zero. For \(Q(x,y)=x^2-y^2\), the inertia is \((1,1,0)\).

For \(f\in C^2\), \(f(x_0+h)=f(x_0)+Df(x_0)h+\tfrac12h^T\nabla^2f(x_0)h+o(\|h\|^2)\). Positive-definite Hessian at a critical point is sufficient for a strict local minimum, not necessary.

##### Exercises with answers

1. Is \(Q(x,y)=(x-y)^2\) positive definite? **Answer:** no, it vanishes on the nonzero line \(x=y\).
2. Determine the signature of \(x^2-y^2\). **Answer:** one positive and one negative direction.
3. Why does an alternating form satisfy \(B(v,v)=0\)? **Answer:** exchanging identical arguments reverses sign, hence the value is its negative over a field of characteristic not two.
4. Does a zero Hessian force a critical point to be a saddle? **Answer:** no, \(x^4\) has a strict minimum with zero Hessian at zero.

##### Sources and further reading

- Sheldon Axler, [Linear Algebra Done Right](https://linear.axler.net/), multilinear algebra and bilinear forms.
- MIT OpenCourseWare, [18.06 Linear Algebra](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/), symmetric and positive-definite matrices.
- [Sylvester's law of inertia](https://en.wikipedia.org/wiki/Sylvester%27s_law_of_inertia).

### Tensor Products and Exterior Algebra: How Measurements Combine

**Track:** Linear Algebra from First Principles. **Background:** dual spaces, linear maps and bilinear forms. **Question:** how can we encode measurements that depend on several vectors, and why does alternating them describe area?

#### Mathematical companion (not spoken)

The tensor product \(V\otimes W\) represents bilinear maps: \(\mathrm{Bilin}(V\times W,Z)\cong\mathrm{Lin}(V\otimes W,Z)\). In finite dimensions, \(\dim(V\otimes W)=\dim(V)\dim(W)\) and \(\mathrm{Bil}(V\times V,\mathbb F)\cong V^*\otimes V^*\). Alternating k-tensors form \(\Lambda^kV^*\), of dimension \(\binom nk\) if \(n=\dim V\). For one-forms,
\[
(\alpha\wedge\beta)(u,v)=\alpha(u)\beta(v)-\alpha(v)\beta(u).
\]
In general \(\alpha\wedge\beta=(-1)^{pq}\beta\wedge\alpha\) when degrees are \(p,q\). For \(F(s,t)=(2s,s+3t)\), \(F^*(dx\wedge dy)=d(2s)\wedge d(s+3t)=6\,ds\wedge dt\).

##### Exercises with answers

1. What is the dimension of \(\mathbb R^2\otimes\mathbb R^3\)? **Answer:** six.
2. Evaluate \((dx\wedge dy)((1,2),(3,4))\). **Answer:** \(1\cdot4-3\cdot2=-2\).
3. Why does \(dx\wedge dx=0\)? **Answer:** a one-form wedged with itself is alternating and vanishes (over characteristic not two).
4. How many independent two-forms are there on a four-dimensional vector space? **Answer:** six.

##### Sources and further reading

- Sheldon Axler, [Linear Algebra Done Right](https://linear.axler.net/), multilinear algebra and tensor products.
- Raoul Bott and Loring Tu, [Differential Forms in Algebraic Topology](https://doi.org/10.1007/978-1-4757-3951-0), exterior products and de Rham cohomology.
- [Exterior algebra](https://en.wikipedia.org/wiki/Exterior_algebra).

### Quotient Spaces and Exact Sequences: Forgetting Information on Purpose

**Track:** Linear Algebra from First Principles. **Background:** subspaces, kernels, images and dimension. **Question:** how can we treat different vectors as equivalent and still do linear algebra?

#### Mathematical companion (not spoken)

For a subspace \(U\subseteq V\), define \(v\sim w\) iff \(v-w\in U\). The quotient \(V/U\) consists of cosets \(v+U\), with \((v+U)+(w+U)=(v+w)+U\) and \(a(v+U)=av+U\). The projection \(\pi:V\to V/U\) has kernel \(U\). For any linear \(T:V\to W\), the induced map \(V/\ker T\to\operatorname{im}T\), \([v]\mapsto T(v)\), is a well-defined isomorphism.

A complex \(U\xrightarrow{f}V\xrightarrow{g}W\) is exact at \(V\) iff \(\operatorname{im}f=\ker g\). If \(gf=0\), then \(\operatorname{im}f\subseteq\ker g\), and the quotient \(\ker g/\operatorname{im}f\) is the homology at \(V\). A short exact sequence \(0\to U\to V\to W\to0\) of finite-dimensional vector spaces yields \(\dim V=\dim U+\dim W\). The same exact sequences split for **all** vector spaces over a field, using choice as needed in infinite dimensions; not all short exact sequences of modules split.

##### Exercises with answers

1. Identify \(\mathbb R^2/\operatorname{span}(1,-1)\). **Answer:** naturally with \(\mathbb R\) via the sum of coordinates.
2. What is \(\dim(V/U)\) when \(\dim V=7,\dim U=2\)? **Answer:** five.
3. What does exactness at V mean? **Answer:** the image of the incoming map equals the kernel of the outgoing map.
4. If \(gf=0\) but \(\ker g\ne\operatorname{im}f\), what remains? **Answer:** nonzero homology \(\ker g/\operatorname{im}f\).

##### Sources and further reading

- Sheldon Axler, [Linear Algebra Done Right](https://linear.axler.net/), quotient spaces and linear maps.
- Jim Hefferon, [Linear Algebra](https://hefferon.net/linearalgebra/), quotient spaces and homomorphisms.
- [Exact sequence](https://en.wikipedia.org/wiki/Exact_sequence).
