# Positivity, moduli, singular values, and polar factors

<!-- BEGIN SPOKEN LECTURE -->

# Positivity, moduli, singular values, and polar factors

## Quadratic-form order and positive operators

For an ordinary number, positivity is straightforward. Three is positive, negative two is not, and zero sits at the boundary.

For a matrix, it cannot mean that all its entries are positive. A matrix can have negative entries and still be positive in the sense used in operator theory. Conversely, a matrix with all positive entries need not satisfy that operator-theoretic condition.

What we need is a definition that survives a change of orthonormal coordinates and tells us how the operator acts on *every direction*.

### A matrix as a measurement of energy

Take a real symmetric matrix A and a vector x. Form the number obtained by multiplying x by A and taking the inner product of x with the result. This number is called the quadratic form of A at x.

You have already met its normalized version: the Rayleigh quotient. Here we keep the length of x in the expression instead of dividing by it.

We call A *positive semidefinite* when its quadratic form is never negative, no matter which vector we choose. In the complex setting, we use self-adjoint operators and their real-valued quadratic forms.

Why require self-adjointness? Because we want an order on operators with the same geometric behavior as the order on real numbers. A general matrix can mix symmetric and skew effects, and the quadratic expression alone need not detect the skew part in the real case.

Consider the real ninety-degree rotation matrix: zero on the diagonal, negative one in the upper-right entry, and one in the lower-left. Its quadratic form is zero for every vector, because a vector is perpendicular to its ninety-degree rotation. Yet this matrix is not self-adjoint. So merely testing that its quadratic form is nonnegative would not give the right definition of a positive operator unless we also require self-adjointness.

### A matrix with negative entries can be positive

Look at the symmetric matrix with two on both diagonal entries and negative one in both off-diagonal positions.

Choose a vector with real coordinates x and y. Its quadratic form is two x squared, minus two x times y, plus two y squared.

Rewrite that as the square of x minus y, plus x squared, plus y squared. Each term is nonnegative. Therefore the entire expression is nonnegative for every vector. In fact, it is strictly positive for every nonzero vector.

So this matrix is positive definite, although two entries are negative.

Now take the diagonal matrix with entries negative one and two. Its entries are easy to inspect, but the important test is directional. On the first coordinate direction its quadratic form is negative one. That single vector proves it is not positive semidefinite.

Positivity means the quadratic form is nonnegative on every vector, regardless of the signs of individual matrix entries.

#### Why positive entries do not suffice either

We have seen that negative entries do not rule out positivity. The opposite error is just as easy to make. Consider the symmetric matrix whose diagonal entries are one and whose off-diagonal entries are two. All four entries are positive.

Test the direction with first coordinate one and second coordinate negative one. The matrix sends that vector to its negative. Its quadratic form is therefore negative two. So this matrix is not positive, even though every entry in its displayed array is positive.

The two examples point to the same test: choose a direction and ask whether the operator gives a nonnegative quadratic measurement there. Checking a table of entries cannot answer that question.

### The spectral criterion

We can test positivity using the finite spectral theorem.

Suppose A is self-adjoint, with an orthonormal basis of eigenvectors. Write a vector as a sum of components along those directions. Its quadratic form is the sum of each eigenvalue multiplied by the squared length of the corresponding component.

If every eigenvalue is nonnegative, each term in that sum is nonnegative. Therefore the operator is positive semidefinite.

Conversely, if an eigenvalue is negative, choose a unit eigenvector for it. Its quadratic form equals that negative eigenvalue. So the operator cannot be positive semidefinite.

We have proved a precise equivalence: a finite-dimensional self-adjoint operator is positive semidefinite if and only if all its eigenvalues are nonnegative.

And it is positive definite if and only if all its eigenvalues are strictly positive. In finite dimensions, that also means there is a fixed positive number c such that the quadratic form is at least c times the squared length of every vector. We can choose c to be the smallest eigenvalue.

The condition involving a *uniform* positive c becomes especially important in infinite dimensions, where positivity on every nonzero vector need not provide such a bound.

### Ordering two operators

Now we can compare matrices using an analogue of the usual number-line order.

For two self-adjoint operators A and B on the same space, say that A is less than or equal to B when B minus A is positive semidefinite.

Equivalently, for every vector x, the quadratic form of A at x is at most the quadratic form of B at x.

This is sometimes called the Loewner order, or quadratic-form order.

Notice that it is a *partial* order. Some pairs of operators cannot be compared in either direction.

For example, consider A with diagonal entries one and zero, and B with diagonal entries zero and one. On the first coordinate vector, A gives the larger quadratic form. On the second, B gives the larger one. Neither operator is below the other.

We should not expect every pair of self-adjoint matrices to line up like two real numbers.

### Order survives changes of coordinates and compression

There is a particularly useful rule. If A is less than or equal to B, and C is any linear map into their space, then C adjoint times A times C is less than or equal to C adjoint times B times C.

Let's prove it with one vector.

Choose any input vector y for C. The quadratic form of C adjoint A C at y is exactly the quadratic form of A at the vector C y. By our assumption, that is no greater than the quadratic form of B at C y. Rewrite this as the quadratic form of C adjoint B C at y. Since the inequality holds for every y, the operator inequality follows.

If C is unitary, this is simply a change of orthonormal coordinates. Positivity must survive because the geometry has not changed.

If C is an isometric embedding of a smaller coordinate space, we get the compression C adjoint A C. Positivity survives that operation too. This explains why a positive operator remains positive when we examine it on a trial subspace.

But be careful with the converse. An operator may look positive on one selected subspace while having a negative direction somewhere else. Testing a compression does not necessarily test the entire operator.

### Gram operators are automatically positive

We already constructed Gram operators from linear maps. For any linear map S between finite-dimensional inner-product spaces, its source Gram operator is S adjoint times S.

Evaluate its quadratic form at x. The result is the inner product of S x with itself: the squared norm of S x. Squared lengths are nonnegative. Therefore S adjoint S is positive semidefinite.

The Gram construction encodes lengths and inner products in a positive self-adjoint operator, whose spectrum determines the singular values.

The kernel also has a simple interpretation. The quadratic form of S adjoint S vanishes at x exactly when S x is zero. So its zero directions are precisely the kernel of S.

Conversely, every positive semidefinite operator in finite dimensions can be factored as S adjoint S, using the finite spectral theorem and nonnegative square roots.

### Why products require care

It is tempting to say that the product of two positive operators is always positive, just as the product of two nonnegative numbers is nonnegative. That is false unless we impose additional structure.

Take the projection A onto the first coordinate axis. Take B to be the matrix with every entry equal to one. Both are positive semidefinite. But the product A B has first row one, one and second row zero, zero. It is not symmetric, so it is not a positive operator in our sense.

When positive operators commute, they can be diagonalized together in finite dimensions, and their product is again positive. Without commutation, even self-adjointness of the product can fail.

This is one reason the order theory of operators is richer than ordinary scalar arithmetic. We must prove the rules we use, not assume every scalar rule automatically transfers to matrices.

### Toward positive square roots

We have learned to detect positivity through quadratic forms and through eigenvalues. We have also learned how to apply functions to self-adjoint operators.

Combine those ideas. If A is positive, all its eigenvalues are nonnegative. We can take the ordinary nonnegative square root of each eigenvalue, then reassemble an operator using the same spectral projections.

The result will be positive, and squaring it will recover A.

But is it the *only* positive operator whose square is A? And can we characterize it without choosing coordinates? Those are the questions.

To test your understanding, explain why the quadratic form of a Gram operator is a squared length, why a negative eigenvalue rules out positivity, and why comparing A with B requires checking every vector. Then prove that compression preserves positivity using only the adjoint identity.

That reconstruction gives us the tools we will need for positive square roots, the operator modulus, and eventually polar decomposition.

## Positive square roots and their uniqueness

If I tell you that a real number is nine, finding a square root is easy. Three works, and negative three works. But if I ask for the *nonnegative* square root, there is only one answer.

For matrices, there is a similar distinction. We can sometimes find many matrices whose square equals a given matrix. We want one special square root that is positive in the operator sense. The positive square root is defined through the spectral decomposition. It exists uniquely for a positive matrix, unlike an entrywise square-root construction, which does not respect changes of orthonormal basis.

Positive square roots define the operator modulus and provide the spectral ingredients for singular-value decomposition.

### Why entrywise square roots don't work

Consider a matrix with two diagonal entries, nine and one, and zeros elsewhere. Its positive square root is the diagonal matrix with entries three and one. So far, this looks like taking ordinary square roots.

But now imagine describing the very same operator using a different orthonormal basis. Its matrix might acquire nonzero off-diagonal entries. Taking an entrywise square root would not respect this change of coordinates, and there is no reason the resulting matrix should square back to the original.

This tells us what to preserve: not the table of entries, but the operator's action on its eigenspaces.

### Building the square root

Let P be a positive semidefinite, self-adjoint operator on a finite-dimensional real or complex inner-product space.

The finite spectral theorem gives an orthonormal basis of eigenvectors. For a self-adjoint positive matrix P, every eigenvalue is nonnegative, because evaluating its quadratic form on an eigenvector gives that eigenvalue times the squared norm.

Write any vector x as a sum of components along these eigenvectors. On a component corresponding to eigenvalue lambda, P multiplies by lambda.

Define a new operator S by doing the same thing, but multiplying that component by the ordinary *nonnegative square root* of lambda. This is an instance of functional calculus: S is the square-root function applied to P.

Now apply S twice. Along the lambda-eigenspace, the first application multiplies by square root of lambda, and the second does it again. Their product is lambda. So S squared equals P on every eigenvector and therefore on every vector.

S is also self-adjoint: it has a real diagonal representation in an orthonormal eigenbasis. And its eigenvalues are nonnegative, so S is positive semidefinite.

We have established existence without solving a new matrix equation entry by entry.

### A matrix we can check by hand

Consider the symmetric two-by-two matrix whose diagonal entries are five and whose off-diagonal entries are four.

The direction with equal coordinates is an eigenvector with eigenvalue nine. The direction with opposite coordinates is an eigenvector with eigenvalue one. Those two directions are perpendicular.

Our construction says that the square root must multiply the equal-coordinate direction by three and the opposite-coordinate direction by one.

When we express that operation back in ordinary coordinates, we get a matrix with two on the diagonal and one in each off-diagonal position.

Check its square. The upper-left entry is two times two plus one times one, giving five. The upper-right entry is two times one plus one times two, giving four. The other entries work the same way. So the square is exactly the original matrix.

The new matrix has eigenvalues three and one. It is positive, as required.

Notice that the entries five and four did not simply turn into their individual square roots. The eigenvectors tell us how to take the square root correctly.

### Why positivity gives uniqueness

We have found *a* positive square root. Could there be a different positive operator B whose square is also P?

Start with B, not with P. Because B is positive and self-adjoint, the finite spectral theorem gives an orthonormal eigenbasis for B. Every eigenvalue of B is a nonnegative real number.

Choose one of those eigenvectors. Suppose B multiplies it by a number called beta. Since B squared is P, applying P to this eigenvector multiplies it by beta squared.

And because beta is nonnegative, beta is precisely the nonnegative square root of beta squared.

What does the square-root construction applied directly to P do to that same eigenvector? P acts there by beta squared, so our constructed operator S acts there by beta.

Therefore B and S agree on an entire orthonormal basis of eigenvectors of B. Two linear operators that agree on a basis are equal. Thus B equals S.

That is the uniqueness proof. It does not assume in advance that B and P have conveniently chosen matching eigenbases. It derives what is needed from the equation B squared equals P.

If we remove positivity, uniqueness fails immediately: the negative of S also squares to P. In our numerical example, the matrix with ones on the diagonal and twos off the diagonal also squares to P, but it has a negative eigenvalue. Positivity rules out these alternative signs.

#### A degeneracy that tests uniqueness

The identity matrix provides a useful stress test. Every direction is an eigenvector with eigenvalue one, so there is no preferred eigenbasis. Its positive square root must nevertheless be the identity, because the nonnegative square root of that eigenvalue is one on *every* direction.

There are other square roots of the identity. A reflection, for example, squares to the identity. But it has a negative eigenvalue, so it is not positive. This shows exactly how positivity resolves the apparent ambiguity: it chooses the nonnegative scalar square root on each spectral direction, even when the eigenspace contains many possible bases.

### What happens on zero eigenspaces?

Suppose P has a zero eigenvalue. Our positive square root uses square root of zero, which is zero. So S vanishes on exactly the same eigendirections as P.

In fact their kernels are equal. If P kills a vector, expand that vector in an eigenbasis and observe that it lies entirely in the zero-eigenspace, which S also kills. Conversely, if S kills a vector, then P, being S squared, kills it too.

If P is invertible, it has no zero eigenvalues. Then S is also invertible, with inverse formed by taking the reciprocals of its positive eigenvalues. If P is not invertible, its positive square root still exists. We have no need to divide by zero.

Later we will also need to handle maps that collapse directions and therefore cannot be inverted.

### Two rules worth remembering

First, taking the positive square root is compatible with an orthonormal change of coordinates. If we rotate or otherwise unitarily change the coordinate system, the new matrix for S is simply the transformed matrix for the original S. That follows because both matrices represent the same construction on the corresponding eigenspaces.

Second, S commutes with P. We can see this directly: both operators multiply the same eigenspace components by scalar values. The order of those multiplications does not matter. In fact, S also commutes with any polynomial in P.

But do not conclude that the square root of a product is always the product of the square roots. In general, products of positive matrices need not even be self-adjoint. That scalar-looking formula requires additional hypotheses, such as appropriate commutation.

### Why this construction matters

We have learned how to turn a positive operator P into a unique positive operator S with S squared equal to P.

Now recall a map A that is not necessarily square, self-adjoint, or invertible. Its source Gram operator, A adjoint times A, is always positive. So it always has a positive square root.

That new operator will be called the *modulus* of A. It will tell us exactly how much length A produces in each input direction, even when A also rotates, reflects, or embeds those directions somewhere else.

Three useful reconstructions are these: explain why entrywise square roots fail under a change of basis. Rebuild the two-by-two example by using the eigenvectors with equal and opposite coordinates. And prove uniqueness starting from an arbitrary positive square root B, rather than assuming that B is already diagonal in your favorite basis for P.

The spectral construction produces the unique positive square root, and its uniqueness follows by comparing any positive square root with the original positive operator through functional calculus.

## The operator modulus |A|

A linear map can do several things at once. It can stretch some vectors, shrink others, rotate directions, or send a space into a higher-dimensional one. Sometimes it sends a nonzero vector to zero.

What if we want to separate the information about *length change* from everything else?

For a real number a, its absolute value tells us how much multiplication by a changes length. Multiplying by negative three reverses a direction and triples its length; the absolute value, three, remembers only the length change.

There is an operator construction with the same purpose. It is called the *modulus* of A, written as vertical bars around A. But it is not the matrix obtained by taking the absolute value of each entry.

We will build it from the Gram operator and the positive square root of the positive Gram matrix.

### Start with the length of an output

Let A map one finite-dimensional inner-product space E into another space F. The two spaces do not have to have the same dimension.

Choose a vector x in E. We know that the squared length of A x is the inner product of A x with itself.

By the defining identity of the adjoint, this is also the inner product of x with A adjoint A x. So the squared output length is determined entirely by the source Gram operator, A adjoint A.

That is an important observation. The expression A adjoint A acts on the *input* space E, even though A x lives in the output space F. This lets us measure the stretching without moving into the output space.

The operator A adjoint A is positive semidefinite, since pairing A adjoint A x with x gives the squared norm of A x. So it has a unique positive square root.

**Definition:** the modulus of A is the positive square root of A adjoint A.

It acts on E, not on F. Its square is A adjoint A.

### Why the modulus preserves the output lengths

Call the modulus M for a moment. Since M is positive, it is self-adjoint. And by construction, M squared is A adjoint A.

Now compute the squared length of M x. Using the adjoint identity, this equals the inner product of x with M adjoint M x. But M adjoint is M, so M adjoint M is M squared, which is A adjoint A.

We are back to the squared length of A x.

Thus M x and A x always have the same length. In spoken terms: *the modulus of A stretches every input vector by exactly the same amount as A does.*

This does not mean they produce the same output vector. They may not even live in the same space. A x lies in F, while M x lies in E.

Nor does it mean M and A have the same effect on angles relative to a fixed output coordinate system. The modulus retains the positive, self-adjoint part of the length-change geometry. Later, polar decomposition will describe the remaining isometric motion.

### A two-dimensional example

Let A take the vector with coordinates x and y and output the vector whose first coordinate is x plus y and whose second coordinate is zero.

The matrix of A has first row one, one and second row zero, zero.

What happens to lengths? The output has length equal to the absolute value of x plus y. The input direction with equal coordinates survives and gets stretched. The direction with opposite coordinates disappears completely.

Compute A adjoint A. Because we are using real coordinates, adjoint means transpose. The result is the two-by-two matrix with every entry equal to one.

That Gram operator has eigenvalue two on the equal-coordinate direction and eigenvalue zero on the opposite-coordinate direction.

Its positive square root therefore has eigenvalue square root of two on the first direction and zero on the second. In ordinary coordinates, its matrix has every entry equal to one divided by square root of two.

Check the length identity. Applied to x and y, this modulus produces two equal coordinates, each equal to x plus y divided by square root of two. Their squared lengths add to the square of x plus y. Exactly the same squared length as A's output.

But the modulus produces an output along the diagonal of the input plane. A produces an output along the horizontal axis. The length changes agree; the directions do not.

That is the separation we wanted.

#### Check a single direction before the formula

Return to the map that sends x comma y to x plus y comma zero. Use the unit diagonal input with both coordinates equal to one over the square root of two. The original map sends it to the horizontal vector of length square root of two.

The modulus instead sends that same unit diagonal input to a diagonal vector of length square root of two. In contrast, the unit anti-diagonal input is sent to zero by both maps. This is the whole story in two directions: one survives with the same stretching factor, the other is lost. The Gram eigenvectors tell us which directions to test; the modulus tells us their stretching without choosing output directions.

### Three examples that test the definition

First, suppose A is itself a positive operator on E. It is already the unique positive square root of A squared. Because A adjoint equals A, the modulus of A equals A. A positive operator has no sign or orientation change for the modulus to remove.

Second, suppose A is a unitary operator, or more generally an isometric embedding. Every input length is preserved. The defining adjoint identity for an isometry is A adjoint A equals the identity on E. The positive square root of the identity is the identity. Therefore the modulus of any isometry is simply the identity on its input space.

Third, suppose A is self-adjoint but has both positive and negative eigenvalues. Its adjoint equals itself, so A adjoint A equals A squared. On an eigenvector of A with eigenvalue lambda, its modulus acts by the absolute value of lambda.

For instance, a diagonal operator with entries negative three and two has modulus with diagonal entries three and two. Here the operator modulus really does behave like taking absolute values—but it does so on the *eigenvalues*, not on an arbitrary table of matrix entries.

### Kernels and directions that disappear

We can now prove a useful kernel identity.

If A kills x, its output length is zero. The modulus produces an output of exactly the same length, so the modulus also kills x.

Conversely, if the modulus kills x, the output length of A x must also be zero. Thus A kills x.

So A and its modulus have precisely the same kernel.

The kernel marks the input directions that disappear. The orthogonal complement of the kernel consists of directions on which there is no complete collapse. Later, the partial isometry in the polar decomposition will preserve lengths on that orthogonal complement and vanish on the kernel.

Notice that none of this required A to be invertible. The modulus is defined even when A maps a higher-dimensional space into a lower-dimensional one and must therefore have a nontrivial kernel.

### Modulus and the operator norm

Recall that the operator norm of A is the largest output length among inputs of length one.

Because A and its modulus produce equal lengths on every input, their operator norms are equal.

The modulus has an extra advantage: it is positive and self-adjoint, so the finite spectral theorem applies. Its operator norm is its largest eigenvalue.

Consequently, the largest possible stretching factor of A can be found by inspecting the eigenvalues of its modulus.

The complete ordered list of these nonnegative eigenvalues will become the singular values of A. So singular values are not mysterious numbers attached to an arbitrary rectangular matrix. They are the spectral data of an explicitly constructed positive operator that measures length change.

### What we have and what is still missing

We now know how to construct a canonical positive operator that captures the lengths produced by A. We know its square, its kernel, and its largest eigenvalue interpretation.

What we do not yet know is how to match each input stretching direction with its corresponding direction in the output space. That relationship is what singular-value decomposition will provide.

Try to reconstruct the chain before moving on: squared length of A x, then the Gram operator A adjoint A, then the positive square root, then equality of output lengths. Explain why the modulus lives on the source space even for a rectangular map. And check the example where A maps x and y to x plus y and zero.

## Singular-value decomposition

Imagine a flat sheet of material drawn as a circle. Apply a linear transformation. Typically, the circle becomes an ellipse. One direction is stretched most, another least, and in higher dimensions there are several independent stretching directions.

A general matrix does not tell us those directions just by looking at its entries. It mixes stretching with changes in orientation, and the matrix may be rectangular. But the operator modulus gives us a precise way to find the stretching information.

The singular-value decomposition, or S V D, follows from the spectral theorem for the positive Gram operator. Its eigenvectors identify input directions, and their images determine the corresponding output directions.

### Start with the source Gram operator

Let A be a linear map from a finite-dimensional real or complex inner-product space E to another such space F.

The source Gram operator, A adjoint A, acts on E. It is positive and self-adjoint. Therefore the finite spectral theorem supplies an orthonormal basis of E consisting of its eigenvectors.

Call these vectors v one, v two, and so on. Each has a nonnegative eigenvalue, since a Gram operator is positive.

For each eigenvalue, take its nonnegative square root. Call that number the corresponding singular value. We conventionally arrange the singular values from largest to smallest, counting multiplicity.

Why take square roots? Because the eigenvalues of A adjoint A describe *squared* output lengths. The singular values describe actual stretching factors.

If a unit input vector v has Gram eigenvalue nine, the length of A v is three. It is three, not nine, that belongs in a decomposition of A as stretches followed by orientation changes.

### Construct the output directions

Consider an eigenvector v with a *positive* Gram eigenvalue. Its image A v is nonzero. We can normalize it by dividing by its singular value.

Call the resulting unit vector u. In words, u equals A v divided by sigma, where sigma is the positive singular value.

Then A v equals sigma times u. We have a unit input direction, a nonnegative stretching factor, and a unit output direction.

Now the crucial question: if two input eigenvectors are orthogonal, are their corresponding output directions orthogonal?

Take two eigenvectors v i and v j with positive eigenvalues. Compute the inner product of A v i and A v j. Move A from the first slot to the second using the adjoint identity. What remains is the inner product of v i with A adjoint A v j.

Because v j is an eigenvector, that is its Gram eigenvalue multiplied by the inner product of v i and v j. For distinct indices, the latter is zero. So the output images are orthogonal.

On a single index, the squared length of A v i equals the corresponding Gram eigenvalue, which is sigma i squared. Therefore dividing by sigma i makes a unit vector.

We have proved that the output vectors obtained from the positive singular values are orthonormal.

This is the heart of the singular-value decomposition. The Gram operator identifies perpendicular input directions that A sends to perpendicular output directions.

### What happens when a singular value is zero?

We cannot divide by zero, and we do not need to.

A zero Gram eigenvalue means the squared length of A v is zero. So A v is the zero vector.

Those zero-eigenvalue input vectors form an orthonormal basis for the kernel of A. They are exactly the directions that disappear under the map.

For every positive singular value, we get a unit output direction. Since those output directions are orthonormal, we can extend them to an orthonormal basis of the entire output space F. The additional output vectors do not need matching nonzero input directions; they simply complete the coordinate system.

This handles rectangular maps and rank-deficient maps in one construction.

### A complete example

Take A from two-dimensional real space to three-dimensional real space. It sends the vector with coordinates x and y to the three-coordinate vector x plus y, zero, zero.

Its matrix has three rows and two columns. The first row is one, one. The other rows are zero.

For A of x comma y equal to x plus y, zero, zero, the adjoint sends an output triple to the pair whose two entries both equal the first coordinate of the triple. Consequently A adjoint A sends x comma y to x plus y, x plus y. Its two-by-two matrix has all entries one, as can also be checked by taking the dot products of A's two identical columns.

There are two perpendicular unit input directions. The first points along equal coordinates: one over square root of two, one over square root of two. Its Gram eigenvalue is two. The second points along opposite coordinates: one over square root of two, negative one over square root of two. Its Gram eigenvalue is zero.

Thus the singular values are square root of two and zero.

Apply A to the first unit input direction. Its output is square root of two, zero, zero. Normalize by its singular value and we obtain the first output basis vector, one, zero, zero.

Apply A to the second input direction and we obtain zero. That direction spans the kernel.

To finish the output basis, we can choose the other two coordinate axes in three-dimensional space. They are orthogonal to the first output vector and to each other.

In these specially chosen input and output coordinates, A does something very simple: it multiplies the first input coordinate by square root of two and sends the second to zero. Nothing else happens.

The complicated-looking relationship between the original coordinate systems has been absorbed into the choices of orthonormal bases.

### Putting the pieces into a factorization

Let V be the matrix whose columns are the orthonormal input eigenvectors we constructed. Let U be the matrix whose columns form the orthonormal output basis.

These are unitary matrices in complex coordinates, or orthogonal matrices in real coordinates.

Between them, place a rectangular diagonal matrix called Sigma. Along its diagonal are the singular values, in decreasing order. The remaining entries are zero.

The transformation A can then be written as U times Sigma times V adjoint.

Read that formula from right to left. First, V adjoint expresses the input in the special input basis. Second, Sigma independently stretches each coordinate by a nonnegative amount, possibly collapsing some to zero. Third, U places the result into the output space using the chosen output basis.

That is the singular-value decomposition.

We did not assume that A was normal, symmetric, square, or invertible. We only used finite-dimensional inner-product geometry and the spectral theorem for the positive Gram operator.

### What is intrinsic, and what can vary?

The ordered singular values are determined by A. They do not depend on which orthonormal bases we used to represent it. They are the eigenvalues of the modulus, with the appropriate zero-padding convention for rectangular matrices.

The singular vectors are less rigid.

If two positive singular values are equal, we can choose different orthonormal bases within their shared eigenspace and get different, equally valid singular vectors. Even for an isolated singular value, multiplying a complex singular vector by a unit-modulus phase changes its coordinates without changing the underlying decomposition when the corresponding output vector changes compatibly.

And when a singular value is zero, there is no associated normalized image vector. Choices made when completing the output basis are not determined by A.

This repeats a theme from spectral theory: eigenvalues and eigenspaces carry more intrinsic information than a particular selected basis.

### The two Gram operators and rank

The source Gram operator A adjoint A and the output Gram operator A A adjoint live on different spaces. Yet they have the same *positive* eigenvalues, counted with multiplicity.

We can now see why. Every positive singular value sigma yields an input vector v and output vector u satisfying A v equals sigma u. Applying A adjoint to u gives sigma v. It follows that A A adjoint acts on u by sigma squared, just as A adjoint A acts on v.

The reverse construction works too for every nonzero eigenvalue: start with an output eigenvector and apply A adjoint to recover an input eigenvector. Dividing by the positive eigenvalue provides an inverse on those eigenspaces. This is why multiplicities match, not just the set of positive values.

Now return to the two-to-three example. The source Gram matrix has one positive eigenvalue and one zero. The output Gram matrix has that same positive eigenvalue but *two* zero eigenvalues. The extra zero comes from a direction in the output space that no input can reach. The zero lists differ because E and F have different dimensions.

The number of positive singular values is the rank of A. And the largest singular value is the operator norm of A: the largest amount any unit input can be stretched.

Later, sums and functions of singular values will define the Schatten norms and the unitarily invariant norms used in Davis–Kahan estimates.

### The bridge to polar decomposition

The modulus tells us the stretching factors. The S V D also tells us how to carry each nonzero input stretching direction to its output direction without changing length.

That second operation can be assembled into a partial isometry. Composing the modulus with that partial isometry recovers A.

We will construct this factorization next, including what happens on the kernel and why the partial isometry is not always a unitary operator.

For now, reconstruct the proof that positive Gram eigenvectors produce orthonormal output directions. Explain why division by a singular value requires that it be positive. Then work through the three-by-two example and identify its rank, kernel, operator norm, and one possible pair of orthonormal input and output bases.

If you can do those things, the S V D is no longer merely a formula to remember. You have built it.

## Polar decomposition

Imagine pulling a rubber sheet over a table. You stretch it more in one direction than another, and then turn it. If I tell you only where each point ends up, can you separate the stretching from the motion that carries the stretched sheet to its final position?

For a linear map, this is exactly what polar decomposition does. And we already have most of its ingredients. The modulus of a map tells us its stretching, and the singular-value decomposition tells us which input and output directions correspond. Combining these ideas gives a factorization into a positive stretching operator and a partial isometry. The partial isometry handles the directions on which the map vanishes.

### Review what the modulus knows

Let A be a linear map from one finite-dimensional inner-product space, E, to another, F. The spaces may have different dimensions.

The modulus of A is the positive square root of A adjoint times A. We proved that the modulus and A give the same output length for every input. We also proved that they have the same kernel: a vector is killed by A exactly when it is killed by the modulus.

So the modulus tells us *how much* the map stretches a vector. It does not tell us *where the output points*. We want a second operator, call it U, that restores that missing directional information.

Our goal is to apply the modulus first, then U, and obtain A. In symbols, A equals U composed with the modulus of A.

Why should U preserve lengths? The modulus has already accounted for the length change. All that remains should be a length-preserving transformation wherever there was some nonzero length to preserve.

The qualification at the end is important: where the modulus sends a vector to zero, no output direction remains to be recovered.

### Construct U where its action is determined

Start with a vector of the form modulus of A applied to x. Define U on that vector by declaring that its output is A applied to x.

There are two things to check before this is a legitimate definition. First, could the same vector be written as modulus of A applied to two different inputs? If so, must the proposed output agree?

Suppose the modulus sends x and y to the same vector. Then it kills their difference. The kernels of A and its modulus agree, so A also kills their difference. Thus A x and A y are equal. Good: our proposed U does not depend on which input we chose.

Second, does U preserve length? Yes. The modulus is the positive square root of A adjoint A, so its squared norm on x equals the inner product of x with A adjoint A x, which is exactly the squared norm of A x. Therefore the proposed U sends every vector in the range of the modulus to a vector with exactly the same length.

It is also linear. The range of a linear map is a subspace, and the rule respects sums and scalar multiples because A and the modulus are linear.

We have constructed a length-preserving linear map from the range of the modulus into F. It carries that range onto the range of A.

### What happens to the kernel?

Here is the step that makes the construction canonical.

The range of the positive self-adjoint modulus is the orthogonal complement of its kernel, in finite dimensions. And that kernel is the kernel of A. So the input space splits into two perpendicular pieces: the directions that survive, and the directions that A kills.

On the surviving directions, U has already been determined. On the kernel, define U to be zero.

For any input vector, split it into a surviving component and a kernel component. Apply the length-preserving rule to the first, and zero to the second. That gives a linear map U from E to F.

It is not necessarily an isometry on the *whole* input space: a nonzero vector in the kernel still gets sent to zero. Instead, it is an isometry on the orthogonal complement of the kernel, and zero on the kernel. This kind of map is called a *partial isometry*.

Now check the desired factorization. The modulus of x belongs to the surviving subspace. By the definition of U there, U applied to modulus of x is exactly A x. That is polar decomposition.

We have proved it constructively, not just named it.

### A two-dimensional example

Take a map on the real plane that sends the vector with coordinates x and y to the vector with coordinates two y and zero.

It ignores the first coordinate. It doubles the second coordinate and places the result on the horizontal axis.

Its matrix has first row zero, two, and second row zero, zero. The adjoint-times-A matrix is diagonal, with entries zero and four. Its positive square root is diagonal with entries zero and two.

So the modulus leaves the first direction collapsed and doubles the vertical direction. The missing step is to take that stretched vertical direction and lay it along the horizontal axis.

Our polar factor U sends the vector with coordinates x and y to the vector with coordinates y and zero. In matrix language, its first row is zero, one, and its second row is zero, zero.

Check the composition. The modulus sends x and y to zero and two y. U then sends that to two y and zero. This is exactly A.

Notice the zero in U. U does not rotate the whole plane rigidly. It kills the horizontal input direction because that is the kernel of A. On the vertical input line, however, it preserves lengths perfectly.

Its input support and output range can be different subspaces of the same plane.

### Relation to singular-value decomposition

The singular-value decomposition chooses perpendicular input directions, one for each singular value. For a positive singular value, A sends its input direction to the associated output direction, multiplied by that singular value.

The modulus performs the multiplication by the singular value while staying in the input space. U then carries that input direction to its corresponding output direction, without additional stretching.

For a zero singular value, the modulus kills the input direction, and the canonical U kills it too. Thus polar decomposition is what remains of the singular-value decomposition after we stop insisting on choosing complete coordinate bases.

That is a conceptual advantage: the polar factor and modulus are intrinsic to A. The choice of singular vectors within repeated singular-value spaces is not.

### A nonsingular example

Consider a diagonal map that multiplies the first coordinate by negative three and the second by two.

Its modulus multiplies the first coordinate by three and the second by two. Its polar factor reverses the first coordinate and leaves the second alone.

Here U preserves lengths on the whole plane. It is an orthogonal transformation: a reflection. The original operator is a reflection followed by positive stretching.

When A has no kernel, the polar factor is an isometric embedding of its entire input space. If A is an invertible square matrix, that factor is actually unitary—or orthogonal in the real case.

But if A is rectangular, even an injective map need not have an onto unitary factor. It may embed a two-dimensional space in a three-dimensional one.

### What polar decomposition separates

Polar decomposition also explains canonical alignment between subspaces: the positive modulus measures how much each direction is stretched, while the polar partial isometry transports the surviving directions without depending on arbitrary orthonormal coordinates.

It also separates two quantities that appear throughout operator theory: the positive operator that records singular values, and the partial isometry that records where surviving vectors go. This separation extends to bounded operators on Hilbert spaces. In infinite dimensions the initial space is the closure of the modulus range, and the polar factor is defined there by continuous extension before being set to zero on its orthogonal complement.

Return to the map that takes the vertical component, doubles it, and places it horizontally. The modulus handles the doubling while staying on the vertical axis. The polar factor carries the stretched vertical vector to the horizontal axis without changing its length. The horizontal input, which the original map kills, is also killed by the canonical polar factor.

The construction is determined because the kernel has been accounted for and because two inputs with the same modulus image have the same original output. In that way, the equation A equals U times its modulus follows from a geometric rule that is both well-defined and length-preserving on surviving directions.

## Partial isometries and polar uniqueness

Suppose I take a sheet of paper, draw a short arrow on it, and ask you to move that arrow onto another arrow of the same length. You can decide exactly what happens to that arrow. But have I told you how to move every other direction in the plane? Not necessarily.

Polar decomposition expresses a linear map as a partial isometry followed by its positive modulus. The modulus determines the isometric action on the complement of its kernel. Extending that action onto unused directions, however, can involve a choice. The adjoint identifies precisely which input and output directions participate.

For spectral subspaces, a canonical motion on the relevant directions need not determine a unique unitary motion on the whole ambient space.

### An isometry on only part of a space

Recall the definition. A partial isometry is a linear map U that preserves lengths on the orthogonal complement of its kernel, and vanishes on its kernel.

The orthogonal complement of the kernel is called its *initial space*. The range is called its *final space*.

Think of the initial space as the part of the input on which genuine motion takes place. The kernel is not moved elsewhere; it is collapsed to zero. The final space is where the surviving part lands.

If there is no kernel, U is an isometry on the whole input. But it still might not be onto. An isometric embedding of a plane into three-dimensional space is not a unitary equivalence between those spaces.

If U also maps onto the entire output space, then it is a unitary map, or orthogonal in real coordinates.

So these words describe different promises. An isometry promises no change of length. A unitary promises that, and also that every output direction is reached. A partial isometry promises no change of length only on its initial space.

### Use the adjoint to locate the initial space

We can detect these spaces algebraically.

Take an input vector and split it into an initial-space part and a kernel part. U discards the second part and preserves the first part's inner products.

Apply U adjoint after U. On an initial-space vector, this composition returns the original vector. On a kernel vector, it returns zero.

That is precisely the orthogonal projection onto the initial space. In symbols, U adjoint U is that projection.

Likewise, U U adjoint is the orthogonal projection onto the final space. On the final space it acts as the identity, and outside that space it acts as zero.

These are two distinct projections, generally acting on two distinct Hilbert spaces. They tell us where the operator starts and where it lands.

For the real map A sending the vector x comma y to y comma zero, its polar factor U sends x and y to y and zero. Its initial space is the vertical axis. Its final space is the horizontal axis. Consequently U adjoint U projects onto the vertical axis, while U U adjoint projects onto the horizontal axis.

The two products are not equal, but each is a projection. This is a useful warning: a partial isometry need not be normal.

### The uniqueness question

Recall that the polar decomposition of A takes the form A equals U times the modulus of A.

Could some other operator W produce the same factorization?

Of course. The equation only asks W to act on vectors that occur as outputs of the modulus. If a direction never appears as an output of the modulus, the factorization cannot constrain W there.

But we built U with an extra requirement: U is zero on the kernel of A.

I claim that these two conditions uniquely determine U among linear maps: first, U applied after the modulus gives A; second, U kills the kernel of A.

To see why, suppose V satisfies the same two requirements. Every vector in the range of the modulus has the form modulus of A applied to x. On such a vector, both U and V must equal A x. So they agree on the range of the modulus.

They also agree on the kernel, because both vanish there. In finite dimensions the range of the modulus and the kernel are perpendicular complements and together span the entire input space. Therefore U and V agree everywhere.

That is the canonical uniqueness theorem for the polar factor. It does not depend on choosing an orthonormal basis or completing any missing directions.

### A factorization that is not canonical

Now remove the rule about vanishing on the kernel, and ask instead for a full unitary factor in a square-matrix factorization.

Take the two-by-two diagonal matrix whose first diagonal entry is two and whose second diagonal entry is zero. This A is already positive, so its modulus is A itself.

The identity matrix gives a factorization: A is identity times its modulus.

But the reflection that keeps the horizontal axis fixed and reverses the vertical axis gives the same factorization. Why? Because the modulus sends every input into the horizontal axis. The reflection agrees with the identity on that axis. What it does to the vertical axis is never tested.

Both factors are orthogonal maps of the whole plane. Neither is the canonical partial isometry: the canonical factor is the projection onto the horizontal axis, which kills the vertical direction.

The distinction is observable on one test vector. Feed the vertical unit vector directly into the two orthogonal factors: the identity leaves it fixed while the reflection reverses it. But feed it first through the modulus: the modulus returns zero, so both factorizations agree after composition. The factorization can test only what survives the modulus.

There is no contradiction. We are discussing two different optimization criteria for the missing part: either demand zero on the kernel, giving the unique partial isometry, or demand a unitary extension, which may allow choices.

### When can we complete the motion?

For a square matrix in finite dimensions, the kernel and the orthogonal complement of the range have the same dimension. That is a consequence of rank-nullity.

The canonical polar factor already provides an isometry from the complement of the kernel onto the range. Choose any isometry from the kernel onto the complement of the range and combine the two pieces. The result is a full unitary, or orthogonal, map of the whole space.

When the kernel is nonzero, that second piece is a choice. In fact, different choices generally give different unitary completions.

When A is invertible, the kernel is zero. There is no missing piece, so the polar factor is already a unitary map and is uniquely determined. You can also express it as A followed by the inverse of its modulus.

Unitary completion depends on the dimensions of the unused initial and final spaces. A rectangular map between spaces of different dimensions does not have a unitary equivalence between the entire spaces. In infinite dimensions, even a square bounded operator can have unequal dimensions of these missing pieces, preventing a unitary completion. The canonical partial isometry still makes sense.

### Why negative signs and symmetry are informative

Take any operator A and negate it. Negation reverses every output direction but leaves every output length unchanged. The modulus of negative A is therefore the same as the modulus of A.

The canonical polar factor, on the other hand, changes sign. On the surviving input directions, it must send the stretched vector to negative A's output. On the kernel it remains zero. Uniqueness then forces the whole canonical factor to be the negative of the original factor.

This illustrates how the two factors divide the work: the modulus remembers stretching, while the polar factor remembers orientation and alignment of surviving directions.

### What an incomplete transport can determine

For a unitary transport between subspaces, a polar factor can determine motion canonically on its initial space. Its action on the complementary directions is a separate extension problem: the unused source and target dimensions must match if a unitary extension is to exist.

If those directions are silently ignored, one can claim a rotation is uniquely determined when it is not, or claim a transformation is unitary when it only preserves length on a subspace. The mathematical distinction affects theorems about existence, uniqueness, and optimality.

Try reconstructing the argument in reverse. Starting with a partial isometry U, show that U adjoint U projects onto its initial space. Starting with a polar factorization, show why the modulus determines the factor only on the modulus's range. Finally, work through the rank-one diagonal example and exhibit two different full orthogonal factors.

The modulus determines the polar factor on the closure of its range; the complementary action may remain undetermined.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Quadratic-form order and positive operators

**Draft status:** audio-first mathematical lecture. **Prerequisites:** inner products, adjoints, the finite spectral theorem, Rayleigh quotients, and finite functional calculus. **Next:** positive square roots and uniqueness.

---

#### Companion: mathematical facts and Lean correspondence (display only)

For finite-dimensional self-adjoint \(A,B\) on a real or complex inner-product space,

\[
A\succeq0\iff \langle Ax,x\rangle\ge0\quad\forall x
\iff \sigma(A)\subseteq[0,\infty),
\]

and \(A\preceq B\iff B-A\succeq0\). For any linear \(C:F\to E\),

\[
A\preceq B\implies C^*AC\preceq C^*BC.
\]

In particular \(S^*S\succeq0\), because \(\langle S^*Sx,x\rangle=\|Sx\|^2\). The strict condition \(\langle Ax,x\rangle>0\) for all \(x\ne0\) implies a uniform positive lower bound in finite dimensions; this implication must **not** be silently extended to all infinite-dimensional operators.

**Entrywise signs do not decide operator positivity.** The matrix \(\bigl(\begin{smallmatrix}2&-1\\-1&2\end{smallmatrix}\bigr)\) has eigenvalues \(1,3\), whereas the entrywise positive matrix \(B=\bigl(\begin{smallmatrix}1&2\\2&1\end{smallmatrix}\bigr)\) has eigenvalues \(3,-1\) and \(\langle B(1,-1),(1,-1)\rangle=-2\).

**Lean bridge.** A source-level representation of a two-block quadratic-form hypothesis occurs in `ForTauCeti/Analysis/InnerProductSpace/Spectral/Gap.lean`:

```lean
def TwoBlockFormGap (A : E →ₗ[𝕜] E) (U : Submodule 𝕜 E)
    (a b : ℝ) : Prop :=
  (∀ x ∈ U, b * ‖x‖ ^ 2 ≤ RCLike.re ⟪A x, x⟫_𝕜) ∧
    (∀ x ∈ Uᗮ, RCLike.re ⟪A x, x⟫_𝕜 ≤ a * ‖x‖ ^ 2)
```

This is the quadratic-form version of an ordered spectral gap on the selected block and its perpendicular complement. `RCLike.re` extracts the real part so the order relation makes sense for real and complex scalars. The declared predicate packages inequalities; it does not itself prove that they follow from a spectrum hypothesis.

The companion `ForTauCeti/Analysis/InnerProductSpace/SpectralOrder.lean` has the following exact theorem signature (proof body omitted for display):

```lean
theorem lowerFormBoundOn_top_of_spectrum_subset_Ici
    (T : H →L[𝕜] H) (hT : IsSelfAdjoint T) {c : ℝ}
    (hσ : spectrum ℝ T ⊆ Set.Ici c) :
    T.LowerFormBoundOn ⊤ c := by
```

Here `Set.Ici c` denotes the closed set of numbers at least \(c\), `⊤` is the whole Hilbert space as a subspace, and `LowerFormBoundOn` records the lower quadratic-form inequality. This bridge connects the finite eigenvalue argument in the spoken lecture to a bounded Hilbert-space version that will receive its own analytic proof development later.

**Reconstruction:** Derive \(A\succeq0\iff\lambda_{\min}(A)\ge0\) from spectral expansion. Prove congruence preserves order. Give an explicit pair of positive semidefinite matrices whose product is not self-adjoint.

### Positive square roots and their uniqueness

**Draft status:** audio-first mathematical lecture. **Prerequisites:** finite spectral theorem, finite functional calculus, self-adjoint operators, quadratic-form positivity. **Next:** the operator modulus.

---

#### Companion: mathematical facts and Lean correspondence (display only)

For finite-dimensional self-adjoint positive semidefinite \(P\), with distinct eigenvalues \(\lambda\ge0\) and spectral projections \(P_\lambda\), define

\[
P^{1/2}=\sum_{\lambda\in\sigma(P)}\sqrt\lambda\,P_\lambda.
\]

Then \(P^{1/2}\succeq0\), \((P^{1/2})^2=P\), and if \(B\succeq0\) and \(B^2=P\), then \(B=P^{1/2}\). Moreover \(\ker P^{1/2}=\ker P\) and \(P^{1/2}P=PP^{1/2}\).

The DKPS-staged source `ForTauCeti/Analysis/InnerProductSpace/Positive/SquareRoot/Eigenspace.lean` **imports** `TauCeti.Analysis.InnerProductSpace.Positive.SquareRoot` and proves the following additional eigenvector principle (exact signature):

```lean
theorem apply_eq_smul_of_apply_apply_eq_smul {S : E →ₗ[𝕜] E} (hS : S.IsPositive)
    {v : E} {μ : ℝ} (hμ : 0 ≤ μ)
    (hv : S (S v) = ((μ : 𝕜) * (μ : 𝕜)) • v) :
    S v = (μ : 𝕜) • v := by
```

The mathematical meaning is that a positive operator cannot act by the negative square root on a vector where its square acts by \(\mu^2\). This is a local refinement of the square-root theory now imported from TauCeti; the theorem signature is cited as a source bridge, not as a substitute for the preceding uniqueness proof.

`ForTauCeti/Analysis/InnerProductSpace/Polar/Isometry.lean` also uses the exact imported uniqueness result:

```lean
  have hmodsqrt : CFC.sqrt a = M.modulus :=
    CFC.sqrt_unique M.modulus_comp_modulus M.modulus_nonneg
```

Here `CFC.sqrt` denotes the positive square root from continuous functional calculus, and `M.modulus_nonneg` and `M.modulus_comp_modulus` supply positivity and the square equation. The current bounded-Hilbert-space API is more general than the finite-dimensional construction proved in the spoken lecture.

**Reconstruction:** Prove existence and uniqueness from the finite spectral theorem. Verify directly that \(\begin{pmatrix}2&1\\1&2\end{pmatrix}^2=\begin{pmatrix}5&4\\4&5\end{pmatrix}\), and exhibit a different, nonpositive square root.

### The operator modulus |A|

**Draft status:** audio-first mathematical lecture. **Prerequisites:** adjoints, Gram operators, positivity, finite spectral calculus, positive square roots. **Next:** singular-value decomposition and polar decomposition.

---

#### Companion: mathematical facts and Lean correspondence (display only)

For finite-dimensional real or complex inner-product spaces \(E,F\) and \(A:E\to F\),

\[
|A|=(A^*A)^{1/2}:E\to E,\qquad |A|^2=A^*A,
\]
\[
\|Ax\|=\||A|x\|,\quad \ker|A|=\ker A,\quad \||A|\|_{\mathrm{op}}=\|A\|_{\mathrm{op}}.
\]

For self-adjoint \(A\), \(|A|\) acts on the \(\lambda\)-eigenspace by \(|\lambda|\). For an isometry \(A\), \(|A|=I_E\).

**Lean bridge.** The bounded Hilbert-space modulus is imported from `TauCeti.Analysis.InnerProductSpace.Modulus` by `ForTauCeti/Analysis/InnerProductSpace/ModulusTransport.lean`. The latter uses the exact defining identity:

```lean
  have hsq : A.modulus * A.modulus = A.adjoint ∘L A := A.modulus_comp_modulus
```

`A.modulus` lives on the source Hilbert space; `A.adjoint ∘L A` is the source Gram operator. The same file proves compatibility with real complexification, extending the coordinate-independent idea to scalar transport:

```lean
@[simp] theorem complexify_modulus (T : E →L[ℝ] E) :
    complexify T.modulus = (complexify T).modulus := by
```

This second statement is a later application of the modulus theory, not a prerequisite for understanding its finite-dimensional definition. The source currently refers to the accepted TauCeti modulus API; its present location is not evidence that the underlying mathematical work originated independently of DKPS.

`ForTauCeti/Analysis/InnerProductSpace/Polar/Isometry.lean` also records the identity relating Gram and modulus invertibility:

```lean
theorem isUnit_modulus_iff (M : E →L[ℂ] F) :
    IsUnit M.modulus ↔ IsUnit (M.adjoint ∘L M) := by
```

The lecture does not require invertibility; the theorem describes a useful additional property under the stated bounded complex-Hilbert-space assumptions.

**Reconstruction:** Prove equality of output lengths and equality of kernels. Compute \(|A|\) for \(A=\begin{pmatrix}1&1\\0&0\end{pmatrix}\). Show that \(|A|=A\) for positive \(A\) and \(|A|=I\) for isometric \(A\).

### Singular-value decomposition

**Draft status:** audio-first mathematical lecture. **Prerequisites:** Gram operators, the finite spectral theorem, adjoints, operator modulus, orthonormal bases. **Next:** polar decomposition.

---

#### Companion: mathematical facts and Lean correspondence (display only)

Let \(A:E\to F\) be a finite-dimensional linear map over \(\mathbb R\) or \(\mathbb C\). Choose an orthonormal eigenbasis \(v_i\) of \(A^*A\), with eigenvalues \(\lambda_i\ge0\). Let \(\sigma_i=\sqrt{\lambda_i}\). For \(\sigma_i>0\), define \(u_i=Av_i/\sigma_i\); these vectors are orthonormal. Extend to an orthonormal basis of \(F\). Then

\[
A=U\Sigma V^*,\qquad |A|=V(\Sigma^*\Sigma)^{1/2}V^*,
\]

where \(\Sigma\) is rectangular diagonal with nonnegative entries and suitable zeros. The number of positive singular values is \(\operatorname{rank}A\), and \(\|A\|_{\mathrm{op}}=\max_i\sigma_i\), with value zero if there are no positive singular values.

**Lean bridge.** The DKPS-staged file `ForTauCeti/Analysis/InnerProductSpace/RectangularSingularValues.lean` proves equality of the nonzero Gram spectral multiplicities. Its exact theorem signature is:

```lean
theorem finrank_eigenspace_adjointCompSelf_eq_selfCompAdjoint
    (A : E →ₗ[𝕜] F) (μ : 𝕜) (hμ : μ ≠ 0) :
    finrank 𝕜 (Module.End.eigenspace (A.adjoint.comp A) μ) =
      finrank 𝕜 (Module.End.eigenspace (A.comp A.adjoint) μ) :=
```

The corresponding equivalence is explicitly constructed by `nonzeroEigenspaceEquivAdjointCompSelfSelfCompAdjoint`, using the action \(x\mapsto Ax\) and inverse \(y\mapsto\mu^{-1}A^*y\). Thus this bridge captures the multiplicity-preserving argument from the spoken proof rather than merely mentioning singular values by name.

The same source also gives the exact relationship between singular values and the output Gram eigenvalues:

```lean
theorem sq_singularValues_selfCompAdjoint (A : E →ₗ[𝕜] F) {n : ℕ}
    (hn : finrank 𝕜 F = n) (i : Fin n) :
    A.singularValues i ^ 2 = (isSymmetric_self_comp_adjoint A).eigenvalues hn i := by
```

`A.singularValues` is the zero-padded finite sequence used by the library. `finrank` is dimension, and `Module.End.eigenspace` packages the eigenspace as a submodule. The accepted TauCeti singular-value machinery now supplies portions of the construction consumed by this local bridge; that does not erase the DKPS donor history.

**Reconstruction:** Prove orthonormality of \(u_i=Av_i/\sigma_i\), identify the kernel from zero Gram eigenvalues, and derive the rectangular formula \(U\Sigma V^*\). Explain why an output Gram operator has additional zero eigenvalues if the output dimension is larger than the rank.

### Polar decomposition

**Draft status:** audio-first mathematical lecture. **Prerequisites:** adjoints, kernels and orthogonal complements, positive square roots, operator modulus, singular-value decomposition. **Next:** partial-isometry uniqueness and unitary completion.

---

#### Companion: mathematical facts and Lean correspondence (display only)

For finite-dimensional real or complex inner-product spaces and any linear map \(A:E\to F\), put \(|A|=(A^*A)^{1/2}\). There is a canonical partial isometry \(U:E\to F\) such that

\[
A=U|A|,\qquad \ker U=\ker A,\qquad
U^*U=P_{(\ker A)^\perp},\qquad UU^*=P_{\operatorname{ran}A}.
\]

Construct \(U\) on \(\operatorname{ran}|A|\) via \(U(|A|x)=Ax\), then extend by zero on \(\ker A\). Well-definedness follows from \(\ker |A|=\ker A\), and isometry follows from \(\||A|x\|=\|Ax\|\).

**Lean bridge.** The DKPS-derived source `ForTauCeti/Analysis/InnerProductSpace/Polar/Decomposition.lean` records that `LinearMap.operatorAbs` and `LinearMap.polarFactor` are now supplied by TauCeti, retaining the original DKPS donor history. It also gives a selected **unitary completion for square finite-dimensional maps**, a stronger but less canonical choice:

```lean
noncomputable def choosePolarUnitary (A : E →ₗ[𝕜] E) : E ≃ₗᵢ[𝕜] E :=
  (A.exists_linearIsometryEquiv_eqOn_polarFactor rfl).choose
```

The equation connecting the chosen completion to the modulus is explicit:

```lean
@[simp]
theorem choosePolarUnitary_apply_operatorAbs_apply (A : E →ₗ[𝕜] E) (x : E) :
    choosePolarUnitary A (A.operatorAbs x) = A x := by
```

`operatorAbs` corresponds to \(|A|\). `polarFactor` is the canonical partial isometry. `E ≃ₗᵢ[𝕜] E` is a linear isometric equivalence of the whole space; the selected completion is not the canonical polar factor on the kernel. Its nonuniqueness is the subject of the next lesson.

**Reconstruction:** Build the polar factor for \(A(x,y)=(2y,0)\); calculate both support projections; and verify \(A=U|A|\) directly. Identify exactly where finite-dimensionality enters the range/complement argument.

### Partial isometries and polar uniqueness

**Draft status:** audio-first mathematical lecture. **Prerequisites:** Hilbert-space projections, adjoints, isometries, operator modulus, polar decomposition. **Next:** operator exponentials and continuous rotations.

---

#### Companion: mathematical facts and Lean correspondence (display only)

For finite-dimensional \(A:E\to F\), the canonical polar factor \(U\) satisfies \(A=U|A|\) and \(\ker U=\ker A\). It is the **unique** linear map meeting those two conditions; equivalently it is the unique partial isometry with that factorization and the canonical kernel. Its support identities are

\[
U^*U=P_{(\ker A)^\perp},\qquad UU^*=P_{\operatorname{ran}A}.
\]

In the square finite-dimensional case, a unitary extension of \(U|_{(\ker A)^\perp}\) exists because \(\dim\ker A=\dim(\operatorname{ran}A)^\perp\). The extension need not equal the canonical partial isometry on \(\ker A\), and need not be unique. For example, with \(A=\operatorname{diag}(2,0)\), both \(W=I\) and \(W=\operatorname{diag}(1,-1)\) satisfy \(A=W|A|\), while the canonical polar factor is \(U=\operatorname{diag}(1,0)\).

**Lean bridge.** In `ForTauCeti/Analysis/InnerProductSpace/Polar/PartialIsometry.lean`, the DKPS-staged development uses the accepted canonical uniqueness API in an exact proof that negation negates the polar factor:

```lean
@[simp]
theorem polarFactor_neg (M : E →L[𝕜] F) : (-M).polarFactor = -M.polarFactor := by
  symm
  apply (-M).eq_polarFactor
```

The subsequent proof establishes the composition condition and vanishing on the kernel. `ContinuousLinearMap.polarFactor` is the canonical operator. The imported `eq_polarFactor` theorem is used to establish equality from the characterizing equations; it is not a statement about arbitrary unitary completions.

The square finite-dimensional completion is separately realized by the exact source declaration in `ForTauCeti/Analysis/InnerProductSpace/Polar/Decomposition.lean`:

```lean
theorem polar_decomposition_choosePolarUnitary (A : E →ₗ[𝕜] E) :
    A = (choosePolarUnitary A : E →ₗ[𝕜] E) ∘ₗ A.operatorAbs := by
```

Note the distinct Lean types: `E →L[𝕜] F` is a bounded map on complete spaces; `E →ₗ[𝕜] E` is a finite-dimensional linear map in this source context; `E ≃ₗᵢ[𝕜] E` denotes a full linear isometric equivalence.

**Reconstruction:** Prove polar-factor uniqueness using \(E=\operatorname{ran}|A|\oplus\ker A\). Explain why the unitary completion is nonunique for \(\operatorname{diag}(2,0)\), and why the completion exists for all square finite matrices but not for every square bounded Hilbert-space operator.
