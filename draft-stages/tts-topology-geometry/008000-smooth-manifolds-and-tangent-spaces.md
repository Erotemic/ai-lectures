# 008000 — Smooth Manifolds: Coordinates without a Global Grid

**Track:** Topology and Geometry. **Background:** topology, multivariable calculus, smooth functions, and linear algebra. **Question:** what does differentiation mean on a space that has no global coordinates?

<!-- BEGIN SPOKEN LECTURE -->

# Smooth Manifolds: Coordinates without a Global Grid

A globe cannot be flattened into a single ordinary map without seams or distortions. But a small neighborhood around nearly any point can be described using two coordinates. Change to another map, and the same location receives different numbers. Neither set of numbers is the globe itself. They are local descriptions of an underlying space.

A smooth manifold turns this observation into a mathematical framework. It is a space that looks locally like ordinary Euclidean space and whose overlapping coordinate systems change smoothly. Once we know how to compare coordinates on overlaps, we can define derivatives and tangent vectors intrinsically, without requiring the manifold to sit inside a larger Euclidean space.

## A chart is local, not global

Take a topological space M. An n-dimensional coordinate chart is an open subset U of M together with a homeomorphism from U onto an open subset of n-dimensional Euclidean space. The chart assigns n real coordinates to points in U. Another chart may cover a different region.

Where two charts overlap, the first set of coordinates can be converted into the second. The conversion is called a transition map. For smooth calculus, we require those transition maps and their inverses to be smooth. A collection of compatible charts is a smooth atlas. We regard atlases that fit together smoothly as giving the same smooth structure.

The usual definition also requires M to be Hausdorff and second-countable. These conditions rule out some topological pathologies and make standard theorems possible. The line with two origins, for example, can look locally like an ordinary line yet fail the Hausdorff condition. It is not a manifold under the standard definition.

A circle is a one-dimensional smooth manifold. We can describe a short arc by an angle, but one angle coordinate cannot cover the whole circle continuously and injectively. By overlapping multiple arcs we avoid the artificial discontinuity where a global angle would jump by a full turn. A sphere is a two-dimensional smooth manifold; local maps use two coordinates, even though the sphere is often drawn in three-dimensional space.

## What should a tangent vector be?

In elementary calculus, a velocity vector is the derivative of a curve. Suppose a smooth curve passes through a point p on our manifold. Choose coordinates near p and differentiate the coordinate functions of that curve with respect to time. We obtain n numbers, the coordinate components of its tangent velocity.

But another chart gives different components. Why can we say they describe the same tangent vector? Because the chain rule relates them: multiply the component column by the Jacobian matrix of the transition map. Since chart transitions are smooth with smooth inverses, that Jacobian is invertible. Tangent vectors in different charts are connected by a reversible change of coordinates.

We can turn this into an intrinsic definition. Two smooth curves through p represent the same tangent vector if their coordinate velocities agree in one, and hence every, chart. The resulting equivalence classes form the tangent space at p, an n-dimensional real vector space.

A second definition views a tangent vector as a rule that differentiates smooth functions near p. Such a rule is linear and obeys the product rule. Given a velocity vector v, evaluate it on a smooth function f by taking the derivative of f along any curve representing v. This yields a derivation at p. Conversely, every derivation comes from a tangent vector. The equivalence connects the geometric idea of velocity to the algebraic idea of differentiation.

## Tangent vectors on the circle and sphere

Embed the unit circle in the plane for a moment. A point has coordinates x and y satisfying x squared plus y squared equals one. A tangent velocity v with components a and b must preserve that equation to first order. Differentiate along a curve: two x times a plus two y times b equals zero. Thus the tangent line consists of vectors perpendicular to the radius.

At the point one, zero, tangent vectors are vertical. At the point zero, one, tangent vectors are horizontal. The tangent line changes as the point changes, but its dimension stays one.

For the unit sphere in three-dimensional space, the same calculation says that a tangent vector at p is perpendicular to the position vector p. Its tangent space is a two-dimensional plane. The ambient coordinates are convenient for this calculation, but the definition of tangent space does not require us to choose an embedding first.

These are examples of regular level sets. If a smooth function from n-dimensional Euclidean space to the real numbers has nonzero gradient on a level set, the implicit function theorem says that level set is locally an n minus one dimensional smooth manifold. The nonzero-gradient condition guarantees that one coordinate can locally be solved in terms of the others.

If the gradient vanishes, that conclusion is not automatic. The crossing of the coordinate axes in the plane is the zero set of x times y. At the origin it fails to look like one smooth line; four branches meet. A defining equation by itself does not guarantee a smooth manifold.

## Differentiating maps between manifolds

Suppose F maps one smooth manifold to another. We call F smooth when, after selecting suitable charts in the domain and target, its coordinate expression is a smooth map between Euclidean spaces. Smoothness does not depend on which compatible charts we chose: composing with smooth transition maps preserves it.

The derivative of F at p is a linear map from the tangent space at p to the tangent space at F of p. If v is the velocity of a curve through p, apply F to that curve and take its new velocity. In coordinates, the derivative is represented by the familiar Jacobian matrix. In different charts the numerical matrix changes, but the underlying tangent map is the same.

The chain rule now becomes a statement about tangent maps. The derivative of G composed with F is the derivative of G at F of p composed with the derivative of F at p. This is exactly the structure required for coordinate-independent calculus.

A smooth map with a smooth inverse is a diffeomorphism. Topological equivalence alone does not promise that a particular map is a diffeomorphism. For example, the map from the real line to itself that cubes its input is a homeomorphism, but its inverse is not differentiable at zero. It is not a diffeomorphism with the standard smooth structures.

## Why topology and calculus need each other

The local part of a smooth manifold is Euclidean calculus. The global part is topology: how charts are glued, how paths wind, whether a continuous vector field can be defined everywhere, and whether a local construction extends across the whole space.

On a circle it is possible to choose a continuous nonzero tangent direction everywhere. On the two-dimensional sphere it is not possible to choose a continuous tangent vector field that is nonzero at every point. That is the content of the hairy-ball theorem, which requires more topological machinery to prove. The contrast shows why local coordinate formulas cannot by themselves answer every global geometric question.

Smooth manifolds provide the setting for differential forms, vector fields, flows, metrics, and curvature. The essential achievement is that derivatives make sense even when no single coordinate system does. Once we have tangent spaces and maps between them, we can ask global geometric questions without being trapped by the map we happened to draw.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

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

### Exercises with answers

1. What is the dimension of \(T_p S^2\)? **Answer:** two.
2. Find a tangent direction to \(S^1\) at \((3/5,4/5)\). **Answer:** \((-4/5,3/5)\), or any scalar multiple.
3. Why can one compute smoothness in any compatible charts? **Answer:** coordinate expressions are related by smooth transition maps, and compositions of smooth maps are smooth.
4. Why is \(x\mapsto x^3\) not a diffeomorphism of the standard real line? **Answer:** its inverse cube-root map is not differentiable at zero.

### Reading

MIT 18.965, [Geometry of Manifolds lecture notes](https://ocw.mit.edu/courses/18-965-geometry-of-manifolds-fall-2004/pages/lecture-notes/), manifolds, tangent spaces, and smooth maps; John M. Lee, *Introduction to Smooth Manifolds*, second edition, Springer Graduate Texts in Mathematics 218.
