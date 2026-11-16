# Weak measurements, bounded inverses, and representation

<!-- BEGIN SPOKEN LECTURE -->

# Weak measurements, bounded inverses, and representation

## Hahn–Banach: Extending Measurements and Seeing Weak Convergence

Imagine that you have learned to measure signals of a very specific form. Perhaps your measuring device was designed only for signals that are constant across an interval. Or perhaps it was calibrated on the finite-dimensional subspace spanned by a small collection of waveforms. On that familiar subspace, the measurement is linear and its output is bounded by the size of the input.

Now the larger space contains many more signals. Can we extend the measurement to every signal while retaining exactly the same sensitivity bound? We do not want to invent an extension that produces huge readings on small inputs. And we are not asking whether there is a unique extension: many different extensions may agree on the calibrated subspace.

The Hahn–Banach theorem answers the existence question with a remarkable yes. Every bounded linear functional on a subspace of a normed vector space extends to the entire space without increasing its norm. The theorem is true for real and complex spaces, and the full space does not even have to be complete.

This is one of the structural facts that makes the idea of a dual space powerful. It says that a measurement on a small part of a space can be made globally consistent with the same numerical bound. And it implies that the continuous dual has enough measurements to detect every nonzero vector and distinguish a point from a closed linear subspace.

### First, an extension you can see

Take the ordinary plane, but measure vector size by the larger of the absolute values of its two coordinates. Focus only on the diagonal line: vectors whose two coordinates agree. Along that line, define a measurement that returns the common coordinate. The measurement has norm one. An input of size one cannot produce a reading larger than one.

One extension to the whole plane returns the first coordinate. Another returns the second coordinate. Both agree on the diagonal and both have norm one. A third returns the average of the two coordinates. Again the same norm, again the same values on the diagonal. In fact, there is a whole interval of norm-preserving extensions.

So the theorem is about existence with controlled size, not unique recovery. The information known on a subspace may leave the off-subspace behavior underdetermined. That is important in applications: extending a linear observable without increasing its norm is an abstract mathematical guarantee, not a method for recovering the one physically intended measurement.

The question is why the same principle works in spaces with infinitely many independent directions. We will first add just one direction and see the key inequality that makes the proof possible.

### Adding one new direction without breaking the bound

Suppose the space is real. We have a linear functional on a subspace M, and its readings are bounded by a constant times the input norm. Choose a vector x-zero outside M. Every vector in the enlarged span has a unique form: a vector m from M plus a scalar multiple of x-zero. If we choose the value of the extended functional on x-zero, linearity determines all other new values.

So one extension step boils down to selecting one real number, call it a. The old measurement and the value a must cooperate so that the bound still holds for every vector in this larger span.

The condition imposes both upper and lower restrictions on a. Vary the vector m, and you get a collection of permissible lower bounds. Vary it another way, and you get upper bounds. At first it seems possible that the lower restrictions force a above the upper restrictions, making any extension impossible.

But the triangle inequality—the same inequality that defines our norm—guarantees those ranges do not cross. It lets us compare the lower requirement from one old vector with the upper requirement from another by adding the two old vectors and cancelling the new direction. The old functional already obeys the norm bound, so the cancellation makes the inequality work.

Choose any a in the resulting interval. Now the measurement extends to one more independent direction without changing its norm. Nothing in this step depends on the dimension being finite.

To reach an arbitrary space, we organize all possible norm-preserving extensions by inclusion: an extension is larger if it is defined on a larger subspace and agrees with the smaller one. Every totally ordered family of such extensions has a consistent union. A maximal-extension principle, commonly formulated as Zorn's lemma, then gives an extension that cannot be enlarged. If its domain were not the whole space, the one-direction construction would enlarge it. That contradiction finishes the real theorem.

For complex vector spaces, the proof needs another step because one complex direction contains two real directions. We apply the real theorem to the real part of the functional and then reconstruct the complex-linear functional from that real-linear extension. The norm is preserved. The result is the complex Hahn–Banach theorem.

This proof is not an explicit recipe for writing down an extension in every infinite-dimensional case. The maximal-extension step invokes a choice principle. What it provides is a global existence theorem with a sharp bound.

### No vector can hide from every bounded measurement

Choose a nonzero vector x in any normed space. Define a measurement on the one-dimensional subspace spanned by x: ask for the coefficient of x, multiplied by the norm of x. This functional has norm one and reads exactly the norm of x when applied to x itself.

Hahn–Banach extends that measurement to the entire space without increasing its norm. Therefore, for every nonzero x, there is some bounded linear functional of norm one whose absolute reading on x equals the norm of x.

Notice the distinction from an operator necessarily attaining its norm. We are choosing a functional *in response to a specified vector*. We are not claiming that every pre-existing functional has a maximizing vector. Hahn–Banach tells us that the entire family of functionals is rich enough to find one tailored to any given nonzero input.

This immediately yields a dual formula for the norm: the norm of x is the supremum of the absolute values of all norm-one-bounded measurements applied to x. One inequality follows because every such measurement is bounded by the input norm. The other follows from the norm-one functional we just constructed.

Now consider a closed linear subspace M and a point x outside it. We can separate x from M with a bounded linear functional that vanishes on all of M and is nonzero on x. In fact, we can arrange its value on x to equal the distance from x to M while its norm is one. The construction passes to the quotient space X modulo M, where vectors differing by an element of M are treated as equivalent. The quotient norm of x is precisely that distance. A norming functional on the quotient pulls back to the desired measurement on X.

Closedness matters. If x lay in the closure of M, every continuous functional vanishing on M would also have to vanish at x. We cannot demand a strictly separating continuous measurement where no positive distance exists.

### Convergence viewed through every observer

We can now define a weaker kind of convergence. A sequence of vectors converges weakly to x if every bounded linear functional assigns readings that converge to the reading of x. In other words, no fixed continuous linear measurement can distinguish the later vectors from x in the limit.

Norm convergence implies weak convergence: a bounded functional cannot amplify a norm-small difference by more than its norm. But weak convergence does not require the vectors themselves to become close in norm. Different observers can all see convergence without a common uniform error bound over every possible observer.

Think of the standard basis in the Hilbert space of square-summable sequences. The first vector has a one in the first coordinate and zeros elsewhere; the second has a one in the second coordinate; and so on. Every vector in the sequence has norm one, so the vectors do not approach zero in norm.

Yet choose any fixed continuous linear functional. In this Hilbert space, it is represented by an inner product with some square-summable coefficient sequence. Applying the functional to the n-th basis vector picks out the n-th coefficient. Since the coefficients form a square-summable sequence, they must tend to zero. Therefore every fixed bounded linear measurement tends to zero, and the basis vectors converge weakly to zero.

This is a genuine change of viewpoint. Norm convergence asks for one uniform bound covering all unit-norm measurements simultaneously. Weak convergence allows the accuracy threshold to depend on which measurement was selected. Every observer eventually sees a tiny reading, but observers chosen differently at each stage can keep finding a full-size discrepancy.

### Weak convergence is not automatic in every sequence space

It is tempting to conclude that standard basis vectors always converge weakly to zero in any infinite-dimensional sequence space. That is false. In the space of absolutely summable sequences, the functional that sums all coordinates is bounded: its absolute value cannot exceed the sum of their absolute values. Applied to each standard basis vector, that functional returns one. So the sequence cannot converge weakly to zero in L-one's sequence counterpart, usually called ell-one.

The contrast between ell-one and ell-two is informative. The geometric and dual structures differ; the available measurements differ; and hence the weak convergence behavior differs. The same coordinatewise picture does not guarantee the same weak limit.

We should also avoid confusing weak convergence of vectors with weak-star convergence of functionals. If we consider elements of X-star as vectors in their own right, weak convergence there uses every element of its dual, the double dual. Weak-star convergence of functionals means only testing each functional against fixed vectors in X. Those are different collections of observers, and weak-star convergence can be strictly weaker.

The double dual gives us a natural map from each vector x into the functional on X-star that sends a measurement to its value on x. Our norm formula shows this map preserves norm. When it happens to be onto, the space is called reflexive. Hilbert spaces and L-p spaces for p strictly between one and infinity are reflexive; many endpoint spaces are not. A full proof of these characterizations requires more work, but the language explains why functionals can themselves be analyzed as mathematical objects.

### What must come next

There is an important assertion we have not proved: a weakly convergent sequence is bounded in norm. It sounds plausible, but its quantifiers are delicate. Weak convergence tells us that for each fixed functional, its readings on the sequence are bounded. It does not directly give a single bound uniform across all functionals, and Hahn–Banach's norm formula is a supremum over many different functionals.

The missing tool is the uniform boundedness principle. It converts pointwise boundedness of a family of continuous linear operators into a uniform operator norm bound, provided the common input space is complete. Its proof begins not with linear algebra, but with a topological theorem about complete metric spaces: the Baire category theorem.

The path from extension of one measurement to control of whole families may seem indirect. It is not. Hahn–Banach guarantees there are enough measurements to recognize the size and location of a vector. Baire category will tell us when pointwise control of those measurements can be upgraded to a global bound. Together they make weak convergence into a serious tool rather than just a change in vocabulary.

## Weak and Weak-Star Convergence: Compactness Without Norm Convergence

Imagine a sequence of vectors whose lengths all equal one, while their nonzero entries march farther and farther along an infinite list of coordinates. The first vector has a one in the first position, the next in the second, and so on. In the ordinary norm, no two of these vectors become close. Yet if we take the inner product with a fixed square-summable vector, the answer tends to zero: the test vector's coordinates must themselves become small. This sequence converges in one sense and fails to converge in another.

Norm convergence demands that every part of a vector become close simultaneously. Weak convergence asks a more modest question: do all continuous linear measurements agree in the limit? Think of each measurement as a fixed experiment. If every such experiment eventually sees the same answer, we call the sequence weakly convergent. The marching unit vectors converge weakly to zero in the Hilbert space of square-summable sequences, even though their distance from zero is always one.

The distinction becomes useful for approximation schemes. An approximate solution may have uniformly bounded energy but retain fine oscillations. The function need not have a strongly convergent subsequence in the energy norm. Weak convergence may be available, and a weak limit can still satisfy linear equations. Convexity lets us retain something else: the norm of the limit cannot exceed the limit inferior of the norms. Energy does not suddenly increase when we take a weak limit.

But a bounded sequence does not automatically have a weakly convergent subsequence in every Banach space. Reflexivity matters. Informally, a space is reflexive when taking its continuous dual twice returns the original space without losing elements. Hilbert spaces, and L-p spaces for p strictly between one and infinity, have this property. On these spaces, closed bounded sets have the right kind of weak compactness. The spaces L-one and L-infinity generally behave differently.

A second notion, weak-star convergence, applies to functionals. Suppose our objects are themselves measurements on a space X. Rather than test them with all measurements on the dual space, we evaluate each functional at every fixed vector in X. When these values converge, we have weak-star convergence. It is deliberately weaker than weak convergence on the dual, because fewer tests are required.

Here is a concrete example. A bounded sequence of numbers defines a functional on absolutely summable sequences by multiplying corresponding coordinates and adding the results. Consider again a sequence with one nonzero coordinate moving to the right, now treated as a bounded sequence. Against any absolutely summable test sequence, the value tends to zero. So it converges weak-star to zero as an element of the dual of the absolutely summable sequences. The argument uses the fact that the coordinates of an absolutely summable sequence go to zero.

Banach–Alaoglu says something remarkable: the closed unit ball in the dual of a normed space is compact in the weak-star topology. The word compact here concerns the topology of these evaluations; it does not mean norm compact. And in general it concerns convergent subnets, not necessarily subsequences. If the underlying space is separable, the weak-star topology on the dual unit ball is metrizable, and subsequence arguments become available.

Why is this not just an abstract curiosity? Think of a sequence of bounded linear measurements, or a family of probability measures on a compact space. Their numerical responses to continuous test functions may stabilize even when there is no meaningful point-by-point density convergence. Weak-star compactness is one reason variational limits and measure-valued limits can be constructed.

The discipline is to name the topology. A proof that has produced weak convergence has not produced convergence of norms, products, or pointwise values. If a nonlinear term is involved, an extra compactness argument or some structural monotonicity may be required. Weak compactness is a powerful way to obtain candidates for solutions; it does not by itself certify that every operation passes to the limit.

## Baire Category and Uniform Boundedness: From Individual Control to a Common Bound

Imagine a collection of measuring devices. Each device transforms a signal into a reading, and every device is individually linear and continuous. There might be infinitely many of them, perhaps one for each stage of a numerical approximation or one for each frequency we examine.

Suppose you test any one signal against the entire collection. The readings may change from device to device, but they remain bounded for that particular signal. You choose another signal, test it against every device, and again the readings remain bounded. This happens for every signal in your space.

Can we conclude that there is one universal amplification bound for all the devices? It is a quantifier problem. Our hypothesis says: for each input, some bound works across the entire family. The conclusion says: one bound works simultaneously for every input of unit size. We are trying to exchange the order of “for each input” and “there exists a bound.” In general, exchanging these quantifiers is unsafe.

The uniform boundedness principle says the exchange is nevertheless valid for families of bounded linear operators whose common input space is Banach. The output spaces only need to be normed. Completeness of the input space is the decisive hypothesis.

The theorem is also called the Banach–Steinhaus theorem. Its proof depends on a seemingly different fact about complete metric spaces: they cannot be assembled from countably many closed pieces, each of which is thin everywhere. This is the Baire category theorem. Let us build the connection rather than treating the name as an explanation.

### What “thin everywhere” means

Take an interval of real numbers and mark a single point. A point is closed, but it cannot contain any interval of positive length. If you move to any open interval, there is room to avoid the marked point. In a metric space, a closed set with empty interior behaves like that: it contains no open ball, so every ball contains some point outside it.

A set is called nowhere dense if its closure has empty interior. For closed sets, that is simply the condition we just described. Now imagine covering a complete metric space by countably many such closed nowhere-dense sets.

Could the cover succeed? Baire's theorem says no. The space must contain a point that escapes all of them. Equivalently, if a complete metric space is a countable union of closed sets, at least one of those sets must contain a nonempty open ball.

This sounds like a theorem about sets rather than functions. But the proof shows why it belongs to analysis. It constructs a sequence of smaller and smaller balls, ensuring that each new ball avoids one more forbidden set. The radii shrink toward zero. Completeness guarantees that the nested search does not converge to a missing point.

Let's outline that argument. Start with any nonempty open ball. Because the first closed set has empty interior, there is a smaller closed ball lying inside our first ball but outside that set. Its radius can be chosen less than one half. The second closed set also has empty interior, so inside the first smaller ball there is another even smaller closed ball avoiding the second set, and we can keep it inside the previous ball. Continue, shrinking the radii so that they approach zero.

The centers form a Cauchy sequence: all sufficiently late centers lie in the same tiny earlier ball. In a complete metric space the centers converge to a point. Because every later ball is nested in the earlier closed balls, that limit lies inside each selected ball. But the selected ball at stage n was chosen to avoid the n-th forbidden closed set. Thus the limit avoids every forbidden set. This contradicts the claim that the countably many sets covered the entire space.

The proof never uses linearity. Completeness is enough. Linearity comes in when we apply the theorem to operator families.

### Turn pointwise bounds into closed sets

Let our Banach space of inputs be X. Let the family of bounded linear operators be T-alpha, each mapping X into a normed space Y. The collection can have any number of indices; it need not be countable.

For every positive integer m, collect the inputs x for which the norm of T-alpha applied to x never exceeds m, no matter which operator we choose. Call this set E-m. Because each operator is continuous, the condition for any one operator describes a closed set. The intersection of all those conditions, even an infinite intersection, is closed. Therefore E-m is closed.

Our hypothesis was that each fixed input has a finite bound across all operators. That means each input belongs to at least one E-m, because we can choose an integer larger than its particular bound. So X is the union of the closed sets E-one, E-two, and so on.

Baire now says that at least one E-m has an interior ball. The key new information is not just that many inputs satisfy a common bound. It is that a whole ball of nearby inputs satisfies one common bound, for every operator at once.

Suppose a ball of radius r around some center x-zero lies in E-m. We need to move the estimate from that ball to the unit ball around zero. Take a small perturbation h of x-zero, with norm less than r. Both x-zero and x-zero plus h lie in E-m. For every operator, the norms of the two outputs are at most m. By linearity, T of h is their difference. By the triangle inequality, its norm is at most two m.

We have obtained one common bound on a ball around zero. Rescale h, just as we did when deriving boundedness from continuity for a single operator, and the same reasoning provides a uniform bound on the operator norms of the entire family. Every device has operator norm bounded by the same constant.

That is the whole proof. The hidden work is the Baire step, which converts pointwise boundedness into a ball on which the bound is uniform. Once we have a ball, linearity carries the estimate everywhere.

### A family that looks safe on smooth functions

The completeness hypothesis is not optional. Let's see its force with a family of elementary measurements on continuous functions.

On the unit interval, define the n-th measurement to be n times the difference between the value of f at one over n and its value at zero. This is a finite difference quotient. For a fixed n, the measurement is continuous in the supremum norm: changing f by at most epsilon everywhere changes the two sampled values by at most epsilon each, and hence changes the reading by at most two n epsilon.

For every differentiable function near zero, the finite difference quotients eventually approach the derivative at zero. Thus the family of readings is bounded for each such smooth input. That might tempt us to claim that all the measurements have uniformly bounded norms on the space of differentiable functions.

But their operator norms do not remain bounded. For a fixed n, we can choose a smooth function that is near minus one at zero and near plus one at one over n, while staying between those heights. Its finite difference reading is close to two n, even though its supremum norm is one. The operator norm grows linearly with n.

There is no contradiction with uniform boundedness because the differentiable functions equipped only with the supremum norm do not form a complete space. Their uniform limits can fail to be differentiable. In fact, on the larger complete space of all continuous functions, the family is not pointwise bounded. Take f of x equal to the square root of x. Its finite difference at zero is the square root of n, which diverges.

The example shows exactly where the theorem fails when completeness is removed: individual tests on a noncomplete class may all look safe while the worst amplification runs away. The missing limit functions can expose the instability.

### Why strong convergence still gives some uniform control

Recall the coordinate truncation operators P-n on the square-summable sequences. For each fixed input x, P-n of x converges to x. So the family is pointwise bounded. Uniform boundedness tells us the operator norms of the P-n must have some common upper bound. In this example we already know their norms are one, but the theorem gives the bound even when no explicit calculation is available.

Do not conclude that strong convergence implies convergence in operator norm. The difference between P-n and the identity always has norm one, since there is a unit vector beyond the retained coordinates. Strong convergence gives pointwise convergence; uniform boundedness upgrades it to a uniform *bound*, not to uniform *convergence*.

A second consequence is a useful extension method. Suppose the operators have one uniform norm bound and we can prove their outputs converge on a dense collection of easy inputs. For an arbitrary input x, approximate it by an easy input d. The operator difference between x and d is uniformly small because of the common norm bound. On d we already know that sufficiently late operators are close to each other. Combining these estimates shows the outputs on x form a Cauchy sequence. If the output space is complete, they converge. Thus convergence on a dense core plus a uniform operator estimate produces convergence everywhere.

This argument is a workhorse in analysis. We first prove a theorem on smooth, finite-dimensional, or otherwise easy functions; then an operator bound lets us pass to limits and extend it to the full completed space.

### Recovering the boundedness of weakly convergent sequences

Uniform boundedness also answers a question left hanging from weak convergence. Suppose x-n converges weakly to x in a normed space X. For every continuous linear functional f, the scalar sequence f of x-n converges, and therefore remains bounded. Can the norms of x-n nevertheless grow without limit?

Turn each vector x-n into an operator on the dual space X-star: this operator takes a functional f and returns its reading f of x-n. Such evaluation operators are linear and bounded. Their common domain, X-star, is a Banach space, even if X itself is not complete.

For every fixed functional f in X-star, the readings f of x-n form a bounded sequence. So the evaluation operators are pointwise bounded. Uniform boundedness gives one common bound on their operator norms. Hahn–Banach tells us that the norm of evaluation at x-n is exactly the norm of x-n. Therefore the norms of the original weakly convergent vectors are bounded.

Notice how the two theorems cooperate. Hahn–Banach guarantees the dual is rich enough to measure each vector's norm exactly. Baire and uniform boundedness prevent a sequence from evading all fixed measurements while its norm becomes arbitrarily large. Neither step alone would make the conclusion immediate.

It does not follow that a weakly convergent sequence converges in norm. The standard basis of square-summable sequences is still the counterexample: every vector has norm one while the sequence converges weakly to zero. Boundedness is a weaker conclusion than norm convergence.

### Completeness as a principle of mathematical control

We have now encountered completeness in several roles. Completeness of the real numbers made Cauchy numerical approximations converge. Completeness of L-p made norm-Cauchy functions converge to functions inside the same space. Completeness of the common input space now forces a pointwise bounded family of operators to have bounded operator norms.

The last conclusion feels stronger because it begins with a different bound for each input. But the topology of a complete space stops an entire family of closed sets from being thin everywhere. That topological fact creates the single ball on which the family is controlled, and linearity does the rest.

This is an important transition in functional analysis. We can now extend bounded measurements by Hahn–Banach, measure transformations with operator norms, understand strong and weak convergence, and prove uniform control over entire operator families. The same Baire method will underpin two further theorems: a bounded bijection between Banach spaces has bounded inverse, and a linear operator between Banach spaces with a closed graph is bounded. Those results are natural next steps toward spectral theory, differential equations, and the mathematics of inverse problems.

## Why a Bijective Operator Has a Bounded Inverse

Imagine a measurement device. A dial gives a number and the device returns a signal. You can reverse the procedure: given a signal, find the dial setting that produced it. But a question remains. If the measured signal changes by a tiny amount, can the inferred setting change enormously?

That is the distinction between finding an inverse and having a stable inverse. In linear algebra, a square matrix with nonzero determinant has an inverse, and because the setting is finite dimensional, that inverse is automatically continuous. In spaces of functions, neither the existence of an inverse nor its stability can be assumed. Two great results of functional analysis explain why completeness rescues stability.

Let us start with a familiar bad inverse. On the interval from zero to one, take a continuously differentiable function that vanishes at zero and measure only the size of its values, using the maximum absolute value. Differentiation turns this function into another continuous function. As an algebraic map, differentiation is one-to-one and onto: integrate any continuous output from zero to x to recover the input. Yet high-frequency sine waves can be tiny in height and large in slope. The inverse, integration, is stable in the maximum norm; differentiation itself is not stable in that norm. This warns us to specify both the spaces and their norms before saying that an equation is well posed.

A cleaner example of an unstable inverse uses sequences. Let a sequence x be square summable. Form another sequence by dividing its N-th entry by N. This is a bounded, one-to-one operator. Its inverse, where defined, multiplies the N-th entry by N. A sequence concentrated in a distant coordinate barely registers in the output. Recovering its amplitude magnifies noise by N. Here the problem is that the operator is not onto the entire square-summable space. The missing surjectivity matters.

Now suppose we have two Banach spaces. That name means they are normed spaces in which every Cauchy sequence has a limit. Assume a linear operator from the first to the second is bounded, meaning that a constant controls the output norm by the input norm. Suppose it is also one-to-one and onto. The bounded inverse theorem says its inverse is bounded. Thus a genuinely bounded bijection between complete normed spaces is stable in both directions.

What does completeness have to do with it? We can hear the main idea through the open mapping theorem. It says a bounded linear map from one Banach space onto another sends every open set to an open set. A small neighborhood of the zero input therefore reaches a whole, perhaps smaller, neighborhood of the zero output. Scaling by linearity then says that every output has a preimage whose size is controlled by the output size. If the map is one-to-one, that preimage is unique, giving the bounded inverse.

To see why the theorem is not trivial, imagine mapping the unit ball of inputs into an enormous but very thin set of outputs. Surjectivity says that, if we scale and combine enough such images, every output can eventually be reached. It does not immediately say the image of the unit ball contains any neighborhood of zero. Baire's category theorem supplies this missing interior. Very roughly, a complete space cannot be assembled as a countable union of sets that are each nowhere dense. The image of the whole input space is a countable union of scaled images of its unit ball. One closure must contain some open ball. Linearity recenters this information at zero. An iterative correction argument then turns approximate outputs into actual outputs with a controlled sum of input corrections.

There is a related theorem about closed graphs. The graph of an operator is the set of pairs consisting of an input and its output. The graph is closed when converging inputs and converging outputs remain compatible: if inputs approach x and their outputs approach y, then y really is the output of x. A bounded operator automatically has a closed graph. Remarkably, a linear operator defined on all of a Banach space with values in another Banach space is bounded whenever its graph is closed.

This is an efficient way to prove continuity. Sometimes direct estimates are hard, but passing to a limit in an equation is easy. If we can show any pair of limits still satisfies the defining equation, the closed graph theorem gives the norm estimate we wanted. Notice the phrase defined on all of a Banach space. Differential operators often act only on functions with enough derivatives; for them a closed graph does not imply boundedness with respect to the ambient norm.

Why is this important for differential equations? An operator may encode the relationship between a forcing function and a solution. A uniqueness proof tells us that two solutions with the same forcing cannot differ. An existence proof tells us every admissible forcing has a solution. If this relationship is described by a bounded operator between Banach spaces, the bounded inverse theorem supplies continuous dependence on the forcing. This is the third leg of well-posedness: existence, uniqueness, and stability.

The subtlety is in selecting spaces that reflect the equation. Solving a second-order equation may gain two derivatives in a suitable sense, while the second-derivative operator is not bounded on the original space of square-integrable functions. Changing to a norm that also measures derivatives can make a closed operator into a bounded one between the correct domain and output spaces. Mathematics does not erase instability. It tells us how to diagnose it and which hypotheses are strong enough to rule it out.

The practical test is simple. When someone writes the symbol T inverse, ask: onto what space, and with which norm? If those questions have satisfactory answers, the abstract theorems turn the word inverse from an algebraic promise into an analytical guarantee.

## Radon–Nikodym and Riesz: When Measurements Have Densities

Suppose someone gives us a rule that assigns a number to every measurable region of a landscape. The rule might report area, mass, or the amount of a chemical substance in the region. A natural question is whether this information comes from a density: a function whose integral over each region produces the reported number.

Sometimes it does. Sometimes it cannot. The Radon–Nikodym theorem explains the dividing line. Another theorem, the Riesz representation theorem, describes when continuous linear measurements of vectors or functions can also be written as inner products or integrals. The two results share an idea: replace a rule that acts on whole objects by a representer that we can analyze point by point.

Start with two measures, which we will call mu and nu. Think of mu as ordinary length or area, and nu as mass. If a region has zero area, and every such region also has zero mass, we say nu is absolutely continuous with respect to mu. This is a statement about zero sets. It is not yet a statement about a formula.

For a finite measure nu and a sigma-finite base measure mu, the Radon–Nikodym theorem says that this condition is enough: there exists an integrable density, locally interpreted where needed, such that nu of a region equals the integral of the density over that region. When nu is a finite signed measure, the density may be negative; when nu is positive, the density is nonnegative. The density is unique up to changes on sets of mu measure zero.

An example on the unit interval helps. Let nu of a set be the integral over that set of twice x. Then nu is absolutely continuous with respect to length, with density twice x. The entire interval has mass one, but the right half contains more than half of the mass. The density records how that mass is distributed.

Now consider a measure concentrated entirely at the midpoint. It assigns mass one to any region containing the midpoint and zero to regions not containing it. The single point has length zero but mass one. No ordinary integrable density with respect to length can represent this measure. That is precisely what absolute continuity rules out. The point mass is not an exception to integration; it tells us we chose the wrong base measure if we expected an ordinary density.

Why should such a density exist whenever absolute continuity holds? The proof in a finite-measure setting uses the geometry of L two. Among all candidate densities that do not assign more mass to any region than nu, one constructs a maximal candidate. If there were leftover positive measure that the candidate failed to account for, a suitable local adjustment would improve it, contradicting maximality. An alternative proof uses the Hilbert-space representation theorem, and measures on general sigma-finite spaces can be handled by a countable exhaustion. The full argument needs care because measures and functions may be infinite on large regions; the essential idea is to turn a set-by-set compatibility condition into a globally defined function.

The name Riesz occurs in two related representation results. Let us first take a Hilbert space: a space with an inner product and complete norm. A bounded linear functional assigns a scalar to each vector, varying continuously and linearly with that vector. The Hilbert-space Riesz theorem says there is one unique vector g such that the functional of x is the inner product of x with g. Thus every continuous linear measurement of a Hilbert-space vector is itself encoded by a vector.

In ordinary two-dimensional geometry, the rule that measures the sum of the first coordinate and twice the second is represented by the vector with coordinates one and two. The inner product with that vector gives exactly the measurement. In a function space, the same idea becomes integration against a function g. If we work in L two, the functional of f can be written as the integral of f times the complex conjugate of g, with the usual convention about which argument is linear.

There is a useful geometric proof. If a bounded functional is nonzero, its kernel is a closed hyperplane. Find a unit vector perpendicular to that hyperplane. Every input decomposes into a part inside the kernel and a scalar multiple of the perpendicular vector. The functional ignores the kernel part. Its entire value is determined by the single scalar coefficient. That is exactly the representation by an inner product.

A separate Riesz representation theorem concerns continuous functions on a compact space. A positive linear functional on continuous functions can be represented by integration against a finite regular Borel measure. Here the representing object is a measure, not necessarily a density relative to length. For example, evaluation of a continuous function at a point is represented by a point mass. It is continuous in the maximum norm even though no ordinary L one density represents it relative to length.

These distinctions prevent several common confusions. The Hilbert-space theorem represents bounded functionals by vectors. The measure-theoretic Riesz theorem represents positive functionals on continuous functions by measures. Radon–Nikodym then asks whether that representing measure has a density with respect to another measure. None of these steps is automatic if we change the space or norm without checking assumptions.

Why does this matter elsewhere? When a numerical method reports a linear output, a Riesz representer identifies the direction in which the output is sensitive. When a probability law is absolutely continuous relative to another, Radon–Nikodym gives the likelihood ratio. When we describe a forcing term in a weak differential equation, we need to know whether it is represented by an ordinary function, an L two vector, or a more general distribution.

The general lesson is that a formula involving an integral is not merely notation. It is the conclusion of a representation theorem whose hypotheses tell us exactly which kinds of measurements can be compressed into a density, a vector, or a measure.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Hahn–Banach: Extending Measurements and Seeing Weak Convergence

**Track:** Analysis from First Principles. **Background:** Normed and Banach spaces, bounded linear functionals and dual norms, and the distinction between norm and pointwise operator convergence. **Question:** Can a bounded linear measurement defined on a subspace be extended to the whole space without increasing its sensitivity, and what does this reveal about convergence?

#### Mathematical companion (display only)

##### Norm-preserving Hahn–Banach

If \(M\subseteq X\) is a linear subspace of a real or complex normed space and \(f\in M^*\), there exists \(F\in X^*\) with
\[
F|_M=f,\qquad \|F\|=\|f\|.
\]
The more general real form: given sublinear \(p:X\to\mathbb R\), and real-linear \(f:M\to\mathbb R\) with \(f(m)\le p(m)\) for every \(m\in M\), extend \(f\) to all of \(X\) so that \(F(x)\le p(x)\) for every \(x\in X\).

##### The one-step inequality

For \(x_0\notin M\), set \(F(m+t x_0)=f(m)+t a\). A value \(a\in\mathbb R\) is admissible whenever
\[
\sup_{m\in M}[f(m)-p(m-x_0)]\ \le a\ \le
\inf_{m\in M}[p(m+x_0)-f(m)].
\]
The left side does not exceed the right: for \(m,n\in M\), linearity and subadditivity imply
\(f(m)+f(n)=f(m+n)\le p(m+n)\le p(m-x_0)+p(n+x_0)\).
Zorn's lemma yields a maximal extension after iterating the one-dimensional argument. In the complex case, extend \(u=\operatorname{Re}f\) on the underlying real space and recover \(F(x)=u(x)-i u(ix)\), with the same norm.

##### Norming functionals and subspace separation

For any \(x\ne0\), there exists \(f\in X^*\) with \(\|f\|=1\) and \(f(x)=\|x\|\). Consequently,
\[
\|x\|=\sup_{\|f\|\le1}|f(x)|.
\]
For a **closed** subspace \(M\subset X\) and \(x_0\notin M\), its quotient \(X/M\) is normed and \(d=\operatorname{dist}(x_0,M)>0\). Hahn–Banach on the quotient supplies \(f\in X^*\) with \(f|_M=0\), \(\|f\|=1\), and \(f(x_0)=d\).

##### Weak and weak-star convergence

\[
x_n\rightharpoonup x \quad\Longleftrightarrow\quad
\forall f\in X^*:\ f(x_n)\to f(x).
\]
For \(f_n\in X^*\), weak-star convergence \(f_n\overset{w^*}{\rightharpoonup}f\) means \(f_n(x)\to f(x)\) for all \(x\in X\); weak convergence in \(X^*\) tests against all elements of \(X^{**}\).

On \(\ell^2\), \(e_n\rightharpoonup0\) but \(\|e_n\|=1\), since any \(y\in\ell^2\) has \(y_n\to0\) and \(\langle e_n,y\rangle=\overline{y_n}\) with the convention linear in the first slot. On \(\ell^1\), the functional \(x\mapsto\sum_n x_n\) witnesses that \(e_n\) is not weakly null.

##### Exercises with answers

1. **Non-unique extensions:** On \((\mathbb R^2,\|\cdot\|_\infty)\), define \(f(t,t)=t\). Find two different norm-one extensions. **Answer:** \(F_1(x,y)=x\) and \(F_2(x,y)=y\).
2. **A separating functional:** In \(\mathbb R^2\) with Euclidean norm, find a norm-one functional vanishing on the horizontal axis and taking value \(2\) at \((1,2)\). **Answer:** \(F(x,y)=y\).
3. **Two weak behaviors:** Why is \(e_n\) weakly null in \(\ell^2\) but not \(\ell^1\)? **Answer:** All \(\ell^2\) representing coefficients tend to zero, while the bounded \(\ell^1\) functional summing coordinates remains one.
4. **The embedding into the double dual:** Define \(J:X\to X^{**}\) by \(J(x)(f)=f(x)\). Why is \(J\) an isometry? **Answer:** \(\|Jx\|=\sup_{\|f\|\le1}|f(x)|=\|x\|\) by Hahn–Banach.

##### References

- Terence Tao, *245B, Notes 6: Duality and the Hahn–Banach theorem*: https://terrytao.wordpress.com/2009/01/26/245b-notes-6-duality-and-the-hahn-banach-theorem/.
- Terence Tao, *245B, Notes 11: The strong and weak topologies*: https://terrytao.wordpress.com/2009/02/21/245b-notes-11-the-strong-and-weak-topologies/.
- MIT OpenCourseWare, *18.102 Introduction to Functional Analysis* (2021), lecture 5 on Zorn's lemma and Hahn–Banach: https://ocw.mit.edu/courses/18-102-introduction-to-functional-analysis-spring-2021/pages/lecture-notes-and-readings/.

### Weak and Weak-Star Convergence: Compactness Without Norm Convergence

**Track:** Analysis from First Principles. **Background:** L-p spaces, basic Hilbert spaces and weak derivatives as introduced earlier in this course. **Central question:** What assumptions make this construction rigorous?

#### Mathematical companion (not spoken)

Let \(X\) be a Banach space. \(x_n\rightharpoonup x\) in \(X\) means \(\phi(x_n)\to\phi(x)\) for every \(\phi\in X^*\). For \(\phi_n\in X^*\), \(\phi_n\overset{*}{\rightharpoonup}\phi\) means \(\phi_n(x)\to\phi(x)\) for each \(x\in X\).

For \(e_n\in\ell^2\), \(\langle e_n,y\rangle=y_n\to0\) for every \(y\in\ell^2\), so \(e_n\rightharpoonup0\) but \(\|e_n\|_2=1\). Similarly \(e_n\in\ell^\infty=(\ell^1)^*\) converges \(\sigma(\ell^\infty,\ell^1)\)-weak-star to zero. Weak lower semicontinuity: \(\|x\|\le\liminf_n\|x_n\|\) when \(x_n\rightharpoonup x\).

Banach–Alaoglu: the dual unit ball \(B_{X^*}\) is compact in \(\sigma(X^*,X)\), by embedding it as a closed subset of \(\prod_{x\in X}\{z:|z|\le\|x\|\}\). This is not generally sequential compactness; if \(X\) is separable, the weak-star topology on bounded subsets of \(X^*\) is metrizable.

If \(X\) is reflexive, its closed bounded subsets are relatively weakly compact. In a Banach space, Eberlein–Šmulian also relates weak compactness and weak sequential compactness; reflexivity is a *hypothesis*, not a consequence of boundedness.

##### Exercises with answers

1. **Coordinate test.** Why is \(e_n\rightharpoonup0\) in \(\ell^2\)? **Answer:** For each \(y\in\ell^2\), \(y_n\to0\), hence \(\langle e_n,y\rangle\to0\).
2. **Norm test.** Does \(\|e_n\|_2\to0\)? **Answer:** No; every norm equals one.
3. **Weak limit energy.** If \(u_n\rightharpoonup u\) and \(\|u_n\|\le4\), what follows? **Answer:** \(\|u\|\le4\), by weak lower semicontinuity.

##### Reading and source notes

- [MIT OpenCourseWare, Introduction to Functional Analysis](https://ocw.mit.edu/courses/18-102-introduction-to-functional-analysis-spring-2021/)
- [Princeton MAT520 Functional Analysis lecture notes](https://web.math.princeton.edu/~js129/PDFs/teaching/MAT520_fall_2025/MAT520_Lecture_Notes.pdf)

### Baire Category and Uniform Boundedness: From Individual Control to a Common Bound

**Track:** Analysis from First Principles. **Background:** Complete metric spaces, bounded operators and dual spaces, Hahn–Banach, and weak convergence. **Question:** If every fixed input is handled safely by an entire family of operators, does a single bound work for the whole family?

#### Mathematical companion (display only)

##### Baire category theorem

If \(X\) is a nonempty complete metric space, it is **not** a countable union of closed nowhere-dense sets. Equivalently, if \(X=\bigcup_{m\ge1}F_m\) with each \(F_m\) closed, then at least one \(F_m\) has nonempty interior.

Proof: assuming all \(F_m\) nowhere dense, recursively choose nonempty closed balls \(\overline B_m\) nested with \(\overline B_m\subset B_{m-1}\setminus F_m\) and radii tending to zero. Completeness and shrinking diameters supply a unique point in all balls, outside every \(F_m\), contradiction.

##### Uniform boundedness (Banach–Steinhaus)

Let \(X\) be Banach, \(Y\) a normed space, and \(\mathcal F\subset\mathcal B(X,Y)\) any family. If
\[
\forall x\in X:\quad \sup_{T\in\mathcal F}\|Tx\|_Y<\infty,
\]
then
\[
\sup_{T\in\mathcal F}\|T\|_{\mathcal B(X,Y)}<\infty.
\]
Set \(E_m=\{x: \sup_{T\in\mathcal F}\|Tx\|\le m\}\). Each \(E_m\) is closed; \(X=\bigcup_mE_m\). Baire gives \(B(x_0,r)\subset E_m\) for some \(m,r>0\). If \(\|h\|<r\), then \(\|Th\|\le\|T(x_0+h)\|+\|Tx_0\|\le2m\); scaling yields \(\|T\|\le2m/r\) for all \(T\in\mathcal F\).

##### Why completeness is necessary

Let \(X=c_{00}\) (finitely supported sequences) with the supremum norm, and \(T_n:X\to\mathbb R\) by \(T_nx=n x_n\). Every \(x\in X\) has only finitely many nonzero coordinates, so \(\sup_n|T_nx|<\infty\). But \(\|T_n\|=n\to\infty\). The normed space \(c_{00}\) is not complete. Its completion is \(c_0\); e.g. \(x_n=1/\sqrt n\) defines a point in \(c_0\) where the readings \(T_nx=\sqrt n\) diverge.

##### Uniformly bounded convergence on a dense subspace

Suppose \(T_n\in\mathcal B(X,Y)\), \(\sup_n\|T_n\|\le M\), \(D\subset X\) dense, and \((T_nd)_n\) converges in Y for every \(d\in D\). If Y is Banach, then \(T_nx\) converges for every \(x\in X\): for \(d\approx x\),
\[
\|T_nx-T_kx\|\le 2M\|x-d\|+\|T_nd-T_kd\|.
\]
The limit is bounded and linear with norm at most M. This is *strong* convergence, not necessarily operator-norm convergence.

##### Weakly convergent sequences are bounded

For a normed X, each \(x\in X\) defines \(Jx\in X^{**}\) by \(Jx(f)=f(x)\). Hahn–Banach yields \(\|Jx\|=\|x\|\). If \(x_n\rightharpoonup x\), the family \(\{Jx_n\}\subset\mathcal B(X^*,\mathbb K)\) is pointwise bounded. Since \(X^*\) is Banach, uniform boundedness implies \(\sup_n\|x_n\|<\infty\).

##### Exercises with answers

1. **Difference quotients:** For \(T_n f=n(f(1/n)-f(0))\) on \(C[0,1]\), show \(\|T_n\|=2n\). **Answer:** \(\le2n\) by the triangle inequality, and a continuous piecewise-linear function with \(f(0)=-1\), \(f(1/n)=1\), \(\|f\|_\infty=1\) achieves \(2n\).
2. **A nonsmooth witness:** Set \(f(x)=\sqrt x\). Evaluate \(T_nf\). **Answer:** \(T_nf=\sqrt n\), which is unbounded; thus the family is not pointwise bounded on all of \(C[0,1]\).
3. **Pointwise versus uniform:** Let \(P_n\) truncate \(\ell^2\) sequences. What does Banach–Steinhaus guarantee, and what does it *not* guarantee? **Answer:** Uniform boundedness of \(\|P_n\|\); it does not give \(\|P_n-I\|\to0\).
4. **Weak boundedness:** A sequence in a normed space converges weakly. Show its norms are bounded. **Answer:** Apply uniform boundedness to its evaluations \(Jx_n\) on the Banach space \(X^*\), then use Hahn–Banach's isometry \(\|Jx_n\|=\|x_n\|\).

##### References

- MIT OpenCourseWare, *18.102 Introduction to Functional Analysis* (2021), Lecture 3 on quotient spaces, Baire and Banach–Steinhaus; Lecture 4 on open mapping and closed graph: https://ocw.mit.edu/courses/18-102-introduction-to-functional-analysis-spring-2021/pages/lecture-notes-and-readings/.
- Terence Tao, *245B, Notes 9: The Baire category theorem and its Banach space consequences*: https://terrytao.wordpress.com/2009/02/01/245b-notes-9-the-baire-category-theorem-and-its-banach-space-consequences/.
- Terence Tao, *245B, Notes 11: The strong and weak topologies*: https://terrytao.wordpress.com/2009/02/21/245b-notes-11-the-strong-and-weak-topologies/.

### Why a Bijective Operator Has a Bounded Inverse

**Track:** Analysis from First Principles. **Background:** Banach spaces, bounded linear maps, and the Baire category theorem. **Central question:** When does solving an equation depend continuously on the data?

#### Mathematical companion (not spoken)

Let \(X,Y\) be Banach spaces, \(T\in\mathcal B(X,Y)\). Open mapping: if \(T\) is surjective, then \(T(U)\) is open for each open \(U\subset X\). Bounded inverse: if \(T\) is bijective, then \(T^{-1}\in\mathcal B(Y,X)\). Closed graph: for a *linear, everywhere-defined* \(T:X\to Y\), closedness of \(G(T)\subset X\times Y\) implies boundedness.

A proof mechanism for open mapping: \(Y=\bigcup_{n\ge1}T(nB_X)\), hence by Baire some \(\overline{T(B_X)}\) has interior after rescaling. Linear translation gives \(B_Y(0,\delta)\subset\overline{T(B_X)}\). Successively approximate a target by errors of size \(2^{-n}\) with preimages of norm \(O(2^{-n})\). Completeness of \(X\) makes the corrections converge, yielding \(B_Y(0,c\delta)\subset T(B_X)\) for a suitable \(c>0\).

Counterexample to dropping surjectivity: \(T:\ell^2\to\ell^2\), \((Tx)_n=x_n/n\). It is bounded, injective, and \(\|Te_n\|=1/n\to0\) while \(\|e_n\|=1\). The range is dense but not closed. The inverse exists on \(\operatorname{ran}T\), yet is unbounded there.

Counterexample to dropping completeness of the domain: \(D:\{f\in C^1([0,1]):f(0)=0\}\to C([0,1])\), \(Df=f'\), with \(\|f\|_\infty\) on the domain. The map is a linear bijection whose inverse is bounded, but \(D\) is unbounded, since \(f_n(x)=\sin(n\pi x)/(n\pi)\) has vanishing sup norm while \(\|Df_n\|_\infty=1\). The domain under \(\|\cdot\|_\infty\) is incomplete.

##### Exercises with answers

1. **Diagonal inverse.** For \(T e_n=n^{-1}e_n\), find \(\|T\|\). **Answer:** One. Its inverse on the range is unbounded.
2. **Closed graph.** If \(T\) is bounded and \(x_n\to x\), \(Tx_n\to y\), why is \(y=Tx\)? **Answer:** By continuity \(Tx_n\to Tx\), and limits are unique.
3. **Well posedness.** What does bijectivity alone fail to ensure in a noncomplete domain? **Answer:** Continuous dependence of solutions on inputs; bounded-inverse conclusions require complete spaces and a bounded forward map.

##### Reading and source notes

- [MIT OpenCourseWare, 18.102 Introduction to Functional Analysis, lecture notes](https://ocw.mit.edu/courses/18-102-introduction-to-functional-analysis-spring-2021/pages/lecture-notes-and-readings/)
- [Sheldon Axler, Measure, Integration and Real Analysis](https://measure.axler.net/)

### Radon–Nikodym and Riesz: When Measurements Have Densities

**Track:** Analysis from First Principles. **Background:** Lebesgue integration, finite measures, Hilbert spaces and bounded functionals. **Central question:** When can an abstract measurement be written as an integral?

#### Mathematical companion (not spoken)

**Radon–Nikodym.** If \(\mu\) is sigma-finite and \(\nu\) is a sigma-finite positive measure with \(\nu\ll\mu\), then there is a measurable \(h\ge0\), finite \(\mu\)-a.e. under these hypotheses, with \(\nu(E)=\int_Eh\,d\mu\). For a finite signed or complex measure absolutely continuous with respect to \(\mu\), \(h\in L^1(\mu)\) is unique a.e. Be careful that a sigma-finite \(\nu\) need not have a globally \(L^1\) density if \(\nu(X)=\infty\).

**Hilbert-space Riesz.** Fix \(\langle x,y\rangle\) linear in \(x\). For any bounded complex-linear \(\Lambda:H\to\mathbb C\) there exists unique \(g\in H\) with \(\Lambda(x)=\langle x,g\rangle\), \(\|\Lambda\|=\|g\|\).

**Riesz–Markov.** For compact Hausdorff \(X\), each positive linear functional \(L:C(X)\to\mathbb R\) is \(L(f)=\int_X f\,d\mu\) for a unique finite regular Borel measure \(\mu\). Point evaluation is represented by \(\delta_{x_0}\).

Example: for \(d\nu=2x\,dx\) on \([0,1]\), \(\nu([1/2,1])=\int_{1/2}^1 2x\,dx=3/4\).

##### Exercises with answers

1. **Point mass.** Why is \(\delta_{1/2}\not\ll dx\)? **Answer:** A singleton has Lebesgue measure zero but Dirac measure one.
2. **Hilbert representer.** Find the \(\ell^2\) representer of \(\Lambda(x)=2x_1-x_3\). **Answer:** \(g=(2,0,-1,0,\ldots)\) for real sequences.
3. **Compare the theorems.** What represents point evaluation on \(C([0,1])\)? **Answer:** A Dirac measure via Riesz–Markov, not an L-one density with respect to length.

##### Reading and source notes

- [John K. Hunter, Measure Theory notes](https://www.math.ucdavis.edu/~hunter/m206/intro_measure_notes.pdf)
- [Sheldon Axler, Measure, Integration and Real Analysis](https://measure.axler.net/)
- [MIT OpenCourseWare, 18.102 Introduction to Functional Analysis, lecture notes](https://ocw.mit.edu/courses/18-102-introduction-to-functional-analysis-spring-2021/pages/lecture-notes-and-readings/)
