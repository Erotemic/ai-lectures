# 001000 — When Symmetry Moves Continuously

**Track:** Lie Groups, Lie Algebras, and Representations. **Preparation:** matrices, derivatives, and elementary groups. **Theme:** a continuous symmetry group has linear information near its identity.

<!-- BEGIN SPOKEN LECTURE -->

# When Symmetry Moves Continuously

A square has a finite collection of exact symmetries. We can list the rotations and reflections, make a multiplication table, and be finished. A circle has a different sort of symmetry. Rotate it by one degree, half a degree, or a thousandth of a degree; every intermediate angle is another symmetry. The group has infinitely many members, arranged so that one rotation can approach another continuously.

The phrase *Lie group* gives a name to this combination: a group whose elements also form a smooth geometric space, with multiplication and inversion varying smoothly. The group structure tells us how transformations compose. The smooth structure lets us differentiate that composition. From their interaction we can extract a new object, a Lie algebra. Its elements are not complete transformations but infinitesimal directions in which a transformation can begin to move.

We will build that object with matrices. This keeps the first encounter grounded in linear algebra rather than requiring a general theory of smooth manifolds.

## A rotation and its first derivative

Write a plane rotation by an angle theta as a two-by-two matrix. The first row consists of cosine theta and negative sine theta. The second row consists of sine theta and cosine theta. Multiplying rotations adds angles: rotating by theta and then by phi is rotation by theta plus phi. The identity transformation is rotation by zero.

Now imagine slowly turning the plane, beginning at zero angle. Ask only for the instantaneous velocity of the matrix at the beginning. Differentiating cosine gives zero at zero; differentiating sine gives one. The resulting matrix, which we will call J, has first row zero, negative one, and second row one, zero.

There is a coincidence worth noticing: J happens to be a quarter-turn rotation itself. That does not mean infinitesimal generators are generally group elements. Their defining role is to give the derivative at the identity. What J supplies here is the first-order approximation to a *small* rotation: the identity plus theta times J, up to an error of order theta squared. That approximation does not exactly preserve lengths when theta is nonzero. The exact rotation is recovered from the matrix exponential of theta J. The derivative gives the local direction; the exponential reconstructs the continuous family.

Why bother with the derivative when we already know sine and cosine? Because for a much larger group we may not know every transformation explicitly, yet a few simple conditions on its infinitesimal generators can reveal the structure of the whole family near the identity.

## Orthogonal matrices and a tangent condition

The group O of n consists of all real n-by-n matrices Q satisfying Q transpose times Q equals the identity. This is exactly the equation saying the transformation preserves Euclidean inner products. Its determinant is either positive one or negative one. The subgroup SO of n is the determinant-positive part: rotations without reflections.

Suppose Q of t is a smooth path of orthogonal matrices beginning at the identity. Call its derivative at zero X. Differentiate the equation Q transpose times Q equals the identity. At time zero both copies of Q are the identity, so the product rule gives X transpose plus X equals zero.

That equation says X is skew-symmetric. Conversely, if X is skew-symmetric, its matrix exponential produces an orthogonal matrix for every real time. Indeed, the transpose of the exponential of tX is the exponential of negative tX, and the two multiply to the identity. The resulting path starts at the identity and therefore stays in SO of n rather than crossing into the reflection component.

We have discovered the Lie algebra of SO of n: precisely the skew-symmetric real matrices. A general three-by-three matrix has nine real entries. A skew-symmetric one has zeros on its diagonal, while the three entries above the diagonal determine those below. So the three-dimensional rotation group has three independent infinitesimal directions. That matches our intuition: a small rotation can tilt around any one of three independent axes.

The tangent space at the identity of a Lie group is a vector space. Here we have exhibited it as a particular vector subspace of matrices. But a Lie algebra has additional structure beyond vector addition. The extra operation will come from how two infinitesimal movements fail to commute. We will reach that shortly.

## Other matrix groups, other linear conditions

Consider all invertible real n-by-n matrices, the general linear group. Near the identity, any sufficiently small matrix perturbation remains invertible. There is therefore no linear restriction on the derivative. Its Lie algebra consists of all real n-by-n matrices.

Now restrict to determinant one, forming SL of n. Differentiate the determinant along a path through the identity. The derivative of the determinant at the identity in direction X is the trace of X, the sum of its diagonal entries. Thus a determinant-one path must have a traceless derivative. The converse again comes from the exponential: the determinant of exp tX equals the exponential of t times the trace of X. When the trace is zero, the determinant stays one. The Lie algebra of SL of n is therefore the space of traceless real matrices.

Over the complex numbers, a unitary matrix U preserves the complex inner product: U conjugate transpose times U equals the identity. Differentiating gives X conjugate transpose plus X equals zero. Such matrices are called skew-Hermitian. For SU of n we add determinant one, so the generators are skew-Hermitian *and* traceless. These are real Lie algebras: their allowed scalar multiples are real, even though their matrix entries are complex.

These examples have a common pattern. Begin with an equation defining the symmetry group. Insert a path through the identity. Differentiate the equation. The derivative lives in a linear space of allowable infinitesimal motions. Then use matrix exponentials to verify that these motions really generate group paths.

## What makes this a group rather than merely a curved space?

A sphere is a smooth space. The rotation group is also a smooth space. But a sphere does not come with a natural multiplication of its points that makes every point an invertible symmetry. To say a space is a Lie group is not merely to say it is smooth; it must also carry group multiplication and inversion compatible with its smoothness.

Multiplication tells us how to transport a tangent direction from the identity to any other point of the group. If we know how to move infinitesimally at the identity, we can move in an analogous way from another transformation by multiplying on one side. These transported directions form what geometers call left-invariant vector fields. Their brackets reproduce the Lie algebra structure we will uncover from matrices.

This is why the tangent space at one special point can carry information about movements everywhere in the group. The group law makes all points geometrically related. Ordinary manifolds have tangent spaces at each point; Lie groups have a canonical way to compare them by translation.

## A three-dimensional surprise

A skew-symmetric three-by-three matrix can be encoded by a vector with three real coordinates. Given a vector a, form the matrix whose action on another vector v is the cross product of a with v. The resulting matrix is skew-symmetric, and every skew-symmetric three-by-three matrix arises this way.

This correspondence is useful because infinitesimal rotations can now be described as angular-velocity vectors. Two different angular velocities can be added. Multiplying their matrices is a more delicate operation, but their commutator, matrix X times Y minus Y times X, has a particularly clean description. Under this encoding it corresponds to the cross product of the angular-velocity vectors.

So something elementary from vector calculus, the cross product, will reappear as the intrinsic algebraic operation of three-dimensional rotations. It is not an accident. The cross product measures the order-sensitive interaction of two small rotations.

This also hints at a caution. The cross product exists in this convenient three-dimensional form because of special features of three-dimensional Euclidean space. The matrix commutator is more general: it makes sense in every matrix size and supplies a Lie bracket for many different groups.

## Local information is not the whole group

The derivative of an angular rotation does not record how many full turns a path has completed. The real line under addition and the circle group of complex numbers of modulus one both have one-dimensional abelian Lie algebras. Locally, both look like a straight line of possible infinitesimal movements. Globally, one stretches indefinitely, while the other closes on itself after a full turn.

Likewise, a Lie algebra captures the connected group's local structure, but it need not determine the group's global topology. To understand which representations exist or how paths close, we may need additional information beyond the algebra. This distinction will become concrete when we compare SU of two with SO of three.

We can now describe the central question of Lie theory with some precision. Given a smooth family of symmetries, how much can we learn by replacing finite transformations with their infinitesimal generators? The remarkable answer is that we can learn an enormous amount: which small motions combine, which linear actions are possible, which invariant geometric structures exist, and often which finite-dimensional representations can occur. But the transition must be made carefully. An infinitesimal rotation is not itself the finished rotation, and a local algebra is not automatically a complete description of a global group.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For a matrix Lie group \(G\le GL_n(\mathbb F)\), its Lie algebra is \(\mathfrak g=T_I G\). For \(X\in\mathfrak g\) in the matrix-group setting, \(\exp(tX)\in G\). The bracket is \([X,Y]=XY-YX\).

\[
R(\theta)=\begin{pmatrix}\cos\theta&-\sin\theta\\ \sin\theta&\cos\theta\end{pmatrix},\quad
J=R'(0)=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\quad R(\theta)=e^{\theta J}.
\]

\[
\begin{aligned}
\mathfrak{gl}_n(\mathbb R)&=M_n(\mathbb R),\\
\mathfrak{so}_n&=\{X:X^T=-X\},\\
\mathfrak{sl}_n(\mathbb R)&=\{X:\operatorname{tr}X=0\},\\
\mathfrak{su}_n&=\{X\in M_n(\mathbb C):X^*=-X,\operatorname{tr}X=0\}.
\end{aligned}
\]

Use \(\frac{d}{dt}|_0 Q(t)^TQ(t)=X^T+X\); \(\det e^X=e^{\operatorname{tr}X}\). If \(\widehat a v=a\times v\) in \(\mathbb R^3\), then \([\widehat a,\widehat b]=\widehat{a\times b}\).

**Exercises with solutions.** (1) How many dimensions does \(\mathfrak{so}_4\) have? *Six, one for each entry above the diagonal.* (2) Show that \(\mathfrak{sl}_2\) is closed under commutators. *The trace of \(AB-BA\) is zero by cyclicity of trace.* (3) Is \(\exp(tX)\) orthogonal if \(X^T=X\) and \(X\ne0\)? *Not in general; orthogonality requires skew-symmetry (except special isolated times).* (4) Does \(\mathbb R\) have the same Lie algebra as \(S^1\)? *Yes, both are one-dimensional with zero bracket; their global topologies differ.*

### Sources and further reading

- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations*, 2nd ed., chapters on matrix groups and the exponential: https://doi.org/10.1007/978-3-319-13467-3
- MIT OpenCourseWare 18.745 (2020), lectures 2, 6, 7, and 8: https://ocw.mit.edu/courses/18-745-lie-groups-and-lie-algebras-i-fall-2020/resources/lecture-notes/
- Existing preparation: `linear-algebra:001000`, `abstract-algebra:001000`, and `topology-geometry:008000`.
