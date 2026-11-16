# 008100 - Inverse and Implicit Function Theorems

**Track:** Topology and Geometry. **Background:** derivatives in several variables, linear maps, smooth charts. **Question:** when can a geometric equation be solved locally for coordinates?

<!-- BEGIN SPOKEN LECTURE -->

# Inverse and Implicit Function Theorems

A globe is round, but a street map is flat. Locally, the map can assign two numbers to each point on the Earth's surface. The fact that this works near a chosen point, but not necessarily with a single map for the entire globe, is a recurring theme in differential geometry. One of its analytic foundations is the inverse function theorem. A companion result, the implicit function theorem, explains why solutions of equations become smooth curves and surfaces.

To understand them, begin with something familiar. A real function might be increasing near a point. If its derivative there is nonzero, then near that point it changes its output reliably as its input changes. We should be able to run the process backward. For a function of several variables, increasing is no longer the right description. Instead, look at the derivative as a linear transformation. If that linear transformation has an inverse, then sufficiently close to the point the original nonlinear function does too.

## A derivative that can be inverted

Consider the transformation that takes a pair of numbers x and y to the pair x plus y, x minus y. It is already linear. Given the outputs u and v, we recover x by adding u and v and dividing by two, and y by subtracting v from u and dividing by two. Nothing is lost by the transformation: its derivative is the same invertible linear map at every point.

Now perturb it with nonlinear terms. We cannot generally solve the equations by inspection. Yet if the derivative at a point is still invertible, the inverse function theorem says there are neighborhoods of that point and its image on which the transformation has a smooth inverse. This is a local assertion. It does not say the transformation is injective everywhere, or that every possible output has an input.

Here is a concrete nonlinear case. Take the map sending x and y to x squared minus y squared and twice x y. Treat the plane, if you like, as complex numbers; this map is squaring. At the point with x equal to one and y equal to zero, its derivative multiplies every vector by two. That derivative is invertible. Near that point, we can choose one consistent square root of a nearby output. But there is another square root near negative one. The map is not globally one-to-one. Local inversion and global inversion are different questions.

At the origin, the derivative of the squaring map is zero. No neighborhood of the origin has an inverse of the kind the theorem promises. It is important not to reverse the theorem: a singular derivative does not always prevent an inverse as a set-theoretic function. For example, the real function x cubed is invertible everywhere, although its inverse has an infinite slope at zero and is not differentiable there. The theorem guarantees a smooth local inverse when the derivative is nonsingular.

## What the proof is trying to accomplish

Why should the linear derivative govern a nonlinear map? Fix a point and zoom in. The difference between the map and its first-order linear approximation becomes small relative to the distance being examined. If we seek the input corresponding to a target output, we can use the inverse of the derivative to correct a guess. Repeating the correction produces a fixed-point problem. On a sufficiently small neighborhood, the error term is controlled well enough that the iteration converges.

That is a proof strategy, not a substitute for the hypotheses. We use a continuously differentiable map on an open subset of Euclidean space, and the derivative must be invertible at the chosen point. Stronger smoothness in the original map passes to its local inverse. The essential analytic step is the control of the derivative's variation near the point.

## Solving an equation without finding an explicit formula

Suppose an equation says x squared plus y squared equals one. It describes a circle. Near the point where x is zero and y is one, we can solve for y as the positive square root of one minus x squared. This expresses the nearby circle as a graph over the x-axis. Near the point where x is one and y is zero, the same choice of dependent variable fails: as we move through the rightmost point, one x-value corresponds to two nearby y-values. But we can solve for x as a function of y instead.

The implicit function theorem turns this observation into a general method. Suppose F depends on x variables and y variables, and the equation F equals zero describes the objects of interest. If the derivative with respect to the y variables is invertible at a solution, then nearby solutions are exactly those of the form y equals a smooth function of x. We have chosen which variables are dependent and which are free. We have not claimed that all solutions everywhere can be represented by that graph.

For a circle, F is x squared plus y squared minus one. The derivative with respect to y is twice y. It is nonzero near the top of the circle, and zero at the rightmost point. That tells us exactly where a graph of y against x is guaranteed. The geometric circle does not stop being smooth at the rightmost point. Only our choice of graph coordinates becomes defective.

## Level sets and tangent spaces

This generalizes from curves to surfaces. Imagine a smooth function of three coordinates whose value is zero on a surface. At a point where its gradient is nonzero, at least one partial derivative is nonzero. We can solve for that coordinate as a function of the other two. So the zero set near that point is a smooth surface, whether or not we know an explicit solution.

The gradient also determines the tangent plane: a velocity tangent to the level surface must produce zero instantaneous change in F. Thus its dot product with the gradient is zero. For a sphere, the gradient points radially outward, while tangent velocities lie perpendicular to the radius. The implicit function theorem gives local coordinates; differentiation then gives the tangent space.

For several simultaneous equations, the gradient is replaced by a Jacobian matrix. If the derivative of a map from n-dimensional space to k-dimensional space has rank k at a point, with k no larger than n, its nearby level set is an n minus k dimensional manifold. Sometimes this is called the regular level-set theorem. When rank drops, strange things can happen: the zero set might cross itself, come to a point, or even remain perfectly smooth for another reason. Rank is a sufficient local condition, not a complete classification of every possible zero set.

## One more example: a constraint with a singularity

Take the equation x squared minus y squared equals zero. Its solutions are the two crossing lines y equals x and y equals negative x. Away from the origin each branch is an ordinary smooth curve. At the origin the gradient of F vanishes, and the whole solution set is not locally a single one-dimensional manifold. The missing rank hypothesis predicted where our smooth-manifold argument would break down.

Compare that with the equation x squared plus y squared equals zero over the real numbers. Its only solution is the origin. The same zero gradient appears, but the solution set is now an isolated point, not crossing branches. The failure of regularity allows several different geometries. It does not specify which one occurs.

These theorems are the bridge from calculus to the local geometry of manifolds. They tell us when coordinates can be exchanged, when constraints leave a smooth space of solutions, and why the right dimension is the number of free variables after independent constraints. The word local matters at every step. The payoff is that we can study geometric objects without first finding a single global formula for them.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

**Inverse function theorem.** For a \(C^r\) map \(F:U\subset\mathbb R^n\to\mathbb R^n\), \(r\ge1\), if \(DF(a)\) is invertible, then some neighborhoods \(V\ni a\), \(W\ni F(a)\) satisfy \(F|_V:V\to W\) is a \(C^r\) diffeomorphism, with
\[
D(F^{-1})_{F(a)}=(DF_a)^{-1}.
\]
The complex-squaring example \(F(x,y)=(x^2-y^2,2xy)\) has
\[DF(x,y)=\begin{pmatrix}2x&-2y\\2y&2x\end{pmatrix},\qquad\det DF=4(x^2+y^2).\]

**Implicit function theorem.** Let \(F:\mathbb R^m\times\mathbb R^k\to\mathbb R^k\) be \(C^r\), \(F(a,b)=0\), and \(D_yF(a,b)\) invertible. Locally the solution set is \(\{(x,g(x))\}\), with
\[Dg(a)=-[D_yF(a,b)]^{-1}D_xF(a,b).\]
If \(f:M^n\to N^k\) has surjective differential along \(f^{-1}(q)\), then \(f^{-1}(q)\) is a submanifold of dimension \(n-k\), assuming the preimage is nonempty.

### Check your understanding

1. Find the dimension of the regular level set \(x^2+y^2+z^2=4\). **Answer:** two, since the gradient is nonzero on the sphere.
2. Why can the real cubic map be inverted near zero although its derivative vanishes? **Answer:** it has a continuous but not differentiable inverse; the smooth inverse theorem does not apply.
3. For \(F(x,y)=x^2+y^2-1\), compute \(dy/dx\) near \((0,1)\). **Answer:** \(-x/y\).

### Reading and sources

- MIT OCW, [Geometry of Manifolds, Lecture 4: Inverse and Implicit Function Theorems](https://ocw.mit.edu/courses/18-965-geometry-of-manifolds-fall-2004/pages/lecture-notes/).
- Overview: [Inverse function theorem](https://en.wikipedia.org/wiki/Inverse_function_theorem) and [Implicit function theorem](https://en.wikipedia.org/wiki/Implicit_function_theorem).
