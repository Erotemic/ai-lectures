# 008200 - Vector Fields, Flows, and Lie Brackets

**Track:** Topology and Geometry. **Background:** tangent spaces, derivatives, differential equations. **Question:** what does it mean to move through a manifold under a smoothly varying velocity?

<!-- BEGIN SPOKEN LECTURE -->

# Vector Fields, Flows, and Lie Brackets

A tangent vector at one point describes an instantaneous velocity. A vector field describes a velocity at every point. Think of a steady wind above a landscape: at each location an arrow tells a small particle where to move next. The arrows need not all point in the same direction. What interests us is not only the collection of arrows but the paths traced by particles following them.

On a smooth manifold the picture is the same, except there may be no global coordinate grid. A smooth vector field assigns to each point a tangent vector, and those vectors vary smoothly when expressed in a chart. It does not, in general, assign a single arrow inside one fixed ambient vector space. The arrow at one point belongs to its tangent space, and the arrow at another belongs to a different tangent space.

## From an arrow to a motion

In the plane, let the velocity field send the point with coordinates x and y to the arrow pointing x units in the horizontal direction and y units in the vertical direction. A moving point obeys the equations: the time derivative of x equals x, and the time derivative of y equals y. Starting at coordinates a and b, its path is given by a times the exponential of time and b times the same exponential. Each point moves radially outward for positive time.

The collection of motions is called a flow. Write the operation as: take a point, evolve for time t, and return its new point. Evolving for time zero does nothing. If the solution exists for both time intervals, evolving for time s and then time t is the same as evolving for time s plus t. This is the flow property.

Why the qualification about existence? Consider the one-dimensional field whose velocity is x squared. Starting at a positive x, its solution grows faster and faster and becomes unbounded at a finite time. The vector field is perfectly smooth on the real line, but its flow is not defined for all future times from every point. A field whose solutions exist for all real times is called complete. Smoothness alone does not imply completeness on a noncompact manifold. On a compact smooth manifold without boundary, every smooth vector field is complete.

## Flows let us differentiate functions geometrically

Take a height function f on the surface. Follow the flow of a vector field X, watching how the height changes. Its instantaneous rate is the directional derivative X applied to f. So a vector field can be treated as an operator taking smooth functions to smooth functions. This operator obeys the product rule: X applied to f times g equals X applied to f, times g, plus f times X applied to g.

The product rule is more than convenient notation. It explains why a tangent vector can be defined without reference to an embedding: a tangent vector at a point is a first-order derivation of smooth functions at that point. A vector field is a compatible family of such derivations.

## Two motions may interfere

Imagine moving east and then north. In a flat coordinate grid with constant velocities, this reaches the same endpoint as moving north and then east. But what if the amount of movement in one direction depends on where the other movement has taken you? The two orders may differ.

Take X to be motion to the right at speed one. Take Y to be motion upward at a speed equal to the current x coordinate. Begin at the origin. If you move right a small distance, then move according to Y for a short time, the upward motion sees a positive x and moves you upward. If you use Y first, at the origin it has zero speed, so you gain no height before moving right. The difference between the two routes is of second order in the small time intervals.

This discrepancy is measured by the Lie bracket of X and Y. It is again a vector field, formed by applying X to the coefficients of Y and subtracting the effect of applying Y to the coefficients of X. In our example the bracket is simply the constant unit upward field. The bracket is not an invented extra direction: it records a direction of motion obtainable to leading order by a tiny loop of alternating available motions.

The exact sign depends on the order chosen for the four little moves. With the conventional bracket, X bracket Y means X acts on the operator Y minus Y acts on X. Reversing the bracket reverses its sign. The important invariant point is that this discrepancy can be computed in any coordinate chart and gives the same geometric vector field.

## Why ordinary subtraction of arrows is not enough

At one point in the plane we can subtract two vectors, but a Lie bracket is not the difference X minus Y. It measures how each field changes in the direction of the other. Constant coordinate fields commute, so their bracket is zero even though the arrows differ. A varying pair may have a nonzero bracket even when the two arrows are linearly independent everywhere.

For a general smooth function f, the bracket acts by first applying Y then X and subtracting first applying X then Y. This operator definition immediately explains two properties: the bracket is antisymmetric, and it obeys the Jacobi identity. These are the laws of a Lie algebra. The collection of all smooth vector fields on a manifold is an infinite-dimensional Lie algebra under this operation.

## Coordinates and change of chart

In local coordinates, a field has components attached to the coordinate directions. If we change coordinates, the components change by the Jacobian, just as tangent vector components do. We must also change the derivatives that act on those components. The resulting bracket formula is compatible with this change; we have not privileged the original x and y axes.

There is another intrinsic description. A flow moves points around the manifold, and the derivative of the flow pushes tangent vectors forward. To compare a field before and after flowing, we transport it back using that derivative. The rate of change of this transported field is the Lie derivative; applied to a second vector field it produces the Lie bracket, with a sign convention fixed by which transport direction we use.

## A bridge to geometry and control

Lie brackets are useful whenever two allowed movements combine into something that neither movement can achieve instantly. A vehicle may move forward and turn but cannot instantly slide sideways. By steering through a sequence of short motions it can change its sideways position. The mathematics of such effects belongs to nonholonomic control and distributions of tangent directions. One must be careful: the ability to generate bracket directions is part of a theorem with hypotheses, not a promise that any arbitrary control problem is solvable.

Vector fields also generate symmetries. Rotating a sphere continuously around its axis is a flow. Differentiating a function along that rotation tells us how it changes under the symmetry. A zero derivative means the function is constant along the rotation orbits. This is the beginning of a geometric way to study conservation laws and invariants.

The conceptual chain is now complete. A vector field assigns a velocity. Differential equations turn velocities into local motions. A field acts on functions by differentiation. Comparing the orders of two motions yields the Lie bracket. These constructions belong to the manifold itself, not to the coordinates drawn on it.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For \(X=\sum_i X^i\partial_i\) and \(Y=\sum_iY^i\partial_i\) in a smooth chart,
\[
[X,Y]=\sum_j\left(\sum_i X^i\partial_iY^j-Y^i\partial_iX^j\right)\partial_j,
\quad [X,Y](f)=X(Yf)-Y(Xf).
\]
For \(X=\partial_x\) and \(Y=x\partial_y\), \([X,Y]=\partial_y\).
A local flow \(\Phi_t\) solves \(\frac{d}{dt}\Phi_t(p)=X_{\Phi_t(p)}\), \(\Phi_0(p)=p\). When defined, \(\Phi_t\circ\Phi_s=\Phi_{t+s}\). The solution for \(x'=x^2\) with \(x(0)=a>0\) is \(x(t)=a/(1-at)\), which blows up at \(1/a\).

### Check your understanding

1. Compute \([\partial_x,x^2\partial_y]\). **Answer:** \(2x\partial_y\).
2. Does a zero bracket imply the fields themselves coincide? **No:** \(\partial_x\) and \(\partial_y\) are different, commuting fields.
3. Is every smooth vector field on \(\mathbb R\) complete? **No:** \(x^2\partial_x\) is not.

### Reading and sources

- MIT OCW, [Geometry of Manifolds](https://ocw.mit.edu/courses/18-965-geometry-of-manifolds-fall-2004/pages/lecture-notes/), lecture on the Lie derivative and prerequisites on tangent bundles.
- Overview: [Vector field](https://en.wikipedia.org/wiki/Vector_field), [Flow (mathematics)](https://en.wikipedia.org/wiki/Flow_(mathematics)), [Lie bracket of vector fields](https://en.wikipedia.org/wiki/Lie_bracket_of_vector_fields).
