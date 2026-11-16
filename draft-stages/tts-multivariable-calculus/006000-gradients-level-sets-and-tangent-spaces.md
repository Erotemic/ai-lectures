# 006000 — Gradients, Level Sets, and Tangent Directions

**Track:** Multivariable Calculus from First Principles. **Background:** linear approximation, directional derivatives, inner products. **Question:** why does a gradient point perpendicular to a contour, and what exactly does that mean?

<!-- BEGIN SPOKEN LECTURE -->

# Gradients, Level Sets, and Tangent Directions

A topographic map gives elevation along contour lines. Every point on one contour has the same height. If a hiker moves along that contour, their elevation does not change to first order. If the hiker turns across the contours, their elevation changes. A single vector at each point encodes these rates: the gradient.

For a differentiable scalar function in ordinary Euclidean coordinates, the gradient is the vector of all first partial derivatives. If the function is the altitude f of x comma y, the gradient has components f sub x and f sub y. Its dot product with a displacement predicts the change in altitude. The gradient is not merely an arrow chosen by inspection; it is the vector that represents the derivative covector using the Euclidean inner product.

## Compute a contour and its normal

Take f of x and y equal to x squared plus four y squared. The level sets are ellipses. At the point one comma one, the value is five. The gradient is two comma eight. For a small displacement h comma k, the first-order change is two h plus eight k.

If we want a direction tangent to the ellipse at this point, choose a vector perpendicular to the gradient, such as four comma minus one. The dot product is eight minus eight, or zero. Thus moving a little in that direction produces no first-order change in f. The curve will still bend, so moving along the straight tangent line a finite distance does not remain exactly on the ellipse. The statement is local and first order.

More generally, suppose a smooth curve r of t lies in the level set f equals c. The composition f of r is the constant c. Differentiate: the gradient of f dotted with the curve's velocity is zero. Every velocity tangent to the level set is orthogonal to the gradient. At a regular point, where the gradient is nonzero, the level set is locally a smooth curve in two dimensions or a smooth hypersurface in higher dimensions, and the gradient is a nonzero normal vector.

At a critical point, where the gradient vanishes, this conclusion needs qualification. The set could cross itself or have a cusp or singular point. The equation f equals zero for f of x and y equal to x squared minus y squared, for example, describes two crossing lines through the origin; the gradient vanishes there and cannot choose a unique normal.

## The direction of steepest increase

What direction produces the fastest increase in the function for a unit step? The directional derivative along a unit vector v equals the gradient dotted with v. By the Cauchy–Schwarz inequality, that dot product is at most the length of the gradient. When the gradient is nonzero, equality occurs if v points in the same direction as the gradient. The opposite direction produces the steepest decrease.

In our ellipse example the gradient two comma eight has length the square root of sixty-eight. A unit step along that normalized vector produces the maximum first-order increase, with rate square root of sixty-eight. A unit step along the normalized tangent produces rate zero.

This statement assumes distance is measured with the ordinary Euclidean inner product. Change the metric, and the meaning of a unit step changes; the representing gradient changes too. The derivative as a covector does not need a metric. This is why Riemannian geometry distinguishes differential of a function from gradient of the function.

## Gradient flow

Suppose a particle moves according to the differential equation position prime equals minus the gradient of f. Along a differentiable solution, the chain rule gives the rate of change of f as minus the squared length of the gradient. Thus f never increases. This is gradient descent as a continuous-time dynamical system.

For f of x and y equal to one half times x squared plus one half times four y squared, the negative gradient flow satisfies x prime equals minus x and y prime equals minus four y. Its solutions are x of t equals initial x times exponential minus t, and y of t equals initial y times exponential minus four t. Both coordinates decay, but the y coordinate decays four times as fast in the exponent. The ellipses tell us the energy levels; the gradient tells us how the flow crosses them.

There is a subtlety: an actual discrete gradient-descent step can overshoot if it is too large. The continuous-time identity does not prove that every finite numerical step decreases the function. Optimization theory studies conditions on step size, curvature and smoothness to control that issue.

## The same idea in three dimensions

Imagine a scalar field T of x, y and z representing temperature. A level surface consists of points with the same temperature. If the gradient is nonzero, it is normal to that surface. A fluid particle with velocity v experiences temperature change at the rate gradient T dot v, in a time-independent field. If the temperature field itself changes with time, an additional time partial derivative appears. Keeping the particle's motion separate from the field's own evolution is essential in fluid mechanics.

The gradient converts local scalar variation into geometry. Its direction comes from an inner product; its orthogonality to level sets comes from the chain rule; and its role in optimization comes from the inequality relating dot products to vector lengths.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For \(f:\mathbb R^n\to\mathbb R\), \(Df(a)h=\nabla f(a)\cdot h\) in Euclidean coordinates. If \(r(t)\) lies in \(\{x:f(x)=c\}\), then
\[
0=\frac{d}{dt}f(r(t))=\nabla f(r(t))\cdot r'(t).
\]
At regular points \(\nabla f\ne0\), the level set is a hypersurface, with tangent space \(\ker Df(a)\). For \(\|v\|_2=1\), \(D_vf(a)\le\|\nabla f(a)\|_2\), equality at \(v=\nabla f/\|\nabla f\|\).

For \(f=x^2+4y^2\) at \((1,1)\), \(\nabla f=(2,8)\) and tangent direction \((4,-1)\). Gradient flow for \(E=(x^2+4y^2)/2\) satisfies \(\dot x=-x,\dot y=-4y\) and \(dE/dt=-\|\nabla E\|^2\).

### Exercises with answers

1. Give a tangent vector to \(x^2+9y^2=10\) at \((1,1)\). **Answer:** \((9,-1)\), since \((2,18)\cdot(9,-1)=0\).
2. Find the maximum directional derivative of \(f=x+2y\). **Answer:** \(\sqrt5\), attained along \((1,2)/\sqrt5\).
3. Why does a vanishing gradient make normal-vector arguments inconclusive? **Answer:** the zero vector has no distinguished direction and the level set need not be regular.
4. Find \(dE/dt\) for \(\dot r=-\nabla E\). **Answer:** \(-\|\nabla E\|^2\le0\).

### Sources and further reading

- MIT OpenCourseWare, [18.02SC Multivariable Calculus](https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/), gradients and directional derivatives.
- OpenStax, [Calculus Volume 3](https://openstax.org/books/calculus-volume-3/pages/preface), gradients and level surfaces.
- [Gradient](https://en.wikipedia.org/wiki/Gradient); [Level set](https://en.wikipedia.org/wiki/Level_set).
