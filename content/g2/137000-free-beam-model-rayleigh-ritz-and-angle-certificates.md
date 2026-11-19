# Free-beam model, Rayleigh-Ritz, and angle certificates

<!-- BEGIN SPOKEN LECTURE -->

# Free-beam model, Rayleigh-Ritz, and angle certificates

## The free-beam operator and its domain

A thin beam can bend, but two simple motions cause no bending at all. The entire beam can shift upward by the same amount, or tilt so that its displacement increases linearly along its length. Both motions have zero second derivative and therefore zero bending energy in the elementary elastic-beam model.

Those two motions become the zero modes of the fourth-derivative operator with free-end boundary conditions. To understand why, we need more than the expression 'take four derivatives': we must specify which functions belong to its domain and what happens at both endpoints. Once that operator is defined, its low-frequency subspace becomes a concrete setting for testing spectral perturbation estimates.

The word free refers to the boundary conditions. It does not mean that the operator acts on every square-integrable function, and it does not mean that its zero eigenspace is trivial. In fact, the free boundary conditions produce two independent zero modes, and that is exactly what makes the perturbation example interesting.

### Why a fourth derivative appears

Imagine a thin elastic beam occupying the interval from zero to one. In a simplified linear bending model, the energy associated with a displacement u is proportional to the integral of the square of its second derivative. The second derivative measures bending curvature in the small-deflection approximation. Oscillation modes are governed by the fourth derivative.

We choose the Hilbert space of real square-integrable functions on the unit interval. Its inner product is the integral of u times v. Define the formal differential expression A of u to be the fourth derivative of u.

But a formal expression is not yet an operator on a Hilbert space. Most square-integrable functions do not possess four ordinary derivatives. Even if a fourth weak derivative exists, we must specify boundary conditions to get the desired self-adjoint realization.

For a freely supported end, the bending moment and shear force vanish. In this normalized model those are the second and third derivatives. Therefore we require that the second and third derivatives vanish at both endpoints.

In total we have four scalar conditions: the second derivative at zero is zero, the third derivative at zero is zero, and the same two conditions hold at one. The operator's domain is the appropriate fourth-order Sobolev class satisfying those trace equations. One may also characterize the final operator as the self-adjoint closure of a suitable classical fourth-derivative realization.

Why insist on the domain? Consider a candidate displacement that is square-integrable but whose fourth derivative is not. Writing A of that displacement as if it were a vector in the same Hilbert space would make an expression such as A E minus E M undefined on some trial vectors, so the corresponding residual estimate could not be applied. The domain will become part of the numerical argument, not a detail hidden behind notation.

### Green's identity explains symmetry

Take smooth functions u and v in the free-end domain. Start with the integral of the fourth derivative of u times v. Integrate by parts once. The boundary term involves the third derivative of u times v, and the integral now involves the third derivative of u times the first derivative of v, with a minus sign.

Integrate the remaining integral by parts again. The new boundary term involves the second derivative of u times the first derivative of v, and the interior integral becomes the integral of u double-prime times v double-prime.

At each endpoint, both boundary terms vanish because u's second and third derivatives vanish there. Therefore the inner product of A u with v equals the integral of u double-prime times v double-prime.

Interchange u and v. The same integral appears, so the operator is symmetric on the stated domain. Moreover, setting v equal to u gives the nonnegative quadratic form: inner product of A u with u equals the integral of the square of u double-prime.

Integration by parts gives the nonnegative beam energy form, the integral of the squared second derivative. This proves symmetry and nonnegativity on the specified domain, but not self-adjointness: equality with the adjoint also requires equality of domains. A rigorous realization uses a closed quadratic form or a proved graph-closure construction.

For an unbounded operator, specifying the domain is part of specifying the operator itself.

### Why there are exactly two zero modes

Suppose u belongs to the operator domain and A u equals zero. Then its bending energy is zero. The integral of the square of u double-prime vanishes, so u double-prime is zero almost everywhere.

Consequently u is affine: a constant plus a multiple of t. Both the second and third derivatives of every affine function vanish identically, so all affine functions satisfy the free boundary conditions and lie in the kernel.

Thus the kernel has dimension two. One direction translates the whole beam up or down without bending it. The other gives a uniform tilt, which also produces no curvature. There are two zero eigenvalues, counted with multiplicity, even though the beam is not physically locked in place.

This is the trial subspace Davis and Kahan will use: the two-dimensional affine plane inside the infinite-dimensional Hilbert space.

### Find the positive frequencies

Now look for a nonzero eigenvalue lambda. The eigenvalue equation says the fourth derivative of u equals lambda times u. Because A is nonnegative, any such lambda is positive. Write lambda as beta to the fourth power, with beta positive.

The general classical solution is a linear combination of cosine beta t, sine beta t, hyperbolic cosine beta t, and hyperbolic sine beta t. There are four coefficients because this is a fourth-order differential equation.

Apply the two free conditions at the left endpoint. They impose two linear relations among the coefficients. After those are used, only two free parameters remain. Apply the two free conditions at the right endpoint. That gives a homogeneous two-by-two system in those parameters.

A nonzero eigenfunction requires this system to have a nontrivial solution, so its determinant must vanish. The determinant simplifies to a constant multiple of one minus cosine beta times hyperbolic cosine beta. Thus the positive frequencies satisfy cosine beta times hyperbolic cosine beta equals one.

This characteristic equation is not an approximation. It follows from the differential equation and the four boundary conditions. The first positive root lies just above four point seven three, whose fourth power is already greater than five hundred. Hence every positive free-beam eigenvalue is greater than five hundred.

The zero eigenspace therefore sits across a substantial spectral gap from all the positive modes. We have two zero eigenvalues, followed by a third eigenvalue greater than five hundred, and then an increasing sequence of positive eigenvalues.

### Why the spectral picture is complete

We still need to know that no unexpected continuous spectrum lies between these eigenvalues. For a bounded interval, the relevant Sobolev embedding is compact. Roughly, a family of functions with uniformly controlled square-integrable displacement and bending derivatives cannot keep producing arbitrarily fine independent oscillations without a convergent subsequence in L two.

More formally, the graph or form-domain embedding underlying the free-beam realization is compact. A shifted inverse of the operator is then compact and self-adjoint. The compact spectral theorem gives an orthonormal eigenbasis and a discrete set of eigenvalues, with no finite accumulation of positive frequencies.

This is how the differential equation, the operator domain, and the abstract spectral theorem fit together. The characteristic equation identifies possible positive eigenvalues. Compactness and the realization theorem show these are all the nonzero spectral values.

### Turn on a bounded perturbation

Introduce a positive parameter epsilon, smaller than one hundred. Let H multiply a function by epsilon times t. This is a bounded self-adjoint operator on L two, because t lies between zero and one. Its operator norm is at most epsilon, and its quadratic form is nonnegative.

Our perturbed operator is A plus H on the same domain as A. Being a bounded self-adjoint perturbation, H does not require us to shrink the domain. The new eigenvalue problem reads: fourth derivative of u plus epsilon t times u equals lambda times u, under the same four free-end boundary conditions.

Since H is nonnegative, the third eigenvalue of the perturbed system cannot lie below the third eigenvalue of the original system. The high-frequency sector remains above five hundred. The two zero modes are pushed into a small low-frequency cluster, while the large gap protects that cluster's subspace from large rotation.

## Beam Rayleigh–Ritz calculation

A free elastic beam can move without bending: it can translate upward by a constant amount, or tilt as a straight line. Both motions have zero bending energy, because their second derivatives vanish. They form a two-dimensional space of zero modes of the free-beam fourth-derivative operator.

Now add a weak position-dependent potential. Multiplying a function by epsilon times its position along the beam changes those two modes. We can estimate the new low spectral plane by keeping the original constant and affine functions as a trial space. Before using a spectral-angle theorem, though, we need three quantities: an orthonormal basis of that plane, the small two-by-two matrix obtained by compressing the perturbed operator, and the residual left over after that compression.

The beam operator is self-adjoint on its free-endpoint domain: functions with four square-integrable weak derivatives, whose second and third derivatives vanish at both ends. Its kernel is the affine plane, and the remaining spectral values lie above five hundred. The bounded multiplication perturbation preserves the operator domain.

The calculation will start with elementary integrals of polynomials. Once the Ritz matrix and residual are explicit, we can see how recentering at the Ritz value improves an estimate and how the complementary spectral gap turns that estimate into an angle bound.

### Orthonormal coordinates for the affine kernel

Put x equal to two t minus one. Then x ranges from minus one to one, symmetrically about zero. Averaging over the original unit interval gives mean x equal to zero and mean x squared equal to one third.

Choose our first trial function to be one over square root of two times one minus square root of three times x. Choose the second with a plus sign instead of a minus sign.

Let us verify normalization. Squaring either trial function gives one half times one plus three x squared, plus a mixed term whose average is zero. The mean is one half times one plus three times one third, which equals one. For their cross inner product, multiply the plus and minus expressions. The cross product is one half times one minus three x squared. Its mean is zero. So the two functions are orthonormal.

They span the affine functions because their sum is a nonzero constant and their difference is a nonzero multiple of x. Each belongs to the domain of the unperturbed beam operator, and A annihilates each.

We can therefore package them as an isometric map E from real two-space into our Hilbert space. The unperturbed compression E star A E is the zero two-by-two matrix.

### Compute the perturbed compression

The perturbation H multiplies by epsilon t. Hence the compressed operator is epsilon times the matrix whose entries are integrals of t times products of the trial functions.

Rather than multiply four polynomials independently, use centered moments. The average of t equals one half. The average of t times x equals one sixth. And the average of t times x squared equals one sixth. These follow immediately from t equals one half times x plus one and the first three centered moments.

Substitute the two trial functions. The off-diagonal compressed entry is the average of t times one half times one minus three x squared. This equals one half times one half minus three times one sixth, which is zero.

The diagonal entries are not equal. For the first trial function, the negative mixed term reduces the mean to one half times one minus one over square root of three. For the second, the positive mixed term gives one half times one plus one over square root of three.

Thus our Rayleigh–Ritz matrix is already diagonal in the chosen trial basis. Its lower Ritz value is epsilon over two times one minus one over square root of three. Its upper Ritz value is epsilon over two times one plus one over square root of three.

Their sum is epsilon. Their difference is epsilon divided by square root of three. Both are positive for epsilon positive, and the upper one is less than about point seven eight eight seven times epsilon.

This internal Ritz gap will later help us separate the individual low-frequency modes.

### First residual: comparing against zero

Davis and Kahan begin with a simpler comparison operator on the trial space: zero. Because A E equals zero, its residual is simply H E. Its two columns are epsilon t times the two trial functions.

Compute the Gram matrix of this residual. The entry in row i and column j is epsilon squared times the integral of t squared times the product of trial functions i and j.

The centered moments now needed are the mean of t squared, equal to one third; the mean of t squared times x, equal to one sixth; and the mean of t squared times x squared, equal to two fifteenths. They are simple polynomial integrals on the unit interval.

Carrying out the multiplication gives epsilon squared over thirty times a symmetric two-by-two matrix. Its first diagonal entry is eleven minus square root of seventy-five. Its second diagonal entry is eleven plus square root of seventy-five. Both off-diagonal entries are negative one.

A Gram matrix is positive semidefinite, and its eigenvalues are the squares of the residual's singular values. The trace of this particular matrix is eleven epsilon squared over fifteen. Its two eigenvalues are epsilon squared over thirty times eleven minus square root of seventy-six, and eleven plus square root of seventy-six.

Therefore the largest residual singular value is epsilon times the square root of eleven plus square root of seventy-six, divided by thirty. This coefficient is approximately point eight one one. The second coefficient is approximately point two seven six.

These are the exact pieces behind the paper's first sine-angle estimate and its Ky Fan two-term estimate. Their derivation involved neither numerical eigenvalue solvers nor approximations to free-beam eigenfunctions.

### Recenter at the Ritz matrix

We can do better by allowing the trial coordinates to evolve under their own compressed matrix. Let A hat be the diagonal Ritz matrix. Define the recentered residual R hat to be the perturbed operator applied to E, minus E followed by A hat.

Because A hat equals E star times the perturbed operator times E, the adjoint E star annihilates this new residual. This is Galerkin orthogonality. R hat takes values entirely in the orthogonal complement of the trial plane.

For its Gram matrix, use the identity R hat star R hat equals E star H squared E minus A hat squared. The first term can be integrated directly from the trial functions. Its upper-left entry is epsilon squared times eleven thirtieths minus one over twice the square root of three. Its lower-right entry has a plus sign in place of that minus sign. Its two off-diagonal entries are minus epsilon squared over thirty. Subtracting the square of the diagonal Ritz matrix cancels most of the diagonal energy.

The result is strikingly simple: epsilon squared over thirty times the matrix whose diagonal entries are one and whose off-diagonal entries are negative one.

That matrix has eigenvectors in the sum and difference directions. The sum direction has eigenvalue zero; the difference direction has eigenvalue two. Thus the recentered residual has singular values epsilon divided by square root of fifteen and zero.

It is rank one. Its operator norm and its two-term Ky Fan norm are the same: epsilon over square root of fifteen. And each of its two columns separately has norm epsilon over square root of thirty.

One might be surprised that two distinct trial functions yield a rank-one residual. The explanation is that multiplication by t sends the affine plane into polynomials of degree at most two. After removing the affine component, only the single quadratic direction remains. There is exactly one direction in which both residual columns can escape.

### A numerical consistency check

Take epsilon equal to ten, which lies in the parameter range zero less than epsilon less than one hundred. The Ritz values are approximately two point one one three and seven point eight eight seven. The recentered residual's only nonzero singular value is ten divided by square root of fifteen, about two point five eight two.

The high modes remain above five hundred. So the gap between our upper Ritz value and the high spectrum is greater than five hundred minus seven point eight eight seven, or approximately four hundred ninety-two point one one three.

An estimate that divides the recentered residual by that gap produces an angle of only about five thousandths in tangent units. This is why treating the Ritz matrix rather than the zero matrix improves the result.

### What the calculation does and does not prove

The calculation determines the Rayleigh–Ritz compression and residual. Ritz vectors generally are not exact eigenvectors of the perturbed beam, and identifying its low two-dimensional spectral subspace additionally requires a spectral theorem and a separating gap.

An operator-norm bound controls the largest principal angle, while a Ky Fan bound controls a sum of principal angles. A tangent estimate also uses stronger spectral placement and can improve on the initial sine estimate.

The broader method is reusable: choose trial functions in the operator domain; form their Gram and compressed matrices; orthonormalize; compute the residual Gram operator; and only then invoke a gap theorem. Nothing in this workflow depends on having closed-form eigenfunctions of the perturbed operator.

## Comparing angle and Ky Fan beam estimates

Two spectral-angle estimates can be valid and still give noticeably different numerical bounds for the same trial plane. One might control only the worst principal angle; another might control the sum of the two largest principal sines. A third might improve the right-hand side by replacing an unrecentered defect with a true Ritz residual.

Our common example is the free beam on the unit interval. The unperturbed fourth-derivative operator has the two-dimensional affine kernel and positive spectrum above five hundred. We perturb it by multiplication by epsilon times position, where epsilon is positive and below one hundred. The trial plane is still the affine kernel, with normalized basis consisting of the constant function and a centered linear function.

The original kernel is invariant under the unperturbed beam operator, so the perturbation alone determines the first residual. Its component outside the trial plane can be calculated explicitly by subtracting the two-by-two Ritz compression. Those two residuals have different norms; they are not interchangeable in a theorem unless the trial operator and gap are changed together.

We will put the hypotheses and numerical values beside each candidate estimate. This is how to compare the single-angle, Ky Fan, and doubled-angle approaches without treating the smallest displayed number as automatically the strongest theorem.

### First use the unrecentered residual

Start with the reference operator zero on the affine trial plane. Since the unperturbed fourth derivative annihilates both trial functions, the residual is H applied to the frame. For this map the Gram matrix equals epsilon squared over thirty times the symmetric matrix with diagonal entries eleven minus square root of seventy-five and eleven plus square root of seventy-five, and both off-diagonal entries negative one. Its eigenvalues are epsilon squared over thirty times eleven plus or minus square root of seventy-six. Thus the top singular value is epsilon times the square root of the quotient of eleven plus square root of seventy-six by thirty, a little smaller than point eight one one.

The high part of the perturbed beam has spectrum above five hundred. Because the trial reference value is zero, the ordered gap is at least five hundred. The directed sine theorem gives five hundred times the norm of the sine operator no greater than the residual operator norm.

Divide through. The largest sine of a principal angle is smaller than point eight one one divided by five hundred times epsilon. That is the printed bound, sine theta one less than point zero zero one six two two times epsilon, equation nine point one.

Why call it the largest principal angle? In the relevant range, the principal sine increases with the angle. Operator norm selects the largest singular value of the sine operator, hence the largest angle.

The bound assumes epsilon is positive and below one hundred. At epsilon equal to ten, this initial result says sine theta one is below about point zero one six two two. It is a useful certificate, but we can improve it considerably.

### What a two-term Ky Fan norm adds

Operator norm sees only the largest singular value. We also know the second singular value of the initial residual. Its coefficient is the square root of eleven minus square root of seventy-six, divided by thirty, about point two seven six.

Add the two coefficients and divide by five hundred. The result is below point zero zero two one eight times epsilon. So the sum of the sines of the two principal angles is bounded by that quantity. This is the paper's equation nine point three.

The Ky Fan estimate bounds the sum of the two principal sines, not each sine by half that sum; their contributions can be unequal. What the inequality controls is their cumulative rotation, measured by the first two singular values of the directed sine map.

Why can we make that inference? The Hilbert-space singular-value comparison supports a compatible invariant norm. The Ky Fan two-norm adds the two largest singular values, and both the residual and the sine map have at most two nonzero singular values because their source is two-dimensional.

The largest-angle and two-term results are complementary. If we need a guarantee for the worst single direction, the operator norm is natural. If we need the total leakage of a two-dimensional cluster, the Ky Fan sum carries more information.

### The doubled-angle alternative

The paper next applies the sine-two-theta theorem. This theorem compares two reducing subspaces of the unperturbed and perturbed operators, not simply one trial residual. In the beam example the perturbation has norm at most epsilon and the relevant separation is five hundred.

The ambient sine-two-theta estimate gives sine of twice the largest angle less than point zero zero four times epsilon. Its two-term Ky Fan version gives the sum of the doubled sines less than point zero zero eight times epsilon. These are equations nine point two and nine point four.

At first sight these coefficients look larger than the single-angle sine coefficient. But the left sides are different functions: sine of twice an angle is approximately twice the sine of that angle for small angles.

The double-angle estimate has a branch ambiguity. The sine of twice an angle can be small near zero degrees or near ninety degrees. A separate spectral-selection or small-angle argument is needed before converting it into a unique small-angle certificate. In the beam problem, the low spectral cluster is selected across a large gap, and its continuity under bounded perturbation supplies the intended branch.

The doubled-angle theorem is valuable because it uses ambient off-diagonal structure. It is not automatically the sharpest numerical estimate for this particular data.

### Recenter at the Ritz matrix

Now use the actual Rayleigh-Ritz compression rather than zero. Its diagonal entries are epsilon over two times one minus one over square root of three, and epsilon over two times one plus one over square root of three. Subtracting the compressed action from the full action leaves a rank-one residual, whose Gram matrix is epsilon squared over thirty times the matrix with diagonal entries one and off-diagonal entries negative one. The only nonzero singular value is epsilon divided by square root of fifteen.

The separation is no longer the full five hundred because the trial Ritz values are positive. But a valid lower gap is five hundred minus point seven eight eight seven times epsilon. This remains positive for the stipulated parameter range, since epsilon is below one hundred.

Apply the ordered-gap tangent theorem. Tangent of the largest principal angle is bounded by epsilon divided by square root of fifteen, divided again by five hundred minus point seven eight eight seven epsilon.

Factor five hundred out of the denominator. The resulting coefficient is approximately point zero zero zero five one six four times epsilon, divided by one minus point zero zero one five seven seven four times epsilon.

That is equation nine point six. Because the recentered residual has rank one, its operator norm and its two-term Ky Fan norm agree. Therefore the same right-hand side controls the sum of the two principal tangents, as long as the theorem is applied with that norm.

Take epsilon equal to ten again. The bound is roughly point zero zero five two five, markedly smaller than the initial sine bound of point zero one six two two. The improvement comes from removing the part of H that acts within the trial plane. We spend a little of the spectral gap but reduce the residual by a much larger proportion.

### A recentered doubled-tangent bound

There is also a tangent-two-theta estimate. Use the perturbed operator's compression to the complementary trial space. The complement remains above five hundred because the original beam is nonnegative with its high spectrum above five hundred and the perturbation is positive.

The corresponding bound for tangent of twice the largest angle has twice the numerator of the tangent estimate. Thus the paper obtains point zero zero one zero three two eight times epsilon, divided by the same denominator, one minus point zero zero one five seven seven four times epsilon.

This is equation nine point seven. As before, there is a two-term Ky Fan version with the same scalar right-hand side because the residual responsible for the estimate is rank one.

The sharp tangent-two-theta estimate applies to selected matched spectral branches under the required off-diagonal conditions. In this example, those conditions are justified by the low-high spectral split, not by the numerical fraction alone.

### Comparison at one concrete parameter

With epsilon ten, the initial largest-angle sine bound is about point zero one six two two, while the recentered tangent bound is about point zero zero five two five. The initial doubled-sine bound is point zero four, while the recentered doubled-tangent bound is about point zero one zero five.

These are not four numbers measuring an identical quantity. Yet when the angles are small, they give a coherent picture, and the recentered estimates use the information that the Ritz matrix contains.

There is one more distinction. All the results so far concern the two-dimensional low spectral subspace relative to the trial plane. They do not tell us which of the two trial functions is closest to which individual perturbed eigenvector. A basis can rotate substantially inside a plane even if the plane itself hardly moves.

To estimate an individual eigenvector rather than the low spectral plane, an additional in-plane rotation must be controlled. A two-by-two Schur complement separates that rotation from the leakage out of the trial plane.

## From subspace bounds to individual modes

Imagine two coordinate axes drawn on the same sheet of paper. Rotate both axes through forty-five degrees, leaving the sheet itself fixed. The span of the axes is exactly the same two-dimensional plane before and after the rotation, so its subspace angle is zero. Yet each individual axis has moved.

This distinction becomes essential when tracking eigenfunctions. A perturbation theorem may show that a low spectral plane of a differential operator has barely changed, even while the two eigenvectors selected inside that plane rotate significantly. The subspace estimate controls leakage outside the plane. To identify a specific eigenfunction, we must also separate the eigenvalues within the plane.

Consider the self-adjoint free-beam fourth-derivative operator on the unit interval with vanishing second and third endpoint derivatives. Its kernel consists of affine functions. Add multiplication by epsilon times position, for a small positive epsilon. The perturbed low spectral plane lies close to the affine kernel, but its two individual modes are distinguished only by the two-by-two compressed operator and their internal eigenvalue separation.

We will use a block eigenvalue equation to solve for the component outside the trial plane, then substitute back into an effective equation inside the plane. This separates the out-of-plane angle error from the in-plane eigenvector error.

### Separate the two angle contributions

Take one normalized exact low eigenvector, call it f. Project it orthogonally onto the trial plane. If the projection is nonzero, normalize it to obtain g. Let eta be the angle from f to the trial plane, equivalently the angle from f to g.

Now choose the Ritz vector e that we expect to approximate f. Let psi be the angle between g and e, both of which lie in the trial plane. Finally, let omega be the total angle between e and f.

Because e lies in the plane, its inner product with f equals its inner product with the projection of f. The projection has length cosine eta and direction g. Thus the absolute inner product between e and f equals cosine eta times cosine psi.

In other words, cosine omega equals cosine eta times cosine psi, after choosing acute vector-angle conventions. This is an exact identity.

A useful consequence is that omega squared is bounded by eta squared plus psi squared in the relevant range. The geometry can be proved by comparing the cosine expressions, or by elementary trigonometric inequalities. It turns a two-stage rotation into a quantitative estimate for the individual vector.

We already control eta by a subspace perturbation theorem. We must now control psi, the in-plane rotation.

### Express the eigenproblem in blocks

Use the orthogonal decomposition of the Hilbert space into the trial plane and its perpendicular complement. The perturbed beam operator becomes a two-by-two operator matrix in block form.

The upper-left block is the diagonal two-by-two Ritz matrix. The lower-right block is the perturbed beam compressed to the complementary space. The lower-left block sends a trial vector into its Galerkin residual, and the upper-right block is its adjoint.

Write our exact eigenvector as a pair of coordinates: x in the trial plane and y in the complement. The eigenvalue equation gives two coupled relations.

The upper equation says the Ritz matrix applied to x, plus the adjoint residual block applied to y, equals lambda times x. The lower equation says the residual block applied to x, plus the complementary operator applied to y, equals lambda times y.

Every term is meaningful because the eigenvector belongs to the operator domain. We must keep that condition in an unbounded problem. An abstract block matrix is shorthand for the properly restricted operator action, not permission to apply the fourth derivative to arbitrary vectors.

### Solve for the out-of-plane coordinate

The complementary operator has quadratic-form lower bound greater than five hundred, while our low eigenvalue is below five hundred. The lower equation can be rearranged so that the shifted lower block, lambda minus the complementary operator, acts on y and gives the residual block applied to x.

That shifted block has a bounded inverse on the appropriate space. Formally, y equals that inverse applied to B x, where B denotes the residual block.

To prove a bound, we do not even need to write the inverse. Take the inner product of the lower equation with y. The form lower bound gives five hundred times the squared norm of y. The lambda term subtracts lambda times that squared norm. Cauchy–Schwarz controls the residual pairing by the norm of B x times the norm of y.

Cancel one factor when y is nonzero. We obtain five hundred minus lambda times the norm of y no greater than the norm of B x.

Since the full residual block has norm at most epsilon divided by square root of fifteen, the out-of-plane coordinate is of order epsilon over the large spectral gap. This gives our control of eta.

### Substitute back into the trial equation

Now substitute the formula for y into the upper equation. The result is an eigenvalue problem entirely on the two-dimensional trial plane, but with an extra correction term.

The effective matrix is the diagonal Ritz matrix plus B star times the inverse of lambda minus the complementary operator times B. Because lambda lies below the complementary spectrum, that correction is negative semidefinite.

The Galerkin residual is rank one, because multiplication by t sends affine functions to quadratics and the component perpendicular to the affine plane occupies just one direction. Its Gram matrix, in the orthonormal Ritz basis, is epsilon squared over thirty times the matrix with diagonal entries one and off-diagonal entries negative one. This can be obtained by computing E star H squared E and subtracting the square of E star H E. Consequently the Schur correction is controlled by a scalar multiple of that rank-one matrix.

Let the scalar be q. The lower-block spectral estimate gives q no greater than epsilon squared divided by the product of thirty and the quantity five hundred minus lambda. The effective two-by-two matrix therefore has diagonal Ritz entries, shifted by a common correction, and an off-diagonal coupling of size q.

A common diagonal shift does not rotate eigenvectors. The mixing comes from the off-diagonal entry. For a real symmetric two-by-two matrix with diagonal gap Delta and off-diagonal entry q, the eigenvector rotation psi satisfies tangent of twice psi equal to two q divided by Delta, with an appropriate sign convention.

Here Delta is the Ritz gap, epsilon divided by square root of three. Therefore one half of tangent of twice psi is bounded by square root of three over thirty times epsilon divided by five hundred minus lambda.

That identifies the internal rotation explicitly. It is also why the Ritz gap matters: the out-of-plane separation protects the plane, while the internal separation identifies the individual basis vectors within the plane.

### Combine the errors

The argument combines a subspace estimate for eta with this two-by-two bound for psi. One convenient common envelope has coefficient square root of seven over ten, divided by five hundred minus an upper bound on lambda, times epsilon.

The two Ritz eigenvalues have different upper bounds: the lower one is about point two one one three times epsilon, and the higher is about point seven eight eight seven times epsilon. Hence the two final eigenvector estimates carry different denominators.

In the printed numerical form, the lower eigenvector angle omega one is below approximately point zero zero zero five three epsilon divided by one minus point zero zero zero four three epsilon. The upper angle omega two has the same numerator, but denominator one minus point zero zero one six epsilon.

The precise source rational forms use slightly conservative decimals. What matters is that these are individual eigenvector angles, not principal angles between entire planes.

### The alternative one-vector route

The paper also applies its one-vector tangent theorem directly to each Ritz vector. Each recentered residual column has norm epsilon divided by square root of thirty, smaller than the norm of the full rank-one residual map.

Divide that individual residual by the appropriate gap. This yields sharper individual tangent bounds with numerator about point zero zero zero three six five two times epsilon. The denominator for the lower vector uses its lower Ritz value, while the upper vector uses the upper Ritz value.

Those estimates are statements about the angle between each fixed trial vector and the exact low spectral plane. To turn such information into pairing with an individual exact eigenvector, we still need internal spectral separation and the Schur argument. The full eigenvector comparison supplies that extra step by controlling the effective two-by-two coupling relative to the Ritz gap.

Three angles occur in this calculation: the angle of a whole subspace, the angle of one trial vector to that subspace, and the angle between a named trial vector and a named exact eigenvector.

### General method

When you want individual modes rather than a low-frequency cluster, proceed in two stages. First estimate the leakage of the entire cluster into its orthogonal complement. Then construct an effective operator on the cluster using a Schur complement. Control its off-diagonal entries relative to the internal Ritz gap.

If the internal gap closes, even a perfectly stable subspace may have unstable individual eigenvectors. The beam calculation makes this distinction measurable, and it prepares us for the open questions about what spectral separation assumptions really suffice.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### The free-beam operator and its domain

**Draft status:** audio-first mathematical lecture. **Prerequisites:** `072000–094000`, `136000`. **Next:** `138000`.

---

#### Companion: mathematics and Lean correspondence (display only)

On real \(L^2(0,1)\), the free realization acts by \(Au=u^{(4)}\) on a domain supporting traces \(u''(0)=u'''(0)=u''(1)=u'''(1)=0\). Smooth integration by parts yields
\[\langle Au,v\rangle=\int_0^1u''(t)v''(t)\,dt=\langle u,Av\rangle.\]
The genuine self-adjoint operator uses domain and graph closure, beyond the formal Green identity. Its zero eigenspace is \(\operatorname{span}\{1,t\}\); nonzero eigenvalues satisfy \(\lambda=\beta^4\), \(\cos\beta\cosh\beta=1\). The source proves the positive spectral values exceed 500 for this model.

#### Exact Lean declaration excerpts


**`FreeBoundary`.** The four free-end traces on classical modal solutions are second and third derivatives at both endpoints.

`DavisKahan/Sources/DavisKahan1970/Section9/FreeBeamCharacteristic.lean` — `FreeBoundary` (exact declaration header; proof body omitted):

```lean
@[expose]
def FreeBoundary (beta a b c d : ℝ) : Prop :=
```


**`characteristic_eq_zero_of_freeBoundary`.** A nontrivial positive-frequency classical eigenmode obeying free-end conditions satisfies the characteristic equation. The converse requires a separate modal construction.

`DavisKahan/Sources/DavisKahan1970/Section9/FreeBeamCharacteristic.lean` — `characteristic_eq_zero_of_freeBoundary` (exact declaration header; proof body omitted):

```lean
theorem characteristic_eq_zero_of_freeBoundary
    {beta a b c d : ℝ} (hbeta : beta ≠ 0)
    (hboundary : FreeBoundary beta a b c d)
    (hnonzero : a ≠ 0 ∨ b ≠ 0 ∨ c ≠ 0 ∨ d ≠ 0) :
    characteristic beta = 0 :=
```


**`beamOperator_is_closure_of_classical_freeBeam_fourthDerivative`.** The concrete **real** beam realization is identified as the closure of the classical fourth-derivative graph; formal Green symmetry by itself is not enough.

`DavisKahan/Specialized/FreeBeam/BeamClassicalReal.lean` — `beamOperator_is_closure_of_classical_freeBeam_fourthDerivative` (exact declaration header; proof body omitted):

```lean
theorem beamOperator_is_closure_of_classical_freeBeam_fourthDerivative :
    _root_.IsSelfAdjoint beamOperator ∧
      closure classicalFreeBeamGraph =
        (beamOperator.graph : Set (BeamL2 × BeamL2)) :=
```


**`real_freeBeam_zero_eigenspace_eq_beamTrial`.** The zero eigenspace is precisely the two-dimensional affine trial plane, with the domain condition retained explicitly.

`DavisKahan/Sources/DavisKahan1970/Section9/RealModel.lean` — `real_freeBeam_zero_eigenspace_eq_beamTrial` (exact declaration header; proof body omitted):

```lean
theorem real_freeBeam_zero_eigenspace_eq_beamTrial :
    Module.finrank ℝ
        DavisKahan.FreeBeam.Model.Real.beamTrial = 2 ∧
      ∀ (x : RealBeamL2) (h : x ∈ realBeamOperator.domain),
        realBeamOperator ⟨x, h⟩ = 0 ↔
          x ∈ DavisKahan.FreeBeam.Model.Real.beamTrial :=
```

### Beam Rayleigh–Ritz calculation

**Draft status:** audio-first mathematical lecture. **Prerequisites:** `027000–030000`, `107000`, `137000`. **Next:** `139000`.

---

#### Companion: mathematics and Lean correspondence (display only)

Let \(x=2t-1\), \(e_{1,2}(t)=(1\mp\sqrt3 x)/\sqrt2\). With \(T=A+H\), \(Hf(t)=\varepsilon tf(t)\), and \(E=(e_1,e_2)\),
\[
E^*TE=\frac\varepsilon2\operatorname{diag}(1-1/\sqrt3,1+1/\sqrt3),
\]
\[
(HE)^*(HE)=\frac{\varepsilon^2}{30}
\begin{pmatrix}11-\sqrt{75}&-1\\-1&11+\sqrt{75}\end{pmatrix},\qquad
\widehat R^*\widehat R=\frac{\varepsilon^2}{30}
\begin{pmatrix}1&-1\\-1&1\end{pmatrix}.
\]
Here \(\widehat R=TE-E(E^*TE)=(I-EE^*)HE\). Thus \(s(\widehat R)=(\varepsilon/\sqrt{15},0)\) for \(\varepsilon>0\). The initial residual singular values follow from \(\frac{\varepsilon^2}{30}(11\pm\sqrt{76})\).

#### Exact Lean declaration excerpts


**`ritz_matrix_from_affine_moments`.** Integrals of multiplication by `t` against the explicit orthonormal affine pair give the diagonal Ritz matrix.

`DavisKahan/Sources/DavisKahan1970/Section9/TrialSubspace.lean` — `ritz_matrix_from_affine_moments` (exact declaration header; proof body omitted):

```lean
theorem ritz_matrix_from_affine_moments (ε : ℝ) :
    ε * CenteredAffine.tInner trialOne trialOne = ritzLow ε ∧
    ε * CenteredAffine.tInner trialOne trialTwo = 0 ∧
    ε * CenteredAffine.tInner trialTwo trialTwo = ritzHigh ε :=
```


**`initial_residual_gram_from_affine_moments`.** Second moments of `t` give the unrecentered residual Gram matrix; this result is an exact finite-moment identity.

`DavisKahan/Sources/DavisKahan1970/Section9/TrialSubspace.lean` — `initial_residual_gram_from_affine_moments` (exact declaration header; proof body omitted):

```lean
theorem initial_residual_gram_from_affine_moments (ε : ℝ) :
    SymmetricTwoByTwo.mk
      (ε ^ 2 * CenteredAffine.tSqInner trialOne trialOne)
      (ε ^ 2 * CenteredAffine.tSqInner trialOne trialTwo)
      (ε ^ 2 * CenteredAffine.tSqInner trialTwo trialTwo) = residualGram ε :=
```


**`recentered_residual_gram_from_affine_moments`.** Subtracting the square of the Ritz compression gives the exact rank-one recentered residual Gram matrix.

`DavisKahan/Sources/DavisKahan1970/Section9/TrialSubspace.lean` — `recentered_residual_gram_from_affine_moments` (exact declaration header; proof body omitted):

```lean
theorem recentered_residual_gram_from_affine_moments (ε : ℝ) :
    SymmetricTwoByTwo.mk
      (ε ^ 2 * (CenteredAffine.tSqInner trialOne trialOne -
        CenteredAffine.tInner trialOne trialOne ^ 2))
      (ε ^ 2 * (CenteredAffine.tSqInner trialOne trialTwo -
        CenteredAffine.tInner trialOne trialOne *
          CenteredAffine.tInner trialOne trialTwo))
      (ε ^ 2 * (CenteredAffine.tSqInner trialTwo trialTwo -
        CenteredAffine.tInner trialTwo trialTwo ^ 2)) =
      orthogonalResidualGram ε :=
```


**`orthogonalResidualGram_det`.** The determinant vanishes; together with its trace and nonnegativity, the Gram eigenvalues are zero and epsilon squared over fifteen.

`DavisKahan/Sources/DavisKahan1970/Section9/ExactData.lean` — `orthogonalResidualGram_det` (exact declaration header; proof body omitted):

```lean
lemma orthogonalResidualGram_det (ε : ℝ) :
    (orthogonalResidualGram ε).det = 0 :=
```

### Comparing angle and Ky Fan beam estimates

**Draft status:** audio-first mathematical lecture. **Prerequisites:** `054000–059000`, `110000–127000`, `137000–138000`. **Next:** `140000`.

---

#### Companion: mathematics and Lean correspondence (display only)

For \(0<\varepsilon<100\), Section 9 states the rigorous decimal envelopes
\[
\sin\theta_1<0.001622\varepsilon,\qquad
\sin\theta_1+\sin\theta_2<0.00218\varepsilon,
\]
\[
\sin2\theta_1<0.004\varepsilon,\qquad
\sin2\theta_1+\sin2\theta_2<0.008\varepsilon,
\]
\[
\tan\theta_1<\frac{0.0005164\varepsilon}{1-0.0015774\varepsilon},\qquad
\tan2\theta_1<\frac{0.0010328\varepsilon}{1-0.0015774\varepsilon}.
\]
The companion two-term Ky Fan tangent bounds use the same RHS as their respective operator-norm estimates. The source-facing Lean statements invoke the genuine free-beam realization; the bound-conversion lemmas are separately proved using exact radicals and rational comparisons.

#### Exact Lean declaration excerpts


**`equation_9_1_freeBeam`.** The source-facing complex-model wrapper supplies the printed largest-sine bound for the genuine beam realization; the repository also has a separately established real model. Epsilon is positive and less than 100.

`DavisKahan/Sources/DavisKahan1970/Section9/NumericalResults.lean` — `equation_9_1_freeBeam` (exact declaration header; proof body omitted):

```lean
theorem equation_9_1_freeBeam (ε : ℝ) (hε : 0 < ε) (_hε100 : ε < 100) :
    beamSinTheta ε < (811 : ℝ) / 500000 * ε :=
```


**`equation_9_3_freeBeam`.** The two-term Ky Fan inequality bounds the *sum* of both principal sines, not each separately by half.

`DavisKahan/Sources/DavisKahan1970/Section9/NumericalResults.lean` — `equation_9_3_freeBeam` (exact declaration header; proof body omitted):

```lean
theorem equation_9_3_freeBeam (ε : ℝ) (hε : 0 < ε) (_hε100 : ε < 100) :
    beamSinThetaSum ε < (109 : ℝ) / 50000 * ε :=
```


**`equation_9_6_freeBeam`.** Both operator-norm tangent and Ky Fan two-term tangent bounds are included in this theorem conclusion.

`DavisKahan/Sources/DavisKahan1970/Section9/NumericalResults.lean` — `equation_9_6_freeBeam` (exact declaration header; proof body omitted):

```lean
theorem equation_9_6_freeBeam (ε : ℝ) (hε : 0 < ε) (hε100 : ε < 100) :
    beamTanTheta ε
        < ((1291 : ℝ) / 2500000 * ε) /
            (1 - (7887 : ℝ) / 5000000 * ε) ∧
      beamTanThetaSum ε
        < ((1291 : ℝ) / 2500000 * ε) /
            (1 - (7887 : ℝ) / 5000000 * ε) :=
```


**`equation_9_7_freeBeam`.** The doubled-tangent inequalities come from the specific source-model branch with its high block and comparison hypotheses already discharged upstream.

`DavisKahan/Sources/DavisKahan1970/Section9/NumericalResults.lean` — `equation_9_7_freeBeam` (exact declaration header; proof body omitted):

```lean
theorem equation_9_7_freeBeam (ε : ℝ) (hε : 0 < ε) (hε100 : ε < 100) :
    beamTanTwoTheta ε
        < ((1291 : ℝ) / 1250000 * ε) /
            (1 - (7887 : ℝ) / 5000000 * ε) ∧
      beamTanTwoThetaSum ε
        < ((1291 : ℝ) / 1250000 * ε) /
            (1 - (7887 : ℝ) / 5000000 * ε) :=
```

### From subspace bounds to individual modes

**Draft status:** audio-first mathematical lecture. **Prerequisites:** `111000–113000`, `127000–129000`, `137000–139000`. **Next:** `141000`.

---

#### Companion: mathematics and Lean correspondence (display only)

##### Frame displacement need not measure subspace displacement

In \(\mathbb R^2\), take \(V=I_2\) and
\(W=\left(\begin{smallmatrix}\cos\theta&-\sin\theta\\
\sin\theta&\cos\theta\end{smallmatrix}\right)\).
Both frames span the whole plane: \(VV^*=WW^*=I_2\), hence the
projection distance is zero. Yet
\(\|V-W\|_F^2=4(1-\cos\theta)\), which is nonzero unless
\(\theta=0\) modulo a full turn. Optimizing over within-subspace
coordinate changes removes this artificial disagreement.

For a normalized eigenvector \(f=(x,y)\) of the block operator, with \(\lambda<\inf\sigma(A_1)\),
\[
B x+A_1 y=\lambda y,\qquad
(\beta-\lambda)\|y\|\le\|Bx\|,
\]
\[
\bigl[A_0+B^*(\lambda-A_1)^{-1}B\bigr]x=\lambda x.
\]
Writing \(\cos\omega=\cos\eta\cos\psi\), the source controls the complementary angle \(\eta\) and internal Ritz rotation \(\psi\) separately. In the free-beam model \(\widehat R^*\widehat R=(\varepsilon^2/30)\begin{psmallmatrix}1&-1\\-1&1\end{psmallmatrix}\), yielding a rank-one Schur correction. The final source-facing eigenvector-angle statements concern paired exact eigenvectors, whereas the one-vector tangent bounds initially concern trial vectors versus the exact low eigenspace.

#### Exact Lean declaration excerpts


**`schur_complement_reduction`.** This algebraic theorem assumes a left inverse of `lambda I - A1`; the unbounded beam case additionally requires checking the block domains.

`DavisKahan/Sources/DavisKahan1970/Section9/SchurComplement.lean` — `schur_complement_reduction` (exact declaration header; proof body omitted):

```lean
theorem schur_complement_reduction
    (x : E) (y : F)
    (htop : A₀ x + Bstar y = lam • x)
    (hbottom : B x + A₁ y = lam • y)
    (hleft : Function.LeftInverse C (lowerShift A₁ lam)) :
    y = C (B x) ∧ A₀ x + Bstar (C (B x)) = lam • x :=
```


**`norm_lower_coordinate_le`.** A quadratic-form lower bound and the lower block equation yield the inverse-free estimate for the complementary eigenvector coordinate.

`DavisKahan/Sources/DavisKahan1970/Section9/SchurComplement.lean` — `norm_lower_coordinate_le` (exact declaration header; proof body omitted):

```lean
theorem norm_lower_coordinate_le {b w y : F} {lam β : ℝ}
    (hbottom : b + w = (lam : 𝕜) • y)
    (hform : β * ‖y‖ ^ 2 ≤ RCLike.re (inner 𝕜 w y))
    (_hlt : lam < β) :
    (β - lam) * ‖y‖ ≤ ‖b‖ :=
```


**`half_tanTwoPsi_ratio_lt`.** A scalar upper bound for the rank-one Schur correction and the Ritz gap yields the exact coefficient in the half-tangent bound.

`DavisKahan/Sources/DavisKahan1970/Section9/RankOneCorrection.lean` — `half_tanTwoPsi_ratio_lt` (exact declaration header; proof body omitted):

```lean
theorem half_tanTwoPsi_ratio_lt
    {ε D q : ℝ} (hε : 0 < ε) (hD : 0 < D)
    (_hq0 : 0 ≤ q) (hq : q < ε ^ 2 / (30 * D)) :
    q / (ritzHigh ε - ritzLow ε) <
      (Real.sqrt 3 / 30) * ε / D :=
```


**`freeBeam_individualEigenvectorAngle_bounds`.** The final **paired eigenvector** result uses two distinct denominators and ordered exact eigenvalues; it is stronger in scope than a trial-vector-to-eigenspace estimate.

`DavisKahan/Sources/DavisKahan1970/Section9/NumericalResults.lean` — `freeBeam_individualEigenvectorAngle_bounds` (exact declaration header; proof body omitted):

```lean
theorem freeBeam_individualEigenvectorAngle_bounds (ε : ℝ) (hε : 0 < ε) (hε100 : ε < 100)
    {j k : Fin 2} (hjk : j ≠ k)
    (hle : beamLowEigenvalue ε hε.le hε100 j ≤ beamLowEigenvalue ε hε.le hε100 k) :
    Real.arccos ‖inner ℂ (centeredAffineLp trialOne) (beamLowEigenvector ε hε.le hε100 j)‖
        < ((53 : ℝ) / 100000 * ε) / (1 - (43 : ℝ) / 100000 * ε) ∧
      Real.arccos ‖inner ℂ (centeredAffineLp trialTwo) (beamLowEigenvector ε hε.le hε100 k)‖
        < ((53 : ℝ) / 100000 * ε) / (1 - (1 : ℝ) / 625 * ε) :=
```


**`freeBeam_trialVector_tanAngle_bounds`.** The sharper one-column tangent conclusions apply to each specific trial vector relative to the low exact spectral subspace.

`DavisKahan/Sources/DavisKahan1970/Section9/NumericalResults.lean` — `freeBeam_trialVector_tanAngle_bounds` (exact declaration header; proof body omitted):

```lean
theorem freeBeam_trialVector_tanAngle_bounds
    (ε : ℝ) (hε : 0 < ε) (hε100 : ε < 100) :
    beamTanPhi ε (centeredAffineLp trialOne)
        < ((913 : ℝ) / 2500000 * ε) /
            (1 - (4227 : ℝ) / 10000000 * ε) ∧
      beamTanPhi ε (centeredAffineLp trialTwo)
        < ((913 : ℝ) / 2500000 * ε) /
            (1 - (7887 : ℝ) / 5000000 * ε) :=
```
