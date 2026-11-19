# Tensor multiplicities, crystal combinatorics, and Hecke theory

<!-- BEGIN SPOKEN LECTURE -->

# Tensor multiplicities, crystal combinatorics, and Hecke theory

## Littlewood-Richardson Rules: Counting Tensor-Product Multiplicities

Take two representations of a group and form their tensor product. The new vector space has dimension equal to the product of the old dimensions. But the resulting representation usually decomposes into several irreducible pieces, sometimes with repetitions. Dimension tells us how many vectors we have, not how those vectors transform.

For the general linear group over the complex numbers, polynomial irreducible representations are indexed by partitions. A partition is a weakly decreasing list of nonnegative integers; it is often drawn as a diagram of boxes. This combinatorial encoding is not accidental decoration. The partitions label highest weights, and the characters of the representations are Schur polynomials. A product of Schur polynomials is therefore a decomposition of a tensor product.

The Littlewood-Richardson rule answers the central question. Given two partitions, which third partitions appear in their product, and with what multiplicity? The answer is the number of certain fillings of a skew diagram that obey two families of constraints. We will first understand a small representation-theoretic example and then see how the counting rule reproduces it.

## The simplest example: symmetric and alternating tensors

Let V be a complex vector space of dimension at least two. The tensor square of V splits into symmetric tensors and alternating tensors. Swapping the two factors acts with eigenvalue plus one on the symmetric part and minus one on the alternating part. Every simple tensor has a symmetric and antisymmetric decomposition, so the whole tensor product is the direct sum.

In partition notation, V is labelled by the one-box partition. Its tensor square decomposes into the two-box horizontal partition and the two-box vertical partition. In Schur-polynomial notation, multiplying the one-box Schur function by itself gives the sum of the two corresponding Schur functions.

This is a first glimpse of the Littlewood-Richardson rule. There are two possible Young-diagram shapes after adding one box to a one-box shape: a row of length two or a column of height two. Each is counted once. The multiplicities are not guessed from dimensions; they are encoded by permitted box additions.

If V has dimension three, the symmetric square has dimension six and the alternating square has dimension three. Their sum is nine, the dimension of the tensor square. This is a helpful consistency check but not a proof of the decomposition for arbitrary group actions. The representation structure is supplied by the symmetry under swapping factors.

## Partitions and skew shapes

A partition such as three, one is a first row of three boxes and a second row of one box. If another partition fits inside it, we may remove the smaller diagram and obtain a skew shape. A skew diagram is not necessarily left-justified; it remembers which boxes were removed.

The Littlewood-Richardson rule uses skew diagrams whose large shape is the proposed output representation and whose removed shape is one input. We fill the remaining boxes using positive integers. The content tells us how many ones, how many twos, and so on, according to the other input partition.

The filling must be semistandard: numbers weakly increase along each row and strictly increase down each column. There is one more condition. Read the entries row by row from right to left, starting at the top. At every initial segment of that reading word, the number of ones must be at least the number of twos; the number of twos at least the number of threes; and so forth. This is called the lattice-word or ballot condition.

The number of fillings satisfying all these conditions is the corresponding Littlewood-Richardson coefficient. The rule is not merely a formula for dimension; it is a positive counting formula for every multiplicity. No alternating signs survive in the final answer.

## A three-term product

Now tensor the representation indexed by the partition two, one with the defining three-dimensional representation V. The rule for multiplying by a one-box partition is particularly simple: add a single box while keeping a valid partition.

Starting from the diagram two, one, we can add a box to the end of the first row, giving three, one. We can add to the second row, giving two, two. Or we can create a third row, giving two, one, one. Each option appears once. For the group of invertible three-by-three matrices, all three diagrams are allowed.

Let us check the dimensions. The original representation two, one has dimension eight in dimension three. Tensoring with V gives dimension twenty-four. The output diagrams three, one; two, two; and two, one, one have dimensions fifteen, six, and three, respectively. Fifteen plus six plus three is twenty-four.

This check is valuable because it catches forgotten shapes. But if two different fillings produce the same output partition, its multiplicity can exceed one. Such repetitions are a genuine feature of tensor products, and they are exactly why a counting rule is more informative than a rule that only lists possible shapes.

## Why the ballot condition matters

A semistandard filling can have the right content and still fail to describe a highest-weight contribution. The ballot condition imposes a directional balance: as we scan the word, we never see more twos than ones before enough ones have appeared, and the analogous condition holds at each higher value.

There is a representation-theoretic reason. Highest-weight vectors are killed by certain raising operators. In a combinatorial model, those raising conditions become restrictions on the reading word. The ballot criterion packages these restrictions into a test that uses only integers and boxes.

Different textbook conventions sometimes read the skew tableau in a different order and modify the ballot rule accordingly. Those conventions are equivalent when used consistently. Mixing the reading rule from one convention with the tableau shape convention from another is an easy way to get a wrong coefficient.

## The boundary imposed by the number of variables

A Schur polynomial in n variables vanishes when its partition has more than n nonzero parts. Accordingly, when describing polynomial representations of the general linear group of an n-dimensional space, we must discard partitions with too many rows. An abstract identity in the ring of symmetric functions may display shapes that are simply absent for a small chosen n.

This explains why the same universal Littlewood-Richardson coefficients describe tensor products of general linear groups in all sufficiently large dimensions, while smaller dimensions require a row-length restriction. The multiplicities stabilize once the ambient dimension has enough rows for the partitions involved.

## Why a counting rule is a structural theorem

There are several ways to prove the Littlewood-Richardson rule: geometric intersections of Schubert varieties, representation-theoretic constructions, and combinatorial correspondences. These approaches illuminate different aspects of the same coefficients. In geometry they are structure constants for intersections. In representation theory they are tensor-product multiplicities. In symmetric-function theory they are coefficients in a distinguished positive basis.

The concrete lesson is that tensor products do not have to be opaque. For representations of general linear groups, a continuous symmetry problem is converted into counting discrete objects. The boxes are not a toy model of the representation. They are a precise coordinate system for its highest-weight structure, and their permitted fillings encode how representations combine.

## Crystal Bases and Canonical Bases

A representation is a vector space carrying operators that obey algebraic relations. In a basis, those operators become matrices. But a large matrix can obscure the basic question: which weights can be reached from which other weights, and how are those connections assembled under tensor products?

Crystal bases were introduced to expose this combinatorial skeleton. They arise from representations of quantum groups, in which a parameter usually called q deforms the enveloping algebra of a semisimple Lie algebra. In an appropriate integral lattice, a carefully normalized basis survives at q equal to zero. The result is not an ordinary vector-space representation at that value. It is a finite or locally finite directed, colored graph, with edges generated by raising and lowering operators.

The remarkable point is that the graph retains enough information to recover weight multiplicities and to organize tensor-product decompositions. Canonical or global bases go further. They lift this combinatorial framework back to distinguished vectors of the quantum representation, with additional normalization, integrality, and positivity properties in settings where those results hold.

## The simplest highest-weight chain

Start with the two-dimensional defining representation of sl two. It has a highest-weight vector, often called plus, and a lowest-weight vector, called minus. The lowering operator moves from plus to minus; applied again it gives zero. The raising operator reverses the edge.

The crystal graph is just a chain of two vertices. One vertex has weight plus one, the other weight minus one, and a single lowering edge connects them. No matrix coefficients are needed to read the weights or the allowed lowering move.

For the irreducible representation of highest weight two, the crystal is a chain of three vertices with weights two, zero, and minus two. More generally, the irreducible representation of highest weight n for sl two has n plus one vertices. The weights descend in steps of two, and a lowering edge joins each successive pair.

This picture is deceptively simple, but it already captures the decomposition rules for tensor products. The challenge is defining how the lowering operation acts on a tensor of crystal elements. It cannot simply act on both factors indiscriminately; a comparison of the factors' available raising and lowering steps determines which factor changes.

## Four tensor states become two components

Take two copies of the two-vertex crystal. Their cartesian product contains four formal tensor states: plus with plus, plus with minus, minus with plus, and minus with minus. Under the crystal tensor-product rule, these four states do not form one irreducible chain.

Three form the highest-weight-two chain. The remaining state is an isolated vertex of weight zero. That is exactly the combinatorial form of the familiar representation identity: two copies of the two-dimensional representation tensor together to give the three-dimensional symmetric representation and a one-dimensional trivial representation.

The distinction between the two weight-zero tensor states matters. Counting weights alone tells us that weight zero has multiplicity two, but it does not say which combination belongs to the three-dimensional summand and which one belongs to the trivial summand. The crystal edges distinguish them.

At the ordinary classical value of the deformation parameter, the trivial line is spanned by an antisymmetric tensor, plus tensor minus minus minus tensor plus. The quantum analogue uses q-dependent coefficients, and the precise combination depends on coproduct conventions. The crystal graph correctly predicts the one-dimensional summand without requiring us to pretend that a q-dependent canonical vector is literally the classical antisymmetric tensor.

## What is actually being reduced at q equals zero

An important technical detail prevents a common misunderstanding. We do not set q equal to zero in every formula of the quantum group and hope that its matrices remain finite. Quantum-group actions often contain inverse powers of q, so direct substitution can be singular.

Instead, one chooses a suitable lattice over functions regular at q equal to zero and works modulo the parameter. Kashiwara's modified raising and lowering operators preserve that lattice. Their induced action on the reduced basis gives the crystal arrows.

Thus the crystal is a controlled limiting structure, not an accidental singular value of the original representation. The existence of the suitable lattice and its compatibility with the operators are part of the theorem. For integrable highest-weight modules, this construction has a powerful theory; arbitrary modules do not automatically come equipped with a crystal basis.

The edge colors are indexed by simple roots. In sl two there is only one color. In a larger Lie algebra, different colors correspond to different simple-root directions. Each color isolates its own sl-two-like chains, while relations among colors encode the larger root system.

## From a crystal to a distinguished basis

A crystal graph gives combinatorial labels, but it does not uniquely specify vectors of the original q-dependent representation. Canonical and global bases address that lifting problem. They impose compatible normalization conditions, often including invariance under a bar involution, integral structure, and a specified leading behavior at the crystal limit.

This extra structure can reveal positivity of certain structure constants, but the phrase “all coefficients are positive” would be too broad. Positivity depends on the algebra, the basis, and the particular operations. The important promise is more precise: in suitable representation categories, the distinguished basis behaves well under geometric or categorical constructions and is independent of arbitrary choices of coordinates.

Lusztig's geometric constructions use quiver representations and intersection cohomology to realize canonical bases. Kashiwara's operators construct the crystal side. Their approaches meet in profound comparisons between geometry, combinatorics, and quantum algebra. A crystal vertex can label a basis vector whose construction involves deep geometry, even when the vertex itself looks like a simple box in a graph.

## Why tableaux and paths appear

For higher-rank Lie algebras, a vertex may be described by a semistandard Young tableau or a combinatorial path. The operators alter a tableau according to rules that preserve certain shape and weight constraints. This is not merely a mnemonic. Under the representation-theoretic hypotheses, those moves realize the same crystal structure as the abstract Kashiwara operators.

The payoff is algorithmic. Tensor-product multiplicities can be found by counting highest-weight components of a crystal tensor product. Weight multiplicities become counts of vertices. Relations that are opaque in matrix language become local combinatorial moves.

We must still watch the boundaries of the model. The crystal records rich decomposition data, but it does not automatically retain every scalar matrix coefficient, every extension between non-semisimple modules, or every analytic feature of a quantum-group representation. It is a deliberately compressed invariant.

## What the picture teaches

The crystal viewpoint suggests a general mathematical strategy. First isolate the structure you need to preserve. Next find a controlled limit in which that structure becomes combinatorial. Then lift back to a canonical object when more information is required.

For sl two, the process is visible in a four-state tensor square that separates into a three-vertex chain and a single vertex. For larger groups, it becomes a method for constructing and decomposing representations without expanding immense matrices. The graph is not a replacement for the representation; it is a map of its internal algebraic organization.

## Demazure Crystals and Key Polynomials

A Schur polynomial records the weights of an irreducible polynomial representation of a general linear group. It is symmetric in its variables because the complete representation has the relevant Weyl-group symmetry. But there are representation-theoretic spaces that are not closed under every direction of that symmetry.

A Demazure module is a structured partial representation attached to a Weyl-group element. Its character is a key polynomial in type A. These polynomials need not be symmetric, and that lack of symmetry is informative. They remember how far we have moved through the Weyl group, rather than erasing that history in the full irreducible character.

A useful way to understand this is to imagine the crystal graph of a highest-weight representation. Vertices represent basis-like combinatorial states; edges of different colors encode lowering operators for simple roots. A Demazure crystal selects certain vertices generated by a chosen pattern of lowering directions. The selection is constrained: it is not an arbitrary subgraph, and changing the Weyl-group word by a braid relation should not change the resulting object.

## Start with the smallest crystal

Consider the three-dimensional second symmetric power of the standard two-dimensional representation. It has weight monomials x-one squared, x-one times x-two, and x-two squared. The full character is their sum.

The highest-weight vertex alone contributes x-one squared. Following the single crystal string of color one takes us to the mixed weight and then to x-two squared. Those are three distinct vertices, and the full string yields the three-term character.

This small example already shows the contrast. One Demazure choice gives only the highest monomial, while the longer Weyl-group choice gives the entire Schur polynomial. With more variables, an intermediate Demazure character can be a genuine nonsymmetric key polynomial, neither one monomial nor the full Schur character.

The crystal picture matters because it contains more information than a formal manipulation of monomials. Operators along the graph know about representation strings and can be used for branching, tensor products, and combinatorial positivity.

## Demazure operators as divided differences

There is also an algebraic recipe. Let a simple transposition exchange two neighboring variables. The corresponding isobaric divided-difference operator takes a polynomial, multiplies it by the first of those variables, subtracts the result obtained after exchanging the variables, and divides by the difference of the variables.

It sounds as though we have divided by a polynomial and might obtain a rational function. But the numerator is antisymmetric under that exchange, so the difference of the variables divides it. The result is polynomial.

Apply the operator to x-one squared. The calculation produces x-one squared plus x-one x-two plus x-two squared. We have recovered the three crystal weights by algebra. This is the rank-one shadow of a much larger theory, but it is a genuine check: the operator and the crystal string agree term by term.

Repeated Demazure operators obey idempotence and braid relations. Those relations permit a composition attached to a Weyl-group element rather than to one particular reduced word. Without them, the character of a supposed geometric object would depend on an arbitrary choice of how to write a permutation.

## Why keys are not just smaller Schur functions

A Schur polynomial is indexed by a partition, a weakly decreasing sequence of nonnegative integers. Key polynomials naturally remember weak compositions as well as partitions. The ordering of their entries matters.

For a simple example in two variables, one Demazure character is x-one squared alone; another is the symmetric three-term sum. In three or more variables, there are intermediate possibilities. These are not generally invariant under swapping all variables, and one should not mistake them for ordinary symmetric functions with fewer terms.

There are different conventions for associating a composition and a Weyl-group element to a key polynomial. The safest statement is representation-theoretic: a Demazure character counts the weights in the corresponding Demazure module, and its crystal model counts the selected crystal vertices. When writing explicit combinatorial formulas, the chosen Borel and permutation conventions must be stated.

## Geometry behind a divided difference

Why should a character be built by successively applying simple reflections? The flag variety has Schubert varieties indexed by Weyl-group elements. A Demazure module can be realized using sections of line bundles associated with these Schubert varieties, under standard highest-weight conventions.

As a Schubert variety grows by one simple reflection, its combinatorial character changes according to a Demazure operator. The divided-difference identity is therefore a compressed shadow of geometry. A crystal string is another shadow of the same inclusion of representation-theoretic information.

This is why key polynomials appear in several apparently distant subjects: representation theory, Schubert calculus, tableau combinatorics, and algorithms for multiplying or decomposing characters. They are not merely a convenient nonsymmetric basis; they retain a filtration by geometric and algebraic choices.

## The limits of a picture

A crystal graph correctly records weight data and lowering behavior, but it does not by itself prove a statement about all modules over all fields. The standard crystal basis construction belongs to an appropriate quantum-group or integrable highest-weight setting. Demazure module geometry has its own hypotheses on weights, groups, and line bundles.

Likewise, a positive expansion of one polynomial into keys must be proved for that particular class of polynomials. It is not a consequence of saying that crystals exist. Much of current combinatorics asks which characters and generating functions admit such positive decompositions and what explicit crystal structures explain them.

The essential idea is that symmetry can be recovered in stages. The full Weyl character is the endpoint. A Demazure character records one controlled stage; the crystal graph makes that stage visible; and the divided-difference operators make it computable.

## Kazhdan-Lusztig Polynomials and Hecke Algebras

The symmetric group can be generated by adjacent transpositions: exchange two neighboring entries, and then repeat. Different words in those generators can describe the same permutation. The shortest length of such a word is a surprisingly important statistic. For permutations it equals the number of inversions.

A Hecke algebra begins with this combinatorics and introduces a parameter. The generators still obey the braid relations, but exchanging the same pair twice no longer simply gives the identity. Instead the square of a generator satisfies a quadratic relation involving the parameter. When that parameter is specialized to one, the original group algebra reappears.

At first this sounds like a formal deformation. Yet the resulting algebra contains a distinguished family of polynomials whose coefficients record geometry and representation theory. Those are the Kazhdan–Lusztig polynomials.

## Length and the Bruhat order

The symmetric group on three letters is a manageable test case. Its longest element reverses the order of all three letters and has length three. One may write it using the first adjacent exchange, then the second, then the first again. The braid relation says the opposite alternating word gives the same permutation.

The Bruhat order compares permutations by containment of reduced subwords. The identity lies below every permutation. A simple reflection lies below the longest permutation because a reduced word for the latter contains it. This order is not merely a ranking by length: there can be several elements of the same length that cannot be compared.

Kazhdan–Lusztig theory attaches a polynomial to each comparable pair of elements. The construction is characterized by a special basis of the Hecke algebra that is fixed by a bar involution, together with a triangularity requirement. The coefficients of the transition from the ordinary Hecke basis to this special basis are the polynomials of interest.

A remarkable feature is that these coefficients are nonnegative integers, but that positivity is a theorem. It is not evident from recursive calculations that mix additions and subtractions.

## A simple and a singular example

For the symmetric group on three letters, every Schubert variety in the full flag variety is smooth. In this small case the ordinary Kazhdan–Lusztig polynomials for comparable pairs are all equal to one. Thus one can work through the Hecke multiplication and the bar-invariant basis without yet encountering a nontrivial coefficient.

The first genuinely instructive singular example appears in the symmetric group on four letters. The permutation written three, four, one, two has a Schubert variety with a singularity, and the Kazhdan–Lusztig polynomial from the identity to that permutation is one plus q. Here q is the polynomial parameter, not a probability and not the size of a finite field in this sentence.

That extra term indicates nontrivial local intersection-cohomology behavior. Ordinary cohomology of a singular space can fail to have the duality properties enjoyed by smooth manifolds. Intersection cohomology restores an appropriate form of duality by modifying what chains are permitted near singular strata. Kazhdan–Lusztig polynomials encode graded information from this theory for Schubert varieties.

## Why geometry makes positivity believable

The algebraic definition gives a recursion, but a recursion alone does not explain why coefficients should be nonnegative. Geometry supplies graded vector spaces; their dimensions cannot be negative. The intersection-cohomology interpretation turns the coefficients into dimensions of graded pieces, subject to precise normalizations.

There is also an algebraic categorification. Soergel bimodules replace some of the Hecke algebra's formal basis elements by actual graded bimodules. Multiplication becomes tensor product, and taking a suitable character recovers the Hecke algebra. Deep Hodge-type properties of those bimodules imply coefficient positivity for arbitrary Coxeter systems.

It is worth distinguishing the results. The original Kazhdan–Lusztig construction gives the polynomials and conjectural representation-theoretic meaning. The geometric interpretation identifies them with intersection cohomology in the Weyl-group setting. The much later Hodge theory of Soergel bimodules proves positivity in the general Coxeter setting. Those are connected achievements, not one tautology.

## A representation-theoretic change of coordinates

Why does a special Hecke basis matter for representations? Because standard objects can be easy to define but poorly adapted to decomposition. Canonical or self-dual bases often organize the transition from standard representations to irreducible ones. The same phenomenon occurs in highest-weight categories, where multiplicities are encoded by Kazhdan–Lusztig data under suitable hypotheses.

The challenge is to preserve precise conventions. Reversing the indexing order, changing q into its inverse, or choosing the opposite Hecke normalization can alter the displayed polynomial formula. The intrinsic statement is not that the letters look identical in every book, but that the bar-invariant basis and geometric grading define a consistent invariant.

Kazhdan–Lusztig polynomials show how far one can travel from elementary permutations. A reduced word produces a partial order. Deforming multiplication produces a canonical basis. Its coefficients reveal singularities of flag varieties and multiplicities of representations. The parameter in the algebra has become a record of geometry.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Littlewood-Richardson Rules: Counting Tensor-Product Multiplicities

**Track:** Abstract Algebra. **Background:** representations of general linear groups, partitions, Young diagrams, tensor products, and symmetric polynomials. **Central question:** why can a tensor-product multiplicity be counted by filling boxes with numbers?

#### Mathematical companion (not spoken)

For partitions `lambda,mu,nu`, Schur functions satisfy
\[
 s_\lambda s_\mu=\sum_\nu c^\nu_{\lambda\mu}s_\nu.
\]
The integer `c^nu_(lambda,mu)` counts semistandard skew tableaux of shape `nu/lambda` and content `mu` whose top-to-bottom, rowwise right-to-left reading word is a lattice word. It is nonzero only for `|nu|=|lambda|+|mu|`. In `GL_n(C)` polynomial representation theory, discard partitions with more than n parts.

Pieri's rule for the one-box partition gives
\[
 s_{(2,1)}s_{(1)}=s_{(3,1)}+s_{(2,2)}+s_{(2,1,1)}.
\]
For `GL_3`, hook-content dimensions are `dim S_(2,1)(C^3)=8`, `dim S_(3,1)=15`, `dim S_(2,2)=6`, `dim S_(2,1,1)=3`, and `8*3=15+6+3`.

For the tensor square of the defining representation, `V tensor V = Sym^2(V) direct_sum wedge^2(V)` over characteristic not two, corresponding to `s_(1)^2=s_(2)+s_(1,1)`. The full LR rule is positive and independent of n once n is sufficiently large; specializing to small n can eliminate terms.

##### Exercises with answers

1. Expand `s_(2) s_(1)` by adding a box. **Answer:** `s_(3)+s_(2,1)`.
2. Why is the summand `s_(1,1,1,1)` absent in polynomial representations of `GL_3`? **Answer:** its partition has four nonzero rows.
3. What does a Littlewood-Richardson coefficient of two mean? **Answer:** two independent copies of the same irreducible representation occur in the tensor product.
4. Why does checking dimensions not establish the whole tensor decomposition? **Answer:** dimensions do not distinguish inequivalent representations of the same size.

##### Reading and source notes

- [Fulton and Harris, Representation Theory: A First Course](https://link.springer.com/book/10.1007/978-1-4612-0979-9), Young diagrams, Schur functors, and tensor-product rules.
- [Luoto, Mykytiuk, and van Willigenburg, An Introduction to Quasisymmetric Schur Functions](https://sites.math.washington.edu/~billey/colombia/references/QuasiSchurBook.pdf), combinatorial Schur expansions and variants of the LR rule.
- [Stanley, Enumerative Combinatorics, Volume 2](https://www.cambridge.org/core/books/enumerative-combinatorics/BC511C62A1EBE39B96F90838569C2825), symmetric functions and tableaux.

### Crystal Bases and Canonical Bases

**Track:** Abstract Algebra. **Background:** Lie algebra representations, weights, tensor products, quantum groups, and highest-weight modules. **Central question:** how can representation theory retain its combinatorial structure when a deformation parameter approaches zero?

#### Mathematical companion (not spoken)

For `U_q(sl_2)` and integrable highest-weight modules, a crystal basis consists of a lattice `L` regular at `q=0` and a basis `B` of `L/qL` preserved as a set, up to zero, by Kashiwara operators `\tilde e, \tilde f`. The irreducible crystal `B(n)` is a chain of `n+1` vertices of weights `n,n-2,...,-n`. The tensor product rule involves the string parameters `epsilon(b)` and `phi(b)`; different conventions affect which weight-zero element is isolated but not the decomposition
\[
B(1)\otimes B(1)\cong B(2)\sqcup B(0),\qquad V_1\otimes V_1\cong V_2\oplus V_0.
\]
At classical `q=1`, a basis of `V_0` is `v_+\otimes v_- - v_-\otimes v_+`; this is **not** asserted to be an identical formula for the global basis vector at generic q. Canonical/global bases refine crystal labels with integral and bar-invariance properties under suitable hypotheses.

##### Exercises with answers

1. How many crystal vertices belong to the sl-two highest-weight-five irreducible? **Answer:** six.
2. What are the weights of the irreducible highest-weight-two crystal? **Answer:** two, zero, minus two.
3. How many connected components appear in `B(1) tensor B(1)`? **Answer:** two, of sizes three and one.
4. Why not substitute `q=0` into arbitrary quantum-group matrices? **Answer:** entries may have poles; a compatible lattice and modified operators are required.

##### Reading and source notes

- [Hong and Kang, Introduction to Quantum Groups and Crystal Bases](https://doi.org/10.1090/gsm/042), standard introduction to crystal and global bases.
- [Schiffmann, Lectures on Canonical and Crystal Bases of Hall Algebras](https://www-fourier.ujf-grenoble.fr/sites/ifmaquette.ujf-grenoble.fr/files/schiffmann2_rev.pdf), geometric connections to quivers and canonical bases.

### Demazure Crystals and Key Polynomials

**Track:** Abstract Algebra. **Background:** highest-weight representations, Weyl groups, crystal graphs, and symmetric polynomials. **Central question:** what remains when we keep only the part of a highest-weight representation generated by one Borel orbit?

#### Mathematical companion (not spoken)

For variables `x_i,x_{i+1}`, let `s_i` exchange them. In the type-A convention used here,
\[
\pi_i f=\frac{x_i f-x_{i+1}s_i f}{x_i-x_{i+1}}.
\]
For `f=x_i^2`, this gives `pi_i f=(x_i^3-x_{i+1}^3)/(x_i-x_{i+1})=x_i^2+x_i x_{i+1}+x_{i+1}^2`. More generally for `a>=b`,
\[
\pi_i(x_i^a x_{i+1}^b)=\sum_{j=0}^{a-b}x_i^{a-j}x_{i+1}^{b+j}.
\]
Isobaric operators satisfy `pi_i^2=pi_i` and braid relations. With fixed highest-weight/Borel indexing conventions, the character of the Demazure crystal `B_w(lambda)` equals the Demazure character. The full longest-element crystal produces the Weyl character; intermediate characters need not be symmetric.

##### Exercises with answers

1. Compute `pi_1(x_1 x_2)`. **Answer:** `x_1 x_2`.
2. Compute `pi_1(x_1^3)`. **Answer:** `x_1^3+x_1^2 x_2+x_1 x_2^2+x_2^3`.
3. Why does the displayed operator return a polynomial? **Answer:** its numerator is antisymmetric under swapping `x_i,x_{i+1}`, hence divisible by their difference.
4. Does a Demazure character have to be symmetric in every variable? **Answer:** No; a partial Weyl orbit generally breaks full symmetry.

##### Reading and source notes

- [Demazure crystals and Schur positivity of Catalan functions](https://link.springer.com/article/10.1007/s00222-024-01237-5), key-polynomial and crystal-character formulas.
- [Demazure crystals for flagged key polynomials](https://arxiv.org/abs/2309.17025), crystal realizations and conventions.
- [Hong and Kang, Introduction to Quantum Groups and Crystal Bases](https://doi.org/10.1090/gsm/042), general theory of crystals.

### Kazhdan-Lusztig Polynomials and Hecke Algebras

**Track:** Abstract Algebra. **Background:** Coxeter groups, permutations, rings, and representation theory. **Central question:** why do polynomials arising from algebraic multiplication measure singularities of geometric spaces?

#### Mathematical companion (not spoken)

For a Coxeter system `(W,S)` use the equal-parameter Hecke algebra over `\mathbb Z[q,q^{-1}]` with basis `T_w` and generators satisfying `(T_s-q)(T_s+1)=0` plus braid relations, and `T_xT_y=T_{xy}` when lengths add. The bar involution sends `q\mapsto q^{-1}` and `T_w\mapsto T_{w^{-1}}^{-1}`. Normalizing by powers of `q^{1/2}` produces a self-dual Kazhdan–Lusztig basis, whose triangular expansion defines `P_{x,w}(q)` for `x\le w` in Bruhat order.

For `S_3` all ordinary Kazhdan–Lusztig polynomials `P_{x,w}` with `x\le w` are `1`. For `S_4`, with one-line notation `w=3412`, `P_{e,w}(q)=1+q` in the standard ordinary normalization. Check orientation and polynomial convention before comparing to tables of inverse or parabolic KL polynomials.

In type A the coefficients have a geometric interpretation through graded local intersection cohomology of Schubert varieties in `GL_n/B`. The Elias–Williamson theorem provides positivity for arbitrary Coxeter systems via Hodge theory for Soergel bimodules, not by assuming a flag variety exists for every such system.

##### Exercises with answers

1. Compute the Coxeter length of `321` in `S_3`. **Answer:** `3`, its three inversions.
2. Which specialization of the quadratic relation recovers `T_s^2=1`? **Answer:** `q=1`.
3. Why can an algebraic recursion containing subtraction still yield nonnegative coefficients? **Answer:** positivity comes from a separate geometric or categorified theorem, not a term-by-term sign argument.
4. What does `P_{e,3412}=1+q` suggest geometrically? **Answer:** nontrivial graded local intersection cohomology in the corresponding singular Schubert variety.

##### Reading and source notes

- [Kazhdan and Lusztig, Representations of Coxeter Groups and Hecke Algebras](https://doi.org/10.1007/BF01390031), original polynomial and canonical-basis construction.
- [Elias and Williamson, The Hodge Theory of Soergel Bimodules](https://arxiv.org/abs/1212.0791), positivity by categorified Hodge theory.
- [Elias and Williamson, The Hodge Theory of Soergel Bimodules (Annals)](https://annals.math.princeton.edu/2014/180-3/p06), published account and theorem statements.
