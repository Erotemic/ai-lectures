# 070000 - Littlewood-Richardson Rules: Counting Tensor-Product Multiplicities

**Track:** Abstract Algebra. **Background:** representations of general linear groups, partitions, Young diagrams, tensor products, and symmetric polynomials. **Central question:** why can a tensor-product multiplicity be counted by filling boxes with numbers?

<!-- BEGIN SPOKEN LECTURE -->

# Multiplying representations is not multiplying dimensions

Take two representations of a group and form their tensor product. The new vector space has dimension equal to the product of the old dimensions. But the resulting representation usually decomposes into several irreducible pieces, sometimes with repetitions. Dimension tells us how many vectors we have, not how those vectors transform.

For the general linear group over the complex numbers, polynomial irreducible representations are indexed by partitions. A partition is a weakly decreasing list of nonnegative integers; it is often drawn as a diagram of boxes. This combinatorial encoding is not accidental decoration. The partitions label highest weights, and the characters of the representations are Schur polynomials. A product of Schur polynomials is therefore a decomposition of a tensor product.

The Littlewood-Richardson rule answers the central question. Given two partitions, which third partitions appear in their product, and with what multiplicity? The answer is the number of certain fillings of a skew diagram that obey two families of constraints. We will first understand a small representation-theoretic example and then see how the counting rule reproduces it.

# The simplest example: symmetric and alternating tensors

Let V be a complex vector space of dimension at least two. The tensor square of V splits into symmetric tensors and alternating tensors. Swapping the two factors acts with eigenvalue plus one on the symmetric part and minus one on the alternating part. Every simple tensor has a symmetric and antisymmetric decomposition, so the whole tensor product is the direct sum.

In partition notation, V is labelled by the one-box partition. Its tensor square decomposes into the two-box horizontal partition and the two-box vertical partition. In Schur-polynomial notation, multiplying the one-box Schur function by itself gives the sum of the two corresponding Schur functions.

This is a first glimpse of the Littlewood-Richardson rule. There are two possible Young-diagram shapes after adding one box to a one-box shape: a row of length two or a column of height two. Each is counted once. The multiplicities are not guessed from dimensions; they are encoded by permitted box additions.

If V has dimension three, the symmetric square has dimension six and the alternating square has dimension three. Their sum is nine, the dimension of the tensor square. This is a helpful consistency check but not a proof of the decomposition for arbitrary group actions. The representation structure is supplied by the symmetry under swapping factors.

# Partitions and skew shapes

A partition such as three, one is a first row of three boxes and a second row of one box. If another partition fits inside it, we may remove the smaller diagram and obtain a skew shape. A skew diagram is not necessarily left-justified; it remembers which boxes were removed.

The Littlewood-Richardson rule uses skew diagrams whose large shape is the proposed output representation and whose removed shape is one input. We fill the remaining boxes using positive integers. The content tells us how many ones, how many twos, and so on, according to the other input partition.

The filling must be semistandard: numbers weakly increase along each row and strictly increase down each column. There is one more condition. Read the entries row by row from right to left, starting at the top. At every initial segment of that reading word, the number of ones must be at least the number of twos; the number of twos at least the number of threes; and so forth. This is called the lattice-word or ballot condition.

The number of fillings satisfying all these conditions is the corresponding Littlewood-Richardson coefficient. The rule is not merely a formula for dimension; it is a positive counting formula for every multiplicity. No alternating signs survive in the final answer.

# A three-term product

Now tensor the representation indexed by the partition two, one with the defining three-dimensional representation V. The rule for multiplying by a one-box partition is particularly simple: add a single box while keeping a valid partition.

Starting from the diagram two, one, we can add a box to the end of the first row, giving three, one. We can add to the second row, giving two, two. Or we can create a third row, giving two, one, one. Each option appears once. For the group of invertible three-by-three matrices, all three diagrams are allowed.

Let us check the dimensions. The original representation two, one has dimension eight in dimension three. Tensoring with V gives dimension twenty-four. The output diagrams three, one; two, two; and two, one, one have dimensions fifteen, six, and three, respectively. Fifteen plus six plus three is twenty-four.

This check is valuable because it catches forgotten shapes. But if two different fillings produce the same output partition, its multiplicity can exceed one. Such repetitions are a genuine feature of tensor products, and they are exactly why a counting rule is more informative than a rule that only lists possible shapes.

# Why the ballot condition matters

A semistandard filling can have the right content and still fail to describe a highest-weight contribution. The ballot condition imposes a directional balance: as we scan the word, we never see more twos than ones before enough ones have appeared, and the analogous condition holds at each higher value.

There is a representation-theoretic reason. Highest-weight vectors are killed by certain raising operators. In a combinatorial model, those raising conditions become restrictions on the reading word. The ballot criterion packages these restrictions into a test that uses only integers and boxes.

Different textbook conventions sometimes read the skew tableau in a different order and modify the ballot rule accordingly. Those conventions are equivalent when used consistently. Mixing the reading rule from one convention with the tableau shape convention from another is an easy way to get a wrong coefficient.

# The boundary imposed by the number of variables

A Schur polynomial in n variables vanishes when its partition has more than n nonzero parts. Accordingly, when describing polynomial representations of the general linear group of an n-dimensional space, we must discard partitions with too many rows. An abstract identity in the ring of symmetric functions may display shapes that are simply absent for a small chosen n.

This explains why the same universal Littlewood-Richardson coefficients describe tensor products of general linear groups in all sufficiently large dimensions, while smaller dimensions require a row-length restriction. The multiplicities stabilize once the ambient dimension has enough rows for the partitions involved.

# Why a counting rule is a structural theorem

There are several ways to prove the Littlewood-Richardson rule: geometric intersections of Schubert varieties, representation-theoretic constructions, and combinatorial correspondences. These approaches illuminate different aspects of the same coefficients. In geometry they are structure constants for intersections. In representation theory they are tensor-product multiplicities. In symmetric-function theory they are coefficients in a distinguished positive basis.

The concrete lesson is that tensor products do not have to be opaque. For representations of general linear groups, a continuous symmetry problem is converted into counting discrete objects. The boxes are not a toy model of the representation. They are a precise coordinate system for its highest-weight structure, and their permitted fillings encode how representations combine.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

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

### Exercises with answers

1. Expand `s_(2) s_(1)` by adding a box. **Answer:** `s_(3)+s_(2,1)`.
2. Why is the summand `s_(1,1,1,1)` absent in polynomial representations of `GL_3`? **Answer:** its partition has four nonzero rows.
3. What does a Littlewood-Richardson coefficient of two mean? **Answer:** two independent copies of the same irreducible representation occur in the tensor product.
4. Why does checking dimensions not establish the whole tensor decomposition? **Answer:** dimensions do not distinguish inequivalent representations of the same size.

### Reading and source notes

- [Fulton and Harris, Representation Theory: A First Course](https://link.springer.com/book/10.1007/978-1-4612-0979-9), Young diagrams, Schur functors, and tensor-product rules.
- [Luoto, Mykytiuk, and van Willigenburg, An Introduction to Quasisymmetric Schur Functions](https://sites.math.washington.edu/~billey/colombia/references/QuasiSchurBook.pdf), combinatorial Schur expansions and variants of the LR rule.
- [Stanley, Enumerative Combinatorics, Volume 2](https://www.cambridge.org/core/books/enumerative-combinatorics/BC511C62A1EBE39B96F90838569C2825), symmetric functions and tableaux.
