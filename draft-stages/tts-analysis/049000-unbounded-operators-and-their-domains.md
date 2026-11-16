# 049000 — Unbounded Operators: Why the Domain Is Part of the Definition

**Track:** Analysis from First Principles. **Background:** Hilbert spaces, linear operators, convergence, and self-adjointness. **Question:** Why do differentiation and infinite diagonal multipliers demand special attention to their domains?

<!-- BEGIN SPOKEN LECTURE -->

# Unbounded Operators: Why the Domain Is Part of the Definition

Imagine an infinite diagonal matrix whose entries are one, two, three, four, and so on. On a finite vector, multiplying by this matrix causes no difficulty. On a square-summable infinite sequence, the same formula may produce a sequence that is not square summable. The instruction makes sense for some inputs but not for every vector in the Hilbert space.

An unbounded operator is not simply a bounded operator whose norm happens to be large. It is a linear transformation defined on a specified subspace called its domain, often a dense subspace of the Hilbert space. Its action and its domain belong together. Changing the domain can change the operator's adjoint, spectrum, and self-adjointness, even when the formal formula stays the same.

## An infinite diagonal example

Let H be the space of square-summable sequences. Define A by multiplying the N-th coordinate by N. For the output to remain square summable, the sum of N squared times the squared magnitude of the input's N-th coordinate must be finite. That condition defines the domain of A.

Take an input whose N-th coordinate is one over N. This sequence belongs to H, since the sum of reciprocal squares converges. But applying A would give the sequence of ones, which is not square summable. Thus the input is outside the domain of A.

Now take an input whose N-th coordinate is one over N squared. It is in the domain of A: the output is the reciprocal sequence, which is square summable. Yet applying A twice would produce a sequence of ones. This input belongs to the domain of A but not to the domain of A squared.

This is not an obscure corner case. It shows that writing A squared without checking domains can assert the existence of an output that does not belong to the Hilbert space.

## Dense domains and the graph

Even though A is not defined everywhere, its domain is dense in H. Every finitely supported sequence belongs to the domain, and finitely supported sequences approximate every square-summable sequence. Density lets us test the operator against arbitrary vectors and develop an adjoint.

Another important property is closedness. Consider the graph of A: all pairs consisting of an allowed input and its output. If a sequence of allowed inputs converges in H, and their outputs also converge in H, a closed operator guarantees that the limit input is still allowed and its output is the output limit.

Our infinite diagonal operator is closed. The reason is coordinatewise: convergence of the inputs and outputs forces the N-th output coordinate to remain N times the N-th input coordinate. If the output limit is square summable, the input limit satisfies the domain condition.

Closedness is the infinite-dimensional version of refusing to lose legitimate input-output pairs when taking limits. It is critical for differential operators, where a sequence of smooth functions can converge to a less regular limit and the derivative may converge only under additional hypotheses.

## Symmetric is not automatically self-adjoint

For a bounded operator on the whole Hilbert space, self-adjointness is the identity A equals its adjoint. For an unbounded operator, we must additionally compare domains. An operator is symmetric if the inner product of A x with y equals the inner product of x with A y for all x and y in its domain. It is self-adjoint when its adjoint has the same domain and agrees there.

These are not equivalent. Take the derivative operator multiplied by negative i on square-integrable functions on an interval. If we initially define it only on smooth functions supported away from the endpoints, integration by parts shows symmetry. But the adjoint allows a larger domain. The operator is not self-adjoint on the small initial domain.

Boundary conditions influence whether a differential operator becomes self-adjoint. Periodic conditions, for instance, can lead to a self-adjoint momentum operator. Different boundary choices can yield different operators even when each one uses the same formal differential expression.

The real distinction is therefore not a cosmetic technicality. It changes which spectral theorem can be applied and which time evolutions are well-defined.

## The graph norm measures what the operator demands

For an unbounded closed operator, define the graph norm of an allowed input by combining its Hilbert-space norm with the Hilbert-space norm of its output. An input is small in graph norm only when both the input and the action of A on it are small.

Our diagonal operator gives large penalties to high coordinates. A sequence may be small in ordinary square-sum norm while having a large output under A. The graph norm detects this because it gives each coordinate a weight involving one plus N squared.

Closedness of A is equivalent to completeness of its domain in the graph norm, provided the ambient Hilbert space is complete. This is a useful way to reframe an unbounded problem: the same operator is bounded as a map from its graph-normed domain into H.

The input space has changed, which is why there is no contradiction in calling the original operator unbounded on H but bounded on the stronger domain norm.

## A multiplication operator on the real line

Take H to be L two of the real line. Define A by multiplying a function by t. A function is in the domain exactly when t times that function is still square integrable. For example, a rapidly decaying function belongs to the domain. Some slowly decaying L-two functions do not.

The operator is self-adjoint on this maximal multiplication domain. It is unbounded because unit functions concentrated far from zero can have arbitrarily large output norms. Yet its action is no more complicated than scalar multiplication point by point.

Here is the bridge to spectral theory. A is already in the representation form promised by the spectral theorem. We can apply a bounded scalar function f by multiplying by f of t on all of H. We can apply an unbounded f only to those vectors for which f of t times the vector remains in H.

So unbounded functional calculus is conceptually a familiar multiplication rule with a domain attached. The general theorem gives the same rule for every self-adjoint operator, including differential operators that need a change of representation before their spectral variables become visible.

## Why this matters for equations

Many equations of mathematical physics involve derivatives. The Laplacian, momentum, and Hamiltonian operators are typically unbounded on L two. One can formally exponentiate them, take square roots, or form inverse powers. But each expression must be checked against the appropriate functional calculus and domain.

The distinction is clearest when comparing two functions of an unbounded self-adjoint A. The function e to the imaginary t times the spectral variable is bounded, so its operator value acts on every vector in H. The function given by the spectral variable squared is unbounded, so its operator value has a smaller domain than A itself.

Thus a very complicated-looking unitary evolution may be defined everywhere, while the apparently simpler expression A squared is only defined on sufficiently regular vectors. Functional calculus makes that contrast precise instead of concealing it behind formal notation.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For \(A:\mathcal D(A)\subset H\to H\) closed and densely defined, the graph norm is \(\|x\|_A=(\|x\|^2+\|Ax\|^2)^{1/2}\); \((\mathcal D(A),\|\cdot\|_A)\) is Banach. For the diagonal operator \((Ax)_n=nx_n\) on \(\ell^2(\mathbb N)\),
\[
\mathcal D(A)=\left\{x:\sum_{n\ge1}n^2|x_n|^2<\infty\right\},\quad
\mathcal D(A^2)=\left\{x:\sum_{n\ge1}n^4|x_n|^2<\infty\right\}.
\]
This A is self-adjoint and positive, with pure point spectrum \(\{1,2,3,\ldots\}\).

For \(M_t\) on \(L^2(\mathbb R)\), \(\mathcal D(M_t)=\{f\in L^2:tf(t)\in L^2\}\); it is self-adjoint and has \(\sigma(M_t)=\mathbb R\). The full spectrum of an unbounded self-adjoint operator may be unbounded, unlike that of a bounded operator.

For an unbounded densely defined A, symmetry means \(\langle Ax,y\rangle=\langle x,Ay\rangle\) for x,y in \(\mathcal D(A)\); self-adjointness requires \(\mathcal D(A^*)=\mathcal D(A)\) and \(A^*x=Ax\). A formal differential expression alone does not determine the domain.

### Exercises with answers

1. **One power but not two.** Show \(x_n=1/n^2\) lies in \(\mathcal D(A)\setminus\mathcal D(A^2)\). **Answer:** \(\sum n^2/n^4=\sum1/n^2<\infty\) but \(\sum n^4/n^4=\infty\).
2. **Unit input, large output.** Find unit vectors showing A is unbounded. **Answer:** The standard unit vector \(e_n\) has \(\|Ae_n\|=n\to\infty\).
3. **Why graph norm?** Does \(x_k\to x\) in H alone imply \(Ax_k\to Ax\)? **Answer:** No; graph-norm convergence requires both input and output convergence.
4. **Boundary choice.** Why is a symmetric derivative expression not necessarily self-adjoint? **Answer:** Its adjoint can have a larger domain; self-adjointness compares domains as well as formulas.

### Reading and source notes

- [University of Potsdam, Functional Analysis II, unbounded spectral theorem](https://www.math.uni-potsdam.de/fileadmin/user_upload/Prof-Math-Phy/Rosenberger/Skripte/Funktionalanalysis_2.pdf).
- [Sheldon Axler, Measure, Integration & Real Analysis](https://measure.axler.net/).
- [MIT OpenCourseWare, Introduction to Functional Analysis](https://ocw.mit.edu/courses/18-102-introduction-to-functional-analysis-spring-2021/pages/lecture-notes-and-readings/).
