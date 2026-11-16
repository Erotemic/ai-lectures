# 031300 — A Complete Lagrangian Floer Model: Two Graphs over a Circle

**Track:** Topology and Geometry. **Background:** cotangent bundle graphs, exact Lagrangians, Morse homology, holomorphic strips and compactness. **Central question:** how do the geometry and the algebra fit together in a model that can be calculated from start to finish?

<!-- BEGIN SPOKEN LECTURE -->

# A Complete Lagrangian Floer Model: Two Graphs over a Circle

We have assembled many pieces of symplectic geometry: Lagrangian submanifolds, elliptic equations on strips, Maslov indices, area identities, compactness, and chain complexes. It is time to put them together in a single calculation.

Our position space will be a circle. The phase space will be its cotangent bundle, a cylinder carrying position around the circle and momentum along the cylinder's height. We will choose two Lagrangian circles and compute their Floer homology in a small-graph model.

## Choose two Lagrangian circles

The first Lagrangian is the zero section: all positions, with momentum equal to zero. The second is the graph of the derivative of a function. Choose the function cosine of two pi times position, where position is measured modulo one full turn.

The derivative vanishes at exactly two places: one maximum and one minimum. Therefore the second graph intersects the zero section at exactly two points. Both intersections are transverse because the function has a nonzero second derivative there.

If we thought only in terms of intersection counts, we might conclude that there are two special points and stop. Floer theory asks something deeper. It treats the intersections as generators of a chain complex and counts connecting holomorphic strips to define a boundary operator.

## Why these Lagrangians are exact

The cotangent bundle has a natural symplectic form, and the zero section is exact. The derivative graph is also exact. In our sign convention, the natural primitive of the symplectic form restricts to minus the derivative of the function along the second graph.

Exactness makes two later steps much more manageable. First, the action of a path between the two Lagrangians can be defined using the endpoint primitives, without ambiguity from choosing a spanning surface. Second, there can be no nonconstant compatible holomorphic disk bubble whose whole boundary lies on either exact Lagrangian, because its area would be zero.

But the ambient cotangent bundle is noncompact. We still have to choose tame almost-complex data and appropriate small-graph or confinement conditions to prevent strips from escaping to infinite momentum. We will work in that controlled standard setting.

## The action of a constant chord

Think of a path that starts on the zero section and ends on the derivative graph. When the Hamiltonian is zero, the stationary paths are constant paths at intersection points.

For such a constant path, the path integral of the ambient primitive vanishes. The endpoint correction uses the primitive on the second Lagrangian, which is minus the original function f. Thus the action at an intersection is minus the value of f at that critical point, with our conventions.

The two intersections therefore have opposite action values. This is analogous to the two critical points of the Morse function, with the direction reversed by the sign of the action.

A Floer strip connecting them follows a negative gradient trajectory of the action. In the small-graph limit, solutions of the strip equation correspond to gradient trajectories of the original function, with the expected sign and grading adjustments.

## Two routes between the critical points

Draw the circle and mark the maximum at one position and the minimum opposite it. There are exactly two arcs connecting them. For the round metric, these arcs are the two ordinary Morse gradient trajectories from maximum to minimum.

In the small-graph Floer model, the corresponding holomorphic strips give two rigid connecting trajectories between the two intersection generators, after translation is removed. Working with coefficients modulo two, two contributions add to zero.

The chain complex therefore has two generators and a zero differential. Its homology has one generator in each of two consecutive degrees, just as the ordinary homology of the circle does: one for its connected component and one for its fundamental loop.

This is the first complete example where the conclusion of Lagrangian Floer theory can be checked against a familiar topological answer.

## What happens when the graph changes?

Suppose we replace cosine by a more complicated smooth function with several maxima and minima. Its derivative graph may intersect the zero section at many points. The chain complex becomes larger. But the extra generators can be paired by nonzero differential terms, and the homology remains that of the circle under the relevant Hamiltonian isotopy and continuation results.

The graph of a derivative is Hamiltonian isotopic to the zero section. In our canonical coordinates, a Hamiltonian depending only on position can shift momentum vertically by the derivative of a function. That is why changing the exact graph belongs to the kind of deformation Floer theory is designed to handle.

Now compare a circle at constant nonzero momentum. It is Lagrangian and symplectically translates the zero section, but its defining closed one-form has nonzero period around the circle. It is not an exact derivative graph. It need not intersect the zero section at all. There is no contradiction: we have left the Hamiltonian-isotopic exact-graph situation.

## Why the small-graph correspondence matters

The argument that Floer strips correspond to gradient trajectories is a genuine analytic theorem in the appropriate regime, not a definition of a strip. One chooses the geometry and graph sufficiently close to the zero section, analyzes the strip equation, and controls the solutions using elliptic estimates and energy bounds.

Then a Floer strip can be viewed as a slightly thickened version of a gradient line. When the graph becomes very small, the strip's leading behavior is governed by the Morse gradient equation. This comparison gives a bridge between classical topology and Floer homology.

We have now seen what each ingredient contributes. Exactness removes disk bubbles. The small-graph setup allows analytic control. Transverse intersections give generators. The Maslov and Morse indices determine the relevant degrees. The two rigid strips cancel in the differential. And continuation explains stability under allowed deformations.

## Beyond the simple model

More complicated Lagrangian Floer theories study submanifolds that are not exact, targets with holomorphic disk bubbles, and noncompact Lagrangians extending to infinity. Wrapped Floer homology, for example, uses Hamiltonians that grow at infinity and records additional intersection or chord information. Its construction needs careful asymptotic and compactness control that our little cylinder model does not supply.

But the architecture is already visible. Floer homology is not a mysterious replacement for counting intersections. It is a way of correcting a naive intersection count with the geometry of trajectories between intersections, so that the resulting algebra remembers topology under appropriate deformations.

The circle model is a good reference point whenever the advanced theory becomes difficult. Ask what corresponds to the two intersections, what corresponds to the two connecting arcs, which bubble types have been excluded, and what theorem keeps the answer invariant.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Work on \(T^*S^1\) with \(q\in\mathbb R/\mathbb Z\), momentum \(p\in\mathbb R\), \(\omega=dq\wedge dp=d\lambda\), and \(\lambda=-p\,dq\). Put \(L_0=\{p=0\}\) and \(L_1=\Gamma_{df}\) for \(f(q)=\epsilon\cos(2\pi q)\), \(\epsilon>0\) small. Then \(\lambda|_{L_0}=df_0=0\), \(\lambda|_{L_1}=df_1=-df\), so \(f_1=-f\). The intersections are the critical points \(q=0,1/2\) of \(f\). For a path \(x:[0,1]\to T^*S^1\), \(x(0)\in L_0\), \(x(1)\in L_1\), a consistent action is
\[
\mathcal A_{H,L_0,L_1}(x)=-\int_0^1\lambda(\dot x)dt-\int_0^1H_t(x)dt+f_1(x(1))-f_0(x(0)).
\]
For zero Hamiltonian and a constant chord at critical point \(q\), this equals \(-f(q)\). Its first variation is the symplectic pairing of \(\dot x-X_H\) with a variation having endpoints tangent to the Lagrangians.

The standard small-exact-graph correspondence identifies regular rigid holomorphic strips with Morse gradient lines of \(f\) up to grading and flow-direction conventions, after confinement and transversality are established. Over \(\mathbb F_2\), the two gradient arcs cancel, so \(HF(L_0,L_1;\mathbb F_2)\cong H_*(S^1;\mathbb F_2)\) up to grading shift, with rank two. An arbitrary closed nonexact graph \(p=c\ne0\) is not covered by this exact Hamiltonian-isotopy comparison.

### Exercises with answers

1. **Intersections.** Where do \(L_0\) and \(\Gamma_{df}\) meet for \(f(q)=\epsilon\cos(2\pi q)\)? **Answer:** at \(q=0\) and \(q=1/2\) mod one.
2. **Actions.** What are the two constant-chord actions? **Answer:** \(-\epsilon\) and \(+\epsilon\).
3. **Differential.** Why do two rigid gradient arcs contribute zero over \(\mathbb F_2\)? **Answer:** \(1+1=0\) modulo two.
4. **Counterexample.** Why can a constant-momentum Lagrangian miss the zero section without contradicting Floer intersection bounds for exact graphs? **Answer:** its underlying closed one-form is nonexact and the translation is not a Hamiltonian exact-graph deformation.

### Sources and further reading

- Andreas Floer, [Morse Theory for Lagrangian Intersections](https://doi.org/10.4310/JDG/1214442477), *J. Differential Geometry* 28 (1988), 513–547.
- Alberto Abbondandolo and Matthias Schwarz, [On the Floer Homology of Cotangent Bundles](https://arxiv.org/abs/math/0408280), cotangent bundle versions of Floer theory.
- [Morse homology](https://en.wikipedia.org/wiki/Morse_homology); [Cotangent bundle](https://en.wikipedia.org/wiki/Cotangent_bundle).
