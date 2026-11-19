# Time stepping, verified enclosures, and validated dynamics

<!-- BEGIN SPOKEN LECTURE -->

# Time stepping, verified enclosures, and validated dynamics

## Euler and Runge–Kutta Methods: Accuracy Is Not Stability

A differential equation tells us the velocity of a system at each moment. A numerical solver turns that local information into a sequence of states, each separated by a chosen time step. The simplest method looks at the current derivative and moves along its direction for one step. It is called Euler's method.

Suppose y-prime equals f of time and y, with an initial value y at time zero. Choose a step size h. Euler's rule says: the next value equals the current value plus h times the derivative evaluated at the current time and value. Geometrically, we follow the tangent line from the current point rather than the unknown curved solution.

For a linear function with constant slope, this is exact. For a curved trajectory it introduces error. Understanding that error requires distinguishing what happens in one step from what accumulates over many steps.

### A test equation we can solve exactly

Take y-prime equals negative two times y, starting at y equals one. The exact solution decays exponentially: at time t it equals e raised to negative two t. Euler's method instead multiplies the current value by one minus two h at every step.

If h is one quarter and we take four steps to reach time one, the numerical values are one, one half, one quarter, one eighth, and one sixteenth. The final approximation is 0.0625. The true value is approximately 0.1353. We have underestimated it substantially.

Decrease h and the approximation improves. But simply taking a positive step size does not guarantee reasonable behavior. If h is larger than one, the factor one minus two h has magnitude greater than one. Successive Euler values grow in magnitude while changing sign, even though the true solution decays monotonically to zero. The numerical method can be unstable on a mathematically stable problem.

This simple example tells us that the behavior of the discretization is not identical to the behavior of the differential equation.

### Local error and global error

Imagine starting a numerical step from the exact value of the solution. Compare the output of the numerical step with the true solution at the next time. That difference is the one-step local error, also called the local truncation defect. It isolates the error of a single update without allowing earlier numerical mistakes to contaminate the experiment.

For Euler's method, Taylor's theorem gives the exact next value as the current value plus h times the derivative plus a term proportional to h squared, assuming suitable smoothness. Euler keeps the first two terms and discards the rest. Therefore its local error is of order h squared.

But to simulate a fixed interval of length T, we take roughly T divided by h steps. Earlier errors are propagated by later updates, and each step contributes another new defect. Under a Lipschitz condition and suitable regularity, those effects accumulate so that the global error at a fixed final time is of order h, not h squared.

There is a useful way to derive the bound. Let e be the difference between the numerical approximation and the true value at a time step. Lipschitz continuity of f says the difference between two evaluated derivatives is at most L times the difference in their states. Euler therefore amplifies the prior error by at most one plus h L, then adds the new local error of order h squared. Repeat this inequality over N steps. The geometric sum of the amplification factors remains bounded by an exponential in L T, while the accumulated local errors are proportional to h. This is a discrete version of Grönwall's inequality.

The constant can be large when the dynamics strongly amplify perturbations. Convergence order describes what happens as h shrinks with the final time fixed and assumptions satisfied; it does not promise a small error at a particular coarse step size.

### Improve the step by sampling more intelligently

Euler uses only the slope at the beginning of the interval. One improvement is the explicit midpoint method. First predict where the solution would be halfway through the interval using a half Euler step. Evaluate the derivative at that predicted midpoint. Then use that midpoint slope for the full step.

For a smooth differential equation, this scheme has local error of order h cubed and global error of order h squared. It is often substantially more accurate than Euler for the same step size, though each step needs an extra derivative evaluation.

The classical fourth-order Runge–Kutta method, often called RK four, takes four slopes: at the beginning, at two intermediate predicted states near the midpoint, and at a predicted endpoint. It combines those slopes with weights one, two, two, and one, divided by six. The weighting is chosen so that its Taylor expansion matches the exact solution through fourth order.

Under sufficient smoothness, RK four has local error of order h to the fifth power and global error of order h to the fourth power on a fixed interval. It uses more derivative evaluations per step, but can be far more accurate at a given step size.

This tradeoff suggests an important practical question: how many evaluations are needed to reach a desired accuracy, not simply how accurate one step is in isolation?

### Return to the decay equation and test stability

Write the linear test equation as y-prime equals lambda times y, where lambda can be a complex number. Its exact solution multiplies by e to the lambda h after one step. Euler instead multiplies by one plus lambda h. For a decaying exact solution, the real part of lambda is negative. The numerical values decay only if the magnitude of one plus lambda h is less than one.

For a real negative lambda, this means the step size must be small enough that lambda h lies strictly between negative two and zero. If lambda is negative one hundred, h must be smaller than 0.02 for Euler's iterates to decay. A simulation over a long interval using h equals 0.03 may produce alternating values whose magnitude grows, although the real solution decays extremely rapidly.

Classical RK four has its own stability multiplier, a fourth-degree polynomial in lambda h obtained by truncating the exponential series after the fourth power. On the negative real axis it remains stable over a larger interval than Euler, but that interval is still finite. Higher order does not make an explicit method stable for every possible step size.

This is one motivation for implicit methods. A backward Euler step evaluates the derivative at the new unknown state. Applied to the linear test equation it gives a multiplier equal to one divided by one minus lambda h. For real negative lambda, its magnitude is less than one for every positive h. More generally backward Euler is stable for the whole left half of the complex plane, a property called A-stability.

Implicit steps require solving equations. That additional cost can be justified when the dynamics include fast-decaying components that force explicit methods to take tiny steps for stability even though the behavior of interest evolves slowly. Such systems are called stiff.

### Accuracy, stability, and conditioning are different questions

An accurate method can still use an unstable step size. A stable step may still be too inaccurate to resolve the quantity we care about. And even if a numerical method is stable, the original differential equation may be sensitive to perturbations in its initial conditions or parameters.

For linear test problems we can analyze the stability multiplier exactly. For nonlinear problems we combine local error estimates, stability analysis, adaptive step-size control, and sometimes conservation laws or qualitative checks. If a physical pendulum is supposed to conserve energy in the absence of friction, long-time numerical energy drift is a warning about the integrator, not automatically evidence of real damping or energy input.

The central numerical lesson is that consistency, stability, and convergence play distinct roles. The solver must approximate the differential equation locally; errors must not be amplified uncontrollably; and the cumulative approximation must approach the true solution as the step is refined. Euler and Runge–Kutta make those distinctions visible with formulas simple enough to analyze by hand.

Time-stepping error describes the approximation we deliberately choose. To certify a computed bound, we also need control of rounding in the arithmetic used to evaluate it.

## Interval Arithmetic: From Plausible Answers to Verified Enclosures

A numerical program returns a number. How do we know the true answer is near it? Sometimes we compare several step sizes and observe convergence. Sometimes a solver prints a residual. Those are useful diagnostics, but they do not automatically prove an upper bound on the error. Interval arithmetic takes a different approach: compute a range that is guaranteed to contain the exact result, provided the mathematical input and each interval operation are represented correctly.

The idea sounds simple. Instead of carrying one approximate number, carry a lower and upper bound. But to make those bounds rigorous on a finite machine, every arithmetic operation must be implemented with the right rounding direction. The width of the interval must account for all uncertainties being represented, not just the ones convenient to model.

### Intervals as sets

An interval from a to b means the set of all real numbers between a and b, including the endpoints. If X and Y are intervals, their exact interval sum is the set of all x plus y with x in X and y in Y. Its endpoints are the sums of the respective lower and upper endpoints. Multiplication is a little more involved: inspect all four products of endpoint choices and take the smallest and largest.

In exact real arithmetic, these set operations enclose every possible result. On a floating-point machine, though, the exact mathematical endpoint may not have a representable binary value. If we round the lower endpoint toward the nearest representable number, we might round upward and accidentally exclude the true result. A rigorous interval addition instead rounds the lower endpoint down and the upper endpoint up. The same outward-rounding principle applies to multiplication, division, and transcendental functions using certified enclosures.

Without this distinction, an interval-looking data structure is not automatically validated arithmetic. A pair of ordinary floating-point numbers is just a pair until the operations maintain the enclosure invariant.

### Why input conversion matters

Consider the decimal number one tenth. Its exact rational value cannot be represented exactly by a finite binary floating-point fraction. If a program converts that decimal into a nearest floating-point value and then wraps the result in an interval with equal endpoints, the interval contains the rounded binary number, not necessarily the mathematical decimal one tenth.

To enclose the original decimal exactly, the conversion must produce lower and upper representable neighbors around the rational value, or retain the rational value symbolically. Similar care is needed for measured input data. If a length is known only to within a millimeter, outward floating-point rounding alone does not capture that physical uncertainty; the starting interval must include the measurement range too.

Validated arithmetic can certify a statement about the model it was given. It cannot certify that an uncertain model describes reality more accurately than its assumptions permit.

### The dependency problem

A guaranteed enclosure can still be frustratingly wide. Take X to be the interval from zero to one. The mathematical function f of x equals x minus x is identically zero. Its exact range is just zero. But evaluate the expression using independent interval occurrences of X: X minus X gives the interval from negative one to one.

The interval operation has done nothing incorrect. It allowed the first x and the second x to vary independently, even though in the mathematical expression they are the same variable. That lost relationship is called the dependency problem.

It gets worse in long expressions. Repeated uses of a variable can inflate a natural interval evaluation far beyond the true range. Algebraic simplification, centered forms, Taylor models, or subdivision can restore useful tightness. This is a reminder that rigorous and sharp are different properties. A huge enclosing interval may be correct but practically uninformative.

### An interval Newton step

Consider the equation x squared equals two. We know one positive root lies between one and two. Ordinary Newton iteration takes an approximate midpoint, evaluates a derivative there, and predicts a better point. Interval Newton replaces the point derivative with an interval enclosing derivatives throughout the current candidate range.

Start with the interval from one to two and choose its midpoint, one and a half. The function value at the midpoint is one quarter. Over the full interval, the derivative two x ranges from two to four. Dividing one quarter by that derivative interval gives values from one sixteenth to one eighth. Subtract from one and a half, and we obtain the interval from one and three eighths to one and seven sixteenths.

In decimals, that is from 1.375 to 1.4375. It contains the positive square root of two. More importantly, the interval Newton theorem gives a route to certify both existence and uniqueness when the computed Newton image is contained strictly in the interior of the original interval and the required differentiability and nonzero-derivative conditions hold. Here those conditions are met. The enclosure can then be refined with further outward-rounded steps.

The calculation has not merely generated more digits. It has constructed a statement about all possible roots in the initial interval. In higher dimensions the analogous methods involve interval Jacobians, fixed-point or contraction arguments, and additional care with matrix inverses and conditioning.

### What constitutes a certificate

A certified numerical result should say exactly what is enclosed. It might assert that a polynomial has exactly one real root in a stated interval. It might assert that a computed integral differs from an exact integral by at most a certain amount under a specific regularity assumption. It might bound the solution of a linear system when coefficients and right-hand sides belong to known intervals.

Different problems require different proof ingredients. Outward-rounded evaluation alone may bound the range of a function on a box, but it does not automatically prove a root exists there. A zero appearing inside f of X says only that zero has not been excluded by the range bound. Existence generally requires a sign argument, an interval Newton inclusion, topological degree, or another theorem. Similarly, a small residual does not automatically imply a small solution error unless the inverse sensitivity is controlled.

We should also distinguish an interval method that encloses the exact answer to the stated finite-dimensional equations from a validated solution of a continuous differential equation. The latter may require explicit discretization-error estimates in addition to floating-point control. Certifying the algebraic solve is only one part of certifying a numerical model of a PDE.

### Reproducibility and libraries

The details of machine arithmetic matter. IEEE floating-point environments support specified rounding behavior, but how a language or compiler exposes and preserves directed rounding must be checked. Some interval libraries use hardware rounding modes; others implement conservative endpoint operations through software. Transcendental bounds, exceptional values, overflow, and interval division through zero all require defined treatment.

The goal is not to mistrust every decimal approximation. Ordinary floating-point methods are often extremely effective, and an error estimate may be more useful than a heavy certificate when decisions tolerate uncertainty. The goal is to know which claim we are making. If we say the exact answer lies in a particular interval, then every stage must preserve that inclusion. The strength of interval arithmetic is that it makes the burden of proof explicit: an enclosure is a theorem the computation has to maintain, not a visual impression of numerical accuracy.

## Verified nonlinear systems, trajectories, bifurcations, and periods

### Verified Nonlinear Systems: Interval Newton and Krawczyk Operators

Suppose a nonlinear solver returns a vector and reports that the residual is extremely small. That is useful evidence, but it is not necessarily a proof that a nearby root exists. The Jacobian might be nearly singular. Rounding might have hidden an important error. There might be multiple roots in the neighborhood, or no exact root at all.

Validated numerical analysis asks a stronger question. Can we produce a box, with rigorously represented endpoints, and prove that the equation has a solution inside it? Better still, can we prove that the solution is unique in that box?

Interval Newton and Krawczyk methods provide answers when a suitable local enclosure and derivative information are available. They combine ordinary approximate computation with interval bounds and a fixed-point theorem.

#### Return to Newton's idea

For a scalar equation f of x equals zero, Newton's method moves from a current guess by subtracting the function value divided by the derivative. For a system of equations, we solve a linear system involving the Jacobian matrix.

In an unverified implementation, both the function and the Jacobian are evaluated at approximate points. If those evaluations are inaccurate, the iteration can move in the wrong direction. Even if the iteration converges numerically, it might have converged to an answer without a rigorous error bound.

An interval method changes the goal. Instead of guessing where the next point is, it computes an enclosure that contains what the exact mathematics permits. A verified method uses directed rounding, so computed bounds are guaranteed to enclose the corresponding exact operations.

#### Constructing the Krawczyk operator

Begin with a box X, a point m inside it, and an approximate inverse C of the Jacobian at m. We form a map T that takes x to x minus C times f of x. A zero of f is a fixed point of T, provided C is nonsingular. The derivative of T is the identity minus C times the Jacobian.

Now bound that derivative over every point of X using interval arithmetic. The mean-value theorem tells us that every value T of x lies in a particular interval expression built from m, f of m, C, and the interval Jacobian. This enclosure is the Krawczyk operator.

If the resulting enclosure fits strictly inside X, we have a compelling geometric picture: the fixed-point map sends a compact convex set into its own interior. Under the standard assumptions, this yields existence. If we also establish a contraction bound for the derivative, we obtain uniqueness of the fixed point and hence uniqueness of the root in the box.

Importantly, these are conditions to check, not properties that every Newton-like approximation automatically satisfies. A poor box or preconditioner may fail the test even though a root exists. Failure to certify is not proof of nonexistence.

#### An exact one-dimensional example

Consider the equation x squared equals two. We know the positive root numerically as approximately one point four one four two. Let's prove it exists uniquely between one point four and one point five.

Choose the midpoint m equals one point four five. The derivative of x squared minus two is twice x, so on the proposed interval it lies between two point eight and three. Take C equal to one divided by two point nine, the inverse derivative at the midpoint.

The ordinary Newton correction from m is approximately one point four one four six five five. The interval derivative correction accounts for the fact that the true derivative changes across the box. In this case, the correction is small: its maximum magnitude is about one point seven two four thousandths.

Therefore the Krawczyk enclosure lies approximately between one point four one two nine three one and one point four one six three seven nine. This lies strictly inside our original interval. The derivative of the fixed-point map has absolute value no greater than one divided by twenty-nine throughout the original interval. That is less than one, so the map is a contraction. Banach's fixed-point theorem gives exactly one root in the interval.

This is stronger than saying the solver found about one point four one four. We have proved the existence and uniqueness of an exact mathematical solution in a rigorous enclosure.

#### Interval Newton versus Krawczyk

The interval Newton method also uses a Jacobian enclosure, but it solves an interval linear system to bound the Newton correction. The Krawczyk method uses a chosen numerical preconditioner C, which can make computation easier and reduce sensitivity to directly inverting an interval matrix.

The two methods are closely related. Both can shrink a box, reject boxes that cannot contain a zero, and provide existence or uniqueness certificates under precise inclusion conditions. For larger systems, the quality of the preconditioner and the width of the interval Jacobian are critical.

An important difficulty is interval dependency. If a variable appears repeatedly in an expression, naive interval evaluation may treat those occurrences as though they were independent, producing an overly wide bound. Better formulations, automatic differentiation with rigorous enclosures, and box subdivision can help.

#### What a certificate should contain

A verified computation should record the original equations, the interval box, the evaluation conventions, the preconditioner, and the actual inclusion or contraction inequalities. Merely labeling a solver result verified is not enough. The final inequalities must be reproducible with mathematically controlled arithmetic.

For a large nonlinear system, certification can be substantially harder than finding a candidate root. That extra work is justified when the result is to support a theorem, rule out an alternative branch, or validate a computed equilibrium in a sensitive scientific model.

The conceptual shift is from numerical plausibility to a fixed-point proof. We use floating-point computation to discover where to look, then use interval arithmetic and analytic conditions to demonstrate what is truly there.

### Validated Integration of Ordinary Differential Equations

A numerical integrator takes an initial state and produces a succession of approximate states. It may use very small time steps. It may compare two methods of different orders and report a tiny estimated error. Yet none of that alone proves the exact solution lies inside a particular interval.

Validated integration has a stronger goal. It constructs an enclosure: a region of state space guaranteed to contain the exact solution throughout a time step, or at least at the step's endpoint. The guarantee must account for uncertainty in initial conditions, truncation error in the numerical method, and floating-point rounding.

Start with the simplest differential equation: the rate of change of x equals x. At time zero, suppose x lies between one and one point zero one. The exact solutions are exponential curves, and after a short time the uncertainty interval expands. A standard numerical method might give a good approximation to its midpoint. A validated method must surround the entire family of possible exact trajectories.

#### First prove the solution stays inside a box

The first task is not to take a numerical step. It is to find a region Y that provably contains the solution over the whole proposed time interval. Consider a short interval from zero to one tenth. Suppose we choose Y from point nine to one point two.

Inside Y, the derivative x is between point nine and one point two. Over one tenth of a time unit, its total contribution to change is between zero and one tenth times that derivative range. Starting anywhere between one and one point zero one, the integral equation therefore maps candidate paths back inside our chosen box.

This is an a priori enclosure. With a locally Lipschitz vector field and a suitable inclusion test, a fixed-point argument establishes the existence of a solution inside Y, with uniqueness under the standard hypotheses. The value of the test is that the region is known before we trust any approximate trajectory.

The box may be deliberately broad. Its purpose is correctness. Once we know where the solution can go, we can bound higher derivatives and obtain a much tighter enclosure for the endpoint.

#### Taylor expansions with a certified remainder

For the exponential example, write a second-order Taylor approximation: the initial value multiplied by one plus the step size plus half the step size squared. A Taylor theorem tells us that the omitted third-order remainder depends on the third derivative at an intermediate time.

Here every time derivative of x equals x, and the a priori box bounds x above by one point two. The remainder over a step of one tenth is therefore at most one point two times one tenth cubed, divided by six. That is two ten-thousandths.

The endpoint then lies in a specific interval obtained by evaluating the Taylor polynomial over the entire initial interval and adding the rigorous remainder interval. Unlike an empirical step-size controller, this computation gives an inclusion that can be checked mathematically.

If we implement it using floating-point numbers, we must round interval endpoints outward. Rounding to nearest can quietly exclude a valid solution. Libraries for validated numerics therefore use directed rounding or exact rational arithmetic where practical.

#### Why narrow intervals become wide

Validated does not mean automatically tight. Interval arithmetic can lose correlations. Suppose two quantities are known to be equal. Their difference is zero, but if we replace each with the same broad interval and subtract them independently, the resulting interval contains a whole range of possible differences.

Over many ODE steps this dependency problem can cause interval enclosures to grow far faster than the true uncertainty set. The geometric effect is called wrapping: a narrow, rotated, or curved set is repeatedly boxed in axis-aligned rectangles, and the empty corners accumulate as apparent uncertainty.

More sophisticated validated integrators track changes of coordinates, use interval or Taylor models with correlated remainders, and split or refine sets when necessary. These techniques do not weaken the proof. They help the proof remain informative over longer trajectories.

#### An integrator can fail honestly

What happens if a proposed step is too large? The inclusion test for the a priori enclosure may fail. A rigorous solver should reduce the step, choose a better set representation, or report that it could not validate the step. It must not silently replace a failed proof with a plausible-looking floating-point answer.

Notice the distinction between a solver failure and a mathematical singularity. A rigorous method may fail because its enclosure became too wide, even though the true solution continues smoothly. Conversely, a numerical method may continue returning numbers while the mathematical solution approaches finite-time blow-up.

Validated integration therefore offers a new kind of computational contract. An accepted step comes with a mathematically justified containing set. An unaccepted step makes no such claim. Together with interval methods for root finding and verified linear algebra, this is one of the ways numerical computation can produce evidence suitable for later mathematical proofs.

### Validated Bifurcation Diagrams and Computer-Assisted Proof

Imagine solving a nonlinear equation over a range of parameter values. A numerical package finds equilibria, draws a curve of solutions, and shows a turning point where two branches meet. The picture may look smooth and convincing. But a finite collection of approximate roots does not prove that the continuum of solutions connects as drawn.

A Newton solve can converge to an unintended branch. It can miss a narrow loop. Two nearby roots can merge, and numerical conditioning becomes poor just where the most interesting dynamics occurs. A step-size choice can create apparent gaps or crossings. Rounding can even move a computed root across a narrow threshold.

Validated numerical analysis asks for a stronger output. Instead of merely providing approximate points on a curve, produce enclosures that provably contain true solutions. Instead of estimating where a fold occurs, verify the defining equations and nondegeneracy conditions for a saddle-node bifurcation. This converts a numerical exploration into a finite chain of mathematical certificates.

### What makes a saddle-node a fold?

Start with an equilibrium equation F of x and a parameter mu equal to zero. At a regular solution, the derivative of F with respect to x is nonzero. The implicit-function theorem then says the solution can be described locally as a smooth function of mu.

At a turning point this derivative vanishes. The ordinary parameterization by mu fails. But the failure alone is not enough to prove a genuine saddle-node. We also need the parameter to unfold the degeneracy and the second derivative in x to be nonzero.

For a scalar equation, a nondegenerate fold has four essential conditions: F equals zero, its first x derivative equals zero, its second x derivative is nonzero, and its parameter derivative is nonzero. The first two locate the candidate. The last two distinguish a quadratic turning point from a higher-order degeneracy or a parameter that does not actually change the equation near the point.

A concrete model is x cubed minus x plus mu equal to zero. Its turning points are determined by three x squared minus one equal to zero. One fold has x equal to one over the square root of three, with mu equal to two over three square roots of three. The other fold is its negative counterpart.

Near the positive fold, two nearby equilibria occur for parameter values slightly below the fold value; for slightly higher values there are none in that neighborhood. The third real root of the cubic may still exist far away. The local fold statement must not be confused with the count of all roots of the equation.

### Isolate the candidate with intervals

We need not know the irrational fold coordinates as decimal approximations with many digits. A short rational interval suffices. For x, use the interval from 0.577 to 0.578. At the left endpoint, three x squared minus one is negative. At the right endpoint it is positive. The expression is strictly increasing throughout this positive interval.

Therefore exactly one value of x in the interval makes the derivative vanish. The corresponding mu is x minus x cubed. Simple interval bounds put it inside a small rational interval around 0.385. We have isolated the fold by exact inequalities rather than by a floating-point plot.

The same method works for simple polynomial examples, but large systems call for a more systematic framework. One creates an augmented system consisting of F equal to zero and the x derivative of F equal to zero. The fold is now an ordinary isolated zero of that augmented system, because its Jacobian is invertible under the nondegeneracy conditions.

### Interval Newton and the Krawczyk operator

Classical Newton iteration uses an approximate derivative to improve an approximate root. Interval Newton replaces a point derivative with an interval enclosure of all derivatives over a whole box. Its conclusion is a theorem about every possible root in that box.

The Krawczyk operator is a closely related tool. Start with a candidate center, an approximate inverse Jacobian, and an interval box. Compute a corrected center and add an interval bound for all possible linearization errors. If the resulting Krawczyk set lies strictly inside the original box, and the relevant nonsingularity or contraction conditions hold, we can establish existence and uniqueness of a true root in the box.

The distinction between existence and uniqueness matters. A small residual at the center alone does not prove either. An inward inclusion establishes an existence statement under the theorem's hypotheses; a suitable contraction bound can strengthen it to uniqueness. Neither result can be inferred simply from the number of Newton iterations that converged.

For the cubic fold, the augmented Jacobian has one row containing the x derivative and parameter derivative, and another containing the second x derivative and mixed derivative. At the fold it has nonzero determinant. That is why we can isolate the fold as an ordinary zero of a two-component system even though the original equation is singular with respect to x.

### From points to entire branches

Validating a handful of roots still does not prove the whole branch diagram. To cover a branch, we need intervals that enclose solution arcs, with verified overlaps and conditions excluding unobserved segments in the region of interest.

Away from folds, the implicit-function theorem gives smooth local parameterizations. Near a fold, pseudo-arclength continuation replaces the physical parameter by a coordinate along the solution curve. The augmented continuation equations remain nonsingular through a simple turning point.

A rigorous implementation can cover the curve by validated boxes or tube segments. Each local segment is connected to the next using verified continuation bounds. Additional global arguments may be needed to prove that no other disconnected branches exist in a chosen parameter region. A certificate of the branch we followed is not automatically a census of every solution everywhere.

This is especially important in high-dimensional discretized PDEs. A visualized branch may include unstable equilibria, folds, symmetry-breaking transitions, and reconnections. Verifying a specific branch segment and proving global completeness are distinct computational achievements.

### Floating-point direction matters

Interval arithmetic is only rigorous if its operations enclose the exact results. Ordinary rounded-to-nearest arithmetic may shrink an interval accidentally. Rigorous packages use outward rounding or exact rational arithmetic for critical steps. Bounds on transcendental functions, linear solves, and truncation errors must obey the same enclosure discipline.

One must also distinguish a verified zero of a finite discretization from a verified solution of the original continuous equation. For a PDE, a grid-based calculation might validate the discrete system while discretization error remains uncontrolled. To prove a continuous bifurcation, one needs estimates connecting the finite-dimensional approximation to the infinite-dimensional problem.

### What the final proof artifact should contain

A convincing computer-assisted bifurcation result records the equation, parameter domain, approximate centers, interval boxes, derivative enclosures, and the precise theorem applied. It identifies each validated root, branch segment, and fold, and states what has not been excluded.

In our cubic example, the hand calculation already certifies the folds. In a large reaction–diffusion system, the same logical structure can be implemented with interval matrices, validated continuation, and a priori bounds. The goal is not to replace mathematics with a plot. It is to make the computer produce the inequalities that a conventional proof would require.

### Validated Periodic Orbits and Floquet Multipliers

A numerical solver can draw a trajectory that seems to close upon itself. After one revolution, the simulated state is close to where it started. Such a plot is evidence for a periodic orbit, but it can be misleading. Numerical error may close a trajectory that is not actually periodic. Or an actual orbit may be unstable, with the solver tracing it only because we carefully initialized near it.

To turn a computed picture into a mathematical statement, we need a quantitative enclosure of a true orbit, not just a small plotted discrepancy. Validated numerics does this by combining an approximate orbit with rigorous bounds on the differential equation's flow and derivatives.

There are two assertions to certify. Existence asks whether some exact solution returns to its initial condition after a positive time. Stability asks what nearby solutions do after that return. The second is measured by Floquet multipliers, and proving existence alone does not determine them.

### Shooting turns an orbit into a root

For an autonomous differential equation, write the flow as a function that takes an initial state and a time duration to the evolved state. A periodic orbit is an initial point and a positive period for which the flow returns exactly to the point.

The equation that the final state equals the initial state is called the shooting equation. A numerical method can solve it approximately. But an autonomous orbit has a built-in ambiguity: shifting the initial time along the same orbit produces another solution of the shooting equation. As a result, naive Newton iteration on the shooting equation has a singular Jacobian in the direction tangent to the orbit.

We remove that ambiguity by adding a phase condition. For example, we can require the initial point to lie on a chosen transverse section. The unknowns are then the initial state and the period, and the equations include periodic return plus one phase condition. Under a suitable nondegeneracy assumption, the augmented system has an invertible derivative.

This phase condition is mathematical gauge fixing. It does not change the closed geometric orbit; it selects one representative among all choices of starting point.

### The radial normal form has an exact cycle

Consider a planar system described in polar coordinates. Let the radius grow at a rate equal to radius times one minus radius squared, and let the angle advance at one radian per unit time. At radius one, the radial derivative is zero. The angle continues to rotate uniformly. Thus the unit circle is an exact periodic orbit with period two pi.

This is a clean reference problem because its stability is also calculable. Perturb the radius slightly above or below one. Differentiate the radial equation at radius one. The derivative is negative two. Therefore a small radial perturbation is multiplied by the exponential of negative two times elapsed time, to first order.

After one complete revolution, the radial multiplier is the exponential of negative four pi. This is strictly between zero and one, so small radial errors decay geometrically from period to period. The angular direction has multiplier one because translating the starting phase along the same orbit yields another point on the orbit.

The two multipliers have completely different meanings. The unit multiplier is the unavoidable neutral tangent direction. The smaller multiplier measures attraction transverse to the orbit. This separation is what a validated Floquet calculation must reproduce.

### Variational equations compute the derivative of the return

For a general differential equation, the derivative of the flow with respect to initial conditions satisfies a matrix differential equation called the variational equation. Its coefficient matrix is the Jacobian of the vector field evaluated along the evolving trajectory.

Integrate the variational equation for one period. The resulting matrix is the monodromy matrix. Its eigenvalues are Floquet multipliers. A multiplier of magnitude greater than one implies a linearly growing direction over repeated periods. Multipliers strictly inside the unit circle indicate linear transverse decay, provided the neutral directions required by symmetries are treated correctly.

Autonomous systems always have at least one multiplier equal to one along a non-equilibrium periodic orbit. Hamiltonian systems often have additional reciprocal-pairing structure, and conservation laws can create further neutral modes. Therefore a naive test that all multipliers lie strictly inside the unit circle is not the correct stability criterion for such systems.

### Why ordinary floating point is insufficient

Suppose an approximate shooting residual is one in a billion. That is impressive, but it is not proof of a zero nearby. The derivative might be nearly singular, the flow solver might have uncontrolled accumulated error, or a hidden nonlinear term might eliminate the apparent root.

Interval arithmetic encloses every computed quantity. A validated flow integrator supplies intervals guaranteed to contain the true flow and its derivative over the period. Using those intervals, an interval Newton or Krawczyk operator can test whether a candidate box contains a unique solution of the phase-fixed shooting equations.

The decisive result is usually an inward inclusion or contraction condition on an explicitly defined box. If it succeeds, the approximate closed orbit is replaced by a theorem: there exists an exact periodic orbit whose initial data and period lie within the stated bounds.

Careful treatment of time is required. Period uncertainty changes the integration endpoint. If a Poincare return map is used instead of fixed-time shooting, the event time must be enclosed and transversality of the section verified. A numerical event detector that reports the first sign change is not by itself a certified return map.

### Certifying the Floquet spectrum

After validating the orbit, enclose the monodromy matrix using rigorous integration of the variational equation. Then use interval spectral tools or verified bounds on the characteristic polynomial to locate its eigenvalues. For low dimensions, trace and determinant bounds can be enough. For larger systems, eigenvalue separation and invariant-subspace methods may be necessary.

One must distinguish an approximate eigenvalue from a proved spectral enclosure. In nonnormal systems, small matrix errors can move eigenvalues much more than a naive residual suggests. An interval containing the monodromy entries is a first step; a rigorous eigenvalue inclusion theorem is another step.

For the radial normal form, the exact transverse multiplier is the exponential of negative four pi. An interval computation might enclose it in a narrow positive interval strictly below one. That would certify local transverse linear attraction. But it would not by itself prove a global basin of attraction for every initial condition.

### Verifying an entire branch of cycles

Now suppose the vector field depends on a parameter. Numerical continuation may draw a smooth family of closed orbits as the parameter varies. Validating one point on that family does not certify the whole branch.

A rigorous continuation algorithm uses overlapping validated boxes or segments with parameter-dependent bounds. Each step proves the existence of a nearby periodic orbit; controlled overlaps show that the pieces connect. At a fold of cycles, ordinary parameterization can fail and a pseudo-arclength or other augmented system may be needed.

Even a rigorously continued branch may not be the only branch. Completeness requires additional exclusion arguments. This is the same distinction encountered when validating equilibrium bifurcations: local correctness and global census are different claims.

### Infinite-dimensional systems add a second layer

If the original problem is a partial differential equation and we discretize it into a finite set of ordinary differential equations, validating a periodic orbit of the discretization does not yet validate a periodic solution of the PDE. One must bound the discretization or truncation remainder in a function space.

Fourier-series approaches and radii-polynomial methods can provide these infinite-dimensional tail estimates for suitable analytic or smooth equations. The computer checks a finite collection of inequalities, while the accompanying estimates control all omitted modes. This creates a genuine computer-assisted proof instead of a high-resolution simulation.

### What a reproducible certificate records

A useful verification artifact specifies the vector field, parameter box, approximate initial state and period, phase condition, interval flow bounds, derivative bounds, zero-inclusion theorem, and spectral enclosures. It also states the region where uniqueness is proved and any unresolved global alternatives.

The principle is direct. A plot suggests a periodic orbit. An exact return equation defines it. A phase condition removes a redundant degree of freedom. Interval Newton certifies the return. The variational equation and verified Floquet multipliers describe its local stability. Each step has a distinct mathematical role, and combining them yields a claim stronger than any attractive trajectory plot.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Euler and Runge–Kutta Methods: Accuracy Is Not Stability

**Track:** Numerical Analysis. **Background:** derivatives, initial-value problems, Taylor expansion, and elementary error bounds. **Question:** how can a sequence of discrete updates approximate a continuous trajectory, and why can small steps still give unstable or misleading answers?

#### Mathematical companion (not spoken)

For \(y'=f(t,y)\), explicit Euler is \(y_{n+1}=y_n+h f(t_n,y_n)\). Explicit midpoint is
\[
k_1=f(t_n,y_n),\quad k_2=f(t_n+h/2,y_n+hk_1/2),\quad y_{n+1}=y_n+h k_2.
\]
Classical RK4 is
\[
\begin{aligned}
k_1&=f(t_n,y_n),\\
k_2&=f(t_n+h/2,y_n+hk_1/2),\\
k_3&=f(t_n+h/2,y_n+hk_2/2),\\
k_4&=f(t_n+h,y_n+hk_3),\\
y_{n+1}&=y_n+\frac h6(k_1+2k_2+2k_3+k_4).
\end{aligned}
\]
Under sufficient smoothness and a Lipschitz bound, Euler local defect is \(O(h^2)\), global error \(O(h)\); explicit midpoint \(O(h^3)\) and \(O(h^2)\); RK4 \(O(h^5)\) and \(O(h^4)\). These are fixed-time asymptotic statements, not uniform guarantees for arbitrarily stiff equations.

**Discrete Grönwall.** If \(\|e_{n+1}\|\le(1+hL)\|e_n\|+Ch^{p+1}\) and \(e_0=0\), then for \(t_n\le T\) and \(L>0\),
\[
\|e_n\|\le Ch^p\frac{(1+hL)^n-1}{L}\le Ch^p\frac{e^{LT}-1}{L}.
\]
For \(L=0\), the bound is \(CT h^p\).

**Absolute stability for \(y'=\lambda y\).** Euler: \(R(z)=1+z\). RK4: \(R(z)=1+z+z^2/2+z^3/6+z^4/24\). Backward Euler: \(R(z)=(1-z)^{-1}\). The linear test iterates decay when \(|R(h\lambda)|<1\). Backward Euler satisfies \(|R(z)|\le1\) for \(\Re z\le0\), where the denominator is nonzero.

**Worked step.** \(y'=-2y\), \(y(0)=1\), \(h=1/4\): Euler \(y_4=(1-2h)^4=(1/2)^4=0.0625\), while \(y(1)=e^{-2}\approx0.135335\).

##### Exercises with answers

1. For \(y'=-10y\), what is Euler's absolute-stability requirement? **Answer:** \(0<h<0.2\).
2. How many derivative evaluations does classical RK4 require per step? **Answer:** four.
3. Does \(O(h^2)\) local defect imply \(O(h^2)\) global accuracy for Euler? **No.** Under the stated conditions its global accuracy is first order.
4. Is backward Euler explicit? **No.** Its update generally requires solving for the new state.

##### Reading

MIT 18.330, [Introduction to Numerical Analysis lecture notes](https://ocw.mit.edu/courses/18-330-introduction-to-numerical-analysis-spring-2004/pages/lecture-notes/), ODE integration and error; MIT 18.330, [initial-value problem notes](https://math.mit.edu/icg/resources/teaching/18.330/18.330-Feb23.pdf), local and global order and linear stability.

### Interval Arithmetic: From Plausible Answers to Verified Enclosures

**Track:** Numerical Analysis and Reliable Computation. **Background:** floating-point error, conditioning, Newton iteration, numerical quadrature. **Central question:** what does a computation need to do before we can claim it encloses the exact mathematical answer?

#### Mathematical companion (not spoken)

An interval \(X=[\underline x,\overline x]\) denotes a set of real numbers. Exact set addition is
\[
X+Y=[\underline x+\underline y,\overline x+\overline y].
\]
A validated floating-point implementation rounds the lower endpoint **downward** and the upper **upward** for every primitive operation. Multiplication encloses all four endpoint products. If \(0\in Y\), interval division by \(Y\) requires a specified extended-interval or failure policy; naive reciprocal formulas are invalid.

**Dependency example:** for \(X=[0,1]\), \(X-X=[-1,1]\), whereas \(\{x-x:x\in X\}=\{0\}\). Inclusion does not imply a tight enclosure.

**Interval Newton:** for \(f(x)=x^2-2\), \(X=[1,2]\), midpoint \(m=3/2\), and derivative enclosure \(f'(X)=[2,4]\),
\[
N(X)=m-\frac{f(m)}{f'(X)}=\frac32-\frac{1/4}{[2,4]}
=[11/8,23/16]=[1.375,1.4375]\subset\operatorname{int}(X).
\]
The interval-Newton inclusion and nonzero derivative certify a unique zero of \(f\) in \(X\), with all displayed rational endpoints exactly representable in binary. Further interval iteration contracts the enclosure.

A validated result must specify the mathematical input uncertainty, outward-rounded implementation, treatment of exceptional operations, and any analytic hypotheses used to infer roots, uniqueness, or discretization error. IEEE 1788-2015 specified a standard interval arithmetic model, but its status and actual implementations should be verified for a given project.

##### Exercises with answers

1. What does natural interval evaluation give for \(X-X\) when \(X=[2,3]\)? **Answer:** \([-1,1]\), even though the exact range of \(x-x\) is \(\{0\}\).
2. Does \(0\in f(X)\) prove \(f\) has a root in \(X\)? **No:** interval overestimation may include zero even when the actual range does not.
3. Why can a single nearest-rounded floating point value fail to enclose the decimal \(0.1\)? **Answer:** the rounded binary value generally differs from the exact rational \(1/10\).
4. Does a certified small residual suffice to bound a linear-system solution error? **Not by itself:** the inverse or condition of the operator must be bounded too.

##### Reading and source notes

- IEEE Standards Association, [IEEE 1788-2015 Standard for Interval Arithmetic](https://standards.ieee.org/ieee/1788/4431/), interval operation semantics (standards status subject to change).
- Siegfried M. Rump, *Verification Methods: Rigorous Results Using Floating-Point Arithmetic*, Acta Numerica 19 (2010), https://doi.org/10.1017/S096249291000005X.
- Ramon E. Moore, R. Baker Kearfott, and Michael J. Cloud, *Introduction to Interval Analysis* (SIAM, 2009).

### Verified nonlinear systems, trajectories, bifurcations, and periods

### Verified nonlinear systems, trajectories, bifurcations, and periods

#### Companions, sources, and study material (not spoken)

##### Verified Nonlinear Systems: Interval Newton and Krawczyk Operators

**Track:** Numerical Analysis. **Background:** interval arithmetic, Jacobians, Newton's method, fixed-point theorems. **Central question:** when can computation prove that a root exists and is unique within a stated box?

###### Mathematical companion (not spoken)

Let `f:D subset R^n -> R^n` be continuously differentiable, `X subset D` a closed interval box, `m in X`, `C` a nonsingular approximate inverse Jacobian, and `J(X)` an interval matrix enclosing every exact Jacobian `Df(x)` for `x in X`. The Krawczyk enclosure is
\[
K(X)=m-Cf(m)+(I-CJ(X))(X-m).
\]
For the fixed-point map `T(x)=x-Cf(x)`, the mean-value theorem guarantees `T(X) subset K(X)` under inclusion-correct interval arithmetic. Thus `K(X) subset X` gives a self-map of a compact convex box, proving existence by Brouwer's theorem. If also `sup_{J in J(X)} ||I-CJ||<1` in a specified induced norm, Banach proves uniqueness of the fixed point in X; nonsingularity of C makes fixed points equivalent to roots of f. Standard interval-Newton/Krawczyk theorems provide further sufficient conditions, but state the actual assumptions used.

For `f(x)=x^2-2`, choose `X=[7/5,3/2]`, `m=29/20`, `C=10/29`. Then `f(m)=41/400`, `J(X)=[14/5,3]`, and
\[
I-CJ(X)=[-1/29,1/29],\qquad X-m=[-1/20,1/20].
\]
So
\[
K(X)=\left[\frac{1639}{1160},\frac{1643}{1160}\right]
\subset (7/5,3/2),
\]
and the contraction factor is at most `1/29`. The rational endpoints avoid any ambiguity about floating-point rounding; an actual implementation must use outward-rounded intervals.

##### Exercises with answers

1. What does a small residual alone fail to establish? **Answer:** existence and uniqueness of a nearby exact zero without conditioning and derivative bounds.
2. What upper bound on the derivative of T is obtained in the square-root example? **Answer:** `1/29`.
3. If the Krawczyk enclosure is not contained in X, has nonexistence been proved? **Answer:** no; this sufficient test has simply failed.
4. Why must interval operations use outward rounding? **Answer:** otherwise computed endpoints may exclude exact values and invalidate the proof.

##### Reading and source notes

- [Krawczyk and Neumaier, An Improved Interval Newton Operator](https://arnold-neumaier.at/scan/45.pdf), existence and uniqueness enclosures for nonlinear systems.
- [Moore, Kearfott, and Cloud, Introduction to Interval Analysis](https://doi.org/10.1137/1.9780898717716), interval Newton and validation.
- [Alefeld and Mayer, Interval Analysis: Theory and Applications](https://doi.org/10.1016/S0377-0427(00)00505-4), interval enclosures and computational techniques.

##### Validated Integration of Ordinary Differential Equations

**Track:** Numerical Analysis and Reliable Computation. **Background:** local existence, Taylor methods, interval arithmetic, floating-point rounding. **Central question:** how can a computer return a set guaranteed to contain every true solution arising from an initial uncertainty set?

###### Mathematical companion (not spoken)

For \(x'(t)=f(x(t))\), initial set \(X_0\subset\mathbf R^d\), and step \([0,h]\), one sufficient enclosure test is to find a compact convex box Y with
\[X_0+[0,h]f(Y)\subset\operatorname{int}(Y)\]
and a locally Lipschitz f on a neighborhood of Y. Under standard integral-operator fixed-point conditions this gives existence of trajectories in Y for all initial values in X_0 over [0,h]; Lipschitz continuity ensures uniqueness. The inclusion is sufficient, not necessary, and more general ODE methods use sharper operators.

**Verified example:** \(x'=x\), \(X_0=[1,1.01]\), h=0.1, Y=[0.9,1.2]. Then \(f(Y)=[0.9,1.2]\) and \(X_0+[0,0.1]f(Y)\subseteq[1,1.13]\subset\operatorname{int}Y\).

Second-order Taylor with the certified third-derivative bound \(|x'''|=|x|\le1.2\) gives
\[x(h)\in X_0\left(1+h+\frac{h^2}2\right)+[0,1.2h^3/6]\subseteq[1.105,1.11625].\]
The exact endpoint set is \([e^{0.1},1.01e^{0.1}]\), which lies inside this interval. These numerical endpoints are rational decimals and can be evaluated without floating-point uncertainty; an implementation using binary floats must enclose them outward.

**Error mechanisms:** truncation remainder, initial uncertainty, rounding error, and the dependency/wrapping effect. A numerical error estimate without a certified bound does not prove containment. An inclusion failure does not imply ODE nonexistence.

##### Exercises with answers

1. For x'=x and X_0=[1,1.01], is Y=[0.9,1.2] a valid a priori box over h=0.1? **Answer:** yes; the integral-image interval lies in [1,1.13] inside the interior of Y.
2. Why is the third derivative bound 1.2 valid? **Answer:** x'''=x for this ODE, and the a priori enclosure bounds x along the step by 1.2.
3. What is wrong with subtracting the interval [1,2] from itself to infer x-x=0? **Answer:** ordinary interval subtraction loses the equality dependency and returns [-1,1].
4. What must a validated solver report when its inclusion test fails? **Answer:** no validated enclosure for that step; it may retry with a smaller step or better set representation, but may not assert containment.

##### Reading and source notes

- [CAPD DynSys documentation, rigorous interval Poincaré maps](https://capd.sourceforge.net/capdDynSys/docs/html/a05237.html), certified integration and return maps.
- [CAPD DynSys documentation, interval set representations](https://capd.sourceforge.net/capdDynSys/docs/html/a05202.html), practical control of wrapping.
- [CAPD DynSys documentation, one-step Taylor method](https://capd.sourceforge.net/capdDynSys/docs/html/a05230.html), introduction to Taylor-method integration (non-rigorous and interval variants must be distinguished).

##### Validated Bifurcation Diagrams and Computer-Assisted Proof

**Track:** Numerical Analysis. **Background:** Newton's method, interval arithmetic, the implicit-function theorem, and equilibria of parameterized differential equations. **Central question:** how can a numerical diagram be turned into a proof that branches and turning points actually exist?

###### Mathematical companion (not spoken)

Consider `F(x,mu)=x^3-x+mu`. Fold conditions are `F=0`, `F_x=3x^2-1=0`, `F_xx=6x!=0`, `F_mu=1!=0`. The positive fold is
\[
(x_*,\mu_*)=(1/\sqrt3,\ 2/(3\sqrt3)).
\]
**Exact rational isolation:** `F_x(577/1000)<0` and `F_x(578/1000)>0`, and `F_xx>0` on this interval. Thus it contains exactly one zero of F_x; setting `mu=x-x^3` isolates the fold parameter. The rough rational box `x in [577/1000,578/1000]`, `mu in [383/1000,387/1000]` contains the positive fold. For `mu<mu_*` sufficiently close to `mu_*`, two nearby roots exist; for `mu>mu_*` sufficiently close, none exists in this neighborhood.

For `G(x,mu)=(F,F_x)`, the Jacobian is
\[
 DG=\begin{pmatrix}3x^2-1&1\\6x&0\end{pmatrix},\quad
\det DG\big|_{(x_*,\mu_*)}=-2\sqrt3\ne0.
\]
For general G, Krawczyk form `K(X)=x_0-CG(x_0)+(I-CDG(X))(X-x_0)` uses an interval extension `DG(X)` and approximate inverse C. Under standard Krawczyk hypotheses, strict inward inclusion plus an appropriate contraction/nonsingularity bound certifies a unique zero. For a continuous PDE, separately bound the discretization remainder.

##### Exercises with answers

1. Find the negative fold. **Answer:** `x=-1/sqrt3`, `mu=-2/(3sqrt3)`.
2. Why is solving `F=0,F_x=0` preferable to Newton on F alone at a fold? **Answer:** the augmented Jacobian is nonsingular at a nondegenerate fold while F_x vanishes there.
3. Does a validated branch segment prove no other solution branches exist in the domain? **Answer:** no; that requires global exclusion or covering arguments.
4. What makes interval arithmetic mathematically rigorous? **Answer:** outward enclosures for every operation and controlled approximation/truncation error.

##### Reading and source notes

- [Sander and Wanner, Validated Saddle-Node Bifurcations and Applications to Lattice Dynamical Systems](https://epubs.siam.org/doi/10.1137/16M1061011), rigorous branch validation and fold tests.
- [J.-P. Lessard, Research on computer-assisted proofs](https://www.math.mcgill.ca/jplessard/research.html), validated nonlinear dynamics and bifurcation results.
- [SageMath documentation, Real Interval Fields](https://doc.sagemath.org/html/en/reference/rings_numerical/sage/rings/real_mpfi.html), outward-rounded interval computations.

##### Validated Periodic Orbits and Floquet Multipliers

**Track:** Numerical Analysis. **Background:** ordinary differential equations, interval Newton methods, Poincare maps, and linearization of dynamical systems. **Central question:** how can a numerical closed orbit become a theorem about the existence and stability of a true periodic solution?

###### Mathematical companion (not spoken)

For `x'=f(x)`, denote the flow by `phi_T(x_0)`. A phase-fixed shooting system in dimension n is
\[
F(x_0,T)=\big(\phi_T(x_0)-x_0,\ g(x_0)\big)=0
\]
with n+1 equations for n+1 unknowns, where g fixes a transverse section and the root is restricted to `T>0`. The flow derivative `Phi(t)=D_(x_0)phi_t(x_0)` satisfies `Phi'=Df(phi_t(x_0))Phi`, `Phi(0)=I`. Floquet multipliers are eigenvalues of `Phi(T)`; an autonomous non-equilibrium periodic orbit has a unit tangential multiplier.

For `r'=r(1-r^2)`, `theta'=1`, the unit circle has period `T=2pi`. Linearizing radial dynamics gives `delta r'=-2 delta r`, so transverse multiplier `mu_r=e^(-4pi)`; the tangential multiplier is one. A Krawczyk inclusion on the augmented shooting box with rigorously enclosed flow and Jacobian can establish a unique phase-fixed root in the box, provided the standard nonsingularity/contraction hypotheses hold. Enclosing Phi(T) does **not** automatically certify its eigenvalues without a justified spectral inclusion method.

##### Exercises with answers

1. What is the neutral multiplier of a generic autonomous periodic orbit? **Answer:** one, due to phase translation.
2. What is the transverse multiplier of the radial model after half a revolution? **Answer:** `e^(-2pi)`.
3. Why add a phase condition to shooting? **Answer:** to eliminate the free time-shift direction and make the local root system nonsingular.
4. Does verifying a Galerkin periodic orbit prove a periodic orbit of the original PDE? **Answer:** not without bounds on the omitted modes and discretization error.

##### Reading and source notes

- [Hungria, Lessard, and Mireles James, Radii Polynomial Rigorous Numerics for Periodic Solutions](https://doi.org/10.1090/mcom/3046), infinite-dimensional a posteriori existence proofs.
- [Recent Advances in Rigorous Computation of Poincare Maps](https://doi.org/10.1016/j.cnsns.2022.106366), validated event maps and return sections.
- [Systematic Computer-Assisted Proofs of Periodic Orbits of Hamiltonian Systems](https://doi.org/10.1016/j.cnsns.2013.12.025), interval Newton and stability verification.
