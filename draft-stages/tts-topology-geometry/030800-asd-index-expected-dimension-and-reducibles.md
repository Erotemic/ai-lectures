# 030800 - Instanton Expected Dimension: What the Index Really Counts

**Track:** Topology and Geometry. **Background:** anti-self-dual deformation complex, Atiyah-Singer index, Betti numbers, gauge slices. **Central question:** how does topology predict the virtual dimension of an instanton moduli space, and why is that not always its actual dimension?

<!-- BEGIN SPOKEN LECTURE -->

# Instanton Expected Dimension: What the Index Really Counts

For a moment, forget the spectacular four-manifold applications of instantons. We have a more basic mathematical problem. A connection on a bundle over a four-manifold must satisfy an equation involving its curvature. We identify connections related by gauge transformations. What can we predict about the family of solutions using topology alone?

The elliptic deformation complex provides an integer called the expected, or virtual, dimension. In the case of an SU-two bundle, its formula involves a topological charge and just three familiar Betti-number ingredients. But the meaning of that formula depends on exactly what has been subtracted and on whether the moduli space is regular.

## Count constraints, subtract symmetries

A connection perturbation is a one-form with values in the three-dimensional Lie algebra of SU-two. At each point of a four-manifold, that suggests twelve coefficient directions. The anti-self-dual equation constrains the self-dual part of curvature: a self-dual two-form has three components, giving nine equation components after accounting for the Lie algebra.

The gauge group provides three infinitesimal symmetry directions. Twelve minus nine minus three is zero in this crude pointwise arithmetic. Yet actual instanton moduli spaces often have positive dimension. Why did this naive count miss something?

Because differentiation couples different points. A differential equation's global degrees of freedom are controlled by the kernel and cokernel of an elliptic operator, not by subtracting the number of coefficients at one point. The correction depends on the topology of the underlying manifold and bundle. The Fredholm index is the right global count.

## The anti-self-dual elliptic operator

At an anti-self-dual connection, the first deformation map sends a Lie-algebra-valued function to its covariant derivative. The second sends a Lie-algebra-valued one-form to the self-dual part of its covariant exterior derivative. A Coulomb gauge condition adds the adjoint of the first map. Together they produce a Fredholm operator from one-forms to functions plus self-dual two-forms.

Its index equals the dimension of infinitesimal deformations minus the dimensions of infinitesimal stabilizers and obstructions. If the connection is irreducible and regular, stabilizers have no Lie-algebra directions and the obstruction space vanishes. Then the index equals the actual local moduli dimension. If either hypothesis fails, the relation must be interpreted more carefully.

For an SU-two bundle of second Chern number k on a connected closed oriented four-manifold, the index is eight times k minus three times the quantity one minus the first Betti number plus the dimension of positive second cohomology. That last dimension is usually called b-plus: the number of positive eigenvalues of the intersection form.

## Check the formula on a four-sphere

A four-sphere has no first cohomology and no second cohomology. So the parenthesized quantity is one. The expected dimension becomes eight k minus three. For charge one, it is five.

There is a geometrically suggestive five-parameter family of charge-one instantons on the round four-sphere, seen in a stereographic chart: four parameters for the center and one for the scale. Gauge orientation parameters are removed when we quotient by the full unframed gauge group. The five predicted dimensions are therefore visible in a concrete family.

That is a useful check, not a proof that every instanton moduli component is a smooth five-manifold. The chart description has limiting degenerations, and compactifying the moduli space introduces additional boundary phenomena. We will study the concentration of scale in later lectures.

## What happens at charge zero?

The same formula on a four-sphere gives minus three when k is zero. A negative expected dimension does not mean there is a manifold with negative dimension. The trivial flat connection exists, but it is reducible in the sense that the full SU-two group stabilizes it. Its infinitesimal stabilizer has dimension three. At that point, the index calculation includes a negative contribution from symmetry that a regular irreducible solution would not have.

This is a clean illustration of why an index can be negative without forcing the solution set to be empty. Under generic perturbations or suitable restrictions, negative expected dimension can imply absence of regular solutions, but that is an additional statement.

## A second topological way to write the count

On a closed oriented four-manifold, the Euler characteristic and the signature encode the same Betti-number combination. For a connected manifold, one minus b-one plus b-plus equals half the sum of Euler characteristic and signature.

So the expected dimension may also be written as eight k minus three halves of Euler characteristic plus signature. This version reveals that the index is built from characteristic numbers. It is not an arbitrary combinatorial count.

For Donaldson theory, the dimensions of moduli spaces tell us what degree of cohomology classes must be paired to obtain numerical invariants. For Seiberg-Witten theory, a related but different Fredholm calculation includes a spin-C Dirac index and the abelian gauge-curvature complex. The two moduli theories therefore have different expected-dimension formulas.

The key point is conceptual. An index measures the balance of infinitesimal deformation, symmetry, and obstruction. When transversality and irreducibility let that balance become an actual manifold dimension, topology has predicted the dimension of a nonlinear solution space. When those hypotheses fail, the same index remains meaningful as a virtual count, but we must not confuse the virtual answer with the geometry actually present.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For an SU(2)-bundle \(P\to X^4\) on a connected closed oriented four-manifold, choose the instanton-number convention \(k=\langle c_2(P),[X]\rangle\) such that ASD instantons have \(k\geq0\) (with the compatible curvature trace convention of 034100). Let \(b^+(X)\) be the positive rank of the real intersection form. The ASD gauge-fixed Fredholm operator
\[\mathcal D_A=d_A^*\oplus d_A^+:\Omega^1(\operatorname{ad}P)\to\Omega^0(\operatorname{ad}P)\oplus\Omega^{2,+}(\operatorname{ad}P)\]
has real index
\[\operatorname{ind}_\mathbb R\mathcal D_A=8k-3(1-b_1(X)+b^+(X))=8k-\frac32(\chi(X)+\sigma(X)).\]
The index also equals \(\dim H_A^1-\dim H_A^0-\dim H_A^2\). At a regular irreducible solution, \(H_A^0=H_A^2=0\), so the local unframed moduli dimension equals the index. At a reducible solution, the stabilizer affects the quotient. For \(X=S^4\), \(b_1=b^+=0\), hence \(\operatorname{ind}=8k-3\). Charge one predicts five; at \(k=0\), the flat trivial solution has a three-dimensional infinitesimal stabilizer, explaining the index \(-3\) without invoking negative-dimensional geometry.

### Exercises with answers

1. **Sphere.** Compute the expected SU(2) ASD dimension on \(S^4\) with \(k=2\). **Answer:** \(16-3=13\).
2. **Betti data.** What is \(1-b_1+b^+\) in terms of \(\chi\) and \(\sigma\)? **Answer:** \((\chi+\sigma)/2\).
3. **Regularity.** Which deformation cohomology spaces vanish at a regular irreducible solution? **Answer:** \(H_A^0\) and \(H_A^2\).
4. **Meaning.** Does expected dimension zero imply exactly one instanton? **Answer:** no; it makes no assertion about existence or the number of components or points.

### Sources and further reading

- Daniel Freed and Karen Uhlenbeck, [Instantons and Four-Manifolds](https://doi.org/10.1007/978-1-4613-9703-8), instanton moduli and index.
- Tim Perutz, [Lectures on gauge theory and symplectic geometry](https://web.ma.utexas.edu/users/perutz/Northwestern/NorthwesternL3.pdf).
- Overviews: [Instanton](https://en.wikipedia.org/wiki/Instanton), [Donaldson theory](https://en.wikipedia.org/wiki/Donaldson_theory), [Intersection form of a 4-manifold](https://en.wikipedia.org/wiki/Intersection_form_of_a_4-manifold).
