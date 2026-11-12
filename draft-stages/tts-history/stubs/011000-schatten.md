# 011000 — Robert Schatten: What happens when a matrix norm becomes an operator ideal?

**Track:** History · People and ideas. **Theme:** Singular values and matrix norms. **Background:** introductory linear algebra; the lecture defines its local objects.

<!-- BEGIN SPOKEN LECTURE -->

# Robert Schatten: What happens when a matrix norm becomes an operator ideal?

A matrix has finitely many singular values, so raising them to powers and adding them is straightforward. An operator on an infinite-dimensional space may have infinitely many singular values. The same procedure can give a finite number, or it can diverge. That distinction determines which operators belong to a Schatten class.

Robert Schatten was a Polish-American mathematician whose work helped develop the language of norm ideals and tensor products in functional analysis. His 1950 book A Theory of Cross-Spaces and his later work on norm ideals belong to the development of operator structures that extend finite matrix ideas. His name is attached to the Schatten classes.

Let us begin with a diagonal operator on square-summable sequences. On the nth coordinate, it multiplies by one over n. The singular values are one, one half, one third, and so on. The sum of their squares converges. The sum of their magnitudes does not. Therefore the operator is Hilbert–Schmidt but not trace class.

The same transformation can thus be small in one aggregate sense without belonging to another. Schatten p norms formalize this: take the pth powers of the singular values, sum, and then take the pth root. For p equal to two we obtain the Hilbert–Schmidt norm; for p equal to one we obtain the trace norm. The operator norm appears as the limiting maximum-size viewpoint.

This is useful for error bounds because a theorem proved in one norm need not automatically hold with the same constant in another. A componentwise estimate on singular values may justify a Hilbert–Schmidt conclusion after squaring and adding. Getting an operator-norm estimate can require a different argument.

For a self-adjoint perturbation, one may want to measure the rotation of an entire spectral subspace, not merely the worst affected direction. A Schatten norm collects information across many principal angles. In an infinite-dimensional space, the statement also needs an ideal-membership hypothesis so that the proposed quantity is finite.

Schatten's place in the mathematical story is the bridge from finite singular-value arithmetic to infinite-dimensional analysis. The name on a norm records a substantial body of work on how operator size should be defined and controlled when matrices become infinite.

<!-- END SPOKEN LECTURE -->

---

## Mathematical and historical companion (display only)

For the diagonal compact operator \(Te_n=n^{-1}e_n\),
\(\sum_{n\ge1}s_n(T)^2=\sum_{n\ge1}n^{-2}<\infty\), whereas
\(\sum_{n\ge1}s_n(T)=\sum_{n\ge1}n^{-1}=\infty\).
Thus \(T\in\mathcal S_2\setminus\mathcal S_1\).

## Reading notes (non-spoken)

The linked biography or contributor record identifies the person; the mathematical source documents a related publication or mathematical construction. The accessible topic article supplies background. Publication and personal history are distinguished from later eponymous terminology.
