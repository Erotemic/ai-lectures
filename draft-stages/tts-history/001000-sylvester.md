# 001000 — James Joseph Sylvester: When can one matrix equation be solved uniquely?

**Track:** History · People and ideas. **Theme:** Subspaces and matrix language. **Background:** introductory linear algebra; the lecture defines its local objects.

<!-- BEGIN SPOKEN LECTURE -->

# James Joseph Sylvester: When can one matrix equation be solved uniquely?

An equation with one unknown number is familiar. An equation whose unknown is a whole matrix is a different kind of problem. Suppose a matrix acts on the left of an unknown transformation, while another acts on its right. We want to know when the transformation is determined and how sensitive it is to the data.

James Joseph Sylvester's name remains attached to this problem. Born in London in 1814, Sylvester worked during the nineteenth-century expansion of matrix theory. He taught and researched in Britain and the United States, and his mathematical exchanges with Arthur Cayley were part of the development of a language for matrices that could be studied as objects in their own right. His 1884 publications included equations between matrices. The modern Sylvester equation is one thread of that history.

Here is a miniature version. Let the matrix on the left scale the first coordinate by two and the second by five. Let the matrix on the right scale its coordinates by one and four. In the equation left matrix times X, minus X times right matrix, equals a known matrix C, each entry of X is multiplied by one difference of spectral values. Those differences are one, negative two, four, and one. All are nonzero, so every entry of X can be recovered by division.

Now change the right matrix so one of its spectral values is five. A denominator becomes zero. The equation may have no solution for some data, or several solutions for other data. The central point is easy to remember: a matrix equation can lose uniqueness when the two spectra meet.

For a diagonal example, this is entrywise division. For general matrices, an equivalent equation acts on a space of matrices. The mathematical result that disjoint spectra yield unique solvability extends well beyond diagonal examples, although one must be precise about the operator setting.

That connection is why Sylvester's name appears in spectral perturbation theory. When an approximate invariant subspace leaks into the unwanted spectral region, that leakage satisfies a Sylvester-type equation. The residual is known, the leakage is unknown, and the spectral gap controls the inverse equation.

Sylvester's historical significance here is the change of viewpoint. We are solving for an entire transformation, and the spectra of two other transformations determine whether this can be done reliably. The later subspace-angle estimates are a geometric application of that algebraic idea.

<!-- END SPOKEN LECTURE -->

---

## Mathematical and historical companion (display only)

For diagonal matrices \(A=\operatorname{diag}(2,5)\) and \(B=\operatorname{diag}(1,4)\),
\((AX-XB)_{ij}=(a_i-b_j)x_{ij}\). The denominator table is
\(\left(\begin{smallmatrix}1&-2\\4&1\end{smallmatrix}\right)\).
If \(B\) instead has eigenvalue \(5\), an entrywise denominator vanishes.
The modern finite-dimensional criterion is \(\sigma(A)\cap\sigma(B)=\varnothing\).

## Reading notes (non-spoken)

The linked biography or contributor record identifies the person; the mathematical source documents a related publication or mathematical construction. The accessible topic article supplies background. Publication and personal history are distinguished from later eponymous terminology.
