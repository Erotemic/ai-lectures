# Spinors, Dirac operators, and an explicit spin-c index

<!-- BEGIN SPOKEN LECTURE -->

# Spinors, Dirac operators, and an explicit spin-c index

## Clifford Algebra: How a Metric Becomes Operator Multiplication

In the index-theory lectures we met an operator on differential forms that looked like a derivative plus its adjoint. Its principal symbol had a remarkable property: when you squared it, the result was minus the squared length of the frequency, times the identity. That algebraic fact guaranteed ellipticity.

The same pattern lies at the heart of Dirac operators and spin geometry. Before spinors or gauge theory can make sense, we need to understand the multiplication rule that creates it. This is Clifford algebra.

### Starting with one direction

Take a Euclidean vector of length one and imagine assigning it a linear operator. We demand that the operator square to minus the identity. Scaling the vector by a factor of three should make the square minus nine times the identity. In words, the square of the operator records the vector's squared length, with a minus sign.

Two perpendicular unit vectors receive operators that anticommute. Multiplying first by the operator for one direction and then by the operator for the other gives the negative of multiplying them in the opposite order. This means the algebra remembers angle as well as length.

Why anticommutation? Apply the rule to the sum of two vectors. Its squared length contains twice their inner product. Expanding the square of the corresponding operator gives the two individual squares and the sum of the two cross products. Matching the two expressions forces that cross-product sum to equal minus twice the inner product times the identity.

This construction packages the entire metric inside a multiplication law. It is not merely an algebra with convenient generators: the inner product can be recovered from their anticommutator.

### The two-dimensional matrix example

Let us see actual matrices. There are three famous two-by-two complex matrices called the Pauli matrices. The first swaps the two coordinates. The second swaps them with imaginary factors. The third negates one coordinate while leaving the other unchanged.

Multiply the first two Pauli matrices by the imaginary unit and use them as operators for the two perpendicular coordinate directions. Each operator squares to minus the identity, and they anticommute. The product of the two coordinate operators is proportional to the third Pauli matrix. The signs depend on how we choose the order and the imaginary unit, but the Clifford relation does not.

These two-by-two matrices therefore represent the complex Clifford algebra of the Euclidean plane. A spinor in this model is a two-component complex column vector on which the Clifford operators act. Nothing mystical has been added. We have found a small representation of a metric-dependent algebra.

### Exterior algebra gives another representation

We already have a familiar space on which directions act: differential forms. A covector can increase form degree by exterior multiplication. The associated vector can decrease form degree by contraction. Subtract contraction from wedge multiplication. The resulting operator squares to minus the covector's squared norm.

This is Clifford multiplication on the exterior algebra. It is the symbol construction behind the de Rham operator. So Clifford multiplication is not confined to quantum particles or spinors. It is already present in the calculus of forms.

The two representations have different dimensions. On an n-dimensional space, the full exterior algebra has dimension two to the n, whereas an irreducible complex spin representation is often much smaller. The ability to realize the same Clifford relation on different modules explains why many Dirac-type operators exist, but have different kernels and different index formulas.

### Rotations hiding in pairs of vectors

Now multiply two unit vectors in the Clifford algebra. An even product can act on vectors by conjugation and implement a rotation. The group formed by suitable even products is called the spin group. Its map to the rotation group is a double covering: two elements differing by a sign produce the same physical rotation of vectors.

This is the origin of the two-to-one phenomenon that becomes important for spin structures. We did not invent a double cover for convenience. It appears when rotations are represented by products of Clifford generators, and the elements plus one and minus one act identically on vectors by conjugation.

In the plane, a rotation through a full turn returns every vector to its starting position. But the corresponding continuous path in the spin group ends at minus one, not at plus one. Only a double turn closes the lifted path. This is not a statement that ordinary vectors require two turns. It is a statement about the representation that spinors carry.

### From algebra to a differential operator

A Dirac operator combines Clifford multiplication with covariant differentiation. Choose an orthonormal frame, differentiate a spinor in each frame direction using a compatible connection, multiply each derivative by the Clifford operator for that direction, and sum.

The highest-frequency part of that operator is Clifford multiplication by the frequency covector. Because its square is minus the squared norm, the symbol is invertible away from zero frequency. Thus a Dirac operator is elliptic, just as the de Rham operator is elliptic.

But the global spinor bundle is not yet constructed. Having matrices in each tangent space does not tell us how to glue those local representations when our orthonormal frames rotate across chart overlaps. That gluing problem is the next step, and it is exactly where spin and spin-C structures enter.

The chain of ideas is now visible: a metric determines an anticommutation relation; that relation defines Clifford multiplication; products of generators encode rotations; representations carry spinors; and a connection turns the algebra into a first-order elliptic operator. Each link has an independent mathematical meaning, and we will build the global version rather than treating it as an unexplained package.

## Spin and Spin-C Structures: Gluing Rotations and Spinors

Suppose we have an oriented Riemannian manifold. At each point, its tangent space looks like ordinary Euclidean space, so we can construct the Clifford algebra and its spinor representations. The problem is that one tangent space has no preferred orientation-preserving orthonormal basis. As we move from chart to chart, the bases rotate. Do those rotations act consistently on the spinors we want to glue together?

This question is not solved by choosing enough charts. It is a global topological problem. The extra datum that solves it, when possible, is a spin structure. A related and more flexible datum is a spin-C structure.

### A familiar bundle-gluing problem

Recall how a vector bundle is assembled. Over each chart it looks like a product with a fixed vector space. On an overlap between two charts, we use a transition function to change one trivialization to the other. On a triple overlap, the three changes of trivialization must compose to the identity.

For an oriented orthonormal frame bundle, the transition functions take values in the rotation group. Our Clifford construction has another group, the spin group, which maps two-to-one onto rotations. A spin structure amounts to lifting the rotation transition functions to spin-valued transition functions that still obey the triple-overlap compatibility condition.

We can always choose lifts locally on sufficiently small overlaps. But the signs accumulated on triple overlaps may not cancel. If they do not, there is no globally consistent spinor bundle built by this recipe. The obstruction is encoded in the second Stiefel-Whitney class of the tangent bundle, a cohomology class with coefficients modulo two.

For an oriented manifold, a spin structure exists exactly when that obstruction vanishes. When one spin structure exists, the distinct choices form a family parameterized by first cohomology with modulo-two coefficients. Thus existence and uniqueness are different questions.

### A small example with two answers

The circle provides the simplest example. Its oriented tangent bundle is trivial, so it admits spin structures. But it has two different spin structures. In a convenient trivialization, a spinor carried once around the circle can return with the same sign or with the opposite sign.

These choices become periodic and antiperiodic boundary conditions for the simplest flat Dirac operator. They change its spectrum: periodic complex spinors permit a zero mode, while antiperiodic ones do not. The underlying circle and its Riemannian metric have not changed. The spin structure supplies genuine additional global data.

The two-sphere is spin as well. On an oriented surface, the relevant modulo-two obstruction is the Euler class reduced modulo two. The two-sphere has Euler characteristic two, so the obstruction vanishes. The projective plane over the complex numbers gives the contrasting four-dimensional example. Its second Stiefel-Whitney class is nonzero, and it is not spin.

### Repairing the sign obstruction with a circle phase

A spin-C structure enlarges the spin group by incorporating a unit complex phase. Formally, we take the spin group times the circle group, identifying the pair of negative signs with the pair of positive signs.

This construction permits a failure of the spin lifts to close up if a compensating phase repairs it. The combined transition functions form a spin-C bundle even when there is no spin bundle. Attached to this structure is a complex line bundle called its determinant line. Its first Chern class reduces modulo two to the second Stiefel-Whitney class of the tangent bundle.

That leads to a precise existence criterion. An oriented manifold has a spin-C structure if and only if its second Stiefel-Whitney class is the modulo-two reduction of an integral second cohomology class. The criterion is weaker than requiring the Stiefel-Whitney class to vanish. Not every oriented manifold in arbitrary dimension satisfies it, although every oriented smooth four-manifold does.

For the complex projective plane, the generator of second integral cohomology reduces to the nonzero modulo-two class. It supplies a compatible determinant line, even though it cannot make the manifold spin. The complex structure also supplies a canonical spin-C construction, with determinant line related to the complex tangent bundle.

### Why the determinant line matters

The spin-C structure does more than allow spinors to exist. A connection on its determinant line, combined with the Levi-Civita connection, defines a connection on the spinor bundle. Changing that line connection changes the Dirac operator. The determinant-line curvature then appears explicitly in the equation for the square of the Dirac operator.

In four dimensions, the complex spinor bundle splits into positive and negative chirality pieces. A spin-C Dirac operator maps positive spinors to negative spinors. This is the operator that later enters the Seiberg-Witten equations, paired with an equation involving the self-dual curvature of the determinant line.

We should distinguish three notions. An oriented manifold has frames whose transition functions lie in the rotation group. A spin structure lifts those transitions to the spin double cover. A spin-C structure allows an additional phase and carries a determinant line whose Chern class records the remaining modulo-two obstruction. Saying only that 'spinors are like vectors with two components' loses the global issue and also misses the line bundle on which gauge theory depends.

Our next job is to construct the resulting global spinor bundle and its differential operator. The local Clifford algebra will provide the multiplication, while the spin-C gluing and determinant connection make that construction independent of which charts and frames we use.

## Spinor Bundles and Dirac Operators: Differentiating a Spinor

We have constructed the Clifford algebra in one Euclidean space and examined the extra gluing data needed to make its representations global. We can now ask a more dynamic question. Once a spinor is defined across a manifold, what does it mean to differentiate it?

A spinor cannot be differentiated by comparing its components at two different points without additional information. The components refer to local spin frames, just as the components of an ordinary vector refer to a local basis. A connection supplies a consistent way to compare them. A Dirac operator then uses Clifford multiplication to combine all the directional covariant derivatives into one first-order operator.

### From a frame to a spin frame

On a small region, choose an oriented orthonormal frame of tangent vectors. The spinor bundle looks like the region times a fixed complex spin representation. Each tangent direction has a Clifford multiplication operator acting on that representation. We can write the derivative of a spinor as a collection of derivatives of its components plus correction terms describing how the spin frame turns.

These correction terms are not optional decoration. An ordinary derivative would change incorrectly under a moving frame. The Levi-Civita connection tells us how the orthonormal frame rotates. A spin or spin-C structure lifts that frame rotation to the spinor representation, producing the spin connection.

In a spin-C structure there is another ingredient: a unitary connection on the determinant line bundle. The combined connection on spinors includes half the determinant-line connection in local formulas. This factor of one half reflects the way the circle phase enters the spin-C group, and it is responsible for some of the factors appearing later in curvature formulas.

### Assembling directional derivatives

Choose an orthonormal frame with directions one through n. Covariantly differentiate the spinor in each direction. Then Clifford-multiply that derivative by the corresponding dual covector, and add the results. The sum is the Dirac operator.

The formula looks coordinate dependent, but it is not. Rotating the orthonormal frame rotates both the derivative components and the Clifford operators. Because the connection and the Clifford action transform compatibly, the final sum is unchanged. This is why we spent time on gluing and compatibility before writing an operator.

At high frequency, the connection's lower-order coefficients do not affect the principal symbol. The symbol is simply Clifford multiplication by the frequency covector, up to the conventional imaginary factor used in Fourier analysis. Its square is minus the squared frequency length. So away from zero frequency the symbol is invertible. Every Dirac operator of this kind is elliptic.

### The simplest Dirac operator on a circle

A circle of circumference two pi is a useful laboratory. In a flat trivialization and with one choice of spin structure, the Dirac operator can be represented by minus the imaginary unit times angular differentiation. Its eigenvectors are the periodic complex exponentials. Their eigenvalues are the integers. The constant spinor is a zero mode.

Change only the spin structure. Under the other choice, spinors become antiperiodic after one turn. Their Fourier frequencies shift by one half. The eigenvalues are now the half-integers, and no zero mode remains.

The metric is identical in both cases; the local differential expression looks the same. The difference lies in the global identification of the spinor at the end of the circle. This is a concrete reminder that local elliptic formulas do not determine global kernels by themselves.

### Chirality in even dimensions

In an even-dimensional oriented Riemannian manifold, the complex spinor representation splits into two pieces, called positive and negative chirality. Clifford multiplication by a tangent covector exchanges them. So the Dirac operator exchanges them as well.

In four dimensions this gives a particularly important map: the positive spinor bundle to the negative spinor bundle. On a closed four-manifold, it has finite-dimensional kernel and cokernel once we place it in appropriate Sobolev spaces. The difference of their dimensions is its index.

In Seiberg-Witten theory, the unknowns include a unitary determinant-line connection and a positive spinor. The first equation says the Dirac operator coupled to that connection kills the spinor. The second equation constrains the self-dual part of the line's curvature by a quadratic expression in the spinor. The index of the chiral Dirac operator will contribute to the expected dimension of the monopole moduli space.

### Three operators to keep separate

Our de Rham operator, a spin Dirac operator, and a spin-C Dirac operator share the Clifford symbol pattern. But they act on different bundles. The de Rham operator acts on the full exterior algebra. A spin Dirac operator acts on spinors associated with a spin structure. A spin-C Dirac operator acts on spinors associated with a spin-C structure and depends on a choice of determinant-line connection.

Their indices need not agree. On the two-sphere, the de Rham parity operator has index two, the Euler characteristic. The untwisted spin Dirac operator has index zero. That difference is not a contradiction, because the bundles and their grading are different.

The next step is to square a Dirac operator. The result will connect the first-order Dirac equation to a second-order Laplacian plus curvature. This is the key analytic identity used to prove vanishing theorems and establish estimates for spinors. The operator is now fully constructed, so we can examine that curvature identity without treating it as a mysterious formula.

## The Weitzenbock Formula: Curvature in the Square of Dirac

Consider the Dirac equation: a spinor is killed by a first-order differential operator. The equation mixes all coordinate directions through matrix multiplication. How can we tell whether it has nonzero solutions, or control their size without solving it explicitly?

One of the most powerful moves in geometric analysis is to square the operator. The square of a Dirac operator resembles the connection Laplacian, but with a correction involving curvature. This is called a Weitzenbock formula. In the spin case, the familiar version is also known as the Lichnerowicz formula.

### First think about the ordinary Laplacian

For a function on a compact manifold without boundary, integrate the function against its nonnegative Laplacian. Integration by parts says that the result is the integral of the squared length of its gradient. If the Laplacian kills the function, its gradient has zero length everywhere. On a connected manifold, the function is constant.

That argument does not require coordinates. It uses a positive quadratic expression obtained by integrating by parts. We want a corresponding argument for spinors, but spinors carry a connection, and second covariant derivatives do not generally commute.

### What changes when derivatives fail to commute

Apply the Dirac operator twice. Terms involving the same directional second derivative collect into the rough, or connection, Laplacian. Terms in which two different directional derivatives appear in opposite orders produce their commutator. The commutator of covariant derivatives is curvature.

Clifford multiplication combines the curvature components in a specific way. For the untwisted spin Dirac operator, the correction simplifies to one quarter of the scalar curvature times the identity. For a spin-C Dirac operator, there is an additional term involving Clifford multiplication by the curvature of the determinant line.

The exact signs depend on whether one declares Clifford multiplication skew-adjoint or self-adjoint and how one normalizes the determinant connection. We will use the Riemannian convention in which a unit vector squares to minus one. With that choice, the square of the spin Dirac operator is the nonnegative connection Laplacian plus one quarter of scalar curvature.

### A vanishing argument that takes one line of analysis

Suppose the manifold is closed, spin, and has everywhere positive scalar curvature. Let a spinor solve the untwisted Dirac equation. Its Dirac norm is zero. Integrating the Lichnerowicz formula gives the sum of two nonnegative quantities: the squared norm of its covariant derivative and one quarter of scalar curvature times the squared norm of the spinor.

If scalar curvature is strictly positive everywhere, both terms can sum to zero only if the spinor itself vanishes. Thus the untwisted spin Dirac operator has no harmonic spinors.

This is a global statement proved without writing down any special function solutions. The geometry, through scalar curvature, forces an analytic kernel to be zero. It is one of the classic examples of geometry controlling a differential equation.

### The example of the round sphere

A round sphere has positive scalar curvature, so an untwisted spin Dirac operator on it has no zero modes. Compare this with de Rham theory: a round two-sphere certainly has harmonic zero-forms and harmonic top-degree forms. Its de Rham operator therefore has a nontrivial kernel, despite being another Dirac-type operator.

Again, there is no conflict. The Lichnerowicz formula depends on which Clifford module and connection are used. The curvature correction for forms is not simply scalar curvature over four. It includes the curvature action on the form bundle, and the harmonic constants survive.

### Why spin-C curvature changes the argument

A spin-C spinor is coupled to a determinant-line connection. That line's curvature contributes an additional algebraic operator to the squared Dirac equation. The extra term need not be nonnegative. Even on a manifold with positive scalar curvature, a sufficiently strong or suitably signed line curvature can change the picture.

In Seiberg-Witten theory the curvature is not an externally fixed coefficient. It is linked to the spinor by another equation. Combining that equation with the Weitzenbock formula produces estimates for the spinor, often beginning with a maximum-principle argument. Those estimates help establish compactness for monopole solutions on a closed four-manifold.

But the formula alone does not prove compactness. We still need suitable gauges for connections, control of derivatives, and elliptic regularity. The identity supplies a key estimate within that larger chain.

### The broader family of formulas

A Weitzenbock identity is not limited to spinors. On one-forms, the Hodge Laplacian can be written as a connection Laplacian plus a Ricci curvature term. If Ricci curvature is positive, a harmonic one-form must vanish. Through Hodge theory, this gives a topological conclusion: the first real Betti number is zero.

Both stories have the same architecture. An elliptic operator's square or associated Laplacian equals a manifestly nonnegative derivative term plus a curvature term. Integrate against a solution, use positivity, and obtain vanishing or a priori bounds.

When we later meet the Dirac and gauge equations in four-dimensional topology, we should search for this pattern rather than memorizing a particular formula. It explains where estimates come from, which geometric hypotheses they require, and why changing the connection or metric can change the analytic conclusions.

## Computing the Spin-C Dirac Index on a Four-Manifold

A Dirac equation on a closed manifold may have an unknown number of solutions. But when the manifold is even-dimensional, the positive-to-negative chirality Dirac operator has an index: the dimension of its kernel minus the dimension of the kernel of its formal adjoint. That difference is stable under smooth deformations of the operator's coefficients and can often be computed without solving the equation.

In four dimensions, the spin-C Dirac index has a strikingly compact formula. It depends on the first Chern class of the determinant line and the signature of the four-manifold. Understanding what those two quantities mean is more valuable than memorizing a fraction with an eight in the denominator.

### The determinant line records the twist

A spin-C structure comes with a determinant line bundle. Its first Chern class is an integral second cohomology class. Geometrically, that class can be measured by integrating the line's curvature over oriented two-dimensional cycles, with the correct normalization.

On a four-manifold, a second cohomology class can be multiplied with itself using the cup product. Evaluating the resulting fourth-degree class on the fundamental cycle gives an integer: the self-intersection number of the class. This is the square of the determinant line's first Chern class.

That square is not an ordinary square of a number obtained by integrating over one particular surface. It is the intersection pairing on second cohomology. The pairing also has a signature: the number of positive directions minus the number of negative directions after extending the form to the real numbers and ignoring zero directions as appropriate. For a closed oriented four-manifold, this signature is a topological invariant.

### How the index theorem combines them

The Atiyah-Singer theorem for a spin-C Dirac operator says that its index is obtained by integrating a characteristic-class expression, the A-hat class multiplied by the exponential of half the determinant first Chern class.

In real dimension four, only degree-four terms contribute to the integral. The exponential contributes one eighth of the Chern-class square. The A-hat class contributes minus one twenty-fourth of the first Pontryagin class. The signature theorem identifies the Pontryagin number with three times the signature. Substituting gives the answer: the determinant Chern-class square minus the signature, all divided by eight.

This gives a consistency test. The result must be an integer, because it is an analytic Fredholm index. The parity condition on the determinant line, inherited from the spin-C structure, is precisely what makes the numerator divisible by eight in the required topological setting.

### Calculate the complex projective plane

The complex projective plane has a second cohomology generator conventionally called h. Its self-intersection is one. The signature is one. The complex tangent bundle has first Chern class three times h, and the canonical spin-C structure associated with the complex structure has determinant line with that same first Chern class.

Square three times h using the intersection pairing and obtain nine. Subtract the signature, one, to get eight. Divide by eight. The index is one.

That integer can also be understood through complex geometry. For the canonical complex spin-C structure, the Dirac operator is related to the Dolbeault operator and its adjoint. Its index is the holomorphic Euler characteristic. For the complex projective plane, this is one. Two very different languages agree on the same answer.

### Twisting changes the index predictably

Suppose we twist a spin-C structure by a complex line bundle with first Chern class q. The determinant first Chern class changes by twice q, not just q. This reflects the square in the determinant character of the spin-C group.

Substitute the new first Chern class into the formula. The index change is a combination of the original Chern class paired with q and the self-intersection of q, divided by two in the resulting expansion. The point is that changing the line twist changes the index by a calculable integer. We can check the change entirely in cohomology.

### An index does not count every solution

If the index is one, it does not mean there is exactly one Dirac zero mode. The kernel might have dimension five and the cokernel four, or the kernel one and the cokernel zero. The index records their difference, not their individual values.

For a nonlinear monopole equation, the expected dimension of the solution moduli space includes more than the chiral Dirac index. We must also account for the curvature equation, the gauge group, and real versus complex dimensions. That is why a Fredholm index calculation is a component of moduli-space analysis, not the final answer about solutions.

This lecture's payoff is a repeatable method: specify the correct elliptic operator, identify its bundle and topological twisting, expand the index characteristic class to the manifold's dimension, and calculate the relevant intersection numbers. We will next return to the other half of moduli-space theory: linearized equations and gauge symmetries.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Clifford Algebra: How a Metric Becomes Operator Multiplication

**Track:** Topology and Geometry. **Background:** inner products, complex matrices, exterior algebra, elliptic symbols. **Central question:** what algebra turns a direction in space into an operator whose square measures length?

#### Mathematical companion (not spoken)

For a real Euclidean vector space \((V,g)\), define \(\mathrm{Cl}(V,g)=T(V)/\langle v\otimes v+g(v,v)1\rangle\). Then
\[c(v)c(w)+c(w)c(v)=-2g(v,w)\operatorname{id}.\]
For \(V=\mathbb R^2\), let \(\sigma_1=\begin{psmallmatrix}0&1\\1&0\end{psmallmatrix}\) and \(\sigma_2=\begin{psmallmatrix}0&-i\\i&0\end{psmallmatrix}\). Set \(c(e_1)=i\sigma_1\), \(c(e_2)=i\sigma_2\). Both square to \(-I\) and anticommute.

For forms \(\Lambda^*V^*\), \(c(\xi)=\varepsilon(\xi)-\iota_{\xi^\sharp}\); the canonical anticommutation relations imply \(c(\xi)^2=-|\xi|^2\). On a Clifford module \(S\) with compatible connection, \(D=\sum_j c(e^j)\nabla_{e_j}\). Suppressing the Fourier factor \(i\), the principal symbol satisfies \(\sigma(D,\xi)^2=-|\xi|^2I\), hence is invertible for \(\xi\ne0\).

In dimension two, \(\operatorname{Spin}(2)\cong U(1)\), and the covering map to \(SO(2)\cong U(1)\) is \(z\mapsto z^2\).

##### Exercises with answers

1. **Orthogonality.** If \(g(v,w)=0\), what is \(c(v)c(w)+c(w)c(v)\)? **Answer:** zero.
2. **Length.** What is \(c(3v)^2\) for a unit vector? **Answer:** \(-9I\).
3. **Forms.** Why is wedge multiplication alone not a Clifford action? **Answer:** its square is zero for a one-form, not minus the squared norm.
4. **Cover.** How many elements of \(\operatorname{Spin}(2)\) map to a typical planar rotation? **Answer:** two, differing by sign.

##### Sources and further reading

- Liviu Nicolaescu, [Notes on Seiberg-Witten Theory](https://www3.nd.edu/~lnicolae/new1.pdf), Section 1.3.
- Tim Perutz, [Basics of Seiberg-Witten Theory](https://www.imperial.ac.uk/media/imperial-college/research-centres-and-groups/geometry/junior-geometry-seminar/Seiberg-Witten-theory.pdf).
- Overviews: [Clifford algebra](https://en.wikipedia.org/wiki/Clifford_algebra), [Pauli matrices](https://en.wikipedia.org/wiki/Pauli_matrices), [Spin group](https://en.wikipedia.org/wiki/Spin_group).

### Spin and Spin-C Structures: Gluing Rotations and Spinors

**Track:** Topology and Geometry. **Background:** bundles, transition functions, characteristic classes, Clifford algebra. **Central question:** when can local spin representations be glued to a global bundle on a manifold?

#### Mathematical companion (not spoken)

For an oriented rank-\(n\) real bundle \(E\), a spin structure lifts its oriented orthonormal frame bundle \(P_{SO(n)}\) through \(\operatorname{Spin}(n)\to SO(n)\). Its obstruction is \(w_2(E)\in H^2(X;\mathbb Z/2)\). If \(w_2(E)=0\), spin structures form a torsor for \(H^1(X;\mathbb Z/2)\) (subject to the standard equivalence of lifts over the fixed frame bundle).

\[\operatorname{Spin}^c(n)=(\operatorname{Spin}(n)\times U(1))/\{(1,1),(-1,-1)\}.\]
The determinant character \([s,z]\mapsto z^2\) defines a line bundle \(L\) with \(c_1(L)\bmod 2=w_2(E)\). Existence is equivalent to \(W_3(E)=\beta(w_2(E))=0\), equivalently to the existence of an integral lift of \(w_2\). Spin-C structures, when they exist, form a torsor for \(H^2(X;\mathbb Z)\), with twisting by a line bundle \(Q\) changing \(L\) to \(L\otimes Q^{\otimes2}\).

For \(\mathbb{CP}^2\), \(w_2(T\mathbb{CP}^2)=h\bmod2\neq0\) and \(c_1(T^{1,0}\mathbb{CP}^2)=3h\) is an integral lift. For \(S^1\), the two spin structures correspond to the two elements of \(H^1(S^1;\mathbb Z/2)\). Do not conflate a spin-C determinant line with an arbitrary line: its parity must match \(w_2\).

##### Exercises with answers

1. **Obstruction.** Which class obstructs a spin structure on an oriented bundle? **Answer:** \(w_2\).
2. **Two structures.** Why does an oriented circle have two spin structures? **Answer:** \(H^1(S^1;\mathbb Z/2)\cong\mathbb Z/2\).
3. **Spin-C.** Must the determinant line of a spin-C structure have trivial first Chern class? **Answer:** no; its reduction modulo two must equal \(w_2\).
4. **Example.** Why can \(\mathbb{CP}^2\) be spin-C but not spin? **Answer:** its nonzero \(w_2\) has an integral lift \(h\).

##### Sources and further reading

- Liviu Nicolaescu, [Notes on Seiberg-Witten Theory](https://www3.nd.edu/~lnicolae/new1.pdf), discussion of spin and spin-C structures.
- Tim Perutz, [Basics of Seiberg-Witten Theory](https://www.imperial.ac.uk/media/imperial-college/research-centres-and-groups/geometry/junior-geometry-seminar/Seiberg-Witten-theory.pdf).
- Overviews: [Spin structure](https://en.wikipedia.org/wiki/Spin_structure), [Spin-C structure](https://en.wikipedia.org/wiki/Spinc_structure), [Stiefel-Whitney class](https://en.wikipedia.org/wiki/Stiefel%E2%80%93Whitney_class).

### Spinor Bundles and Dirac Operators: Differentiating a Spinor

**Track:** Topology and Geometry. **Background:** Clifford representations, spin-C structures, connections, elliptic operators. **Central question:** how do Clifford multiplication and covariant differentiation combine into a global differential operator?

#### Mathematical companion (not spoken)

For a Hermitian Clifford module \((S,c)\) with compatible connection \(\nabla^S\) and local orthonormal frame \(e_j\),
\[D=\sum_{j=1}^n c(e^j)\nabla^S_{e_j}.\]
Under the Riemannian convention \(c(\xi)^2=-|\xi|^2\), \(\sigma_1(D)(x,\xi)=i c(\xi)\) with the Fourier \(e^{ix\xi}\) convention; it is invertible for \(\xi\ne0\).

In even dimension, \(S=S^+\oplus S^-\) with \(c(\xi):S^\pm\to S^\mp\), and \(D^+:\Gamma(S^+)\to\Gamma(S^-)\). On a spin-C manifold with determinant line \(L\) and connection \(A\), the induced spinor connection is written \(\nabla_A\); locally it contains a half-weight contribution from the determinant-line connection. In dimension four \(\operatorname{rank}_\mathbb C S^\pm=2\).

On the unit-radius flat circle, use \(D=-i\frac{d}{d\theta}\). For periodic spinors \(\psi(\theta+2\pi)=\psi(\theta)\), its spectrum is \(\mathbb Z\); for antiperiodic spinors \(\psi(\theta+2\pi)=-\psi(\theta)\), its spectrum is \(\mathbb Z+\frac12\). This model describes the boundary condition in a chosen local spin trivialization.

##### Exercises with answers

1. **Frame change.** What corrects componentwise differentiation in moving spin frames? **Answer:** the compatible spinor connection.
2. **Principal symbol.** Why is the Dirac symbol invertible for nonzero covectors? **Answer:** its Clifford square is a nonzero scalar multiple of the identity.
3. **Circle.** Which spin structure permits a flat zero mode in the stated circle model? **Answer:** the periodic one.
4. **Chirality.** Where does the chiral Dirac operator map positive spinors in dimension four? **Answer:** into negative spinors.

##### Sources and further reading

- Liviu Nicolaescu, [Notes on Seiberg-Witten Theory](https://www3.nd.edu/~lnicolae/new1.pdf), spinor connections and Dirac operators.
- Tim Perutz, [Basics of Seiberg-Witten Theory](https://www.imperial.ac.uk/media/imperial-college/research-centres-and-groups/geometry/junior-geometry-seminar/Seiberg-Witten-theory.pdf).
- Overviews: [Dirac operator](https://en.wikipedia.org/wiki/Dirac_operator), [Spinor](https://en.wikipedia.org/wiki/Spinor), [Spin-C structure](https://en.wikipedia.org/wiki/Spinc_structure).

### The Weitzenbock Formula: Curvature in the Square of Dirac

**Track:** Topology and Geometry. **Background:** spinor Dirac operators, covariant Laplacians, curvature, integration by parts. **Central question:** why does squaring a first-order geometric operator reveal a useful second-order positivity estimate?

#### Mathematical companion (not spoken)

For the untwisted spin Dirac operator on a closed Riemannian spin manifold, with \(c(v)^2=-|v|^2\),
\[D^2=\nabla^*\nabla+\frac14\operatorname{Scal}.\]
Hence for \(D\psi=0\),
\[0=\|D\psi\|_{L^2}^2=\|\nabla\psi\|_{L^2}^2+\int_X\frac{\operatorname{Scal}}4|\psi|^2\,d\mathrm{vol}.\]
If scalar curvature is everywhere strictly positive, \(\psi=0\). For a spin-C determinant connection \(A\), the standard formula is
\[D_A^2=\nabla_A^*\nabla_A+\frac14\operatorname{Scal}+\frac12c(F_A),\]
where \(F_A\) is the imaginary-valued curvature two-form, and \(c(F_A)\) is the induced Clifford action; adjust the coefficient if using a convention where \(A\) denotes the half-weight spinor line connection instead of the determinant connection.

For harmonic one-forms, the Bochner identity gives \(\Delta_H\alpha=\nabla^*\nabla\alpha+\operatorname{Ric}(\alpha)\); strictly positive Ricci curvature on a closed manifold implies \(H^1(X;\mathbb R)=0\).

##### Exercises with answers

1. **Curvature term.** Which scalar geometric quantity appears in the untwisted spin formula? **Answer:** one quarter of scalar curvature.
2. **Vanishing.** Why does positive scalar curvature rule out harmonic untwisted spinors? **Answer:** the integrated equality is a sum of nonnegative terms, one strictly positive wherever the spinor is nonzero.
3. **Twist.** What new term appears for the spin-C operator? **Answer:** Clifford action by half the determinant-line curvature in the specified convention.
4. **Forms.** Does the untwisted spin vanishing argument eliminate constant harmonic functions? **Answer:** no; functions live in a different Dirac-type module with a different curvature identity.

##### Sources and further reading

- Liviu Nicolaescu, [Notes on Seiberg-Witten Theory](https://www3.nd.edu/~lnicolae/new1.pdf), geometric Dirac bundles and Weitzenbock identities.
- Daniel Freed and Karen Uhlenbeck, [Instantons and Four-Manifolds](https://doi.org/10.1007/978-1-4613-9703-8) (book; publisher access may apply).
- Overviews: [Lichnerowicz formula](https://en.wikipedia.org/wiki/Lichnerowicz_formula), [Bochner technique](https://en.wikipedia.org/wiki/Bochner_technique).

### Computing the Spin-C Dirac Index on a Four-Manifold

**Track:** Topology and Geometry. **Background:** characteristic classes, signature, spin-C determinant line, chiral Dirac operator, analytic index. **Central question:** how can a spinor equation's analytic index be computed from topology before solving the equation?

#### Mathematical companion (not spoken)

Let \(X\) be a closed oriented smooth four-manifold with spin-C structure \(\mathfrak s\), determinant line \(L\), and \(c=c_1(L)\in H^2(X;\mathbb Z)\). The chiral Dirac index is
\[\operatorname{ind}_{\mathbb C}(D_A^+)=\langle e^{c/2}\,\widehat A(TX),[X]\rangle
=\frac{\langle c^2,[X]\rangle-\sigma(X)}8.\]
Here \(\widehat A=1-\tfrac1{24}p_1+\cdots\), and the Hirzebruch signature theorem gives \(\langle p_1,[X]\rangle=3\sigma(X)\). The class \(c\) is characteristic: \(c\bmod2=w_2(TX)\); its characteristic congruence implies \(c^2\equiv\sigma(X)\pmod8\).

For \(X=\mathbb{CP}^2\), write \(h\in H^2(X;\mathbb Z)\), \(\langle h^2,[X]\rangle=1\), \(\sigma(X)=1\), and the canonical complex spin-C determinant \(c=3h\). Then \(\operatorname{ind}_\mathbb C D_A^+=(9-1)/8=1\). Twisting by \(Q\) with \(q=c_1(Q)\) sends \(c\mapsto c+2q\) and changes the index by \(\langle cq+q^2,[X]\rangle/2\), obtained by expanding \(((c+2q)^2-c^2)/8\). This is an integer because the characteristic-class congruence implies \(cq\equiv q^2\pmod 2\). This is the spin-C Dirac index, not the de Rham parity index \(\chi(X)\).

##### Exercises with answers

1. **Four-dimensional term.** Which terms of \(e^{c/2}\widehat A\) contribute to the index integral on a four-manifold? **Answer:** the degree-four terms \(c^2/8-p_1/24\).
2. **Projective plane.** For \(c=3h\), \(h^2=1\), and \(\sigma=1\), compute the index. **Answer:** one.
3. **Kernel.** Does index one force a one-dimensional kernel? **Answer:** no; kernel dimension minus cokernel dimension equals one.
4. **Twist.** If a spin-C structure is twisted by a line bundle with class \(q\), what happens to the determinant class? **Answer:** \(c\) becomes \(c+2q\).

##### Sources and further reading

- Tim Perutz, [Basics of Seiberg-Witten Theory](https://www.imperial.ac.uk/media/imperial-college/research-centres-and-groups/geometry/junior-geometry-seminar/Seiberg-Witten-theory.pdf).
- Liviu Nicolaescu, [Notes on Seiberg-Witten Theory](https://www3.nd.edu/~lnicolae/new1.pdf), Dirac index and characteristic classes.
- Overviews: [Atiyah-Singer index theorem](https://en.wikipedia.org/wiki/Atiyah%E2%80%93Singer_index_theorem), [Signature (topology)](https://en.wikipedia.org/wiki/Signature_(topology)), [Spin-C structure](https://en.wikipedia.org/wiki/Spinc_structure).
