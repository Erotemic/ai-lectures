# 005000 — The Multivariable Chain Rule: Composing Local Linear Maps

**Track:** Multivariable Calculus from First Principles. **Background:** the total derivative and matrix multiplication. **Question:** how does a change of variables affect a derivative?

<!-- BEGIN SPOKEN LECTURE -->

# The Multivariable Chain Rule: Composing Local Linear Maps

A system can transform inputs through several stages. A robotic arm converts joint angles into a position. A temperature field converts that position into a temperature. To determine how a small change in the joint angles affects the measured temperature, we must combine the sensitivity of the position to the angles with the sensitivity of temperature to position. This is the multivariable chain rule.

Its familiar one-variable cousin says that the derivative of a composition is the product of the two derivatives. In several variables the principle is identical, but the derivatives are linear maps and their product is matrix composition. The order matters.

## Follow a displacement through two maps

Let F take an input with n coordinates to an intermediate output with m coordinates, and let G take that intermediate point to a final output with p coordinates. Near a starting point a, F transforms a small displacement h approximately into the matrix J of F at a, multiplied by h. The second map G transforms that intermediate change approximately into its own Jacobian matrix multiplied by the change. Thus the total first-order effect is the Jacobian of G at F of a, multiplied by the Jacobian of F at a, and then multiplied by h.

Notice where each derivative is evaluated. The derivative of F is evaluated at the original input a. The derivative of G is evaluated at the intermediate point F of a. Putting both derivatives at a would not generally even make sense, because the input and intermediate spaces may have different dimensions.

A useful memory aid is to read the composition from right to left. We do F first and G second. Their derivative matrices multiply in the same functional order: derivative of G times derivative of F.

## A complete example

Let F of x and y return the pair u equals x times y and v equals x plus y. Let G of u and v be u squared plus three times v. Then the complete function is x squared times y squared plus three x plus three y.

Differentiate it directly. The x partial derivative is two x times y squared plus three. The y partial derivative is two x squared times y plus three. Now do it as a composition. The Jacobian of F has first row y comma x and second row one comma one. The derivative of G is the row two u comma three. Multiplying the row by the matrix produces two u times y plus three, and two u times x plus three. Substitute u equals x y and the results match the direct calculation exactly.

This equality is a check on both methods. More importantly, it proves we can compute derivatives modularly. A large computation can be organized as many small stages, exactly as in automatic differentiation.

## Paths through a field

Consider a curve r of time describing a moving point in space, and a scalar field T giving temperature at each position. The composition T of r gives temperature as a function of time. Its rate of change is the gradient of T at the moving position dotted with the velocity r prime. If the velocity lies along a level surface of T, this rate is zero. If it has a component toward warmer regions, the rate can be positive.

Take T of x and y equal to x squared plus y squared, and r of t equal to cosine t comma sine t. The particle travels around the unit circle. Its temperature is identically one, so its time derivative is zero. The gradient is the vector two cosine t comma two sine t. The velocity is minus sine t comma cosine t. Their dot product is zero. The algebra reflects the geometry: movement tangent to a circle of constant radius does not change the radius squared.

This example also reveals that a vector field and a path have different roles. The gradient is a property of the scalar field at each location; velocity is a property of how the particle moves through those locations.

## Why the error stays small

The chain rule is not only a trick for multiplying partial derivatives. It follows from the definition of differentiability. The first map produces a linear change plus an error negligible compared with the original displacement. The second map produces another linear change plus an error negligible compared with the intermediate displacement. Since a differentiable first map changes distances by at most a constant times the original small displacement, the composed error is still negligible compared with that original displacement.

This reasoning is why the theorem requires differentiability, not merely a collection of directional derivatives. Without a genuine linear approximation for each stage, there is no justification for composing linear approximations.

## A word about changing coordinates

Suppose we use new coordinates u and v to describe the same points previously described by x and y. The physical function has not changed, but its coordinate expression has. The Jacobian of the coordinate map tells us how small steps in u and v alter x and y. The chain rule converts derivatives between these descriptions.

Later in geometry, a tangent vector will transform by the Jacobian of the coordinate change, while a covector transforms in the dual manner. The distinction is not a convention to memorize; it comes from insisting that the change in an actual scalar quantity be the same whether calculated in the old coordinates or the new ones.

The chain rule is therefore a statement about the compatibility of local linear models. It lets small calculations be composed into large ones and is a central reason derivatives are useful beyond elementary calculus.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

If \(F:U\subset\mathbb R^n\to V\subset\mathbb R^m\) and \(G:V\to\mathbb R^p\) are differentiable at \(a\) and \(F(a)\), respectively, then
\[
D(G\circ F)(a)=DG(F(a))\circ DF(a),\qquad
J_{G\circ F}(a)=J_G(F(a))J_F(a).
\]
For \(F(x,y)=(xy,x+y)\) and \(G(u,v)=u^2+3v\),
\[
J_F=\begin{pmatrix}y&x\\1&1\end{pmatrix},\quad
J_G=(2u,3),\quad
J_G(F)J_F=(2xy^2+3,2x^2y+3).
\]
For \(r(t)=(\cos t,\sin t)\) and \(T(x,y)=x^2+y^2\),
\[
\frac{d}{dt}T(r(t))=\nabla T(r(t))\cdot r'(t)=0.
\]
The intermediate Jacobian dimensions determine the multiplication order: \((p\times m)(m\times n)=(p\times n)\).

### Exercises with answers

1. For \(F(x,y)=(x+y,x-y)\), \(G(u,v)=u^2+v^2\), compute \(\nabla(G\circ F)\). **Answer:** \((4x,4y)\), since \(G\circ F=2x^2+2y^2\).
2. Differentiate \(T(r(t))\) for \(T(x,y)=xy\), \(r(t)=(t,t^2)\). **Answer:** \(3t^2\).
3. Why do Jacobian matrices multiply rather than add? **Answer:** the second linear map acts on the displacement produced by the first.
4. Can the outer derivative be evaluated at the original input if \(n\ne m\)? **Answer:** not generally; it belongs at the intermediate point \(F(a)\).

### Sources and further reading

- MIT OpenCourseWare, [18.02SC Multivariable Calculus](https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/), chain rule.
- OpenStax, [Calculus Volume 3](https://openstax.org/books/calculus-volume-3/pages/preface), multivariable differentiation.
- [Chain rule](https://en.wikipedia.org/wiki/Chain_rule); [Automatic differentiation](https://en.wikipedia.org/wiki/Automatic_differentiation).
