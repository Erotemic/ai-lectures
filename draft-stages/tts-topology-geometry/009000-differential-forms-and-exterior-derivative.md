# 009000 — Differential Forms: Calculus That Survives a Change of Coordinates

**Track:** Topology and Geometry. **Background:** multivariable calculus, tangent spaces, and smooth manifolds. **Central question:** how do we describe integrands and differentiation without committing to a particular coordinate system?

<!-- BEGIN SPOKEN LECTURE -->

# Differential Forms: Calculus That Survives a Change of Coordinates

A curve on a sphere can be described using latitude and longitude, or by coordinates measured on a map projected onto a plane. Neither coordinate system is the sphere. It is only a way to describe a portion of the sphere. If calculus on the sphere is to be meaningful, the answer must not depend on which map we picked.

We already know one coordinate-independent object: a tangent vector. It represents a possible velocity through a point. Coordinates give that vector components, but the velocity itself is not a list of components attached forever to one chart. Differential forms provide a complementary language: they take tangent vectors as inputs, produce numbers, and behave correctly when we change charts.

## From differentials to covectors

At a point of a smooth manifold, a one-form is a linear functional on the tangent space. Feed it a tangent vector and it returns a scalar. For a smooth real-valued function f, its differential at a point is such a one-form: it sends a vector v to the directional derivative of f along v.

In ordinary plane coordinates, write f as a function of x and y. Its differential has an x-component involving the partial derivative of f with respect to x, and a y-component involving the partial derivative with respect to y. If the tangent vector moves with velocity v in the x direction and w in the y direction, the differential returns the partial x derivative times v plus the partial y derivative times w. This is the chain rule expressed as a pairing.

The symbols d x and d y are not tiny increments that we multiply like arbitrary numbers. They are basis covectors that extract the x and y components of a tangent vector. They change when coordinates change, in a way that preserves the value of the pairing.

A differential one-form on the plane can be written P d x plus Q d y, where P and Q are functions of position. Integrating it along a parametrized curve means evaluating the form on the curve's velocity and integrating the resulting scalar over the parameter. This produces an oriented line integral. Reverse the curve's direction and the integral changes sign.

## Why alternating forms appear

A two-form takes two tangent vectors and is linear in each input, but it also changes sign when the two inputs are exchanged. In particular, giving it the same vector twice produces zero. Such objects are called alternating bilinear forms.

On the plane, d x wedge d y is the basic two-form. Feed it two vectors and it returns the signed area of the parallelogram spanned by those vectors. If we reverse the order of the inputs, the signed area reverses. If the vectors are parallel, the area is zero.

The wedge product creates higher-degree forms from lower-degree ones. For one-forms alpha and beta, alpha wedge beta is a two-form measuring their alternating interaction. Swapping two one-forms changes the sign. More generally, swapping forms of degrees p and q introduces a sign determined by the product p times q. This is graded commutativity.

Why does this help integration? A one-form naturally integrates along oriented curves. A two-form naturally integrates over oriented surfaces. On an n-dimensional manifold, an n-form naturally integrates over oriented n-dimensional regions. A coordinate change adjusts the components and the oriented volume element together; the integral remains geometrically meaningful.

## The exterior derivative

We know how to differentiate a function and obtain a one-form. Can we differentiate one-forms and higher forms in a coherent way? The exterior derivative does exactly that. It raises degree by one: functions become one-forms, one-forms become two-forms, and so on.

For a one-form P d x plus Q d y on the plane, the exterior derivative is the difference between the x derivative of Q and the y derivative of P, multiplied by d x wedge d y. The expression looks like the scalar curl from vector calculus. This is no accident: the traditional gradient, curl, and divergence operators are different coordinate shadows of the exterior derivative when combined with other geometric identifications.

Take the one-form negative y d x plus x d y. The x derivative of the coefficient of d y is one, and the y derivative of the coefficient of d x is negative one. Their difference is two. Thus its exterior derivative is two times the area form d x wedge d y.

There is an algebraic rule behind this calculation. Differentiation obeys a graded product law: the derivative of alpha wedge beta is the derivative of alpha wedge beta plus a sign, depending on the degree of alpha, times alpha wedge the derivative of beta. The sign ensures consistency with alternating order.

A central identity is that applying the exterior derivative twice gives zero. For a function f, this follows from equality of mixed second partial derivatives when f is sufficiently smooth. For a general differential form, the cancellation of corresponding mixed partial derivatives gives the same result, and the graded product law extends it to all forms.

This identity says that every exact form, meaning one obtained as the exterior derivative of another form, is closed, meaning its exterior derivative is zero. The converse is not always true. That distinction is where topology enters the calculus.

## An obstruction on the punctured plane

Remove the origin from the plane. Consider the one-form whose coefficients are negative y over x squared plus y squared and x over that same denominator. It is smooth everywhere on the punctured plane. A calculation gives exterior derivative zero, so the form is closed.

But integrate the form once counterclockwise around the unit circle. Parametrize the circle by cosine and sine. The form evaluates to one on the unit-speed angular parametrization, and its integral is two pi. If the form were the differential of a globally defined smooth function, the fundamental theorem for line integrals would force its integral around every closed loop to be zero. Contradiction.

Therefore the form is closed but not exact on the punctured plane. There is no globally defined angle function whose differential equals this form everywhere. Locally we can choose an angle coordinate, but going once around the missing point changes the angle by a full turn.

This is an example of the first de Rham cohomology detecting a topological hole. We have not proved the general equivalence between de Rham cohomology and singular cohomology, but this example already exhibits the organizing idea: differentiate forms, observe that differentiating twice gives zero, and examine which closed forms fail to be derivatives of others.

## Why coordinates no longer dominate

Differential forms have an important compatibility with maps of manifolds. A smooth map can pull a form backward to its source. In coordinates this is substitution followed by the chain rule; geometrically it means feeding a form the pushed-forward tangent vectors. Pullback commutes with the exterior derivative. We can change the coordinates or pull the same form onto a parametrized surface without inventing a separate differentiation law every time.

Forms therefore unify line integrals, surface integrals, and parts of vector calculus. But their deeper value is that the formulas survive any valid smooth change of chart. They also expose the topological distinction between local antiderivatives and globally defined ones.

The same exterior derivative that turns a potential into a gradient-like object will connect boundary integration with interior integration. That is the general form of Stokes' theorem. The machinery may look abstract, but it is designed to keep a simple requirement honest: the calculus should describe geometry, not the coordinate grid used to draw it.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Let \(M\) be a smooth manifold. A differential \(p\)-form is a smooth section of \(\Lambda^pT^*M\). In local coordinates \(x^1,\ldots,x^n\), a one-form is \(\alpha=\sum_i a_i\,dx^i\), and a \(p\)-form is a sum of \(a_{i_1\cdots i_p}\,dx^{i_1}\wedge\cdots\wedge dx^{i_p}\) over increasing multi-indices.

For tangent vectors \(u=(u_1,u_2)\), \(v=(v_1,v_2)\),
\[
(dx\wedge dy)(u,v)=u_1v_2-u_2v_1.
\]
Exterior differentiation is characterized by
\[
\begin{gathered}
df=\sum_i\frac{\partial f}{\partial x^i}\,dx^i,\qquad
 d(\alpha\wedge\beta)=d\alpha\wedge\beta+(-1)^p\alpha\wedge d\beta\quad (\deg\alpha=p),\\
d^2=0,\qquad F^*(d\omega)=d(F^*\omega).
\end{gathered}
\]
For \(\alpha=P\,dx+Q\,dy\), \(d\alpha=(\partial_xQ-\partial_yP)\,dx\wedge dy\). Taking \(\alpha=-y\,dx+x\,dy\) yields \(d\alpha=2\,dx\wedge dy\).

**Closed not exact.** On \(U=\mathbb R^2\setminus\{0\}\),
\[
\eta=\frac{-y\,dx+x\,dy}{x^2+y^2},\qquad d\eta=0,
\qquad \int_{S^1}\eta=2\pi.
\]
Therefore \(\eta\ne df\) for any global smooth \(f:U\to\mathbb R\), because exact one-forms have zero integral around a closed curve.

### Exercises with answers

1. Compute \(d(x^2\,dy)\). **Answer:** \(2x\,dx\wedge dy\).
2. Evaluate \((dx\wedge dy)((1,2),(3,4))\). **Answer:** \(4-6=-2\).
3. Must a closed one-form on any manifold be exact? **No:** the punctured plane example refutes this.
4. Is \(dx\wedge dx\) nonzero? **No:** alternation implies \(dx\wedge dx=0\).

### Reading and source notes

- Denis Auroux, MIT OCW [Geometry of Manifolds, Differential Forms](https://ocw.mit.edu/courses/18-966-geometry-of-manifolds-spring-2007/pages/lecture-notes/), exterior algebra and exterior derivative.
