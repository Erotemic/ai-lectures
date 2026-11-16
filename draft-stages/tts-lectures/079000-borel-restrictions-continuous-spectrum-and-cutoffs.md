# Borel restrictions, continuous spectrum, and cutoffs

<!-- BEGIN SPOKEN LECTURE -->

# Borel restrictions, continuous spectrum, and cutoffs

## Bounded Borel functional calculus

A diagonal matrix can be transformed by applying a function to its eigenvalues. If the function is continuous, the finite-dimensional rule has a direct bounded-operator analogue. But spectral projections require indicator functions, and indicators of intervals are generally discontinuous.

Consider again the multiplication operator A on square-integrable functions of t between zero and one. Applying the function that equals one on the lower half of the interval and zero elsewhere produces the orthogonal projection that keeps the lower-half support. It is a perfectly good bounded operator, even though the indicator function has a jump at one half.

A Borel set is any set generated from open real sets using complements and countable unions. A bounded Borel function is a bounded function whose inverse images of open sets are Borel. The bounded Borel functional calculus extends continuous calculus to these functions through spectral integration. Its outputs preserve multiplication and adjoints, and bounded pointwise convergence of functions leads to strong operator convergence under the appropriate dominated-convergence mechanism. Uniform convergence of scalar functions is a stronger hypothesis and yields operator-norm convergence.

We will develop the simple-function approximation, identify how projection-valued measures enter, and keep the distinction between strong and norm convergence visible throughout.

### Begin with simple functions

A simple function takes finitely many values. Write it as a sum of scalar coefficients times indicators of pairwise disjoint Borel sets.

For each indicator of B, use the spectral projection E of B. This means the orthogonal projection onto the portion of the Hilbert space whose spectral values belong to B. Such projections are supplied by the spectral theorem for a bounded self-adjoint operator A. Define the operator assigned to the simple function as the corresponding finite linear combination of these projections.

We should check that the answer does not depend on the representation of the simple function. If we divide the underlying sets into a common finite partition, both expressions agree cell by cell. The finite additivity of E then gives the same operator.

Multiplication is similarly concrete. Two simple functions multiply by multiplying their values on the intersections of their level sets. The projection identity E of B times E of C equals E of their intersection shows that the corresponding operators multiply in exactly the same way.

Taking complex conjugates of coefficients gives the adjoint operator because the projections are self-adjoint. The constant-one function gives the identity.

The norm of the operator is at most the largest absolute value of the simple function on the spectral support. To see this, decompose any vector into its orthogonal components on the level sets. The squared norm of the resulting vector is the sum of the squared coefficient magnitudes times the squared component lengths. Each coefficient magnitude is bounded by the maximum.

### Extend to bounded Borel functions

Every bounded Borel complex-valued function admits a sequence of simple Borel functions converging uniformly to it. One explicit construction partitions a bounded square in the complex plane into progressively finer cells and replaces each function value by a representative of its cell. The preimage of each cell is Borel, and the approximation error decreases uniformly.

Let f-n be such simple functions. By the norm estimate, the operator difference between f-n of A and f-m of A is bounded by the uniform difference of the symbols. The sequence of operators is therefore Cauchy in operator norm and converges to a bounded operator. Define that limit to be f of A.

Different simple approximations give the same operator, by comparing their uniform errors to f. This provides one direct construction of the bounded Borel calculus from a projection-valued measure.

It is useful to distinguish this step from the construction of the projection-valued measure itself. If we started only with continuous functional calculus, we had to build the scalar measures and projections first. Once E is available, uniform simple-function approximation of a bounded Borel symbol is straightforward.

### The algebraic laws

Addition, multiplication, scalar multiplication, and taking adjoints all commute with the operator-norm limits just used. Their identities for simple functions therefore extend to bounded Borel functions.

Thus the constant-one symbol yields the identity. The product of two symbols yields the composition of their operators. Complex conjugation yields the adjoint. If the symbols are real-valued, their operators are self-adjoint.

Every two operators obtained from the same Borel calculus commute, because their scalar symbols commute pointwise. In particular, every f of A commutes with A itself.

For a nonnegative real symbol f, its square root is again bounded and Borel. If g is that square root, then f of A equals g of A adjoint times g of A. Consequently f of A is a positive operator.

All these facts preserve the intuitive picture of multiplication operators: doing something to the spectral variable before entering the model is the same as doing it to the operator afterward.

### A norm estimate and what it does not say

If the absolute value of f is everywhere bounded by M, then the norm of f of A is at most M. For multiplication operators this follows immediately from integrating the squared magnitude of f times a vector.

There is a sharper statement: the norm is the essential supremum of f relative to the projection-valued measure. That means we ignore sets B for which E of B is zero. We must not automatically use the ordinary pointwise maximum of a Borel function on the entire spectrum.

Consider multiplication by t on L two of the unit interval. Let f be zero everywhere except at t equal to one half, where f equals a million. As a pointwise function on the spectrum its supremum is a million. But the set containing that single point has zero spectral projection. Therefore f of A is the zero operator.

By contrast, if A has an eigenvector with eigenvalue one half, the same symbol acts by a million on that eigenspace. There is no contradiction. The two operators have different spectral measures.

This distinction is absent for continuous functions: a continuous function that is large at a spectral point is large nearby, and a genuine spectral point cannot have every small neighborhood carry zero projection. For discontinuous symbols, the difference matters.

### Strong convergence under bounded pointwise limits

Suppose f-n are Borel functions bounded in magnitude by the same constant M, and f-n converges pointwise to f. Do their operators converge in operator norm? Generally, no. But they do converge strongly.

Fix a vector x. The squared norm of the difference, f-n of A minus f of A, applied to x equals the integral of the squared absolute difference between f-n and f against mu sub x.

That integrand converges pointwise to zero and is bounded by four M squared. The scalar measure mu sub x is finite. Dominated convergence therefore shows that this squared norm tends to zero.

Since x was arbitrary, the operators converge strongly.

For example, on L two of the unit interval let f-n be the indicator of the interval from zero through one over n. These functions approach zero almost everywhere, and their multiplication operators converge strongly to zero. Yet each operator has norm one, so operator-norm convergence fails.

An endpoint convention can make the symbols fail to converge at the point zero; that point has zero spectral measure in this example. Alternatively, use open intervals to obtain pointwise convergence everywhere while retaining the same phenomenon. Either way, strong convergence is the correct operator topology.

### Indicators and spectral projections

The indicator of a Borel set B yields precisely E of B. Hence every spectral projection belongs to the Borel calculus. The indicator of an intersection yields the product of the projections, and the complement yields the identity minus the original projection.

This gives a precise language for selecting a spectral cluster. Suppose A has spectrum in two separated closed intervals, one below zero and the other above two. Choosing the indicator of the lower interval gives the orthogonal projection onto the lower spectral subspace. That selection does not require selecting eigenvectors or assuming finite-dimensionality.

When comparing the spectral projections of two different self-adjoint operators, we must be more careful. Those projections need not commute because they come from different functional calculi. The commuting property applies only to projections belonging to the same P V M.

### Bounded and unbounded symbols

We have restricted f to be bounded. A bounded self-adjoint A has bounded spectral support, so the coordinate function itself is bounded there. But even for bounded A, a measurable scalar function may be unbounded near some point of the spectrum.

Its multiplication operator may then be unbounded and have a proper domain. One cannot assign it a bounded operator simply by using the same notation.

The theory of unbounded measurable functions requires explicit domains and graph-closedness. A Borel function that is not bounded may therefore define an unbounded operator with a proper domain; the bounded functional calculus alone does not authorize that operation. For now, every operator produced by the bounded Borel calculus acts on all of H and is bounded.

### The theorem assembled

We have constructed bounded Borel functional calculus using simple spectral integrals and uniform approximation. We proved the unit, product, adjoint, positivity, and uniform norm bound. We also proved strong convergence under uniformly bounded pointwise limits by reducing it to dominated convergence for scalar spectral measures.

The simplest test case remains the lower-half interval. Its indicator yields an actual orthogonal projection, even though the indicator jumps at the midpoint. Bounded pointwise convergence yields strong convergence on each vector, while uniform scalar error yields operator-norm error. These are different guarantees, and the multiplication example exhibits both.

## Measurable spectral restrictions

In finite-dimensional linear algebra, selecting several eigenspaces and restricting a self-adjoint matrix to their direct sum is routine. We now know how to make a similar selection even when the operator has no eigenvectors.

Take a bounded self-adjoint operator A on a complex Hilbert space H. By the spectral theorem, every Borel set B of real spectral values has an orthogonal spectral projection E of B. The projection keeps the part of a vector carried by B, and sets its orthogonal complement to zero. Choose B and let K be the closed range of that projection. We want to study the operator that A induces on K, and to understand how its spectral calculus relates to the original one.

The key fact is that spectral selection is compatible with restriction. But there is an important boundary issue: the spectrum of the restricted operator need not lie inside B itself when B is not closed.

### First establish invariance

The projection P, meaning E of B, is a bounded Borel function of A. The Borel functional calculus makes a bounded Borel function of A commute with A on the appropriate domain. Therefore A P equals P A.

Let x belong to K. Then P x equals x. Apply P to A x. By commutation, P A x equals A P x, which equals A x. Hence A x lies in K.

Now take y in the orthogonal complement of K. Because P is orthogonal, P y equals zero. Again P A y equals A P y, which is zero. Thus A y stays in the orthogonal complement.

So K reduces A. The restriction A sub K acts on a complete Hilbert space in its own right, since K is a closed subspace of H.

Self-adjointness passes to the restriction. For vectors x and y in K, their inner products with the restricted operator agree with their ambient inner products, and the self-adjoint identity for A applies. Equivalently, in the decomposition H equals K orthogonally summed with its complement, A is block diagonal.

### Spectral projections inside the subspace

Suppose C is another Borel set. The spectral projection E of C preserves K because it commutes with P. Its restriction to K is again an orthogonal projection.

What projection does it represent for A sub K? It represents the portion of the restricted spectrum lying in C. In the notation of spectral measures, E sub K of C is E of C restricted to K.

Here is the proof mechanism. For a simple scalar symbol, the functional calculus is a finite linear combination of spectral projections. Restricting that combination to K clearly agrees with the same finite combination of restricted projections.

Uniformly approximate a bounded Borel symbol by simple symbols and pass to the operator-norm limit. The identity remains true for every bounded Borel function.

In particular, calculating f of the restricted operator gives the same result as first calculating f of A and then restricting to K, after interpreting f on the restricted spectral domain.

This is called naturality of the functional calculus under restriction.

### What the range projection means

A useful identity follows immediately from the product rule:

E of C applied to a vector in K equals E of B intersect C applied to that vector.

Indeed, write a vector x in K as P x, and then E of C P x equals E of B intersect C applied to x.

If C is disjoint from B, this is zero. Thus the restriction has no spectral weight in any Borel set disjoint from B.

But be careful. This statement about spectral weight does not imply that every point of the restricted spectrum lies in B itself. It implies containment in the closure of B intersected with the original spectrum, provided K is nonzero. The closure enters because spectra are closed sets and spectral weight can accumulate near boundary points.

### The open-interval boundary example

Take A to be multiplication by t on L two of the unit interval. Let B be the open interval from zero to one half.

The range of E of B consists of functions supported in that interval, up to equality almost everywhere. On this subspace, A still multiplies by t.

What is the spectrum of the restriction? It is the closed interval from zero to one half, not the open interval. The endpoints belong to the spectrum because there are normalized functions supported in very short intervals approaching zero or one half. On such vectors, multiplication by t is arbitrarily close to multiplication by the endpoint value.

Yet neither endpoint has a nonzero eigenvector in this model. The spectral projection of each singleton endpoint is zero. We have spectral accumulation without point spectrum.

Therefore the statement that the restricted spectrum is contained in B would be false. It is the closure of the selected essential spectral support that controls the spectrum.

### Why the restricted spectrum cannot invent a new point

For a reducing subspace K, A decomposes as a block diagonal operator A sub K and A sub its complement. If a complex number z lies outside the spectrum of A, the full operator A minus z has a bounded inverse.

Because the projection onto K commutes with A, it also commutes with that inverse. We can therefore restrict the inverse to K and obtain an inverse of A sub K minus z.

So every point of the restricted spectrum was already in the spectrum of A. There can be loss of spectral values, but not new ones.

This proof is valid for bounded reducing restrictions. It is more robust than trying to track individual eigenvectors, which might not exist.

### Restriction and composition under a unitary change of coordinates

Suppose U is a unitary map and another operator T is obtained by transporting A through U. Applying any bounded Borel symbol to T gives the transported version of f of A.

The reason is again simple-function approximation. Spectral projections transport under unitary conjugation, and finite combinations inherit that property. The uniform limit preserves it.

This naturality is useful when we choose a cyclic multiplication model. A spectral restriction can be performed before or after moving to the L two coordinates. In the multiplication model, restricting to B simply keeps functions supported on B.

The mathematical result depends on the operator and spectral set, not on whichever orthonormal coordinates were chosen to display them.

### Two different operators are different

A tempting inference must be avoided. Spectral projections of the same self-adjoint operator commute. Projections associated with different self-adjoint operators generally do not.

Take the two-dimensional plane. Let P project onto the horizontal axis. Let Q project onto the diagonal line through the vector with equal coordinates. Applying Q to the horizontal unit vector yields a vector with both coordinates equal to one half. Following Q by P keeps its horizontal half. But applying P first leaves the original horizontal vector, and following that by Q gives the diagonal vector. One result is horizontal and the other is diagonal. Therefore P times Q differs from Q times P.

Each projection could be a spectral projection of a different self-adjoint operator. The fact that projections from one spectral measure commute tells us nothing about this cross-operator pair.

If we perturb A to A plus a small self-adjoint operator V, it is meaningful to compare the old spectral projection P and the new spectral projection Q. Quantitative control of their difference requires additional hypotheses, such as a spectral gap and a sufficiently controlled perturbation. The result is not a consequence of a single P V M product law, because P and Q come from distinct measures.

### Restricting a bounded Borel symbol

Suppose f is bounded and measurable on the spectrum of A. Let f sub K denote the same scalar function restricted to the spectrum of A sub K. Since that spectrum is contained in the original one, this restriction makes sense.

Then f sub K of A sub K equals the restriction to K of f of A.

One can prove this from the diagonal measures. For x in K, its scalar measure for the restricted operator agrees with its ambient scalar measure, after viewing the restricted spectrum inside the full spectrum. Therefore the integrals specifying all diagonal matrix elements coincide. Polarization converts the diagonal equality into equality of operators.

This compression identity follows from commutation with spectral projections and the Borel functional calculus. No selected eigenbasis is needed.

### The result to retain

A Borel spectral region defines a closed reducing subspace. Its restricted functional calculus is the ambient calculus restricted to that subspace, and the restricted spectral projection for C is simply the ambient projection for C acting on the selected subspace.

The spectrum of the restriction lies in the original spectrum and in the closure of the selected region, but may include boundary points not contained in the original Borel set. The multiplication example makes that boundary effect tangible: spectral mass can approach a threshold without placing an eigenvector at the threshold.

## Approximate eigenvectors and the continuous spectrum

In a two-by-two diagonal matrix, a number belongs to the spectrum precisely when it appears as an eigenvalue. We can find a nonzero vector on which the matrix acts by multiplication by that number. Infinite-dimensional self-adjoint operators behave differently: a spectral value may admit vectors that are arbitrarily close to being eigenvectors without admitting any actual eigenvector.

Here is an operator we can calculate with. Take the Hilbert space of square-integrable complex functions on the interval from zero to one. Two functions count as the same vector when they agree almost everywhere. Let A multiply a function by the coordinate: at position t, the output is t times the input. This operator is bounded, self-adjoint, and has norm one.

Could one-half be an eigenvalue? That would require a nonzero square-integrable function f for which t times f of t equals one-half times f of t almost everywhere. Wherever t differs from one-half, the equation forces f of t to be zero. The only remaining point is t equal to one-half, which has measure zero. Any function supported on just that point represents the zero vector in this Hilbert space. So one-half is not an eigenvalue.

### Concentrate near the desired frequency

Now choose a small interval centered at one-half, of total width two epsilon. Define f epsilon to be a constant on that short interval and zero outside it. Choose the constant so that the integral of its squared magnitude is one. The resulting function is a unit vector.

When A acts on f epsilon, it multiplies each value by a number t that lies within epsilon of one-half. The difference between A f epsilon and one-half times f epsilon is therefore small: its norm is at most epsilon. We can calculate more. The normalization constant is one divided by the square root of two epsilon. Integrating the squared distance from one-half across the interval gives a residual norm of epsilon divided by the square root of three. As epsilon approaches zero, this defect tends to zero.

We have produced a sequence of unit vectors with arbitrarily small eigen-equation residual for one-half. They are called approximate eigenvectors because the operator acts almost like multiplication by one-half on each one. It is the residual that approaches zero; the unit vectors themselves do not have to converge to a fixed vector. One-half belongs to the approximate point spectrum. The vectors become narrower and taller; they do not converge in norm to a nonzero eigenvector.

The same construction works at every point strictly inside the interval from zero to one, and one-sided shrinking intervals work at the endpoints. Thus each point of the interval has approximate eigenvectors although this particular multiplication operator has no eigenvectors at all.

### Why an approximate eigenvector prevents a bounded inverse

Suppose A minus lambda times the identity had a bounded inverse S. For every vector x in the space, applying S after A minus lambda would recover x. Therefore the norm of x would be at most the operator norm of S times the norm of A minus lambda applied to x.

Put an approximate unit eigenvector into that inequality. The left side is one, while the residual on the right tends to zero. This is impossible if S has finite norm. Hence lambda belongs to the spectrum whenever it has unit approximate eigenvectors.

For our multiplication operator, every number between zero and one is therefore spectral. What about a real number two? Multiplication by t minus two is bounded away from zero on the whole interval. We can invert it by multiplying by one divided by t minus two. The inverse is bounded because the denominator never gets close to zero. The same reasoning works for every complex number outside the closed interval.

Consequently the spectrum is exactly the interval from zero to one. This conclusion combines approximate eigenvectors inside with a bounded inverse outside.

### A second example: a diagonal sequence with an accumulating spectrum

Take the space of square-summable sequences, and let A multiply coordinate n by one divided by n. Every basis vector is a genuine eigenvector, with eigenvalue one divided by n. Those eigenvalues approach zero.

Zero itself is not an eigenvalue: the equation A x equals zero forces every coordinate of x to vanish. But the basis vectors are approximate zero eigenvectors, since the norm of A e n is one divided by n, which approaches zero. So zero is a spectral value without a corresponding nonzero eigenvector.

This example has a pure diagonal basis, while the multiplication example has no eigenvectors. Both show that the spectrum includes more than the set of eigenvalues. The reason is the same: an inverse may fail to be bounded even when the operator has no nonzero kernel.

### Point spectrum and continuous spectrum

The point spectrum consists of eigenvalues. For a bounded self-adjoint operator, a spectral point that is not an eigenvalue belongs to the continuous spectrum: the shifted operator has zero kernel and dense range, yet has no bounded inverse defined on the full Hilbert space.

Why is its range dense? For a bounded self-adjoint T, the orthogonal complement of the range of T is the kernel of its adjoint. For T equal to A minus a real lambda, the adjoint is the same operator. If lambda is not an eigenvalue, that kernel is zero, so the range is dense. Why can the range fail to be all of the space? A bounded bijective operator between Banach spaces would have a bounded inverse. Our approximate eigenvectors rule that out.

A general nonnormal operator can also have residual spectrum, where the range of the shift is not dense. The self-adjoint argument excludes that possibility for real spectral parameters, and a self-adjoint operator has only real spectrum.

### Spectral windows make the approximation geometrically visible

For the multiplication operator, selecting a short interval around lambda is the same as applying the corresponding spectral projection: it cuts a function down to that interval. By shrinking the window we make the operator act more and more like scalar multiplication by lambda on the selected vectors.

For an arbitrary bounded self-adjoint operator, the spectral theorem provides the same idea. If lambda is in the spectrum, every sufficiently small neighborhood of lambda has nonzero spectral projection. Take a unit vector in that spectral subspace. The spectral theorem bounds the residual by the width of the neighborhood. Hence every spectral value of a bounded self-adjoint operator has approximate unit eigenvectors.

This statement needs self-adjointness. For general bounded operators, spectral points need not all be approximate eigenvalues. It also concerns the operator spectrum itself; a selected finite-dimensional approximation may have a different collection of eigenvalues.

### The resolvent and distance to spectrum

When the shift lambda lies outside the spectrum of a self-adjoint operator, its inverse exists and is bounded. The norm of that inverse is exactly the reciprocal of the distance from lambda to the spectrum. In the multiplication example, the inverse multiplies by one divided by t minus lambda, and its norm is the essential supremum of that reciprocal.

Approaching the spectral interval from outside therefore makes the inverse norm grow. Approaching a point of the interval from within produces approximate eigenvectors with vanishing residual. These are two sides of the same spectral geometry: invertibility is stable away from the spectrum, and unit residuals can become arbitrarily small at spectral points.

One final distinction is worth retaining. A vector with a tiny residual is evidence that a spectral value lies nearby for a self-adjoint operator. It is not automatically evidence that the operator has a genuine eigenvector at that value. In infinite dimensions, the continuous spectrum is where that difference becomes unavoidable.

## Resolvents from spectral integrals

For a diagonal matrix, taking an inverse is a coordinate-by-coordinate calculation. The resolvent of an operator A at a complex number z means the bounded inverse of A minus z times the identity, provided that inverse exists. If a diagonal entry is three and we subtract a shift of one, the corresponding entry of the inverse is one half. Each coordinate is handled by taking the reciprocal of its shifted multiplier.

But many self-adjoint operators do not have a basis of eigenvectors. Some have continuous spectrum, where no individual eigenvector represents a spectral value. How can the same idea of taking reciprocals still work?

The spectral theorem provides an answer. It lets us treat a self-adjoint operator as multiplication by a spectral coordinate, even when that coordinate ranges continuously. A resolvent is then obtained by taking reciprocals inside a spectral integral.

This viewpoint explains three things: how the resolvent is constructed, why its norm measures the distance to the spectrum, and how a resolvent can reveal the distribution of spectral mass.

Throughout this recording, A is a bounded self-adjoint operator on a nonzero complex Hilbert space. Its spectrum is a nonempty compact set of real numbers. We use the convention that the resolvent at z is the inverse of A minus z times the identity.

### Start where the answer is visible

Take a diagonal matrix with entries negative two and three. Choose z equal to i, the imaginary unit.

Subtract i times the identity. The two diagonal entries become negative two minus i, and three minus i. Each is nonzero, so the resolvent exists. Its entries are their reciprocals.

The magnitudes of these reciprocal entries are one divided by the square root of five, and one divided by the square root of ten. The first is larger, so the norm of the resolvent is one over the square root of five.

Now look at the spectrum. It consists of the points negative two and three on the real axis. The point i is distance square root of five from negative two, and distance square root of ten from three.

So the resolvent norm is the reciprocal of the distance to the nearest spectral value.

The calculation suggests a general rule: if an operator behaves like multiplication by a number lambda, then A minus z behaves like multiplication by lambda minus z, and its inverse behaves like division by lambda minus z.

What we need is a replacement for the list of diagonal entries when the spectrum contains a continuum.

### Replace diagonal entries by spectral slices

Consider the Hilbert space of square-integrable functions on the interval from zero to one. Define A by multiplying a function by its input coordinate. At a point t, the output is t times the function's value there.

This operator is bounded and self-adjoint. Its spectrum is the whole interval from zero to one. There is no nonzero square-integrable eigenfunction concentrated at a single value of t, because one point has measure zero.

Nevertheless, we can isolate a band of spectral values. For example, we can keep the part of a function supported where t lies between one quarter and one half, and set the rest to zero.

That operation is an orthogonal projection. It is exactly the spectral projection associated with that interval.

For a general self-adjoint operator, a projection-valued measure plays the same role. To every suitable set of real spectral values it assigns an orthogonal projection onto the part of the Hilbert space carried by those values.

A spectral integral combines these projections, weighting each spectral slice by a scalar function of its spectral value. In the multiplication example, the construction simply multiplies the function at t by the chosen scalar function evaluated at t.

The spectral theorem says that A itself is obtained by weighting its spectral slices by lambda. More generally, a bounded continuous function g on the spectrum defines an operator called g of A. Products of scalar functions become products of operators, and the constant-one function becomes the identity.

That product rule is what makes inversion possible.

### Taking the reciprocal

Choose a complex number z outside the spectrum. On the spectrum, the scalar function that divides one by lambda minus z never has a zero denominator.

Because the spectrum is compact, the reciprocal function is bounded and continuous there. We can therefore form its operator through the spectral calculus.

Now multiply the reciprocal function by lambda minus z. The product equals one at every spectral value. The functional calculus carries that scalar identity into an operator identity.

So the operator formed from the reciprocal function undoes A minus z times the identity, in either composition order. It is the resolvent.

In the language of spectral integrals, the resolvent is the integral of the reciprocal of lambda minus z against the projection-valued spectral measure.

This is precisely the same calculation as inverting a diagonal matrix, except that the diagonal entries have been replaced by a continuum of spectral values and a corresponding family of projections.

Return to the multiplication operator on square-integrable functions. Its resolvent at z divides a function's value at t by t minus z. If z lies outside the interval from zero to one, the denominator stays a positive distance from zero and this division is bounded.

No eigenvectors were required to perform that calculation.

### Why distance gives the norm

Let d be the distance from z to the spectrum. Because z lies outside the compact spectrum, d is positive.

Every spectral denominator, lambda minus z, has absolute value at least d. Its reciprocal has absolute value at most one over d. Therefore the resolvent norm is at most one over d.

Why is the estimate exact?

There is at least one spectral value nearest z, because the spectrum is compact. In a neighborhood of that value, the reciprocal multiplier is as large as we wish, up to the maximum one over d. The spectral theorem guarantees nonzero spectral content in every neighborhood of a spectral point. We can choose unit vectors concentrated in such a neighborhood to obtain outputs arbitrarily close to that maximum size.

Thus the norm is at least one over d as well. We have equality: for a bounded self-adjoint operator, resolvent norm equals one divided by distance to spectrum.

This equality extends to normal operators, for which the spectral calculus is still governed by scalar multiplication. It can fail for nonnormal operators, whose inverse may grow substantially even away from eigenvalues.

The formula also explains what happens near an isolated spectral point. In our diagonal matrix, move z toward negative two along a vertical line in the complex plane. If z is negative two plus i times eta, with eta positive, the nearest spectral distance is eta. The resolvent norm is one over eta. It becomes large as eta approaches zero.

### Where do approximate eigenvectors come from?

The spectral-integral picture gives a way to understand why a spectral point need not be an eigenvalue.

Take a real number c in the spectrum. Every narrow interval around c has a nonzero spectral projection. Choose a unit vector supported in that spectral slice.

When we apply A minus c times the identity, every multiplier on that slice has absolute value no larger than the width of the interval. The output norm is therefore at most that width.

As we shrink the interval, we obtain unit vectors for which A minus c times the identity produces arbitrarily small outputs. These are approximate eigenvectors.

If the shifted operator had a bounded inverse, it could not shrink unit vectors arbitrarily close to zero. So c belongs to the spectrum whether or not an exact eigenvector exists.

The multiplication operator on square-integrable functions gives a picture you can keep in mind: concentrate a normalized function on a narrower and narrower interval around c. Multiplication by t then acts more and more like multiplication by c.

### A scalar resolvent can reveal a measure

Now fix one vector x in the Hilbert space. The spectral projections tell us how much of x lies in each spectral band. That information defines a positive scalar measure, often called the spectral measure of x.

If x is a normalized eigenvector with eigenvalue c, all of its spectral mass sits at c. For the multiplication operator, a general square-integrable function spreads its spectral mass across the interval, weighted by the square of its magnitude.

Take the inner product of x with the resolvent applied to x. The result is a complex number. In the spectral calculus it equals the integral of one divided by lambda minus z against the spectral measure of x.

This scalar function of z is a Cauchy transform, also called a Stieltjes transform with the present sign convention.

To see why it is informative, take z with real part u and positive imaginary part eta. The imaginary part of the reciprocal of lambda minus u minus i eta equals eta divided by the sum of the square of lambda minus u and eta squared.

That expression is nonnegative. It is largest when lambda is near u, and becomes more concentrated near u as eta decreases. The imaginary part of our scalar resolvent is the integral of this concentrated kernel against the spectral measure.

Fix eta. As u moves along the real line, the kernel is a rounded peak of total area pi, centered at each spectral value lambda. Dividing by pi therefore gives a normalized averaging kernel. Now let eta decrease. The peak narrows while retaining that area. If we integrate its contribution over an interval whose endpoints carry no spectral mass, the normalized limit records exactly the measure inside the interval. At an endpoint atom, symmetric boundary limits contribute half that atom instead. This is a recovery procedure for a scalar measure, using only resolvent values near the real axis.

So the resolvent does more than report where the spectrum is. Its behavior near the real axis contains information about how a vector's spectral mass is distributed.

### Compare two nearby shifts

The same reciprocal picture explains an important algebraic identity. Subtract the reciprocal of lambda minus w from the reciprocal of lambda minus z. The numerator is z minus w, and the denominator is the product of the two shifted factors.

Apply the functional calculus. The resolvent at z minus the resolvent at w equals z minus w times the product of those two resolvents.

This resolvent identity controls how the inverse changes as the shift moves. Wherever both shifts remain a positive distance from the spectrum, their resolvents stay bounded and close shifts give close resolvents.

The dependence on z is in fact complex analytic away from the spectrum. That additional structure underlies contour formulas for isolated spectral projections.

### A glimpse of the unbounded case

One might expect an unbounded self-adjoint operator to have only unbounded inverses. The spectral integral shows why that expectation is false.

For a nonreal shift z, every real lambda is at least the absolute value of the imaginary part of z away from z. Therefore the reciprocal of lambda minus z is bounded, even if lambda ranges across the entire real line.

An unbounded operator requires a proper domain, and we must still establish that the inverse maps into that domain. The reciprocal formula supplies the right candidate, and the spectral theorem provides the domain argument.

The same picture survives: the resolvent is a bounded operator obtained by taking reciprocals of shifted spectral multipliers.

### The central connection

For a diagonal matrix, inversion means taking a reciprocal at each eigenvalue. For a general self-adjoint operator, spectral integration replaces the diagonal coordinates. The reciprocal becomes a function on the spectrum, and the spectral calculus turns that function into the resolvent.

From this one construction we obtain the exact inverse-distance norm formula, approximate eigenvectors near spectral points, and a scalar transform that reveals spectral mass.

One last calculation connects the cases. Move z vertically toward negative two in the diagonal example. Its distance from the spectrum is just the height above the real axis once z is close enough to that eigenvalue. The resolvent norm is the reciprocal of that height. In the multiplication example, moving toward any point inside the continuous spectral interval produces the same growth without creating an eigenvector. Spectral integration explains both behaviors with the same scalar reciprocal.

## Spectral approximation by cutoffs

An infinite diagonal operator on square-summable sequences can be studied by retaining finitely many coordinates. The approximations improve on each fixed square-summable vector as we keep more coordinates, but the operator-norm error need not become small.

For example, project a square-summable sequence onto its first n coordinates. Each fixed sequence has a tail whose squared sum tends to zero, so the projections converge strongly to the identity. But their operator-norm error is always one: the next basis vector is still discarded completely. This is the model to keep in mind when spectral integrals are approximated by cutoffs.

For a self-adjoint operator A, a spectral projection is the orthogonal projection selecting a specified Borel set of its spectral values. In the diagonal case it keeps chosen eigenvector components; for multiplication by t on an L two space it keeps a region of the function's support. Increasing spectral windows may approximate the identity strongly. On the corresponding domains, functions of an unbounded operator may be approximated by bounded truncations, but a statement about convergence of vectors need not imply convergence in graph norm or in operator norm.

We will make the allowable approximation steps explicit, explain which continuity theorem supports each passage, and separate finite-rank approximations from spectral cutoffs: a bounded spectral window can still have infinite-dimensional range.

### Finite spectral partitions

Let A be a bounded self-adjoint operator on a complex Hilbert space, and write E of B for its spectral projection on a Borel set B.

Suppose the spectrum has been divided into finitely many disjoint Borel regions. Call them B one through B m. Choose a scalar c j for each region. The simple function s takes the value c j on region B j.

Its operator is a finite sum: c one times E of B one, plus the corresponding terms for the remaining regions.

Why is this construction well behaved? The projections of disjoint regions are orthogonal, and their sum is the identity when the regions cover the spectrum. Any vector x splits into orthogonal pieces, one for each region. The simple-function operator multiplies each piece by just one scalar.

Consequently its squared output length is the sum over j of the squared magnitude of c j times the squared length of E of B j applied to x. The operator norm is therefore no larger than the largest magnitude of the chosen scalars.

We have reduced a spectral integral to finitely many orthogonal components, without assuming that any component is one-dimensional. A spectral projection onto an interval can have infinite-dimensional range.

### Approximating a bounded symbol

Now let f be any bounded Borel function on the spectrum. Choose a small positive tolerance, epsilon.

The values of f lie in a bounded region of the complex plane. Divide that region into finitely many small squares, each of diameter less than epsilon. For each square, take the set of spectral points whose f-values fall in that square. These preimages are Borel sets because f is measurable.

Choose one representative value in each square. This produces a simple function s whose value differs from f by less than epsilon at every spectral point.

The squared-norm formula for simple functions, followed by passage to the functional-calculus limit, shows that f of A minus s of A has operator norm at most epsilon. The reason is orthogonality: errors supported on disjoint spectral slices do not reinforce each other in a vector norm. We need the largest scalar error, rather than the sum of all slice errors.

This is genuine operator-norm approximation. One finite spectral sum approximates the action of f of A uniformly on every unit vector.

Notice what made the argument work. We partitioned according to the values of f, not necessarily into intervals of the spectral variable. A wildly discontinuous Borel function need not be approximated uniformly by choosing ever smaller ordinary intervals in its input.

For a continuous function on a compact real spectrum, ordinary spectral intervals do suffice: uniform continuity guarantees that its values vary little inside each sufficiently short interval.

### A concrete matrix calculation

Consider a diagonal matrix with eigenvalues minus two, zero, and three. Suppose we want to approximate its absolute-value operator.

Partition the spectrum into the singleton sets containing those three values. Choose the corresponding function values two, zero, and three. The resulting finite spectral sum is exactly the diagonal matrix with entries two, zero, and three.

Now replace the selected values by two point one, zero, and two point nine. The new operator differs from the absolute-value operator by a diagonal matrix whose nonzero entries are plus point one and minus point one. Its operator norm is point one.

The same calculation works when a spectral region has many dimensions. The error bound is controlled by the worst scalar approximation on a region, rather than by counting eigenvectors.

### Bounded functions can converge strongly without converging in norm

Operator-norm approximation is powerful, but it is not the only limit we need.

Let A be multiplication by t on L two of the interval from zero to one. For each positive integer n, let f n be the indicator of the open interval from zero to one over n.

For each fixed t in the interval, f n of t eventually becomes zero. The functions are uniformly bounded by one. Dominated convergence shows that for every fixed square-integrable vector x, the length of f n of A applied to x tends to zero.

So these operators converge strongly to zero.

But every f n of A still has operator norm one. We can choose a unit vector supported entirely inside the small interval where f n equals one. That choice depends on n.

Strong convergence fixes x first and then lets n increase. Operator-norm convergence allows the test vector to change with n. This is why the conclusions differ.

### Expanding spectral bands

We now allow A to be an unbounded self-adjoint operator. The word unbounded means that A is defined only on a specified dense domain, and no uniform constant controls the length of A x by the length of x over that domain.

For each nonnegative radius R, let P R be the spectral projection onto the closed interval from minus R to R.

The projections P R increase as R increases, because their spectral regions are nested. Their ranges are orthogonal spectral subspaces. These are called spectral cutoffs.

Fix any vector x in the Hilbert space, whether or not x lies in the domain of A. The squared length of x minus P R x is the scalar spectral mass of x outside that interval.

As R increases, those outside sets shrink to the empty set. The scalar spectral measure of x has finite total mass, equal to the squared length of x. Continuity of finite measures from above therefore makes the outside mass tend to zero.

We have proved that P R x tends to x for every fixed x. The cutoffs converge strongly to the identity.

We have not proved norm convergence, and in general it is false. Whenever P R is a proper orthogonal projection, the norm of the identity minus P R is one. A unit vector in its nonzero orthogonal complement witnesses that fact.

### Why a bounded band belongs to the operator domain

Here is the first payoff from the cutoff construction.

Take an arbitrary vector x and form y equal to P R x. Its scalar spectral measure is supported in the interval from minus R to R.

The integral of lambda squared against that measure is at most R squared times the squared length of y. In the unbounded spectral theorem, finiteness of that integral is exactly the condition for y to belong to the domain of A.

Therefore every cutoff vector lies in the domain of A, even if the original x does not.

Moreover, the length of A y is at most R times the length of y. A may be unbounded on its full domain, but its restriction to a fixed bounded spectral band is bounded.

The operator that sends x to A applied to P R x is therefore a bounded operator defined on the whole Hilbert space. It has spectral symbol lambda inside the band and zero outside.

This is the correct interpretation of truncating an unbounded operator. We are not claiming that A itself suddenly becomes bounded.

### Commutation and convergence in the graph norm

Because P R comes from the spectral measure of A, it commutes with A wherever applying A makes sense. Here the domain matters: when A is unbounded, the expression A x is not defined for an arbitrary x in the Hilbert space. A statement about A P R x can hold for every x, while A x itself only makes sense for domain vectors.

More precisely, if x is already in the domain of A, then P R x is in that domain, and A applied to P R x equals P R applied to A x.

We already know P R x tends to x. Apply the strong convergence theorem again, this time to the vector A x. It gives P R A x tending to A x. By commutation, A P R x tends to A x as well.

Thus cutoff vectors approximate every domain vector in both ordinary length and the length of its image under A.

The graph norm combines these two quantities: its square is the squared length of x plus the squared length of A x. Picture the graph as pairs consisting of the input vector and its image under A. Converging in graph norm means that both parts of the pair converge together. We have proved convergence in this graph norm for vectors in the domain.

This is stronger than ordinary strong convergence, and it is the reason bounded spectral cutoffs can safely support proofs involving an unbounded operator.

### A diagonal example showing the domain obstruction

Take the Hilbert space of square-summable sequences. Let A multiply the n-th coordinate by n. Its domain consists of sequences for which the sum of n squared times the squared magnitude of the n-th coordinate is finite.

Consider the sequence whose n-th coordinate is one divided by n. That sequence is square-summable, since the sum of reciprocal squares converges. But it is not in the domain of A: multiplying by n produces a sequence of ones, which is not square-summable.

The radius-N cutoff keeps the first N coordinates and removes all later ones. These cutoff vectors converge in Hilbert-space norm to our original sequence.

Yet the length of A applied to the cutoff vector is the square root of N. It grows without bound. There is no vector A x to which those images could converge.

So strong approximation of x by domain vectors does not by itself imply graph convergence. For graph convergence, x must already belong to the domain.

### What finite rank does and does not mean

One final distinction will matter when we return to singular values.

A finite spectral partition contains finitely many projection terms, but those projections need not have finite rank. On L two of a continuum, a spectral interval ordinarily supports infinitely many independent vectors.

Likewise, an expanding cutoff P R need not be finite rank. Finite partitions, bounded spectral bands, and finite-rank approximations are three different ideas.

There is, however, a useful bridge. If K is compact and P R converges strongly to the identity, then P R K converges to K in operator norm. The reason is that a compact operator sends the unit ball to a set with compact closure. Uniformly bounded projections that converge on every fixed vector converge uniformly on that compact set.

Applying the same reasoning to the adjoint of K shows that K P R converges to K in norm too. Therefore P R K P R converges to K in operator norm.

Without compactness, that conclusion can fail. In particular, taking K equal to the identity would assert norm convergence of P R to the identity, which we have just disproved.

### The bridge to unbounded operator theory

We now have two precise approximation tools. Bounded Borel symbols can be approximated in operator norm by finite spectral sums. For an unbounded self-adjoint operator, bounded spectral cutoffs converge strongly to the identity and approximate domain vectors in graph norm.

The diagonal example identifies the boundary exactly. For the vector with coordinates one over n, the cutoffs converge in ordinary length, but their images under A have lengths growing like square root of N. There is no graph limit because the original vector is outside the domain. For a vector already in the domain, the same cutoffs converge in graph norm. The domain condition determines which approximation statement is true.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Bounded Borel functional calculus

**Draft status:** audio-first mathematical lecture. **Prerequisites:** `032000` finite functional calculus, `075000` continuous calculus, `076000-078000` spectral measures and cyclic models. **Next:** `080000` measurable spectral restrictions.

---

#### Companion: mathematics and Lean correspondence (display only)

For bounded self-adjoint `A` with PVM `E`, bounded Borel `f` gives `f(A) = integral f(lambda) dE(lambda)`, first for simple functions and then by uniform simple approximation. The calculus is a unital star-homomorphism and satisfies `||f(A)|| <= sup |f|`. Uniformly bounded pointwise convergence of symbols implies strong operator convergence by dominated convergence for each scalar spectral measure. Source declarations below use a more general normal operator `a` and symbols on `spectrum C a`; the self-adjoint real-spectrum API pulls back along the real coordinate.

##### Three different senses of size and limit

For \(A=M_t\) on \(L^2([0,1])\), let \(g=10^6\mathbf1_{\{1/2\}}\). Its pointwise supremum on the spectrum is \(10^6\), while \(g(A)=0\), because \(E_A(\{1/2\})=0\). Hence
\[
\|f(A)\|=\operatorname*{ess\,sup}_{E_A}|f|
\le\sup_{\lambda\in\sigma(A)}|f(\lambda)|.
\]
For \(f_n=\mathbf1_{(0,1/n)}\), \(f_n(t)\to0\) at every \(t\in[0,1]\), and dominated convergence gives \(f_n(A)x\to0\) for each \(x\in H\), but \(\|f_n(A)\|=1\) for every \(n\). Thus bounded pointwise convergence gives strong convergence, not generally norm convergence.

**Lean bridge (verbatim source declaration headers).**

`ForTauCeti/Analysis/InnerProductSpace/BorelCalculus/Operator.lean` - `borelCalculus`:

```lean
noncomputable def borelCalculus (hf : IsBddMeasurable f) : H →L[ℂ] H :=
```

The bounded operator is constructed through the Riesz vector representing the polarized diagonal integrals, rather than by starting from a PVM.

`ForTauCeti/Analysis/InnerProductSpace/BorelCalculus/Multiplicative.lean` - `borelCalculus_mul`:

```lean
theorem borelCalculus_mul (hf : IsBddMeasurable f) (hg : IsBddMeasurable g) :
    borelCalculus ha (hf.mul hg) = borelCalculus ha hf * borelCalculus ha hg :=
```

The normal-operator Borel calculus is multiplicative for bounded measurable symbols.

`ForTauCeti/Analysis/InnerProductSpace/BorelCalculus/Multiplicative.lean` - `borelCalculus_conj`:

```lean
theorem borelCalculus_conj (hf : IsBddMeasurable f) :
    borelCalculus ha hf.conj = ContinuousLinearMap.adjoint (borelCalculus ha hf) :=
```

Complex conjugation of the scalar symbol corresponds to the Hilbert-space adjoint.

`ForTauCeti/Analysis/InnerProductSpace/BorelCalculus/Multiplicative.lean` - `norm_borelCalculus_apply_le`:

```lean
theorem norm_borelCalculus_apply_le (hf : IsBddMeasurable f) {M : ℝ} (hM : 0 ≤ M)
    (hfb : ∀ x, ‖f x‖ ≤ M) (ξ : H) :
    ‖borelCalculus ha hf ξ‖ ≤ M * ‖ξ‖ :=
```

The source provides the sharp pointwise symbol-bound inequality acting on each vector; it improves the preliminary bound present in the defining construction.

**Scope:** The excerpts are declaration headers, not complete proof bodies. Their enclosing modules supply scalar types, normality/self-adjointness assumptions, and typeclass instances. The prose derives the mathematical statements and does not claim that all of the pedagogical arguments have separate local Lean theorems.

### Measurable spectral restrictions

**Draft status:** audio-first mathematical lecture. **Prerequisites:** `015000` reducing subspaces, `030000` spectral projections, `075000-079000` functional calculus and spectral measures. **Next:** `081000` resolvents from spectral integrals.

---

#### Companion: mathematics and Lean correspondence (display only)

For `P = E(B)` and `K = range P`, `PA = AP` makes `K` reducing and `A|K` self-adjoint. For a Borel `C`, `E_K(C) = E(C)|K`. For bounded Borel `f`, the restricted calculus satisfies `f(A|K) = f(A)|K` after composing symbols with the spectral inclusion. `spectrum(A|K)` is a subset of `spectrum(A)` and is contained in `closure(B intersect spectrum(A))`; it need not be a subset of a nonclosed `B`.

##### Noncommuting spectral selections

The projections onto the horizontal axis and the forty-five-degree line in \(\mathbb R^2\) are
\[
P=\begin{pmatrix}1&0\\0&0\end{pmatrix},\qquad
Q=\frac12\begin{pmatrix}1&1\\1&1\end{pmatrix}.
\]
Then
\[
PQ=\frac12\begin{pmatrix}1&1\\0&0\end{pmatrix},\qquad
QP=\frac12\begin{pmatrix}1&0\\1&0\end{pmatrix},
\]
so they do not commute, though each may be a spectral projection for its *own* self-adjoint operator. In contrast, projections \(E_A(B)\) and \(E_A(C)\) of one operator always obey \(E_A(B)E_A(C)=E_A(B\cap C)\). If \(K=\operatorname{ran}E_A(B)\), then \(\sigma(A|_K)\subseteq\sigma(A)\cap\overline B\) for nonzero \(K\).

**Lean bridge (verbatim source declaration headers).**

`ForTauCeti/Analysis/InnerProductSpace/BorelCalculus/PVM.lean` - `specProj_inter`:

```lean
theorem specProj_inter (B₁ B₂ : Set ℝ) (hB₁ : MeasurableSet B₁) (hB₂ : MeasurableSet B₂) :
    specProj (H := H) ha hκ B₁ hB₁ * specProj ha hκ B₂ hB₂
      = specProj ha hκ (B₁ ∩ B₂) (hB₁.inter hB₂) :=
```

The product of two spectral projections is the projection of the set intersection, which makes all projections for a fixed operator commute.

`ForTauCeti/Analysis/InnerProductSpace/BorelCalculus/Restriction.lean` - `spectrum_compress_subset`:

```lean
theorem spectrum_compress_subset (ha : IsStarNormal a) (hK : IsCalculusInvariant ha K) :
    spectrum ℂ (compress K a) ⊆ spectrum ℂ a :=
```

The spectrum of the compressed normal operator is contained in the ambient spectrum, under the calculus-invariance hypothesis.

`ForTauCeti/Analysis/InnerProductSpace/BorelCalculus/Restriction.lean` - `borelCalculus_compress`:

```lean
theorem borelCalculus_compress (ha : IsStarNormal a) (hK : IsCalculusInvariant ha K)
    {f : spectrum ℂ a → ℂ} (hf : IsBddMeasurable f) :
    borelCalculus (isStarNormal_compress ha hK) (hf.comp_specIncl ha hK)
      = compress K (borelCalculus ha hf) :=
```

The Borel calculus of the restricted operator agrees with compression of the ambient Borel calculus, after restricting symbols by the spectral inclusion.

**Scope:** The excerpts are declaration headers, not complete proof bodies. Their enclosing modules supply scalar types, normality/self-adjointness assumptions, and typeclass instances. The prose derives the mathematical statements and does not claim that all of the pedagogical arguments have separate local Lean theorems.

### Approximate eigenvectors and the continuous spectrum

**Draft status:** audio-first mathematical lecture. **Prerequisites:** bounded self-adjoint operators, Hilbert spaces, the spectrum, and L2 multiplication operators. **Related:** `080000` spectral restrictions, `081000` resolvent integrals, `086000` spectral location.

---

#### Mathematical companion (display only)

Let \(H=L^2([0,1])\) and \(Af(t)=t f(t)\). Then \(A=A^*\), \(\|A\|=1\), \(\sigma(A)=[0,1]\), and \(\sigma_p(A)=\varnothing\). For \(\lambda\in(0,1)\) and \(0<\varepsilon<\min\{\lambda,1-\lambda\}\), put
\[
f_\varepsilon(t)=\frac{\mathbf 1_{[\lambda-\varepsilon,\lambda+\varepsilon]}(t)}{\sqrt{2\varepsilon}}.
\]
Then \(\|f_\varepsilon\|_2=1\), and
\[
\|(A-\lambda I)f_\varepsilon\|_2^2
=\frac1{2\varepsilon}\int_{-\varepsilon}^{\varepsilon}s^2\,ds
=\frac{\varepsilon^2}{3}.
\]
The bound \(\|(A-\lambda I)f_\varepsilon\|\leq\varepsilon\) also follows without computing the integral. One-sided normalized indicators treat \(\lambda\in\{0,1\}\).

For \(z\notin[0,1]\), \(((A-zI)^{-1}f)(t)=f(t)/(t-z)\), and
\[
\|(A-zI)^{-1}\|=\frac1{\operatorname{dist}(z,[0,1])}.
\]
For \(De_n=n^{-1}e_n\) on \(\ell^2\), \(D\) has eigenvalues \(1/n\) but \(0\notin\sigma_p(D)\); nevertheless \(\|De_n\|=1/n\to0\), so \(0\in\sigma(D)\).

If \(T=T^*\in\mathcal B(H)\), then \(\lambda\in\sigma(T)\) implies \(\forall\varepsilon>0\), \(E_T((\lambda-\varepsilon,\lambda+\varepsilon))\ne0\). A unit vector \(x\) in its range obeys \(\|(T-\lambda I)x\|\le\varepsilon\). For real \(\lambda\), \(\overline{\operatorname{Ran}(T-\lambda I)}=(\ker(T-\lambda I))^\perp\); if \(\lambda\notin\sigma_p(T)\), the range is dense but not all of \(H\).

No Lean declaration is asserted for these standard spectral-theorem consequences.

### Resolvents from spectral integrals

**Draft status:** audio-first mathematical lecture. **Prerequisites:** `008000` resolvents, `031000` spectral separation, `075000-080000` spectral calculus and measurable restriction. **Next:** `082000` spectral approximation by cutoffs.

---

#### Companion: mathematics and Lean correspondence (display only)

With `A = A*` bounded and `z` in the complex resolvent set, `R_A(z) = (A - z I)^(-1) = integral (lambda - z)^(-1) dE(lambda)`, and `||R_A(z)|| = 1 / dist(z,spectrum(A))` on a nonzero Hilbert space. For a scalar spectral measure `mu_x`, `<x,R_A(z)x> = integral (lambda-z)^(-1) d mu_x(lambda)`. For \(z=u+i\eta\) with \(\eta>0\), the imaginary part of the scalar transform has kernel \(\eta/((\lambda-u)^2+\eta^2)\); integrating over an interval and dividing by \(\pi\) recovers its measure in the \(\eta\to0^+\) limit when the endpoints have zero mass. The source formalizes inverse-distance *upper bounds* for bounded self-adjoint resolvents and resolvent identities; the full equality and scalar-transform interpretation here are derived mathematically, not attributed to those specific theorem headers.

##### Resolvent and scalar-measure recovery

For bounded self-adjoint \(A\) with PVM \(E_A\), define \(R(z)=(A-zI)^{-1}\) for \(z\notin\sigma(A)\). Then
\[
R(z)=\int_{\sigma(A)}\frac{1}{\lambda-z}\,dE_A(\lambda),\qquad
\|R(z)\|=\frac{1}{\operatorname{dist}(z,\sigma(A))},
\]
\[
R(z)-R(w)=(z-w)R(z)R(w).
\]
For \(\mu_x(B)=\|E_A(B)x\|^2\), taking \(z=u+i\eta\), \(\eta>0\), gives
\[
\operatorname{Im}\langle x,R(u+i\eta)x\rangle
=\int\frac{\eta}{(\lambda-u)^2+\eta^2}\,d\mu_x(\lambda).
\]
For an interval \((a,b)\) with \(\mu_x(\{a,b\})=0\), integrate the imaginary part in \(u\in(a,b)\), divide by \(\pi\), then let \(\eta\downarrow0\) to recover \(\mu_x((a,b))\). Without the no-atoms condition the symmetric kernel contributes half of each endpoint mass.

**Lean bridge (verbatim source declaration headers).**

`DavisKahan/SpectralTheory/ResolventOperator.lean` - `resolvent_identity`:

```lean
theorem resolvent_identity
    (A : E →L[𝕜] E) {z w : 𝕜}
    (hz : InResolventSet A z) (hw : InResolventSet A w) :
    resolventOperator A z - resolventOperator A w =
      (z - w) • (resolventOperator A z ∘L resolventOperator A w) :=
```

This module defines its bounded resolvent as the inverse of `A - z I`; the displayed identity uses that sign convention.

`DavisKahan/SpectralTheory/ResolventOperator.lean` - `complex_inResolventSet_and_norm_resolvent_le_inv_distance`:

```lean
theorem complex_inResolventSet_and_norm_resolvent_le_inv_distance
    (A : H →L[ℂ] H) (hA : A.IsSymmetric)
    (z : ℂ) (delta : ℝ) (hdelta : 0 < delta)
    (hsep : ∀ lam ∈ realSpectrum A, delta ≤ ‖z - (lam : ℂ)‖) :
    InResolventSet A z ∧ ‖resolventOperator A z‖ ≤ delta⁻¹ :=
```

For symmetric bounded complex operators, a positive lower bound `delta` on spectral distance yields resolvent-set membership and the norm upper bound `delta^-1`.

`ForTauCeti/Analysis/InnerProductSpace/LinearPMap/SpectralMeasure/Construction.lean` - `spectralPVM_resolvent_formula`:

```lean
theorem spectralPVM_resolvent_formula (hzr : z ∈ resolventSet A) (ξ : H) :
    ⟪ξ, resolvent A z ξ⟫_ℂ
      = ∫ s, (z - (s : ℂ))⁻¹ ∂((spectralPVM hA).diag ξ) :=
```

This theorem concerns an unbounded self-adjoint operator and uses the separate convention `resolvent A z = (z I - A)^-1`, so its integrand is `(z-lambda)^-1`, the negative of the bounded resolvent convention used in this lecture. Do not identify the two without a minus sign.

**Scope:** The excerpts are declaration headers, not complete proof bodies. Their enclosing modules supply scalar types, normality/self-adjointness assumptions, and typeclass instances. The prose derives the mathematical statements and does not claim that all of the pedagogical arguments have separate local Lean theorems.

### Spectral approximation by cutoffs

**Draft status:** audio-first mathematical lecture. **Prerequisites:** `073000` Borel sets, `074000` integration and L two, `076000` projection-valued measures, `079000` bounded Borel calculus, and `081000` resolvents. **Next:** `083000` densely defined operators and their graphs.

---

#### Companion: mathematics and Lean correspondence (display only)

Let `E` be the projection-valued measure of a self-adjoint operator `A`, possibly unbounded, and write `P_R = E([-R,R])` for `R ≥ 0`. For any `x ∈ H`,

\[
\|x-P_Rx\|^2=\mu_x(\mathbb R\setminus[-R,R])\longrightarrow0.
\]

The bounded truncation `A_R = A P_R = \int_{[-R,R]}\lambda\,dE(\lambda)` is defined on all of `H` and has `\|A_R\|\le R`. Every `P_R x` is in `Dom(A)`; if `x∈Dom(A)`, then `A P_Rx=P_R Ax\to Ax`. In particular, `P_Rx → x` in the graph norm for each domain vector. For a bounded Borel `f`, uniformly approximating its values by finite simple functions gives operator-norm approximation of `f(A)`. None of these assertions makes `P_R` finite rank.

For a compact bounded operator `K`, strong convergence `P_R → I`, the uniform bound `\|P_R\|≤1`, and compactness give `\|P_RK P_R-K\|→0`; this compact-operator extension is a mathematical argument in the lecture rather than an assertion that the source declarations quoted below directly formalize it.

##### Domain-sensitive cutoff example

For \(Ae_n=n e_n\) on \(\ell^2\), put
\[
D(A)=\{x:\sum_{n\ge1}n^2|x_n|^2<\infty\},\quad
P_Nx=(x_1,\ldots,x_N,0,\ldots).
\]
For \(x=(1/n)_{n\ge1}\in\ell^2\setminus D(A)\), \(P_Nx\to x\) in \(\ell^2\), but
\[
\|AP_Nx\|^2=\sum_{n=1}^N1=N\to\infty.
\]
For \(y\in D(A)\) instead, \(P_Ny\to y\) and \(AP_Ny=P_NAy\to Ay\), hence
\[
\|P_Ny-y\|_A^2=\|P_Ny-y\|^2+\|AP_Ny-Ay\|^2\to0.
\]
Thus the cutoff sequence converges strongly on all of \(H\), and in graph norm only when the target vector is in the operator domain.

**Lean bridge (verbatim source declaration headers).**

`DavisKahan/SpectralTheory/SpectralCutoff.lean` — `spectraSpectralCutoff`:

```lean
@[expose] noncomputable def spectraSpectralCutoff
    (A : H →ₗ.[ℂ] H)
    (hA : IsSelfAdjoint A) (τ : ℝ) : H →L[ℂ] H :=
```

This is the bounded projection onto the closed spectral interval `[-τ, τ]` for a *partial linear map* `A`, not the restriction of an everywhere-defined bounded operator. The cutoff is meaningful even when `τ` is negative, though the narrated exhaustion uses nonnegative radii.

`DavisKahan/SpectralTheory/SpectralCutoff.lean` — `spectraSpectralCutoff_range_le_domain`:

```lean
theorem spectraSpectralCutoff_range_le_domain
    (A : H →ₗ.[ℂ] H)
    (hA : IsSelfAdjoint A) (τ : ℝ) :
    LinearMap.range (spectraSpectralCutoff A hA τ).toLinearMap ≤ A.domain := by
```

The entire range of the cutoff lies in `A.domain`; this is stronger than preservation of the domain when starting from a domain vector.

`DavisKahan/SpectralTheory/SpectralCutoff.lean` — `spectraSpectralCutoff_commutes_on_domain`:

```lean
theorem spectraSpectralCutoff_commutes_on_domain
    (A : H →ₗ.[ℂ] H)
    (hA : IsSelfAdjoint A) (τ : ℝ) (x : A.domain) :
    ∃ hx : spectraSpectralCutoff A hA τ (x : H) ∈ A.domain,
      A ⟨spectraSpectralCutoff A hA τ (x : H), hx⟩ =
        spectraSpectralCutoff A hA τ (A x) :=
```

The membership proof `hx` makes the left side a legal application of an unbounded operator. Its equality with the projected image `P_R(Ax)` gives graph-norm convergence in conjunction with the next theorem.

`DavisKahan/SpectralTheory/SpectralCutoff.lean` — `spectraSpectralCutoff_tendsto_identity`:

```lean
theorem spectraSpectralCutoff_tendsto_identity
    (A : H →ₗ.[ℂ] H)
    (hA : IsSelfAdjoint A) (x : H) :
    Tendsto (fun τ : ℝ => spectraSpectralCutoff A hA τ x)
      atTop (𝓝 x) :=
```

This is convergence in the norm topology of `H` **for each fixed `x`**. It does not assert operator-norm convergence of the cutoff family.

`ForTauCeti/Analysis/InnerProductSpace/LinearPMap/SpectralMeasure.lean` — `truncation_eq_on_specProjection`:

```lean
theorem truncation_eq_on_specProjection {M : ℝ} (hbnd : ∀ s ∈ B, |s| ≤ M) (y : H) :
    ∃ hy : specProjection hA B hB y ∈ A.domain,
      A ⟨specProjection hA B hB y, hy⟩ = truncation hA B hB hbnd y := by
```

The theorem identifies applying `A` to a bounded spectral band with a total bounded truncation operator, and explicitly carries the domain proof needed to type the expression.

`ForTauCeti/Analysis/InnerProductSpace/LinearPMap/SpectralMeasure.lean` — `norm_truncation_apply_le`:

```lean
theorem norm_truncation_apply_le {M : ℝ} (hbnd : ∀ s ∈ B, |s| ≤ M) (y : H) :
    ‖truncation hA B hB hbnd y‖ ≤ max 0 M * ‖y‖ :=
```

The bound on the truncated operator follows from the boundedness of its spectral set. In the closed interval case with `R≥0`, this is the claimed norm bound `R`.

**Real Hilbert spaces:** `DavisKahan/SpectralTheory/Real/SpectralCutoff.lean` supplies a separate real implementation by complexification and descent, including `realSpectralCutoff_tendsto_identity`. The statements displayed above use the complex Hilbert-space API. The `ForTauCeti` spectral-measure files belong to the body of mathematics developed within the DKPS program and subsequently reorganized/upstreamed, so their present import path does not imply separate mathematical origin.

**Scope:** These are source declaration headers, not complete proof bodies. The finite-simple-function approximation and compact-operator norm convergence are proved mathematically in the narration but are not claimed to be the direct statements of the quoted Lean theorems. No Lean compilation of new code is implied.
