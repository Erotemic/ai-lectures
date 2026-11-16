# Semigroups, smoothing, and nonlinear existence

<!-- BEGIN SPOKEN LECTURE -->

# Semigroups, smoothing, and nonlinear existence

## Semigroups and Generators: Solving Time Evolution Beyond Self-Adjoint Operators

A room cools after the heater switches off. A dye cloud spreads through water. A conveyor belt carries material from one position to another. These processes all change with time, but they are not all governed by self-adjoint operators. We need a language that describes evolution before we insist that the generator has a special spectral decomposition.

A semigroup is a family of operators, one for each nonnegative time, with two properties. At time zero, nothing has happened: the operator is the identity. Advancing first by time s and then by time t gives the same result as advancing by their sum. This is the rule that makes a time-homogeneous evolution consistent.

For ordinary matrices, we write the evolution as an exponential: e to the t times A. The semigroup property follows from the usual exponential algebra when the same matrix appears in both factors. In an infinite-dimensional function space, the generator A may be unbounded, so a naive power series in A need not act on arbitrary inputs. Rather than defining the evolution by that series, we can begin with the family of bounded operators and recover A by asking for its instantaneous rate of change at zero.

Here is a concrete example that does not depend on eigenvectors. Let the state be a square-integrable function on the real line. Define the evolution by shifting the function to the right: the new profile at x is the old profile at x minus t. Translation preserves the L two norm. Advancing by two time intervals adds the shifts, so the semigroup law holds. As the time shift approaches zero, the translated function approaches the original in L two. This is strong continuity.

For a sufficiently smooth state, the rate of change at time zero is minus its spatial derivative. Thus the generator of right translation is minus differentiation, with an appropriate Sobolev domain. The generator is unbounded as an operator on L two, even though every finite-time shift has operator norm one. High-frequency functions can have large derivatives while remaining perfectly finite-energy functions.

Another example is heat flow. The heat propagator at time t convolves the initial condition with a Gaussian of variance proportional to t. The operators are contractions on L two and form a semigroup. The generator is the Laplacian on its H two domain. For positive time, heat flow smooths. Translation flow does not smooth; it simply moves features through space. Both fit the semigroup framework despite their very different physical behavior.

The connection to derivatives requires a distinction. Strong continuity means that for each fixed input, the evolved vector approaches that input as time approaches zero. It does not mean the family is continuous in operator norm. Translation on L two is strongly continuous but not norm continuous at zero. The generator is defined only on inputs where the difference quotient converges in the Hilbert or Banach space norm. That domain can be a strict dense subset of the state space.

If A were a bounded operator, the exponential power series would define the semigroup for all real times and the derivative at zero would exist for every input. For an unbounded generator, we need criteria that say the evolution exists even though the instantaneous derivative is not everywhere defined. The Hille–Yosida theorem provides such criteria through resolvent estimates. For contraction semigroups on Banach spaces, it links the existence of a strongly continuous semigroup to dense domain, closedness, and bounds on resolvents of the generator.

In Hilbert spaces there is a particularly useful form. If an operator is densely defined, dissipative, and sufficiently surjective after a positive shift, it generates a contraction semigroup. This is the Lumer–Phillips theorem. Dissipative means the generator does not increase norm instantaneously, in a precise inner-product sense. The range condition guarantees enough solvability to construct the evolution rather than merely checking a formal energy inequality.

What if the equation is driven by an external forcing? A formal differential equation says the time derivative of u equals A u plus f of time. For sufficiently regular data, one can write the solution as the freely evolved initial state plus an integral of the forcing, each past contribution evolved for the remaining time. This is the variation-of-constants formula. It defines a mild solution even when the forcing and initial state do not lie in the generator's domain.

Take the simplest forced relaxation process: a scalar state loses a fixed fraction of its value per unit time and receives a constant input. The solution is the initial value times an exponential decay plus the accumulated, decaying contributions of the input. The semigroup formula is exactly the infinite-dimensional extension of this elementary calculation. For heat flow, each added forcing pattern is smoothed from the moment it enters the system until observation time.

We should not confuse a mild solution with a classical one. A mild solution satisfies the integral representation. To differentiate it in the strong sense, we generally need additional assumptions on the data and generator. This distinction is another case of the domain issue that appeared in functional calculus: the time-evolution operator may act on every state while its instantaneous derivative is meaningful only for some.

Semigroups are therefore a bridge between abstract operators and dynamics. Spectral calculus constructs many examples when the generator is self-adjoint or sectorial. But the semigroup viewpoint also accommodates transport, nonsymmetric diffusion, and equations whose operators do not possess an orthogonal eigenbasis. It tells us which properties must be proved before an evolution law can be trusted: strong continuity, the semigroup identity, generator domain, and estimates that control the effect of errors over time.

## Sectorial Operators: Why Diffusion Smooths Immediately

A diffusion problem has a distinctive behavior. Even if the initial temperature profile contains a sharp corner, the profile becomes smooth as soon as a positive amount of time has passed, at least for the standard heat equation in open space. Contrast that with transporting the same profile rigidly to the right. Translation keeps every corner intact. Both motions are governed by semigroups, but only one is smoothing. We need language that explains the difference.

In a finite-dimensional system, a matrix A generates motion by the exponential of time times A. We can differentiate that exponential because its power series converges in matrix norm. In a differential equation, the generator may be an unbounded differential operator. The Laplacian is a standard example. It measures curvature of a function, and acting on increasingly rapid oscillations makes the result increasingly large. We should not expect an operator-norm power series for the exponential of such a generator.

Fortunately there are two alternative viewpoints. The first works through Fourier frequencies. For the heat equation on the whole line, an initial sine wave with frequency n decays at a rate proportional to n squared. High frequencies disappear much faster than low frequencies. The evolution multiplier is exponential decay in time times frequency squared. This one formula both defines the heat flow on square-integrable data and tells us why derivatives become controlled for positive time.

The second viewpoint uses the resolvent. A resolvent asks us to solve an equation involving the generator shifted by a scalar. Instead of inverting the Laplacian itself, which can have low-frequency problems, we invert a positive shift minus the Laplacian. In Fourier variables, this means dividing by the positive shift plus frequency squared. The division is stable, and the collection of these inverses has uniform bounds in sectors of the complex plane. Such sector-shaped resolvent estimates characterize the class of sectorial generators relevant to analytic semigroups, subject to the standard density and closedness conditions.

The geometric word analytic means more than differentiable in time along the positive real axis. For a suitable generator, the solution operator can be extended to complex times in a sector. This extra regularity implies that differentiating the semigroup for positive times costs a factor that behaves like one over time. At the first instant, such an estimate blows up; we do not claim the initial profile was smooth. At any later instant, however, the operator has had time to suppress high frequencies.

We can verify the size of the effect directly. Take the heat multiplier and apply a Laplacian afterward. The frequency contribution is frequency squared times its exponential damping. Its largest value over all frequencies is proportional to one divided by time. Thus the map taking initial data to the second spatial derivatives of the heat solution is bounded on L two for every positive time, but there is no uniform bound as time approaches zero.

Translation does not do this. Under the translation flow, the size of each Fourier frequency stays constant. Moving a step function does not turn it into a smooth function. The generator, the first spatial derivative, is unbounded, and its semigroup is strongly continuous, but it is not a smoothing analytic semigroup of the heat type. This supplies an important counterexample to the claim that every C-zero semigroup automatically improves regularity.

A realistic parabolic equation may contain variable coefficients or act on a bounded domain. Fourier diagonalization might no longer be available. Resolvent bounds let us reason without knowing every eigenfunction. That is why the operator-theoretic language matters in the proofs of existence, smoothing, maximal regularity and numerical stability.

At the same time, a sectorial estimate is never free. We must check the operator domain, boundary conditions, and the chosen Banach space. Dirichlet and Neumann Laplacians have different domains and different zero modes. The bare symbol for a differential operator does not uniquely specify its evolution. The central lesson is that the smoothing effect of heat is encoded both in frequency damping and in the geometry of the resolvent.

## Banach Fixed Points and Picard Iteration: Constructing a Solution

An equation can sometimes be solved by looking for something that does not change under a certain procedure. If we write a problem as u equals F of u, a solution is a fixed point of F. We might begin with a guess, apply F, apply F again, and hope the guesses approach a limit. But hoping is not a proof. The Banach fixed-point theorem tells us exactly what makes such an iteration work.

Imagine a map that always brings any two points closer by the same fixed percentage. If their original distance is one, their distance after applying the map is at most a half. After another application, at most a quarter. Every new correction becomes smaller at a geometric rate. In a complete metric space, the sequence of guesses is Cauchy and therefore converges. Continuity then shows that its limit is a fixed point. And if there were two fixed points, the map would have to bring them closer while leaving both unchanged, which is possible only if they are identical.

Two conditions are essential: the space must be complete, and the map must send the closed set under consideration back into itself with a contraction constant strictly less than one. A map that merely has Lipschitz constant one may have many fixed points or none. A map that shrinks distances but sends the proposed set outside itself does not give the required iteration either.

Now apply this to a differential equation. Consider a quantity whose rate of change equals its square, beginning with value one. We know from calculus that any sufficiently smooth solution satisfies an integral equation: its value at time t is one plus the integral, from zero to t, of the square of its earlier values. Conversely, a continuous function satisfying this integral equation is differentiable and solves the original equation. This is the integral formulation we can iterate.

Choose the complete space of continuous functions on a short time interval with the maximum norm. Restrict attention to the closed ball of functions whose maximum absolute value is at most two. For any function in that ball, its square is at most four, so the integral map produces a function whose size is at most one plus four times the interval length. If we keep the interval short enough, that stays within the ball.

We must also compare two guesses. Their squares differ by the difference of the guesses multiplied by their sum. Since each guess has size at most two, the sum has size at most four. Integrating over a short interval shows that the map shrinks the maximum distance by at most four times the interval length. On an interval of length one eighth, this contraction factor is at most one half. Both conditions hold. A unique continuous fixed point exists there, and therefore so does a unique solution of the differential equation.

What does the iteration look like? Start with the constant function one. The next guess is one plus time. The next replaces the square inside the integral with the square of one plus time, producing more terms in a power series. Every iteration uses the previous curve to construct a better one. The contraction argument proves this process approaches the actual solution, not just a plausible formal series.

The exact solution is one divided by one minus time. It grows without bound at time one. So local existence does not automatically imply global existence. The fixed-point construction worked on a short interval because the map stayed in a bounded ball. As the solution approaches blow-up, no fixed bounded ball can contain the continuation on an interval reaching beyond time one.

In a Banach space, the same idea works for many systems of ordinary differential equations and semilinear evolution equations. The challenge is to choose a space in which the nonlinear map is locally Lipschitz and the integral operator is small for short times. When the space is a Sobolev space, the product estimates we derived earlier supply the needed Lipschitz constants.

A fixed-point proof therefore has a logical order: select a complete solution space; establish that the map preserves the chosen ball; estimate the difference between two outputs; and choose the time or other parameter to make the contraction constant smaller than one. The conclusion is both an existence theorem and a uniqueness theorem, with a concrete iteration that can be implemented numerically.

## Duhamel’s Formula: Solving a Nonlinear Equation with a Linear Flow

A linear evolution equation can sometimes be solved very explicitly. For the heat equation, Fourier analysis gives us an operator that advances any initial temperature profile through time. But what if the material generates heat at a rate depending on the current temperature? The evolution is no longer linear, and Fourier modes interact. Duhamel's formula offers a way to use the known linear flow as the foundation of a nonlinear solution.

First recall a familiar equation from calculus. Suppose the rate of change of a quantity equals a fixed multiple of the quantity plus a forcing term. If the forcing were absent, an exponential would describe the evolution. With forcing, the solution consists of the freely evolving initial value plus an integral of the forcing, where each contribution is carried forward from the time it entered. This is variation of constants. Duhamel's formula is the same idea when the exponential is replaced by a semigroup of operators.

For heat flow, think of the initial temperature as a collection of many small heat sources. The linear heat semigroup spreads and attenuates their sharp features. If new heat is added at time s, that addition has only the remaining time, from s to the current time, to spread. We add the effects of all contributions over their times of arrival. The formula is an integral of the heat semigroup applied to the forcing at each earlier time.

Now let the forcing depend on the unknown temperature. For example, imagine a reaction term proportional to temperature squared. Formally the evolution equation is heat diffusion plus a quadratic reaction. Duhamel's formula tells us that the candidate solution at time t is the heat evolution of the initial profile plus the integral of the heat evolution of the square of the candidate at earlier times. The unknown appears on both sides, so the formula becomes a fixed-point problem.

The right function space matters. Suppose the initial data are bounded functions on the whole real line, and we seek a solution bounded uniformly over a short time interval. The heat semigroup does not increase the maximum norm. The square of a function bounded by M is bounded by M squared. Therefore the Duhamel map sends a ball of size M into itself if the initial maximum plus the time interval times M squared stays at most M. Choosing M larger than the initial maximum and time small enough makes that possible.

For uniqueness we compare two candidates. Their squares differ by their difference times their sum, so the nonlinear contribution is controlled by twice M times the difference. The time integral contributes another factor of the interval length. When this product is smaller than one, the Duhamel map is a contraction. The Banach fixed-point theorem constructs a unique bounded mild solution on that short interval.

The word mild does not mean approximate. It means the solution satisfies the integral form of the evolution equation, without requiring all derivatives at the initial moment to exist classically. When the semigroup smooths and the data have suitable regularity, a mild solution may become a classical solution for positive times. But the distinction is useful because the integral equation can make sense for rough initial data that do not belong to the differential operator's domain.

Diffusion is not a guarantee against blow-up. If the initial temperature is a positive constant and the reaction is the square of temperature, then the spatial derivative terms vanish forever. The partial differential equation reduces to the same ordinary differential equation in which a quantity grows at a rate equal to its square. Its solution blows up in finite time. This exact example prevents us from drawing a false conclusion: heat flow smooths spatial variation, but a sufficiently strong positive reaction may still drive unlimited growth.

The method extends far beyond a single reaction term. Schrödinger and wave equations have their own linear propagators. Their nonlinearities are often controlled in Sobolev or spacetime norms rather than by a simple maximum norm. The integral formula still has the same architecture, but the estimates required to show that the map is contractive can be far more delicate.

When reading a semilinear PDE argument, distinguish four layers: a linear propagator; an integral formula for the nonlinear forcing; a function space in which this integral is defined; and an estimate that lets the fixed-point theorem work. Duhamel's formula is the bridge between knowledge of the linear equation and the construction of a nonlinear solution.

## Energy Estimates and Gronwall: Turning Local Calculations into Global Bounds

When a physical system evolves, it may be difficult to compute its exact state at every moment. But perhaps we can calculate something simpler: an energy that measures the overall size of the state. If that energy cannot grow too quickly, we obtain control without solving the equation explicitly. Energy estimates are among the most reusable tools in differential equations.

Begin with a string whose temperature spreads by diffusion and which also has a reaction proportional to its current temperature. Let the ends be held at zero temperature. Multiply the equation by the temperature itself and integrate along the string. The left side becomes half the time derivative of the square-integral of temperature. The diffusion term becomes minus the square-integral of the spatial derivative, after integrating by parts. The boundary term vanishes because the temperature is zero at both ends.

The negative derivative contribution is good news: diffusion dissipates energy. The reaction term may add or remove energy. If the reaction coefficient is bounded above by M, then its contribution is bounded by M times the square-integral of temperature. We therefore obtain a differential inequality for the energy: its rate of change is at most twice M times the energy. We have not solved the PDE, but we have reduced its growth to a one-dimensional inequality.

Gronwall's inequality handles precisely this situation. If a nonnegative quantity grows at a rate bounded by a constant times itself, then it cannot outgrow the corresponding exponential. The proof is short: multiply by the decaying exponential, observe that the product has nonpositive derivative, and compare its values at different times. A more general integral version handles accumulated forcing and time-dependent coefficients.

The resulting estimate says that the L-two size of the temperature is at most its initial L-two size multiplied by an exponential involving the coefficient bound and time. If the reaction coefficient is nonpositive, we can do better: the energy does not increase. If it is positive, the estimate is still useful, because it prevents arbitrarily fast growth on a fixed finite time interval, as long as the coefficient bound remains valid.

This is also a uniqueness argument. Suppose we have two solutions of a linear equation with the same initial data. Subtract their equations. The difference satisfies the same type of energy inequality but starts with zero energy. Gronwall forces its energy to remain zero. The difference vanishes, so the solutions agree. We did not need an explicit Fourier transform or an eigenfunction expansion to establish uniqueness.

For a nonlinear equation, subtracting two solutions produces a difference of nonlinear terms. If the nonlinearity is locally Lipschitz in the function norm and the solutions remain in a bounded region, the difference can often be controlled by a constant times the difference itself. Gronwall again gives continuous dependence and uniqueness. But the bound may hold only while the solutions are known to remain inside that region. This is why local theory and continuation criteria are linked to a priori energy bounds.

There is a subtle danger. The energy we choose might control the L-two size of a function but not its maximum value or its derivatives. A bound in one norm is not automatically a bound in every norm. For a nonlinear term containing derivatives, we may need to differentiate the equation and build a higher-order energy. That calculation can introduce new products and require Sobolev estimates. Energy arguments therefore work together with the function-space tools, not instead of them.

Boundary conditions matter as well. If the string has nonzero boundary flux, integration by parts produces a boundary term, which may inject energy. The simple dissipative estimate cannot be reused without accounting for it. On a moving domain, the changing geometry adds further terms. A careful energy proof records exactly where the boundary contribution goes.

There is also a distinction between stability and decay. An estimate that keeps energy below a growing exponential establishes continuous dependence over finite times, but does not prove that solutions approach zero. To prove decay we need additional inequalities linking energy dissipation to energy itself, such as a Poincaré inequality for a string with fixed ends. This can turn a nonincrease statement into genuine exponential decay.

The core technique is remarkably portable: choose a norm or energy; differentiate it along the evolution; use integration by parts and inequalities to estimate its derivative; and solve the resulting scalar inequality. With that single pattern we can establish bounds, uniqueness, stability and sometimes long-time decay for equations far more complicated than the examples that introduced it.

## Compactness in Space and Time: Passing to a Nonlinear Limit

Suppose we approximate a nonlinear evolution equation with finer and finer grids. Each approximate solution has controlled energy, and the grids are refined until they seem to describe the same physical process. We want to extract an actual solution from this sequence. The difficulty is that an energy bound does not necessarily provide convergence strong enough to pass through nonlinear expressions.

For functions on a bounded spatial domain, a first-order Sobolev bound controls oscillation in a way that can lead to compactness in L two. Under the standard embedding hypotheses, a bounded sequence in H-one has a strongly convergent subsequence in L two. This is the Rellich compactness theorem. It is one of the reasons weak formulations work: a derivative bound can produce strong convergence of the functions even if the derivatives themselves converge only weakly.

Now add time. Our approximate solutions vary both in space and in time. A compactness theorem for spatial snapshots does not automatically give compactness of an entire movie. Consider a single smooth shape multiplied by a rapidly oscillating sine wave in time. Every spatial snapshot belongs to the same one-dimensional span; all spatial derivatives are controlled. But as the time frequency increases, the solutions oscillate too rapidly for a strongly convergent subsequence in spacetime L two. We need control of temporal variation as well.

Aubin–Lions compactness supplies the missing ingredient. We work with three nested spaces. The strongest space, call it X, controls spatial derivatives. It embeds compactly into a middle space B, where we want strong convergence. The middle space embeds continuously into a weaker space Y, where time derivatives can be estimated. We do not demand that the time derivative have the same spatial regularity as the function. It is enough to control it in a weaker space.

A standard PDE choice is X equal to the first-order zero-boundary Sobolev space, B equal to L two, and Y equal to the negative first-order Sobolev space. A sequence bounded in square-integrable time with values in X, whose time derivative is also bounded in square-integrable time with values in Y, has a subsequence converging strongly in square-integrable spacetime L two. The compact spatial embedding and the time-derivative estimate work together.

Why should the time derivative be measured in a negative-order space? Look at the heat equation. The spatial Laplacian of an H-one function may not be an L-two function. But when tested against an H-one function, its action is represented by an integral involving first derivatives. That makes the Laplacian a well-defined element of the dual of H-one. So the equation can bound the time derivative in H minus one even when no classical second derivative exists.

Once we have strong convergence in L two, we can pass through certain nonlinearities. If the nonlinearity is Lipschitz on a uniformly bounded range, the difference between the nonlinear outputs is controlled by the difference between the inputs. Strong convergence makes that difference vanish. For polynomial nonlinearities and other growth conditions, the argument may need additional integrability bounds or interpolation. We must not assume that every nonlinear term passes through every weak limit.

Consider the simpler problem of approximating a reaction-diffusion equation by finite-dimensional modes. Energy estimates bound the spatial H-one norm of each approximation over time. The equation bounds its temporal derivative in a weaker space. Aubin–Lions produces a strongly convergent subsequence in L two, allowing us to pass to the limit in a bounded or suitably controlled reaction term. A weak limit then becomes a genuine solution, provided all terms in the equation and the initial condition are handled correctly.

There are two illuminating failure cases. On the whole real line, translating a fixed pulse farther away retains its H-one size but prevents strong L-two convergence. Spatial compactness is lost because the domain is not bounded. Separately, a fixed spatial shape oscillating faster and faster in time defeats spacetime compactness unless we control temporal variation. Together, these examples show why the theorem requires both types of information.

This way of proving existence is different from a contraction argument. A contraction gives a unique fixed point in a setting with strong Lipschitz control. A compactness argument constructs limit points of approximations and may establish existence even when the nonlinearity is not Lipschitz enough for a contraction. Uniqueness may require an additional estimate. The two methods complement each other, and a PDE course should teach both.

## The Direct Method and Monotone Operators: Nonlinear Existence Without a Contraction

Not every nonlinear problem can be solved by making an iteration contract. Some nonlinearities are too steep, some maps are not sufficiently Lipschitz, and some natural solution spaces do not support the desired fixed-point estimate. There is another strategy: instead of repeatedly applying a map, find the state that minimizes a suitable energy.

Imagine a stretched elastic string, fixed at both ends, under an external load. Its potential energy includes a term that penalizes slopes. A large gradient costs energy, so the string resists sharp bends. If the string also experiences a nonlinear restoring force, we can add a positive quartic term to the potential. Finally the load contributes a term that rewards movement in the direction of the applied force. The equilibrium should minimize the combined energy.

Why is a minimum likely to exist? First we need a lower bound. Without one, the energy could keep decreasing without reaching a finite value. For a string fixed at both ends, Poincaré's inequality controls its overall size by the size of its derivative. Thus a sufficiently positive quadratic derivative term eventually dominates the linear work done by a fixed square-integrable load. The quartic term is also nonnegative. As the Sobolev norm grows, the energy grows. We call this coercivity.

Choose a sequence of string shapes whose energies approach the infimum. Coercivity prevents the sequence from running off to infinite Sobolev norm. Because this Sobolev space is reflexive, a bounded sequence has a weakly convergent subsequence. We now have a candidate limiting shape. The next task is to show that the limit does not have larger energy than the values approaching the infimum. This is weak lower semicontinuity, supplied here by convexity of the derivative and quartic terms and continuity of the load pairing.

If those ingredients hold, the limit actually minimizes the energy. We have constructed an equilibrium without solving a differential equation explicitly. The differential equation emerges when we vary the minimizer slightly and require that the first variation of energy vanish. The quadratic gradient term becomes the negative second derivative in the weak sense; the quartic potential contributes a cubic restoring force; and the external load appears on the other side. We arrive at a nonlinear boundary-value problem for the string.

There is also a way to understand uniqueness. The cubic function is increasing. If two candidate solutions are subtracted and the difference equation is tested against their difference, the gradient term is nonnegative. The cubic difference times the difference of its arguments is also nonnegative. The sum can vanish only when the two candidates are identical, once the zero boundary condition is imposed. This is a monotonicity argument, not a contraction argument.

Monotonicity generalizes the simple fact that an increasing scalar function preserves order. A nonlinear operator is monotone when the difference between its outputs has a nonnegative dual pairing with the difference between its inputs. Strict monotonicity may give uniqueness. Coercivity and suitable continuity properties can give existence by theorems associated with Minty and Browder. These theorems provide a general framework for nonlinear elliptic equations and convex optimization.

But convexity matters. A nonconvex energy can have multiple local minima and saddle points. A minimizing sequence might approach a global minimum, yet a different stationary point could also solve the Euler–Lagrange equation. Critical points are not automatically global minimizers. We should keep separate the claims of existence of a minimizer, uniqueness of a minimizer, and existence of arbitrary solutions to the stationary equation.

There is another distinction between the weak and classical formulations. A Sobolev minimizer initially satisfies an integral identity against test functions. Extra regularity is needed before we can interpret its second derivative pointwise. In a one-dimensional string problem, that additional smoothness is often obtainable for smooth loads. In rough domains or with rough coefficients, it may fail. The variational construction itself does not require classical second derivatives from the outset.

The direct method is a model of existence by compactness: bounded minimizing sequences, weak convergence, and lower semicontinuity. A fixed-point theorem is a model of existence by contraction: a map that repeatedly improves guesses. Energy estimates and monotonicity help establish uniqueness and stability. Together these approaches form a basic toolkit for understanding nonlinear equations, even when no closed-form solution is available.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Semigroups and Generators: Solving Time Evolution Beyond Self-Adjoint Operators

**Track:** Analysis from First Principles. **Background:** bounded operators, functional calculus and weak derivatives. **Central question:** How do we describe a continuously evolving system when its generator is unbounded or not self-adjoint?

#### Mathematical companion (not spoken)

A \(C_0\)-semigroup \((T(t))_{t\ge0}\) on Banach X satisfies \(T(0)=I\), \(T(t+s)=T(t)T(s)\), and \(\lim_{t\downarrow0}T(t)x=x\) for every x. Its generator is
\[Ax=\lim_{h\downarrow0}\frac{T(h)x-x}{h},\qquad D(A)=\left\{x:\text{limit exists in }X\right\}.\]

Translation on \(L^2(\mathbb R)\): \((T(t)f)(x)=f(x-t)\) for \(t\ge0\) defines an isometric strongly continuous semigroup with generator \(A=-\partial_x\) on \(H^1(\mathbb R)\). This is not norm continuous: \(\|T(t)-I\|=2\) for every \(t>0\), as seen in the Fourier representation \(e^{-it\xi}\).

For a strongly continuous contraction semigroup, a dense closed generator satisfies the Hille–Yosida resolvent bounds \((0,\infty)\subset\rho(A)\) and \(\|(\lambda I-A)^{-1}\|\le1/\lambda\) for \(\lambda>0\); conversely the stated domain and resolvent hypotheses generate a contraction semigroup. For Hilbert spaces the Lumer–Phillips theorem equivalently characterizes maximal dissipativity.

For \(f\in L^1([0,T];X)\), the integral formula
\[u(t)=T(t)u_0+\int_0^t T(t-s)f(s)\,ds\]
defines a mild solution of \(u'=Au+f\), with strong differentiability requiring extra regularity.

##### Exercises with answers

1. **Shift law.** Show \(T(s)T(t)f(x)=f(x-s-t)\). **Answer:** Apply the translation definition twice.
2. **Shift generator.** For differentiable compactly supported f, compute the derivative at zero. **Answer:** \(Af=-f'\).
3. **Forced scalar.** Solve \(u'=-u+1\), \(u(0)=0\). **Answer:** \(u(t)=1-e^{-t}\), also given by the semigroup integral.

##### Reading and source notes

- [Mathew A. Johnson, Introduction to Semigroup Methods](https://matjohn.ku.edu/Notes/Math951Notes_Ch6.pdf)
- [MIT OpenCourseWare, 18.102 Introduction to Functional Analysis, lecture notes](https://ocw.mit.edu/courses/18-102-introduction-to-functional-analysis-spring-2021/pages/lecture-notes-and-readings/)
- [John K. Hunter, Notes on Partial Differential Equations](https://www.math.ucdavis.edu/~hunter/m218a_09/pde_notes.pdf)

### Sectorial Operators: Why Diffusion Smooths Immediately

**Track:** Analysis from First Principles. **Background:** L-p spaces, basic Hilbert spaces and weak derivatives as introduced earlier in this course. **Central question:** What assumptions make this construction rigorous?

#### Mathematical companion (not spoken)

Let \(A=\Delta\) with domain \(H^2(\mathbb R^d)\) on \(L^2(\mathbb R^d)\). Then \(T(t)=e^{t\Delta}\) has Fourier multiplier \(e^{-t|\xi|^2}\), and \(\|T(t)\|_{2\to2}\le1\). For \(\mathrm{Re}\,\lambda>0\), \(\|R(\lambda,A)\|\le(\mathrm{Re}\,\lambda)^{-1}\). The sharper sectorial estimates concern sectors bounded away from the negative real axis; \(A\) generates an analytic semigroup.

For \(t>0\), \(\|\Delta T(t)\|_{2\to2}=\sup_{r\ge0}r^2e^{-tr^2}=1/(et)\). More generally \(\|(-\Delta)^{\alpha/2}T(t)\|_{2\to2}\le C_\alpha t^{-\alpha/2}\). These estimates do not assert \(u_0\in D(\Delta)\).

By contrast \((S(t)f)(x)=f(x+t)\) is a strongly continuous group on \(L^2(\mathbb R)\) with generator \(f'\) on \(H^1\); its Fourier multiplier has modulus one, so it does not smooth initial data.

One common convention calls \(-A\) sectorial of angle less than \(\pi/2\) when \(A\) generates a bounded analytic semigroup. Always specify sign and sector convention in statements.

##### Exercises with answers

1. **Frequency decay.** Compare frequencies 1 and 5 at time 1 for the heat equation. **Answer:** Multipliers are \(e^{-1}\) and \(e^{-25}\), respectively.
2. **Optimization.** Find the maximum of \(s e^{-ts}\) over \(s\ge0\). **Answer:** At \(s=1/t\), with value \(1/(et)\).
3. **Counterexample.** Does translation smooth a step? **Answer:** No, the jump is translated but retained.

##### Reading and source notes

- [Engel and Nagel, One-Parameter Semigroups for Linear Evolution Equations](https://www.math.uni-tuebingen.de/de/forschung/agfa/members/engel-nagel_one-parameter-semigroups.pdf/@@download/file/engel-nagel_one-parameter-semigroups.pdf)
- [John K. Hunter, Notes on Nonlinear Evolution Equations](https://www.math.ucdavis.edu/~hunter/notes/nonlinev.pdf)

### Banach Fixed Points and Picard Iteration: Constructing a Solution

**Track:** Analysis from First Principles. **Background:** L-p spaces, basic Hilbert spaces and weak derivatives as introduced earlier in this course. **Central question:** What assumptions make this construction rigorous?

#### Mathematical companion (not spoken)

Banach's contraction principle: if \((X,d)\) is complete and \(F:X\to X\) satisfies \(d(Fx,Fy)\le qd(x,y)\) with \(0\le q<1\), then F has a unique fixed point \(x_*\), and \(d(F^nx,x_*)\le q^n d(x,x_*)\). For a contraction on a closed subset \(B\subset X\), use completeness of B.

For \(u'=u^2,\ u(0)=1\), put \(X=C([0,T])\) and \((Fu)(t)=1+\int_0^tu(s)^2ds\). On \(B=\{u:\|u\|_\infty\le2\}\), \(\|Fu\|_\infty\le1+4T\) and \(\|Fu-Fv\|_\infty\le4T\|u-v\|_\infty\). With \(T=1/8\), the ball is invariant and F is a contraction. The exact maximal solution is \(u(t)=(1-t)^{-1}\), defined for \(t<1\).

Picard iterates: \(u_0=1\); \(u_1=1+t\); \(u_2=1+t+t^2+t^3/3\). Do not confuse these partial approximants with exact power-series truncations at every stage.

##### Exercises with answers

1. **Contraction factor.** For T equal to one eighth, what is the Lipschitz factor of F on the radius-two ball? **Answer:** At most one half.
2. **Second iterate.** Starting from \(u_0=1\), compute \(u_1\) and \(u_2\). **Answer:** \(u_1=1+t\) and \(u_2=1+t+t^2+t^3/3\).
3. **Global behavior.** Does local existence imply the solution survives past time one? **Answer:** No; the exact solution \(1/(1-t)\) blows up at time one.

##### Reading and source notes

- [John K. Hunter, Notes on Nonlinear Evolution Equations, nonlinear existence](https://www.math.ucdavis.edu/~hunter/notes/nonlinev.pdf)
- [MIT OpenCourseWare, Introduction to Functional Analysis](https://ocw.mit.edu/courses/18-102-introduction-to-functional-analysis-spring-2021/)

### Duhamel’s Formula: Solving a Nonlinear Equation with a Linear Flow

**Track:** Analysis from First Principles. **Background:** L-p spaces, basic Hilbert spaces and weak derivatives as introduced earlier in this course. **Central question:** What assumptions make this construction rigorous?

#### Mathematical companion (not spoken)

Let \(A\) generate a \(C_0\)-semigroup \(T(t)\) on a Banach space X. A mild solution of \(u'(t)=Au(t)+F(u(t))\) satisfies
\[u(t)=T(t)u_0+\int_0^tT(t-s)F(u(s))\,ds,\]
where the integral is a Bochner integral in X. Local existence follows if F is locally Lipschitz in the chosen X and the semigroup is locally bounded.

On X = \(BUC(\mathbb R^d)\), the bounded *uniformly continuous* functions, the heat semigroup is \(C_0\) and is L-infinity contractive. For \(F(u)=u^2\), fix \(M>\|u_0\|_\infty\) and B = \(\{u\in C([0,T];BUC): \sup_t\|u(t)\|_\infty\le M\}\). Then
\[\|\Phi u\|\le\|u_0\|_\infty+TM^2,\quad \|\Phi u-\Phi v\|\le2MT\|u-v\|.\]
Choose T so both invariance and strict contraction hold. **Caution:** the heat semigroup is not strongly continuous on all of \(L^\infty(\mathbb R^d)\) in the supremum norm; using BUC avoids this issue.

For constant \(u_0=c>0\), the exact spatially constant solution is \(u(t,x)=c/(1-ct)\), \(t<1/c\), showing finite-time reaction blow-up.

##### Exercises with answers

1. **Semigroup input.** Where does the forcing at time s enter the solution at time t? **Answer:** Through \(T(t-s)F(u(s))\).
2. **Contraction criterion.** What bound must be strictly below one for the quadratic reaction in the radius-M ball? **Answer:** \(2MT\).
3. **Counterexample.** Does spatial diffusion guarantee global existence for \(u_t=\Delta u+u^2\)? **Answer:** No; constant positive solutions blow up at \(1/c\).

##### Reading and source notes

- [John K. Hunter, Notes on Nonlinear Evolution Equations](https://www.math.ucdavis.edu/~hunter/notes/nonlinev.pdf)
- [Engel and Nagel, One-Parameter Semigroups](https://www.math.uni-tuebingen.de/de/forschung/agfa/members/engel-nagel_one-parameter-semigroups.pdf/@@download/file/engel-nagel_one-parameter-semigroups.pdf)

### Energy Estimates and Gronwall: Turning Local Calculations into Global Bounds

**Track:** Analysis from First Principles. **Background:** L-p spaces, basic Hilbert spaces and weak derivatives as introduced earlier in this course. **Central question:** What assumptions make this construction rigorous?

#### Mathematical companion (not spoken)

For smooth \(u\) on \((0,L)\) solving \(u_t=u_{xx}+a(t,x)u\) with homogeneous Dirichlet endpoints, define \(E(t)=\frac12\int_0^L|u|^2dx\). Integration by parts yields
\[E'(t)=-\int_0^L|u_x|^2dx+\int_0^La|u|^2dx\le2ME(t)\]
if \(a(t,x)\le M\) almost everywhere. Thus \(E(t)\le e^{2Mt}E(0)\). For a complex solution use the real part of the inner product.

Gronwall integral form: if nonnegative \(y(t)\le a(t)+\int_0^tb(s)y(s)ds\), with \(a\) nondecreasing and \(b\ge0\) integrable, then \(y(t)\le a(t)\exp(\int_0^tb)\). Other versions allow forcing and varying a.

If \(a\le0\) and \(u(0)=0\) at endpoints, Poincaré gives \(\int|u_x|^2\ge(\pi/L)^2\int|u|^2\), hence \(E(t)\le E(0)e^{-2\pi^2t/L^2}\). For weak solutions, justify by Galerkin approximation or an energy identity under standard temporal regularity assumptions.

##### Exercises with answers

1. **Heat energy.** For zero reaction, is E nonincreasing? **Answer:** Yes, \(E'=-\int|u_x|^2\le0\).
2. **Poincaré decay.** For a unit interval with Dirichlet endpoints and no reaction, what decay bound holds? **Answer:** \(E(t)\le E(0)e^{-2\pi^2t}\).
3. **Uniqueness.** What happens if the difference of two solutions starts at zero and satisfies \(E'\le 10E\)? **Answer:** Gronwall gives E identically zero.

##### Reading and source notes

- [John K. Hunter, Notes on Nonlinear Evolution Equations, energy estimates](https://www.math.ucdavis.edu/~hunter/notes/nonlinev.pdf)
- [MIT OpenCourseWare, Introduction to Functional Analysis](https://ocw.mit.edu/courses/18-102-introduction-to-functional-analysis-spring-2021/)

### Compactness in Space and Time: Passing to a Nonlinear Limit

**Track:** Analysis from First Principles. **Background:** L-p spaces, basic Hilbert spaces and weak derivatives as introduced earlier in this course. **Central question:** What assumptions make this construction rigorous?

#### Mathematical companion (not spoken)

Let \(X\hookrightarrow\hookrightarrow B\hookrightarrow Y\) denote a compact embedding followed by a continuous embedding of Banach spaces. A standard Aubin–Lions result states: for \(1\le p<\infty\), a family bounded in \(L^p(0,T;X)\) with distributional time derivative bounded in \(L^q(0,T;Y)\), \(q>1\), is relatively compact in \(L^p(0,T;B)\) under the usual assumptions; many refinements cover endpoint cases.

On a bounded Lipschitz \(\Omega\), take \(X=H^1_0(\Omega)\), \(B=L^2(\Omega)\), \(Y=H^{-1}(\Omega)\). If
\[\sup_n\|u_n\|_{L^2(0,T;H^1_0)}<\infty,\quad \sup_n\|\partial_tu_n\|_{L^2(0,T;H^{-1})}<\infty,\]
then some subsequence converges strongly in \(L^2(0,T;L^2)\).

Failure without time control: \(u_n(t,x)=\sin(nt)\phi(x)\) on a fixed interval \(0<t<2\pi\) with \(\phi\ne0\in H^1_0(\Omega)\) is uniformly spatially bounded but not precompact in spacetime L-two; \(\partial_tu_n=n\cos(nt)\phi\) grows in any fixed nonzero norm of \(\phi\).

##### Exercises with answers

1. **Triple of spaces.** Name the spaces for the common parabolic PDE application. **Answer:** \(H^1_0(\Omega)\hookrightarrow\hookrightarrow L^2(\Omega)\hookrightarrow H^{-1}(\Omega)\).
2. **Time oscillation.** Why does \(\sin(nt)\phi(x)\) defeat a spatial-only compactness argument? **Answer:** Its temporal frequency diverges, so it lacks strong compactness in spacetime L-two.
3. **Nonlinearity.** Does weak L-two convergence alone guarantee convergence of squares in L-one? **Answer:** No; strong L-two convergence does, by factorization and Cauchy–Schwarz when norms remain bounded.

##### Reading and source notes

- [John K. Hunter, Notes on Nonlinear Evolution Equations, compactness arguments](https://www.math.ucdavis.edu/~hunter/notes/nonlinev.pdf)
- [Princeton MAT520 Functional Analysis lecture notes](https://web.math.princeton.edu/~js129/PDFs/teaching/MAT520_fall_2025/MAT520_Lecture_Notes.pdf)

### The Direct Method and Monotone Operators: Nonlinear Existence Without a Contraction

**Track:** Analysis from First Principles. **Background:** L-p spaces, basic Hilbert spaces and weak derivatives as introduced earlier in this course. **Central question:** What assumptions make this construction rigorous?

#### Mathematical companion (not spoken)

On \(I=(0,1)\) and \(f\in L^2(I)\), define \(J:H^1_0(I)\to\mathbb R\) by
\[J(u)=\frac12\int_I|u'|^2dx+\frac14\int_Iu^4dx-\int_Ifu\,dx.\]
In one dimension \(H^1_0(I)\hookrightarrow L^4(I)\). Poincaré and Young imply coercivity. The convex terms are weakly lower semicontinuous, and the load term is weakly continuous. By reflexivity and the direct method, J has a minimizer. Its first variation gives
\[\int_Iu'v'\,dx+\int_Iu^3v\,dx=\int_Ifv\,dx\qquad(v\in H^1_0(I)),\]
which is the weak form of \(-u''+u^3=f\) with zero trace.

If u and w solve the same problem, subtract and test by u-w:
\[\int_I|u'-w'|^2dx+\int_I(u^3-w^3)(u-w)\,dx=0.\]
Both integrands are nonnegative, so u=w. More generally an operator \(A:X\to X^*\) is monotone if \(\langle Au-Av,u-v\rangle\ge0\). The Minty–Browder theory supplies nonlinear existence under reflexivity, coercivity, monotonicity and suitable hemicontinuity assumptions; these hypotheses must not be omitted.

##### Exercises with answers

1. **First variation.** What is the derivative of \(\frac14\int u^4\) in direction v? **Answer:** \(\int u^3v\).
2. **Monotonicity.** Why is \((a^3-b^3)(a-b)\ge0\) for real a,b? **Answer:** \((a-b)^2(a^2+ab+b^2)\ge0\).
3. **Counterexample.** Does every critical point of a nonconvex energy minimize it? **Answer:** No; a local maximum or saddle can also have zero first derivative.

##### Reading and source notes

- [John K. Hunter, Notes on Nonlinear Evolution Equations, weak and variational problems](https://www.math.ucdavis.edu/~hunter/notes/nonlinev.pdf)
- [MIT OpenCourseWare, Introduction to Functional Analysis, weak compactness](https://ocw.mit.edu/courses/18-102-introduction-to-functional-analysis-spring-2021/)
