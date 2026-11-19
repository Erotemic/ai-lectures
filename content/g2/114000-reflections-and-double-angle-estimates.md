# Reflections and double-angle estimates

<!-- BEGIN SPOKEN LECTURE -->

# Reflections and double-angle estimates

## Off-diagonal perturbations and block reflection

Consider a symmetric matrix made of two diagonal blocks and one coupling between them. For the smallest example, use a two-by-two matrix with diagonal entries minus one and one, and equal off-diagonal entries h. The diagonal entries describe the two uncoupled coordinates. The off-diagonal entries move information between them.

Now change the sign of the second coordinate while leaving the first unchanged. This is an orthogonal reflection. Applying it before and after the matrix leaves the diagonal entries alone but changes both off-diagonal entries from h to minus h. If we add the reflected matrix to the original and divide by two, the coupling disappears. If we subtract them and divide by two, only the coupling remains.

This is the block-reflection method in miniature. It separates perturbations that act within the chosen subspaces from perturbations that send vectors across the decomposition. The separation matters because the two pieces affect spectral gaps and subspace rotation differently.

The reflection is defined by an orthogonal projection, so the same algebra works on Hilbert spaces. We will derive its exact action on a general two-block operator, then distinguish reflecting an operator's blocks from reflecting one subspace across another. The latter operation is what produces doubled-angle geometry.

### Split the ambient space into two components

Let H be a real or complex Hilbert space, and let U be a closed subspace. Write P for orthogonal projection onto U, and Q for the complementary projection, identity minus P.

Relative to the orthogonal decomposition H equals U plus U perpendicular, every bounded operator T has four blocks. The upper-left block sends U into U; the lower-right sends U perpendicular into itself; and the two off-diagonal blocks cross between the spaces.

Suppose T is self-adjoint and U is reducing for T. Then the off-diagonal blocks vanish. We may write T as a diagonal block matrix with A plus on U and A minus on U perpendicular.

The source's two-block gap hypothesis says the quadratic form of A plus is at least b times squared length, while the form of A minus is at most a times squared length, where b is greater than a. The gap is b minus a.

We have not assumed A plus or A minus is a scalar matrix. Each block may have many eigenvalues. Only the uniform form inequalities matter.

### Define the reflection

The reflection through U is J equal to P minus Q, or equivalently twice P minus the identity.

It acts as plus one on U and minus one on U perpendicular. Because P and Q are orthogonal projections, J is self-adjoint, J squared is the identity, and J preserves all lengths. Thus J is a unitary or orthogonal operator.

In the two-by-two block picture, J is diagonal with entries plus identity and minus identity.

Conjugate T by J. Its upper-left block is unchanged; its lower-right block is unchanged; and each off-diagonal block changes sign. This is immediate from multiplying by the signs on the left and right.

For a general T, subtracting T from J T J therefore removes both diagonal blocks and doubles the negative of the off-diagonal blocks.

### Define an off-diagonal perturbation

Let S equal T plus H, with H self-adjoint. We call H off-diagonal with respect to U when its two diagonal compressions vanish: P H P equals zero and Q H Q equals zero.

Then H maps U into its perpendicular complement and maps that complement back into U. Its matrix has zero diagonal blocks and off-diagonal blocks K and K adjoint.

Conjugation gives J H J equals negative H. We say H anticommutes with J, because J H equals negative H J.

This identity is stronger than saying H has small norm. It is an exact structural restriction. A perturbation can be arbitrarily large and still be off-diagonal.

Because T is block diagonal, J T J equals T. Consequently J S J equals T minus H, while S equals T plus H. Their difference is negative two H. In every unitarily invariant norm, its size is precisely twice the size of H.

There is another useful choice of reflection: the one through a reducing subspace of the perturbed operator S. That reflection gives a bound by twice the perturbation norm without requiring H itself to be off-diagonal.

### Verify everything in two dimensions

Take U to be the horizontal axis. Let T be diagonal with entries three and negative one. The quadratic form gap between the two blocks is four.

Let H have zero diagonal entries and equal off-diagonal entries h. Then S has rows three, h and h, negative one.

The reflection J is diagonal with entries one and negative one. Multiplying J S J gives a matrix with the same diagonal entries three and negative one, but off-diagonal entries negative h.

Subtract S, and the result has zero diagonal entries and off-diagonal entries negative two h. Its operator norm is two times the absolute value of h.

If h equals zero, the original subspace U remains invariant. If h is nonzero, the new eigenvectors tilt away from the coordinate axes even though the perturbation has zero diagonal compressions.

### Why this structure affects the spectrum

Set c equal to the midpoint between a and b. Consider J multiplied by T minus c times the identity.

On U, both J and T minus c are positive in the sense needed for the quadratic form, because T is at least b. On U perpendicular, both factors change sign: J is negative, and T minus c is at most a minus c, a negative number. Their product is again positive.

More precisely, the real part of the inner product of J times T minus c with a vector is at least half the gap times the squared length of that vector.

Now add the off-diagonal perturbation H. Since H anticommutes with self-adjoint J, the product J H is skew-adjoint. Its quadratic form has zero real part.

Therefore the same positive lower bound holds for the real part of J times S minus c. The off-diagonal perturbation cannot cancel the positive real part that comes from the diagonal block gap.

This observation is the starting point for spectral repulsion. For every real point strictly between a and b, we can repeat the midpoint argument with that point as the center and obtain a positive lower bound. In finite dimensions S therefore has no eigenvalue inside the open gap.

The resulting gap protection is one ingredient in selecting a specific perturbed spectral subspace and proving that it lies on the small-angle branch.

### Distinguish two reflections

The same construction applies to a reducing subspace V of another operator S: write J V for reflection through V.

Since V reduces S, J V commutes with S. Thus J V S J V equals S.

Rearrange S equals T plus H. We obtain J V T J V minus T equals H minus J V H J V. Its norm is at most twice the norm of H, since reflection preserves unitarily invariant norms.

The quantity J V T J V minus T is called the mirror defect of T through V. It is small whenever H is small. It will provide the right-hand side of the sine-two-theta theorem.

This second reflection is the bridge between an operator perturbation and a geometric doubled angle. The first reflection exposed the off-diagonal structure; the second transports an exact reducing subspace across a perturbed symmetry.

### Why the distinction matters

The sine-two-theta theorem does not require the perturbation itself to be off-diagonal. It uses a two-block gap and a mirror-defect estimate that works for any self-adjoint perturbation.

The tangent-two-theta theorem has a stronger geometric conclusion: the selected subspaces remain on the branch strictly below forty-five degrees. The off-diagonal hypothesis is what supplies that conclusion in its classical form.

In a principal plane, reflecting one line across another doubles the angle between their directions. The block reflection converts that planar identity into an operator estimate for the doubled principal angles; spectral selection is an additional requirement when a tangent bound is sought.

## Doubled angles from symmetry

Place a horizontal line through the origin and a second line inclined at thirty degrees. Reflect a point on the horizontal line across the inclined line. Its image lands on the line at sixty degrees: the reflection has doubled the original angle.

This is an elementary fact of plane geometry. But it has an operator-theoretic form that remains meaningful when two subspaces have several principal angles rather than a single direction. Every closed subspace has an orthogonal projection. Twice that projection minus the identity acts by plus one along the subspace and minus one perpendicular to it. That is reflection across the subspace.

If we use the tilted line for the reflection, the horizontal line moves to another line. In the plane, its angular displacement doubles. In a general Hilbert space, the principal-angle sine operator for the reflected subspace is the sine of twice the original angle operator, with the usual care about the selected directed or ambient representation.

We will compute the projection matrices in the plane, then translate the calculation into a coordinate-free identity. The point of doubling is that a reflected operator can sometimes be compared with the original operator using a smaller algebraic expression. A perturbation estimate for that comparison can then control the doubled sine.

### Reflect the horizontal axis across a tilted line

Start in the real plane. Let U be the horizontal axis. Let V be the line making an angle theta counterclockwise from U, with theta between zero and ninety degrees.

A reflection across V fixes the vectors along V and reverses the perpendicular vectors. We can derive its matrix by choosing the unit vector v with coordinates cosine theta and sine theta.

Projection onto V is the rank-one matrix formed from v times its transpose. Its entries are cosine squared theta, sine theta cosine theta, and sine squared theta in the familiar symmetric pattern.

The reflection is twice that projection minus the identity. Using the double-angle identities, its matrix has first row cosine twice theta and sine twice theta, and second row sine twice theta and negative cosine twice theta.

Apply this reflection to the horizontal unit vector. The result has coordinates cosine twice theta and sine twice theta. Therefore the reflected line has oriented angle twice theta relative to U.

The ordinary acute angle between two unoriented lines may fold back after ninety degrees, but the magnitude of the sine of that angle remains the magnitude of sine twice theta. Because theta lies between zero and ninety degrees, sine twice theta is nonnegative.

### Turn the geometry into a difference of projections

Let P be the orthogonal projection onto U, and let J be reflection through V. The projection onto the reflected subspace J U is J P J, because J is an isometry and its inverse equals itself.

Define the projection difference D equal to J P J minus P. It is self-adjoint. In the two-dimensional principal plane, the eigenvalues of D are plus sine twice theta and minus sine twice theta.

One way to see this without solving a characteristic polynomial is to square D. Direct multiplication using the reflection matrix gives D squared equal to sine squared twice theta times the identity.

The modulus of D is the positive square root of D squared. It therefore equals sine twice theta times the identity on that principal plane.

So the positive operator that measures sine twice the angle is precisely the modulus of the displacement of P under reflection through V.

This identity is more informative than a statement about maximum angles. It identifies an actual operator, and therefore determines every singular value and every unitarily invariant norm.

### Repeat the calculation using a cosine–sine block

In a principal plane for two subspaces U and V, the projection P onto U has matrix with one on the first diagonal entry and zero on the second.

The projection Q onto V has entries cosine squared theta, sine theta cosine theta in the two off-diagonal positions, and sine squared theta.

The reflection J equals twice Q minus the identity. Multiply J P J. The resulting projection is the one onto the line spanned by the vector with coordinates cosine twice theta and sine twice theta.

The eigenvalues of the difference J P J minus P are therefore plus and minus sine twice theta. This verifies the reflection identity directly from the cosine–sine decomposition.

An orthogonal direct sum of principal planes repeats this calculation independently. On each plane, the positive modulus contributes sine twice the corresponding principal angle. Degenerate intersection and perpendicular blocks contribute zero.

The full-space operator has repeated singular values on each nontrivial principal plane. A directed coordinate block may record each principal angle only once. We must keep these conventions distinct when comparing Frobenius or nuclear norms.

### A coordinate-free operator identity

The same result can be proved without choosing a principal-vector basis.

Let S be the positive sine-angle operator, the modulus of P minus Q. Its spectrum lies between zero and one. The positive angle operator Theta can be defined by applying arcsine to S.

Now apply the scalar function sine of twice the angle to Theta. Since the spectrum of Theta lies between zero and pi over two, this produces a positive operator.

The scalar identity says that sine squared of twice theta equals four times sine squared theta times one minus sine squared theta.

On the operator side, the square of the sine-two-theta operator is therefore four times S squared minus four times S to the fourth power. The two factors commute because both are functions of S.

Independently, expand the square of J P J minus P using only P squared equals P, Q squared equals Q, and their self-adjointness. Its square is exactly the same polynomial in S.

Both the sine-two-theta operator and the modulus of the projection difference are positive. They have the same square. By uniqueness of the positive square root, they are equal.

This is the coordinate-free reflection double-angle identity. The functional-calculus identity applies in the complex Hilbert-space setting, with corresponding real formulations.

### Check the two extreme angles

If theta is zero, U and V coincide. Reflection through V leaves U unchanged, so the displaced projection is zero. Sine of zero is zero, as expected.

If theta is ninety degrees, V is perpendicular to U. Reflection through V sends a vector of U to its negative, which spans the same line U. Again the displaced projection is zero. Sine of one hundred eighty degrees is zero.

At forty-five degrees, the reflected horizontal line is vertical. The projection difference has norm one, and sine twice theta equals one.

The three tests show that the doubled sine is not a monotone measure of the original angle across the entire interval from zero to ninety degrees. It increases up to forty-five degrees, then decreases.

This branch ambiguity will be crucial when we interpret perturbation estimates. A small doubled sine may mean that two subspaces are nearly equal, but it may also mean that they are nearly perpendicular.

### Why reflection helps a perturbation theorem

Suppose T is self-adjoint and U reduces T. Suppose S equals T plus H, and V reduces S. Reflection through V commutes with S, even though it need not commute with T.

The mirror defect J V T J V minus T equals H minus J V H J V. Its norm is at most twice the norm of H in any compatible unitarily invariant norm.

The reflected operator J V T J V has a reducing subspace J V U, because U reduces T. We can now apply a single-angle sine comparison to T and its reflected copy, provided the spectral separation hypotheses match.

But the angle between U and the reflected U is encoded by the sine-two-theta operator we have just constructed. Thus reflection converts a doubled-angle question for U and V into a single-angle question for a reflected pair.

The algebra explains both the doubled angle and the factor of two in the perturbation norm. Neither is an arbitrary feature of the statement.

### What to retain

The key geometric identity is: positive sine of twice the operator angle equals the modulus of the difference between the projection onto U and the projection onto U reflected through V.

It works across the full angle range, including right angles, because the sine is nonnegative on twice that range. It does not, by itself, choose the near-zero branch.

The outcome is the sine-two-theta theorem, with a bound valid even when the permitted geometry has not yet identified which branch of the doubled sine is relevant.

## The sine-two-theta theorem

Take a symmetric two-by-two matrix whose eigenvalues are minus one and one. Its two eigenspaces are the horizontal and vertical axes, with a spectral gap of two. Add a symmetric coupling h between the axes. The eigenvectors rotate, and the rotation angle theta is governed by twice theta: elementary diagonalization gives tangent of twice theta equal to h in absolute value.

Reflection supplies a route to an inequality without first diagonalizing the perturbed matrix. Reflect through a reducing subspace of the perturbed operator. That reflection preserves the perturbed operator, while the difference between the reflected original operator and the original is controlled by twice the size of the perturbation. A single-angle estimate applied to the reflected pair becomes a bound for the sine of twice the principal angle.

The setting is a self-adjoint original operator with an ordered form gap between the restrictions to an exact reducing subspace and its orthogonal complement. The perturbed operator is also self-adjoint, and a chosen reducing subspace of it is compared with the exact one. The spectral-gap predicate, rather than just an arbitrary pairwise distance, permits the estimate.

The resulting inequality is quantitative, but it has a built-in ambiguity: sine of twice an angle is small near zero and again near ninety degrees. We will derive the bound and then exhibit why an independent spectral-selection argument is needed before treating a small doubled sine as evidence of a small original angle.

### Set up the operators and reducing subspaces

Work first in a finite-dimensional real or complex inner-product space. Let T be self-adjoint, and let U be a reducing subspace for T.

Assume there are real numbers a and b, with a less than b, such that T is at least b in quadratic-form order on U and at most a on U perpendicular. This places its two diagonal blocks on opposite sides of an ordered gap delta equal to b minus a.

Now perturb T to another self-adjoint operator S equal to T plus H. Choose a reducing subspace V for S. At this stage, we do not need to assume that H is off-diagonal relative to U.

The theorem bounds the ambient positive sine-two-theta operator between U and V, measured in any supported unitarily invariant norm, by twice the norm of H divided by delta.

Notice what is not in the hypotheses. V need not have been described as the graph of a small operator. We have not assumed the principal angles are below forty-five degrees. The theorem's conclusion uses a function of the angle that makes sense over the entire interval from zero to ninety degrees.

### Reflect through the perturbed reducing space

Let J be the reflection through V, equal to twice its orthogonal projection minus the identity.

Because V reduces S and S is self-adjoint, J commutes with S. Thus J S J equals S.

Replace S by T plus H. We obtain J T J plus J H J equals T plus H. Rearranging gives J T J minus T equal to H minus J H J.

The norm of J H J equals the norm of H in every unitarily invariant norm because J is unitary. The triangle inequality therefore yields that the norm of J T J minus T is at most twice the norm of H.

This is the mirror defect bound. It is the only place where the perturbation appears on the right side of our proof.

### What is the reflected spectral subspace?

Define T prime as J T J. Since J is an isometry and U reduces T, the reflected subspace J U also reduces T prime. The reflected complement J U perpendicular reduces T prime as well.

Furthermore, the quadratic-form spectral bounds are preserved by this unitary conjugation. T prime has the same upper and lower block spectra as T, merely transported by J.

Thus the single-angle sine theorem can be applied to a suitable crossed pair of reducing subspaces: one belonging to T and the other to T prime. One block lies above b, the other below a, so the gap remains delta.

The resulting cross-projection norm is bounded by the norm of T prime minus T divided by delta.

Which cross projection do we obtain? Project from U onto the reflected perpendicular subspace J U perpendicular. In a principal plane, that projection has magnitude sine twice theta, where theta is the angle between U and V.

This is exactly the reflected overlap given by composing the reflected projections. The relevant ambient positive operator, after matching the polar and singular-value representations, is sine of twice the angle operator.

### Put the two inequalities together

The single-angle theorem for the reflected pair yields delta times the norm of the sine of twice theta at most the norm of the mirror defect J T J minus T.

The mirror defect bound yields that this norm is at most twice the norm of H.

Combining them gives the result: delta times the unitarily invariant norm of the sine of twice theta is at most two times the unitarily invariant norm of the perturbation.

For operator norm, this controls the largest value of sine twice a principal angle, not necessarily twice the largest angle itself. For a Frobenius or Ky Fan norm, we must account for the complete singular-value list of the ambient angle operator. The formal theorem does so through the full-space angle representation and the corresponding unitarily invariant norm.

This norm inequality is stated for finite-dimensional unitarily invariant seminorms. In infinite-dimensional symmetric ideals the same conclusion requires the appropriate membership, domain, and spectral-separation hypotheses.

### Examine a two-by-two perturbation

Take the real plane with T diagonal, having entries negative one and one. Choose U to be the upper eigenspace, the vertical line. Then the quadratic-form gap is two.

Let H be symmetric with zero diagonal and off-diagonal entries h. The perturbed operator S has rows negative one, h and h, one.

The upper eigenvector of S rotates away from the vertical line through an angle theta satisfying tangent twice theta equals h. For now, recall the equivalent relation: sine twice theta equals the absolute value of h divided by the square root of one plus h squared.

The sine-two-theta inequality reads two times sine twice theta at most twice times the absolute value of h. This holds because the square root of one plus h squared is at least one.

For small h, the ratio between the two sides approaches one. Thus the factor two in this normalization cannot be uniformly reduced in the perturbation theorem even though equality need not hold for a nonzero finite h.

At h equal to one, theta equals twenty-two point five degrees. Sine twice theta is the square root of two divided by two. The left side is the square root of two and the right side is two.

As the coupling becomes larger, theta approaches forty-five degrees and sine twice theta approaches one. The estimate becomes less restrictive, because its right-hand side grows without bound.

### A different example shows the branch ambiguity

Take two perpendicular lines U and V in the same plane. Their principal angle is ninety degrees. Sine twice that angle is zero.

So the doubled-sine operator vanishes even though the projection difference has norm one, the maximum possible value.

The theorem therefore cannot by itself certify that V is close to U. A small right-hand side may indicate closeness, but without information selecting the relevant branch, the same small doubled sine is consistent with an almost perpendicular pair.

This is a statement about the information carried by the left-hand side, not a defect in the proof. The function sine twice theta loses the distinction between angles near zero and angles near ninety degrees.

Later spectral-selection results will supply conditions that choose the intended branch.

### Compare with the single-angle sine theorem

The single-angle sine theorem typically uses a residual and a gap between a trial operator and the unwanted exact spectrum. Its angle is directed from the trial space toward the exact subspace.

The sine-two-theta theorem uses a two-block form gap for one exact operator and a perturbation difference between two self-adjoint operators. Its angle is the ambient angle between two reducing subspaces.

The formulas can look similar, but their inputs are different. One cannot simply substitute a residual in place of the full perturbation or replace the two-block gap with an arbitrary pairwise distance.

In the special off-diagonal setting, the two-block structure has an additional consequence: it prevents the selected spectral subspace from rotating beyond forty-five degrees. That extra information makes it possible to divide the doubled sine by a positive doubled cosine and obtain a tangent theorem.

### The theorem we have proved

We began with a self-adjoint T whose reducing subspace U lies on one side of a form gap, and a self-adjoint perturbation S with reducing subspace V. Reflection through V turned T into a nearby operator with a reflected reducing subspace. The ordinary sine theorem controlled that reflected overlap. The reflection identity identified it with the sine of twice the original angle.

The result has a clean constant and accommodates arbitrary angles, but it does not select the near-zero branch.

A bound on the doubled sine alone does not rule out angles close to ninety degrees. To deduce a doubled-tangent bound, one needs additional conditions selecting the spectral branch and keeping every relevant angle strictly below forty-five degrees. Off-diagonal perturbations with appropriately matched spectral subspaces provide one such setting.

## The tangent-two-theta theorem

Take a diagonal symmetric matrix with an upper eigenvalue b and a lower eigenvalue a, separated by a positive gap. Add a coupling h that is purely off-diagonal in the decomposition into their eigenspaces. The eigenvectors rotate, but the two spectral branches remain distinguishable.

In the plane, diagonalizing the new matrix shows that the rotation angle theta of the upper eigenspace satisfies tangent of twice theta equal to two times the absolute coupling divided by the gap. For a gap of two and a coupling of one, the angle is twenty-two and a half degrees. Its doubled tangent is exactly one.

Why is this stronger than a doubled-sine estimate? Because tangent of twice theta becomes unbounded as theta approaches forty-five degrees. To use it, we must first establish that the relevant spectral subspace really stays on the branch with angles below forty-five degrees. Off-diagonality and the ordered block gap are the structural facts that make this possible.

We will prove spectral selection, represent the perturbed subspace as a graph, and then obtain the tangent estimate from its invariance equation. Along the way, the two-dimensional computation will identify both the sharp constant and the branch restriction. Neither conclusion follows from the doubled-sine inequality alone.

### State the strong hypotheses

Let T be self-adjoint on a finite-dimensional Hilbert space H. Let U reduce T. Assume the quadratic form of T on U is at least b times squared length, and its form on U perpendicular is at most a times squared length, with b greater than a.

Write delta for b minus a. Perturb T by a self-adjoint operator H zero whose diagonal compressions onto U and onto U perpendicular both vanish. Denote the new operator by S.

Let V be the upper reducing subspace selected from S. To make the theorem precise, assume the quadratic form of S on V is at least b, and on V perpendicular at most a. The source states the theorem with these matched bounds; when V is chosen from spectral subspaces, a separate spectral-repulsion result provides them.

Suppose H zero has operator norm at most epsilon.

Then the maximal angle theta between U and V is strictly less than forty-five degrees, and delta times tangent of twice theta is at most twice epsilon.

This is an operator-norm theorem under the stated finite-dimensional hypotheses. We should not automatically promote it to every symmetric ideal norm without using a separately proved result.

### Derive the exact planar formula

Take T diagonal with entries b and a, where b is greater than a. Let the perturbation H zero have zero diagonal and off-diagonal entries h. Then S has rows b, h and h, a.

Consider an eigenvector for the upper eigenvalue, making an angle theta from the first coordinate axis. To diagonalize S, use an ordinary plane rotation. The off-diagonal entry in the rotated matrix is h times cosine twice theta minus half of b minus a times sine twice theta, with the sign depending on the orientation of the rotation.

Setting that entry equal to zero gives tangent twice theta equal to two h divided by delta, with an appropriate choice of oriented theta. The acute absolute-angle version replaces h by its absolute value.

Because arctangent of a finite nonnegative number lies below ninety degrees, theta equals half of that arctangent and is strictly below forty-five degrees.

The perturbation norm is the absolute value of h. Therefore delta times tangent twice theta equals twice the perturbation norm. The factor two is exactly sharp in this model.

Unlike the sine-two-theta estimate, which approached equality only as h tended to zero, the tangent-two-theta estimate attains equality for every positive h in this planar family.

### How do we know the upper space stays on the correct branch?

We need a reason that does not depend on diagonalizing a two-by-two matrix. Let P be projection onto U and let J equal twice P minus the identity.

Center T at the midpoint c of a and b. The form-gap hypothesis gives a coercive inequality: the real part of the inner product of J times T minus c with x is at least half delta times the squared norm of x.

Because the perturbation is off-diagonal, J H zero is skew-adjoint. Its quadratic form has zero real part. So the same coercive lower bound holds with S in place of T.

This bound first proves spectral repulsion: no eigenvector of S can have an eigenvalue in the open gap. Replacing the center c by any point between a and b gives the required contradiction. In finite dimensions, the gap contains no spectrum.

To select a subspace, choose V from the upper spectrum of S and let K be S minus c restricted to V. K is positive and bounded below by half delta.

Take any nonzero x in V, and evolve it by the decaying semigroup generated by K. Call the evolving vector y of time t. It stays in V and tends to zero as time grows.

Consider its reflected quadratic form: the real inner product of J y with y. Its time derivative is negative twice the real inner product of J K y with y. By our coercive inequality, this derivative is at most negative delta times the squared norm of y.

Integrate from time zero to infinity. The final reflected quadratic form vanishes. Hence the initial value is at least delta times the integral of the squared norm of y, which is strictly positive for nonzero x.

But the reflected quadratic form of x is exactly the squared norm of its U component minus the squared norm of its perpendicular component.

Therefore every nonzero vector of V has a strictly larger U component than perpendicular component. In finite dimensions this uniform positivity means the largest principal angle between V and U is below forty-five degrees. It also makes V a graph over U when the dimensions match, as they do for the selected upper spectral branch.

### Derive the sharp graph inequality

Represent V as the graph of an operator Z from U into U perpendicular. The strict branch conclusion gives operator norm Z less than one. Its singular values are tangents of the principal angles.

Relative to U plus U perpendicular, write T as diagonal blocks A plus and A minus. Write the off-diagonal perturbation using K and K adjoint. Thus S has upper-right block K adjoint and lower-left block K.

A graph vector has components u and Z u. The condition that its image under S remains on the graph yields a Riccati equation. In words: K plus A minus Z equals Z A plus plus Z K adjoint Z.

This equation contains both linear Sylvester terms and a quadratic correction from the off-diagonal coupling.

Take a unit right singular vector u of Z associated with the largest singular value t. Let v be its corresponding unit left singular vector. Then Z u equals t v and Z adjoint v equals t u.

Pair the Riccati equation applied to u with v and take real parts. The diagonal terms contribute t times the difference between a Rayleigh quotient of A plus and a Rayleigh quotient of A minus. That difference is at least delta.

The two off-diagonal terms combine into one minus t squared times the real part of the scalar pairing of v with K u.

Therefore delta times t is at most epsilon times one minus t squared. The sign is legitimate because the branch proof already established t less than one.

Rearrange and multiply by two. The scalar identity tangent twice theta equals twice tangent theta divided by one minus tangent squared theta now yields delta times tangent twice theta is at most twice epsilon, where theta is the largest principal angle.

This completes the finite-dimensional operator-norm argument. An equivalent route works with a maximal eigenvector in the permitted angular sector and controls the projection difference directly, avoiding a choice of graph coordinates.

### Interpret the cosine denominator

The difference between the doubled sine and doubled tangent is the denominator cosine twice theta.

For angles below forty-five degrees, cosine twice theta is positive. We can therefore pass from a bound on sine twice theta to a bound on tangent twice theta only if we can control that denominator. The off-diagonal spectral structure supplies the required positivity, and the graph argument obtains the sharp quantitative comparison.

At forty-five degrees the denominator vanishes. The theorem says that no finite off-diagonal perturbation satisfying its hypotheses reaches that angle. A family can approach it as the coupling grows, but never attain it at finite size.

This is a structural statement about a selected spectral branch. It is not true for an arbitrary reducing subspace chosen without regard to which side of the gap it occupies.

### Compare the two double-angle theorems

The sine-two-theta theorem needs a two-block gap for T and reducing subspaces for T and S. It allows a general self-adjoint perturbation and gives delta times a doubled-sine norm at most twice the perturbation norm.

The tangent-two-theta theorem adds off-diagonality, matching upper and lower spectral bounds for the selected perturbed subspace, and an operator-norm control. It gives both an angle strictly below forty-five degrees and the sharp doubled-tangent inequality.

The stronger conclusion costs stronger hypotheses. It cannot be obtained simply by dividing the sine estimate by cosine twice theta without proving the branch and controlling that cosine.

### A final numerical check

Let delta equal two and let the coupling h equal one. The formula gives tangent twice theta equal one, so theta is twenty-two point five degrees.

Then cosine twice theta and sine twice theta both equal the square root of two divided by two. The sine-two-theta estimate gives two times approximately zero point seven zero seven at most two. The tangent-two-theta estimate gives two times one at most two, with equality.

As h increases to ten, tangent twice theta equals ten and theta approaches forty-five degrees from below. The doubled sine becomes close to one, while the doubled tangent records the increasing difficulty of maintaining a graph with slope below one.

The sharp doubled-tangent estimate is therefore a joint statement about a perturbation and the correctly selected spectral subspace. The spectral branch proof establishes that the cosine of twice every relevant angle is positive; the Riccati estimate then controls its reciprocal effect quantitatively.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Off-diagonal perturbations and block reflection

**Draft status:** audio-first mathematical lecture. **Prerequisites:** `015000–016000` reducing subspaces and blocks, `043000–045000` projection geometry, `049000` direct rotation. **Next:** `115000` doubled angles from symmetry.

---

#### Companion: mathematics and Lean correspondence (display only)

##### Exact two-block pinching

For \(A=\left(\begin{smallmatrix}-1&h\\h&1\end{smallmatrix}\right)\)
and \(J=\operatorname{diag}(1,-1)\),
\[
\tfrac12(A+JAJ)=\operatorname{diag}(-1,1),\qquad
\tfrac12(A-JAJ)=\begin{pmatrix}0&h\\h&0\end{pmatrix}.
\]
The first expression is diagonal pinching; the second is the
purely off-diagonal part relative to the chosen decomposition.

For `P=P_U`, `Q=I-P`, `J=P-Q`, and `S=T+H`, with `U` reducing self-adjoint `T`,

\[J^*=J,\quad J^2=I,\quad JTJ=T.\]

Off-diagonal `H` means `PHP=QHQ=0`, equivalently `JHJ=-H`; hence `JSJ-S=-2H`. For any reducing `V` of self-adjoint `S`, `J_V S J_V=S`, so

\[J_V T J_V-T=H-J_VHJ_V,\qquad N(J_V T J_V-T)\le 2N(H).\]

The source distinguishes the finite block-reflection algebra from the general mirror-defect inequality; the latter requires the reducing comparison operator.

##### Source declaration excerpts

`DavisKahan/FiniteDimensional/DoubleAngle/TanTheta.lean` — `starProjection_comp_comp_starProjection_eq_zero` (exact declaration header; body omitted):

```lean
theorem starProjection_comp_comp_starProjection_eq_zero
    (U : Submodule 𝕜 E) [U.HasOrthogonalProjection] {H : E →ₗ[𝕜] E}
    (hH : ∀ u ∈ U, ∀ u' ∈ U, ⟪u, H u'⟫_𝕜 = 0) :
    (U.starProjection : E →ₗ[𝕜] E) ∘ₗ H ∘ₗ (U.starProjection : E →ₗ[𝕜] E) = 0 := by
```

`DavisKahan/BoundedOperator/Reflection.lean` — `reflectionDefect` (exact declaration header; body omitted):

```lean
noncomputable def reflectionDefect (U : Submodule 𝕜 E)
    [U.HasOrthogonalProjection] (A : E →L[𝕜] E) : E →L[𝕜] E :=
```

`DavisKahan/BoundedOperator/Reflection.lean` — `reflectionOperator_comp_reflectionDefect` (exact declaration header; body omitted):

```lean
theorem reflectionOperator_comp_reflectionDefect
    (U : Submodule 𝕜 E) [U.HasOrthogonalProjection] (A : E →L[𝕜] E) :
    U.reflectionOperator ∘L reflectionDefect U A =
      -(reflectionDefect U A ∘L U.reflectionOperator) := by
```

`DavisKahan/BoundedOperator/Reflection.lean` — `norm_reflectionDefect_le_two_mul` (exact declaration header; body omitted):

```lean
theorem norm_reflectionDefect_le_two_mul
    (A B : E →L[𝕜] E) (V : Submodule 𝕜 E)
    [V.HasOrthogonalProjection] (hV : Submodule.IsReducing V B) :
    ‖reflectionDefect V A‖ ≤ 2 * ‖A - B‖ := by
```

**Mapping.** `starProjection_comp_comp_starProjection_eq_zero` formalizes vanishing diagonal compressions. `reflectionDefect` uses a continuous linear map and is zero for an operator reduced by the reflecting subspace. `norm_reflectionDefect_le_two_mul` is the norm estimate used by the doubled-angle perturbation proof. The finite two-block form gap appears in `sin_two_theta_reflection_le`.

### Doubled angles from symmetry

**Draft status:** audio-first mathematical lecture. **Prerequisites:** `042000–045000` principal angles, CS blocks, and projections; `114000` block reflections. **Next:** `116000` the sine-two-theta theorem.

---

#### Companion: mathematics and Lean correspondence (display only)

##### The reflection identity in a plane

For \(u_\theta=(\cos\theta,\sin\theta)^T\), let
\(P_\theta=u_\theta u_\theta^T\) and \(J_\theta=2P_\theta-I\).
Then
\[
J_\theta e_1=
\begin{pmatrix}\cos(2\theta)\\\sin(2\theta)\end{pmatrix}.
\]
At \(\theta=30^\circ\), this is a sixty-degree direction.
This identity is the scalar model for the doubled-angle operator
obtained by reflecting a subspace.

Let `P=P_U`, `Q=P_V`, `J_V=2Q-I`, and `Θ=arcsin |P-Q|` (ambient positive angle). The operator identity is

\[\sin(2\Theta)=|J_V P J_V-P|=|P_{J_VU}-P_U|.\]

In each nondegenerate principal plane, `|J_V P J_V-P| = sin(2θ) I`. In ambient coordinates, every plane contributes twice to the singular-value list; a directed sine block generally contributes once. For `θ∈[0,π/2]`, `sin(2θ)≥0` but is not injective as a function of `θ`.

##### Source declaration excerpts

`DavisKahan/Geometry/Angle/DoubleAngleFunctionalCalculus.lean` — `sinTwoAngleOperatorC` (exact declaration header; body omitted):

```lean
noncomputable def sinTwoAngleOperatorC (U V : Submodule ℂ E)
    [U.HasOrthogonalProjection] [V.HasOrthogonalProjection] : E →L[ℂ] E :=
```

`DavisKahan/Geometry/Angle/DoubleAngleFunctionalCalculus.lean` — `starProjection_map_reflection_eq` (exact declaration header; body omitted):

```lean
theorem starProjection_map_reflection_eq (U V : Submodule ℂ E)
    [U.HasOrthogonalProjection] [V.HasOrthogonalProjection] :
    (U.map (V.reflection.toLinearEquiv : E →ₗ[ℂ] E)).starProjection =
      V.reflectionOperator * U.starProjection * V.reflectionOperator := by
```

`DavisKahan/Geometry/Angle/DoubleAngleFunctionalCalculus.lean` — `directedSinTwoAngleOperatorC_eq_modulus_reflect` (exact declaration header; body omitted):

```lean
theorem directedSinTwoAngleOperatorC_eq_modulus_reflect :
    sinTwoAngleOperatorC U V =
      (V.reflectionOperator * U.starProjection * V.reflectionOperator -
        U.starProjection).modulus := by
```

**Mapping.** `sinTwoAngleOperatorC` uses functional calculus on the ambient positive angle; `starProjection_map_reflection_eq` expresses projection conjugation; `directedSinTwoAngleOperatorC_eq_modulus_reflect` identifies the full positive doubled-sine operator, not merely its operator norm. The formal theorem's types and complete Hilbert-space assumptions are retained in the excerpts.

### The sine-two-theta theorem

**Draft status:** audio-first mathematical lecture. **Prerequisites:** `110000` the sine theorem, `114000` block reflection, `115000` doubled-angle identity. **Next:** `117000` the tangent-two-theta theorem.

---

#### Companion: mathematics and Lean correspondence (display only)

##### An exact off-diagonal two-level formula

For
\[
S=\begin{pmatrix}-1&h\\h&1\end{pmatrix},
\qquad \sigma(S)=\{-\sqrt{1+h^2},\sqrt{1+h^2}\},
\]
the acute rotation angle \(\theta\) of the negative spectral branch
from the horizontal axis satisfies
\(\tan(2\theta)=|h|\) and
\(\sin(2\theta)=|h|/\sqrt{1+h^2}\).
The ordered diagonal gap of the unperturbed matrix is two;
consequently \(2\sin(2\theta)\le2|h|\), with equality in the
zero-coupling limit to first order.

For finite-dimensional self-adjoint `T,S`, `H=S-T`, reducing `U` of `T` and reducing `V` of `S`, and a two-block form gap `T|U ≥ b`, `T|Uᗮ ≤ a` (`δ=b-a>0`), the canonical ambient theorem is

\[(b-a)\,N(\sin(2\Theta(U,V)))\le 2N(S-T).\]

Let `J=J_V`. Because `J S J=S`, `J T J-T=H-JHJ`, whence `N(J T J-T)≤2N(H)`. Applying the cross-subspace sine comparison to `T` and `J T J` and identifying `|J P_U J-P_U|=sin(2Θ)` supplies the conclusion. No off-diagonal hypothesis on `H` is required. The full ambient-angle norm and directed coordinate norms should not be silently interchanged.

##### Source declaration excerpts

`DavisKahan/FiniteDimensional/DoubleAngle/SinTheta.lean` — `sin_two_theta_reflection_le` (exact declaration header; body omitted):

```lean
theorem sin_two_theta_reflection_le (N : UnitarilyInvariantSeminorm 𝕜 E E)
    (hT : T.IsSymmetric) {U W : Submodule 𝕜 E}
    [U.HasOrthogonalProjection] [W.HasOrthogonalProjection]
    (hUinv : ∀ x ∈ U, T x ∈ U) {a b : ℝ} (hab : a < b)
    (hUb : ∀ x ∈ U, b * ‖x‖ ^ 2 ≤ RCLike.re ⟪T x, x⟫_𝕜)
    (hUa : ∀ x ∈ Uᗮ, RCLike.re ⟪T x, x⟫_𝕜 ≤ a * ‖x‖ ^ 2) :
    2 * N ((Uᗮ.starProjection ∘L W.starProjection ∘L U.starProjection
        : E →L[𝕜] E) : E →ₗ[𝕜] E)
      ≤ N (W.reflection.toLinearMap ∘ₗ T ∘ₗ W.reflection.toLinearMap - T)
        / (b - a) := by
```

`DavisKahan/FiniteDimensional/DoubleAngle/SinTheta.lean` — `sinTwoTheta_perturbation_le` (exact declaration header; body omitted):

```lean
theorem sinTwoTheta_perturbation_le
    (N : UnitarilyInvariantSeminorm 𝕜 E E)
    {A B : E →ₗ[𝕜] E} (hA : A.IsSymmetric) (hB : B.IsSymmetric)
    {U V : Submodule 𝕜 E} [U.HasOrthogonalProjection]
    [V.HasOrthogonalProjection] (hU : (U ∈ Module.End.invtSubmodule A)) (hV : (V ∈
        Module.End.invtSubmodule B))
    {a b : ℝ} (_hab : a < b) (hgap : TwoBlockFormGap A U a b) :
    (b - a) * N ((U.sinTwoAngleOperator V).toLinearMap) ≤ 2 * N (B - A) := by
```

`DavisKahan/FiniteDimensional/DoubleAngle/SinTheta.lean` — `opNorm_sinTwoTheta_le` (exact declaration header; body omitted):

```lean
theorem opNorm_sinTwoTheta_le
    {A B : E →ₗ[𝕜] E} (hA : A.IsSymmetric) (hB : B.IsSymmetric)
    {U V : Submodule 𝕜 E} [U.HasOrthogonalProjection]
    [V.HasOrthogonalProjection] (hU : (U ∈ Module.End.invtSubmodule A)) (hV : (V ∈
        Module.End.invtSubmodule B))
    {a b : ℝ} (hab : a < b) (hgap : TwoBlockFormGap A U a b) :
    (b - a) * ‖(U.sinTwoAngleOperator V)‖ ≤
      2 * ‖(B - A).toContinuousLinearMap‖ := by
```

**Mapping.** `sinTwoTheta_perturbation_le` is the finite-dimensional every-UI-norm statement for reducing `U,V`; `sin_two_theta_reflection_le` is the mirror-defect intermediate result. The `opNorm` specialization records the usual maximum singular-angle bound. `TwoBlockFormGap` encodes a form-order gap on both exact blocks rather than a generic distance between two unordered spectral sets.

### The tangent-two-theta theorem

**Draft status:** audio-first mathematical lecture. **Prerequisites:** `111000–112000` graph tangents; `114000–116000` off-diagonal reflection and sine-two-theta. **Next:** `118000` why a small doubled sine proves little alone.

---

#### Companion: mathematics and Lean correspondence (display only)

##### The doubled tangent and the diagonal gap

For \(a<b\), \(\Delta=b-a\), and
\(S=\left(\begin{smallmatrix}a&h\\h&b\end{smallmatrix}\right)\),
the spectral-branch angle \(\theta\in[0,\pi/4)\) satisfies
\[
\tan(2\theta)=\frac{2|h|}{\Delta}.
\]
When \(\Delta=2\) and \(|h|=1\), the angle is \(22.5^\circ\).
This conclusion uses the ordering of the two spectral branches;
without branch selection, tangent alone does not label them.

Let `T=T*` reduce `U`, with `T|U≥b`, `T|Uᗮ≤a`, `δ=b-a>0`. Let `S=T+H=S*` and assume `PHP=(I-P)H(I-P)=0`, `‖H‖≤ε`; let `V` reduce `S` and satisfy the corresponding form bounds on `V` and `Vᗮ`. Then with `t=‖P_U-P_V‖=sin θ_max` the source proves

\[t^2<\tfrac12,\qquad \delta\,2t\sqrt{1-t^2}\le 2\varepsilon(1-2t^2).\]

Equivalently `θ_max<π/4` and `δ tan(2θ_max)≤2ε`. The source theorem is **operator norm** and carries the matched form bounds explicitly. For `T=diag(b,a)` and `H=[[0,h],[h,0]]`, `tan(2θ)=2|h|/(b-a)` yields equality.

The finite-dimensional graph calculation uses `Z:U→Uᗮ`, `‖Z‖=tangent θ_max<1`, and the Riccati equation `K + A_- Z = Z A_+ + Z K* Z`. A maximizing singular pair yields `δt ≤ ‖K‖(1-t²)`, hence the double-tangent bound. Source proof uses a basis-free maximal-eigenvector/sectorial argument.

##### Source declaration excerpts

`DavisKahan/FiniteDimensional/DoubleAngle/TanTheta.lean` — `starProjection_comp_comp_starProjection_congr` (exact declaration header; body omitted):

```lean
theorem starProjection_comp_comp_starProjection_congr
    (U : Submodule 𝕜 E) [U.HasOrthogonalProjection] {S T : E →ₗ[𝕜] E}
    (h : ∀ u ∈ U, ∀ u' ∈ U, ⟪u, S u'⟫_𝕜 = ⟪u, T u'⟫_𝕜) :
    (U.starProjection : E →ₗ[𝕜] E) ∘ₗ S ∘ₗ (U.starProjection : E →ₗ[𝕜] E)
      = (U.starProjection : E →ₗ[𝕜] E) ∘ₗ T ∘ₗ (U.starProjection : E →ₗ[𝕜] E) := by
```

`DavisKahan/FiniteDimensional/DoubleAngle/TanTheta.lean` — `eigenvalue_notMem_gap_of_diagonal_form` (exact declaration header; body omitted):

```lean
theorem eigenvalue_notMem_gap_of_diagonal_form (hS : S.IsSymmetric)
    {U : Submodule 𝕜 E} [U.HasOrthogonalProjection] {a b : ℝ}
    (hUb : ∀ u ∈ U, b * ‖u‖ ^ 2 ≤ RCLike.re ⟪S u, u⟫_𝕜)
    (hUa : ∀ w ∈ Uᗮ, RCLike.re ⟪S w, w⟫_𝕜 ≤ a * ‖w‖ ^ 2)
    {x : E} (hx : x ≠ 0) {μ : ℝ} (hμ : S x = (μ : 𝕜) • x) :
    μ ≤ a ∨ b ≤ μ := by
```

`DavisKahan/FiniteDimensional/DoubleAngle/TanTheta.lean` — `tan_two_theta_norm_sub_le` (exact declaration header; body omitted):

```lean
theorem tan_two_theta_norm_sub_le (hT : T.IsSymmetric) (hS : S.IsSymmetric)
    {U V : Submodule 𝕜 E} [U.HasOrthogonalProjection] [V.HasOrthogonalProjection]
    (hUinv : ∀ x ∈ U, T x ∈ U) (hVinv : ∀ x ∈ V, S x ∈ V)
    {a b ε : ℝ} (hab : a < b) (hε0 : 0 ≤ ε)
    (hUb : ∀ x ∈ U, b * ‖x‖ ^ 2 ≤ RCLike.re ⟪T x, x⟫_𝕜)
    (hUa : ∀ x ∈ Uᗮ, RCLike.re ⟪T x, x⟫_𝕜 ≤ a * ‖x‖ ^ 2)
    (hVb : ∀ x ∈ V, b * ‖x‖ ^ 2 ≤ RCLike.re ⟪S x, x⟫_𝕜)
    (hVa : ∀ x ∈ Vᗮ, RCLike.re ⟪S x, x⟫_𝕜 ≤ a * ‖x‖ ^ 2)
    (hHU : ∀ x ∈ U, ∀ y ∈ U, ⟪x, (S - T) y⟫_𝕜 = 0)
    (hHUperp : ∀ x ∈ Uᗮ, ∀ y ∈ Uᗮ, ⟪x, (S - T) y⟫_𝕜 = 0)
    (hε : ∀ x, ‖(S - T) x‖ ≤ ε * ‖x‖) :
    ‖(U.starProjection - V.starProjection : E →L[𝕜] E)‖ ^ 2 < 1 / 2 ∧
      (b - a) * (2 * ‖(U.starProjection - V.starProjection : E →L[𝕜] E)‖
          * Real.sqrt (1 - ‖(U.starProjection - V.starProjection : E →L[𝕜] E)‖ ^ 2))
        ≤ 2 * ε * (1 - 2 * ‖(U.starProjection - V.starProjection : E →L[𝕜] E)‖ ^ 2) := by
```

**Mapping.** `tan_two_theta_norm_sub_le` assumes self-adjoint `T,S`, both invariant subspaces and their matching form bounds, both vanishing perturbation compressions, and a global norm bound. Its conclusion first proves `‖P_U-P_V‖²<1/2`, then a scalar inequality equivalent to the doubled-tangent estimate. The source's spectral-repulsion theorem discharges the matched perturbed form bounds for the intended spectral selection; the latter are not silently removed from the theorem excerpt.
