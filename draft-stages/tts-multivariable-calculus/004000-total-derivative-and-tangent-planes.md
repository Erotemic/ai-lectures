# 004000 — The Total Derivative: One Linear Map for Every Small Change

**Track:** Multivariable Calculus from First Principles. **Background:** partial derivatives and linear maps. **Question:** what makes a tangent plane a genuine approximation rather than a sketch?

<!-- BEGIN SPOKEN LECTURE -->

# The Total Derivative: One Linear Map for Every Small Change

In one-variable calculus, saying a function is differentiable at a point means that a line predicts its change with an error negligible compared with the distance moved. We want exactly the same idea for multiple inputs. The difference is that the best first-order predictor is no longer just multiplication by one slope. It is a linear map applied to a displacement vector.

Suppose f takes two real inputs and returns one number. At a point a, write h for a small displacement. We seek a linear rule L of h such that f at a plus h equals f at a plus L of h, with an error that becomes small compared with the length of h. That last comparison is the definition. It quantifies the word tangent. We are not satisfied with a plane that happens to match a few chosen directions; the approximation must work uniformly as h approaches zero from anywhere.

## Build the approximation in a concrete example

Let f of x and y be x squared times y plus the sine of x y. Start at the point one comma zero. The function value is zero. The x partial derivative is two x y plus y times cosine of x y. At one comma zero this equals zero. The y partial derivative is x squared plus x times cosine of x y, which equals two there.

The proposed first-order prediction is therefore that changing x by h and y by k changes f by approximately two k. The x displacement contributes nothing at first order at this particular base point. That does not mean x is irrelevant in general. It means its influence is small compared with the total displacement at this point when y is close to zero.

Write the exact value at one plus h comma k. It is the square of one plus h times k, plus sine of one plus h times k. The coefficient of k in the linear part is two. All remaining terms contain at least a product of two small quantities or a higher-order sine error. After dividing their sum by the distance of the displacement from zero, the result tends to zero. This verifies the linear approximation rather than merely guessing it from partial derivatives.

In the graph of z equals f of x comma y, the equation z equals two times y near one comma zero is the tangent plane, adjusted to pass through the original graph point. The plane is the graph of the linearized change plus the original height.

## The Jacobian is a matrix representation, not a different object

Now let F send an input vector with n coordinates to an output vector with m coordinates. Its derivative, when it exists, is a linear map from input displacements to output displacements. In chosen standard coordinates we represent that map by an m-by-n matrix. Entry number i comma j is the partial derivative of output component i with respect to input coordinate j. This is the Jacobian matrix.

For example, let F of x comma y be the pair whose first component is x y and whose second component is x plus y squared. At one comma two, the first row of the Jacobian is two comma one. The second row is one comma four. For a small displacement h comma k, the predicted output change is two h plus k in the first component and h plus four k in the second. There is no need to invent a separate approximation for each displacement: one matrix handles all of them.

The derivative depends on the base point. The matrix changes as we move through the domain. The displacement vector is the input to the linear map, not the location of the base point itself. Mixing these roles causes many errors in geometry and differential equations.

## Why the error is measured relative to distance

Any continuous function has the property that its output error tends to zero. Differentiability demands something more exacting. The error after subtracting the linear part must shrink faster than the displacement itself. If the displacement length is one thousandth, an error of one thousandth is not necessarily good enough; the ratio of error to displacement must tend to zero as we keep shrinking.

This distinguishes first-order approximation from mere continuity. It also explains why derivatives are so useful for sensitivity analysis. When the input perturbation is small, the linear term captures the leading change, and the remaining error has lower relative importance.

## Uniqueness and connection to covectors

Could two different linear maps both satisfy the definition? No. Their difference would have to be negligible compared with every sufficiently small displacement. Fix a direction and scale it down. Because linear maps scale exactly with the displacement, their difference in that direction could not vanish faster than the displacement unless it were zero. Repeating for every direction shows the maps are equal.

For a real-valued function, the total derivative is a linear functional on displacement vectors: a covector. In Euclidean coordinates we represent it by the row of partial derivatives, or equivalently by its associated gradient vector using the dot product. Later, on a manifold, the covector remains meaningful even when there is no preferred notion of gradient until we choose a metric.

The central payoff is a change of perspective. A derivative is not fundamentally a table of partial derivatives. It is one best linear approximation, with an error condition that tests all directions simultaneously. The table of partial derivatives is how we write that map in coordinates.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For \(f:U\subset\mathbb R^n\to\mathbb R^m\), differentiability at interior point \(a\in U\) means there exists a linear map \(A:\mathbb R^n\to\mathbb R^m\) satisfying
\[
\lim_{h\to0}\frac{\|f(a+h)-f(a)-Ah\|}{\|h\|}=0.
\]
Then \(A=Df(a)\) and its standard-coordinate matrix is \(J_f(a)=(\partial_jf_i(a))\). For scalar \(f\), the tangent hyperplane to the graph at \((a,f(a))\) is \(z=f(a)+Df(a)(x-a)\).

For \(f(x,y)=x^2y+\sin(xy)\),
\[
Df(1,0)=(0,2),\qquad f(1+h,k)=2k+3hk+h^2k+O(|(1+h)k|^3).
\]
The term \(hk\) is \(O(\|(h,k)\|^2)\), and \(k^3\) is smaller still, so the remainder divided by \(\|(h,k)\|\) tends to zero. (The big-O sine statement holds near \((h,k)=(0,0)\).)

For \(F(x,y)=(xy,x+y^2)\), \(J_F(1,2)=\begin{pmatrix}2&1\\1&4\end{pmatrix}\).

### Exercises with answers

1. Find the total derivative of \(f(x,y)=3x-2y\). **Answer:** the constant row \((3,-2)\) and zero remainder.
2. Find the tangent plane to \(z=x^2+y^2\) above \((1,2)\). **Answer:** \(z=5+2(x-1)+4(y-2)\).
3. Linearize \(F(x,y)=(xy,x+y^2)\) at \((1,2)\) for displacement \((0.01,-0.02)\). **Answer:** predicted change \((0, -0.07)\).
4. Why is the derivative unique? **Answer:** if \(A,B\) work, apply the difference quotient to \(h=tv\); \(\|(A-B)v\|=0\) for every \(v\).

### Sources and further reading

- MIT OpenCourseWare, [18.022 Calculus of Several Variables](https://ocw.mit.edu/courses/18-022-calculus-of-several-variables-fall-2010/pages/syllabus/), the derivative and its matrix.
- OpenStax, [Calculus Volume 3](https://openstax.org/books/calculus-volume-3/pages/preface), linear approximation and tangent planes.
- [Fréchet derivative](https://en.wikipedia.org/wiki/Fr%C3%A9chet_derivative); [Jacobian matrix and determinant](https://en.wikipedia.org/wiki/Jacobian_matrix_and_determinant).
