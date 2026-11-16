# 001000 — Points, Vectors, and Nearness in Several Dimensions

**Track:** Multivariable Calculus from First Principles. **Background:** one-variable calculus and basic vectors. **Question:** what must be meant by “near a point” when there are many ways to approach it?

<!-- BEGIN SPOKEN LECTURE -->

# Points, Vectors, and Nearness in Several Dimensions

Imagine recording the temperature of a room. A reading at one location depends on where you stand: left versus right, front versus back, floor versus ceiling. Time may add another independent coordinate. A function of several variables assigns an output to an entire collection of inputs, not to one number on a line. Before differentiating such functions we must specify what it means for the input to change only a little.

A point in the plane is an ordered pair, such as three comma four. A point in space has three coordinates. Mathematicians speak of R to the n: lists of n real numbers. The same notation can describe positions, measurements, concentrations, or the settings of n controls. A vector is a change in those coordinates. If we start at the point two comma one and add the displacement one comma minus three, we end at three comma minus two. Keeping points and displacements conceptually separate will become valuable when our points live on a curved surface.

## Distances describe neighborhoods

The familiar distance between two points in the plane comes from Pythagoras. Subtract the corresponding coordinates, square the differences, add, and take the square root. In more dimensions we do the same. This is the Euclidean distance. A ball of radius one around the origin contains the points whose squared coordinates add to less than one. In a plane that ball is the interior of a circle. In three dimensions it is the interior of a sphere.

Why use balls rather than just rectangles? A ball tells us that every component of the displacement is controlled at once. When we say that a vector approaches zero, we mean its distance from zero approaches zero. Equivalently, for a finite list of coordinates, every coordinate tends to zero. One direction cannot quietly remain far away while the others shrink.

There are other sensible measurements of size. We could add the absolute values of all coordinates, or take the largest absolute coordinate. These produce diamond-shaped and square-shaped balls in the plane. The shapes differ, but in a fixed finite dimension all three notions declare exactly the same sequences convergent. For instance, the largest coordinate is no greater than the Euclidean length, and the Euclidean length is no greater than the square root of n times the largest coordinate. The inequalities squeeze one notion of smallness between constant multiples of another.

This fact lets us choose a convenient norm for a calculation. But it does not mean every conceivable way of assigning sizes is equivalent in infinite-dimensional function spaces. That distinction will matter in analysis.

## Open sets, domains, and boundaries

A region is open if every point in it has a small ball lying entirely within the region. The interior of a disk is open; the closed disk, including its boundary circle, is not. A function may be defined only on a restricted domain, such as the points where the denominator of a formula is nonzero. If we write the square root of one minus x squared minus y squared, its real domain is the closed unit disk. At an interior point we can move a little in any direction. At a boundary point, not every movement stays in the domain.

This is why theorems about ordinary derivatives normally assume the function is defined on an open neighborhood. At a boundary we may still study one-sided movements or derivatives along the surface, but the statement has changed. The domain is part of the mathematical object, not an afterthought.

## A path is one way to move, not every way

Take a particle whose location at time t is the point with coordinates t and t squared. As t approaches zero, the particle approaches the origin. Its distance from the origin is the square root of t squared plus t to the fourth. That quantity goes to zero. The path approaches along a parabola, not a straight line.

If a temperature function is continuous at the origin, its readings along this path must approach the reading at the origin. The same is true along a diagonal line, a spiral, or any other path that approaches the point while staying in the domain. But checking one convenient path will never establish continuity in every direction. A function can behave well on both coordinate axes while behaving differently between them.

The right mental picture is not that the point moves along a single line toward a target. It is that every sufficiently small displacement, from every direction and with every mixture of coordinates, must lead to a controlled change in the output. A proof of a multivariable limit must control all such displacements together.

## The first quantitative estimate

Consider the function that squares x and adds y squared. Its value at the origin is zero. At any nearby point its value is exactly the square of the distance to the origin. To make the output smaller than one thousandth, it suffices to keep the input closer than the square root of one thousandth. That is an epsilon–delta argument: for each requested output tolerance, we choose an input tolerance that works for all points in the nearby ball.

We have not yet differentiated or integrated anything. But we have established the common language of both operations: points, displacements, neighborhoods, domains, and uniform control in all directions. A derivative will soon be a linear rule that approximates what happens after a small displacement. An integral will be a limit of sums taken over small regions. Both constructions begin with this geometry of nearness.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For \(x=(x_1,\ldots,x_n)\in\mathbb R^n\),
\[
\|x\|_2=(\sum_i x_i^2)^{1/2},\qquad \|x\|_\infty=\max_i|x_i|,
\qquad \|x\|_1=\sum_i|x_i|.
\]
In finite-dimensional Euclidean space,
\[
\|x\|_\infty\le\|x\|_2\le\sqrt n\,\|x\|_\infty,
\qquad \|x\|_2\le\|x\|_1\le\sqrt n\,\|x\|_2.
\]
The open ball is \(B_r(a)=\{x:\|x-a\|_2<r\}\). A limit \(\lim_{x\to a}f(x)=L\) relative to domain \(D\) requires: for every \(\varepsilon>0\) there is \(\delta>0\) so that \(x\in D\), \(0<\|x-a\|_2<\delta\) implies \(\|f(x)-L\|<\varepsilon\).

The example \(f(x,y)=x^2+y^2\) satisfies \(|f(x,y)|=\|(x,y)\|_2^2\); choosing \(\delta=\sqrt\varepsilon\) proves the limit at the origin is zero. A boundary point of a domain may support a *relative* limit even though the domain is not open; standard full Fréchet differentiability is then not automatically available.

### Exercises with answers

1. Show \((t,t^2)\to(0,0)\). **Answer:** \(\|(t,t^2)\|_2=|t|\sqrt{1+t^2}\to0\).
2. Describe the unit ball in the maximum norm. **Answer:** the open square \((-1,1)\times(-1,1)\).
3. Find the domain of \(1/(x^2+y^2-1)\). **Answer:** all of \(\mathbb R^2\) except the unit circle.
4. Prove coordinatewise convergence implies Euclidean convergence for fixed \(n\). **Answer:** if each of finitely many squared differences tends to zero, so does their sum and its square root.

### Sources and further reading

- OpenStax, [Calculus Volume 3](https://openstax.org/books/calculus-volume-3/pages/preface), vectors and functions of several variables.
- MIT OpenCourseWare, [18.022 Calculus of Several Variables](https://ocw.mit.edu/courses/18-022-calculus-of-several-variables-fall-2010/pages/syllabus/), the metric and geometric viewpoint.
- [Euclidean space](https://en.wikipedia.org/wiki/Euclidean_space); [Norm (mathematics)](https://en.wikipedia.org/wiki/Norm_(mathematics)).
