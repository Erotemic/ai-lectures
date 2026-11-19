# Algebraic symmetry, weights, and geometric realization

<!-- BEGIN SPOKEN LECTURE -->

# Algebraic symmetry, weights, and geometric realization

## Algebraic Groups, Group Schemes, and Lie Algebras

A group is a set with multiplication, inverses, and an identity. An algebraic variety is described by polynomial equations. An algebraic group combines these structures: the group operations must themselves be algebraic. This sounds like adding extra conditions to a familiar group. In fact it changes the questions we can ask.

Consider the invertible matrices of size n. Their multiplication uses polynomial expressions in their entries, but inversion introduces division by the determinant. That is still algebraic on the locus where the determinant is invertible. We obtain a group with a geometric structure, called the general linear group.

Another example is the multiplicative group of nonzero scalars. As a variety it can be described by adjoining an inverse to a coordinate. The additive group is the affine line with addition. These are elementary, but they reveal a key principle: the group law is not something pasted onto the points after the geometry is finished. It is part of the geometry.

### Why points over one field are not enough

Imagine a group described by equations over the real numbers. We might list its real points. We could also look at its complex points, or its solutions over a ring containing infinitesimal elements. All of these are different windows onto the same algebraic structure.

A group scheme assigns a group of solutions to each test ring in a way compatible with ring homomorphisms. For the multiplicative group, the solutions over a ring R are its units. For the general linear group, the solutions are invertible matrices with entries in R. Using all rings rather than one field is important because it lets us detect infinitesimal directions and families.

The coordinate ring of an affine group scheme carries a dual algebraic description. Multiplication of group points corresponds to a comultiplication of functions. Identity gives a counit; inversion gives an antipode. These are the defining pieces of a Hopf algebra. The reversal is worth emphasizing: a geometric multiplication map goes in one direction, while pullback of coordinate functions goes in the other.

### Tangent vectors at the identity

Now consider matrices that differ infinitesimally from the identity. Work over dual numbers, where epsilon squared is zero. A matrix of the form identity plus epsilon times A is invertible, and multiplying two such matrices adds their first-order parts. Thus the tangent vectors at the identity form the full space of n by n matrices.

Where does the Lie bracket come from? Compare products in opposite orders, carefully tracking terms to second order in independent infinitesimals. The commutator is AB minus BA. This bracket makes the tangent space a Lie algebra. For the general linear group, the Lie algebra is precisely the matrix algebra equipped with the commutator bracket.

The Lie algebra is a local, first-order shadow of the group near its identity. It tells us about infinitesimal symmetries and provides a bridge to differential equations and representation theory. But it does not remember the whole global group. The circle and the additive real line have isomorphic one-dimensional real Lie algebras, yet very different global topology.

### What goes wrong in positive characteristic

Group schemes also distinguish phenomena invisible from an ordinary list of points. Let the field have characteristic p. Consider the solutions of x to the pth power equal to zero, with the additive group law. Over a field there is only one solution, zero. But over a ring containing nilpotent elements, more solutions appear. This group scheme is called alpha p.

Its coordinate ring is not reduced. Despite having a single rational point over the field, it has a nonzero tangent space at that point. So counting geometric points does not reveal its infinitesimal structure. In positive characteristic the distinction between smooth algebraic groups and non-smooth group schemes becomes essential.

This is also why moving between algebraic groups and Lie algebras requires care. Over characteristic zero, smooth connected groups and their Lie algebras are closely connected, but even then global questions remain. In characteristic p, Frobenius maps and infinitesimal subgroup schemes introduce behavior that cannot be reconstructed from the ordinary Lie algebra alone.

### Representations and geometry together

A representation of a group scheme on a finite module is a compatible algebraic action, not merely a homomorphism from a chosen set of field-valued points. Its infinitesimal action gives a Lie algebra representation under appropriate smoothness assumptions. Conversely, a representation of a Lie algebra does not automatically integrate to the desired algebraic group representation.

Group schemes let arithmetic and geometry share a vocabulary. The same general linear group can act on lattices, vector spaces, families of curves, or modules over rings. Tangent Lie algebras expose the local structure, while the full functor of points retains global and infinitesimal information. The lesson is that symmetry can be a geometric object, not only a collection of transformations.

## Tannakian Reconstruction: Recovering Symmetry from Representations

A group acts on a vector space through matrices. Usually we begin with the group and study its representations. But suppose someone erases the name and definition of the group, leaving us its entire collection of finite-dimensional representations. We can still see the linear maps between them. We know how to take direct sums, duals, and tensor products. We know which representation is the trivial one. Is the original symmetry recoverable from this information?

For a suitable class of algebraic groups, the answer is yes. Tannakian reconstruction makes that statement precise. It also explains why a category, together with its tensor operations, can carry enough information to describe an object that seems external to the category.

It is tempting to say that a group is just the collection of dimensions of its irreducible representations. That is false. Dimensions discard most of the relationships between representations. The tensor product carries more information: it tells us which representations appear when two symmetries act jointly. Morphisms, duals, and the symmetry of the tensor operation carry still more.

### An example we can reconstruct

Consider the multiplicative algebraic group: nonzero scalars acting by multiplication. Its finite-dimensional representations in characteristic zero decompose into weight spaces. On a weight-n line, a scalar t acts as t to the n. The weight-zero line is trivial. The dual of weight n has weight negative n. The tensor product of weight m and weight n has weight m plus n.

Imagine forgetting the scalars but remembering the weight lines and their tensor multiplication. A symmetry of the forgetful functor to vector spaces must act on each weight line by a scalar. If it acts by lambda on weight one, compatibility with tensor products forces it to act by lambda squared on weight two, by lambda cubed on weight three, and by the inverse of lambda on weight negative one. The entire action is determined by a single invertible scalar.

We have recovered the multiplicative group from the requirement that a family of linear transformations respect every tensor operation. This is the simplest tangible example of the reconstruction principle.

### The fiber functor is essential

Here is the formal setup, expressed carefully. We have a suitable rigid, abelian, symmetric tensor category over a field. Rigid means that objects have duals. A fiber functor sends its objects to finite-dimensional vector spaces, preserving the tensor product and the unit object. We require it to be faithful and exact: it must not identify distinct morphisms or destroy the short exact sequence structure.

Now consider all tensor-compatible natural automorphisms of that functor. To every commutative algebra over the base field, we can assign a group of such automorphisms after extending scalars. This assignment is represented, under the Tannakian hypotheses, by an affine group scheme. In other words, an algebraic symmetry object emerges from the category and the fiber functor.

The phrase group scheme matters. The recovered object need not be understood completely by listing its points over one field. It may carry infinitesimal structure, or possess fewer rational points than its geometry over larger fields suggests. The reconstruction is algebraic, not merely set-theoretic.

Without a specified fiber functor, the category can still contain substantial symmetry information, but reconstruction may produce a group over an extension or a more general gerbe. The chosen way of realizing abstract objects as vector spaces is part of the neutral reconstruction data. This is why the theorem is not simply that any tensor category secretly *is* a group.

### Why naturality constrains the answer

A natural transformation of the fiber functor provides a linear transformation on every representation. But those choices cannot be arbitrary. If a map between two representations commutes with the group action, our family of transformations must commute with that map as well. It must respect tensor products and the identity representation.

These constraints are strong enough to prevent fake symmetries. In the weight example, assigning independent scalars to weight one and weight two violates the tensor product law unless the second is the square of the first. The category's internal operations enforce the same relations that multiplication enforces in the original group.

This perspective is useful when the representations come first. In arithmetic geometry, we may study a category of vector bundles with connection, local systems, or motives and ask what symmetry object governs them. A Tannakian group can encode monodromy or other hidden symmetries of those objects.

The reconstruction does not make every such category easy to calculate. It tells us which data are sufficient to pose the question correctly and why tensor structure is indispensable. If the category is not abelian, if duals are missing, or if the proposed functor is not exact, the standard theorem may not apply.

### What counts as recovering the group?

A powerful feature of the theorem is that it is reversible. Starting with an affine group scheme, we form its finite-dimensional representation category with the ordinary forgetful functor. Reconstructing from that pair gives back the group scheme. Conversely, a neutral Tannakian category can be described as the representation category of its recovered affine group scheme.

The lesson is that symmetry is not only a set of transformations of one object. It is also the pattern of coherent transformations across *all* objects of a representation theory. Tensor products tell us how separate actions coexist; duals tell us how to reverse them; naturality tells us which choices are compatible. Recovering the group means recovering those constraints as a single algebraic object.

## Roots, Weights, and Representations of Reductive Groups

Think of rotations. The same rotation group can act on ordinary three-dimensional vectors, on matrices, on polynomials, and on complicated spaces of functions. These actions are not identical, but they carry a recognizable common structure. Representation theory studies exactly how a group can act linearly while preserving composition.

For compact or complex reductive groups, an enormous amount of representation theory can be organized using a surprisingly small amount of combinatorial data: roots, weights, and a distinguished region called a Weyl chamber. The clearest way to see the mechanism is through the two-by-two matrices of determinant one.

Our running example is the complex group SL two, whose Lie algebra consists of two-by-two matrices with trace zero. Its representations are small enough to calculate explicitly, yet already exhibit the essential logic of highest weights.

## Diagonal symmetries and weights

Start with diagonal matrices whose diagonal entries are z and its reciprocal. Such matrices form a maximal torus in SL two. On the natural two-dimensional vector space, the first coordinate is multiplied by z and the second by the reciprocal of z.

A weight is a label describing one of these one-dimensional scaling behaviors. In the natural representation, the two weights are plus one and minus one. On homogeneous polynomials of degree n in two variables, the monomial with k copies of the first variable and n minus k copies of the second has weight two k minus n.

So the degree-three polynomial representation has four weights: minus three, minus one, plus one, and plus three. Each occurs once. These weights are not an arbitrary mnemonic. They tell us exactly how the diagonal subgroup acts, and their pattern persists when we introduce the other elements of the Lie algebra.

## Raising and lowering operators

The Lie algebra of SL two has three standard generators. One is diagonal and measures weight. One turns a second-coordinate factor into a first-coordinate factor, raising the weight by two. The other performs the reverse operation, lowering the weight by two.

On homogeneous polynomials, the raising operator differentiates with respect to the second variable and multiplies by the first. The lowering operator differentiates with respect to the first and multiplies by the second. We can follow their action without knowing any classification theorem.

Take a pure power of the first variable, say x to the fourth power. Raising it gives zero, because no second-variable factor remains. Lowering it produces four times x cubed times y. Lowering again produces a multiple of x squared times y squared. Continue until we reach y to the fourth. The entire five-dimensional space is generated from the first pure power by repeated lowering.

This top vector has the highest weight. Its weight determines the rest of the representation, provided we are working with finite-dimensional representations in the appropriate characteristic-zero setting. That is the seed of the highest-weight classification.

## Why the roots control the motion

The root system describes how the Lie algebra changes weights. For SL two there is one positive root, with weight increment two. The raising and lowering operations move along the resulting weight string.

For larger groups there are several simple roots. Applying the corresponding root operators moves from a highest weight through a network of other weights. Not every arbitrary weight label can start a finite-dimensional irreducible representation. The highest weight must be dominant and integral relative to the root datum.

For SL two, dominance simply means that the highest weight is a nonnegative integer. For the group SL two itself, each such integer yields the symmetric power representation of that degree. For a related group such as PGL two, the permitted group-level highest weights differ because the central element acts trivially. The Lie algebras may be closely related while the representation categories of the groups are not literally the same.

## The Weyl group

There is one other symmetry in the picture. A matrix exchanging the two coordinate axes conjugates a diagonal matrix to one with reciprocal entries. This symmetry reverses the sign of weights. The Weyl group for SL two has two elements: the identity and this reflection.

In general the Weyl group is generated by reflections associated with roots. It relates different choices of positive directions in weight space. The Weyl chambers are regions cut out by root hyperplanes. Selecting a positive chamber lets us speak consistently about the highest weight.

An irreducible representation of highest weight three has weights three, one, minus one, and minus three. This list is symmetric because of the Weyl reflection. But the Weyl group alone does not determine multiplicities in every higher-rank representation. Those require more structure, such as the Weyl character formula or combinatorial models of the representation.

## Semisimplicity and its hypotheses

For a complex reductive algebraic group, finite-dimensional rational representations are completely reducible: they split into direct sums of irreducible representations. This means highest weights can classify the irreducible pieces from which other finite-dimensional representations are assembled.

The field matters. In positive characteristic, representations of reductive groups need not be completely reducible. The familiar argument that averages a projection over a finite group likewise needs the group order to be invertible in the field, or an appropriate substitute for averaging. One should never transfer a characteristic-zero classification statement without checking the setting.

## Why this classification matters

A highest weight is not merely a name for a representation. It predicts dimension, possible tensor-product constituents, and the behavior of invariant vectors. The simplest example already displays all three themes. Symmetric powers of a two-dimensional space have dimension n plus one; their weights form a chain; and tensor products can be decomposed by comparing how these chains combine.

This is a powerful general pattern: continuous symmetry becomes arithmetic data in a lattice. Roots specify allowed moves, a Weyl group specifies reflections, and dominant integral highest weights label the finite-dimensional irreducibles in the standard complex semisimple setting.

## Borel–Weil–Bott: Finding Representations in Line-Bundle Cohomology

Suppose we want to construct every finite-dimensional irreducible representation of a complex semisimple Lie group. Pure algebra says to classify highest weights, build a highest-weight vector, and act with lowering operators. Geometry offers another answer. Put a suitable line bundle on the space of all flags in a vector space, take the cohomology of that line bundle, and let the group act on the result.

For dominant weights, the space of global sections produces a representation. For non-dominant weights, the correct cohomology can appear in a higher degree. The Borel–Weil–Bott theorem organizes both phenomena and explains why the Weyl group enters the calculation with a shift by the vector called rho.

The smallest complete example is the projective line, which is also the flag variety for the group of two-by-two matrices of determinant one. Working this example gives us an entire table of representations and cohomology groups that can be checked without abstract machinery.

## The projective line carries the group action

The group SL two acts on the two-dimensional complex vector space. It therefore acts on the collection of one-dimensional subspaces, because multiplying a line by an invertible matrix gives another line. That collection is the projective line.

A line bundle over the projective line assigns a one-dimensional vector space to each point. The bundles named O of n, for integers n, are fundamental. For nonnegative n, a global section of O of n can be represented by a homogeneous polynomial of degree n in two variables. Substitute the transformed coordinates into the polynomial, and the group moves sections into sections. The space of homogeneous degree-n polynomials is exactly the symmetric-power representation, up to the standard choice of dual action.

Count monomials. Degree zero gives one constant. Degree one gives two linear forms. Degree two gives three quadratic monomials. In general the dimension is n plus one. In the highest-weight classification of SL two, that is the irreducible representation of highest weight n.

The geometry has manufactured a representation from functions that vary coherently over a space of lines. No basis-dependent matrix formula had to be guessed.

## Why negative degree changes the answer

There are no nonzero global holomorphic sections of a negative-degree line bundle on the projective line. A putative section would need poles to compensate for its negative twisting, but a global holomorphic section cannot acquire those poles. Thus for n less than zero, degree-zero cohomology vanishes.

That does not mean the bundle contains no representation-theoretic information. The first cohomology group measures the failure to glue local sections into one global section. For n equal to negative one, both the zeroth and first groups vanish. For n equal to negative two, the first cohomology has dimension one. For n equal to negative three, it has dimension two. In general, when n is at most negative two, the dimension of the first cohomology is minus n minus one.

This is precisely the representation that a reflected highest weight predicts. The two-dimensional representation returns at n equal to negative three, not in global sections but in first cohomology. The line bundle has changed degree, and the representation has moved to a different cohomological degree.

## A gluing calculation explains the jump

Cover the projective line with two copies of the affine line. Their overlap is the punctured affine line. A line bundle is trivial on each chart, but the two trivializations differ by a power of the overlap coordinate. A global section is a compatible pair of polynomials, one on each chart. First cohomology is the space of overlap data modulo differences of chartwise data.

If the twisting degree is minus two, one Laurent monomial survives this quotient. If it is minus three, two independent Laurent monomials survive. More negative twisting allows more of these gluing obstructions. That count gives the first-cohomology dimensions just stated.

Serre duality offers another check. The canonical bundle of the projective line is O of negative two. Consequently the first cohomology of O of negative n minus two is dual to the global sections of O of n for n nonnegative. A degree-n polynomial representation and its cohomological partner have the same dimension, as they must.

## From one reflection to a Weyl group

In a higher-rank reductive group the flag variety is the space of Borel subgroups, or equivalently the homogeneous space G modulo a Borel subgroup. Characters of the Borel define equivariant line bundles. Their cohomology groups inherit group actions.

The theorem starts with a weight lambda and adds rho, half the sum of positive roots. If lambda plus rho lies on a Weyl reflection hyperplane, every cohomology group vanishes. Otherwise one can reflect lambda plus rho into the dominant chamber using a unique Weyl-group element. Exactly one cohomology degree survives, and that degree is the length of the reflection element. Its nonzero group is an irreducible representation of the resulting dominant highest weight, with a dual convention depending on the line bundle definition.

Why the rho shift? Even for SL two, the shift explains the exceptional weight negative one, where everything vanishes. Reflection about negative one sends an integer n to negative n minus two. That is exactly the symmetry seen between the positive-degree global sections and the negative-degree first cohomology.

## What the theorem does and does not say

This calculation is powerful because it integrates topology, algebraic geometry, and representation theory. The same Weyl group that classifies chambers in root space dictates which cohomology degree appears. The Euler characteristic of a line bundle recovers the alternating character calculation underlying the Weyl character formula.

But not every vector bundle on an arbitrary variety has one nonzero cohomology group. This theorem is tied to homogeneous flag varieties, equivariant line bundles, and reductive symmetry, with an appropriate base field and hypotheses. For more complicated bundles, cohomology can occur in several degrees. In positive characteristic the characteristic-zero statement needs care.

On the projective line the entire pattern can be heard as one rule: positive twisting gives polynomial sections, twisting by negative one gives silence, and more negative twisting produces representations one degree higher. Borel–Weil–Bott recognizes the same pattern across all flag varieties by replacing the single reflection with an entire Weyl group.

## Weyl Characters, Root Symmetry, and Flag Varieties

Imagine a finite-dimensional vector space on which a semisimple Lie algebra acts. We might know the highest weight of this representation but still wish to know its dimension, and more specifically the multiplicity with which every weight occurs. A character packages that entire census into a formal expression. Each weight contributes a symbol, repeated according to the dimension of its weight space.

A character is more precise than the dimension. Two representations can have the same dimension while their weights, and therefore their actions under a maximal torus, are different. The Weyl character formula takes a dominant integral highest weight and produces exactly this richer information.

The startling aspect is its form. One builds an alternating sum indexed by reflections, divides by a universal alternating denominator, and receives a sum with nonnegative integer coefficients. The numerator looks like cancellation; the result is a list of actual representation dimensions. Explaining why cancellation yields something positive is part of the mathematical story.

## The two-dimensional model that contains the idea

Start with the Lie algebra of trace-zero two-by-two matrices. Its finite-dimensional irreducible representations are indexed by nonnegative integers m. The representation of highest weight m has weights m, m minus two, m minus four, and so on down to negative m. Each weight occurs once. Its dimension is m plus one.

Introduce a formal variable z. The character is the sum of z raised to each of those weights. For m equal to three, it is z cubed plus z plus z inverse plus z inverse cubed. That is the complete weight census.

Now multiply that sum by z minus z inverse. Nearly all terms cancel, leaving z to the power m plus one minus z to the negative power m plus one. Therefore the character can be written as that difference divided by z minus z inverse.

This is already the Weyl character formula in its simplest case. There is a reflection that exchanges a weight with its negative. The numerator antisymmetrizes the shifted highest weight. The denominator antisymmetrizes the fundamental shift. The quotient restores a symmetric character.

## Why weights are shifted before reflecting

For a general complex semisimple Lie algebra, choose positive roots. Their half-sum is called rho. The Weyl group is generated by reflections associated to roots. A dominant integral weight lambda specifies the irreducible highest-weight representation.

The numerator alternates the formal exponentials of all the reflected weights lambda plus rho. Each reflection contributes a plus or minus sign according to its parity. The denominator is the same alternating construction applied to rho alone.

Why introduce rho? Without that shift, the walls of the dominant Weyl chamber would spoil the clean cancellation. The rho shift aligns the combinatorics of positive roots with the weights produced by lowering operators. It makes the alternating numerator transform with exactly the sign needed to be divisible by the alternating denominator.

One must be careful about where the quotient lives. These are formal characters in the group ring of the weight lattice, or functions on a torus when evaluated appropriately. We are not dividing ordinary numbers at a point where the denominator happens to vanish. The quotient is a regular character that can be continued across those apparent singularities.

## From the character to a dimension

If we evaluate a character at the identity of the torus, every weight symbol becomes one. The result is the dimension of the representation. But substituting one directly into the Weyl quotient seems to give zero divided by zero.

There is a controlled way out. Approach the identity along a generic direction and cancel the vanishing factors. The result is the Weyl dimension formula, a product over positive roots of ratios involving lambda plus rho and rho.

For the Lie algebra of trace-zero three-by-three matrices, dominant weights are described by two nonnegative integers a and b. The resulting dimension is one half times a plus one, times b plus one, times a plus b plus two. The fundamental representation with a equal to one and b equal to zero has dimension three. The weight with a and b both equal to one has dimension eight, the dimension of the adjoint representation.

This is a concrete check on the product formula. It is also a warning that simply counting the number of Weyl-group elements cannot give the representation dimension. The highest weight still matters, and often changes the dimension dramatically.

## The flag variety explains the formula geometrically

There is a geometric side. A flag variety parametrizes nested subspaces, or more generally the cosets of a reductive group by a Borel subgroup. Its line bundles are indexed by weights. For dominant weights, the global holomorphic sections of an appropriately chosen line bundle carry the irreducible representation, possibly dualized according to convention.

This construction is known as Borel–Weil. Its cohomological extension, Borel–Weil–Bott, explains how non-dominant weights can produce representations in higher cohomology, and when all cohomology vanishes. The Weyl-group signs now have a geometric interpretation through alternating cohomology and the reordering needed to move a weight into the dominant chamber.

Thus a character formula is not merely a miraculous manipulation of exponentials. It is compatible with geometry on a space whose points are flags. The same root system controls the line bundles, the tangent directions, and the behavior of cohomology.

## Weyl cancellation is a calculation, not a dimension guess

There are important conditions. We are speaking about finite-dimensional representations of complex semisimple Lie algebras, or the corresponding compact-group setting. In positive characteristic, the category of representations changes and the same formulas do not classify arbitrary simple modules in the same way. For nonintegral highest weights, finite-dimensional irreducibles need not exist.

Also, a highest-weight module can exist even when it is infinite-dimensional. The Weyl character formula discussed here requires the finite-dimensional dominant-integral situation. One must distinguish that theorem from formal character formulas for Verma modules and other highest-weight categories.

The payoff is substantial. A single alternating expression recovers all weight multiplicities and specializes to dimensions. It simultaneously reflects the geometry of flag varieties and the combinatorics of root systems. What looks like cancellation in the formula is symmetry doing the work of counting.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Algebraic Groups, Group Schemes, and Lie Algebras

**Track:** Abstract Algebra. **Background:** affine schemes, functors of points, tangent spaces, representations. **Central question:** how can a group law be encoded algebraically so it works over fields, rings, and infinitesimal test objects?

#### Mathematical companion (not spoken)

The group schemes `G_a=Spec Z[t]`, `G_m=Spec Z[t,t^{-1}]`, and `GL_n=Spec Z[a_ij,1/det(a)]` represent the functors `R |-> (R,+)`, `R |-> R^x`, and `R |-> GL_n(R)`. For an affine group `G=Spec A`, the multiplication `m:GxG->G` induces the comultiplication `Delta=m^*:A->A tensor A`, with counit and antipode from identity and inversion.

For a field k and `R=k[epsilon]/(epsilon^2)`, the kernel of `GL_n(R)->GL_n(k)` comprises matrices `I+epsilon A`. As a vector space `Lie(GL_n)=M_n(k)`, with bracket `[A,B]=AB-BA`. For `E_12,E_21`, `[E_12,E_21]=E_11-E_22` (valid in all characteristics, with signs interpreted in k).

In characteristic `p>0`, `alpha_p=Spec k[t]/(t^p)` is an infinitesimal additive subgroup scheme; `alpha_p(k)={0}` when k is a field, but `Lie(alpha_p)` is one-dimensional. The group law is well-defined because `(a+b)^p=a^p+b^p` in characteristic p. The group scheme is not smooth over k. Group-point cardinality and tangent dimension are therefore distinct invariants.

##### Exercises with answers

1. What are `G_m(Z)` and `G_m(Q)`? **Answer:** `{1,-1}` and all nonzero rational numbers.
2. For `GL_2`, compute `[E_12,E_21]`. **Answer:** `E_11-E_22`.
3. Why is `alpha_p(k)` insufficient to recover its tangent space? **Answer:** field-valued points miss nonreduced infinitesimal directions; dual-number points detect them.
4. Does a Lie algebra determine global topology? **Answer:** no; the real circle and the additive real line have isomorphic one-dimensional Lie algebras.

##### Reading and source notes

- [Gabor Wiese, The Lie algebra of an algebraic group](https://math.uni.lu/wiese/talks/LieAlgebras.pdf), functor-of-points tangent constructions.
- [Milne, Algebraic Groups](https://www.jmilne.org/math/CourseNotes/iAG200.pdf), group schemes and representations.
- [Stacks Project, Group schemes](https://stacks.math.columbia.edu/tag/022R), definition and scheme-theoretic group operations.

### Tannakian Reconstruction: Recovering Symmetry from Representations

**Track:** Abstract Algebra. **Background:** representations, tensor products, symmetric monoidal categories, algebraic groups. **Central question:** if we know every representation and how representations combine, can we recover the group itself?

#### Mathematical companion (not spoken)

A neutral Tannakian category over a field `k` (classically `char(k)=0` for the simplest formulation) is a rigid abelian `k`-linear symmetric monoidal category `C` with `End(1)=k` and an exact faithful `k`-linear tensor functor `omega:C -> Vec_k^fd`. Its Tannaka group is the affine group scheme
\[
G=\operatorname{Aut}^{\otimes}(\omega), \qquad
G(R)=\operatorname{Aut}^{\otimes}(R\otimes_k\omega),
\]
with scalar-extension and naturality conditions understood. The reconstruction theorem identifies `(C,omega)` with `(Rep_k^fd(G), forget)` as tensor categories with fiber functor.

For `G_m`, weight representations `k(n)` satisfy `k(m) \otimes k(n) \cong k(m+n)`, `k(n)^\vee \cong k(-n)`. A monoidal automorphism is determined by its scalar `lambda in R^x` on `k(1)`; the action on `k(n)` is `lambda^n`. Hence `Aut^tensor(omega) = G_m` as a functor of algebras, not just by a pointwise count.

The theorem needs structural hypotheses. An arbitrary monoidal category with a functor to sets is not automatically Tannakian. The recovered group scheme can be nonreduced in positive characteristic, and the Tannakian formalism there requires attention to the precise formulation.

##### Exercises with answers

1. If a tensor automorphism acts by `lambda` on `k(1)`, how does it act on `k(-3)`? **Answer:** by `lambda^{-3}`.
2. Why can't we choose independent actions on `k(1)` and `k(2)`? **Answer:** their tensor relationship forces the second action to be the square of the first.
3. What does the fiber functor supply? **Answer:** a faithful exact tensor realization of abstract objects as finite-dimensional vector spaces.
4. Why reconstruct a group *scheme* rather than only its k-valued points? **Answer:** points over varying k-algebras can detect algebraic and infinitesimal structure invisible over k alone.

##### Reading and source notes

- [Deligne and Milne, Tannakian Categories](https://www.jmilne.org/math/xnotes/tc2022.pdf), reconstruction, fiber functors and affine group schemes.
- [Milne, Algebraic Groups](https://www.jmilne.org/math/CourseNotes/iAG200.pdf), algebraic group representations and group schemes.
- [The Stacks Project, Groupoid Schemes](https://stacks.math.columbia.edu/download/groupoids.pdf), group schemes and quotient structures.

### Roots, Weights, and Representations of Reductive Groups

**Track:** Abstract Algebra. **Background:** Lie algebras, matrix groups, group representations, and tensor products. **Central question:** how can the geometry of roots classify finite-dimensional representations of a semisimple Lie algebra?

#### Mathematical companion (not spoken)

Over C define
\[
H=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\quad
E=\begin{pmatrix}0&1\\0&0\end{pmatrix},\quad
F=\begin{pmatrix}0&0\\1&0\end{pmatrix}.
\]
Then `[H,E]=2E`, `[H,F]=-2F`, `[E,F]=H`. On `Sym^n(C^2)` realize
\[
H=x\partial_x-y\partial_y,\quad E=x\partial_y,\quad F=y\partial_x.
\]
The monomial `x^k y^(n-k)` has weight `2k-n`. In particular `x^n` is highest weight n and `F(x^n)=n x^(n-1)y`. The representation has character
\[
\chi_n(z)=z^n+z^{n-2}+\cdots+z^{-n},\quad \dim \operatorname{Sym}^n(C^2)=n+1.
\]
The Weyl group of SL_2 has order two and sends `z -> z^{-1}`. The dominant integral weights are n >= 0. For the algebraic group PGL_2 the allowable character lattice is smaller: only even weights of SL_2 descend, as `-I` acts on `Sym^n` by `(-1)^n`. The highest-weight classification for finite-dimensional rational representations of complex reductive groups uses the group-specific weight lattice and dominance; characteristic-p analogues require different semisimplicity statements.

##### Exercises with answers

1. List the weights of `Sym^4(C^2)`. **Answer:** `4,2,0,-2,-4`, each with multiplicity one.
2. Evaluate `E(x^2 y^2)`. **Answer:** `2 x^3 y`.
3. Why does `Sym^3(C^2)` not descend to PGL_2? **Answer:** its central element `-I` acts as minus identity rather than identity.
4. What is the dimension of the SL_2 irreducible of highest weight 7? **Answer:** eight.

##### Reading and source notes

- [MIT OCW 18.755 Lie Groups and Lie Algebras II](https://ocw.mit.edu/courses/18-755-lie-groups-and-lie-algebras-ii-spring-2024/pages/calendar/), weights, root systems and finite-dimensional representation theory.
- [MIT OCW 18.757 Representations of Lie Groups](https://ocw.mit.edu/courses/18-757-representations-of-lie-groups-fall-2023/pages/syllabus/), reductive groups and representation-theoretic background.
- [Pavel Etingof and collaborators, Introduction to Representation Theory](https://ocw.mit.edu/courses/18-712-introduction-to-representation-theory-fall-2010/pages/lecture-notes/), representations, complete reducibility and character methods.

### Borel–Weil–Bott: Finding Representations in Line-Bundle Cohomology

**Track:** Abstract Algebra. **Background:** representations of reductive groups, algebraic line bundles, projective spaces, and sheaf cohomology. **Central question:** why does a geometric space of flags encode highest-weight representations?

#### Mathematical companion (not spoken)

For `G=SL_2(C)` and `G/B=P^1`, standard line bundles satisfy
\[
H^0(\mathbf P^1,\mathcal O(n))\cong\begin{cases}\operatorname{Sym}^n(\mathbb C^2)^*&n\ge0,\\0&n<0,\end{cases}\quad
H^1(\mathbf P^1,\mathcal O(n))\cong\begin{cases}0&n\ge-1,\\ H^0(\mathbf P^1,\mathcal O(-n-2))^*&n\le-2.\end{cases}
\]
Here duals depend on the convention for the SL2 linearization, and SL2 irreducibles are self-dual. The second identity is Serre duality with `K_{P1}=O(-2)`.

For a connected, simply connected, complex semisimple G, a weight lambda and its equivariant line bundle `L_lambda` on `G/B`, the Borel–Weil–Bott statement (with compatible sign convention) is: if `lambda+rho` is singular, all `H^i` vanish; if regular, the unique w taking `lambda+rho` to the dominant chamber yields one nonzero cohomology group in degree `ell(w)`, of highest weight `w(lambda+rho)-rho`. This is the dot action `w·lambda=w(lambda+rho)-rho`.

**Čech count:** on affine charts U0 and U∞, gluing is by a monomial of degree n. The quotient of Laurent polynomials on their overlap by extendible chartwise sections has basis represented by `z^{-1},...,z^{-m+1}` for `n=-m` and `m>=2`; its dimension is `m-1`. Equivalent powers depend on the chosen trivialization.

##### Exercises with answers

1. Give dimensions of `H0(O(4))` and `H1(O(-5))`. **Answer:** five and four, respectively.
2. Why is n=-1 exceptional? **Answer:** it is the singular shifted weight; both cohomology groups vanish.
3. What is the highest weight associated to `H1(O(-4))` for SL2? **Answer:** two, with a three-dimensional irreducible representation.
4. If lambda+rho lies on a reflection wall, does a different cohomology degree necessarily rescue it? **Answer:** no; all cohomology vanishes in the characteristic-zero theorem.

##### Reading and source notes

- [Serganova, Lectures in Lie Groups and Quantum Groups, Borel–Weil–Bott](https://math.berkeley.edu/~serganov/261/part1.pdf), general theorem and SL2 calculations.
- [University of Michigan seminar, Borel–Weil–Bott for SL2](https://websites.umich.edu/~charchan/seminar/20210927.pdf), projective-line model.
- [Stacks Project, Cohomology of Schemes](https://stacks.math.columbia.edu/download/cohomology.pdf), sheaf cohomology and base-change context.

### Weyl Characters, Root Symmetry, and Flag Varieties

**Track:** Abstract Algebra. **Background:** roots and weights of semisimple Lie algebras, representations, and Borel–Weil–Bott. **Central question:** how can an alternating sum over reflections encode every weight of an irreducible representation?

#### Mathematical companion (not spoken)

For a complex semisimple Lie algebra with weight lattice P, chosen positive roots `R_+`, half sum `rho=(1/2)sum_{alpha in R_+}alpha`, Weyl group W and dominant integral lambda, let `A_mu=sum_{w in W}det(w)e^{w(mu)}`. The Weyl character formula is
\[
\mathrm{ch}(V_\lambda)=\frac{A_{\lambda+\rho}}{A_\rho}
=\frac{\sum_{w\in W}\det(w)e^{w(\lambda+\rho)}}{e^\rho\prod_{\alpha\in R_+}(1-e^{-\alpha})}.
\]
The Weyl dimension formula is
\[
\dim V_\lambda=\prod_{\alpha\in R_+}\frac{\langle\lambda+\rho,\alpha^\vee\rangle}{\langle\rho,\alpha^\vee\rangle}.
\]
For `sl_2`, with weight coordinate m, `chi_m(z)=(z^{m+1}-z^{-(m+1)})/(z-z^{-1})=sum_{j=0}^m z^{m-2j}`. For `sl_3`, write `lambda=a omega_1+b omega_2`; the dimension is `(a+1)(b+1)(a+b+2)/2`.

**Borel–Weil convention:** for a dominant weight lambda and an appropriately signed line bundle `L_lambda` on `G/B`, `H^0(G/B,L_lambda)` is `V_lambda` or `V_lambda^*` depending on which action and line-bundle convention is used. Do not suppress this convention in a precise geometric statement.

##### Exercises with answers

1. Expand the sl2 character for highest weight four. **Answer:** `z^4+z^2+1+z^-2+z^-4`, dimension five.
2. Evaluate the sl3 dimension at (a,b)=(2,1). **Answer:** `(3*2*5)/2=15`.
3. Why is evaluation of the Weyl quotient at the identity not naive division by two numbers? **Answer:** numerator and denominator both vanish; the quotient is a regular character and its limit gives the dimension formula.
4. Does a nonintegral highest weight necessarily define a finite-dimensional irreducible? **Answer:** no, the dominant-integral condition is essential here.

##### Reading and source notes

- [MIT 18.755: Lie Groups and Lie Algebras II, Weyl character formula](https://ocw.mit.edu/courses/18-755-lie-groups-and-lie-algebras-ii-spring-2024/mit18_755_s24_lec_full.pdf), formal alternating sums and the character theorem.
- [MIT 18.745: Introduction to Lie Algebras, Lecture 25](https://math.mit.edu/classes/18.745/Notes/Lecture_25_Notes.pdf), character-to-dimension derivation and examples.
- [Wolfram MathWorld: Weyl Character Formula](https://mathworld.wolfram.com/WeylCharacterFormula.html), compact statement and references.
