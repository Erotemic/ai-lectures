# 023000 — Morse Theory: Critical Points and Handle Decompositions

**Track:** Topology and Geometry. **Background:** smooth manifolds, tangent spaces, homology, Euler characteristic. **Central question:** how can the critical points of a smooth function reveal the topology of an entire manifold?

<!-- BEGIN SPOKEN LECTURE -->

# Reading the topology from the height of a landscape

Imagine a smooth landscape and raise the water level from far below it. At first the land is dry. When the water reaches the bottom of a valley, a new pool appears. When it passes a saddle, two regions may join, or a tunnel may form. At a peak, a remaining boundary may close. The topology of the flooded region changes only at certain heights.

Morse theory turns that picture into a theorem about smooth manifolds. Choose a smooth real-valued function on the manifold and examine its critical points, the places where its first derivative vanishes. If these critical points are nondegenerate, their local behavior is completely controlled by a quadratic form. The number of negative directions in that form, called the Morse index, predicts the kind of topological change that occurs.

The theory is remarkable because a numerical function, which seems to throw away most of the geometry, can recover information about holes, cells, and homology.

## What nondegenerate means

At a critical point, the first derivative vanishes. The Hessian is the matrix of second derivatives in local coordinates. Nondegeneracy means that this matrix is invertible. Its numbers of positive and negative eigenvalues are independent of the coordinate system. The number of negative eigenvalues is the index.

A nondegenerate minimum has index zero. On a two-dimensional surface, a saddle has index one and a maximum has index two. In higher dimensions there are more possibilities: the index can be any integer from zero through the dimension of the manifold.

The Morse lemma states that near such a critical point there are local coordinates in which the function is exactly a constant minus a sum of squares in the negative directions plus a sum of squares in the positive directions. Not merely approximately quadratic: after a smooth change of coordinates, the higher-order terms disappear locally.

This normal form provides the model for what happens when we cross the corresponding critical value.

## Passing a critical value

For any real number a, consider the sublevel set consisting of points where the function is at most a. If we move a through an interval that contains no critical values, the sublevel set does not change its diffeomorphism type under the standard compactness hypotheses.

Cross one isolated nondegenerate critical point of index lambda. The new sublevel set is obtained from the old one by attaching a lambda-dimensional handle. At the level of homotopy type, it is like attaching a lambda-dimensional cell. A zero-handle creates a component. A one-handle can join components or create a tunnel. A top-dimensional handle can close off a cavity.

The word can matters. The effect of attaching a handle depends on where it is attached. A one-handle may connect two previously separate disks, reducing the number of connected components, or it may attach twice to the same component, increasing the number of independent cycles.

## Counting on a sphere and a torus

Take a round two-sphere and use ordinary height. There is one minimum at the south pole and one maximum at the north pole, with no saddles. As the threshold rises, a disk appears at the minimum and is eventually capped at the maximum. The alternating count of critical points is one plus one, giving Euler characteristic two.

Now picture an upright torus, a doughnut standing on its edge, with a generic height function. It has one minimum, two saddles, and one maximum. The first saddle creates a tunnel-like change, and the second changes how a boundary component connects. The alternating sum is one minus two plus one, giving zero, which is the Euler characteristic of the torus.

These examples motivate the Morse inequalities. If m sub k counts critical points of index k and b sub k is the kth Betti number over a field, then there must be at least b sub k critical points of index k. In particular, the counts of critical points constrain possible homology. Stronger alternating-sum inequalities contain additional information.

## From handles to a chain complex

There is a second step beyond counting critical points. Choose a Riemannian metric and follow negative gradient flow lines. Generically, after a Morse-Smale transversality condition, one can count flow lines connecting critical points of successive indices, with signs when orientations permit. These counts form a differential in a chain complex whose generators are the critical points.

The deep fact is that the differential squares to zero and the resulting homology agrees with ordinary homology. Critical points give the chain groups; flow trajectories tell us how the pieces attach. Betti numbers are what survive after the attachments and cancellations have been accounted for.

A simple warning illustrates the distinction. Two functions might have the same number of critical points in each index but different flow-line incidence data. Critical-point counts alone give bounds and Euler characteristics; the Morse differential is needed to recover the finer homology groups.

## The boundary of this method

A generic smooth function on a compact smooth manifold can be made Morse by a small perturbation. But not every smooth function is Morse. A whole circle of critical points, for example, violates the isolated nondegenerate condition. Morse-Bott theory addresses certain structured degeneracies, while more general singularities need other tools.

Morse theory gives a systematic bridge from calculus to topology. A local second-derivative test becomes a global handle decomposition. And once gradient trajectories are added, the same calculus produces a homology theory. That is a compelling example of differential equations, geometry, and algebra working together rather than merely borrowing terminology from each other.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Let M be a smooth compact n-manifold and `f:M->R` a Morse function. A critical point p satisfies `df_p=0`; it is nondegenerate when its Hessian has no zero eigenvalues. Morse index `lambda(p)` is the number of negative eigenvalues. The Morse lemma gives local coordinates with
\[
f=f(p)-x_1^2-\cdots-x_\lambda^2+x_{\lambda+1}^2+\cdots+x_n^2.
\]
Under the usual isolated critical-value and compactness hypotheses, crossing one index-lambda critical point attaches a lambda-handle `D^lambda x D^{n-lambda}` and changes the sublevel-set homotopy type by a lambda-cell. With `m_k=# critical points of index k` and Betti numbers `b_k=dim H_k(M;F)`, weak Morse inequalities give `m_k >= b_k`, and
\[
\sum_k(-1)^k m_k=\chi(M)=\sum_k(-1)^k b_k.
\]
A Morse-Smale metric allows a chain differential defined by signed counts of negative gradient trajectories between critical points whose indices differ by one. Proving `d^2=0` uses compactification of one-dimensional moduli spaces of flow lines; the full argument requires transversality and orientation choices (or coefficients in `F_2`).

For height on `S^2`, critical indices are 0 and 2, giving Euler characteristic `1+1=2`. A generic vertical height on a standard torus has indices 0,1,1,2, giving `1-2+1=0`.

### Exercises with answers

1. What is the Morse index of a nondegenerate local maximum of a three-manifold? **Answer:** three.
2. What does crossing an index-zero point attach? **Answer:** a zero-handle, creating a new component of the sublevel set.
3. Why do equal critical-point counts not necessarily determine full homology? **Answer:** attachment maps or the Morse differential may differ.
4. Calculate the alternating critical-point count for a torus height function with one minimum, two saddles, and one maximum. **Answer:** zero.

### Reading and source notes

- [University of Toronto, Morse Theory notes](https://www.math.utoronto.ca/mgualt/Morse%20Theory/Notes12-13.pdf), handles and critical values.
- [Arun Debray, Morse Theory lecture notes](https://adebray.github.io/lecture_notes/m392c_Morse_notes.pdf), local model and handle attachment.
- [Milnor, Morse Theory](https://press.princeton.edu/books/paperback/9780691080086/morse-theory), classical treatment.
