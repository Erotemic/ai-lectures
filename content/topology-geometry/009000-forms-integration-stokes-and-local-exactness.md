# Forms, integration, Stokes, and local exactness

<!-- BEGIN SPOKEN LECTURE -->

# Forms, integration, Stokes, and local exactness

## Differential Forms: Calculus That Survives a Change of Coordinates

A curve on a sphere can be described using latitude and longitude, or by coordinates measured on a map projected onto a plane. Neither coordinate system is the sphere. It is only a way to describe a portion of the sphere. If calculus on the sphere is to be meaningful, the answer must not depend on which map we picked.

We already know one coordinate-independent object: a tangent vector. It represents a possible velocity through a point. Coordinates give that vector components, but the velocity itself is not a list of components attached forever to one chart. Differential forms provide a complementary language: they take tangent vectors as inputs, produce numbers, and behave correctly when we change charts.

### From differentials to covectors

At a point of a smooth manifold, a one-form is a linear functional on the tangent space. Feed it a tangent vector and it returns a scalar. For a smooth real-valued function f, its differential at a point is such a one-form: it sends a vector v to the directional derivative of f along v.

In ordinary plane coordinates, write f as a function of x and y. Its differential has an x-component involving the partial derivative of f with respect to x, and a y-component involving the partial derivative with respect to y. If the tangent vector moves with velocity v in the x direction and w in the y direction, the differential returns the partial x derivative times v plus the partial y derivative times w. This is the chain rule expressed as a pairing.

The symbols d x and d y are not tiny increments that we multiply like arbitrary numbers. They are basis covectors that extract the x and y components of a tangent vector. They change when coordinates change, in a way that preserves the value of the pairing.

A differential one-form on the plane can be written P d x plus Q d y, where P and Q are functions of position. Integrating it along a parametrized curve means evaluating the form on the curve's velocity and integrating the resulting scalar over the parameter. This produces an oriented line integral. Reverse the curve's direction and the integral changes sign.

### Why alternating forms appear

A two-form takes two tangent vectors and is linear in each input, but it also changes sign when the two inputs are exchanged. In particular, giving it the same vector twice produces zero. Such objects are called alternating bilinear forms.

On the plane, d x wedge d y is the basic two-form. Feed it two vectors and it returns the signed area of the parallelogram spanned by those vectors. If we reverse the order of the inputs, the signed area reverses. If the vectors are parallel, the area is zero.

The wedge product creates higher-degree forms from lower-degree ones. For one-forms alpha and beta, alpha wedge beta is a two-form measuring their alternating interaction. Swapping two one-forms changes the sign. More generally, swapping forms of degrees p and q introduces a sign determined by the product p times q. This is graded commutativity.

Why does this help integration? A one-form naturally integrates along oriented curves. A two-form naturally integrates over oriented surfaces. On an n-dimensional manifold, an n-form naturally integrates over oriented n-dimensional regions. A coordinate change adjusts the components and the oriented volume element together; the integral remains geometrically meaningful.

### The exterior derivative

We know how to differentiate a function and obtain a one-form. Can we differentiate one-forms and higher forms in a coherent way? The exterior derivative does exactly that. It raises degree by one: functions become one-forms, one-forms become two-forms, and so on.

For a one-form P d x plus Q d y on the plane, the exterior derivative is the difference between the x derivative of Q and the y derivative of P, multiplied by d x wedge d y. The expression looks like the scalar curl from vector calculus. This is no accident: the traditional gradient, curl, and divergence operators are different coordinate shadows of the exterior derivative when combined with other geometric identifications.

Take the one-form negative y d x plus x d y. The x derivative of the coefficient of d y is one, and the y derivative of the coefficient of d x is negative one. Their difference is two. Thus its exterior derivative is two times the area form d x wedge d y.

There is an algebraic rule behind this calculation. Differentiation obeys a graded product law: the derivative of alpha wedge beta is the derivative of alpha wedge beta plus a sign, depending on the degree of alpha, times alpha wedge the derivative of beta. The sign ensures consistency with alternating order.

A central identity is that applying the exterior derivative twice gives zero. For a function f, this follows from equality of mixed second partial derivatives when f is sufficiently smooth. For a general differential form, the cancellation of corresponding mixed partial derivatives gives the same result, and the graded product law extends it to all forms.

This identity says that every exact form, meaning one obtained as the exterior derivative of another form, is closed, meaning its exterior derivative is zero. The converse is not always true. That distinction is where topology enters the calculus.

### An obstruction on the punctured plane

Remove the origin from the plane. Consider the one-form whose coefficients are negative y over x squared plus y squared and x over that same denominator. It is smooth everywhere on the punctured plane. A calculation gives exterior derivative zero, so the form is closed.

But integrate the form once counterclockwise around the unit circle. Parametrize the circle by cosine and sine. The form evaluates to one on the unit-speed angular parametrization, and its integral is two pi. If the form were the differential of a globally defined smooth function, the fundamental theorem for line integrals would force its integral around every closed loop to be zero. Contradiction.

Therefore the form is closed but not exact on the punctured plane. There is no globally defined angle function whose differential equals this form everywhere. Locally we can choose an angle coordinate, but going once around the missing point changes the angle by a full turn.

This is an example of the first de Rham cohomology detecting a topological hole. We have not proved the general equivalence between de Rham cohomology and singular cohomology, but this example already exhibits the organizing idea: differentiate forms, observe that differentiating twice gives zero, and examine which closed forms fail to be derivatives of others.

### Why coordinates no longer dominate

Differential forms have an important compatibility with maps of manifolds. A smooth map can pull a form backward to its source. In coordinates this is substitution followed by the chain rule; geometrically it means feeding a form the pushed-forward tangent vectors. Pullback commutes with the exterior derivative. We can change the coordinates or pull the same form onto a parametrized surface without inventing a separate differentiation law every time.

Forms therefore unify line integrals, surface integrals, and parts of vector calculus. But their deeper value is that the formulas survive any valid smooth change of chart. They also expose the topological distinction between local antiderivatives and globally defined ones.

The same exterior derivative that turns a potential into a gradient-like object will connect boundary integration with interior integration. That is the general form of Stokes' theorem. The machinery may look abstract, but it is designed to keep a simple requirement honest: the calculus should describe geometry, not the coordinate grid used to draw it.

## Differential Forms: Circulation, Flux, and Curl

Imagine a small paddle wheel in a flowing stream. Whether it turns depends on how the water moves around it. Now imagine a closed curve in the stream and ask how strongly the current pushes along the curve as you travel around it. These are two views of the same circulation phenomenon, one local and one integrated. Differential forms make the relationship precise and reveal that several familiar vector-calculus theorems have the same underlying shape.

We will work first in the plane, with coordinates x and y and the usual counterclockwise orientation. Suppose the flow has horizontal component P and vertical component Q. The associated one-form is P d x plus Q d y. When a particle traces a parametrized path, we evaluate this form on its velocity. The result is P times the horizontal velocity plus Q times the vertical velocity: the rate at which the field works along the path.

### Computing a circulation integral

Take the field whose horizontal component is negative y and whose vertical component is x. Its arrows circulate around the origin. On the unit circle parametrized counterclockwise by cosine t and sine t, the velocity is negative sine t in the x direction and cosine t in the y direction. The field evaluated at that point is exactly the same vector. Their dot product is one. Integrating from zero to two pi gives circulation two pi.

We can also measure local circulation. Differentiate the one-form negative y d x plus x d y. The exterior derivative is two times d x wedge d y. Thus the exterior derivative says that every unit of oriented area carries local circulation density two. The unit disk has area pi, so integrating the two-form over the disk gives two pi. The boundary integral and the area integral agree.

This is Green's theorem in differential-form language. In conventional coordinates it says the counterclockwise line integral of P d x plus Q d y equals the double integral of the x derivative of Q minus the y derivative of P. The expression in the integrand is the scalar curl in two dimensions. The derivative of the one-form automatically produces it with the correct orientation.

### Why orientation changes the sign

Walking the same curve in the opposite direction changes every tangent velocity to its negative, so the line integral changes sign. Reversing orientation on the region changes its area form sign as well. Boundary and interior must be oriented compatibly for Green's theorem. The usual convention on a planar region is that a counterclockwise boundary walk keeps the region on your left.

The sign is not bookkeeping to be repaired after the calculation. An oriented integral measures something with a direction. If you want an unsigned total amount, that is a different operation. This becomes especially important when we move from curves to surfaces.

### Flux uses a different form

In the plane, circulation measures the component tangent to a boundary. Flux measures the component passing across it. For a vector field with components P and Q, the outward-flux one-form along a positively oriented boundary is P d y minus Q d x. You can see this on the right side of a rectangle. As you walk upward, d y is positive and the outward normal points right, so the contribution is positive P times height. On the top edge, walking left makes d x negative, and the outward normal points upward, so the contribution is positive Q times width.

Differentiate the flux form: it becomes the sum of the x derivative of P and the y derivative of Q, times d x wedge d y. That sum is the divergence. Integrating it over a region measures total outward flux. The same Stokes principle that gave circulation and curl now gives flux and divergence, simply because we chose the form appropriate to the measurement.

Consider the outward-pointing radial field P equals x, Q equals y on the unit disk. Its divergence is two, so total outward flux is two pi. On the unit circle, the field has unit normal component and the boundary has circumference two pi. Both calculations return two pi. This example is not merely a mnemonic: it tells us why an integral over a boundary can be replaced with an integral of a local source density.

### Moving up to three dimensions

In three dimensions, the differential-form degree is crucial. A one-form integrates along a curve, and its exterior derivative is a two-form that integrates over a surface. With a Euclidean metric and chosen orientation, the coefficients of that two-form correspond to the curl vector. The theorem says circulation along the boundary curve equals the flux of curl through the spanning oriented surface.

For a three-dimensional vector field with components P, Q and R, the outward-flux two-form is P d y wedge d z plus Q d z wedge d x plus R d x wedge d y. Its exterior derivative is divergence times d x wedge d y wedge d z. Integrating over a solid region gives the divergence theorem. There is no distinct exterior derivative invented for flux; the same operator d is used on forms of different degrees.

Why do conventional vector-calculus courses seem to use several different operators? Because the Euclidean metric and orientation allow us to identify vectors with covectors and with particular forms. The gradient comes from the derivative of a function; curl from the derivative of a one-form; divergence from the derivative of a two-form. When we change the dimension or metric, these identifications change, but the exterior derivative remains.

### The zero-after-zero principle

There is a structural reason that curl of gradient is zero, and divergence of curl is zero in their usual three-dimensional interpretation. Applying the exterior derivative twice gives zero. A potential function produces an exact one-form. Differentiating it again gives zero. A one-form produces a two-form; differentiating that again also gives zero. The familiar vector identities are just instances of the same algebraic rule.

But the reverse statements are not automatic. A curl-free field in a domain with a hole need not be the gradient of a globally defined potential. The circulating field proportional to negative y over radius squared and x over radius squared is curl-free away from the origin and still circulates around the missing point. Likewise, the global existence of a potential in higher dimensions depends on topology as well as local differential identities.

The lesson is that line and surface integrals are not unrelated recipes. Differential forms distinguish what type of oriented object we integrate over. The exterior derivative translates local change into a boundary integral. The metric may translate these forms into familiar vector fields, but the Stokes identity underneath them is the same.

## Partitions of Unity and Global Integration

A sphere cannot be covered by one ordinary smooth coordinate chart that behaves like a plane everywhere. Nevertheless, we can integrate a smooth area form over the entire sphere. We can define metrics and connections globally, even when we construct them one chart at a time. How can local formulas produce a single global mathematical object without requiring a global system of coordinates?

The device that makes this possible is a partition of unity. Its ingredients are smooth functions that act as carefully arranged weights. Each weight is supported in a local region where we can work in coordinates. The weights sum to one, so their local contributions combine without changing the quantity we mean to describe.

### A weight that vanishes smoothly

Begin on the real line. We want a smooth bump that is positive near zero and exactly zero outside a bounded interval. There is a difference between being zero and smoothly becoming zero. A triangular tent has corners; if we take derivatives, the corners cause trouble. A true smooth bump flattens out to all orders at its boundary.

One standard construction uses an exponential that decays faster than any power as we approach the endpoint of an interval. The formula matters less than the property it establishes: smooth functions need not be analytic. A nonzero smooth function can vanish identically outside a compact region. That gives us local weights we can extend by zero beyond the chart without introducing seams.

Imagine covering a circle by several overlapping arcs. On each arc choose a bump that becomes zero before reaching the edge of that arc. Arrange for the positive parts of these bumps to cover the whole circle. At each point add up their values, then divide each bump by that sum. The new weights still vanish outside their assigned arcs, but now add to exactly one at every point.

The sum in the denominator must be positive. That is why we arranged for at least one bump to be positive at every point. In a compact space we can often perform this with finitely many bumps. On a noncompact manifold we may need infinitely many. We then require a locally finite family: every point has a neighborhood meeting the supports of only finitely many weights. All the sums we use are locally finite smooth sums, not uncontrolled infinite series.

### What a partition actually promises

A smooth partition of unity subordinate to an open cover consists of nonnegative smooth functions, each supported inside an appropriate member of the cover, whose sum is one. The standard existence theorem assumes a smooth, Hausdorff, second-countable manifold, or more generally the appropriate paracompact conditions. That hypothesis is not decorative. Without enough topological control, a locally finite refinement need not exist.

These weights do not magically make incompatible local data agree. Suppose two coordinate patches both describe the same geometric one-form. On their overlap, the component expressions must transform correctly. Once we know they agree as forms, multiplying by partition weights and summing recovers that form. If the two local definitions genuinely conflict, their weighted average is a new object, not proof that they were the same object all along.

There are, however, geometric structures that can be assembled by averaging. In each chart, construct a positive-definite metric. A weighted sum of positive-definite metrics remains positive definite, provided at least one positive weight is present. Thus partitions of unity help show that every ordinary smooth manifold admits a Riemannian metric. This is one concrete reason the existence theorem is so powerful.

### How global integration is defined

Suppose M is an oriented smooth surface and omega is a smooth two-form with compact support. Choose oriented coordinate charts and a partition of unity subordinate to those charts. Multiply omega by each weight. Each weighted form can be integrated by ordinary calculus after translating it into the local coordinates. Then add those local integrals.

Because the weights sum to one, the result should represent the integral of omega over the whole surface. But why is it independent of the chosen cover? If we use another partition, we can refine both decompositions together. The double weights still sum to one, and ordinary change-of-variables in overlapping charts shows that the same geometric two-form receives the same oriented integral. Orientation is what makes the Jacobian signs match consistently across patches.

The compact-support assumption ensures that the contribution is finite and that we do not need a theory of improper integration at infinity. On a noncompact manifold, a non-compactly-supported form may also be integrable, but convergence requires additional work. A partition of unity does not by itself turn a divergent integral into a convergent one.

### A familiar area calculation in disguise

On a sphere of radius R, the usual latitude and longitude coordinates have an area element involving R squared times the cosine of latitude. Integrating longitude through a full turn and latitude from south to north gives four pi R squared. But longitude is undefined at the poles. How can this calculation be legitimate if there is no single smooth longitude chart on all of the sphere?

One answer is to exclude tiny polar caps, compute on the regular coordinate region, and show the cap contribution tends to zero. A second, more systematic answer is to use overlapping charts and a partition of unity. On each chart we integrate the appropriate weighted area form. The total agrees with the usual calculation. We are not pretending the coordinate singularity is a geometric singularity. We simply avoid giving one chart more responsibility than it can bear.

The same idea works for manifolds whose coordinate maps are far less explicit than a sphere's. Local integration is a definition, not just a convenient computational trick, because the partition-of-unity construction specifies how all local answers are combined.

### Boundaries and orientations

If a manifold has a boundary, charts near the boundary look like pieces of a half-space. The boundary inherits an orientation from the orientation of the interior, using the outward-normal-first convention. A partition of unity can be chosen compatible with such charts. Then the integral of a derivative over the manifold can be compared with the integral of the original form over its boundary.

That comparison will give the general Stokes theorem. The partitions ensure that local versions of the fundamental theorem of calculus can be summed into a global statement. Interior chart contributions cancel or vanish; boundary chart contributions survive, with signs fixed by orientation.

There is one further distinction worth retaining. On a nonorientable manifold, a globally consistent top-degree differential form cannot serve as a positive volume measure in the usual way. To integrate an unsigned density, one uses densities rather than oriented top-forms. A partition of unity still performs the local-to-global assembly, but it does not remove the need to choose the correct kind of object to integrate.

A partition of unity is therefore not a claim that a manifold secretly has one coordinate system. It is a way to respect the absence of one. We work in trustworthy local charts, weight the results smoothly, and combine them into objects and integrals whose definitions do not depend on the charts. This is a central bridge between local calculus and global geometry.

## Generalized Stokes' Theorem: The Interior Speaks Through Its Boundary

The fundamental theorem of calculus relates a derivative integrated over an interval to the values of a function at the two endpoints. In the plane, Green's theorem relates a derivative-like quantity spread across a region to a line integral around its boundary. In three-dimensional space, the divergence theorem relates sources inside a volume to flux through its enclosing surface.

These are often taught as separate results with separate formulas. Differential forms show that they are versions of one assertion: the integral of the exterior derivative of a form over an oriented region equals the integral of the original form over its oriented boundary.

Before this assertion can be precise, we must decide what orientation means, what boundary means, and which degree of form we are integrating.

### The role of orientation

An orientation is a coherent choice of what counts as positive ordering of tangent directions. In the plane, it decides whether the pair of directions right then up is positive or negative. On a curve, it decides which way we traverse. On a surface, it chooses a consistent normal direction whenever such a global choice is possible.

If we reverse the orientation of an oriented manifold, the integral of a top-degree form changes sign. This is not a nuisance to be removed; it carries directional information. A line integral around a circle in the clockwise direction is the negative of the same integral counterclockwise.

The orientation on a boundary is not chosen independently. There is a convention called outward normal first. At a point on the boundary, put an outward-pointing normal vector first, then an oriented basis of tangent directions to the boundary. Together they should give a positive orientation of the ambient manifold.

In the standard oriented plane, that convention makes the boundary of a disk travel counterclockwise. On the interval from a to b, the right endpoint contributes positively and the left endpoint negatively. These choices are what make the signs in the theorem work.

### State the general theorem

Let M be an oriented smooth n-dimensional manifold with boundary, and let omega be a smooth differential form of degree n minus one. If M is compact, we can integrate omega over its boundary and the exterior derivative of omega over M. Generalized Stokes says those integrals are equal. On a noncompact manifold, a standard version requires omega to have compact support so that the integrals are well defined.

The smooth manifold and compact-support assumptions are not decorative. They rule out ways of losing contributions at infinity and give meaning to integration and the boundary orientation. The theorem also requires the form to have precisely the correct degree: a one-form integrates over a curve, while its two-form derivative integrates over a surface.

### Return to the interval

Take M to be the closed interval from a to b. Here n equals one, so the form omega has degree zero: it is an ordinary smooth function f. The exterior derivative is f prime times d x. Integrating it from a to b gives f of b minus f of a. The boundary consists of two oriented points. Its integral of f is f at b with a plus sign and f at a with a minus sign. The generalized formula is exactly the fundamental theorem of calculus.

Nothing mysterious has been added. The familiar theorem is already a statement that the interior derivative controls the contribution from the boundary.

### A disk and its circular boundary

Consider the unit disk in the plane, with its usual orientation. Let omega be negative y d x plus x d y. Its exterior derivative is two times d x wedge d y. The integral of that derivative over the unit disk is twice the area of the disk, so it equals two pi.

Now look at the boundary circle. Parametrize it counterclockwise by x equals cosine t and y equals sine t, with t moving from zero to two pi. Along that curve, d x contributes negative sine t times d t, and d y contributes cosine t times d t. Substitute these into omega. The result is sine squared t plus cosine squared t, all multiplied by d t. That is simply d t. Integrate once around, and the result is two pi.

The two calculations agree. One integrates rotation-like information throughout the disk; the other measures its circulation along the circle. This is Green's theorem for this particular one-form, and the same structure works for general smooth planar fields and sufficiently regular regions.

### Recover familiar vector calculus

On an oriented surface in three-dimensional space, a one-form corresponding to a vector field has an exterior derivative corresponding to the normal component of curl. Stokes' theorem says the circulation of the field around the boundary equals the flux of curl through the surface.

For a three-dimensional region, associate a two-form to the flux of a vector field across an oriented surface. Its exterior derivative corresponds to divergence times the oriented volume form. Generalized Stokes becomes the divergence theorem: total outward flux equals total divergence in the interior.

To make these identifications, we use the Euclidean metric and orientation to translate vector fields into differential forms. The exterior derivative itself does not require a metric; curl and divergence in their usual vector forms involve those additional identifications. This is one reason differential forms are useful on manifolds where no single flat coordinate grid covers the entire space.

### Why interior contributions cancel

Imagine cutting a surface into many small oriented patches. Apply a local boundary formula to every patch. Along an edge shared by two adjacent patches, the induced orientations are opposite. The integral along that edge appears twice with opposite signs and cancels. Only edges on the external boundary survive.

This cancellation is the geometric heart of Stokes' theorem. A rigorous proof uses coordinate charts and partitions of unity to reduce the statement to the fundamental theorem of calculus on Euclidean half-spaces. In that local calculation, contributions from interior directions cancel and only the true boundary remains. The partition of unity then reassembles the result without double-counting overlapping charts.

This reasoning also suggests why the boundary of a boundary vanishes. Algebraically, the exterior derivative squared is zero. Geometrically, oriented boundaries of adjacent boundary pieces cancel. These two statements are dual expressions of the same underlying structure, one in differentiation and the other in chains.

### A limitation with topological consequences

Stokes does not say that every closed form is exact. On the punctured plane, there is a closed one-form whose integral around a circle enclosing the missing point is nonzero. The circle is not the boundary of a disk lying entirely inside the punctured plane. We cannot invoke Stokes over a disk that includes a point absent from our manifold. The missing point is exactly the obstruction.

This is where calculus meets topology. A local derivative equation does not automatically supply a global potential, and whether a cycle bounds a region can depend on the topology of the space. Generalized Stokes connects the two sides without pretending that topology disappears.

The theorem teaches a principle broader than any one integral formula. The interior is not independent of its boundary: differentiation measures what must appear along that boundary, and orientation tells us how the contributions combine. Once the degrees and signs are handled coherently, several classical theorems become one geometric statement.

## Deriving Stokes' Theorem from Elementary Calculus

The fundamental theorem of calculus says that the integral of a derivative along an interval is the difference between the function's values at its endpoints. Green's theorem says that the circulation of a vector field around a planar region is the integral of its curl across the region. The divergence theorem says that the flux through the boundary of a solid is the integral of divergence inside it. These do not look like the same formula at first glance. But generalized Stokes' theorem puts all of them into one sentence: integrate the exterior derivative over a region, and you obtain the integral of the original form over its oriented boundary.

We will not simply quote that sentence. We will see how the elementary one-dimensional result supplies the entire mechanism, and where orientation and local coordinates enter.

### Begin with an interval

Let f be a smooth real function on the interval from a to b. Its differential is f prime times d x. Integrate this one-form from a to b. The fundamental theorem says the answer is f of b minus f of a. The boundary of an oriented interval consists of the right endpoint with positive sign and the left endpoint with negative sign. If we regard f as a zero-form and integrate it over that signed boundary, we obtain the same answer.

This is already Stokes' theorem in dimension one. The mysterious boundary orientation is simply a precise way to record the subtraction that was present in elementary calculus all along.

### A rectangle and Green's theorem

Take a rectangle with x between a and b and y between c and d. Let alpha be the one-form P d x plus Q d y. Walk around the rectangle counterclockwise. Along the bottom edge we integrate P from left to right. Along the top we integrate P from right to left. Subtract the two, and use the fundamental theorem in the y direction: their combined contribution is the negative of the double integral of the y derivative of P.

Now inspect the right and left edges. The right edge travels upward and contributes Q integrated from c to d. The left travels downward and contributes the negative of the corresponding integral. Their difference, by the fundamental theorem in the x direction, is the double integral of the x derivative of Q.

Add all four edges. We obtain the double integral of the x derivative of Q minus the y derivative of P. But that expression is exactly the coefficient of d alpha, since d of P d x plus Q d y is that coefficient times d x wedge d y.

We have proved Green's theorem for a rectangle by using the fundamental theorem twice and keeping the orientation of each edge. For regions built from rectangles, the shared interior edges are traversed in opposite directions and cancel. For more general smooth regions, approximation, parametrization, or local chart arguments carry the result further. Notice the pattern: the contributions inside adjacent pieces cancel; only the outer boundary remains.

### What changes in higher dimensions

On a three-dimensional box, a two-form has three kinds of coefficient terms, corresponding to the three coordinate-plane directions. Differentiate it. Each coefficient contributes a partial derivative in the one direction not already present. Integrate over the box. By the one-dimensional fundamental theorem, that contribution becomes the difference between the values on the two faces perpendicular to that direction.

The orientation of the two opposite faces is opposite. Again the signs are not optional: one face has outward normal pointing toward increasing coordinate, the opposite face toward decreasing coordinate. After gathering all faces we have the integral of the original two-form over the oriented boundary. In familiar vector language this is the divergence theorem.

The same proof works in n dimensions. A form of degree n minus one has one coefficient term for each omitted coordinate. Its exterior derivative differentiates that coefficient in the omitted coordinate, with the sign determined by where that coordinate would appear in the ordered wedge product. Integrating over a rectangular box reduces each term to boundary faces. The algebra of wedge products remembers the signs that in vector calculus might be inserted by a separate normal-vector convention.

### Why the statement is about manifolds

A manifold is locally modeled on Euclidean space or a Euclidean half-space if it has a boundary. In an interior chart, a compactly supported form contributes no boundary integral; applying the Euclidean theorem to its compact support gives zero on both sides. In a boundary chart, its support can meet the flat boundary of the half-space. Applying the one-dimensional fundamental theorem perpendicular to that flat boundary produces the boundary contribution, with the induced orientation.

Now choose a smooth partition of unity subordinate to such charts. Multiply the form by each weight and apply the local theorem to each piece. Because the weights add to one, the sum of their exterior derivatives is the exterior derivative of the original form: the extra terms produced by differentiating the weights cancel since the derivative of their sum is zero. The boundary pieces add to the integral over the global boundary. This is how local calculus becomes global Stokes, not by pretending we found a chart covering the whole manifold.

One should state the scope. The usual clean theorem concerns a compact oriented smooth manifold with smooth boundary and a smooth form of degree one less than the dimension. A version for noncompact manifolds holds for compactly supported forms under suitable hypotheses. Corners can be handled with compatible conventions, but they are an extension of the simplest formulation.

### The punctured disk and the missing boundary

Here is a calculation that reveals why boundary bookkeeping matters. On the punctured plane, take the one-form negative y d x plus x d y divided by x squared plus y squared. Its exterior derivative is zero away from the origin. Nevertheless the integral around a counterclockwise unit circle is two pi.

Does this contradict Stokes' theorem? No. The one-form is not smooth on the full unit disk because it is undefined at the origin. If we remove a smaller disk around the origin, the remaining annulus has two boundary components. The outer circle receives counterclockwise orientation; the inner circle receives clockwise orientation. The integral around the outer circle is two pi and around the inner circle is negative two pi. Their sum is zero, exactly equal to the integral of the zero exterior derivative over the annulus.

The missing boundary is a geometric way of seeing the obstruction to a global potential. This example also prepares us for cohomology: closed forms integrate to zero over boundaries of regions on which they are defined, but they may have nonzero integrals over cycles that do not bound such a region in the domain.

### What Stokes tells us, and what it does not

Stokes' theorem does not assert that every curve bounds a surface within the domain. It says that when a suitable oriented region and boundary are present, and the form is smooth where required, the two integrals agree. Nor does it eliminate the need to specify orientation. Reverse orientation of the region and both sides change sign. Changing only the boundary orientation breaks the equality.

From the interval to the rectangle, from the box to the smooth manifold, the proof is the same idea repeated under better organization. Integration of a derivative is a boundary calculation. The exterior derivative is engineered to make the cancellations work in every dimension, while partitions of unity make the local result independent of chart choices. Stokes is not a collection of lucky analogies. It is the fundamental theorem of calculus written in a language that survives geometry.

## Poincare Lemma and Homotopy Invariance

A differential form can be closed without being exact. We have seen this on the punctured plane: the form measuring angle around the missing origin has zero exterior derivative, but its integral around a full loop is two pi. Yet if we zoom in to a small disk that avoids the origin, we can choose an angle function there, and the same form becomes its differential. The form is locally exact but globally not exact.

The Poincare lemma explains this local behavior in every degree. On a star-shaped open region in Euclidean space, every closed differential form of positive degree is exact. That statement is the analytic starting point for understanding why de Rham cohomology detects global topology rather than local failures of calculus.

### What star-shaped buys us

A region is star-shaped with respect to a chosen center if every straight segment connecting that center to a point in the region stays inside the region. An open ball is star-shaped, and so is any convex open set. A ring with a hole is not star-shaped with respect to any point, because some straight lines to the center would cross the missing region.

The geometry of a star-shaped region offers a simple deformation. Keep the center fixed, and move every point straight toward it. At time one we have the identity map; at time zero everything has collapsed to the center. This is a homotopy: a smoothly varying family of maps. Its existence gives us a method for constructing antiderivatives of forms.

### Recovering a potential by integrating along rays

First consider a closed one-form on a star-shaped plane region. Write it as P d x plus Q d y. Closed means the x derivative of Q equals the y derivative of P. Choose the star center as the origin for simplicity. Define a candidate potential at a point by integrating the one-form along the straight path from the origin to that point.

Why should this work? Differentiate the path integral with respect to the endpoint. The derivative consists of the local value of the form plus a correction measuring how the form changes along the ray. The equality of the mixed partial derivatives makes that correction collapse into the appropriate endpoint expression. The resulting differential of the potential is the original form.

For a familiar example, let the form be y d x plus x d y. The mixed-derivative condition holds: both relevant derivatives equal one. Integrating along the ray from zero to the point x,y gives x times y. Differentiate the function x y, and we indeed recover y d x plus x d y.

This local primitive is not unique. Adding a constant does not change its differential. On a connected region any two primitives of the same one-form differ by a constant. The star center and chosen integration paths give a construction, not a uniquely distinguished potential.

### The higher-degree problem

For a two-form, an antiderivative is a one-form; for a three-form, it is a two-form. Simply integrating one scalar along a path no longer captures all the alternating inputs. The general construction is a homotopy operator. It contracts the form with the radial direction and integrates that contraction as the point moves along its ray.

The crucial identity says that applying the exterior derivative after the homotopy operator, then adding the homotopy operator after the exterior derivative, equals the identity on positive-degree forms on a star-shaped region. More accurately, in every degree the difference between the identity map and pullback by the collapse to the center appears on the right. The collapse pulls positive-degree forms back to zero, so in those degrees the right side is simply the original form.

Now take a closed form omega. Its exterior derivative is zero. The identity becomes: omega equals the exterior derivative of the homotopy operator applied to omega. That is the antiderivative we wanted. This is the Poincare lemma, with an explicit construction behind the existence claim.

There is a special case in degree zero. A closed zero-form is a function whose differential is zero, hence is locally constant. On a connected star-shaped domain it is constant. It is not sensible to say that every constant function is the differential of a minus-one-form. The positive-degree qualification matters.

### From star-shaped regions to manifolds

A smooth manifold has coordinate neighborhoods diffeomorphic to open balls. Such neighborhoods allow the Poincare lemma to be transported through the chart. Therefore every closed smooth positive-degree form on a manifold is locally exact. Local exactness is the default. The interesting question is whether those local primitives can be reconciled to obtain a global primitive.

On the circle, the angular one-form has a local potential in every sufficiently small arc. But if we travel around the entire circle, a chosen angle increases by a full turn. No single-valued real function on the circle can serve as a global potential. The obstruction is a global mismatch among local choices, detected by integrating around the loop.

### Homotopy invariance

The radial collapse used in the proof suggests a larger principle. Suppose two smooth maps from M to N are smoothly homotopic. Pulling a closed form on N back along either map produces forms on M that differ by an exact form. Consequently, the two maps induce the same operation on de Rham cohomology. We say de Rham cohomology is homotopy invariant.

To see the mechanism, imagine the homotopy sweeping out a cylinder M times an interval. Pull the form to the cylinder, contract it with the direction of the interval, and integrate along that direction. This produces an operator whose exterior derivative compares the forms at the two ends of the homotopy. Once again the boundary of a deformation supplies the difference between endpoint data.

If two manifolds are homotopy equivalent, their de Rham cohomology groups are isomorphic. A disk is homotopy equivalent to a point, so its positive-degree de Rham cohomology vanishes. The punctured plane retracts onto a circle; its first cohomology is therefore the same as that of the circle, which is nonzero. These topological facts explain the two potential calculations above.

### What homotopy does not preserve

Homotopy invariance is a statement about cohomology, not a claim that every geometric property survives deformation. A circle and an annulus can have the same homotopy type while having different dimensions as manifolds. A Riemannian metric, curvature, area, and geodesic lengths require extra structure and are not determined by homotopy type.

Similarly, a global integral of a nonclosed form need not be invariant under deforming the integration cycle. The proof of invariance for closed forms uses the vanishing of the exterior derivative. The hypothesis is doing real work.

The Poincare lemma and homotopy invariance make a useful pair. The first says closed forms have local potentials on sufficiently simple regions. The second says the global obstruction to finding a potential is unchanged by suitable deformation of the underlying space. Local calculus gives us derivatives; global topology determines what those derivatives cannot resolve.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Differential Forms: Calculus That Survives a Change of Coordinates

**Track:** Topology and Geometry. **Background:** multivariable calculus, tangent spaces, and smooth manifolds. **Central question:** how do we describe integrands and differentiation without committing to a particular coordinate system?

#### Mathematical companion (not spoken)

Let \(M\) be a smooth manifold. A differential \(p\)-form is a smooth section of \(\Lambda^pT^*M\). In local coordinates \(x^1,\ldots,x^n\), a one-form is \(\alpha=\sum_i a_i\,dx^i\), and a \(p\)-form is a sum of \(a_{i_1\cdots i_p}\,dx^{i_1}\wedge\cdots\wedge dx^{i_p}\) over increasing multi-indices.

For tangent vectors \(u=(u_1,u_2)\), \(v=(v_1,v_2)\),
\[
(dx\wedge dy)(u,v)=u_1v_2-u_2v_1.
\]
Exterior differentiation is characterized by
\[
\begin{gathered}
df=\sum_i\frac{\partial f}{\partial x^i}\,dx^i,\qquad
 d(\alpha\wedge\beta)=d\alpha\wedge\beta+(-1)^p\alpha\wedge d\beta\quad (\deg\alpha=p),\\
d^2=0,\qquad F^*(d\omega)=d(F^*\omega).
\end{gathered}
\]
For \(\alpha=P\,dx+Q\,dy\), \(d\alpha=(\partial_xQ-\partial_yP)\,dx\wedge dy\). Taking \(\alpha=-y\,dx+x\,dy\) yields \(d\alpha=2\,dx\wedge dy\).

**Closed not exact.** On \(U=\mathbb R^2\setminus\{0\}\),
\[
\eta=\frac{-y\,dx+x\,dy}{x^2+y^2},\qquad d\eta=0,
\qquad \int_{S^1}\eta=2\pi.
\]
Therefore \(\eta\ne df\) for any global smooth \(f:U\to\mathbb R\), because exact one-forms have zero integral around a closed curve.

##### Exercises with answers

1. Compute \(d(x^2\,dy)\). **Answer:** \(2x\,dx\wedge dy\).
2. Evaluate \((dx\wedge dy)((1,2),(3,4))\). **Answer:** \(4-6=-2\).
3. Must a closed one-form on any manifold be exact? **No:** the punctured plane example refutes this.
4. Is \(dx\wedge dx\) nonzero? **No:** alternation implies \(dx\wedge dx=0\).

##### Reading and source notes

- Denis Auroux, MIT OCW [Geometry of Manifolds, Differential Forms](https://ocw.mit.edu/courses/18-966-geometry-of-manifolds-spring-2007/pages/lecture-notes/), exterior algebra and exterior derivative.

### Differential Forms: Circulation, Flux, and Curl

**Track:** Topology and Geometry. **Background:** multivariable calculus, oriented curves and surfaces, elementary differential forms. **Question:** how are line integrals, flux integrals, curl and divergence related?

#### Mathematical companion (not spoken)

On a region \(D\subset\mathbb R^2\), for \(\alpha=P\,dx+Q\,dy\),
\[d\alpha=(\partial_x Q-\partial_y P)\,dx\wedge dy,\qquad \int_{\partial D}\alpha=\int_Dd\alpha.\]
For the outward-flux one-form \(\beta=P\,dy-Q\,dx\),
\[d\beta=(\partial_xP+\partial_yQ)\,dx\wedge dy,\qquad \int_{\partial D}\beta=\int_D\operatorname{div}(P,Q)\,dx\,dy.\]
In \(\mathbb R^3\), the flux form of \(V=(P,Q,R)\) is \(\iota_V(dx\wedge dy\wedge dz)=P\,dy\wedge dz+Q\,dz\wedge dx+R\,dx\wedge dy\). Then \(d(\iota_V\mathrm{vol})=(\operatorname{div}V)\mathrm{vol}\).

##### Worked examples and checks

1. For \(V=(-y,x)\), \(\oint_{\partial D} V\cdot d\mathbf r=\int_D2\,dA=2\pi\) for the unit disk.
2. For \(V=(x,y)\), outward flux across the unit circle is \(\int_D2\,dA=2\pi\).
3. Does reversing the orientation of the boundary keep a circulation integral fixed? **No:** it negates the integral.
4. Does curl-free imply a global gradient on the punctured plane? **No:** nontrivial periods obstruct it.

##### Reading and sources

- Denis Auroux and Kartik Venkatram, MIT OCW [Geometry of Manifolds](https://ocw.mit.edu/courses/18-966-geometry-of-manifolds-spring-2007/pages/lecture-notes/), differential forms and integration.
- Dominic Joyce, [Stokes Theorem: Orientations and Integration](https://people.maths.ox.ac.uk/~joyce/Nairobi2019/IDG5%2B6handout.pdf).
- Overview: [Green's theorem](https://en.wikipedia.org/wiki/Green%27s_theorem), [Divergence theorem](https://en.wikipedia.org/wiki/Divergence_theorem), [Stokes' theorem](https://en.wikipedia.org/wiki/Stokes%27_theorem).

### Partitions of Unity and Global Integration

**Track:** Topology and Geometry. **Background:** charts, smooth functions, differential forms. **Question:** how can local computations be assembled into constructions on an entire manifold?

#### Mathematical companion (not spoken)

For a locally finite open cover \(\{U_i\}\) of a paracompact smooth manifold, a subordinate smooth partition is \(\{\rho_i\}\) with
\[0\le\rho_i\le1,\qquad \operatorname{supp}\rho_i\subseteq U_i,\qquad \sum_i\rho_i=1,\]
where the support inclusion is achieved relative to a suitable locally finite refinement when necessary.

If \(\omega\in\Omega_c^n(M)\) on oriented \(M^n\),
\[\int_M\omega=\sum_i\int_{U_i}\rho_i\omega,\]
with each summand computed via an orientation-preserving chart and ordinary integration of its coefficient. If \(\{\sigma_j\}\) is another partition, insert \(1=\sum_j\sigma_j\) into each term to compare the definitions. For local positive-definite metrics \(g_i\), \(g=\sum_i\rho_i g_i\) is positive definite where the cover is locally finite.

##### Check your understanding

1. Why must the covering family be locally finite? **Answer:** to ensure a point has only finitely many nonzero contributions nearby, so smooth sums are well defined.
2. Does a partition of unity repair contradictory local tensors on overlaps? **No:** it can average to create another tensor, but it does not make incompatible definitions identical.
3. What replaces an oriented volume form if the goal is unsigned integration on a nonorientable manifold? **Answer:** a density.

##### Reading and sources

- MIT OCW, [Geometry of Manifolds](https://ocw.mit.edu/courses/18-965-geometry-of-manifolds-fall-2004/pages/lecture-notes/), lecture on connections and partitions of unity.
- Overview: [Partition of unity](https://en.wikipedia.org/wiki/Partition_of_unity), [Integration on manifolds](https://en.wikipedia.org/wiki/Integration_on_manifolds).

### Generalized Stokes' Theorem: The Interior Speaks Through Its Boundary

**Track:** Topology and Geometry. **Background:** oriented smooth manifolds, differential forms, exterior derivatives, and classical calculus. **Central question:** why do the fundamental theorem of calculus, Green's theorem, and the classical Stokes and divergence theorems share one formula?

#### Mathematical companion (not spoken)

Let \(M\) be a compact, oriented smooth \(n\)-manifold with boundary, and \(\omega\in\Omega^{n-1}(M)\). The induced orientation on \(\partial M\) uses **outward normal first**. Generalized Stokes' theorem is
\[
\boxed{\int_M d\omega=\int_{\partial M}\iota^*\omega},\qquad \iota:\partial M\hookrightarrow M.
\]
For noncompact \(M\), the common formulation assumes \(\omega\) compactly supported. Corners require an appropriate manifolds-with-corners formulation; the piecewise-smooth disk boundary example is covered by the usual extensions.

**One dimension.** \(M=[a,b]\), \(\omega=f\), \(\partial[a,b]=\{b\}-\{a\}\): \(\int_a^b f'(x)\,dx=f(b)-f(a)\).

**Unit disk.** \(D=\{x^2+y^2\le1\}\), \(\omega=-y\,dx+x\,dy\), \(d\omega=2\,dx\wedge dy\),
\[
\int_Dd\omega=2\pi=\int_{\partial D}\omega,
\]
with \(x=\cos t,y=\sin t\), \(0\le t\le2\pi\), and the counterclockwise boundary orientation.

**Vector-calculus identifications in Euclidean \(\mathbb R^3\).** For \(F=(P,Q,R)\), set \(\alpha=Pdx+Qdy+Rdz\). Then \(d\alpha\) corresponds to \(\nabla\times F\) via the metric and volume form. Set \(\beta=P\,dy\wedge dz+Q\,dz\wedge dx+R\,dx\wedge dy\). Then \(d\beta=(\nabla\cdot F)\,dx\wedge dy\wedge dz\). These give classical curl and divergence theorems.

##### Exercises with answers

1. What is the induced boundary orientation of the standard interval? **Answer:** \(\{b\}-\{a\}\).
2. If the disk's orientation is reversed, what happens to both sides of Stokes? **Answer:** both integrals reverse sign.
3. Can the punctured-plane closed one-form with nonzero circular integral be exact? **No:** exact forms integrate to zero around every closed curve.
4. Why cannot a two-form be integrated over a curve in the ordinary differential-forms integration theory? **Answer:** integration of differential forms pairs a degree-\(k\) form with an oriented \(k\)-dimensional domain; the degrees must match.

##### Reading and source notes

- Dominic Joyce, Oxford University, [Stokes' Theorem: Orientations and Integration](https://people.maths.ox.ac.uk/~joyce/Nairobi2019/IDG5%2B6handout.pdf).
- MIT OCW [Geometry of Manifolds](https://ocw.mit.edu/courses/18-966-geometry-of-manifolds-spring-2007/pages/lecture-notes/), differential forms and generalized Stokes.

### Deriving Stokes' Theorem from Elementary Calculus

**Track:** Topology and Geometry. **Background:** line integrals, partial derivatives, oriented forms, partitions of unity. **Question:** how does the fundamental theorem of calculus become a theorem on manifolds?

#### Mathematical companion (not spoken)

For a compact oriented \(n\)-manifold \(M\) with smooth boundary and \(\omega\in\Omega^{n-1}(M)\),
\[\boxed{\int_Md\omega=\int_{\partial M}\omega}.\]
Boundary orientation is determined by the rule: an outward-pointing normal followed by a positively oriented basis of \(T\partial M\) gives a positive basis of \(TM\).

For \(R=[a,b]\times[c,d]\), \(\alpha=P\,dx+Q\,dy\), Green's theorem is
\[\oint_{\partial R}\alpha=\int_c^d\int_a^b(\partial_xQ-\partial_yP)\,dx\,dy.\]
For a partition \(\sum_i\rho_i=1\), \(\sum_i d(\rho_i\omega)=d\omega\), since \(\sum_i d\rho_i=d1=0\).

**Annulus calculation.** For \(\eta=(-y\,dx+x\,dy)/(x^2+y^2)\), \(d\eta=0\) on \(r_0\le r\le r_1\), and \(\int_{\partial A}\eta=2\pi-2\pi=0\).

##### Check your understanding

1. What is \(\partial[a,b]\) as an oriented zero-chain? **Answer:** \([b]-[a]\).
2. Why do the interior edges cancel when neighboring rectangles are combined? **Answer:** they inherit opposite orientations.
3. May Stokes be applied to the singular one-form \(\eta\) on the disk including the origin? **No:** it is not defined there.

##### Reading and sources

- Dominic Joyce, [Stokes Theorem: Orientations and Integration](https://people.maths.ox.ac.uk/~joyce/Nairobi2019/IDG5%2B6handout.pdf).
- MIT OCW, [Geometry of Manifolds](https://ocw.mit.edu/courses/18-965-geometry-of-manifolds-fall-2004/pages/lecture-notes/).
- Overview: [Generalized Stokes theorem](https://en.wikipedia.org/wiki/Generalized_Stokes_theorem).

### Poincare Lemma and Homotopy Invariance

**Track:** Topology and Geometry. **Background:** differential forms, exterior derivative, Stokes' theorem, homotopy. **Question:** why does closed imply exact locally, and what survives continuous deformation?

#### Mathematical companion (not spoken)

Let \(U\subset\mathbb R^n\) be star-shaped about the origin. For \(\omega\in\Omega^k(U)\), \(k\ge1\), define
\[(K\omega)_x(v_1,\ldots,v_{k-1})=\int_0^1t^{k-1}\omega_{tx}(x,v_1,\ldots,v_{k-1})\,dt.\]
Then \(dK+Kd=\mathrm{id}-c_0^*\), where \(c_0(x)=0\); \(c_0^*\omega=0\) for \(k>0\). Thus \(d\omega=0\) implies \(\omega=d(K\omega)\). In degree zero, \(df=0\) implies \(f\) is constant on a connected domain.

For a smooth homotopy \(H:M\times[0,1]\to N\) between \(f_0,f_1\), the homotopy formula is
\[f_1^*-f_0^*=dK_H+K_Hd\]
on forms (with \(K_H\) of degree \(-1\)). Hence \([f_1^*\omega]=[f_0^*\omega]\) when \(d\omega=0\).

##### Check your understanding

1. On \(\mathbb R^2\), find a primitive of \(y\,dx+x\,dy\). **Answer:** \(xy\).
2. Is a closed zero-form necessarily exact? **No:** the usual de Rham complex starts at degree zero, and closed zero-forms are locally constant.
3. Why is a small disk avoiding the origin different from the entire punctured plane? **Answer:** the disk contracts through points inside itself, while the punctured plane retains a noncontractible loop.

##### Reading and sources

- MIT OCW, [Geometry of Manifolds, lecture on Poincare Lemma and homotopy invariance](https://ocw.mit.edu/courses/18-965-geometry-of-manifolds-fall-2004/pages/lecture-notes/).
- Overview: [Poincare lemma](https://en.wikipedia.org/wiki/Poincar%C3%A9_lemma), [De Rham cohomology](https://en.wikipedia.org/wiki/De_Rham_cohomology).
