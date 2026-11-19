# Action, Floer cylinders, compactness, and boundary cancellation

<!-- BEGIN SPOKEN LECTURE -->

# Action, Floer cylinders, compactness, and boundary cancellation

## Hamiltonian Action: Why Periodic Orbits Are Critical Points

To study periodic trajectories by Morse theory, we need a function whose critical points are exactly those trajectories. It cannot be an ordinary function on phase space, because a periodic orbit is a whole loop rather than a single point. Our unknown is now a path that goes all the way around the time circle and ends where it began.

The natural function is Hamiltonian action. It measures a combination of enclosed symplectic area and accumulated Hamiltonian energy. The first task is to define it, then vary the loop and see why its stationary points satisfy Hamilton's equations.

### Start with ordinary mechanical action

In elementary mechanics, one often integrates momentum times the rate of change of position, minus the Hamiltonian, over a time interval. The first term remembers how the path winds through position-momentum space. The second subtracts the accumulated energy function.

For the standard phase plane, this gives the integral of p times d q, minus the time integral of H. An ordinary calculus-of-variations calculation shows that its stationary paths obey Hamilton's equations, provided endpoint conditions are handled correctly.

For periodic paths, the endpoints are identified. We can vary an entire closed loop without fixing a distinguished starting position, while keeping the period equal to one. The variation of the action then has no leftover endpoint contribution.

The point of rewriting action geometrically is that a general symplectic manifold may have no global q and p coordinates and no global momentum one-form. The formula in coordinates is still a useful model, but it cannot be the definition in every target.

### Replace the line integral with area

A contractible loop can be filled by a disk. We integrate the symplectic form over that disk, with a minus sign in our chosen convention, and subtract the time integral of the Hamiltonian along the boundary loop.

Why this sign? Earlier we defined the Hamiltonian vector field by inserting it into the symplectic form to obtain the differential of H. With that choice, the negative area plus negative Hamiltonian formula is the one whose stationary points satisfy the forward Hamiltonian equation. Different books make different simultaneous sign choices. We will keep this one fixed.

In the phase plane, use the global one-form minus p times d q, whose derivative is the standard symplectic form. Stokes' theorem turns minus the disk area into plus the integral of p d q around the loop. We recover the familiar mechanical action exactly.

### Vary the loop

Now perturb the loop slightly. At each moment, the perturbation is a vector tangent to phase space. Differentiating the disk-area term produces a boundary integral that pairs the loop's velocity with the perturbation under the symplectic form. Differentiating the Hamiltonian term produces the differential of H paired with the same perturbation.

By the definition of Hamiltonian vector field, the latter is the symplectic pairing with that vector field. Subtracting it leaves the pairing of the difference between the actual loop velocity and the Hamiltonian velocity with every possible perturbation.

Nondegeneracy of the symplectic form now does the final work. If the first variation vanishes for every perturbation, the actual velocity must equal the Hamiltonian vector field at every time. Thus the critical points of the action are precisely the one-periodic Hamiltonian trajectories, in the selected contractible class.

This is the central variational observation behind Hamiltonian Floer homology.

### A concrete oscillator calculation

Consider the phase plane with energy one half times a positive constant a times the sum of q squared and p squared. The Hamiltonian equation rotates the plane at angular speed a. If a is not an integer multiple of two pi, no nonconstant circular orbit closes up after exactly one unit of time. The origin is the only one-periodic orbit.

At the origin the loop encloses no area and the Hamiltonian vanishes. Its action is zero. If we add a constant c to H, the Hamiltonian vector field does not change at all, but the action of every one-periodic loop decreases by c. Action values depend on how we normalize H; action differences for the same Hamiltonian do not.

If a is exactly two pi, every circular trajectory closes after one unit. The periodic orbits occur in continuous families, so the standard nondegenerate-orbit setup is no longer available. This makes a useful example of why generic perturbations matter.

### The dependence on a filling disk

On the sphere, one loop might be filled by a northern disk or by the opposite disk with suitable orientation. Gluing the two fillings produces a sphere. Their symplectic areas can differ by the total symplectic area of that sphere.

Therefore the action of a bare loop need not be a single real number. The choice of filling, often called a capping, may be part of the generator. If we change the capping by a sphere class A, the action changes by minus the symplectic area of A under our convention.

This ambiguity vanishes when the symplectic form evaluates to zero on every sphere. That condition is symplectic asphericity. It is satisfied on the two-torus, even though the symplectic form on the torus is not globally exact. Every contractible loop on the torus then has a well-defined action independent of its filling disk.

The distinction is useful: exactness of the symplectic form is a stronger global condition than vanishing of its integrals over spheres.

### Why the critical points require extra labels

A periodic orbit may be nondegenerate, meaning its linearized time-one return map does not have one as an eigenvalue. For generic Hamiltonians on compact targets, nondegenerate periodic orbits are isolated. Such orbits can serve as generators of a chain complex.

But we still need to grade those generators. The linearized flow twists tangent directions along the loop, and the Conley–Zehnder index converts that twisting into an integer, once a suitable trivialization or capping is chosen. Changing the capping can change both the action and the grading.

The action functional therefore has two layers of topology: its critical loops are trajectories of an ordinary differential equation, while its values and gradings may remember how those loops are filled by surfaces.

### Turning the variational idea into homology

The next step is to put a metric on loop space using a compatible almost-complex structure. We can then study paths of steepest descent for the action. Such a path is a whole sequence of loops, so it has two variables: progress along descent and periodic time around each loop.

The resulting equation is a first-order elliptic PDE. Energy of a solution will equal the drop in action between its limiting orbits. In other words, the same action we just defined will both select the generators and control the curves connecting them.

Without this derivation, Floer homology can seem like an arbitrary count of mysterious cylinders. With it, the strategy is familiar: find a function, locate its critical points, study its gradient trajectories, and turn the geometry into a chain complex. The infinite-dimensional setting is harder, but the organizing idea is Morse theory.

## Floer Cylinders: Negative Gradient Flow Becomes an Elliptic Equation

We now have an action function on a space of loops. Each critical loop is a periodic Hamiltonian trajectory. In Morse theory, the next step would be to follow descending paths from one critical point to another. In our case a point of the function's domain is already a loop, so a descending path is a moving family of loops.

Imagine a cylinder. Travel around it to traverse periodic time. Travel along its length to move from one loop to the next. A Floer trajectory is a map from that cylinder into phase space, and it obeys an elliptic equation derived from negative-gradient flow of action.

### Build a metric on the space of loops

Choose a compatible almost-complex structure J on the symplectic manifold. It combines with the symplectic form to give a Riemannian metric at each point of the target.

Now take two small perturbations of a loop. At each time t, they are tangent vectors to the target. Use the Riemannian metric to pair them, then integrate this pairing over one full period. We have defined a formal metric on the infinite-dimensional space of loops.

The gradient of the action is the vector field along the loop whose pairing with every perturbation reproduces the first variation of action. For our sign convention, the gradient is J applied to the difference between the loop velocity and the Hamiltonian vector field.

So the negative gradient points in the direction opposite to that expression. If we call the direction along the cylinder s and the periodic time t, the equation for a descending trajectory becomes: the s derivative plus J applied to the t derivative minus Hamiltonian velocity equals zero.

This is the Floer equation. With no Hamiltonian it becomes the equation for a J-holomorphic cylinder. With a Hamiltonian it is an inhomogeneous Cauchy-Riemann equation.

### Check the sign by examining stationary solutions

A crucial test is to freeze the cylinder in the s direction. Then all the loops in the family are the same. The Floer equation reduces to the condition that the t velocity equals the Hamiltonian vector field. Thus its stationary solutions really are the periodic trajectories we intended to count.

Another test uses a very small time-independent Hamiltonian and looks only at cylinders that are constant in periodic time. The equation reduces to a gradient flow of H in the increasing direction. That might sound odd because we called the Floer flow descending. There is no contradiction: for a constant loop, our action is minus H. Going uphill in H goes downhill in action.

This check is more valuable than memorizing a sign from a different text. Authors may define the symplectic form, Hamiltonian vector field, and action using different combinations of signs. What must remain consistent is the derivation from the variational formula.

### Derive the energy identity

Take a solution of the Floer equation. At each point of the cylinder, the norm of its s derivative measures how quickly the loop is changing. Square that norm and integrate over all s and one period of t. This is the Floer energy.

Along a negative-gradient trajectory, the rate of change of the action equals minus the squared norm of its gradient. The Floer equation identifies the gradient's norm with the norm of the s derivative. Integrate this rate from the distant negative end of the cylinder to the distant positive end.

If the solution converges to periodic orbits at both ends, the energy equals the action of the incoming orbit minus the action of the outgoing orbit. Energy is nonnegative. Therefore a nonconstant finite-energy Floer trajectory can only move from higher action to lower action.

This is the organizing estimate behind the chain differential. It also prevents infinite wandering within a bounded action window under suitable discreteness assumptions.

### Finite energy and asymptotic orbits

We want solutions that become close to periodic Hamiltonian trajectories as s tends to minus and plus infinity. The chosen asymptotic orbits must usually be nondegenerate. Under the standard analytic conditions, a finite-energy solution approaches its nondegenerate ends exponentially.

The reason is closely related to linear stability. Near an orbit, linearize the Floer equation. The resulting operator along the periodic direction has a spectral gap when the orbit is nondegenerate. Modes of a finite-energy solution then decay along the cylinder rather than persisting with zero decay rate.

This statement has hypotheses. In a noncompact target, finite energy alone does not necessarily keep a map inside a compact subset. When ends are degenerate, the exponential-decay argument changes. We will isolate these issues rather than treating convergence as free.

### Translation symmetry and rigidity

Suppose u of s and t is a solution. Replace s by s plus a constant. The shifted map solves the same equation because the data do not depend on s. This is the translation symmetry of the cylinder.

If a nonconstant solution belongs to a one-parameter family made only by shifting s, we regard all those shifts as the same geometric connecting trajectory. So a moduli space of cylinders is commonly divided by translation before we count rigid solutions.

The Fredholm index predicts the parameterized dimension. After quotienting the free translation action, the expected dimension decreases by one. A connecting cylinder with index one may therefore be isolated modulo translation and contribute one unit to a differential.

### Test the theory on the torus

A symplectic two-torus has no nonconstant holomorphic spheres, because its second homotopy group vanishes. Choose a sufficiently small generic Hamiltonian whose critical points form a Morse function with one minimum, two saddles, and one maximum. For appropriate small data, the relevant contractible periodic trajectories are those four critical points.

The Floer complex then resembles the Morse complex of the torus, with grading conventions carefully matched. Its homology has ranks one, two, and one. We will return to why this survives changes in the Hamiltonian.

The main lesson for now is the role of the equation. It has not been invented to make the desired counts work. It is the negative gradient equation for a geometrically defined action. The energy identity then follows from gradient descent, exactly as it does for a finite-dimensional function.

The difficult work begins when we ask whether the set of all such cylinders is compact, smooth, oriented, and countable in the needed dimensions. Those are the questions addressed by compactness, regularity, and boundary cancellation in the remainder of this construction.

## Compactness for Holomorphic Curves: Bubbles, Breaking, and Escape

We now know how to write the Floer equation, how to calculate the energy of a solution, and how to predict the dimension of its moduli space. None of that, by itself, means we can count solutions.

Imagine that we have infinitely many distinct cylinders, each with energy at most a fixed constant. If they fail to converge to an ordinary cylinder, where can they go? The answer organizes one of the central subjects of symplectic analysis: compactness up to carefully classified degenerations.

### Bounded total energy is not a pointwise derivative bound

A function can have a derivative that grows very large inside a region whose area becomes very small, while the integral of the squared derivative remains bounded. A total-energy bound sees the amount of variation but may not see where the variation is becoming concentrated.

For holomorphic maps, the elliptic equation prevents completely arbitrary concentration. Small-energy regularity gives control when sufficiently little energy is present in a small neighborhood. Thus a sequence with uniformly bounded total energy can have only finitely many separate regions containing a fixed positive amount of concentrated energy, provided the relevant energy quantization and geometry hypotheses hold.

Away from those regions, elliptic estimates can often upgrade weak convergence to smooth convergence. Near a concentration point we zoom in instead.

### A sphere map shrinking to a point

Take the Riemann sphere and the degree-one holomorphic maps that send z to z divided by a small positive number epsilon. Each is an automorphism of the sphere and has normalized symplectic energy one.

As epsilon tends to zero, at every fixed point other than z equals zero, the image tends toward the point at infinity. The maps appear to become constant across almost the whole sphere. But the total energy remains one. Where did it go?

Look near z equals zero using the new coordinate w equal to z divided by epsilon. In that magnified view, the map is simply w itself. A nonconstant holomorphic sphere reappears. The sequence did not lose energy; it concentrated it at a vanishing scale.

This is a simple model of sphere bubbling. The limiting object can consist of a main curve and one or more holomorphic sphere components attached at nodes. A correct compactification records that extra geometry.

### Breaking is a different degeneration

Floer cylinders have a long s direction. Even without any pointwise blow-up, a sequence of cylinders can develop a very long middle region that is almost a periodic orbit. After shifting each end separately along s, we may see one cylinder from orbit x to orbit y and another from y to orbit z.

The sequence has converged to a broken trajectory: a two-stage chain of cylinders. Each stage has finite energy, and the total action drop is the sum of the drops through the intermediate orbit.

Breaking is the Floer analogue of broken gradient trajectories in finite-dimensional Morse theory. Sphere bubbling is an additional phenomenon caused by the two-dimensional map equation. They must not be conflated.

### Disks can bubble from Lagrangian boundaries

For a strip with its lower edge on one Lagrangian and its upper edge on another, concentration may occur near a boundary point. Rescaling can produce a holomorphic disk whose boundary lies on one Lagrangian.

The disk may change the algebraic boundary of moduli spaces. It is one reason the most general Lagrangian Floer theory cannot be reduced to simply counting strips and declaring the differential squared zero.

Exactness gives a transparent way to eliminate this particular degeneration in a useful model. If the symplectic form is exact and each relevant Lagrangian is exact, a holomorphic disk with boundary on one Lagrangian has zero area by Stokes' theorem. The area–energy identity then forces it to be constant.

Likewise, a symplectically aspherical target has no nonconstant holomorphic spheres. These two conditions remove two major classes of bubbles, though they do not remove breaking.

### The problem of noncompact targets

A cotangent bundle is generally noncompact. Even if we have ruled out all nonconstant sphere and disk bubbles, a sequence of maps might run farther and farther out along momentum directions. Its image might leave every compact set.

Therefore exactness alone is not a global compactness theorem. A Floer theory on a noncompact target needs additional control at infinity: an appropriate Hamiltonian growth condition, geometry that supports a maximum principle, or another valid confinement argument.

On a closed symplectic manifold the image cannot escape the target, but sphere bubbling may remain. One has traded one compactness problem for another. Choosing the right hypotheses depends on the situation being studied.

### The meaning of Gromov compactness

Gromov compactness does not usually mean that every bounded-energy sequence has a smooth limit on the original fixed domain. It says that under precise assumptions, after passing to a subsequence and allowing reparameterizations and controlled degenerations, the sequence converges to a richer object such as a stable holomorphic map with bubble components.

For Floer trajectories, the suitable compactification may also contain broken cylinders. In favorable aspherical situations, for the lowest-dimensional moduli spaces, breaking is the only boundary phenomenon that survives.

This is exactly the situation we need for the Floer differential. A one-dimensional moduli space of unbroken cylinders, after dividing by translation, should compactify to something like a collection of closed intervals and circles. The endpoints of the intervals are broken pairs of rigid trajectories.

If a sphere or disk bubble can also appear as a boundary point, that simple algebraic picture may fail. If the curves can escape to infinity, there may be no finite boundary count at all. Thus the compactness hypotheses are part of the definition's correctness, not technical footnotes.

### Why this is stronger than a vague convergence statement

When you read an advanced theorem, ask four separate questions. Is total energy bounded? Can local derivatives become unbounded? Can a solution break along the cylinder? Can the target or domain geometry escape the compact region under consideration?

Different hypotheses answer different questions. Symplectic asphericity removes nonconstant sphere bubbles. Exact Lagrangians remove nonconstant boundary disks in the exact setting. Nondegenerate asymptotics and finite-energy analysis identify the ends of broken cylinders. Proper confinement or compactness of the target prevents escape.

Once these mechanisms are separated, the later proof that a differential squares to zero becomes intelligible. It is an assertion about the entire boundary of a compactified one-dimensional moduli space, not merely a symbolic cancellation.

## Why Floer Boundaries Cancel: Moduli Spaces and Differential Squared

We have finally assembled the objects needed for a Floer chain complex. There are periodic Hamiltonian orbits, the critical points of action. There are Floer cylinders connecting those orbits, obtained from negative gradient flow. There is a Fredholm index predicting the dimensions of solution families. And there are compactness results describing how such families can degenerate.

Now comes the algebraic claim: applying the Floer boundary operator twice gives zero. The proof is geometric, and every analytic hypothesis has a role.

### Begin with a finite-dimensional rehearsal

Imagine a hill landscape with several critical points. In Morse homology, the boundary of an index-two critical point counts downward gradient trajectories to index-one critical points. Each trajectory is considered up to translating the time at which we start watching it.

To compute the boundary twice, we count two-step paths: from an index-two point to an index-one point, then from that point to an index-zero point.

Why do these counts cancel? Because the two-step configurations are endpoints of one-dimensional families of unbroken trajectories between the original endpoints. A compact one-dimensional manifold is a collection of circles and closed intervals. Every interval has two endpoints, and every circle has none. Modulo two, the total number of boundary points is therefore zero.

The same structure drives Floer homology. But the phrase 'one-dimensional manifold' now refers to a space of solutions of an elliptic PDE, not a family of ordinary integral curves.

### Generators and rigid cylinders

Choose a closed symplectic manifold with no nonconstant holomorphic spheres, and a Hamiltonian whose one-periodic orbits in the chosen class are nondegenerate. Choose suitable almost-complex data so the relevant cylinder moduli spaces are regular.

Build a vector space over the field with two elements, one basis generator for each orbit. For now, work modulo two so we do not need to construct coherent orientations.

Between two orbits x and y, consider the set of Floer cylinders from x to y. Divide nonconstant solutions by translation along the length of the cylinder. If the relative index is one, the expected dimension after this quotient is zero. Under the needed compactness, there are finitely many such rigid cylinders.

Define the boundary of x by summing, for each y of index one lower, the number of rigid cylinders from x to y, reduced modulo two, times the generator y.

We have defined an actual linear operator, not just a metaphor. Its input is one orbit, and its output is a finite combination of other orbits.

### Expand the boundary twice

Apply the boundary once to x. Each term is an intermediate orbit y weighted by the count of rigid cylinders from x to y. Apply the boundary again. A term involving a final orbit z counts pairs of rigid cylinders: the first from x to y, the second from y to z, summed over all y.

So the coefficient of z in the boundary squared is a count of broken two-stage trajectories.

How can we see that it is zero? Look at unbroken cylinders from x to z whose relative index is two. After translation is removed, their expected dimension is one. Under regularity, this is locally a smooth one-dimensional moduli space.

The compactness theorem says that a sequence in this space can converge either to another unbroken cylinder or to a broken pair of rigid cylinders, provided bubbling and escape have been ruled out in the relevant dimension.

### Compactification and gluing must agree

Compactness alone is not enough. It tells us what limits can occur, but it does not automatically say that every broken pair is the endpoint of precisely the right local family of unbroken solutions.

A gluing theorem supplies the missing direction. Start with two rigid cylinders that meet at the same intermediate orbit. Cut off their distant ends, insert a long neck, and solve away the small error produced by the approximate joining. Under suitable transversality and uniform inverse estimates, one obtains a nearby genuine cylinder. As the neck becomes longer, it approaches the broken pair.

Thus the compactified one-dimensional moduli space has boundary points exactly corresponding to the two-stage configurations counted in the boundary squared. The total number of endpoints of this compact one-manifold is even. Therefore every coefficient in the boundary squared vanishes over the field with two elements.

With integer coefficients, orientations assign signs to boundary points, and the signed sum is zero. That requires coherent orientation data; it is not obtained by merely replacing the number two with the integers.

### A circle calculation to keep the picture concrete

Take a cosine function on a circle. It has one maximum and one minimum. For an appropriate metric, there are two gradient trajectories descending from the maximum to the minimum, one along each arc of the circle.

Over the field with two elements, those two trajectories cancel. The Morse differential is zero. The chain groups have one generator in degree one and one in degree zero, giving the homology of a circle.

For a small graph of the derivative of cosine in the cotangent bundle of a circle, the Lagrangian intersection picture has the same two generators. Under a suitable small-graph correspondence, rigid Floer strips reproduce the Morse trajectories. That makes the cancellation visible in a genuine geometric example, not only in the abstract moduli-space proof.

### Where the proof can fail

If we count strips with boundaries on nonexact Lagrangians, holomorphic disks can bubble off. Such bubbles may contribute additional ends to what we hoped was a one-dimensional moduli space. Then the naive count of broken pairs need not be the complete boundary count.

Likewise, sphere bubbles may matter in a general closed target, and loss of control at infinity matters in noncompact targets. Multiple covers and failed transversality may prevent the moduli space from being an ordinary smooth manifold of the expected dimension.

The general theory has sophisticated ways to address these issues: monotonicity hypotheses, Novikov coefficients, coherent perturbations, virtual cycles, and higher algebraic corrections. We do not need to implement all of those systems to understand the foundational proof. We do need to know why the simpler proof is valid only after its assumptions are checked.

### What the new homology can say

Because the boundary squared is zero, we can take the kernel of the boundary modulo its image, just as for any chain complex. Under suitable continuation arguments, changing the Hamiltonian or almost-complex structure does not change the resulting Floer homology.

When this invariant agrees with ordinary homology in a small-Hamiltonian model, it can give a lower bound on the number of periodic orbits for more complicated Hamiltonians. That is how topology can force dynamics.

The foundational result of this lecture is therefore not merely an equation. It is a chain of implications: regularity gives a one-dimensional moduli space; compactness classifies its degenerations; gluing identifies its boundary; and the elementary fact that boundaries of one-manifolds cancel gives the algebraic identity.

This is what it means to build homology from solutions of a partial differential equation.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Hamiltonian Action: Why Periodic Orbits Are Critical Points

**Track:** Topology and Geometry. **Background:** Hamiltonian vector fields, line integrals, disk fillings, de Rham cohomology, variational calculus. **Central question:** what quantity on the space of loops has Hamiltonian periodic orbits as its stationary points?

#### Mathematical companion (not spoken)

Fix \(\omega=dq\wedge dp\), \(\iota_{X_{H_t}}\omega=dH_t\), and a contractible one-periodic loop \(x:S^1\to M\) with capping \(u:D^2\to M\), \(u|_{\partial D^2}=x\). Use
\[
\mathcal A_H([x,u])=-\int_{D^2}u^*\omega-\int_0^1H_t(x(t))\,dt.
\]
For a variation \(\xi\) of the loop, \(d\mathcal A_H(x)\cdot\xi=\int_0^1\omega(\dot x-X_{H_t}(x),\xi)\,dt\). Hence \(d\mathcal A_H=0\) iff \(\dot x=X_{H_t}(x)\). In canonical coordinates \(\lambda=-p\,dq\), \(d\lambda=\omega\), so \(\mathcal A_H=\int_0^1(p\dot q-H_t)\,dt\).

If two cappings differ by \(A\in\pi_2(M)\), the action difference is \(-\int_A\omega\). Vanishing of \(\omega|_{\pi_2(M)}\) removes capping ambiguity for contractible loops; vanishing of \(c_1(TM)|_{\pi_2(M)}\) removes the corresponding absolute Conley–Zehnder grading ambiguity (up to a global grading convention). Under a Hamiltonian shift \(H_t\mapsto H_t+c(t)\), each action changes by \(-\int_0^1c(t)dt\), but the flow is unchanged.

For \(H=(a/2)(q^2+p^2)\) on \(\mathbb R^2\), \(\dot q=ap\), \(\dot p=-aq\); nonzero trajectories have period \(2\pi/|a|\). If \(a\notin2\pi\mathbb Z\), the origin is the only one-periodic solution.

##### Exercises with answers

1. **Stationarity.** What equation characterizes critical loops of the stated action? **Answer:** \(\dot x=X_H(x)\).
2. **Stokes.** With \(\lambda=-p\,dq\), what is the exact-case action? **Answer:** \(\int (p\dot q-H)dt\).
3. **Capping.** What changes when the disk is replaced by one differing by sphere class \(A\)? **Answer:** action changes by \(-\int_A\omega\).
4. **Oscillator.** For \(a=1\), how many one-periodic oscillator orbits exist on \(\mathbb R^2\)? **Answer:** only the origin.

##### Sources and further reading

- Dietmar Salamon, [Lectures on Floer Homology](https://people.math.ethz.ch/~salamon/PREPRINTS/floer.pdf), §§1.1–1.5; action convention and variation.
- Andreas Floer, [Symplectic Fixed Points and Holomorphic Spheres](https://doi.org/10.1007/BF01260388), *Communications in Mathematical Physics* 120 (1989), 575–611.
- [Action (physics)](https://en.wikipedia.org/wiki/Action_(physics)); [Hamiltonian mechanics](https://en.wikipedia.org/wiki/Hamiltonian_mechanics).

### Floer Cylinders: Negative Gradient Flow Becomes an Elliptic Equation

**Track:** Topology and Geometry. **Background:** action functionals, compatible J, Cauchy–Riemann operators and gradient flow. **Central question:** how does the energy of a Floer cylinder equal the action lost between two periodic orbits?

#### Mathematical companion (not spoken)

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

##### Exercises with answers

1. **Stationary cylinder.** What does the Floer equation become if \(u_s=0\)? **Answer:** \(u_t=X_H(u)\).
2. **Gradient sign.** For \(u_t=0\) and autonomous \(H\), does the resulting \(s\)-flow increase or decrease H? **Answer:** increase H, while decreasing the action \(-H\).
3. **Energy.** If \(\mathcal A_H(x_-)=5\) and \(\mathcal A_H(x_+)=3\), what is the energy of a connecting cylinder? **Answer:** two.
4. **Symmetry.** What is modded out when counting rigid nonconstant cylinders? **Answer:** translation along the \(s\) coordinate.

##### Sources and further reading

- Dietmar Salamon, [Lectures on Floer Homology](https://people.math.ethz.ch/~salamon/PREPRINTS/floer.pdf), §§1.4–1.6, exact action and energy conventions.
- Michael Hutchings, [Floer Theory course](https://math.berkeley.edu/~hutching/teach/277-2008/index.html), conceptual bridge from Morse to Floer.
- [Floer homology](https://en.wikipedia.org/wiki/Floer_homology); [Gradient flow](https://en.wikipedia.org/wiki/Gradient_flow).

### Compactness for Holomorphic Curves: Bubbles, Breaking, and Escape

**Track:** Topology and Geometry. **Background:** J-holomorphic area–energy, elliptic estimates, Floer cylinders, topology of spheres and disks. **Central question:** what can a bounded-energy sequence of holomorphic curves do instead of converging smoothly?

#### Mathematical companion (not spoken)

A concrete bubble sequence on \(\mathbb{CP}^1\) is \(u_\epsilon(z)=z/\epsilon\), \(\epsilon\downarrow0\), extended by \(\infty\mapsto\infty\). With \(\int_{\mathbb{CP}^1}\omega_{FS}=1\), \(E(u_\epsilon)=1\) for every \(\epsilon\), but \(u_\epsilon\to\infty\) locally smoothly on \(\mathbb{CP}^1\setminus\{0\}\). Under rescaling \(z=\epsilon w\), \(u_\epsilon(\epsilon w)=w\), revealing a degree-one bubble. Domain reparameterization and stable-map convergence provide the correct compactification.

For Floer trajectories \(u_k\), a broken limit may contain \(u^1:x_-\to y\) and \(u^2:y\to x_+\), with \(E(u^1)+E(u^2)=\mathcal A(x_-)-\mathcal A(x_+)\). On a closed symplectically aspherical target, nonconstant holomorphic sphere bubbles are impossible; for exact \((M,\omega=d\lambda)\) with exact Lagrangians \(\lambda|_{L_i}=df_i\), nonconstant disk bubbles on one \(L_i\) are impossible. Both conclusions use the energy–area identity. Additional regularity and nonescape hypotheses are still necessary for compactness.

##### Exercises with answers

1. **Bubble.** What is the energy of every map \(z\mapsto z/\epsilon\) on the normalized Riemann sphere? **Answer:** one, since it has degree one.
2. **Breaking.** If a Floer cylinder breaks through an intermediate orbit \(y\), how do the action drops combine? **Answer:** additively: \(A(x_-)-A(y)+A(y)-A(x_+)=A(x_-)-A(x_+)\).
3. **Disk.** Which hypothesis rules out nonconstant boundary bubbles by Stokes in the model? **Answer:** exact symplectic form and exact boundary Lagrangians.
4. **Escape.** Can noncompact cotangent-bundle targets have escape to infinity even when sphere and disk bubbles are excluded? **Answer:** yes, without extra confinement estimates.

##### Sources and further reading

- Mikhail Gromov, [Pseudo-holomorphic Curves in Symplectic Manifolds](https://doi.org/10.1007/BF01388806), original holomorphic-curve compactness framework.
- Dusa McDuff and Dietmar Salamon, [J-Holomorphic Curves and Symplectic Topology](https://bookstore.ams.org/coll-52), bubble-tree and stable-map compactness proofs.
- Chris Wendl, [Lectures on Holomorphic Curves](https://arxiv.org/abs/1011.1690), energy quantization and compactness.
- [Gromov compactness theorem](https://en.wikipedia.org/wiki/Gromov%27s_compactness_theorem_%28topology%29).

### Why Floer Boundaries Cancel: Moduli Spaces and Differential Squared

**Track:** Topology and Geometry. **Background:** Morse chain complexes, Fredholm index, regular Floer cylinders, compactness and broken trajectories. **Central question:** exactly which analytic facts make the algebraic Floer boundary square to zero?

#### Mathematical companion (not spoken)

In a closed symplectically aspherical setting \(\omega|_{\pi_2(M)}=0\), \(c_1(TM)|_{\pi_2(M)}=0\), for nondegenerate orbits \(x,y\), assume standard Floer regularity and compactness. The unparameterized moduli space \(\mathcal M(x,y)/\mathbb R\) of nonconstant cylinders has expected real dimension \(\mu(x)-\mu(y)-1\) for the compatible grading and index convention. Define over \(\mathbb F_2\)
\[
\partial x=\sum_{\mu(x)-\mu(y)=1}\#_2(\mathcal M(x,y)/\mathbb R)\,y.
\]
The compactification of a one-dimensional quotient moduli space \(\mu(x)-\mu(z)=2\) has boundary strata \(\coprod_y(\mathcal M(x,y)/\mathbb R)\times(\mathcal M(y,z)/\mathbb R)\) with each relative index one. Under compactness, no bubbling or escape, and gluing, this is the entire boundary, so \(\partial^2=0\) by even boundary count. Integral coefficients require coherent orientations. If Lagrangian disk bubbling contributes to codimension-one strata, naive \(\partial^2=0\) may fail, motivating obstruction and \(A_\infty\)-structures.

For \(f(q)=\cos(2\pi q)\) on \(S^1\), there are two descending gradient arcs from the maximum to the minimum. Their count vanishes in \(\mathbb F_2\), giving the ordinary circle Morse complex \(C_1=C_0=\mathbb F_2\), \(\partial=0\). This is not yet a proof of the general Hamiltonian Floer comparison, only its finite-dimensional model.

##### Exercises with answers

1. **Rigid dimension.** What relative index gives zero-dimensional unparameterized regular Floer cylinders? **Answer:** one.
2. **Square.** Which configurations appear in a coefficient of \(\partial^2 x\)? **Answer:** pairs of rigid cylinders through an intermediate orbit.
3. **Boundary count.** Why does a compact one-manifold have even total boundary cardinality? **Answer:** each interval contributes two endpoints and each circle contributes none.
4. **Caveat.** Name one degeneration that invalidates the simple broken-only boundary description. **Answer:** nonconstant holomorphic sphere bubbling or boundary disk bubbling, depending on the setup.

##### Sources and further reading

- Andreas Floer, [Morse Theory for Lagrangian Intersections](https://doi.org/10.4310/JDG/1214442477), original chain-count construction.
- Dietmar Salamon, [Lectures on Floer Homology](https://people.math.ethz.ch/~salamon/PREPRINTS/floer.pdf), gluing, compactness, and invariance.
- Michael Hutchings, [Floer Theory course notes](https://math.berkeley.edu/~hutching/teach/277-2008/index.html), Morse-to-Floer progression.
- [Floer homology](https://en.wikipedia.org/wiki/Floer_homology).
