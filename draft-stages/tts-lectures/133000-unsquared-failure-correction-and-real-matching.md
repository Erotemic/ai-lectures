# Unsquared failure, correction, and real matching

<!-- BEGIN SPOKEN LECTURE -->

# Unsquared failure, correction, and real matching

## Unsquared ambient displacement is different

Suppose we must carry one line to another by an orthogonal motion. If the angle is forty-five degrees, rotating the whole plane by forty-five degrees seems economical: both directions move a little. A reflection also succeeds, but it reverses one direction completely. In the plane, the rotation wins for every unitarily invariant norm of displacement. In four dimensions, with two such line-pairs, a transporter can do better in trace norm by linking the planes.

The difference is freedom in the **whole-space transport constraint**. Understanding that freedom also explains why a bound for restricted movement cannot simply be promoted to a bound for the entire ambient space.

### What is allowed to move?

Let U and V be equally dimensional subspaces of a finite-dimensional real inner-product space. An admissible transporter W is an orthogonal map with W of U equal to V. Its full displacement is identity minus W. A unitarily invariant norm measures that displacement through its singular values, without choosing a favored coordinate basis.

To describe that freedom, first choose the direct rotation D as a reference motion. Think of a competitor as having two stages. Before the direct rotation acts, it may rearrange directions *inside* the source. It may independently rearrange directions inside the perpendicular complement. As long as it leaves those two spaces intact, the final direct rotation still sends the source onto V.

Call this preliminary rearrangement S. Algebraically, S is D inverse followed by W, because undoing D after W brings the target V back to U. Thus S maps U onto itself. Since S is orthogonal, it also maps U perpendicular onto itself. Conversely, every orthogonal S with these two properties produces an admissible W by composing D with S.

Relative to the split into U and its complement, S has two diagonal blocks. That sounds restrictive, but each block may mix the principal-vector directions inside its own space. When D acts afterward, the resulting W need not preserve the separate principal planes. The distinction is between preserving the **source subspace** and preserving **each canonical principal plane**. The transport constraint requires the first, not the second.

That is the extra variable missing from a plane-by-plane comparison. The principal angles are fixed by U and V, but the displacement singular values of W are not.

### Why the planar sixty-degree rule is correct

Take one real source line and one target line making angle theta, between zero and ninety degrees, inside a two-dimensional ambient plane. Up to signs, the best orientation-preserving transporter is the rotation through theta. Its two displacement singular values are equal to a, where a is twice the sine of half theta.

The orientation-reversing option is a reflection that maps the source line onto the target line. Its displacement singular values are two and zero. We can compare these lists without choosing a particular unitarily invariant norm. For two nonnegative entries, weak majorization has just two tests. Compare the largest entry, and compare the sum of both entries.

For the rotation, the list is a and a. For the reflection, it is two and zero. The largest-entry test always succeeds: a is at most two. The total-sum test asks whether twice a is at most two, or simply whether a is at most one. Since a is twice the sine of half theta, this holds exactly when theta is at most sixty degrees.

So the sixty-degree threshold is a theorem about the **two-dimensional choice** between a rotation and a reflection. It has not examined internal rearrangements across several principal planes.

This proves the familiar threshold for the planar choice. It does not tell us that a higher-dimensional W is a direct sum of these same planar choices. An arbitrary source-preserving S can rearrange directions *within* U and *within* its complement, so the global list of displacement singular values can change shape.

### What two equal angles permit

Now let U be a two-dimensional coordinate plane in real four-space. Write a vector as two two-component pieces. For an angle theta, define a canonical map D that sends a source vector, with second component zero, to the vector whose first component is cosine theta times the source and whose second component is sine theta times the source. Its action on the whole space is a direct sum of two equal planar rotations.

Let A be an ordinary rotation by theta inside the two-dimensional source coordinates. Apply A to each of the two component spaces before applying D. This produces another orthogonal W, equal to D composed with the block-diagonal map having A in each block. It still carries U onto the same V, because A merely changes coordinates within the source plane.

What changes is W's action on the ambient four-space. Two orthogonal planes, built by pairing a vector with its quarter-turned copy, reveal the answer. On one such plane W is the identity. On the other it is a rotation through twice theta. The direct map D instead rotates two planes through theta each.

Now measure how much each ambient direction moves. The direct rotation gives four equal displacement singular values. Each is twice the sine of half theta. All four directions contribute.

The coupled transporter has a different list: twice sine theta, twice sine theta, zero, zero. On a suitable two-plane the vectors move farther, while on its perpendicular two-plane the map acts as the identity.

The trace norm adds the four lengths before squaring any of them. It can therefore reward the coupled map for leaving half the directions fixed, despite its larger maximum displacement. The operator norm asks the opposite question: how far does the most affected direction move?

For trace norm the direct cost is eight times the sine of half theta. The coupled map costs four times the sine of theta. The double-angle formula says this second cost equals the first times the cosine of half theta. For every strictly positive theta, that cosine is less than one. Thus W has strictly smaller trace cost, even if theta is far below sixty degrees.

The planar threshold remains true. It simply addresses a smaller feasible family.

### Why squared displacement can still be minimal

At forty-five degrees, the four singular values of the direct displacement are all approximately point seven six five. The coupled competitor has approximately one point four one four, one point four one four, zero, zero.

Square the lists. The direct values become four copies of point five eight six. The competitor becomes two, two, zero, zero. Every Ky Fan prefix of the squared direct list is no larger than the corresponding prefix of the competitor list. Yet the sum of the *unsquared* values is larger for D.

Taking square roots entry by entry does not preserve weak-majorization comparisons. The square-root function rewards distributing a fixed amount of squared energy across more entries. This is why the positive squared-displacement theorem and the failed universal trace-norm claim can coexist.

### A lower bound that never depended on the direct rotation

There is still a universal comparison for unsquared full displacement. Denote the source and target orthogonal projections by P and Q. The transport constraint gives Q equal to W P W adjoint.

The geometric obstacle is visible in the projections. Let P project onto the source and Q onto the target. Their difference measures how much the two subspaces disagree. Any map W carrying one subspace onto the other must pay at least that much displacement, in every unitarily invariant norm.

Here is the reason. Form the source reflection J by making it plus one on U and minus one on U perpendicular. Form the target reflection the same way using V. Since W sends both source pieces to their corresponding target pieces, transporting first and reflecting second agrees with reflecting first and transporting second.

Each reflection equals twice its projection minus the identity. The difference of the two reflections is therefore twice Q minus twice P. Multiply that difference by W. Using their intertwining property, the result can be written as W times J minus J times W: a commutator.

Now replace each occurrence of W in this commutator by identity plus W minus identity. The identity terms cancel. What remains is the difference of two products, each containing W minus identity and one orthogonal reflection. Multiplication by a reflection leaves an invariant norm unchanged. The triangle inequality therefore bounds the commutator by **twice** the norm of identity minus W.

But the commutator also represents **twice** the difference of the two projections, up to the orthogonal factor W. The factors of two cancel. We obtain the promised lower bound: the norm of P minus Q is no greater than the norm of identity minus W, for every admissible W. This bound applies whether or not the direct rotation minimizes the chosen norm.

The bound does not say that D achieves equality. In the four-dimensional equal-angle trace example, the coupled transporter does achieve equality, while D has larger cost. We can therefore certify that the competing map is globally trace-optimal without searching through every orthogonal matrix.

### Conclusion

A two-dimensional angle restriction can settle the choice between planar rotation and reflection. The unrestricted ambient problem includes internal source and complement motions, and those motions can couple principal planes. Restricted singular-value optimality survives; squared full-displacement optimality survives. A universal unsquared statement requires its own argument, and for trace norm in the real four-dimensional case the direct rotation is not the minimizer.

## The four-dimensional real counterexample

Consider two two-dimensional subspaces in real four-space whose principal angles are both forty-five degrees. The canonical direct rotation is obvious once the principal planes are known: rotate each plane by forty-five degrees. We will build a second, equally admissible orthogonal motion that fixes two ambient directions completely and turns the other two through ninety degrees. Its trace-norm displacement is strictly smaller.

We will verify three things independently: that the competing map really carries the source onto the target, that the subspaces have the claimed principal angles, and that the competing map has the claimed singular values. Only after those checks can the cost comparison refute a universal optimality statement.

### Construct the subspaces first

Write real four-space as two copies of the ordinary coordinate plane. We can specify any ambient vector by giving two planar vectors, x and y. The source U consists of all pairs where y is zero. So x can move freely in two directions, while the other two coordinates begin at zero. This is a two-dimensional source inside a four-dimensional ambient space.

Fix an angle theta strictly between zero and ninety degrees, and abbreviate its cosine and sine by c and s. Define the direct rotation D of this four-space by the following rule. Its first output component is c times x minus s times y. Its second output component is s times x plus c times y.

This is an orthogonal map because the usual cosine-sine rotation identity works componentwise. It sends U onto V, where V consists of the pairs c x and s x as x ranges over the coordinate plane. The source and target both have dimension two.

To find their principal angles, choose an orthonormal basis of U and use its images under D as an orthonormal basis of V. The matrix of overlaps between these two bases is simply c times the two-by-two identity. Its two singular values are c. Therefore both principal angles equal theta. In particular, theta equal forty-five degrees satisfies the printed sixty-degree restriction with room to spare.

### Introduce an internal rotation

Inside the two-dimensional coordinate plane, let A be the ordinary counterclockwise rotation by theta. Construct a new ambient orthogonal operator W by first applying A to x and A to y, and then applying D.

The first stage is orthogonal because each A is. The second stage is orthogonal because D is. Therefore their composition W is orthogonal. On a vector in U, whose second component is zero, the result is the pair c times A x and s times A x. As x ranges over the plane, so does A x. Thus W of U equals V exactly.

This is a proof of admissibility, not an assertion based on the appearance of a matrix. We are now free to compare W against D for a norm that measures full ambient displacement.

### Find the two planes on which W acts simply

We want to understand W without expanding a four-by-four characteristic polynomial. The trick is to describe two planes by how their two coordinate pieces relate.

Let J be the quarter-turn in the ordinary coordinate plane. It rotates a vector by ninety degrees, and applying J twice sends a vector to its negative. The internal rotation A is cosine theta times identity plus sine theta times J.

Consider first the pairs x and J x. If x points to the right, J x points upward. So one example of such a four-dimensional vector is the pair of planar arrows right and up. These pairs fill a two-dimensional plane inside the ambient four-space.

Apply W to such a pair. The internal A turns both pieces forward by theta. The subsequent D turns this linked pair back by theta. The two effects cancel. Every vector of this form is fixed by W.

For a second family, use the pairs x and minus J x: right paired with down in the example. These pairs form the orthogonal complement of the fixed plane. This time the internal turn and the direct rotation reinforce one another. W sends x to A applied twice to x, a rotation through twice theta, and preserves the negative-quarter-turn relation between the two components.

We have accounted for all four ambient dimensions. Two form a fixed plane; the other two form a plane rotated through twice theta. That is the mental picture behind the singular values.

The eigenvalue picture follows without diagonalizing a four-by-four characteristic polynomial. W fixes two orthogonal directions and rotates their perpendicular plane through twice theta. Its displacement has two zero singular values and two equal nonzero singular values, each twice the sine of theta.

The canonical D has a different distribution. It rotates two perpendicular principal planes through theta, so all four singular values of identity minus D are twice the sine of half theta.

### Compare the costs at forty-five degrees

Set theta equal to forty-five degrees. The two nonzero singular values of identity minus W become square root of two, while the other two are zero. Its trace norm, the sum of all four singular values, is two square roots of two, approximately two point eight two eight.

For D, all four singular values are equal. Each is approximately point seven six five. Exactly, it is the square root of the quantity two minus square root of two. Adding four copies gives a trace cost of approximately three point zero six one.

The decimal comparison tells us which cost is smaller. To verify it exactly, both costs are positive, so compare their squares.

The direct trace cost squared is sixteen times two minus square root of two. The competitor cost squared is eight. Subtracting gives a positive quantity precisely when square root of two is less than three halves. That last statement follows by squaring again: two is less than nine quarters.

So the strict improvement is an exact inequality, with no reliance on rounding.

This supplies two acute real subspaces, an admissible orthogonal transporter, and a specific invariant norm for which the direct rotation loses. That is enough to disprove a statement asserting that D minimizes *every* such norm under a sixty-degree threshold.

### Check the positive squared displacement too

The example is stronger when we calculate the quantity that remains optimal. For D, the eigenvalues of its positive squared displacement are four copies of two minus square root of two, about point five eight six. For W, they are two, two, zero, zero.

At prefixes of length one through four, the direct sums are approximately point five eight six, one point one seven two, one point seven five seven, and two point three four three. The competitor prefixes are two, four, four, and four. Every prefix of the direct squared list is smaller.

Consequently the direct rotation satisfies the squared-displacement theorem here. It also has smaller Frobenius displacement, whose square is the sum of the squared singular values. It loses only the unsquared trace-norm comparison in this calculation. The two conclusions concern different spectral operations.

### Certify global trace optimality

We have proved that W beats D. To know whether W is actually best among *all* orthogonal transports, we need a lower bound that applies to every competitor.

The source and target each have an orthogonal projection. Their difference measures the unavoidable geometric change between the subspaces. For any orthogonal transporter Z carrying U to V, the trace norm of its full displacement is at least the trace norm of that projection difference. A reflection-commutator argument proves the bound without assuming Z preserves principal planes.

Our two principal angles are both theta. Each contributes two projection-difference singular values, each equal to the sine of theta. So the projection-difference trace norm is four times the sine of theta.

Now look back at W. It has exactly two moving singular directions, each with displacement twice the sine of theta. Their sum is also four times the sine of theta. W reaches the lower bound shared by all admissible transports. That is why it is a global trace-norm minimizer, not just an improvement over D.

The same calculation works for every positive theta at most a right angle. D costs eight times the sine of half theta, while W costs four times the sine of theta. The double-angle formula makes the second cost the first multiplied by the cosine of half theta, strictly less than one for positive theta. Thus no positive angle threshold, however small, can make the printed unsquared all-norm assertion valid for arbitrary real ambient dimensions.

### Conclusion

The transport constraint allows a coordinated internal rotation of the source and its complement. In four real dimensions that freedom changes two small ambient rotations into one larger rotation and one fixed plane. The full trace norm favors the latter, while the squared displacement favors the canonical direct rotation. The distinction comes from the actual singular-value lists, and it persists for arbitrarily small positive principal angles.

## Corrected scopes and surviving results

Imagine four directions in space. A transporter moves each of them by a distance just under point eight. Another transporter moves two directions by about one point four and fixes two completely. Which motion is cheaper? If the cost is the largest displacement, the first one wins. If the cost is the sum of squared displacements, the first also wins. If the cost is the sum of the displacement lengths, the second wins.

These are the actual singular-value patterns in a four-dimensional subspace transport example with two principal angles of forty-five degrees. They give us a practical way to distinguish the theorems that hold from a printed claim about unsquared ambient transport that does not.

### The geometric data do not determine the cost function

Let U and V be subspaces of equal finite dimension in a real or complex inner-product space, and let W range over unitary or orthogonal maps carrying U onto V. When the appropriate direct rotation D exists, it is an especially symmetric choice. Its action is fixed by the principal-angle geometry.

To tell whether W is economical, we must decide which movement is being charged. We might charge only vectors that **start in the source U**. We might instead measure how far an orthonormal source frame tilts away from the target. Or we might charge movement in **every ambient direction**, including those perpendicular to U.

For whole-space movement, there is one more choice. We can square displacement lengths first, forming the positive Gram operator of identity minus W, or we can measure unsquared displacement directly. Those choices lead to different comparisons.

This gives a hierarchy of questions. First: which input directions count? Second: how are their movements combined? The word optimal must answer both questions before we can state a theorem.

### Restricted movement has the strongest pointwise control

For a source unit vector x, the canonical principal match has a displacement chord of length twice the sine of half its angle. The restricted theorem formalizes this across all directions in U. It says the ordered singular values of identity minus D restricted to U are no larger than those for identity minus W restricted to U.

This is a pointwise statement about an ordered list, so it immediately controls every invariant norm of the restricted map. It has no claim about the independent motion of W on U perpendicular.

For a simple example, take two perpendicular lines in separate principal planes, both at forty-five degrees to their targets. Restricted to the two-dimensional source, D has two equal singular values of approximately point seven six five. A transporter can agree with D on the source while rotating or reflecting the source complement very differently. Its restricted cost remains the same, but its full displacement can change.

The other source-only result concerns angular error of an orthonormal frame. For each source basis vector x, its sine-angle error relative to its transported image dominates the length of the component of x perpendicular to V. Summing the squares of those projection escapes over the source basis gives the sum of the squared principal sines. This is an energy lower bound, not a pointwise eigenvalue assertion for full displacement.

### Squared whole-space movement uses a second argument

To include the whole ambient space, count directions in U and also directions perpendicular to U. Because W carries U onto V, it carries the perpendicular pieces onto one another as well. So the restricted singular-value comparison applies **twice**.

Squaring these two comparisons gives control of the two diagonal blocks of the positive Gram operator of full displacement. But the competitor may still have cross terms connecting the blocks. Merely combining the two diagonal eigenvalue lists would overlook those terms.

Pinching supplies the missing step. Reflect across the split into U and its perpendicular complement, conjugate the competitor's Gram operator by that reflection, and average the result with the original. The cross terms cancel. Averaging cannot increase any Ky Fan sum, meaning the sum of the largest chosen number of eigenvalues.

The direct rotation's Gram operator already respects the split, so it is unchanged by this average. Comparing the two source halves, merging their eigenvalue lists, and then applying pinching gives the whole-space result. We get control of the *prefix sums of squared singular values*. That conclusion is weaker than controlling each unsquared singular value separately, and it is exactly strong enough for the next class of norms.

This is what the whole-space squared-displacement theorem proves. Its proof supplies weak-majorization control of squared singular values, not pointwise control of unsquared singular values.

### Which full-displacement norms inherit the result?

The operator norm does: the largest squared singular value is the square of the largest singular value. The Hilbert–Schmidt norm does too: its square is the trace of the positive Gram operator. More generally, the Schatten p norms for p at least two satisfy the same pattern. Their squares are invariant norms of the Gram operator with exponent p over two.

The norms whose squares can be written as invariant norms of the positive Gram operator are called Q-norms. For these norms, the squared-displacement theorem does give exact optimality of the direct rotation, under the hypotheses that provide the direct rotation and the restricted bounds. There is no separate universal sixty-degree restriction in this result.

Here is the practical meaning. If we care about the single worst displacement, or about the sum of squared displacements, direct rotation wins. If we care instead about the sum of unsquared lengths, we have changed the question.

Go back to the two four-element displacement lists. The direct rotation gives about point seven six five in every position. The coupled transporter gives about one point four one four in two positions and zero in the other two.

The maximum entry favors the direct rotation. So does the sum of squares. But trace norm adds the entries directly: about three point zero six one for the direct rotation, versus two point eight two eight for the coupled map.

These are three answers to three different questions about the same motions. Before applying an optimality theorem, we must ask whether it measures the largest movement, total squared movement, or total movement length.

Thus the printed general statement about **every** invariant norm of unsquared ambient displacement cannot be correct. An acute two-subspace pair in real four-space refutes it, and an equal-angle family gives the same failure at every strictly positive angle.

### A universal lower bound and a controlled approximation

Even when D does not minimize a chosen unsquared norm, the difference of source and target projections gives a universal lower bound. If P and Q are those projections and W transports U onto V, then for every invariant norm N, the norm of P minus Q is no greater than the norm of identity minus W.

The proof uses the source and target reflections, twice their projections minus identity. Their conjugacy under W expresses twice the projection difference as a commutator involving W minus identity. The triangle inequality gives the bound with constant one, because the factor of two from the reflection difference cancels the factor of two from the commutator estimate.

For D itself, each positive principal angle theta contributes two displacement singular values, each equal to twice the sine of half theta. For P minus Q, it contributes two singular values equal to the sine of theta. The ratio is one divided by the cosine of half theta.

If the largest principal angle is at most sixty degrees, each ratio is at most two divided by the square root of three. Symmetric-gauge monotonicity therefore gives an approximation guarantee: the norm of identity minus D is at most that factor times the norm of identity minus W for every competitor W. It does **not** say D minimizes the norm.

The four-dimensional equal-angle example shows this factor is attained in trace norm at theta equal to sixty degrees. The direct trace cost is four, while the coupled map costs two times the square root of three and attains the projection-difference lower bound. Their ratio is exactly two divided by the square root of three. This makes the approximation constant sharp for the stated short-angle comparison.

### Real and complex transport have different choices

There is one last distinction: we can carry subspaces over the real numbers or over the complex numbers. In complex space, multiplying every vector in a complex line by the same unit-magnitude phase does not change the line. It does change how far individual vectors travel. So complex transport has an extra way to adjust full displacement.

On one complex principal plane of angle theta, take the ordinary direct rotation, interpreted as a unitary map. Its two eigenphases are plus theta and minus theta. Now multiply the whole two-dimensional block by the complex phase corresponding to minus theta. The two eigenphases become zero and minus twice theta. The map still carries the source complex line to the target complex line, because multiplying all its outputs by a scalar phase does not change that line.

One eigenphase is now zero, so one singular value of displacement vanishes. The other is twice the sine of theta. The trace cost on this plane is therefore twice the sine of theta, equal to the trace norm of the difference between the two rank-one projections. We have concentrated the motion into one complex direction instead of distributing it across two.

Do this independently on each complex principal plane, with identity on common directions. In finite dimension, the resulting unitary transporter attains the projection-difference trace lower bound and is therefore globally trace-optimal. The canonical direct rotation generally does not have that trace cost.

In real space, multiplying a two-dimensional block by an arbitrary complex phase is unavailable. In the minimal plane, the competing choices are a rotation and a reflection; weak majorization yields the sixty-degree threshold for the direct rotation to beat reflection in every invariant norm. In four real dimensions, separate principal planes can be coupled. That is the first ambient dimension where the corresponding universal claim fails.

### Conclusion

Restricted displacement has pointwise singular-value control. Squared full displacement has Ky Fan prefix control. Q-norms carry that squared result back to selected unsquared norms. For an arbitrary unsquared invariant norm, the projection difference is a lower bound and the direct rotation has a quantitative approximation guarantee, but exact optimization depends on the scalar field and on the admissible ambient couplings. These statements answer distinct mathematical questions and can all be true simultaneously.

## Classification and realizations of direct rotations

In the plane, two distinct lines through the origin are classified up to a common rotation by the acute angle between them. If we rotate both lines together, their absolute coordinates change, but the angle between them does not.

For two subspaces in a larger Hilbert space, one angle is no longer enough. Some directions may lie in both subspaces; some in one subspace and perpendicular to the other; and the remaining directions come in two-dimensional principal-angle pieces. Those cases must be recorded separately.

For example, in three dimensions, compare the horizontal plane with a plane spanned by their common first coordinate axis and the vertical axis. The subspaces have one shared direction with principal angle zero and one perpendicular pair with principal angle ninety degrees. A single operator norm of their projection difference reports only the largest angle and loses the shared direction.

The classification theorem packages the common and defect dimensions together with the cosine operator on the generic part. We will use it to ask when a direct rotation exists, what its uniqueness condition really means, and how to realize a prescribed list of angles. In infinite dimensions, compactness adds useful discrete spectral structure, while noncompact angle operators can carry continuous spectral data.

### Four elementary pieces

Take two closed subspaces, U and V, of a Hilbert space. Split the ambient space according to their intersections. The common part belongs to both. The source defect belongs to U and is perpendicular to V. The target defect belongs to V and is perpendicular to U. The exterior part is perpendicular to both.

Every vector in one of these pieces has an immediately understood relationship to the two subspaces. Common vectors need no movement. Source-defect vectors sit at a right angle to every vector of V. Target-defect vectors are the corresponding right-angle directions from the other side. Exterior vectors should remain outside both.

Remove those four closed pieces and look at their orthogonal complement. This is the generic part. There, neither a zero principal angle nor an exact right angle contributes an eigenvector of the elementary kinds just listed.

The distinction between the dimensions of the source and target defects is already decisive. For a direct rotation through right angles, every source-defect direction needs a target-defect partner. A quarter-turn sends the first to the second and the second to the negative of the first. That is an orthogonal, orientation-compatible action on their direct sum. If one defect space has greater Hilbert dimension than the other, no such matching can cover both.

For example, in real three-space let U be the first coordinate axis and let V be the plane spanned by the second and third axes. The source defect has dimension one, and the target defect has dimension two. This is a legitimate pair of subspaces, but the crossed defects cannot be paired. No direct rotation of the prescribed kind transports U onto V.

Contrast that with two perpendicular lines in the plane. The two crossed defects both have dimension one. The quarter-turn exists, even though the pair is not acute. Thus an exact right angle is not by itself an obstruction: unmatched right-angle multiplicity is the obstruction.

### The generic cosine operator

On the generic part, write the pair using Halmos's two-projection construction. In suitable coordinates, the first projection picks out the first factor. The second has a block whose upper-left entry is cosine squared, whose off-diagonal entries are cosine times sine, and whose lower-right entry is sine squared.

These are positive commuting operators, and their squares add to the identity. Think of them as many simultaneous principal planes, but without assuming that a basis of individual planes exists.

The cosine operator contains the relative position data. If it is diagonalizable, its eigenvalues are cosines of principal angles. In general there may be continuous spectrum, so an enumerable list of angles is insufficient. The correct invariant is the operator itself up to unitary equivalence, together with the four elementary dimensions.

To see why an operator is needed, consider multiplication by a varying function on an L two space. It may have no eigenvectors, yet it has a perfectly definite spectrum and changes the geometry of the associated pair. Any classification that merely counts principal-angle eigenvectors would miss that example.

Thus, for arbitrary Hilbert-space pairs, the Halmos decomposition has two kinds of data: the four elementary multiplicities, and the unitary-equivalence class of the generic cosine-square operator. A global unitary identifying two pairs must preserve each kind of data. Conversely, matching these data lets us assemble a unitary from the individual elementary identifications and a compatible unitary on the generic model.

### Why compactness simplifies the answer

Now suppose the relevant generic cosine operator is compact. The spectral theorem for compact positive operators says its positive spectral data consist of eigenvalues of finite multiplicity, with only zero available as an accumulation point.

We can record the positive eigenvalues as a decreasing sequence, repeated according to multiplicity, or equivalently record the dimension of the eigenspace for each positive eigenvalue. Both describe the same compact operator up to unitary equivalence, provided the kernel information is handled too.

For this application, remember that elementary zero-angle and right-angle multiplicities live in separate summands. We should not try to smuggle them into a generic eigenvalue sequence. A zero of the generic cosine may be excluded by generic-position hypotheses even when zero remains in its continuous spectrum.

Compactness makes the classification numerical; it does not abolish the four elementary dimensions.

### Building a prescribed angle sequence

We can run the process backward. Suppose we choose angles theta one, theta two, and so on between zero and ninety degrees. For simplicity first assume each lies strictly between those endpoints.

Take an orthogonal sum of two-dimensional coordinate planes. In each plane, let U use the horizontal axis, and let V use the unit line with horizontal component cosine theta and vertical component sine theta.

The projection onto U has matrix with entries one, zero, zero, zero. The projection onto V has entries cosine squared, cosine sine, cosine sine, sine squared. Assembled as a direct sum, these give the prescribed principal-angle blocks.

If we want infinitely many angles, use the Hilbert direct sum of those planes. Boundedness is automatic for the projection blocks because cosine and sine have magnitude at most one. If the angles tend to zero, the squared-sine defect operator is compact, as its diagonal entries tend to zero. That compactness statement concerns the sine defect; it is different from compactness of the cosine itself.

We can add common directions, exterior directions, and matched pairs of perpendicular directions. This realizes the elementary multiplicities as well as the angle data. The construction also shows why a direct rotation on the generic planes is straightforward: rotate each plane by its prescribed angle, with a consistent sign convention.

### Acuteness, uniformity, and uniqueness

There remains an infinite-dimensional subtlety. It is possible for every angle to be strictly less than ninety degrees while a sequence of angles approaches ninety degrees. In that case, no individual perpendicular vector exists, but the largest-angle supremum is still ninety degrees.

The polar construction of the canonical intertwiner is tied to the cosine operator and its kernel. When both crossed defects vanish, the canonical partial-isometry construction has the appropriate unitary extension. A uniform projection gap below one gives stronger information: the cosine is bounded below and has a bounded inverse, so the direct rotation can also be written by the usual inverse-square-root formula without a singular limiting problem.

Do not confuse those two levels of hypothesis. Absence of an exact perpendicular vector does not guarantee a uniform gap.

Finally, this classification does not restore the false full-displacement optimization claim we examined previously. The geometry may determine a canonical direct rotation uniquely while another admissible transporter has a smaller unsquared trace displacement. Classification and optimization ask different questions.

### Final reconstruction

If you need to classify a pair, begin by extracting the four elementary intersection pieces. Match their dimensions. On the generic remainder, compare the cosine-square operators by unitary equivalence. In the compact case, compare their positive eigenvalues with multiplicities. If instead you need a concrete realization, build an orthogonal sum of principal planes and append the elementary pieces. And if you need a direct rotation, check crossed-defect matching and the desired boundedness or acuteness hypotheses before writing a polar formula.

Classification, realization, and direct rotation therefore have distinct hypotheses: classification matches the full relative-position data, realization constructs a pair with prescribed data, and rotation additionally requires compatible crossed defects and the chosen transport conditions.

## From rotation counterexample to real transport matching

Two equal-dimensional subspaces in real Euclidean space can be connected by many orthogonal transformations. One natural choice rotates each principal plane by its smallest angle. That is the direct rotation, and it has several genuine optimality properties.

But suppose our objective is the sum of the singular values of the full displacement from the identity, or more generally a Schatten norm with exponent between one and two. In four dimensions, moving two principal planes separately can be beaten by a different orthogonal transporter that mixes the matching of directions. This is why the shortest individual rotations need not minimize every global norm of the full motion.

The optimization problem has two inputs: a pair of subspaces and a class of allowed orthogonal maps carrying one onto the other. The objective is a function of the singular values of identity minus the transporter. The correct answer depends on the exponent and on which directions are paired in the transport.

We will reduce the geometry to principal-angle blocks, identify the finite matching decision, and explain how lower bounds and explicit constructions fit together. The problem is over real orthogonal transports; a complex unitary problem can have a different feasible set and therefore requires its own analysis.

### What are we optimizing?

Take two subspaces K and L of equal finite dimension inside a real Euclidean space. Consider every orthogonal operator U that maps K onto L. Measure its displacement from the identity using a Schatten p norm. Concretely, take every singular value of the difference between U and the identity, raise it to power p, add, and then take the pth root.

For p equal two, this is the Frobenius norm. For p equal one, it is the nuclear or trace norm. When p lies strictly between one and two, the contribution of a set of singular values differs from its squared-energy contribution. That is precisely where the direct rotation can lose optimality.

Why do we require equal dimensions? An invertible orthogonal map preserves dimension. If K and L have different dimensions, no such U maps one onto the other, regardless of how close their projections might be. We would first need a different admissible notion of transport.

### The single principal-angle block

Begin with a single principal angle theta between two lines. In their common real two-dimensional principal plane, an orthogonal rotation through theta maps the first line to the second. Its displacement operator has two equal singular values, each equal to twice the sine of half theta. Therefore its pth power Schatten cost is two times the pth power of twice the sine of half theta.

There is a choice of the sign of the rotation, but its singular values are the same. Reflections can also map one line to the other. Their displacement costs may differ, so the full optimization must allow all orthogonal transports, not just orientation-preserving rotations.

With two or more principal angles, a naive strategy would minimize the cost in each principal plane independently and sum. That works for some objectives, but our four-dimensional counterexample demonstrated a failure of unrestricted independent-plane optimality.

The missing degree of freedom is a coupling between two principal-angle blocks. A four-dimensional orthogonal operator can mix their coordinates while still mapping the entire source subspace onto the target. It might produce a more favorable distribution of displacement singular values under the chosen exponent.

### Why a matching appears

The real transport optimization turns that freedom into a finite combinatorial problem. Label the positive principal angles. Each label can remain a singleton, carrying the best permitted one-angle cost, or it can be paired with another label, carrying the best two-angle cost from a four-dimensional block.

A matching consists of disjoint pairs together with unmatched singletons. Represent it by a permutation that equals its own inverse: a fixed point denotes a singleton, and a two-cycle a paired block. No angle label can belong to two different pairs.

The cost of a matching is the sum of singleton weights and complete pair weights. If we sum over all labels rather than over edges, each pair contributes half its full weight at each endpoint, so it is counted exactly once. The minimum over all matchings exists because the set of involutive permutations of finitely many labels is finite.

This is a substantial simplification. Instead of optimizing over a continuum of orthogonal matrices all at once, we can evaluate finitely many candidate matchings, where the difficult continuous optimization has been absorbed into the one-angle and two-angle weights.

### An exact two-angle test

Suppose the positive principal angles are theta and psi. There are two combinatorial candidates. One leaves both labels unmatched. Its cost is the sum of the two singleton costs. The other pairs them, and its cost is a single optimized four-dimensional value.

The global minimum is the smaller of those two numbers. For p equal two, the squared Frobenius objective is tied directly to the sum of squared displacements, and the canonical direct rotation satisfies the established squared-objective theorem. For exponents strictly between one and two, the paired option can be better.

The optimized cost of a paired block need not equal the cost of the direct rotation acting independently on its two principal planes. The correct pair cost minimizes over both relevant four-dimensional determinant classes. Replacing it with the direct rotation's candidate cost would assert an optimality property that fails for the unsquared objective.

For three positive angles, the finite choices are: three singletons, or one pair and one singleton. For four, we also have two disjoint pairs. In general, the number of matchings grows, but the mathematical structure stays finite and explicit.

### The two directions of an optimality proof

A formula for the minimum needs two distinct inequalities. First, every admissible real orthogonal transporter must have a displacement cost at least the matching minimum. Second, every candidate matching, or at least an optimal matching, must be realizable by a genuine orthogonal transporter with exactly the assigned cost.

The first direction is an extraction theorem. It analyzes an ambient optimizer and shows that its cost is represented by suitable singleton and paired blocks, preserving the original principal-angle labels. The second direction is a realization theorem. It assembles orthogonal blocks into an ambient transporter with the required action on the source subspace.

Neither direction can be replaced merely by noting that the minimum of finitely many numbers exists. A combinatorial optimizer might describe no actual geometric operator unless realization is proved. Conversely, a construction of candidate transports does not rule out a more exotic, lower-cost orthogonal matrix.

The result combines two arguments in finite-dimensional real spaces with equal-dimensional subspaces and Schatten exponent p strictly between one and two: a lower bound extracting matching data from every ambient optimizer, and an upper bound constructing an orthogonal transporter from an optimizing matching. Repeated and zero principal angles remain legitimate labeled inputs.

### Why the exponent matters

The nuclear norm is the sum of singular values, and the Frobenius norm comes from their squared sum. A cost that is additive in squared singular values rewards a different distribution than a cost that is additive in singular values themselves. Between powers one and two, changing the singular-value distribution by mixing principal planes can be advantageous.

This is why one must name the exponent in an optimality theorem. The best operator for one Schatten norm need not minimize another. The direct rotation's optimality for a squared objective does not imply its optimality for an unsquared objective, even though the underlying pair of subspaces is identical.

There are also delicate endpoint questions. A theorem proved for exponents strictly between one and two should not be quoted as automatically covering p equal one or p equal two. Continuity of an optimized value can help study endpoint costs, but a complete endpoint statement may need its own realization and attainment arguments.

### Scope of the matching theorem

For real finite-dimensional Hilbert spaces with equal-dimensional source and target subspaces, and Schatten exponent p strictly between one and two, there is an orthogonal transporter attaining the matching minimum. Every admissible orthogonal transporter has pth-power displacement cost at least this value, and an optimizing matching can be realized geometrically.

The assumptions include finite dimension, a real inner product, equal source and target dimension, and p strictly between one and two. The conclusion concerns the pth power of the Schatten norm of identity minus the transporter; taking the pth root preserves comparisons because p is positive. The theorem does not state a universal result for arbitrary symmetric gauges or every exponent.

To reconstruct the argument, begin with principal planes, calculate the two equal singular values of a planar rotation, state the optimized one- and two-angle costs, and prove that any matching can be assembled by orthogonal direct sum. Then identify the genuinely difficult converse: ruling out an ambient transport more efficient than every matching. That converse is why this is a mathematical theorem rather than a convenient search heuristic.

The matching theorem supplies a positive classification for the stated real Schatten optimization problem. Its assumptions on dimension, rank, and exponent remain part of the claim.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Unsquared ambient displacement is different

**Draft status:** audio-first mathematical lecture. **Prerequisites:** `130000–132000`. **Next:** `134000`.

---

#### Companion: mathematics and Lean correspondence (display only)

##### Exact transport fiber and why its stabilizer can mix principal planes

Fix one admissible orthogonal transport \(D(U)=V\). Every other admissible
orthogonal \(W\) factors uniquely as
\[
W=DS,\qquad S=D^*W,\qquad S(U)=U,\quad S(U^\perp)=U^\perp.
\]
Relative to \(U\oplus U^\perp\), \(S=A\oplus B\) with independent orthogonal
blocks. There is no requirement that these blocks preserve the principal vectors.
For repeated principal angles, selecting nontrivial \(A,B\) redistributes
full-space displacement without changing \(U,V\) or their principal angles.

For one real principal plane the direct and reflecting candidates have
\(s(I-D)=(a,a)\), \(s(I-F)=(2,0)\),
\(a=2\sin(\theta/2)\). Weak majorization of \((a,a)\) by \((2,0)\)
is equivalent to \(2a\le2\), hence \(\theta\le\pi/3\). This implication is
specific to that one-plane comparison.

For the global lower bound, put \(P=P_U\), \(Q=P_V\),
\(J_P=2P-I\), \(J_Q=2Q-I\). Since \(J_QW=WJ_P\),
\[
2(Q-P)W=(J_Q-J_P)W=WJ_P-J_PW
=(W-I)J_P-J_P(W-I).
\]
Every unitarily invariant norm \(N\) therefore satisfies
\[
2N(Q-P)\le 2N(W-I),\quad\text{so}\quad N(P-Q)\le N(I-W).
\]
The proof uses no angle restriction and does not assume optimality of \(D\).

The printed real claim is a universal inequality for \(N(I-D)\) over every unitarily invariant norm and every orthogonal \(W\) mapping \(U\) to \(V\) when \(\theta_{\max}\le\pi/3\). The repository represents it as a proposition-valued definition and proves its negation. The planar candidates have singular values \((2\sin(\theta/2),2\sin(\theta/2))\) and \((2,0)\). Their all-gauge weak-majorization threshold is \(\theta\le\pi/3\), but this planar classification does not extend to arbitrary four-dimensional transporters.

For all admissible \(W\), \(N(P_U-P_V)\le N(I-W)\). This is a general lower bound, not an optimality assertion for \(D\).

#### Exact Lean declaration excerpts

**`example4_1_directRotation_uiNorm_minimal_of_le_pi_div_three`.** This is the **two-dimensional Example 4.1 model**, with a Boolean choice between direct and reflecting transporter. It does not assert arbitrary-dimensional minimality.

`DavisKahan/Sources/DavisKahan1970/Section4LowDimensional.lean` — `example4_1_directRotation_uiNorm_minimal_of_le_pi_div_three` (exact declaration header; proof body omitted):

```lean
theorem example4_1_directRotation_uiNorm_minimal_of_le_pi_div_three
    {theta : ℝ} (h0 : 0 ≤ theta) (hpi : theta ≤ Real.pi / 2)
    (hθ : theta ≤ Real.pi / 3)
    (flip : Bool)
    (N : UnitarilyInvariantSeminorm ℝ RealPlane RealPlane) :
    N (LinearMap.id - example41DirectRotation theta) ≤
      N (LinearMap.id - example4_1_competitor theta flip) :=
```

**`DavisKahanProposition4_4_Finite`.** This is the proposition-valued **false** printed assertion. It universally quantifies over real finite-dimensional spaces, acute pairs below `π/3`, transporters, and unitarily invariant seminorms.

`DavisKahan/FiniteDimensional/DirectRotation/ShortRotationCounterexample.lean` — `DavisKahanProposition4_4_Finite` (exact declaration header; proof body omitted):

```lean
def DavisKahanProposition4_4_Finite : Prop :=
```

**`projectionDifference_uiNorm_le_displacement`.** For every admissible transporter and invariant seminorm, projection difference is a lower bound for **full** displacement with no small-angle assumption.

`DavisKahan/FiniteDimensional/DirectRotation/ProjectionDisplacement.lean` — `projectionDifference_uiNorm_le_displacement` (exact declaration header; proof body omitted):

```lean
theorem projectionDifference_uiNorm_le_displacement
    (N : UnitarilyInvariantSeminorm 𝕜 E E)
    (U V : Submodule 𝕜 E)
    [U.HasOrthogonalProjection] [V.HasOrthogonalProjection]
    (W : E ≃ₗᵢ[𝕜] E) (hmap : U.map W.toLinearMap = V) :
    N (U.starProjection.toLinearMap - V.starProjection.toLinearMap) ≤ N (LinearMap.id -
        W.toLinearMap) :=
```

### The four-dimensional real counterexample

**Draft status:** audio-first mathematical lecture. **Prerequisites:** `042000–045000`, `132000–133000`. **Next:** `135000`.

---

#### Companion: mathematics and Lean correspondence (display only)

##### A parameterized, verified four-dimensional family

Write \(\mathbb R^4=\mathbb R^2\oplus\mathbb R^2\),
\(J=\begin{psmallmatrix}0&-1\\1&0\end{psmallmatrix}\),
\(c=\cos\theta\), \(s=\sin\theta\), and
\[
A_\theta=cI+sJ,\qquad
D_\theta=\begin{pmatrix}cI&-sI\\sI&cI\end{pmatrix},\qquad
W_\theta=D_\theta\begin{pmatrix}A_\theta&0\\0&A_\theta\end{pmatrix}.
\]
Both factors in \(W_\theta\) are orthogonal. Let
\(U=\{(x,0):x\in\mathbb R^2\}\),
\(V=\{(cx,sx):x\in\mathbb R^2\}\). Since
\(W_\theta(x,0)=(cA_\theta x,sA_\theta x)\), one has \(W_\theta U=V\).
The cross-Gram matrix for the natural orthonormal frames of \(U,V\) is
\(cI_2\), giving exactly two principal angles equal to \(\theta\).

Set \(M_+=\{(x,Jx)\}\) and \(M_-=\{(x,-Jx)\}\). These are orthogonal,
span \(\mathbb R^4\), and satisfy
\[
W_\theta|_{M_+}=I,\qquad
W_\theta(x,-Jx)=(A_\theta^2x,-JA_\theta^2x).
\]
Thus the latter restriction rotates through \(2\theta\). Exact singular values:
\[
\begin{aligned}
s(I-D_\theta)&=(2\sin(\theta/2))^{[4]},\\
s(I-W_\theta)&=(2\sin\theta,2\sin\theta,0,0),\\
s(P_U-P_V)&=(\sin\theta)^{[4]}.
\end{aligned}
\]
Therefore \(\|I-W_\theta\|_1=4\sin\theta=\|P_U-P_V\|_1\) is
the **global** trace minimum; for \(0<\theta\le\pi/2\),
\(\|I-D_\theta\|_1=8\sin(\theta/2)>4\sin\theta\).

At \(\theta=\pi/4\), a separate coordinate realization already certified
by `ShortRotationCounterexample.lean` is the sign matrix \(W\) displayed
below. Its eigenvalues and trace costs agree with the family above; no
identity between these two coordinate matrices is asserted.

With \(U=\operatorname{span}(e_1,e_2)\) and
\[
W=\tfrac12\begin{pmatrix}
1&-1&-1&-1\\1&1&1&-1\\-1&-1&1&-1\\1&-1&1&1
\end{pmatrix},\quad V=WU,
\]
the cross-Gram matrix has \(C^*C=\tfrac12I_2\), so \(\theta_1=\theta_2=\pi/4\). The singular values are
\[
s(I-W)=(\sqrt2,\sqrt2,0,0),\qquad
s(I-D)=(\sqrt{2-\sqrt2},\sqrt{2-\sqrt2},\sqrt{2-\sqrt2},\sqrt{2-\sqrt2}).
\]
Hence \(\|I-W\|_1=2\sqrt2<4\sqrt{2-\sqrt2}=\|I-D\|_1\). Yet \(s((I-D)^*(I-D))\prec_w s((I-W)^*(I-W))\). The exact matrix and refutation are in `ShortRotationCounterexample.lean`; a continuum of equal-angle examples is documented in `papers/dk_formalization_journal/counterexample.tex`.

#### Exact Lean declaration excerpts

**`Wmat`.** The explicit real `4×4` witness matrix is `½` times a sign matrix. Its orthogonality and transport properties are established elsewhere in the same source module.

`DavisKahan/FiniteDimensional/DirectRotation/ShortRotationCounterexample.lean` — `Wmat` (exact declaration header; proof body omitted):

```lean
@[expose] def Wmat : Matrix (Fin 4) (Fin 4) ℝ :=
```

**`principalAngle_le`.** The source proves the maximal principal angle is at most `π/3` for the exact witness (and the module establishes that both angles equal `π/4`).

`DavisKahan/FiniteDimensional/DirectRotation/ShortRotationCounterexample.lean` — `principalAngle_le` (exact declaration header; proof body omitted):

```lean
theorem principalAngle_le : Submodule.principalAngles U4 V4 0 ≤ Real.pi / 3 :=
```

**`kyFanSum_lt`.** This proves the strict reversed trace-norm comparison at full Ky Fan rank four.

`DavisKahan/FiniteDimensional/DirectRotation/ShortRotationCounterexample.lean` — `kyFanSum_lt` (exact declaration header; proof body omitted):

```lean
theorem kyFanSum_lt :
    (LinearMap.id - Wequiv.toLinearMap).kyFanSum 4 <
      (LinearMap.id -
        (directRotation U4 V4 acute).toLinearMap).kyFanSum 4 :=
```

**`shortRotation_fullDisplacement_refuted`.** The witness includes real subspaces, acuteness, an admissible unitary, a short largest principal angle, and a strict trace-norm improvement.

`DavisKahan/FiniteDimensional/DirectRotation/ShortRotationCounterexample.lean` — `shortRotation_fullDisplacement_refuted` (exact declaration header; proof body omitted):

```lean
theorem shortRotation_fullDisplacement_refuted :
    ∃ (U V : Submodule ℝ (EuclideanSpace ℝ (Fin 4)))
      (hacute : Submodule.IsAcute U V)
      (W : EuclideanSpace ℝ (Fin 4) ≃ₗᵢ[ℝ] EuclideanSpace ℝ (Fin 4)),
      U.map W.toLinearMap = V ∧
      Submodule.principalAngles U V 0 ≤ Real.pi / 3 ∧
      (LinearMap.id - W.toLinearMap).kyFanSum 4 <
        (LinearMap.id - (directRotation U V hacute).toLinearMap).kyFanSum 4 :=
```

**`not_davisKahanProposition4_4_Finite`.** This discharges the formal negation of the universal proposition by instantiating it with trace norm.

`DavisKahan/FiniteDimensional/DirectRotation/ShortRotationCounterexample.lean` — `not_davisKahanProposition4_4_Finite` (exact declaration header; proof body omitted):

```lean
theorem not_davisKahanProposition4_4_Finite :
    ¬ DavisKahanProposition4_4_Finite.{0} :=
```

### Corrected scopes and surviving results

**Draft status:** audio-first mathematical lecture. **Prerequisites:** `130000–134000`. **Next:** `136000`.

---

#### Companion: mathematics and Lean correspondence (display only)

##### Numerical scope comparison and sharp short-angle ratio

For the real equal-angle pair \(\theta_1=\theta_2=\pi/4\), let
\(a=\sqrt{2-\sqrt2}\) and \(b=\sqrt2\). A canonical direct rotation
and a coupled admissible transport have displacement singular-value lists
\(a^{[4]}\) and \((b,b,0,0)\). Their costs are
\[
\begin{array}{c|cc}
& D & W\\\hline
\|I-\cdot\|_\infty & a & b\\
\|I-\cdot\|_2 & 2a & 2\\
\|I-\cdot\|_1 & 4a & 2b\\
\|\,(I-\cdot)^*(I-\cdot)\,\|_1 & 4a^2 & 4
\end{array}
\]
Thus the Q-norm comparisons and the reversed nuclear-norm ordering are
consistent on the same input pair.

For a principal angle \(\theta\), the two nonzero singular values of
\(I-D\) on its real principal plane are \(2\sin(\theta/2)\),
whereas those of \(P_U-P_V\) are \(\sin\theta\). Hence, for maximum angle
\(\theta_{\max}<\pi\) in the direct-rotation regime,
\[
\|I-D\|_N\le\sec(\theta_{\max}/2)\|P_U-P_V\|_N
\le\sec(\theta_{\max}/2)\|I-W\|_N.
\]
At \(\theta_{\max}=\pi/3\) the factor is \(2/\sqrt3\). The real
four-dimensional equal-angle family gives
\(\|I-D\|_1=4\), \(\|I-W\|_1=2\sqrt3\), with \(W\) attaining the
projection-difference lower bound: the factor is sharp.

For a **complex** principal plane, \(D_\theta\) has eigenvalues
\(e^{\pm i\theta}\). Multiplication by the complex scalar
\(e^{-i\theta}\) preserves the target complex line and gives a transporter
with eigenvalues \((1,e^{-2i\theta})\), displacement singular values
\((0,2\sin\theta)\), and trace cost equal to the rank-one projection
trace distance. Direct sums produce finite-dimensional complex trace attainers.
The real scalar field does not permit this phase multiplier.

For \(WU=V\), the source-supported inequalities include:
\[
\begin{aligned}
s_k((I-D)|_U)&\le s_k((I-W)|_U),\\
\| (I-D)^*(I-D)\|_{\mathcal I}&\le\|(I-W)^*(I-W)\|_{\mathcal I},\\
\|I-D\|_{Q}&\le\|I-W\|_{Q},\\
\|P_U-P_V\|_N&\le\|I-W\|_N.
\end{aligned}
\]
The second inequality requires a suitable invariant norm/ideal and its membership assumptions; the third requires the Q-norm property. The first is restricted displacement, the final two concern full displacement.

For finite-dimensional complex spaces, a **phase-corrected** transporter attains \(\min_{WU=V}\|I-W\|_1=2\sum_j\sin\theta_j=\|P_U-P_V\|_1\), but need not be the canonical direct rotation. The conventional real line/hyperplane result appears in `REAL_TRANSPORT_MINIMIZATION_NOTES.md` and is explicitly **not** certified there as a compiled Lean theorem. The `ℝ⁴` counterexample and Q-norm repair are compiled source results.

#### Exact Lean declaration excerpts

**`directRotation_fullDisplacement_qnorm`.** The Q-norm repair applies to **unsquared full** displacement; without `IsQNorm`, the implication from squared-displacement optimality is unjustified.

`DavisKahan/FiniteDimensional/DirectRotation/QNorm.lean` — `directRotation_fullDisplacement_qnorm` (exact declaration header; proof body omitted):

```lean
theorem directRotation_fullDisplacement_qnorm
    (N : UnitarilyInvariantSeminorm 𝕜 E E) (hN : IsQNorm N)
    (U V : Submodule 𝕜 E)
    [U.HasOrthogonalProjection] [V.HasOrthogonalProjection]
    (hacute : Submodule.IsAcute U V) (W : E ≃ₗᵢ[𝕜] E)
    (hmap : U.map W.toLinearMap = V) :
    N (LinearMap.id - (directRotation U V hacute).toLinearMap) ≤
      N (LinearMap.id - W.toLinearMap) :=
```

**`uiNorm_directRotation_le_two_div_sqrt_three_mul_displacement`.** This is an approximation-factor bound under a short-angle hypothesis, not a minimizer theorem.

`DavisKahan/FiniteDimensional/DirectRotation/SharpDisplacement.lean` — `uiNorm_directRotation_le_two_div_sqrt_three_mul_displacement` (exact declaration header; proof body omitted):

```lean
theorem uiNorm_directRotation_le_two_div_sqrt_three_mul_displacement
    (N : UnitarilyInvariantSeminorm 𝕜 E E)
    (U V : Submodule 𝕜 E)
    [U.HasOrthogonalProjection] [V.HasOrthogonalProjection]
    (hacute : Submodule.IsAcute U V)
    (hgap : U.projectionGap V ≤ Real.sin (Real.pi / 3))
    (W : E ≃ₗᵢ[𝕜] E) (hmap : U.map W.toLinearMap = V) :
    N (LinearMap.id - (directRotation U V hacute).toLinearMap) ≤
      (2 / Real.sqrt 3) * N (LinearMap.id - W.toLinearMap) :=
```

**`exists_global_complex_trace_minimizer_with_principalAngles`.** Finite-dimensional **complex** spaces with equal-rank subspaces admit a phase-corrected trace-norm minimizer whose cost equals twice the sum of principal sines. It need not be the canonical direct rotation.

`DavisKahan/FiniteDimensional/DirectRotation/ComplexTracePrincipalAngles.lean` — `exists_global_complex_trace_minimizer_with_principalAngles` (exact declaration header; proof body omitted):

```lean
theorem exists_global_complex_trace_minimizer_with_principalAngles
    (U V : Submodule ℂ H) [U.HasOrthogonalProjection]
    [V.HasOrthogonalProjection]
    (hUV : finrank ℂ U = finrank ℂ V) :
    ∃ W : H ≃ₗᵢ[ℂ] H,
      U.map W.toLinearMap = V ∧
      (LinearMap.id - W.toLinearMap).kyFanSum (finrank ℂ H) =
        (U.starProjection.toLinearMap - V.starProjection.toLinearMap).kyFanSum (finrank ℂ H) ∧
      (LinearMap.id - W.toLinearMap).kyFanSum (finrank ℂ H) =
        2 * ∑ j : Fin (finrank ℂ U), Real.sin (Submodule.principalAngles U V (j : ℕ)) ∧
      ∀ Z : H ≃ₗᵢ[ℂ] H, U.map Z.toLinearMap = V →
        (LinearMap.id - W.toLinearMap).kyFanSum (finrank ℂ H) ≤
          (LinearMap.id - Z.toLinearMap).kyFanSum (finrank ℂ H) :=
```

**`proposition4_3_directRotation_sourceExact_complex`.** The source-facing squared-displacement theorem explicitly takes `IsSourceDirectRotation`, preserving the paper’s definition rather than weakening it to an arbitrary rotation predicate.

`DavisKahan/Sources/DavisKahan1970/Section4DirectRotationSource.lean` — `proposition4_3_directRotation_sourceExact_complex` (exact declaration header; proof body omitted):

```lean
theorem proposition4_3_directRotation_sourceExact_complex
    [TopologicalSpace.SeparableSpace H]
    (N : NormalizedUnitaryInvariantNorm.{0, v} ℂ)
    (U V : Submodule ℂ H) [U.HasOrthogonalProjection] [V.HasOrthogonalProjection]
    (hcompact : IsCompactOperator (TauCeti.principalSineOperator U V))
    (D : H →L[ℂ] H) (hD : DavisKahan.IsSourceDirectRotation U V D)
    (W : H →L[ℂ] H) (hWunitary : W ∈ unitary (H →L[ℂ] H))
    (hWmap : W * U.starProjection = V.starProjection * W)
    (hWmem : N.Mem ((1 - star W) * (1 - W))) :
    N.Mem ((1 - star D) * (1 - D)) ∧
      N.gauge ((1 - star D) * (1 - D)) ≤ N.gauge ((1 - star W) * (1 - W)) :=
```

### Classification and realizations of direct rotations

**Draft status:** audio-first mathematical lecture. **Prerequisites:** `045000–051000`, `049000–050000`, `130000–135000`. **Next:** `137000`.

---

#### Companion: mathematics and Lean correspondence (display only)

For orthogonal projections onto closed subspaces \(U,V\), define
\[
H_{11}=U\cap V,\quad H_{10}=U\cap V^\perp,\quad
H_{01}=U^\perp\cap V,\quad H_{00}=U^\perp\cap V^\perp.
\]
The generic part is the orthogonal complement of their sum. Its positive commuting cosine and sine operators satisfy \(C^2+S^2=I\). Unitary equivalence of the pairs preserves elementary multiplicities and the generic positive-contraction operator, including its non-eigenvalue spectral information. At appropriate compact scope, positive eigenvalue multiplicities classify the generic part. For a diagonal model with \(\theta_n\to0\), \(S^2\) is compact; \(C\) need not be compact.

#### Exact Lean declaration excerpts


**`theorem3_1_realization_ofAngles`.** An admissible abstract angle datum is realized by a pair of closed subspaces. The ambient Hilbert space and two block dimensions are supplied by the datum; this is not a theorem that arbitrary angle lists fit inside a prechosen finite-dimensional ambient space.

`DavisKahan/Sources/DavisKahan1970/Section3Theorem31Realization.lean` — `theorem3_1_realization_ofAngles` (exact declaration header; proof body omitted):

```lean
theorem theorem3_1_realization_ofAngles
    {Θ₀ : E →L[𝕜] E} {Θ₁ : F →L[𝕜] F}
    (hΘ₀ : IsSelfAdjoint Θ₀) (hΘ₁ : IsSelfAdjoint Θ₁)
    (_hspec₀ : spectrum ℝ Θ₀ ⊆ Set.Icc 0 (Real.pi / 2))
    (_hspec₁ : spectrum ℝ Θ₁ ⊆ Set.Icc 0 (Real.pi / 2))
    (J : E →L[𝕜] F) (hJ : J ∘L Θ₀ = Θ₁ ∘L J)
    (hisom : ContinuousLinearMap.adjoint J ∘L J ∘L cfc Real.sin Θ₀ = cfc Real.sin Θ₀)
    (hcoisom : J ∘L ContinuousLinearMap.adjoint J ∘L cfc Real.sin Θ₁ = cfc Real.sin Θ₁) :
    (∀ x : E, (sourceSubspace 𝕜 E F).starProjection
        ((HalmosAngleDatum.ofIntertwinedAngles hΘ₀ hΘ₁ J hJ hisom
            hcoisom).targetSubspace.starProjection (modelInl 𝕜 E F x)) =
          modelInl 𝕜 E F (cfc Real.cos Θ₀ (cfc Real.cos Θ₀ x))) ∧
      (∀ y : F, (sourceSubspace 𝕜 E F)ᗮ.starProjection
        (((HalmosAngleDatum.ofIntertwinedAngles hΘ₀ hΘ₁ J hJ hisom
            hcoisom).targetSubspace)ᗮ.starProjection (modelInr 𝕜 E F y)) =
          modelInr 𝕜 E F (cfc Real.cos Θ₁ (cfc Real.cos Θ₁ y))) ∧
      halmosCommonPart (sourceSubspace 𝕜 E F)
          (HalmosAngleDatum.ofIntertwinedAngles hΘ₀ hΘ₁ J hJ hisom hcoisom).targetSubspace =
        Submodule.map (modelInl 𝕜 E F : E →ₗ[𝕜] WithLp 2 (E × F))
          (LinearMap.ker ((cfc Real.sin Θ₀ : E →L[𝕜] E) : E →ₗ[𝕜] E)) ∧
      halmosExteriorPart (sourceSubspace 𝕜 E F)
          (HalmosAngleDatum.ofIntertwinedAngles hΘ₀ hΘ₁ J hJ hisom hcoisom).targetSubspace =
        Submodule.map (modelInr 𝕜 E F : F →ₗ[𝕜] WithLp 2 (E × F))
          (LinearMap.ker ((cfc Real.sin Θ₁ : F →L[𝕜] F) : F →ₗ[𝕜] F)) ∧
      halmosSourceDefect (sourceSubspace 𝕜 E F)
          (HalmosAngleDatum.ofIntertwinedAngles hΘ₀ hΘ₁ J hJ hisom hcoisom).targetSubspace =
        Submodule.map (modelInl 𝕜 E F : E →ₗ[𝕜] WithLp 2 (E × F))
          (LinearMap.ker ((cfc Real.cos Θ₀ : E →L[𝕜] E) : E →ₗ[𝕜] E)) ∧
      halmosTargetDefect (sourceSubspace 𝕜 E F)
          (HalmosAngleDatum.ofIntertwinedAngles hΘ₀ hΘ₁ J hJ hisom hcoisom).targetSubspace =
        Submodule.map (modelInr 𝕜 E F : F →ₗ[𝕜] WithLp 2 (E × F))
          (LinearMap.ker ((cfc Real.cos Θ₁ : F →L[𝕜] F) : F →ₗ[𝕜] F)) ∧
      Nonempty (↥(halmosSourceDefect (sourceSubspace 𝕜 E F)
          (HalmosAngleDatum.ofIntertwinedAngles hΘ₀ hΘ₁ J hJ hisom
            hcoisom).targetSubspace) ≃ₗᵢ[𝕜]
        ↥(halmosTargetDefect (sourceSubspace 𝕜 E F)
          (HalmosAngleDatum.ofIntertwinedAngles hΘ₀ hΘ₁ J hJ hisom
            hcoisom).targetSubspace)) :=
```


**`pairOfSubspacesUnitaryEquivalent_iff_sameCompactAngleData`.** The four elementary Halmos summands and positive generic-angle multiplicities form the complete invariant under the specific compactness hypotheses on the sandwiched projections.

`DavisKahan/Geometry/Halmos/CompactClassification.lean` — `pairOfSubspacesUnitaryEquivalent_iff_sameCompactAngleData` (exact declaration header; proof body omitted):

```lean
theorem pairOfSubspacesUnitaryEquivalent_iff_sameCompactAngleData
    (hc₁ : IsCompactOperator (U₁.starProjection ∘L V₁.starProjection ∘L U₁.starProjection))
    (hc₂ : IsCompactOperator (U₂.starProjection ∘L V₂.starProjection ∘L U₂.starProjection)) :
    PairOfSubspacesUnitaryEquivalent U₁ V₁ U₂ V₂ ↔
      SameCompactAngleData U₁ V₁ U₂ V₂ :=
```


**`isCompactOperator_angleSinSqOp`.** This construction concerns the *squared sine* diagonal operator when the prescribed angles tend to zero; it must not be confused with compactness of the cosine operator.

`DavisKahan/Geometry/Halmos/AngleSequenceRealization.lean` — `isCompactOperator_angleSinSqOp` (exact declaration header; proof body omitted):

```lean
theorem isCompactOperator_angleSinSqOp (hlim : Tendsto θ atTop (nhds 0)) :
    IsCompactOperator (angleSinSqOp 𝕜 θ) :=
```

### From rotation counterexample to real transport matching

**Draft status:** audio-first mathematical lecture. **Prerequisites:** `034000–038000`, `042000–051000`, `130000–135000`. **Next:** `146000`.

---

#### Display-only mathematical and Lean correspondence

The matching program lives in `DavisKahan/FiniteDimensional/DirectRotation/SchattenRealMatching.lean`, `.../SchattenRealMatchingWeights.lean`, and `.../RealMatchingAttainment.lean`. For a planar rotation by `θ`, the two displacement singular values equal `2 sin(θ/2)`; the direct-rotation **candidate** p-cost is therefore `2(2 sin(θ/2))^p`. The singleton and paired weights in the matching theorem refer to their own optimized class-specific definitions, not to this candidate formula by default.

The source theorem `exists_minimizing_real_schatten_transport_matching` proves the unrestricted ambient minimum for real finite-dimensional equally ranked subspaces and `1<p<2`. Do not extend the result to other exponents merely from this declaration.

#### Exact Lean declaration excerpts

**`realSchattenMatchingCost`** — The combinatorial cost sums fixed-point singleton weights and half a paired weight at each endpoint of a two-cycle. The paired weight comes from the optimized four-dimensional model.

Source: `DavisKahan/FiniteDimensional/DirectRotation/SchattenRealMatching.lean`; exact declaration header (proof body omitted).

```lean
def realSchattenMatchingCost {ι : Type*} [Fintype ι]
    (p : ℝ) (theta : ι → ℝ) (s : Equiv.Perm ι) : ℝ := by
```

**`exists_attains_realSchattenMatchingMinimum`** — This theorem only attains the FINITE COMBINATORIAL minimum. It does not by itself construct an ambient orthogonal transporter.

Source: `DavisKahan/FiniteDimensional/DirectRotation/SchattenRealMatching.lean`; exact declaration header (proof body omitted).

```lean
theorem exists_attains_realSchattenMatchingMinimum {ι : Type*} [Fintype ι]
    (p : ℝ) (theta : ι → ℝ) :
    ∃ s : Equiv.Perm ι, Function.Involutive s ∧
      realSchattenMatchingCost p theta s = realSchattenMatchingMinimum p theta := by
```

**`exists_minimizing_real_schatten_transport_matching`** — This theorem supplies the missing geometric attainment and global comparison for equal-dimensional REAL subspaces with Schatten exponent strictly between one and two.

Source: `DavisKahan/FiniteDimensional/DirectRotation/RealMatchingAttainment.lean`; exact declaration header (proof body omitted).

```lean
theorem exists_minimizing_real_schatten_transport_matching
    (p : ℝ≥0∞) [Fact (1 ≤ p)] (hp : p ≠ ∞)
    (hp1 : 1 < p.toReal) (hp2 : p.toReal < 2)
    (K L : Submodule ℝ E) (hKL : Module.finrank ℝ K = Module.finrank ℝ L) :
    ∃ U : E ≃ₗᵢ[ℝ] E, K.map U.toLinearMap = L ∧
      UnitarilyInvariantSeminorm.schatten ℝ E E p
          (LinearMap.id - U.toLinearMap) ^ p.toReal =
        realPositiveSchattenMatchingMinimum p.toReal
          (fun j : {j : Fin (Module.finrank ℝ K) // 0 < K.principalAngles L j} =>
            K.principalAngles L j.val) ∧
      ∀ T : E ≃ₗᵢ[ℝ] E, K.map T.toLinearMap = L →
        UnitarilyInvariantSeminorm.schatten ℝ E E p
            (LinearMap.id - U.toLinearMap) ^ p.toReal ≤
          UnitarilyInvariantSeminorm.schatten ℝ E E p
            (LinearMap.id - T.toLinearMap) ^ p.toReal := by
```
