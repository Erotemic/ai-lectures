# How Random Walks Become the Heat Equation

**Track:** Probability, Measure, and Statistical Reasoning  
**Lecture:** 033000  
**Preparation:** Random walks, basic derivatives, conditional probability, and finite differences.  
**Companion:** A discrete master equation, diffusive scaling, heat kernel, and graph generators.

<!-- BEGIN SPOKEN LECTURE -->

A drop of dye spreads through a still fluid. If you look at the concentration on a large scale, it evolves smoothly: sharp peaks flatten, and dye spreads from crowded regions into less crowded ones. If you follow individual molecules, however, each moves through a complicated succession of random collisions. How can a deterministic equation for concentration emerge from random microscopic motion?

We can see the mechanism with an idealized random walk on a line of evenly spaced sites. Let the distance between neighboring sites be h. Every interval of length delta t, a particle moves left or right one site, each with probability one half. Let p at site j and time step n be the probability that the particle occupies that site. The probability of being at j one tick later is half the probability of coming from j minus one, plus half the probability of coming from j plus one.

This is already a deterministic equation. Although one particle's movement is random, the probability distribution evolves according to a fixed linear rule. Rewrite the change in p as half the difference between the sum of the neighbor probabilities and twice the current probability. The expression inside those parentheses is a discrete second difference, a finite-difference approximation to a second spatial derivative. The random walk has produced the algebra of diffusion before we have mentioned temperature, heat, or any physical constitutive law.

To connect the discrete recurrence to a continuous equation, divide both sides by delta t. Multiply and divide the discrete second difference by h squared. If h and delta t shrink together while the ratio h squared divided by twice delta t approaches a positive constant D, the resulting equation has the form: the time derivative of concentration equals D times its second spatial derivative. This is the one-dimensional heat equation, also called the diffusion equation. The scaling coefficient D tells us how quickly spreading occurs.

Notice the distinction between an exact identity and a limiting approximation. The discrete master equation is exact for the specified random walk. The continuous heat equation emerges under a scaling limit and assumptions ensuring sufficient convergence. Merely replacing difference symbols with derivatives does not prove convergence for every initial condition or boundary treatment. The derivation explains why the equation is natural; establishing a precise limit requires estimates and a specified topology of convergence.

What does the equation predict? If all probability begins concentrated at the origin on the infinite line, the solution at positive time t is a Gaussian density with mean zero and variance two D t. It has a bell-shaped profile that broadens as the square root of t. This agrees with the diffusive scaling of random-walk displacement. The Gaussian is not a separate coincidence. It is the position density of the scaled Brownian motion that arises as the random-walk limit.

Let's derive the coefficient without solving a differential equation. Each discrete step has variance h squared. In physical time t, there are roughly t divided by delta t steps, so the total position variance is approximately t h squared divided by delta t. Under the scaling relation, that becomes two D t. On the continuous side, the Gaussian heat kernel has exactly that variance. The variance computation and the differential equation determine the same spreading speed from two directions: microscopic random steps and macroscopic concentration.

Mass conservation is another bridge. Sum the probabilities over all lattice sites. The recurrence simply redistributes probability to neighbors, so the sum stays one. Integrate a diffusion density over all space, assuming sufficient decay so boundary terms vanish. The time derivative of total mass is D times the integral of its second derivative, which reduces to a boundary flux and vanishes on the whole line. Total mass is constant. On a bounded domain we must specify boundary behavior. A reflecting boundary has no outward probability flux; an absorbing boundary allows probability to leave the system when a particle is killed or removed. The physical boundary condition is not determined by the differential operator alone.

The language of flux makes this clear. A concentration gradient means one side has more material than the other. Fick's law models the flux as proportional to the negative concentration gradient. Combine flux with local mass conservation, and the same heat equation follows. This is a different modeling route: instead of averaging a random walk, we postulate a constitutive relationship between flux and gradient. Both descriptions agree under conditions where microscopic random motion produces Fickian diffusion.

What changes on a network rather than a straight line? Suppose the particle moves continuously in time among vertices of a finite undirected graph. Give every edge a symmetric transition rate kappa. At a vertex, each incident edge independently offers the possibility of a jump with rate kappa; the total departure rate is degree times kappa. The probability at a vertex decreases as particles leave through its incident edges and increases as particles arrive along the edges from neighbors.

Write the graph Laplacian L as degree matrix minus adjacency matrix. The probability vector then evolves according to time derivative equal to negative kappa times L times the probability vector. This graph heat equation is the finite-dimensional cousin of the spatial heat equation. For a graph with symmetric rates, its total probability is conserved because the Laplacian's rows and columns sum to zero. If the graph is connected, the constant vector is its zero-eigenvalue direction, and every other eigenvalue is positive. Thus all nonconstant modes decay with time.

There is a subtle but important choice of random walk here. The continuous-time process that assigns the same jump rate to every undirected edge has a uniform stationary distribution on a connected finite graph. A different, very common discrete-time walk chooses a neighboring vertex uniformly each step. That discrete-time chain has a stationary distribution proportional to vertex degree. They use the same graph, but different transition rules. It would be wrong to transfer the stationary distribution of one process to the other without checking the definition.

Try a three-vertex path: left, middle, right, with edges only between neighboring vertices. The graph Laplacian has degrees one, two, one on its diagonal and negative ones at adjacent off-diagonal entries. Its eigenvalues are zero, one, and three. A probability difference between left and right decays with an exponential rate proportional to one. A sharper imbalance concentrated at the middle decays with rate proportional to three. The constant mode remains. This simple computation shows how eigenvalues turn a diffusion process into a collection of independent decay rates.

That statement depends on symmetry. For directed graphs or nonsymmetric transition rates, the generator need not be a symmetric Laplacian, and its spectral theory is more complicated. Real diffusion on irregular spatial grids may require geometry-aware weights. The lesson is not that every network is an ordinary undirected graph. It is that a conservative local exchange rule produces a linear operator, and the operator's structure controls how large-scale variation relaxes.

There is also a connection to partial differential equations that goes beyond probability distributions. The heat equation can describe temperature, chemical concentration, or other fields that spread through local exchange. For temperature, the physical coefficient depends on conductivity and heat capacity. A mathematical density and a physical temperature obey similar equations for different reasons, with different units and boundary interactions. Reusing a differential operator does not identify every physical variable with a probability density.

The random-walk derivation teaches an essential modeling pattern. A microscopic rule tells us where material can move and how often. Conservation turns that rule into an evolution equation. Scaling identifies which combinations of space and time survive in a continuum limit. Spectral analysis explains how deviations from equilibrium disappear. The same mathematics can appear as chance, transport, a differential equation, or a linear-algebra problem because all four descriptions preserve the same local balance.

<!-- END SPOKEN LECTURE -->

## Mathematical companion

On \(h\mathbb Z\), for symmetric nearest-neighbor steps,
\[
p_j^{n+1}=\tfrac12p_{j-1}^n+\tfrac12p_{j+1}^n,
\qquad \frac{p_j^{n+1}-p_j^n}{\Delta t}
=\frac{h^2}{2\Delta t}\frac{p_{j-1}^n-2p_j^n+p_{j+1}^n}{h^2}.
\]
Choosing \(\Delta t=h^2/(2D)\) gives a consistent discretization of \(u_t=Du_{xx}\); probability masses need conversion to densities by a factor of \(1/h\) in a continuum interpretation. On \(\mathbb R\), the fundamental solution for initial point mass is
\[
p(x,t)=(4\pi Dt)^{-1/2}\exp[-x^2/(4Dt)],\quad \operatorname{Var}(X_t)=2Dt.
\]
For a finite undirected graph with adjacency matrix \(A\), degree matrix \(D_g\), and \(L=D_g-A\), the continuous-time edge-rate process has column probability evolution \(p'(t)=-\kappa Lp(t)\). Connected graph: zero eigenvalue is simple; eigenvalues nonnegative; \(p(t)\to\mathbf1/|V|\). In contrast, the discrete-time neighbor-uniform walk has transition matrix \(P=D_g^{-1}A\) (row-stochastic convention) and stationary \(\pi_i\propto\deg(i)\); for a bipartite graph, periodicity can obstruct convergence of the discrete-time distribution even when the stationary distribution exists.

For the path on three vertices, \(L=\begin{psmallmatrix}1&-1&0\\-1&2&-1\\0&-1&1\end{psmallmatrix}\), eigenvalues \(0,1,3\). Its modes evolve as \(e^{-\kappa\lambda t}\).

### Exercises and answers

1. **Coefficient.** If the step length is 0.1 and time step 0.005, what is D? **Answer:** \(h^2/(2\Delta t)=0.01/0.01=1\).
2. **Spread.** What is the variance of the Brownian diffusion with D equal to two at time three? **Answer:** Twelve.
3. **Three-vertex path.** What stationary distribution does the symmetric edge-rate continuous-time walk have? **Answer:** Uniform: one third at each vertex. A discrete neighbor-uniform walk instead has proportions one quarter, one half, one quarter.
4. **Boundary.** Does an absorbing boundary conserve total probability inside the domain? **Answer:** Not if absorption removes particles; the missing mass records absorption.

### Reading and attribution

- Levin and Peres, *Markov Chains and Mixing Times*, second edition, for finite-state random walks and spectral structure: https://pages.uoregon.edu/dlevin/MARKOV/.
- MIT OpenCourseWare, *Theory of Probability* (18.175): https://ocw.mit.edu/courses/18-175-theory-of-probability-spring-2014/pages/lecture-slides/.
- The random-walk to heat-equation scaling and three-vertex mode calculation are independently derived examples of standard results.
