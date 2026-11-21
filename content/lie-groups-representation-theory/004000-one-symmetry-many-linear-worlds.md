# 004000 — One Symmetry, Many Linear Worlds

**Track:** Lie Groups, Lie Algebras, and Representations. **Preparation:** eigenvectors, invariant subspaces, group homomorphisms, Lie brackets. **Theme:** representations turn continuous symmetries into linked families of linear transformations.

<!-- BEGIN SPOKEN LECTURE -->

# One Symmetry, Many Linear Worlds

Imagine rotating a disk. A dot on its rim moves around a circle. A velocity vector rotates with it. A photograph of the disk changes as a whole image. A vibrating membrane may have several modes whose phases change at different speeds. These are all responses to the *same* group of rotations, yet they occur in different vector spaces and may behave very differently.

Representation theory investigates these different linear worlds. A representation of a group G on a vector space V assigns an invertible linear map to each group element, preserving multiplication. If g followed by h is represented by two matrices, the product gh must be represented by their matrix product. In Lie theory we also ask for a sufficiently smooth dependence on the group element, because we want to differentiate the representation.

Earlier algebra lectures developed representations of finite groups and their characters. Continuous groups add a new feature: a representation can be studied through the Lie algebra, and smooth one-parameter motions in the group become exponential families of matrices on the representation space.

## Differentiating the action

Let rho be a smooth finite-dimensional representation. For a Lie-algebra element X, take the group path exponential tX. Apply rho, then differentiate at time zero. The resulting linear operator on V is called d rho of X. It is the infinitesimal action of X on the vectors of the representation.

The derivative behaves exactly as it should. It is linear in X, and it respects Lie brackets: d rho of the bracket of X and Y equals the matrix commutator of d rho X and d rho Y. Furthermore, along a one-parameter subgroup, rho of exp tX equals exp of t times d rho X.

This means an enormous family of representation matrices near the identity can be recovered from a much smaller collection of generators and their commutation relations. We can work with linear operators first, then reconstruct the continuous transformations they generate.

But global topology still enters. An operator may satisfy the Lie-algebra relations and yet fail to define a representation of the *particular* Lie group we want, because winding around a closed loop might not return the operator to the identity. One learns the infinitesimal action locally and then checks whether it descends to a well-defined group action globally.

## The circle and integer frequencies

Our cleanest example is the circle group. Write its elements as complex numbers of modulus one, or equivalently as angles theta with angles differing by a full turn identified. A one-dimensional complex representation must send each rotation to a nonzero complex number, multiplicatively and continuously.

For each integer n, consider the rule that sends rotation by theta to the complex number exponential of i n theta. This is a representation. Adding two angles multiplies the corresponding complex numbers. And when theta increases by two pi, the value returns to itself precisely because n is an integer.

Why can we not use a noninteger n? If theta and theta plus two pi denote the *same group element*, they must receive the same matrix. A noninteger n generally assigns different values, so it fails to define a function on the circle group. The Lie algebra alone would let us differentiate a formula with arbitrary real n; the global periodicity of the group restricts n to integers.

There is something surprisingly physical about these integers. Acting on a function of an angle, rotation can move the argument of the function. The complex waves with n oscillations around the circle, sine and cosine combined into complex exponentials, transform by precisely these one-dimensional characters. Fourier modes are irreducible representations of the circle group.

A general signal can be decomposed into these modes under suitable analytic hypotheses. Rotation acts on each mode by multiplying by a phase, rather than mixing all its coordinates. Representation theory has turned the operation of rotating a complicated function into separate scalar operations on simple building blocks.

The tensor product of the character n and the character m is the character n plus m. Its phase is the product of their phases, which equals exponential of i times n plus m times theta. This is the first glimpse of the arithmetic of weights: integers attached to representations behave additively under tensor products.

## Invariant subspaces and irreducibility

Suppose a representation acts on a vector space V, and W is a subspace preserved by every group element. We call W invariant. We can restrict the action to W, and we can ask whether there is another invariant subspace completing it to the whole space.

If no nonzero proper invariant subspaces exist, the representation is irreducible. Irreducibles are the basic pieces from which many other representations can be assembled. But decomposition into invariant pieces is not automatic. As we saw for finite groups in positive characteristic, an invariant subspace need not have an invariant complement. For noncompact Lie groups, failure can occur even over the complex numbers and in characteristic zero.

Consider the additive group of real numbers represented by upper-triangular two-by-two matrices with ones on the diagonal and t in the upper-right corner. Multiplying two such matrices adds the parameters, so this is a genuine representation of the additive group. The line spanned by the first coordinate vector is invariant. Yet there is no different invariant line providing a complement: any vector with a nonzero second coordinate is moved by the shear into a different line.

This two-dimensional representation does not split into a direct sum of one-dimensional representations. Its infinitesimal generator is a nonzero nilpotent matrix. The example warns us not to transfer a theorem from compact groups to arbitrary continuous groups.

## Why compact groups split

For a compact Lie group, there is a replacement for the finite average used in Maschke's theorem. We integrate over the group using its normalized Haar probability measure. Haar measure is invariant under translation, so integrating over the group is the continuous analogue of summing uniformly over a finite group.

Start with any positive-definite Hermitian inner product on the representation space. Average the inner product after acting by each group element. The result is another positive-definite Hermitian inner product, now invariant under the group. This is a direct calculation: translating the group element inside the integral leaves Haar measure unchanged.

Once the inner product is invariant, any invariant subspace W has an invariant orthogonal complement. If a vector is perpendicular to W, then applying a group transformation preserves inner products and carries W onto itself, so the transformed vector remains perpendicular to W. Consequently every finite-dimensional complex representation of a compact Lie group splits into irreducible pieces.

This is the compact-group counterpart of Maschke's theorem. The proof is different in its surface details, replacing a finite sum by an integral, but the idea is the same: average an arbitrary piece of linear algebra until it respects the symmetries.

Compactness is doing real work. Without a finite invariant measure that can be normalized across the whole group, this averaging argument does not go through in general. A noncompact group may have other good representation theories, but complete reducibility cannot simply be assumed.

## Schur's lemma and what it really says

Let two complex irreducible representations be given. A linear map between their spaces is an intertwiner if it commutes with the group actions in the appropriate sense. Schur's lemma says that a nonzero intertwiner between irreducibles is an isomorphism. If the two representations are inequivalent, every intertwiner between them is zero. If they are the same finite-dimensional complex irreducible representation, every endomorphism intertwiner is a scalar multiple of the identity.

The proof of the last assertion uses an ordinary eigenvector. A complex matrix has an eigenvalue. If an operator commutes with the representation, the eigenspace for that eigenvalue is invariant. Irreducibility forces it to be the whole space, so the operator equals that eigenvalue times the identity.

This is one reason irreducible components are powerful. An operator that respects all the symmetries cannot act arbitrarily inside an irreducible piece. In spectral problems, this constrains degeneracies and allowable couplings. In quantum mechanics, conservation laws and selection rules often become statements about intertwiners and tensor products. In harmonic analysis, decomposition into irreducibles is a way of finding coordinates in which symmetric operators simplify.

We should note the field restriction. Over the real numbers the commuting endomorphism algebra of an irreducible representation can be larger than the real scalars. Complex Schur's lemma has the clean scalar conclusion because the field is algebraically closed.

## Characters return, but with a new scale

For a finite-dimensional representation, take the trace of the matrix assigned to a group element. The resulting function is its character. It is constant on conjugacy classes, because trace is unchanged by conjugating a matrix. Characters of compact groups retain deep orthogonality and decomposition properties, now with integrals over Haar measure instead of finite sums.

For the circle, the characters are exactly our integer-frequency exponentials. Integrating the product of one character with the complex conjugate of another over a full turn gives zero if the frequencies differ, and one if they agree. That is ordinary Fourier orthogonality understood as a representation-theoretic statement.

For nonabelian groups such as SU two, irreducible representations can have dimension greater than one. Their characters are no longer single Fourier waves, but they still encode the decomposition of tensor products and the multiplicity of irreducible pieces. We will construct a family of these representations explicitly rather than invoking an abstract existence theorem and moving on.

A continuous symmetry can therefore appear in many mathematical settings: as motion of a point, as a transformation of a vector, or as a change of an entire function. The representation describes which linear world we have chosen. Differentiating it exposes the infinitesimal generators. Compactness helps us split that world into irreducibles. And the characters tell us how the irreducibles fit together. With these tools in place, we are ready for a concrete group whose representations can be classified using only three small matrices.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For a smooth representation \(\rho:G\to GL(V)\), define
\[
d\rho(X)=\left.\frac{d}{dt}\right|_{0}\rho(\exp(tX)),\quad
 d\rho([X,Y])=[d\rho(X),d\rho(Y)],\quad
 \rho(\exp X)=\exp(d\rho X).
\]
For \(S^1\), \(\chi_n(e^{i\theta})=e^{in\theta}\) for \(n\in\mathbb Z\), and \(\chi_n\otimes\chi_m=\chi_{n+m}\). Orthogonality: \(\frac1{2\pi}\int_0^{2\pi}\chi_n\overline{\chi_m}\,d\theta=\delta_{nm}\).

For compact \(G\), given any Hermitian inner product \(\langle\ ,\ \rangle_0\) on \(V\), set \(\langle v,w\rangle_G=\int_G\langle\rho(g)v,\rho(g)w\rangle_0\,dg\). The result is invariant, so \(W^\perp\) is invariant whenever \(W\) is.

**Counterexample outside compactness:** \(\rho(t)=\left(\begin{smallmatrix}1&t\\0&1\end{smallmatrix}\right)\) represents \((\mathbb R,+)\) on \(\mathbb C^2\), preserving \(\mathbb C e_1\) without invariant complementary line.

**Exercises and solutions.** (1) Which continuous complex characters of \(S^1\) are trivial? *Only \(n=0\).* (2) Compute \(\chi_2\chi_3\). *\(\chi_5\).* (3) Why does averaging an inner product over a compact group give an invariant inner product? *Substitute \(gh\) in the integral and use Haar invariance.* (4) Why does the upper-triangular shear representation not split? *Its only invariant one-dimensional subspace is the line spanned by the first basis vector.*

### Sources and further reading

- MIT OCW 18.745 (2020), lecture 11 on representations of groups and Lie algebras: https://ocw.mit.edu/courses/18-745-lie-groups-and-lie-algebras-i-fall-2020/resources/lecture-notes/
- Pavel Etingof et al., *Introduction to Representation Theory* (MIT author-hosted text): https://math.mit.edu/~etingof/replect.pdf
- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations*, 2nd ed., basic representation theory and compact-group chapters: https://doi.org/10.1007/978-3-319-13467-3
- Existing preparation: `abstract-algebra:013000` for finite-group characters, and `linear-algebra:006000` for eigenspaces and inner products.
