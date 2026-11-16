# Semigroup representations and distance-gap limits

<!-- BEGIN SPOKEN LECTURE -->

# Semigroup representations and distance-gap limits

## Unitary and semigroup representations

Consider a map from the real numbers into the plane. It sends the number one to the column with entries two and four. Call the map C. On the plane, let A stretch the horizontal direction by negative two and the vertical direction by positive two. On the input line, let B be zero.

We want a map X for which A applied to X, minus X followed by B, equals C. Because B is zero, we can solve this one by inspection. The horizontal entry of X is negative one, and the vertical entry is positive two. Applying A gives back two and four.

The two coordinates tell us something important. One spectral difference is negative two and the other is positive two. Both are safely away from zero. But a method that requires every spectral difference to have the same sign cannot handle this example as a single decaying evolution. We need to understand two kinds of time evolution and the different inverse formulas they support.

### A Sylvester equation as a moving map

Let A be a bounded self-adjoint operator on an output Hilbert space, and B a bounded self-adjoint operator on an input Hilbert space. The unknown X maps inputs to outputs. Its equation is A X minus X B equals C, where C is a known map with the same input and output spaces as X.

First forget about inversion. Imagine observing a map as the two spaces evolve independently. At time t, evolve the output using the exponential of i times t A. Evolve the input using the exponential of i times t B, and undo that evolution on the right. The resulting map is called F of t. At time zero it is the original map.

Because A and B are self-adjoint, both evolutions are unitary. Unitary means they preserve lengths. Left and right unitary multiplication therefore preserve both the operator norm and, when applicable, the Hilbert-Schmidt norm of the map they transport.

Differentiate F in finite dimensions. The left exponential contributes i A F. Differentiating the reversed right evolution contributes negative i F B. Putting the pieces together, the derivative is i times the Sylvester expression A F minus F B.

This is the mental model: the Sylvester operator measures the instantaneous relative motion of a map under two different unitary evolutions. It is an operator acting on operators.

### Hear the two frequencies in the example

Return to the diagonal A with values negative two and positive two, and B equal to zero. Apply the unitary transport to the column C with entries two and four.

Its horizontal component acquires a complex phase that winds at frequency negative two. Its vertical component acquires a phase that winds at frequency positive two. Both keep their magnitudes. The components rotate in opposite directions in the complex plane.

A phase of negative two must eventually produce the reciprocal negative one half. A phase of positive two must produce positive one half. Multiplying those reciprocals by two and four gives our solution column, negative one and positive two.

The question is how an integral over time can perform that division without referring to a particular eigenbasis.

### Why an ordered gap gives a simpler integral

Suppose, unlike our example, that every spectral value of A is at least delta greater than every spectral value of B, with delta positive. Evolve by ordinary exponentials rather than imaginary ones: apply the exponential of negative t A on the left, and the exponential of positive t B on the right.

Every difference of spectral values is now positive. Consequently, each coefficient of the transported C decays at least as rapidly as the exponential of negative delta times t. Integration from time zero to infinity divides a coefficient by its positive spectral difference. The integral of the common decay envelope is one over delta.

This gives a Sylvester solution and a constant-one norm estimate: delta times the norm of X is at most the norm of C. The proof works because the entire operator decays under one common bound, not because we divided individual entries and added their sizes.

Try that orientation on our two-coordinate example. The positive-two component decays, but the negative-two component grows. Reversing the orientation merely exchanges which one grows. The ordered semigroup argument has failed to meet its own hypothesis; the Sylvester equation has not failed to be solvable.

### Build a two-sided oscillatory inverse

Return to unitary evolution, where neither component grows. Instead of integrating the orbit without a weight, multiply it by a suitable scalar function of time and integrate over all real times, both positive and negative.

The weight is chosen by its Fourier transform. At every frequency whose absolute value is at least delta, its transform must equal the reciprocal of that frequency. In our example delta is two, so the transform must take negative two to negative one half and positive two to positive one half.

Why specify the weight only outside the gap around zero? The reciprocal function becomes singular at zero. But zero cannot occur as a spectral difference under the assumed separation. We may modify the Fourier multiplier near zero to obtain an integrable time weight without changing any frequency needed by the equation.

There is a construction whose total absolute mass is pi divided by twice delta. This number measures the size of the integral kernel; it is not the time for a physical evolution, and it is not the actual cost of our two-coordinate example.

Integrating the weighted unitary orbit of C now reconstructs X. On each pair of spectral values, the Fourier transform supplies exactly one over their difference. In our example the two resulting entries are negative one and positive two.

### From a formula to a norm estimate

Each unitary factor preserves norms, so the size of the transported C never exceeds the size of C. Multiplying by the weight contributes its absolute value. The norm of an operator-valued integral is at most the integral of the norms.

We therefore obtain the operator-norm bound: delta times the norm of X is at most pi over two times the norm of C. The gap need only separate every left spectral value from every right spectral value. It does not impose an order on them.

Notice what the constant records. For the ordered semigroup we integrated a decaying envelope of total mass one over delta. For general separated spectra we use a two-sided oscillatory kernel whose absolute mass is pi over two delta. The latter is a general bound, even though a particular solution may be considerably smaller.

### What survives without eigenvectors

In an infinite-dimensional Hilbert space, a self-adjoint operator need not have a basis of eigenvectors. The finite coefficient story remains a guide, but a proof must use the spectral theorem.

For bounded self-adjoint A and B, approximate each by a finite spectral step operator, assembled from orthogonal spectral projections. Choose step values inside the original spectral sets. That choice preserves the lower bound on every cross-spectral difference.

The weighted integral works on each pair of spectral blocks. As the spectral steps approach A and B in operator norm, their unitary exponentials converge at each fixed time. The same integrable kernel dominates all these integrands. Dominated convergence gives the representation for the original bounded operators.

For unbounded self-adjoint operators, exponential evolution still gives strongly continuous unitary groups, but differentiating requires vectors in the generator's domain. One cannot replace that domain argument by a formal infinite power series. The distinction is between a valid group representation and a derivative identity that is meaningful only on its domain.

### A second Hilbert space made of maps

There is also a useful change of viewpoint. Hilbert-Schmidt maps form a Hilbert space whose squared norm sums the squared magnitudes of matrix entries in orthonormal bases. Left-right unitary transport acts unitarily on this new Hilbert space.

Its generator is i times the Sylvester operator. The spectral differences become the generator's frequencies. In the Hilbert-Schmidt norm, orthogonality of distinct spectral blocks permits a sharper constant-one estimate even when positive and negative differences coexist.

Our small example thus has three readings. Direct division solves it. A semigroup cannot use a single decaying orientation because the differences have opposite signs. The unitary Fourier method handles both signs and gives a general operator-norm bound, while the Hilbert-Schmidt geometry supplies additional square-summable control. The hypotheses on the spectrum and the norm determine which argument is available.

## Disjoint spectral sets and Rosenblum theory

Imagine two spectral values on the left: negative two and positive two. On the right there is just zero. The Sylvester equation asks for a map X such that A X minus X B equals C. Take A to be the diagonal matrix with values negative two and positive two, B equal to zero, and C the column two, four. Entrywise division gives X equal to negative one, two.

That is an easy calculation because A is diagonal. But suppose A has a Jordan block and does not possess enough eigenvectors to diagonalize. Or suppose A acts on an infinite-dimensional Banach space. Can we still divide by the separation between the two spectra?

The answer is yes for bounded complex operators with disjoint spectra. The method is associated with Rosenblum. Its engine is a contour integral of resolvents. The contour allows us to isolate one spectrum from the other without constructing eigenvectors.

### A resolvent is division by a shifted operator

For a scalar a, the number one divided by z minus a is defined whenever z differs from a. Here z may be complex. Replace a by a bounded operator A: the resolvent at z is the inverse of z times identity minus A, wherever that inverse exists.

The collection of z for which the inverse fails is the spectrum. For a nonnormal matrix, a spectral value may belong to a Jordan block; for an infinite-dimensional operator it may fail to be an eigenvalue at all. The resolvent still describes its spectral boundary.

In the complex plane, integrating the scalar function one over z minus a around a counterclockwise loop yields one after dividing by two pi i if a lies inside, and zero if it lies outside. The operator version is a Riesz spectral projection. When the loop surrounds the entire spectrum of A, the resulting projection is the identity.

This is exactly the kind of selector we need: a contour that counts A's spectrum but excludes B's.

### Put the spaces and the factors in order

Let A act on a complex Banach space Y, and B act on a possibly different complex Banach space H. The unknown X and the given C both map H into Y.

At a complex number z outside both spectra, build a map by applying B's resolvent first to a vector in H, then C, then A's resolvent on Y. The order is important: the operator product is the A resolvent, then C, then the B resolvent.

Call that product K of z. Integrate K around a counterclockwise contour that encloses A's spectrum and excludes B's. Divide the integral by two pi i. Our claim is that this operator is the solution X.

The proof comes from one cancellation identity. We can derive it without spectral decompositions.

### Watch the cancellation

For the A resolvent, multiplying by A is the same as multiplying by z and then subtracting the identity. For the B resolvent, multiplying by B on the right is likewise multiplying by z and subtracting the identity.

Apply the Sylvester operator to K. In the first term, A acts on the left resolvent. In the second term, B acts on the right resolvent.

The first substitution creates z times K, minus C followed by the B resolvent. The second creates z times K, minus the A resolvent followed by C. Subtract the second from the first. The two copies of z times K cancel.

What remains is the A resolvent followed by C, minus C followed by the B resolvent.

Now integrate. The normalized integral of the A resolvent is identity because A is enclosed. The normalized integral of the B resolvent is zero because B is excluded. So the integral of that difference is C. The proposed X therefore satisfies A X minus X B equals C.

Notice the work done by each ingredient. Resolvent algebra creates the cancellation. The contour distinguishes the two spectral sets. Neither step asks for orthogonal eigenvectors, real eigenvalues, or an ordering of the spectra.

### The two-loop example

Return to A with diagonal entries negative two and positive two, and B equal to zero. There is no single disk containing both left eigenvalues while excluding zero: a disk is convex, so a disk containing both endpoints also contains their midpoint.

Instead choose two small counterclockwise circles, one around negative two and the other around positive two. Neither contains zero. Add their contour integrals.

For the horizontal component of C, the integrand has a pole at negative two and a harmless factor from the B resolvent. The residue supplies two divided by negative two, which is negative one. The second circle supplies four divided by positive two, which is two. The same two-entry answer appears, now obtained by contour integration.

This is the concrete reason to allow several contour components. A spectral separator need not be a single circle, even for three scalar spectral values.

### What changes for a Jordan block

Consider the upper-triangular matrix with negative two on the diagonal and one immediately above the diagonal. Its only eigenvalue is negative two, yet it has too few eigenvectors for ordinary diagonalization. Keep B equal to zero.

Solving A X equals C with C equal to the column two, four gives X equal to negative two, negative two. The first output includes a contribution from the second entry of C because of the off-diagonal one. A simple rule that divides each entry of C by negative two would miss that coupling.

The contour formula does not miss it. The resolvent of this Jordan block contains both a first-order pole and a second-order pole at negative two. Integrating their residues reproduces the coupling term in the inverse. The details belong in the companion equations, but the lesson is concrete: resolvents know about Jordan structure even when eigenvectors do not provide a basis.

### Why the solution is unique

So far we have shown that the contour recipe produces a solution for every C. We also need to rule out a second solution.

Start with any map Y and form its residual A Y minus Y B. Feed that residual into the contour recipe. Another resolvent cancellation reduces the integrand to the A resolvent followed by Y, minus Y followed by the B resolvent. Integrating gives identity times Y minus Y times zero, which is Y.

Thus the contour recipe recovers any map from its Sylvester residual. If two maps had the same residual, their difference would have residual zero and therefore be zero. Existence and uniqueness hold together.

For bounded complex operators with disjoint compact spectra, one can choose a finite union of suitable contours in the common resolvent set. This yields a bounded inverse of the Sylvester map on the Banach space of bounded cross-operators.

### The size of the inverse is another question

Look again at the example with negative two and positive two. It has a gap of two from zero, and the solution is half as large as C in norm. That numerical statement used the special diagonal matrix.

For a nonnormal operator, resolvent norms can become large far from what a simple spectral-distance picture would suggest. The contour formula gives a bound involving contour lengths and resolvent norms along the curves, not a universal constant-one estimate based only on distance between the two spectral sets.

This separates two questions that are easy to conflate. Disjoint spectra give a unique bounded solution for bounded complex operators. A quantitative error estimate requires additional information about operator geometry and the norm used to measure X and C.

A Riesz projection need not be orthogonal for a nonnormal operator. The contour argument works because its projection algebra is valid, not because it preserves Euclidean lengths. That distinction explains both the breadth of the existence theorem and why norm estimates need separate proofs.

## The Banach-space Sylvester lower-bound theorem

Start with a scalar equation: four times an unknown, minus the unknown itself, equals six. The answer is two. But there is a revealing way to obtain it without dividing by three immediately.

Move the smaller term to the right and divide by four. The unknown equals one and a half plus one quarter of itself. Substitute that formula back into itself. The result is one and a half, plus a quarter of one and a half, plus another quarter of that, and so on. Every correction is one quarter of its predecessor.

The sum converges because the correction shrinks. More importantly, its total size is controlled by the margin between the large coefficient and the small one. Davis and Kahan's Theorem five point one turns this elementary picture into a bound on a map between two Banach spaces.

### Which operator acts on which space?

A Banach space is a complete normed vector space: every Cauchy sequence has a limit in the space. We need two of them because a Sylvester unknown may be rectangular.

Call the input space H and the output space Y. The unknown map T carries vectors from H into Y. A acts on Y, B acts on H, and the known residual C also maps H into Y. The equation is A T minus T B equals C.

We are going to measure T with a norm N. It may be the ordinary operator norm, or a compatible operator ideal norm when the spaces have that additional structure. Only three properties are used: the triangle inequality, scaling by scalars, and control under multiplication on the left and right.

Specifically, if L acts on Y and R acts on H, then N of L T R is at most the operator norm of L, times N of T, times the operator norm of R. Think of this as a rule against magnifying T more than the two outside multipliers can magnify it.

For the ordinary operator norm this follows by applying the composite to a unit vector. For a Schatten norm on Hilbert spaces it follows from the ideal property. For arbitrary Banach spaces it must be an explicit assumption; there is no basis-independent Frobenius norm available for every Banach space.

### Identify the contraction

Assume B has operator norm at most gamma, where gamma is nonnegative. Assume A has a bounded inverse, whose norm is at most one over gamma plus delta, for some positive delta.

Why these two bounds? Apply the inverse of A to the equation. The result is T equals A inverse C plus A inverse T B. This is the operator version of our scalar geometric-series equation.

The first term is the known starting point. The second term is the correction, which takes any map T, applies B before it and A inverse after it. By compatibility, its size is at most gamma over gamma plus delta times the size of T.

That ratio is strictly less than one. We have identified a contraction on the space of cross-operators. The number delta is the leftover margin that makes contraction possible.

### Derive the constant-one estimate

Apply the norm N to the fixed-point identity. The triangle inequality bounds N of T by N of A inverse C plus N of A inverse T B.

Use the two-sided multiplication rule. The first term is at most N of C divided by gamma plus delta. The second is at most gamma over gamma plus delta times N of T.

Now gather the unknown terms. Multiply by gamma plus delta, and move gamma times N of T to the left. Precisely delta times N of T remains. The result is delta times N of T at most N of C.

No matrix size appears. We did not compare Frobenius and operator norms or count eigenvalues. The constant is one because the same contraction margin, delta, appears when the unknown term is moved across the inequality.

This estimate applies to any solution T that satisfies the equation. To obtain a solution from scratch, use the geometric series of repeated correction maps. In the ordinary bounded-operator norm, the space of cross-operators is complete, so that series converges. In an operator ideal, convergence in its own norm requires the ideal to be complete and stable under the multiplications used here.

### Revisit a two-sided spectral example

Now use a concrete example with spectral values on both sides of zero. Let the input space be one-dimensional and B equal to zero. Let A on the output plane be diagonal with entries negative two and positive two. Let C send one to the column two, four.

The inverse of A is diagonal with entries negative one half and positive one half. Its norm is one half. Choose gamma equal to zero and delta equal to two. Our contraction has ratio zero, because B is zero, and the geometric series stops after its first term.

Applying A inverse gives T with entries negative one and positive two. Its length is the square root of five. The length of C is twice the square root of five. Thus delta times the norm of T equals the norm of C, an exact instance of the constant-one estimate.

Here the spectral values of A straddle B. We did not need an ordered gap. We needed a controlled inverse of A relative to the small norm of B.

### Shifting the center of the picture

The equation does not change if the same scalar c is subtracted from A and B. The extra terms are negative c times T on both sides of the Sylvester difference, so they cancel.

This lets us move the center of a spectral picture to zero. Suppose B is self-adjoint with spectrum inside an interval of radius gamma around c. Then B minus c identity has norm at most gamma.

Suppose A is self-adjoint and every spectral value lies at least gamma plus delta away from c. Then A minus c identity has a bounded inverse with norm at most one over gamma plus delta. Apply the same contraction proof to these shifted operators.

Geometrically, the B spectrum is contained in a central interval while the A spectrum stays outside a larger interval. A may lie to the left, to the right, or on both sides. This is the interval-versus-exterior situation. The ordinary ordered semigroup proof cannot handle both sides simultaneously, but the bounded-inverse proof can.

### Spectral separation is not enough on a Banach space

The hypotheses refer to an inverse norm, not merely a distance to the spectrum. That difference is decisive when operators are nonnormal.

For example, take an upper-triangular two-by-two matrix with diagonal entries one and a very large upper-right entry. Its only spectral value is one, at distance one from zero. Yet its inverse has a correspondingly large off-diagonal entry, and its norm can be much greater than one.

Thus knowing that the spectrum of A stays away from zero does not ensure the inverse norm bound used by this theorem. For self-adjoint operators on Hilbert spaces, spectral calculus supplies the reciprocal-distance formula. For arbitrary Banach operators, the theorem insists on the actual inverse estimate.

There is also a useful refinement. The inequality itself only needs a bounded left inverse L of A, meaning L A is identity. In the fixed-point derivation, nothing uses A L equal to identity. The original printed hypothesis includes a two-sided inverse, and the reusable result can be stated under the weaker explicit left-inverse condition.

A lower bound on vector lengths does not automatically supply such an everywhere-defined bounded left inverse on a general Banach space: the range may lack a bounded complement. State the inverse data rather than assume it.

### What has been established

The estimate attributed to Theorem five point one concerns a solution that is already given. Under its bounded-inverse and compatible-norm hypotheses, the residual C controls the unknown T with constant one and margin delta. A separate contraction argument can construct the solution when the relevant operator space is complete.

The same two-sided spectral example can therefore support several different conclusions. Spectral separation alone ensures invertibility in the bounded complex Rosenblum setting. A quantitative inverse-norm condition supplies this constant-one estimate. The distinction is worth retaining whenever a spectral gap appears in the denominator of a subspace perturbation theorem.

## Norm dependence of Sylvester bounds

Suppose two operators have no spectral values closer than two units. You might reasonably expect that solving a Sylvester equation divides the size of its residual by at least two. In a one-column example that intuition is exactly right.

Let A be diagonal on the plane, with values negative two and positive two, and B be zero on the input line. With C equal to the column two, four, the solution X has entries negative one and positive two. The output length is precisely half the residual length.

But now change the input space from a line to a plane. The unknown becomes a full matrix. Even if every individual coefficient is divided by a spectral difference of magnitude at least one, its operator norm can behave differently from the sum of the squares of its entries. This is why any claim about a Sylvester gap must name both the gap configuration and the norm.

### Three ways to measure the same matrix

The operator norm asks: among unit input vectors, which one is stretched the most? It is the largest singular value.

The Hilbert-Schmidt, or Frobenius, norm takes the square root of the total sum of squared entry magnitudes in orthonormal coordinates. Equivalently it takes the square root of the sum of squares of the singular values. It measures total energy over independent directions.

The nuclear norm adds the singular values without squaring. These norms agree on the absolute value of a one-by-one matrix. For matrices with multiple independent directions, they need not agree at all.

That is the first lesson of our column example. Its operator norm and Hilbert-Schmidt norm happen to coincide because a column has rank one. It cannot reveal the difficulty that arises with a full matrix.

### What every cross-spectral denominator guarantees

Let A and B be finite-dimensional self-adjoint matrices, and suppose every difference between their respective eigenvalues has absolute value at least delta, with delta positive.

Choose orthonormal eigenbases. In those coordinates, the equation A X minus X B equals C says that each coefficient of X equals the matching coefficient of C divided by its left eigenvalue minus its right eigenvalue.

For each coefficient, its squared magnitude in X is at most one over delta squared times the squared magnitude in C. Add these inequalities across all pairs of eigenvectors. Taking the square root gives delta times the Hilbert-Schmidt norm of X at most the Hilbert-Schmidt norm of C.

The spectral values may interlace. Some differences may be positive and others negative. Absolute squares remove that sign issue. The estimate is sharp, because a single pair of eigenvectors with separation exactly delta attains equality.

Pause at the key step: summing squared coefficients is exactly how the Hilbert-Schmidt norm works. There is no analogous step that sums independent coefficientwise estimates into a sharp operator-norm inequality.

### A two-by-two matrix that defeats constant one

Let A have diagonal entries positive one and negative one. Let B have diagonal entries zero and two. The two spectra are disjoint, and every cross difference has magnitude at least one. The gap delta is one.

Choose X to be the symmetric matrix whose first row is three, negative three, and whose second row is negative three, one. Form the residual C by multiplying X on the left by A and subtracting X multiplied on the right by B.

The result C has rows three, three, and three, negative three. Its columns are perpendicular and have the same length. As a consequence, C stretches every unit direction by three times the square root of two, approximately four point two four.

Now examine X. Its largest absolute eigenvalue is two plus the square root of ten, about five point one six. A unit vector aligned with that eigenvector is stretched by X more than any unit input direction is stretched by C.

So the operator norm of X exceeds the operator norm of C, even though every entry of X was obtained by dividing by a denominator of absolute value at least one.

Nothing contradicts the coefficientwise argument. The Frobenius norm of X is the square root of twenty-eight; the Frobenius norm of C is six. The square-norm inequality still holds. The counterexample isolates the false step: translating independent coefficient bounds into a constant-one claim about maximum directional amplification.

### Recovering a rank-dependent operator estimate

There is a safe route from the square norm to the operator norm, but it has a price. The operator norm of X is at most its Hilbert-Schmidt norm. And if C has rank r, the Hilbert-Schmidt norm of C is at most the square root of r times its operator norm.

Chaining these facts gives delta times the operator norm of X at most the square root of r times the operator norm of C. The rank factor belongs to the norm comparison, not to the underlying spectral division.

In the two-by-two counterexample, r is two. A factor of the square root of two is more than enough to accommodate the observed increase. But for large rank, that estimate grows with dimension and may be wasteful.

### Two ways to obtain dimension-free control

Return to the spectral picture. If all left eigenvalues lie at least delta above all right eigenvalues, there is a single orientation in which the exponential transport decays. Integrating that decay gives the operator-norm inequality with constant one. The same argument works for compatible ideal norms because left and right multiplication obey their ideal estimates.

There is also the interval-versus-exterior picture. After a common scalar shift, suppose B has norm at most gamma and A has a bounded inverse of norm at most one over gamma plus delta. The fixed-point identity then gives constant one. In a self-adjoint Hilbert setting, the spectral theorem can supply those inverse bounds from a central interval and an exterior set.

Our original column with left values negative two and positive two and right value zero belongs to the interval-versus-exterior setting, even though it is not ordered. Its constant-one behavior has an explanation stronger than pairwise separation alone.

### A universal Fourier estimate for pairwise gaps

For bounded self-adjoint A and B under arbitrary pairwise separation, use their unitary groups instead. Weight the left-right evolution by an integrable scalar function whose Fourier transform divides by the spectral differences.

Unitary multiplication preserves operator norms. The norm of the weighted integral is therefore controlled by the absolute integral of the scalar kernel. A suitable kernel has mass pi divided by twice delta. This yields delta times the operator norm of X at most pi over two times the operator norm of C, without any rank factor.

The same integral argument applies to suitable compatible unitarily invariant ideal norms. It provides a general bound. It does not change the fact that in the Hilbert-Schmidt norm, orthogonal spectral blocks already give the better constant one.

### What to carry into a subspace theorem

An angle estimate often comes from dividing a projected residual by a spectral separation. Before choosing the division theorem, identify the two compressed operators, locate their spectra, and decide which norm is measuring the unknown cross block.

If the proof squares and sums spectral coefficients, the natural output is a Hilbert-Schmidt estimate. If it needs the largest directional error, the operator norm is relevant, and pairwise separation alone cannot justify constant one. Ordered decay, central-interval inverse bounds, or a Fourier multiplier each come with their own hypotheses.

A spectral gap controls division; the chosen norm determines how the divided coefficients can be combined. Both decisions are needed for a correct bound.

## Hilbert–Schmidt Sylvester group estimates

Take a column map C with entries two and four. Let A on the output plane have eigenvalues negative two and positive two, while B on the input line is zero. To solve A X minus X B equals C, divide the two coordinates by their spectral differences. The answer X is the column negative one, two.

The length of C is twice the square root of five. The length of X is the square root of five. Their ratio reflects the spectral gap of two. In this column example there is only one input direction, so the ordinary operator norm and the Hilbert-Schmidt norm happen to agree.

With more columns, the Hilbert-Schmidt norm has a special advantage. It treats the entries of a matrix as orthogonal coordinates of a new vector. Once we make that change of viewpoint, the Sylvester equation becomes an ordinary self-adjoint operator equation on a Hilbert space of maps.

### Treat rectangular maps as vectors

Consider a two-by-three complex matrix. It is a map from three-dimensional input space to two-dimensional output space. But it can also be seen as a vector with six complex coordinates.

Its Hilbert-Schmidt norm is the square root of the sum of the squared magnitudes of those six entries. We can define an inner product of two matrices by summing the conjugate of each entry of the first times the corresponding entry of the second.

Why is this useful? Imagine separating a matrix into blocks by orthogonal output and input projections. Blocks belonging to different pairs of projections are perpendicular in this matrix Hilbert space. The total squared norm is exactly the sum of their squared norms.

For the two-by-two matrix with entries one, two, three, four, that total squared norm is one plus four plus nine plus sixteen, or thirty. Rearranging it into individual entry blocks does not change the sum. Operator norm, which asks for the single most stretched input direction, has no such additivity rule.

### The Sylvester map is self-adjoint here

Let A be bounded and self-adjoint on the output Hilbert space and B bounded and self-adjoint on the input Hilbert space. Define a new operator on Hilbert-Schmidt maps: send Z to A Z minus Z B. Call it the Sylvester map S.

We can move A from one argument of the Hilbert-Schmidt inner product to the other, because A equals its adjoint. We can do the same for B. The minus sign stays attached to the right multiplication. Therefore S is self-adjoint on this Hilbert space of maps.

This is a change in the level at which we apply spectral theory. A and B act on ordinary vectors in different spaces. S acts on entire cross-space operators, and its spectral values describe differences between the spectral values of A and B.

### One rank-one map at a time

In finite dimensions choose an orthonormal eigenbasis for A and another for B. Pick one output eigenvector u, with eigenvalue a, and one input eigenvector v, with eigenvalue b.

Build a rank-one map that measures how much an input points along v, and produces that multiple of u. Apply the Sylvester map to this rank-one operator. Left multiplication by A gives a copies of the map. Right multiplication by B gives b copies. Their difference is a minus b copies.

So the rank-one map is an eigenvector of S, with eigenvalue a minus b. All pairs of eigenvectors give an orthonormal basis for the Hilbert space of matrices.

In the running column example, there are two such rank-one maps and their Sylvester eigenvalues are negative two and positive two. A spectral gap around zero for S is exactly the assertion that neither cross difference is too small.

### Prove the square-norm gap estimate

Suppose every cross-spectral difference has absolute value at least delta, where delta is positive. Expand any matrix Z in the rank-one eigenbasis. The Sylvester map multiplies each coefficient by its own difference a minus b.

Square the Hilbert-Schmidt norm after applying S. Each coefficient contributes its original squared magnitude times the square of that difference. Every multiplier is at least delta squared. Add over all coefficients, and take a square root.

The result says: the Hilbert-Schmidt norm of S Z is at least delta times the Hilbert-Schmidt norm of Z. If S X equals C, this becomes delta times the Hilbert-Schmidt norm of X at most the Hilbert-Schmidt norm of C.

Notice why the constant is one. We used a spectral lower bound on each orthogonal coordinate and then added squares. We never inserted a comparison between different matrix norms.

For our column, delta is two, and the estimate is an equality. In a full matrix with interlaced spectra, it remains valid even when the same constant-one statement in operator norm fails. The proof has not changed; the definition of the norm is doing essential work.

### A unitary group on the space of maps

There is a dynamical way to view the same self-adjoint Sylvester map. Evolve a map Z by multiplying it on the left with the exponential of i times t A, and on the right with the exponential of negative i times t B.

Because both factors are unitary, this evolution preserves the Hilbert-Schmidt inner product. Applying time s and then time t is the same as evolving for s plus t. We have a unitary group acting on a space whose vectors happen to be operators.

For bounded A and B, differentiating at zero gives i times A Z minus Z B, or i times S Z. So S is the self-adjoint generator after removing i. Its spectral gap is the cross-spectral gap between A and B.

This viewpoint replaces entrywise manipulation with spectral theory for a single operator. It also explains the appearance of the same left-right evolution in Fourier representations of Sylvester inverses.

### Extend from matrices to infinite dimensions

An infinite-dimensional bounded operator need not be Hilbert-Schmidt. The identity map on a countably infinite-dimensional Hilbert space sends every basis vector to a vector of length one, so the sum of squared output lengths diverges.

Hilbert-Schmidt operators form a complete Hilbert space in their own norm. Left or right multiplication by a bounded operator preserves this class, and unitary multiplications preserve its inner product.

For bounded self-adjoint A and B, we can define the same self-adjoint Sylvester map on that Hilbert-Schmidt space. We cannot expect ordinary eigenvectors of A and B to span everything when their spectra have continuous parts. Instead, use their spectral projections onto narrow bands.

A block of an operator connecting one output band to one input band is almost multiplied by the difference of the two band centers. The approximation error is controlled by the band widths. Blocks for different pairs of spectral bands are orthogonal in Hilbert-Schmidt norm.

As the bands narrow, the approximate scalar differences give the same lower bound. One may express this more directly with the spectral measure of S: the entire spectrum of S stays at least delta away from zero when the two original spectra are separated by delta.

The gap then makes S invertible on the Hilbert-Schmidt space, with inverse norm at most one over delta.

### When the known solution was only bounded

There is a further issue worth distinguishing from the inequality. Suppose C is Hilbert-Schmidt but someone has handed us a merely bounded solution X of the Sylvester equation. Are we allowed to apply a Hilbert-Schmidt estimate to X before knowing that X is Hilbert-Schmidt?

No. First construct a Hilbert-Schmidt solution Y using the inverse of S on the Hilbert-Schmidt space. This Y also solves the equation as a bounded cross-operator. For bounded operators A and B with disjoint spectra, the bounded Sylvester solution is unique. Hence X equals Y, and X is Hilbert-Schmidt after all. Only then apply the square-norm estimate.

This order prevents a common circular argument: assuming ideal membership in order to prove ideal membership.

For unbounded self-adjoint A or B, the unitary groups remain strongly continuous, but their generator lives on a specified domain. One must prove domain compatibility of the Sylvester expression and use the appropriate closed generator; a formula using A Z and Z B cannot automatically be applied to every Hilbert-Schmidt Z.

### What the estimate gives a subspace problem

If a projected subspace error X satisfies a Sylvester equation, its residual C is the known quantity. The spectral gap for the two compressed coefficients controls the Hilbert-Schmidt size of X without a dimension factor.

The geometric interpretation of X then converts that estimate into an angle bound. But the intermediate step is still a theorem about the space of Hilbert-Schmidt maps. It is the square-sum structure, rather than a generic appeal to spectral distance, that provides the constant-one estimate under arbitrary pairwise separation.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Unitary and semigroup representations

**Draft status:** audio-first mathematical lecture. **Prerequisites:** `039000–041000` exponentials and unitary flows; `063000–065000` Sylvester equations and ordered semigroups. **Next:** Rosenblum's contour method.

---

#### Companion: mathematics and Lean correspondence (display only)

For bounded self-adjoint \(A,B\), set \(U_A(t)=e^{itA}\), \(U_B(t)=e^{itB}\). Then
\[
\frac d{dt}\bigl(U_A(t)XU_B(-t)\bigr)
=iU_A(t)(AX-XB)U_B(-t).
\]
For \(\operatorname{dist}(\sigma(A),\sigma(B))\ge\delta>0\), choose \(\mu_\delta\in L^1(\mathbb R,\mathbb C)\) with
\[
\int_\mathbb R \mu_\delta(t)e^{it\omega}\,dt=\omega^{-1}
\quad(|\omega|\ge\delta),\qquad
\|\mu_\delta\|_{L^1}=\frac{\pi}{2\delta}.
\]
Then the separated-spectrum Sylvester inverse has representation
\[
X=\int_\mathbb R\mu_\delta(t)e^{itA}Ce^{-itB}\,dt,
\qquad \|X\|\le\frac\pi{2\delta}\|C\|.
\]
The source proves bounded infinite-dimensional reconstruction using finite spectral step approximations and dominated convergence. Compare `065000` for the better constant-one ordered case.

**One column through both signs.** With
\[
 A=\operatorname{diag}(-2,2),\quad B=[0],\quad
 C=\begin{bmatrix}2\\4\end{bmatrix},\quad
 X=\begin{bmatrix}-1\\2\end{bmatrix},
\]
we have \(AX-XB=C\), \(\delta=2\),
\(\|C\|=2\sqrt5\), and \(\|X\|=\sqrt5\).
The two spectral differences are \(-2\) and \(2\), with reciprocal multipliers
\(-\tfrac12\) and \(\tfrac12\). This particular column attains
\(\delta\|X\|=\|C\|\) even though the general operator-norm Fourier bound is
\(\delta\|X\|\le(\pi/2)\|C\|\). The universal upper bound need not be sharp
for a given pair of operators.

**Ordered comparison.** If \(A\ge aI\), \(B\le bI\), and \(a-b\ge\delta>0\),
then for bounded self-adjoint \(A,B\),
\[
 X=\int_0^\infty e^{-tA}Ce^{tB}\,dt,
 \quad \|e^{-tA}Ce^{tB}\|\le e^{-\delta t}\|C\|.
\]
The integral is operator-norm convergent. The two-sided example does not
satisfy this ordering, although its spectra are pairwise separated.

**Lean bridge (verbatim source excerpts).**

`DavisKahan/InfiniteDimensional/Sylvester/FourierSemigroup.lean` — `separatedSylvesterMultiplier_identity`:

```lean
theorem separatedSylvesterMultiplier_identity
    (d : ℝ) (hd : 0 < d) (a b : ℝ) (hab : d ≤ |a - b|) :
    (∫ t : ℝ, separatedSylvesterMultiplier d hd t *
      Complex.exp ((((t * (a - b) : ℝ) : ℂ) * Complex.I))) =
      (((a - b)⁻¹ : ℝ) : ℂ) := by
```

The complex Fourier identity supplies reciprocal spectral differences outside the gap.

`DavisKahan/InfiniteDimensional/Sylvester/FourierSemigroup.lean` — `l1_norm_separatedSylvesterMultiplier`:

```lean
theorem l1_norm_separatedSylvesterMultiplier (d : ℝ) (hd : 0 < d) :
    (∫ t : ℝ, ‖separatedSylvesterMultiplier d hd t‖) =
      Real.pi / (2 * d) := by
```

The exact scalar `L¹` mass produces the `π/2` constant; this is distinct from the ordered exponential estimate.

`DavisKahan/InfiniteDimensional/Sylvester/FourierSemigroup.lean` — `separatedSylvester_reconstruction_complex`:

```lean
theorem separatedSylvester_reconstruction_complex
    {A : F →L[ℂ] F} {B : E →L[ℂ] E}
    (hA : A.IsSymmetric) (hB : B.IsSymmetric)
    {d : ℝ} (hd : 0 < d) (hsep : SpectraSeparated A ⊤ B ⊤ d)
    (X C : E →L[ℂ] F)
    (hEq : A ∘L X - X ∘L B = C) :
    X = ∫ t : ℝ, separatedSylvesterMultiplier d hd t •
      (unitaryGroup A t ∘L C ∘L unitaryGroup B (-t)) := by
```

The complex Hilbert-space theorem reconstructs a known solution using unitary conjugation and a pairwise spectral gap. The finite spectral-step limit appears in its proof.

### Disjoint spectral sets and Rosenblum theory

**Draft status:** audio-first mathematical lecture. **Prerequisites:** `008000` resolvents; `030000` spectral projections; `063000–066000` Sylvester inversion and integral representations. **Next:** the Banach-space Theorem 5.1 lower bound.

---

#### Companion: mathematics and Lean correspondence (display only)

For \(R_A(z)=(zI-A)^{-1}\) and \(R_B(z)=(zI-B)^{-1}\),
\[
A\bigl(R_A(z)CR_B(z)\bigr)-\bigl(R_A(z)CR_B(z)\bigr)B
=R_A(z)C-CR_B(z).
\]
If a positively oriented contour \(\Gamma\) lies in the common resolvent set, encloses \(\sigma(A)\) and excludes \(\sigma(B)\), then
\[
X=\frac1{2\pi i}\oint_\Gamma R_A(z)CR_B(z)\,dz,
\qquad AX-XB=C.
\]
The complementary identity \(R_A(z)(AX-XB)R_B(z)=R_A(z)X-XR_B(z)\) proves uniqueness. The cited Lean existence/uniqueness theorem uses one positively oriented separating **circle**; general disjoint compact spectra may require a union of contour components, not covered by that exact theorem statement.

**Two-component contour.** For
\[
A=\begin{bmatrix}-2&0\\0&2\end{bmatrix},\quad B=[0],\quad
C=\begin{bmatrix}2\\4\end{bmatrix},
\]
choose \(\Gamma=\Gamma_{-2}+\Gamma_{2}\), the sum of two positively
oriented circles with radius smaller than 2. They surround \(\sigma(A)\)
but have winding number zero about \(\sigma(B)=\{0\}\). Then
\[
X=\frac{1}{2\pi i}\int_{\Gamma}(zI-A)^{-1}C(zI-B)^{-1}\,dz
=\begin{bmatrix}2/(-2)\\4/2\end{bmatrix}
=\begin{bmatrix}-1\\2\end{bmatrix}.
\]
A single disk enclosing both \(-2\) and \(2\) must contain \(0\), so two
contour components (or a noncircular separator with suitable winding) are
needed.

**Nonnormal Jordan check.** With
\[
A_J=\begin{bmatrix}-2&1\\0&-2\end{bmatrix},\quad B=[0],\quad
C=\begin{bmatrix}2\\4\end{bmatrix},\quad
A_J^{-1}=\begin{bmatrix}-\tfrac12&-\tfrac14\\0&-\tfrac12\end{bmatrix},
\]
we obtain \(X=A_J^{-1}C=(-2,-2)^\mathsf T\). The resolvent is
\[
(zI-A_J)^{-1}=\begin{bmatrix}(z+2)^{-1}&(z+2)^{-2}\\0&(z+2)^{-1}\end{bmatrix}.
\]
The second-order pole contributes the off-diagonal inverse term. This is
why dividing individual entries by the eigenvalue is invalid for a Jordan block.

**Lean bridge (verbatim source excerpts).**

`DavisKahan/Sylvester/RosenblumExistence.lean` — `rosenblumSolution`:

```lean
noncomputable def rosenblumSolution (A : E →L[ℂ] E) (B : F →L[ℂ] F)
    (C : F →L[ℂ] E) (center radius : ℝ) : F →L[ℂ] E :=
  (2 * Real.pi * Complex.I)⁻¹ •
    ∮ z in C((center : ℂ), radius), rosenblumIntegrand A B C z
```

The concrete contour solver uses circle integrals and bounded complex Banach-space operators.

`DavisKahan/Sylvester/RosenblumExistence.lean` — `existsUnique_comp_sub_comp_eq`:

```lean
theorem existsUnique_comp_sub_comp_eq (hr : 0 < radius)
    (hA : spectrum ℂ A ⊆ ball ((center : ℂ)) radius)
    (hB : ∀ z : ℂ, z ∈ closedBall ((center : ℂ)) radius → z ∉ spectrum ℂ B) :
    ∃! S : F →L[ℂ] E, A ∘L S - S ∘L B = C := by
```

The theorem proves both existence and uniqueness when **one circle** encloses the spectrum of `A` and its closed disk excludes the spectrum of `B`. It does not directly state the arbitrary-contour version.

### The Banach-space Sylvester lower-bound theorem

**Draft status:** audio-first mathematical lecture. **Prerequisites:** `004000–005000` bounded operators and their algebra; `057000–058000` compatible operator norms; `064000–067000` Sylvester invertibility and spectral separation. **Next:** norm dependence of Sylvester bounds.

---

#### Companion: mathematics and Lean correspondence (display only)

Davis–Kahan (1970), Theorem 5.1, in its printed inverse formulation: for \(T,C\in\mathcal B(X,Y)\), \(AT-TB=C\), and a compatible cross-operator norm \(N\), assume
\[
\gamma\ge0,\quad\delta>0,\quad\|B\|\le\gamma,\quad
A^{-1}\in\mathcal B(Y),\quad\|A^{-1}\|\le(\gamma+\delta)^{-1}.
\]
Then
\[
\delta N(T)\le N(C).
\]
The fixed point \(T=A^{-1}C+A^{-1}TB\) and the ideal inequality give
\[
N(T)\le(\gamma+\delta)^{-1}N(C)
+\gamma(\gamma+\delta)^{-1}N(T).
\]
The reusable strengthened theorem needs only a *bounded left inverse*; the printed statement includes a two-sided inverse. A lower bound \(\|Ay\|\ge c\|y\|\) on an arbitrary Banach space need not provide a bounded everywhere-defined left inverse without further hypotheses.

**Contraction and example.** Set \(\mathcal K(T)=A^{-1}TB\). The hypotheses give
\[
N(\mathcal K T)\le\frac{\gamma}{\gamma+\delta}N(T),\qquad
T=(I-\mathcal K)^{-1}(A^{-1}C)
=\sum_{n=0}^\infty\mathcal K^n(A^{-1}C),
\]
where the series assertion requires completeness of the chosen normed space
and a two-sided inverse to recover the Sylvester equation from the fixed point.
In the printed theorem, \(A^{-1}\) is two-sided; the **estimate alone** also
holds with an explicitly supplied bounded left inverse.

For \(A=\operatorname{diag}(-2,2)\), \(B=[0]\), and
\(C=(2,4)^\mathsf T\), choose \(\gamma=0,\delta=2\). Then
\[
T=A^{-1}C=(-1,2)^\mathsf T,\qquad
\delta\|T\|=2\sqrt5=\|C\|.
\]
A nonnormal counterpoint is \(A_M=\begin{bmatrix}1&M\\0&1\end{bmatrix}\),
\(A_M^{-1}=\begin{bmatrix}1&-M\\0&1\end{bmatrix}\): its spectrum is
\(\{1\}\), while \(\|A_M^{-1}\|\ge\sqrt{1+M^2}\) by applying it to the
second coordinate vector.

**Lean bridge (verbatim source excerpts).**

`DavisKahan/Sources/DavisKahan1970/Section5BanachSylvester.lean` — `theorem5_1_banach_sylvester_exact`:

```lean
theorem theorem5_1_banach_sylvester_exact
    (N : CompatibleCrossOperatorNorm (𝕜 := 𝕜) (X := X) (Y := Y))
    (A Ainv : Y →L[𝕜] Y) (B : X →L[𝕜] X)
    (T C : X →L[𝕜] Y) {gamma delta : ℝ}
    (hgamma : 0 ≤ gamma) (hdelta : 0 < delta)
    (hB : ‖B‖ ≤ gamma)
    (hAinv_left : Ainv ∘L A = ContinuousLinearMap.id 𝕜 Y)
    (_hAinv_right : A ∘L Ainv = ContinuousLinearMap.id 𝕜 Y)
    (hAinv_norm : ‖Ainv‖ ≤ (gamma + delta)⁻¹)
    (hEq : A ∘L T - T ∘L B = C) :
    delta * N T ≤ N C := by
```

This is the printed two-sided inverse hypothesis: `Ainv` cancels `A` on both sides, `‖Ainv‖ ≤ (gamma + delta)⁻¹`, `‖B‖ ≤ gamma`, and `N` is a compatible cross-operator norm.

`DavisKahan/Sources/DavisKahan1970/Section5BanachSylvester.lean` — `theorem5_1_banach_sylvester`:

```lean
theorem theorem5_1_banach_sylvester
    (N : CompatibleCrossOperatorNorm (𝕜 := 𝕜) (X := X) (Y := Y))
    (A : Y →L[𝕜] Y) (B : X →L[𝕜] X)
    (T C : X →L[𝕜] Y) {gamma delta : ℝ}
    (hgamma : 0 ≤ gamma) (hdelta : 0 < delta)
    (hB : ‖B‖ ≤ gamma)
    (hleft : BoundedLeftInverseData A (gamma + delta)⁻¹)
    (hEq : A ∘L T - T ∘L B = C) :
    delta * N T ≤ N C := by
```

The reusable result only needs the explicitly supplied **bounded left inverse** data; that is a stronger theorem than the printed version. Neither theorem requires an inner-product structure.

### Norm dependence of Sylvester bounds

**Draft status:** audio-first mathematical lecture. **Prerequisites:** `052000–058000` singular values and operator ideals; `063000–068000` Sylvester equations and their integral/inverse estimates. **Next:** Hilbert–Schmidt Sylvester group estimates.

---

#### Companion: mathematics and Lean correspondence (display only)

Let \(A,B\) be bounded self-adjoint operators and let \(AX-XB=C\). Comparison by hypothesis and norm:

| Gap geometry | Norm | Supported estimate |
|---|---|---|
| Pairwise \(|a-b|\ge\delta\) | Hilbert–Schmidt | \(\delta\|X\|_{S_2}\le\|C\|_{S_2}\) |
| Pairwise, \(\operatorname{rank}(C)\le r\) | Operator | \(\delta\|X\|\le\sqrt r\|C\|\) |
| Pairwise | Operator | \(\delta\|X\|\le\tfrac\pi2\|C\|\) via the Fourier kernel |
| Ordered | Operator, compatible ideals | \(\delta N(X)\le N(C)\) via semigroup decay |
| Bounded inverse \(\|A^{-1}\|\le(\gamma+\delta)^{-1}\), \(\|B\|\le\gamma\) | Compatible Banach cross-operator norm | \(\delta N(X)\le N(C)\) |

The real symmetric source witness has
\[
A=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\quad
B=\begin{pmatrix}0&0\\0&2\end{pmatrix},\quad
X=\begin{pmatrix}3&-3\\-3&1\end{pmatrix},\quad
C=\begin{pmatrix}3&3\\3&-3\end{pmatrix}.
\]
For \(\delta=1\), \(\|X\|=2+\sqrt{10}>3\sqrt2=\|C\|\), refuting a constant-one pairwise-gap operator-norm claim.

**Shared scalar example and the matrix obstruction.** With
\(A=\operatorname{diag}(-2,2)\), \(B=[0]\), and \(C=(2,4)^\mathsf T\),
\(X=(-1,2)^\mathsf T\) and \(\delta\|X\|_2=\|C\|_2=2\sqrt5\).
For the interlaced two-by-two witness already displayed above,
\[
\|X\|_{S_2}^2=3^2+(-3)^2+(-3)^2+1^2=28,
\qquad \|C\|_{S_2}^2=36.
\]
Thus \(\|X\|_{S_2}\le\|C\|_{S_2}\) with \(\delta=1\), while
\(\|X\|_{op}=2+\sqrt{10}>3\sqrt2=\|C\|_{op}\). The example separates
the two *norm* claims without altering the spectral configuration.

**Lean bridge (verbatim source excerpts).**

`DavisKahan/Sources/DavisKahan1970/Sylvester/OperatorNormEstimate.lean` — `opNorm_sylvester_le_of_pairwiseSpectrumGap`:

```lean
theorem opNorm_sylvester_le_of_pairwiseSpectrumGap
    {E F : Type v}
    [NormedAddCommGroup E] [InnerProductSpace ℂ E] [CompleteSpace E]
    [NormedAddCommGroup F] [InnerProductSpace ℂ F] [CompleteSpace F]
    {A : E →ₗ.[ℂ] E}
    {B : F →ₗ.[ℂ] F}
    {X C : F →L[ℂ] E}
    (hA : IsSelfAdjoint A) (hB : IsSelfAdjoint B)
    {δ : ℝ} (hδ : 0 < δ)
    (hgap : PairwiseSpectrumGap A B δ)
    (hEq : _root_.LinearPMap.SylvesterEquation A B X C)
    {r : ℕ} (hRank : C.rank ≤ (r : Cardinal)) :
    δ * ‖X‖ ≤ ‖C‖ * Real.sqrt r := by
```

The theorem derives the rank-dependent operator-norm bound from the Hilbert–Schmidt estimate. It applies to self-adjoint partial operators and a finite-rank right-hand side.

`DavisKahan/Sources/DavisKahan1970/Sylvester/OperatorNormEstimate.lean` — `sharp52_constant_one_too_small`:

```lean
theorem sharp52_constant_one_too_small :
    ‖sharpC52.toContinuousLinearMap‖ < 1 * ‖sharpX52.toContinuousLinearMap‖ := by
```

This is the exact counterexample showing that constant one fails for the operator norm under merely pairwise separation.

`DavisKahan/InfiniteDimensional/Sylvester/FourierSemigroup.lean` — `mul_l1_norm_separatedSylvesterMultiplier`:

```lean
theorem mul_l1_norm_separatedSylvesterMultiplier (d : ℝ) (hd : 0 < d) :
    d * (∫ t : ℝ, ‖separatedSylvesterMultiplier d hd t‖) = Real.pi / 2 := by
```

The source proves the exact `π/2` mass of the reciprocal Fourier multiplier, which underwrites the corresponding universal operator-norm upper bound.

### Hilbert–Schmidt Sylvester group estimates

**Draft status:** audio-first mathematical lecture. **Prerequisites:** `057000` Schatten and Frobenius norms; `062000–069000` Sylvester equations and spectral gap estimates. **Next:** `071000` Sylvester identities for compressed blocks.

---

#### Companion: mathematics and Lean correspondence (display only)

For finite Hilbert spaces, equip rectangular maps with
\[
\langle Z,W\rangle_{HS}=\operatorname{tr}(Z^*W),\qquad
\mathscr S(Z)=AZ-ZB.
\]
For self-adjoint \(A,B\), the induced \(\mathscr S\) is self-adjoint; on rank-one eigenblocks \(u_i v_j^*\) it has eigenvalue \(a_i-b_j\). Hence, under \(\operatorname{dist}(\sigma(A),\sigma(B))\ge\delta>0\),
\[
\|\mathscr S Z\|_{HS}^2=\sum_{i,j}|a_i-b_j|^2|z_{ij}|^2
\ge\delta^2\|Z\|_{HS}^2.
\]
For infinite-dimensional Hilbert spaces, the spectral-block and unitary-group construction replaces the finite eigenbasis. The source theorem also proves Hilbert–Schmidt membership of a bounded solution when the defect has finite energy.

**The same exact column in the matrix-Hilbert-space picture.** For
\[
 A=\operatorname{diag}(-2,2),\quad B=[0],\quad
 C=(2,4)^\mathsf T,\quad X=(-1,2)^\mathsf T,
\]
we have \(\mathscr S(X)=AX-XB=C\) and
\[
\|C\|_{HS}^2=20,\qquad \|X\|_{HS}^2=5,\qquad
\delta^2\|X\|_{HS}^2=4\cdot5=20=\|C\|_{HS}^2.
\]
For bounded self-adjoint \(A,B\), the induced bounded self-adjoint
\(\mathscr S\) acts on the Hilbert space \(S_2(H_{in},H_{out})\).
Spectral separation yields
\(\operatorname{dist}(0,\sigma(\mathscr S))\ge\delta\), hence
\(\|\mathscr S^{-1}\|_{S_2\to S_2}\le1/\delta\).
A bounded solution for a Hilbert-Schmidt right-hand side belongs to \(S_2\)
by bounded-solution uniqueness and comparison with this \(S_2\) solution.
The generator for unbounded \(A,B\) requires its own domain statement.

**Lean bridge (verified source excerpts).**

`DavisKahan/Sources/DavisKahan1970/Sylvester/HilbertSchmidtEstimate.lean` — `hilbertSchmidt_sylvester_le_of_pairwiseSpectrumGap` (exact source declaration header):

```lean
theorem hilbertSchmidt_sylvester_le_of_pairwiseSpectrumGap
    {E F : Type v}
    [NormedAddCommGroup E] [InnerProductSpace ℂ E] [CompleteSpace E]
    [NormedAddCommGroup F] [InnerProductSpace ℂ F] [CompleteSpace F]
    {A : E →ₗ.[ℂ] E}
    {B : F →ₗ.[ℂ] F}
    {X C : F →L[ℂ] E}
    (hA : IsSelfAdjoint A) (hB : IsSelfAdjoint B)
    {δ : ℝ} (hδ : 0 < δ)
    (hgap : PairwiseSpectrumGap A B δ)
    (hEq : _root_.LinearPMap.SylvesterEquation A B X C)
    (hC : approximationNumberEnergy C ≠ ⊤) :
    approximationNumberEnergy X ≠ ⊤ ∧
      δ * ContinuousLinearMap.hilbertSchmidtNorm X ≤ ContinuousLinearMap.hilbertSchmidtNorm C :=
```

The hypotheses require complex Hilbert spaces, self-adjoint partial operators, a positive pairwise spectral gap, an exact Sylvester equation, and finite defect approximation-number energy. The conclusion includes both solution ideal membership and the sharp square-norm estimate.

`ForTauCeti/Analysis/InnerProductSpace/HilbertSchmidt/Block.lean` — `tsum_enorm_sq_blockFun` (exact source declaration header):

```lean
theorem tsum_enorm_sq_blockFun {ι' : Type*} (b : HilbertBasis ι 𝕜 F)
    (P : ι' → (E →L[𝕜] E)) (Q : ι' → (F →L[𝕜] F))
    (hP : ∀ v : E, ∑' i, ‖P i v‖ₑ ^ 2 = ‖v‖ₑ ^ 2)
    (hQ : ∀ v : F, ∑' j, ‖(Q j).adjoint v‖ₑ ^ 2 = ‖v‖ₑ ^ 2)
    (f : lp (fun _ : ι => E) 2) :
    ∑' p : ι' × ι', ‖blockFun b (P p.1) (Q p.2) f‖ₑ ^ 2 = ‖f‖ₑ ^ 2 := by
```

This is the orthogonal block-energy reassembly on the ell-two column model, subject to norm-splitting hypotheses for the two projection families.
