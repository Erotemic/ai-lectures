# 067000 — Sectorial Operators: Why Diffusion Smooths Immediately
**Track:** Analysis from First Principles. **Background:** L-p spaces, basic Hilbert spaces and weak derivatives as introduced earlier in this course. **Central question:** What assumptions make this construction rigorous?

<!-- BEGIN SPOKEN LECTURE -->
# Sectorial Operators: Why Diffusion Smooths Immediately

A diffusion problem has a distinctive behavior. Even if the initial temperature profile contains a sharp corner, the profile becomes smooth as soon as a positive amount of time has passed, at least for the standard heat equation in open space. Contrast that with transporting the same profile rigidly to the right. Translation keeps every corner intact. Both motions are governed by semigroups, but only one is smoothing. We need language that explains the difference.

In a finite-dimensional system, a matrix A generates motion by the exponential of time times A. We can differentiate that exponential because its power series converges in matrix norm. In a differential equation, the generator may be an unbounded differential operator. The Laplacian is a standard example. It measures curvature of a function, and acting on increasingly rapid oscillations makes the result increasingly large. We should not expect an operator-norm power series for the exponential of such a generator.

Fortunately there are two alternative viewpoints. The first works through Fourier frequencies. For the heat equation on the whole line, an initial sine wave with frequency n decays at a rate proportional to n squared. High frequencies disappear much faster than low frequencies. The evolution multiplier is exponential decay in time times frequency squared. This one formula both defines the heat flow on square-integrable data and tells us why derivatives become controlled for positive time.

The second viewpoint uses the resolvent. A resolvent asks us to solve an equation involving the generator shifted by a scalar. Instead of inverting the Laplacian itself, which can have low-frequency problems, we invert a positive shift minus the Laplacian. In Fourier variables, this means dividing by the positive shift plus frequency squared. The division is stable, and the collection of these inverses has uniform bounds in sectors of the complex plane. Such sector-shaped resolvent estimates characterize the class of sectorial generators relevant to analytic semigroups, subject to the standard density and closedness conditions.

The geometric word analytic means more than differentiable in time along the positive real axis. For a suitable generator, the solution operator can be extended to complex times in a sector. This extra regularity implies that differentiating the semigroup for positive times costs a factor that behaves like one over time. At the first instant, such an estimate blows up; we do not claim the initial profile was smooth. At any later instant, however, the operator has had time to suppress high frequencies.

We can verify the size of the effect directly. Take the heat multiplier and apply a Laplacian afterward. The frequency contribution is frequency squared times its exponential damping. Its largest value over all frequencies is proportional to one divided by time. Thus the map taking initial data to the second spatial derivatives of the heat solution is bounded on L two for every positive time, but there is no uniform bound as time approaches zero.

Translation does not do this. Under the translation flow, the size of each Fourier frequency stays constant. Moving a step function does not turn it into a smooth function. The generator, the first spatial derivative, is unbounded, and its semigroup is strongly continuous, but it is not a smoothing analytic semigroup of the heat type. This supplies an important counterexample to the claim that every C-zero semigroup automatically improves regularity.

A realistic parabolic equation may contain variable coefficients or act on a bounded domain. Fourier diagonalization might no longer be available. Resolvent bounds let us reason without knowing every eigenfunction. That is why the operator-theoretic language matters in the proofs of existence, smoothing, maximal regularity and numerical stability.

At the same time, a sectorial estimate is never free. We must check the operator domain, boundary conditions, and the chosen Banach space. Dirichlet and Neumann Laplacians have different domains and different zero modes. The bare symbol for a differential operator does not uniquely specify its evolution. The central lesson is that the smoothing effect of heat is encoded both in frequency damping and in the geometry of the resolvent.
<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Let \(A=\Delta\) with domain \(H^2(\mathbb R^d)\) on \(L^2(\mathbb R^d)\). Then \(T(t)=e^{t\Delta}\) has Fourier multiplier \(e^{-t|\xi|^2}\), and \(\|T(t)\|_{2\to2}\le1\). For \(\mathrm{Re}\,\lambda>0\), \(\|R(\lambda,A)\|\le(\mathrm{Re}\,\lambda)^{-1}\). The sharper sectorial estimates concern sectors bounded away from the negative real axis; \(A\) generates an analytic semigroup.

For \(t>0\), \(\|\Delta T(t)\|_{2\to2}=\sup_{r\ge0}r^2e^{-tr^2}=1/(et)\). More generally \(\|(-\Delta)^{\alpha/2}T(t)\|_{2\to2}\le C_\alpha t^{-\alpha/2}\). These estimates do not assert \(u_0\in D(\Delta)\).

By contrast \((S(t)f)(x)=f(x+t)\) is a strongly continuous group on \(L^2(\mathbb R)\) with generator \(f'\) on \(H^1\); its Fourier multiplier has modulus one, so it does not smooth initial data.

One common convention calls \(-A\) sectorial of angle less than \(\pi/2\) when \(A\) generates a bounded analytic semigroup. Always specify sign and sector convention in statements.

### Exercises with answers

1. **Frequency decay.** Compare frequencies 1 and 5 at time 1 for the heat equation. **Answer:** Multipliers are \(e^{-1}\) and \(e^{-25}\), respectively.
2. **Optimization.** Find the maximum of \(s e^{-ts}\) over \(s\ge0\). **Answer:** At \(s=1/t\), with value \(1/(et)\).
3. **Counterexample.** Does translation smooth a step? **Answer:** No, the jump is translated but retained.

### Reading and source notes

- [Engel and Nagel, One-Parameter Semigroups for Linear Evolution Equations](https://www.math.uni-tuebingen.de/de/forschung/agfa/members/engel-nagel_one-parameter-semigroups.pdf/@@download/file/engel-nagel_one-parameter-semigroups.pdf)
- [John K. Hunter, Notes on Nonlinear Evolution Equations](https://www.math.ucdavis.edu/~hunter/notes/nonlinev.pdf)
