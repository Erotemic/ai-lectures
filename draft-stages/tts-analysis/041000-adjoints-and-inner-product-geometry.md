# 041000 — Adjoints: Moving an Operator Across an Inner Product

**Track:** Analysis from First Principles. **Background:** Hilbert spaces, bounded operators, and orthogonal projection. **Question:** How can one operator reveal what another does to lengths, angles, and measurements?

<!-- BEGIN SPOKEN LECTURE -->

# Adjoints: Moving an Operator Across an Inner Product

Imagine a microphone that records two numbers: the left-channel signal and the right-channel signal. A mixing device outputs their sum in one channel and their difference in another. It is a linear transformation, so a matrix describes it. But suppose that instead of asking what the device outputs, you ask what combination of input signals is being measured when someone listens to a particular output channel. That is the question answered by the adjoint.

A linear operator takes a vector to another vector. An inner product lets us measure how strongly two vectors align. If we apply an operator to the first vector and then take an inner product with the second, the adjoint tells us how to move that transformation across the inner product. For every input x and every test vector y, the inner product of T x with y equals the inner product of x with T adjoint y.

That sentence is worth hearing twice in different language. First transform the signal and then measure it against y. Or transform the measuring instrument backward by the adjoint and apply the resulting measurement directly to the original signal. The numerical result agrees exactly.

## What transposition misses

In ordinary real Euclidean space, the adjoint of a matrix is its transpose. The row of a matrix that computes one output coordinate becomes a column describing the corresponding input measurement. For a complex vector space there is another operation: complex conjugation. The adjoint is the conjugate transpose, because the complex inner product conjugates one of its arguments.

For example, multiplying a complex number by the imaginary unit rotates its plane by a quarter turn. The adjoint multiplies by the negative imaginary unit, undoing that rotation inside an inner product. An ordinary transpose would not record the reversal of complex phase.

In an infinite-dimensional Hilbert space we may have no finite matrix. Yet the same definition works, and a bounded operator has exactly one bounded adjoint. The reason is that, for fixed y, the rule assigning to x the inner product of T x with y is a continuous linear measurement. The representation theorem for Hilbert spaces says every such measurement comes from a unique vector. Call that vector T adjoint y. This is how the adjoint exists without coordinates.

## An example with an endless sequence

Take a square-summable sequence and shift every entry one place to the right, putting zero into the first position. The right-shift operator does not change the length of a sequence. It simply changes where its entries live.

What is its adjoint? It is the left shift: remove the first entry and slide the remaining entries toward the beginning. To check, pair a right-shifted sequence with a second sequence. The first coordinate contributes nothing, and every later coordinate pairs with the preceding input coordinate. That is exactly the pairing of the original input with the left-shifted test sequence.

This one example makes an important warning visible. The right shift preserves length, so T adjoint followed by T is the identity. But T followed by T adjoint is not the identity: it erases the first coordinate. An operator may preserve every input norm without being onto. Its adjoint records that asymmetry.

## Adjoint geometry of ranges and kernels

The kernel of an operator consists of inputs that disappear. The range consists of outputs that are actually attainable. The adjoint relates these two ideas through perpendicularity.

Suppose y is perpendicular to every output T x. Then every inner product of T x with y is zero. Move T across the pairing: every inner product of x with T adjoint y is zero. That forces T adjoint y to be zero. Conversely, if T adjoint y vanishes, y is perpendicular to every output.

So the vectors perpendicular to the range of T are exactly the kernel of T adjoint. This gives a geometric criterion for solvability. A proposed output must be perpendicular to every obstruction in the adjoint kernel if it is to lie in the closure of the range. The word closure matters: in an infinite-dimensional space, the range need not be closed, so satisfying every orthogonality test may mean an output can be approximated arbitrarily well without being attained exactly.

This distinction shows up in inverse problems. A measurement can be compatible with all linear constraints and still be attainable only as a limit of increasingly unstable approximate inputs.

## Products, projections, and norms

The adjoint reverses the order of a composition. If you apply T and then S, the adjoint first moves S backward and then T. It is the same reversal that happens when taking the transpose of a matrix product.

An orthogonal projection equals its own adjoint. That equality expresses the fact that projecting a vector onto a closed subspace is the same operation whether you examine how inputs act against test vectors or reverse the measurement. A projection along an oblique direction generally is not self-adjoint.

There is another formula we will need repeatedly. For every bounded T, the operator T adjoint T measures squared output lengths: its inner product with x on both sides equals the squared norm of T x. Consequently T adjoint T can never yield a negative quadratic measurement. That property is called positivity.

Moreover, the operator norm of T adjoint T is the square of the norm of T. One direction follows from the ordinary norm bound for compositions. The other follows by testing the inner product of T adjoint T with unit inputs whose transformed lengths approach the operator norm. This is the C-star identity, and it will eventually make functional calculus precise.

## The reason to learn adjoints first

It is tempting to define a function of an operator by writing a power series and hoping for the best. But for self-adjoint operators, we can do better. The adjoint gives us the notion of self-adjointness. Self-adjointness leads to real spectral values. Positivity leads to square roots and inequalities. Those structures make it possible to define a wide class of scalar functions of an operator and know that the result behaves correctly.

The adjoint is therefore not merely a way to reverse matrix arrows. It is the bridge from a transformation to the geometry of its measurements. It tells us what the transformation does to energy, orthogonality, solvability, and ultimately spectrum.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Throughout, the complex Hilbert-space inner product is linear in its first argument. For bounded \(T:H\to K\), its Hilbert adjoint is the unique \(T^*:K\to H\) such that
\[
\langle Tx,y\rangle_K=\langle x,T^*y\rangle_H.
\]
Existence and uniqueness follow from Riesz representation; \(\|T^*\|=\|T\|\). We have \((ST)^*=T^*S^*\), \((T^*)^*=T\), and
\[
(\operatorname{ran}T)^\perp=\ker T^*,\qquad
\overline{\operatorname{ran}T}=(\ker T^*)^\perp.
\]
For the unilateral right shift \(S:\ell^2(\mathbb N)\to\ell^2(\mathbb N)\), \(S^*(x_1,x_2,\ldots)=(x_2,x_3,\ldots)\), \(S^*S=I\), and \(SS^*=I-P_{e_1}\).

The C-star identity is \(\|T^*T\|=\|T\|^2\). Proof: \(\|Tx\|^2=\langle T^*Tx,x\rangle\le\|T^*T\|\|x\|^2\); hence \(\|T\|^2\le\|T^*T\|\). Reverse via \(\|T^*T\|\le\|T^*\|\|T\|=\|T\|^2\).

### Exercises with answers

1. **Two-channel mixer.** Let \(T=\begin{pmatrix}1&1\\1&-1\end{pmatrix}\) on \(\mathbb R^2\). Find its adjoint and norm. **Answer:** \(T^*=T\) and \(T^*T=2I\), so \(\|T\|=\sqrt2\).
2. **Shift asymmetry.** Why is the right shift not unitary? **Answer:** It is an isometry, \(S^*S=I\), but \(SS^*\ne I\); its range has zero first coordinate.
3. **Range test.** If \(\ker T^*=\{0\}\), is T necessarily onto? **Answer:** No. Its range is dense; surjectivity requires more, such as closedness of the range.
4. **Order reversal.** Prove \((ST)^*=T^*S^*\) from the pairing. **Answer:** Apply the adjoint identity twice and use uniqueness.

### Reading and source notes

- [MIT OpenCourseWare, 18.102 Introduction to Functional Analysis, lecture notes](https://ocw.mit.edu/courses/18-102-introduction-to-functional-analysis-spring-2021/pages/lecture-notes-and-readings/).
- [Sheldon Axler, Measure, Integration & Real Analysis](https://measure.axler.net/).
