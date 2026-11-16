# 020000 — Block Designs, Finite Planes, and Hamming Codes

**Track:** Discrete Mathematics and Combinatorics. **Background:** incidence counting, finite fields, vector spaces, elementary coding theory. **Central question:** how can a small collection of subsets be balanced enough to support both experiments and error correction?

<!-- BEGIN SPOKEN LECTURE -->

# Block Designs, Finite Planes, and Hamming Codes

Suppose an experiment has seven treatments, and each trial can include three of them. We want to compare every pair fairly. Can we arrange the trials so that each pair of treatments appears together exactly once? The question sounds like scheduling. The answer is a piece of geometry, and the same geometry builds an error-correcting code.

Call the seven treatments points and the three-treatment trials blocks. There is no requirement that the points lie on a physical plane. What matters is which points belong to which blocks.

A balanced incomplete block design is specified by four numbers. There are v points, each block contains k points, and every pair of distinct points appears together in exactly lambda blocks. The number of blocks and the number of blocks containing one point are additional parameters. We do not get to choose all six numbers independently: simple counting forces equations between them.

## Two double counts

Count incidences of a point in a block. If there are b blocks of size k, there are b times k incidences. If each of the v points appears in r blocks, the same incidences number v times r. Those quantities must agree.

Now fix a point P. In each of its r blocks, P is paired with k minus one other points. Across all blocks through P, each of the v minus one other points appears exactly lambda times. Thus r times k minus one equals lambda times v minus one.

The equalities are elementary, but powerful. They can rule out proposed designs before we try to construct anything. For seven points, blocks of size three, and one appearance per pair, the second relation gives r equal to three. The first then gives b equal to seven. We must find seven triples, each point in three triples, covering every pair exactly once.

## The Fano plane without a drawing

Take the seven nonzero vectors in three-dimensional vector space over the field with two elements. For any two distinct nonzero vectors u and v, their sum is a third nonzero vector different from either one. Make a block from u, v, and their sum.

Why does this construction work? Every two distinct nonzero vectors determine a two-dimensional subspace. That subspace has four vectors in all: zero and three nonzero ones. So it determines a unique block of size three. Each pair belongs to exactly one such block. The seven points and seven blocks form the Fano plane.

The word plane is justified by its incidence axioms: any two points lie on a unique line and any two lines meet in a unique point. But the geometry is finite. It uses addition modulo two instead of distances and angles. Its symmetry comes from the linear algebra of a small field.

## Counting is a structural test, not an existence proof

The parameter equations are necessary, not sufficient. A proposed collection of numbers can satisfy the incidence counts without any design existing. Additional divisibility, parity, and geometric obstructions may intervene.

This is a lesson worth remembering when using counting arguments. A successful count verifies that a construction is possible in principle; it does not produce the construction. The Fano plane is valuable precisely because the vector-space model supplies both the necessary counts and an explicit family of blocks.

## From geometry to a parity check

Now arrange those same seven nonzero binary vectors as the columns of a matrix with three rows. Interpret the matrix as a parity-check operator. A seven-bit string is accepted as a codeword if multiplying its column vector by the matrix gives the zero vector over the field with two elements.

The matrix has rank three, so its kernel is four-dimensional. There are sixteen codewords among the one hundred twenty-eight possible seven-bit strings. This is the binary Hamming code of length seven and dimension four.

Why can it correct one bit error? If exactly one bit flips, the syndrome is the corresponding column of the parity-check matrix. Since all seven columns are distinct and nonzero, the syndrome tells us exactly which position was corrupted. A zero syndrome means the received word passes the parity checks, although it does not guarantee that no two or more errors occurred.

The smallest nonzero codeword has weight three. To see why, no one column is zero, and no two distinct columns add to zero. Yet every line of the Fano plane consists of three columns that add to zero. Thus the minimum distance is exactly three. By the standard distance criterion, the code can correct any one error or detect any two errors.

## A common combinatorial skeleton

The experimental design asks for balanced pair coverage. The finite geometry asks for unique lines through pairs of points. The error-correcting code asks for a sparse way to distinguish possible error locations. They are not three separate coincidences. They are consequences of the same incidence structure in a vector space over a finite field.

That is a recurring role of combinatorics: an arrangement first invented for one purpose may encode information useful in a different problem. When the relationships are exact, the translation can be proved, not merely suggested.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

A \(2\text{-}(v,k,\lambda)\) design has b blocks, each of size k, such that each unordered pair of distinct points occurs in exactly \(\lambda\) blocks. If every point occurs in r blocks, incidence counting gives
\[vr=bk,\qquad r(k-1)=\lambda(v-1),\qquad b=\frac{\lambda v(v-1)}{k(k-1)}.\]
These are necessary conditions. For the Fano plane, \((v,b,r,k,\lambda)=(7,7,3,3,1)\).

**Explicit construction.** Let points be \(V=\mathbf F_2^3\setminus\{0\}\). For distinct u,v in V, the unique line through them is \(\{u,v,u+v\}\). There are \(\binom72/\binom32=21/3=7\) lines. Each nonzero vector belongs to three lines. A seven-by-seven incidence matrix B (rows points, columns lines) has \(BB^T=(r-\lambda)I+\lambda J=2I+J\) over the integers, not modulo two.

For the binary Hamming code, form \(H\in\mathbf F_2^{3\times7}\) whose columns are the seven nonzero binary triples. Then C=ker H has dimension \(7-3=4\) and minimum Hamming distance 3. For any line \(\{u,v,u+v\}\), its three indicator coordinates give a codeword because \(u+v+(u+v)=0\). A single error at position j has syndrome \(He_j=h_j\), identifying its column.

### Exercises with answers

1. For a \(2\text{-}(9,3,1)\) design, what values of r and b are required? **Answer:** \(r=(9-1)/(3-1)=4\), \(b=9\cdot4/3=12\) (such designs exist as affine planes of order three).
2. Why can a parity-check matrix with two identical nonzero columns not correct every single error? **Answer:** flips in those positions give the same syndrome.
3. How many weight-three codewords arise from the Fano lines? **Answer:** seven, one for each line.
4. Why is minimum distance at least three for the seven-column construction? **Answer:** a nonzero kernel word of weight one needs a zero column; one of weight two needs two equal columns; neither exists.

### Reading and source notes

- [MIT OpenCourseWare, Mathematics for Computer Science](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/pages/readings/), counting and finite-field prerequisites.
- [Encyclopedia of Mathematics, Block design](https://encyclopediaofmath.org/wiki/Block_design), incidence parameters and balance.
- [MIT OpenCourseWare, Information and Entropy, Chapter 4](https://ocw.mit.edu/courses/6-050j-information-and-entropy-spring-2008/71667aa5e13663096278c6617fca34e5_MIT6_050JS08_chapter4.pdf), the (7,4,3) Hamming code.
