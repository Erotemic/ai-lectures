# 023100 — Morse Theory by Example: Critical Points Become a Chain Complex

**Track:** Topology and Geometry. **Background:** derivatives, Hessians, gradient flow, chain complexes, homology. **Central question:** how can a smooth function's critical points describe the topology of the space on which it lives?

<!-- BEGIN SPOKEN LECTURE -->

# Morse Theory by Example: Critical Points Become a Chain Complex

Imagine exploring a landscape by measuring elevation. At the bottom of a valley you find a minimum. On a mountain pass you find a saddle. On the summit you find a maximum. These critical points are not only features of one particular height function. Under suitable nondegeneracy assumptions, the pattern of critical points constrains the topology of the underlying surface.

Morse theory makes that statement precise. It has two complementary sides. As we raise the elevation level, we watch how the region below it changes shape. And if we follow the downhill gradient flow, we can build a chain complex whose generators are critical points and whose differential counts special flow lines between them.

The second side is the direct ancestor of Floer homology. But the construction is easier to understand in two dimensions, where we can draw every critical-point type.

## A Hessian that counts descending directions

A critical point of a smooth function is a point where its first derivative vanishes. The Hessian measures the leading quadratic behavior near that point. For a function of two variables, a positive-definite Hessian indicates a nondegenerate minimum. A negative-definite Hessian indicates a nondegenerate maximum. A Hessian with one positive and one negative eigenvalue indicates a saddle.

The Morse index of a nondegenerate critical point is the number of negative eigenvalues of the Hessian, counted with multiplicity. It is zero for a minimum, one for a saddle on a surface, and two for a maximum on a surface.

Why does this number matter? Near a nondegenerate critical point, the Morse lemma gives coordinates in which the function is a constant minus the squares of its descending coordinates plus the squares of its ascending coordinates. The number of descending directions is therefore an intrinsic local feature of the critical point, independent of which smooth coordinates we use.

This is a bridge from calculus to topology. A quadratic approximation determines the dimension of the handle added when an elevation threshold passes through a critical point.

## Watch a sphere appear level by level

Take the ordinary height function on a round sphere. Near the south pole, the sublevel set begins as a small disk after we pass the minimum. As we raise the threshold, the region expands but remains a disk. When we pass the north-pole maximum, a two-dimensional cap is attached and the boundary closes. The completed space is a sphere.

The function has two critical points: a minimum of index zero and a maximum of index two. From the handle viewpoint we have attached one zero-handle and one two-handle, with no one-handles. The alternating count of critical points is one plus one, or two. This is the Euler characteristic of the sphere.

The Morse inequalities say more generally that the number of critical points of each index cannot be smaller than the corresponding Betti number, subject to the usual refined relations. The height function on a sphere reaches the lower bound in each degree.

## What changes on a torus?

Stand a doughnut-shaped torus upright and measure height. As we raise the water level, a component appears at a minimum. At the first saddle, a passage changes the shape of the flooded region. At a second saddle, another passage appears, creating the torus's two independent one-dimensional loop directions. At the maximum, the remaining boundary closes.

A generic vertical height function on a standard embedded torus has four nondegenerate critical points: one minimum, two saddles, and one maximum. Their Morse indices are zero, one, one, and two. The alternating critical-point count is one minus two plus one, which is zero, agreeing with the torus's Euler characteristic.

This does not mean that critical-point counts uniquely determine every homology group. To recover homology we also need to know how the handles attach, or equivalently how the corresponding Morse differential maps critical points of one index to critical points of the next lower index.

## The negative-gradient flow makes a differential

Choose a Riemannian metric so that the gradient of the function is defined. Then consider trajectories moving downhill according to the negative gradient. The function decreases along every nonconstant such trajectory because its derivative along the motion equals minus the squared norm of the gradient.

Some trajectories connect one critical point to another. Under Morse–Smale transversality, critical points whose Morse indices differ by one are connected by a finite collection of appropriate trajectories, up to time translation. Give each trajectory a sign after choosing coherent orientations, and count them. These signed counts give the coefficients of the Morse boundary operator.

The chain group in degree k is generated by critical points of Morse index k. The boundary of a generator is a signed combination of critical points of index k minus one. The central theorem is that the boundary applied twice gives zero.

Why should it? The boundary of a one-dimensional family of flow trajectories consists of broken trajectories: one path from index k to k minus one, followed by another from k minus one to k minus two. The oriented endpoints of a compact one-dimensional family cancel in pairs. This geometric cancellation becomes the algebraic identity that two consecutive Morse boundaries compose to zero.

The full proof needs compactness, transversality, and coherent orientation arguments. The slogan that 'the boundary of a boundary vanishes' is the correct organizing idea, but it is not a substitute for establishing those analytic facts.

## The circle as a signed-count example

Take the height function on a circle. There is one minimum of index zero and one maximum of index one. Exactly two downhill arcs connect the maximum to the minimum. When counted with compatible orientations, the two arcs have opposite signs. Their contributions cancel, so the Morse boundary from degree one to degree zero is zero.

The resulting homology has one integer generator in degree zero and one in degree one. That agrees with the ordinary homology of the circle.

If we work with coefficients modulo two, there are two connecting trajectories, and two is zero modulo two. The conclusion is the same, with less orientation bookkeeping. But using mod-two coefficients discards information about signs and integer torsion. It is a simplification, not a universal replacement for integral Morse theory.

## What survives beyond ordinary landscapes?

Now replace the finite-dimensional manifold by a space of paths, loops, or connections. Define a functional whose critical points represent special geometric objects: geodesics, Hamiltonian periodic orbits, or solutions of gauge equations. Try to count connecting gradient trajectories and build a chain complex.

This is the philosophy behind Floer homology and related theories. The infinite-dimensional setting creates new difficulties: compactness can fail through bubbling or escape, transversality can be hard, and orientations must be controlled. The basic algebraic target remains recognizable. Critical objects generate a complex; connecting trajectories define its boundary; the proof that the boundary squares to zero comes from the geometry of boundaries of moduli spaces.

Morse theory therefore offers more than a way to compute the Euler characteristic. It demonstrates an architecture for building topology from dynamics. Local critical-point data, global flow, compactness, and the chain-complex identity cooperate to produce homology. That architecture will be reused, with substantial extra analysis, in advanced symplectic and gauge theory.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For a Morse function \(f:M\to\mathbf R\) (all critical points nondegenerate), the Morse index \(\lambda(p)\) is the number of negative eigenvalues of \(\operatorname{Hess}_p f\). By the Morse lemma, near \(p\) suitable coordinates give \(f=f(p)-\sum_{i=1}^{\lambda}x_i^2+\sum_{i=\lambda+1}^n x_i^2\). Passing a single index-\(\lambda\) critical value attaches a \(\lambda\)-handle under the standard handle-attachment hypotheses.

With a Morse–Smale gradient and coherent orientations, \(C_k^{\mathrm{Morse}}\) is freely generated over \(\mathbf Z\) by index-k critical points and \(\partial p=\sum_{\lambda(q)=k-1}n(p,q)q\), where \(n(p,q)\) counts signed unparameterized negative-gradient trajectories. Compactified one-dimensional moduli spaces provide \(\partial^2=0\). For closed M, Morse homology is naturally isomorphic to singular homology; the Euler characteristic is \(\chi(M)=\sum_k(-1)^k c_k\), where \(c_k\) counts index-k critical points. Morse inequalities give \(c_k\ge b_k\) over a chosen field.

For the sphere's height function, \((c_0,c_1,c_2)=(1,0,1)\); for the standard upright torus, \((1,2,1)\); for the circle, the two oriented downhill arcs between maximum and minimum cancel in the Morse differential, giving \(H_0\cong H_1\cong\mathbf Z\).

### Exercises with answers

1. **Index.** What is the Morse index of \(f(x,y)=-x^2+y^2\) at zero? **Answer:** One.
2. **Sphere.** Compute the alternating critical-point count for the height function on \(S^2\). **Answer:** \(1+1=2\).
3. **Torus.** Compute \(c_0-c_1+c_2\) for \((1,2,1)\). **Answer:** Zero.
4. **Why a complex?** What geometric structure explains \(\partial^2=0\)? **Answer:** Oriented endpoints of compactified one-dimensional moduli spaces of trajectories, corresponding to pairs of broken trajectories, cancel.

### Sources and further reading

- MIT OpenCourseWare, [18.965 Geometry of Manifolds, lectures 23–28](https://ocw.mit.edu/courses/18-965-geometry-of-manifolds-fall-2004/pages/lecture-notes/).
- University of Toronto, [Morse Theory lecture notes](https://www.math.utoronto.ca/mgualt/Morse%20Theory/Notes12-13.pdf).
- Overviews: [Morse theory](https://en.wikipedia.org/wiki/Morse_theory), [Morse homology](https://en.wikipedia.org/wiki/Morse_homology).
