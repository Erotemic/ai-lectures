# Curvature, constrained extrema, and volume integration

<!-- BEGIN SPOKEN LECTURE -->

# Curvature, constrained extrema, and volume integration

## Hessians and Taylor's Formula: The Shape Beyond the Tangent Plane

A tangent plane captures the leading change in a smooth surface. But two surfaces can have the same tangent plane at a point and bend in entirely different ways. The second derivatives describe that bending. Collected into a matrix, they form the Hessian.

Consider the functions x squared plus y squared and x squared minus y squared. Both have value zero and gradient zero at the origin. Their tangent planes are the same horizontal plane. Yet the first is a bowl, rising in every nonzero direction, while the second is a saddle, rising along the x axis and falling along the y axis. First derivatives cannot distinguish them at the origin. Their second-order terms do.

### Differentiate a derivative

For a twice-differentiable scalar function of x and y, we can differentiate first with respect to x and then with respect to y, or vice versa. The resulting mixed partial derivatives measure how the x slope changes as y changes and how the y slope changes as x changes. Under the usual hypothesis of continuous second partial derivatives near the point, these mixed derivatives agree. The Hessian is then a symmetric matrix.

Why should symmetry matter? A symmetric matrix has real eigenvalues and an orthogonal set of eigenvectors. Along those eigenvector directions, the quadratic bending separates into independent curvatures. The Hessian is a linear-algebraic picture of local shape.

But do not drop the continuity qualification on the mixed-derivative theorem. At less regular points, both mixed second derivatives can exist and still differ. The elementary rule is powerful because it comes with hypotheses.

### The second-order Taylor approximation

For a smooth f, near a base point a, the value of f at a plus h can be approximated by f at a, plus the derivative of f applied to h, plus one half of h transposed times the Hessian at a times h. The remaining error is small compared with the square of the displacement length, provided the second derivatives are continuous near the point.

We can see where this comes from without memorizing a many-variable formula. Fix the displacement h and follow the line a plus t h as t runs from zero to one. Along this line, f becomes an ordinary one-variable function of t. Its first derivative is Df times h. Its second derivative is h transposed times the Hessian times h. Apply one-variable Taylor's theorem, and the multivariable formula follows.

The method of restricting to a line is valid here because a full smoothness hypothesis already gives uniform control of the derivatives. Contrast this with the failed path tests for continuity: there we tried to infer a global limit merely by checking selected curves. Here we derive an identity for each displacement from a theorem that already applies everywhere nearby.

### A computed saddle

Take the function exponential x times cosine y. At the origin its value is one. Its gradient there is one comma zero. The Hessian there has entries one and minus one along the diagonal, with zero off-diagonal entries. Therefore its quadratic Taylor approximation is one plus x plus one half times x squared minus one half times y squared. The first-order term tilts the surface in the x direction, and the opposite signs of the second-order terms describe different bending along x and y.

For a still simpler example, f equals x squared minus y squared has no remainder beyond second order. Its Hessian is the constant diagonal matrix with entries two and minus two. A displacement along the x axis raises the value by a square, while one along the y axis lowers it by a square. There is no local minimum or maximum at the origin despite the gradient being zero.

### The Hessian as a bilinear form

The expression h transposed H h is a quadratic form. A positive definite Hessian means this expression is positive for every nonzero h. A negative definite Hessian makes it negative. An indefinite Hessian has both signs. At a critical point these distinctions often classify a strict local minimum, a strict local maximum, or a saddle.

If the Hessian has a zero eigenvalue, the second-order test is inconclusive. The function x to the fourth at the origin has zero second derivative but a strict minimum. The function minus x to the fourth has the same zero second derivative but a strict maximum. The function x cubed has neither. Higher-order terms decide.

This is not a failure of Taylor's theorem. The theorem accurately reports that the quadratic contribution is absent. It is our attempt to classify the point using only that contribution that runs out of information.

### Why quadratic approximations matter

Optimization algorithms use Hessians to predict curvature and propose steps. Mechanics uses quadratic energy approximations to analyze the stability of an equilibrium. Statistics uses local quadratic approximations of log-likelihoods. Riemannian geometry later uses second derivatives of coordinate data to describe acceleration and curvature, with additional geometric care about what is coordinate invariant.

The Hessian completes a progression. Continuity controls values. The derivative predicts first-order change. The Hessian predicts second-order bending. Each layer requires stronger information, and each gives a more refined local model.

## Maxima, Minima, and Saddle Points in Several Variables

A function of one variable may have a local maximum at a point where its derivative is zero. In several variables, we might begin with the same idea: at an interior local maximum or minimum of a differentiable function, the gradient must vanish. But solving the gradient equations is only the beginning. A critical point could be a minimum, a maximum, a saddle, or something more complicated. And the largest value on a restricted region may occur on its boundary, where the unconstrained gradient need not vanish.

Let's see how to organize these possibilities without losing candidates.

### An interior minimum by completing the square

Consider f of x and y equal to x squared plus twice y squared minus twice x minus four y. Its x partial derivative is two x minus two, and its y partial derivative is four y minus four. Both vanish at one comma one. The Hessian is diagonal with entries two and four, so it is positive definite. The second-derivative test therefore identifies a strict local minimum.

But we can say more. Complete the squares. The function equals x minus one squared, plus twice y minus one squared, minus three. Every squared term is nonnegative, so the function is at least negative three everywhere, with equality only at one comma one. This proves a global minimum, not just a local one. It also shows the value of having more than one proof method: the Hessian classifies local shape, while the algebraic identity gives a global bound.

The absence of a global maximum is equally clear. Let x grow without bound while y stays one. The function goes to infinity.

### Why zero gradient is not enough

At the origin, the function x squared minus y squared has gradient zero. Along the x axis it is positive away from the origin; along the y axis it is negative. No neighborhood of the origin consists entirely of values above or entirely below the value at the origin. This is a saddle point.

The Hessian has a positive and a negative eigenvalue. The second-derivative test detects the saddle. A positive definite Hessian at a critical point implies a strict local minimum; a negative definite Hessian implies a strict local maximum; an indefinite Hessian implies a saddle. If the Hessian has zero eigenvalues, the test may be inconclusive.

Consider x to the fourth plus y to the fourth. The Hessian at zero is the zero matrix, but the function has a strict global minimum there. The geometry first becomes visible at fourth order. Derivative tests are tools, not substitutes for examining the function.

### Boundary candidates are different

Now maximize x plus y on the closed unit disk. The gradient is the nonzero constant vector one comma one. It never vanishes anywhere, so there are no interior critical points. Does this mean the function has no maximum? No. The disk is closed and bounded, hence compact, and the function is continuous, so a maximum and minimum must exist.

We need to check the boundary circle. Write x equals cosine t, y equals sine t. Along the circle the function is cosine t plus sine t. This reaches its maximum square root of two at the point one over square root of two comma one over square root of two, and its minimum negative square root of two at the opposite point. The extrema occur on the boundary, although the full gradient is not zero there.

The Cauchy–Schwarz inequality provides another solution. The dot product of one comma one with a point in the unit disk is at most square root of two times the length of that point, hence at most square root of two. Equality requires the point to be the outward unit vector in the gradient direction. Both proofs emphasize that the domain matters.

### A systematic procedure for closed regions

Suppose we seek absolute extrema of a continuous function on a compact region in the plane. First find interior critical points, where all partial derivatives vanish or, for a less regular function, where differentiability fails. Then analyze the boundary separately. If the boundary is a smooth curve, parametrize it and optimize the resulting one-variable function. If the boundary has corners or several pieces, examine each piece and its endpoints. Finally compare actual function values at all the candidates.

This method handles a rectangle, triangle, disk, or other manageable region. It is tempting to solve only the gradient equations and announce an answer, but that can miss the true extrema entirely.

For noncompact regions, continuity alone does not guarantee that absolute extrema exist. Even a bounded function can approach a supremum without attaining it. On the whole real line, arctangent x approaches one half pi but never reaches it. In several variables the same escape to infinity is possible.

### Beyond calculus exercises

The calculus of extrema leads directly to optimization, equilibrium mechanics, and variational problems. A system at an interior stable equilibrium often has vanishing first variation and positive second variation, at least after relevant constraints are accounted for. A saddle can be an equilibrium without being stable. On a boundary or a constraint surface, the gradient need only vanish along allowed directions.

That final observation leads to constrained optimization. First learn to identify all the places where extrema may occur. Then ask which directions are actually permitted by the problem.

## Lagrange Multipliers: Optimization Along Constraints

Suppose a designer can choose x and y, but not independently. The available budget fixes x plus y equal to one. The designer wants to minimize x squared plus y squared. The unconstrained minimum would be x equals zero and y equals zero, but that point violates the constraint. We must optimize only along the line of feasible choices.

On that line, y equals one minus x. Substitute into the objective. It becomes x squared plus the square of one minus x. Differentiate the one-variable expression: four x minus two. The minimum occurs at x equals one half, y equals one half. The objective value is one half. This direct substitution method is reliable when the constraint is easy to solve.

Lagrange multipliers generalize the same geometry when substitution is inconvenient.

### Allowed directions at a constraint

Write the constraint as g of x and y equals zero. If the gradient of g is nonzero at a feasible point, it is normal to the constraint curve. Any velocity along the curve is perpendicular to the gradient of g. At an extremum of f restricted to that curve, the derivative of f in every allowed tangent direction must vanish. So the gradient of f must also be perpendicular to the tangent direction.

In the plane, when the constraint is a regular smooth curve, two nonzero vectors perpendicular to the same tangent line are parallel. Therefore the gradient of f is a scalar multiple of the gradient of g. We call that scalar lambda, the Lagrange multiplier.

The equations are gradient f equals lambda times gradient g, together with g equals zero. They are necessary conditions for a regular constrained extremum. They do not automatically guarantee that a solution is a minimum or maximum. We still need to compare candidates or analyze second-order behavior along the constraint.

### Solve the example using the multiplier

Let f equal x squared plus y squared and let g equal x plus y minus one. The gradients are two x comma two y and one comma one. The multiplier condition says two x equals lambda and two y equals lambda. Thus x equals y. Combined with x plus y equals one, we obtain x and y both one half.

For this problem we can also prove global minimality without derivatives. The identity x squared plus y squared equals one half times the square of x plus y, plus one half times the square of x minus y, shows that every feasible point has objective at least one half. Equality occurs exactly when x equals y. This is a useful check on a stationary-point calculation.

What does lambda mean? If the constraint right-hand side changes from one to a nearby value b, the minimum becomes b squared divided by two. Its derivative with respect to b is b. At b equals one, that derivative equals one, which is precisely the multiplier under our convention g equals x plus y minus b. The multiplier measures how the optimum changes when the constraint level changes, under suitable regularity and uniqueness assumptions. This sensitivity interpretation is not merely a trick of algebra.

### A curved constraint

Consider maximizing and minimizing f equals x plus y on the unit circle x squared plus y squared equals one. The objective gradient is one comma one. The constraint gradient is two x comma two y. The multiplier equation gives one comma one equals lambda times two x comma two y. Consequently x equals y at a regular solution. On the unit circle that leaves two points: both coordinates one over square root of two, or both negative one over square root of two. Their objective values are square root of two and negative square root of two.

The circle is compact, so these are the global maximum and minimum after checking the candidate values. The Lagrange equations alone only generated candidates; compactness and comparison completed the argument.

### Why regularity cannot be ignored

Now impose the constraint x squared plus y squared equals zero. There is only one feasible point: the origin. Every objective function defined there attains both its feasible maximum and feasible minimum at that singleton. But the constraint gradient vanishes at the origin. Take the objective f equals x, whose gradient is one comma zero. There is no lambda that makes one comma zero equal to lambda times zero comma zero.

The multiplier condition fails, not because the extremum is unreal, but because the constraint is singular at the point. The theorem assumes the constraint gradients are independent and nonzero in the required sense. Singular constraints demand separate analysis.

With several constraints, their gradients span a normal space, and the objective gradient must lie in that span at a regular constrained extremum. Independence of constraint gradients is the matrix rank condition that makes the feasible set locally smooth.

### What to do in a real optimization problem

First write the constraints clearly and determine the feasible set. Check whether it is compact, whether it has a boundary, and whether the constraints are regular. Solve the multiplier equations only for regular interior points of the feasible constraint set. Analyze any singular points, corners and inequality boundaries separately. Compare the actual objective values. If the feasible set is not compact, establish existence or rule out escape to infinity by another argument.

Lagrange multipliers are not a magic equation that replaces geometry. They are the algebraic expression of a simple fact: at an optimum, change in the objective vanishes along directions you are allowed to move.

## Double and Triple Integrals: Adding Values Across a Region

A road map can describe the temperature at every point on a field. A single temperature reading tells us little about the total heat content. To combine information across the whole field, we divide the region into small patches, multiply each patch's area by a representative temperature, add the contributions, and let the patches become small. That is a double integral.

The familiar one-variable integral uses intervals of small length. In two variables the pieces have small area. In three variables they have small volume. The principle is the same: a sum weighted by the size of each piece converges to an integral if the function and domain behave well enough.

### A rectangle and a complete calculation

Take the unit square, where x and y each run from zero to one. Let the density at a point be x plus twice y. This is nonnegative on the square and increases as we move right or up. To find the total mass of a sheet with this density, divide the square into tiny rectangles. At a sample point in each rectangle, evaluate x plus twice y and multiply by the rectangle's area. Add the contributions.

As the subdivisions become fine, the sum approaches the double integral over the square. We can calculate it using one-variable antiderivatives. First integrate with respect to x while keeping y fixed. The result from zero to one is one half plus twice y. Next integrate that expression with respect to y from zero to one. We obtain one half plus one, or three halves.

There is a useful check. The average value of x on the unit square is one half; the average value of y is one half. The average of x plus twice y is one half plus twice one half, which is three halves. Since the square has area one, its total mass is also three halves.

The units keep the calculation honest. If density is measured in kilograms per square meter and coordinates are measured in meters, then density times area gives kilograms. The integral is not a mysterious anti-derivative symbol; it is the limit of a weighted sum.

### Integrating over a curved region

What if the region is a disk rather than a rectangle? We can still divide a containing rectangle into small boxes, count the pieces that lie inside the region, and approximate the curved boundary more and more closely. For a bounded region with a sufficiently regular boundary and a continuous bounded integrand, the boundary contribution disappears in the limit as the mesh gets fine.

The value of the integral depends on both the function and the region. Two regions with the same area need not give the same integral of a nonconstant density. The function may be larger on one region than the other. This is why the domain must be specified explicitly, not merely sketched vaguely.

When the integrand equals one, the double integral gives the area of the region. When it equals a constant density rho, the integral gives rho times area. When it varies, the integral adds all local contributions. Similarly, integrating one over a solid region gives its volume.

### Three dimensions

Imagine a cube one meter on each side with a density that depends only on height z, say one plus z. The bottom has density one and the top density two. Divide the cube into tiny boxes. Each contribution is density times small volume. Integrating first over the horizontal square gives area one times the density at height z. Integrating from height zero to one gives one plus one half, or three halves units of mass.

This shows how triple integration can sometimes be understood as stacking thin slices. The same idea works when each horizontal slice has a different area, provided we describe that area correctly. A ball is a natural example: its slices perpendicular to an axis are disks of varying radius.

### What conditions are being assumed?

For a continuous function on a compact rectangle, ordinary Riemann sums converge to an integral. For bounded regions with suitably negligible boundaries, the same works after extending the integrand by zero outside. There are more complicated bounded functions and sets for which Riemann integration is inadequate; Lebesgue integration offers a broader framework. Our first goal is to understand the geometric sum and compute it on well-behaved regions.

A double integral is not automatically a single-variable integral with an extra symbol attached. It expresses a fundamentally two-dimensional sum. The reason iterated single-variable integrals can compute it is a theorem, with hypotheses. That theorem is the subject of the next step.

### Looking ahead conceptually

Double and triple integrals appear whenever a local quantity must be accumulated over an area or volume. Density gives mass, probability density gives probability, and energy density gives total energy. A change of variables will let us use coordinates adapted to the shape of the region. But that change will require a scale factor: a tiny coordinate rectangle may not represent a rectangle of equal physical area.

For now the defining picture is enough. Cut the region into small pieces, approximate each contribution, add, and take the limit. Every later integration theorem is a way of making that fundamental construction more efficient or more invariant.

## Iterated Integrals: Slicing Regions and Exchanging the Order

Imagine a triangular garden. Rather than trying to calculate its area in one two-dimensional step, we can slice it into thin vertical strips. At each x coordinate, the strip runs between a lower y boundary and an upper y boundary. Find the area or mass of the strip by integrating in y, then accumulate the strips by integrating in x. This is an iterated integral.

The method is familiar from elementary geometry. The theorem that justifies it is a form of Fubini's theorem: under suitable integrability assumptions, integrating successively in the two variables equals integrating over the whole region. We must understand the region and the assumptions, not only the notation.

### Describe a triangle carefully

Take the region where zero is at most y, y is at most x, and x is at most one. Draw it or imagine a right triangle under the diagonal y equals x in the unit square. For a fixed x between zero and one, y ranges from zero to x. The integral of x plus y over that region becomes an outer integral over x from zero to one and an inner integral over y from zero to x.

Perform the inner integral. Since x is fixed, integrating x with respect to y contributes x times x, or x squared. Integrating y contributes half of x squared. The total is three halves times x squared. Integrating from zero to one gives one half. Thus the total mass for this density is one half.

We can calculate the same integral by horizontal slicing. A fixed y lies between zero and one. The condition y at most x says x runs from y to one. Integrating x plus y first in x produces one half of one minus y squared, plus y times one minus y. Simplify and integrate from zero to one; the result is again one half.

Changing the order is often the fastest way to simplify a difficult integral. But the limits must describe the same region, not just use the same numbers in a different order. A common error is to swap the integration symbols while leaving the bounds unchanged even though the bounds depend on the other variable.

### The rectangular case

For a continuous function on a closed rectangle, both orders of iterated integration are valid and equal to the double integral. The continuity hypothesis ensures ordinary Riemann integrability and avoids many pathologies. For more general measurable functions, the correct theorem has conditions on integrability and signs.

A nonnegative measurable function can be integrated with Tonelli's theorem, even if the result is infinite. Nonnegative contributions cannot cancel to conceal a divergent total. For a signed measurable function, Fubini's theorem is safely applied when the integral of the absolute value is finite. Under this absolute-integrability condition, both iterated integrals exist almost everywhere in the relevant sense and agree with the multiple integral.

This distinction is not merely technical. Reordering infinitely many positive terms is safe in an extended sense; reordering conditionally convergent signed terms can change their sum. Integrals have a related issue. When you meet a function with singularities, or a domain of infinite extent, check nonnegativity or absolute integrability before exchanging operations.

### Slicing a solid

For a three-dimensional region, choose a coordinate such as z. At each height, the horizontal cross-section has some area A of z. The volume equals the integral of A of z over the permitted heights, for well-behaved solids.

For the unit ball, the slice at height z is a disk of radius the square root of one minus z squared. Its area is pi times one minus z squared. Integrate this from minus one to one. We get pi times two minus two thirds, or four pi over three, the volume of the unit ball. The same calculation extends to a ball of radius R and produces four pi R cubed over three.

This argument is more than memorizing the sphere-volume formula. It shows how higher-dimensional accumulation can be organized into nested lower-dimensional problems. It also explains why units multiply: an area times a small thickness produces a small volume.

### Why order can matter computationally even when it does not mathematically

Suppose the region is easier to describe vertically than horizontally. The integral with vertical slices may have simple bounds; the horizontal description could require splitting into several pieces. The two results are mathematically equal under the theorem, but one setup is easier and less error prone.

Similarly, an integrand that is hard to integrate with respect to x might be simple with respect to y. Before beginning symbolic integration, inspect the region and the formula. Choosing the order is part of solving the problem, not a mechanical afterthought.

The essential picture is that a multiple integral totals contributions over an entire region, while iterated integrals total them in successive families of slices. Tonelli and Fubini tell us when these two ways of accumulating information are equivalent.

## Polar, Cylindrical, and Spherical Integrals: Coordinates Built for Shape

A disk is difficult to describe using horizontal and vertical bounds. Its boundary involves square roots, and a rectangular grid cuts many pieces across the edge. But in polar coordinates the same disk is described by two simple statements: the radius runs from zero to one, and the angle makes one complete turn. This simplification is worth making only if we correctly transform the area element.

Suppose the location of a point in the plane is given by its radius r and its angle theta. The Cartesian coordinates are x equals r cosine theta and y equals r sine theta. Each small change in r moves outward. Each small change in theta moves around a circle. A small angular change of size delta theta creates an arc of length approximately r times delta theta. Multiply that by a small radial thickness delta r, and the resulting thin wedge has area approximately r times delta r times delta theta.

This is why the polar area element is r times d r times d theta. It is not simply d r times d theta. Near the center, an angular interval covers almost no area; far from the center, the same angular interval sweeps a wider strip. The factor r corrects for that changing scale.

### Integrate a radial function on a disk

Consider the function x squared plus y squared over the unit disk. In polar coordinates the function is r squared. The disk is zero at most r at most one, zero at most theta at most two pi. The integral is therefore the integral of r squared times the area factor r. Integrate r cubed from zero to one to obtain one quarter, then multiply by two pi. The answer is pi over two.

We can check its meaning: the disk has area pi, and its average squared distance from the origin is one half. Points near the rim have larger squared radius than points near the center, but there is more area near the rim. The result reflects both facts.

If we had forgotten the r factor, we would have computed two pi over three, a different value with no valid geometric justification. Most early errors in polar integration are errors about area scaling rather than about antiderivatives.

### Cylindrical coordinates

In three dimensions, cylindrical coordinates keep the polar description in the horizontal plane and add height z. We write x equals r cosine theta, y equals r sine theta, and z stays z. The volume element is r times d r times d theta times d z. A cylinder of radius two and height three can be described by r between zero and two, theta over a full turn, and z between zero and three. Integrating one over that region gives twelve pi, exactly base area four pi times height three.

Cylindrical coordinates are useful for pipes, rotating shafts, radial heat distributions, and any problem with symmetry around an axis. They separate the angular variable from the vertical one without forcing the geometry into rectangular bounds.

### Spherical coordinates

For a solid ball, even cylindrical coordinates can require a square-root height bound. Spherical coordinates use distance rho from the origin, polar angle phi measured down from the positive z axis, and azimuth theta measured around that axis. A point has x equal to rho sine phi cosine theta, y equal to rho sine phi sine theta, and z equal to rho cosine phi.

A small radial displacement contributes one length factor. A small polar-angle displacement travels approximately rho times delta phi. A small azimuthal displacement travels around a circle of radius rho sine phi, contributing rho sine phi times delta theta. Multiply the three small lengths and we obtain the volume factor rho squared times sine phi.

The unit ball is described by rho between zero and one, phi between zero and pi, and theta from zero to two pi. Integrating one with the spherical volume factor gives one third from the radial integral, two from the polar-angle integral, and two pi from azimuth. The product is four pi over three, the usual unit-ball volume.

### Coordinate singularities are not physical singularities

At r equals zero, every polar angle names the same point. At the poles of spherical coordinates, the azimuth is similarly redundant. The coordinate maps lose local invertibility there, and the scale factor vanishes. This does not mean the disk or ball is singular. It means our chosen coordinates are redundant at those locations.

These singular sets have zero area or volume in the usual integrals, and the change-of-variables formula can be applied away from them, then extended across them for integrable functions. In more delicate settings, singular behavior of the integrand still requires analysis; a vanishing Jacobian factor does not automatically remove an actual divergence.

### Choose coordinates for the mathematics, not for tradition

When the region and integrand depend mostly on distance from an axis, cylindrical coordinates may reduce a triple integral to a one-variable calculation. When they depend on distance from the origin, spherical coordinates can do the same. For a rectangular box, Cartesian coordinates are usually simpler.

The lesson is not to memorize three unrelated volume elements. Each is a consequence of the same geometric principle: a small coordinate box is transformed into a tiny physical parallelepiped, and its volume is scaled by the Jacobian determinant. The general change-of-variables theorem formalizes that picture.

## The Change-of-Variables Theorem: What the Jacobian Measures

Imagine drawing a fine square grid on a sheet of rubber and stretching the sheet. A small square becomes approximately a parallelogram. The area of that parallelogram may be larger or smaller than the original square, and it may be turned over. The determinant of the derivative matrix describes the signed first-order area scale. Its absolute value tells us how much area, independent of orientation, is gained or lost.

This is the geometric heart of the change-of-variables theorem. When we integrate a density over a region using new coordinates, the integrand must be multiplied by the absolute value of the Jacobian determinant of the coordinate map. Otherwise we count equal-sized coordinate boxes as equal physical areas even though the transformation may stretch some more than others.

### First see a linear transformation

Take the map from coordinates u and v to x equals two u and y equals three v. A unit square in the u-v plane becomes a rectangle with side lengths two and three in the x-y plane. Its area is six. The derivative matrix has diagonal entries two and three; its determinant is six. This exact computation illustrates the general rule.

Now take x equals u plus v and y equals u minus v. The derivative matrix has rows one comma one and one comma minus one. Its determinant is minus two. The negative sign means the orientation is reversed; the magnitude two means areas are doubled. A unit square maps to a parallelogram of area two. An ordinary area integral must use two, not negative two.

Why retain the sign at all? Signed determinants matter for orientation-sensitive integration, especially differential forms. If we reverse an oriented coordinate chart, an oriented area form changes sign. But mass, physical area and unsigned volume do not become negative. Their change-of-variables formula uses the absolute value.

### A nonlinear map with varying scale

Let x equal u, and let y equal the product of one plus u and v. Take both u and v between zero and one. For a fixed u, the v interval maps to y from zero to one plus u. The image region is therefore between y equals zero and y equals one plus x, with x between zero and one.

The Jacobian matrix has first row one comma zero. The second row is v comma one plus u. Its determinant is one plus u. Integrate that factor over the unit u-v square. The v integral contributes one, and the u integral of one plus u from zero to one gives three halves. So the image has area three halves.

Check by direct geometry. The region is a trapezoid with vertical height one at x equals zero and height two at x equals one. Average height is three halves over width one. Same answer. The nonlinear coordinate calculation and geometric slicing agree.

Notice that the Jacobian is not constant here. A small box at u equals zero maps with area scale one; a small box at u equals one maps with scale two. The integral averages the local stretching across the whole domain. This is why a nonlinear map's area factor must remain inside the integral.

### Statement of the theorem and its boundaries

Suppose a smooth enough coordinate map is one-to-one from a region in the new coordinates onto the region of integration, with a smooth inverse and nonzero Jacobian determinant in the interior. Then the integral of f over the image equals the integral over the new-coordinate region of f composed with the map, times the absolute value of the determinant.

In practical cases it is enough to split the region into suitable pieces, ignoring boundary sets of zero measure. The theorem has more general versions for measurable maps and regions; the essential local picture persists.

A warning: the magnitude of a Jacobian does not correct for multiple counting by itself. If the map traces the same physical region twice, a naive integral over both copies counts it twice. Polar coordinates with angle running from zero to four pi trace the disk twice. Integrating the usual polar area factor over that interval gives twice the disk area. The transformation must be injective almost everywhere on the chosen parametrization or the multiplicity must be handled explicitly.

### Derive the rule from linearization

Take a tiny coordinate box centered at a point. A differentiable map sends its edges approximately to the images of the coordinate edge vectors under the derivative matrix. The volume of the resulting parallelepiped is the absolute determinant times the original box volume. The nonlinear error becomes negligible as the box shrinks. Summing the transformed local contributions and passing to the limit yields the change-of-variables formula under the theorem's hypotheses.

This argument links three foundational ideas. The derivative is a local linear map. The determinant measures the volume scaling of a linear map. The integral is a limit of weighted sums. Their combination makes the change-of-variables theorem almost inevitable.

In later geometry, the same mechanism appears in the transformation law for top-degree differential forms, where orientation is retained instead of discarded. Understanding both versions prevents a persistent confusion: the determinant has a sign, but a physical volume element carries its magnitude.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Hessians and Taylor's Formula: The Shape Beyond the Tangent Plane

**Track:** Multivariable Calculus from First Principles. **Background:** total derivatives and one-variable Taylor expansions. **Question:** what does the first-order approximation miss, and how does second-order geometry appear?

#### Mathematical companion (not spoken)

For \(f\in C^2(U)\), the Hessian is \(H_f(a)=(\partial_i\partial_j f(a))\), which is symmetric by Schwarz–Clairaut. Taylor's second-order formula is
\[
f(a+h)=f(a)+Df(a)h+\tfrac12 h^TH_f(a)h+o(\|h\|^2).
\]
The remainder \(o(\|h\|^2)\) follows from continuity of second derivatives. If \(\varphi(t)=f(a+th)\), then \(\varphi''(t)=h^TH_f(a+th)h\).

For \(f(x,y)=e^x\cos y\),
\[
f(0,0)=1,\quad\nabla f(0,0)=(1,0),\quad
H_f(0,0)=\begin{pmatrix}1&0\\0&-1\end{pmatrix},
\]
so \(f(x,y)=1+x+\frac12(x^2-y^2)+o(x^2+y^2)\). For the strict second-derivative test, evaluate the Hessian **at a critical point**; definiteness gives the corresponding strict local extremum and indefiniteness gives a saddle.

##### Exercises with answers

1. Find the Hessian of \(x^2+3xy+2y^2\). **Answer:** \(\begin{pmatrix}2&3\\3&4\end{pmatrix}\).
2. Classify the origin for \(x^2-2y^2\). **Answer:** saddle, because the Hessian has one positive and one negative eigenvalue.
3. Can a zero Hessian classify a critical point? **Answer:** no; compare \(x^4\), \(-x^4\), and \(x^3\) at zero.
4. Why are the cross terms in \(h^THh\) doubled when \(H\) is symmetric? **Answer:** \(H_{ij}h_ih_j\) and \(H_{ji}h_jh_i\) contribute equally for each distinct pair.

##### Sources and further reading

- MIT OpenCourseWare, [18.022 Calculus of Several Variables](https://ocw.mit.edu/courses/18-022-calculus-of-several-variables-fall-2010/pages/syllabus/), second derivatives and Taylor polynomials.
- OpenStax, [Calculus Volume 3](https://openstax.org/books/calculus-volume-3/pages/preface), local extrema.
- [Hessian matrix](https://en.wikipedia.org/wiki/Hessian_matrix); [Taylor's theorem](https://en.wikipedia.org/wiki/Taylor%27s_theorem).

### Maxima, Minima, and Saddle Points in Several Variables

**Track:** Multivariable Calculus from First Principles. **Background:** gradients, Hessians, compactness. **Question:** where can a multivariable function attain its largest or smallest value?

#### Mathematical companion (not spoken)

**Fermat necessary condition.** If \(f\) is differentiable at an interior local extremum \(a\), then \(Df(a)=0\), equivalently \(\nabla f(a)=0\). If \(H_f(a)\) is positive definite, \(a\) is a strict local minimum; negative definite gives strict local maximum; indefinite gives a saddle. Semidefinite Hessians require further analysis.

For \(f(x,y)=x^2+2y^2-2x-4y\),
\[
f=(x-1)^2+2(y-1)^2-3,\quad \nabla f=(2x-2,4y-4),\quad H=\begin{pmatrix}2&0\\0&4\end{pmatrix}.
\]
On \(D=\{x^2+y^2\le1\}\), \(g=x+y\) attains \(\max_D g=\sqrt2\) and \(\min_D g=-\sqrt2\), both on the boundary. Compactness is used to guarantee existence of global extrema, not to identify them.

##### Exercises with answers

1. Classify \((0,0)\) for \(f=x^2+y^2\). **Answer:** strict global minimum.
2. Find the minimum of \((x-2)^2+3(y+1)^2+4\). **Answer:** value four at \((2,-1)\).
3. Maximize \(x\) on the unit disk. **Answer:** maximum one at \((1,0)\).
4. Why is the origin for \(x^4+y^4\) a minimum despite the inconclusive Hessian? **Answer:** both fourth powers are nonnegative and vanish simultaneously only at the origin.

##### Sources and further reading

- MIT OpenCourseWare, [18.02SC Multivariable Calculus](https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/), maxima and minima.
- OpenStax, [Calculus Volume 3](https://openstax.org/books/calculus-volume-3/pages/preface), extrema of several-variable functions.
- [Critical point (mathematics)](https://en.wikipedia.org/wiki/Critical_point_(mathematics)); [Extreme value theorem](https://en.wikipedia.org/wiki/Extreme_value_theorem).

### Lagrange Multipliers: Optimization Along Constraints

**Track:** Multivariable Calculus from First Principles. **Background:** gradients, level sets, constrained geometry. **Question:** how can an extremum occur where the gradient is not zero?

#### Mathematical companion (not spoken)

For one smooth equality constraint \(g(x)=0\), if \(\nabla g(a)\ne0\) and \(f\) has a local constrained extremum at \(a\), then
\[
\nabla f(a)=\lambda\nabla g(a),\qquad g(a)=0.
\]
For constraints \(g_1=\dots=g_k=0\) with linearly independent gradients (rank \(k\)), \(\nabla f=\sum_i\lambda_i\nabla g_i\). Regularity is a substantive hypothesis.

With \(f=x^2+y^2\), \(g=x+y-b\), \(x=y=b/2\), optimal value \(V(b)=b^2/2\), and \(V'(b)=b=\lambda\) under the convention \(\nabla f=\lambda\nabla(x+y-b)\). For the singular constraint \(x^2+y^2=0\), \(\nabla g(0)=0\), so the multiplier necessary condition is inapplicable.

##### Exercises with answers

1. Maximize \(xy\) subject to \(x+y=2\) over real x,y. **Answer:** maximum one at \((1,1)\); there is no minimum because \(x(2-x)\to-\infty\).
2. Find extrema of \(x\) on \(x^2+y^2=4\). **Answer:** maximum two at \((2,0)\), minimum minus two at \((-2,0)\).
3. Why does \(\nabla f=0\) need not hold at a constrained extremum? **Answer:** only derivatives along feasible tangent directions must vanish.
4. Give a singular constraint. **Answer:** \(x^2+y^2=0\) at the origin has vanishing constraint gradient.

##### Sources and further reading

- MIT OpenCourseWare, [18.02SC Multivariable Calculus](https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/), Lagrange multipliers.
- OpenStax, [Calculus Volume 3](https://openstax.org/books/calculus-volume-3/pages/preface), constrained optimization.
- [Lagrange multiplier](https://en.wikipedia.org/wiki/Lagrange_multiplier); [Karush–Kuhn–Tucker conditions](https://en.wikipedia.org/wiki/Karush%E2%80%93Kuhn%E2%80%93Tucker_conditions), an extension to inequality constraints.

### Double and Triple Integrals: Adding Values Across a Region

**Track:** Multivariable Calculus from First Principles. **Background:** one-variable Riemann integrals, areas and volumes. **Question:** how does an integral add contributions over a two- or three-dimensional domain?

#### Mathematical companion (not spoken)

For \(R=[a,b]\times[c,d]\), with tagged partitions \(R=\bigcup R_{ij}\), the Riemann integral is the limit of
\[
\sum_{i,j}f(\xi_{ij},\eta_{ij})\,\Delta x_i\Delta y_j
\]
as mesh size tends to zero, independent of sample choices. For \(f(x,y)=x+2y\) on \([0,1]^2\),
\[
\int_0^1\!\int_0^1(x+2y)\,dx\,dy
=\int_0^1(1/2+2y)\,dy=3/2.
\]
For \(\rho(x,y,z)=1+z\) on \([0,1]^3\), \(\iiint\rho\,dV=3/2\). For a bounded Jordan-measurable region \(D\), integrals over \(D\) can be viewed as integrals of \(f\mathbf 1_D\) over an enclosing rectangle, when that function is Riemann-integrable.

##### Exercises with answers

1. Compute \(\int_{[0,2]\times[0,1]}1\,dA\). **Answer:** two, the area of the rectangle.
2. Compute \(\int_{[0,1]^2}xy\,dA\). **Answer:** one fourth.
3. A cube of side two has constant density three. What is its mass? **Answer:** \(3\cdot 2^3=24\).
4. Why does an integrand of one yield area or volume? **Answer:** each weighted Riemann-sum contribution equals the geometric size of its piece.

##### Sources and further reading

- OpenStax, [Calculus Volume 3](https://openstax.org/books/calculus-volume-3/pages/preface), multiple integration.
- MIT OpenCourseWare, [18.02SC Multivariable Calculus](https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/), double and triple integrals.
- [Multiple integral](https://en.wikipedia.org/wiki/Multiple_integral); [Riemann integral](https://en.wikipedia.org/wiki/Riemann_integral).

### Iterated Integrals: Slicing Regions and Exchanging the Order

**Track:** Multivariable Calculus from First Principles. **Background:** double integrals and one-variable integration. **Question:** when can a two-dimensional integral be computed by integrating one variable at a time?

#### Mathematical companion (not spoken)

Let \(D=\{(x,y):0\le y\le x\le1\}\) and \(f(x,y)=x+y\). Then
\[
\int_0^1\int_0^x(x+y)\,dy\,dx
=\int_0^1\tfrac32 x^2\,dx=\tfrac12,
\]
whereas reversing order gives
\[
\int_0^1\int_y^1(x+y)\,dx\,dy
=\int_0^1\left(\tfrac12+y-\tfrac32y^2\right)dy=\tfrac12.
\]
For the unit ball \(B^3\), the section at height \(z\) has area \(\pi(1-z^2)\); hence
\[
\operatorname{Vol}(B^3)=\int_{-1}^1\pi(1-z^2)\,dz=4\pi/3.
\]
**Conditions:** Tonelli applies to nonnegative measurable functions (extended values are allowed). Fubini applies to integrable functions, for instance \(\int |f|<\infty\). For continuous functions on compact rectangular domains the Riemann versions suffice.

##### Exercises with answers

1. Reverse \(\int_{x=0}^1\int_{y=0}^{x}1\,dy\,dx\). **Answer:** \(\int_{y=0}^1\int_{x=y}^11\,dx\,dy=1/2\).
2. Compute \(\int_0^1\int_0^x xy\,dy\,dx\). **Answer:** \(\int_0^1x^3/2\,dx=1/8\).
3. Find the volume of a ball of radius \(R\) by slicing. **Answer:** \(\int_{-R}^{R}\pi(R^2-z^2)\,dz=4\pi R^3/3\).
4. What hypothesis lets you exchange integrals of a signed measurable function without relying on cancellation? **Answer:** absolute integrability, \(\int |f|<\infty\).

##### Sources and further reading

- OpenStax, [Calculus Volume 3](https://openstax.org/books/calculus-volume-3/pages/preface), iterated integrals and regions.
- MIT OpenCourseWare, [18.02SC Multivariable Calculus](https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/), integration order.
- [Fubini's theorem](https://en.wikipedia.org/wiki/Fubini%27s_theorem); [Tonelli's theorem](https://en.wikipedia.org/wiki/Fubini%27s_theorem#Tonelli's_theorem).

### Polar, Cylindrical, and Spherical Integrals: Coordinates Built for Shape

**Track:** Multivariable Calculus from First Principles. **Background:** double and triple integrals, trigonometry. **Question:** why does polar area contain a factor of radius?

#### Mathematical companion (not spoken)

Polar: \((x,y)=(r\cos\theta,r\sin\theta)\), \(dA=r\,dr\,d\theta\) for \(r\ge0\). Cylindrical: \((x,y,z)=(r\cos\theta,r\sin\theta,z)\), \(dV=r\,dr\,d\theta\,dz\). Spherical (\(\phi\) measured from +z):
\[
(x,y,z)=(\rho\sin\phi\cos\theta,\rho\sin\phi\sin\theta,\rho\cos\phi),
\quad dV=\rho^2\sin\phi\,d\rho\,d\phi\,d\theta.
\]
For \(D=\{x^2+y^2\le1\}\),
\[
\iint_D(x^2+y^2)\,dA
=\int_0^{2\pi}\int_0^1r^3\,dr\,d\theta=\pi/2.
\]
For the unit ball,
\[
\iiint_{B^3}1\,dV=\int_0^{2\pi}\int_0^\pi\int_0^1\rho^2\sin\phi\,d\rho\,d\phi\,d\theta=4\pi/3.
\]
Coordinate maps fail to be one-to-one on edges of a full angular interval and at the coordinate axes; restrict to domains where the map is injective in applying the general theorem, ignoring boundaries of zero measure when justified.

##### Exercises with answers

1. Find the area of a disk of radius \(R\) in polar coordinates. **Answer:** \(\int_0^{2\pi}\int_0^Rr\,dr\,d\theta=\pi R^2\).
2. Find the volume of a cylinder of radius two and height three. **Answer:** \(12\pi\).
3. Compute \(\int_{x^2+y^2\le1}1/(1+x^2+y^2)\,dA\). **Answer:** \(2\pi\int_0^1r/(1+r^2)dr=\pi\log2\).
4. Why is the spherical factor \(\rho^2\sin\phi\) rather than \(\rho^2\) alone? **Answer:** the azimuthal circle has radius \(\rho\sin\phi\), which shrinks near the poles.

##### Sources and further reading

- MIT OpenCourseWare, [18.02SC Multivariable Calculus](https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/), coordinate systems and multiple integrals.
- OpenStax, [Calculus Volume 3](https://openstax.org/books/calculus-volume-3/pages/preface), polar and spherical substitutions.
- [Polar coordinate system](https://en.wikipedia.org/wiki/Polar_coordinate_system); [Spherical coordinate system](https://en.wikipedia.org/wiki/Spherical_coordinate_system).

### The Change-of-Variables Theorem: What the Jacobian Measures

**Track:** Multivariable Calculus from First Principles. **Background:** determinants, Jacobians, multiple integration. **Question:** why must an integral be rescaled after changing coordinates?

#### Mathematical companion (not spoken)

For a \(C^1\) diffeomorphism \(T:U\to V\) between open subsets of \(\mathbb R^n\), and integrable \(f\),
\[
\int_V f(x)\,dx=\int_U f(T(u))\,|\det DT(u)|\,du.
\]
Extensions cover suitable domains up to null boundaries. For \(T(u,v)=(u,(1+u)v)\) on \([0,1]^2\),
\[
DT=\begin{pmatrix}1&0\\v&1+u\end{pmatrix},\quad
\det DT=1+u,\quad
\operatorname{Area}(T([0,1]^2))=\int_0^1\int_0^1(1+u)\,dv\,du=3/2.
\]
For \(T(u,v)=(u+v,u-v)\), \(\det DT=-2\) (oriented scale) and \(|\det DT|=2\) (unsigned area scale). A noninjective parametrization counts with multiplicity unless the domain is appropriately restricted.

##### Exercises with answers

1. Find the area scale of \(T(u,v)=(4u,v/2)\). **Answer:** \(|\det DT|=2\).
2. What is the area of the image of \([0,1]^2\) under \((u,v)\mapsto(u+v,u-v)\)? **Answer:** two.
3. Why is \(\det DT\), not \(|\det DT|\), appropriate for oriented top forms? **Answer:** reversing orientation must reverse the sign of an oriented integral.
4. What happens if polar angle covers \(0\le\theta\le4\pi\) on a disk? **Answer:** almost every physical point is counted twice.

##### Sources and further reading

- MIT OpenCourseWare, [18.022 Calculus of Several Variables](https://ocw.mit.edu/courses/18-022-calculus-of-several-variables-fall-2010/pages/syllabus/), change of coordinates.
- OpenStax, [Calculus Volume 3](https://openstax.org/books/calculus-volume-3/pages/preface), Jacobians and substitutions.
- [Integration by substitution](https://en.wikipedia.org/wiki/Integration_by_substitution); [Jacobian matrix and determinant](https://en.wikipedia.org/wiki/Jacobian_matrix_and_determinant).
