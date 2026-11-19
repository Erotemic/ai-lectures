# Cayley, spectral calculus, reducing domains, and forms

<!-- BEGIN SPOKEN LECTURE -->

# Cayley, spectral calculus, reducing domains, and forms

## Cayley transforms and graph-level equivalence

Imagine trying to describe an unbounded self-adjoint operator using only bounded operators. At first that sounds impossible. If the original operator can amplify some unit vectors by arbitrarily large amounts, how could a bounded operator retain enough information to reconstruct it?

The answer is that the bounded operator can carry information in the failure of another bounded map to have a bounded inverse. The Cayley transform gives a precise version of this idea.

It turns a self-adjoint operator into a unitary operator, meaning a linear transformation that preserves lengths and is onto. And from that unitary, we can recover the original operator together with its domain.

### Begin with a resolvent

Let A be a self-adjoint operator on a complex Hilbert space. Its domain may be proper, and A may be unbounded.

A useful theorem says that if we shift a self-adjoint operator by a nonreal complex number, the shifted operator has an inverse that is bounded and defined on the whole Hilbert space. In particular, both A plus i times the identity and A minus i times the identity are bijections from the domain of A onto the Hilbert space.

Here i is the imaginary unit, the number whose square is negative one.

The Cayley transform uses these two shifts. To apply it to an arbitrary vector y, first invert A plus i. That produces some vector x in the domain of A. Then apply A minus i to x.

The input to the second step is guaranteed to be legal. That is crucial. We have constructed a map on the whole Hilbert space, even though its formula includes an unbounded operator.

Call the resulting map U. It is the Cayley transform of A.

We can rewrite the formula without explicitly applying A. The expression A minus i is the same as A plus i minus two i. Therefore U equals the identity minus two i times the inverse of A plus i.

The inverse in this formula is a bounded resolvent. So U is bounded, too.

But something stronger is true: U is unitary.

### Why the Cayley transform preserves length

Take any vector x in the domain of A. Compare the lengths of A x plus i x and A x minus i x.

When we square these lengths, both expressions contain the squared length of A x and the squared length of x. The cross terms have opposite signs. They disappear when compared because the inner product of A x with x is real for a self-adjoint operator.

Thus A plus i applied to x and A minus i applied to x have equal lengths.

Now start with an arbitrary vector y. Because A plus i is onto, there is a domain vector x for which y equals A plus i applied to x. By definition, U y equals A minus i applied to that same x. The equality we just proved gives equal lengths for y and U y.

So U preserves every vector's length.

It is also onto. Given any target v, solve A minus i applied to x equals v, and then choose y to be A plus i applied to x. The Cayley transform sends that y to v.

A surjective linear isometry is unitary. We have converted a possibly unbounded self-adjoint operator into an everywhere-defined bounded unitary operator.

### A calculation with a single spectral value

Before discussing infinite dimensions, try the formula on an ordinary scalar. Suppose A is just multiplication by the real number one.

The Cayley transform multiplies by one minus i divided by one plus i. Multiplying numerator and denominator appropriately gives negative i. The complex number negative i lies on the unit circle, so it preserves absolute value.

If A is multiplication by two, the Cayley scalar is two minus i divided by two plus i. This is also on the unit circle.

In fact, for any real lambda, lambda minus i and lambda plus i have the same absolute value. Their ratio must therefore have magnitude one.

This scalar picture helps explain the operator result. The real line is being mapped around the unit circle. The transform replaces unbounded real spectral values with unit-magnitude complex values.

There is one point on the circle that no finite real lambda reaches: the number one. As lambda becomes very large in either direction, its Cayley value approaches one.

That exceptional point is where information about unboundedness is stored.

### The domain is hiding in one minus U

From the earlier formula, U equals the identity minus two i times the inverse of A plus i. Rearranging, one minus U equals two i times that resolvent.

Now think about the range. The inverse of A plus i takes the whole Hilbert space onto the domain of A. It lands in every allowed input, and only allowed inputs. Multiplying by two i does not change the range.

Therefore the range of one minus U is exactly the domain of A.

This is the central reconstruction fact. The bounded operator one minus U has a range that may be a dense, proper subset of the Hilbert space. That subset remembers the domain of the unbounded operator.

Can we also recover the action of A? Yes.

Take any vector y and form x equal to one minus U applied to y. We already know x lies in the domain of A. Then A applied to x equals i times one plus U applied to y.

We can verify this with a direct substitution. Let v be the inverse of A plus i applied to y. Then one minus U applied to y equals two i times v. And one plus U applied to y equals two times A applied to v. Multiplying the latter by i gives two i times A v, exactly A applied to the former.

So the action of A is recovered from U by this equation. There is no ambiguity in choosing y, because one minus U is injective.

Why injective? If U y equaled y, write y as A plus i applied to a domain vector v. The equation would force A minus i applied to v to equal A plus i applied to v. Subtracting shows v is zero, so y is zero.

U has no nonzero fixed vector. Equivalently, one is not an eigenvalue of U.

### Why missing an eigenvalue is not enough

It is tempting to conclude that because one is not an eigenvalue, one minus U must be invertible on the whole Hilbert space. That conclusion is false in infinite dimensions.

Return to ell two and let A multiply coordinate N by N, on its weighted square-summability domain.

Every coordinate vector is an eigenvector of A. Its eigenvalue is N. Under the Cayley transform, that coordinate vector has eigenvalue N minus i divided by N plus i.

None of those Cayley eigenvalues equals one. But they approach one as N increases.

So we can find unit vectors whose images under one minus U get arbitrarily small. If one minus U had a bounded inverse on the whole space, that could not happen.

The number one belongs to the spectrum of U as a limit of its eigenvalues, although it has no eigenvector there.

And look at what the range of one minus U is: precisely the proper domain of our original diagonal operator. That is how the bounded Cayley transform retains the unboundedness of A.

### Can every suitable unitary be reversed?

Yes. Start with a unitary operator U that has no nonzero fixed vector. Define a candidate domain to be the range of one minus U.

First check density. If a vector were orthogonal to this range, the adjoint of one minus U would send it to zero. Since U is unitary, that would force the vector to be fixed by U. Only zero is fixed. Thus the range is dense.

Now define A on this range. For an input of the form one minus U applied to y, set A of that input equal to i times one plus U applied to y. Injectivity of one minus U makes the definition single valued.

The unitary identity shows that this operator is symmetric. The shifted equations are especially revealing: A plus i applied to that domain vector equals two i times y, while A minus i applied to it equals two i times U y. Both shifts are onto the whole Hilbert space.

For a densely defined symmetric operator, surjectivity of both nonreal shifts implies self-adjointness. So the reconstructed A is self-adjoint, and its Cayley transform is exactly U.

We have a genuine correspondence: self-adjoint operators, including unbounded ones, are encoded by unitary operators with no nonzero fixed vector.

The bounded unitary carries the geometry. The range of one minus U carries the domain. And the reconstruction equation recovers the operator's action. None of those pieces can be omitted if we want the original unbounded operator back.

## Unbounded spectral theorem and domain calculus

Imagine a diagonal matrix with entries one, two, three, and so on. Its action is easy to describe: multiply each coordinate by the corresponding diagonal entry. But on infinite square-summable sequences, we cannot do that for every input. The resulting sequence might fail to be square summable.

This is the central problem solved by the unbounded spectral theorem. It tells us how a self-adjoint operator acts, even when there is no eigenvector basis, and it tells us exactly which vectors belong to its domain.

We will first understand the theorem through an infinite diagonal example. Then we will replace individual eigenvalues with spectral regions and see how the same reasoning works for continuous spectrum.

### The diagonal picture

Let A multiply coordinate N of an ell-two sequence by N. The Hilbert space ell two consists of sequences whose squared magnitudes have a finite sum.

To apply A, we multiply each coordinate by its index. The output is in ell two exactly when the sum of N squared times the squared magnitude of the input coordinate is finite.

That condition can be described as a weighted sum over spectral values. Each coordinate carries a spectral value N, and the squared magnitude of that coordinate measures how much of the vector is sitting at that spectral value. The output length squared is the sum of spectral value squared times that coordinate's weight.

This is what the spectral theorem will generalize. Instead of always having a discrete list of eigenvalues, we may have spectral mass spread across intervals. Instead of adding the contributions, we integrate them. And the same weighted-square-integrability condition determines the domain.

### How a spectral projection measures a vector

Let A now be any self-adjoint operator on a complex Hilbert space, possibly unbounded.

Its spectral theorem supplies a projection for each Borel set of real numbers. A Borel set can be an interval, a countable union of intervals, or a set formed by the usual countable operations starting from open sets.

Call the projection associated with a spectral set B the projection onto B. Applying it to a vector extracts the component belonging to that spectral region.

In the diagonal example, projecting onto the interval from two to four keeps only coordinates two, three, and four. Projecting onto all even positive integers keeps just the even-numbered coordinates.

Now measure the squared length of the extracted component. For each vector x, this measurement gives a nonnegative number to every Borel set. These numbers form a finite measure, called the scalar spectral measure of x.

Its total mass is the squared length of x. You can think of it as a distribution of the vector's squared magnitude across the real spectral line. It is not necessarily a probability distribution because the vector might not have unit length.

For a diagonal operator, the measure consists of masses at eigenvalues. For continuous spectrum, the mass may be spread across intervals with no mass concentrated at any single point.

This lets us say what it means to apply a function of the operator.

### From a bounded function to an unbounded one

Suppose f is a bounded function of a real spectral value. We can define f of A by spectral calculus. In the diagonal example, it multiplies coordinate N by f of N. For a general self-adjoint operator, it multiplies the contribution in each spectral region by the corresponding function value.

A fundamental norm identity says that the squared length of f of A applied to x is the integral of the squared absolute value of f against the scalar spectral measure of x.

If f is bounded, this is at most the square of its largest magnitude times the squared length of x. So f of A is a bounded operator on the whole Hilbert space.

Now let f grow without bound. The same formula tells us what can go wrong: the integral of the squared magnitude of f might be infinite for some vectors.

The unbounded spectral calculus therefore defines the domain of f of A to be exactly those vectors for which this integral is finite.

For those vectors, the output can be constructed by truncating f to bounded functions, applying the bounded spectral calculus, and then taking a limit. The integrability condition ensures the truncated outputs are Cauchy in Hilbert-space norm.

Here is the essential point. The theorem provides the operator and its domain together. A formal symbol like f of A cannot, by itself, tell us whether a particular input is legal.

### Recover the original operator

To reconstruct A, choose the simplest unbounded function: the spectral variable itself. In the diagonal example, the function sends N to N. In a multiplication-operator example, it sends a real input t to t.

The domain condition becomes finiteness of the integral of the square of the spectral value against the scalar spectral measure.

The output norm squared equals that integral. And the graph norm squared adds the ordinary squared length of x, giving an integral of one plus the square of the spectral value.

That graph-norm identity tells us how strongly the domain condition weighs parts of a vector living far out in the spectrum. Spectral mass at large absolute values contributes much more to the graph norm than to the ordinary norm.

### A calculation that distinguishes three domains

Return to the diagonal operator with spectral values one, two, three, and so on.

First take the sequence whose N-th coordinate is one divided by N. It is square summable. But A would turn it into a sequence of ones, so it is outside the domain of A.

Next take the sequence whose N-th coordinate is one divided by N squared. Multiplying once by N gives the reciprocal sequence, which is square summable. So this new vector lies in the domain of A.

What about applying A a second time? The second multiplication produces a sequence of ones. That is not square summable. So our vector belongs to the domain of A, but not to the domain of A squared.

Finally, any sequence supported in finitely many coordinates belongs to the domain of every power of this diagonal operator. Repeated multiplication changes only finitely many entries.

These three cases show why we cannot infer that an input is legal for an operator just because it is a Hilbert-space vector, or infer that it is legal for A squared just because it is legal for A.

### Bounded cutoffs approximate the unbounded operator

There is a reliable way to approach A using bounded operators.

Choose a radius R and keep only spectral values between negative R and positive R. Call this spectral projection P R. The cutoff operator multiplies by the spectral variable inside that band and by zero outside. Its norm is at most R.

For an arbitrary Hilbert-space vector x, P R x approaches x as the radius grows. Why? The squared length of the discarded part is the spectral mass outside the band. That tail mass tends to zero because the total spectral measure of x is finite.

Even if x is outside the domain of A, its cutoff P R x always lies inside the domain. All its spectral mass is confined to a region where the multiplier is bounded.

Now suppose x actually belongs to the domain of A. Then not only do the cutoff inputs approach x, but their outputs under A also approach A x. The reason is that A applied to P R x equals P R applied to A x, and the cutoffs converge on every fixed Hilbert-space vector, including A x.

This is convergence in the graph norm. It gives us bounded pieces that approximate the whole unbounded operator on precisely the vectors where the operator is defined.

What if x is outside the domain? The cutoff inputs still converge. But the outputs cannot converge in Hilbert norm. If they did, closedness of A would force x into the domain, a contradiction.

Thus domain membership can be tested through convergence of the truncated outputs.

### Continuous spectrum changes the picture, not the rule

Consider the Hilbert space of square-integrable functions on the real line. Define A by multiplying a function at position t by the number t.

Its domain consists of functions for which the integral of t squared times the squared absolute value of the function is finite.

The spectral projection onto an interval simply keeps the function on that interval and sets it to zero elsewhere. The scalar spectral measure of a vector is the integral of its squared magnitude over the selected region.

This operator has no nonzero eigenvectors. An eigenfunction for a number lambda would need to vanish everywhere except at the single point t equal to lambda. A function concentrated on one point represents zero in this Hilbert space because the point has measure zero.

Nevertheless the spectrum is the entire real line. The spectral theorem describes it without constructing any eigenvector basis.

The formula for the domain remains the same kind of square-integrability test as in the diagonal example. Only the sum has become an integral.

### When an algebraic identity loses its domain

There is one final trap worth seeing with the diagonal operator.

Consider two scalar functions of the spectral value. Let g of N equal N, and let f of N equal one over N. Their product is one for every positive integer N.

The operator g of A is our unbounded diagonal multiplication operator. The operator f of A is bounded; it divides coordinate N by N.

Now compose them in that order: apply g of A first, then f of A. For every input in the domain of g of A, the two multiplications cancel and return the original vector.

But this composition is defined only on the domain of g of A, which is a proper subset of ell two. Meanwhile the spectral operator corresponding to the pointwise product f times g is the identity, defined on all of ell two.

The formulas agree wherever both are defined, but the operators are not equal because their domains differ.

That example captures the discipline of unbounded spectral calculus. Algebraic identities of scalar functions are useful, but operator equalities also require equal domains.

The unbounded spectral theorem gives us a complete model: a spectral distribution, a rule for multiplying it, and an integrability test specifying which input vectors are allowed. Together those three ingredients determine the operator.

## Spectral projections and reducing domains

For a diagonal matrix, separating the coordinates into two groups is easy. If the matrix has no entries mixing those groups, each group evolves independently under the transformation.

In infinite-dimensional spectral theory, we want to make the same kind of separation. We may want the part of an operator associated with high energies, or with one cluster of spectral values, without carrying the rest of the space along.

For a bounded operator, we can often describe this with a block matrix. For an unbounded operator, a block formula can be meaningless unless every vector to which we apply the operator belongs to its domain.

The central question is therefore: when does a spectral projection split both the Hilbert space and the allowable inputs of an unbounded operator?

### Begin with the simple diagonal model

Take ell two, the Hilbert space of square-summable sequences. Let A multiply coordinate N by N. Its domain consists of all sequences for which the weighted sequence of N times the coordinates is also square summable.

Suppose we keep only the even-numbered coordinates and erase the odd ones. Call this projection P.

Every ell-two vector splits uniquely into its even part and its odd part, and those two parts are perpendicular.

Now consider a vector in the domain of A. Its weighted coordinate squares have a finite sum. If we discard the odd terms, that sum can only decrease. So the even part remains in the domain.

Also, multiplying the coordinates by their indices and then discarding the odd ones gives the same result as discarding the odd ones and then multiplying. In other words, P commutes with A on the domain of A.

These two facts are what we need. The even and odd parts are each legal inputs, and A never mixes them.

This gives two operators: one acting on the even-coordinate Hilbert space, the other on the odd-coordinate Hilbert space. Both are unbounded, and both have precisely the weighted domain condition inherited from A.

### What can fail for a different projection

Now choose a different one-dimensional subspace: the line spanned by the vector whose first two coordinates are one and one, with all later coordinates zero.

Projecting onto that line produces a perfectly valid bounded orthogonal projection. Its range consists of finite-support vectors, so it even behaves well with the domain condition in this example.

But the line is not invariant under A. Applying A to that vector changes its first two coordinates to one and two. The result no longer lies on the original line.

So projecting and then applying A is not the same as applying A and then projecting. A mixes the chosen line with its perpendicular complement.

This distinguishes an arbitrary trial subspace from a reducing subspace. A trial subspace may be useful for approximation, but it does not necessarily define an independent part of the original operator.

### The two reducing-domain conditions

Let A be a self-adjoint operator on a Hilbert space H, and let P be an orthogonal projection. Its range is a closed subspace M.

For P to reduce A, we require two things on the domain of A.

First, P must preserve the domain. If x is an allowed input to A, then P x must also be allowed. Otherwise A applied after P might not even make sense.

Second, A applied to P x must equal P applied to A x, for every allowed x. This is commutation on the operator domain.

When these conditions hold, the complementary projection, one minus P, also preserves the domain and commutes with A. Each domain vector splits into two legal pieces, one in M and the other in its perpendicular complement.

The operator acts independently on those pieces, just as a block diagonal matrix would.

But we have earned the block picture by proving that the blocks are defined.

### Why spectral projections satisfy the conditions

A self-adjoint operator has a spectral projection for every Borel set of real spectral values. For a diagonal operator, the projection selects coordinates whose eigenvalues lie in the chosen set. For an operator with continuous spectrum, it selects an entire spectral region.

Write E of B for this projection, and let P equal E of B.

The spectral theorem gives a useful test for membership in the domain of A. A vector x belongs to the domain when the integral of the square of the spectral value against the scalar spectral measure of x is finite.

Applying P discards spectral mass outside B. Since we are integrating a nonnegative quantity, the integral cannot increase. Thus P x remains in the domain whenever x was in the domain.

Commutation follows from the same picture. Applying A multiplies each spectral component by its spectral value. Applying P removes components outside B. Those operations can occur in either order without changing the result.

So a spectral projection preserves the domain and commutes with the operator on that domain.

The selected Borel set does not need to be bounded. It might include arbitrarily large spectral values. The projection is always bounded, but the restricted operator may still be unbounded.

### Construct the restricted operator carefully

We can now define the operator part associated with M. Its Hilbert space is M, rather than all of H. Its domain is the intersection of M with the original domain of A. And its action on an allowed vector x is simply A x.

Why does A x land back in M? Because P commutes with A, and P x equals x for vectors in M. Thus P A x equals A x.

Why is the domain dense in M? Take any vector y in M. Since the original domain is dense in H, choose domain vectors approaching y. Project each of them into M. Domain preservation makes those projected vectors legal, and boundedness of P makes them approach y.

The restricted operator is symmetric because A is symmetric. But for unbounded operators, symmetry alone is not self-adjointness. We still need to justify the adjoint domain.

### Resolvents establish self-adjointness

The resolvent gives a clean route.

Choose a nonreal complex number z. Because A is self-adjoint, A minus z has a bounded inverse on the whole Hilbert space.

We claim that this inverse commutes with P. To see why, start with any vector y and let x be its image under the resolvent. Then x belongs to the domain of A, and A minus z applied to x equals y.

Apply P to both sides. Domain preservation and commutation tell us that A minus z applied to P x equals P y. By uniqueness of the solution, P x must be the resolvent applied to P y.

So applying P before or after the resolvent gives the same result.

Now suppose y lies in M. Then P y equals y, which forces the resolvent output x to lie in M as well. That output solves the shifted equation for the restricted operator.

Both nonreal shifts, with positive and negative imaginary parts, are therefore onto M. The restricted operator is densely defined and symmetric, and these surjectivity properties establish that it is self-adjoint.

This argument shows exactly why the restriction inherits self-adjointness: not because the block formula looks symmetric, but because spectral projection preserves the domain and the resolvent.

### The selected set is not automatically the spectrum

There is one last distinction. Suppose we select a Borel set B and form the restricted operator. Does its spectrum equal B?

Not necessarily. B might contain points that carry no spectral mass. And its boundary points might enter the restricted spectrum even if they were not included in the selected set.

For a concrete example, consider the operator that multiplies square-integrable functions on the real line by their input coordinate t. Select functions supported in the open interval from zero to one.

The restricted operator is multiplication by t on square-integrable functions over that interval. Its spectrum is the closed interval from zero to one. Zero and one are spectral values of the restriction, even though the selected Borel set was open.

So spectral gaps must be checked using the actual spectra of the restricted operators, rather than only the written sets used to select them.

A spectral projection gives more than a geometric decomposition. It supplies legal restricted domains, self-adjoint operator parts, and the bounded resolvents needed to analyze those parts. That is the foundation for comparing separated spectral subspaces of unbounded operators.

## Quadratic forms and ordered half-infinite gaps

Suppose two self-adjoint operators have spectra that are far apart. One operator has all its spectral values above a certain level. The other has all its spectral values below a lower level.

Can we measure the separation without listing eigenvalues, and without assuming that either operator is bounded?

Yes. The useful quantities are lower and upper bounds on quadratic forms. Once those bounds create an ordered gap, the spectral theorem lets us build bounded exponential operators and use them to solve an important operator equation.

Let's develop the argument from a concrete example.

### A gap between two infinite lists

Work on ell two, the Hilbert space of square-summable sequences. Define an operator A that multiplies coordinate N by N plus two. Its spectral values are three, four, five, and so on. They have a lowest value, three, but no upper bound.

On a second copy of ell two, define an operator B that multiplies coordinate N by negative N. Its spectral values are negative one, negative two, negative three, and so on. They have a highest value, negative one, but no lower bound.

These are both unbounded self-adjoint operators, defined on their appropriate weighted square-summability domains.

Every spectral value of A is at least three. Every spectral value of B is at most negative one. The nearest the two spectra can come is a distance of four.

More importantly, all of B lies below all of A. We call this an ordered spectral gap. It has direction, not just a minimum distance.

That extra order will let us construct an inverse using decaying exponentials.

### Translate spectral location into a quadratic-form inequality

For a self-adjoint operator A and an allowed input x, the inner product of A x with x is a real number. It is the quadratic form, or energy pairing, of A at x.

Return to the diagonal operator with eigenvalues three, four, five, and so on. Its quadratic form is the sum of each eigenvalue times the squared magnitude of the corresponding coordinate.

Every eigenvalue in that sum is at least three. Therefore the whole sum is at least three times the squared length of x.

That proves a lower quadratic-form bound. The operator may amplify some directions by arbitrarily large factors, but its quadratic form never drops below three times squared length.

For B, every spectral value is at most negative one. Its quadratic form is therefore at most negative one times squared length. This is an upper form bound.

The general statements have the same shape. An operator is bounded below by a number a in quadratic-form sense if its energy pairing is at least a times squared length for every vector in its domain. It is bounded above by b if the corresponding inequality points the other way.

These are one-sided bounds. They do not assert a finite operator norm.

### Why the bounds survive continuous spectrum

Our diagonal proof used a sum over eigenvalues. But a self-adjoint operator need not possess an eigenvector basis.

The spectral theorem replaces that sum with an integral. For each vector x there is a positive scalar spectral measure describing how its squared magnitude is distributed across the real spectral line.

The quadratic form of A is the integral of the spectral value against that measure, provided x belongs to the domain of A.

Suppose the spectrum of A lies entirely at or above a. Every spectral value that contributes to the integral is then at least a. Subtract a inside the integral. The integrand is nonnegative, so the integral is nonnegative.

We conclude that the quadratic form of A at x is at least a times the squared length of x.

The same argument with reversed inequalities proves an upper bound when the spectrum lies at or below b.

For self-adjoint operators, the converse also holds: a lower quadratic-form bound excludes spectrum below that level, and an upper bound excludes spectrum above it. The argument can be seen by testing the inequality on spectral vectors supported in a region where it would otherwise fail.

This is why quadratic-form inequalities are a practical way to state spectral location even for continuous and unbounded spectra.

### The form can have a larger domain

There is a technical distinction worth building into the picture.

When A is unbounded, the expression involving A x requires x to belong to the domain of A. But if A is positive, we can also define an energy form by applying the positive square root of A and taking the squared length of the result.

That second expression has a possibly larger domain: the domain of the square root.

For the diagonal operator with eigenvalues N, the square-root energy of a sequence is the sum of N times the squared magnitude of coordinate N. The full operator domain instead requires the sum with N squared to converge.

Choose coordinates equal to one divided by N to the power three halves. The sum with one factor of N converges, but the sum with N squared diverges.

This vector has finite square-root energy even though A cannot be applied to it as a Hilbert-space vector.

So a quadratic-form inequality may extend to more vectors than an operator identity. That extension is useful, but we must not insert A x into an equation for a vector that lies only in the form domain.

For an operator bounded below by a, the corresponding nonnegative form is built from the square root of A minus a times the identity, together with the scalar lower-bound term.

### What ordered separation adds

Now let A act on one Hilbert space and B on another. Suppose A has a lower form bound a and B has an upper form bound b, with a strictly greater than b.

Define delta to be a minus b. It is positive.

Every spectral value of A lies above every spectral value of B, with separation at least delta. This is the ordered-gap hypothesis.

Compare this with merely saying that the spectra are disjoint. Disjoint spectral sets need not be separated by a positive distance. Even if they are separated by a positive distance, their pieces may alternate along the line. There may be no single level with all of one spectrum above it and all of the other below it.

An ordered gap gives a uniform direction. That direction determines which exponentials decay together.

### Exponentials of unbounded operators can be bounded

If A is bounded below by a, look at the scalar function that sends a spectral value lambda to the exponential of negative t times lambda, for a nonnegative time t.

Although lambda can grow without bound, this exponential function is bounded on the spectrum of A. Its largest possible magnitude is no more than the exponential of negative a times t.

The spectral calculus therefore defines a bounded operator called the exponential of negative t A.

Similarly, because B is bounded above by b, the spectral calculus defines the exponential of positive t B. Its norm is at most the exponential of b times t.

Return to our diagonal example. On coordinate N, the first exponential multiplies by the exponential of negative t times N plus two. The second multiplies by the exponential of negative t times N. Both decrease as t increases.

Now insert any bounded operator C between them. We can form the composition: first apply the exponential of t B, then C, then the exponential of negative t A.

The operator norm of this composition is at most the norm of C times the product of the two exponential bounds. That product simplifies to the exponential of negative delta times t.

So the entire composition decays at least as fast as an exponential whose rate is the spectral gap.

Notice that each exponential separately need not decay. If a is negative, the first upper bound may grow. If b is positive, the second may grow. What is guaranteed to decay is their product, because a is strictly greater than b.

### A scalar equation suggests the operator formula

Consider the elementary equation: three times an unknown number, minus that unknown number times negative one, equals a prescribed number c.

The left side is four times the unknown. The answer is c divided by four. The denominator is exactly our ordered gap.

There is another way to express that division. Multiply c by the exponential of negative four times t, then integrate from time zero to infinity. The result is c divided by four.

This integral suggests how to solve a matrix or operator equation where multiplication occurs on both sides.

The equation is called a Sylvester equation. We seek an operator X such that A applied to X, minus X applied to B, equals a given bounded operator C.

When A and B are unbounded, this is an equation on a specified domain, not a formula that can be applied to arbitrary vectors without checking. In particular, X must carry the domain of B into the domain of A for the expression to make sense.

The natural candidate for X is obtained by integrating the composition we just bounded: the exponential of negative t A, followed around C by the exponential of t B, from time zero to infinity.

For each fixed input vector, the integrand is a continuous Hilbert-space-valued function, and its norm has the exponential upper bound we proved. The integral therefore defines a bounded operator X. Its norm is at most the norm of C divided by delta.

The gap has turned into an inverse bound.

To see why the integral solves the equation, consider differentiating the integrand. Formally, its derivative is negative A applied to the integrand plus the integrand followed by B. Integrating that derivative from zero to infinity gives zero at infinity minus C at time zero.

For unbounded operators, we must justify the differentiation and show that X really sends allowable inputs for B into the domain of A. Here is the mechanism.

Choose a vector in the domain of B. Instead of integrating immediately from zero to infinity, first integrate from a small positive time epsilon to a large finite time T. At positive times, the exponential of negative t A smooths enough that applying A is legal. We can differentiate the integrand and integrate the resulting identity on that finite interval.

The identity expresses A applied to the truncated integral in terms of three legal pieces: the integrand at epsilon, the integrand at T, and the truncated integral applied to B of our input vector.

As epsilon approaches zero, the first piece approaches C applied to the vector. As T grows, the second piece vanishes because of the exponential gap bound. The third piece approaches X applied to B of the vector.

Both the truncated inputs and their images under A now converge. Because a self-adjoint operator is closed, the limit X of our original input belongs to the domain of A, and A X minus X B equals C on the domain of B.

So the formal integration argument becomes a genuine operator identity, with the required domain preservation proved along the way.

### What the gap estimate tells us

The important quantitative result is simple. If the spectrum of A lies above a, the spectrum of B lies below b, and a exceeds b by delta, then the ordered-gap construction gives a bounded Sylvester solution with norm no greater than the norm of C divided by delta.

In the scalar example, the estimate is exact. The unknown is c divided by four, and the gap is four.

The larger the gap, the smaller the possible response to a fixed forcing term C. That is the mechanism behind many spectral subspace perturbation estimates: separation in the spectrum turns into control of an operator that measures how the subspaces interact.

The main ingredients are now connected. Quadratic forms describe one-sided spectral bounds. Self-adjoint functional calculus gives bounded exponentials of unbounded operators. Ordered separation makes their product decay. Integrating that product produces the inverse estimate, with the operator domains handled explicitly.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Cayley transforms and graph-level equivalence

**Draft status:** audio-first mathematical lecture. **Prerequisites:** `014000` unitary operators, `083000` graphs, `086000` resolvents. **Next:** `088000` unbounded spectral theorem.

---

#### Companion: mathematics and Lean correspondence (display only)

Use \(U=(A-iI)(A+iI)^{-1}=I-2i(A+iI)^{-1}\). This bounded operator is unitary, \(\ker(I-U)=0\), and \(D(A)=\operatorname{Ran}(I-U)\). Recover the graph by \(A((I-U)y)=i(I+U)y\). The source's `LinearPMap.resolvent A (-i)` is the inverse of \((-i)I-A\); hence its displayed identity \(I-U=-2iR(-i)\) agrees with the lecture's \(I-U=2i(A+iI)^{-1}\). The Cayley spectral point \(1\) can belong to continuous spectrum despite having no eigenvectors.

##### Scalar and diagonal checks

For the chosen Cayley convention,
\[c(\lambda)=\frac{\lambda-i}{\lambda+i},\quad c(1)=-i,\quad
1-c(\lambda)=\frac{2i}{\lambda+i}.\]
For \(A=\operatorname{diag}(1,2,3,\ldots)\) on its maximal domain,
\(Ue_n=c(n)e_n\), \(c(n)\to1\), and \(Ue_n\ne e_n\). Hence
\(1\in\sigma(U)\) but \(\ker(I-U)=\{0\}\).

##### Actual source declarations

`ForTauCeti/Analysis/InnerProductSpace/LinearPMap/SpectralMeasure/Construction.lean` — `one_sub_cayley_apply`:

```lean
theorem one_sub_cayley_apply (ξ : H) :
    ((1 : H →L[ℂ] H) - A.cayley) ξ
      = -((2 * Complex.I) • resolvent A (-Complex.I) ξ) := by
```

This is the exact convention-sensitive Cayley/resolvent identity.

`ForTauCeti/Analysis/InnerProductSpace/LinearPMap/SpectralMeasure/Construction.lean` — `injective_one_sub_cayley`:

```lean
theorem injective_one_sub_cayley :
    Function.Injective ((1 : H →L[ℂ] H) - A.cayley) := by
```

It proves the Cayley transform has no nonzero fixed vector.

`ForTauCeti/Analysis/InnerProductSpace/LinearPMap/SpectralMeasure/Construction.lean` — `spectralPVM_def`:

```lean
theorem spectralPVM_def :
    spectralPVM hA
      = BorelCalculus.toProjValMeasure (hA.isStarNormal_cayley)
          (measurable_cayleyInv A) := (rfl)
```

The unbounded self-adjoint spectral measure is recovered by relabeling the Borel calculus of the Cayley unitary.

**Scope:** The full converse Cayley correspondence and graph-reconstruction calculations are established in the lecture; the displayed declarations are selected bridge results from the actual project source. These excerpts are from the supplied source snapshot and are not new compiled Lean code. Reusable `ForTauCeti` constructions have explicit DKPS donor/origin notes; the current file namespace does not imply an external origin.

### Unbounded spectral theorem and domain calculus

**Draft status:** audio-first mathematical lecture. **Prerequisites:** `074000` integration and L two, `076000` projection-valued measures, `082000` spectral cutoffs, `087000` Cayley transforms. **Next:** `089000` reducing domains.

---

#### Companion: mathematics and Lean correspondence (display only)

For a self-adjoint \(A\) with projection-valued measure \(E\), put \(\mu_x(B)=\|E(B)x\|^2\). The domain of a measurable spectral operator is \(D(f(A))=\{x:\int |f(\lambda)|^2\,d\mu_x(\lambda)<\infty\}\). In particular \(D(A)\) requires the finite second spectral moment, and \(\|Ax\|^2=\int\lambda^2\,d\mu_x\). The cutoff \(P_R=E([-R,R])\) maps all of \(H\) into \(D(A)\), and for \(x\in D(A)\) satisfies \(AP_Rx=P_RAx\to Ax\), while \(P_Rx\to x\).

##### Domain-sensitive product example

For the maximal diagonal operator \(A=\operatorname{diag}(1,2,\ldots)\),
let \(g(\lambda)=\lambda\) and \(f(\lambda)=1/\lambda\) on
\(\sigma(A)=\{1,2,\ldots\}\). Then \(f(A)\) is bounded and
\[f(A)g(A)=I|_{D(A)},\qquad (fg)(A)=I|_{\ell^2}.\]
The actions agree on \(D(A)\), but the operators have different domains.
In general the composition domain is
\(\{x\in D(g(A)):g(A)x\in D(f(A))\}\), and the scalar product identity
alone does not imply equality with the maximal operator \((fg)(A)\).

##### Actual source declarations

`ForTauCeti/Analysis/InnerProductSpace/LinearPMap/SpectralMeasure/Construction.lean` — `specProjection_mem_domain`:

```lean
theorem specProjection_mem_domain (B : Set ℝ) (hB : MeasurableSet B) (x : A.domain) :
    specProjection hA B hB (x : H) ∈ A.domain := by
```

Spectral projections preserve the original operator domain.

`ForTauCeti/Analysis/InnerProductSpace/LinearPMap/SpectralMeasure/Construction.lean` — `specProjection_apply_domain`:

```lean
theorem specProjection_apply_domain (B : Set ℝ) (hB : MeasurableSet B) (x : A.domain) :
    A ⟨specProjection hA B hB (x : H), specProjection_mem_domain hA B hB x⟩
      = specProjection hA B hB (A x) := by
```

Commutation with an unbounded operator is a typed equality using an explicit proof of domain membership.

`ForTauCeti/Analysis/InnerProductSpace/LinearPMap/SpectralMeasure.lean` — `tendsto_specProjection_Icc`:

```lean
theorem tendsto_specProjection_Icc (x : H) :
    Filter.Tendsto
      (fun τ : ℝ => specProjection hA (Set.Icc (-τ) τ) measurableSet_Icc x)
      Filter.atTop (nhds x) := by
```

The bounded spectral-band projections converge strongly, pointwise on each Hilbert vector.

`ForTauCeti/Analysis/InnerProductSpace/LinearPMap/SpectralMeasure.lean` — `truncation_eq_on_specProjection`:

```lean
theorem truncation_eq_on_specProjection {M : ℝ} (hbnd : ∀ s ∈ B, |s| ≤ M) (y : H) :
    ∃ hy : specProjection hA B hB y ∈ A.domain,
      A ⟨specProjection hA B hB y, hy⟩ = truncation hA B hB hbnd y := by
```

A bounded truncation agrees with the original operator on the selected bounded band.

`ForTauCeti/Analysis/InnerProductSpace/LinearPMap/SpectralMeasure.lean` — `norm_truncation_apply_le`:

```lean
theorem norm_truncation_apply_le {M : ℝ} (hbnd : ∀ s ∈ B, |s| ≤ M) (y : H) :
    ‖truncation hA B hB hbnd y‖ ≤ max 0 M * ‖y‖ :=
```

The bounded truncation norm is controlled by the spectral-band radius.

**Scope:** The spectral-moment domain characterization is taught from the spectral theorem; these excerpts formalize the projected-domain, commutation, convergence and bounded-band aspects. They do not assert that arbitrary unbounded products have equal domains. These excerpts are from the supplied source snapshot and are not new compiled Lean code. Reusable `ForTauCeti` constructions have explicit DKPS donor/origin notes; the current file namespace does not imply an external origin.

### Spectral projections and reducing domains

**Draft status:** audio-first mathematical lecture. **Prerequisites:** `010000` orthogonal complements, `015000` reducing subspaces, `076000` projection-valued measures, `088000` unbounded domain calculus. **Next:** `090000` quadratic forms and ordered half-infinite gaps.

---

#### Companion: mathematics and Lean correspondence (display only)

Let \(A:D(A)\subset H\to H\) be self-adjoint and \(P=E_A(B)\) a spectral projection. Then \(P D(A)\subset D(A)\), \(APx=PAx\) for \(x\in D(A)\), and \(D(A_P)=D(A)\cap\operatorname{ran}P\). The restriction \(A_P\) is self-adjoint on \(\operatorname{ran}P\). Its resolvent is the restriction of the full resolvent, with \(P(A-z)^{-1}=(A-z)^{-1}P\). The spectrum of the restricted operator is contained in the support of the restricted spectral measure, not generally equal to the original Borel selector.

##### Selected set versus restricted spectrum

For \(A=M_t\) on \(L^2(\mathbb R)\), let
\(P=E_A((0,1))\). Then \(PH\cong L^2(0,1)\) and the operator
part \(A_P\) multiplies by \(t\). Its spectrum is \([0,1]\), although
its Borel selector is \((0,1)\). Any spectral-gap hypothesis must use the
actual restricted spectra or verified bounds on them.

##### Actual source declarations

`ForTauCeti/Analysis/InnerProductSpace/LinearPMap/SpectralMeasure/Construction.lean` — `specProjection_mem_domain`:

```lean
theorem specProjection_mem_domain (B : Set ℝ) (hB : MeasurableSet B) (x : A.domain) :
    specProjection hA B hB (x : H) ∈ A.domain := by
```

`ForTauCeti/Analysis/InnerProductSpace/LinearPMap/SpectralMeasure/Construction.lean` — `specProjection_apply_domain`:

```lean
theorem specProjection_apply_domain (B : Set ℝ) (hB : MeasurableSet B) (x : A.domain) :
    A ⟨specProjection hA B hB (x : H), specProjection_mem_domain hA B hB x⟩
      = specProjection hA B hB (A x) := by
```

`ForTauCeti/Analysis/InnerProductSpace/LinearPMap/SpectralMeasure/Construction.lean` — `isSelfAdjoint_specRestrict`:

```lean
theorem isSelfAdjoint_specRestrict : IsSelfAdjoint (specRestrict hA B hB) := by
```


**Type and hypothesis map.** In Lean, `A : H →ₗ.[ℂ] H` is the partially defined linear operator, and `A.domain` is the set of legal input vectors. `hA : IsSelfAdjoint A` supplies self-adjointness, while `(B : Set ℝ)` and `(hB : MeasurableSet B)` authorize a spectral selector. The first theorem proves `specProjection` preserves the domain; the second explicitly inserts that membership proof into the typed application of `A`; the final theorem states self-adjointness of `specRestrict`, the true operator part on the selected spectral range. Its proof in the source uses the domain-preserving resolvent and density, precisely the steps derived in the lecture.

**Scope:** The snippets exhibit spectral-subspace construction, domain preservation and domain-aware commutation. The narrated self-adjoint restriction proof uses the standard nonreal resolvent criterion and is not claimed to be entirely encapsulated by these excerpts. Source declarations are taken from the supplied DKPS snapshot, which includes DKPS-origin results subsequently upstreamed to TauCeti; these excerpts are not newly compiled Lean code.

### Quadratic forms and ordered half-infinite gaps

**Draft status:** audio-first mathematical lecture. **Prerequisites:** `033000` quadratic-form order, `065000` ordered separation, `074000` integration, `088000` unbounded spectral calculus, `089000` reducing domains. **Next:** `091000` Yosida approximation.

---

#### Companion: mathematics and Lean correspondence (display only)

If \(A\) is self-adjoint and \(\sigma(A)\subset[a,\infty)\), then \(\langle Ax,x\rangle\ge a\|x\|^2\) for \(x\in D(A)\). For \(B\) with \(\sigma(B)\subset(-\infty,b]\) and \(a>b\), the gap is \(\delta=a-b>0\). The spectral calculus yields \(\|e^{-tA}\|\le e^{-at}\), \(\|e^{tB}\|\le e^{bt}\), and \(\|e^{-tA}Ce^{tB}\|\le e^{-\delta t}\|C\|\) for \(t\ge0\). The quadratic form of a semibounded operator has a closed form-domain extension defined by its shifted square root; this is distinct from the domain of the operator itself.

##### Ordered-gap Sylvester integral

Let \(A\) be self-adjoint on \(H_A\) with \(A\ge aI\) in form sense,
and let \(B\) be self-adjoint on \(H_B\) with \(B\le bI\), where
\(\delta=a-b>0\). For bounded \(C:H_B\to H_A\), define the
strong (vectorwise) operator integral
\[Xx=\int_0^\infty e^{-tA}Ce^{tB}x\,dt.\]
The semigroup bound yields \(\|X\|\le\|C\|/\delta\). With the
appropriate domain argument, \(X(D(B))\subseteq D(A)\) and
\(AXx-XBx=Cx\) for \(x\in D(B)\). In the scalar example
\(A=3\), \(B=-1\), the formula gives \(X=C/4\).

##### Actual source declarations

`ForTauCeti/Analysis/InnerProductSpace/LinearPMap/Sylvester.lean` — `SemiboundedBelow`:

```lean
def SemiboundedBelow (A : E →ₗ.[𝕜] E) (c : ℝ) : Prop :=
  ∀ x : A.domain,
    c * ‖(x : E)‖ ^ 2 ≤ RCLike.re ⟪A x, (x : E)⟫_𝕜
```

`ForTauCeti/Analysis/InnerProductSpace/LinearPMap/SpectralFormBounds.lean` — `le_re_inner_of_specProjection_Iio_eq_zero`:

```lean
theorem le_re_inner_of_specProjection_Iio_eq_zero {c : ℝ}
    (hz : specProjection hA (Set.Iio c) measurableSet_Iio = 0) (x : A.domain) :
    c * ‖(x : H)‖ ^ 2 ≤ (⟪A x, (x : H)⟫_ℂ).re := by
```

`DavisKahan/SpectralTheory/OrderedHalfLine.lean` — `semiboundedBelow_of_spectrum_subset_Ici`:

```lean
theorem semiboundedBelow_of_spectrum_subset_Ici
    (A : H →ₗ.[ℂ] H) (hA : IsSelfAdjoint A)
    {c : ℝ}
    (hσ : Complex.ofReal ⁻¹' _root_.LinearPMap.spectrum A ⊆
        Set.Ici c) :
    TauCeti.LinearPMap.SemiboundedBelow A c := by
```

`DavisKahan/SpectralTheory/OrderedHalfLine.lean` — `semiboundedAbove_of_spectrum_subset_Iic`:

```lean
theorem semiboundedAbove_of_spectrum_subset_Iic
    (A : H →ₗ.[ℂ] H) (hA : IsSelfAdjoint A)
    {c : ℝ}
    (hσ : Complex.ofReal ⁻¹' _root_.LinearPMap.spectrum A ⊆
        Set.Iic c) :
    TauCeti.LinearPMap.SemiboundedAbove A c := by
```


**Type and hypothesis map.** `SemiboundedBelow A c` is the assertion that every `x : A.domain` satisfies a lower bound for the real part of its energy pairing. `Set.Ici c` is the closed half-line from `c` upward; `Set.Iic c` is the opposite closed half-line. The spectral-containment theorems convert these set hypotheses into the domain-restricted inequalities, without assuming a finite upper or lower operator norm. The square-root form-domain discussion is mathematical background rather than a statement of these particular Lean declarations.

**Scope:** The referenced Lean declarations connect spectral half-line containment to form inequalities and express spectral form bounds. They should not be mistaken for a theorem asserting boundedness of either unbounded generator, nor for the complete unbounded semigroup estimate, which is developed later. Source snippets come from the supplied DKPS snapshot; no Lean compilation was performed for this lecture.
