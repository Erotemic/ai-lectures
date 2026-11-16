# 030300 - Spinor Bundles and Dirac Operators: Differentiating a Spinor

**Track:** Topology and Geometry. **Background:** Clifford representations, spin-C structures, connections, elliptic operators. **Central question:** how do Clifford multiplication and covariant differentiation combine into a global differential operator?

<!-- BEGIN SPOKEN LECTURE -->

# Spinor Bundles and Dirac Operators: Differentiating a Spinor

We have constructed the Clifford algebra in one Euclidean space and examined the extra gluing data needed to make its representations global. We can now ask a more dynamic question. Once a spinor is defined across a manifold, what does it mean to differentiate it?

A spinor cannot be differentiated by comparing its components at two different points without additional information. The components refer to local spin frames, just as the components of an ordinary vector refer to a local basis. A connection supplies a consistent way to compare them. A Dirac operator then uses Clifford multiplication to combine all the directional covariant derivatives into one first-order operator.

## From a frame to a spin frame

On a small region, choose an oriented orthonormal frame of tangent vectors. The spinor bundle looks like the region times a fixed complex spin representation. Each tangent direction has a Clifford multiplication operator acting on that representation. We can write the derivative of a spinor as a collection of derivatives of its components plus correction terms describing how the spin frame turns.

These correction terms are not optional decoration. An ordinary derivative would change incorrectly under a moving frame. The Levi-Civita connection tells us how the orthonormal frame rotates. A spin or spin-C structure lifts that frame rotation to the spinor representation, producing the spin connection.

In a spin-C structure there is another ingredient: a unitary connection on the determinant line bundle. The combined connection on spinors includes half the determinant-line connection in local formulas. This factor of one half reflects the way the circle phase enters the spin-C group, and it is responsible for some of the factors appearing later in curvature formulas.

## Assembling directional derivatives

Choose an orthonormal frame with directions one through n. Covariantly differentiate the spinor in each direction. Then Clifford-multiply that derivative by the corresponding dual covector, and add the results. The sum is the Dirac operator.

The formula looks coordinate dependent, but it is not. Rotating the orthonormal frame rotates both the derivative components and the Clifford operators. Because the connection and the Clifford action transform compatibly, the final sum is unchanged. This is why we spent time on gluing and compatibility before writing an operator.

At high frequency, the connection's lower-order coefficients do not affect the principal symbol. The symbol is simply Clifford multiplication by the frequency covector, up to the conventional imaginary factor used in Fourier analysis. Its square is minus the squared frequency length. So away from zero frequency the symbol is invertible. Every Dirac operator of this kind is elliptic.

## The simplest Dirac operator on a circle

A circle of circumference two pi is a useful laboratory. In a flat trivialization and with one choice of spin structure, the Dirac operator can be represented by minus the imaginary unit times angular differentiation. Its eigenvectors are the periodic complex exponentials. Their eigenvalues are the integers. The constant spinor is a zero mode.

Change only the spin structure. Under the other choice, spinors become antiperiodic after one turn. Their Fourier frequencies shift by one half. The eigenvalues are now the half-integers, and no zero mode remains.

The metric is identical in both cases; the local differential expression looks the same. The difference lies in the global identification of the spinor at the end of the circle. This is a concrete reminder that local elliptic formulas do not determine global kernels by themselves.

## Chirality in even dimensions

In an even-dimensional oriented Riemannian manifold, the complex spinor representation splits into two pieces, called positive and negative chirality. Clifford multiplication by a tangent covector exchanges them. So the Dirac operator exchanges them as well.

In four dimensions this gives a particularly important map: the positive spinor bundle to the negative spinor bundle. On a closed four-manifold, it has finite-dimensional kernel and cokernel once we place it in appropriate Sobolev spaces. The difference of their dimensions is its index.

In Seiberg-Witten theory, the unknowns include a unitary determinant-line connection and a positive spinor. The first equation says the Dirac operator coupled to that connection kills the spinor. The second equation constrains the self-dual part of the line's curvature by a quadratic expression in the spinor. The index of the chiral Dirac operator will contribute to the expected dimension of the monopole moduli space.

## Three operators to keep separate

Our de Rham operator, a spin Dirac operator, and a spin-C Dirac operator share the Clifford symbol pattern. But they act on different bundles. The de Rham operator acts on the full exterior algebra. A spin Dirac operator acts on spinors associated with a spin structure. A spin-C Dirac operator acts on spinors associated with a spin-C structure and depends on a choice of determinant-line connection.

Their indices need not agree. On the two-sphere, the de Rham parity operator has index two, the Euler characteristic. The untwisted spin Dirac operator has index zero. That difference is not a contradiction, because the bundles and their grading are different.

The next step is to square a Dirac operator. The result will connect the first-order Dirac equation to a second-order Laplacian plus curvature. This is the key analytic identity used to prove vanishing theorems and establish estimates for spinors. The operator is now fully constructed, so we can examine that curvature identity without treating it as a mysterious formula.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For a Hermitian Clifford module \((S,c)\) with compatible connection \(\nabla^S\) and local orthonormal frame \(e_j\),
\[D=\sum_{j=1}^n c(e^j)\nabla^S_{e_j}.\]
Under the Riemannian convention \(c(\xi)^2=-|\xi|^2\), \(\sigma_1(D)(x,\xi)=i c(\xi)\) with the Fourier \(e^{ix\xi}\) convention; it is invertible for \(\xi\ne0\).

In even dimension, \(S=S^+\oplus S^-\) with \(c(\xi):S^\pm\to S^\mp\), and \(D^+:\Gamma(S^+)\to\Gamma(S^-)\). On a spin-C manifold with determinant line \(L\) and connection \(A\), the induced spinor connection is written \(\nabla_A\); locally it contains a half-weight contribution from the determinant-line connection. In dimension four \(\operatorname{rank}_\mathbb C S^\pm=2\).

On the unit-radius flat circle, use \(D=-i\frac{d}{d\theta}\). For periodic spinors \(\psi(\theta+2\pi)=\psi(\theta)\), its spectrum is \(\mathbb Z\); for antiperiodic spinors \(\psi(\theta+2\pi)=-\psi(\theta)\), its spectrum is \(\mathbb Z+\frac12\). This model describes the boundary condition in a chosen local spin trivialization.

### Exercises with answers

1. **Frame change.** What corrects componentwise differentiation in moving spin frames? **Answer:** the compatible spinor connection.
2. **Principal symbol.** Why is the Dirac symbol invertible for nonzero covectors? **Answer:** its Clifford square is a nonzero scalar multiple of the identity.
3. **Circle.** Which spin structure permits a flat zero mode in the stated circle model? **Answer:** the periodic one.
4. **Chirality.** Where does the chiral Dirac operator map positive spinors in dimension four? **Answer:** into negative spinors.

### Sources and further reading

- Liviu Nicolaescu, [Notes on Seiberg-Witten Theory](https://www3.nd.edu/~lnicolae/new1.pdf), spinor connections and Dirac operators.
- Tim Perutz, [Basics of Seiberg-Witten Theory](https://www.imperial.ac.uk/media/imperial-college/research-centres-and-groups/geometry/junior-geometry-seminar/Seiberg-Witten-theory.pdf).
- Overviews: [Dirac operator](https://en.wikipedia.org/wiki/Dirac_operator), [Spinor](https://en.wikipedia.org/wiki/Spinor), [Spin-C structure](https://en.wikipedia.org/wiki/Spinc_structure).
