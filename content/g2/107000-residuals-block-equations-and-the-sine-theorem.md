# Residuals, block equations, and the sine theorem

<!-- BEGIN SPOKEN LECTURE -->

# Residuals, block equations, and the sine theorem

## Trial spaces, exact subspaces and residuals

A numerical eigensolver gives us a line in the plane and claims it is close to an eigenspace. How can we test that claim using the matrix, without first knowing the exact eigenvector?

Take the symmetric matrix whose rows are zero, one, and one, three. Suppose the algorithm returns the horizontal unit vector. Multiplying by the matrix sends that vector straight upward. The trial line cannot account for the output: the entire transformed vector lies outside it. We have detected a failure of invariance using only one matrix multiplication.

The same experiment works for a trial plane and a much larger matrix, provided we describe the trial plane by orthonormal columns. We compress the matrix to that plane to capture the part of the action that stays inside, and subtract that captured part. The remainder is a residual. Its input lives in the small trial-coordinate space; its output lives in the original ambient space.

There are two subspaces to keep distinct. The trial subspace is what the algorithm gives us. The exact reducing subspace is the spectral target. Initially we can compute a residual using the trial subspace alone. A spectral gap will later let us convert that defect into a comparison with the target. First we need the exact identity satisfied by the residual.

### Choose orthonormal coordinates for the trial space

Let A be a self-adjoint operator on an ambient finite-dimensional Hilbert space H. Let F be a lower-dimensional coordinate space. Choose an isometric linear map E from F into H. Its columns are orthonormal trial vectors, and the range of E is the trial subspace V.

The equation E adjoint E equals the identity says that E preserves the lengths and inner products of trial-coordinate vectors. The ambient projection onto V is P equals E E adjoint.

For any ambient vector z, E adjoint z contains the trial coordinates of its projection. Applying E again returns the component of z inside V. Thus P z equals E E adjoint z. The complementary projection is the identity minus P.

The trial basis can change without changing V. If W is unitary on F, the map E W is another orthonormal frame for exactly the same subspace. A valid subspace-angle theorem should be insensitive to that replacement.

### Compress A to obtain the Ritz operator

Define the compressed or Ritz operator M as E adjoint A E. This is an operator on F. Because A is self-adjoint, M is self-adjoint too.

The compression answers a limited question: if we start with a trial vector E x, apply A, then retain only the component in V, which trial coordinates do we obtain? The answer is M x.

We should not confuse this compression with the whole action of A. The vector A E x can have a component outside V. Exactly that missing component is the residual.

Define R to be A E minus E M. Its input is a trial-coordinate vector x and its output is an ambient vector. In a matrix representation, its columns are the eigen-equation defects of the chosen trial basis.

Take E adjoint of the residual. We find E adjoint R equals E adjoint A E minus E adjoint E M. By the definitions of M and isometry, these terms are equal. Therefore E adjoint R is zero.

Every residual vector is orthogonal to the trial subspace. This is the Galerkin orthogonality principle. It is not an assumption in this construction; it follows from choosing the Ritz compression.

### Derive the residual's projection formula

Since M equals E adjoint A E, substitute it into the definition of R. The result is A E minus E E adjoint A E. Factor out A E on the right. We get R equals the identity minus P, composed with A E.

Thus the residual is simply the part of A E that escapes V. In particular, R vanishes exactly when A maps every vector in V back into V. For a self-adjoint operator, that means V is reducing: its orthogonal complement is invariant as well.

This gives a concrete diagnostic for approximate invariant subspaces. Instead of inspecting every vector in V, compute the norm of the residual map. The operator norm of R is the largest escape length among unit trial-coordinate inputs.

The Frobenius or Hilbert–Schmidt norm measures the total squared escape over an orthonormal trial basis. Those two norms quantify different aspects of the same map.

### A worked two-dimensional example

Consider the real symmetric matrix with first row zero, one, and second row one, three. Choose the horizontal axis as our one-dimensional trial space. E sends a scalar t to t times the first basis vector.

The Ritz operator is multiplication by the upper-left matrix entry, which is zero. But A applied to the horizontal unit vector is the vertical unit vector. Therefore R sends one to the vertical unit vector. Its norm is one.

The trial space is not invariant. Importantly, the residual is orthogonal to the trial line as Galerkin orthogonality predicts.

If we instead choose a normalized eigenvector of A as our trial vector, the compressed scalar equals its exact eigenvalue and R becomes zero. The residual detects exact invariance regardless of which orthonormal coordinates we use for the resulting one-dimensional space.

### A residual depends on the chosen trial operator

The Ritz operator is natural, but sometimes the numerical method supplies a separate self-adjoint trial operator A zero. Then we may define a more general residual R zero equals A E minus E A zero.

Insert and subtract E M. We obtain a decomposition into two terms: the perpendicular escape R, and the trial-space discrepancy E times M minus A zero.

The two terms are orthogonal on every trial vector. The first lies in V perpendicular, while the second lies in V. Pythagoras therefore gives a sum-of-squares formula for the residual's output length.

If A zero equals M, the internal discrepancy disappears. But in perturbation arguments we sometimes choose A zero from an unperturbed operator or a simpler model, and retaining the general residual is advantageous.

Take the example where A is diagonal with entries zero and five. Let the trial unit vector make an angle theta with the horizontal axis. If A zero is multiplication by zero, the general residual has length five times the sine of theta. If instead A zero is the Ritz value five sine squared theta, the residual length is five times the absolute value of sine theta times cosine theta.

These are two different residuals for the same trial line. Both are mathematically valid. Their associated spectral gaps to the exact complement differ, so a theorem must pair each residual with its own specified trial operator.

### Make the exact subspace explicit

Now let U be the exact target subspace. Its orthogonal projection is Q. Because A is self-adjoint and U is reducing, we may choose orthonormal coordinate maps F zero for U and F one for its orthogonal complement.

These satisfy F zero F zero adjoint plus F one F one adjoint equals the identity. They give the two exact blocks of A.

The residual R, by contrast, is computed from E and A zero. It does not need to lie in the exact complement U perpendicular. Galerkin orthogonality places the Ritz residual in the complement of V, which is usually a different subspace.

This distinction is essential. That component is the right-hand side of a Sylvester equation.

### What remains true in infinite dimensions

The formulas for projections and compressions remain valid for bounded self-adjoint operators on Hilbert spaces. If A is unbounded, writing A E requires that E send the trial operator's domain into the domain of A. We also need a bounded residual extending the algebraic difference on that common domain.

For the unbounded case, domain inclusion only makes the difference A E minus E A zero meaningful on the trial-operator domain. We must separately verify that the difference extends boundedly and, when applying a closed-operator Sylvester estimate, that the complementary overlap respects the domain of the unwanted exact block.

For now the finite-dimensional computation is enough to fix the geometry. Trial coordinates E, compressed operator M, residual R, exact coordinates F zero and F one. We have separated these roles, proved Galerkin orthogonality, and identified the residual as an escape from the trial space.

Projection of the residual onto the exact complementary subspace produces a Sylvester equation. Its solution measures the trial vectors that leak out of the selected spectral subspace, and the spectral gap controls their size.

## The complementary-block Sylvester equation

Consider a diagonal matrix with entries zero and five. Its horizontal axis is the exact zero-eigenspace, and the vertical axis is the unwanted eigenspace. Tilt a trial line away from horizontal by thirty degrees. Half of its unit vector now points vertically, because the sine of thirty degrees is one half.

If the matrix acts on that trial vector, its vertical component is multiplied by five. Suppose the intended trial eigenvalue is zero. The vertical component of the residual is therefore five times one half, or two and a half. The unwanted spectral value is five units away from the trial value. Dividing the residual by that distance recovers the vertical overlap, one half. In this simple problem the entire perturbation estimate is a scalar division.

For a larger problem, the vertical overlap becomes a map from trial coordinates into unwanted exact spectral coordinates. Multiplying by the unwanted block on its left and subtracting multiplication by the trial block on its right reproduces the projected residual. This is a Sylvester equation. We will derive it before taking any norm, so that every input space, output space and gap belongs to the right object.

In particular, the trial block need not equal the exact target block. A residual may use a Ritz compression or another specified self-adjoint trial operator. That choice determines the spectral separation we must check.

### Start with an exact reducing decomposition

Let A be a self-adjoint operator on an ambient Hilbert space H. Choose a reducing subspace U and its orthogonal complement. Represent U by an isometric coordinate map F zero, and its complement by an isometric coordinate map F one.

Because these two coordinate ranges form an orthogonal decomposition of H, the sum of their range projections equals the identity. In symbols spoken aloud, F zero F zero adjoint plus F one F one adjoint is the identity.

On the exact target subspace, the operator A is represented by a self-adjoint block Lambda zero. On the complement it is represented by a self-adjoint block Lambda one. In the corresponding exact coordinates, A is block diagonal. The crossed blocks vanish because U is reducing.

We are about to compare a trial space against U. Therefore Lambda one, the block on the unwanted exact complement, will be the decisive operator. The spectrum of Lambda zero is important for identifying the target cluster, but it is Lambda one that enters the Sylvester equation for the error.

### Introduce the trial map and residual

Let E be an isometric trial map from coordinate space F into H. Let A zero be a self-adjoint operator on F. It might be the Ritz compression E adjoint A E, but the algebra does not require that choice.

Define the residual R as A E minus E A zero. This is a map from F into H. If the trial vectors were exact eigenvectors, with A zero giving their eigenvalues, R would vanish.

We want to measure how much the trial space lies in the exact complement U perpendicular. Define X to be F one adjoint E. For a trial-coordinate vector x, X x tells us its coordinates in that exact complement.

Notice that X is bounded and has norm at most one. It is the product of an adjoint isometry and an isometry. Its norm is the largest directed sine of the principal angles from the trial subspace to U, since it measures the complementary component of each unit trial vector.

### Derive the equation, one factor at a time

Start with R equals A E minus E A zero. Apply F one adjoint on the left. Then F one adjoint R equals F one adjoint A E minus F one adjoint E A zero.

The second term is simply X A zero, by the definition of X.

For the first term, use the exact reducing decomposition. Applying A and then taking complementary coordinates is equivalent to taking complementary coordinates first and then applying Lambda one. Thus F one adjoint A E equals Lambda one F one adjoint E, which equals Lambda one X.

Combining the terms gives F one adjoint R equals Lambda one X minus X A zero.

This is a Sylvester equation. The unknown is X, the complementary overlap of the trial frame. The right-hand side is the compressed residual F one adjoint R. Its two coefficient operators are Lambda one and A zero, acting on different coordinate Hilbert spaces.

No approximation was made in deriving the equation. It is an exact identity.

### Why the compression is part of the proof

The residual R is ambient-valued. The Sylvester unknown X is complementary-coordinate-valued. These maps do not even have the same target space, so they cannot be substituted for one another.

The factor F one adjoint sends the ambient residual into the correct target coordinates. Since F one is an isometry, its adjoint is a contraction. Consequently, the norm of F one adjoint R is at most the norm of R. The same contraction statement holds for compatible symmetric operator ideals, provided their membership and composition hypotheses are in force.

This is the first of two inequalities in the sine theorem. The exact equation gives the stronger right-hand side F one adjoint R; replacing it with R is a convenient bound.

There is a similar but not identical equation obtained by taking adjoints. Its unknown becomes E adjoint F one, and its right-hand side involves the adjoint residual. We may use either orientation, but we must change the coefficient order and sign consistently.

### A worked diagonal model

Let A be diagonal on the plane, with entries zero and five. Take the exact target U to be the horizontal axis and the exact complement to be the vertical axis. Therefore Lambda one is the scalar five.

Choose the trial unit vector u with coordinates cosine theta and sine theta. E sends one to u. The complementary overlap X sends one to sine theta.

First choose A zero to be the scalar zero. Then the residual A u minus zero times u is five sine theta times the vertical basis vector. Its complementary coordinate is five sine theta.

The Sylvester equation becomes five times sine theta minus sine theta times zero equals five sine theta. Both sides agree. If theta is thirty degrees, X is one half and the right-hand side is two point five.

Now choose the Ritz operator instead. The Ritz scalar is five sine squared theta. The residual becomes A u minus five sine squared theta times u. Its vertical coordinate is five sine theta minus five sine cubed theta, which simplifies to five sine theta times cosine squared theta.

The Sylvester left-hand side is now five times sine theta minus five sine squared theta times sine theta, exactly the same expression.

Both equations are valid. But their spectral gaps are different. In the first, the distance between A zero and Lambda one is five. In the second, it is five cosine squared theta. The residual shrinks under Ritz compression, but the gap may shrink too.

This example is why the spectral-gap theorem must use the coefficient A zero actually present in the residual identity. Substituting a different reference eigenvalue changes both sides of the relevant estimate.

### Apply a genuine Sylvester bound

Suppose the spectra of Lambda one and A zero satisfy an ordered gap of size delta, or another separation condition covered by the appropriate Sylvester theorem. Then the Sylvester inverse controls X by F one adjoint R.

In the simplest operator-norm case with an ordered self-adjoint gap, delta times the norm of X is at most the norm of F one adjoint R, hence at most the norm of R.

The result is already a bound on the amount of trial space outside the exact target.

Do not replace the gap hypothesis by the statement that Lambda one and A zero have different eigenvalues. In dimensions greater than one, interlaced spectral sets can have positive pairwise distance and still require a weaker norm constant. The distinction follows from the Sylvester inverse itself: ordered self-adjoint spectra admit a sharp constant-one operator-norm estimate, while an arbitrary pairwise gap need not.

### Restore the domain conditions for unbounded A

For unbounded self-adjoint A, the line A E minus E A zero is not automatically a globally defined bounded map. We require E to carry the domain of A zero into the domain of A, and R to be the bounded extension of the corresponding difference.

Likewise F one must take vectors in the domain of Lambda one to legal vectors in the domain of A. To justify applying the complementary block, one uses the reducing property together with the corresponding adjoint intertwining identity on the relevant domains.

Then X maps the domain of A zero into the domain of Lambda one, and the Sylvester equation holds there. This is the closed-operator equation to which our unbounded Sylvester estimates apply.

We have completed the algebraic bridge: exact reducing coordinates, trial residual, complementary overlap, and a domain-aware Sylvester equation.

## Directed sine as a rectangular modulus

A line tilted by thirty degrees from the horizontal has an escape length of one half: project its unit direction onto the vertical axis, and the vertical component has length one half. That simple measurement is the sine of the angle.

Now replace the line with a plane. Different unit directions in the trial plane may escape the desired exact plane by different amounts. We need one object that records all those escape lengths and behaves correctly when we change the orthonormal coordinates used to describe the trial plane.

Let the exact target subspace be U, and let E carry trial-coordinate vectors isometrically into the ambient Hilbert space. Project E's outputs onto the orthogonal complement of U. Call the resulting map S. It sends each trial input to the part of its ambient vector lying outside the target. The positive square root of S adjoint S measures the length of that escape for every direction, and its singular values give the directed principal sines.

There is another way to record exactly the same data. Choose orthonormal coordinates in the exact complement and take the overlap between those coordinates and E. That rectangular overlap is the variable solved for by the complementary Sylvester equation. We will show that its modulus is the same as the modulus of S. Once established, an estimate for the overlap becomes an estimate for subspace angles, with no need to match individual eigenvectors.

### Define the two projections

Let U be the exact target subspace of a Hilbert space H. Write P for the orthogonal projection onto U. Let E be an isometry from a trial-coordinate Hilbert space F into H. Its range is the trial subspace V.

Split E into two parts. The component inside the target space is C equals P E. The component outside is S equals the identity minus P, composed with E.

The maps C and S both start in F and end in H. Their ranges are orthogonal, because one lands in U and the other in U perpendicular. Their sum is E.

Because E preserves lengths, the sum of the squares of the output lengths of C and S equals the input length squared. In operator language, C adjoint C plus S adjoint S equals the identity on F.

The positive square roots of these two Gram operators are the cosine and sine magnitudes associated with the trial space relative to the exact target. Their eigenvalues are the squared cosines and squared sines of the directed principal angles, because the two orthogonal components of each unit trial vector have squared lengths summing to one.

### Construct the sine modulus

Consider S adjoint S. Since S equals the identity minus P times E, and the complementary projection is self-adjoint and idempotent, S adjoint S equals E adjoint times the identity minus P times E.

This is a positive operator on the trial-coordinate space F. Its unique positive square root is the modulus of S, written absolute value of S.

For a unit coordinate vector x, the squared norm of S x is the amount of the trial vector E x that lies outside U. The largest such amount is the square of the operator norm of S.

In finite dimensions, diagonalize S adjoint S. Its eigenvalues lie between zero and one. If they are the squares of numbers s one, s two, and so on, those s values are the singular values of S. Define each directed angle theta by sine theta equals the corresponding s, with theta between zero and ninety degrees.

This definition is geometrically natural. A trial vector already lying in U produces sine zero. A trial vector perpendicular to U produces sine one, corresponding to a right angle. Intermediate values measure how much of the vector escapes the exact target.

### Replace ambient escape with exact complementary coordinates

Now choose an isometric coordinate map F one whose range is U perpendicular. The projection onto U perpendicular is F one F one adjoint.

Define X equal to F one adjoint E, the same map as in the complementary Sylvester equation. It sends trial coordinates to coordinates in U perpendicular.

Compute X adjoint X. It equals E adjoint F one F one adjoint E. Replace F one F one adjoint by the identity minus P. We get E adjoint times the identity minus P times E.

That is exactly S adjoint S.

Therefore X and S have the same Gram operator, the same positive modulus, and the same singular values where those are defined. The directed sine operator on F is their common modulus.

There is a subtle point here. S and X have different codomains. They do not have to be equal maps. Their identical Gram operators mean that they encode the same lengths and principal-angle data. For symmetric ideals that are invariant under rectangular isometries and polar factors, that is exactly enough to transfer both membership and gauge bounds.

### Work out the plane

Let U be the horizontal axis in the real plane. Choose a unit trial vector u with coordinates cosine theta and sine theta. The trial-coordinate space is one-dimensional, so E sends a scalar t to t times u.

The complementary projection removes the horizontal coordinate. Therefore S applied to one is sine theta times the vertical basis vector.

If F one identifies the complement with the real line, X applied to one is the scalar sine theta. The maps have different outputs, a plane vector versus a scalar, but they have the same modulus: multiplication by the absolute value of sine theta.

At thirty degrees, that modulus is one half. At ninety degrees, it is one. At zero degrees, it is zero.

This verifies the geometric and algebraic definitions in the simplest setting.

### A two-dimensional trial space can have two different directed angles

Now work in three-dimensional space. Let the exact target U be the plane spanned by the first two coordinate axes. Let the trial space V be the plane spanned by the first and third axes.

Choose E whose columns are the first and third basis vectors. The first trial vector lies entirely in U, so its escape under the complementary projection is zero. The second trial vector lies perpendicular to U, so its escape has length one.

The singular values of S are therefore one and zero, or equivalently the directed principal angles are ninety and zero degrees, in descending sine order.

This example illustrates why an operator or an entire list of sines is often more informative than a single angle. A largest-angle bound controls the worst direction. A Frobenius bound controls the combined squared escapes, and Ky Fan or symmetric-ideal bounds control cumulative singular-value information.

If the trial dimension exceeds the target dimension, there must be a trial direction perpendicular to the target, by a dimension argument. Its directed sine is one. For infinite dimensions, dimensional statements require more care, but the rectangular modulus continues to make sense without enumerating eigenvectors.

### Prove trial-basis independence

Suppose we change the orthonormal trial coordinates by a unitary map W. The new trial map is E W. Its escape map becomes S W. Its complementary-coordinate map becomes X W.

The new Gram operator is W adjoint S adjoint S W. The positive square root transforms in the same way, by the uniqueness of the positive square root or functional calculus. Thus the new sine modulus is W adjoint absolute value of S times W.

Unitary conjugation changes the matrix representation on the trial-coordinate space, but not its spectrum, singular values, or unitarily invariant norm.

Likewise changing the exact complementary frame F one by a unitary coordinate transformation only multiplies X by a unitary on the left. It leaves X adjoint X unchanged.

Our directed sine geometry depends on the two subspaces, not on the particular coordinates used to describe them.

### Distinguish directed from symmetric angles

The construction starts from V and measures its escape from U. Reversing the direction means starting with an isometric frame for U and measuring escape from V. These directional maps can have different numbers of singular values and different zero or right-angle multiplicities when dimensions differ.

For equal finite dimensions the nonzero principal-angle information agrees in the usual paired convention. But the source-indexed rectangular operator retains the correct multiplicities for the direction actually used by a residual theorem.

The ambient projection difference P minus the trial projection is yet another angle representative. Its modulus describes a symmetric subspace gap. It agrees with the largest directed sine in common equal-dimensional acute situations, but we should not identify every list or ideal norm without checking the dimensional and multiplicity conventions.

### The resulting geometric estimate

We now have both ingredients. The complementary Sylvester equation controls X in terms of the compressed residual. The Gram identity identifies the modulus of X with the directed sine operator. Consequently a suitable Sylvester estimate becomes a principal-angle estimate with no further approximation.

## The single-angle sine theorem

Suppose a self-adjoint operator has an invariant subspace that we want to identify. We have calculated another subspace that appears to approximate it. How can we estimate the angle between the two without knowing the exact subspace's basis vectors in advance?

A natural test is to apply the operator to our trial vectors and measure how badly they fail to satisfy the operator equation we expect. That failure is a residual.

The Davis–Kahan sine theorem says that a residual can control the angle to a chosen exact subspace, provided the trial operator is spectrally separated from the action of the original operator on the exact subspace's unwanted complement.

The separation is indispensable. An exactly invariant trial space can be the wrong invariant space, so a zero residual alone is not enough to identify the target.

Let's discover the inequality in the plane. Then we'll state its precise hypotheses and explain why an operator equation called the Sylvester equation gives the general result.

### The whole calculation in two dimensions

Take the real plane. Let A be diagonal, with eigenvalue zero along the horizontal axis and eigenvalue five along the vertical axis.

Suppose the exact subspace we want is the horizontal axis. Call it U. Its orthogonal complement is the vertical axis, where A acts by multiplication by five.

Now choose a trial line V making an angle theta with the horizontal, where theta lies between zero and ninety degrees. A unit vector along the trial line has horizontal coordinate cosine theta and vertical coordinate sine theta.

We also need a trial operator, which prescribes how we think A acts on our trial coefficients. For this first example, choose the trial operator to be multiplication by zero. We're trying to model the horizontal eigenvalue.

Apply A to our trial vector. The horizontal coordinate becomes zero and the vertical coordinate becomes five times sine theta. The trial operator predicts zero, so that entire output is the residual. Its length is five times sine theta.

What is the geometric error? The component of our trial vector outside U is its vertical coordinate, sine theta. Its length is exactly the sine of the angle from V to U.

And what spectral separation do we have? The trial operator is zero, while A acts by five on U's complement. Those two actions differ by five.

So the residual length equals the spectral separation, five, multiplied by the sine of the angle.

In symbols spoken aloud: five times sine theta equals the residual length.

This is the basic form of the sine theorem. In the general setting the equality becomes a bound. But this example shows that the coefficient one in front of residual divided by gap can be attained exactly.

### Why the residual needs a gap

Change the example. Keep A and the exact horizontal target, but choose the trial line to be the vertical axis. This line is itself invariant under A.

If we choose the trial operator to be multiplication by five, the residual is zero. The equation is satisfied perfectly.

Yet the trial line is perpendicular to the target line. Its sine of angle is one, as large as possible.

The missing assumption is visible immediately. On the unwanted vertical complement, A also acts by five. The trial operator and the unwanted complementary operator have no spectral gap at all.

This example establishes the role of the gap before we introduce any abstraction. The residual says how accurately a trial space satisfies its own operator equation. The gap tells us whether that equation distinguishes the intended subspace from competing invariant subspaces.

### State the isometric theorem

Now work in a real or complex Hilbert space H. Let A be self-adjoint, the Hilbert-space analogue of a symmetric real matrix, with the operator agreeing with its adjoint. For the initial argument, assume A is bounded, so there are no domain complications.

Choose an exact closed subspace U that is reducing for A. Reducing means both U and its orthogonal complement are invariant under A. Let P be the orthogonal projection onto U.

Choose a trial coordinate Hilbert space F and an isometric map E from F into H. Isometric means E preserves lengths. The range of E is the trial subspace V.

Choose a self-adjoint trial operator A zero on F. It is the operator whose action E A zero predicts in ambient space. Define the residual R as A E minus E A zero. Thus R takes trial coefficients and returns ambient vectors.

On the unwanted orthogonal complement of U, let Lambda one denote A's self-adjoint action, expressed in coordinates of that complement.

Assume a positive number delta supplies an admissible spectral separation between A zero and Lambda one, strong enough to give a Sylvester estimate with constant one. A concrete sufficient configuration is an ordered gap: every spectral value of A zero is at most some real threshold a, and every spectral value of Lambda one is at least a plus delta. The reverse ordering also works. A specified interval-and-exterior separation is another admissible configuration.

Under such a gap hypothesis, the operator-norm conclusion is this: delta multiplied by the norm of the component of E outside U is no greater than the norm of R.

Since E is isometric, the norm of that escaping component is the sine of the largest directed angle from the trial subspace toward U, or the supremum of those sines in infinite dimensions.

So the largest directed sine is at most residual norm divided by delta.

The word directed is deliberate. We measure how much trial vectors fall outside U. If the dimensions differ, reversing the roles of U and V need not produce the same angle information.

There is also an operator-ideal version. An operator ideal is a family of operators equipped with norms that can distinguish, for example, a largest singular value from the sum of many singular values. The trace norm and Hilbert–Schmidt norm are familiar examples in finite dimensions. For a suitable symmetric ideal satisfying the required Ky Fan dominance property, and with R belonging to that ideal, the directed sine representative belongs to the ideal too and obeys the same gap-times-sine bound. Ky Fan dominance is the condition that lets inequalities about accumulated singular values control the chosen ideal norm.

That's the target. Now let's explain where it comes from.

### First bridge: isolate the unwanted component

Choose isometric coordinate maps for the exact subspace U and for its orthogonal complement. Call them F zero and F one.

Think of F one as taking coordinates of an unwanted direction and placing that vector in H. Its adjoint, F one star, extracts the unwanted coordinates from an ambient vector.

Apply F one star to the trial embedding E. The result is an operator X from trial coefficients into complementary coordinates. X tells us exactly how much each trial vector points outside the desired subspace.

Our two-dimensional example had just one trial coordinate and one complementary coordinate. There, X was the number sine theta.

Now apply F one star to the residual equation. The residual was A E minus E A zero.

Because U reduces A, the action of A on complementary coordinates is Lambda one. Therefore the complementary part of the residual is Lambda one X minus X A zero.

This is a Sylvester equation. Its unknown is X. The two coefficient operators are Lambda one and A zero. Its right-hand side is the complementary part of the residual.

In the plane, the equation reduces to five times sine theta minus zero times sine theta equals five times sine theta. Nothing has changed except notation.

In a larger Hilbert space, the same equation encodes all the complementary directions simultaneously.

### Second bridge: use spectral separation

A Sylvester equation has the form: one operator applied to X, minus X followed by another operator, equals a known right-hand side.

If the two coefficient operators have an admissible spectral gap, the Sylvester estimate bounds X in terms of that right-hand side. For the constant-one gap conditions stated here, delta times the operator norm of X is at most the norm of the complementary residual.

Why does the gap appear in the denominator? In the scalar case, an equation such as five times x equals r is solved by dividing r by five. If the two spectral actions get closer, the corresponding difference becomes harder to invert. The Sylvester theorem is the operator-level version of that calculation.

Extracting complementary coordinates cannot increase a vector's length. F one star is a contraction. Therefore the norm of the complementary residual is no greater than the norm of the full residual R.

Combining the two estimates gives delta times the norm of X no greater than the norm of R.

For a suitable symmetric operator ideal, the same reasoning uses the ideal's singular-value dominance and composition properties. Membership of R in that ideal must be included: boundedness alone does not imply that R is trace class or belongs to another specified ideal.

A positive distance between arbitrary interlaced spectral sets is not, by itself, a guarantee of the same sharp operator-norm Sylvester estimate. The constant-one conclusion uses the stated stronger gap configuration.

### Third bridge: turn X into an angle

We have estimated X, but the geometric theorem is about the trial subspace's angle to U. We need to identify those quantities.

Let S take a trial coefficient, embed it with E, and remove its orthogonal projection onto U. Thus S is the composition of identity minus P with E.

The output of S is an ambient vector perpendicular to U. The output of X gives the coordinates of that same vector in the complementary subspace.

Since F one is an isometry and its range is the entire complement, S equals F one applied to X. For every trial coefficient, S and X have outputs of the same length.

Equivalently, their Gram operators are equal: S star S equals X star X.

So S and X have the same positive modulus, the same relevant singular values, and the same operator norm. The positive modulus of S is the directed sine operator. In one dimension it is simply the scalar sine theta.

We can now replace X in the Sylvester bound with S. We obtain the desired inequality: delta times the directed sine norm is at most the residual norm.

The proof consists of three exact connections: extract the complementary residual to get a Sylvester equation, use the admissible gap to bound its solution, and identify that solution's size with the directed sine.

### Why the coefficient one is sharp

Return to the diagonal plane operator with eigenvalues zero and five. Use the horizontal target, an arbitrary trial line at angle theta, and the trial operator equal to zero.

The complementary spectrum is five. The gap is five. The complementary coordinate X is sine theta. The residual length is five sine theta.

Every inequality in the proof is an equality in this example. So a universal estimate with any smaller coefficient multiplying the residual on the right would fail for this family.

There is one detail worth preserving. The trial operator zero is not the Rayleigh–Ritz compression of A onto the tilted trial line, except when theta is zero.

The Ritz compression would instead be multiplication by five times sine theta squared. Its residual would have length five times sine theta times cosine theta, and its gap from the unwanted eigenvalue five would be five times cosine theta squared.

Both the residual and the gap change. We cannot use the smaller Ritz residual together with the old gap of five. The theorem compares a residual and a gap built from the same chosen trial operator.

### What changes with a nonisometric trial frame?

So far E preserves lengths. A general trial map may stretch or shrink its coefficient vectors. Suppose E is bounded below: every output has length at least epsilon times the input length, for some positive epsilon.

This lower frame bound guarantees that E has a closed range and a stable normalization to an isometric embedding. Normalization changes the coordinates used to measure the angle, but not the trial subspace itself.

The inverse normalization can amplify a coefficient vector by at most one divided by epsilon. Consequently the general inequality gains an epsilon factor on the left: delta times epsilon times the directed sine gauge is no greater than the residual gauge, under the corresponding general-frame hypotheses.

The scaling is necessary. If we multiply E by a positive constant, its residual scales by that constant while the angle of its range stays fixed. The frame lower bound scales by the same constant and restores the correct balance.

### What changes for unbounded operators?

For an unbounded self-adjoint A, the formula A E requires a domain condition. An arbitrary vector in the range of E need not lie in the domain of A.

We require the trial map to send the domain of A zero into the domain of A. On that legal domain, A E minus E A zero must agree with a residual that extends to a bounded operator. The complementary coordinate maps and Lambda one must also respect the relevant domains and intertwining identities.

With those assumptions and an admissible unbounded Sylvester gap, the same three bridges work. The complementary equation is first interpreted on its allowed domain; the Sylvester theorem supplies the bounded estimate; and the isometric geometry identifies the directed sine. The real case can be treated directly or through the appropriate complexification and descent arguments.

### What the theorem actually says

The residual alone measures how well a trial space satisfies its proposed equation. A gap between the trial operator and the unwanted complementary action identifies which exact subspace that equation can approximate.

With the correct gap, the escape of trial vectors from the target is bounded by residual divided by gap. The diagonal plane example gives equality, while the wrong-invariant-line example shows why the separation condition cannot be omitted.

A useful final check is to compare those two examples. In the first, the residual and gap are both tied to the trial operator zero, and the sine bound is sharp. In the second, the trial operator is five, the residual is zero, the angle is ninety degrees, and the complementary gap has vanished. Being able to explain that contrast is the core intuition behind the single-angle sine theorem.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Trial spaces, exact subspaces and residuals

**Draft status:** audio-first mathematical lecture. **Prerequisites:** `021000` Rayleigh–Ritz compressions; `028000` min–max; `071000` complementary blocks; `106000` perturbation question. **Next:** `108000` the complementary-block Sylvester equation.

---

#### Companion: mathematics and Lean correspondence (display only)

##### Exact residual in the opening numerical model

With
\[
A=\begin{pmatrix}0&1\\1&3\end{pmatrix},\qquad
E:\mathbb R\to\mathbb R^2,\quad Et=(t,0),
\]
we have \(M=E^*AE=0\) and
\(R=AE-EM=(0,1)^T\). Thus \(E^*R=0\), and
\(R=(I-EE^*)AE\) explicitly. The eigenvalues of \(A\) are
\((3\pm\sqrt{13})/2\), showing that zero Ritz value is only an
approximation even though the trial vector is normalized.

For a finite-dimensional isometry `E : F → H`, define `P=EE*`, `M=E*AE`, and `R=AE−EM`. Then `E*R=0` and `R=(I−P)AE`. For an arbitrary trial operator `A₀`, `R₀=AE−EA₀=R+E(M−A₀)`; the two summands have orthogonal ranges. With unbounded `A`, use common-domain hypotheses before asserting a bounded extension.

##### Source declaration excerpts

`DavisKahan/BoundedOperator/TrialResidual.lean` — `trialResidualCore` (exact declaration header; body omitted):

```lean
@[expose] noncomputable def trialResidualCore
    (T : H →L[ℂ] H) (Z : Submodule ℂ H)
    [Z.HasOrthogonalProjection] : Z →L[ℂ] H :=
```

`DavisKahan/BoundedOperator/TrialResidual.lean` — `trialResidualCore_eq_ritzDifference` (exact declaration header; body omitted):

```lean
theorem trialResidualCore_eq_ritzDifference
    (T : H →L[ℂ] H) (Z : Submodule ℂ H)
    [Z.HasOrthogonalProjection] [CompleteSpace Z] :
    trialResidualCore T Z =
      T ∘L Z.subtypeL - Z.subtypeL ∘L compressOperator Z T := by
```

`DavisKahan/BoundedOperator/TrialResidual.lean` — `trialResidualCore_apply_mem_orthogonal` (exact declaration header; body omitted):

```lean
theorem trialResidualCore_apply_mem_orthogonal
    (T : H →L[ℂ] H) (Z : Submodule ℂ H)
    [Z.HasOrthogonalProjection] (z : Z) :
    trialResidualCore T Z z ∈ Zᗮ := by
```

**Mapping.** In `TrialResidual.lean`, `Z.subtypeL` is the isometric inclusion of the trial subspace; `compressOperator Z T` is its Ritz compression; `trialResidualCore` takes values in `Zᗮ`. In the source's general `residual A X M`, `X` corresponds to the trial map `E`, and `M` to the chosen trial operator. The source code explicitly distinguishes projected Ritz residuals from arbitrary trial residuals.

### The complementary-block Sylvester equation

**Draft status:** audio-first mathematical lecture. **Prerequisites:** `017000` orthogonal coordinates; `063000–071000` Sylvester equations; `093000` common domains; `107000` trial residuals. **Next:** `109000` directed sine geometry.

---

#### Companion: mathematics and Lean correspondence (display only)

##### The rotated-line residual and complementary quotient

Let \(A=\operatorname{diag}(0,5)\),
\(e=(\sqrt3/2,1/2)^T\), and \(M=e^*Ae=5/4\). Then
\[
R=Ae-eM=\begin{pmatrix}-5\sqrt3/8\\15/8\end{pmatrix},\qquad
\|R\|=5\sqrt3/4.
\]
For \(Q=\operatorname{span}\{(1,0)\}\), the complementary
projection of \(R\) has length \(15/8\), while the gap between
\(M=5/4\) and the unwanted eigenvalue \(5\) is \(15/4\).
Their quotient is \(1/2\), the directed sine of the thirty-degree
angle. The projected residual, not the full residual, yields equality
in this complementary-block equation.

With reducing coordinates `F₀,F₁`, `F₁* A=Λ₁ F₁*` on the legal domain. For `R=AE−EA₀` and `X=F₁*E`, derive `F₁*R=Λ₁X−XA₀`. A valid `FormBoundedSylvesterGap` plus the domain-aware `SylvesterEquation` gives `δ gauge(X)≤gauge(F₁*R)` in the supported symmetric ideal family, including the membership conclusion. The orientation in some Lean statements is adjointed: the unknown is `E*F₁` and the equation changes sign accordingly.

##### Source declaration excerpts

`DavisKahan/Sources/DavisKahan1970/SineTheta/CommonDomain.lean` — `HasCommonDomain` (exact declaration header; body omitted):

```lean
def HasCommonDomain
    (A : E →ₗ.[𝕜] E)
    (A₀ : F →ₗ.[𝕜] F)
    (X : F →L[𝕜] E) : Prop :=
```

`DavisKahan/Sources/DavisKahan1970/SineTheta/ScalarGeneric.lean` — `sinTheta_unbounded_formGap_idealFamily_block_rclike` (exact declaration header; body omitted):

```lean
theorem sinTheta_unbounded_formGap_idealFamily_block_rclike
    (N : TauCeti.SymmetricOperatorIdealFamily 𝕜)
    [N.toOperatorIdealFamily.IsKyFanDominant]
    (D : UnboundedSinThetaData (𝕜 := 𝕜) (E := E) (F := F) (G := G))
```

**Mapping.** The Lean `UnboundedSinThetaData` packages trial and complementary maps, their self-adjoint coefficient operators, and a bounded residual extending the common-domain identity. The `unbounded_adjoint_residual_block_identity` theorem supplies the legal complementary equation in the adjointed orientation. `ScalarGeneric.sinTheta_unbounded_formGap_idealFamily_block_rclike` then applies the domain-aware Sylvester estimate and ideal contraction.

### Directed sine as a rectangular modulus

**Draft status:** audio-first mathematical lecture. **Prerequisites:** `035000` operator modulus; `042000` principal angles; `043000` cross projections; `108000` complementary Sylvester equation. **Next:** `110000` the single-angle sine theorem.

---

#### Companion: mathematics and Lean correspondence (display only)

##### Rectangular sine for a line

For \(u=(\cos\theta,\sin\theta)^T\) and the horizontal reference
line \(Q=\operatorname{span}\{e_1\}\), the escape map
\((I-P_Q)u=(0,\sin\theta)^T\) has the sole singular value
\(|\sin\theta|\). At thirty degrees that singular value is
\(1/2\). In unequal dimensions the escape map remains rectangular;
its nonzero singular values encode the directed principal sines.

Let `P=F₀F₀*`, `S=(I−P)E`, and `X=F₁*E` with `F₁F₁*=I−P`. Then `S*S=E*(I−P)E=X*X`, hence `|S|=|X|`. Under trial frame change `E↦EW`, the modulus conjugates by `W`. The resulting source-indexed sine operator is rectangular; ideal membership and gauge transport use invariance of complete singular-value/approximation-number data.

##### Source declaration excerpts

`DavisKahan/Geometry/Angle/SinAngle.lean` — `spectraSinAngleOperator` (exact declaration header; body omitted):

```lean
noncomputable def spectraSinAngleOperator
    (U V : Submodule ℂ H)
    [U.HasOrthogonalProjection] [V.HasOrthogonalProjection] : H →L[ℂ] H :=
```

`DavisKahan/Sources/DavisKahan1970/SineTheta/AngleIdentity.lean` — `sourceDirectedAngleC_eq_arcsin_sineModulus` (exact declaration header; body omitted):

```lean
theorem sourceDirectedAngleC_eq_arcsin_sineModulus
    (U V : Submodule ℂ E)
    [U.HasOrthogonalProjection] [V.HasOrthogonalProjection] :
    directedAngleBlockC U V =
      cfc Real.arcsin (sineBlockModulusC U V) :=
```

**Mapping.** `spectraSinAngleOperator` is an *ambient symmetric* modulus of a projection difference, which is distinct from the directed rectangular `sinThetaEmbedding`/`directedSinThetaOperator`. The `AngleIdentity` results connect a directed angle block to the `arcsin` of its sine modulus. The paired equality of `S*S` and `X*X` explains why the theorem may use the complementary-coordinate representative without asserting the maps themselves equal.

### The single-angle sine theorem

**Draft status:** audio-first mathematical lecture. **Prerequisites:** `071000` compressed Sylvester identity; `094000` unbounded Sylvester estimates; `098000–101000` ideal membership; `105000` proof assembly; `108000–109000` residual and directed sine. **Next:** `111000` graph subspaces and tangent geometry.

---

#### Companion: mathematics and Lean correspondence (display only)

Given a self-adjoint ambient `A`, a reducing exact decomposition `F₀,F₁`, an isometric trial `E`, self-adjoint `A₀,Λ₁`, a bounded residual `R` extending `AE−EA₀` on its common domain, an admissible `δ>0` `FormBoundedSylvesterGap A₀ Λ₁ δ`, and a Ky-Fan-dominant symmetric ideal `N` with `N.Mem R`, the isometric theorem gives `N.Mem((I−F₀F₀*)E)` and `δ N.gaugeReal((I−F₀F₀*)E) ≤ N.gaugeReal R`. Nonisometric trial maps with lower frame bound `ε>0` give `δε` on the left. For `A=diag(0,δ)`, `A₀=0`, `E=(cosθ,sinθ)`, equality holds. The gap must support the constant-one Sylvester estimate, such as an ordered form gap or a supported interval/exterior configuration; mere pairwise spectral distance need not do so in operator norm. In the plane example with \(A=\operatorname{diag}(0,5)\), the Ritz choice instead is \(A_0=5\sin^2\theta\), with \(\|R\|=5\sin\theta\cos\theta\) and complementary gap \(5\cos^2\theta\).

##### Source declaration excerpts

`DavisKahan/Sources/DavisKahan1970/SineTheta/ScalarGeneric.lean` — `sinTheta_unbounded_formGap_idealFamily_rclike` (exact declaration header; body omitted):

```lean
theorem sinTheta_unbounded_formGap_idealFamily_rclike
    (N : TauCeti.SymmetricOperatorIdealFamily 𝕜)
    [N.toOperatorIdealFamily.IsKyFanDominant]
    (D : UnboundedSinThetaData (𝕜 := 𝕜) (E := E) (F := F) (G := G))
```

`DavisKahan/Sources/DavisKahan1970/SineTheta/Theorem61.lean` — `result` (exact declaration header; body omitted):

```lean
theorem result
    (N : TauCeti.SymmetricOperatorIdealFamily ℂ)
    [N.toOperatorIdealFamily.IsKyFanDominant]
    (P : GeneralSinThetaRepresentativeProblem (E := E) (F := F)
```

`DavisKahan/Sources/DavisKahan1970/SineTheta/Theorem61.lean` — `result` (exact declaration header; body omitted):

```lean
theorem result
    (N : TauCeti.SymmetricOperatorIdealFamily ℂ)
    [N.toOperatorIdealFamily.IsKyFanDominant]
    (P : IsometricSinThetaRepresentativeProblem (E := E) (F := F)
```

**Mapping.** `ScalarGeneric.sinTheta_unbounded_formGap_idealFamily_rclike` states the canonical isometric result for `UnboundedSinThetaData` and a `SymmetricOperatorIdealFamily` with `IsKyFanDominant`. `Theorem61.GeneralSinThetaRepresentativeProblem.result` carries the nonisometric `frameLowerBound` and `gap` factors, and transfers to a paper-facing representative with matching singular-value data. The general paper-facing theorem's gap and domain hypotheses are contained in its `problem` data; one cannot infer them from the displayed result type alone.
