# Deformations, gauge slices, dimensions, and instantons

<!-- BEGIN SPOKEN LECTURE -->

# Deformations, gauge slices, dimensions, and instantons

## Deformation Complexes: Tangents, Symmetries, and Obstructions

A nonlinear differential equation on a manifold can have infinitely many unknown degrees of freedom. If the unknown is a connection, we can also change its local description by a gauge transformation without changing the underlying geometry. Yet advanced geometry often speaks of a moduli space of solutions that is finite-dimensional. Where did all those degrees of freedom go?

The short answer is that we linearize both the equation and the symmetry. Their interaction produces a sequence of linear maps. When that sequence is an elliptic complex, its cohomology spaces are finite-dimensional and describe the local geometry of solutions modulo symmetry.

### Begin with an ordinary equation and a redundant variable

Imagine a finite-dimensional map from a space of unknowns to a space of constraints. Near a solution, its derivative tells us which small changes preserve the constraint to first order. That kernel is the space of infinitesimal solutions.

Now suppose a group acts on the unknowns without changing the constraint. Moving along a group orbit produces changes that solve the linearized constraint automatically. Such motions are not genuinely new solutions after quotienting by the group. So the infinitesimal moduli space is the kernel of the constraint derivative, modulo directions coming from the symmetry derivative.

This is already a chain complex: the map from infinitesimal symmetries to infinitesimal unknowns, followed by the map to infinitesimal constraints, has zero composition. Its first cohomology measures deformations that cannot be removed by symmetry.

### The three cohomology groups

There are three recurring roles. Degree zero consists of infinitesimal symmetries that do nothing to the solution, often called stabilizers. Degree one consists of infinitesimal genuine deformations. Degree two measures obstructions, or constraints that cannot be solved by an arbitrary infinitesimal correction.

If the obstruction group is zero, an implicit-function-type argument often turns the infinitesimal picture into a smooth local moduli space, after accounting for stabilizers. If obstructions remain, the local solution space can be singular or cut out by an additional finite-dimensional nonlinear equation. Vanishing of the obstruction space is a sufficient regularity condition, not a property every solution enjoys.

### A toy model on the circle

Take a unitary line connection on a circle. Locally it is an imaginary-valued one-form. A gauge transformation changes it by the differential of a phase. In infinitesimal terms, functions map to one-forms by differentiation. Since every connection on a one-dimensional base is flat, there is no curvature two-form constraint to add.

The deformation quotient is one-forms modulo exact one-forms. The constant angular one-form survives. It corresponds to changing the holonomy around the circle. Gauge transformations with nonzero winding identify holonomies that differ by an integral phase, so the actual moduli space is a circle rather than a real line. Its tangent space is still one-dimensional.

Constant gauge transformations act trivially on every unitary line connection. They form the stabilizer. This means the quotient has a symmetry that must be understood separately from its tangent direction. It also illustrates the difference between local linearized geometry and global discrete identifications.

### The anti-self-dual connection equation

On an oriented Riemannian four-manifold, two-forms split into self-dual and anti-self-dual parts. For a connection on a principal bundle, the anti-self-duality equation sets the self-dual part of its curvature to zero.

Perturb a solution connection by a Lie-algebra-valued one-form. The first variation of curvature is its covariant exterior derivative. The linearized equation therefore takes the self-dual projection of that derivative. An infinitesimal gauge transformation, on the other hand, changes the connection by the covariant derivative of a Lie-algebra-valued function.

At an anti-self-dual solution, the composition of these maps vanishes because its value is the bracket with the self-dual curvature, which is zero. So we obtain the anti-self-dual deformation complex: functions to one-forms to self-dual two-forms.

### Why ellipticity is more than a label

To decide whether the resulting cohomology is finite-dimensional, we examine the highest-derivative symbols. For nonzero frequency, the symbol of the first map inserts that frequency covector. The second map takes the self-dual projection of wedging with the same covector. The resulting symbol sequence is exact.

This exactness is the definition of an elliptic complex. On a closed manifold, elliptic theory gives finite-dimensional cohomology. It also allows the combined gauge-fixed operator, which includes both the formal adjoint of the first map and the second map, to be treated as Fredholm.

That operator has an index. The index is related to the alternating dimensions of the deformation cohomology groups. But the actual dimension of a moduli space at one solution can depend on the stabilizers and obstructions. A virtual or expected dimension is not a guarantee that a smooth manifold of that dimension is present.

### What nonlinear analysis must still do

The complex only describes first-order behavior. The curvature equation includes a quadratic term in the connection perturbation. To construct the local solution space, one chooses a gauge slice, solves an infinite-dimensional complement equation using elliptic estimates, and reduces the remaining problem to a finite-dimensional obstruction map. That is the Kuranishi viewpoint.

At a regular irreducible solution, with no infinitesimal stabilizers beyond the discrete center and no obstruction group, the moduli space is locally smooth, with tangent space given by the first cohomology. At reducible or obstructed solutions, singularities can occur. Nothing in the word 'elliptic' eliminates these possibilities.

We have therefore separated three questions that are often compressed together: which variations satisfy the linearized equation, which of those variations are pure symmetry, and whether the nonlinear equation can actually realize them. This separation is the foundation of instanton and monopole moduli theory.

## Coulomb Gauge and Local Moduli: Removing Redundant Directions

Imagine trying to find the geometry of all connections satisfying a differential equation. A connection can be described by a one-form in each chart. But that description is redundant: infinitely many one-forms related by gauge transformations describe the same geometric connection. If we blindly linearize the equation, some directions of change are merely changes of coordinates in the bundle.

To do analysis, we need a local rule that selects a manageable representative from each nearby gauge orbit. One such rule is a Coulomb gauge condition. Its name recalls the divergence-free condition of electromagnetism, but here it is a geometric statement involving the adjoint of a covariant derivative.

### The elementary abelian model

Start with a unitary line bundle over a region where it is trivial. Its connection one-form is imaginary valued. A gauge transformation is a circle-valued function, and it shifts the connection one-form by an exact imaginary one-form. If we write the gauge as the exponential of a real phase, the shift is the differential of that phase, times the imaginary unit.

Fix a reference connection and let a denote the difference from that reference. The simplest Coulomb condition says the divergence of a is zero, or in the language of forms, its codifferential is zero. We seek a gauge phase whose differential removes the divergence part of a.

This requires solving a Laplace equation for the phase. On a closed connected manifold, constants lie in the kernel of the scalar Laplacian, and the right-hand side has integral zero automatically. So a solution exists after choosing the phase's average to be zero. The remaining constant gauges are stabilizers: they act trivially on an abelian connection.

Already we can see why a gauge condition is a local slice, not a universal one-to-one coordinate system. The constant ambiguity survives, and large gauge transformations with nonzero winding can identify different representatives that satisfy the same divergence condition.

### Nonabelian Coulomb gauge

For a connection with a noncommutative structure group, the transformation law contains both a derivative term and a conjugation term. Fix a smooth connection A nought. A nearby connection is A nought plus a Lie-algebra-valued one-form a. The Coulomb slice uses the formal adjoint of the covariant derivative at A nought: the covariant divergence of a is set to zero.

To find a small gauge transformation bringing the connection into the slice, linearize the gauge-fixing equation in an infinitesimal Lie-algebra-valued function. The leading operator is the covariant Laplacian: derivative, then adjoint derivative. On a compact manifold it is elliptic. If we restrict away from its kernel, the implicit function theorem supplies a local solution under appropriate Sobolev regularity and smallness conditions.

The kernel consists of covariantly constant infinitesimal gauge transformations, which are precisely the infinitesimal stabilizers of the reference connection. For an irreducible SU-two connection, that Lie-algebra kernel vanishes: its remaining central stabilizer is discrete. At a reducible connection, a continuous stabilizer may remain, and the local quotient can be singular.

### A finite-dimensional picture of the same problem

Picture an ordinary sphere and a symmetry group rotating it around the vertical axis. Away from the poles, nearby group orbits are circles, and a short transverse segment can meet each nearby orbit once. At a pole, the whole rotation group stabilizes the point. A naive transverse coordinate picture changes because the orbit size collapses.

Gauge theory follows the same logic in an infinite-dimensional setting. The slice gives local transverse directions. Stabilizers control how those directions are identified. A slice theorem does not prove there is one globally preferred gauge throughout the entire space of connections.

### The Kuranishi reduction

Now impose a nonlinear equation, such as anti-self-duality of the curvature. On the Coulomb slice, its linearization is the gauge-fixed elliptic operator we met in the deformation-complex lecture. Ellipticity splits the local function space into a finite-dimensional kernel and a closed complement. The implicit function theorem can solve the equation in the complement as a function of the kernel coordinates, subject to a finite-dimensional obstruction equation.

The surviving finite-dimensional map is called a Kuranishi map. Its source is closely related to first deformation cohomology, and its target to the obstruction space in second cohomology. Zeros of that map, modulo the residual stabilizer, model the moduli space locally.

If the obstruction space vanishes and the stabilizer is discrete, the quotient is locally a smooth manifold with dimension given by the deformation-space dimension. If not, we may obtain a singular zero set or a quotient singularity. Those are mathematical features of the moduli space, not failures of notation.

### Why function spaces matter here

The nonlinear curvature map includes the product of two connection perturbations. To run the implicit function theorem, that product must be continuous between the chosen Banach spaces, and the gauge group must act smoothly at the required regularity. On a four-manifold, one often works with Sobolev exponents strictly above critical thresholds for a clean Banach Lie group setup, then uses regularity to compare with smooth solutions.

The weak first-Sobolev estimates from earlier lectures are central to compactness questions, but a local slice theorem at exactly critical regularity can require subtler arguments. These are different uses of Sobolev theory and should not be combined into an unsupported statement that any bounded weak connection has a unique smooth gauge.

We have now built the local analytic scaffold of gauge moduli. The gauge condition removes redundant infinitesimal directions, ellipticity leaves finite-dimensional data, and the nonlinear equation produces an obstruction map. When advanced lectures refer to a 'moduli space cut out transversely,' this is the structure behind the phrase.

## Instanton Expected Dimension: What the Index Really Counts

For a moment, forget the spectacular four-manifold applications of instantons. We have a more basic mathematical problem. A connection on a bundle over a four-manifold must satisfy an equation involving its curvature. We identify connections related by gauge transformations. What can we predict about the family of solutions using topology alone?

The elliptic deformation complex provides an integer called the expected, or virtual, dimension. In the case of an SU-two bundle, its formula involves a topological charge and just three familiar Betti-number ingredients. But the meaning of that formula depends on exactly what has been subtracted and on whether the moduli space is regular.

### Count constraints, subtract symmetries

A connection perturbation is a one-form with values in the three-dimensional Lie algebra of SU-two. At each point of a four-manifold, that suggests twelve coefficient directions. The anti-self-dual equation constrains the self-dual part of curvature: a self-dual two-form has three components, giving nine equation components after accounting for the Lie algebra.

The gauge group provides three infinitesimal symmetry directions. Twelve minus nine minus three is zero in this crude pointwise arithmetic. Yet actual instanton moduli spaces often have positive dimension. Why did this naive count miss something?

Because differentiation couples different points. A differential equation's global degrees of freedom are controlled by the kernel and cokernel of an elliptic operator, not by subtracting the number of coefficients at one point. The correction depends on the topology of the underlying manifold and bundle. The Fredholm index is the right global count.

### The anti-self-dual elliptic operator

At an anti-self-dual connection, the first deformation map sends a Lie-algebra-valued function to its covariant derivative. The second sends a Lie-algebra-valued one-form to the self-dual part of its covariant exterior derivative. A Coulomb gauge condition adds the adjoint of the first map. Together they produce a Fredholm operator from one-forms to functions plus self-dual two-forms.

Its index equals the dimension of infinitesimal deformations minus the dimensions of infinitesimal stabilizers and obstructions. If the connection is irreducible and regular, stabilizers have no Lie-algebra directions and the obstruction space vanishes. Then the index equals the actual local moduli dimension. If either hypothesis fails, the relation must be interpreted more carefully.

For an SU-two bundle of second Chern number k on a connected closed oriented four-manifold, the index is eight times k minus three times the quantity one minus the first Betti number plus the dimension of positive second cohomology. That last dimension is usually called b-plus: the number of positive eigenvalues of the intersection form.

### Check the formula on a four-sphere

A four-sphere has no first cohomology and no second cohomology. So the parenthesized quantity is one. The expected dimension becomes eight k minus three. For charge one, it is five.

There is a geometrically suggestive five-parameter family of charge-one instantons on the round four-sphere, seen in a stereographic chart: four parameters for the center and one for the scale. Gauge orientation parameters are removed when we quotient by the full unframed gauge group. The five predicted dimensions are therefore visible in a concrete family.

That is a useful check, not a proof that every instanton moduli component is a smooth five-manifold. The chart description has limiting degenerations, and compactifying the moduli space introduces additional boundary phenomena. We will study the concentration of scale in later lectures.

### What happens at charge zero?

The same formula on a four-sphere gives minus three when k is zero. A negative expected dimension does not mean there is a manifold with negative dimension. The trivial flat connection exists, but it is reducible in the sense that the full SU-two group stabilizes it. Its infinitesimal stabilizer has dimension three. At that point, the index calculation includes a negative contribution from symmetry that a regular irreducible solution would not have.

This is a clean illustration of why an index can be negative without forcing the solution set to be empty. Under generic perturbations or suitable restrictions, negative expected dimension can imply absence of regular solutions, but that is an additional statement.

### A second topological way to write the count

On a closed oriented four-manifold, the Euler characteristic and the signature encode the same Betti-number combination. For a connected manifold, one minus b-one plus b-plus equals half the sum of Euler characteristic and signature.

So the expected dimension may also be written as eight k minus three halves of Euler characteristic plus signature. This version reveals that the index is built from characteristic numbers. It is not an arbitrary combinatorial count.

For Donaldson theory, the dimensions of moduli spaces tell us what degree of cohomology classes must be paired to obtain numerical invariants. For Seiberg-Witten theory, a related but different Fredholm calculation includes a spin-C Dirac index and the abelian gauge-curvature complex. The two moduli theories therefore have different expected-dimension formulas.

The key point is conceptual. An index measures the balance of infinitesimal deformation, symmetry, and obstruction. When transversality and irreducibility let that balance become an actual manifold dimension, topology has predicted the dimension of a nonlinear solution space. When those hypotheses fail, the same index remains meaningful as a virtual count, but we must not confuse the virtual answer with the geometry actually present.

## Instantons: Curvature, Topological Charge, and Gauge Moduli

Imagine a curved geometric object with an internal symmetry attached to each point. A connection tells us how to compare the internal states at neighboring points. Move around a tiny loop, and the comparison may fail to return exactly to where it started. That failure is curvature.

In gauge theory, the connection is the unknown field. The curvature is not merely a scalar: it is a two-form taking values in the Lie algebra of the symmetry group. Its size gives an energy, and a natural Euler–Lagrange equation asks for critical points of that energy.

In four dimensions a special simplification occurs. The Hodge star sends two-forms to two-forms, and applying it twice returns the original form. This splits curvature into a self-dual part and an anti-self-dual part. Setting either part to zero gives a first-order equation that automatically solves the second-order Yang–Mills equation. These special solutions are called instantons, with the precise self-duality convention depending on orientation.

The remarkable point is that the least possible Yang–Mills energy in a fixed topological sector is controlled by an integer. Curvature, analysis, and topology meet in one inequality.

## How the Hodge star makes four dimensions special

On an oriented Riemannian four-manifold, the Hodge star acts on ordinary two-forms by replacing an oriented two-plane element with its complementary oriented two-plane. Apply it again and the two-form returns. So the space of two-forms decomposes into the plus-one and minus-one eigenspaces.

Every curvature two-form therefore splits into a self-dual part and an anti-self-dual part. These components are orthogonal in the metric induced by the Riemannian structure. The Yang–Mills energy is their squared norms added together.

The wedge product of curvature with itself measures a different combination: the difference of the two squared norms, with a sign depending on orientation and trace conventions. When integrated with the proper normalization for an SU two bundle, this expression gives the second Chern number, an integer.

Now compare a sum of two nonnegative numbers with the absolute value of their difference. The sum must be at least the absolute difference. Applied to curvature, this immediately gives a lower bound on energy by the absolute topological charge. Equality holds exactly when one of the two curvature components vanishes.

This inequality is often called a Bogomolny bound. It is not a numerical observation about a particular solution. It comes from the algebraic decomposition of two-forms and Chern–Weil theory.

## From the first-order equation to Yang–Mills

The Yang–Mills equation says the covariant divergence of curvature is zero. The curvature also satisfies the Bianchi identity, a geometric identity obeyed by every connection.

For a self-dual or anti-self-dual connection, the Hodge star of curvature equals plus or minus curvature. Substitute this into the Yang–Mills equation. The covariant derivative of the Hodge dual becomes, up to sign, the covariant derivative of curvature, which vanishes by Bianchi. Thus every smooth instanton solves Yang–Mills.

The converse is false. A general Yang–Mills critical point may have both curvature components nonzero. The first-order equation identifies special minima of the action in their topological sector, not all critical points.

## Gauge symmetry changes what counts as a solution

Different formulas for a connection can describe the same geometry. Change a local frame in the bundle and the connection one-form transforms, acquiring an inhomogeneous term. The curvature transforms by conjugation. The Yang–Mills energy, the instanton equation, and characteristic classes remain gauge invariant.

Therefore a moduli problem must identify gauge-equivalent connections. Merely counting coordinate formulas would count the same geometry many times. The space of connections modulo gauge transformations is infinite-dimensional before imposing a differential equation. The instanton equation cuts out a space that is often finite-dimensional after appropriate elliptic analysis and quotienting, though singular points can remain where a connection has extra stabilizers.

Linearizing the instanton equation, and then accounting for infinitesimal gauge transformations, gives an elliptic deformation complex. Its index predicts the expected dimension of the moduli space. This is a topological number involving the second Chern class and Betti numbers of the underlying four-manifold.

## A five-parameter family on the four-sphere

For SU two bundles on the round four-sphere, the basic charge-one instanton has five familiar parameters after quotienting by gauge transformations. Four specify its center in a stereographic chart, and one specifies its scale. The expected dimension formula gives five, agreeing with that picture.

Move the center and the curvature concentrates elsewhere. Change the scale and the curvature spreads out or contracts. The Yang–Mills energy stays at its topological minimum, because a conformal change of scale in dimension four preserves the relevant action.

This family also shows why moduli spaces require compactification. As the scale shrinks toward zero, curvature can concentrate in smaller and smaller regions. A sequence of instantons may fail to converge smoothly as a sequence of connections even though its energy remains bounded. Uhlenbeck compactness allows controlled limits together with bubbling data that records lost topological charge.

There is no equivalent nontrivial SU two instanton phenomenon on every four-manifold for every charge. Bundle topology and the geometry of the base impose constraints. Even when the expected dimension is positive, a moduli space may be empty or obstructed.

## How instantons detect smooth structure

Donaldson's work used moduli spaces of anti-self-dual connections to construct invariants of smooth four-manifolds. The moduli spaces and their compactifications can record intersection data and constrain which smooth structures exist on a topological four-manifold.

One should not compress this achievement into the claim that an instanton count identifies every smooth structure. The invariants require orientations, transversality or perturbations, compactness and careful treatment of reducible connections; distinct manifolds can share invariants. The important conceptual point is that an analytic moduli space of curvature equations produces information about the topology and smooth structure of the underlying manifold.

A useful comparison is with ordinary de Rham cohomology. Closed forms detect topology through linear differential equations. Instantons introduce nonlinear curvature equations coupled to a gauge quotient, and the resulting moduli spaces can see subtler four-dimensional information.

## The geometry behind the integer

The core story has four stages. A connection produces curvature. In four dimensions, curvature splits into self-dual and anti-self-dual pieces. Their squared norms bound a characteristic number, and equality forces a first-order PDE. Finally, identify solutions related by gauge transformations and study the resulting moduli space.

The integer topological charge is not an arbitrary label attached after finding a solution. It already appears in the energy inequality that tells us which solutions are geometrically distinguished. Four-dimensional geometry makes an infinite-dimensional variational problem answerable, in part, with topology.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Deformation Complexes: Tangents, Symmetries, and Obstructions

**Track:** Topology and Geometry. **Background:** chain complexes, gauge connections, covariant exterior derivative, Fredholm operators. **Central question:** how can a nonlinear equation with symmetries have a finite-dimensional local space of solutions?

#### Mathematical companion (not spoken)

For an ASD connection \(A\) on \(P\to X^4\), the deformation complex is
\[0\longrightarrow\Omega^0(\operatorname{ad}P)\xrightarrow{d_A}\Omega^1(\operatorname{ad}P)\xrightarrow{d_A^+}\Omega^{2,+}(\operatorname{ad}P)\longrightarrow0.\]
The identity \(d_A^+d_A\phi=[F_A^+,\phi]\) makes this a complex only at a solution with \(F_A^+=0\) (or under a special central-curvature modification). Its cohomology spaces are
\[H_A^0=\ker d_A,\quad H_A^1=\ker d_A^+/\operatorname{im}d_A,\quad H_A^2=\operatorname{coker}d_A^+.\]
The Fredholm gauge-fixed operator \(\mathcal D_A=d_A^*\oplus d_A^+:\Omega^1(\operatorname{ad}P)\to\Omega^0(\operatorname{ad}P)\oplus\Omega^{2,+}(\operatorname{ad}P)\) has
\[\operatorname{ind}\mathcal D_A=\dim H_A^1-\dim H_A^0-\dim H_A^2.\]
Symbol exactness holds for \(\xi\ne0\): \(\operatorname{im}(\xi\otimes\cdot)=\ker(\pi_+\circ(\xi\wedge\cdot))\) on one-forms tensored with \(\operatorname{ad}P\), using \(\dim\Omega^1=4\), \(\dim\Omega^{2,+}=3\). On a circle, the abelian flat-connection tangent quotient \(\Omega^1/d\Omega^0\cong H^1(S^1;i\mathbb R)\) is real one-dimensional; the global quotient by large gauges is \(U(1)\) holonomy.

##### Exercises with answers

1. **Symmetry directions.** Why do infinitesimal gauge variations lie in the kernel of the linearized ASD equation at an ASD connection? **Answer:** \(d_A^+d_A\phi=[F_A^+,\phi]=0\).
2. **First cohomology.** What does \(H_A^1\) represent? **Answer:** infinitesimal solutions modulo infinitesimal gauge transformations.
3. **Obstructions.** What does \(H_A^2\) measure? **Answer:** failure of surjectivity of the linearized equation after quotienting, hence possible nonlinear obstructions.
4. **Dimension.** Does a Fredholm index by itself imply a smooth moduli space? **Answer:** no; reducibles and nonzero obstruction spaces may create singularities.

##### Sources and further reading

- Daniel Freed and Karen Uhlenbeck, [Instantons and Four-Manifolds](https://doi.org/10.1007/978-1-4613-9703-8) (book; publisher access may apply).
- Tim Perutz, [Lectures on gauge theory and symplectic geometry](https://web.ma.utexas.edu/users/perutz/Northwestern/NorthwesternL3.pdf).
- Overviews: [Instanton](https://en.wikipedia.org/wiki/Instanton), [Elliptic complex](https://en.wikipedia.org/wiki/Elliptic_complex), [Moduli space](https://en.wikipedia.org/wiki/Moduli_space).

### Coulomb Gauge and Local Moduli: Removing Redundant Directions

**Track:** Topology and Geometry. **Background:** covariant derivatives, adjoints, implicit function theorem, Sobolev spaces, deformation complexes. **Central question:** how do we turn a gauge-invariant equation into a local elliptic problem without pretending the gauge symmetry disappears globally?

#### Mathematical companion (not spoken)

For a unitary connection \(A\) and \(g:X\to U(1)\), \(A^g=A+g^{-1}dg\). In a local logarithm \(g=e^{i\phi}\), \(A^g=A+i\,d\phi\). If \(a=A-A_0\), Coulomb gauge relative to \(A_0\) requires \(d^*a=0\); solve \(\Delta\phi\) with a sign determined by \(d^*d\phi\) to reach the slice, modulo constants and large gauges.

For compact structure group \(G\), a local slice through \(A_0\) is \(d_{A_0}^*(A-A_0)=0\). Linearizing the gauge condition at the identity yields (up to sign) \(d_{A_0}^*d_{A_0}\xi\), an elliptic operator whose kernel is \(\ker d_{A_0}=H_{A_0}^0\). In a suitable Sobolev setup, invert the linearization perpendicular to its kernel and apply the Banach implicit function theorem to obtain a local slice. The nonlinear ASD equation in this slice has a local Kuranishi model
\[\{x\in H_A^1:\kappa(x)=0\}/\operatorname{Stab}(A),\qquad \kappa:H_A^1\to H_A^2,\quad \kappa(0)=0,\quad d\kappa_0=0.\]
Smoothness needs suitable transversality and control of the residual stabilizer. Do not infer a global gauge slice or a global unique representative from the local argument.

##### Exercises with answers

1. **Abelian gauge.** What equation determines an infinitesimal phase that imposes \(d^*a=0\)? **Answer:** a scalar Laplace equation with right side minus the divergence of the original perturbation, after fixing the sign convention.
2. **Stabilizer.** Why are constants an ambiguity for the abelian Laplacian? **Answer:** their derivatives vanish, so they do not change the connection.
3. **Reducibility.** What can fail at a reducible solution? **Answer:** the stabilizer may have positive dimension, affecting the local quotient.
4. **Obstructions.** What remains after solving the equation in the infinite-dimensional complement? **Answer:** a finite-dimensional Kuranishi obstruction map on deformation cohomology.

##### Sources and further reading

- Daniel Freed and Karen Uhlenbeck, [Instantons and Four-Manifolds](https://doi.org/10.1007/978-1-4613-9703-8), manifolds of connections and Sobolev gauge transformations.
- Karen Uhlenbeck, [Connections with L-p bounds on curvature](https://doi.org/10.1007/BF01947069), 1982.
- Overviews: [Gauge fixing](https://en.wikipedia.org/wiki/Gauge_fixing), [Yang-Mills theory](https://en.wikipedia.org/wiki/Yang%E2%80%93Mills_theory).

### Instanton Expected Dimension: What the Index Really Counts

**Track:** Topology and Geometry. **Background:** anti-self-dual deformation complex, Atiyah-Singer index, Betti numbers, gauge slices. **Central question:** how does topology predict the virtual dimension of an instanton moduli space, and why is that not always its actual dimension?

#### Mathematical companion (not spoken)

For an SU(2)-bundle \(P\to X^4\) on a connected closed oriented four-manifold, choose the instanton-number convention \(k=\langle c_2(P),[X]\rangle\) such that ASD instantons have \(k\geq0\) (with the compatible curvature trace convention of 034100). Let \(b^+(X)\) be the positive rank of the real intersection form. The ASD gauge-fixed Fredholm operator
\[\mathcal D_A=d_A^*\oplus d_A^+:\Omega^1(\operatorname{ad}P)\to\Omega^0(\operatorname{ad}P)\oplus\Omega^{2,+}(\operatorname{ad}P)\]
has real index
\[\operatorname{ind}_\mathbb R\mathcal D_A=8k-3(1-b_1(X)+b^+(X))=8k-\frac32(\chi(X)+\sigma(X)).\]
The index also equals \(\dim H_A^1-\dim H_A^0-\dim H_A^2\). At a regular irreducible solution, \(H_A^0=H_A^2=0\), so the local unframed moduli dimension equals the index. At a reducible solution, the stabilizer affects the quotient. For \(X=S^4\), \(b_1=b^+=0\), hence \(\operatorname{ind}=8k-3\). Charge one predicts five; at \(k=0\), the flat trivial solution has a three-dimensional infinitesimal stabilizer, explaining the index \(-3\) without invoking negative-dimensional geometry.

##### Exercises with answers

1. **Sphere.** Compute the expected SU(2) ASD dimension on \(S^4\) with \(k=2\). **Answer:** \(16-3=13\).
2. **Betti data.** What is \(1-b_1+b^+\) in terms of \(\chi\) and \(\sigma\)? **Answer:** \((\chi+\sigma)/2\).
3. **Regularity.** Which deformation cohomology spaces vanish at a regular irreducible solution? **Answer:** \(H_A^0\) and \(H_A^2\).
4. **Meaning.** Does expected dimension zero imply exactly one instanton? **Answer:** no; it makes no assertion about existence or the number of components or points.

##### Sources and further reading

- Daniel Freed and Karen Uhlenbeck, [Instantons and Four-Manifolds](https://doi.org/10.1007/978-1-4613-9703-8), instanton moduli and index.
- Tim Perutz, [Lectures on gauge theory and symplectic geometry](https://web.ma.utexas.edu/users/perutz/Northwestern/NorthwesternL3.pdf).
- Overviews: [Instanton](https://en.wikipedia.org/wiki/Instanton), [Donaldson theory](https://en.wikipedia.org/wiki/Donaldson_theory), [Intersection form of a 4-manifold](https://en.wikipedia.org/wiki/Intersection_form_of_a_4-manifold).

### Instantons: Curvature, Topological Charge, and Gauge Moduli

**Track:** Topology and Geometry. **Background:** connections, curvature two-forms, characteristic classes, Hodge star and elliptic operators. **Central question:** how can a differential equation for a connection detect a four-dimensional topological invariant?

#### Mathematical companion (not spoken)

Let X be a closed oriented Riemannian four-manifold and P a principal SU(2) bundle. For a connection A with curvature `F_A`, the Hodge decomposition is
\[
\Lambda^2=\Lambda^2_+\oplus\Lambda^2_-,\qquad
F_A^\pm=\tfrac12(F_A\pm *F_A).
\]
With the standard positive norm from `-tr` on `su(2)`, the Yang–Mills energy `YM(A)=int_X |F_A|^2` and the topological charge `k=c_2(P)[X]` satisfy `YM(A)>=8 pi^2 |k|` with the conventional normalization (some authors include a factor one half in the action and alter the numerical coefficient). Equality corresponds to `F_A^+=0` or `F_A^-=0`, depending on orientation and sign of k. Since `d_A F_A=0` (Bianchi), a (anti-)self-dual connection satisfies `d_A *F_A=0`.

The deformation complex for ASD connections is
\[
0\longrightarrow\Omega^0(X,\operatorname{ad}P)\xrightarrow{d_A}
\Omega^1(X,\operatorname{ad}P)\xrightarrow{d_A^+}
\Omega^2_+(X,\operatorname{ad}P)\longrightarrow0.
\]
Its expected (virtual) dimension for irreducible SU2 connections is `8k-3(1-b_1(X)+b_+(X))` using the charge convention with k positive for ASD. On `S^4`, `b_1=b_+=0`, so for `k=1` it is five. The index does not alone guarantee smoothness or nonemptiness.

##### Exercises with answers

1. Why is four dimensions special for the star operator on two-forms? **Answer:** it maps two-forms back to two-forms and squares to the identity in the Riemannian oriented case.
2. Does every Yang–Mills solution satisfy the ASD equation? **Answer:** no; ASD is sufficient but not necessary for the second-order equation.
3. What must be quotiented out to get the instanton moduli space? **Answer:** gauge transformations of the underlying bundle.
4. What causes bubbling? **Answer:** a bounded-energy sequence can concentrate curvature at smaller scales and lose smooth compactness.

##### Reading and source notes

- [Donaldson and Kronheimer, The Geometry of Four-Manifolds](https://global.oup.com/academic/product/the-geometry-of-four-manifolds-9780198502692), ASD deformation complexes and gauge-theoretic topology.
- [Atiyah, Hitchin and Singer, Self-Duality in Four-Dimensional Riemannian Geometry](https://doi.org/10.1098/rspa.1978.0010), foundational geometric framework.
- [Freed and Uhlenbeck, Instantons and Four-Manifolds](https://link.springer.com/book/10.1007/978-1-4613-9703-8), compactness and instanton moduli.
