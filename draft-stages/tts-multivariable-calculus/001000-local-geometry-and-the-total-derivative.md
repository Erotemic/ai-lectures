# Local geometry and the total derivative

<!-- BEGIN SPOKEN LECTURE -->

# Local geometry and the total derivative

## Points, Vectors, and Nearness in Several Dimensions

Imagine recording the temperature of a room. A reading at one location depends on where you stand: left versus right, front versus back, floor versus ceiling. Time may add another independent coordinate. A function of several variables assigns an output to an entire collection of inputs, not to one number on a line. Before differentiating such functions we must specify what it means for the input to change only a little.

A point in the plane is an ordered pair, such as three comma four. A point in space has three coordinates. Mathematicians speak of R to the n: lists of n real numbers. The same notation can describe positions, measurements, concentrations, or the settings of n controls. A vector is a change in those coordinates. If we start at the point two comma one and add the displacement one comma minus three, we end at three comma minus two. Keeping points and displacements conceptually separate will become valuable when our points live on a curved surface.

### Distances describe neighborhoods

The familiar distance between two points in the plane comes from Pythagoras. Subtract the corresponding coordinates, square the differences, add, and take the square root. In more dimensions we do the same. This is the Euclidean distance. A ball of radius one around the origin contains the points whose squared coordinates add to less than one. In a plane that ball is the interior of a circle. In three dimensions it is the interior of a sphere.

Why use balls rather than just rectangles? A ball tells us that every component of the displacement is controlled at once. When we say that a vector approaches zero, we mean its distance from zero approaches zero. Equivalently, for a finite list of coordinates, every coordinate tends to zero. One direction cannot quietly remain far away while the others shrink.

There are other sensible measurements of size. We could add the absolute values of all coordinates, or take the largest absolute coordinate. These produce diamond-shaped and square-shaped balls in the plane. The shapes differ, but in a fixed finite dimension all three notions declare exactly the same sequences convergent. For instance, the largest coordinate is no greater than the Euclidean length, and the Euclidean length is no greater than the square root of n times the largest coordinate. The inequalities squeeze one notion of smallness between constant multiples of another.

This fact lets us choose a convenient norm for a calculation. But it does not mean every conceivable way of assigning sizes is equivalent in infinite-dimensional function spaces. That distinction will matter in analysis.

### Open sets, domains, and boundaries

A region is open if every point in it has a small ball lying entirely within the region. The interior of a disk is open; the closed disk, including its boundary circle, is not. A function may be defined only on a restricted domain, such as the points where the denominator of a formula is nonzero. If we write the square root of one minus x squared minus y squared, its real domain is the closed unit disk. At an interior point we can move a little in any direction. At a boundary point, not every movement stays in the domain.

This is why theorems about ordinary derivatives normally assume the function is defined on an open neighborhood. At a boundary we may still study one-sided movements or derivatives along the surface, but the statement has changed. The domain is part of the mathematical object, not an afterthought.

### A path is one way to move, not every way

Take a particle whose location at time t is the point with coordinates t and t squared. As t approaches zero, the particle approaches the origin. Its distance from the origin is the square root of t squared plus t to the fourth. That quantity goes to zero. The path approaches along a parabola, not a straight line.

If a temperature function is continuous at the origin, its readings along this path must approach the reading at the origin. The same is true along a diagonal line, a spiral, or any other path that approaches the point while staying in the domain. But checking one convenient path will never establish continuity in every direction. A function can behave well on both coordinate axes while behaving differently between them.

The right mental picture is not that the point moves along a single line toward a target. It is that every sufficiently small displacement, from every direction and with every mixture of coordinates, must lead to a controlled change in the output. A proof of a multivariable limit must control all such displacements together.

### The first quantitative estimate

Consider the function that squares x and adds y squared. Its value at the origin is zero. At any nearby point its value is exactly the square of the distance to the origin. To make the output smaller than one thousandth, it suffices to keep the input closer than the square root of one thousandth. That is an epsilon–delta argument: for each requested output tolerance, we choose an input tolerance that works for all points in the nearby ball.

We have not yet differentiated or integrated anything. But we have established the common language of both operations: points, displacements, neighborhoods, domains, and uniform control in all directions. A derivative will soon be a linear rule that approximates what happens after a small displacement. An integral will be a limit of sums taken over small regions. Both constructions begin with this geometry of nearness.

## Multivariable Limits: Why Paths Can Deceive

Suppose a scientist reports that a measurement approaches zero whenever one control is reduced to zero while the other is held fixed at zero. That sounds encouraging. But what happens if both controls change together? In two dimensions there are not merely a left approach and a right approach. There are infinitely many straight lines, parabolas, oscillating paths, and mixtures of coordinates. A genuine limit must give the same answer along every approach permitted by the domain.

For a function of two variables, the statement that f approaches L at the origin means this: whatever accuracy we demand for the output, we can find a radius around the origin such that every point of the domain inside that radius, except perhaps the origin itself, has a function value within the demanded accuracy of L. This definition uses all nearby points simultaneously. It does not mention a selected path.

### Use paths to disprove a limit

Consider the fraction with numerator x times y and denominator x squared plus y squared, defined away from the origin. Along the x axis, y is zero, so the fraction is zero. Along the diagonal where y equals x, the numerator is x squared and the denominator is twice x squared, so the fraction equals one half. These two paths reach the same point but produce different limiting values. The two-variable limit does not exist.

A path calculation is a powerful tool for disproof because one counterexample is enough. But path calculations are asymmetric as a method. Agreement along two paths, or ten, does not prove a limit exists. Even agreement along every straight line can fail to reveal what happens along a curved path.

Here is a deliberate trap. Away from the origin, let f be x squared times y divided by x to the fourth plus y squared, and set f at the origin equal to zero. Follow the straight line y equals m times x. For nonzero m, after cancellation the function tends to zero. Along the horizontal axis it is also zero, and along the vertical axis it is zero. Every line through the origin therefore gives the value zero in the limit. But on the parabola y equals x squared, the fraction becomes x to the fourth divided by twice x to the fourth: exactly one half for every nonzero x. The function is not continuous at the origin. Straight-line tests were insufficient.

That example is important whenever a derivative is checked only along coordinate directions. The behavior may be stable in each of those directions while the combined geometry is still badly behaved.

### To prove a limit, find one bound for all directions

Now examine x squared times y divided by x squared plus y squared, again defining the value at the origin to be zero. We could try many lines, but a direct estimate is stronger. The absolute value of x squared divided by x squared plus y squared is no greater than one. Therefore the absolute value of the entire fraction is no greater than the absolute value of y, which is no greater than the distance to the origin. So the function value approaches zero along every path at once.

This is the central technique of multivariable limits: replace a complicated expression with a simpler quantity that depends only on distance to the target. If the bound tends to zero with the radius, we are finished.

Polar coordinates often make the same idea visible. Write x as radius times cosine and y as radius times sine. The angle tells us the direction, and the radius tells us how close we are. For the well-behaved fraction, a factor of radius remains and the angular factor stays bounded. The radial factor forces the limit to zero. For the bad fraction with numerator x y, no radial factor remains: the answer still depends on the direction. Polar coordinates are an aid to uniform estimates, not a substitute for them.

### Continuity and composition

A function is continuous at a point when its limit there equals its defined value. Polynomials in several coordinates are continuous everywhere. Rational expressions are continuous wherever their denominators are nonzero. The usual algebra of continuous functions still works because addition, multiplication, and division where permitted respect limits.

For a more geometric statement, let a moving point follow a continuous curve, and feed that point into a continuous temperature field. The resulting temperature as a function of time is continuous. This is composition: a continuous path through a continuous field cannot produce a jump. Conversely, if a field has a genuine two-variable limit at a point, every path approaching that point through other points of the domain inherits the same limit. If a path repeatedly visits the target itself, continuity of the field at the target is needed for that conclusion.

This last implication is a one-way test. We have already seen why testing a limited family of paths cannot establish the field's continuity. The full definition remains the referee.

### Why the distinction matters later

The definition of differentiability will demand something even stronger than continuity. It will require that the error after subtracting a proposed linear approximation becomes small compared with the total distance moved. A calculation along one coordinate axis may suggest the linear approximation, but only a bound on all small displacements can prove it is correct.

The lesson is operational. When your goal is to refute a limit, find two paths with incompatible behavior. When your goal is to prove a limit, construct a uniform estimate that does not rely on choosing a path. That difference is the first genuinely new habit of thought in calculus of several variables.

## Partial and Directional Derivatives: The Information They Miss

A function of two variables can change when we move east, when we move north, or when we move diagonally. We might begin by measuring the eastward slope and the northward slope separately. Those are partial derivatives. They are often easy to compute, but the important question is whether they tell the whole story.

For a function f of x and y, the partial derivative with respect to x fixes y and takes an ordinary one-variable derivative. The partial derivative with respect to y fixes x instead. On the surface whose height is x squared plus three times y squared, the x partial derivative is two x and the y partial derivative is six y. At one comma one, a small step to the right changes the height at a rate of two per unit distance; a step upward in the y direction changes it at rate six.

A directional derivative asks about a prescribed vector v, not just a coordinate axis. We look at f of a plus t times v, subtract f of a, and divide by t as t approaches zero. The vector v describes the displacement for one unit of t. If v is twice as long, the rate is twice as large when the derivative behaves linearly. Unit vectors are used when comparing rates per unit distance.

### What the familiar formula predicts

For a smooth surface, the directional derivative in direction v equals the x partial derivative times the x component of v, plus the y partial derivative times the y component. In the quadratic example, at one comma one the directional rate along the vector three comma four is two times three plus six times four, which is thirty. Along the unit direction three fifths comma four fifths, the rate per unit distance is six.

This formula is extremely useful. But its hypothesis matters. It follows from the existence of a full linear derivative; it does not follow merely from the separate existence of the two partial derivatives at a point.

### A function with every directional derivative but no linear derivative

Define a function away from the origin by x cubed divided by x squared plus y squared, and define its value at the origin as zero. It is continuous at zero: the absolute value is no greater than the distance to zero. Its partial derivative along the x axis at zero is one; along the y axis it is zero.

What about the diagonal direction one comma one? At the point t comma t the function equals t divided by two. Divide by t and the directional derivative is one half. Yet the formula predicted by the two partial derivatives would give one times one plus zero times one, or one. The measured rate is one half, not one.

In fact, every directional derivative exists at the origin for this function, but the dependence on direction is not linear. This is the obstruction. A total derivative must be a single linear map that simultaneously predicts the change for every small displacement. Direction-by-direction limits can fail to assemble into that map.

There is a second caution. Suppose a function has partial derivatives at the origin. It need not even be continuous there. Consider the fraction x squared times y divided by x to the fourth plus y squared, with value zero at the origin. Both coordinate-axis partial derivatives at the origin are zero. Yet along y equals x squared, the function is one half rather than something tending to zero. A measurement along each axis has missed a discontinuity between them.

### A sufficient condition that repairs the gap

Here is a theorem worth remembering. If all the first partial derivatives exist on an open neighborhood of the point and are continuous at the point, then the function is differentiable there. In particular, if the partial derivatives are continuous throughout a neighborhood, they produce a full linear approximation at each point of that neighborhood. The key is not simply the existence of slopes, but their controlled behavior as the base point moves.

Why is continuity of partial derivatives helpful? Move from x comma y to x plus h comma y plus k in two stages: first change x, then change y. Apply the one-variable mean value theorem to each stage. The coefficients are partial derivatives at nearby points. As h and k shrink, continuity makes those coefficients approach the partial derivatives at the original point. The error is small compared with the total displacement.

That proof strategy already explains why the theorem is stronger than the bare existence of partial derivatives at one isolated point. To control an error after moving, we need information at nearby points.

### A practical diagnostic

When given a formula that is smooth wherever its denominator is nonzero, ordinary differentiation rules are enough away from singularities. At a suspect point, however, distinguish four questions. Does the function have a limit? Is it continuous? Do the coordinate partial derivatives exist? Is it fully differentiable? These questions are related, but none of the weaker facts should be silently promoted into a stronger one.

Directional derivatives are valuable physical measurements, and partial derivatives are the coordinate entries of the true derivative when it exists. Their limitations lead us to the central object of multivariable calculus: a linear approximation controlled by the total size of the displacement, not just by selected directions.

## The Total Derivative: One Linear Map for Every Small Change

In one-variable calculus, saying a function is differentiable at a point means that a line predicts its change with an error negligible compared with the distance moved. We want exactly the same idea for multiple inputs. The difference is that the best first-order predictor is no longer just multiplication by one slope. It is a linear map applied to a displacement vector.

Suppose f takes two real inputs and returns one number. At a point a, write h for a small displacement. We seek a linear rule L of h such that f at a plus h equals f at a plus L of h, with an error that becomes small compared with the length of h. That last comparison is the definition. It quantifies the word tangent. We are not satisfied with a plane that happens to match a few chosen directions; the approximation must work uniformly as h approaches zero from anywhere.

### Build the approximation in a concrete example

Let f of x and y be x squared times y plus the sine of x y. Start at the point one comma zero. The function value is zero. The x partial derivative is two x y plus y times cosine of x y. At one comma zero this equals zero. The y partial derivative is x squared plus x times cosine of x y, which equals two there.

The proposed first-order prediction is therefore that changing x by h and y by k changes f by approximately two k. The x displacement contributes nothing at first order at this particular base point. That does not mean x is irrelevant in general. It means its influence is small compared with the total displacement at this point when y is close to zero.

Write the exact value at one plus h comma k. It is the square of one plus h times k, plus sine of one plus h times k. The coefficient of k in the linear part is two. All remaining terms contain at least a product of two small quantities or a higher-order sine error. After dividing their sum by the distance of the displacement from zero, the result tends to zero. This verifies the linear approximation rather than merely guessing it from partial derivatives.

In the graph of z equals f of x comma y, the equation z equals two times y near one comma zero is the tangent plane, adjusted to pass through the original graph point. The plane is the graph of the linearized change plus the original height.

### The Jacobian is a matrix representation, not a different object

Now let F send an input vector with n coordinates to an output vector with m coordinates. Its derivative, when it exists, is a linear map from input displacements to output displacements. In chosen standard coordinates we represent that map by an m-by-n matrix. Entry number i comma j is the partial derivative of output component i with respect to input coordinate j. This is the Jacobian matrix.

For example, let F of x comma y be the pair whose first component is x y and whose second component is x plus y squared. At one comma two, the first row of the Jacobian is two comma one. The second row is one comma four. For a small displacement h comma k, the predicted output change is two h plus k in the first component and h plus four k in the second. There is no need to invent a separate approximation for each displacement: one matrix handles all of them.

The derivative depends on the base point. The matrix changes as we move through the domain. The displacement vector is the input to the linear map, not the location of the base point itself. Mixing these roles causes many errors in geometry and differential equations.

### Why the error is measured relative to distance

Any continuous function has the property that its output error tends to zero. Differentiability demands something more exacting. The error after subtracting the linear part must shrink faster than the displacement itself. If the displacement length is one thousandth, an error of one thousandth is not necessarily good enough; the ratio of error to displacement must tend to zero as we keep shrinking.

This distinguishes first-order approximation from mere continuity. It also explains why derivatives are so useful for sensitivity analysis. When the input perturbation is small, the linear term captures the leading change, and the remaining error has lower relative importance.

### Uniqueness and connection to covectors

Could two different linear maps both satisfy the definition? No. Their difference would have to be negligible compared with every sufficiently small displacement. Fix a direction and scale it down. Because linear maps scale exactly with the displacement, their difference in that direction could not vanish faster than the displacement unless it were zero. Repeating for every direction shows the maps are equal.

For a real-valued function, the total derivative is a linear functional on displacement vectors: a covector. In Euclidean coordinates we represent it by the row of partial derivatives, or equivalently by its associated gradient vector using the dot product. Later, on a manifold, the covector remains meaningful even when there is no preferred notion of gradient until we choose a metric.

The central payoff is a change of perspective. A derivative is not fundamentally a table of partial derivatives. It is one best linear approximation, with an error condition that tests all directions simultaneously. The table of partial derivatives is how we write that map in coordinates.

## The Multivariable Chain Rule: Composing Local Linear Maps

A system can transform inputs through several stages. A robotic arm converts joint angles into a position. A temperature field converts that position into a temperature. To determine how a small change in the joint angles affects the measured temperature, we must combine the sensitivity of the position to the angles with the sensitivity of temperature to position. This is the multivariable chain rule.

Its familiar one-variable cousin says that the derivative of a composition is the product of the two derivatives. In several variables the principle is identical, but the derivatives are linear maps and their product is matrix composition. The order matters.

### Follow a displacement through two maps

Let F take an input with n coordinates to an intermediate output with m coordinates, and let G take that intermediate point to a final output with p coordinates. Near a starting point a, F transforms a small displacement h approximately into the matrix J of F at a, multiplied by h. The second map G transforms that intermediate change approximately into its own Jacobian matrix multiplied by the change. Thus the total first-order effect is the Jacobian of G at F of a, multiplied by the Jacobian of F at a, and then multiplied by h.

Notice where each derivative is evaluated. The derivative of F is evaluated at the original input a. The derivative of G is evaluated at the intermediate point F of a. Putting both derivatives at a would not generally even make sense, because the input and intermediate spaces may have different dimensions.

A useful memory aid is to read the composition from right to left. We do F first and G second. Their derivative matrices multiply in the same functional order: derivative of G times derivative of F.

### A complete example

Let F of x and y return the pair u equals x times y and v equals x plus y. Let G of u and v be u squared plus three times v. Then the complete function is x squared times y squared plus three x plus three y.

Differentiate it directly. The x partial derivative is two x times y squared plus three. The y partial derivative is two x squared times y plus three. Now do it as a composition. The Jacobian of F has first row y comma x and second row one comma one. The derivative of G is the row two u comma three. Multiplying the row by the matrix produces two u times y plus three, and two u times x plus three. Substitute u equals x y and the results match the direct calculation exactly.

This equality is a check on both methods. More importantly, it proves we can compute derivatives modularly. A large computation can be organized as many small stages, exactly as in automatic differentiation.

### Paths through a field

Consider a curve r of time describing a moving point in space, and a scalar field T giving temperature at each position. The composition T of r gives temperature as a function of time. Its rate of change is the gradient of T at the moving position dotted with the velocity r prime. If the velocity lies along a level surface of T, this rate is zero. If it has a component toward warmer regions, the rate can be positive.

Take T of x and y equal to x squared plus y squared, and r of t equal to cosine t comma sine t. The particle travels around the unit circle. Its temperature is identically one, so its time derivative is zero. The gradient is the vector two cosine t comma two sine t. The velocity is minus sine t comma cosine t. Their dot product is zero. The algebra reflects the geometry: movement tangent to a circle of constant radius does not change the radius squared.

This example also reveals that a vector field and a path have different roles. The gradient is a property of the scalar field at each location; velocity is a property of how the particle moves through those locations.

### Why the error stays small

The chain rule is not only a trick for multiplying partial derivatives. It follows from the definition of differentiability. The first map produces a linear change plus an error negligible compared with the original displacement. The second map produces another linear change plus an error negligible compared with the intermediate displacement. Since a differentiable first map changes distances by at most a constant times the original small displacement, the composed error is still negligible compared with that original displacement.

This reasoning is why the theorem requires differentiability, not merely a collection of directional derivatives. Without a genuine linear approximation for each stage, there is no justification for composing linear approximations.

### A word about changing coordinates

Suppose we use new coordinates u and v to describe the same points previously described by x and y. The physical function has not changed, but its coordinate expression has. The Jacobian of the coordinate map tells us how small steps in u and v alter x and y. The chain rule converts derivatives between these descriptions.

Later in geometry, a tangent vector will transform by the Jacobian of the coordinate change, while a covector transforms in the dual manner. The distinction is not a convention to memorize; it comes from insisting that the change in an actual scalar quantity be the same whether calculated in the old coordinates or the new ones.

The chain rule is therefore a statement about the compatibility of local linear models. It lets small calculations be composed into large ones and is a central reason derivatives are useful beyond elementary calculus.

## Gradients, Level Sets, and Tangent Directions

A topographic map gives elevation along contour lines. Every point on one contour has the same height. If a hiker moves along that contour, their elevation does not change to first order. If the hiker turns across the contours, their elevation changes. A single vector at each point encodes these rates: the gradient.

For a differentiable scalar function in ordinary Euclidean coordinates, the gradient is the vector of all first partial derivatives. If the function is the altitude f of x comma y, the gradient has components f sub x and f sub y. Its dot product with a displacement predicts the change in altitude. The gradient is not merely an arrow chosen by inspection; it is the vector that represents the derivative covector using the Euclidean inner product.

### Compute a contour and its normal

Take f of x and y equal to x squared plus four y squared. The level sets are ellipses. At the point one comma one, the value is five. The gradient is two comma eight. For a small displacement h comma k, the first-order change is two h plus eight k.

If we want a direction tangent to the ellipse at this point, choose a vector perpendicular to the gradient, such as four comma minus one. The dot product is eight minus eight, or zero. Thus moving a little in that direction produces no first-order change in f. The curve will still bend, so moving along the straight tangent line a finite distance does not remain exactly on the ellipse. The statement is local and first order.

More generally, suppose a smooth curve r of t lies in the level set f equals c. The composition f of r is the constant c. Differentiate: the gradient of f dotted with the curve's velocity is zero. Every velocity tangent to the level set is orthogonal to the gradient. At a regular point, where the gradient is nonzero, the level set is locally a smooth curve in two dimensions or a smooth hypersurface in higher dimensions, and the gradient is a nonzero normal vector.

At a critical point, where the gradient vanishes, this conclusion needs qualification. The set could cross itself or have a cusp or singular point. The equation f equals zero for f of x and y equal to x squared minus y squared, for example, describes two crossing lines through the origin; the gradient vanishes there and cannot choose a unique normal.

### The direction of steepest increase

What direction produces the fastest increase in the function for a unit step? The directional derivative along a unit vector v equals the gradient dotted with v. By the Cauchy–Schwarz inequality, that dot product is at most the length of the gradient. When the gradient is nonzero, equality occurs if v points in the same direction as the gradient. The opposite direction produces the steepest decrease.

In our ellipse example the gradient two comma eight has length the square root of sixty-eight. A unit step along that normalized vector produces the maximum first-order increase, with rate square root of sixty-eight. A unit step along the normalized tangent produces rate zero.

This statement assumes distance is measured with the ordinary Euclidean inner product. Change the metric, and the meaning of a unit step changes; the representing gradient changes too. The derivative as a covector does not need a metric. This is why Riemannian geometry distinguishes differential of a function from gradient of the function.

### Gradient flow

Suppose a particle moves according to the differential equation position prime equals minus the gradient of f. Along a differentiable solution, the chain rule gives the rate of change of f as minus the squared length of the gradient. Thus f never increases. This is gradient descent as a continuous-time dynamical system.

For f of x and y equal to one half times x squared plus one half times four y squared, the negative gradient flow satisfies x prime equals minus x and y prime equals minus four y. Its solutions are x of t equals initial x times exponential minus t, and y of t equals initial y times exponential minus four t. Both coordinates decay, but the y coordinate decays four times as fast in the exponent. The ellipses tell us the energy levels; the gradient tells us how the flow crosses them.

There is a subtlety: an actual discrete gradient-descent step can overshoot if it is too large. The continuous-time identity does not prove that every finite numerical step decreases the function. Optimization theory studies conditions on step size, curvature and smoothness to control that issue.

### The same idea in three dimensions

Imagine a scalar field T of x, y and z representing temperature. A level surface consists of points with the same temperature. If the gradient is nonzero, it is normal to that surface. A fluid particle with velocity v experiences temperature change at the rate gradient T dot v, in a time-independent field. If the temperature field itself changes with time, an additional time partial derivative appears. Keeping the particle's motion separate from the field's own evolution is essential in fluid mechanics.

The gradient converts local scalar variation into geometry. Its direction comes from an inner product; its orthogonality to level sets comes from the chain rule; and its role in optimization comes from the inequality relating dot products to vector lengths.

## Inverse and Implicit Functions: Solving Nearby Equations

The algebra of two equations in two unknowns is straightforward when the equations are linear. For nonlinear equations, even writing down an explicit inverse can be impossible. Yet we often need only a local answer: if the data change slightly, is there one nearby solution, and how quickly does that solution move? The inverse and implicit function theorems answer this question through the derivative matrix.

Begin with an invertible linear map. If u equals x plus y and v equals x minus y, the inverse gives x as one half of u plus v and y as one half of u minus v. The Jacobian has rows one comma one and one comma minus one. Its determinant is minus two, which is nonzero. A small change in the output determines a unique small change in the input.

A nonlinear map is approximately linear near a differentiable point. If its derivative matrix is invertible there, the inverse function theorem says the map is locally invertible, provided the derivative behaves continuously in a neighborhood. The inverse is differentiable, and its derivative is the matrix inverse of the original Jacobian, evaluated at the corresponding point.

### A map that has local but not global inverses

Consider the transformation from polar-like coordinates s and t to plane coordinates x equals exponential s times cosine t, and y equals exponential s times sine t. Its Jacobian determinant is exponential of twice s, always positive. Therefore near every input point, a small output change can be inverted uniquely. But t and t plus two pi produce the same output. There is no one-to-one global inverse on the entire s–t plane. Nonzero determinant guarantees local invertibility, not global uniqueness.

This distinction is important whenever coordinates wrap around a circle, overlap, or omit a point. A perfectly valid local coordinate chart may fail to cover a whole manifold or may repeat points beyond its chosen domain.

### Solve one variable as a function of another

Now consider the unit circle, whose equation is x squared plus y squared equals one. We can write this as F of x and y equals zero, where F is x squared plus y squared minus one. Near the point zero comma one, there is a unique branch of the circle with y near one. It can be described as y as a smooth function of x. We could solve explicitly using the positive square root of one minus x squared, but the implicit function theorem works without such a formula.

The key condition is that the partial derivative of F with respect to the variable we want to solve for, here y, is nonzero. At zero comma one, that derivative is two. We can therefore differentiate the equation F of x comma y of x equals zero. The chain rule gives F sub x plus F sub y times y prime equals zero. Solve to obtain y prime equals negative F sub x divided by F sub y. For the circle this becomes negative x divided by y. At the top of the circle the derivative is zero, so the tangent is horizontal.

At the point one comma zero, F sub y is zero. We cannot solve locally for y as a smooth function of x near that point in the same way. The circle has a vertical tangent; nearby values of x less than one correspond to two values of y, one positive and one negative. Yet F sub x is nonzero there, so we can instead solve for x as a smooth function of y. The failure concerns the chosen variable, not smoothness of the circle itself.

### General systems and the block Jacobian

For several equations F of x comma y equals zero, where y represents the unknowns we wish to solve and x represents parameters, the derivative with respect to y is a square matrix. If that matrix is invertible, the implicit function theorem gives a local solution y of x. Its derivative is minus the inverse of the y-Jacobian times the x-Jacobian. The dimensions make the formula readable: it converts a change of parameters into the corresponding change of the solved variables.

This provides a sensitivity calculation even if no explicit nonlinear solution formula is available. A parameter may be a temperature, a measurement or an applied force. The theorem tells us how the nearby equilibrium responds, as long as the relevant linearization is invertible.

### Why invertibility matters

If the linearized map loses rank, nearby solutions can branch, disappear, or change multiplicity. The scalar equation y squared equals x illustrates the issue at the origin. For x positive it has two nearby values of y. For x negative it has no real solution. The derivative with respect to y is zero at the origin. A smooth unique branch through that point is not guaranteed.

Failure of the hypothesis does not prove that a solution is impossible. It means the theorem cannot certify a smooth local inverse. One must analyze the particular equation by other means.

The inverse and implicit function theorems connect linear algebra to nonlinear geometry. They explain why invertible Jacobians permit local coordinates, why regular level sets are smooth, and why a constraint can often be solved for some variables without writing them down explicitly.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Points, Vectors, and Nearness in Several Dimensions

**Track:** Multivariable Calculus from First Principles. **Background:** one-variable calculus and basic vectors. **Question:** what must be meant by “near a point” when there are many ways to approach it?

#### Mathematical companion (not spoken)

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

##### Exercises with answers

1. Show \((t,t^2)\to(0,0)\). **Answer:** \(\|(t,t^2)\|_2=|t|\sqrt{1+t^2}\to0\).
2. Describe the unit ball in the maximum norm. **Answer:** the open square \((-1,1)\times(-1,1)\).
3. Find the domain of \(1/(x^2+y^2-1)\). **Answer:** all of \(\mathbb R^2\) except the unit circle.
4. Prove coordinatewise convergence implies Euclidean convergence for fixed \(n\). **Answer:** if each of finitely many squared differences tends to zero, so does their sum and its square root.

##### Sources and further reading

- OpenStax, [Calculus Volume 3](https://openstax.org/books/calculus-volume-3/pages/preface), vectors and functions of several variables.
- MIT OpenCourseWare, [18.022 Calculus of Several Variables](https://ocw.mit.edu/courses/18-022-calculus-of-several-variables-fall-2010/pages/syllabus/), the metric and geometric viewpoint.
- [Euclidean space](https://en.wikipedia.org/wiki/Euclidean_space); [Norm (mathematics)](https://en.wikipedia.org/wiki/Norm_(mathematics)).

### Multivariable Limits: Why Paths Can Deceive

**Track:** Multivariable Calculus from First Principles. **Background:** neighborhoods, one-variable limits. **Question:** how can we prove a limit when infinitely many paths approach a point?

#### Mathematical companion (not spoken)

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

##### Exercises with answers

1. Does \(x^2/(x^2+y^2)\) have a limit at the origin? **Answer:** no; the x axis gives one and y axis zero.
2. Show \(xy^2/(x^2+y^2)\to0\). **Answer:** its absolute value is at most \(|x|\) because \(y^2/(x^2+y^2)\le1\).
3. Why is continuity of \(f\) at \(a\) enough to ensure \(f(\gamma(t))\to f(a)\) when \(\gamma(t)\to a\)? **Answer:** apply the epsilon–delta definition to \(\gamma(t)\).
4. What does failure along two curves establish? **Answer:** the multivariable limit cannot exist when their limiting values differ.

##### Sources and further reading

- OpenStax, [Calculus Volume 3](https://openstax.org/books/calculus-volume-3/pages/preface), functions and limits.
- MIT OpenCourseWare, [18.022 Calculus of Several Variables](https://ocw.mit.edu/courses/18-022-calculus-of-several-variables-fall-2010/pages/syllabus/), limits in several dimensions.
- [Limit of a function](https://en.wikipedia.org/wiki/Limit_of_a_function); [Continuous function](https://en.wikipedia.org/wiki/Continuous_function).

### Partial and Directional Derivatives: The Information They Miss

**Track:** Multivariable Calculus from First Principles. **Background:** one-variable derivatives and multivariable limits. **Question:** when do slopes measured along lines describe a true local linear map?

#### Mathematical companion (not spoken)

For \(v\in\mathbb R^n\), the two-sided directional derivative, when it exists, is
\[
D_vf(a)=\lim_{t\to0}\frac{f(a+tv)-f(a)}{t}.
\]
If \(f\) is differentiable at \(a\), then \(D_vf(a)=Df(a)v=\sum_i\partial_i f(a)v_i\). The converse fails. Define
\[
f(x,y)=\begin{cases}x^3/(x^2+y^2), &(x,y)\ne(0,0),\\0,&(x,y)=(0,0).
\end{cases}
\]
Then \(D_{(a,b)}f(0)=a^3/(a^2+b^2)\) for \((a,b)\ne0\), which is not linear in \((a,b)\). Along \((1,1)\) it equals \(1/2\), whereas the linear map predicted from partials \((1,0)\) would equal one. The function is continuous because \(|f(x,y)|\le |x|\le\sqrt{x^2+y^2}\).

**Sufficient criterion:** first-order partial derivatives existing in a neighborhood of \(a\) and continuous at \(a\) imply differentiability at \(a\). For vector-valued functions apply componentwise.

##### Exercises with answers

1. Compute \(\partial_x,\partial_y\) of \(x^2+3y^2\) at \((1,1)\). **Answer:** \((2,6)\).
2. Find the directional rate along \((3/5,4/5)\). **Answer:** \(2(3/5)+6(4/5)=6\).
3. For the counterexample above, compute \(D_{(0,1)}f(0)\). **Answer:** zero.
4. Can a discontinuous function be differentiable? **Answer:** not at that point; differentiability implies continuity.

##### Sources and further reading

- MIT OpenCourseWare, [18.02SC Multivariable Calculus](https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/), partial and directional derivatives.
- OpenStax, [Calculus Volume 3](https://openstax.org/books/calculus-volume-3/pages/preface), differentiability.
- [Partial derivative](https://en.wikipedia.org/wiki/Partial_derivative); [Directional derivative](https://en.wikipedia.org/wiki/Directional_derivative).

### The Total Derivative: One Linear Map for Every Small Change

**Track:** Multivariable Calculus from First Principles. **Background:** partial derivatives and linear maps. **Question:** what makes a tangent plane a genuine approximation rather than a sketch?

#### Mathematical companion (not spoken)

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

##### Exercises with answers

1. Find the total derivative of \(f(x,y)=3x-2y\). **Answer:** the constant row \((3,-2)\) and zero remainder.
2. Find the tangent plane to \(z=x^2+y^2\) above \((1,2)\). **Answer:** \(z=5+2(x-1)+4(y-2)\).
3. Linearize \(F(x,y)=(xy,x+y^2)\) at \((1,2)\) for displacement \((0.01,-0.02)\). **Answer:** predicted change \((0, -0.07)\).
4. Why is the derivative unique? **Answer:** if \(A,B\) work, apply the difference quotient to \(h=tv\); \(\|(A-B)v\|=0\) for every \(v\).

##### Sources and further reading

- MIT OpenCourseWare, [18.022 Calculus of Several Variables](https://ocw.mit.edu/courses/18-022-calculus-of-several-variables-fall-2010/pages/syllabus/), the derivative and its matrix.
- OpenStax, [Calculus Volume 3](https://openstax.org/books/calculus-volume-3/pages/preface), linear approximation and tangent planes.
- [Fréchet derivative](https://en.wikipedia.org/wiki/Fr%C3%A9chet_derivative); [Jacobian matrix and determinant](https://en.wikipedia.org/wiki/Jacobian_matrix_and_determinant).

### The Multivariable Chain Rule: Composing Local Linear Maps

**Track:** Multivariable Calculus from First Principles. **Background:** the total derivative and matrix multiplication. **Question:** how does a change of variables affect a derivative?

#### Mathematical companion (not spoken)

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

##### Exercises with answers

1. For \(F(x,y)=(x+y,x-y)\), \(G(u,v)=u^2+v^2\), compute \(\nabla(G\circ F)\). **Answer:** \((4x,4y)\), since \(G\circ F=2x^2+2y^2\).
2. Differentiate \(T(r(t))\) for \(T(x,y)=xy\), \(r(t)=(t,t^2)\). **Answer:** \(3t^2\).
3. Why do Jacobian matrices multiply rather than add? **Answer:** the second linear map acts on the displacement produced by the first.
4. Can the outer derivative be evaluated at the original input if \(n\ne m\)? **Answer:** not generally; it belongs at the intermediate point \(F(a)\).

##### Sources and further reading

- MIT OpenCourseWare, [18.02SC Multivariable Calculus](https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/), chain rule.
- OpenStax, [Calculus Volume 3](https://openstax.org/books/calculus-volume-3/pages/preface), multivariable differentiation.
- [Chain rule](https://en.wikipedia.org/wiki/Chain_rule); [Automatic differentiation](https://en.wikipedia.org/wiki/Automatic_differentiation).

### Gradients, Level Sets, and Tangent Directions

**Track:** Multivariable Calculus from First Principles. **Background:** linear approximation, directional derivatives, inner products. **Question:** why does a gradient point perpendicular to a contour, and what exactly does that mean?

#### Mathematical companion (not spoken)

For \(f:\mathbb R^n\to\mathbb R\), \(Df(a)h=\nabla f(a)\cdot h\) in Euclidean coordinates. If \(r(t)\) lies in \(\{x:f(x)=c\}\), then
\[
0=\frac{d}{dt}f(r(t))=\nabla f(r(t))\cdot r'(t).
\]
At regular points \(\nabla f\ne0\), the level set is a hypersurface, with tangent space \(\ker Df(a)\). For \(\|v\|_2=1\), \(D_vf(a)\le\|\nabla f(a)\|_2\), equality at \(v=\nabla f/\|\nabla f\|\).

For \(f=x^2+4y^2\) at \((1,1)\), \(\nabla f=(2,8)\) and tangent direction \((4,-1)\). Gradient flow for \(E=(x^2+4y^2)/2\) satisfies \(\dot x=-x,\dot y=-4y\) and \(dE/dt=-\|\nabla E\|^2\).

##### Exercises with answers

1. Give a tangent vector to \(x^2+9y^2=10\) at \((1,1)\). **Answer:** \((9,-1)\), since \((2,18)\cdot(9,-1)=0\).
2. Find the maximum directional derivative of \(f=x+2y\). **Answer:** \(\sqrt5\), attained along \((1,2)/\sqrt5\).
3. Why does a vanishing gradient make normal-vector arguments inconclusive? **Answer:** the zero vector has no distinguished direction and the level set need not be regular.
4. Find \(dE/dt\) for \(\dot r=-\nabla E\). **Answer:** \(-\|\nabla E\|^2\le0\).

##### Sources and further reading

- MIT OpenCourseWare, [18.02SC Multivariable Calculus](https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/), gradients and directional derivatives.
- OpenStax, [Calculus Volume 3](https://openstax.org/books/calculus-volume-3/pages/preface), gradients and level surfaces.
- [Gradient](https://en.wikipedia.org/wiki/Gradient); [Level set](https://en.wikipedia.org/wiki/Level_set).

### Inverse and Implicit Functions: Solving Nearby Equations

**Track:** Multivariable Calculus from First Principles. **Background:** Jacobians, matrix inverses, chain rule. **Question:** when can we solve equations for variables without an explicit formula?

#### Mathematical companion (not spoken)

**Inverse function theorem.** If \(F:U\subset\mathbb R^n\to\mathbb R^n\) is \(C^1\) and \(\det DF(a)\ne0\), there exist neighborhoods of \(a\) and \(F(a)\) on which \(F\) is a \(C^1\) diffeomorphism, with
\[
D(F^{-1})(F(a))=[DF(a)]^{-1}.
\]
**Implicit function theorem.** If \(F:U\subset\mathbb R^p\times\mathbb R^q\to\mathbb R^q\) is \(C^1\), \(F(a,b)=0\), and \(D_yF(a,b)\) is invertible, then locally \(y=\phi(x)\) and
\[
D\phi(x)=-[D_yF(x,\phi(x))]^{-1}D_xF(x,\phi(x)).
\]
On \(x^2+y^2=1\) with \(y\ne0\), \(dy/dx=-x/y\). The map \((s,t)\mapsto(e^s\cos t,e^s\sin t)\) has determinant \(e^{2s}\) but is globally periodic in \(t\).

##### Exercises with answers

1. For \(F(x,y)=(x+y,x-y)\), compute \(DF^{-1}\). **Answer:** \(\frac12\begin{pmatrix}1&1\\1&-1\end{pmatrix}\).
2. Implicitly differentiate \(x^2+xy+y^2=3\) where \(x+2y\ne0\). **Answer:** \(y'=-(2x+y)/(x+2y)\).
3. At \((1,0)\) on the circle, which variable is locally a function of the other? **Answer:** \(x\) is locally a smooth function of \(y\).
4. Does nonzero Jacobian determinant imply global injectivity? **Answer:** no; the exponential polar map repeats after one full turn.

##### Sources and further reading

- MIT OpenCourseWare, [18.022 Calculus of Several Variables](https://ocw.mit.edu/courses/18-022-calculus-of-several-variables-fall-2010/pages/syllabus/), implicit functions.
- OpenStax, [Calculus Volume 3](https://openstax.org/books/calculus-volume-3/pages/preface), derivatives and applications.
- [Inverse function theorem](https://en.wikipedia.org/wiki/Inverse_function_theorem); [Implicit function theorem](https://en.wikipedia.org/wiki/Implicit_function_theorem).
