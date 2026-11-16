# Ideal membership, trace classes, and modulus invariance

<!-- BEGIN SPOKEN LECTURE -->

# Ideal membership, trace classes, and modulus invariance

## Symmetric operator ideals and membership

Let's begin with an infinite diagonal operator. It acts on square-summable sequences, multiplying coordinate number n by one over n.

Its largest amplification is one. Its coefficients tend to zero, so it is compact. The sum of the squares of its coefficients is finite. But the sum of the coefficients themselves is infinite.

Here is the question. Is this operator small or large?

The answer depends on what we are measuring. In operator norm, its size is one. In Hilbert-Schmidt norm, its size is finite. In trace norm, it does not even have a finite value.

That is why infinite-dimensional analysis needs operator ideals. An ideal records which operators satisfy a specified kind of summability or approximation condition, and a norm records their size inside that class.

### Separate membership from measurement

Imagine an ordinary number sequence. One sequence might have a finite sum of absolute values. Another might have a finite sum of squares but an infinite sum of absolute values. Both can be bounded sequences, but they belong to different summability classes.

Exactly the same distinction occurs for sequences of singular values of operators.

In finite dimensions, any fixed list of singular values has finite sum and finite sum of squares. Every matrix is automatically trace class and Hilbert-Schmidt. There can be large quantitative differences between norms, but no membership obstruction.

In an infinite Hilbert space, there may be infinitely many singular values. Their ordinary sum can diverge even when their squared sum converges. A bounded operator may fail both conditions.

So when someone states an inequality in trace norm, we have two questions. First, does the operator belong to the trace class? Second, assuming it does, how large is the trace norm?

An operator ideal is built to answer both questions coherently.

### What makes a family of operators an ideal?

Let E and F be Hilbert spaces. We consider bounded linear maps from E to F. They need not be square operators on the same space; rectangular maps are essential when we study subspaces and coordinate embeddings.

An operator ideal selects admissible bounded maps for every compatible pair of Hilbert spaces. The admissible maps are closed under addition and multiplication by scalars.

The defining stability condition is this: start with an admissible operator T. Put any bounded map B before it and any bounded map A after it, provided all the source and target spaces match. The combined operator A T B must remain admissible.

Think about why this makes sense. If T has only finitely many independent output directions, bounded transformations cannot create infinitely many new ones. If T has square-summable singular values, bounded transformations can amplify them by fixed factors, but cannot turn a finite square sum into an infinite one.

This is called the two-sided ideal property.

The ideal norm follows the same pattern. The size of A T B in the ideal norm is bounded by the ordinary operator norm of A, times the ideal norm of T, times the ordinary operator norm of B.

This estimate is central when an operator is compressed to a subspace or moved through an isometric coordinate representation.

### Three concrete examples

The first ideal is the compact operators. A compact operator is one that can be approximated arbitrarily well in operator norm by finite-rank operators. For this ideal, the ordinary operator norm is a natural ideal norm.

The second example is the Hilbert-Schmidt class. For a compact operator, square every singular value, add the results, and take the square root. If that is finite, the operator is Hilbert-Schmidt.

The third example is the trace class. Add the singular values themselves. If their sum is finite, the operator is trace class. That sum is the trace norm, sometimes called the nuclear norm.

In infinite dimensions, trace class is contained in Hilbert-Schmidt, and Hilbert-Schmidt is contained in compact operators.

Let's check this using diagonal examples rather than memorizing the containment diagram.

Our operator with coefficients one over n has squared coefficients one over n squared. Their sum is finite, so it belongs to the Hilbert-Schmidt class. But the harmonic series diverges, so it is not trace class.

Now choose coefficients one over the square root of n. They tend to zero, so the diagonal operator is compact. But their squares are one over n, and that series diverges. So this operator is not Hilbert-Schmidt.

Finally, the identity on infinite-dimensional ell two is bounded but not compact at all. Its singular-size sequence, understood through approximation numbers, remains equal to one forever.

These examples tell us that the three classes are genuinely different, even though every finite matrix belongs to all three.

### Why changing coordinates does not change the size

Suppose we rotate the source and output coordinates by unitary operators. These preserve lengths and inner products. They can change the matrix entries of T, but they preserve its singular values.

A symmetric operator ideal is designed so that the associated gauge is unchanged by such unitary transformations. The choice of orthonormal coordinates should not change whether an operator belongs, or how large it is in that ideal.

The adjoint behaves similarly. T and its adjoint have the same positive nonzero singular values, counted with multiplicity. Hence the familiar symmetric ideals give them equal norms and corresponding membership.

When the source and target Hilbert spaces are different, one may not be able to extend every geometric correspondence to a unitary between the full spaces. This is why ideal theory also works with rectangular maps, partial isometries, and the positive modulus of an operator.

The invariance is about the singular action, not about the superficial arrangement of matrix entries.

### An extended gauge records nonmembership

There is a useful mathematical convenience. Instead of defining the trace norm only for trace-class operators, we can first assign an extended value to every bounded operator.

If the singular values have finite sum, the extended trace gauge is that sum. If the sum diverges, the extended gauge is infinity.

The same design works for Hilbert-Schmidt energy and more general symmetric ideal gauges. A finite value indicates membership in the associated ideal. An infinite value indicates nonmembership.

Why bother doing that? It lets us write certain inequalities uniformly without splitting them into separate cases at every line. But we must remember that infinity is not an ordinary real number.

Suppose we want a perturbation bound in trace norm. The proper conclusion contains both statements: the perturbed quantity is trace class, and its finite trace norm satisfies the bound. We cannot skip the membership claim and treat an infinite extended value like a finite norm.

### Operator norm convergence is too weak for some ideals

Here is a revealing sequence of finite-rank operators. For each N, make a diagonal operator whose first N entries are one over N and whose later entries are zero.

Its ordinary operator norm is one over N. That tends to zero. So the operators converge to zero in operator norm.

But each has exactly N nonzero singular values, all equal to one over N. Their trace norm is N times one over N, which equals one.

The sequence does not converge to zero in trace norm.

This is the difference between controlling the worst individual stretching direction and controlling the sum over all directions. Even a huge collection of tiny stretches can have substantial total size.

The ideal norm is generally stronger than the ordinary operator norm. A sequence converging in trace norm also converges in operator norm, but the converse is false.

When we approximate an operator using finite spectral cutoffs, we have to specify which of these two kinds of error our theorem actually controls.

### Where the composition bound comes from

We can derive the ideal inequality for Schatten norms using approximation numbers.

Start with an operator T and a low-rank approximation R. If we compose both with bounded maps A and B, the approximation A R B has rank no larger than R. The error between A T B and A R B is at most the product of the operator norms of A and B and the original approximation error.

Taking the best error at each rank gives an inequality for every approximation number. If we then raise these nonnegative numbers to a power p at least one, sum them, and take the p-th root, we get the Schatten p composition bound.

For p equal to one, this is the trace norm. For p equal to two, it is the Hilbert-Schmidt norm.

An orthogonal projection has operator norm at most one. Consequently, compressing a Schatten-class operator with orthogonal projections cannot increase its Schatten norm.

This is particularly useful when comparing a full operator with one of its spectral blocks.

### Completeness and what it does not guarantee

The standard Schatten ideals are complete under their ideal norms. Their finite-rank operators are dense for finite p, because we can discard singular values after N terms and make the remaining p-power sum as small as desired.

The compact operators are also complete in the operator norm, and finite-rank operators are dense there as well.

But finite-rank density is not a consequence of every possible symmetric-ideal axiom. Some larger ideals have norms for which the finite-rank closure is a proper subspace. So when a proof uses finite-rank approximation in a particular ideal norm, that property must be available for the chosen ideal.

### One operator, three answers

Return to the diagonal operator with coefficients one over n. In operator norm it has size one. In Hilbert-Schmidt norm it has a finite size determined by the convergent sum of one over n squared. In trace norm it has no finite size at all.

We did not change the operator. We changed the kind of cumulative behavior we wanted to measure.

That is the role of a symmetric operator ideal: it supplies a coordinate-invariant notion of operator size, a class of operators on which that size is finite, and stability under bounded composition. In infinite-dimensional perturbation theory, those three ingredients are what make a norm estimate meaningful.

## Hilbert–Schmidt and trace-class operators

Imagine a two-by-two diagonal matrix. It stretches the first coordinate by three and the second by one.

What is the size of this matrix? If we ask for the maximum stretch of a unit vector, the answer is three. If we add the squared magnitudes of every entry and take the square root, the answer is square root of ten. If we add its two singular values, the answer is four.

All three answers are correct. They measure different things.

The first is the operator norm. The second is the Frobenius norm. The third is the trace norm.

In infinite dimensions, the difference becomes more than a numerical choice. The Frobenius-style calculation may converge while the trace-norm calculation diverges. That is why we distinguish Hilbert-Schmidt operators from trace-class operators.

### Extend the Frobenius calculation

Let's start with ell two, the Hilbert space of square-summable sequences. An operator T acts on each standard basis vector, one at a time. We can measure the length of every resulting output vector.

Square those output lengths and add them over all basis vectors. This sum might be finite or infinite. When it is finite, we say T is Hilbert-Schmidt. The square root of the sum is its Hilbert-Schmidt norm.

Why is this the infinite-dimensional Frobenius norm? In a finite matrix, the image of a standard basis vector is one column of the matrix. The squared length of that column is the sum of the squared magnitudes of its entries. Adding over all columns produces exactly the sum of squared magnitudes of every matrix entry.

So the Hilbert-Schmidt construction is simply the same calculation allowed to run over infinitely many orthonormal input directions.

For a diagonal operator with coefficients one over n, applying T to basis vector n produces a vector of length one over n. The squared lengths add to the convergent series one plus one quarter plus one ninth, and so forth. This operator is Hilbert-Schmidt.

Change the coefficients to one over the square root of n. They still tend to zero, so the diagonal operator is compact. But their squared lengths add to the harmonic series, which diverges. So this operator is not Hilbert-Schmidt.

We are measuring accumulated squared output size, not merely the largest output size.

### A serious question: which basis?

Our definition appeared to depend on the chosen orthonormal basis. Suppose we rotate the basis. Do we get a different Hilbert-Schmidt norm?

We need to prove that we do not.

Take one orthonormal basis in the input space, and another orthonormal basis in the output space. We will temporarily call their vectors e and f.

Apply T to one input basis vector e. Parseval's identity says the squared length of T e equals the sum of the squared magnitudes of its inner products with all the output basis vectors f.

Now add that identity over every input basis vector. We have a double sum: one index for input directions and one for output directions.

Every summand is nonnegative. That lets us exchange the order of summation without relying on conditional cancellation.

Next use the adjoint. The inner product of T e with f has the same absolute value as the inner product of e with T adjoint applied to f. This simply transfers T from one side of the inner product to the other.

For each fixed output basis vector f, Parseval's identity in the input space now adds the squared inner products over e. The result is the squared length of T adjoint f.

We have proved that the sum of squared output lengths of T in the input basis equals the corresponding sum for T adjoint in the output basis.

Now repeat the calculation with a different input basis but the same output basis. Both versions give the same sum for T adjoint. Therefore the original sum is independent of the input basis.

We also learned that T and its adjoint have equal Hilbert-Schmidt norms.

For a nonseparable Hilbert space, orthonormal bases may have arbitrary index sets. The same reasoning uses suprema of finite subsums in place of a single numbered series.

### Connect the energy to singular values

For a compact operator T, its singular values measure the stretches in its mutually orthogonal singular directions. When we choose those directions as part of an orthonormal basis, T sends the n-th singular direction to a vector of length equal to the n-th singular value.

Because the Hilbert-Schmidt energy is basis independent, we may compute it using these convenient directions. We get the sum of the squares of all singular values.

So there are two equivalent descriptions. We can square the output lengths on any orthonormal input basis, or we can square the singular values and sum them. They give the same Hilbert-Schmidt energy.

This equivalence helps us move between concrete matrix entries and the intrinsic spectral description of an operator.

### The Hilbert-Schmidt operators form a Hilbert space

There is a further payoff. Suppose S and T are both Hilbert-Schmidt and have the same input and output spaces.

Apply each operator to an orthonormal input basis. Take the inner product of S e with T e for each basis vector e, and add those inner products.

The ordinary Cauchy-Schwarz inequality for series tells us that the absolute sum is bounded by the product of the two Hilbert-Schmidt norms. Therefore this pairing is well-defined.

It behaves like an inner product on the space of operators. Pairing T with itself gives its squared Hilbert-Schmidt norm. And the class is complete in that norm.

That means Hilbert-Schmidt operators form a Hilbert space in their own right. We can use familiar geometric ideas, such as orthogonality and projections, but now the points of the space are operators rather than vectors.

In finite dimensions this pairing is the Frobenius inner product. In infinite dimensions it is the corresponding trace pairing, once we establish why the trace exists.

### Why trace class is stricter

For a compact operator, take its singular values and add them without squaring. If the sum is finite, the operator is trace class. That sum is its trace norm.

Our diagonal operator with coefficients one over n is the perfect separator. It has a finite sum of squared singular values, but an infinite sum of singular values. So it is Hilbert-Schmidt and not trace class.

Any trace-class operator is Hilbert-Schmidt. Here is the reason. A summable sequence of nonnegative singular values is bounded, and multiplying each value by itself cannot destroy summability when all the values are uniformly bounded. More concretely, the sum of squares is at most the largest singular value times the sum of singular values.

Thus trace class sits inside Hilbert-Schmidt. The containment is strict in infinite dimensions.

In finite dimensions every matrix belongs to both classes. It is the infinite number of directions that creates the membership question.

### The trace itself

For a positive trace-class operator on a single Hilbert space, the trace is the sum of its eigenvalues, counted with multiplicity. Because the operator is positive, the eigenvalues are nonnegative, and this sum equals its trace norm.

For a general trace-class operator on one Hilbert space, the trace can be computed by choosing any orthonormal basis and summing the diagonal inner products of each basis vector with its image under the operator.

The trace-class condition ensures that this series converges absolutely and that the answer is independent of the basis. The absolute value of the trace is at most the trace norm.

The distinction between trace and trace norm is important. The trace can involve cancellations, and it may even be zero for a nonzero operator. The trace norm adds the nonnegative singular values and never relies on cancellation.

Also, the trace belongs naturally to operators from a Hilbert space back to itself. The trace norm still makes sense for rectangular operators between different Hilbert spaces.

### Why multiplying two square-summable operators works

Suppose S sends vectors from E to F, and T sends vectors from F back to E. Both are Hilbert-Schmidt.

Their composition T after S maps E back to itself. A powerful theorem says that this product is trace class, with trace norm at most the Hilbert-Schmidt norm of T times the Hilbert-Schmidt norm of S.

Let's see the mechanism in a diagonal example. Suppose both factors multiply coordinate number n by one over n. Each factor is Hilbert-Schmidt, because the sum of one over n squared converges.

Their product multiplies coordinate n by one over n squared. Now the sum of the singular values of the product converges. So the product is trace class.

The scalar calculation suggests Cauchy-Schwarz: multiplying two square-summable sequences produces a summable sequence.

For general operators we cannot assume the factors share singular vectors. The operator version is a Schatten Holder inequality. One rigorous route starts with finite-rank approximations, proves the matrix inequality, and then passes to the limit in the Hilbert-Schmidt and trace norms. It yields exactly the same product bound without requiring simultaneous diagonalization.

The operator inner product from a moment ago can now be identified with the trace of a product involving the adjoint. Its existence is explained by this theorem.

### Cyclicity needs a finite trace

In finite-dimensional linear algebra, we know the trace of B T equals the trace of T B. In infinite dimensions, we must ensure both traces are defined.

If T is trace class and B is bounded on the same Hilbert space, then both products are trace class, and the traces are equal.

The proof can begin with finite-rank T, where ordinary matrix cyclicity applies. Approximate a general trace-class T by finite-rank operators in trace norm. The trace is continuous in that norm, so the identity passes to the limit.

Without a trace-class hypothesis, there may be no trace to cycle. A bounded operator can have infinitely many diagonal contributions whose sum diverges.

### Return to finite-dimensional approximations

For a Hilbert-Schmidt operator, retain its first N singular directions. The squared Hilbert-Schmidt error is the sum of the squares of all omitted singular values. Since the full square sum converges, that tail tends to zero.

For a trace-class operator, the trace-norm error is the ordinary sum of the omitted singular values. It also tends to zero because the full sum is finite.

These two facts justify using finite-rank operators to prove many infinite-dimensional statements, provided the approximation is taken in the correct norm.

The lesson is that one operator can have several valid notions of size, each collecting its singular directions differently. The operator norm records the largest stretch. Hilbert-Schmidt records accumulated squared stretch. Trace norm records accumulated singular stretch. Only the last two impose the corresponding infinite-dimensional summability conditions.

## Smoothed singular-value energies

Suppose we want to encourage a matrix to have few significant singular values. One familiar penalty is the nuclear norm: add all the singular values. Large singular values are expensive, and setting a singular value to zero removes its contribution entirely.

There is an optimization difficulty. A singular value behaves rather like an absolute value, and the nuclear norm can fail to be differentiable when singular values reach zero. In numerical optimization, it can be useful to replace this sharp cost with a smooth one.

But there is a mathematical surprise. In infinite dimensions, smoothing the cost changes which operators have finite total energy. To understand why, we need to look closely at one scalar function near zero.

### Start with one nonnegative number

Let s be a singular value, so s is nonnegative. Choose a positive smoothing scale, which we'll call tau.

Define the smoothed penalty by taking the square root of tau squared plus s squared, and then subtracting tau.

This is sometimes called a Charbonnier-style penalty. It equals zero when s is zero. It is smooth as a function of s because tau is strictly positive.

Let's set tau equal to one for a numerical picture.

If s is one, the cost is square root of two minus one, about zero point four one four.

If s is one tenth, the cost is square root of one point zero one minus one, approximately zero point zero zero five. That is much smaller than one tenth.

If s is ten, the cost is square root of one hundred and one minus one, a little more than nine. For large s, it behaves approximately like s minus tau.

So the smoothed penalty has two regimes. It is roughly quadratic for singular values much smaller than tau. It is roughly linear for singular values much larger than tau.

That change near zero is the entire story behind its infinite-dimensional domain.

### Reveal the quadratic behavior exactly

There is a useful algebraic trick. Take the square root of tau squared plus s squared minus tau, and multiply numerator and denominator by the matching sum, the square root plus tau.

In the numerator, the difference of squares simplifies to s squared. In the denominator, we retain the square root of tau squared plus s squared, plus tau.

So the penalty is exactly s squared divided by that denominator.

When s is very small, the square root in the denominator is close to tau. The denominator is therefore close to twice tau, and the penalty is approximately s squared divided by twice tau.

The derivative tells the same story. Its first derivative is s divided by the square root of tau squared plus s squared, which becomes zero at s equal to zero. The second derivative is positive for tau greater than zero. The penalty is smooth and convex.

For a scalar input, the calculation is straightforward. But summing these penalties over infinitely many singular values requires more thought.

### From one value to a whole operator

Let T be a bounded compact operator on a Hilbert space, or between two Hilbert spaces. It has singular values listed in descending order, possibly infinitely many.

Define its smoothed spectral energy by applying our scalar penalty to every singular value and adding the results.

The total could be finite or infinite. To decide which, remember that a bounded operator has a finite largest singular value. Call that upper bound M.

Every singular value s lies between zero and M. In our rationalized expression, the denominator is at least twice tau, and it is at most the square root of tau squared plus M squared, plus tau.

Therefore the penalty lies between two positive constant multiples of s squared. One constant comes from twice tau, and the other from the upper bound M.

Now sum those inequalities across all singular values.

We find that the total smoothed energy is finite exactly when the sum of squared singular values is finite. And that is precisely the Hilbert-Schmidt condition.

This is the crucial conclusion. For every fixed positive smoothing scale, this smooth nuclear-like penalty has the Hilbert-Schmidt class as its finite-energy domain.

It may look approximately like a sum of singular values for large s, but there can only be finitely many singular values above a fixed positive threshold for a compact operator. It is the infinite tail of small singular values that determines whether the total converges.

The near-zero quadratic behavior wins.

### Two diagonal operators clarify the boundary

First take an operator on ell two with diagonal entries one over n. Its singular values are one, one half, one third, and so on.

The sum of the singular values diverges, because it is the harmonic series. So this operator is not trace class.

However, their squares have finite sum. For every fixed positive tau, the smoothed penalty is comparable to the square of each small singular value, so the total smoothed energy is finite.

Now change the diagonal coefficients to one over the square root of n. They still tend to zero, so the operator is compact. But their squares add to the harmonic series and diverge. Consequently, even the smoothed energy is infinite for every fixed positive tau.

These two examples separate three different properties: compactness, finite Hilbert-Schmidt energy, and finite trace norm.

Our smooth penalty detects the second one.

### What happens when smoothing disappears?

Return to the operator with coefficients one over n. Keep the operator fixed, and make tau smaller and smaller.

For every fixed positive singular value s, the penalty approaches s as tau approaches zero. The smoothing disappears, and we recover the sharp absolute-value-like penalty.

There is an additional useful fact. As tau decreases, the penalty for each fixed s increases. So the total energies form an increasing family as the smoothing parameter moves down toward zero.

Because every summand is nonnegative, monotone convergence lets us pass the limit through the infinite sum. The limiting total is the sum of the singular values, which is infinite for this operator.

Thus every positive smoothing scale gives a finite answer, yet the energy tends to infinity as the smoothing scale goes to zero.

That is a real change of domain at the limiting parameter. It is a warning against treating an infinite sum as though it were a finite list of singular values.

### Why the energy is not a norm

A norm must scale linearly with the absolute value of a scalar. Double an operator, and its norm must double.

Our smoothed energy does not obey that rule. For a very small singular value, the cost is approximately proportional to its square. Doubling that singular value multiplies its cost by about four, not two.

For a very large singular value, the cost behaves more nearly linearly. So the scaling behavior depends on the magnitude relative to tau.

The smoothed energy is a convex spectral penalty, not a norm, even though the class of operators on which it is finite is a familiar normed ideal.

That distinction is useful. Optimization methods may use the penalty because it has a smooth gradient, while functional analysis uses an ideal norm to describe the underlying space and convergence.

### The finite-dimensional gradient

For a finite rectangular matrix T, we can express the smoothed energy as the trace of the positive square root of T adjoint T plus tau squared times identity, minus tau times the number of input coordinates.

The subtraction is essential. Every zero singular value contributes zero to the desired cost. If we did not subtract tau for each input coordinate, extra zero directions would add an irrelevant constant in finite dimensions and an infinite offset in infinite dimensions.

The gradient of the finite-dimensional energy, with respect to the Frobenius inner product, has a clean expression. Multiply T on the right by the inverse square root of T adjoint T plus tau squared identity.

Why is that reasonable? In a singular-value decomposition, the gradient acts along the same left and right singular directions. It replaces each singular value s by the derivative of the scalar penalty: s divided by the square root of tau squared plus s squared.

Because tau is positive, the denominator never vanishes, even when s is zero. This is the computational advantage of smoothing.

In an infinite-dimensional setting, differentiability must be considered on a specified operator space, with a specified norm or topology. The finite matrix formula alone does not justify taking traces or gradients of arbitrary bounded operators.

### The underlying principle

A scalar penalty can be smooth and finite for every individual input, while its sum over infinitely many singular values is infinite.

For this particular square-root penalty, rationalizing the expression showed exactly why: near zero, it is comparable to the square of the singular value. That determines a Hilbert-Schmidt finite-energy domain. Sending the smoothing scale to zero recovers the trace-norm sum, and the domain can become smaller.

The reliable method is to examine the penalty near zero, compare it with a familiar power, and only then sum over the singular-value sequence. That tells us what an infinite-dimensional regularizer is actually measuring.

## Modulus, polar factors, and ideal invariance

Consider a map on the plane that takes the vector pointing straight up, stretches it by three, and sends it to the right. It sends every horizontal vector to zero.

There are two different effects in that description. The map decides how much of an input survives and how long its output becomes. It also decides which direction that output points.

Can we separate those two effects?

That question leads to the modulus of an operator and its polar decomposition. It also gives us a way to show that changing output directions does not change singular-value norms, including the norms used for Hilbert–Schmidt and trace-class operators.

We'll do the calculation in the plane first. Then we'll see why the same reasoning works for rectangular operators and infinite-dimensional Hilbert spaces.

### The simple map

Let T take an input with coordinates x and y and return a vector with first coordinate three y and second coordinate zero.

The input pointing right has coordinates one and zero. T sends it to zero. The input pointing up has coordinates zero and one. T sends it to a vector of length three pointing right.

The matrix of T has a three in its upper-right position and zeros everywhere else.

Now ask what the length of T applied to an arbitrary input is. The answer is three times the absolute value of y. The x coordinate contributes nothing.

Suppose we want another operator that preserves exactly this length information, but doesn't redirect the surviving vertical coordinate into the horizontal direction. A natural choice is the diagonal operator that kills the first coordinate and multiplies the second by three.

This second operator sends x,y to zero,three y. On every input, its output has exactly the same length as the output of T.

That second operator is the modulus of T. The modulus records the stretching without the directional rearrangement.

### Why the modulus has that definition

For a general bounded operator T from a Hilbert space E to a Hilbert space F, the source and target may be different. We begin with its adjoint, which runs from F back to E.

Compose T with its adjoint in the order T adjoint followed by T. The resulting operator acts on the source E.

Here's the key identity. Pair T adjoint T applied to x with x. The answer is the squared length of T x.

This tells us that T adjoint T is positive. It can therefore have a unique positive square root. We call that square root the modulus, or absolute T.

In our plane example, T adjoint T is diagonal with entries zero and nine. Its positive square root is diagonal with entries zero and three, just as we guessed.

The definition is designed to ensure that T and absolute T give outputs of equal length for every input. It also ensures that they lose exactly the same input directions: their kernels agree.

We have separated out the length data. What restores the direction?

### Restore the direction with a partial isometry

In the plane example, the modulus sends the upward unit vector to a vertical vector of length three. To recover T, we need to turn that surviving vertical direction into a horizontal direction, without changing its length.

Define U to send the upward unit vector to the rightward unit vector. Define U to send the rightward unit vector to zero.

Then applying the modulus first and U second gives exactly T. The modulus supplies the factor three; U chooses the direction.

Notice that U is not a rotation of the whole plane. It kills one direction. It only preserves lengths on the part of the source that survives the modulus.

That is what a partial isometry does. It acts isometrically on an initial subspace and vanishes on the orthogonal complement of that subspace. In particular, its operator norm is at most one.

Now we can build U for any bounded T, even without a matrix or a basis of singular vectors.

First consider a vector that can be written as absolute T applied to some x. Send it to T x. This prescription is well-defined: if two choices of x give the same output under the modulus, their difference lies in the common kernel and gives the same output under T.

And it preserves lengths, because T x and absolute T x have equal lengths.

Extend that isometry to the closure of the range of the modulus. On its orthogonal complement, which is the kernel of T, set it to zero.

That gives the canonical polar factor U. We obtain the polar decomposition: T is U followed by the modulus.

There's an equally useful reverse identity. The modulus is U adjoint followed by T. In the example, T sends the vertical direction to the horizontal one, and U adjoint turns that horizontal output back to the vertical direction. The stretch of three is unchanged.

These two factorizations are the heart of the ideal-norm argument.

### Why every symmetric ideal gauge is unchanged

Let's first recall what an operator ideal gives us. Its gauge is a way to measure an operator's size, defined on the appropriate family of operators. A symmetric ideal family has the property that composing with bounded operators on the left or right cannot enlarge the gauge by more than the product of their operator norms.

Think about multiplying a matrix by a rotation. Its singular values stay the same. The ideal inequality extends the useful part of that observation beyond invertible rotations, to contractions and partial isometries.

Since U is a contraction and T equals U times absolute T, the gauge of T is no greater than the gauge of absolute T.

Now run the calculation backward. Absolute T equals U adjoint times T. U adjoint is also a contraction, so the gauge of absolute T is no greater than the gauge of T.

Each is at most the other. Therefore they are equal.

We have also proved something about membership. Some ideals include only operators whose gauge is finite. The same comparison works with extended gauges that may be infinite. So T belongs to the ideal if and only if its modulus belongs to the ideal.

Let's check the conclusion on our little matrix. The only nonzero singular value of T is three, and the modulus has the same singular values, three and zero. The operator norm is three. The Hilbert–Schmidt norm is three. The trace norm is also three.

The fact that all three norms agree in this example is incidental. The fact that each norm of T equals the corresponding norm of its modulus is the general result.

### Why a full unitary is unnecessary

Our map loses the horizontal direction. We cannot demand that U preserve lengths on every direction in the source, because the full operator T is allowed to have a kernel.

In higher or infinite dimensions, the source and target might not even have the same dimension. A full unitary between them might not exist.

But nothing in our proof needed one. We used a partial isometry from the source to the target and its adjoint in the reverse direction. Both have norm at most one, and their compositions are valid between the relevant Hilbert spaces.

The construction also explains why the canonical factor is specified to be zero on the kernel. If we only required a factorization, other choices could be possible on directions that the modulus already kills. Setting U to zero there removes the ambiguity.

As another check, imagine a map from the plane into three-dimensional space. It preserves only the upward input coordinate, stretches it, and sends it along some chosen axis in three-dimensional space. The modulus still acts on the source plane. U carries the surviving direction into the target. The two ideal-gauge inequalities are identical to the ones we just used.

### Infinite dimensions and what the result buys us

A bounded operator on a Hilbert space need not have a finite singular-vector basis. Its range need not be closed. That's why the general construction used the closure of the modulus range instead of assuming that every output is reached by a finite set of eigenvectors.

The modulus is positive, so it can be studied with the spectral theorem. Many inequalities are easier to understand for positive operators than for arbitrary maps between different spaces.

Polar decomposition lets us prove an estimate for the positive modulus, then transfer it back to the original operator without changing its symmetric ideal gauge.

In particular, compactness, Hilbert–Schmidt membership, and trace-class membership agree between T and its modulus.

The central calculation is now easy to remember. T factors through a partial isometry in one direction. Its modulus factors through the adjoint partial isometry in the other. Both factors are contractions. Those two inequalities force equality of ideal size, even for rectangular maps with kernels.

## Ideal estimates for compressions and block sums

Take a two-by-two matrix. Imagine that its first row is three and four, and its second row is one and two.

Suppose we're interested only in what happens when an input points horizontally, and only in the horizontal part of the output. Under those restrictions, the matrix behaves like multiplication by three.

We have thrown away most of the original operation. A natural question is whether this remaining piece could somehow be larger, in a singular-value norm, than the operator it came from.

The answer is no. Compressing an operator between orthogonal subspaces cannot increase a symmetric ideal gauge.

But there's a second question that looks similar and has a different answer. What if we keep several pieces, put them on the diagonal, or assemble independent operators into one big block matrix? To reason correctly about these operations, we'll distinguish three things: selecting a block, averaging away off-diagonal blocks, and forming a direct sum.

### Selecting one block

Return to our matrix with rows three, four and one, two.

Let P project an input onto the horizontal axis. So P keeps its first coordinate and discards its second. Let Q do the same thing to the output.

The composed map Q T P has just one nonzero entry: three in the upper-left position. This is the selected source-to-target block.

Why can't this compression increase an ideal gauge?

Because an orthogonal projection never lengthens a vector. Its operator norm is at most one. An operator ideal is stable under composition by bounded operators: the gauge of A T B is at most the norm of A times the gauge of T times the norm of B.

With A equal to Q and B equal to P, both outside factors have norm at most one. So the compressed gauge is at most the original gauge.

This argument works even if the source and target have different dimensions. And it does more than compare numerical values. If T belongs to a proper operator ideal, the compressed map belongs too.

For example, a trace-class map stays trace class after compression. The same is true for Hilbert–Schmidt operators.

### Four pieces, but no automatic addition rule

Now keep both the horizontal and vertical parts of the source and target. Our matrix has four blocks: three in the upper-left, four in the upper-right, one in the lower-left, and two in the lower-right.

Each individual block is a compression. Each has gauge at most the gauge of the full matrix.

Can we add all four of their gauges and get the gauge of T? Not in general.

For instance, the trace norm of a rank-one matrix with all four entries equal to one is two. But each of its four single-entry blocks has trace norm one. Adding the block trace norms gives four, not two.

Blockwise estimates remain useful, but they don't turn the gauge into a sum over matrix entries.

Let's try a different operation. Keep the two diagonal blocks and discard both off-diagonal blocks. For our running example, the result is the diagonal matrix with entries three and two.

We would like a sharp estimate saying that this diagonal part has gauge no larger than the original matrix. Bounding the two diagonal entries separately and adding would waste a factor. There is a cleaner argument.

### Pinching by reflection and averaging

Imagine reflecting the horizontal and vertical coordinates with opposite signs: keep the horizontal direction as it is and reverse the vertical one.

Apply this reflection to the input side and the output side of our matrix. The diagonal entries stay three and two. The off-diagonal entries change sign, from four and one to negative four and negative one.

Now average the original matrix and this reflected matrix. The off-diagonal entries cancel, and the diagonal entries survive. The average is exactly the diagonal matrix with three and two.

Why does this give a norm estimate? Both reflections are unitary: they preserve all vector lengths. A symmetric ideal gauge is invariant under multiplying by unitaries. So the reflected matrix has exactly the same gauge as the original.

The triangle inequality then tells us that the gauge of their average is at most the average of their gauges. That's just the original gauge.

We've proved the constant-one pinching inequality.

There is a useful difference between the two proofs we've used. A single block is controlled by contractive composition. The sum of the diagonal blocks is controlled by symmetry and averaging. Those are different mechanisms, and recognizing which one applies prevents unnecessary constants.

### Put independent blocks next to each other

Now consider a new construction. Take an operator A with singular values five and one, and an operator B with singular values four and two.

Build a bigger operator that applies A to one input space and B to an orthogonal input space, without mixing the two. This is called their orthogonal direct sum.

Its singular values are the values from both blocks merged into one descending list: five, four, two, one.

Here is why. When we take the adjoint of the direct sum and multiply, the result stays block diagonal. Its diagonal blocks are A adjoint A and B adjoint B. So the eigenvalues that describe squared singular values come from the two blocks independently. We merge them and take square roots.

Let's look at the Ky Fan sums: sums of the largest few singular values.

The first sum is five. The first two sum to nine. The first three sum to eleven. All four sum to twelve.

The two-slot result is worth calculating another way. We could take both slots from A, giving five plus one, or six. We could take one from each, giving five plus four, or nine. Or we could take both from B, giving four plus two, or six. The best allocation gives nine.

For any number of slots, the Ky Fan sum of a direct sum is the maximum over possible allocations between its blocks.

### Why the exact allocation rule is useful

The direct-sum rule immediately explains three familiar but different norms.

For operator norm, we only take the largest singular value, so the direct-sum norm is the larger block norm.

For Hilbert–Schmidt norm, we square all singular values and add them. Consequently, the square of the direct-sum Hilbert–Schmidt norm is the sum of the squares for the two blocks.

For trace norm, we add the singular values directly. So the direct-sum trace norm is the sum of the two trace norms when both operators are trace class.

These combination laws are different. An arbitrary symmetric gauge does not have to follow any single one of them.

The Ky Fan allocation formula survives on general Hilbert spaces when singular values are expressed through approximation numbers. That extension uses the appropriate min–max theory; it does not require the operator to possess a finite eigenbasis.

### Dominance and the membership question

Suppose A has every Ky Fan prefix no larger than C, and B has every prefix no larger than D.

Take any allocation of slots between A and B. The sum from those blocks is no larger than the corresponding allocation between C and D. Maximizing over allocations preserves the inequality.

So the direct sum of A and B has every Ky Fan prefix no larger than the direct sum of C and D.

Can we now conclude an inequality for every operator ideal gauge? Only if the ideal has the Ky Fan dominance property, and the dominating operator belongs to the ideal. Under those hypotheses, the dominated operator also belongs, and its gauge is no larger.

In infinite dimensions, comparing each finite prefix does not automatically guarantee membership in any chosen ideal. The dominance property supplies that implication.

The three constructions are now distinct. Selecting a block uses projections and contractions. Keeping diagonal blocks uses reflection averaging. Combining independent maps uses a merge of singular-value data. Knowing which operation we're performing tells us which proof and which constant are justified.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Symmetric operator ideals and membership

**Draft status:** audio-first mathematical lecture. **Prerequisites:** `057000` Schatten norms, `058000` invariant gauges, `095000` compactness, `097000` Ky Fan dominance. **Next:** `099000` Hilbert–Schmidt and trace-class operators.

---

#### Companion: mathematics and Lean correspondence (display only)

A symmetric operator ideal family provides a carrier Mem(T) for rectangular bounded operators and a gauge with composition control and adjoint invariance. An extended gauge equals the finite gauge on members and infinity off the carrier. The compact ideal's carrier is compactness and its finite gauge is operator norm. Schatten p membership, for p at least one, means the p-th powers of approximation numbers are summable; p=2 is Hilbert–Schmidt and p=1 is trace class. The infinite-dimensional identity has finite operator norm but infinite p-gauge for each finite p.

##### Actual Lean source declarations

`DavisKahan/OperatorIdeal/UnitarilyInvariant/FamilyCore.lean` — `Core.extendedGauge_ne_top_iff` (declaration header, proof omitted):

```lean
theorem Core.extendedGauge_ne_top_iff {A : E →L[𝕜] F} :
    Core.extendedGauge N A ≠ ∞ ↔ N.Mem A := by
```

`ForTauCeti/Analysis/OperatorIdeal/Family/CompactOperator.lean` — `mem_finiteSubmodule_compactOperatorIdealFamily` (declaration header, proof omitted):

```lean
theorem mem_finiteSubmodule_compactOperatorIdealFamily {A : E →L[𝕜] F} :
    A ∈ ((compactOperatorIdealFamily.{u, v, w} 𝕜).operatorGauge E F).finiteSubmodule ↔
      IsCompactOperator A := by
```

`ForTauCeti/Analysis/OperatorIdeal/Family/Schatten.lean` — `IsSchattenClass` (declaration header, proof omitted):

```lean
def IsSchattenClass (p : ℝ) (T : E →L[𝕜] F) : Prop := T.schattenENorm p ≠ ∞
```

**Type and hypothesis map.** The notation `N.Mem` is the family carrier. Finiteness of the extended `ℝ≥0∞` gauge is equivalent to membership. Compact-ideal membership is exactly `IsCompactOperator`. `schattenENorm p` is an extended-valued gauge, finite on the Schatten carrier.

These are exact excerpts from the supplied DKPS source snapshot. The mathematical narration develops its arguments independently; citing these declarations does not assert that the narrated intermediate proof has been separately compiled in Lean. Where the current declaration lives in `ForTauCeti`, its placement does not imply the mathematical result originated outside the DKPS project.

### Hilbert–Schmidt and trace-class operators

**Draft status:** audio-first mathematical lecture. **Prerequisites:** `012000` adjoints and Riesz, `036000` SVD, `074000` integration and L2, `098000` operator ideals. **Next:** `100000` modulus, polar factors, and ideal invariance.

---

#### Companion: mathematics and Lean correspondence (display only)

For a Hilbert basis e_i of E, HS energy of T:E→F is sum_i ‖T e_i‖², with extended value allowed. Parseval, the adjoint identity and interchange of nonnegative sums prove basis independence and equality with HS energy of T*. For compact T this energy equals sum_i s_i(T)². The trace-class norm is sum_i s_i(T); absolute summability ensures the basis-independent trace ∑⟨e_i,T e_i⟩. Two Hilbert–Schmidt factors compose to trace class with nuclear norm ≤ product of their Hilbert–Schmidt norms.

##### Actual Lean source declarations

`DavisKahan/Sources/DavisKahan1970/Ideals/HilbertSchmidtBasis.lean` — `hilbertSchmidtBasisEnergy_indep` (declaration header, proof omitted):

```lean
theorem hilbertSchmidtBasisEnergy_indep
    {ι κ : Type*} (b c : HilbertBasis ι 𝕜 F)
    (d : HilbertBasis κ 𝕜 E) (A : F →L[𝕜] E) :
    hilbertSchmidtBasisEnergy b A =
      hilbertSchmidtBasisEnergy c A := by
```

`DavisKahan/Sources/DavisKahan1970/Ideals/HilbertSchmidtBasis.lean` — `approximationNumberEnergy_eq_basisEnergy` (declaration header, proof omitted):

```lean
theorem approximationNumberEnergy_eq_basisEnergy {ι : Type*}
    (b : HilbertBasis ι 𝕜 F) (A : F →L[𝕜] E) :
    approximationNumberEnergy A = hilbertSchmidtBasisEnergy b A := by
```

`ForTauCeti/Analysis/OperatorIdeal/Nuclear/Trace.lean` — `nuclearTrace_eq_tsum_inner` (declaration header, proof omitted):

```lean
theorem nuclearTrace_eq_tsum_inner
    (A : E →L[𝕜] E) (b : HilbertBasis ι 𝕜 E) (hA : A.nuclearENorm ≠ ∞) :
    A.nuclearTrace = ∑' i, ⟪b i, A (b i)⟫_𝕜 := by
```

`ForTauCeti/Analysis/OperatorIdeal/Nuclear/Trace.lean` — `norm_nuclearTrace_le_nuclearENorm` (declaration header, proof omitted):

```lean
theorem norm_nuclearTrace_le_nuclearENorm
    (A : E →L[𝕜] E) (hA : A.nuclearENorm ≠ ∞) :
    ‖A.nuclearTrace‖ ≤ A.nuclearENorm.toReal := by
```

**Type and hypothesis map.** The input-basis energy is unchanged between Hilbert bases using adjoint cross-swap. This bridge relates the approximation-number energy to basis-column energy; note all Hilbert basis assumptions. The `nuclearENorm ≠ ∞` hypothesis is essential for the basis-independent trace series. A trace-class hypothesis yields the canonical trace bound.

These are exact excerpts from the supplied DKPS source snapshot. The mathematical narration develops its arguments independently; citing these declarations does not assert that the narrated intermediate proof has been separately compiled in Lean. Where the current declaration lives in `ForTauCeti`, its placement does not imply the mathematical result originated outside the DKPS project.

### Smoothed singular-value energies

**Draft status:** audio-first mathematical lecture. **Recommended background:** `096000` singular-value sequences, `098000` symmetric operator ideals, `099000` Hilbert–Schmidt and trace-class operators.

---

#### Companion: mathematics and source correspondence (display only)

For \(\tau>0\) and \(s\ge0\),
\[
\phi_\tau(s)=\sqrt{\tau^2+s^2}-\tau
=\frac{s^2}{\sqrt{\tau^2+s^2}+\tau},\qquad
\frac{s^2}{\sqrt{\tau^2+M^2}+\tau}\le\phi_\tau(s)\le\frac{s^2}{2\tau}\quad(0\le s\le M).
\]
For a compact bounded T, \(\Phi_\tau(T)=\sum_j\phi_\tau(s_j(T))\) is finite if and only if \(T\in S_2\). The extended cost defined using approximation-number singular values can be treated across bounded operators, with nonmembership recorded as infinity. For a finite rectangular complex matrix, \(\nabla\Phi_\tau(T)=T(T^*T+\tau^2I)^{-1/2}\) in the real Frobenius pairing.

**Checked source map.** `ForTauCeti/Analysis/OperatorIdeal/Charbonnier.lean` includes `charbonnier_quadratic_bounds`, `charbonnierCost`, `schatten_two_sq_le_mul_charbonnierCost`, `charbonnierCost_le_mul_schatten_two_sq`, and `charbonnierCost_ne_top_iff_schatten_two`. `ForTauCeti/Analysis/OperatorIdeal/SmoothedPower.lean` develops a wider family of smoothed spectral power costs. The matrix gradient is an independent finite-dimensional calculus calculation; the named declarations above establish the quadratic bounds and domain characterization, not that gradient formula.

### Modulus, polar factors, and ideal invariance

**Draft status:** audio-first mathematical lecture. **Prerequisites:** `035000` operator modulus, `037000` polar decomposition, `038000` partial isometries, `098000` symmetric ideals, `099000` Schatten classes. **Next:** `101000` ideal estimates for compressions and block sums.

---

#### Companion: mathematics and Lean correspondence (display only)

For T:E→F, |T|=(T* T)^{1/2} acts on E. The canonical polar factor U:E→F is a contraction satisfying T=U|T| and |T|=U* T. Every symmetric ideal gauge obeys gauge(A T B)≤‖A‖ gauge(T) ‖B‖ for bounded composable A,B. Thus gauge(T)≤gauge(|T|) and gauge(|T|)≤gauge(T), giving equality in the extended nonnegative reals. Consequently Mem(T) iff Mem(|T|). No invertibility or equality of source and target dimensions is required.

##### Worked example: canonical partial isometry

For \(T=\begin{pmatrix}0&3\\0&0\end{pmatrix}\) on \(\mathbb R^2\),
\[
T^*T=\begin{pmatrix}0&0\\0&9\end{pmatrix},\qquad
|T|=\begin{pmatrix}0&0\\0&3\end{pmatrix},\qquad
U=\begin{pmatrix}0&1\\0&0\end{pmatrix}.
\]
Then \(T=U|T|\), \(|T|=U^*T\), and \(U^*U=\operatorname{diag}(0,1)\). The initial space of the canonical polar factor is \(\operatorname{span}(e_2)\), and the kernel is \(\operatorname{span}(e_1)\). Both \(T\) and \(|T|\) have singular values \((3,0)\).

##### Actual Lean source declarations

`ForTauCeti/Analysis/OperatorIdeal/Family/Modulus.lean` — `norm_polarFactor_le_one_rectangular` (declaration header, proof omitted):

```lean
theorem norm_polarFactor_le_one_rectangular (T : E →L[K] F) :
    ‖T.polarFactor‖ ≤ 1 := by
```

`ForTauCeti/Analysis/OperatorIdeal/Family/Modulus.lean` — `gauge_modulus_eq` (declaration header, proof omitted):

```lean
theorem gauge_modulus_eq
    (N : SymmetricOperatorIdealFamily.{u, v} K) (T : E →L[K] F) :
    N.toOperatorIdealFamily.gauge T.modulus =
      N.toOperatorIdealFamily.gauge T := by
```

`ForTauCeti/Analysis/OperatorIdeal/Family/Modulus.lean` — `modulus_mem_iff` (declaration header, proof omitted):

```lean
theorem modulus_mem_iff
    (N : SymmetricOperatorIdealFamily.{u, v} K) (T : E →L[K] F) :
    T.modulus ∈ (N.toOperatorIdealFamily.operatorGauge E E).finiteSubmodule ↔
      T ∈ (N.toOperatorIdealFamily.operatorGauge E F).finiteSubmodule := by
```

**Type and hypothesis map.** The polar factor is contractive for `T : E →L[K] F`, even when source and target differ. The two contractions `T.polarFactor` and its adjoint give both inequalities and hence equality of extended gauges. Finiteness of the gauge gives equivalence between membership of `T` and membership of `T.modulus`.

These are exact excerpts from the supplied DKPS source snapshot. The mathematical narration develops its arguments independently; citing these declarations does not assert that the narrated intermediate proof has been separately compiled in Lean. Where the current declaration lives in `ForTauCeti`, its placement does not imply the mathematical result originated outside the DKPS project.

### Ideal estimates for compressions and block sums

**Draft status:** audio-first mathematical lecture. **Prerequisites:** `054000` Ky Fan sums, `060000` pinching, `097000` Hilbert-space Ky Fan dominance, `098000` symmetric ideals, `100000` modulus invariance. **Next:** `102000` real Hilbert complexification.

---

#### Companion: mathematics and Lean correspondence (display only)

For orthogonal projections `P` on `E` and `Q` on `F`, the ideal-composition inequality gives `gauge(Q ∘ T ∘ P) ≤ gauge(T)` and preserves the carrier. The rectangular pinching identity is

\[
QTP+(I-Q)T(I-P)=\tfrac12(T+U_QTU_P),\qquad U_Q=2Q-I,\quad U_P=2P-I.
\]

Both reflections are unitary, so the symmetric ideal triangle and invariance laws yield the sharp bound. For the orthogonal direct sum, the exact prefix formula is

\[
K_k(A\oplus B)=\max_{0\le r\le k}\bigl(K_r(A)+K_{k-r}(B)\bigr).
\]

##### Worked example: compression, pinching, direct sum

For \(T=\begin{pmatrix}3&4\\1&2\end{pmatrix}\), let \(P=Q=\operatorname{diag}(1,0)\) and \(J=2P-I\). Then
\[
QTP=\begin{pmatrix}3&0\\0&0\end{pmatrix},\quad
J T J=\begin{pmatrix}3&-4\\-1&2\end{pmatrix},\quad
\tfrac12(T+JTJ)=\operatorname{diag}(3,2).
\]
The rectangular pinching is an average of two unitarily equivalent operators. The trace norm of the pinching is \(5\), while \(\|T\|_1=\sqrt{\|T\|_F^2+2|\det T|}=\sqrt{34}\).

For \(A=\operatorname{diag}(5,1)\) and \(B=\operatorname{diag}(4,2)\), the singular values of \(A\oplus B\) are \((5,4,2,1)\), yielding prefixes \((5,9,11,12)\). For the two-slot prefix, \(\max\{K_2(A),K_1(A)+K_1(B),K_2(B)\}=\max\{6,9,6\}=9\).

##### Actual Lean source declarations

`ForTauCeti/Analysis/OperatorIdeal/Family/BlockSum.lean` — `gauge_blockSum_le` (exact declaration header; proof omitted):

```lean
theorem gauge_blockSum_le {T : E →L[𝕜] F} {P₁ P₂ : E →L[𝕜] E} {Q₁ Q₂ : F →L[𝕜] F}
    (hP₁ : ‖P₁‖ ≤ 1) (hP₂ : ‖P₂‖ ≤ 1) (hQ₁ : ‖Q₁‖ ≤ 1) (hQ₂ : ‖Q₂‖ ≤ 1)
    (hsplit : Q₁ ∘L T ∘L P₁ + Q₂ ∘L T ∘L P₂ = T) :
    max (N.gauge (Q₁ ∘L T ∘L P₁)) (N.gauge (Q₂ ∘L T ∘L P₂)) ≤ N.gauge T ∧
      N.gauge T ≤ N.gauge (Q₁ ∘L T ∘L P₁) + N.gauge (Q₂ ∘L T ∘L P₂) := by
```

`DavisKahan/OperatorIdeal/ApproximationNumbers/BlockSum.lean` — `kyFanApproximationGauge_continuousOrthogonalBlockSum` (exact declaration header; proof omitted):

```lean
theorem kyFanApproximationGauge_continuousOrthogonalBlockSum
    {E₀ E₁ F₀ F₁ : Type v}
    [NormedAddCommGroup E₀] [InnerProductSpace 𝕜 E₀] [CompleteSpace E₀]
    [NormedAddCommGroup E₁] [InnerProductSpace 𝕜 E₁] [CompleteSpace E₁]
    [NormedAddCommGroup F₀] [InnerProductSpace 𝕜 F₀] [CompleteSpace F₀]
    [NormedAddCommGroup F₁] [InnerProductSpace 𝕜 F₁] [CompleteSpace F₁]
    (k : ℕ) (A : E₀ →L[𝕜] F₀) (B : E₁ →L[𝕜] F₁) :
    ((continuousOrthogonalBlockSum A B).kyFanGauge k : ℝ) =
      splitKyFanGauge k A B := by
```

`DavisKahan/OperatorIdeal/ApproximationNumbers/BlockSum.lean` — `kyFanApproximationGauge_blockSum_le` (exact declaration header; proof omitted):

```lean
theorem kyFanApproximationGauge_blockSum_le
    {E₀ E₁ F₀ F₁ : Type v}
    [NormedAddCommGroup E₀] [InnerProductSpace 𝕜 E₀] [CompleteSpace E₀]
    [NormedAddCommGroup E₁] [InnerProductSpace 𝕜 E₁] [CompleteSpace E₁]
    [NormedAddCommGroup F₀] [InnerProductSpace 𝕜 F₀] [CompleteSpace F₀]
    [NormedAddCommGroup F₁] [InnerProductSpace 𝕜 F₁] [CompleteSpace F₁]
    {A C : E₀ →L[𝕜] F₀} {B D : E₁ →L[𝕜] F₁}
    (hA : ∀ k, (A.kyFanGauge k : ℝ) ≤ (C.kyFanGauge k : ℝ))
    (hB : ∀ k, (B.kyFanGauge k : ℝ) ≤ (D.kyFanGauge k : ℝ)) :
    ∀ k, ((continuousOrthogonalBlockSum A B).kyFanGauge k : ℝ) ≤
      ((continuousOrthogonalBlockSum C D).kyFanGauge k : ℝ) := by
```

**Type and hypothesis map.** `gauge_blockSum_le` assumes four contractive factors and an exact two-block reconstruction, and gives both a maximum lower bound and a sum upper bound. The two Ky Fan statements concern `ContinuousLinearMap` block sums between possibly different Hilbert spaces, without assuming a finite singular-vector basis. Their outputs are finite-prefix comparisons, not automatic membership in every symmetric ideal.

These Lean snippets are copied exactly from the supplied DKPS repository snapshot. The narration is an independent mathematical derivation; this appendix does not claim that the narrated text was compiled in Lean. Foundational results currently in `ForTauCeti` may have been developed in DKPS before upstreaming.
