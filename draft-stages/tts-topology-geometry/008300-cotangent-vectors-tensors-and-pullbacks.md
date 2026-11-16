# 008300 - Cotangent Vectors, Tensors, and Pullbacks

**Track:** Topology and Geometry. **Background:** smooth maps, chain rule, tangent vectors. **Question:** how do measurements of vectors transform under coordinate changes and smooth maps?

<!-- BEGIN SPOKEN LECTURE -->

# Cotangent Vectors, Tensors, and Pullbacks

The speed of a particle can be described by a tangent vector. But what sort of object measures the rate at which the particle climbs a hill? A height function f has a differential, which takes the particle's tangent velocity and returns the instantaneous rate of change of height. The velocity and the measurement live in different, complementary spaces. Keeping them separate is one of the most useful habits in geometry.

At a point p of a manifold, the tangent space consists of possible velocities. Its dual space, called the cotangent space, consists of linear functions on those velocities. An element of the cotangent space is a covector. Given a vector v and covector alpha at the same point, alpha of v is a real number. This evaluation does not require a metric, an angle, or a coordinate chart.

## Why the components transform differently

Suppose the x coordinate is measured in meters. Introduce a new coordinate u equal to one hundred times x, so u is the numerical count of centimeters. A velocity of two meters per second has x component two, but u component two hundred. Meanwhile the covector d x, which measures the rate of change of x, becomes one one-hundredth of d u. Pair the components and their scaling cancels. The geometric rate is unchanged.

The simple scaling example exhibits a general pattern. Vectors transform by the derivative of the new coordinates with respect to the old. Covectors transform in the opposite direction, by the inverse relation that preserves evaluation. We sometimes call the first behavior contravariant components and the second covariant components, although there are different textbook indexing conventions for how to describe these. The point is to watch the pairing rather than memorize the adjectives.

## A map pushes velocities and pulls measurements

Let F be a smooth map from one manifold M to another N. Its differential sends a tangent vector at p in M to a tangent vector at F of p in N. We call this the pushforward of the vector at that point. It describes how a trajectory's velocity changes after we apply F.

A covector on N travels the other way. To apply it to a vector at p, first push that vector through F, then evaluate the covector at F of p. This produces a covector on M. We call the operation pullback. It is defined even when F is not invertible. There is generally no analogous canonical pushforward of arbitrary covector fields through a many-to-one map.

Take F from the plane to itself with u equals x squared and v equals y. The covector d u on the target pulls back to two x times d x on the source. At a point where x equals three, a small horizontal source velocity is magnified by six in the u coordinate. The pullback of d u reports precisely this factor. At x equal to zero, the derivative in that direction vanishes. Pullback still makes perfect sense there, even though F lacks a smooth local inverse.

There is an elegant chain-rule identity behind this. If g is a smooth scalar function on the target, pulling back its differential is the same as differentiating g composed with F. In words: measure the change of g after mapping forward, or first pull its measurement backward. The answer is identical.

## Tensor fields add more inputs

A covector takes one tangent vector and returns a number. What if a geometric measurement needs two velocities? A bilinear form takes two vectors. The metric of Euclidean geometry is a symmetric bilinear form: it takes two vectors and returns their dot product. Feed it a vector twice and you obtain squared length.

On a curved surface, a Riemannian metric is a smoothly varying positive-definite symmetric bilinear form on the tangent spaces. It lets us measure lengths and angles without requiring an ambient plane or space. In local coordinates it is described by a matrix of functions, and under change of chart that matrix transforms using a Jacobian on both inputs. It is not legitimate to keep the same component matrix after a nonlinear coordinate change.

A two-form also takes two vectors, but is antisymmetric rather than symmetric. The basic plane area form d x wedge d y returns the signed area spanned by two vectors. Swapping the inputs reverses the sign. This distinction is fundamental: metrics encode lengths and angles, while alternating forms encode oriented area, volume, and integrands for Stokes' theorem.

More generally, a tensor at a point is a multilinear object with specified vector and covector inputs. A field of such tensors varies smoothly across the manifold. Once we know how each input transforms, the whole object transforms by composing those rules. This is the point of tensor notation: the object is invariantly defined; a chart supplies one way to describe its components.

## The covector called the differential

For every smooth scalar function f, the differential d f is a covector field. At a point it acts on a velocity v by taking the directional derivative of f. Many people first meet this idea as a gradient. But the gradient is actually a vector and depends on a metric. The differential does not.

In standard Euclidean coordinates we use the dot product to turn the differential into the gradient vector. On a surface with another metric, the gradient can point in a different coordinate direction from what a naive list of partial derivatives suggests. If we work in polar coordinates, for example, the angular component of the gradient contains a factor of one over radius squared relative to the coefficient of d theta. That factor comes from the metric, not from the definition of the differential.

This separation matters whenever coordinates are stretched. You should not identify a column of partial derivatives with a geometric vector without specifying the rule used to raise the index. The metric supplies that rule.

## Pulling back an area form

Consider the map from coordinates r and theta to the plane: x equals r cosine theta, y equals r sine theta. The pullback of d x wedge d y is r times d r wedge d theta, for positive r. That familiar factor of r in polar integration is not an arbitrary correction inserted by calculus textbooks. It comes from how the area form transforms under the map.

If we reverse orientation, the pullback may acquire a negative sign. If we only want unsigned area, we take the absolute value of the Jacobian determinant in the usual change-of-variables formula. Differential forms instead remember orientation, so the signed Jacobian appears naturally. This explains both the agreement and the difference between oriented form integration and the conventional positive-volume integral.

The picture now fits together. Tangent vectors describe motions, covectors test those motions, tensors combine tests and motions into more elaborate measurements, and pullback transfers measurements along smooth maps. These rules were designed to survive changes of coordinates. They give us the language needed to describe differential forms, metrics, and connections without confusing an object with its component table.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For \(F:M\to N\), \(dF_p:T_pM\to T_{F(p)}N\). If \(\alpha\in T^*_{F(p)}N\),
\[(F^*\alpha)_p(v)=\alpha_{F(p)}(dF_pv),\qquad F^*(dg)=d(g\circ F).\]
For a covariant \((0,2)\)-tensor \(g\), \((F^*g)_p(u,v)=g_{F(p)}(dF_pu,dF_pv)\). If local coordinates satisfy \(y=y(x)\), metric components obey \(g_{ij}^{(x)}=\frac{\partial y^a}{\partial x^i}\frac{\partial y^b}{\partial x^j}g_{ab}^{(y)}\).

**Polar coordinates.** \(F(r,\theta)=(r\cos\theta,r\sin\theta)\). Then
\[F^*(dx\wedge dy)=r\,dr\wedge d\theta,\quad F^*(dx^2+dy^2)=dr^2+r^2d\theta^2.\]
The Riemannian gradient is specified by \(g(\operatorname{grad}f,v)=df(v)\), so \(\operatorname{grad} f=\partial_r f\,\partial_r+r^{-2}\partial_\theta f\,\partial_\theta\) for \(r>0\).

### Check your understanding

1. Under \(u=100x\), how is \(dx\) expressed? **Answer:** \(dx=du/100\).
2. Why can one pull back a one-form through a non-invertible map? **Answer:** pullback only requires the forward differential on tangent vectors.
3. Is the gradient of \(f\) defined without a metric? **No:** \(df\) is intrinsic; turning it into a vector requires a metric or equivalent pairing.

### Reading and sources

- MIT OCW, [Geometry of Manifolds](https://ocw.mit.edu/courses/18-965-geometry-of-manifolds-fall-2004/pages/lecture-notes/), derivatives, vector bundles and exterior algebra.
- Overview: [Cotangent space](https://en.wikipedia.org/wiki/Cotangent_space), [Pullback (differential geometry)](https://en.wikipedia.org/wiki/Pullback_(differential_geometry)), [Tensor field](https://en.wikipedia.org/wiki/Tensor_field).
