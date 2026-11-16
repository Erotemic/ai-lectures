# 037000 - Wrapped Floer Homology and Symplectic Cohomology

**Track:** Topology and Geometry. **Background:** exact symplectic manifolds, Lagrangian intersection theory, Hamiltonian flows, and Floer complexes. **Central question:** how can counting Hamiltonian chords at infinity recover topology of loop spaces?

<!-- BEGIN SPOKEN LECTURE -->

# Ordinary Floer theory stops too early

Imagine two Lagrangian submanifolds inside a symplectic manifold. Their intersections are the starting points for a version of Floer theory. A differential counts certain solutions of a nonlinear elliptic equation connecting intersection points. Under suitable compactness and transversality conditions, the homology carries information that survives Hamiltonian deformations.

That construction works especially naturally in compact settings. But many symplectic spaces of central interest are noncompact. A cotangent bundle, for example, extends indefinitely in momentum directions. Its fiber over one base point is also noncompact. Two copies of that fiber may intersect at one point, yet the ambient geometry contains an entire space of based loops that the single intersection cannot reveal.

Wrapped Floer theory changes the problem deliberately. Instead of forbidding the Lagrangians from exploring infinity, it allows Hamiltonian dynamics that grow appropriately toward infinity. New Hamiltonian chords appear, and their homology captures information invisible to the most literal intersection count.

# The symplectic geometry of a cotangent bundle

Let Q be a smooth closed manifold. Its cotangent bundle consists of all covectors attached to points of Q. It carries a canonical one-form and a symplectic form obtained by differentiating that one-form. These are not arbitrary choices; they come from the very definition of cotangent vectors.

A cotangent fiber is the set of all covectors over one fixed point. It is a Lagrangian submanifold, meaning the symplectic form restricts to zero on it and its dimension is half the dimension of the cotangent bundle.

Take a Hamiltonian that grows with momentum. Its trajectories project to paths in Q, and chords whose endpoints lie on the fixed cotangent fiber correspond, under standard kinetic Hamiltonians and appropriate nondegeneracy conditions, to based paths that start and end at the selected point. Such a path is a based loop.

This observation is the geometric clue behind the comparison between wrapped Floer homology of a cotangent fiber and homology of the based loop space of Q. The wrapped generators are not just points of intersection. They encode paths with different winding or homotopy behavior.

# A circle gives infinitely many generators

Take Q to be a circle. Fix a base point. A based loop may go around the circle zero times, once in the positive direction, once in the negative direction, or any integer number of times. The winding number classifies its based homotopy class.

The based loop space of a circle therefore has connected components indexed by all integers. Each component is contractible. Its degree-zero homology has one generator for every integer and can be described as the group ring of the integers, or Laurent polynomials in a symbol t and its inverse.

The wrapped Floer cohomology of a cotangent fiber in the cotangent bundle of the circle recovers this structure, with appropriate grading and coefficient conventions. That is a dramatic improvement over the naive picture of a single fiber intersecting itself at one point.

The infinite collection of wrapped generators does not mean that the resulting theory has lost control. The generators are filtered by Hamiltonian action, and the differential counts solutions with energy estimates. Taking a directed limit over larger Hamiltonian slopes reveals successively more of the noncompact geometry.

# Why the word wrapped is literal

On a Liouville manifold, there is a natural radial direction near infinity. The Hamiltonian flow winds a Lagrangian along this end. A wrapping Hamiltonian is chosen to grow so that new chords are created in a controlled manner.

One then forms a Floer complex from these chords, counts rigid Floer strips as the differential, and uses continuation maps to compare different choices of wrapping Hamiltonian. The wrapped Floer homology is obtained through an appropriate direct limit or an equivalent cofinal construction.

The maximum principle and exactness conditions help keep relevant Floer trajectories from escaping uncontrollably to infinity. Without such analytic controls, an infinite collection of chords could become an ill-defined counting problem. Wrapped Floer theory is not simply “count everything at infinity.” It is an organized limit of well-posed chain complexes.

The precise foundations depend on exactness, grading, orientations, coefficients, stops or boundary conditions, and on the ambient symplectic category. A result proved for exact cotangent bundles should not be casually transferred to arbitrary nonexact symplectic manifolds.

# A product hides in the loop-space comparison

Floer homology often supports more than a vector-space structure. In the wrapped setting, one can compose chords using operations defined by holomorphic polygons. At the chain level, these operations organize into an A-infinity algebra or category.

On based loops, there is a natural operation: concatenate two loops that share a base point. Under suitable hypotheses, the wrapped algebra of a cotangent fiber matches chains on the based loop space with this concatenation-type product, up to the appropriate homotopical structures.

For the circle, winding numbers add under concatenation. A loop with winding three followed by one with winding minus one has winding two. The corresponding Laurent monomials multiply in the obvious way. This makes the topology visible directly in the algebra.

We should distinguish an isomorphism of graded homology groups from an equivalence of chain-level algebraic structures. The latter is a stronger statement and requires care with higher products, gradings, and signs. The underlying homology calculation is the accessible entrance, not the whole theorem.

# From one Lagrangian to the ambient manifold

Wrapped Floer theory is centered on noncompact Lagrangian objects. Symplectic cohomology is a related invariant of the noncompact symplectic manifold itself. Its generators are periodic Hamiltonian orbits rather than chords with Lagrangian endpoints.

The same wrapping philosophy appears. We use Hamiltonians with prescribed behavior at infinity, build Floer complexes, and pass to a limit. On cotangent bundles, symplectic cohomology is related to the homology of the free loop space, where loops no longer have a fixed base point.

The distinction is instructive. Based loops correspond to cotangent-fiber endomorphisms. Free loops correspond to the ambient Hamiltonian periodic-orbit problem. These constructions are related by deep open–closed maps and categorical structures, but their generators and algebraic operations are different.

# What wrapping can detect

An invariant of a noncompact symplectic manifold should be sensitive to its geometry at infinity. Wrapped Floer theory and symplectic cohomology accomplish this in a controlled way. They can distinguish symplectic spaces with similar ordinary topology, provide obstructions to certain fillings, and test generation statements for Fukaya categories.

The circle calculation is a miniature model of the broader principle. A cotangent fiber is locally simple, but its interaction with Hamiltonian trajectories encodes all the based loops of the underlying manifold. Allowing controlled motion at infinity converts local intersection information into global loop-space topology.

This is why wrapped Floer theory belongs simultaneously to symplectic geometry, algebraic topology, and categorical algebra. Its analytic foundation consists of solutions to differential equations; its generators come from Hamiltonian dynamics; and its answer can be the homology of an infinite-dimensional space of loops.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For an exact cotangent bundle `T^*Q` of a closed smooth manifold `Q` with a cotangent fiber `L=T^*_qQ`, the wrapped Floer cohomology of `L` is related by the Abbondandolo–Schwarz/Abouzaid comparison, with grading and coefficient hypotheses, to based-loop homology:
\[
HW^*(L,L)\cong H_{-*}(\Omega_q Q).
\]
At an A-infinity level, the wrapped endomorphism algebra corresponds to chains on `Omega_q Q`, with based-loop concatenation. For `Q=S^1`, components are labeled by integers, each contractible, hence `H_0(Omega S^1;Z) ~= Z[t,t^{-1}]` and other homology vanishes. Symplectic cohomology of `T^*Q` is instead related to homology of the **free** loop space `LQ`, with degree shifts and orientation conventions.

### Exercises with answers

1. What distinguishes Hamiltonian chords from periodic Hamiltonian orbits? **Answer:** chords have specified Lagrangian endpoint conditions; periodic orbits close in phase space.
2. How many connected components does the based loop space of a circle have? **Answer:** countably infinitely many, indexed by winding numbers.
3. What operation corresponds to multiplication of Laurent monomials in the circle example? **Answer:** concatenation of based loops, adding winding numbers.
4. Why does a wrapped theory require analytic control at infinity? **Answer:** to keep Floer trajectories and counts compact or otherwise well-defined.

### Reading and source notes

- [Abouzaid, On the Wrapped Fukaya Category and Based Loops](https://arxiv.org/abs/0907.5606), comparison of cotangent fibers with chains on based loops.
- [Abbondandolo and Schwarz, On the Floer Homology of Cotangent Bundles](https://arxiv.org/abs/math/0408280), cotangent-bundle Floer and loop-space comparisons.
