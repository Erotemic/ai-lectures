# From Random Walks to Brownian Motion: A Limit That Becomes a Process

**Track:** Probability, Measure, and Statistical Reasoning  
**Lecture:** 015000  
**Preparation:** Independent random variables, variance, the normal approximation, and basic continuous functions.  
**Companion:** Scaling, Gaussian increments, functional convergence, and exercises.

<!-- BEGIN SPOKEN LECTURE -->

Imagine a particle on an infinitely long line. At every tick of a clock, it moves one unit right or one unit left, with equal probability, independently of its previous moves. The particle's trajectory is a jagged path, made entirely of jumps. After a hundred steps, its average displacement is zero, but it is unlikely to be exactly where it started. The mean says the motion has no preferred direction; the variance tells us how far it typically wanders.

Call each step a random sign, plus one or minus one with equal probability. Add the first n signs to get the particle's position after n steps. The expected position is zero. Each step has variance one; because the steps are independent, the variance of their sum is n. The typical magnitude of the displacement therefore grows like the square root of n, not like n. A thousand steps need not move the particle a thousand units away. Most of the movement cancels in the sum.

Now suppose our clock ticks more and more quickly while the physical distance of each step becomes smaller. What continuous motion should emerge from this refinement? If we shrink the step length but keep the clock rate unchanged, movement freezes. If we make the steps very frequent without shrinking their length, the fluctuations explode. We need to balance time and space so variance over a fixed physical time remains finite and nonzero.

Let each step have size h, while each tick lasts h squared units of time. In one unit of physical time there are about one over h squared steps. Their displacement variance is that number times h squared, approximately one. Therefore after physical time t the variance is approximately t. As h approaches zero, the individual jumps vanish, but the accumulated fluctuations remain. This balance of distance squared against time is called diffusive scaling.

For a single fixed time, the central limit theorem explains much of the result. The sum of many independent centered steps, divided by the square root of their number, approaches a normal distribution. With our scaling, the particle's position at time t approaches a normal random variable with mean zero and variance t. But this only describes one time slice. A continuous-time stochastic process is not specified by saying what distribution the position has at each time. We must also explain how positions at different times fit together.

The full limiting object is standard Brownian motion, also called a Wiener process. It starts at zero. It has continuous sample paths. It has independent increments: movement over disjoint time intervals is independent. An increment over an interval of length t has a normal distribution with mean zero and variance t, regardless of when that interval begins. These properties determine its probability law. The process is a random continuous curve, not a sequence of independent normal draws at each time.

If you simply sampled an independent normal position at every rational time, you would almost certainly fail to obtain a continuous curve with the Brownian increment structure. Temporal dependence matters. Brownian motion at time two includes everything that happened by time one plus a new increment from one to two. As a result, for times s and t, the covariance of Brownian positions is the smaller of the two times. Two positions are correlated because they share the same earlier motion, even though their nonoverlapping increments are independent.

There is a simple computation behind this. For s less than t, write B at time t as B at time s plus the increment after s. That increment is independent of B at time s and has mean zero. So the covariance of B at s with B at t equals the variance of B at s, which is s. That proves the minimum-of-times covariance formula without appealing to an abstract theorem. It is one reason covariance matrices and stochastic processes belong in the same mathematical curriculum.

What does the word convergence mean when an entire random path approaches Brownian motion? At a handful of chosen times, we can discuss convergence of joint distributions. A stronger statement, known as an invariance principle or functional central limit theorem, says the properly scaled random-walk paths, with a suitable interpolation between their steps, converge in distribution as random continuous functions on a fixed time interval. This is a theorem about probability laws on a space of paths. It is not a claim that one particular random walk drawn today gets uniformly close to one particular Brownian path drawn independently tomorrow.

For the symmetric independent steps we chose, the functional convergence theorem is valid under the diffusive scaling. Extensions exist for other centered increments with finite positive variance, with the variance determining the time or space scale. But not every microscopic noise model leads to Brownian motion. Heavy-tailed increments can have different scaling limits; strongly dependent steps may produce processes with different temporal structure. The limit follows from assumptions, not from the visual impression that a path looks irregular.

Brownian sample paths have another striking property. Although they are continuous with probability one, they are nowhere differentiable with probability one. Continuity says the path has no jumps; differentiability would require an ordinary instantaneous velocity. Brownian motion has no such classical velocity. The path keeps fluctuating on every time scale. This is not a contradiction: ordinary continuity never promised the existence of a tangent.

The statistical reason is already visible in the increment scaling. Over a small interval of length delta t, a Brownian increment typically has size proportional to the square root of delta t. Divide that increment by delta t to form an attempted velocity, and its typical magnitude grows like one over the square root of delta t. This heuristic is not by itself a full proof of nowhere differentiability, but it shows why a finite classical velocity is the wrong expectation.

We can calculate something else without needing pathwise derivatives. Square the increments and sum over a partition of a fixed interval. Because the variance of an increment equals the length of that interval, the expected sum of squared increments is the total elapsed time. With increasingly fine partitions, the realized squared-increment sum converges to elapsed time in an appropriate probabilistic sense, and for standard deterministic refining partitions it can be sharpened. This is Brownian quadratic variation. An ordinary differentiable curve with bounded derivative over a finite interval would instead have vanishing quadratic variation as the mesh shrinks.

Quadratic variation is not a technical curiosity; it changes the chain rule. For a smooth ordinary trajectory x of t, we would expect a small change in x squared to be approximately twice x times the change in x, with the squared increment negligible compared with the time step. For Brownian motion, the accumulated squared increments do not disappear. Their total produces an additional elapsed-time term. This is the seed of Ito calculus, where the stochastic chain rule contains a second-derivative correction.

Brownian motion is a useful model for random forcing, particle diffusion, fluctuating prices under simplified assumptions, and the cumulative effect of many small independent disturbances. But it is not a literal model of every physical motion. A real particle has inertia and interacts with a medium at finite time scales; a Brownian idealization describes a regime in which sufficiently fine microscopic behavior has been averaged into a continuous random process. Deciding whether that approximation fits an experiment is a modeling question.

It helps to distinguish three different mathematical objects. A single random-walk trajectory is a finite or countable sequence of random positions. Brownian motion is a continuous-time process with a law on entire paths. The probability density of a particle's position at time t is a deterministic function of position and time. The density changes smoothly according to a diffusion equation, even though an individual Brownian path is almost surely nowhere differentiable. That contrast is one of the deepest connections between probability and partial differential equations.

A final practical point: simulating Brownian motion at a grid of times does not create an exact full continuous path. A correct simulation of the grid values draws independent normal increments with variance equal to each time interval's length, then sums them. Interpolating with straight line segments produces a visual approximation, not a differentiable version of true Brownian motion at arbitrarily fine scales. Refining the grid reveals more fluctuation; it does not reveal a smooth underlying velocity.

We began with a childlike walk, step right or step left. The square-root growth of displacement forced a particular relation between space and time. The central limit theorem explained positions at a time, and the invariance principle explained the whole random path. The result is a process continuous in time but fundamentally different from a smooth deterministic motion. It gives us the proper random object from which diffusion equations and stochastic differential equations can be developed.

<!-- END SPOKEN LECTURE -->

## Mathematical companion

Let \(\xi_i\) be independent random signs with \(P(\xi_i=1)=P(\xi_i=-1)=1/2\). Define \(S_n=\sum_{i=1}^n\xi_i\). Then \(E[S_n]=0\), \(\operatorname{Var}(S_n)=n\). For \(h>0\), define the interpolated process \(X_h(t)\) by joining points \((kh^2,h S_k)\) linearly. On fixed \([0,T]\), the functional CLT yields \(X_h\Rightarrow B\) in \(C([0,T])\) as \(h\to0\), with \(B\) standard Brownian motion. This is weak convergence of path distributions, not pointwise convergence under arbitrary coupling.

Properties: \(B_0=0\); for \(s<t\), \(B_t-B_s\sim N(0,t-s)\); disjoint increments independent; paths almost surely continuous; \(\operatorname{Cov}(B_s,B_t)=\min(s,t)\). For a deterministic partition \(0=t_0<\cdots<t_n=T\), the sum \(\sum_i(B_{t_{i+1}}-B_{t_i})^2\) tends to \(T\) in \(L^2\) when the mesh goes to zero.

**Diffusion-scale variant.** With step size \(h\) every \(\Delta t=h^2/(2D)\), \(\operatorname{Var}(X_t)\approx2Dt\). The limiting process is \(\sqrt{2D}\,B_t\) and its density solves \(p_t=D p_{xx}\), under suitable initial/boundary conditions.

### Exercises and answers

1. **Scale.** Why take a time step proportional to the square of the spatial step? **Answer:** About \(1/h^2\) steps occur per unit time, making total variance \((1/h^2)h^2\) finite.
2. **Covariance.** What is \(\operatorname{Cov}(B_2,B_5)\)? **Answer:** Two.
3. **Paths versus marginals.** Do the distributions of \(X_t\) at each individual t fully determine the path law? **Answer:** Not in general; joint distributions and regularity are also needed.
4. **Velocity.** Can one obtain Brownian velocity by refining finite-difference quotients? **Answer:** Not as an ordinary sample-path derivative; Brownian paths are almost surely nowhere differentiable.

### Reading and attribution

- MIT OpenCourseWare, *Theory of Probability* (18.175), weak convergence and stochastic process materials: https://ocw.mit.edu/courses/18-175-theory-of-probability-spring-2014/pages/lecture-slides/.
- Billingsley, *Convergence of Probability Measures*, second edition, for the path-space perspective.
- Levin and Peres, *Markov Chains and Mixing Times*, second edition, for discrete random-walk and Markov-chain foundations: https://pages.uoregon.edu/dlevin/MARKOV/.
- The scaling argument is an original exposition of standard probability results.
