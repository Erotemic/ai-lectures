# 073000 — Duhamel’s Formula: Solving a Nonlinear Equation with a Linear Flow
**Track:** Analysis from First Principles. **Background:** L-p spaces, basic Hilbert spaces and weak derivatives as introduced earlier in this course. **Central question:** What assumptions make this construction rigorous?

<!-- BEGIN SPOKEN LECTURE -->
# Duhamel’s Formula: Solving a Nonlinear Equation with a Linear Flow

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
<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Let \(A\) generate a \(C_0\)-semigroup \(T(t)\) on a Banach space X. A mild solution of \(u'(t)=Au(t)+F(u(t))\) satisfies
\[u(t)=T(t)u_0+\int_0^tT(t-s)F(u(s))\,ds,\]
where the integral is a Bochner integral in X. Local existence follows if F is locally Lipschitz in the chosen X and the semigroup is locally bounded.

On X = \(BUC(\mathbb R^d)\), the bounded *uniformly continuous* functions, the heat semigroup is \(C_0\) and is L-infinity contractive. For \(F(u)=u^2\), fix \(M>\|u_0\|_\infty\) and B = \(\{u\in C([0,T];BUC): \sup_t\|u(t)\|_\infty\le M\}\). Then
\[\|\Phi u\|\le\|u_0\|_\infty+TM^2,\quad \|\Phi u-\Phi v\|\le2MT\|u-v\|.\]
Choose T so both invariance and strict contraction hold. **Caution:** the heat semigroup is not strongly continuous on all of \(L^\infty(\mathbb R^d)\) in the supremum norm; using BUC avoids this issue.

For constant \(u_0=c>0\), the exact spatially constant solution is \(u(t,x)=c/(1-ct)\), \(t<1/c\), showing finite-time reaction blow-up.

### Exercises with answers

1. **Semigroup input.** Where does the forcing at time s enter the solution at time t? **Answer:** Through \(T(t-s)F(u(s))\).
2. **Contraction criterion.** What bound must be strictly below one for the quadratic reaction in the radius-M ball? **Answer:** \(2MT\).
3. **Counterexample.** Does spatial diffusion guarantee global existence for \(u_t=\Delta u+u^2\)? **Answer:** No; constant positive solutions blow up at \(1/c\).

### Reading and source notes

- [John K. Hunter, Notes on Nonlinear Evolution Equations](https://www.math.ucdavis.edu/~hunter/notes/nonlinev.pdf)
- [Engel and Nagel, One-Parameter Semigroups](https://www.math.uni-tuebingen.de/de/forschung/agfa/members/engel-nagel_one-parameter-semigroups.pdf/@@download/file/engel-nagel_one-parameter-semigroups.pdf)
