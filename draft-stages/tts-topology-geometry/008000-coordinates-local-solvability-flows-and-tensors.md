# Coordinates, local solvability, flows, and tensors

<!-- BEGIN SPOKEN LECTURE -->

# Coordinates, local solvability, flows, and tensors

## Smooth Manifolds: Coordinates without a Global Grid

A globe cannot be flattened into a single ordinary map without seams or distortions. But a small neighborhood around nearly any point can be described using two coordinates. Change to another map, and the same location receives different numbers. Neither set of numbers is the globe itself. They are local descriptions of an underlying space.

A smooth manifold turns this observation into a mathematical framework. It is a space that looks locally like ordinary Euclidean space and whose overlapping coordinate systems change smoothly. Once we know how to compare coordinates on overlaps, we can define derivatives and tangent vectors intrinsically, without requiring the manifold to sit inside a larger Euclidean space.

### A chart is local, not global

Take a topological space M. An n-dimensional coordinate chart is an open subset U of M together with a homeomorphism from U onto an open subset of n-dimensional Euclidean space. The chart assigns n real coordinates to points in U. Another chart may cover a different region.

Where two charts overlap, the first set of coordinates can be converted into the second. The conversion is called a transition map. For smooth calculus, we require those transition maps and their inverses to be smooth. A collection of compatible charts is a smooth atlas. We regard atlases that fit together smoothly as giving the same smooth structure.

The usual definition also requires M to be Hausdorff and second-countable. These conditions rule out some topological pathologies and make standard theorems possible. The line with two origins, for example, can look locally like an ordinary line yet fail the Hausdorff condition. It is not a manifold under the standard definition.

A circle is a one-dimensional smooth manifold. We can describe a short arc by an angle, but one angle coordinate cannot cover the whole circle continuously and injectively. By overlapping multiple arcs we avoid the artificial discontinuity where a global angle would jump by a full turn. A sphere is a two-dimensional smooth manifold; local maps use two coordinates, even though the sphere is often drawn in three-dimensional space.

### What should a tangent vector be?

In elementary calculus, a velocity vector is the derivative of a curve. Suppose a smooth curve passes through a point p on our manifold. Choose coordinates near p and differentiate the coordinate functions of that curve with respect to time. We obtain n numbers, the coordinate components of its tangent velocity.

But another chart gives different components. Why can we say they describe the same tangent vector? Because the chain rule relates them: multiply the component column by the Jacobian matrix of the transition map. Since chart transitions are smooth with smooth inverses, that Jacobian is invertible. Tangent vectors in different charts are connected by a reversible change of coordinates.

We can turn this into an intrinsic definition. Two smooth curves through p represent the same tangent vector if their coordinate velocities agree in one, and hence every, chart. The resulting equivalence classes form the tangent space at p, an n-dimensional real vector space.

A second definition views a tangent vector as a rule that differentiates smooth functions near p. Such a rule is linear and obeys the product rule. Given a velocity vector v, evaluate it on a smooth function f by taking the derivative of f along any curve representing v. This yields a derivation at p. Conversely, every derivation comes from a tangent vector. The equivalence connects the geometric idea of velocity to the algebraic idea of differentiation.

### Tangent vectors on the circle and sphere

Embed the unit circle in the plane for a moment. A point has coordinates x and y satisfying x squared plus y squared equals one. A tangent velocity v with components a and b must preserve that equation to first order. Differentiate along a curve: two x times a plus two y times b equals zero. Thus the tangent line consists of vectors perpendicular to the radius.

At the point one, zero, tangent vectors are vertical. At the point zero, one, tangent vectors are horizontal. The tangent line changes as the point changes, but its dimension stays one.

For the unit sphere in three-dimensional space, the same calculation says that a tangent vector at p is perpendicular to the position vector p. Its tangent space is a two-dimensional plane. The ambient coordinates are convenient for this calculation, but the definition of tangent space does not require us to choose an embedding first.

These are examples of regular level sets. If a smooth function from n-dimensional Euclidean space to the real numbers has nonzero gradient on a level set, the implicit function theorem says that level set is locally an n minus one dimensional smooth manifold. The nonzero-gradient condition guarantees that one coordinate can locally be solved in terms of the others.

If the gradient vanishes, that conclusion is not automatic. The crossing of the coordinate axes in the plane is the zero set of x times y. At the origin it fails to look like one smooth line; four branches meet. A defining equation by itself does not guarantee a smooth manifold.

### Differentiating maps between manifolds

Suppose F maps one smooth manifold to another. We call F smooth when, after selecting suitable charts in the domain and target, its coordinate expression is a smooth map between Euclidean spaces. Smoothness does not depend on which compatible charts we chose: composing with smooth transition maps preserves it.

The derivative of F at p is a linear map from the tangent space at p to the tangent space at F of p. If v is the velocity of a curve through p, apply F to that curve and take its new velocity. In coordinates, the derivative is represented by the familiar Jacobian matrix. In different charts the numerical matrix changes, but the underlying tangent map is the same.

The chain rule now becomes a statement about tangent maps. The derivative of G composed with F is the derivative of G at F of p composed with the derivative of F at p. This is exactly the structure required for coordinate-independent calculus.

A smooth map with a smooth inverse is a diffeomorphism. Topological equivalence alone does not promise that a particular map is a diffeomorphism. For example, the map from the real line to itself that cubes its input is a homeomorphism, but its inverse is not differentiable at zero. It is not a diffeomorphism with the standard smooth structures.

### Why topology and calculus need each other

The local part of a smooth manifold is Euclidean calculus. The global part is topology: how charts are glued, how paths wind, whether a continuous vector field can be defined everywhere, and whether a local construction extends across the whole space.

On a circle it is possible to choose a continuous nonzero tangent direction everywhere. On the two-dimensional sphere it is not possible to choose a continuous tangent vector field that is nonzero at every point. That is the content of the hairy-ball theorem, which requires more topological machinery to prove. The contrast shows why local coordinate formulas cannot by themselves answer every global geometric question.

Smooth manifolds provide the setting for differential forms, vector fields, flows, metrics, and curvature. The essential achievement is that derivatives make sense even when no single coordinate system does. Once we have tangent spaces and maps between them, we can ask global geometric questions without being trapped by the map we happened to draw.

## Inverse and Implicit Function Theorems

A globe is round, but a street map is flat. Locally, the map can assign two numbers to each point on the Earth's surface. The fact that this works near a chosen point, but not necessarily with a single map for the entire globe, is a recurring theme in differential geometry. One of its analytic foundations is the inverse function theorem. A companion result, the implicit function theorem, explains why solutions of equations become smooth curves and surfaces.

To understand them, begin with something familiar. A real function might be increasing near a point. If its derivative there is nonzero, then near that point it changes its output reliably as its input changes. We should be able to run the process backward. For a function of several variables, increasing is no longer the right description. Instead, look at the derivative as a linear transformation. If that linear transformation has an inverse, then sufficiently close to the point the original nonlinear function does too.

### A derivative that can be inverted

Consider the transformation that takes a pair of numbers x and y to the pair x plus y, x minus y. It is already linear. Given the outputs u and v, we recover x by adding u and v and dividing by two, and y by subtracting v from u and dividing by two. Nothing is lost by the transformation: its derivative is the same invertible linear map at every point.

Now perturb it with nonlinear terms. We cannot generally solve the equations by inspection. Yet if the derivative at a point is still invertible, the inverse function theorem says there are neighborhoods of that point and its image on which the transformation has a smooth inverse. This is a local assertion. It does not say the transformation is injective everywhere, or that every possible output has an input.

Here is a concrete nonlinear case. Take the map sending x and y to x squared minus y squared and twice x y. Treat the plane, if you like, as complex numbers; this map is squaring. At the point with x equal to one and y equal to zero, its derivative multiplies every vector by two. That derivative is invertible. Near that point, we can choose one consistent square root of a nearby output. But there is another square root near negative one. The map is not globally one-to-one. Local inversion and global inversion are different questions.

At the origin, the derivative of the squaring map is zero. No neighborhood of the origin has an inverse of the kind the theorem promises. It is important not to reverse the theorem: a singular derivative does not always prevent an inverse as a set-theoretic function. For example, the real function x cubed is invertible everywhere, although its inverse has an infinite slope at zero and is not differentiable there. The theorem guarantees a smooth local inverse when the derivative is nonsingular.

### What the proof is trying to accomplish

Why should the linear derivative govern a nonlinear map? Fix a point and zoom in. The difference between the map and its first-order linear approximation becomes small relative to the distance being examined. If we seek the input corresponding to a target output, we can use the inverse of the derivative to correct a guess. Repeating the correction produces a fixed-point problem. On a sufficiently small neighborhood, the error term is controlled well enough that the iteration converges.

That is a proof strategy, not a substitute for the hypotheses. We use a continuously differentiable map on an open subset of Euclidean space, and the derivative must be invertible at the chosen point. Stronger smoothness in the original map passes to its local inverse. The essential analytic step is the control of the derivative's variation near the point.

### Solving an equation without finding an explicit formula

Suppose an equation says x squared plus y squared equals one. It describes a circle. Near the point where x is zero and y is one, we can solve for y as the positive square root of one minus x squared. This expresses the nearby circle as a graph over the x-axis. Near the point where x is one and y is zero, the same choice of dependent variable fails: as we move through the rightmost point, one x-value corresponds to two nearby y-values. But we can solve for x as a function of y instead.

The implicit function theorem turns this observation into a general method. Suppose F depends on x variables and y variables, and the equation F equals zero describes the objects of interest. If the derivative with respect to the y variables is invertible at a solution, then nearby solutions are exactly those of the form y equals a smooth function of x. We have chosen which variables are dependent and which are free. We have not claimed that all solutions everywhere can be represented by that graph.

For a circle, F is x squared plus y squared minus one. The derivative with respect to y is twice y. It is nonzero near the top of the circle, and zero at the rightmost point. That tells us exactly where a graph of y against x is guaranteed. The geometric circle does not stop being smooth at the rightmost point. Only our choice of graph coordinates becomes defective.

### Level sets and tangent spaces

This generalizes from curves to surfaces. Imagine a smooth function of three coordinates whose value is zero on a surface. At a point where its gradient is nonzero, at least one partial derivative is nonzero. We can solve for that coordinate as a function of the other two. So the zero set near that point is a smooth surface, whether or not we know an explicit solution.

The gradient also determines the tangent plane: a velocity tangent to the level surface must produce zero instantaneous change in F. Thus its dot product with the gradient is zero. For a sphere, the gradient points radially outward, while tangent velocities lie perpendicular to the radius. The implicit function theorem gives local coordinates; differentiation then gives the tangent space.

For several simultaneous equations, the gradient is replaced by a Jacobian matrix. If the derivative of a map from n-dimensional space to k-dimensional space has rank k at a point, with k no larger than n, its nearby level set is an n minus k dimensional manifold. Sometimes this is called the regular level-set theorem. When rank drops, strange things can happen: the zero set might cross itself, come to a point, or even remain perfectly smooth for another reason. Rank is a sufficient local condition, not a complete classification of every possible zero set.

### One more example: a constraint with a singularity

Take the equation x squared minus y squared equals zero. Its solutions are the two crossing lines y equals x and y equals negative x. Away from the origin each branch is an ordinary smooth curve. At the origin the gradient of F vanishes, and the whole solution set is not locally a single one-dimensional manifold. The missing rank hypothesis predicted where our smooth-manifold argument would break down.

Compare that with the equation x squared plus y squared equals zero over the real numbers. Its only solution is the origin. The same zero gradient appears, but the solution set is now an isolated point, not crossing branches. The failure of regularity allows several different geometries. It does not specify which one occurs.

These theorems are the bridge from calculus to the local geometry of manifolds. They tell us when coordinates can be exchanged, when constraints leave a smooth space of solutions, and why the right dimension is the number of free variables after independent constraints. The word local matters at every step. The payoff is that we can study geometric objects without first finding a single global formula for them.

## Vector Fields, Flows, and Lie Brackets

A tangent vector at one point describes an instantaneous velocity. A vector field describes a velocity at every point. Think of a steady wind above a landscape: at each location an arrow tells a small particle where to move next. The arrows need not all point in the same direction. What interests us is not only the collection of arrows but the paths traced by particles following them.

On a smooth manifold the picture is the same, except there may be no global coordinate grid. A smooth vector field assigns to each point a tangent vector, and those vectors vary smoothly when expressed in a chart. It does not, in general, assign a single arrow inside one fixed ambient vector space. The arrow at one point belongs to its tangent space, and the arrow at another belongs to a different tangent space.

### From an arrow to a motion

In the plane, let the velocity field send the point with coordinates x and y to the arrow pointing x units in the horizontal direction and y units in the vertical direction. A moving point obeys the equations: the time derivative of x equals x, and the time derivative of y equals y. Starting at coordinates a and b, its path is given by a times the exponential of time and b times the same exponential. Each point moves radially outward for positive time.

The collection of motions is called a flow. Write the operation as: take a point, evolve for time t, and return its new point. Evolving for time zero does nothing. If the solution exists for both time intervals, evolving for time s and then time t is the same as evolving for time s plus t. This is the flow property.

Why the qualification about existence? Consider the one-dimensional field whose velocity is x squared. Starting at a positive x, its solution grows faster and faster and becomes unbounded at a finite time. The vector field is perfectly smooth on the real line, but its flow is not defined for all future times from every point. A field whose solutions exist for all real times is called complete. Smoothness alone does not imply completeness on a noncompact manifold. On a compact smooth manifold without boundary, every smooth vector field is complete.

### Flows let us differentiate functions geometrically

Take a height function f on the surface. Follow the flow of a vector field X, watching how the height changes. Its instantaneous rate is the directional derivative X applied to f. So a vector field can be treated as an operator taking smooth functions to smooth functions. This operator obeys the product rule: X applied to f times g equals X applied to f, times g, plus f times X applied to g.

The product rule is more than convenient notation. It explains why a tangent vector can be defined without reference to an embedding: a tangent vector at a point is a first-order derivation of smooth functions at that point. A vector field is a compatible family of such derivations.

### Two motions may interfere

Imagine moving east and then north. In a flat coordinate grid with constant velocities, this reaches the same endpoint as moving north and then east. But what if the amount of movement in one direction depends on where the other movement has taken you? The two orders may differ.

Take X to be motion to the right at speed one. Take Y to be motion upward at a speed equal to the current x coordinate. Begin at the origin. If you move right a small distance, then move according to Y for a short time, the upward motion sees a positive x and moves you upward. If you use Y first, at the origin it has zero speed, so you gain no height before moving right. The difference between the two routes is of second order in the small time intervals.

This discrepancy is measured by the Lie bracket of X and Y. It is again a vector field, formed by applying X to the coefficients of Y and subtracting the effect of applying Y to the coefficients of X. In our example the bracket is simply the constant unit upward field. The bracket is not an invented extra direction: it records a direction of motion obtainable to leading order by a tiny loop of alternating available motions.

The exact sign depends on the order chosen for the four little moves. With the conventional bracket, X bracket Y means X acts on the operator Y minus Y acts on X. Reversing the bracket reverses its sign. The important invariant point is that this discrepancy can be computed in any coordinate chart and gives the same geometric vector field.

### Why ordinary subtraction of arrows is not enough

At one point in the plane we can subtract two vectors, but a Lie bracket is not the difference X minus Y. It measures how each field changes in the direction of the other. Constant coordinate fields commute, so their bracket is zero even though the arrows differ. A varying pair may have a nonzero bracket even when the two arrows are linearly independent everywhere.

For a general smooth function f, the bracket acts by first applying Y then X and subtracting first applying X then Y. This operator definition immediately explains two properties: the bracket is antisymmetric, and it obeys the Jacobi identity. These are the laws of a Lie algebra. The collection of all smooth vector fields on a manifold is an infinite-dimensional Lie algebra under this operation.

### Coordinates and change of chart

In local coordinates, a field has components attached to the coordinate directions. If we change coordinates, the components change by the Jacobian, just as tangent vector components do. We must also change the derivatives that act on those components. The resulting bracket formula is compatible with this change; we have not privileged the original x and y axes.

There is another intrinsic description. A flow moves points around the manifold, and the derivative of the flow pushes tangent vectors forward. To compare a field before and after flowing, we transport it back using that derivative. The rate of change of this transported field is the Lie derivative; applied to a second vector field it produces the Lie bracket, with a sign convention fixed by which transport direction we use.

### A bridge to geometry and control

Lie brackets are useful whenever two allowed movements combine into something that neither movement can achieve instantly. A vehicle may move forward and turn but cannot instantly slide sideways. By steering through a sequence of short motions it can change its sideways position. The mathematics of such effects belongs to nonholonomic control and distributions of tangent directions. One must be careful: the ability to generate bracket directions is part of a theorem with hypotheses, not a promise that any arbitrary control problem is solvable.

Vector fields also generate symmetries. Rotating a sphere continuously around its axis is a flow. Differentiating a function along that rotation tells us how it changes under the symmetry. A zero derivative means the function is constant along the rotation orbits. This is the beginning of a geometric way to study conservation laws and invariants.

The conceptual chain is now complete. A vector field assigns a velocity. Differential equations turn velocities into local motions. A field acts on functions by differentiation. Comparing the orders of two motions yields the Lie bracket. These constructions belong to the manifold itself, not to the coordinates drawn on it.

## Cotangent Vectors, Tensors, and Pullbacks

The speed of a particle can be described by a tangent vector. But what sort of object measures the rate at which the particle climbs a hill? A height function f has a differential, which takes the particle's tangent velocity and returns the instantaneous rate of change of height. The velocity and the measurement live in different, complementary spaces. Keeping them separate is one of the most useful habits in geometry.

At a point p of a manifold, the tangent space consists of possible velocities. Its dual space, called the cotangent space, consists of linear functions on those velocities. An element of the cotangent space is a covector. Given a vector v and covector alpha at the same point, alpha of v is a real number. This evaluation does not require a metric, an angle, or a coordinate chart.

### Why the components transform differently

Suppose the x coordinate is measured in meters. Introduce a new coordinate u equal to one hundred times x, so u is the numerical count of centimeters. A velocity of two meters per second has x component two, but u component two hundred. Meanwhile the covector d x, which measures the rate of change of x, becomes one one-hundredth of d u. Pair the components and their scaling cancels. The geometric rate is unchanged.

The simple scaling example exhibits a general pattern. Vectors transform by the derivative of the new coordinates with respect to the old. Covectors transform in the opposite direction, by the inverse relation that preserves evaluation. We sometimes call the first behavior contravariant components and the second covariant components, although there are different textbook indexing conventions for how to describe these. The point is to watch the pairing rather than memorize the adjectives.

### A map pushes velocities and pulls measurements

Let F be a smooth map from one manifold M to another N. Its differential sends a tangent vector at p in M to a tangent vector at F of p in N. We call this the pushforward of the vector at that point. It describes how a trajectory's velocity changes after we apply F.

A covector on N travels the other way. To apply it to a vector at p, first push that vector through F, then evaluate the covector at F of p. This produces a covector on M. We call the operation pullback. It is defined even when F is not invertible. There is generally no analogous canonical pushforward of arbitrary covector fields through a many-to-one map.

Take F from the plane to itself with u equals x squared and v equals y. The covector d u on the target pulls back to two x times d x on the source. At a point where x equals three, a small horizontal source velocity is magnified by six in the u coordinate. The pullback of d u reports precisely this factor. At x equal to zero, the derivative in that direction vanishes. Pullback still makes perfect sense there, even though F lacks a smooth local inverse.

There is an elegant chain-rule identity behind this. If g is a smooth scalar function on the target, pulling back its differential is the same as differentiating g composed with F. In words: measure the change of g after mapping forward, or first pull its measurement backward. The answer is identical.

### Tensor fields add more inputs

A covector takes one tangent vector and returns a number. What if a geometric measurement needs two velocities? A bilinear form takes two vectors. The metric of Euclidean geometry is a symmetric bilinear form: it takes two vectors and returns their dot product. Feed it a vector twice and you obtain squared length.

On a curved surface, a Riemannian metric is a smoothly varying positive-definite symmetric bilinear form on the tangent spaces. It lets us measure lengths and angles without requiring an ambient plane or space. In local coordinates it is described by a matrix of functions, and under change of chart that matrix transforms using a Jacobian on both inputs. It is not legitimate to keep the same component matrix after a nonlinear coordinate change.

A two-form also takes two vectors, but is antisymmetric rather than symmetric. The basic plane area form d x wedge d y returns the signed area spanned by two vectors. Swapping the inputs reverses the sign. This distinction is fundamental: metrics encode lengths and angles, while alternating forms encode oriented area, volume, and integrands for Stokes' theorem.

More generally, a tensor at a point is a multilinear object with specified vector and covector inputs. A field of such tensors varies smoothly across the manifold. Once we know how each input transforms, the whole object transforms by composing those rules. This is the point of tensor notation: the object is invariantly defined; a chart supplies one way to describe its components.

### The covector called the differential

For every smooth scalar function f, the differential d f is a covector field. At a point it acts on a velocity v by taking the directional derivative of f. Many people first meet this idea as a gradient. But the gradient is actually a vector and depends on a metric. The differential does not.

In standard Euclidean coordinates we use the dot product to turn the differential into the gradient vector. On a surface with another metric, the gradient can point in a different coordinate direction from what a naive list of partial derivatives suggests. If we work in polar coordinates, for example, the angular component of the gradient contains a factor of one over radius squared relative to the coefficient of d theta. That factor comes from the metric, not from the definition of the differential.

This separation matters whenever coordinates are stretched. You should not identify a column of partial derivatives with a geometric vector without specifying the rule used to raise the index. The metric supplies that rule.

### Pulling back an area form

Consider the map from coordinates r and theta to the plane: x equals r cosine theta, y equals r sine theta. The pullback of d x wedge d y is r times d r wedge d theta, for positive r. That familiar factor of r in polar integration is not an arbitrary correction inserted by calculus textbooks. It comes from how the area form transforms under the map.

If we reverse orientation, the pullback may acquire a negative sign. If we only want unsigned area, we take the absolute value of the Jacobian determinant in the usual change-of-variables formula. Differential forms instead remember orientation, so the signed Jacobian appears naturally. This explains both the agreement and the difference between oriented form integration and the conventional positive-volume integral.

The picture now fits together. Tangent vectors describe motions, covectors test those motions, tensors combine tests and motions into more elaborate measurements, and pullback transfers measurements along smooth maps. These rules were designed to survive changes of coordinates. They give us the language needed to describe differential forms, metrics, and connections without confusing an object with its component table.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Smooth Manifolds: Coordinates without a Global Grid

**Track:** Topology and Geometry. **Background:** topology, multivariable calculus, smooth functions, and linear algebra. **Question:** what does differentiation mean on a space that has no global coordinates?

#### Mathematical companion (not spoken)

A smooth \(n\)-manifold is a Hausdorff, second-countable space locally homeomorphic to open subsets of \(\mathbb R^n\), equipped with a maximal atlas whose transition maps are \(C^\infty\) diffeomorphisms on overlaps. Charts \((U,\varphi)\), \((V,\psi)\) have transition map
\[
\psi\circ\varphi^{-1}:\varphi(U\cap V)\longrightarrow\psi(U\cap V).
\]

**Tangent via curves.** A tangent vector at \(p\) is an equivalence class of curves \(\gamma:(-\epsilon,\epsilon)\to M\) through \(p\), with two curves equivalent if their coordinate derivatives at zero agree. Under a chart change, \(v_\psi=D(\psi\circ\varphi^{-1})_{\varphi(p)}v_\varphi\).

**Tangent via derivations.** \(T_pM\cong\{D:C_p^\infty(M)\to\mathbb R: D(fg)=f(p)Dg+g(p)Df\}\), where \(C_p^\infty(M)\) denotes germs of smooth functions at \(p\).

**Sphere.** For \(S^{n-1}=\{x\in\mathbb R^n:\lVert x\rVert^2=1\}\), the regular level-set theorem gives
\[
T_pS^{n-1}=\{v\in\mathbb R^n:p\cdot v=0\}.
\]

**Chain rule.** For smooth \(F:M\to N\) and \(G:N\to P\), \(d(G\circ F)_p=dG_{F(p)}\circ dF_p\).

##### Exercises with answers

1. What is the dimension of \(T_p S^2\)? **Answer:** two.
2. Find a tangent direction to \(S^1\) at \((3/5,4/5)\). **Answer:** \((-4/5,3/5)\), or any scalar multiple.
3. Why can one compute smoothness in any compatible charts? **Answer:** coordinate expressions are related by smooth transition maps, and compositions of smooth maps are smooth.
4. Why is \(x\mapsto x^3\) not a diffeomorphism of the standard real line? **Answer:** its inverse cube-root map is not differentiable at zero.

##### Reading

MIT 18.965, [Geometry of Manifolds lecture notes](https://ocw.mit.edu/courses/18-965-geometry-of-manifolds-fall-2004/pages/lecture-notes/), manifolds, tangent spaces, and smooth maps; John M. Lee, *Introduction to Smooth Manifolds*, second edition, Springer Graduate Texts in Mathematics 218.

### Inverse and Implicit Function Theorems

**Track:** Topology and Geometry. **Background:** derivatives in several variables, linear maps, smooth charts. **Question:** when can a geometric equation be solved locally for coordinates?

#### Mathematical companion (not spoken)

**Inverse function theorem.** For a \(C^r\) map \(F:U\subset\mathbb R^n\to\mathbb R^n\), \(r\ge1\), if \(DF(a)\) is invertible, then some neighborhoods \(V\ni a\), \(W\ni F(a)\) satisfy \(F|_V:V\to W\) is a \(C^r\) diffeomorphism, with
\[
D(F^{-1})_{F(a)}=(DF_a)^{-1}.
\]
The complex-squaring example \(F(x,y)=(x^2-y^2,2xy)\) has
\[DF(x,y)=\begin{pmatrix}2x&-2y\\2y&2x\end{pmatrix},\qquad\det DF=4(x^2+y^2).\]

**Implicit function theorem.** Let \(F:\mathbb R^m\times\mathbb R^k\to\mathbb R^k\) be \(C^r\), \(F(a,b)=0\), and \(D_yF(a,b)\) invertible. Locally the solution set is \(\{(x,g(x))\}\), with
\[Dg(a)=-[D_yF(a,b)]^{-1}D_xF(a,b).\]
If \(f:M^n\to N^k\) has surjective differential along \(f^{-1}(q)\), then \(f^{-1}(q)\) is a submanifold of dimension \(n-k\), assuming the preimage is nonempty.

##### Check your understanding

1. Find the dimension of the regular level set \(x^2+y^2+z^2=4\). **Answer:** two, since the gradient is nonzero on the sphere.
2. Why can the real cubic map be inverted near zero although its derivative vanishes? **Answer:** it has a continuous but not differentiable inverse; the smooth inverse theorem does not apply.
3. For \(F(x,y)=x^2+y^2-1\), compute \(dy/dx\) near \((0,1)\). **Answer:** \(-x/y\).

##### Reading and sources

- MIT OCW, [Geometry of Manifolds, Lecture 4: Inverse and Implicit Function Theorems](https://ocw.mit.edu/courses/18-965-geometry-of-manifolds-fall-2004/pages/lecture-notes/).
- Overview: [Inverse function theorem](https://en.wikipedia.org/wiki/Inverse_function_theorem) and [Implicit function theorem](https://en.wikipedia.org/wiki/Implicit_function_theorem).

### Vector Fields, Flows, and Lie Brackets

**Track:** Topology and Geometry. **Background:** tangent spaces, derivatives, differential equations. **Question:** what does it mean to move through a manifold under a smoothly varying velocity?

#### Mathematical companion (not spoken)

For \(X=\sum_i X^i\partial_i\) and \(Y=\sum_iY^i\partial_i\) in a smooth chart,
\[
[X,Y]=\sum_j\left(\sum_i X^i\partial_iY^j-Y^i\partial_iX^j\right)\partial_j,
\quad [X,Y](f)=X(Yf)-Y(Xf).
\]
For \(X=\partial_x\) and \(Y=x\partial_y\), \([X,Y]=\partial_y\).
A local flow \(\Phi_t\) solves \(\frac{d}{dt}\Phi_t(p)=X_{\Phi_t(p)}\), \(\Phi_0(p)=p\). When defined, \(\Phi_t\circ\Phi_s=\Phi_{t+s}\). The solution for \(x'=x^2\) with \(x(0)=a>0\) is \(x(t)=a/(1-at)\), which blows up at \(1/a\).

##### Check your understanding

1. Compute \([\partial_x,x^2\partial_y]\). **Answer:** \(2x\partial_y\).
2. Does a zero bracket imply the fields themselves coincide? **No:** \(\partial_x\) and \(\partial_y\) are different, commuting fields.
3. Is every smooth vector field on \(\mathbb R\) complete? **No:** \(x^2\partial_x\) is not.

##### Reading and sources

- MIT OCW, [Geometry of Manifolds](https://ocw.mit.edu/courses/18-965-geometry-of-manifolds-fall-2004/pages/lecture-notes/), lecture on the Lie derivative and prerequisites on tangent bundles.
- Overview: [Vector field](https://en.wikipedia.org/wiki/Vector_field), [Flow (mathematics)](https://en.wikipedia.org/wiki/Flow_(mathematics)), [Lie bracket of vector fields](https://en.wikipedia.org/wiki/Lie_bracket_of_vector_fields).

### Cotangent Vectors, Tensors, and Pullbacks

**Track:** Topology and Geometry. **Background:** smooth maps, chain rule, tangent vectors. **Question:** how do measurements of vectors transform under coordinate changes and smooth maps?

#### Mathematical companion (not spoken)

For \(F:M\to N\), \(dF_p:T_pM\to T_{F(p)}N\). If \(\alpha\in T^*_{F(p)}N\),
\[(F^*\alpha)_p(v)=\alpha_{F(p)}(dF_pv),\qquad F^*(dg)=d(g\circ F).\]
For a covariant \((0,2)\)-tensor \(g\), \((F^*g)_p(u,v)=g_{F(p)}(dF_pu,dF_pv)\). If local coordinates satisfy \(y=y(x)\), metric components obey \(g_{ij}^{(x)}=\frac{\partial y^a}{\partial x^i}\frac{\partial y^b}{\partial x^j}g_{ab}^{(y)}\).

**Polar coordinates.** \(F(r,\theta)=(r\cos\theta,r\sin\theta)\). Then
\[F^*(dx\wedge dy)=r\,dr\wedge d\theta,\quad F^*(dx^2+dy^2)=dr^2+r^2d\theta^2.\]
The Riemannian gradient is specified by \(g(\operatorname{grad}f,v)=df(v)\), so \(\operatorname{grad} f=\partial_r f\,\partial_r+r^{-2}\partial_\theta f\,\partial_\theta\) for \(r>0\).

##### Check your understanding

1. Under \(u=100x\), how is \(dx\) expressed? **Answer:** \(dx=du/100\).
2. Why can one pull back a one-form through a non-invertible map? **Answer:** pullback only requires the forward differential on tangent vectors.
3. Is the gradient of \(f\) defined without a metric? **No:** \(df\) is intrinsic; turning it into a vector requires a metric or equivalent pairing.

##### Reading and sources

- MIT OCW, [Geometry of Manifolds](https://ocw.mit.edu/courses/18-965-geometry-of-manifolds-fall-2004/pages/lecture-notes/), derivatives, vector bundles and exterior algebra.
- Overview: [Cotangent space](https://en.wikipedia.org/wiki/Cotangent_space), [Pullback (differential geometry)](https://en.wikipedia.org/wiki/Pullback_(differential_geometry)), [Tensor field](https://en.wikipedia.org/wiki/Tensor_field).
