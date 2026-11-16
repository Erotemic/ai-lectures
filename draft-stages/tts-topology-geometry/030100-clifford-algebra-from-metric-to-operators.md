# 030100 - Clifford Algebra: How a Metric Becomes Operator Multiplication

**Track:** Topology and Geometry. **Background:** inner products, complex matrices, exterior algebra, elliptic symbols. **Central question:** what algebra turns a direction in space into an operator whose square measures length?

<!-- BEGIN SPOKEN LECTURE -->

# Clifford Algebra: How a Metric Becomes Operator Multiplication

In the index-theory lectures we met an operator on differential forms that looked like a derivative plus its adjoint. Its principal symbol had a remarkable property: when you squared it, the result was minus the squared length of the frequency, times the identity. That algebraic fact guaranteed ellipticity.

The same pattern lies at the heart of Dirac operators and spin geometry. Before spinors or gauge theory can make sense, we need to understand the multiplication rule that creates it. This is Clifford algebra.

## Starting with one direction

Take a Euclidean vector of length one and imagine assigning it a linear operator. We demand that the operator square to minus the identity. Scaling the vector by a factor of three should make the square minus nine times the identity. In words, the square of the operator records the vector's squared length, with a minus sign.

Two perpendicular unit vectors receive operators that anticommute. Multiplying first by the operator for one direction and then by the operator for the other gives the negative of multiplying them in the opposite order. This means the algebra remembers angle as well as length.

Why anticommutation? Apply the rule to the sum of two vectors. Its squared length contains twice their inner product. Expanding the square of the corresponding operator gives the two individual squares and the sum of the two cross products. Matching the two expressions forces that cross-product sum to equal minus twice the inner product times the identity.

This construction packages the entire metric inside a multiplication law. It is not merely an algebra with convenient generators: the inner product can be recovered from their anticommutator.

## The two-dimensional matrix example

Let us see actual matrices. There are three famous two-by-two complex matrices called the Pauli matrices. The first swaps the two coordinates. The second swaps them with imaginary factors. The third negates one coordinate while leaving the other unchanged.

Multiply the first two Pauli matrices by the imaginary unit and use them as operators for the two perpendicular coordinate directions. Each operator squares to minus the identity, and they anticommute. The product of the two coordinate operators is proportional to the third Pauli matrix. The signs depend on how we choose the order and the imaginary unit, but the Clifford relation does not.

These two-by-two matrices therefore represent the complex Clifford algebra of the Euclidean plane. A spinor in this model is a two-component complex column vector on which the Clifford operators act. Nothing mystical has been added. We have found a small representation of a metric-dependent algebra.

## Exterior algebra gives another representation

We already have a familiar space on which directions act: differential forms. A covector can increase form degree by exterior multiplication. The associated vector can decrease form degree by contraction. Subtract contraction from wedge multiplication. The resulting operator squares to minus the covector's squared norm.

This is Clifford multiplication on the exterior algebra. It is the symbol construction behind the de Rham operator. So Clifford multiplication is not confined to quantum particles or spinors. It is already present in the calculus of forms.

The two representations have different dimensions. On an n-dimensional space, the full exterior algebra has dimension two to the n, whereas an irreducible complex spin representation is often much smaller. The ability to realize the same Clifford relation on different modules explains why many Dirac-type operators exist, but have different kernels and different index formulas.

## Rotations hiding in pairs of vectors

Now multiply two unit vectors in the Clifford algebra. An even product can act on vectors by conjugation and implement a rotation. The group formed by suitable even products is called the spin group. Its map to the rotation group is a double covering: two elements differing by a sign produce the same physical rotation of vectors.

This is the origin of the two-to-one phenomenon that becomes important for spin structures. We did not invent a double cover for convenience. It appears when rotations are represented by products of Clifford generators, and the elements plus one and minus one act identically on vectors by conjugation.

In the plane, a rotation through a full turn returns every vector to its starting position. But the corresponding continuous path in the spin group ends at minus one, not at plus one. Only a double turn closes the lifted path. This is not a statement that ordinary vectors require two turns. It is a statement about the representation that spinors carry.

## From algebra to a differential operator

A Dirac operator combines Clifford multiplication with covariant differentiation. Choose an orthonormal frame, differentiate a spinor in each frame direction using a compatible connection, multiply each derivative by the Clifford operator for that direction, and sum.

The highest-frequency part of that operator is Clifford multiplication by the frequency covector. Because its square is minus the squared norm, the symbol is invertible away from zero frequency. Thus a Dirac operator is elliptic, just as the de Rham operator is elliptic.

But the global spinor bundle is not yet constructed. Having matrices in each tangent space does not tell us how to glue those local representations when our orthonormal frames rotate across chart overlaps. That gluing problem is the next step, and it is exactly where spin and spin-C structures enter.

The chain of ideas is now visible: a metric determines an anticommutation relation; that relation defines Clifford multiplication; products of generators encode rotations; representations carry spinors; and a connection turns the algebra into a first-order elliptic operator. Each link has an independent mathematical meaning, and we will build the global version rather than treating it as an unexplained package.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For a real Euclidean vector space \((V,g)\), define \(\mathrm{Cl}(V,g)=T(V)/\langle v\otimes v+g(v,v)1\rangle\). Then
\[c(v)c(w)+c(w)c(v)=-2g(v,w)\operatorname{id}.\]
For \(V=\mathbb R^2\), let \(\sigma_1=\begin{psmallmatrix}0&1\\1&0\end{psmallmatrix}\) and \(\sigma_2=\begin{psmallmatrix}0&-i\\i&0\end{psmallmatrix}\). Set \(c(e_1)=i\sigma_1\), \(c(e_2)=i\sigma_2\). Both square to \(-I\) and anticommute.

For forms \(\Lambda^*V^*\), \(c(\xi)=\varepsilon(\xi)-\iota_{\xi^\sharp}\); the canonical anticommutation relations imply \(c(\xi)^2=-|\xi|^2\). On a Clifford module \(S\) with compatible connection, \(D=\sum_j c(e^j)\nabla_{e_j}\). Suppressing the Fourier factor \(i\), the principal symbol satisfies \(\sigma(D,\xi)^2=-|\xi|^2I\), hence is invertible for \(\xi\ne0\).

In dimension two, \(\operatorname{Spin}(2)\cong U(1)\), and the covering map to \(SO(2)\cong U(1)\) is \(z\mapsto z^2\).

### Exercises with answers

1. **Orthogonality.** If \(g(v,w)=0\), what is \(c(v)c(w)+c(w)c(v)\)? **Answer:** zero.
2. **Length.** What is \(c(3v)^2\) for a unit vector? **Answer:** \(-9I\).
3. **Forms.** Why is wedge multiplication alone not a Clifford action? **Answer:** its square is zero for a one-form, not minus the squared norm.
4. **Cover.** How many elements of \(\operatorname{Spin}(2)\) map to a typical planar rotation? **Answer:** two, differing by sign.

### Sources and further reading

- Liviu Nicolaescu, [Notes on Seiberg-Witten Theory](https://www3.nd.edu/~lnicolae/new1.pdf), Section 1.3.
- Tim Perutz, [Basics of Seiberg-Witten Theory](https://www.imperial.ac.uk/media/imperial-college/research-centres-and-groups/geometry/junior-geometry-seminar/Seiberg-Witten-theory.pdf).
- Overviews: [Clifford algebra](https://en.wikipedia.org/wiki/Clifford_algebra), [Pauli matrices](https://en.wikipedia.org/wiki/Pauli_matrices), [Spin group](https://en.wikipedia.org/wiki/Spin_group).
