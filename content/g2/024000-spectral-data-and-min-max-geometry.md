# Spectral data and min-max geometry

<!-- BEGIN SPOKEN LECTURE -->

# Spectral data and min-max geometry

## Eigenvalues, eigenspaces, and algebraic multiplicity

Take a diagonal matrix with the number two on both diagonal entries. Every vector in the plane is an eigenvector with eigenvalue two. Now change the upper-right entry to one, leaving the diagonal entries unchanged. The characteristic polynomial is still the square of lambda minus two, so two has algebraic multiplicity two. But the new matrix has only a one-dimensional eigenspace.

This example separates two counts that are easy to confuse. Algebraic multiplicity counts occurrences of an eigenvalue as a root of the characteristic polynomial. Geometric multiplicity counts independent eigenvectors. The counts agree for self-adjoint matrices, which admit orthonormal eigenbases, but can differ for general matrices with Jordan blocks.

In operator theory, eigenvalues are only part of the spectrum, and infinite-dimensional operators can have spectral points with no eigenvector at all. We will start with the finite calculation, keep the definitions precise, and reserve the broader spectral distinction for the setting where it becomes necessary. The immediate goal is to understand what an eigenspace represents and which information is lost when one counts eigenvalues without counting directions.

### The eigenvector equation

Let A be a linear operator on a finite-dimensional vector space. Unlike a map between two different vector spaces, A goes from the space back to itself.

A nonzero vector v is an eigenvector with eigenvalue lambda when A of v equals lambda times v. The number lambda is an eigenvalue, and the equation says something geometric: A sends the line through v into itself. It may stretch it, shrink it, reverse its direction, or annihilate it if lambda is zero.

Why insist that v be nonzero? Because the zero vector satisfies A of zero equals lambda times zero for every lambda. If we allowed it as an eigenvector, the definition would convey no information at all.

Once lambda is fixed, all vectors satisfying the eigenvector equation form a subspace. This is the eigenspace for lambda. In symbols, it is the kernel of A minus lambda times the identity.

A kernel is closed under adding vectors and multiplying by scalars. So if two independent vectors share an eigenvalue, every linear combination of them shares that eigenvalue too. That eigenspace can have dimension greater than one.

### From the kernel to a determinant

In finite dimensions, choose a basis and write A as a square matrix. We can restate the eigenvector equation: A minus lambda times the identity sends some nonzero vector to zero.

A square matrix has a nonzero vector in its kernel exactly when it is not invertible. And a square matrix is not invertible exactly when its determinant is zero.

Thus lambda is an eigenvalue exactly when the determinant of A minus lambda times the identity is zero. Equivalently, it is a root of the characteristic polynomial, often written as the determinant of t times the identity minus A.

Those two determinant conventions have the same roots. They may differ by an overall sign depending on the dimension. When we speak of the characteristic polynomial, we will use the convention with t times the identity minus A, which gives a monic polynomial.

The characteristic polynomial does not depend on which basis we choose. If we change coordinates by an invertible matrix S, the new matrix is S inverse times A times S. The determinant of t times the identity minus that new matrix equals the old determinant, because the outer S and S inverse factors cancel inside the determinant.

That is an important point. The matrix entries change with a basis. The characteristic polynomial does not. It describes the operator rather than a particular coordinate chart.

### One eigenvalue can occur more than once

Let's start with the simplest repeated eigenvalue. Take the two-by-two matrix that multiplies every vector by two. Its matrix is two times the identity. Every nonzero vector is an eigenvector with eigenvalue two.

The characteristic polynomial is t minus two, squared. So the eigenvalue two is a repeated root, occurring twice. We call that repetition its algebraic multiplicity: two.

Its eigenspace is the entire two-dimensional plane. We call the dimension of the eigenspace its geometric multiplicity: also two.

So here the two multiplicities agree. The matrix has two independent eigenvectors, indeed infinitely many choices of eigenvector basis. We can diagonalize it using any basis we like.

Now I want to change just one entry of the matrix. Keep the two diagonal entries equal to two, but put a one in the upper-right corner. Leave the lower-left entry zero. In row form, our matrix is two, one on the first row, and zero, two on the second.

The characteristic polynomial is still t minus two, squared, because this is an upper triangular matrix. Its determinant after subtracting t along the diagonal is the product of the two diagonal factors. Algebraic multiplicity is still two.

But solve the eigenvector equation. Subtract two times the identity, and the remaining matrix sends a vector with coordinates x and y to the vector with coordinates y and zero. To land in the kernel, y must be zero. The first coordinate x can be anything.

Therefore the eigenspace consists only of horizontal vectors. Its geometric multiplicity is one.

Same eigenvalue. Same characteristic polynomial. Different number of independent eigenvectors.

### What the missing direction does

Consider the vertical unit vector under our second matrix. The operator sends it to the vertical vector multiplied by two, plus a horizontal vector. So the vertical direction is not an eigenvector. It leaks into the horizontal direction.

There is a useful way to describe that leakage. Subtract two times the identity, and call the resulting operator N. It sends the vertical unit vector to the horizontal unit vector, and sends the horizontal unit vector to zero.

Apply N twice to any vector and you get zero. So N is not zero, but N squared is zero. Such an operator is called nilpotent.

The vertical unit vector is an example of a generalized eigenvector for eigenvalue two. It is not killed by A minus two times the identity in one step, but it is killed after two steps. Together with the horizontal eigenvector, it forms what is called a Jordan chain.

A repeated root of the characteristic polynomial can correspond either to several independent eigenvectors or to a Jordan chain of generalized eigenvectors.

Our two examples make that distinction visible without any new machinery.

### Geometric multiplicity cannot exceed algebraic multiplicity

There is a general inequality here, and we can prove it with a smart choice of basis.

Fix an eigenvalue lambda whose eigenspace has dimension k. Choose a basis of that eigenspace and extend it to a basis of the entire space.

Because each of the first k basis vectors is an eigenvector, the first k columns of A have lambda in the corresponding diagonal position and zeros everywhere else. In this basis, A has an upper block-triangular shape. Its upper-left block is lambda times a k-by-k identity matrix, and its lower-left block is zero.

When we form t times the identity minus A and take its determinant, the determinant of a block-triangular matrix is the product of the determinants of its diagonal blocks. One factor is therefore t minus lambda, raised to the k-th power.

That means the characteristic polynomial has lambda as a root at least k times. So geometric multiplicity, which is k, can never exceed algebraic multiplicity.

The first of our two-by-two examples has equality. The second has strict inequality.

This proof is worth remembering. It turns the geometry of the eigenspace into a factor of the characteristic polynomial by choosing coordinates adapted to an invariant subspace.

### What diagonalization asks for

A matrix is diagonalizable when there is a basis made entirely of eigenvectors. In that basis, the matrix is diagonal: each basis vector is merely scaled.

Having eigenvalues is not enough. Having the right total number of roots counted with algebraic multiplicity is not enough either. We need enough *independent eigenvectors* to fill the space.

For the second two-by-two matrix, every genuine eigenvector lies on the horizontal axis. No collection of them can form a basis for the plane. So the matrix cannot be diagonalized.

Why do we care? Because a diagonal operator is much easier to understand. Its powers, exponentials, and many functions act separately on the eigenvector coordinates. If we can diagonalize an operator, we can often reduce a complicated equation to independent scalar calculations.

Their eigenspaces at distinct eigenvalues are orthogonal, and they admit an orthonormal eigenbasis. That is a theorem we will prove, not an assumption about every matrix.

### Real matrices may need complex scalars

There is one last qualification. A real matrix can have no real eigenvectors even though it has complex eigenvalues. For example, the real quarter-turn rotation has no real eigenvectors: it rotates every nonzero real vector by ninety degrees, so no real line is preserved. Over the complex numbers, however, it has two eigenvalues, i and negative i.

Over the complex numbers, every nonconstant polynomial has a root. Therefore every finite-dimensional complex matrix has at least one eigenvalue. Over the real numbers, that statement fails, as the quarter-turn example shows.

This is part of why spectral theory often uses complex scalars even when the motivating problem is real. We will keep track of which field we are working over rather than silently moving between them.

### What to take forward

Here is the hierarchy. An eigenvalue is a scalar for which A minus lambda I has a nonzero kernel. The eigenspace is that kernel. Geometric multiplicity counts independent eigenvectors for lambda. Algebraic multiplicity counts the root's repetition in the characteristic polynomial. The latter can be larger than the former, because a general matrix may contain nontrivial Jordan chains.

Try to reconstruct both two-by-two examples without notes. Compute their characteristic polynomials. Compute their eigenspaces. Explain why they have equal algebraic multiplicities but different geometric multiplicities. Then reproduce the block-triangular argument showing that geometric multiplicity cannot exceed algebraic multiplicity.

Their additional inner-product structure will rule out the kind of defect we just saw and set the stage for a spectral decomposition into orthogonal subspaces.

## Hermitian and self-adjoint matrices

A real symmetric matrix has the same entry above and below its diagonal. This simple-looking condition has strong consequences: its quadratic form is real, its eigenvalues are real, and eigenvectors with distinct eigenvalues are perpendicular.

Take the symmetric matrix with diagonal entries one and off-diagonal entries two. The diagonal direction with equal coordinates is an eigenvector with eigenvalue three. The direction with opposite coordinates is an eigenvector with eigenvalue negative one. These perpendicular directions describe the matrix completely.

Over the complex numbers, the correct condition is Hermitian symmetry: the matrix equals its conjugate transpose. An imaginary entry may occur above the diagonal, provided its complex conjugate occurs below. Calling a complex matrix symmetric without conjugation describes a different class.

We will examine exactly what Hermitian symmetry implies, why the inner-product convention matters, and how the self-adjoint finite-dimensional picture prepares us to use spectral subspaces rather than arbitrary matrix coordinates.

### What an adjoint does

Recall that the adjoint of an operator A is the unique operator A star for which the inner product of A x with y agrees with the inner product of x with A star y. The Riesz representation theorem supplies the adjoint, and the identity relates how A acts on one vector to how its adjoint acts on another.

In orthonormal coordinates over the real numbers, the adjoint matrix is the transpose. Rows and columns swap positions. Over the complex numbers, we must also conjugate the entries. The matrix of the adjoint is the conjugate transpose.

A matrix is self-adjoint when A equals A star. A real self-adjoint matrix is therefore symmetric across its main diagonal. A complex self-adjoint matrix is Hermitian: the entry below the diagonal must be the complex conjugate of the entry above it.

Why conjugate? A complex inner product already conjugates one of its arguments. The adjoint must respect that convention. If we used only the transpose for complex matrices, many of the geometric conclusions we want would fail.

Every diagonal entry of a Hermitian matrix is real, because a diagonal entry has to equal its own complex conjugate. But the off-diagonal entries can still be complex.

### Two small examples

First take the real two-by-two matrix whose first row is two, one, and whose second row is one, two. It is symmetric. Apply it to the vector with coordinates one, one. The result is three, three, so that vector has eigenvalue three. Apply it instead to one, negative one. The result is one, negative one, so that vector has eigenvalue one.

Notice two things. Both eigenvalues are real. And those two eigenvectors are perpendicular: their dot product is one minus one, which is zero.

Now take a genuinely complex example. Put two on both diagonal entries, put i in the upper-right corner, and negative i in the lower-left corner. Here i is the complex number whose square is negative one. This matrix is Hermitian because the lower-left entry is the conjugate of the upper-right entry.

Its vector with coordinates i, one is an eigenvector with eigenvalue three. You can verify this by multiplying. The first output is three i; the second is three. Its vector with coordinates negative i, one has eigenvalue one. These two vectors are orthogonal under the complex inner product, even though ordinary multiplication without conjugation would be misleading.

These examples illustrate the claims. Now let's prove the reasons.

### Why the eigenvalues must be real

Suppose A is self-adjoint, and a nonzero vector v satisfies A v equals lambda times v. We know lambda might initially be a complex number. We want to prove that it is real.

Look at the inner product of A v with v. Because A is self-adjoint, that number equals the inner product of v with A v. The two quantities are complex conjugates of each other, since swapping the arguments of an inner product conjugates its value. Therefore the inner product of A v with v equals its own conjugate. It is real.

But the eigenvector equation lets us evaluate the same number another way. It is lambda times the squared length of v, with the possible placement of the conjugation determined by which argument we chose to make linear. In the convention we are using, the coefficient appears as lambda in the inner product of A v with v.

The squared length of v is positive and real because v is not zero. If lambda times a positive real number is real, lambda itself must be real.

The proof is that short. The conclusion follows not from the size of the matrix or a characteristic-polynomial trick, but from how self-adjointness interacts with the inner product.

### Why different eigenspaces are perpendicular

Take two eigenvectors, v and w, with eigenvalues lambda and mu. Suppose the eigenvalues are different. We already know both numbers are real.

Compute the inner product of A v with w. The eigenvector equation says that this is lambda times the inner product of v with w.

Self-adjointness lets us move A to the other argument. The same expression becomes the inner product of v with A w. The second eigenvector equation makes this mu times the inner product of v with w.

So lambda times their inner product equals mu times their inner product. Subtract. The difference between lambda and mu, multiplied by their inner product, is zero.

Since the eigenvalues are different, that difference is nonzero. Therefore the inner product is zero. The eigenvectors are orthogonal.

This statement concerns *different* eigenvalues. Two arbitrary eigenvectors with the same eigenvalue need not be perpendicular. But within an eigenspace, we can use Gram–Schmidt to choose an orthonormal basis without changing the eigenvalue. Every linear combination of vectors in that eigenspace is still an eigenvector with that eigenvalue.

This is exactly what we need to combine different eigenspaces into one orthonormal collection.

### Why Jordan chains disappear

Consider the defective real matrix with first row two, one and second row zero, two. Let v be the horizontal unit vector and w the vertical unit vector. For eigenvalue lambda equal two, A minus lambda times the identity sends w to v and sends v to zero. Thus v is an eigenvector and w is a generalized eigenvector, forming a length-two Jordan chain.

Could such a chain exist for a self-adjoint matrix? No. Here is a short argument.

Write B for A minus lambda times the identity. Since lambda is real and A is self-adjoint, B is self-adjoint too. Assume B v equals zero and B w equals v.

Take the inner product of B w with v. Because B w equals v, this is the squared length of v, which is positive.

But self-adjointness lets us move B onto v. The same inner product is the inner product of w with B v. And B v is zero. So the result is zero.

That is a contradiction. The same number cannot be both positive and zero. Therefore the defective chain cannot exist.

This does not yet prove the entire spectral theorem, but it removes the phenomenon that made the previous example fail.

### A caution about the word symmetric

There are several meanings of symmetric in operator theory. For a finite-dimensional real matrix, being symmetric means being self-adjoint. For complex matrices, we say Hermitian or self-adjoint and use conjugate transpose.

Later, when we study unbounded operators on Hilbert spaces, we must distinguish a symmetric operator from a self-adjoint one. There, the domain on which an operator is defined matters, and symmetry alone may not give equality with the adjoint. That is a real mathematical distinction, not a terminological preference. We will develop it when we have the necessary domain theory.

For today's finite-dimensional matrices, no such domain difficulty arises. Every matrix acts on the entire coordinate space.

### What this gives us, and what remains

We have proved three important facts. A Hermitian matrix has real eigenvalues. Eigenvectors with distinct eigenvalues are orthogonal. And a nontrivial Jordan chain attached to an eigenvalue is impossible.

To obtain a full spectral decomposition, we also need enough orthogonal eigenvectors to span the space. The structural facts proved here give the orthogonality of eigenspaces, while existence of a complete eigenbasis requires an additional argument.

Three useful reconstructions are these. Show why the conjugate transpose, not the plain transpose, is the complex adjoint. Reproduce the proof that distinct eigenspaces are perpendicular. And explain exactly where the attempted Jordan chain contradicts self-adjointness.

These facts provide the ingredients for the finite spectral theorem: a self-adjoint matrix admits an orthonormal eigenbasis, so the operator is reconstructed from its eigenvalues and orthogonal spectral projections.

## The finite spectral theorem

Consider the symmetric two-by-two matrix whose diagonal entries are two and whose off-diagonal entries are one. The vector with equal coordinates points along an eigenvector of eigenvalue three. The vector with opposite coordinates is an eigenvector of eigenvalue one. Normalize them and they form a perpendicular pair spanning the plane.

Every vector can now be decomposed into these two directions. Applying the matrix simply multiplies one component by three and the other by one. That is what diagonalization accomplishes: the operator acts separately on orthogonal coordinates adapted to its own geometry.

The finite spectral theorem says that this calculation always works for a real symmetric or complex Hermitian matrix. We will explain why a maximizing direction for the Rayleigh quotient yields an eigenvector, why its orthogonal complement is invariant, and how induction supplies enough eigenvectors to span the whole space. Self-adjointness is the essential hypothesis; general square matrices may lack a complete eigenbasis.

### First, what would a spectral decomposition accomplish?

Imagine a room in which a transformation stretches one direction by three and a perpendicular direction by one. If you express a vector in those directions, the transformation is easy: multiply the first coordinate by three and leave the second alone.

An arbitrary matrix may mix coordinates. A self-adjoint matrix, we hope, has some orthonormal coordinates in which it stops mixing them.

An orthonormal basis of eigenvectors would do exactly that. Every vector x could be written as a sum of components along eigenvectors. The operator would act on each component by multiplying by that component's eigenvalue. Adding those scaled components would recover A x.

That is the spectral theorem in its most useful finite-dimensional form. Let's prove the existence of the basis rather than assuming it.

### Finding one eigenvector

We'll work first over the complex numbers. Let A be a self-adjoint operator on a nonzero finite-dimensional complex inner-product space.

The characteristic polynomial has positive degree. The fundamental theorem of algebra says that it has at least one complex root. If lambda is a root of the characteristic polynomial of a finite matrix A, then A minus lambda times the identity is singular. Its kernel therefore contains a nonzero eigenvector. So choose an eigenvalue lambda and a unit eigenvector v.

Since A is self-adjoint, lambda is real. This matters because the restriction of A to the directions perpendicular to v will remain self-adjoint.

We know one good direction. How can we find the rest without interfering with it?

### The perpendicular complement stays closed under A

Consider the subspace of all vectors perpendicular to v. Take any vector w in that subspace. Its inner product with v is zero.

We want to show that A w is also perpendicular to v. Move A across the inner product using self-adjointness. The inner product of A w with v equals the inner product of w with A v. Because v is an eigenvector, A v is lambda times v. The result is therefore lambda times the inner product of w with v, which is zero.

So A sends every vector perpendicular to v back into the same perpendicular subspace.

This is the reducing-subspace idea, now doing concrete proof work. We have split the space into the line along v and its orthogonal complement. And A respects both pieces.

The orthogonal complement has dimension one less than the original space. The restriction of A to that complement is still self-adjoint, because its inner products are computed using the same rule as before.

We have therefore reduced our problem to a smaller problem of the same kind.

### Induction gives an orthonormal eigenbasis

In a one-dimensional space, the theorem is immediate. Every linear operator is multiplication by one scalar in the sole unit direction, and self-adjointness makes that scalar real.

Assume the theorem works in dimension one less than our current space. We already chose one unit eigenvector v, and we just proved that its perpendicular complement is invariant and carries a self-adjoint restriction.

By the inductive hypothesis, the complement has an orthonormal eigenbasis for that restriction. Put v together with that basis. Because every vector in the complement is perpendicular to v, the combined list is orthonormal. Because the line along v and its complement fill the space, the list is a basis. And every vector on the list is an eigenvector of A.

We have proved the theorem for the next dimension, and therefore for every finite dimension.

The proof proceeds by induction: existence of an eigenvalue gives an eigenvector; self-adjointness makes its perpendicular complement invariant; and the argument repeats in smaller dimension. This is why self-adjointness gives more than merely real eigenvalues: it permits the reduction that makes the induction work.

### What about real symmetric matrices?

We used the fundamental theorem of algebra over the complex numbers, but a real symmetric matrix should have a real orthonormal eigenbasis too.

View a real symmetric matrix as a complex Hermitian matrix. The complex proof gives an eigenvalue. Because a Hermitian operator satisfies the identity that the inner product of A v with v is real, any eigenvalue at a nonzero eigenvector must be real.

Write a corresponding complex eigenvector as its real part plus i times its imaginary part. Because the matrix and eigenvalue are real, comparing real and imaginary parts shows that each part separately satisfies the same eigenvector equation. At least one part is nonzero, since the complex eigenvector is nonzero.

Thus a real symmetric matrix has a nonzero real eigenvector. Repeat the perpendicular-complement induction entirely over the real numbers. That proves the real theorem without secretly treating complex vectors as a real orthonormal basis.

### From eigenvectors to projections

Let's make the result independent of a particular choice of basis.

For each *distinct* eigenvalue lambda, gather all eigenvectors with that eigenvalue, along with zero, into its eigenspace. Let P lambda mean orthogonal projection onto that eigenspace.

Distinct eigenspaces are orthogonal: self-adjointness equates lambda times the inner product of two eigenvectors with mu times that inner product, forcing it to vanish when lambda and mu differ. Their direct sum is the entire space, by the spectral theorem we just proved.

That gives three properties. First, each P lambda is an orthogonal projection, so applying it twice is the same as applying it once. Second, projections for distinct eigenvalues annihilate one another: a vector lying in one eigenspace has no component in a different one. Third, adding all these spectral projections gives the identity operator, because every vector is the sum of its spectral components.

The operator A itself is the sum of lambda times P lambda over the distinct eigenvalues. To see why, apply both sides to an arbitrary vector. Every projection extracts one eigenspace component, and multiplying it by lambda is exactly how A acts on that component.

That is the spectral decomposition.

### A two-dimensional calculation

Let's use our real symmetric example: the matrix with rows two, one and one, two.

The line along the vector one, one has eigenvalue three. The line along one, negative one has eigenvalue one. Normalize each vector by dividing by the square root of two.

Projection onto the first line takes a vector, measures its component along that normalized direction, and returns exactly that component. Its matrix has one half in every entry.

Projection onto the second line has one half on the diagonal and negative one half off the diagonal.

Add the two projection matrices. Their off-diagonal entries cancel and the diagonal entries add to one. We get the identity.

Now multiply the first projection by three and add the second projection once. The diagonal entries become two; the off-diagonal entries become one. We recover the original matrix exactly.

There is no approximation here. The projections split the operator into separate pieces, each carrying one eigenvalue.

### What happens when an eigenvalue repeats?

Suppose an eigenvalue occurs twice. Its eigenspace may be a plane. We could choose one pair of perpendicular unit vectors in that plane, or rotate that pair and choose another. Both give valid eigenbases.

But the plane itself has not changed. Its orthogonal projection has not changed either.

This is why it is often more informative to speak of a spectral subspace and its projection than to insist on a particular eigenvector. The projection records the whole component associated with the eigenvalue, without making an arbitrary coordinate choice inside it.

For any selected cluster of eigenvalues, the projection onto the sum of their eigenspaces captures the geometry of the cluster.

### What the theorem does not say

Today's theorem is finite-dimensional and assumes self-adjointness. General matrices may fail to have a basis of eigenvectors. General bounded self-adjoint operators on infinite-dimensional spaces need not have an eigenbasis either, because the spectrum may contain values that are not eigenvalues.

We will eventually replace finite sums over eigenvalues by integration with respect to projection-valued measures. That is not a minor change of notation; it requires new mathematics, which we will build later.

For now, the finite theorem is a complete result in its setting.

### Reconstructing the theorem

Try to reproduce the induction without looking back. Where does the first eigenvector come from? Why does the perpendicular complement stay invariant? What makes the restricted operator self-adjoint? And how do we know the pieces span the original space?

Then reconstruct the two-by-two example from its two spectral projections. Explain why changing the eigenbasis within a repeated eigenspace does not change its projection.

That question leads to Rayleigh quotients, and eventually to the variational theory of eigenvalues.

## Rayleigh quotients and extrema

Take a diagonal matrix with eigenvalues one and four. A unit vector making an angle theta with the first coordinate axis has coordinates cosine theta and sine theta. Its quadratic measurement under the matrix is one times cosine squared theta plus four times sine squared theta, or one plus three times sine squared theta.

At theta equal to zero, the measurement is one. At ninety degrees it is four. At intermediate angles it lies between the eigenvalues, and changing the vector changes the weighted average. This is the Rayleigh quotient for unit vectors. For a nonunit vector we divide the same quadratic form by its squared length to remove the effect of scaling.

The extremal values recover the smallest and largest eigenvalues of a self-adjoint matrix. But a Rayleigh quotient alone does not identify an eigenvector unless its value attains a suitable extremum or we have additional information. We will derive the weighted-average formula from the spectral theorem, use it to prove the extrema, and then explain why the same variational viewpoint supports eigenvalue approximation on subspaces.

### What does the quotient measure?

Start with a real two-dimensional vector. A x may point in a different direction from x. If we take the dot product of A x with x, we keep only the component of A x aligned with x, weighted by the length of x.

Dividing by the squared length makes the result independent of scale. Replace x by twice x. The numerator becomes four times as large, and so does the denominator. The quotient stays the same. We are measuring a property of the *direction*, not of the particular length of the vector.

Over the complex numbers we use the complex inner product. For self-adjoint A, this quadratic form is real, because self-adjointness makes the quadratic form equal to its own complex conjugate. So we can compare Rayleigh quotients using ordinary inequalities on real numbers.

If x is an eigenvector with eigenvalue lambda, then A x equals lambda times x. Its Rayleigh quotient is exactly lambda. Every eigenvector direction therefore gives one of the operator's eigenvalues.

What about a vector that is not an eigenvector? Its quotient still exists, but it does not generally equal an eigenvalue. Let's calculate one.

### A rotating direction between two eigenvectors

Take the symmetric matrix with rows two, one and one, two. Its eigenvalues are three and one: the characteristic polynomial is lambda squared minus four lambda plus three, which factors as lambda minus one times lambda minus three. Its normalized eigenvectors point along one, one and one, negative one.

Any unit vector in the plane can be written as cosine theta in the horizontal direction and sine theta in the vertical direction. Apply the matrix to that vector, then take the dot product with the original vector.

The calculation gives two plus twice cosine theta times sine theta. The double-angle identity turns this into two plus sine of two theta.

So as the direction moves around the unit circle, its Rayleigh quotient varies smoothly between one and three. It reaches three along the eigenvector with equal coordinates, and one along the eigenvector with opposite coordinates. In between, most directions give numbers that are not eigenvalues.

For example, along the horizontal axis the quotient is two. But two is not an eigenvalue of this matrix. The quotient records the quadratic form on a direction, not a claim that the direction is invariant.

We can now see the first major result: the smallest and largest eigenvalues are exactly the smallest and largest possible Rayleigh quotients.

### Why the extremes equal eigenvalues

Let A have orthonormal eigenvectors e one through e n, with real eigenvalues lambda one through lambda n. We may arrange the eigenvalues from smallest to largest for this argument.

Write any vector x as a sum of coefficients times those eigenvectors. Because the basis is orthonormal, the squared length of x is the sum of the squared magnitudes of its coefficients.

Apply A to x. It multiplies each coefficient by the corresponding eigenvalue. Taking the inner product with x gives the sum of each eigenvalue times that coefficient's squared magnitude.

Now divide by the squared length of x. The result is a weighted average of the eigenvalues. Every weight is nonnegative, and all the weights add up to one.

A weighted average cannot fall below the smallest number being averaged or rise above the largest. Therefore every Rayleigh quotient lies between the smallest and largest eigenvalues.

And these bounds are attained: choose an eigenvector for the smallest eigenvalue or an eigenvector for the largest. Its quotient is that eigenvalue.

So the minimum Rayleigh quotient equals the smallest eigenvalue, and the maximum equals the largest eigenvalue.

This proof also tells us about equality. The quotient reaches the largest eigenvalue only when all of the vector's nonzero components belong to eigenspaces carrying that largest eigenvalue. If the top eigenvalue repeats, the maximum occurs on an entire eigenspace, not just along one selected line.

### Why a weighted average is not the whole story

Our weighted-average formula gives the global extremes immediately. But it also invites a sharper question. What if the Rayleigh quotient stops changing at some direction that is neither a maximum nor a minimum?

Could that direction still be an eigenvector? Yes. In a three-dimensional example with three distinct eigenvalues, a middle eigenvector produces a stationary value. Moving in some directions raises the quotient; moving in others lowers it.

So stationary does not always mean maximum or minimum. We need a separate argument connecting stationary directions with the eigenvalue equation.

### Deriving the stationary-point condition

We can investigate small changes using calculus. Let x be any nonzero vector, and choose another vector h describing a possible direction of motion. Replace x by x plus t times h, where t is a small real number.

The Rayleigh quotient has a numerator, the inner product of A x with x, and a denominator, the squared length of x. Differentiate the numerator at t equals zero. Self-adjointness makes its derivative twice the real part of the inner product of A x with h.

Differentiate the denominator. Its derivative is twice the real part of the inner product of x with h.

The quotient rule now says that the derivative is twice, divided by the squared length of x, times the real part of the inner product of A x minus the Rayleigh quotient times x, with h.

Focus on the vector inside that inner product: A x minus R of x times x. It is the failure of x to satisfy the eigenvector equation with candidate eigenvalue R of x. In other words, it is an eigenvector residual.

If x is an eigenvector, this residual is zero, so every directional derivative is zero.

Conversely, suppose the quotient is stationary under every small change of x. The derivative must be zero for every h. Choose h to be the residual itself. The derivative becomes twice the squared length of the residual, divided by the squared length of x. That can be zero only when the residual is zero.

Therefore a nonzero direction is stationary for the Rayleigh quotient exactly when it is an eigenvector direction.

This is a genuine connection between calculus and spectral theory. The eigenvalue equation emerges as the condition that a quadratic ratio has no first-order change.

### How does this relate to Rayleigh–Ritz?

Earlier we constructed the Rayleigh–Ritz compression of an operator to a trial subspace. For an orthonormal coordinate embedding V, the compressed matrix is V star A V.

If we take a coordinate vector c in that trial space, its compressed Rayleigh quotient equals the ambient Rayleigh quotient of V c. This follows because V preserves lengths and because the adjoint transfers the inner product back into trial coordinates.

Thus the Ritz values are the stationary values of the Rayleigh quotient when we restrict ourselves to directions lying inside the trial subspace.

But restricted stationarity is weaker than stationarity in the whole ambient space. A vector may be optimal within the trial space while the operator still pushes part of it outside. That outside component is exactly what the Ritz residual records.

So we now see a useful distinction. A Rayleigh quotient measures one direction's quadratic form. A Ritz value is a stationary value under directions available in a trial subspace. An actual eigenvalue comes with stationarity under all directions in the ambient space.

### Why we are not finished with variational theory

The smallest and largest eigenvalues are easy to recover by optimizing over all unit vectors. But how could we recover the second-largest eigenvalue, or the fifth? Simply searching for a second-highest value makes no sense: we can approach the largest eigenvector as closely as we like and get quotient values arbitrarily close to the maximum.

The answer will involve optimization over *subspaces*, not just individual vectors. We will ask what happens if we have to choose a whole subspace of a specified dimension, and then face the worst direction inside it. That is the idea behind the Courant–Fischer min–max theorem.


For now, reconstruct these three steps. First, write the Rayleigh quotient as a weighted average of eigenvalues. Second, prove why its endpoints are attained exactly on the extreme eigenspaces. Third, follow the directional derivative until the eigenvector residual appears, and explain why choosing the variation equal to that residual completes the proof.

We now have a bridge from spectral decomposition to optimization.

## Courant–Fischer min–max: finding every eigenvalue by geometry

Take a diagonal three-by-three matrix with eigenvalues one, three, and seven. Its smallest eigenvalue is easy to obtain by minimizing the Rayleigh quotient over unit vectors. Its largest is obtained by maximizing. But how can we locate the middle eigenvalue using a rule that makes no reference to coordinates or a characteristic polynomial?

Choose a plane in the three-dimensional space and ask for the largest Rayleigh quotient among unit vectors in that plane. The plane spanned by the first two eigenvectors has largest quotient three. Any two-dimensional plane must intersect the plane spanned by the last two eigenvectors in a nonzero direction, where the quotient is at least three. So the smallest achievable maximum over all planes is exactly three.

That is a concrete min–max principle. The Courant–Fischer theorem generalizes it to every ordered eigenvalue, with a choice of subspace dimension and an inner optimization. We will prove the dimension-intersection argument and explain why reversing min and max requires changing the dimension. This formula is the starting point for many eigenvalue inequalities and numerical approximations.

### Why simply finding the second-best vector fails

Start with a three-dimensional real symmetric matrix having eigenvalues five, two, and negative one. Imagine its three perpendicular unit eigenvectors. In the direction of the first, the Rayleigh quotient is five. In the second, it is two. In the third, it is negative one.

Could we get the second eigenvalue by asking for the largest Rayleigh quotient among vectors that are not the top eigenvector? No. We can choose vectors almost parallel to the top eigenvector. Their quotients are arbitrarily close to five. Excluding one line does not make two the new maximum.

One way out would be to forbid every component along the top eigenvector. Then the maximum over its perpendicular plane is two. That works, but it assumes we already know the top eigenvector. We want a characterization that does not require it.

Instead, we will let someone choose a plane, ask what the smallest Rayleigh quotient in that plane must be, and then choose the plane with the best possible worst case.

### An experiment with planes

Stay in three dimensions. Every plane through the origin contains many directions. The Rayleigh quotient will usually vary as we move around those directions.

If the plane is spanned by the eigenvectors for five and two, every unit vector in it has a quotient between two and five. Its smallest quotient is exactly two.

What if we choose another plane? Here is the important observation: every plane through the origin intersects the plane spanned by the eigenvectors for two and negative one along at least one nonzero direction. Along that second plane, the quotient is never greater than two. Therefore our chosen plane contains at least one direction whose quotient is at most two.

No plane can make its worst direction better than two. And we already found a plane whose worst direction achieves two. So the best possible worst Rayleigh quotient among two-dimensional planes is exactly the middle eigenvalue, two.

The expression “best possible worst case” is the max–min construction: choose a subspace to maximize the minimum Rayleigh quotient inside it.

### Why two planes must intersect

Let's justify the geometric step rather than simply assert it.

A plane through the origin in three-dimensional space has two independent directions. Two such planes would have four independent directions between them if they shared nothing except zero. But the ambient space has room for only three independent directions. So they must share a nonzero vector.

In general, suppose a space has dimension n, while two subspaces have dimensions p and q. If their intersection were only zero, we could combine a basis from each to get p plus q independent vectors. That is impossible when p plus q exceeds n.

More precisely, the dimension of their intersection is at least p plus q minus n. We need only the consequence: when their dimensions add to more than n, the intersection contains a nonzero vector.

The proof of Courant–Fischer repeatedly uses this fact to force an arbitrary subspace to meet a carefully chosen spectral subspace.

### The general max–min formula

Take an n-dimensional real or complex inner-product space and a self-adjoint operator A. List its eigenvalues from largest to smallest, counting repetitions: lambda one, lambda two, through lambda n.

Pick an index k, somewhere between one and n. Consider every subspace of dimension k. For each subspace, find the smallest Rayleigh quotient among its unit vectors. Then take the largest of those smallest values over all choices of the subspace.

Courant–Fischer says the result is lambda k.

Let's prove both directions of that equality.

First, choose the particular k-dimensional subspace spanned by eigenvectors one through k. On this subspace, the quotient is a weighted average of the first k eigenvalues. Its minimum is lambda k, achieved by the kth eigenvector. So the max–min value is at least lambda k.

Second, let someone choose any other k-dimensional subspace V. Look at the spectral subspace spanned by eigenvectors k through n. Its dimension is n minus k plus one. The dimensions of these two subspaces add to n plus one. Their intersection therefore contains a nonzero vector.

Normalize a vector from that intersection. Because it lies in the trailing spectral subspace, its Rayleigh quotient is a weighted average of lambda k and the smaller eigenvalues. So its quotient cannot exceed lambda k.

Since this vector lies in V, the minimum quotient in V is at most lambda k. This holds for every k-dimensional V. So even the best choice of V has minimum at most lambda k.

We have both inequalities. The max–min value equals lambda k.

Notice that nothing depended on choosing a particular basis inside a repeated eigenspace. The proof used the dimensions and the invariant subspaces. Those are geometric properties of the operator.

### Turning the order around

There is a companion formula, sometimes called the min–max form. Instead of choosing a k-dimensional subspace and maximizing its minimum, choose a subspace of dimension n minus k plus one and minimize its maximum Rayleigh quotient.

Why should that also give lambda k?

Take the trailing spectral subspace, spanned by eigenvectors k through n. Its maximum quotient is lambda k. So the min–max value cannot be greater than lambda k.

Now let someone choose any subspace of that same dimension. It must intersect the leading spectral subspace, spanned by eigenvectors one through k, because their dimensions again add to n plus one. A unit vector in the intersection has a quotient at least lambda k. Hence the maximum quotient in the chosen subspace is at least lambda k.

The best attempt to make that maximum small cannot push it below lambda k. The min–max value therefore also equals lambda k.

These are two symmetric ways of locating the same eigenvalue: maximize the minimum on a k-dimensional subspace, or minimize the maximum on a complementary-sized subspace.

### Why multiplicities do not break the argument

Suppose the second and third eigenvalues are both two. Their eigenvectors span a two-dimensional eigenspace, and we may rotate our orthonormal basis inside it. Nothing changes in either variational expression.

Our statements use eigenvalues with multiplicity and the *dimensions* of chosen subspaces. They do not require us to pick a unique second or third eigenvector.

This feature becomes important when a numerical calculation gives us an approximate subspace but not a uniquely aligned list of eigenvectors.

### A first consequence for trial spaces

Remember the Rayleigh–Ritz construction. We restricted an operator to a smaller trial subspace and obtained a compressed self-adjoint matrix. Every quotient in that compressed problem is an ambient Rayleigh quotient evaluated on a vector from the trial subspace.

The min–max theorem therefore gives a direct route to comparing Ritz values with the full operator's eigenvalues. We can optimize inside fewer available directions, and the constraint changes what maxima and minima are possible. The min–max principle supplies the precise comparison.

For now, the essential result is complete. We can recover every sorted eigenvalue by a competition between choosing subspaces and choosing directions inside them.

Try reconstructing the middle-eigenvalue example in three dimensions without formulas. Then explain why two subspaces whose dimensions add to more than the ambient dimension must intersect. Finally, repeat the two halves of the general proof, carefully identifying which spectral subspace produces the upper bound and which one attains equality.

The min-max characterization allows eigenvalue comparisons of different self-adjoint matrices without requiring their eigenvectors to align.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Eigenvalues, eigenspaces, and algebraic multiplicity

### Eigenvalues, eigenspaces, and algebraic multiplicity

---

#### Companion: mathematical facts and Lean correspondence (display only)

For \(A:\mathbb K^n\to\mathbb K^n\), \(\lambda\) is an eigenvalue iff \(\ker(A-\lambda I)\ne\{0\}\), equivalently \(\det(\lambda I-A)=0\). The algebraic multiplicity of \(\lambda\) is its multiplicity as a root of \(\chi_A(t)=\det(tI-A)\); its geometric multiplicity is \(\dim\ker(A-\lambda I)\). An adapted basis gives \(\chi_A(t)=(t-\lambda)^k q(t)\) where \(k\) is geometric multiplicity, hence \(k\) does not exceed algebraic multiplicity.

For example, \(A=\begin{pmatrix}2&1\\0&2\end{pmatrix}\) has \(\chi_A(t)=(t-2)^2\), but \(\ker(A-2I)=\operatorname{span}\{(1,0)\}\). The generalized vector \((0,1)\) satisfies \((A-2I)^2(0,1)=0\) but \((A-2I)(0,1)\ne0\).

**Lean bridge.** A later DKPS theorem uses Mathlib's characteristic-polynomial API to compare the polynomial under an equivalence of coordinate order. The following is an exact excerpt from `DavisKahan/FiniteDimensional/DirectRotation/RealFourSpectrum.lean`:

```lean
theorem charpoly_fourTransport (t u a b e f : ℝ) :
    (fourTransport ![t, u] a b e f).charpoly =
      (fourTransportMatrix t u a b e f).charpoly := by
  rw [← fourTransportMatrix_submatrix]
  exact Matrix.charpoly_reindex finSumFinEquiv.symm _
```

`Matrix.charpoly` is the characteristic polynomial of a square matrix. `Matrix.charpoly_reindex` expresses its invariance under reindexing rows and columns by the same equivalence. The displayed theorem concerns a later four-dimensional rotation construction; the present lecture teaches the linear-algebra principle that makes such a step valid. `finSumFinEquiv` reorganizes two pairs of coordinates into four coordinates. This is not offered as a Lean proof of the general geometric/algebraic multiplicity inequality; that theorem's companion will be identified when its exact source declaration is audited. The excerpt was verified against the supplied source snapshot; no new Lean code was compiled.

### Hermitian and self-adjoint matrices

### Hermitian and self-adjoint matrices

---

#### Companion: mathematical facts and Lean correspondence (display only)

##### Equal eigenvalue multiplicity, different eigenspaces

Compare
\[
D=\begin{pmatrix}2&0\\0&2\end{pmatrix},\qquad
J=\begin{pmatrix}2&1\\0&2\end{pmatrix}.
\]
Both characteristic polynomials are \((t-2)^2\), but
\(\ker(D-2I)=\mathbb R^2\), while
\(\ker(J-2I)=\operatorname{span}\{e_1\}\). Therefore algebraic
multiplicity is two in both cases, whereas geometric multiplicity
is two for \(D\) and one for \(J\).

For a matrix over \(\mathbb C\), Hermitian means \(A=A^*\), where \(A^*=\overline A^{\mathsf T}\). If \(Av=\lambda v\) with \(v\ne0\), then
\[
\langle Av,v\rangle=\lambda\|v\|^2\in\mathbb R
\quad\Longrightarrow\quad\lambda\in\mathbb R.
\]
If \(Av=\lambda v\) and \(Aw=\mu w\), with \(\lambda\ne\mu\), then \((\lambda-\mu)\langle v,w\rangle=0\). The nonzero Jordan-chain contradiction is \(\|v\|^2=\langle (A-\lambda I)w,v\rangle=\langle w,(A-\lambda I)v\rangle=0\).

**Lean bridge.** The project uses both `Matrix.IsHermitian` for finite matrices and `IsSelfAdjoint` for bounded or domain-aware operators. This is an exact excerpt from `ForTauCeti/Analysis/InnerProductSpace/CompactApproximationEigenvalues.lean`:

```lean
theorem eq_ofReal_re_of_eigenspace_ne_bot (hAs : IsSelfAdjoint A)
    (hApos : ∀ x, 0 ≤ RCLike.re ⟪A x, x⟫_𝕜) {μ : 𝕜}
    (h : eigenspace A.toLinearMap μ ≠ ⊥) :
    μ = ((RCLike.re μ : ℝ) : 𝕜) ∧ 0 ≤ RCLike.re μ := by
```

The theorem's conclusion says an eigenvalue of a **positive** self-adjoint operator is real and nonnegative. `hAs` encodes self-adjointness; `hApos` supplies positivity; `eigenspace ... ≠ ⊥` asserts a nonzero eigenspace. The displayed source continues by using `conj_eigenvalue_eq_self` for reality and a separate positivity argument for nonnegativity. This is stronger than the reality fact taught today, and its nonnegativity portion will be developed in the positive-operator unit. The excerpt is an exact declaration prefix, not a standalone proof. The mathematical result belongs to the DKPS development regardless of later upstream location.

### The finite spectral theorem

### The finite spectral theorem

---

#### Companion: mathematical facts and Lean correspondence (display only)

For a finite-dimensional real or complex inner-product space and self-adjoint \(A\), there is an orthonormal eigenbasis. Let \(\Lambda\) be the set of **distinct** eigenvalues and \(P_\lambda\) the orthogonal projector onto the corresponding eigenspace. Then
\[
P_\lambda^*=P_\lambda=P_\lambda^2,\quad
P_\lambda P_\mu=0\ (\lambda\neq\mu),\quad
\sum_{\lambda\in\Lambda}P_\lambda=I,\quad
A=\sum_{\lambda\in\Lambda}\lambda P_\lambda.
\]

**Lean bridge.** The DKPS-developed `ForTauCeti/LinearAlgebra/Matrix/PosDef.lean` proves an entrywise form of `Matrix.IsHermitian.spectral_theorem`:

```lean
theorem isHermitian_entry_eq_sum_eigenvalues
    (B : Matrix (Fin n) (Fin n) 𝕜) (hB : B.IsHermitian) (i j : Fin n) :
    B i j = ∑ k : Fin n,
      (hB.eigenvalues k : 𝕜) * (hB.eigenvectorUnitary i k) *
        conj (hB.eigenvectorUnitary j k) := by
  have hspec := hB.spectral_theorem
```

`hB` is the Hermitian hypothesis; `eigenvectorUnitary` supplies orthonormal eigenvector coordinates and `eigenvalues` lists eigenvalues **with multiplicity**, unlike the distinct-eigenvalue indexing of the projector formula above. The sum is the entrywise expansion of \(B=UDU^*\). The source then expands this matrix product into the displayed sum. Our spoken proof constructs the basis inductively; the Lean development reuses Mathlib's spectral theorem and proves a useful representation of its conclusion. The quoted lines are an exact source prefix, not a new independent Lean proof.

### Rayleigh quotients and extrema

### Rayleigh quotients and extrema

---

#### Companion: mathematical facts and Lean correspondence (display only)

For nonzero \(x\) and finite-dimensional self-adjoint \(A\), define the real Rayleigh quotient
\[
R_A(x)=\frac{\langle Ax,x\rangle}{\langle x,x\rangle}.
\]
If \(x=\sum_j c_je_j\) in an orthonormal eigenbasis, then
\[
R_A(x)=\frac{\sum_j\lambda_j|c_j|^2}{\sum_j|c_j|^2}
\in[\lambda_{\min},\lambda_{\max}].
\]
For real \(t\), the directional derivative is
\[
\left.\frac{d}{dt}R_A(x+th)\right|_{t=0}
=\frac{2\operatorname{Re}\langle (A-R_A(x)I)x,h\rangle}{\|x\|^2}.
\]
Stationarity for every real direction \(h\) is equivalent to \((A-R_A(x)I)x=0\). The same conclusion applies over \(\mathbb C\) by treating directional variations as real-parameter curves.

**Lean bridge.** The pre-existing DKPS lecture companion `visualizations/lectures/002666_minmax/facts.lean` uses the accepted TauCeti Courant–Fischer API in an exact theorem example:

```lean
example : hT.eigenvalues hn k =
    ⨆ V : {V : Submodule ℝ E //
        finrank ℝ V = (k : ℕ) + 1},
      ⨅ x : {x : E //
          x ∈ (V : Submodule ℝ E) ∧ ‖x‖ = 1},
        RCLike.re ⟪T (x : E), (x : E)⟫_ℝ :=
  hT.eigenvalues_eq_iSup_iInf_re_inner hn k
```

Here `T` is a continuous self-adjoint operator over a finite-dimensional real Hilbert space, `hT` is its symmetry proof, and `hT.eigenvalues hn k` selects a sorted eigenvalue. The expression `RCLike.re ⟪T x,x⟫_ℝ` is the Rayleigh numerator; the vector hypothesis `‖x‖ = 1` makes the denominator one. The indexed supremum and infimum encode the more sophisticated subspace optimization to be proved in `028000`. This companion shows exactly where today's quotient enters the actual Lean theorem, without claiming that the displayed min–max theorem was proved in this lecture. The source lives in the DKPS lecture tree and imports the accepted TauCeti theorem; as in the provenance census, its current import location does not by itself identify the theorem's original donor history.

### Courant–Fischer min–max: finding every eigenvalue by geometry

### Courant–Fischer min–max: finding every eigenvalue by geometry

---

#### Companion: mathematical facts and Lean correspondence (display only)

Let \(A=A^*\) on an \(n\)-dimensional real or complex Hilbert space, with eigenvalues \(\lambda_1\ge\cdots\ge\lambda_n\), counted with multiplicity. For \(x\ne0\), \(R_A(x)=\langle Ax,x\rangle/\|x\|^2\). Then, for \(1\le k\le n\),

\[
\lambda_k
=\max_{\dim V=k}\;\min_{\substack{x\in V\\\|x\|=1}}R_A(x)
=\min_{\dim W=n-k+1}\;\max_{\substack{x\in W\\\|x\|=1}}R_A(x).
\]

The key geometric lemma is \(\dim(U\cap V)\ge\dim U+\dim V-n\). With \(V\) arbitrary of dimension \(k\), intersect it with \(\operatorname{span}(e_k,\dots,e_n)\); with \(W\) arbitrary of dimension \(n-k+1\), intersect it with \(\operatorname{span}(e_1,\dots,e_k)\). No distinct-eigenvalue hypothesis is needed.

**Lean bridge.** `visualizations/lectures/002666_minmax/facts.lean` gives the following exact application of the accepted TauCeti min–max API (the index `k : Fin n` is zero-based):

```lean
example : hT.eigenvalues hn k =
    ⨆ V : {V : Submodule ℝ E //
        finrank ℝ V = (k : ℕ) + 1},
      ⨅ x : {x : E //
          x ∈ (V : Submodule ℝ E) ∧ ‖x‖ = 1},
        RCLike.re ⟪T (x : E), (x : E)⟫_ℝ :=
  hT.eigenvalues_eq_iSup_iInf_re_inner hn k
```

`Submodule ℝ E` is a real linear subspace, `finrank` is its dimension, and the dependent subtype after `//` carries the dimension or unit-vector requirement. `⨆` and `⨅` are indexed supremum and infimum, not computational loops; for the finite-dimensional setting they express the extrema proved above. The statement in this source is real-scalar; the spoken proof also applies to complex self-adjoint operators. The matching mathematics was developed in the DKPS project and moved into the TauCeti library; importing it from TauCeti does not make it external to this course's proof obligations. The Lean sample invokes the theorem rather than reproducing its proof term, which is why the transcript supplies the geometric proof.
