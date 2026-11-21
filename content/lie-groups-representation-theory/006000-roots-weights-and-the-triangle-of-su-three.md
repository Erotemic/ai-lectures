# 006000 — Roots, Weights, and the Triangle of SU(3)

**Track:** Lie Groups, Lie Algebras, and Representations. **Preparation:** matrix commutators, the sl-two ladder, basic tensor and exterior products. **Theme:** higher-rank Lie algebras organize representations by a lattice of weights and a finite root system.

<!-- BEGIN SPOKEN LECTURE -->

# Roots, Weights, and the Triangle of SU(3)

A single ladder of weights is easy to visualize. You start at a highest point, move downward in steps of two, and eventually stop. That is the world of sl two, the simplest nonabelian complex semisimple Lie algebra. What happens when there are two independent directions in which a weight can change?

The first genuinely new example is sl three: all complex three-by-three matrices of trace zero, with commutator bracket. Its compact relative is SU three, the special unitary three-by-three matrices. As with SU two, the complexification of the compact Lie algebra gives the complex traceless-matrix algebra. The difference is that the natural diagonal subalgebra is now two-dimensional. Instead of placing weights on a line, we can place them in a plane.

A triangle emerges. From that triangle grow the root system, the Weyl group, and the highest-weight classification for a much wider family of Lie algebras.

## Diagonal matrices as measuring instruments

Consider all diagonal traceless complex three-by-three matrices. Such a matrix has diagonal entries h one, h two, h three, constrained so their sum is zero. So only two numbers are independent. This diagonal subalgebra is commonly called a Cartan subalgebra; in this example it is an abelian Lie algebra of dimension two.

For a representation, we look for vectors that are simultaneous eigenvectors of all these diagonal operators. A weight tells us how each diagonal operator scales such a vector. Since the diagonal algebra has dimension two, a weight is a linear functional on a two-dimensional space. After choosing coordinates, we can draw weights as points in a plane.

The standard three-dimensional representation is our first example. On the basis vectors e one, e two, e three, a diagonal matrix acts by multiplying each vector by its corresponding diagonal entry. Their weights are therefore the three coordinate functions: read h one, read h two, and read h three. Because h one plus h two plus h three equals zero, these three linear functionals sum to zero when restricted to the Cartan subalgebra.

Draw their points in the trace-zero plane, with a symmetric choice of scale. They lie at the vertices of an equilateral triangle centered at the origin. This is already more interesting than the straight line of SU two weights. But the basic mechanisms remain the same: diagonal operators measure weights, while off-diagonal operators move us between weight spaces.

## Six roots from six off-diagonal matrices

Let E i j be the three-by-three matrix that sends basis vector e j to e i and kills the other basis vectors. For distinct i and j it has a single one outside the diagonal. These six matrices are part of a basis for sl three, together with two independent diagonal traceless matrices.

Take a diagonal matrix H and compute its commutator with E i j. Multiplying H on the left scales row i by h i; multiplying on the right scales column j by h j. Their difference is h i minus h j times E i j.

Therefore each E i j is an eigenvector for the adjoint action of the diagonal algebra. Its eigenvalue is the linear functional that takes H to h i minus h j. Such a nonzero weight of the adjoint representation is called a **root**.

There are six roots, one for each ordered pair of different indices: h one minus h two, h two minus h one, h two minus h three, h three minus h two, and the two differences involving one and three. They form a hexagon when drawn in the two-dimensional root plane.

Choose two roots as simple positive roots: alpha one is h one minus h two, and alpha two is h two minus h three. A third positive root is their sum, h one minus h three. The negative roots point in the opposite directions. All six can therefore be described using just two simple roots and their addition.

This is the root system called A two. The root system of sl two was A one, merely two opposite points on a line. We have moved from one-dimensional to two-dimensional root geometry.

## Roots are not arbitrary weights

A weight belongs to a particular representation. The three weights of the standard representation describe how diagonal matrices act on the three basis vectors. A root is a special weight: one belonging to the adjoint representation of the Lie algebra on itself.

Why care about the distinction? Because the roots govern how the Lie algebra moves weights in *every* representation. If a vector has weight mu and a root operator E alpha acts nontrivially on it, the result has weight mu plus alpha. This is the same calculation we performed for the raising operator of sl two, now in two dimensions.

The root operator E one two moves weight from the second coordinate direction to the first. E two three moves from the third to the second. Their commutator is E one three, which moves directly from the third to the first. Algebraically, the bracket of E one two and E two three equals E one three. Geometrically, the associated roots add: alpha one plus alpha two is the third positive root.

This relation gives a satisfying reason to draw roots as vectors and add them. The geometry encodes a multiplication law between operators, not merely an arrangement of decorative dots.

## A finite symmetry of the root picture

The Weyl group of sl three acts by permuting the three diagonal coordinates. Each permutation sends roots to roots. Geometrically, these permutations act as symmetries of the hexagonal root arrangement, and the Weyl group is isomorphic to the symmetric group on three letters.

We can generate it by two reflections, each interchanging adjacent coordinates. The first swaps the first and second, corresponding to the simple root alpha one. The second swaps the second and third, corresponding to alpha two. Composing them generates all six permutations.

This is a subtle compression. A continuous Lie group with infinitely many elements gives rise to a finite reflection group acting on a much smaller vector space. The Weyl group captures part of the residual symmetry after we choose a diagonal Cartan subalgebra. It organizes the weights and allows many representation formulas to be expressed in a finite combinatorial language.

At this point the mathematics links back to discrete geometry. Root systems and Weyl groups are studied using reflections, chambers, lattices, and Coxeter relations. Lie theory is therefore not isolated from combinatorics; it creates a particularly rich family of combinatorial objects from continuous symmetry.

## Highest weights in two directions

For sl two, a highest-weight vector was annihilated by the raising operator E. For sl three, choose the upper-triangular off-diagonal matrices as raising operators. A highest-weight vector is killed by all of them. Its weight lies in a certain cone of the weight plane, called the dominant chamber, if we are describing a finite-dimensional irreducible representation.

Two fundamental dominant weights serve as building blocks. In coordinates on the trace-zero plane, they can be written as one third of the vectors two, negative one, negative one; and one third of one, one, negative two. Call them omega one and omega two. These are not roots; they are weights that pair with the simple coroots in the most elementary possible way.

Every dominant integral highest weight is p times omega one plus q times omega two, where p and q are nonnegative integers. For each such pair there is, up to equivalence, a unique finite-dimensional irreducible complex representation of sl three, equivalently a corresponding representation of the simply connected compact group SU three. So an infinite family of representations is organized by points on a two-dimensional integer lattice in a cone.

The dimension of the representation with highest-weight coordinates p and q is one half times p plus one, times q plus one, times p plus q plus two. This is the A-two instance of the Weyl dimension formula. We will not derive the general formula from scratch here. But we can test it against constructions we can see: p equals one and q equals zero gives dimension three; p equals zero and q equals one also gives dimension three; p and q both zero gives the one-dimensional trivial representation; p equals two and q equals zero gives dimension six.

The first three-dimensional representation is the defining action on complex triples. The other is its dual, which can be realized as the exterior square of the defining representation because determinant-one matrices preserve volume. This is a useful reminder that equal dimension does not imply equivalent representation. The two fundamental representations have different highest weights, even though both have dimension three.

## A tensor product that contains its own explanation

Take the defining three-dimensional representation V and tensor it with itself. Its dimension is nine. Every tensor can be separated into a symmetric part and an antisymmetric part, so the tensor square splits into the symmetric square and the exterior square. The symmetric square has dimension six; the exterior square has dimension three.

Both subspaces are preserved by SU three, because applying the same transformation to both tensor factors commutes with swapping those factors. The six-dimensional symmetric square is irreducible, with highest weight two omega one. The three-dimensional exterior square is the other fundamental representation, with highest weight omega two. Thus three tensor three decomposes as six plus three-dual.

You can verify the weights of the symmetric square directly. The underlying basis vectors have weights read h one, h two, and h three. Tensoring adds weights. The symmetric basis contains e one tensor e one, e two tensor e two, e three tensor e three, and one symmetric combination for each distinct pair of indices. That gives six weight vectors, exactly the dimension predicted by the formula.

In the exterior square, the three basis elements are e one wedge e two, e one wedge e three, and e two wedge e three. Their weights are the pairwise sums of coordinate weights. Since the three coordinate weights sum to zero, each pairwise sum is the negative of the omitted coordinate weight. That explains why the exterior square is dual to the defining representation, without demanding a long matrix computation.

This construction bridges representation theory and multilinear algebra. Tensor and exterior products are not arbitrary ways to enlarge vector spaces; they carry natural group actions, and their invariant decompositions expose new irreducibles.

## What is gained, and what we have not proved

The sl-three example shows why roots, weights, and the Weyl group are worth learning. From one concrete class of traceless matrices, we found two diagonal measurements, six root operators, a finite reflection group, a lattice of dominant highest weights, and exact dimension formulas for irreducible representations.

There are deeper results behind that summary. A general classification of semisimple Lie algebras requires understanding possible root systems and their Dynkin diagrams. The highest-weight classification requires careful proof that dominant integral weights both construct representations and enumerate them without duplication. The Weyl character formula refines dimension counting into a character identity. Those are substantial theorems, not facts we have silently established by drawing a hexagon.

We have established the concrete calculations that motivate the general theory: the diagonal commutator formula, the root additions, the Weyl permutations, and the tensor-square decomposition. For the full classification and dimension formula we are using stated theorems, with sources and hypotheses identified in the companion notes. That boundary is useful. It lets us recognize what a later rigorous course needs to prove while understanding why its definitions are arranged the way they are.

## The perspective across the whole course

A Lie group starts as a smooth family of transformations. Differentiating at the identity produces a Lie algebra. Its bracket records the failure of infinitesimal movements to commute. A group action can turn a space into a homogeneous space. A representation turns each group element into a linear operator, and in compact settings those operators can be organized into irreducible components.

For SU two, that organization is a ladder. For SU three, it is a lattice picture in a plane. In both cases, the highest-weight idea describes representations through a finite amount of data, while the group itself contains continuously many transformations.

The course has therefore led from a rotating disk to a geometric pattern of roots and weights. The bridge is not merely vocabulary. Every step is a way of replacing an unwieldy family of transformations with a smaller, structured mathematical object that can be computed with, reasoned about, and eventually formalized. That is the central utility of Lie theory: making continuous symmetry algebraically legible.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For \(\mathfrak{sl}_3(\mathbb C)\), let \(\mathfrak h=\{\operatorname{diag}(h_1,h_2,h_3):h_1+h_2+h_3=0\}\). If \(E_{ij}\) is the standard matrix unit, then
\[
[H,E_{ij}]=(h_i-h_j)E_{ij},\quad
[E_{12},E_{23}]=E_{13}.
\]
The root system is \(\Phi=\{\varepsilon_i-\varepsilon_j:i\ne j\}\), with simple roots \(\alpha_1=\varepsilon_1-\varepsilon_2\), \(\alpha_2=\varepsilon_2-\varepsilon_3\) and positive roots \(\alpha_1,\alpha_2,\alpha_1+\alpha_2\). The Weyl group \(W\cong S_3\) acts on diagonal coordinates by permutations.

In the trace-zero plane one may take
\[
\omega_1=\tfrac13(2,-1,-1),\qquad
\omega_2=\tfrac13(1,1,-2).
\]
Highest weights \(p\omega_1+q\omega_2\), \(p,q\in\mathbb Z_{\ge0}\), classify finite-dimensional complex irreducible \(\mathfrak{sl}_3\)-modules (and representations of simply connected \(SU(3)\)); the Weyl dimension formula specializes to
\[
\dim V_{p,q}=\frac{(p+1)(q+1)(p+q+2)}2.
\]
For \(V=\mathbb C^3\), \(V\otimes V=\operatorname{Sym}^2 V\oplus\wedge^2 V\), with dimensions \(6+3\); for \(SL_3\), \(\wedge^2 V\cong V^*\) via the invariant volume form.

**Exercises and solutions.** (1) Compute \([E_{23},E_{12}]\). *\(-E_{13}\).* (2) How many roots are in \(\mathfrak{sl}_3\)? *Six.* (3) Use the dimension formula at \((p,q)=(1,1)\). *Eight, the dimension of the adjoint representation.* (4) Explain why the weight of \(e_1\wedge e_2\) equals the negative of the weight of \(e_3\). *The three coordinate weights sum to zero on traceless diagonal matrices.* (5) Does this lecture prove the general Weyl dimension formula? *No; it states that theorem and verifies low-dimensional instances while proving the concrete root and tensor calculations.*

### Sources and further reading

- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations*, 2nd ed., chapters on \(\mathfrak{sl}_3\), roots and finite-dimensional modules: https://doi.org/10.1007/978-3-319-13467-3
- MIT OCW 18.745 (2020), lectures 19–26 on semisimple Lie algebras, roots, Weyl groups, and highest weights: https://ocw.mit.edu/courses/18-745-lie-groups-and-lie-algebras-i-fall-2020/resources/lecture-notes/
- Pavel Etingof et al., *Introduction to Representation Theory* (author-hosted MIT notes): https://math.mit.edu/~etingof/replect.pdf
- Related courses: `abstract-algebra:013000` for finite-group representations and `topology-geometry:008000` for tangent and flow foundations.
