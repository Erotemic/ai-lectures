# 014000 — Complex Differentiation and the Cauchy–Riemann Equations

**Track:** Analysis from First Principles. **Background:** complex multiplication, real differentiability, partial derivatives, and limits. **Theme:** a complex derivative must agree with increments in every direction, forcing the differential to be multiplication by a single complex number.

<!-- BEGIN SPOKEN LECTURE -->

# Complex Differentiation and the Cauchy–Riemann Equations

Think about the ordinary map that reflects a point across the horizontal axis. It sends the point with coordinates x and y to the point with coordinates x and negative y. This is an excellent real-variable function. It is linear, continuous, and infinitely differentiable as a map from the plane to itself. Its derivative matrix is constant. Yet, viewed as a function of one complex variable, it fails to have a complex derivative at every point.

Why would a derivative, of all things, reject a perfectly smooth linear reflection? The answer is not that reflection behaves erratically. It is that the complex derivative is a more restrictive kind of local linear approximation. It insists that the same complex multiplier describe the change in the function, regardless of the direction from which the input approaches.

That insistence will be responsible for the Cauchy–Riemann equations. It will also prepare us for the much stronger theorems about holomorphic functions: their contour integrals, their power series, and the constraints on their values inside a region. To see why, let us first compare two different meanings of a derivative on the same plane.

## Two real inputs and one complex input

Write a complex number as x plus i y. A complex-valued function can be described by two real-valued component functions. Its output has a real part u, depending on x and y, and an imaginary part v, also depending on x and y.

From multivariable real calculus, we may know what it means for this map to be differentiable at a point. A small change in the input, represented by a two-dimensional vector, produces a change in the output approximated by a real linear transformation. Such a transformation can stretch horizontally by one factor, vertically by another, shear the plane, rotate it, or reflect it. Four real matrix entries describe its first-order action.

Complex differentiation is narrower. At a point a, we take the difference between the function value at a nearby point and the function value at a, divide by the complex increment, and ask whether the quotient has a single limit as the increment tends to zero through all nonzero complex directions. If the limit exists, it is the complex derivative at a.

Equivalently, the change in the output must equal one fixed complex number multiplied by the input change, plus an error that is small compared with the magnitude of that change. The fixed multiplier may rotate and uniformly scale, because those are the geometric actions of complex multiplication. But it cannot perform an independent horizontal stretch, a shear, or a reflection.

That is the crucial difference. A general real derivative is a matrix. A complex derivative is the much more special real matrix that represents multiplication by one complex number.

The word special should not suggest a minor technicality. The restriction survives at every point of an open domain, and so it couples the two component functions. A map that meets the condition at every point is called holomorphic on that domain. You may also hear analytic function, but we will reserve the proof that holomorphic functions admit local power series until after we have Cauchy's integral formula. At this stage, holomorphic means complex differentiable on an open set.

## The reflection that fails

Return to complex conjugation. It sends z to z bar. For a small increment h, the change in output is h bar, and the complex difference quotient is h bar divided by h. If h is real, its conjugate is itself, and the quotient is one. If h is purely imaginary, its conjugate is its negative, and the quotient is negative one.

Both approaches use increments tending to zero. The quotients disagree. The complex derivative does not exist.

This example is worth more than a memorized counterexample. It shows why two-dimensional smoothness alone cannot justify a complex derivative. Indeed, a smooth real map can fail the complex test in the simplest possible way. The problem is directional inconsistency: the local action along the horizontal axis is not the same complex multiplication as the local action along the vertical axis.

There is also a useful positive example. Let f of z equal z squared. Replace z by z plus h, expand the square, and subtract z squared. The remaining change is two z times h plus h squared. Divide by h, and the quotient is two z plus h. As h approaches zero from any direction, that converges to two z. So the complex derivative exists everywhere, and it equals two z.

Observe the logic of the proof: we did not separately check a horizontal and vertical approach and then declare success. We simplified the quotient for every nonzero complex h, and we obtained an expression with one common limit. That is the kind of argument a complex limit requires.

## Deriving the Cauchy–Riemann equations

Suppose a function is complex differentiable at a point. Write its output as u plus i v, where u and v are real functions of x and y.

First, approach the point using real increments h. Dividing the output change by a real h gives a limit whose real component is the partial derivative of u with respect to x, and whose imaginary component is the partial derivative of v with respect to x. Thus the complex derivative, if it exists, must equal the x partial of u plus i times the x partial of v.

Now approach using purely imaginary increments, i times a real h. The output change is still described by the component functions, but dividing by i times h multiplies by negative i divided by h. The resulting limit has real part the y partial of v and imaginary part minus the y partial of u.

The complex derivative must be independent of our chosen approach. Therefore the real parts of these two expressions agree, and so do the imaginary parts. The x partial of u equals the y partial of v. The y partial of u equals negative the x partial of v.

Those are the Cauchy–Riemann equations.

Pause to interpret them rather than merely remembering their arrangement. The equations force the derivative matrix of the real coordinate map to have the form required by complex multiplication. One diagonal entry equals the other, and one off-diagonal entry is the negative of the other. That matrix cannot reflect the plane unless it collapses all directions to zero.

Check our two examples. For z squared, the real part is x squared minus y squared, and the imaginary part is two x y. The x partial of the real part is two x; the y partial of the imaginary part is also two x. The y partial of the real part is negative two y; the x partial of the imaginary part is two y. The equations hold everywhere.

For conjugation, the real part is x and the imaginary part is negative y. The x partial of the real part is one, but the y partial of the imaginary part is negative one. The first equation fails everywhere, matching the difference-quotient calculation.

## Necessary does not automatically mean sufficient

There is a temptation to stop here. We have two equations involving partial derivatives; if a function satisfies them at a point, should that not prove it is complex differentiable there?

Not without another hypothesis. The equations were derived from the existence of a complex derivative, so they are necessary whenever that derivative exists. They are not, on their own at a single point, enough to control how the function behaves along arbitrary approaches.

The hidden problem is the difference between partial derivatives and a full linear approximation. Partial derivatives measure changes along the coordinate axes. A function can behave well on each axis while behaving badly along a diagonal or a curved approach. Real differentiability provides the missing uniform first-order control across all directions.

Here is a constructive counterexample. For nonzero points, take the real-valued function whose value is x times y divided by the distance from the origin, and define its value at the origin to be zero. On either coordinate axis it is identically zero. All four first partial derivatives of the real and imaginary components at the origin are therefore zero, so the Cauchy–Riemann equations hold there.

But along the diagonal x equals y and is positive, the function is proportional to x, not small compared with the distance to the origin. The complex difference quotient along that diagonal does not approach zero, whereas along the horizontal axis it is zero. There is no complex derivative at the origin.

What additional hypothesis is enough? A standard theorem says that if the component functions possess continuous first partial derivatives in a neighborhood of the point, and the Cauchy–Riemann equations hold at the point, then the function is complex differentiable there. More generally, real differentiability at the point plus the Cauchy–Riemann equations there suffices. We can prove this directly using the first-order real approximation.

Because the component map is real differentiable, its change equals a real matrix applied to the input increment, plus an error small compared with the increment's length. The Cauchy–Riemann equations force that matrix to equal multiplication by a particular complex number. Divide the approximation by the complex increment. The error divided by that increment tends to zero in modulus. The quotient therefore tends to the required complex multiplier.

The continuity of the first partials is a convenient sufficient condition because it implies real differentiability. It is not part of the definition of holomorphic, and it is not an extra condition required by the major theorems to come.

## A derivative at one point is not a holomorphic function

A different pitfall comes from confusing complex differentiability at one point with complex differentiability throughout a neighborhood. Consider the function that returns the squared modulus of z, or in coordinates, x squared plus y squared. This is a real-valued polynomial in two real variables, so it is real smooth everywhere.

At the origin, the complex difference quotient simplifies to the conjugate of h, which tends to zero. Thus this function has complex derivative zero at the origin. At a nonzero point, the Cauchy–Riemann equations fail: its imaginary component is zero, while the real component has nonzero partial derivatives. It is not holomorphic on any open disk.

The conclusion is subtle but essential. Holomorphicity is an open-set property. Having a complex derivative at one isolated point is mathematically meaningful, but it does not automatically produce the local power series, contour-integral theorems, or other rigidity we will ultimately prove for holomorphic functions.

The distinction also prevents a common mistake about functions that satisfy a special identity only at an isolated point. When we prove later that the real and imaginary parts of a holomorphic function are harmonic, we will be using derivatives on an open neighborhood, not merely one derivative at a single point.

## The geometric content: angles and local scale

Suppose a function is holomorphic near a point and its complex derivative at that point is not zero. To first order, the function multiplies every small increment by that derivative. Multiplication rotates all directions by the same angle and multiplies their lengths by the same positive factor. The function therefore preserves angles between sufficiently short curves, including their orientation, to first order.

This is the local conformal behavior of holomorphic maps at noncritical points. It is not the claim that every holomorphic map is globally one-to-one, and it does not apply unchanged at a point where the derivative vanishes.

For example, z squared has derivative two z, which vanishes at the origin. Near a nonzero point it acts to first order like a rotation and scaling. At the origin, however, the dominant behavior is quadratic: angles in its output are doubled. The origin is a critical point. If we want a theorem about local invertibility or preservation of angles, the nonzero derivative condition matters.

The determinant of the real derivative matrix gives another way to see the geometry. For a holomorphic function the determinant equals the squared modulus of the complex derivative. It is nonnegative, and positive wherever the complex derivative is nonzero. Thus a noncritical holomorphic map locally preserves orientation. Conjugation, by contrast, has determinant negative one because it reverses orientation. The algebra and geometry are saying the same thing.

## Building examples instead of memorizing classifications

Try the complex exponential. We already know that its power series converges uniformly on every closed disk. On a smaller disk inside any chosen convergence region, the differentiated series also converges uniformly. We may therefore differentiate term by term and obtain again the exponential series. So the complex exponential is holomorphic everywhere, and its complex derivative is itself.

Written in real coordinates, the exponential of x plus i y has real part the real exponential of x times cosine y, and imaginary part the real exponential of x times sine y. Differentiate those components. The x partial of the real part equals the y partial of the imaginary part. The y partial of the real part is the negative of the x partial of the imaginary part. The equations work, but now we understand why: they are the coordinate expression of complex multiplication by the function's own value.

The reciprocal function, one divided by z, is also holomorphic wherever z is nonzero. Differentiate by a direct difference quotient or by the quotient rule for complex derivatives. Its derivative is negative one divided by z squared. But at zero the function is undefined, and we may not use continuity or differentiability there. That missing point will matter sharply when we integrate around a circle.

Finally, consider a function of z and its conjugate, such as z squared plus z bar. Real differentiation sees a harmless polynomial in x and y. Complex differentiation sees the conjugate term, which introduces directional disagreement. The derivative fails everywhere, not because the function is discontinuous but because its linear action has a reflection component.

These examples suggest a useful diagnostic. When a candidate function is built from complex powers, exponential series, and holomorphic compositions on a suitable domain, complex differentiation rules are often available. When complex conjugation or modulus enters, do not assume holomorphicity. Check the limit, the Cauchy–Riemann equations under suitable regularity, and the domain.

## What we have earned, and what is still ahead

We have reached an important threshold. We defined the complex derivative using one quotient that must converge through every direction. We derived the Cauchy–Riemann equations, understood their geometric meaning, and identified exactly which additional real differentiability hypothesis makes them sufficient at a point. We distinguished holomorphicity on an open set from the existence of a derivative at an isolated point.

But several extraordinary claims remain unproved. We have not shown that a function holomorphic just once is automatically differentiable again. We have not shown that its values are determined by values on a boundary curve. We have not shown that it equals a convergent power series near every interior point.

The next tool is integration along paths in the plane. Initially we will define these integrals using only ordinary real-variable integration along parametrized curves. Then we will see a case in which two paths with the same endpoints produce different answers. That experiment will show why a missing point in a domain can change the outcome of calculus. Afterward, Cauchy's theorem and Cauchy's integral formula will explain why holomorphic functions nevertheless possess such strong structure when the geometry of a region is properly accounted for.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

### Complex derivative and Cauchy–Riemann

For \(f:U\to\mathbb C\), \(U\) open, define
\[
f'(a)=\lim_{h\to0}\frac{f(a+h)-f(a)}{h},\qquad h\in\mathbb C\setminus\{0\}.
\]
If \(f=u+iv\) and \(f'(a)\) exists, the partials exist at \(a\), and
\[
u_x=v_y,\qquad u_y=-v_x,\qquad f'(a)=u_x+iv_x=v_y-iu_y.
\]
For real differentiable \((u,v)\), \(Df(a)\) has matrix
\[
\begin{pmatrix}u_x&u_y\\ v_x&v_y\end{pmatrix}=
\begin{pmatrix}A&-B\\ B&A\end{pmatrix},\quad A=u_x,\ B=v_x.
\]
Thus the differential is complex multiplication by \(A+iB\), proving sufficiency of real differentiability plus Cauchy–Riemann at \(a\). Having continuous partial derivatives in a neighborhood is a sufficient way to ensure real differentiability, not a necessary hypothesis for holomorphicity.

### Counterexamples that isolate hypotheses

- \(f(z)=\bar z\): quotient \(\bar h/h\) equals \(1\) for real \(h\), \(-1\) for imaginary \(h\); never complex differentiable.
- \(f(z)=|z|^2=z\bar z\): complex differentiable at \(0\) with \(f'(0)=0\), but not holomorphic on any open neighborhood.
- \(f(x+iy)=xy/\sqrt{x^2+y^2}\) for \((x,y)\ne(0,0)\), and \(f(0)=0\): all first partials at \(0\) are zero, hence CR holds there, but the complex quotient along \(h=t(1+i)\), \(t>0\), is \(1/(\sqrt2(1+i))\), not zero. This exhibits failure without real differentiability.
- For \(f(z)=z^2\), \(u=x^2-y^2\), \(v=2xy\), \(f'(z)=2z\).

### Orientation and conformity

At \(a\) with \(f'(a)=A+iB\ne0\), \(\det Df(a)=A^2+B^2=|f'(a)|^2>0\). The first-order map preserves oriented angles and multiplies all infinitesimal lengths by \(|f'(a)|\). This does not assert global injectivity or conformality at critical points.

### Exercises with answers

1. **Compute:** Show that \(f(z)=3z^2-2iz\) is entire and calculate \(f'(z)\). **Answer:** Polynomial rules give \(6z-2i\).
2. **Use CR:** Is \(f(z)=x+2iy\) complex differentiable? **Answer:** No: \(u_x=1\), \(v_y=2\).
3. **Point versus domain:** Determine the points where \(|z|^2\) is complex differentiable. **Answer:** Only \(z=0\).
4. **Geometry:** What is the real Jacobian determinant of \(f(z)=z^2\) at \(z=2+i\)? **Answer:** \(|2z|^2=20\).
5. **Hypotheses:** Why is CR at one point insufficient? **Answer:** Coordinate-axis partial derivatives need not provide a full first-order approximation; see the diagonal counterexample above.

### Further reading

- MIT OpenCourseWare, *18.04 Complex Variables with Applications*, Topic 2, https://ocw.mit.edu/courses/18-04-complex-variables-with-applications-spring-2018/pages/lecture-notes/.
- MIT OpenCourseWare, *18.112 Functions of a Complex Variable*, Lecture 3, https://ocw.mit.edu/courses/18-112-functions-of-a-complex-variable-fall-2008/pages/lecture-notes/.
- Wikipedia, *Cauchy–Riemann equations*, https://en.wikipedia.org/wiki/Cauchy%E2%80%93Riemann_equations.
- [Robert B. Ash and W. P. Novinger, Complex Variables, 2nd ed.](https://people.math.sc.edu/girardi/m7034/book/AshComplexVariablesMerged.pdf) — Ash & Novinger, Complex Variables, chapter 1: the real differentiability hypothesis and Cauchy–Riemann equations.
