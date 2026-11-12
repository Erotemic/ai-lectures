# 008000 — David Hilbert: Why do infinitely many coordinates still have geometry?

**Track:** History · People and ideas. **Theme:** Hilbert spaces and operator theory. **Background:** introductory linear algebra; the lecture defines its local objects.

<!-- BEGIN SPOKEN LECTURE -->

# David Hilbert: Why do infinitely many coordinates still have geometry?

A vector in ordinary space has two or three coordinates. A Fourier series or a vibrating string can be described by an infinite sequence of coefficients. To reason geometrically about such objects, we need to know when the sequence represents a legitimate point and when approximations converge.

David Hilbert's work on integral equations and analysis helped shape the mathematical setting now called Hilbert space. The terminology and modern axiomatization developed through the work of many people, so the name should not be mistaken for the work of one inventor. Hilbert was central to the movement from finite systems of equations to infinite-dimensional spectral analysis.

Take a sequence of numbers whose squares add to a finite total. Such sequences form square-summable sequence space, commonly called ell two. The inner product of two sequences is obtained by multiplying matching coordinates and adding. A convergent sequence of finite-coordinate approximations can approach a genuine point of ell two even though the limit may have infinitely many nonzero coordinates.

That last sentence depends on completeness. If every Cauchy sequence converges inside the space, then procedures built from increasingly good approximations have somewhere to arrive. Without completeness, formal orthogonal expansions might point outside the objects we have allowed.

The spectral question becomes subtler in such a space. Consider the operator that multiplies the nth coordinate by one over n. It has eigenvectors given by the coordinate axes and eigenvalues approaching zero. Zero belongs to the spectrum even though it is not an eigenvalue. There is no nonzero square-summable sequence annihilated by the operator, yet the inverse is not bounded.

This example shows why spectral theory must extend beyond a list of eigenvalues. Resolvents, projections, and spectral measures describe bounded and unbounded phenomena in a common framework. The distinction between eigenvalue and spectrum becomes necessary as soon as infinitely many directions are present.

Hilbert's legacy for the Davis–Kahan story is the geometric environment in which subspace perturbation survives beyond matrices. Orthogonality, projection, and the notion of a closed subspace remain meaningful. What changes is that convergence, domains, and the continuous spectrum require explicit attention.

<!-- END SPOKEN LECTURE -->

---

## Mathematical and historical companion (display only)

On \(\ell^2\), define \(Te_n=n^{-1}e_n\). Then \(T\) is bounded,
compact and injective. Its eigenvalues are \(1/n\), whereas
\(0\in\sigma(T)\) but \(0\notin\sigma_p(T)\). The unit vectors \(e_n\)
satisfy \(\|Te_n\|\to0\), so no bounded inverse exists.

## Reading notes (non-spoken)

The linked biography or contributor record identifies the person; the mathematical source documents a related publication or mathematical construction. The accessible topic article supplies background. Publication and personal history are distinguished from later eponymous terminology.
