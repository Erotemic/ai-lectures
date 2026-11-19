# Continuous and measurable calculus, domains, and evolution

<!-- BEGIN SPOKEN LECTURE -->

# Continuous and measurable calculus, domains, and evolution

## Continuous Functional Calculus: Build the Operator by Approximation

Suppose A is a bounded self-adjoint operator with spectrum between zero and one. We know how to form A squared. We know how to form three A plus the identity. But what should the square root of A mean if A has no eigenvectors?

There are two ideas in the answer. First, every polynomial has an unambiguous meaning when the scalar variable is replaced by an operator. Second, we can approximate a continuous scalar function by polynomials, and the operator norm behaves well enough to carry that approximation into the operator world.

The second idea requires care. It is not enough that the scalar polynomials converge pointwise. We need one error bound controlling every possible input vector. That is what uniform convergence on the spectrum provides.

### Start from a polynomial

Let p of t be t squared minus two t plus three. Define p of A as A composed with A minus two A plus three times the identity. This uses only addition, scalar multiplication, and composition of bounded operators.

Polynomial evaluation preserves sums and products of polynomials. It also preserves complex conjugation in the form of taking adjoints when A is self-adjoint. At this stage we are doing algebra, not analysis.

The analytic question is how the size of p of A compares with the largest size of p on the spectrum of A. For bounded self-adjoint operators, the answer is exact: the operator norm of p of A equals the maximum of the absolute value of p over the spectrum. This is the crucial norm formula.

Where does it come from? The operator p of A is normal, meaning it commutes with its adjoint. For a normal operator, the operator norm equals the largest magnitude in its spectrum. Polynomial spectral mapping says that the spectrum of p of A consists exactly of values of p on the spectrum of A. Combine the two statements and the norm formula follows.

This is where the self-adjoint hypothesis earns its keep. General non-normal matrices do not satisfy the same norm formula. Their polynomial values can be much larger than the polynomial is on the spectrum.

### Approximate a continuous function

Take a continuous function f on the spectrum of A. Since the spectrum is a compact subset of the real line, we can approximate f uniformly by polynomials. This is a consequence of the Weierstrass approximation theorem, applied to a containing interval if necessary.

Uniformly means that a single small tolerance controls the difference between f and the chosen polynomial at every spectral value. Choose a sequence of polynomials whose maximum approximation errors approach zero.

Now compare two of their operator evaluations. The norm formula says their operator-norm distance is exactly the maximum difference between the two polynomials on the spectrum. So the operators form a Cauchy sequence in operator norm.

The space of bounded operators is complete. The sequence therefore converges to a bounded operator. We define that limit to be f of A. If we had picked a different approximating polynomial sequence, the same estimate would force the same limit. So the definition does not depend on our approximation method.

This is functional calculus constructed from first principles: an approximation theorem for scalar functions, an exact operator norm formula, and completeness.

### What the construction guarantees

The resulting rule from f to f of A preserves sums, products, constants, and complex conjugation. A real-valued continuous function gives a self-adjoint operator. A nonnegative continuous function gives a positive operator.

It is isometric: the norm of f of A is the maximum absolute value of f on the spectrum. This is a much stronger assertion than merely being bounded by a constant times that maximum. It means the functional calculus retains the full uniform size of the scalar function, as seen through the spectrum.

For the square-root function on the nonnegative spectrum of a positive A, we obtain a positive square root. For a real-valued exponential we obtain a positive operator. For the complex-valued function whose value at t is e to the imaginary t, we obtain a unitary operator.

It also satisfies spectral mapping: the spectrum of f of A is the image of the spectrum of A under f. This follows from invertibility. A scalar number lies outside the range of f on the spectrum exactly when one divided by f minus that number is another continuous function there. Functional calculus turns this reciprocal into a bounded inverse.

### A concrete multiplication example

Let A multiply square-integrable functions on the unit interval by t. It has no eigenvectors, but we can evaluate polynomials in it: p of A simply multiplies by p of t.

When we pass to uniformly approximating polynomials, the limit must multiply by f of t. So continuous functional calculus agrees with the obvious answer for this model.

For example, the square root of A multiplies by the square root of t. The exponential of negative A multiplies by e to the negative t. If two continuous functions agree on the interval, they yield the same operator. Nothing requires an eigenbasis.

The general spectral theorem says every bounded self-adjoint operator can be represented, in an appropriate sense, by multiplication. But the polynomial approximation construction allows us to define the continuous calculus before proving the full representation theorem.

### The boundary of the method

What about a function that is one on the left half of the spectrum and zero on the right half? Such a function is discontinuous at the dividing point. Unless that point is isolated from the rest of the spectrum, continuous functions cannot uniformly approximate it. Any continuous approximant must transition somewhere, and the maximum error near the jump cannot be made arbitrarily small.

Yet selecting part of the spectrum is a natural operation. For a matrix, we simply sum the projections corresponding to eigenvalues in the selected region. We want an analogous spectral filter in infinite dimensions.

The missing ingredient is a different notion of approximation. Rather than demand a uniform operator-norm error, we can require convergence when the operators act on each fixed vector. For bounded pointwise approximations, the spectral theorem makes this possible, using measures and dominated convergence. This extension leads to bounded Borel functional calculus.

The important distinction is not just continuous versus discontinuous functions. It is norm convergence versus strong convergence, and the information carried by the spectral measure of each vector. The continuous construction teaches us what functions of operators should do. Spectral measures let us go further without pretending that every scalar approximation is uniform.

## Spectral Projections: Filtering an Operator by Frequency

Imagine a recording that contains low and high tones. A filter that keeps only the low tones does not need to assign a separate name to every frequency. It needs a rule that distinguishes one region of frequencies from another. The result should be a projection: applying the same filter twice does nothing more than applying it once.

A spectral projection performs this kind of selection for a self-adjoint operator. It extracts the component of a vector associated with a chosen set of spectral values. For a finite self-adjoint matrix, the projection is just the sum of projections onto eigenspaces whose eigenvalues lie in that set. In infinite dimensions we need the same idea even when there are no eigenvectors.

### Begin with a matrix switch

Suppose a two-by-two self-adjoint matrix has eigenvalues one and three, with perpendicular eigenspaces. We can ask for the part of an input associated with spectral values below two. That filter keeps the eigenvector component at one and discards the component at three.

The filter is an orthogonal projection. It is self-adjoint, because it treats measurements symmetrically. It is idempotent, meaning its square equals itself. It is also positive, since the squared norm of the retained component is nonnegative.

If we select two disjoint spectral regions and apply both filters in succession, the result is zero. If we select a region and then its complement, the retained pieces add back to the original vector. These are exactly the algebraic rules we want in any dimension.

### Multiplication operators make the rule visible

Take A to be multiplication by t on square-integrable functions on the interval zero to one. For a chosen subset B of the interval, let E of B multiply a function by the indicator of B. In ordinary language, keep the function inside B and erase it outside B.

This is an orthogonal projection. Applying it twice is the same as once. Applying the projections for B and C in succession keeps only their intersection. Selecting the empty set gives the zero operator; selecting the whole interval gives the identity.

Even though A has no eigenvectors, these filters are perfectly meaningful. For the subset from zero to one half, E keeps the left half of a function. For the subset from one half to one, it keeps the right half. We have split a vector by spectral region without finding an eigenvector.

This example also reveals why spectral sets must be measurable. For arbitrary pathological subsets, multiplying by the indicator may not preserve the class of measurable functions we use to define L two. Borel subsets are a standard collection on which the spectral construction works.

### Countably many spectral bands

A finite sum of mutually perpendicular spectral projections behaves just like a finite sum of coordinate projections. But an operator's spectrum can require infinitely many bands. We therefore need countable additivity: if spectral sets are disjoint, the projection for their union is the strong limit of the sum of their projections.

The word strong means that, after applying the partial sums to any fixed vector, the resulting vectors converge in Hilbert-space norm. We do not demand operator-norm convergence of those partial sums. That distinction is necessary when infinitely many spectral pieces are present.

A rule assigning such projections to Borel sets is called a projection-valued measure, or PVM. It looks like a probability measure, but instead of producing a nonnegative number from a set, it produces an orthogonal projection. The analogy becomes exact only after we choose a vector and measure how much of it lies in the projected component.

### From projections to scalar measures

Fix a vector x and consider the squared norm of E of B applied to x. This quantity is nonnegative. It is zero if x has no component in the region B, and the squared norm of x if B is the entire real line.

For disjoint regions, the squared norms of their projected components add, because the components are orthogonal. Thus every vector x produces an ordinary finite measure on the spectral line. This is called its scalar spectral measure.

For the interval multiplication operator, the measure of B is the integral over B of the squared magnitude of x. A vector concentrated on the left side places most of its spectral mass there; a vector concentrated on the right places most of its mass there.

For a diagonal matrix, the measure consists of atoms at the eigenvalues, weighted by squared lengths of the corresponding components. This lets us describe the same mathematics with sums in the diagonal case and integrals in the continuous case.

### A subtle point about a single spectral value

The number one half belongs to the spectrum of multiplication by t. But the projection E of the singleton containing one half is zero. Why? A square-integrable function supported on one point represents the zero vector. The scalar spectral measure assigns that singleton zero mass for every vector.

So a spectral value does not have to carry its own nonzero spectral projection. The spectrum records where the operator cannot be inverted; the projection-valued measure records how vectors distribute across spectral regions. Confusing these two ideas leads to false claims about continuous spectrum.

A small interval around one half can have a nonzero projection, even though the singleton at its center has zero projection. In that sense the spectrum is visible through arbitrarily narrow neighborhoods, not necessarily through point masses.

### Reconstructing an operator from its filters

Consider partitioning the spectrum into many small intervals. Choose one representative number for each interval. Multiply that number by the projection for the corresponding interval, and sum the results. This creates a step-function approximation to the original operator.

As the intervals become finer, the step-function values approach the spectral variable. For bounded self-adjoint operators, we can arrange uniform control over the spectrum, and the approximating operators converge in operator norm. Symbolically, we write A as the integral of lambda against the projection-valued measure E.

Do not imagine that this integral adds projections one physical frequency at a time. It is the limit of finite spectral filters, just as an ordinary Lebesgue integral is built from simple functions.

This is the spectral theorem in projection-valued-measure language. Once we can integrate the identity function of the spectral variable, we can integrate many other functions. In particular, a spectral filter associated with a set B is what we obtain by integrating the indicator function of B.

The spectral theorem therefore gives us a precise way to say, “keep these modes and discard the others,” even if there are no modes represented by individual eigenvectors. It replaces a list of frequencies by a geometry of spectral regions, orthogonal components, and their measures.

## Borel Functional Calculus: When a Function Has Jumps

A thermometer reports a continuously varying temperature. A thermostat makes a discontinuous decision: below a threshold it turns the heat on; above the threshold it turns the heat off. Both are functions of a number, but they behave differently under approximation. A continuously varying function can be uniformly approximated by suitable polynomials. A sharp threshold generally cannot.

Spectral filtering creates the same problem for operators. If A is self-adjoint, we may want to keep spectral values below a cutoff and discard all the others. That is the indicator function of a spectral set applied to A. Such a function may jump, yet the projection-valued measure tells us what it should mean.

### Begin with a step function

Choose several disjoint measurable spectral regions. Assign one scalar value to each region and zero outside their union. The result is a simple function, the kind used to construct the Lebesgue integral.

Its operator value is just a finite linear combination of spectral projections, each weighted by its scalar value. The algebra works immediately: the product of indicator functions for two regions is the indicator of their intersection, and the corresponding projections multiply in exactly the same way.

This also shows why a positive simple function gives a positive operator. A nonnegative linear combination of mutually perpendicular orthogonal projections produces nonnegative quadratic measurements on every vector.

A general bounded Borel measurable function can be approximated pointwise by simple functions that stay uniformly bounded. We want their operator values to converge. But which kind of convergence should we demand?

### Strong convergence instead of norm convergence

Fix one vector x. The spectral theorem associates to x a finite positive measure, recording how much of x lies in each spectral region. The squared norm of the difference between two simple-function operators applied to x is the integral of the squared difference of their scalar functions against that measure.

If the functions converge pointwise and are uniformly bounded, dominated convergence makes this integral tend to zero. Therefore the operator values converge on every fixed vector. This is strong operator convergence.

We define the bounded Borel function of A to be this strong limit. It is independent of the chosen bounded pointwise approximation, and it extends continuous functional calculus.

Why do we not demand operator-norm convergence? Because a step function can disagree substantially with any continuous approximation arbitrarily close to the jump. The operator norm is a worst-case bound over all unit vectors, including vectors concentrated in smaller and smaller spectral neighborhoods of that jump. Strong convergence follows each fixed vector instead, allowing its finite spectral measure to control the error.

This is the correct change of topology, not a relaxation made out of convenience. The difference is exactly what lets discontinuous spectral filters exist.

### Measure-zero changes may disappear

There is a new subtlety. Suppose A multiplies by t on L two of the unit interval. Let f be zero everywhere except at t equal to one half, where it equals one. As an ordinary function on the interval, f is not identically zero. But as a multiplication operator, f of A is the zero operator. A single point has measure zero, so it does not affect any L-two vector.

Consequently, the norm of f of A is not always the ordinary supremum of f over the spectrum. For bounded measurable functions we always have an upper bound by that supremum, but equality may fail. The correct norm is an essential supremum relative to the spectral measure class, equivalently the largest scalar size that matters to the projection-valued measure.

For continuous functions, every nonempty relatively open neighborhood of a spectral value has nonzero spectral projection. This ensures the supremum is still detected, and the continuous norm formula remains exact. For arbitrary Borel functions, pointwise spikes on spectral-null sets can vanish.

### Thresholds and sign functions

Define a function that is one for positive spectral values and zero elsewhere. Applying it to A gives the projection onto its positive spectral part. Similarly, indicators of negative, zero, or interval regions give spectral projections that decompose the Hilbert space.

For a self-adjoint A, the sign function can be defined as plus one on the positive spectrum, minus one on the negative spectrum, and zero at zero. Its operator value is self-adjoint and bounded by one in norm. On the subspace where A has no zero spectral component, it squares to the identity. On the entire space its square is the projection onto the orthogonal complement of the kernel.

A spectral threshold is not necessarily stable under small perturbations of the operator. If spectral values sit near the cutoff, a tiny perturbation may move them across it and change the projection sharply. This is a different phenomenon from the stable evaluation of a continuous function.

That is why the kind of scalar function matters. Smooth or continuous filters often behave robustly, while sharp spectral cuts can be sensitive at gaps that are closing.

### One construction, several useful viewpoints

In a diagonal matrix, bounded Borel calculus is simply entrywise function application in an orthonormal eigenbasis. In a multiplication model, it is multiplication by f composed with the underlying measurable spectral multiplier. In the projection-valued-measure model, it is the integral of f with respect to the spectral projections.

These descriptions are not competing definitions. They are versions of the same operation in different representations. The spectral theorem ensures that the rules agree.

The fundamental identity is a precise description of output length: the squared norm of f of A applied to x equals the integral of the squared absolute value of f against the scalar spectral measure of x. For bounded f that integral is always finite.

The identity also points toward a bigger theory. If f grows without bound, the same integral might be finite for some vectors and infinite for others. A function of an unbounded self-adjoint operator will then need a domain, specifying exactly which vectors are legitimate inputs. The distinction between bounded and unbounded functional calculus is not primarily a new formula. It is the appearance of domain conditions.

## Unbounded Operators: Why the Domain Is Part of the Definition

Imagine an infinite diagonal matrix whose entries are one, two, three, four, and so on. On a finite vector, multiplying by this matrix causes no difficulty. On a square-summable infinite sequence, the same formula may produce a sequence that is not square summable. The instruction makes sense for some inputs but not for every vector in the Hilbert space.

An unbounded operator is not simply a bounded operator whose norm happens to be large. It is a linear transformation defined on a specified subspace called its domain, often a dense subspace of the Hilbert space. Its action and its domain belong together. Changing the domain can change the operator's adjoint, spectrum, and self-adjointness, even when the formal formula stays the same.

### An infinite diagonal example

Let H be the space of square-summable sequences. Define A by multiplying the N-th coordinate by N. For the output to remain square summable, the sum of N squared times the squared magnitude of the input's N-th coordinate must be finite. That condition defines the domain of A.

Take an input whose N-th coordinate is one over N. This sequence belongs to H, since the sum of reciprocal squares converges. But applying A would give the sequence of ones, which is not square summable. Thus the input is outside the domain of A.

Now take an input whose N-th coordinate is one over N squared. It is in the domain of A: the output is the reciprocal sequence, which is square summable. Yet applying A twice would produce a sequence of ones. This input belongs to the domain of A but not to the domain of A squared.

This is not an obscure corner case. It shows that writing A squared without checking domains can assert the existence of an output that does not belong to the Hilbert space.

### Dense domains and the graph

Even though A is not defined everywhere, its domain is dense in H. Every finitely supported sequence belongs to the domain, and finitely supported sequences approximate every square-summable sequence. Density lets us test the operator against arbitrary vectors and develop an adjoint.

Another important property is closedness. Consider the graph of A: all pairs consisting of an allowed input and its output. If a sequence of allowed inputs converges in H, and their outputs also converge in H, a closed operator guarantees that the limit input is still allowed and its output is the output limit.

Our infinite diagonal operator is closed. The reason is coordinatewise: convergence of the inputs and outputs forces the N-th output coordinate to remain N times the N-th input coordinate. If the output limit is square summable, the input limit satisfies the domain condition.

Closedness is the infinite-dimensional version of refusing to lose legitimate input-output pairs when taking limits. It is critical for differential operators, where a sequence of smooth functions can converge to a less regular limit and the derivative may converge only under additional hypotheses.

### Symmetric is not automatically self-adjoint

For a bounded operator on the whole Hilbert space, self-adjointness is the identity A equals its adjoint. For an unbounded operator, we must additionally compare domains. An operator is symmetric if the inner product of A x with y equals the inner product of x with A y for all x and y in its domain. It is self-adjoint when its adjoint has the same domain and agrees there.

These are not equivalent. Take the derivative operator multiplied by negative i on square-integrable functions on an interval. If we initially define it only on smooth functions supported away from the endpoints, integration by parts shows symmetry. But the adjoint allows a larger domain. The operator is not self-adjoint on the small initial domain.

Boundary conditions influence whether a differential operator becomes self-adjoint. Periodic conditions, for instance, can lead to a self-adjoint momentum operator. Different boundary choices can yield different operators even when each one uses the same formal differential expression.

The real distinction is therefore not a cosmetic technicality. It changes which spectral theorem can be applied and which time evolutions are well-defined.

### The graph norm measures what the operator demands

For an unbounded closed operator, define the graph norm of an allowed input by combining its Hilbert-space norm with the Hilbert-space norm of its output. An input is small in graph norm only when both the input and the action of A on it are small.

Our diagonal operator gives large penalties to high coordinates. A sequence may be small in ordinary square-sum norm while having a large output under A. The graph norm detects this because it gives each coordinate a weight involving one plus N squared.

Closedness of A is equivalent to completeness of its domain in the graph norm, provided the ambient Hilbert space is complete. This is a useful way to reframe an unbounded problem: the same operator is bounded as a map from its graph-normed domain into H.

The input space has changed, which is why there is no contradiction in calling the original operator unbounded on H but bounded on the stronger domain norm.

### A multiplication operator on the real line

Take H to be L two of the real line. Define A by multiplying a function by t. A function is in the domain exactly when t times that function is still square integrable. For example, a rapidly decaying function belongs to the domain. Some slowly decaying L-two functions do not.

The operator is self-adjoint on this maximal multiplication domain. It is unbounded because unit functions concentrated far from zero can have arbitrarily large output norms. Yet its action is no more complicated than scalar multiplication point by point.

Here is the bridge to spectral theory. A is already in the representation form promised by the spectral theorem. We can apply a bounded scalar function f by multiplying by f of t on all of H. We can apply an unbounded f only to those vectors for which f of t times the vector remains in H.

So unbounded functional calculus is conceptually a familiar multiplication rule with a domain attached. The general theorem gives the same rule for every self-adjoint operator, including differential operators that need a change of representation before their spectral variables become visible.

### Why this matters for equations

Many equations of mathematical physics involve derivatives. The Laplacian, momentum, and Hamiltonian operators are typically unbounded on L two. One can formally exponentiate them, take square roots, or form inverse powers. But each expression must be checked against the appropriate functional calculus and domain.

The distinction is clearest when comparing two functions of an unbounded self-adjoint A. The function e to the imaginary t times the spectral variable is bounded, so its operator value acts on every vector in H. The function given by the spectral variable squared is unbounded, so its operator value has a smaller domain than A itself.

Thus a very complicated-looking unitary evolution may be defined everywhere, while the apparently simpler expression A squared is only defined on sufficiently regular vectors. Functional calculus makes that contrast precise instead of concealing it behind formal notation.

## Unbounded Functional Calculus: A Formula with an Input Test

Suppose a self-adjoint operator A acts like multiplication by a spectral variable. A bounded scalar function of that variable causes no difficulty: it changes the size of each spectral component by at most a fixed factor. But what if the scalar function grows without bound? Then some inputs may accumulate more squared output magnitude than the Hilbert space allows.

The unbounded spectral calculus answers two questions at once. It tells us what f of A should do, and it tells us exactly which inputs may be given to that operator. The second answer is as important as the first.

### A weighted sum as a model

Start with square-summable sequences and a diagonal operator whose N-th eigenvalue is N. A scalar function f acts on this diagonal by multiplying the N-th coordinate by f of N. To remain in square-summable sequences, the sum of the squared magnitude of f of N times the squared magnitude of the input coordinate must be finite.

If f is bounded, that weighted sum is automatically finite for every square-summable input. If f grows, different vectors behave differently. A vector supported on finitely many coordinates is always allowed, even for a rapidly growing f. Another vector may be square summable but become too large after the spectral multipliers are applied.

For instance, f of N equals N squared gives the square of the original diagonal operator. An input whose N-th coordinate is one divided by N squared belongs to the domain of A, but applying N squared produces the sequence of ones. So it is not in the domain of A squared.

The operator expression f of A therefore includes a hidden integrability condition. Making that condition explicit turns the apparently dangerous unbounded operation into a precise mathematical object.

### Replace sums by spectral measures

The general self-adjoint operator need not have an eigenbasis. It has a projection-valued spectral measure. Every vector x gives an ordinary finite measure, called the scalar spectral measure of x. It records how much squared magnitude the vector places in each spectral region.

To decide whether f of A can act on x, integrate the squared absolute value of f against that measure. If the integral is finite, x belongs to the domain. If the integral is infinite, the operation is not defined on that vector as a Hilbert-space vector.

For an allowed x, the squared norm of the output is exactly that integral. This is the general version of summing weighted squared coordinates.

The construction can be made without guessing. Truncate the scalar function by cutting its magnitude off at a large bound. Each truncation defines a bounded operator by Borel functional calculus. Apply these bounded operators to x. If the weighted integral of the full function is finite, their outputs form a Cauchy sequence in Hilbert-space norm. Define f of A applied to x to be the limit.

That explains the existence of the output. It also explains the domain: outside the weighted-integrability class, the truncated outputs cannot converge to a finite Hilbert-space vector.

### Reconstruct the operator itself

Choose f of lambda equal to lambda. Then f of A is the original self-adjoint operator A. Its domain consists of vectors for which the integral of lambda squared against their scalar spectral measures is finite.

Choose f of lambda equal to lambda squared. Then f of A is A squared with its appropriate domain, often strictly smaller. Choose f of lambda equal to the absolute value of lambda, and obtain the positive operator absolute A. All these constructions use the same spectral measure.

For a positive A, choose the square-root function. The result A to the power one half is a positive self-adjoint operator. Its domain is typically larger than that of A: the square-root weight grows more slowly than the full spectral variable. This is why an energy norm involving one derivative can make sense for functions lacking two derivatives.

The effect is visible in the diagonal model. If the eigenvalue at coordinate N is N squared, then the square-root operator multiplies by N. Some vectors survive multiplication by N but not multiplication by N squared. Fractional powers let us describe intermediate levels of regularity between the ordinary Hilbert-space norm and the stronger domain norms.

### Bounded functions of an unbounded operator

Now take f of lambda equal to one divided by one plus lambda squared. This function is bounded by one on the entire real line. So even when A is unbounded, f of A is bounded and defined on every vector.

The same is true of the complex phase function e to the imaginary t times lambda. Its magnitude is one, so e to the imaginary t A is unitary on all of H. An unbounded self-adjoint generator can thus create an everywhere-defined family of length-preserving transformations.

This is one of the most useful consequences of functional calculus. We may be unable to apply A itself to an arbitrary vector, yet can apply many important functions of A without difficulty.

### Inverses, zero, and domain traps

Suppose A is multiplication by t on L two of the real line. The scalar function one divided by t is unbounded near zero. It defines an operator only on functions whose quotient by t is still square integrable.

There is no genuine contradiction in this statement even though the number zero is not an eigenvalue of A. Inversion may fail because zero lies in the continuous spectrum: there are approximate eigenvectors concentrated near zero on which A becomes arbitrarily small.

A subtle complication arises when multiplying unbounded functions of operators. For bounded functions, f of A followed by g of A equals the function f times g of A on all vectors. For unbounded functions we must check the domain of the composition. Algebraic simplification may produce a bounded scalar function while the two-stage composition is only defined on a proper subspace.

For the multiplication operator on the real line, multiplying by one over t and then by t gives the identity on every input for which division by t was legal. But it does not define the identity on all of L two, because the first step may fail. The single function that equals one almost everywhere, by contrast, does define the identity everywhere. The formulas agree where both are defined, but their operator domains need not be identical.

This is why the spectral calculus is powerful: it tells us when familiar scalar algebra transfers safely to operators and when domain questions remain.

### Functional calculus as a language of regularity

In partial differential equations, positive self-adjoint operators frequently encode derivatives. Applying a square root, a fractional power, or a resolvent changes the regularity demanded of an input. Spectral calculus turns these changes into precise weighted-integrability conditions.

It also gives a common framework for very different physical equations. Heat evolution uses a decaying exponential of a positive operator. Wave evolution uses cosine and sine functions of a square root. Quantum evolution uses unit-modulus complex exponentials.

The reason these constructions coexist is that they are all scalar functions of a spectral variable, interpreted through one operator and its spectral measure. The operator can be unbounded; the function may still be bounded. If the function itself is unbounded, the weighted integral supplies the domain.

## Holomorphic Functional Calculus: Cauchy's Formula for Operators

There is another road from scalar functions to operator functions, and it begins in complex analysis rather than in the spectral theorem for self-adjoint operators. The key idea is Cauchy's integral formula. An analytic function inside a closed contour can be reconstructed from its values along the contour, with a reciprocal factor that measures distance from the evaluation point.

If we replace the scalar point by a bounded operator, the reciprocal becomes the resolvent: the inverse of z times the identity minus the operator. Integrating that resolvent around a contour surrounding the spectrum defines a function of the operator.

This method matters because it works for general bounded operators, not just self-adjoint ones. Its price is a stronger requirement on the scalar function: it must be holomorphic on an open neighborhood of the spectrum.

### Recall the scalar formula

For a complex number a lying inside a positively oriented contour, Cauchy's formula expresses f of a as a contour integral of f of z divided by z minus a. The denominator becomes large near a, but the contour stays away from that point. The integral combines the function's boundary values into its interior value.

Now take a bounded operator T on a complex Banach space. For z outside the spectrum, the operator z times the identity minus T is invertible. Its inverse is the resolvent. As long as our contour stays in the resolvent set, the resolvent varies continuously along it and the operator-valued integral makes sense.

We define f of T by taking one over two pi i times the contour integral of f of z multiplied by the resolvent. The contour must surround the spectrum within a region where f is holomorphic. Different admissible contours give the same result by the operator-valued version of Cauchy's theorem.

This is called the holomorphic, or Riesz–Dunford, functional calculus.

### Why it agrees with polynomials

An unfamiliar definition should pass familiar tests. If f is the constant one, the integral gives the identity operator. If f of z equals z, it gives T. If f is a polynomial, it gives the polynomial evaluated at T in the usual algebraic way.

One way to see the polynomial case is to choose a sufficiently large circle and expand the resolvent as a geometric series in powers of T divided by z. Integrating term by term, all contour integrals vanish except the term matching the desired power. The result is precisely T to that power.

For an exponential, the same construction agrees with the usual norm-convergent power series for e to the T. For a general analytic function, the contour integral supplies the operator value even when no single power series centered at zero covers the whole spectrum.

### A Jordan block reveals the role of derivatives

Consider the two-by-two matrix N with zeros everywhere except a one above the diagonal. Its square is zero. It has only the eigenvalue zero, and only one independent eigenvector.

For a holomorphic scalar function f near zero, the functional calculus gives f of N equal to f of zero times the identity plus f prime of zero times N. The derivative matters because the matrix is not diagonalizable.

For example, the exponential of N is the identity plus N. If we tried to define a function of N using only its eigenvalue zero, we might incorrectly conclude that the exponential is just the identity. The missing derivative term captures the nilpotent part of the matrix.

This is an essential contrast with self-adjoint functional calculus. A self-adjoint matrix cannot have a nontrivial Jordan block; its perpendicular spectral decomposition uses only the values of f at eigenvalues. For a non-normal operator, derivatives of analytic functions may be required.

### Why continuous functions are not enough here

Suppose you know only the value of a continuous function at the spectrum of N, which is the singleton zero. That datum says nothing about its derivative at zero. Two analytic functions can have the same value at zero and different derivatives there, producing different operator values at N.

So for a general non-normal operator there cannot be a functional calculus for all continuous functions on its spectrum that preserves polynomial evaluation and depends only on function values in the self-adjoint manner. The holomorphic calculus solves the problem by requiring functions defined analytically on a neighborhood of the spectrum, so their derivatives are available.

The distinction also explains an important norm phenomenon. The spectrum of N contains only zero, but N itself is not zero. Therefore the norm of the polynomial function t evaluated at N cannot equal the maximum of its absolute value on the spectrum: that maximum is zero while the operator norm of N is positive. The exact norm formula of continuous self-adjoint calculus fails for non-normal operators.

### Spectral mapping survives

Despite these differences, holomorphic functional calculus preserves sums and products and satisfies spectral mapping: the spectrum of f of T is the image of the spectrum of T under f, for holomorphic f on an appropriate neighborhood.

It also provides spectral projections in a different guise. If part of the spectrum is separated from the rest by a contour, the integral of the resolvent around that part projects onto the corresponding invariant spectral subspace. These are called Riesz projections. For a non-normal operator they need not be orthogonal projections. That is another distinction between general analytic calculus and the projection-valued spectral theorem for self-adjoint operators.

### A map of the different calculi

We now have three broad settings. For bounded self-adjoint operators, continuous functions on the spectrum yield bounded operators, with exact norm control. Spectral measures extend that construction to bounded Borel functions and then to unbounded measurable functions with carefully specified domains. For general bounded operators on complex Banach spaces, holomorphic functions near the spectrum yield operator values through contour integration.

The calculi agree on their common ground. Polynomial evaluation means the same thing wherever it appears. For a bounded self-adjoint operator and a holomorphic function defined near its spectrum, the continuous and holomorphic constructions give the same bounded operator.

The different theories are therefore not competing notations. They are tools adapted to different combinations of assumptions and desired scalar functions. The central habit is to ask two questions before using f of A: what kind of operator is A, and what kind of function is f?

## Functional Calculus in Motion: Heat, Waves, and Quantum Evolution

A hot object cools. A plucked string vibrates. A quantum wave function changes phase. These are different physical processes, but their mathematical solutions share a common mechanism: apply a scalar function to an operator that encodes spatial structure.

The scalar function depends on time. The spatial operator supplies spectral values. Functional calculus combines them, turning an ordinary scalar multiplier for each frequency into a transformation on a whole function space.

The advantage is that we do not need to solve a new equation for every initial condition. Once the operator is understood, the same operator-valued function evolves every allowed initial state.

### The heat equation as spectral damping

Begin with a nonnegative self-adjoint operator A. Imagine it as a measure of spatial roughness. For a vibrating string with fixed ends, one example is minus the second derivative, equipped with appropriate boundary conditions. Its eigenfunctions are sine waves. Higher frequencies have larger eigenvalues, growing like the square of the frequency.

The heat equation can be written in the form: the time derivative of u plus A applied to u equals zero. If u begins in a single eigenvector direction, then A acts by multiplication by an eigenvalue lambda, and the equation becomes an ordinary differential equation. Its solution is the initial amplitude multiplied by e to the negative t lambda.

Every eigenmode therefore decays exponentially, with a rate controlled by its eigenvalue. High-frequency roughness decays faster than low-frequency variation. This is why heat flow smooths a signal.

Functional calculus turns this scalar solution into an operator solution: apply the function lambda maps to e to the negative t lambda to A. We write this as e to the negative t A. Because A is nonnegative, the scalar multiplier lies between zero and one for nonnegative time. The resulting operator is a contraction: it cannot increase the Hilbert-space norm of the input.

Even if the initial condition is outside the domain of A, the bounded exponential still acts on it. For positive times, the decay of large spectral values often gives additional regularity. This is why a rough initial temperature profile can immediately become smoother under heat flow.

### Fixed-end strings give a concrete spectrum

For a string of length one with both endpoints fixed, consider the functions sine of n pi x, for positive integers n. After normalization they form an orthonormal basis of L two on the interval. The operator minus the second derivative sends the N-th mode to N squared pi squared times that mode.

Suppose the initial temperature is a sum of the first two modes. The first component decays like e to the negative pi squared times time. The second decays like e to the negative four pi squared times time. At the same positive time, the second mode is suppressed more strongly.

This calculation can be understood without an abstract spectral theorem, because the sine basis is explicit. The spectral theorem generalizes it to settings where the spatial operator cannot be diagonalized by such a familiar formula.

### Quantum motion rotates instead of damping

Now change the scalar exponential. Instead of e to the negative t lambda, use e to the negative imaginary t lambda. Its absolute value is one for every real lambda. If A is self-adjoint, functional calculus makes the resulting operator unitary.

So an initial state keeps its Hilbert-space norm exactly, while each spectral component rotates in complex phase at a rate determined by its spectral value. This is the mechanism behind the abstract Schrödinger evolution.

The contrast with heat is instructive. The same positive operator A may generate a contraction semigroup through a real negative exponential and a unitary group through an imaginary exponential. The difference comes from the scalar function, not from changing the spectral decomposition.

In the quantum case, the equation is expressed with an imaginary unit multiplying the time derivative. In suitable units, the resulting solution is e to the negative imaginary t A applied to the initial vector. For inputs in the domain of A, the derivative in Hilbert-space norm exists and satisfies the equation in the usual strong sense. For arbitrary Hilbert-space vectors, the unitary family still defines a continuous evolution, even when that derivative need not exist.

### Wave motion uses a square root

A wave equation has two time derivatives. In abstract form it is the second time derivative of u plus A u equals zero, with A nonnegative and self-adjoint.

In a single spectral direction with value lambda, the scalar equation describes an oscillator with frequency equal to the square root of lambda. Its solution combines cosine of t times that frequency with sine divided by that frequency. If lambda is zero, the sine-over-frequency expression is interpreted by its continuous limit, which is t.

Functional calculus gives the same solution for the whole operator. The initial displacement is multiplied by cosine of t times square root A. The initial velocity is multiplied by sine of t times square root A divided by square root A, with the zero-frequency value defined by continuity.

The cosine multiplier is bounded by one. The sine-over-square-root multiplier is bounded for every fixed time, because its absolute value is at most the magnitude of t. Thus the operator formula makes sense on the full Hilbert space for fixed time.

For a physically meaningful finite-energy wave solution, more regularity is needed: the initial displacement should lie in the domain of square root A, and the initial velocity in the Hilbert space. Then an energy combining squared velocity and the squared norm of square root A applied to displacement is conserved.

That distinction illustrates the value of domain-aware functional calculus. The operator-valued formula can define a continuous motion on broad input classes; different claims about derivatives and energy require the appropriate domains.

### A computational perspective

In numerical analysis, the same reasoning explains spectral filtering and matrix functions. If a discretization produces a positive self-adjoint matrix, its heat propagator damps high eigenvalue components. Its wave propagator oscillates them. Approximating these operator functions becomes a computational problem: polynomials, rational approximations, Krylov methods, or contour methods can evaluate the action without explicitly forming every eigenvector.

The underlying accuracy question is not just whether a scalar approximation is good on paper. It is whether it is good over the relevant spectrum, in the operator norm or in the state-dependent norm appropriate to the task.

So functional calculus is not an abstract detour from applied mathematics. It is the common language behind smoothing, oscillation, propagation, spectral regularization, and many simulation algorithms.

### What we have gained

We began by asking what it means to apply a function to something that is not a number. For self-adjoint operators, spectral calculus provides the answer by representing an operator through its spectral values and applying the scalar function there. If the scalar function is bounded, the result acts on every vector. If it is unbounded, a weighted-integrability condition specifies the domain.

For non-self-adjoint bounded operators, complex contour integration provides a different but compatible construction for holomorphic functions. Each version preserves the ordinary scalar manipulations that remain valid under its assumptions.

And now the abstractions return to concrete phenomena. Heat decays. Waves oscillate. Quantum states preserve norm. These behaviors emerge from elementary scalar functions evaluated on a spectrum. The achievement of functional calculus is to make that reasoning correct even when the spectrum is infinite, continuous, or hidden from any explicit eigenvector basis.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Continuous Functional Calculus: Build the Operator by Approximation

**Track:** Analysis from First Principles. **Background:** Self-adjoint operators, spectrum, polynomials, and uniform convergence. **Question:** How can a continuous scalar function act on an operator without an eigenbasis?

#### Mathematical companion (not spoken)

For a bounded self-adjoint \(A\) on a nonzero complex Hilbert space with \(K=\sigma(A)\subset\mathbb R\), there exists a unique unital isometric \(*\)-homomorphism
\[
\Phi_A:C(K)\to\mathcal B(H),\qquad \Phi_A(t\mapsto t)=A,
\]
with \(\|\Phi_A(f)\|=\max_{\lambda\in K}|f(\lambda)|\). For polynomials, this follows from spectral mapping and the spectral-radius formula for normal operators; then extend via uniform polynomial approximation and completeness.

The continuous calculus satisfies \(\sigma(f(A))=f(\sigma(A))\), \(f\ge0\implies f(A)\ge0\), and \(f(A)^*=\overline f(A)\). The notation \(f(A)\) here is defined for continuous \(f\) on \(K\); bounded Borel symbols require a later extension.

A useful limit comparison: if continuous \(f_n\to f\) uniformly on \(K\), then \(\|f_n(A)-f(A)\|\to0\). Pointwise convergence alone does not imply norm convergence: with \(A=M_t\) and \(f_n(t)=t^n\) on \([0,1]\), \(f_n(t)\to0\) for \(t<1\) but \(\|f_n(A)\|=1\) for every n. In fact \(f_n(A)x\to0\) for each \(x\in L^2[0,1]\) by dominated convergence, showing strong but not norm convergence.

##### Exercises with answers

1. **Same on spectrum.** If \(\sigma(A)=[0,1]\), can different continuous functions on \(\mathbb R\) define the same operator? **Answer:** Yes, provided their restrictions to \([0,1]\) agree.
2. **Root.** For \(A\ge0\), why is \((\sqrt\cdot(A))^2=A\)? **Answer:** The calculus is multiplicative, and \((\sqrt t)^2=t\) on \(\sigma(A)\).
3. **Norm.** If \(\sigma(A)=\{-2,3\}\), what is \(\|A^2\|\)? **Answer:** \(\max(4,9)=9\).
4. **Pointwise.** Explain why \(t^n\) gives strong but not operator-norm convergence to zero for multiplication on \(L^2[0,1]\). **Answer:** Dominated convergence applies to each fixed vector, but the essential supremum of \(t^n\) is one.

##### Reading and source notes

- [Sheldon Axler, Measure, Integration & Real Analysis](https://measure.axler.net/).
- [Kelly Davis, Spectral Theorem for Bounded Self-Adjoint Operators](https://kellyjdavis.github.io/functional-analysis/spectral-theorems/).
- [MIT OpenCourseWare, Introduction to Functional Analysis](https://ocw.mit.edu/courses/18-102-introduction-to-functional-analysis-spring-2021/pages/lecture-notes-and-readings/).

### Spectral Projections: Filtering an Operator by Frequency

**Track:** Analysis from First Principles. **Background:** Orthogonal projections, self-adjoint operators, Borel sets, and L-two measure. **Question:** How can we select part of a spectrum when there is no eigenvector basis?

#### Mathematical companion (not spoken)

For a bounded self-adjoint \(A\) on a complex Hilbert space, there is a unique projection-valued measure \(E_A:\mathcal B(\mathbb R)\to\mathcal B(H)\) with
\[
E_A(\varnothing)=0,\quad E_A(\mathbb R)=I,\quad E_A(B)E_A(C)=E_A(B\cap C),
\]
and \(E_A(\bigsqcup_n B_n)x=\sum_nE_A(B_n)x\) in Hilbert norm for all x. Its support is \(\sigma(A)\), meaning \(E_A(U)\ne0\) for every open U meeting the spectrum.

For each x, \(\mu_x(B)=\langle E_A(B)x,x\rangle=\|E_A(B)x\|^2\) is a finite positive Borel measure with total mass \(\|x\|^2\). Polarization yields complex measures \(\mu_{x,y}(B)=\langle E_A(B)x,y\rangle\). One writes \(A=\int\lambda\,dE_A(\lambda)\) and for bounded Borel f, \(\langle f(A)x,y\rangle=\int f\,d\mu_{x,y}\).

For \(M_t\) on \(L^2[0,1]\), \((E_A(B)x)(t)=\mathbf1_B(t)x(t)\) and \(\mu_x(B)=\int_{B\cap[0,1]}|x(t)|^2dt\). In particular \(E_A(\{1/2\})=0\), although \(1/2\in\sigma(A)\).

##### Exercises with answers

1. **Two filters.** Prove \(E_A(B)E_A(C)=E_A(B\cap C)\) for a diagonal finite matrix. **Answer:** Both sides retain precisely those eigenspace components whose eigenvalues belong to both sets.
2. **Probability analogy.** If x is a unit vector, what is \(\mu_x(\mathbb R)\)? **Answer:** One, so \(\mu_x\) is a probability measure.
3. **Singleton.** Why can a spectral singleton have zero projection? **Answer:** The corresponding spectral mass may have no atom, as for multiplication on an interval.
4. **Strong additivity.** Does countable additivity of a PVM mean operator-norm convergence of finite sums? **Answer:** No; it means strong operator convergence of the sums on every fixed vector.

##### Reading and source notes

- [Kelly Davis, Spectral Theorem for Bounded Self-Adjoint Operators](https://kellyjdavis.github.io/functional-analysis/spectral-theorems/).
- [Sheldon Axler, Measure, Integration & Real Analysis](https://measure.axler.net/).

### Borel Functional Calculus: When a Function Has Jumps

**Track:** Analysis from First Principles. **Background:** Spectral projections, measurable functions, strong and norm convergence. **Question:** How do we apply a discontinuous function to a self-adjoint operator?

#### Mathematical companion (not spoken)

For a bounded self-adjoint A and bounded complex Borel f on \(\sigma(A)\), define \(f(A)=\int f(\lambda)\,dE_A(\lambda)\). The map is a unital \(*\)-homomorphism into \(\mathcal B(H)\) and
\[
\|f(A)x\|^2=\int_{\sigma(A)}|f(\lambda)|^2\,d\mu_x(\lambda),
\qquad \|f(A)\|\le\sup_{\lambda\in\sigma(A)}|f(\lambda)|.
\]
If \(f_n\) are uniformly bounded in supremum norm and converge pointwise to f, then \(f_n(A)x\to f(A)x\) for every x (bounded convergence). The inequality for the operator norm can be strict: if \(A=M_t\) on \(L^2[0,1]\) and \(f=\mathbf1_{\{1/2\}}\), then \(f(A)=0\) although \(\sup|f|=1\). The precise norm is the essential supremum with respect to the PVM's null sets.

For \(\operatorname{sgn}(A)\), choosing \(\operatorname{sgn}(0)=0\), we have \(\operatorname{sgn}(A)^2=I-E_A(\{0\})\). For bounded self-adjoint A, \(E_A(\{0\})\) is the orthogonal projection onto \(\ker A\).

##### Exercises with answers

1. **Spectral switch.** Let \(A=\operatorname{diag}(-1,2,2)\) and \(f=\mathbf1_{(0,\infty)}\). Find f(A). **Answer:** \(\operatorname{diag}(0,1,1)\).
2. **Point spike.** Why is \(\mathbf1_{\{1/2\}}(M_t)=0\)? **Answer:** It multiplies by an almost-everywhere-zero scalar function.
3. **Two limits.** For \(A=M_t\), do \(A^n\) converge in operator norm to zero? **Answer:** No, every norm is one; they converge strongly to zero by dominated convergence.
4. **Sign.** If A has a nontrivial kernel, why is \(\operatorname{sgn}(A)^2\ne I\)? **Answer:** The sign function vanishes at zero and hence annihilates the kernel.

##### Reading and source notes

- [Kelly Davis, Spectral Theorem for Bounded Self-Adjoint Operators](https://kellyjdavis.github.io/functional-analysis/spectral-theorems/).
- [Sheldon Axler, Measure, Integration & Real Analysis](https://measure.axler.net/).
- [University of Potsdam, Functional Analysis lecture notes](https://www.math.uni-potsdam.de/fileadmin/user_upload/Prof-Math-Phy/Rosenberger/Skripte/Funktionalanalysis_2.pdf).

### Unbounded Operators: Why the Domain Is Part of the Definition

**Track:** Analysis from First Principles. **Background:** Hilbert spaces, linear operators, convergence, and self-adjointness. **Question:** Why do differentiation and infinite diagonal multipliers demand special attention to their domains?

#### Mathematical companion (not spoken)

For \(A:\mathcal D(A)\subset H\to H\) closed and densely defined, the graph norm is \(\|x\|_A=(\|x\|^2+\|Ax\|^2)^{1/2}\); \((\mathcal D(A),\|\cdot\|_A)\) is Banach. For the diagonal operator \((Ax)_n=nx_n\) on \(\ell^2(\mathbb N)\),
\[
\mathcal D(A)=\left\{x:\sum_{n\ge1}n^2|x_n|^2<\infty\right\},\quad
\mathcal D(A^2)=\left\{x:\sum_{n\ge1}n^4|x_n|^2<\infty\right\}.
\]
This A is self-adjoint and positive, with pure point spectrum \(\{1,2,3,\ldots\}\).

For \(M_t\) on \(L^2(\mathbb R)\), \(\mathcal D(M_t)=\{f\in L^2:tf(t)\in L^2\}\); it is self-adjoint and has \(\sigma(M_t)=\mathbb R\). The full spectrum of an unbounded self-adjoint operator may be unbounded, unlike that of a bounded operator.

For an unbounded densely defined A, symmetry means \(\langle Ax,y\rangle=\langle x,Ay\rangle\) for x,y in \(\mathcal D(A)\); self-adjointness requires \(\mathcal D(A^*)=\mathcal D(A)\) and \(A^*x=Ax\). A formal differential expression alone does not determine the domain.

##### Exercises with answers

1. **One power but not two.** Show \(x_n=1/n^2\) lies in \(\mathcal D(A)\setminus\mathcal D(A^2)\). **Answer:** \(\sum n^2/n^4=\sum1/n^2<\infty\) but \(\sum n^4/n^4=\infty\).
2. **Unit input, large output.** Find unit vectors showing A is unbounded. **Answer:** The standard unit vector \(e_n\) has \(\|Ae_n\|=n\to\infty\).
3. **Why graph norm?** Does \(x_k\to x\) in H alone imply \(Ax_k\to Ax\)? **Answer:** No; graph-norm convergence requires both input and output convergence.
4. **Boundary choice.** Why is a symmetric derivative expression not necessarily self-adjoint? **Answer:** Its adjoint can have a larger domain; self-adjointness compares domains as well as formulas.

##### Reading and source notes

- [University of Potsdam, Functional Analysis II, unbounded spectral theorem](https://www.math.uni-potsdam.de/fileadmin/user_upload/Prof-Math-Phy/Rosenberger/Skripte/Funktionalanalysis_2.pdf).
- [Sheldon Axler, Measure, Integration & Real Analysis](https://measure.axler.net/).
- [MIT OpenCourseWare, Introduction to Functional Analysis](https://ocw.mit.edu/courses/18-102-introduction-to-functional-analysis-spring-2021/pages/lecture-notes-and-readings/).

### Unbounded Functional Calculus: A Formula with an Input Test

**Track:** Analysis from First Principles. **Background:** Spectral projections, scalar spectral measures, and domains of closed operators. **Question:** How can a self-adjoint operator act through an unbounded scalar function without losing control of its domain?

#### Mathematical companion (not spoken)

Let A be self-adjoint, possibly unbounded, with spectral PVM \(E_A\). For any Borel measurable \(f:\mathbb R\to\mathbb C\) finite everywhere (or finite \(E_A\)-almost everywhere), define
\[
\mathcal D(f(A))=\{x\in H:\int_{\mathbb R}|f(\lambda)|^2\,d\mu_x(\lambda)<\infty\},
\qquad\|f(A)x\|^2=\int|f|^2d\mu_x.
\]
One constructs \(f(A)x\) as the limit of \(f_n(A)x\) for bounded truncations \(f_n=f\,\mathbf1_{\{|f|\le n\}}\), or magnitude clipping. The resulting operator is closed and normal; it is self-adjoint when f is real-valued \(E_A\)-almost everywhere.

For \(A=\operatorname{diag}(1,2,3,\ldots)\) on \(\ell^2\), \(\mathcal D(A^s)=\{x:\sum n^{2s}|x_n|^2<\infty\}\) for \(s>0\). On \(L^2(\mathbb R)\) with \(A=M_t\), \(f(t)=t^{-1}\) for \(t\ne0\) and \(f(0)=0\), \(f(A)\) is multiplication by \(1/t\) on \(\{x:x/t\in L^2\}\). The product \(A f(A)\) equals I on this proper domain, whereas \((t f(t))(A)=I\) on all of H, since \(t f(t)=1\) almost everywhere relative to the PVM. Product identities for unbounded symbols are domain-sensitive.

##### Exercises with answers

1. **Domain hierarchy.** For \(A=\operatorname{diag}(n)\), is \(\mathcal D(A^2)\subseteq\mathcal D(A)\)? **Answer:** Yes; \(n^4\ge n^2\) for all \(n\ge1\).
2. **Unitary.** If A is self-adjoint, what is the norm of \(e^{itA}x\)? **Answer:** \(\|x\|\), by the weighted-integral formula and \(|e^{it\lambda}|=1\).
3. **Fractional power.** If \(A=\operatorname{diag}(n^2)\), which is more restrictive: \(\mathcal D(A^{1/2})\) or \(\mathcal D(A)\)? **Answer:** \(\mathcal D(A)\subseteq\mathcal D(A^{1/2})\), typically strictly.
4. **Domain trap.** Why need \(A(1/A)\) not be the everywhere-defined identity? **Answer:** The first unbounded inverse may have a proper domain even if the scalar product equals one almost everywhere.

##### Reading and source notes

- [University of Potsdam, Functional Analysis II, spectral theorem for unbounded operators](https://www.math.uni-potsdam.de/fileadmin/user_upload/Prof-Math-Phy/Rosenberger/Skripte/Funktionalanalysis_2.pdf).
- [Johns Hopkins University, Functional Analysis lecture notes, unbounded operators and calculus](https://math.jhu.edu/~js/Math637/eth.functionalanalysis.pdf).

### Holomorphic Functional Calculus: Cauchy's Formula for Operators

**Track:** Analysis from First Principles. **Background:** Complex contour integrals, resolvents, spectra, and matrices. **Question:** How can contour integration define functions even of non-self-adjoint operators?

#### Mathematical companion (not spoken)

For a complex unital Banach algebra B, \(a\in B\), and \(f\) holomorphic on a neighborhood \(U\supset\sigma(a)\), choose a positively oriented cycle \(\Gamma\subset U\cap\rho(a)\) surrounding the full spectrum. Then
\[
f(a)=\frac{1}{2\pi i}\int_\Gamma f(z)(z1-a)^{-1}\,dz.
\]
This is independent of admissible \(\Gamma\); it is a unital algebra homomorphism, agrees with polynomial evaluation, and satisfies \(\sigma(f(a))=f(\sigma(a))\). A large-circle Neumann expansion verifies the polynomial case.

For \(N=\begin{psmallmatrix}0&1\\0&0\end{psmallmatrix}\), \(N^2=0\), so \(f(N)=f(0)I+f'(0)N\). In particular \(e^N=I+N\), although \(\sigma(e^N)=\{1\}\). This demonstrates why \(\|f(N)\|=\sup_{\sigma(N)}|f|\) fails for nonnormal N.

For a spectral component enclosed by \(\Gamma\) disjoint from other components, the Riesz projection is \(P=(2\pi i)^{-1}\int_\Gamma(zI-T)^{-1}dz\). In general \(P^2=P\) but \(P\ne P^*\); orthogonality requires additional structure.

##### Exercises with answers

1. **Nilpotent.** Compute \((I-N)^{-1}\) for \(N^2=0\). **Answer:** \(I+N\).
2. **Analytic function.** If \(f(z)=1/(1-z)\), what is \(f(N)\)? **Answer:** \(I+N\).
3. **Non-normal norm.** Why does \(\|N\|=\max_{z\in\sigma(N)}|z|\) fail? **Answer:** The right side is zero, while N is nonzero and has norm one in the Euclidean operator norm.
4. **Compare calculi.** For a self-adjoint bounded T and holomorphic f near its spectrum, do continuous and holomorphic calculi agree? **Answer:** Yes; both agree on polynomials, and the standard uniqueness/approximation arguments identify them.

##### Reading and source notes

- [Michael Taylor, Lectures on Banach Algebras, Appendix A: Holomorphic Functional Calculus](https://mtaylor.web.unc.edu/wp-content/uploads/sites/16915/2018/04/banalg.pdf).
- [Foundations of von Neumann Algebras, Banach Algebras and Holomorphic Functional Calculus](https://openmaths.org/courses/foundations-of-von-neumann-algebras/banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.html).

### Functional Calculus in Motion: Heat, Waves, and Quantum Evolution

**Track:** Analysis from First Principles. **Background:** Positive self-adjoint operators, bounded Borel functional calculus, and energy norms. **Question:** How do scalar functions of spectral values solve evolution equations?

#### Mathematical companion (not spoken)

For \(A\ge0\) self-adjoint on H, spectral calculus defines the heat semigroup \(S(t)=e^{-tA}\) for \(t\ge0\), with \(\|S(t)\|\le1\), \(S(t+s)=S(t)S(s)\), and strong continuity at \(t=0\). For \(x\in\mathcal D(A)\), \(\frac d{dt}S(t)x=-AS(t)x\). The Schrödinger unitary group \(U(t)=e^{-itA}\) obeys \(\|U(t)x\|=\|x\|\) and for \(x\in\mathcal D(A)\) satisfies \(i\partial_t U(t)x=AU(t)x\).

The abstract wave equation \(u_{tt}+Au=0\) has formula
\[
u(t)=\cos(t\sqrt A)u_0 + g_t(A)v_0,\quad
 g_t(\lambda)=\begin{cases}\sin(t\sqrt\lambda)/\sqrt\lambda,&\lambda>0,\\t,&\lambda=0.\end{cases}
\]
For fixed real t, \(|g_t(\lambda)|\le|t|\), so both terms define bounded operators on H. Finite-energy data \(u_0\in\mathcal D(A^{1/2})\), \(v_0\in H\) yield energy conservation \(E(t)=\tfrac12(\|u_t(t)\|^2+\|A^{1/2}u(t)\|^2)=E(0)\), understood at the appropriate solution regularity.

For the Dirichlet Laplacian \(A=-\partial_x^2\) on \((0,1)\), \(\phi_n(x)=\sqrt2\sin(n\pi x)\), \(A\phi_n=n^2\pi^2\phi_n\), and \(e^{-tA}\phi_n=e^{-tn^2\pi^2}\phi_n\). This directly illustrates high-frequency damping.

##### Exercises with answers

1. **Two heat modes.** Which decays faster under heat flow, \(\phi_1\) or \(\phi_2\)? **Answer:** \(\phi_2\), with exponent \(-4\pi^2t\) rather than \(-\pi^2t\).
2. **Norm preservation.** Why is \(e^{-itA}\) unitary for self-adjoint A? **Answer:** Its scalar spectral multiplier has modulus one for real \(t\).
3. **Zero frequency.** What is \(\lim_{\lambda\downarrow0}\sin(t\sqrt\lambda)/\sqrt\lambda\)? **Answer:** t.
4. **Initial domain.** May \(e^{-tA}u_0\) be defined when \(u_0\notin\mathcal D(A)\)? **Answer:** Yes; for \(t\ge0\) the exponential is bounded. Differentiability at zero is a separate matter.

##### Reading and source notes

- [MIT OpenCourseWare, Introduction to Functional Analysis](https://ocw.mit.edu/courses/18-102-introduction-to-functional-analysis-spring-2021/pages/lecture-notes-and-readings/).
- [University of Potsdam, Functional Analysis II, unbounded spectral theorem](https://www.math.uni-potsdam.de/fileadmin/user_upload/Prof-Math-Phy/Rosenberger/Skripte/Funktionalanalysis_2.pdf).
- [Sheldon Axler, Measure, Integration & Real Analysis](https://measure.axler.net/).
