# 004500 — Two projections and the classification of pairs

**Track:** G3 audio paper track. **Draft:** new G3 lecture, 12 November 2026. **Section:** geometry. **Audience:** principal angles, the angle operator, positive square roots, polar decomposition.

<!-- BEGIN SPOKEN LECTURE -->

Two projections and the classification of pairs

When are two configurations of subspaces the same? Suppose U and V are closed subspaces of a Hilbert space E, and U prime and V prime are closed subspaces of another Hilbert space E prime. Call the two pairs equivalent if there is a unitary map from E onto E prime that carries U onto U prime and V onto V prime at the same time. A unitary preserves lengths and inner products, so it preserves everything geometric about the pair: the angles, the norms of the difference of the projections, whether one subspace can be rotated onto the other. The question is which data decide equivalence.

The answer has three parts, and these are the results of this lecture. First, Halmos's two-subspace theorem: every pair splits the space into five mutually perpendicular pieces. On four of them, each projection is either zero or the identity. On the fifth, the generic part, the pair looks exactly like two lines in a plane, except that the angle between the lines is an operator rather than a number. Second, the classification: two pairs are equivalent exactly when the four elementary pieces have the same dimensions and the angle operators on the generic parts are unitarily equivalent. Davis and Kahan state this as Theorem 3.1 of their paper, in terms of the two directed angle operators Theta zero and Theta one. Third, when the sine of the angle is a compact operator, the generic angle operator is determined by a list of eigenvalues, and the classification becomes a list of principal angles again.

Throughout, P is the orthogonal projection onto U and Q is the projection onto V.

The finite-dimensional case

Begin where everything is visible. In a plane, two lines through the origin form a pair, and two such pairs are equivalent exactly when their angles agree. A rotation, possibly followed by a reflection, carries one configuration to the other.

In higher finite dimensions, use principal vectors. For each principal angle theta i strictly between zero and ninety degrees, there is a unit source vector x i, and the corresponding target vector y i equals cosine theta i times x i plus sine theta i times a unit vector w i perpendicular to U. The x's and w's together are orthonormal. Now take a second pair with the same principal angles. It has its own vectors x i prime and w i prime. A unitary that sends each x i to x i prime and each w i to w i prime automatically sends each y i to y i prime, because y i is built from x i and w i with the same two coefficients. It therefore carries the principal part of U onto that of U prime and the principal part of V onto that of V prime.

What else must match? The directions common to both subspaces, the source directions perpendicular to the target, the target directions perpendicular to the source, and whatever is perpendicular to both. These four leftover spaces must have the same dimensions in the two pairs, and then the unitary can be completed on them in any way. So in finite dimensions, a pair is classified by its principal angles strictly between zero and ninety degrees, counted with multiplicity, together with four dimensions. The rest of this lecture shows that the same structure survives in infinite dimensions, with the list of angles replaced by an operator.

The four elementary pieces

Each projection splits the space into its range and its kernel. Intersecting a piece from one with a piece from the other produces four subspaces.

The common part is U intersected with V: vectors fixed by both projections. The exterior part is the orthogonal complement of U intersected with the complement of V: vectors killed by both projections. The source defect is U intersected with the complement of V: source vectors perpendicular to the whole target. The paper calls this D zero. The target defect is the complement of U intersected with V: target vectors perpendicular to the whole source. The paper calls this D one.

On each of these four, both projections act trivially, as zero or as the identity. Each of the four is mapped into itself by both P and Q. And they are mutually perpendicular: for instance, a vector of U is perpendicular to every vector of the complement of U, which separates the common part and the source defect from the other two, and a vector of V is perpendicular to every vector of the complement of V, which separates the common part from the source defect and the target defect from the exterior part.

The difference of the projections sees these pieces clearly. P minus Q is zero on the common and exterior parts, plus one on the source defect, and minus one on the target defect. The defects are where the two subspaces meet at right angles. When the norm of P minus Q is less than one, both defects must be zero, since a vector on which P minus Q acts as plus or minus one would give norm one. Davis and Kahan call a pair acute when both defects are zero. In finite dimensions the two conditions agree, because then the largest angle is attained and is below ninety degrees. In infinite dimensions the defects can vanish while angles approach ninety degrees, so that the norm of P minus Q equals one; the defect condition is the weaker of the two.

The generic part

The fifth piece, the generic part, is the orthogonal complement of the sum of the four elementary pieces. Call it M. Because each elementary piece is mapped into itself by the self-adjoint projections P and Q, so is the orthogonal complement M. We can therefore study the two projections on M separately.

Inside M, none of the four intersections survives. There is no common direction, no source vector perpendicular to the target, and so on. This is what generic means: the two subspaces, restricted to M, are in general position. Let K be the part of U inside M, and L the part of the complement of U inside M. So M is K plus L, and P acts on M as the identity on K and zero on L.

Now compress Q to K, exactly as in the construction of the angle operator. The compression P Q P on K is a positive contraction; write it as C squared, where C is its positive square root, the cosine of the generic angle. Let S be the positive square root of the identity minus C squared, the generic sine. Two facts follow from genericity. C has no kernel: if C x were zero for a vector x of K, then Q x would be zero, and x would be a source vector perpendicular to the target, which does not exist inside M. And C has no eigenvalue one: if the length of Q x equalled the length of x, then x would lie in V, making it a common direction, which also does not exist inside M. So neither C nor S kills any nonzero vector. In angle language, the generic angle operator has no eigenvalue zero and no eigenvalue ninety degrees, although its spectrum may come arbitrarily close to either end.

Next, look at how Q mixes the two halves of M. Take a vector x of K, apply Q, and keep the part in L. Call this crossing map B: B is the identity minus P, times Q, restricted to K. Let us compute B star B. It equals P Q, times the identity minus P, times Q P on K. Expanding the identity minus P, this is P Q P minus P Q P Q P, which is C squared minus C to the fourth. That factors as C squared times the identity minus C squared, which is C squared S squared. So the modulus of B is C times S.

The polar decomposition writes B as a partial isometry W times its modulus C S. Genericity again ensures W is a full unitary identification of K with L: no vector of K is lost, and nothing in L is missed. Use W to identify L with a second copy of K. Then M becomes K plus K, and in these coordinates P is the block matrix with the identity in the top left corner and zeros elsewhere. Q has C squared in the top left, C S in the bottom left, and, because Q is self-adjoint, C S in the top right. The bottom right block is forced. Write out the equation Q squared equals Q in the bottom left corner: C S times C squared, plus the bottom right block times C S, must equal C S. So the bottom right block times C S equals C S times the identity minus C squared, which is C S times S squared. All of these operators are functions of C and commute with one another, and C S has dense range, so the bottom right block is S squared.

Here is Halmos's form for the generic part. On K plus K, P is the projection onto the first copy of K. Q is the block matrix with entries C squared, C S, C S, S squared. That is the projection onto the set of pairs C h, S h, for h in K. In the plane, the projection onto the line at angle theta has entries cosine squared, cosine times sine, cosine times sine, sine squared. The generic part of any pair is this planar picture, with the angle theta replaced by an operator Theta on K, whose cosine is C and whose sine is S.

You have met an instance already. In the space of pairs of square-integrable functions on the interval from zero to one, with U the pairs whose second function is zero and V the pairs of the form cosine phi of t times h of t, sine phi of t times h of t, the whole space is generic, K is the first copy of the function space, and C is multiplication by cosine phi of t. Halmos's theorem says that every generic pair looks like that example, with a multiplication by cosine phi replaced by an arbitrary positive contraction C that kills no vector and fixes no vector.

Classifying pairs

The decomposition is the key to the classification. Suppose two pairs have elementary pieces of the same dimensions, and suppose their generic cosines C and C prime are unitarily equivalent: there is a unitary G from K onto K prime with G times C equal to C prime times G. Then build a unitary of the whole space piece by piece. On each elementary piece, use any unitary onto the corresponding piece of the other pair; equal dimensions are exactly what make this possible. On the generic part, use G on both copies of K. Since G intertwines C with C prime, it also intertwines S with S prime, because S is a function of C. So G applied to both copies carries the block matrices for P and Q to those for P prime and Q prime. The assembled unitary carries U onto U prime and V onto V prime.

Conversely, a unitary that carries one pair to the other must carry each elementary piece onto the corresponding piece, since those pieces are defined by intersections, and it must carry the generic compression to the generic compression. So the conditions are necessary as well.

This gives the classification theorem. Two pairs are equivalent if and only if their four elementary pieces have equal dimensions and their generic angle operators are unitarily equivalent.

What does unitary equivalence of self-adjoint operators mean in practice? In finite dimensions, two self-adjoint operators are unitarily equivalent exactly when they have the same eigenvalues with the same multiplicities. In general, the Hahn–Hellinger theorem gives the corresponding invariant: a spectral multiplicity function, which records, for each part of the spectrum, how many independent copies of it the operator contains. For example, multiplication by phi of t on square-integrable functions on the interval has spectrum from zero to sixty degrees with multiplicity one. The same multiplication acting on pairs of such functions has the same spectrum with multiplicity two, and the two operators are not unitarily equivalent.

The form in the Davis–Kahan paper

Davis and Kahan state the classification through their angle operators. Theta zero acts on U and Theta one acts on the complement of U. With the decomposition in hand, both are easy to describe.

U is made of three of the pieces: the common part, the source defect, and K. On the common part, Theta zero is zero; on the source defect it is ninety degrees; and on K it is the generic angle. The complement of U is made of the exterior part, the target defect, and L, the second copy of K. On the exterior part, Theta one is zero; on the target defect it is ninety degrees; and on L it is the same generic angle again. So Theta zero and Theta one share the generic part exactly. They can differ only in the multiplicity of the eigenvalue zero, which counts the common and exterior dimensions, and in the multiplicity of ninety degrees, which counts the two defect dimensions.

The paper works under standing dimension assumptions. U and V have the same dimension, their complements have the same dimension, and the two defects have the same dimension. These are the conditions under which some unitary carries U onto V and, as we will see, under which a direct rotation exists. Under these assumptions, Davis and Kahan's Theorem 3.1 states that the spectral multiplicity functions of Theta zero and Theta one form a complete invariant of the pair. Conversely, any two self-adjoint operators Theta zero and Theta one, with spectra between zero and ninety degrees, whose multiplicity functions agree everywhere except possibly at zero, and whose domains have dimensions adding up to the dimension of the whole space, arise as the angle operators of some pair. The proof of the converse is the construction we just did, run backwards: take the generic angle, build K plus K with Halmos's blocks, and attach elementary pieces of the required dimensions.

The phrase except possibly at zero has a precise meaning. Zero angles in Theta zero come from the common part, and zero angles in Theta one come from the exterior part, and these two dimensions are unrelated. If U and V are the same line in three-dimensional space, Theta zero is zero on a one-dimensional space, while Theta one is zero on the two-dimensional complement. Ninety degrees, on the other hand, must have equal multiplicity in the two operators, and that is exactly the standing assumption that the defects have equal dimension.

Equal dimensions do not force equal defects

In finite dimensions, the defect assumption is automatic. U is the sum of the common part, the source defect, and K. V is the sum of the common part, the target defect, and the generic part of V, which consists of the pairs C h, S h and therefore has the same dimension as K. If U and V have the same finite dimension, subtracting the common terms leaves the source defect and the target defect with the same dimension.

In infinite dimensions, subtraction fails, and so does the conclusion. Davis and Kahan give an example. Take square-summable sequences indexed by all the integers, positive, negative, and zero. Let U consist of the sequences that vanish at every negative index, and let V consist of the sequences that vanish at every index less than or equal to zero. Then V is contained in U, with one direction to spare: the sequence that is one at index zero and zero elsewhere lies in U and is perpendicular to V. So the source defect has dimension one. The target defect is zero, because V lies inside U and so no vector of V is perpendicular to U. The generic part is empty.

Yet U and V have the same dimension in the only sense that matters for unitaries. The shift, which moves every entry one place to the right, is a unitary map of the whole space, and it carries U exactly onto V, and the complement of U exactly onto the complement of V. So the first standing assumption holds and the defect assumption fails. Theorem 3.1 as stated does not cover this pair, and, as the paper shows, no direct rotation carries U onto V.

The compact case

There is one more simplification. Suppose the sine squared compression, P times the identity minus Q, times P, restricted to U, is a compact operator. Then Theta zero has a spectral decomposition by eigenvectors, just like a matrix, and Corollary 3.1 of the paper describes the invariants as lists. The eigenvalues of Theta zero can be any sequence starting at most at ninety degrees, decreasing, and converging to zero, possibly together with an eigenvalue zero of any multiplicity. Theta one has the same nonzero eigenvalues with the same multiplicities, and may differ only in the multiplicity of zero.

This is the infinite-dimensional version of a list of principal angles. In the example of infinitely many perpendicular planes with angles of one over n radians, the sine of the angle operator is compact, the list is one, one half, one third, and so on, and the classification is that list. In the interval example, the angle operator is multiplication by phi of t, its sine is not compact, and no list exists; the invariant is the multiplication operator itself, with spectrum from zero to sixty degrees and multiplicity one.

Where these results come from

Paul Halmos published the five-piece decomposition and the block form of the generic part in his 1969 paper titled Two Subspaces. Böttcher and Spitkovsky's survey of two-projection theory relates Halmos's representation to earlier formulations by Jacques Dixmier in 1948 and by Chandler Davis in 1958, and to the closely related projection constructions in the Davis–Kahan paper. Davis and Kahan's own classification, Theorem 3.1, is phrased through the angle operators of their Section 3, and their example with the shift shows why they impose the equal-defect assumption explicitly.

To summarize. Every pair of closed subspaces splits into five perpendicular pieces: the common part, the exterior part, the two defects, and the generic part. On the generic part, after identifying the two halves through the polar decomposition of the crossing map, the projections become the identity on the first copy and the block matrix with entries C squared, C S, C S, S squared, which is the planar two-line picture with an operator angle. Two pairs are equivalent exactly when the four elementary dimensions agree and the generic angle operators are unitarily equivalent, which in the paper's terms means the spectral multiplicity functions of Theta zero and Theta one agree. In finite dimensions, equal dimensions of U and V force equal defect dimensions; in infinite dimensions the shift example shows they need not.

The classification identifies a pair up to a unitary of the whole space, but it does not choose one. Many unitaries carry U onto V, even in the plane, where a rotation through theta and a reflection across the bisector both carry one line onto the other. Singling out a canonical choice requires a further principle, and that is the role of the direct rotation.

<!-- END SPOKEN LECTURE -->

---

## Companion: mathematics and Lean correspondence (display only)

### Halmos decomposition

For closed \(U,V\subseteq\mathcal E\) with projections \(P,Q\):
\[
\mathcal E=(U\cap V)\oplus(U\cap V^\perp)\oplus(U^\perp\cap V)\oplus(U^\perp\cap V^\perp)\oplus M,
\]
with \(D_0=U\cap V^\perp\), \(D_1=U^\perp\cap V\), and \(M\) the generic part. All five summands reduce \(P\) and \(Q\). On the summands, \(P-Q=0,\ +I,\ -I,\ 0\) respectively.

On \(M=K\oplus L\), \(K=U\cap M\), \(L=U^\perp\cap M\):

- \(C^2:=PQP|_K\), \(\ker C=\{0\}\), \(\ker(I-C^2)=\{0\}\), \(S:=(I-C^2)^{1/2}\).
- \(B:=(I-P)QP|_K:K\to L\), \(B^*B=PQP-(PQP)^2=C^2S^2\), \(|B|=CS\), \(B=W\,CS\) with \(W:K\to L\) unitary.
- In \(K\oplus K\) (via \(W\)):
\[
P\sim\begin{pmatrix}I&0\\0&0\end{pmatrix},\qquad
Q\sim\begin{pmatrix}C^2&CS\\CS&S^2\end{pmatrix}=\begin{pmatrix}C\\S\end{pmatrix}\begin{pmatrix}C&S\end{pmatrix}.
\]
- The \((2,2)\) block \(Z\) is forced by \(Q^2=Q\): \((CS)C^2+Z(CS)=CS\Rightarrow Z\,CS=CS\,S^2\), and \(CS\) has dense range, so \(Z=S^2\).

### Classification

\((U,V)\cong(U',V')\) (unitary \(G:\mathcal E\to\mathcal E'\), \(GU=U'\), \(GV=V'\)) iff the four elementary dimensions agree and \(C\cong C'\) (equivalently, equal spectral multiplicity functions, by Hahn–Hellinger).

Davis–Kahan form: \(\Theta_0=0_{U\cap V}\oplus\Theta_{\rm gen}\oplus\tfrac\pi2 I_{D_0}\), \(\Theta_1=0_{U^\perp\cap V^\perp}\oplus\Theta_{\rm gen}\oplus\tfrac\pi2 I_{D_1}\).

- **Theorem 3.1** (assuming \(\dim U=\dim V\), \(\dim U^\perp=\dim V^\perp\), \(\dim D_0=\dim D_1\)): the spectral multiplicity functions of \(\Theta_0,\Theta_1\) are a complete invariant; conversely any Hermitian \(0\le\Theta_j\le\pi/2\) whose multiplicity functions agree except possibly at \(0\), with domain dimensions summing to \(\dim\mathcal E\), are realized.
- **Corollary 3.1** (\(PQ^\perp P\) compact): invariants are the eigenvalues \(\pi/2\ge\theta_1\ge\theta_2\ge\dots\to0\) (plus a possible eigenvalue \(0\)); \(\Theta_1\) has the same nonzero eigenvalues.
- **Finite dimensions:** \(\dim U=\dim(U\cap V)+\dim D_0+\dim K\), \(\dim V=\dim(U\cap V)+\dim D_1+\dim K\), so \(\dim U=\dim V<\infty\Rightarrow\dim D_0=\dim D_1\).
- **Shift example** (source, after Proposition 3.2): \(\ell^2(\mathbb Z)\), \(U=\{a_n=0,\ n<0\}\), \(V=\{a_n=0,\ n\le0\}\). Then \(D_0=\operatorname{span}\{e_0\}\), \(D_1=\{0\}\), \(M=\{0\}\); the bilateral shift carries \(U\to V\), \(U^\perp\to V^\perp\).

### Lean correspondence

Davis–Kahan library, `DavisKahan/Geometry/Halmos/TwoProjections.lean`:

```lean
noncomputable abbrev halmosCommonPart (U V : Submodule 𝕜 H) : Submodule 𝕜 H := U ⊓ V
noncomputable abbrev halmosSourceDefect (U V : Submodule 𝕜 H) : Submodule 𝕜 H := U ⊓ Vᗮ
noncomputable abbrev halmosTargetDefect (U V : Submodule 𝕜 H) : Submodule 𝕜 H := Uᗮ ⊓ V
noncomputable abbrev halmosExteriorPart (U V : Submodule 𝕜 H) : Submodule 𝕜 H := Uᗮ ⊓ Vᗮ

noncomputable abbrev halmosTrivialPart (U V : Submodule 𝕜 H) : Submodule 𝕜 H :=
  (halmosCommonPart U V ⊔ halmosSourceDefect U V) ⊔
    (halmosTargetDefect U V ⊔ halmosExteriorPart U V)

noncomputable abbrev halmosGenericPart (U V : Submodule 𝕜 H) : Submodule 𝕜 H :=
  (halmosTrivialPart U V)ᗮ
```

`DavisKahan/Sources/DavisKahan1970/Section3Classification.lean`, `namespace TauCeti.DavisKahan1970` (complex Hilbert spaces `H₁ H₂`, `U₁ V₁ : Submodule ℂ H₁`, `U₂ V₂ : Submodule ℂ H₂` with orthogonal projections):

```lean
theorem theorem3_1_spectralMultiplicity_classification_complex
    [TopologicalSpace.SeparableSpace H₁] :
    PairOfSubspacesUnitaryEquivalent U₁ V₁ U₂ V₂ ↔
      SameHalmosTrivialDimensions U₁ V₁ U₂ V₂ ∧
      SameSpectralMultiplicity
        (genericCosineBlock U₁ V₁)
        (genericCosineBlock U₂ V₂)
```

**Mapping notes.**

- The formal statement is exactly the lecture's form: four elementary dimensions (`SameHalmosTrivialDimensions`) plus the spectral multiplicity of the generic cosine block on the `U`-side (`genericCosineBlock`). The module docstring explains why the `U`-side block is used instead of the doubled block on \(K\oplus K\).
- It wraps an operator-level classification (`twoProjection_operator_classification`) that needs no separability; separability enters only through the existence half of Hahn–Hellinger.
- A real version (`theorem3_1_spectralMultiplicity_classification_real`), the converse realization (`theorem3_1_realization` and variants), and Corollary 3.1 (`corollary3_1_compact_defectBlock_angleList_classification` in `Section3Corollary31.lean`) are listed in `dev/davis-kahan-1970-formalization-result-inventory.json` under `DK-3.1-thm` and `DK-3.1-cor`.
