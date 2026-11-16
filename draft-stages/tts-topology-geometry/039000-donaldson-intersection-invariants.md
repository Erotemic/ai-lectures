# 039000 - Donaldson Invariants and the Smooth Topology of Four-Manifolds

**Track:** Topology and Geometry. **Background:** four-manifolds, connections and curvature, instanton moduli, and intersection forms. **Central question:** how can counting solutions of a differential equation reveal the smooth structure of a manifold?

<!-- BEGIN SPOKEN LECTURE -->

# Topology is not the whole story in dimension four

Two spaces can be homeomorphic yet fail to be diffeomorphic. Homeomorphism preserves topological continuity; diffeomorphism also preserves smooth coordinate changes. In most elementary geometry, we rarely separate these concepts because the standard examples offer one obvious smooth structure.

Four-dimensional manifolds make the distinction impossible to ignore. A topological four-manifold can support smooth structures that are not equivalent by diffeomorphism. Donaldson's gauge theory opened a way to study the difference by using the geometry of connections on bundles.

The starting object is not a combinatorial triangulation. It is a nonlinear differential equation: the anti-self-dual Yang–Mills equation. Its solutions, organized into a moduli space and then integrated against cohomology classes, produce invariants of smooth four-manifolds.

# The instanton equation

Choose an oriented Riemannian four-manifold and a principal bundle with structure group SU two, or an equivalent suitable rank-two bundle description. A connection describes how to differentiate sections. Its curvature is a two-form taking values in a Lie algebra.

In four dimensions, the Hodge star on two-forms squares to the identity. Thus two-forms split into self-dual and anti-self-dual parts. An anti-self-dual connection has zero self-dual curvature component.

This is a first-order nonlinear elliptic equation after fixing gauge appropriately. The solutions have infinite-dimensional descriptions before quotienting by gauge transformations, because one can alter a connection by changes of bundle frame. The moduli space identifies connections related by such transformations.

At an irreducible regular solution, the moduli space behaves locally like a finite-dimensional smooth manifold. The expected dimension comes from the index of an elliptic deformation complex. The dimension formula connects bundle topology to the intersection form of the underlying four-manifold.

# A dimension calculation on a K3 surface

Consider a K3 surface with its standard orientation. It is simply connected and has three independent positive directions in its second cohomology intersection form. For an SU-two bundle with second Chern number k, the expected dimension of the anti-self-dual moduli space is eight times k minus three times one plus the positive Betti number, in the simply connected case.

For k equal to three, that gives twenty-four minus twelve, or twelve. This is an index calculation. It does not mean the moduli space is guaranteed to be nonempty, compact, or smooth for every metric. It tells us the dimension we expect at regular irreducible connections under the stated conditions.

The number twelve can then be paired with cohomology classes from the original four-manifold. A two-dimensional homology class gives a degree-two cohomology class on the instanton moduli space via the so-called mu map. Six such insertions have total cohomological degree twelve. In a suitable compactified and oriented setting, their product can be evaluated to give a number.

This number is not obtained merely by observing that the degrees add up. We still require transversality, compactification, and control of boundary contributions. The dimension check tells us which evaluations can be meaningful.

# Why a moduli integral can be invariant

The anti-self-dual equation uses a Riemannian metric, so the solutions themselves change when the metric changes. How can integrating over their moduli space yield a smooth-topological invariant?

The answer is to consider a family of metrics and the corresponding family of equations. If the moduli spaces fit into an appropriate oriented cobordism and no uncontrolled solutions escape through boundaries, the integrals of closed cohomology classes remain unchanged. Uhlenbeck compactness is central here: curvature can concentrate and form bubbles, so the naive moduli space need not be compact.

Donaldson's construction handles this geometry through careful compactification and dimension arguments. Under standard conditions, including positive Betti number greater than one, the resulting polynomial invariants are independent of generic metric choices. When the positive Betti number equals one, wall-crossing between chambers can occur and must be accounted for separately.

The conditions are essential. One should not simply say that every instanton count on every four-manifold is automatically an invariant.

# The intersection form becomes rigid

The intersection form of a closed oriented four-manifold measures how second-dimensional homology classes intersect. Donaldson's diagonalization theorem shows that the intersection form of a smooth, closed, simply connected, definite four-manifold is equivalent over the integers to a diagonal form with entries all plus one or all minus one, according to orientation.

This is a surprising restriction. Topological four-manifold theory allows definite unimodular forms that cannot be realized by smooth simply connected closed four-manifolds. Gauge-theoretic analysis therefore distinguishes possibilities invisible to a naive classification by homeomorphism alone.

The polynomial invariants go further. They can distinguish certain smooth manifolds that share many ordinary topological invariants. Later Seiberg–Witten theory gave another approach using different gauge equations, often with simpler moduli spaces, but it did not erase the geometric content of instanton theory.

# What the invariant is actually counting

It is tempting to describe Donaldson invariants as literal counts of instantons. Sometimes zero-dimensional moduli spaces do permit signed counts. In positive dimension, however, the construction evaluates cohomology classes on a fundamental cycle of the moduli space. Geometric cycles and cut-down moduli spaces can turn such integrals into signed intersection counts, but only with transversality and orientation in place.

This is a general lesson in moduli theory. A number associated with a space of solutions is not necessarily the cardinality of that space. It is often an intersection number after imposing enough geometric conditions to reach dimension zero.

Gauge theory converts an analytic problem into differential topology through a sequence of ideas: the curvature equation, elliptic index, moduli-space compactification, cohomological insertions, and deformation invariance. Its force comes from the combination. Removing the analytic control breaks the topological conclusion; removing the topology loses the significance of the solutions.

Donaldson invariants are therefore a model of a powerful mathematical strategy: study a space by placing a nonlinear equation on it, then ask what properties of the equation's complete solution space survive all permissible geometric changes.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For a closed, simply connected, oriented smooth four-manifold `X`, and an `SU(2)` bundle with `c_2=k`, the expected dimension of the regular irreducible ASD moduli space is
\[
\operatorname{vdim}\mathcal M_k=8k-3(1+b_2^+(X)).
\]
More generally `8k-3(1-b_1+b_2^+)`. On standardly oriented `K3`, `b_1=0`, `b_2^+=3`, so for `k=3` the expected dimension is `24-12=12`. The `mu`-map associates degree-`4-j` classes to `j`-dimensional homology insertions. Six homology-2 insertions yield total degree 12; an actual invariant requires the moduli-space orientation, compactification, and regularity procedures, and the dimension count alone does **not** assert nonvanishing.

Donaldson's diagonalization theorem restricts definite intersection forms of closed smooth simply connected four-manifolds to integral diagonal forms with signs fixed by definiteness. Polynomial invariants have additional hypotheses; with `b_2^+=1`, chamber dependence may arise.

### Exercises with answers

1. What is the formal ASD moduli dimension on `K3` when `k=2`? **Answer:** `16-12=4`.
2. How many `mu`-classes of degree two fill virtual dimension 12? **Answer:** six.
3. Why is a noncompact moduli space a problem for integration? **Answer:** sequences of solutions can escape; bubbling and boundary phenomena obstruct naive deformation invariance.
4. What does the index calculation not establish? **Answer:** existence, regularity, compactness, or nonzero invariant value.

### Reading and source notes

- [Donaldson and Kronheimer, The Geometry of Four-Manifolds](https://doi.org/10.1093/oso/9780198535539.001.0001), ASD moduli and Donaldson invariants.
- [Morgan, Gauge Theory and Four-Manifold Topology (lecture notes)](https://www.pdmi.ras.ru/EIMI/2013/morgan.pdf), index and invariant constructions.
- [Donaldson, An Application of Gauge Theory to Four-Dimensional Topology](https://doi.org/10.4310/JDG/1214437665), smooth intersection-form restrictions.
