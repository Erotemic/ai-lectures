# 025700 — Floer Cylinders: Negative Gradient Flow Becomes an Elliptic Equation

**Track:** Topology and Geometry. **Background:** action functionals, compatible J, Cauchy–Riemann operators and gradient flow. **Central question:** how does the energy of a Floer cylinder equal the action lost between two periodic orbits?

<!-- BEGIN SPOKEN LECTURE -->

# Floer Cylinders: Negative Gradient Flow Becomes an Elliptic Equation

We now have an action function on a space of loops. Each critical loop is a periodic Hamiltonian trajectory. In Morse theory, the next step would be to follow descending paths from one critical point to another. In our case a point of the function's domain is already a loop, so a descending path is a moving family of loops.

Imagine a cylinder. Travel around it to traverse periodic time. Travel along its length to move from one loop to the next. A Floer trajectory is a map from that cylinder into phase space, and it obeys an elliptic equation derived from negative-gradient flow of action.

## Build a metric on the space of loops

Choose a compatible almost-complex structure J on the symplectic manifold. It combines with the symplectic form to give a Riemannian metric at each point of the target.

Now take two small perturbations of a loop. At each time t, they are tangent vectors to the target. Use the Riemannian metric to pair them, then integrate this pairing over one full period. We have defined a formal metric on the infinite-dimensional space of loops.

The gradient of the action is the vector field along the loop whose pairing with every perturbation reproduces the first variation of action. For our sign convention, the gradient is J applied to the difference between the loop velocity and the Hamiltonian vector field.

So the negative gradient points in the direction opposite to that expression. If we call the direction along the cylinder s and the periodic time t, the equation for a descending trajectory becomes: the s derivative plus J applied to the t derivative minus Hamiltonian velocity equals zero.

This is the Floer equation. With no Hamiltonian it becomes the equation for a J-holomorphic cylinder. With a Hamiltonian it is an inhomogeneous Cauchy-Riemann equation.

## Check the sign by examining stationary solutions

A crucial test is to freeze the cylinder in the s direction. Then all the loops in the family are the same. The Floer equation reduces to the condition that the t velocity equals the Hamiltonian vector field. Thus its stationary solutions really are the periodic trajectories we intended to count.

Another test uses a very small time-independent Hamiltonian and looks only at cylinders that are constant in periodic time. The equation reduces to a gradient flow of H in the increasing direction. That might sound odd because we called the Floer flow descending. There is no contradiction: for a constant loop, our action is minus H. Going uphill in H goes downhill in action.

This check is more valuable than memorizing a sign from a different text. Authors may define the symplectic form, Hamiltonian vector field, and action using different combinations of signs. What must remain consistent is the derivation from the variational formula.

## Derive the energy identity

Take a solution of the Floer equation. At each point of the cylinder, the norm of its s derivative measures how quickly the loop is changing. Square that norm and integrate over all s and one period of t. This is the Floer energy.

Along a negative-gradient trajectory, the rate of change of the action equals minus the squared norm of its gradient. The Floer equation identifies the gradient's norm with the norm of the s derivative. Integrate this rate from the distant negative end of the cylinder to the distant positive end.

If the solution converges to periodic orbits at both ends, the energy equals the action of the incoming orbit minus the action of the outgoing orbit. Energy is nonnegative. Therefore a nonconstant finite-energy Floer trajectory can only move from higher action to lower action.

This is the organizing estimate behind the chain differential. It also prevents infinite wandering within a bounded action window under suitable discreteness assumptions.

## Finite energy and asymptotic orbits

We want solutions that become close to periodic Hamiltonian trajectories as s tends to minus and plus infinity. The chosen asymptotic orbits must usually be nondegenerate. Under the standard analytic conditions, a finite-energy solution approaches its nondegenerate ends exponentially.

The reason is closely related to linear stability. Near an orbit, linearize the Floer equation. The resulting operator along the periodic direction has a spectral gap when the orbit is nondegenerate. Modes of a finite-energy solution then decay along the cylinder rather than persisting with zero decay rate.

This statement has hypotheses. In a noncompact target, finite energy alone does not necessarily keep a map inside a compact subset. When ends are degenerate, the exponential-decay argument changes. We will isolate these issues rather than treating convergence as free.

## Translation symmetry and rigidity

Suppose u of s and t is a solution. Replace s by s plus a constant. The shifted map solves the same equation because the data do not depend on s. This is the translation symmetry of the cylinder.

If a nonconstant solution belongs to a one-parameter family made only by shifting s, we regard all those shifts as the same geometric connecting trajectory. So a moduli space of cylinders is commonly divided by translation before we count rigid solutions.

The Fredholm index predicts the parameterized dimension. After quotienting the free translation action, the expected dimension decreases by one. A connecting cylinder with index one may therefore be isolated modulo translation and contribute one unit to a differential.

## Test the theory on the torus

A symplectic two-torus has no nonconstant holomorphic spheres, because its second homotopy group vanishes. Choose a sufficiently small generic Hamiltonian whose critical points form a Morse function with one minimum, two saddles, and one maximum. For appropriate small data, the relevant contractible periodic trajectories are those four critical points.

The Floer complex then resembles the Morse complex of the torus, with grading conventions carefully matched. Its homology has ranks one, two, and one. We will return to why this survives changes in the Hamiltonian.

The main lesson for now is the role of the equation. It has not been invented to make the desired counts work. It is the negative gradient equation for a geometrically defined action. The energy identity then follows from gradient descent, exactly as it does for a finite-dimensional function.

The difficult work begins when we ask whether the set of all such cylinders is compact, smooth, oriented, and countable in the needed dimensions. That is the bridge to the next lectures.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Maintain \(\iota_{X_H}\omega=dH\), \(g(v,w)=\omega(v,Jw)\), and
\[
\mathcal A_H([x,u])=-\int_{D^2}u^*\omega-\int_0^1H_t(x(t))dt.
\]
The first variation is \(d\mathcal A_H(x)\cdot\xi=\int_0^1\omega(\dot x-X_H,\xi)dt\), so \(\nabla\mathcal A_H=J(\dot x-X_H)\). The negative-gradient equation is
\[
\partial_su+J_t(u)(\partial_tu-X_{H_t}(u))=0.
\]
For an \(s\)-independent pair \((H,J)\) and finite-energy asymptotic orbits \(x_\pm\) with compatible cappings,
\[
E(u)=\int_{\mathbb R\times S^1}|\partial_su|^2dsdt
=\mathcal A_H(x_-)-\mathcal A_H(x_+)\ge0.
\]
The PDE implies \(|\partial_su|=|\partial_tu-X_H|\). For an autonomous \(H\), solutions independent of \(t\) satisfy \(\partial_su=\nabla_g H(u)\), consistent with \(\mathcal A_H(\mathrm{constant}_x)=-H(x)\). Nondegenerate periodic orbits and appropriate compactness control underlie asymptotic convergence. The \(s\)-translation quotient reduces the local dimension by one for regular nonconstant trajectories.

### Exercises with answers

1. **Stationary cylinder.** What does the Floer equation become if \(u_s=0\)? **Answer:** \(u_t=X_H(u)\).
2. **Gradient sign.** For \(u_t=0\) and autonomous \(H\), does the resulting \(s\)-flow increase or decrease H? **Answer:** increase H, while decreasing the action \(-H\).
3. **Energy.** If \(\mathcal A_H(x_-)=5\) and \(\mathcal A_H(x_+)=3\), what is the energy of a connecting cylinder? **Answer:** two.
4. **Symmetry.** What is modded out when counting rigid nonconstant cylinders? **Answer:** translation along the \(s\) coordinate.

### Sources and further reading

- Dietmar Salamon, [Lectures on Floer Homology](https://people.math.ethz.ch/~salamon/PREPRINTS/floer.pdf), §§1.4–1.6, exact action and energy conventions.
- Michael Hutchings, [Floer Theory course](https://math.berkeley.edu/~hutching/teach/277-2008/index.html), conceptual bridge from Morse to Floer.
- [Floer homology](https://en.wikipedia.org/wiki/Floer_homology); [Gradient flow](https://en.wikipedia.org/wiki/Gradient_flow).
