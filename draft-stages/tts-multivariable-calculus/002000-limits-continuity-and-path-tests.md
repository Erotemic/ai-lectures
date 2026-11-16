# 002000 — Multivariable Limits: Why Paths Can Deceive

**Track:** Multivariable Calculus from First Principles. **Background:** neighborhoods, one-variable limits. **Question:** how can we prove a limit when infinitely many paths approach a point?

<!-- BEGIN SPOKEN LECTURE -->

# Multivariable Limits: Why Paths Can Deceive

Suppose a scientist reports that a measurement approaches zero whenever one control is reduced to zero while the other is held fixed at zero. That sounds encouraging. But what happens if both controls change together? In two dimensions there are not merely a left approach and a right approach. There are infinitely many straight lines, parabolas, oscillating paths, and mixtures of coordinates. A genuine limit must give the same answer along every approach permitted by the domain.

For a function of two variables, the statement that f approaches L at the origin means this: whatever accuracy we demand for the output, we can find a radius around the origin such that every point of the domain inside that radius, except perhaps the origin itself, has a function value within the demanded accuracy of L. This definition uses all nearby points simultaneously. It does not mention a selected path.

## Use paths to disprove a limit

Consider the fraction with numerator x times y and denominator x squared plus y squared, defined away from the origin. Along the x axis, y is zero, so the fraction is zero. Along the diagonal where y equals x, the numerator is x squared and the denominator is twice x squared, so the fraction equals one half. These two paths reach the same point but produce different limiting values. The two-variable limit does not exist.

A path calculation is a powerful tool for disproof because one counterexample is enough. But path calculations are asymmetric as a method. Agreement along two paths, or ten, does not prove a limit exists. Even agreement along every straight line can fail to reveal what happens along a curved path.

Here is a deliberate trap. Away from the origin, let f be x squared times y divided by x to the fourth plus y squared, and set f at the origin equal to zero. Follow the straight line y equals m times x. For nonzero m, after cancellation the function tends to zero. Along the horizontal axis it is also zero, and along the vertical axis it is zero. Every line through the origin therefore gives the value zero in the limit. But on the parabola y equals x squared, the fraction becomes x to the fourth divided by twice x to the fourth: exactly one half for every nonzero x. The function is not continuous at the origin. Straight-line tests were insufficient.

That example is important whenever a derivative is checked only along coordinate directions. The behavior may be stable in each of those directions while the combined geometry is still badly behaved.

## To prove a limit, find one bound for all directions

Now examine x squared times y divided by x squared plus y squared, again defining the value at the origin to be zero. We could try many lines, but a direct estimate is stronger. The absolute value of x squared divided by x squared plus y squared is no greater than one. Therefore the absolute value of the entire fraction is no greater than the absolute value of y, which is no greater than the distance to the origin. So the function value approaches zero along every path at once.

This is the central technique of multivariable limits: replace a complicated expression with a simpler quantity that depends only on distance to the target. If the bound tends to zero with the radius, we are finished.

Polar coordinates often make the same idea visible. Write x as radius times cosine and y as radius times sine. The angle tells us the direction, and the radius tells us how close we are. For the well-behaved fraction, a factor of radius remains and the angular factor stays bounded. The radial factor forces the limit to zero. For the bad fraction with numerator x y, no radial factor remains: the answer still depends on the direction. Polar coordinates are an aid to uniform estimates, not a substitute for them.

## Continuity and composition

A function is continuous at a point when its limit there equals its defined value. Polynomials in several coordinates are continuous everywhere. Rational expressions are continuous wherever their denominators are nonzero. The usual algebra of continuous functions still works because addition, multiplication, and division where permitted respect limits.

For a more geometric statement, let a moving point follow a continuous curve, and feed that point into a continuous temperature field. The resulting temperature as a function of time is continuous. This is composition: a continuous path through a continuous field cannot produce a jump. Conversely, if a field has a genuine two-variable limit at a point, every path approaching that point through other points of the domain inherits the same limit. If a path repeatedly visits the target itself, continuity of the field at the target is needed for that conclusion.

This last implication is a one-way test. We have already seen why testing a limited family of paths cannot establish the field's continuity. The full definition remains the referee.

## Why the distinction matters later

The definition of differentiability will demand something even stronger than continuity. It will require that the error after subtracting a proposed linear approximation becomes small compared with the total distance moved. A calculation along one coordinate axis may suggest the linear approximation, but only a bound on all small displacements can prove it is correct.

The lesson is operational. When your goal is to refute a limit, find two paths with incompatible behavior. When your goal is to prove a limit, construct a uniform estimate that does not rely on choosing a path. That difference is the first genuinely new habit of thought in calculus of several variables.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Define, away from \((0,0)\),
\[
f_1(x,y)=\frac{xy}{x^2+y^2},\qquad
f_2(x,y)=\frac{x^2y}{x^4+y^2},\qquad
f_3(x,y)=\frac{x^2y}{x^2+y^2}.
\]
For \(f_1\), \(f_1(x,0)=0\) but \(f_1(x,x)=1/2\). For \(f_2\), on \(y=mx\) with \(m\ne0\),
\[
f_2(x,mx)=\frac{mx}{x^2+m^2}\to0;
\quad f_2(x,0)=0,\quad f_2(0,y)=0,
\]
while \(f_2(x,x^2)=1/2\) when \(x\ne0\). For \(f_3\),
\[
|f_3(x,y)|\le |y|\le\sqrt{x^2+y^2}\to0.
\]
A statement about *all* paths can characterize a limit in metric spaces when paths/sequences are sufficiently general, but checking all straight lines is not enough; the safe direct method is the epsilon–delta estimate or the equivalent arbitrary-sequence criterion.

### Exercises with answers

1. Does \(x^2/(x^2+y^2)\) have a limit at the origin? **Answer:** no; the x axis gives one and y axis zero.
2. Show \(xy^2/(x^2+y^2)\to0\). **Answer:** its absolute value is at most \(|x|\) because \(y^2/(x^2+y^2)\le1\).
3. Why is continuity of \(f\) at \(a\) enough to ensure \(f(\gamma(t))\to f(a)\) when \(\gamma(t)\to a\)? **Answer:** apply the epsilon–delta definition to \(\gamma(t)\).
4. What does failure along two curves establish? **Answer:** the multivariable limit cannot exist when their limiting values differ.

### Sources and further reading

- OpenStax, [Calculus Volume 3](https://openstax.org/books/calculus-volume-3/pages/preface), functions and limits.
- MIT OpenCourseWare, [18.022 Calculus of Several Variables](https://ocw.mit.edu/courses/18-022-calculus-of-several-variables-fall-2010/pages/syllabus/), limits in several dimensions.
- [Limit of a function](https://en.wikipedia.org/wiki/Limit_of_a_function); [Continuous function](https://en.wikipedia.org/wiki/Continuous_function).
