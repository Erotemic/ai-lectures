# 007000 — Ernst Fischer: What does spectral order have to do with the dimension of a subspace?

**Track:** History · People and ideas. **Theme:** Variational approximation. **Background:** introductory linear algebra; the lecture defines its local objects.

<!-- BEGIN SPOKEN LECTURE -->

# Ernst Fischer: What does spectral order have to do with the dimension of a subspace?

The smallest and largest eigenvalues of a symmetric matrix are easy to describe as extreme Rayleigh quotients. The difficulty is describing the eigenvalues between them without giving away the answer through an eigenvector calculation.

Ernst Fischer was an Austrian mathematician associated with spectral and functional analysis. His name appears in both the Riesz–Fischer theorem, concerning square-summable coefficients and Hilbert-space limits, and the Courant–Fischer variational characterization of eigenvalues. These are distinct results. In this lecture the focus is the min–max viewpoint.

Imagine a three-dimensional space with a symmetric operator that stretches three orthogonal directions by factors one, three, and seven. A chosen plane cannot avoid every low-energy direction. Specifically, any two-dimensional plane intersects the plane spanned by the first two eigenvectors in a line. A vector in that intersection has a Rayleigh quotient no larger than three.

Therefore, no two-dimensional trial plane can make its minimum quotient exceed three. But the plane spanned by the second and third eigenvectors has minimum quotient exactly three. The max-over-planes of min-within-a-plane has identified the middle eigenvalue.

The key step is the dimension count. Two planes in a three-dimensional space must intersect in at least one direction. The spectral estimate then comes from knowing how large the quadratic form can be on one of those planes. General min–max formulas extend this reasoning to the kth eigenvalue and to suitable self-adjoint operators in infinite dimensions.

Fischer also belongs to the development of rigorous Hilbert-space methods. In the square-summable sequence setting, a sequence of coefficients with finite sum of squared magnitudes describes a genuine Hilbert-space object. Such completeness facts permit spectral expansions and approximation arguments to converge where they should.

The connection to subspace perturbation is structural. An approximate eigenspace is a subspace selected by a variational or numerical procedure. A genuine spectral subspace is selected by the exact operator. Understanding their relationship requires both the ordering information supplied by min–max principles and the angular information supplied by projection geometry.

Fischer's example reminds us that a spectral theorem does more than list numbers. It gives a way to reason about the constraints geometry imposes on every possible trial subspace.

<!-- END SPOKEN LECTURE -->

---

## Mathematical and historical companion (display only)

For \(A=\operatorname{diag}(1,3,7)\), every two-dimensional subspace
\(S\subset\mathbb R^3\) intersects \(V=\operatorname{span}(e_1,e_2)\)
nontrivially. Hence
\(\min_{\|x\|=1,x\in S}\langle Ax,x\rangle\le 3\),
with equality at \(S=\operatorname{span}(e_2,e_3)\).

## Reading notes (non-spoken)

The linked biography or contributor record identifies the person; the mathematical source documents a related publication or mathematical construction. The accessible topic article supplies background. Publication and personal history are distinguished from later eponymous terminology.
