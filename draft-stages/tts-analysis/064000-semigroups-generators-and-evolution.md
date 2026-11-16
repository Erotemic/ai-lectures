# 064000 — Semigroups and Generators: Solving Time Evolution Beyond Self-Adjoint Operators

**Track:** Analysis from First Principles. **Background:** bounded operators, functional calculus and weak derivatives. **Central question:** How do we describe a continuously evolving system when its generator is unbounded or not self-adjoint?

<!-- BEGIN SPOKEN LECTURE -->

# Semigroups and Generators: Solving Time Evolution Beyond Self-Adjoint Operators

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

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

A \(C_0\)-semigroup \((T(t))_{t\ge0}\) on Banach X satisfies \(T(0)=I\), \(T(t+s)=T(t)T(s)\), and \(\lim_{t\downarrow0}T(t)x=x\) for every x. Its generator is
\[Ax=\lim_{h\downarrow0}\frac{T(h)x-x}{h},\qquad D(A)=\left\{x:\text{limit exists in }X\right\}.\]

Translation on \(L^2(\mathbb R)\): \((T(t)f)(x)=f(x-t)\) for \(t\ge0\) defines an isometric strongly continuous semigroup with generator \(A=-\partial_x\) on \(H^1(\mathbb R)\). This is not norm continuous: \(\|T(t)-I\|=2\) for every \(t>0\), as seen in the Fourier representation \(e^{-it\xi}\).

For a strongly continuous contraction semigroup, a dense closed generator satisfies the Hille–Yosida resolvent bounds \((0,\infty)\subset\rho(A)\) and \(\|(\lambda I-A)^{-1}\|\le1/\lambda\) for \(\lambda>0\); conversely the stated domain and resolvent hypotheses generate a contraction semigroup. For Hilbert spaces the Lumer–Phillips theorem equivalently characterizes maximal dissipativity.

For \(f\in L^1([0,T];X)\), the integral formula
\[u(t)=T(t)u_0+\int_0^t T(t-s)f(s)\,ds\]
defines a mild solution of \(u'=Au+f\), with strong differentiability requiring extra regularity.

### Exercises with answers

1. **Shift law.** Show \(T(s)T(t)f(x)=f(x-s-t)\). **Answer:** Apply the translation definition twice.
2. **Shift generator.** For differentiable compactly supported f, compute the derivative at zero. **Answer:** \(Af=-f'\).
3. **Forced scalar.** Solve \(u'=-u+1\), \(u(0)=0\). **Answer:** \(u(t)=1-e^{-t}\), also given by the semigroup integral.

### Reading and source notes

- [Mathew A. Johnson, Introduction to Semigroup Methods](https://matjohn.ku.edu/Notes/Math951Notes_Ch6.pdf)
- [MIT OpenCourseWare, 18.102 Introduction to Functional Analysis, lecture notes](https://ocw.mit.edu/courses/18-102-introduction-to-functional-analysis-spring-2021/pages/lecture-notes-and-readings/)
- [John K. Hunter, Notes on Partial Differential Equations](https://www.math.ucdavis.edu/~hunter/m218a_09/pde_notes.pdf)
