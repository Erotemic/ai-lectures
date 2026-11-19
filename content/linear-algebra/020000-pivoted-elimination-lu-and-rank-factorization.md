# Elimination That Remembers Its Work: Pivoted LU and Rank Factorization

**Track:** Linear Algebra from First Principles. **Background:** systems of linear equations, matrix multiplication, linear independence and triangular matrices. **Purpose:** construct reusable factorizations from row operations; connect exact rank to the choices a floating-point solver must make.

<!-- BEGIN SPOKEN LECTURE -->

# Elimination That Remembers Its Work

A system of three equations can be solved by subtracting multiples of one equation from another, then working backward. But suppose the same matrix describes a bridge model, an electrical circuit, or a discretized differential equation, and we must solve it for a hundred different right-hand sides. Starting elimination from scratch for every new set of measurements wastes the most expensive part of the calculation.

The row operations themselves contain reusable information. A factorization stores that information in matrices that are easier to solve with than the original one. To understand exactly what is stored, we will first perform elimination by hand, including the row swaps that are easy to omit when we tell the story too quickly. Then we will follow what happens when the system has no unique solution.

## A pivot is a question we ask the next column

In Gaussian elimination, we start with the leftmost column that still needs attention. We choose a nonzero entry as a pivot, use it to clear entries beneath it, and move to the remaining smaller problem. A row operation changes the equations but not their common solutions. Swapping equations merely changes their order. Subtracting a multiple of one equation from another replaces it by an equivalent one, so long as the pivot equation remains available.

If the first entry is zero but a lower entry is nonzero, we must exchange rows. Even if the first entry is merely tiny rather than exactly zero, exchanging rows can matter greatly in floating-point arithmetic. Partial pivoting chooses, within the current column and among the remaining rows, an entry of largest absolute value. It is a local choice, not a search for an entire globally best matrix.

Consider a three-by-three matrix. Its rows, spoken one by one, are zero, two, one; one, one, zero; and two, zero, one. We choose a right-hand side with entries three, two, three. One can already check that the vector with every entry equal to one is a solution. Our job is to discover that solution using elimination, and to retain the calculation for later use.

The first column begins with zero. The largest entry below it is two, in the third row, so exchange the first and third rows. The upper row is now two, zero, one. To remove the one beneath this pivot, subtract one-half of that upper row from the row that originally began one, one, zero. The new row has entries zero, one, negative one-half. The remaining row has entries zero, two, one.

Our second-column pivot should be the two, not the one. Swap the two lower rows. Now subtract one-half of the new second row from the last row. We arrive at an upper triangular matrix with rows two, zero, one; zero, two, one; and zero, zero, negative one. All three diagonal pivots are nonzero, so the system has a unique solution.

The right-hand side undergoes exactly the same transformations. The accumulated row permutation sends it to three, three, two. Forward substitution with the two multipliers gives negative one in the final transformed entry. Back substitution says negative one times the third unknown equals negative one, so the third unknown is one. The second equation says twice the second unknown plus one equals three; the first says twice the first plus one equals three. We recover the three ones we expected.

## Where the lower triangular matrix comes from

Instead of remembering each subtraction as a sentence, record the multiplier used to clear each entry. Our example uses a multiplier of one-half in the first column, and another one-half in the second column. Multipliers belong in a lower triangular matrix with ones on the diagonal. The final coefficients belong in the upper triangular matrix.

There is one bookkeeping trap. We swapped the lower two rows after the first elimination step. The multipliers already recorded for those rows must follow the same swap. If we forget this, our alleged factorization will not reconstruct the original matrix. After the necessary reordering, the lower triangular matrix has first row one, zero, zero; second row zero, one, zero; and third row one-half, one-half, one. The upper triangular matrix is the one we just calculated.

Let P denote the matrix that performs our final row ordering. Then P times A equals L times U. This is called a pivoted L U factorization. P is a permutation matrix, L is unit lower triangular, and U is upper triangular. We keep P because row swaps are not lower-triangular elimination steps. Different pivot choices can give different factors for the same A.

To solve A times x equals b, first reorder the right-hand side with P. Solve L times y equals P times b by forward substitution, beginning at the top. Then solve U times x equals y by backward substitution, beginning at the bottom. For another right-hand side, P, L and U remain the same. Only the two cheaper triangular solves need to be repeated.

For a dense square matrix, forming the factors requires on the order of the cube of the matrix size arithmetic operations, while one pair of triangular solves takes on the order of its square. Those are asymptotic counts, not promises about actual time or memory. Sparse matrices raise another issue: zero entries may become nonzero during elimination, a phenomenon called fill-in. Row and column order can control how much memory that creates, subject to numerical stability requirements.

## What a tiny pivot does to arithmetic

Why did we choose the largest remaining entry in a column? Imagine a two-by-two system with first row epsilon, one and second row one, one, where epsilon is an extremely small positive number. The matrix is not close to singular just because its upper-left entry is small. As epsilon approaches zero, its determinant approaches negative one.

If we insist on the first row as our pivot, the multiplier needed to clear the one below it is one divided by epsilon. If epsilon is one over ten to the twentieth power, that multiplier is ten to the twentieth power. Intermediate values can become enormous, and later subtractions of nearly equal enormous quantities can erase useful digits. Swapping the two equations first changes the multiplier to epsilon, which is small.

This argument explains partial pivoting's practical power; it does not prove that it always provides tiny rounding errors. The magnitude of intermediate entries can still grow, and there are known matrices on which partial pivoting has a very large growth factor. A solver needs arithmetic and conditioning analysis, not just the reassuring name of a standard algorithm.

A pivot also answers a different question in exact arithmetic: does a new column provide a genuinely independent direction? A zero pivot below all permitted row swaps indicates that the remaining part of that column supplies no new independent equation. In a finite-precision computation, however, nearly zero and exactly zero are not the same statement. A threshold can declare a numerical rank, but that decision depends on scale, error assumptions, and the intended tolerance.

## Rank can be factored, too

Take a three-by-three matrix B with rows one, two, three; two, four, six; and zero, one, one. The second row is twice the first. More importantly, the third column is the sum of the first two columns. The first two columns are independent, so B has rank two.

Rather than just reporting the number two, build a factorization that explains it. Let C consist of the first two columns of B. Let R be a two-by-three matrix whose rows are one, zero, one and zero, one, one. Multiplying C by R reconstructs the three columns of B: first column, second column, and their sum. Thus B equals C times R.

This is a rank factorization. C has two independent columns; R has two independent rows. The factorization separates a map into a compression to two coordinates and an expansion back into three-dimensional space. It also reveals a null vector: negative one, negative one, one. Multiplying B by it produces zero, because the third column cancels the first two.

Notice how different this is from pretending we can solve every singular system by division. Whether B times x equals b has a solution depends on whether b lies in the column space of B. If it does, solutions differ by elements of the nullspace. If it does not, there is no exact solution, and least squares is a different problem, with a different objective.

Exact rank tells us about linear dependence; numerical rank asks whether dependence can be distinguished at available precision. An algebraic rank factorization need not be a well-conditioned basis for computation. Later we will use orthogonal transformations and singular values to make those numerical questions visible.

## Determinants and inverse matrices emerge as by-products

When a square matrix has full rank, all the triangular pivots are nonzero. The determinant of a triangular matrix is the product of its diagonal entries, and the determinant of the unit lower triangular L is one. A row swap changes the determinant's sign, so the determinant of A is the sign of the row permutation times the product of the pivots in U. For our example there are two row swaps. The pivot product is two times two times negative one, giving negative four. That is the determinant of the original matrix.

If the determinant is nonzero, we could solve A times x equals each coordinate vector in turn and assemble the results into an inverse matrix. That construction proves the inverse exists and gives it conceptually. In numerical work, however, explicitly forming the inverse is usually unnecessary if the task is to solve a system: the triangular factors already supply the desired operation, often with less work and less avoidable rounding.

The achievement of elimination is not merely a collection of zeros below a diagonal. We have turned a linear transformation into a sequence of transparent pieces: a reordering, a forward triangular transformation, and a backward triangular transformation. The same process shows us the dimension of its image, the source of its nullspace, and whether a computed solve has a mathematical chance of being unique. But the fact that the pieces are exact on paper says little, by itself, about how accurately finite-precision arithmetic will produce them. That question leads naturally to orthogonal methods and error analysis.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

### Full pivoted factorization and solve

Let

\[
A=\begin{bmatrix}0&2&1\\1&1&0\\2&0&1\end{bmatrix},\quad
P=\begin{bmatrix}0&0&1\\1&0&0\\0&1&0\end{bmatrix},\quad
L=\begin{bmatrix}1&0&0\\0&1&0\\\tfrac12&\tfrac12&1\end{bmatrix},\quad
U=\begin{bmatrix}2&0&1\\0&2&1\\0&0&-1\end{bmatrix}.
\]

Direct multiplication confirms \(PA=LU\). In particular, because the first multiplier belongs to the **original second row**, the later second-column swap moves it to the final row of \(L\).

For \(b=(3,2,3)^T\), we have \(Pb=(3,3,2)^T\); forward substitution gives \(y=(3,3,-1)^T\), and backward substitution gives \(x=(1,1,1)^T\). The permutation is a three-cycle, so \(\det P=1\). Thus \(\det A=\det U=-4\).

### Rank factorization and nullspace

\[
B=\begin{bmatrix}1&2&3\\2&4&6\\0&1&1\end{bmatrix}
=\underbrace{\begin{bmatrix}1&2\\2&4\\0&1\end{bmatrix}}_{C}
\underbrace{\begin{bmatrix}1&0&1\\0&1&1\end{bmatrix}}_{R}.
\]

Both \(C\) and \(R\) have rank 2. Hence \(\operatorname{rank}(B)=2\), and \(B(-1,-1,1)^T=0\). More generally, if \(A=CR\) with \(C\in\mathbb{F}^{m\times r}\) full column rank and \(R\in\mathbb{F}^{r\times n}\) full row rank, then \(\operatorname{im}A=\operatorname{im}C\), \(\ker A=\ker R\), and \(\operatorname{rank}A=r\). The image assertion follows because \(R\) is surjective onto \(\mathbb F^r\); the kernel assertion follows because \(C\) is injective.

### Row operations, stability and cost

In exact arithmetic, a nonzero pivot yields an invertible elementary matrix \(E_k\) such that \(E_k A_k=A_{k+1}\). Multipliers from the inverses of the elimination matrices give \(L\), but row permutations must be interleaved correctly. For partial pivoting \(PA=LU\); **this identity alone is not an error bound**. Pivot growth, data scaling, arithmetic precision, and conditioning matter separately.

Dense elimination costs \(\Theta(n^3)\) flops, while triangular solution costs \(\Theta(n^2)\) per right-hand side. Dense complexity statements do not predict sparse fill or cache behavior.

### Exercises with answers

1. **Check a column.** Reconstruct the third column of \(A\) from \(L\), \(U\), and \(P\). **Answer:** the third column of \(LU\) is \((1,1,0)^T\); applying \(P^T\) gives \((1,0,1)^T\), which is the third column of \(A\).
2. **Rank and solutions.** What is the general solution of \(Bx=0\)? **Answer:** \(x=t(-1,-1,1)^T\), any scalar \(t\).
3. **Determinant sign.** Why is the determinant negative rather than positive four? **Answer:** the diagonal pivots of \(U\) multiply to \(-4\), and there were two swaps, an even permutation.
4. **Zero versus tiny pivot.** Does a tiny leading diagonal entry imply the matrix is nearly singular? **Answer:** no; \(\left[\begin{smallmatrix}\epsilon&1\\1&1\end{smallmatrix}\right]\) approaches a nonsingular limit as \(\epsilon\to0\).

### Further reading and source connections

- Gilbert Strang, MIT OpenCourseWare 18.06SC, *Linear Algebra* (unit on elimination, row swaps, LU and the fundamental subspaces), https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/ .
- Jim Hefferon, *Linear Algebra*, https://hefferon.net/linearalgebra/ , for row equivalence, rank and bases.
- Lloyd N. Trefethen and David Bau III, *Numerical Linear Algebra* (SIAM, 1997; 2022 anniversary edition), https://people.maths.ox.ac.uk/trefethen/text.html , for factorization and finite-precision methods.
- Wikipedia topic pointers: [LU decomposition](https://en.wikipedia.org/wiki/LU_decomposition), [Rank factorization](https://en.wikipedia.org/wiki/Rank_factorization), [Gaussian elimination](https://en.wikipedia.org/wiki/Gaussian_elimination). These are orientation links, not substitutes for the textbooks.

For the numerical-error distinction, also see `numerical-analysis:006000`; for sparse solvers and preconditioning, see `numerical-analysis:014000`.
