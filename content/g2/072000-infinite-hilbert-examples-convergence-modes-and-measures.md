# Infinite Hilbert examples, convergence modes, and measures

<!-- BEGIN SPOKEN LECTURE -->

# Infinite Hilbert examples, convergence modes, and measures

## Infinite-dimensional Hilbert examples

Every real symmetric finite matrix has an orthonormal eigenbasis. Consider what that statement would mean for an operator on functions: could we find enough eigenfunctions to describe every square-integrable signal? For multiplication by the coordinate on the unit interval, the answer is no. An eigenfunction with eigenvalue lambda would have to be supported where the coordinate equals lambda, a set with only one point and hence zero measure.

The operator is nevertheless bounded and self-adjoint, and it has a nonempty spectrum. This single example shows why infinite-dimensional spectral theory needs more than a list of eigenvectors. We will build the surrounding Hilbert-space models first, then explain how approximate eigenvectors and spectral measures recover the missing information.

In infinite dimensions, the same procedure can fail at its first step. A bounded self-adjoint operator can have no nonzero eigenvectors at all. We need to understand a concrete example before replacing matrices with spectral measures.

Four standard models exhibit these phenomena: square-summable sequences, square-integrable functions, multiplication by a coordinate, and the unilateral shift.

### The sequence Hilbert space

Start with an infinite list of complex numbers: x-zero, x-one, and so on. Retain only sequences whose squared absolute values add to a finite number. This is the space called ell two.

The inner product of two such sequences is the sum of the conjugate of one coordinate times the corresponding coordinate of the other. Cauchy–Schwarz guarantees convergence. The norm is the square root of the sum of squared absolute values.

The familiar coordinate vectors, with one entry equal to one and the rest zero, form an orthonormal basis. But a general vector is an infinite sum of these basis directions, converging in norm. Truncating after N coordinates gives approximations, and the squared error is exactly the tail of the convergent series.

To see completeness, imagine a Cauchy sequence of vectors in ell two. Each coordinate is Cauchy in the complex numbers, hence converges. An inequality for finite partial sums shows that the coordinatewise limit still has bounded squared energy. The same tail and Cauchy arguments then show convergence in ell two norm.

This space has the geometric structure of Euclidean space, but no finite list spans it.

### Square-integrable functions

Now consider functions on the interval from zero to one. Keep those for which the integral of squared absolute value is finite. Identify two functions if they differ only on a set of measure zero. We call the resulting space L two.

Why identify functions almost everywhere? Because the integral norm cannot detect a difference at a single point. If f and g disagree only at one position, their difference has norm zero. A normed space must regard any vector of norm zero as the zero vector.

The inner product is the integral of the conjugate of f times g. Again Cauchy–Schwarz controls it.

There is a useful comparison with ell two. In ell two we sum squared coordinates. In L two we integrate squared values over a continuum. Both are Hilbert spaces, and both have countable orthonormal bases in these standard examples. Yet the most natural operators on them can have very different spectral behavior.

For example, take the constant function one on the unit interval. Its L two norm is one. The coordinate function f of x equals x has squared norm equal to the integral of x squared from zero to one, which is one third. Its norm is therefore one over the square root of three.

### Multiplication by the coordinate

Define an operator M on L two by sending a function f to the function x times f of x. Its norm is at most one because the magnitude of x is at most one on the interval. In fact its operator norm equals one: choose unit functions supported very close to the right endpoint, where multiplication by x almost preserves their lengths.

M is self-adjoint. To check this, move the real scalar x between the two factors in the inner-product integral. This is the direct analogue of a real diagonal matrix.

Now ask whether M has an eigenvector. If M f equals lambda times f, then x times f of x equals lambda times f of x for almost every x. So f can be nonzero only where x equals lambda.

For each fixed lambda, that set is either empty or a single point. A single point has Lebesgue measure zero. Therefore f is the zero vector of L two. No nonzero eigenvector exists.

We have constructed a bounded self-adjoint operator on a nonzero Hilbert space with no eigenvectors. The finite eigenbasis proof cannot even begin.

### The spectrum still has content

Perhaps the operator has no spectrum at all? No. Its spectrum is the entire interval from zero to one.

First take a complex number lambda outside that interval. The function one divided by x minus lambda is bounded on the interval. Multiplication by this reciprocal gives a bounded inverse to M minus lambda times the identity. Such lambda lie outside the spectrum.

Now choose lambda inside the interval. Around lambda, take a tiny subinterval and a function supported there, normalized to have L two norm one. On that support, x is close to lambda. The norm of M f minus lambda f is therefore as small as the width of the subinterval.

So M minus lambda cannot have a bounded inverse. If it did, applying that inverse would force every unit vector to have its image bounded below by a positive constant. Our localized test functions contradict this.

At the endpoints, use one-sided small intervals. The same argument works. Hence the full closed interval is the spectrum, even though no spectral point is an eigenvalue.

These localized functions are approximate eigenvectors. Their supports shrink as their errors shrink, so they do not approach a nonzero eigenvector in L two norm.

### A diagonal model with infinitely many eigenvalues

Contrast M with a diagonal operator D on ell two. Let D multiply coordinate n by one divided by n plus one. Every coordinate vector is an eigenvector, and the corresponding eigenvalues approach zero.

Zero belongs to the spectrum because the unit coordinate vectors far out in the sequence have images with norms tending to zero. There is no bounded inverse for D. Yet zero is not an eigenvalue: no nonzero coordinate can be supported where the diagonal entry vanishes, since every entry is positive.

Here the spectrum consists of the listed positive eigenvalues together with their limit point zero. This example shows that even when an eigenbasis exists, the spectrum can contain a point that is not an eigenvalue.

The multiplication example goes further: none of the points in its interval spectrum are eigenvalues.

### The unilateral shift

A final example reminds us why self-adjointness matters. On ell two define the forward shift U by placing a zero at the beginning of a sequence and moving every entry one position to the right.

U preserves the norm exactly, so U adjoint times U equals the identity. But U is not onto: no vector in its range has a nonzero first coordinate. Therefore U times U adjoint is the projection onto the subspace with first coordinate zero, rather than the identity.

In finite dimensions, an isometry of a space into itself must be surjective. In infinite dimensions, this implication fails.

Its adjoint is the backward shift, which discards the first coordinate. The backward shift has genuine eigenvectors: if the magnitude of lambda is less than one, the sequence one, lambda, lambda squared, and so on is square-summable and is an eigenvector of the backward shift with eigenvalue lambda.

This distinction between a shift and its adjoint is impossible for a unitary operator and illustrates why we must not treat every norm-preserving map as unitary.

### What replaces the finite eigenbasis

The continuous multiplication model suggests the answer. For a measurable subset of the interval, define a projection that keeps the values of a function on that subset and sets it to zero elsewhere.

Two disjoint subsets give orthogonal projections. The projection for a union of disjoint subsets combines their contributions. Instead of one projection per eigenvalue, we have one projection for each sufficiently well-behaved set of spectral values.

For a finite diagonal matrix these projections simply select coordinate eigenspaces. For multiplication by x they select the support of a function according to the value of x, even though there are no eigenvectors.

A spectral theorem without an eigenvector basis requires measurable sets and countably additive projection-valued measures, which supply the appropriate sums of spectral projections.

## Weak, strong, and uniform convergence in Hilbert spaces

A sequence of vectors may look smaller and smaller when tested against any fixed direction, while never becoming shorter. A sequence of operators may give increasingly accurate answers for each fixed vector, while its worst-case error never decreases. These two observations force us to distinguish several meanings of convergence in Hilbert space.

Start with the space of square-summable sequences. Its vectors are infinite lists of numbers whose squares have finite sum. The length of a vector is the square root of that sum. The first coordinate direction has one in its first position and zero elsewhere. The second coordinate direction has one in its second position, and so on. Call the direction in position n the n-th basis vector.

Every one of these basis vectors has length one. The sequence of basis vectors therefore never approaches zero in length. Yet for any single fixed square-summable vector, its inner product with the n-th basis vector approaches zero. The inner product simply reads off the n-th coordinate, and the coordinates of a square-summable vector must approach zero. We have found convergence detected by inner products, without convergence detected by lengths.

### Weak convergence of vectors

A sequence of vectors converges weakly to x if, for every fixed test vector y, the inner products of the sequence members with y approach the inner product of x with y. The order of quantifiers is important. Choose y once; then allow n to increase. There is no demand that the convergence happen uniformly over every unit test vector.

Convergence in norm is stronger: the lengths of the differences from x approach zero. The Cauchy–Schwarz inequality shows why norm convergence implies weak convergence. The absolute inner product of a difference with y is at most the length of that difference times the length of y.

Our coordinate example shows the converse fails in infinite dimensions. Each basis vector is weakly convergent to zero, since its inner product with every fixed test vector tends to zero, but its norm stays one.

Notice one more distinction. Weak convergence does not force the norms to converge. It does imply that the norm of the weak limit is no larger than the lower limit of the sequence's norms. One can see the basic reason directly: a fixed unit vector in the direction of the weak limit detects its length through inner products.

### Strong convergence of operators

Now replace a sequence of vectors by a sequence of bounded linear operators. We say the operators converge strongly to T if, for each fixed vector x, their outputs converge in norm to T x. The operators themselves act on the same Hilbert space, and the limit is again a bounded operator when a suitable uniform-boundedness hypothesis is present; in fact a strongly convergent sequence of bounded operators is uniformly bounded by the uniform boundedness principle.

For a concrete example, let P n keep only the first n coordinates of a square-summable sequence and set all remaining coordinates to zero. It is an orthogonal projection onto the span of the first n basis vectors.

For a fixed input x, the error between x and P n x consists of the tail of its coordinate list. Its squared length is the sum of the squares after coordinate n. Because the whole square-sum converges, that tail tends to zero. Thus P n converges strongly to the identity operator.

But each P n kills the next basis vector. Apply the difference between the identity and P n to that unit vector. The output still has length one. Consequently the operator norm of that difference is one for every n. Strong convergence has not reduced the worst-case error.

### Uniform convergence in operator norm

Operator-norm convergence to T requires the maximum output error over all unit inputs to approach zero. It is sometimes called uniform operator convergence. The difference from strong convergence is whether the test vector may vary with n.

With the coordinate projections, the troublesome vector does vary: at stage n, take the next basis direction, which the approximation has not yet included. Every fixed input is eventually well approximated in norm, but there is always another direction witnessing a full unit of error.

In a finite-dimensional space this distinction disappears for bounded linear operators. Check the finitely many coordinate basis vectors. If every basis output error approaches zero, the error on any unit input is bounded by a constant times the sum of those finitely many errors. That argument relies on having only finitely many directions.

### Weak convergence of operators

There is also a weaker notion for operators: T n converges to T in the weak operator sense if, for each fixed pair x and y, the inner product of T n x with y approaches that of T x with y. Strong operator convergence implies this by Cauchy–Schwarz.

Weak operator convergence does not, by itself, imply strong convergence. Take a bounded operator T n that sends a fixed first basis vector to the n-th basis vector and sends every vector perpendicular to the first basis vector to zero. For any fixed x and y, the measured inner product tends to zero, because the n-th coordinate of y tends to zero. But the output on the first basis vector always has norm one. So the operators converge weakly to zero without converging strongly.

There are now three useful operator tests. A fixed pair of input and measurement directions tests weak convergence. A fixed input tests strong convergence through the entire output length. The largest error over all unit inputs tests operator-norm convergence.

### Why the distinction changes mathematical arguments

Suppose T n approaches the identity strongly, as our coordinate projections do. It would be incorrect to conclude that T n is eventually invertible. Every finite-coordinate projection has a nontrivial kernel, even though its strong limit is the identity.

Operator-norm convergence gives a different conclusion. If the norm of T n minus the identity is strictly less than one, then T n is invertible, using the geometric or Neumann series for its inverse. Thus norm convergence to the identity eventually guarantees invertibility.

This difference becomes important when using finite-dimensional approximations to study spectra. Approximation on each fixed vector may be exactly the convergence available, while conclusions about inverse operators require additional hypotheses.

### A domain warning for unbounded operators

If A is unbounded, applying A to the truncated vector P n x requires P n x to belong to the domain of A. Even if P n x tends to x in the Hilbert-space norm, it does not follow that A P n x tends to A x. The stronger graph norm requires both the inputs and their images under A to converge.

For the diagonal operator that multiplies coordinate k by k, the finite-coordinate projections have a particularly good property: they preserve its domain, and for each vector in that domain, both the discarded coordinates and their k-weighted versions have square-summable tails. Hence P n x approaches x in graph norm. That is an extra fact about the chosen operator and cutoffs, not a consequence of strong operator convergence alone.

A useful final test is to ask what remains fixed as n changes. A fixed vector? Two fixed vectors used in an inner product? Or the worst possible vector at each n? Those are, respectively, strong, weak-operator, and norm-operator perspectives. The coordinate examples show exactly why we need all three.

## Sigma-algebras and Borel sets

Imagine a sound whose frequencies fill an interval rather than a list of individual notes. We want a filter that keeps one frequency band and discards the rest. The mathematical version uses the Hilbert space of square-integrable functions on the interval from zero to one. In this space, functions that agree except on a set of length zero represent the same vector. Define an operator A that multiplies a function's value at t by t. To keep only the part supported between one quarter and one half, multiply the function by one on that interval and by zero outside. Doing this twice has the same effect as doing it once: it is an orthogonal projection.

Which sets of frequencies can we legitimately select? Intervals are a start, but repeatedly combining filters produces complements, intersections, and countable unions of intervals. We need a collection of sets that remains valid under those operations. That collection is a sigma-algebra: it contains the whole underlying set and is closed under complements and countable unions. Countable intersections then follow automatically.

The Borel sigma-algebra is generated by the open sets of the real line. It contains the intervals needed for ordinary spectral windows and enough sets for limiting constructions. The distinction is worth developing carefully: a sigma-algebra determines which sets can be selected, while a measure assigns sizes to those sets. Spectral projections use the measurable sets to identify subspaces rather than assigning ordinary numerical sizes.

### Why finite set operations are insufficient

Think first about an event such as a number lying between two endpoints. We may want its complement: the number lies outside that interval. We may want the union of several intervals. These are ordinary finite set operations.

But spectral approximations introduce limits. Suppose we select the union of the intervals from one over n to one, with n ranging over positive integers. The union is the interval strictly above zero and at most one. No finite stage equals that union.

Or suppose we intersect the intervals from negative one over n to positive one over n. Their common intersection is the singleton containing zero.

If the allowed sets were closed only under finite unions and intersections, these natural limiting constructions might leave the collection.

A sigma-algebra is designed to avoid that failure. It is a family of subsets containing the whole space, closed under complements, and closed under countable unions. The empty set then belongs automatically. Countable intersections belong by taking complements twice.

Countable means we can index the operation by the natural numbers. It does not demand closure under every possible uncountable union.

### Three elementary examples

The smallest sigma-algebra on a set contains only the empty set and the whole set. It can distinguish nothing within the space.

The largest sigma-algebra is the power set: every subset is allowed. On a finite set, this choice is harmless and often the default.

Between them lie many other sigma-algebras. For example, partition a set of four points into the pair one and two, and the pair three and four. Allow only the empty set, the whole set, and the two pairs. Complements exchange the pairs, and countable unions cannot produce a singleton. This family is a sigma-algebra.

It represents a limited ability to distinguish events. We can tell which pair contains a point, but not which point inside the pair.

### Generating a sigma-algebra

Given a collection of subsets, consider all sigma-algebras containing them. Their intersection is itself a sigma-algebra: the whole space is in every family, complements stay in every family, and so do countable unions.

Therefore there is a smallest sigma-algebra containing the original collection. We call it the sigma-algebra generated by that collection.

The Borel sigma-algebra of the real line is the sigma-algebra generated by all open subsets. This definition immediately includes closed sets, because complements of open sets are closed. It includes open and closed intervals, half-open intervals, and singleton points.

For example, the singleton zero is the intersection, over positive n, of the open intervals centered at zero with radius one over n. Each stage contains many numbers; only zero survives every stage. We are allowed that countable intersection, so the singleton is Borel.

Likewise, the half-open interval greater than a and at most b is the intersection of the open ray greater than a with the closed ray at most b. Both are Borel.

We do not need every subset of the real line to be Borel. Our construction specifies a substantial collection generated from topology by countable operations, and it is the collection used in the standard spectral-measure theorem.

### Why open sets are a good starting point

Continuity already tells us how open sets behave. A function f between topological spaces is continuous precisely when the preimage of every open set is open.

A measurable function is defined similarly, except the preimage of an open set need only be in the domain's sigma-algebra. The codomain may be the real or complex numbers with their Borel sigma-algebras.

Because preimages commute with complements and countable unions, checking preimages of open sets is enough to ensure that preimages of all Borel sets are measurable.

This is a compact but powerful argument. Let F be the family of target sets whose preimages are measurable. F is a sigma-algebra. If it contains the open sets, it contains the Borel sigma-algebra they generate.

So continuity implies Borel measurability. But measurability permits many discontinuous functions, including the indicator function of a Borel set.

### Indicators and step functions

For a set E, define its indicator to be one on E and zero outside. It is measurable exactly when E is measurable, in the usual real-valued setting. To see the forward direction, take the preimage of an open neighborhood of one that excludes zero. To see the reverse, note that the preimage of any open subset of the real line is one of four sets: empty, whole, E, or its complement.

A finite linear combination of indicators of measurable sets is a simple function. Such functions take only finitely many values. Their role in integration is similar to the role of step functions in basic calculus.

For spectral theory, the indicator has another interpretation: a function of an operator that selects the spectral values in E. In the finite spectral theorem, this was just the sum of eigenspace projections whose eigenvalues belonged to E.

For the multiplication operator M, the indicator of E applied to M will multiply a function f of x by one when x lies in E and by zero elsewhere. The result is an orthogonal projection on L two.

The set operations translate directly into projection algebra. An intersection becomes multiplication of commuting projections. A complement becomes identity minus the projection. For disjoint sets, the corresponding projections have orthogonal ranges.

### Boundary points matter

Consider the sets of spectral values strictly below a threshold and those at or below it. Their difference is the singleton at the threshold.

In the multiplication-by-x model on an interval with Lebesgue measure, that singleton has measure zero. So the two indicator operators act identically on L two functions, because they differ only on a null set.

For a diagonal operator with a genuine eigenvector at the threshold, the singleton projection can be nonzero. Then the open and closed spectral cuts differ by the entire corresponding eigenspace.

This is why we must retain exact endpoint conventions in a perturbation theorem. The phrase spectrum below a threshold does not by itself tell us whether the threshold is included, and the distinction can change the selected subspace.

### Countable addition of spectral projections

Suppose E-one, E-two, and so forth are pairwise disjoint Borel sets. Their union is Borel. A projection-valued spectral measure should assign a projection to each set in a way compatible with such disjoint unions.

But we must be careful about the type of convergence. The sum of the projections need not converge in operator norm. For example, projections onto successive coordinate axes in ell two have partial sums that approach the identity on every individual vector, while the operator-norm distance from any finite partial sum to the identity remains one.

The correct form of countable additivity is therefore usually strong operator convergence: apply the partial sums to each fixed vector and take its norm limit.

This example already identifies the two separate requirements. A sigma-algebra tells us which countable unions are permitted. The strong limit on each fixed vector tells us what it means to add the corresponding projections. Neither condition can replace the other.

### From measurable sets to operator filters

Continuous functional calculus can apply continuous functions to a self-adjoint operator. Indicators of intervals are generally discontinuous, so they are not covered by that construction alone.

A bounded Borel calculus admits bounded measurable functions as symbols. It includes indicators and therefore spectral projections. It also respects addition, multiplication, and adjoints in the appropriate operator algebra.

A spectral projection of a set is defined only for sets in the measurable class of the spectral measure, usually the Borel sets. The practical lesson is that a frequency filter needs two ingredients: an allowed set and a rule that turns that set into an actual projection. Sigma-algebras supply the first. The spectral theorem supplies the second.

## Measures, integration and L2

Consider two functions on the interval from zero to one. One is concentrated on a short interval, and the other is spread across the whole unit interval. To compare their sizes, we need an operation that adds the squared magnitude of each function across its support. That operation is an integral, and the resulting geometry is the Hilbert space called L two.

Before integrating, we need a way to assign sizes to sets. A sigma-algebra is a collection of allowed sets closed under complements and countable unions. A measure assigns a nonnegative size to each allowed set. From those two ingredients we can build integrals, explain which limiting operations preserve them, and obtain a complete space of functions. Everything will be illustrated with ordinary lengths on the unit interval.

### What a measure supplies

A measure assigns a number between zero and infinity, including possibly infinity, to each measurable set. The empty set has measure zero. If we have countably many pairwise disjoint measurable sets, the measure of their union equals the sum of their measures.

That last requirement is called countable additivity. It strengthens the familiar rule that two disjoint intervals have combined length equal to the sum of their lengths.

For Lebesgue measure on the real line, an interval receives its ordinary length. A single point has measure zero. Countable sets have measure zero because they are countable unions of zero-measure singletons.

A different example is the Dirac measure concentrated at a point a. A measurable set has measure one if it contains a, and zero otherwise. In this measure, a singleton can have positive measure. The same Borel set may therefore have very different significance under different measures.

The contrast already appears in the simplest spectral examples. Multiplication by the coordinate t on L two of the unit interval cannot detect a change at a single point under Lebesgue measure. A diagonal matrix, however, can put positive weight on a single eigenvalue. A spectral measure generalizes both situations by recording which sets actually carry weight.

### Three consequences of countable additivity

First comes monotonicity. If E is contained in F, split F into E and the part outside E. Since the second part has nonnegative measure, the measure of E is no larger than that of F.

Second comes continuity from below. If E-one is contained in E-two, then E-three, and so on, the measure of their union equals the limit of their measures. To prove this, divide the union into the disjoint increments appearing at each stage and use countable additivity.

Third comes continuity from above when the first set has finite measure. If the sets decrease, the measure of their intersection is the limit of their measures. This follows by applying continuity from below to the complements relative to the first set. The finite-measure assumption permits the needed subtraction.

Notice how all three statements convert set limits into numerical limits. We will want analogous rules for integrals and spectral projections.

### Integrating the simplest functions

Take a nonnegative simple function: it has finitely many values and can be written as a sum of positive constants multiplied by indicators of disjoint measurable sets.

Define its integral by multiplying each value by the measure of the corresponding set and adding. If a simple function equals three on a set of measure two and one on a disjoint set of measure five, its integral is six plus five, namely eleven.

For a general nonnegative measurable function, consider all nonnegative simple functions bounded above by it. Define the integral as the supremum of their integrals.

This definition extends familiar Riemann sums, but it is organized around measurable sets rather than fixed interval partitions. It also handles functions with infinitely many discontinuities and spaces that are not intervals at all.

A measurable real function that can have negative values is split into its positive and negative parts. We integrate them separately, requiring finite total absolute integral when we say the function is integrable. For complex functions, integrate real and imaginary parts.

### Why approximation works

Every nonnegative measurable function can be approximated from below by an increasing sequence of nonnegative simple functions.

Here is the construction idea. For each positive integer n, round function values downward to multiples of one over two to the n, and cap the values at n. This gives a finite-valued measurable approximation. As n grows, the grid becomes finer and the cap becomes larger. With a suitable choice of partitions, the approximations increase pointwise to the original function.

The monotone convergence theorem says that their integrals increase to the integral of the limit function. The direction of approximation matters: every partial integral is below the target integral. Conversely, any simple function below the limit can be captured in the integral estimate to arbitrary precision using the increasing approximation and countable additivity. These two inequalities force equality of the limit and the integral. The principle allows an increasing limit and integration to be interchanged even when the answer is infinite.

The theorem is stronger than a mere computational recipe. It permits interchange of an increasing limit and integration without assuming a uniform bound on the functions.

### Two more convergence principles

Fatou's lemma says that the integral of the pointwise lower limit of nonnegative measurable functions is no larger than the lower limit of their integrals. A convenient proof applies monotone convergence to the increasing sequence obtained by taking, at each stage, the infimum of the functions from that stage onward.

The dominated convergence theorem gives a different kind of limit interchange. Suppose functions converge almost everywhere to f, and their absolute values are all bounded by one common integrable function g. Then their integrals converge to the integral of f.

Why is domination necessary? Consider functions that equal n on an interval of length one over n, and zero elsewhere. Their integrals remain one. For every positive point, the functions eventually vanish. Thus they converge almost everywhere to zero, but the integrals do not converge to zero.

The mass is concentrating in a narrower region as its height rises. There is no single integrable dominating function for this entire sequence. Pointwise convergence alone cannot control integrals.

These convergence theorems justify passing from finite spectral sums and simple symbols to measurable functions of an operator. Each limit needs its own hypothesis: monotonicity for monotone convergence, nonnegativity for Fatou, and one integrable majorant for dominated convergence.

### The L two norm

Define L two to consist of measurable complex functions whose squared absolute values have finite integral, identifying functions equal almost everywhere. The squared norm of f is the integral of squared absolute value.

For two such functions, define their inner product by integrating the complex conjugate of the first times the second. The integral exists by the Cauchy–Schwarz inequality for integrals: the absolute value of the inner product is bounded by the product of the two L two norms.

One way to prove that inequality is to integrate the nonnegative square of f minus a scalar multiple of g. Choose the scalar so the resulting quadratic expression is minimized. Its discriminant cannot be positive in the forbidden direction, giving Cauchy–Schwarz.

The parallelogram identity follows from expanding squared absolute values pointwise and integrating. Thus L two is an inner-product space.

### Why we identify functions almost everywhere

Consider the function that equals one at a single point of the unit interval and zero everywhere else. Under Lebesgue measure, the integral of its squared absolute value is zero. Without identifying almost-everywhere-equal functions, this nonzero function would have zero norm.

After taking equivalence classes, a vector in L two is not a particular pointwise formula. Its values on sets of measure zero are irrelevant. This distinction is especially important when defining a multiplication operator: changing its symbol on a null set produces the same operator on L two.

For the unit interval, the constant function one has norm one. The coordinate function x has norm one over square root of three. Their inner product is the integral of x, which is one half. Therefore the orthogonal projection of x onto the constants is the constant function one half.

We can verify this by taking the inner product of x minus one half with the constant one: the integral is zero.

### Completeness of L two

The most important analytic claim is that every Cauchy sequence in the L two norm converges to a vector of L two.

Here is a proof outline that shows where integration is needed. From a Cauchy sequence, choose a subsequence whose successive L two distances are smaller than one over two to the n. The sum of these distances is finite.

Take the pointwise sum of the absolute values of those successive differences. Each partial sum has L two norm no larger than the sum of the corresponding L two distances, by the triangle inequality. That sum is finite. Fatou's lemma therefore gives a limiting absolute-sum function with finite L two norm, so it is finite almost everywhere. At those points the subsequence is an absolutely convergent series of functions; call its pointwise limit f.

Apply Fatou's lemma again to the squared differences between a fixed subsequence term and later terms. The Cauchy estimates bound the eventual integral of the squared difference from f. As the fixed term moves farther along the subsequence, this bound tends to zero. Thus the subsequence converges to f in L two norm and f belongs to L two. Since the original sequence was Cauchy and has a convergent subsequence, the entire sequence converges to f.

This produces the completeness missing from a space of ordinary continuous functions with only an integral norm. L two is a Hilbert space.

### Infinite orthogonality from disjoint sets

Take pairwise disjoint measurable sets, each of finite positive measure. Divide each indicator by the square root of its measure. The resulting L two vectors have norm one. Their pairwise inner products vanish because the sets do not overlap.

If there are infinitely many such sets, we obtain an infinite orthonormal family. Hence L two cannot be finite-dimensional.

To exhibit infinitely many orthogonal directions in the unit interval, for each positive n choose the interval from one divided by the quantity n plus two, up to one divided by the quantity n plus one. These intervals are adjacent and disjoint apart from endpoints of measure zero. Each has positive finite length. Their normalized indicator functions form an infinite orthonormal family in the square-integrable space.

### Returning to spectral theory

When a projection-valued measure assigns a projection to each Borel set, each vector will induce a scalar measure: the squared norm of its projected component. Integrals against that scalar measure will define norms of functions of the operator.

The essential mental model is now complete. A measure weighs sets. Integration weighs function values using those sets. Identifying functions that differ only on null sets turns the squared integral into a genuine norm. Completeness then lets approximating functions converge without escaping the space. This is the framework in which a multiplication operator can represent a continuous spectrum.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Infinite-dimensional Hilbert examples

**Draft status:** audio-first mathematical lecture. **Prerequisites:** `003000` completeness, `009000–015000` Hilbert operators, `025000–032000` finite spectral theory. **Next:** `073000` sigma-algebras and Borel sets.

---

#### Companion: mathematics and Lean correspondence (display only)

On \(L^2((0,1),dx)\), \((Mf)(x)=xf(x)\) is bounded and self-adjoint. Its eigen-equation \((x-\lambda)f(x)=0\) almost everywhere forces \(f=0\); nevertheless \(\sigma(M)=[0,1]\). The resolvent is multiplication by \((x-\lambda)^{-1}\) outside \([0,1]\), while normalized indicators on shrinking intervals show the failure of a bounded inverse inside it.

On \(\ell^2(\mathbb N)\), the unilateral shift \(U(x_0,x_1,\ldots)=(0,x_0,x_1,\ldots)\) satisfies \(U^*U=I\) but \(UU^*=I-P_{e_0}\).

**Lean bridge (verified source excerpts).**

`ForTauCeti/MeasureTheory/LpInfiniteDimensional.lean` — `not_finiteDimensional_lpTwo_unitIocMeasure` (exact source declaration header):

```lean
theorem not_finiteDimensional_lpTwo_unitIocMeasure :
    ¬ FiniteDimensional 𝕜 (Lp 𝕜 2 unitIocMeasure) := by
```

The repository proves this L-two space is infinite-dimensional by constructing disjoint positive-measure intervals, rather than assuming a function space must be infinite-dimensional.

`ForTauCeti/MeasureTheory/MulLpSpectrum.lean` — `ae_mem_spectrum_mulLp` (exact source declaration header):

```lean
theorem ae_mem_spectrum_mulLp : ∀ᵐ x ∂ρ, g x ∈ spectrum ℂ (mulLp ρ hg hgC) := by
```

For a bounded measurable complex multiplier on a sigma-finite measure space, the symbol takes values in the multiplication operator spectrum almost everywhere. This is part of the spectral analysis of multiplication models; the interval example is derived mathematically in the narrated lecture.

### Weak, strong, and uniform convergence in Hilbert spaces

**Draft status:** audio-first mathematical lecture. **Prerequisites:** Hilbert spaces, orthogonal projections, and bounded operators. **Related:** `072000` infinite-dimensional examples, `082000` spectral cutoffs, `091500` strong resolvent convergence.

---

#### Mathematical companion (display only)

Let \(H=\ell^2(\mathbb N)\) with standard orthonormal basis \(e_n\). The vector sequence \(e_n\rightharpoonup 0\) because \(\langle e_n,y\rangle=y_n\to0\) for every \(y\in H\), whereas \(\|e_n\|=1\).

For \(P_nx=\sum_{k=1}^n\langle x,e_k\rangle e_k\),
\[
\|(I-P_n)x\|^2=\sum_{k>n}|x_k|^2\to0\quad(x\in H),
\qquad \|I-P_n\|_{\mathrm{op}}=1.
\]
Thus \(P_n\to I\) strongly but not in operator norm. For \(T_nx=\langle x,e_1\rangle e_n\), \(\langle T_nx,y\rangle=\langle x,e_1\rangle\langle e_n,y\rangle\to0\), while \(\|T_ne_1\|=1\). This gives weak-operator convergence without strong convergence.

**Implications:** operator norm \(\Rightarrow\) strong \(\Rightarrow\) weak operator; norm convergence of vectors \(\Rightarrow\) weak convergence of vectors. The stated converses fail in infinite dimension. Under \(\|T-I\|<1\), the Neumann series \(T^{-1}=\sum_{j\ge0}(I-T)^j\) converges in operator norm. No such conclusion follows for the strong sequence \(P_n\).

For \(A e_k= k e_k\) with \(D(A)=\{x\in\ell^2:\sum k^2|x_k|^2<\infty\}\), \(P_nD(A)\subset D(A)\), and \(\|P_nx-x\|_A^2=\sum_{k>n}(1+k^2)|x_k|^2\to0\) on \(D(A)\). This is **graph-norm** convergence, which needs a domain-preserving approximation.

No Lean declaration is asserted for these textbook calculations.

### Sigma-algebras and Borel sets

**Draft status:** audio-first mathematical lecture. **Prerequisites:** `072000` infinite-dimensional Hilbert examples; basic sets, limits, and continuity. **Next:** `074000` measures, integration and L2.

---

#### Companion: mathematics and Lean correspondence (display only)

A sigma-algebra \(\Sigma\) on \(X\) satisfies \(X\in\Sigma\), \(E\in\Sigma\Rightarrow E^c\in\Sigma\), and \((E_n)\subset\Sigma\Rightarrow\bigcup_n E_n\in\Sigma\). The Borel sigma-algebra \(\mathcal B(\mathbb R)\) is generated by the open sets. A map \(f:X\to\mathbb R\) is measurable when the inverse image of each Borel set belongs to \(\Sigma\).

For a bounded self-adjoint \(A\), later spectral calculus will associate an orthogonal projection \(E_A(B)\) with a Borel set \(B\). Disjoint unions are represented by **strong**, rather than necessarily norm-convergent, sums of projections.

##### Running spectral-window model

On \(H=L^2([0,1],dt)\), let \((Af)(t)=t f(t)\). For Borel \(B\subseteq\mathbb R\), the spectral projection is
\[
(E_A(B)f)(t)=\mathbf1_{B\cap[0,1]}(t)f(t).
\]
Hence \(E_A(B)E_A(C)=E_A(B\cap C)\), and \(E_A(B^c)=I-E_A(B)\). The assertions are identities in \(L^2\), so changes on null sets do not affect these operators. For instance \(E_A([0,1/2])=E_A([0,1/2))\), whereas a diagonal operator with eigenvalue \(1/2\) can distinguish those two sets. Countable additivity holds in the strong operator topology rather than in operator norm.

**Lean bridge (verified source excerpts).**

`DavisKahan/SpectralTheory/SelfAdjointBorelCalculus.lean` — `measurableSet_realSpectrum_boundedSelfAdjoint` (exact source declaration header):

```lean
theorem measurableSet_realSpectrum_boundedSelfAdjoint
    (A : H →L[ℂ] H) (hA : A.IsSymmetric) :
    MeasurableSet (realSpectrum A) :=
```

The real spectrum is a measurable set, permitting spectrum-restricted measurable symbols.

`DavisKahan/SpectralTheory/SelfAdjointBorelCalculus.lean` — `boundedSelfAdjointBorelCalculusC_indicator` (exact source declaration header):

```lean
theorem boundedSelfAdjointBorelCalculusC_indicator
    (A : H →L[ℂ] H) (hA : A.IsSymmetric)
    (s : Set ℝ) (hs : MeasurableSet s) :
    boundedSelfAdjointBorelCalculusC A hA
      (Set.indicator s fun _ => (1 : ℂ))
      (measurable_const.indicator hs)
      (indicator_one_bdd s) =
      boundedSelfAdjointSpectralProjection A hA s hs := by
```

The theorem requires `MeasurableSet s` and identifies the Borel indicator calculus with the self-adjoint spectral projection.

### Measures, integration and L2

**Draft status:** audio-first mathematical lecture. **Prerequisites:** `003000` completeness; `009000–010000` inner products and Hilbert spaces; `072000–073000` function-space examples and measurable sets. **Next:** `075000` continuous functional calculus.

---

#### Companion: mathematics and Lean correspondence (display only)

For a measure \(\mu\) on \((X,\Sigma)\), \(L^2(\mu)\) consists of equivalence classes of measurable functions with \(\int |f|^2\,d\mu<\infty\). The inner product is \(\langle f,g\rangle=\int\overline f g\,d\mu\). Disjoint, measurable sets \(E_n\) with \(0<\mu(E_n)<\infty\) yield orthonormal normalized indicators \(1_{E_n}/\sqrt{\mu(E_n)}\), proving infinite dimensionality.

The monotone convergence, Fatou, and dominated convergence theorems are mathematical background supplied by Mathlib's measure-theory infrastructure; the cited DKPS/TauCeti modules use those foundations rather than re-proving their general statements.

##### A complete concrete example

For Lebesgue measure \(m\) on \([0,1]\), the vectors \(u(t)=1\) and \(v(t)=t\) satisfy
\[
\|u\|_2=1,\qquad \|v\|_2^2=\int_0^1t^2dt=\frac13,
\qquad \langle u,v\rangle=\int_0^1t\,dt=\frac12.
\]
Thus the orthogonal projection of \(v\) onto \(\operatorname{span}\{u\}\) is \(\frac12u\). For completeness, choose a Cauchy subsequence \((f_{n_k})\) with \(\|f_{n_{k+1}}-f_{n_k}\|_2\le2^{-k}\); the sum of absolute successive differences belongs to \(L^2\) by Minkowski and Fatou. Its finiteness a.e. yields a pointwise convergent subsequence, and another Fatou estimate gives convergence in \(L^2\).

**Lean bridge (verified source excerpts).**

`ForTauCeti/MeasureTheory/LpInfiniteDimensional.lean` — `unitIocMeasure_Ioc` (exact source declaration header):

```lean
theorem unitIocMeasure_Ioc {a b : ℝ} (ha : 0 ≤ a) (hb : b ≤ 1) :
    unitIocMeasure (Set.Ioc a b) = ENNReal.ofReal (b - a) := by
```

The interval measure computes the ordinary length for subintervals of the unit interval.

`ForTauCeti/MeasureTheory/LpInfiniteDimensional.lean` — `not_finiteDimensional_lpTwo_of_pairwise_disjoint` (exact source declaration header):

```lean
theorem not_finiteDimensional_lpTwo_of_pairwise_disjoint {α : Type*} [MeasurableSpace α]
    {mu : Measure α} (s : ℕ → Set α) (hmeas : ∀ n, MeasurableSet (s n))
    (hfin : ∀ n, mu (s n) ≠ ∞) (hzero : ∀ n, mu (s n) ≠ 0)
    (hdisj : ∀ i j : ℕ, i ≠ j → Disjoint (s i) (s j)) :
    ¬ FiniteDimensional 𝕜 (Lp 𝕜 2 mu) := by
```

The stronger result assumes measurable, finite-positive-mass, pairwise-disjoint sets and concludes that their L-two space is not finite dimensional.
