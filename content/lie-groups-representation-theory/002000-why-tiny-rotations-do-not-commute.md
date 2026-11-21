# 002000 — Why Tiny Rotations Do Not Commute

**Track:** Lie Groups, Lie Algebras, and Representations. **Preparation:** matrix multiplication, derivatives, exponential series, and the infinitesimal matrix groups introduced in `001000`. **Theme:** the Lie bracket records the first noncommutative correction to combining flows.

<!-- BEGIN SPOKEN LECTURE -->

# Why Tiny Rotations Do Not Commute

Try two physical motions. Tip a book slightly forward, then slightly to the left. Reverse the order. Even when both tips are very small, the final orientations are not exactly the same. The difference is tiny: it is a second-order effect. But it has a definite direction. If you could measure such differences accurately enough, you could recover part of the algebra of three-dimensional rotations without ever performing a large rotation.

This is the Lie bracket at work. It extracts the earliest nonzero trace of order from two infinitesimal motions.

## A commutator you can calculate

Let X and Y be matrices that generate one-parameter groups of transformations. We start with the identity, move for a short time t along X, then along Y, then undo X, then undo Y. In matrix notation the four operations form the product: exponential of tX, exponential of tY, exponential of negative tX, exponential of negative tY. Different conventions for when one says a motion occurs can reverse the order or sign; our matrix multiplication order is the one just written.

If the two motions commute, the product is exactly the identity. We moved around a closed rectangle of operations and returned to where we began. If they do not commute, the rectangle fails to close. Expand each exponential in a power series: the identity plus t times its generator plus half t squared times the square of the generator, and higher-order terms. After multiplying the four expansions, all first-order terms cancel. The leading deviation from the identity is t squared times the matrix XY minus YX.

That difference is the **commutator**, written bracket X comma Y. It is zero when X and Y commute. It changes sign when we reverse their roles. It is bilinear: doubling X doubles the bracket, and a sum distributes across it. Crucially, it is itself a valid infinitesimal generator whenever X and Y belong to a matrix Lie algebra.

To see the last point for orthogonal groups, suppose X and Y are skew-symmetric. Transpose XY minus YX. The transpose reverses products. Using X transpose equals negative X and the analogous equation for Y gives the negative of the original commutator. Thus the commutator is skew-symmetric. The allowed infinitesimal rotations are closed under this extra operation.

## A specific two-by-two calculation

Choose X to be the diagonal matrix with entries one and negative one. Choose Y to have a single one above the diagonal and zeros elsewhere. Both have trace zero, so they are in the Lie algebra of SL of two. Multiply in one order: XY equals Y. Multiply in the other: YX equals negative Y. Subtract them, and the commutator is two Y.

That tells us something precise. If a shear is represented by Y and a stretching movement by X, the order in which we perform tiny stretches and shears changes the final transformation in a direction proportional to the shear. The coefficient two comes from how stretching rescales the shear direction.

Notice that the space of all traceless two-by-two matrices is three-dimensional. We have already seen two of its directions, and their commutator points along one of those directions. Later we will name a third matrix and organize their brackets into the relations of the Lie algebra called sl two. Those relations will let us classify its finite-dimensional representations.

## Why a Lie algebra is not just a vector space

A Lie algebra is a vector space equipped with a bilinear bracket satisfying two rules. First, the bracket of X with X is zero, and the bracket is antisymmetric when the field has characteristic different from two. Second, the bracket satisfies the Jacobi identity. In words, the bracket of X with the bracket of Y and Z, plus the two cyclic rearrangements, is zero.

The Jacobi identity can look like an arbitrary technical demand. But for matrix commutators it follows by expanding the nested products. Every term such as XYZ appears twice with opposite signs. For geometric vector fields, it expresses the compatibility of composing infinitesimal changes. For matrices, it is also an algebraic consequence of associative matrix multiplication.

We need not multiply matrices to have a Lie algebra. Abstract Lie algebras can be defined solely by their vector space and bracket, and vector fields form infinite-dimensional Lie algebras. Nevertheless the matrix examples reveal what the axioms mean: the bracket measures the failure of two infinitesimal operations to commute, and the Jacobi identity constrains how these failures interact.

## Rotations and the cross product

Recall the three-dimensional correspondence between a vector a and the skew-symmetric matrix that sends v to a cross v. Call this matrix A-hat. Choose another vector b and matrix B-hat. Acting on v, their commutator produces a cross b cross v, minus b cross a cross v. The vector triple-product identity reduces the difference to a cross b, and then cross v. In other words, the commutator of A-hat and B-hat is the hat matrix belonging to a cross b.

This is a direct geometric interpretation of the Lie algebra of three-dimensional rotations. If the angular-velocity vectors are parallel, their cross product vanishes, so the infinitesimal rotations commute. If they point in different directions, the commutator points along the perpendicular cross-product direction. The second-order failure to close a tiny loop has a direction prescribed by ordinary three-dimensional geometry.

That is why we will later meet a three-dimensional representation of rotations that is naturally related to their own Lie algebra. The algebra acts on itself by commutators. This is called the adjoint representation, and in the three-dimensional rotation case it is the familiar action of rotating vectors.

## The exponential and the extra correction

For real numbers x and y, exponential x times exponential y equals exponential of x plus y. For matrices, that equation holds when X and Y commute. Otherwise, the exponential of X times the exponential of Y is generally not the exponential of X plus Y.

The Baker–Campbell–Hausdorff formula describes the correction. For sufficiently small X and Y, the logarithm of exponential X times exponential Y begins with X plus Y, then half the bracket of X and Y, followed by terms involving nested brackets. With small parameters t and s, the first correction is one half t s times the bracket. It is this term that rescues the calculation from the false assumption that matrix multiplication behaves like ordinary addition.

We will not try to memorize the full infinite series. The important structure is that the multiplication law close to the identity can be reconstructed from Lie brackets, with further corrections built from nested brackets. In suitable settings the formula converges locally. For some special algebras, such as ones whose sufficiently long nested brackets vanish, the formula terminates after finitely many terms.

This is a powerful kind of compression. A group can contain uncountably many elements, but its local multiplication is governed by finitely many structure constants once we choose a basis for a finite-dimensional Lie algebra. If the bracket of basis element i with basis element j is a linear combination of basis elements, the coefficients of those combinations encode the infinitesimal interaction. The Jacobi identity imposes equations on those coefficients.

## What a homomorphism must preserve

Suppose a smooth map between two Lie groups preserves multiplication. Differentiate it at the identity. The derivative is a linear map between their Lie algebras. It also preserves brackets: the image of the bracket of X and Y equals the bracket of the images. This is the infinitesimal shadow of a group homomorphism.

The statement has a converse with qualifications. On connected and simply connected Lie groups, a Lie-algebra homomorphism integrates to a group homomorphism into another Lie group. If the domain is not simply connected, global loops may obstruct integration. On the additive real line, infinitesimal angular velocity can be any real number. On the circle, a well-defined complex one-dimensional representation must respect the fact that theta and theta plus two pi denote the same group element. Its angular frequency must be an integer.

So the derivative preserves a tremendous amount, but it can forget which trips around a closed loop should count as identity. This missing global information will eventually explain the difference between representations of SU two and SO three.

## A bridge to computation

There is a practical consequence in numerical geometry. Suppose a program updates orientation by adding three angle coordinates as though rotations were translations. The approximation can be adequate for tiny isolated steps, but the accumulated orientation can depend on the order of updates. Lie group integrators instead respect the group law: use a generator to build an incremental rotation with an exponential, then compose the rotations by matrix multiplication or a suitable equivalent representation.

The Lie bracket explains why careless coordinate addition fails. It tells us exactly what kind of order-sensitive error appears first. In physics, robotics, computer vision, and control, this is not a decorative abstraction. It is the mechanism that distinguishes a sequence of rotations from a single vector addition.

We began with a book that did not return to the same orientation after reversing two tiny movements. We can now name the mismatch and compute it: the matrix commutator, multiplied by the product of the small step sizes to leading order. The Lie algebra is a space of directions equipped with precisely the operation needed to keep track of noncommuting directions. The exponential brings us back to finite transformations, but the bracket tells us why those finite transformations cannot generally be combined by ordinary addition.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

\[
C(t)=e^{tX}e^{tY}e^{-tX}e^{-tY}
=I+t^2[X,Y]+O(t^3),\qquad [X,Y]=XY-YX.
\]
\[
[X,[Y,Z]]+[Y,[Z,X]]+[Z,[X,Y]]=0.
\]
For \(X,Y\) small in a matrix Lie algebra, \(\log(e^Xe^Y)=X+Y+\tfrac12[X,Y]+\tfrac1{12}([X,[X,Y]]+[Y,[Y,X]])+\cdots\). This is a local series, not a globally single-valued logarithm formula.

Let \(H=\bigl(\begin{smallmatrix}1&0\\0&-1\end{smallmatrix}\bigr)\), \(E=\bigl(\begin{smallmatrix}0&1\\0&0\end{smallmatrix}\bigr)\). Then \([H,E]=2E\). For \(a,b\in\mathbb R^3\), \([\hat a,\hat b]=\widehat{a\times b}\).

**Exercises and solutions.** (1) Compute \([E,E]\). *Zero.* (2) For diagonal \(D=\operatorname{diag}(\lambda_1,\lambda_2)\), compute \([D,E]\). *\((\lambda_1-\lambda_2)E\).* (3) Why is the circle's smooth character \(e^{i c\theta}\) well-defined only for integer \(c\)? *It must agree at angles differing by \(2\pi\), so \(e^{2\pi i c}=1\).* (4) Does a commuting pair have zero Baker–Campbell–Hausdorff correction? *Yes, all nested commutators vanish.*

### Sources and further reading

- MIT OCW 18.745 (2020), Lie algebras, exponential map, BCH and fundamental theorems: https://ocw.mit.edu/courses/18-745-lie-groups-and-lie-algebras-i-fall-2020/resources/lecture-notes/
- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations*, 2nd ed., chapters 3, 4 and 6: https://doi.org/10.1007/978-3-319-13467-3
- Related existing lecture: `topology-geometry:008000` on flows and vector-field brackets.
