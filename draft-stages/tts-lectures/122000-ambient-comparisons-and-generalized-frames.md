# Ambient comparisons and generalized frames

<!-- BEGIN SPOKEN LECTURE -->

# Ambient comparisons and generalized frames

## Direct-sum norm comparison

An estimate for one corner of a block matrix is often the easy part of a perturbation proof. A full angle between subspaces has two complementary corners. How can we combine bounds for the two corners without losing a constant or miscounting singular values?

Davis and Kahan answer this with Lemma six point one. Its basic operation is an orthogonal direct sum. When the two summands act on orthogonal initial spaces and have orthogonal output spaces, their singular values merge into a single ordered list. That list admits a precise Ky Fan comparison.

We will prove the finite-dimensional formula directly, then explain the weak-majorization argument, the converse under matching singular values, and the operator-ideal qualifications in Hilbert space.

### Begin with ordinary diagonal matrices

Take a matrix A with singular values five and two, and a matrix B with singular values four and one. Form their block direct sum. Its nonzero singular values are five, four, two, and one, in decreasing order.

The first Ky Fan sum is five. The second is nine. The third is eleven. The fourth is twelve.

The point is that the direct sum has a combined singular-value list, not the termwise sum of two lists. In particular, the second Ky Fan sum is not the second Ky Fan sum of A plus the second Ky Fan sum of B: that would give seven plus five, or twelve, while the correct second prefix is nine.

To get the first two singular values of the direct sum, we choose how many to take from each block. We might take two from A, none from B, or one from each, or none from A and two from B. The largest sum among those choices is nine.

### Prove the exact prefix formula

Let the singular values of A decrease as a one, a two, and so on. Let those of B decrease as b one, b two, and so on. Include trailing zeros after the rank if needed.

For a fixed positive integer k, the sum of the k largest singular values of their direct sum is the maximum, over all splits of k into i plus j, of the sum of the i largest a values and the sum of the j largest b values.

Why is this formula exact? Every choice of k entries from the merged list takes some number i from the first block and j from the second. For that split, the largest possible selected sum uses the first i values of A and the first j values of B. Conversely, those leading entries are a valid selection from the union, so their sum never exceeds the largest k-entry sum of the union.

Taking the maximum over splits proves both inequalities. This is the Ky Fan direct-sum formula.

The same proof works in finite dimensions when one block is rectangular. Singular values depend on the map, not on whether its matrix is square. Adding zero dimensions for the direct sum does not alter the nonzero singular-value list.

### Derive the forward comparison

Suppose every Ky Fan prefix of A is at most the corresponding prefix of C. Suppose also every Ky Fan prefix of B is at most the corresponding prefix of D.

For every split k equal to i plus j, the sum of the first i singular values of A and the first j of B is at most the analogous sum for C and D. Taking the maximum over all splits preserves the inequality.

Thus every Ky Fan prefix of A direct sum B is at most the corresponding prefix of C direct sum D.

This is exactly a weak-majorization statement for the merged singular-value sequences. It is stronger than a comparison for one selected Schatten norm. It says that every leading partial sum is controlled.

By the symmetric-gauge dominance principles established earlier, the weak-majorization conclusion yields a bound in every applicable unitarily invariant norm. In an infinite-dimensional ideal, it can also imply membership, provided the chosen ideal has the required dominance property and the comparison operator belongs to the ideal.

### Why orthogonality matters

Consider two operators whose ranges overlap and whose domains overlap. Their sum may have cancellations or reinforcing interference. The singular values of the sum need not be the merged lists of their individual singular values.

For the direct-sum formula we need the operator to be block diagonal after suitable orthogonal coordinate changes. More precisely, the first block must act on an initial subspace orthogonal to the second block's initial subspace, and their images must lie in orthogonal final subspaces.

Under those conditions, the Gram operator of the sum is block diagonal in the initial-space coordinates. Its positive square root therefore has the two block moduli on the diagonal. The union of singular values follows directly.

In the Davis–Kahan setting, projection blocks have exactly this structure. One block maps the source subspace into the target subspace. Its complementary partner maps the orthogonal source complement into the orthogonal target complement. Their sum is isometrically equivalent to a true block direct sum.

One can describe a cross-block map either by compressing between the actual subspaces or by inserting the corresponding ambient projections. These are operators with different source and target spaces. Their nonzero singular values agree by an explicit isometric identification; they should not be equated as typed operators.

### The converse requires a symmetry

Can we infer separate bounds on A from a Ky Fan bound for A direct sum B? Not in general. The second block might carry the entire improvement or entire loss, making the combined comparison uninformative about the first block.

There is an important exception. Suppose A and B have identical singular-value sequences, and C and D also have identical singular-value sequences. Then the merged singular values of A direct sum B consist of each singular value of A repeated twice. The same holds for C direct sum D.

Therefore the sum of the first two k singular values of A direct sum B is exactly twice the sum of the first k singular values of A. This can be checked from the merged list, or from the prefix formula by showing that a balanced split maximizes the sum of two decreasing-prefix functions.

If all Ky Fan sums of the direct sum on the left are at most those of the direct sum on the right, apply the inequality at even index two k and divide by two. We recover the Ky Fan bound for A versus C.

That is the converse direction in Lemma six point one. Its matching-singular-value hypothesis is essential; without it, the even-prefix identity is false.

### A concrete converse example

Let A have singular values three and one, and let B have the same list. Their direct sum has singular values three, three, one, one. At k equal to one, the Ky Fan prefix of A is three, and the Ky Fan prefix at two for the direct sum is six.

Let C and D each have singular values four and two. Their direct sum has singular values four, four, two, two. The first two entries sum to eight, twice the first Ky Fan sum of C.

The inequality six at most eight recovers three at most four. At even index four, we obtain eight at most twelve, recovering the full singular-value sum four at most six.

The example is simple, but the algebra survives in arbitrary dimension because it depends only on decreasing singular-value sequences.

### Why this appears in subspace perturbation theory

Let P and Q be orthogonal projections. An ambient sine operator can be assembled from complementary cross maps. One cross map measures the part of vectors in P that lies outside Q; the other measures the reverse direction from P perpendicular.

A spectral Sylvester argument often estimates each cross map against a corresponding projected perturbation. Lemma six point one combines the two inequalities into a comparison for the ambient block sum, preserving all Ky Fan prefixes.

The second lemma in this pair then shows that the corresponding perturbation blocks, taken together, have no larger unitarily invariant norm than the original perturbation. Together they let us pass from directed estimates to ambient estimates without blindly doubling the right-hand side.

### Infinity and ideal membership

For a compact operator in infinite-dimensional Hilbert space, singular values form a sequence tending to zero. The direct-sum reasoning remains valid through finite Ky Fan prefixes. No infinite sum is required to establish a fixed prefix inequality.

But a symmetric ideal norm may be finite only on a proper class of compact operators. To claim an ideal estimate, show that the right direct sum lies in the ideal and invoke the ideal's dominance property to place the left direct sum there as well.

The lemma may be stated by controlling every Ky Fan prefix, or by quantifying over an appropriate family of normalized unitarily invariant norms. The latter statement must also specify membership in each norm's domain. The domain condition cannot be omitted.

### The proof to remember

The entire argument has three steps. Orthogonal blocks yield the union of their singular-value lists. The k-th Ky Fan prefix of that union is the maximum of the sums over all splits of k. Componentwise weak majorization controls every one of those splits and therefore the maximum.

Under matching singular-value lists, even prefixes of the direct sum are twice the prefixes of a single block, giving the converse.

## Pinching through an involution

Suppose we know the size of an operator K. We insert orthogonal projections on both sides, retain two matching diagonal blocks, and discard the other two blocks. Can the remaining operator be larger than K in a unitarily invariant norm?

Davis and Kahan's Lemma six point two says no. The proof is short, but it is worth deriving carefully because it works for different projections on the input and output sides. Its key device is averaging K with its reflection through a pair of subspaces.

### Start with a two-by-two block matrix

Let the input Hilbert space be decomposed as V plus V perpendicular, and the output as U plus U perpendicular. In these coordinates, K has four rectangular blocks.

The first block maps V into U. The second maps V perpendicular into U. The third maps V into U perpendicular. The fourth maps V perpendicular into U perpendicular.

The pinched operator keeps the first and fourth blocks and replaces the two off-diagonal blocks by zero. In projection notation, it is P U times K times P V, plus P U perpendicular times K times P V perpendicular.

The projections on the two sides need not be equal. This is a two-sided pinching, designed for the cross-block geometry of comparing two different subspaces.

### Construct the reflections

Define J U to equal twice P U minus the identity. This operator acts as positive one on U and negative one on U perpendicular. Likewise define J V using V.

Each J is self-adjoint and unitary. Squaring it gives the identity, since P squared equals P. Thus each J is an involution. Its operator norm is one.

Now compute J U times K times J V in the four-block coordinates. A block whose input and output have the same sign keeps its sign. A block connecting opposite signs changes sign. Therefore the first and fourth blocks are unchanged, while the two off-diagonal blocks are negated.

Add K to J U K J V. The off-diagonal blocks cancel and the two diagonal blocks double. Dividing by two gives precisely the pinched operator.

The identity is exact: the pinching equals one half of K plus J U K J V.

### Prove norm contraction

Let N be any unitarily invariant norm for which K is in the relevant normed class. By the triangle inequality, twice the norm of the pinching is at most the norm of K plus the norm of J U K J V.

Because J U and J V are unitaries, the second norm equals the first. Therefore twice the norm of the pinching is at most twice the norm of K. Divide by two.

We have proved that the pinched operator has norm at most the original operator's norm.

Notice the strength of this argument. It did not inspect individual entries. It did not choose eigenvectors or singular vectors. It did not depend on a dimension count. It used only the reflection identity, unitary invariance, and the triangle inequality.

In a symmetric operator ideal, one must also verify the pinched operator is a member. Both K and J U K J V are members by ideal invariance, so their sum and its scalar multiple are members. This is why the formal source states membership and norm control together.

### Test the result on matrices

Take the two-by-two matrix with every entry equal to one. With U and V both the first coordinate axis, pinching removes the off-diagonal entries, leaving the identity matrix.

The original rank-one matrix has singular values two and zero. The pinched identity has singular values one and one. Its operator norm decreases from two to one, and its Frobenius norm decreases from two to the square root of two. Its nuclear norm stays two.

The example also shows why an individual singular value need not decrease. The second singular value has increased from zero to one. What is contracted is every unitarily invariant norm, or equivalently every Ky Fan prefix and the associated weak-majorization relations—not the singular-value list term by term.

For the first Ky Fan prefix, one is at most two. For the first two, two equals two. Both comparisons hold.

### Distinguish two-sided from one-sided compression

A simple compression P K P also contracts many norms, since the factors have operator norm at most one. But the two-block pinching is not merely a single compression. It keeps two separated pieces, each occupying a different diagonal corner.

Bounding them individually by the norm of K and then using the triangle inequality would give the wasteful estimate twice the norm of K. Reflection averaging recovers the sharp constant one.

This constant is important in the symmetric sine-theta proof. If we lose a factor of two here, the final perturbation estimate will not retain the expected normalization.

### Generalize to rectangular spaces

Nothing essential requires the same underlying Hilbert space on the left and right. Let the domain carry its own orthogonal decomposition and the codomain a different one. Define a sign reflection on each space. The same identity holds: diagonal block selection equals the average of K and its left-right conjugate by the two reflections.

The conjugate is not necessarily an inner conjugation by one unitary because the left and right spaces can be different. It is nonetheless a left unitary times K times a right unitary, and rectangular unitarily invariant norms are invariant under such transformations.

The ambient quadratic-form argument concerns two subspaces of one Hilbert space, while the symmetric-ideal norm comparison also applies to rectangular operators.

### Why does the Ky Fan statement follow?

For each positive integer k, the Ky Fan k norm is the sum of the first k singular values. It is unitarily invariant and obeys the triangle inequality. Applying the reflection-averaging proof at that norm gives a comparison of every finite singular-value prefix.

Consequently the singular-value sequence of the pinched operator is weakly majorized by that of K. This formulation is useful because later proofs can combine it with Lemma six point one's direct-sum comparison before passing to another symmetric gauge.

The two lemmas fit together without changing norm classes. Lemma six point one combines prefix inequalities for orthogonal blocks. Lemma six point two controls the selected pair of perturbation blocks by the original perturbation at every prefix.

### Cross-block geometry in the sine theorem

Suppose P and Q are the projections onto two spectral subspaces. The ambient difference P minus Q can be expressed using cross projections. One term measures vectors in P that land in Q perpendicular. Another measures vectors in P perpendicular that land in Q.

A Sylvester argument gives a norm estimate for each cross term separately. The right-hand sides involve corresponding off-diagonal pieces of the perturbation, which can be placed into two compatible diagonal blocks by choosing their source and target decompositions correctly.

Lemma six point one combines the left-side cross terms. Lemma six point two then pinches the perturbation on the right side and guarantees the resulting pair of perturbation blocks has no greater norm than the original perturbation.

This establishes the bridge from two directed equations to an ambient-angle inequality. Without the lemmas, it is easy to add separate estimates and introduce an extra factor or assume two singular-value lists coincide when they do not.

### The role of self-adjointness

The pinching lemma itself does not require K to be self-adjoint. It is a statement about bounded operators and unitary invariance. Self-adjointness enters elsewhere in the spectral perturbation argument, where it guarantees reducing decompositions, real spectra, and adjoint relations between the off-diagonal blocks.

Keeping those logical dependencies separate helps generalize the lemma. We can use it for arbitrary rectangular maps, even though our immediate application is to self-adjoint perturbations.

### What to remember

The pinching operator is the average of two equally sized operators: K and its reflection-transformed copy. Unitary invariance makes their norms equal, and convexity of the norm makes the average no larger.

This is the entire mechanism of Lemma six point two. Its conclusion is both an ideal-membership statement and a norm bound when ideal norms are used.

That proof will show exactly why the perturbation norm appears without an avoidable factor of two.

## Ambient sine from an ambient perturbation

Take a horizontal line inside a two-dimensional plane. Every vector on the line already belongs to the plane, so the distance from the line to the plane, measured in that direction, is zero. But the vertical unit vector in the plane is a full unit away from the line. Reversing the comparison changes the answer completely.

The same asymmetry appears in perturbation theory when we compare a trial subspace with an exact spectral subspace. A residual often bounds only one directed escape. Proposition six point one seeks a bound for the entire ambient angle, which sees both directions. To obtain it, the proof uses two cross-block equations and a norm inequality that recombines their information.

The answer is yes, under spectral separation in both crossed directions. We will derive the two Sylvester equations, combine their singular values, and see exactly why the pinching lemma is needed to recover a constant of one.

### Set up the four spectral blocks

Let A and B be bounded self-adjoint operators on one Hilbert space. Write K for B minus A. Let U reduce A, and let V reduce B. Denote their orthogonal projections by P and Q.

Because U reduces A, the operator A has no blocks connecting U to its orthogonal complement. Likewise B has no blocks connecting V to its complement. But the decompositions need not agree. Their relative orientation is the geometry we want to measure.

Form X by projecting first onto U and then onto V perpendicular. It maps vectors of U into V perpendicular. Its operator norm is the maximal sine of a directed angle from U toward V. Form Y by projecting first onto U perpendicular and then onto V. It maps vectors of V into U perpendicular and measures the reverse direction.

These two directed maps can have different singular-value lists if the dimensions differ. We must retain both of them.

### Derive the first Sylvester equation

Take a vector u in U. Since A preserves U, applying the compression of A on U and then X gives the V-perpendicular component of A u. Since B preserves V perpendicular, applying the compression of B there to X u gives the V-perpendicular component of B u.

Subtract these two expressions. The result is the V-perpendicular component of B u minus A u. But B minus A equals K. Thus the first Sylvester equation has unknown X, coefficients B on V perpendicular and A on U, and right-hand side the block of K from U into V perpendicular.

Suppose the spectrum of A restricted to U is separated from that of B restricted to V perpendicular by a gap delta in the interval-versus-exterior sense. The appropriate Sylvester estimate gives delta times every Ky Fan prefix of X at most the corresponding prefix of that perturbation block.

This is a directed sine estimate, but only one of the two we need.

### Derive the complementary equation

Now reverse the roles of the selected spaces and their complements. Form X prime, the map that projects from U perpendicular into V. This is the adjoint of Y, so X prime and Y have the same singular values.

Because A preserves U perpendicular and B preserves V, a second calculation gives B restricted to V times X prime, minus X prime times A restricted to U perpendicular, equals the block of K from U perpendicular into V.

This requires another gap hypothesis: the selected spectrum of B on V must be separated from the spectrum of A on U perpendicular. The first gap does not automatically imply the second. Proposition six point one assumes both.

Apply the Sylvester inequality again. We obtain a Ky Fan bound on X prime using the second complementary block of K.

### Reassemble the ambient sine

We have two rectangular maps and two inequalities. How do they describe a single operator on the ambient Hilbert space?

Consider the square of P minus Q. Expand the product, remembering that P squared is P and Q squared is Q. The expression is P plus Q minus P Q minus Q P.

Now inspect it using the decomposition U plus U perpendicular. Its off-diagonal blocks vanish. Its U-to-U block is P times one minus Q times P, exactly X adjoint X. Its U-perpendicular block is one minus P times Q times one minus P, exactly Y Y adjoint.

Therefore the positive square root of this square has singular values obtained by combining the singular values of X and Y. This positive operator is the absolute value of P minus Q. It is the ambient sine-angle operator.

There is no dimension-matching assumption in this identity. If U contains a direction perpendicular to all of V, its sine is one. If the reverse defect exists instead, that also appears. The ambient construction records both.

### Combine the two inequalities without losing a constant

We want to combine every Ky Fan prefix of X and X prime. The direct-sum comparison for block-diagonal sums of maps on orthogonal summands tells us how: if each block's singular-value prefixes are dominated by those of a corresponding perturbation block, their orthogonal direct sum inherits the domination.

The two perturbation blocks have orthogonal input supports, U and U perpendicular, and orthogonal output supports, V perpendicular and V. They can therefore be placed together as a single block-diagonal operator, up to exchanging the order of the target blocks.

This combined operator is the two-sided pinching of K that keeps precisely those two blocks. The reflection-averaging identity from Lemma six point two proves its norm, in every unitarily invariant gauge, is no greater than the norm of K.

Combining the Sylvester comparisons, direct-sum comparison, and pinching, we obtain delta times the ambient sine norm at most the norm of B minus A.

Notice what did not work. Adding two scalar operator-norm bounds directly would have yielded a factor of two. Nor could we assume the two directed lists were identical. The block methods preserve the exact multiplicities and the constant.

### Check equality in a two-dimensional example

Let A be diagonal with eigenvalues zero and four. Choose U as its zero-eigenspace, the horizontal axis. Rotate both eigenvectors by an angle theta, and let B be the rotation of A by that change of orthonormal basis. Its zero-eigenspace V is the rotated horizontal line.

Both crossed spectral gaps equal four: each zero block is separated from the opposite four block.

The operator norm of the difference of the two rank-one projections is sine theta. The operator norm of B minus A is four times sine theta. So delta times the ambient sine norm equals the perturbation norm exactly.

In Frobenius norm, each projection difference has two nonzero singular values equal to sine theta. Its Frobenius norm is the square root of two times sine theta. The perturbation difference similarly has two singular values four sine theta. Equality holds again.

This is a sharpness witness, not just an illustration. We cannot improve the universal constant below one in these norm classes.

### Why an arbitrary residual does not suffice

If we start only with a trial residual for U, we control the map from U into V perpendicular. We do not know what happens to a direction in V that lies in U perpendicular. For example, if U is a one-dimensional line inside a two-dimensional V, the directed escape of U from V is zero. Yet P minus Q has norm one because V contains a direction missing from U.

Proposition six point one avoids this defect by assuming two operators, two reducing subspaces, and two crossed spectral gaps. These hypotheses generate both directed equations and give access to the same ambient perturbation K on the right.

This is the precise difference between an ambient perturbation theorem and an arbitrary trial-residual theorem.

### The role of operator ideals

In an infinite-dimensional Hilbert space, a symmetric norm may be finite only for operators in a particular ideal. The statement must therefore establish two things: membership of the ambient sine operator when K belongs to the ideal, and the numerical inequality for its ideal norm.

Controlling every Ky Fan prefix establishes weak majorization. In a symmetric ideal satisfying the required dominance property, the comparison transfers both ideal membership and the norm bound.

The original paper states its theorem in a separable ambient Hilbert space and uses interval-versus-exterior crossed gaps. An abstract Sylvester-gap condition can support a more general formulation. The original proposition assumes the explicit interval-versus-exterior separation.

### Close

The entire proof has four stages. Build two crossed Sylvester equations. Estimate both directed escape maps. Recognize the ambient sine as their combined singular-value list. Finally, pinch the common perturbation K to control both right-hand sides by a single norm.

## Non-isometric frames and unequal dimensions

A trial subspace is often represented by orthonormal columns, but computational trial frames may be scaled, nonorthogonal, or redundant. The Gram operator measures their failure to have orthonormal coordinates, and that error affects how residual estimates are normalized.

Davis and Kahan's Theorem six point one keeps the trial map itself rather than silently replacing it with an isometry. It permits a non-isometric frame and different dimensions of the trial and exact subspaces. Its additional factor, epsilon, comes directly from a lower bound on that frame.

### Distinguish a frame from its range

Let F be a coordinate Hilbert space and H the ambient Hilbert space. A trial frame E zero is a bounded linear map from F to H. Its range is the trial subspace, assuming it has closed range as guaranteed here by a positive lower bound.

If E zero is an isometry, the length of every coordinate vector is preserved. But for a general frame that is false. The same ambient trial subspace can be described by many different frames, such as an orthonormal frame multiplied by an invertible matrix.

We assume there is a positive epsilon such that the length of E zero x is at least epsilon times the length of x for every coordinate vector x. This says the frame does not collapse any coordinate direction. It also says the inverse on its range has norm at most one over epsilon.

Here epsilon bounds the lengths of trial-frame outputs from below. If lambda-min denotes the smallest eigenvalue of E zero adjoint E zero, the corresponding length bound is the square root of lambda-min. Confusing the length bound with the eigenvalue changes the constant.

### Obtain orthonormal coordinates by polar decomposition

Take the positive modulus of E zero, the square root of E zero adjoint E zero. The lower-frame hypothesis implies this modulus is bounded below by epsilon and therefore has a bounded inverse.

Write the polar decomposition of E zero as W times its modulus. Because E zero is injective with closed range, W is an isometry of F onto the trial subspace. This is a canonical way to normalize the frame without changing its range.

If the smallest singular value of E zero is epsilon, then the inverse of its modulus has operator norm at most one over epsilon. That one inequality will explain the entire normalization penalty.

Picture an exact horizontal plane in three-dimensional space, spanned by the first two coordinate axes. We measure how far a trial plane rises out of it.

Use two trial columns. The first points along the first coordinate axis and has length two. The second has length one quarter. It tilts away from the second coordinate axis toward the vertical axis through an angle theta. The columns are perpendicular, but their lengths differ by a factor of eight.

Their Gram matrix measures those column lengths squared: four and one sixteenth on the diagonal. Taking its positive square root recovers the lengths two and one quarter. This is the matrix we divide out when we turn the columns into an orthonormal frame. The small second column then becomes a unit vector with the same tilt theta.

The smallest frame length is one quarter, so epsilon is one quarter. The normalized frame W has two unit columns; its second column still makes angle theta with the selected plane. Normalization changes the coordinates and the residual's scale, while the trial subspace and its angle stay the same.

### Choose exact spectral coordinates

Let A be a possibly unbounded self-adjoint operator on H. Choose an exact reducing spectral decomposition with an exact selected component and its orthogonal complement. Let F one be an isometric coordinate map into that complementary component, and let Lambda one denote the restricted operator there.

Choose a self-adjoint trial coordinate operator A zero on F. Suppose E zero maps the trial coordinates into the domain of A and satisfies the residual equation: A applied to E zero equals E zero followed by A zero, plus a bounded residual map R.

The domain clause is necessary if A is unbounded. We cannot even write the residual for all coordinates unless E zero lands in the domain. The exact complement is also required to reduce A, so its restricted operator is well-defined on the appropriate domain.

### Compress the residual equation

Apply F one adjoint to the residual identity. Because F one identifies the exact complementary reducing space, F one adjoint A E zero becomes Lambda one applied to F one adjoint E zero.

Define X as F one adjoint E zero. The remaining term is X A zero. Thus we obtain the Sylvester equation: Lambda one X minus X A zero equals F one adjoint R.

The spectral hypothesis is a genuine ordered or interval-versus-exterior Sylvester gap of size delta between A zero and Lambda one. Under that hypothesis, the applicable ideal estimate gives delta times the ideal norm of X no greater than the ideal norm of R. Projection by F one adjoint does not increase the relevant singular values.

But X still contains the nonorthonormal scaling of E zero. It is not yet the intrinsic sine map of the trial subspace.

### Remove the scaling, and find epsilon

Replace E zero by its polar factorization W times the modulus. Then X equals F one adjoint W followed by that modulus.

The map F one adjoint W goes from trial coordinates to complementary exact coordinates. Its singular values are the directed sines. Let us call it S. The raw cross operator X has the same domain and codomain, but its singular values also contain the scaling inherited from E zero.

We have X equals S times the modulus. Multiply on the right by the inverse modulus. Then S equals X times that inverse. Since the inverse has norm at most one over epsilon, every supported unitarily invariant ideal norm obeys epsilon times the norm of S at most the norm of X.

Combine this with the Sylvester bound. The conclusion is delta times epsilon times the directed sine norm no greater than the residual norm.

The two factors have different sources. Delta comes from spectral separation. Epsilon comes from frame conditioning. Neither can be omitted without changing the data being estimated.

Return to the tilted second column. Choose the ambient diagonal operator with eigenvalues zero, zero, and positive d. It ignores horizontal motion and multiplies the vertical coordinate by d. Choose the trial operator to be zero.

The long first column has no vertical component, so its residual vanishes. The shorter column has vertical component one quarter times sine theta. Applying the ambient operator makes its residual length d times sine theta divided by four. That is the only nonzero singular value of the residual.

The unnormalized cross projection has size sine theta divided by four. Once we normalize the frame, the geometric sine is simply sine theta. We have gained a factor of four in the normalized sine because we divided out the quarter-length column. The lower frame bound, one quarter, restores the correct scale: gap d times one quarter times sine theta equals the residual length. Here the estimate is exact.

The calculation also shows why it is the smallest frame length that enters: the residual is concentrated in the column whose normalization requires the largest amplification.

### Check the constant in one dimension

Take the ambient plane with A diagonal, with eigenvalues zero and d, where d is positive. Choose the exact selected subspace as the horizontal axis and its complement as the vertical axis.

Let the trial coordinate space be one-dimensional. Map the unit coordinate to epsilon times the unit vector at angle theta above the horizontal axis. Take the trial coordinate operator A zero to be zero. The residual is simply A applied to the trial vector, which has length epsilon d sine theta.

Here the cross operator X has length epsilon sine theta and the normalized directed sine has value sine theta. The gap delta between the trial zero and the complementary eigenvalue d is exactly d.

Thus delta epsilon sine theta equals the residual norm. The estimate is sharp for every positive epsilon and every theta between zero and a right angle.

If we had omitted epsilon, shrinking the frame would make the residual arbitrarily small while the subspace angle stayed fixed. The inequality would become false. The factor is therefore mathematically necessary.

### Unequal dimensions require a direction

Now consider a line U inside a plane V in three-dimensional space. The directed sine from U toward V is zero because every vector of U lies in V. But the reverse directed sine from V toward U is one, since V contains a direction perpendicular to U.

An ambient projection difference registers that missing direction and has norm one. A theorem based only on the trial map E zero and the complementary part of the exact decomposition generally controls the first directed sine, not the entire ambient projection difference.

Theorem six point one therefore allows the trial and exact selected coordinates to have different dimensions without pretending that both directed angles are equal. The conclusion is stated for a representative having the appropriate directed sine singular values.

This is also why a convenient rectangular operator representative is allowed in the formal statement. Different source and target coordinate spaces can carry the same nonzero singular-value list, possibly supplemented by zeros. The ideal norm depends on that list rather than on how the representative is embedded.

### What the theorem does and does not promise

A positive lower-frame bound does not itself establish spectral separation. A small residual does not determine which exact cluster to compare against. The theorem needs the self-adjoint coordinate operators, exact spectral decomposition, domain-aware residual, positive frame bound, and a legitimate Sylvester gap.

In a symmetric ideal one must also assume the residual belongs to the ideal and prove that the sine representative belongs to it. That membership is part of the conclusion, not a default property of arbitrary bounded operators.

The original Section six theorem uses interval-versus-exterior spectral separation, with either ordering allowed. An equivalent or stronger abstract gap condition may also support the analytic estimate, but the interval-versus-exterior assumption is the one used in the original theorem.

### Summary

The result can be reconstructed from three moves. Compress the residual to obtain a Sylvester equation. Bound the crossed operator X by the residual using the spectral gap. Normalize the frame by polar decomposition, paying exactly the inverse lower-frame bound.

The formula is delta epsilon times the directed sine norm at most the residual norm.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Direct-sum norm comparison

**Draft status:** audio-first mathematical lecture. **Prerequisites:** `054000–056000` Ky Fan sums and majorization; `060000` block direct sums. **Next:** `123000` pinching through an involution.

---

#### Companion: mathematics and Lean correspondence (display only)

For rectangular maps `A,B` between orthogonal input/output summands, write `K_k(A)=Σ_{i=1}^k s_i(A)`. Then

\[K_k(A\oplus B)=\max_{0\le i\le k}\bigl(K_i(A)+K_{k-i}(B)\bigr).\]

If `K_i(A)≤K_i(C)` and `K_i(B)≤K_i(D)` at every `i`, the formula implies weak majorization of `A⊕B` by `C⊕D`. Under `s(A)=s(B)` and `s(C)=s(D)`, `K_{2k}(A⊕B)=2K_k(A)` and similarly for `C,D`; hence the converse. The source formalization explicitly tracks `SameSingularValues` across heterogeneous rectangular and ambient projection blocks.

##### Exact Lean declaration excerpts

`DavisKahan/Sources/DavisKahan1970/SineTheta/Lemma61.lean` — `projectionBlock_same_compression` (exact declaration header; proof body omitted):

```lean
theorem projectionBlock_same_compression
    (Ω Γ : Submodule 𝕜 E)
    [Ω.HasOrthogonalProjection] [Γ.HasOrthogonalProjection]
    (K : E →L[𝕜] E) :
    ContinuousLinearMap.SameSingularValues
      (projectionBlock Ω Γ K) (blockCompression Ω Γ K) := by
```

`DavisKahan/Sources/DavisKahan1970/SineTheta/Lemma61.lean` — `lemma61_all_kyFan` (exact declaration header; proof body omitted):

```lean
theorem lemma61_all_kyFan
    (Ω Γ : Submodule 𝕜 E)
    [Ω.HasOrthogonalProjection] [Γ.HasOrthogonalProjection]
    (K Ktilde L Ltilde : E →L[𝕜] E)
    (h₀ : ∀ k,
      ((projectionBlock Ω Γ K).kyFanGauge k : ℝ) ≤
        ((projectionBlock Ω Γ L).kyFanGauge k : ℝ))
    (h₁ : ∀ k,
      ((projectionBlock Ωᗮ Γᗮ Ktilde).kyFanGauge k : ℝ) ≤
        ((projectionBlock Ωᗮ Γᗮ Ltilde).kyFanGauge k : ℝ)) :
    ∀ k,
      ((projectionBlock Ω Γ K +
            projectionBlock Ωᗮ Γᗮ Ktilde).kyFanGauge k : ℝ) ≤
        ((projectionBlock Ω Γ L +
            projectionBlock Ωᗮ Γᗮ Ltilde).kyFanGauge k : ℝ) := by
```

`DavisKahan/Sources/DavisKahan1970/SineTheta/Lemma61.lean` — `lemma61_converse` (exact declaration header; proof body omitted):

```lean
theorem lemma61_converse
    (Ω Γ : Submodule 𝕜 E)
    [Ω.HasOrthogonalProjection] [Γ.HasOrthogonalProjection]
    (K Ktilde L Ltilde : E →L[𝕜] E)
    (hK : ContinuousLinearMap.SameSingularValues
      (projectionBlock Ω Γ K)
      (projectionBlock Ωᗮ Γᗮ Ktilde))
    (hL : ContinuousLinearMap.SameSingularValues
      (projectionBlock Ω Γ L)
      (projectionBlock Ωᗮ Γᗮ Ltilde))
    (hsum : ∀ k,
      ((projectionBlock Ω Γ K +
            projectionBlock Ωᗮ Γᗮ Ktilde).kyFanGauge k : ℝ) ≤
        ((projectionBlock Ω Γ L +
            projectionBlock Ωᗮ Γᗮ Ltilde).kyFanGauge k : ℝ)) :
    ∀ k,
      ((projectionBlock Ω Γ K).kyFanGauge k : ℝ) ≤
        ((projectionBlock Ω Γ L).kyFanGauge k : ℝ) := by
```

**Mapping.** `projectionBlock_same_compression` identifies singular values of an ambient projected map with those of its rectangular compression. `lemma61_all_kyFan` combines two **all-prefix** inequalities, not merely one fixed norm bound. `lemma61_converse` additionally assumes `SameSingularValues` for the paired blocks on each side; the even-prefix argument is the reason.

### Pinching through an involution

**Draft status:** audio-first mathematical lecture. **Prerequisites:** `060000` pinching and `122000` direct-sum comparison. **Next:** `124000` ambient sine from an ambient perturbation.

---

#### Companion: mathematics and Lean correspondence (display only)

Let `P_U,P_V` be orthogonal projections and `J_U=2P_U-I`, `J_V=2P_V-I`. Define

\[\mathcal P_{U,V}(K)=P_UKP_V+(I-P_U)K(I-P_V)=\tfrac12(K+J_UKJ_V).\]

For every compatible unitarily invariant norm `N`, `N(\mathcal P_{U,V}(K))≤N(K)`. The same argument works in rectangular source/target Hilbert spaces with separate left and right reflections. In an operator ideal the source also proves `Mem K ⇒ Mem(\mathcal P_{U,V}(K))`. Individual singular values need not decrease; only their Ky Fan prefixes are bounded.

##### Exact Lean declaration excerpts

`DavisKahan/Sources/DavisKahan1970/SineTheta/ProjectionBlocks.lean` — `diagonalPair` (exact declaration header; proof body omitted):

```lean
def diagonalPair (U V : Submodule 𝕜 E)
    [U.HasOrthogonalProjection] [V.HasOrthogonalProjection]
    (K : E →L[𝕜] E) : E →L[𝕜] E :=
```

`DavisKahan/Sources/DavisKahan1970/SineTheta/ProjectionBlocks.lean` — `two_smul_diagonalPair_eq_add_reflections` (exact declaration header; proof body omitted):

```lean
theorem two_smul_diagonalPair_eq_add_reflections
    (U V : Submodule 𝕜 E)
    [U.HasOrthogonalProjection] [V.HasOrthogonalProjection]
    (K : E →L[𝕜] E) :
    (2 : 𝕜) • diagonalPair U V K =
      K + U.reflectionOperator ∘L K ∘L V.reflectionOperator := by
```

`DavisKahan/Sources/DavisKahan1970/SineTheta/ProjectionBlocks.lean` — `diagonalPair_normingGauge_le` (exact declaration header; proof body omitted):

```lean
theorem diagonalPair_normingGauge_le
    (N : SymmetricNormingFunction)
    (U V : Submodule 𝕜 E)
    [U.HasOrthogonalProjection] [V.HasOrthogonalProjection]
    {K : E →L[𝕜] E} (hK : N.Mem K) :
    N.Mem (diagonalPair U V K) ∧
      N.gauge (diagonalPair U V K) ≤ N.gauge K := by
```

**Mapping.** `diagonalPair` is the two-sided block pinching `P_U K P_V+(I-P_U)K(I-P_V)`. The reflection declaration is the exact algebraic average identity. `diagonalPair_normingGauge_le` includes both membership and the finite gauge inequality under the source `SymmetricNormingFunction` interface.

### Ambient sine from an ambient perturbation

**Draft status:** audio-first mathematical lecture. **Prerequisites:** `110000`, `122000`, `123000`. **Next:** `125000`, non-isometric frames and unequal dimensions.

---

#### Companion: mathematics and Lean correspondence (display only)


Let \(K=B-A\), \(P=P_U\), \(Q=P_V\), and
\[X=P_{V^\perp}P_U,\qquad X'=P_VP_{U^\perp}.\]
The cross-block Sylvester equations are
\[
 B_{V^\perp}X-XA_U=P_{V^\perp}KP_U,\qquad
 B_VX'-X'A_{U^\perp}=P_VKP_{U^\perp}.
\]
The ambient squared difference decomposes as
\[(P-Q)^2=\bigl(X^*X\bigr)|_U\oplus\bigl((X')^*X'\bigr)|_{U^\perp}.\]
Both crossed **interval/exterior** gaps are required in the paper-facing statement. The conclusion is ideal membership plus \(\delta N(\sin\Theta)\le N(K)\), not merely an operator-norm inequality.


##### Exact Lean declaration excerpts


`DavisKahan/Sources/DavisKahan1970/Proposition61.lean` — `proposition6_1_complex` (exact declaration header; proof body omitted):

```lean
theorem proposition6_1_complex
    (N : SymmetricNormingFunction)
    {A B : E →L[ℂ] E} (hA : A.IsSymmetric) (hB : B.IsSymmetric)
    {U V : Submodule ℂ E} [U.HasOrthogonalProjection] [V.HasOrthogonalProjection]
    (hU : Submodule.IsReducing U A) (hV : Submodule.IsReducing V B)
    {δ : ℝ} (hδ : 0 < δ)
    (hgapUV : FormBoundedSylvesterGap
      (PartialMap.boundedReducingBlock A U hU)
      (PartialMap.boundedReducingBlockCompl B V hV) δ)
    (hgapVU : FormBoundedSylvesterGap
      (PartialMap.boundedReducingBlock B V hV)
      (PartialMap.boundedReducingBlockCompl A U hU) δ)
    (hMem : N.Mem (B - A)) :
    N.Mem (cfc Real.sin (Angle.angleOperator U V)) ∧
      δ * N.gauge (cfc Real.sin (Angle.angleOperator U V)) ≤ N.gauge (B - A) := by
```


`DavisKahan/Sources/DavisKahan1970/Section6SourceScope.lean` — `proposition6_1_printedGap_sourceExact_complex` (exact declaration header; proof body omitted):

```lean
theorem proposition6_1_printedGap_sourceExact_complex
    {E : Type v} [NormedAddCommGroup E] [InnerProductSpace ℂ E] [CompleteSpace E]
    [TopologicalSpace.SeparableSpace E]
    (N : NormalizedUnitaryInvariantNorm.{0, v} ℂ)
    {A B : E →L[ℂ] E} (hA : A.IsSymmetric) (hB : B.IsSymmetric)
    {U V : Submodule ℂ E} [U.HasOrthogonalProjection] [V.HasOrthogonalProjection]
    (hU : Submodule.IsReducing U A) (hV : Submodule.IsReducing V B)
    {δ : ℝ} (hδ : 0 < δ)
    {β α β' α' : ℝ} (hβα : β ≤ α) (hβα' : β' ≤ α')
    (hgapUV : DavisKahan.Sylvester.RealSpectrumIntervalExteriorGap
      (DavisKahanExt.PartialMap.boundedReducingBlock A U hU)
      (DavisKahanExt.PartialMap.boundedReducingBlockCompl B V hV) β α δ)
    (hgapVU : DavisKahan.Sylvester.RealSpectrumIntervalExteriorGap
      (DavisKahanExt.PartialMap.boundedReducingBlock B V hV)
      (DavisKahanExt.PartialMap.boundedReducingBlockCompl A U hU) β' α' δ)
    (hMem : N.Mem (B - A)) :
    N.Mem (cfc Real.sin (DavisKahan.Angle.angleOperator U V)) ∧
      δ * N.gauge (cfc Real.sin (DavisKahan.Angle.angleOperator U V)) ≤ N.gauge (B - A) :=
```



**Mapping.** `hU` and `hV` certify reducing subspaces; `hgapUV` and `hgapVU` are two distinct cross-gap proofs. `SymmetricNormingFunction` and `NormalizedUnitaryInvariantNorm` encode the class of norms. `N.Mem` is a necessary premise/conclusion in Hilbert space. The exact source façade in `Section6SourceScope.lean` additionally requires ambient separability and the printed interval/exterior placement.

### Non-isometric frames and unequal dimensions

**Draft status:** audio-first mathematical lecture. **Prerequisites:** `015000`, `017000`, `035000`, `108000`, `124000`. **Next:** `126000`, weak spectral gaps and Hilbert–Schmidt estimates.

---

#### Companion: mathematics and Lean correspondence (display only)


For \(E_0:F\to H\), the Lean predicate `LowerFrameBound E₀ ε` records \(\|E_0x\|\ge\varepsilon\|x\|\). Polar decomposition gives \(E_0=W|E_0|\), with \(W^*W=I_F\) and \(\||E_0|^{-1}\|\le1/\varepsilon\). The raw crossed map \(X=F_1^*E_0\) satisfies a domain-aware Sylvester equation; the normalized directed sine is represented by \(S=F_1^*W=X|E_0|^{-1}\). Thus
\[\delta\,\varepsilon\,N(S)\le N(R).\]
`SinThetaRepresentativeAcross` permits equivalent rectangular realizations, while `IsTrialResidualEquation` and `IsExactSpectralDecomposition` encode the actual domain and exact-reduction obligations. The paper-facing spectral condition is interval/exterior separation, rather than an arbitrary `PairwiseSpectrumGap`.


**A conditioned two-column frame attaining the estimate.** On \(H=\mathbb R^3\), let \(U=\operatorname{span}(e_1,e_2)\), \(A=\operatorname{diag}(0,0,d)\) with \(d>0\), \(F=\mathbb R^2\), and
\[
 W=\begin{pmatrix}1&0\\0&\cos\theta\\0&\sin\theta\end{pmatrix},\qquad
 D=\operatorname{diag}(2,\tfrac14),\qquad E_0=WD,\qquad A_0=0.
\]
Then \(E_0^*E_0=D^2=\operatorname{diag}(4,1/16)\), so \(\varepsilon=1/4\) is the optimal lower frame bound. With \(F_1=e_3\) and \(\Lambda_1=d\),
\[
 X=F_1^*E_0=(0,\tfrac14\sin\theta),\quad
 S=F_1^*W=(0,\sin\theta),\quad
 R=AE_0=(0,0,\tfrac d4\sin\theta)\,e_2^*.
\]
Here \(R\) denotes the \(3\times2\) map whose second column is \((d\sin\theta/4)e_3\); equivalently \(R=(d\sin\theta/4)e_3 e_2^*\). For \(0<\theta<\pi/2\), each map has rank one, and
\[
 \delta\varepsilon\|S\|_{S_q}=d\tfrac14\sin\theta=\|R\|_{S_q}
\]
for every finite Schatten \(q\) and in operator norm. This checks the factor \(1/\varepsilon\) and separates raw leakage from the intrinsic angle.

##### Exact Lean declaration excerpts


`DavisKahan/Sources/DavisKahan1970/Theorem61.lean` — `theorem6_1_complex` (exact declaration header; proof body omitted):

```lean
theorem theorem6_1_complex
    {E₀' F₀' : Type v}
    [NormedAddCommGroup E₀'] [InnerProductSpace ℂ E₀'] [CompleteSpace E₀']
    [NormedAddCommGroup F₀'] [InnerProductSpace ℂ F₀'] [CompleteSpace F₀']
    (N : SymmetricNormingFunction)
    (A : E →ₗ.[ℂ] E) (A₀ : F →ₗ.[ℂ] F) (Λ₁ : G →ₗ.[ℂ] G)
    (E₀ : F →L[ℂ] E) (F₀ : H →L[ℂ] E) (F₁ : G →L[ℂ] E) (R : F →L[ℂ] E)
    (hA : IsSelfAdjoint A) (hA₀ : IsSelfAdjoint A₀) (hΛ₁ : IsSelfAdjoint Λ₁)
    (htrial : IsTrialResidualEquation A A₀ E₀ R)
    (hexact : IsExactSpectralDecomposition A Λ₁ F₀ F₁)
    {ε : ℝ} (hε : 0 < ε) (hframe : LowerFrameBound E₀ ε)
    {δ : ℝ} (hδ : 0 < δ) (hgap : FormBoundedSylvesterGap A₀ Λ₁ δ)
    (S : SinThetaRepresentativeAcross (E₀ :=
```


`DavisKahan/Sources/DavisKahan1970/Section6SourceScope.lean` — `theorem6_1_printedGap_sourceExact_complex` (exact declaration header; proof body omitted):

```lean
theorem theorem6_1_printedGap_sourceExact_complex
    [NormedAddCommGroup E₀'] [InnerProductSpace ℂ E₀'] [CompleteSpace E₀']
    [NormedAddCommGroup F₀'] [InnerProductSpace ℂ F₀'] [CompleteSpace F₀']
    [NormedAddCommGroup E] [InnerProductSpace ℂ E] [CompleteSpace E]
    [TopologicalSpace.SeparableSpace E]
    [NormedAddCommGroup F] [InnerProductSpace ℂ F] [CompleteSpace F]
    [NormedAddCommGroup G] [InnerProductSpace ℂ G] [CompleteSpace G]
    [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H]
    (N : NormalizedUnitaryInvariantNorm.{0, v} ℂ)
    (A : E →ₗ.[ℂ] E) (A₀ : F →ₗ.[ℂ] F) (Λ₁ : G →ₗ.[ℂ] G)
    (E₀ : F →L[ℂ] E) (F₀ : H →L[ℂ] E) (F₁ : G →L[ℂ] E) (R : F →L[ℂ] E)
    (hA : IsSelfAdjoint A) (hA₀ : IsSelfAdjoint A₀) (hΛ₁ : IsSelfAdjoint Λ₁)
    (htrial : IsTrialResidualEquation A A₀ E₀ R)
    (hexact : IsExactSpectralDecomposition A Λ₁ F₀ F₁)
    {ε : ℝ} (hε : 0 < ε) (hframe : LowerFrameBound E₀ ε)
    {δ : ℝ} (hδ : 0 < δ) {β α : ℝ} (hβα : β ≤ α)
    (hgap : DavisKahan.Sylvester.RealSpectrumIntervalExteriorGap A₀ Λ₁ β α δ)
    (S : SinThetaRepresentativeAcross (E₀ :=
```



**Mapping.** `E₀` is the bounded, potentially non-isometric trial map; `F₀` and `F₁` give exact spectral coordinates. `A`, `A₀`, and `Λ₁` are the closed self-adjoint ambient, trial, and complementary operators. `htrial` and `hexact` carry domain and reduction data; `hframe` and `hε` expose the normalization factor. `S` specifies a singular-value-equivalent sine representative; `hR` asserts ideal membership.
