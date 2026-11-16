# 048000 — Borel Functional Calculus: When a Function Has Jumps

**Track:** Analysis from First Principles. **Background:** Spectral projections, measurable functions, strong and norm convergence. **Question:** How do we apply a discontinuous function to a self-adjoint operator?

<!-- BEGIN SPOKEN LECTURE -->

# Borel Functional Calculus: When a Function Has Jumps

A thermometer reports a continuously varying temperature. A thermostat makes a discontinuous decision: below a threshold it turns the heat on; above the threshold it turns the heat off. Both are functions of a number, but they behave differently under approximation. A continuously varying function can be uniformly approximated by suitable polynomials. A sharp threshold generally cannot.

Spectral filtering creates the same problem for operators. If A is self-adjoint, we may want to keep spectral values below a cutoff and discard all the others. That is the indicator function of a spectral set applied to A. Such a function may jump, yet the projection-valued measure tells us what it should mean.

## Begin with a step function

Choose several disjoint measurable spectral regions. Assign one scalar value to each region and zero outside their union. The result is a simple function, the kind used to construct the Lebesgue integral.

Its operator value is just a finite linear combination of spectral projections, each weighted by its scalar value. The algebra works immediately: the product of indicator functions for two regions is the indicator of their intersection, and the corresponding projections multiply in exactly the same way.

This also shows why a positive simple function gives a positive operator. A nonnegative linear combination of mutually perpendicular orthogonal projections produces nonnegative quadratic measurements on every vector.

A general bounded Borel measurable function can be approximated pointwise by simple functions that stay uniformly bounded. We want their operator values to converge. But which kind of convergence should we demand?

## Strong convergence instead of norm convergence

Fix one vector x. The spectral theorem associates to x a finite positive measure, recording how much of x lies in each spectral region. The squared norm of the difference between two simple-function operators applied to x is the integral of the squared difference of their scalar functions against that measure.

If the functions converge pointwise and are uniformly bounded, dominated convergence makes this integral tend to zero. Therefore the operator values converge on every fixed vector. This is strong operator convergence.

We define the bounded Borel function of A to be this strong limit. It is independent of the chosen bounded pointwise approximation, and it extends continuous functional calculus.

Why do we not demand operator-norm convergence? Because a step function can disagree substantially with any continuous approximation arbitrarily close to the jump. The operator norm is a worst-case bound over all unit vectors, including vectors concentrated in smaller and smaller spectral neighborhoods of that jump. Strong convergence follows each fixed vector instead, allowing its finite spectral measure to control the error.

This is the correct change of topology, not a relaxation made out of convenience. The difference is exactly what lets discontinuous spectral filters exist.

## Measure-zero changes may disappear

There is a new subtlety. Suppose A multiplies by t on L two of the unit interval. Let f be zero everywhere except at t equal to one half, where it equals one. As an ordinary function on the interval, f is not identically zero. But as a multiplication operator, f of A is the zero operator. A single point has measure zero, so it does not affect any L-two vector.

Consequently, the norm of f of A is not always the ordinary supremum of f over the spectrum. For bounded measurable functions we always have an upper bound by that supremum, but equality may fail. The correct norm is an essential supremum relative to the spectral measure class, equivalently the largest scalar size that matters to the projection-valued measure.

For continuous functions, every nonempty relatively open neighborhood of a spectral value has nonzero spectral projection. This ensures the supremum is still detected, and the continuous norm formula remains exact. For arbitrary Borel functions, pointwise spikes on spectral-null sets can vanish.

## Thresholds and sign functions

Define a function that is one for positive spectral values and zero elsewhere. Applying it to A gives the projection onto its positive spectral part. Similarly, indicators of negative, zero, or interval regions give spectral projections that decompose the Hilbert space.

For a self-adjoint A, the sign function can be defined as plus one on the positive spectrum, minus one on the negative spectrum, and zero at zero. Its operator value is self-adjoint and bounded by one in norm. On the subspace where A has no zero spectral component, it squares to the identity. On the entire space its square is the projection onto the orthogonal complement of the kernel.

A spectral threshold is not necessarily stable under small perturbations of the operator. If spectral values sit near the cutoff, a tiny perturbation may move them across it and change the projection sharply. This is a different phenomenon from the stable evaluation of a continuous function.

That is why the kind of scalar function matters. Smooth or continuous filters often behave robustly, while sharp spectral cuts can be sensitive at gaps that are closing.

## One construction, several useful viewpoints

In a diagonal matrix, bounded Borel calculus is simply entrywise function application in an orthonormal eigenbasis. In a multiplication model, it is multiplication by f composed with the underlying measurable spectral multiplier. In the projection-valued-measure model, it is the integral of f with respect to the spectral projections.

These descriptions are not competing definitions. They are versions of the same operation in different representations. The spectral theorem ensures that the rules agree.

The fundamental identity is a precise description of output length: the squared norm of f of A applied to x equals the integral of the squared absolute value of f against the scalar spectral measure of x. For bounded f that integral is always finite.

The identity also points toward a bigger theory. If f grows without bound, the same integral might be finite for some vectors and infinite for others. A function of an unbounded self-adjoint operator will then need a domain, specifying exactly which vectors are legitimate inputs. The distinction between bounded and unbounded functional calculus is not primarily a new formula. It is the appearance of domain conditions.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For a bounded self-adjoint A and bounded complex Borel f on \(\sigma(A)\), define \(f(A)=\int f(\lambda)\,dE_A(\lambda)\). The map is a unital \(*\)-homomorphism into \(\mathcal B(H)\) and
\[
\|f(A)x\|^2=\int_{\sigma(A)}|f(\lambda)|^2\,d\mu_x(\lambda),
\qquad \|f(A)\|\le\sup_{\lambda\in\sigma(A)}|f(\lambda)|.
\]
If \(f_n\) are uniformly bounded in supremum norm and converge pointwise to f, then \(f_n(A)x\to f(A)x\) for every x (bounded convergence). The inequality for the operator norm can be strict: if \(A=M_t\) on \(L^2[0,1]\) and \(f=\mathbf1_{\{1/2\}}\), then \(f(A)=0\) although \(\sup|f|=1\). The precise norm is the essential supremum with respect to the PVM's null sets.

For \(\operatorname{sgn}(A)\), choosing \(\operatorname{sgn}(0)=0\), we have \(\operatorname{sgn}(A)^2=I-E_A(\{0\})\). For bounded self-adjoint A, \(E_A(\{0\})\) is the orthogonal projection onto \(\ker A\).

### Exercises with answers

1. **Spectral switch.** Let \(A=\operatorname{diag}(-1,2,2)\) and \(f=\mathbf1_{(0,\infty)}\). Find f(A). **Answer:** \(\operatorname{diag}(0,1,1)\).
2. **Point spike.** Why is \(\mathbf1_{\{1/2\}}(M_t)=0\)? **Answer:** It multiplies by an almost-everywhere-zero scalar function.
3. **Two limits.** For \(A=M_t\), do \(A^n\) converge in operator norm to zero? **Answer:** No, every norm is one; they converge strongly to zero by dominated convergence.
4. **Sign.** If A has a nontrivial kernel, why is \(\operatorname{sgn}(A)^2\ne I\)? **Answer:** The sign function vanishes at zero and hence annihilates the kernel.

### Reading and source notes

- [Kelly Davis, Spectral Theorem for Bounded Self-Adjoint Operators](https://kellyjdavis.github.io/functional-analysis/spectral-theorems/).
- [Sheldon Axler, Measure, Integration & Real Analysis](https://measure.axler.net/).
- [University of Potsdam, Functional Analysis lecture notes](https://www.math.uni-potsdam.de/fileadmin/user_upload/Prof-Math-Phy/Rosenberger/Skripte/Funktionalanalysis_2.pdf).
