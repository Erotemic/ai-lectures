# 013000 — The Complex Plane: Algebra, Geometry, and Limits

**Track:** Analysis from First Principles. **Background:** real-number completeness, metric convergence, continuous functions, and geometric series. **Theme:** the algebraic operation of multiplication becomes geometry, and the ordinary metric limit supplies the foundation for complex analysis.

<!-- BEGIN SPOKEN LECTURE -->

# The Complex Plane: Algebra, Geometry, and Limits

Suppose we want to solve the equation that asks for a number whose square is negative one. There is no answer on the real number line: every real square is nonnegative. We could declare a new symbol, called i, whose square is negative one, and calculate with it. But what is this new object? Is it merely a notational trick, or does it describe a space with a geometry we can reason about?

There is a useful way to answer without taking anything on faith. Imagine a number as a pair of real coordinates. We write the pair as x plus i times y. Two such pairs add coordinate by coordinate, exactly as vectors in a plane do. We define multiplication by expanding parentheses and replacing the square of i by negative one. Thus the real coordinate of a product is the first real coordinate times the second, minus the product of the imaginary coordinates. The imaginary coordinate is the two cross terms added together.

This multiplication is not an arbitrary decoration of the plane. It encodes scaling and rotation, and it is what makes the plane into the field of complex numbers. Let us recover the algebra and geometry slowly, because almost every surprising theorem later in the subject is built from their interaction.

## What a complex number can do

A complex number has a real part and an imaginary part. The adjective imaginary is historical; both coordinates are ordinary real numbers. The number three plus two i is the point three units to the right and two units up. We can also regard it as an arrow from the origin. Adding one plus i moves the endpoint one unit right and one unit up. Multiplying by two doubles both coordinates.

Multiplying by i does something more striking. Take the number x plus i y. Its product with i is negative y plus i x. The original arrow with coordinates x and y has become an arrow with coordinates negative y and x. That is a quarter turn counterclockwise. Multiplying by i twice rotates by a half turn, which is multiplication by negative one. So the relation i squared equals negative one is consistent with a simple physical action on a plane.

What about multiplication by a general complex number? Consider two arrows, each with a length and a direction. Multiply the corresponding complex numbers. Their lengths multiply and their directions add. This is a stronger statement than the quarter-turn example. To understand it, we need a notion of length that respects multiplication.

The modulus, or absolute value, of x plus i y is the square root of x squared plus y squared. It is precisely the Euclidean distance from the origin. The distance between two complex numbers is the modulus of their difference. We therefore inherit the triangle inequality: going from one point to another by way of a third cannot be shorter than the straight-line distance. We also inherit completeness: a complex Cauchy sequence has Cauchy real and imaginary coordinates, and those coordinates converge because the real numbers are complete.

Now introduce conjugation. The complex conjugate of x plus i y is x minus i y: reflection across the horizontal axis. Multiply a number by its conjugate, and the cross terms cancel. The result is x squared plus y squared, the squared modulus. This gives a practical formula for division. To divide by a nonzero number, multiply numerator and denominator by its conjugate. The denominator becomes a positive real number, so division is always possible except by zero.

Try one concrete calculation. Divide one plus i by one minus i. Multiplying the top and bottom by one plus i gives, upstairs, one plus two i plus i squared, which is two i. Downstairs, one minus i squared, which is two. The quotient is i. Geometrically, dividing by an arrow at a negative forty-five degree angle rotates the direction by positive forty-five degrees, and the lengths cancel in this example.

Conjugation will return later when we need counterexamples: it looks like a perfectly good smooth operation on the plane, but it is not complex differentiable in the sense we will soon define. That is an early clue that complex differentiability asks more than ordinary smoothness in two real variables.

## Multiplication is rotation and scaling

A point other than the origin can be described by its length r and by an angle theta, measured from the positive real axis. The point is r times the sum of cosine theta and i times sine theta. This is called polar form.

The angle is not unique. Adding one complete turn gives the same point. Nor is a continuous choice of angle automatically available across the entire punctured plane. Those two observations may seem like fussy bookkeeping, but they become decisive when logarithms and contour integrals appear.

For now, multiply two numbers in polar form. Ordinary algebra plus the sine and cosine addition formulas shows that the new length is the product of the lengths and the new angle is the sum of the angles. This is why powers have such simple geometric meaning. Squaring a complex number squares its distance from zero and doubles its angle. Raising it to the third power triples the angle. Roots reverse this construction: to solve for a fifth root of one, we look for angles whose fifth multiple is a whole number of turns. There are five distinct solutions, equally spaced around the unit circle.

Listen to that result before seeing any formula: in the real line, the equation asking for fifth powers equal to one has only one real solution. In the complex plane, it has five solutions, arranged as vertices of a regular pentagon. Algebraic multiplicity is visible as geometry.

The unit circle, the set of points of modulus one, is particularly useful. It is closed under multiplication. Every complex number of modulus one acts on the plane as a pure rotation. In the language of linear algebra, complex multiplication by a fixed number is a real linear transformation represented by a special two-by-two matrix. That matrix is a rotation followed by uniform scaling, not an arbitrary distortion.

## Exponentials and angles

Where does the familiar exponential function fit? For a real input, the exponential grows by a rate equal to its current value. For a purely imaginary input, the corresponding complex exponential moves along the unit circle. The precise statement is Euler's formula: the exponential of i times theta equals cosine theta plus i sine theta.

We do not need to treat Euler's formula as a magical identity. Start with the power series defining the exponential. Substitute i times theta. Even powers of i alternate between positive and negative real terms. Odd powers contain i and alternate in the same way. Grouping the even terms gives the cosine series, and grouping the odd terms gives i times the sine series. Absolute convergence of the series justifies regrouping. This is a concrete payoff from our work with uniform and power-series convergence.

One more consequence matters for the geometry. The exponential never vanishes. Its modulus at x plus i y is the real exponential of x, while y supplies a rotation. Every nonzero complex number can be written as the exponential of some complex number. But the input is not unique: increase the imaginary part by one full turn, and the output stays the same.

That is why a complex logarithm is not globally single-valued on the punctured plane. We can choose a branch by restricting angles to an interval, for example excluding the negative real axis. On such a cut domain the logarithm can be made continuous, and in fact holomorphic once we develop complex derivatives. Across the cut, the angle has to jump by a full turn. The difficulty is not bad notation; it is a topological obstruction caused by going around the origin.

## Limits in two directions, then all directions

So far we have algebra and geometry. Analysis begins when we let points approach one another. A sequence of complex numbers converges to a target if the moduli of their differences from that target approach zero. Equivalently, both real and imaginary coordinates converge to the corresponding coordinates of the target. There is no new definition to memorize if you already understand limits in a metric space: we are using the Euclidean metric on a plane.

Limits of complex-valued functions work in the same way. A function is continuous at a point when inputs sufficiently close to that point produce outputs close to the function's value. The input is now allowed to approach along any direction in the plane. From the east, west, north, south, along a diagonal, or along a curve, the same limit must emerge.

A warning: checking a few directions is useful for disproving a limit, but it rarely proves a limit. If one path gives zero and another gives one, we have a contradiction and no limit exists. If ten paths give zero, infinitely many more possibilities remain. A complete proof should use a bound that depends on the distance to the target, not on a particular path.

Consider the function that sends a nonzero complex number z to its conjugate divided by itself. Along the positive real axis, the conjugate equals z, so the quotient is one. Along the positive imaginary axis, the conjugate is negative z, so the quotient is negative one. Therefore the function has no limit as z approaches zero. The calculation takes two paths, but the conclusion is about all paths: no common limit is possible.

For a contrasting example, consider z squared. Its modulus is the square of the modulus of z. As z approaches zero through any path, that squared distance approaches zero. This one inequality proves the limit for every possible approach, which is exactly what the definition demands.

It is worth separating the complex modulus from the complex order relation. The real numbers have a natural order compatible with addition and multiplication. Complex numbers do not have an order with the same field properties. We cannot speak of one complex number being larger than another in the ordinary real sense. But distances and upper bounds on distances still make sense, because moduli are nonnegative real numbers. This is why the triangle inequality and estimates do so much work in complex analysis.

## Disks, holes, and domains

A disk is the set of all complex points within a fixed positive distance of a center. An open set is one in which every point has some sufficiently small disk entirely inside the set. That is the right setting for differentiation, because we want to perturb a point in any complex direction without leaving the domain.

A domain is a nonempty, open, connected set. In the plane, an open connected set is also path connected; one can travel between any two of its points by a path staying inside. But being connected does not mean having no holes. The punctured plane, which excludes the origin, is connected. We can walk around the missing point without crossing it. Yet a loop that circles the origin cannot be shrunk to a point while remaining in the punctured plane.

Why should this matter for calculus? In real calculus, an antiderivative lets us evaluate an integral using only endpoints. In complex calculus, a path may wind around a missing point. Some integrals detect that winding. We will compute one explicitly, and it will explain why contour theorems must state where a function is holomorphic, not merely where a curve happens to lie.

The complex plane also provides familiar compactness facts. A closed bounded subset of the plane is compact, because it is a closed bounded subset of two-dimensional Euclidean space. Continuous complex-valued functions on compact sets are bounded and uniformly continuous. We can take maxima of their moduli. But we cannot use the real Extreme Value Theorem to say a complex-valued function has a largest complex value: no such order exists. The modulus is the appropriate real quantity.

To see why closed disks are such powerful working regions, picture a function defined on an open region that contains a closed disk. The closed disk gives a finite maximum for continuous magnitudes, and it leaves room for a slightly larger disk within the domain. That margin lets us bound series and compare function values while keeping denominators away from zero. Later, Cauchy's integral formula will turn information on the boundary circle into strong bounds at the center.

## The polynomial that insists on having five roots

Let us return to the fifth roots of one and make the computation precise enough to trust. A fifth root w of one must have modulus one, because the fifth power of its modulus is one. Its angle multiplied by five must be an integer number of full turns. Choose the angles zero, one fifth of a turn, two fifths, three fifths, and four fifths. These give five different solutions. A polynomial of degree five cannot have more than five distinct roots over a field, so the list is complete.

This is a special case of a large fact: every nonconstant complex polynomial has at least one complex zero. We are not ready to prove that result yet. The proof we will eventually give can arise from the Cauchy integral formula and Liouville's theorem. The complex plane is therefore not just a convenient place to store pairs of real numbers; it is, in a precise algebraic sense, the natural setting in which polynomial equations have all the roots their degrees permit, when counted with multiplicity.

But pay attention to what we have and have not established. We know complex arithmetic, the metric topology, and the exponential geometry. We have not shown that an arbitrary function that is smooth as a map of two real coordinates is complex differentiable. We have not shown that integrals around loops vanish. And we have not yet justified a global logarithm.

The next question is exactly where the subject changes character. Suppose a function changes by approximately a linear expression when its input changes slightly. In two real variables, the linear expression may stretch differently in different directions. But multiplying a complex increment by one complex number can only rotate it and scale it uniformly. If a derivative must work for every approach direction, the geometry places a severe constraint on the function.

That constraint is the source of both the Cauchy–Riemann equations and the extraordinary rigidity of holomorphic functions. The tools we need are already in hand: small increments, distances, directional approaches, and local linear approximation. The surprising results will come from asking all these pieces to cooperate at once.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

### Algebra, norm, and geometry

For \(z=x+iy\), \(w=u+iv\):
\[
zw=(xu-yv)+i(xv+yu),\quad \bar z=x-iy,\quad |z|=\sqrt{x^2+y^2},\quad z\bar z=|z|^2.
\]
For \(w\neq0\), \(z/w=z\bar w/|w|^2\). The norm is multiplicative: \(|zw|=|z||w|\). A Cauchy sequence \(z_n=x_n+iy_n\) has Cauchy real and imaginary coordinates, hence converges in \(\mathbb C\).

For \(z=re^{i\theta}\) and \(w=se^{i\phi}\), \(zw=rs e^{i(\theta+\phi)}\). Euler's formula follows from the absolutely convergent exponential series and parity of the powers of \(i\):
\[
e^{i\theta}=\sum_{n\ge0}\frac{(i\theta)^n}{n!}=\cos\theta+i\sin\theta.
\]
Each nonzero \(z\) has logarithms \(\log|z|+i(\arg z+2\pi k)\) for \(k\in\mathbb Z\); a continuous single-valued logarithm cannot exist on all \(\mathbb C\setminus\{0\}\).

### Relative limits and failed paths

For an open domain \(U\subset\mathbb C\), \(\lim_{z\to a}f(z)=L\) means
\[
\forall\varepsilon>0\;\exists\delta>0:\quad z\in U,\ 0<|z-a|<\delta\implies |f(z)-L|<\varepsilon.
\]
For \(f(z)=\bar z/z\), \(z=t>0\) gives 1 and \(z=it\), \(t>0\), gives \(-1\). Thus the origin has no limit. In contrast \(|z^2|=|z|^2\) gives \(z^2\to0\).

### Exercise set with answers

1. **Explicit rotation:** Compute \(i(3+2i)\). **Answer:** \(-2+3i\), a counterclockwise quarter turn.
2. **Reciprocal:** Compute \((1+i)/(1-i)\). **Answer:** \(i\).
3. **Roots of unity:** Find the four fourth roots of unity. **Answer:** \(1,i,-1,-i\).
4. **Two paths:** Show \(\lim_{z\to0}z/\bar z\) fails. **Answer:** Along the real axis it equals 1; along the imaginary axis it equals \(-1\).
5. **Compactness:** Explain why \(\{z:|z|\le1\}\) is compact but \(\{z:|z|<1\}\) is not. **Answer:** Closed and bounded subsets of \(\mathbb R^2\) are compact; the open disk omits its boundary limit points.
6. **Distinguish order and modulus:** Does \(f(z)=z\) attain a maximum on the unit disk? **Answer:** There is no natural order-based maximum in \(\mathbb C\), but \(|f|\) attains maximum 1 on the boundary.

### Further reading

- MIT OpenCourseWare, *18.112 Functions of a Complex Variable*, Lecture 1 and Lecture 2, https://ocw.mit.edu/courses/18-112-functions-of-a-complex-variable-fall-2008/pages/lecture-notes/.
- MIT OpenCourseWare, *18.04 Complex Variables with Applications*, Topic 1, https://ocw.mit.edu/courses/18-04-complex-variables-with-applications-spring-2018/pages/lecture-notes/.
- Wikipedia, *Complex number*, https://en.wikipedia.org/wiki/Complex_number.
