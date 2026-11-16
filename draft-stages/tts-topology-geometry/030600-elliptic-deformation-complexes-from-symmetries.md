# 030600 - Deformation Complexes: Tangents, Symmetries, and Obstructions

**Track:** Topology and Geometry. **Background:** chain complexes, gauge connections, covariant exterior derivative, Fredholm operators. **Central question:** how can a nonlinear equation with symmetries have a finite-dimensional local space of solutions?

<!-- BEGIN SPOKEN LECTURE -->

# Deformation Complexes: Tangents, Symmetries, and Obstructions

A nonlinear differential equation on a manifold can have infinitely many unknown degrees of freedom. If the unknown is a connection, we can also change its local description by a gauge transformation without changing the underlying geometry. Yet advanced geometry often speaks of a moduli space of solutions that is finite-dimensional. Where did all those degrees of freedom go?

The short answer is that we linearize both the equation and the symmetry. Their interaction produces a sequence of linear maps. When that sequence is an elliptic complex, its cohomology spaces are finite-dimensional and describe the local geometry of solutions modulo symmetry.

## Begin with an ordinary equation and a redundant variable

Imagine a finite-dimensional map from a space of unknowns to a space of constraints. Near a solution, its derivative tells us which small changes preserve the constraint to first order. That kernel is the space of infinitesimal solutions.

Now suppose a group acts on the unknowns without changing the constraint. Moving along a group orbit produces changes that solve the linearized constraint automatically. Such motions are not genuinely new solutions after quotienting by the group. So the infinitesimal moduli space is the kernel of the constraint derivative, modulo directions coming from the symmetry derivative.

This is already a chain complex: the map from infinitesimal symmetries to infinitesimal unknowns, followed by the map to infinitesimal constraints, has zero composition. Its first cohomology measures deformations that cannot be removed by symmetry.

## The three cohomology groups

There are three recurring roles. Degree zero consists of infinitesimal symmetries that do nothing to the solution, often called stabilizers. Degree one consists of infinitesimal genuine deformations. Degree two measures obstructions, or constraints that cannot be solved by an arbitrary infinitesimal correction.

If the obstruction group is zero, an implicit-function-type argument often turns the infinitesimal picture into a smooth local moduli space, after accounting for stabilizers. If obstructions remain, the local solution space can be singular or cut out by an additional finite-dimensional nonlinear equation. Vanishing of the obstruction space is a sufficient regularity condition, not a property every solution enjoys.

## A toy model on the circle

Take a unitary line connection on a circle. Locally it is an imaginary-valued one-form. A gauge transformation changes it by the differential of a phase. In infinitesimal terms, functions map to one-forms by differentiation. Since every connection on a one-dimensional base is flat, there is no curvature two-form constraint to add.

The deformation quotient is one-forms modulo exact one-forms. The constant angular one-form survives. It corresponds to changing the holonomy around the circle. Gauge transformations with nonzero winding identify holonomies that differ by an integral phase, so the actual moduli space is a circle rather than a real line. Its tangent space is still one-dimensional.

Constant gauge transformations act trivially on every unitary line connection. They form the stabilizer. This means the quotient has a symmetry that must be understood separately from its tangent direction. It also illustrates the difference between local linearized geometry and global discrete identifications.

## The anti-self-dual connection equation

On an oriented Riemannian four-manifold, two-forms split into self-dual and anti-self-dual parts. For a connection on a principal bundle, the anti-self-duality equation sets the self-dual part of its curvature to zero.

Perturb a solution connection by a Lie-algebra-valued one-form. The first variation of curvature is its covariant exterior derivative. The linearized equation therefore takes the self-dual projection of that derivative. An infinitesimal gauge transformation, on the other hand, changes the connection by the covariant derivative of a Lie-algebra-valued function.

At an anti-self-dual solution, the composition of these maps vanishes because its value is the bracket with the self-dual curvature, which is zero. So we obtain the anti-self-dual deformation complex: functions to one-forms to self-dual two-forms.

## Why ellipticity is more than a label

To decide whether the resulting cohomology is finite-dimensional, we examine the highest-derivative symbols. For nonzero frequency, the symbol of the first map inserts that frequency covector. The second map takes the self-dual projection of wedging with the same covector. The resulting symbol sequence is exact.

This exactness is the definition of an elliptic complex. On a closed manifold, elliptic theory gives finite-dimensional cohomology. It also allows the combined gauge-fixed operator, which includes both the formal adjoint of the first map and the second map, to be treated as Fredholm.

That operator has an index. The index is related to the alternating dimensions of the deformation cohomology groups. But the actual dimension of a moduli space at one solution can depend on the stabilizers and obstructions. A virtual or expected dimension is not a guarantee that a smooth manifold of that dimension is present.

## What nonlinear analysis must still do

The complex only describes first-order behavior. The curvature equation includes a quadratic term in the connection perturbation. To construct the local solution space, one chooses a gauge slice, solves an infinite-dimensional complement equation using elliptic estimates, and reduces the remaining problem to a finite-dimensional obstruction map. That is the Kuranishi viewpoint.

At a regular irreducible solution, with no infinitesimal stabilizers beyond the discrete center and no obstruction group, the moduli space is locally smooth, with tangent space given by the first cohomology. At reducible or obstructed solutions, singularities can occur. Nothing in the word 'elliptic' eliminates these possibilities.

We have therefore separated three questions that are often compressed together: which variations satisfy the linearized equation, which of those variations are pure symmetry, and whether the nonlinear equation can actually realize them. This separation is the foundation of instanton and monopole moduli theory.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For an ASD connection \(A\) on \(P\to X^4\), the deformation complex is
\[0\longrightarrow\Omega^0(\operatorname{ad}P)\xrightarrow{d_A}\Omega^1(\operatorname{ad}P)\xrightarrow{d_A^+}\Omega^{2,+}(\operatorname{ad}P)\longrightarrow0.\]
The identity \(d_A^+d_A\phi=[F_A^+,\phi]\) makes this a complex only at a solution with \(F_A^+=0\) (or under a special central-curvature modification). Its cohomology spaces are
\[H_A^0=\ker d_A,\quad H_A^1=\ker d_A^+/\operatorname{im}d_A,\quad H_A^2=\operatorname{coker}d_A^+.\]
The Fredholm gauge-fixed operator \(\mathcal D_A=d_A^*\oplus d_A^+:\Omega^1(\operatorname{ad}P)\to\Omega^0(\operatorname{ad}P)\oplus\Omega^{2,+}(\operatorname{ad}P)\) has
\[\operatorname{ind}\mathcal D_A=\dim H_A^1-\dim H_A^0-\dim H_A^2.\]
Symbol exactness holds for \(\xi\ne0\): \(\operatorname{im}(\xi\otimes\cdot)=\ker(\pi_+\circ(\xi\wedge\cdot))\) on one-forms tensored with \(\operatorname{ad}P\), using \(\dim\Omega^1=4\), \(\dim\Omega^{2,+}=3\). On a circle, the abelian flat-connection tangent quotient \(\Omega^1/d\Omega^0\cong H^1(S^1;i\mathbb R)\) is real one-dimensional; the global quotient by large gauges is \(U(1)\) holonomy.

### Exercises with answers

1. **Symmetry directions.** Why do infinitesimal gauge variations lie in the kernel of the linearized ASD equation at an ASD connection? **Answer:** \(d_A^+d_A\phi=[F_A^+,\phi]=0\).
2. **First cohomology.** What does \(H_A^1\) represent? **Answer:** infinitesimal solutions modulo infinitesimal gauge transformations.
3. **Obstructions.** What does \(H_A^2\) measure? **Answer:** failure of surjectivity of the linearized equation after quotienting, hence possible nonlinear obstructions.
4. **Dimension.** Does a Fredholm index by itself imply a smooth moduli space? **Answer:** no; reducibles and nonzero obstruction spaces may create singularities.

### Sources and further reading

- Daniel Freed and Karen Uhlenbeck, [Instantons and Four-Manifolds](https://doi.org/10.1007/978-1-4613-9703-8) (book; publisher access may apply).
- Tim Perutz, [Lectures on gauge theory and symplectic geometry](https://web.ma.utexas.edu/users/perutz/Northwestern/NorthwesternL3.pdf).
- Overviews: [Instanton](https://en.wikipedia.org/wiki/Instanton), [Elliptic complex](https://en.wikipedia.org/wiki/Elliptic_complex), [Moduli space](https://en.wikipedia.org/wiki/Moduli_space).
