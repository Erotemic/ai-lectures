# 025600 — Hamiltonian Action: Why Periodic Orbits Are Critical Points

**Track:** Topology and Geometry. **Background:** Hamiltonian vector fields, line integrals, disk fillings, de Rham cohomology, variational calculus. **Central question:** what quantity on the space of loops has Hamiltonian periodic orbits as its stationary points?

<!-- BEGIN SPOKEN LECTURE -->

# Hamiltonian Action: Why Periodic Orbits Are Critical Points

To study periodic trajectories by Morse theory, we need a function whose critical points are exactly those trajectories. It cannot be an ordinary function on phase space, because a periodic orbit is a whole loop rather than a single point. Our unknown is now a path that goes all the way around the time circle and ends where it began.

The natural function is Hamiltonian action. It measures a combination of enclosed symplectic area and accumulated Hamiltonian energy. The first task is to define it, then vary the loop and see why its stationary points satisfy Hamilton's equations.

## Start with ordinary mechanical action

In elementary mechanics, one often integrates momentum times the rate of change of position, minus the Hamiltonian, over a time interval. The first term remembers how the path winds through position-momentum space. The second subtracts the accumulated energy function.

For the standard phase plane, this gives the integral of p times d q, minus the time integral of H. An ordinary calculus-of-variations calculation shows that its stationary paths obey Hamilton's equations, provided endpoint conditions are handled correctly.

For periodic paths, the endpoints are identified. We can vary an entire closed loop without fixing a distinguished starting position, while keeping the period equal to one. The variation of the action then has no leftover endpoint contribution.

The point of rewriting action geometrically is that a general symplectic manifold may have no global q and p coordinates and no global momentum one-form. The formula in coordinates is still a useful model, but it cannot be the definition in every target.

## Replace the line integral with area

A contractible loop can be filled by a disk. We integrate the symplectic form over that disk, with a minus sign in our chosen convention, and subtract the time integral of the Hamiltonian along the boundary loop.

Why this sign? Earlier we defined the Hamiltonian vector field by inserting it into the symplectic form to obtain the differential of H. With that choice, the negative area plus negative Hamiltonian formula is the one whose stationary points satisfy the forward Hamiltonian equation. Different books make different simultaneous sign choices. We will keep this one fixed.

In the phase plane, use the global one-form minus p times d q, whose derivative is the standard symplectic form. Stokes' theorem turns minus the disk area into plus the integral of p d q around the loop. We recover the familiar mechanical action exactly.

## Vary the loop

Now perturb the loop slightly. At each moment, the perturbation is a vector tangent to phase space. Differentiating the disk-area term produces a boundary integral that pairs the loop's velocity with the perturbation under the symplectic form. Differentiating the Hamiltonian term produces the differential of H paired with the same perturbation.

By the definition of Hamiltonian vector field, the latter is the symplectic pairing with that vector field. Subtracting it leaves the pairing of the difference between the actual loop velocity and the Hamiltonian velocity with every possible perturbation.

Nondegeneracy of the symplectic form now does the final work. If the first variation vanishes for every perturbation, the actual velocity must equal the Hamiltonian vector field at every time. Thus the critical points of the action are precisely the one-periodic Hamiltonian trajectories, in the selected contractible class.

This is the central variational observation behind Hamiltonian Floer homology.

## A concrete oscillator calculation

Consider the phase plane with energy one half times a positive constant a times the sum of q squared and p squared. The Hamiltonian equation rotates the plane at angular speed a. If a is not an integer multiple of two pi, no nonconstant circular orbit closes up after exactly one unit of time. The origin is the only one-periodic orbit.

At the origin the loop encloses no area and the Hamiltonian vanishes. Its action is zero. If we add a constant c to H, the Hamiltonian vector field does not change at all, but the action of every one-periodic loop decreases by c. Action values depend on how we normalize H; action differences for the same Hamiltonian do not.

If a is exactly two pi, every circular trajectory closes after one unit. The periodic orbits occur in continuous families, so the standard nondegenerate-orbit setup is no longer available. This makes a useful example of why generic perturbations matter.

## The dependence on a filling disk

On the sphere, one loop might be filled by a northern disk or by the opposite disk with suitable orientation. Gluing the two fillings produces a sphere. Their symplectic areas can differ by the total symplectic area of that sphere.

Therefore the action of a bare loop need not be a single real number. The choice of filling, often called a capping, may be part of the generator. If we change the capping by a sphere class A, the action changes by minus the symplectic area of A under our convention.

This ambiguity vanishes when the symplectic form evaluates to zero on every sphere. That condition is symplectic asphericity. It is satisfied on the two-torus, even though the symplectic form on the torus is not globally exact. Every contractible loop on the torus then has a well-defined action independent of its filling disk.

The distinction is useful: exactness of the symplectic form is a stronger global condition than vanishing of its integrals over spheres.

## Why the critical points require extra labels

A periodic orbit may be nondegenerate, meaning its linearized time-one return map does not have one as an eigenvalue. For generic Hamiltonians on compact targets, nondegenerate periodic orbits are isolated. Such orbits can serve as generators of a chain complex.

But we still need to grade those generators. The linearized flow twists tangent directions along the loop, and the Conley–Zehnder index converts that twisting into an integer, once a suitable trivialization or capping is chosen. Changing the capping can change both the action and the grading.

The action functional therefore has two layers of topology: its critical loops are trajectories of an ordinary differential equation, while its values and gradings may remember how those loops are filled by surfaces.

## Turning the variational idea into homology

The next step is to put a metric on loop space using a compatible almost-complex structure. We can then study paths of steepest descent for the action. Such a path is a whole sequence of loops, so it has two variables: progress along descent and periodic time around each loop.

The resulting equation is a first-order elliptic PDE. Energy of a solution will equal the drop in action between its limiting orbits. In other words, the same action we just defined will both select the generators and control the curves connecting them.

Without this derivation, Floer homology can seem like an arbitrary count of mysterious cylinders. With it, the strategy is familiar: find a function, locate its critical points, study its gradient trajectories, and turn the geometry into a chain complex. The infinite-dimensional setting is harder, but the organizing idea is Morse theory.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Fix \(\omega=dq\wedge dp\), \(\iota_{X_{H_t}}\omega=dH_t\), and a contractible one-periodic loop \(x:S^1\to M\) with capping \(u:D^2\to M\), \(u|_{\partial D^2}=x\). Use
\[
\mathcal A_H([x,u])=-\int_{D^2}u^*\omega-\int_0^1H_t(x(t))\,dt.
\]
For a variation \(\xi\) of the loop, \(d\mathcal A_H(x)\cdot\xi=\int_0^1\omega(\dot x-X_{H_t}(x),\xi)\,dt\). Hence \(d\mathcal A_H=0\) iff \(\dot x=X_{H_t}(x)\). In canonical coordinates \(\lambda=-p\,dq\), \(d\lambda=\omega\), so \(\mathcal A_H=\int_0^1(p\dot q-H_t)\,dt\).

If two cappings differ by \(A\in\pi_2(M)\), the action difference is \(-\int_A\omega\). Vanishing of \(\omega|_{\pi_2(M)}\) removes capping ambiguity for contractible loops; vanishing of \(c_1(TM)|_{\pi_2(M)}\) removes the corresponding absolute Conley–Zehnder grading ambiguity (up to a global grading convention). Under a Hamiltonian shift \(H_t\mapsto H_t+c(t)\), each action changes by \(-\int_0^1c(t)dt\), but the flow is unchanged.

For \(H=(a/2)(q^2+p^2)\) on \(\mathbb R^2\), \(\dot q=ap\), \(\dot p=-aq\); nonzero trajectories have period \(2\pi/|a|\). If \(a\notin2\pi\mathbb Z\), the origin is the only one-periodic solution.

### Exercises with answers

1. **Stationarity.** What equation characterizes critical loops of the stated action? **Answer:** \(\dot x=X_H(x)\).
2. **Stokes.** With \(\lambda=-p\,dq\), what is the exact-case action? **Answer:** \(\int (p\dot q-H)dt\).
3. **Capping.** What changes when the disk is replaced by one differing by sphere class \(A\)? **Answer:** action changes by \(-\int_A\omega\).
4. **Oscillator.** For \(a=1\), how many one-periodic oscillator orbits exist on \(\mathbb R^2\)? **Answer:** only the origin.

### Sources and further reading

- Dietmar Salamon, [Lectures on Floer Homology](https://people.math.ethz.ch/~salamon/PREPRINTS/floer.pdf), §§1.1–1.5; action convention and variation.
- Andreas Floer, [Symplectic Fixed Points and Holomorphic Spheres](https://doi.org/10.1007/BF01260388), *Communications in Mathematical Physics* 120 (1989), 575–611.
- [Action (physics)](https://en.wikipedia.org/wiki/Action_(physics)); [Hamiltonian mechanics](https://en.wikipedia.org/wiki/Hamiltonian_mechanics).
