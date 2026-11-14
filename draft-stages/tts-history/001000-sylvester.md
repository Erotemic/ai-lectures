# 001000 — James Joseph Sylvester: How did matrices become objects that could be solved for?

**Track:** History · People and ideas. **Theme:** The birth of modern matrix language, invariant theory, and the linear matrix equation. **Background:** elementary algebra, determinants and eigenvalues; the lecture builds its constructions from examples.

<!-- BEGIN SPOKEN LECTURE -->

# James Joseph Sylvester: How did matrices become objects that could be solved for?

Two devices each have a pair of rotating pointers. On the first, they turn at two and five revolutions per minute; on the second, at one and four. Suppose we want a linear rule that translates the state of the first pair into the state of the second. The unknown is a transformation taking two numbers in and returning two numbers. It is itself a matrix. We are trying to solve for the whole transformation rather than for one scalar.

One modern equation for that problem asks us to find a matrix X such that A times X, minus X times B, equals a known matrix C. If A and B are diagonal, we can solve the entries of X by dividing by differences between the numbers on their diagonals. If one of those differences is zero, the division breaks down. The same mathematical question survives when the matrices are not diagonal: what can their spectra tell us about the existence and uniqueness of an unknown transformation?

This is the equation now commonly called the Sylvester equation. Its name leads to James Joseph Sylvester, a London-born mathematician whose career crossed an ocean twice, who was denied a Cambridge degree because he was Jewish, who worked as a lawyer and an actuary, and who helped establish research mathematics at the newly founded Johns Hopkins University. He coined the term matrix decades before most modern students would recognize matrix multiplication. He studied determinants, algebraic invariants and elimination, and in eighteen eighty-four published a sequence of papers on linear equations in matrices.

His life is a way to see how modern algebra became possible. It also warns us against treating a nineteenth-century name as though it referred to a single modern theorem with its exact present-day wording. What Sylvester and his contemporaries were doing was inventing the language in which such theorems could be stated.

## A mathematical education with a locked door

James Joseph Sylvester was born in London on September third, eighteen fourteen. His family name was originally Joseph. He added Sylvester, a surname also used by an older brother, while still young. He grew up in a Jewish family at a time when English universities attached civic and religious qualifications to degrees and academic posts. For an able student, mathematical talent did not automatically open an academic career.

His early education included the recently founded University of London, where Augustus De Morgan taught mathematics. The institution had been established in part as an alternative to the religious restrictions governing Oxford and Cambridge. The young Sylvester's first spell of university study ended abruptly after a serious dispute with another student. It would be misleading to turn that episode into a charming story of eccentric genius: it interrupted his studies. He later entered Saint John's College, Cambridge, in eighteen thirty-one. Illness also interrupted his progress there, and he finally sat the demanding Mathematical Tripos examination in eighteen thirty-seven.

He placed second. In the Cambridge system of that period, the student who ranked second in mathematics was called the Second Wrangler. It was an extraordinary result, achieved in a competition that dominated the mathematical life of the university. But Sylvester could not subscribe to the religious declarations required for a Cambridge degree. He was therefore denied the degree for which his examination performance had qualified him, along with normal access to academic fellowships. The University of Dublin later awarded him degrees, and Cambridge eventually conferred degrees in eighteen seventy-two, after the old restrictions had been removed.

A mathematical career was never simply a line from school to doctorate to professorship for Sylvester. The obstacle at Cambridge helped direct him into appointments abroad and into work outside universities. In eighteen forty-one he moved to the United States to teach at the University of Virginia. That appointment ended after a short and unhappy stay. Accounts of exactly what happened vary in emphasis, but the position did not give him the stable research environment he needed. He returned to England, where his employment included insurance work and the study and practice of law.

These are important details for understanding his mathematics. When we read the word matrix today, we can picture a tidy table on a screen and a standard library of numerical operations. Sylvester worked before that library of ideas existed. Moreover, he did much of his discovery without a permanent research appointment. His most productive mathematical relationships grew in part from the people he met while making a living in quite different settings.

## A lawyer meets another mathematician

Arthur Cayley also trained as a lawyer and worked at Lincoln's Inn. The two men met in London's legal world around eighteen fifty. Cayley was quieter in temperament than Sylvester, but they recognized a shared interest in algebraic forms and their transformations. They discussed mathematics while walking around the courts and continued to correspond and collaborate throughout their careers. Their names are often linked in the history of invariant theory and matrices, though their contributions were different.

To see what occupied them, consider a quadratic expression in two variables. It might be x squared plus four x times y plus three y squared. If we change coordinates by replacing x and y with linear combinations of new variables, the coefficients change. But some features remain. For example, whether the corresponding quadratic form is positive in every nonzero direction is an intrinsic property; it cannot be changed by an invertible real change of coordinates.

Algebraists in the nineteenth century asked which combinations of coefficients were preserved, or changed according to a simple rule, when such substitutions were made. A determinant is one example. Discriminants and other invariants provide further examples. They let someone study an algebraic object without becoming trapped in one particular choice of coordinates.

Take the polynomial x squared minus three x plus two. Its roots are one and two. The squared difference between the roots is one. The discriminant, calculated from the coefficients, is also one. Now change the constant term to nine quarters. The polynomial has a double root at three halves, and its discriminant becomes zero. A compact expression in coefficients has detected a change in the geometry of the roots: two previously distinct points have collided.

Sylvester did major work on discriminants and resultants in this period and helped establish the terminology. The ideas were developed by many predecessors and contemporaries, so none of the modern formulas should be credited to one inventor without qualification. His distinctive contribution was a sustained program of calculation, classification and new relations among algebraic forms. He was willing to introduce words when the available vocabulary did not distinguish the ideas he needed.

One of those words was matrix. In eighteen fifty he described an oblong arrangement of terms, by which he meant a rectangular array of coefficients. His initial conception emphasized a matrix as a source from which families of square determinants could be extracted. The word came with an image: the array was a kind of parent of the minors formed from it. That is already close to our notation, but it was not yet the full algebra of matrices as operators.

Cayley took an important next step. In his eighteen fifty-eight memoir he treated a matrix as an algebraic object that could be added to or multiplied by other matrices, including in settings where multiplication does not commute. It would be inaccurate to say that Sylvester invented every matrix operation that we use. The history is a collaboration and a succession of conceptual changes. Sylvester named and investigated a fertile structure. Cayley helped make its operations into a general theory. Later mathematicians developed its spectral theory and its analysis.

A simple multiplication illustrates why the new object was worth studying. Suppose a transformation first stretches horizontal positions by two and vertical positions by three. A second transformation then rotates the plane by a quarter turn. Reverse their order and most vectors arrive somewhere else. The entries can be written in a rectangular array, but the striking phenomenon is that composing transformations has an order. Matrices record composition, and composition is generally noncommutative. This fact eventually lies at the heart of the linear matrix equation named for Sylvester.

## Eliminating one unknown, then many

There was another strand in Sylvester's work that ran alongside matrices: elimination theory. Suppose two polynomial equations share an unknown x. We wish to know whether they have a common solution without first solving either polynomial explicitly. For linear equations, ordinary substitution works. For higher-degree polynomials, an arrangement of coefficients into a determinant can sometimes answer the common-root question directly.

Begin with the polynomials x squared minus three x plus two, and x minus one. They share the root one. If we divide the quadratic by x minus one, the remainder is zero. That remainder could have been calculated merely by substituting one for x. For a more complicated second polynomial, there is a systematic construction: multiply each polynomial by suitable powers of x, collect the coefficients of the resulting equations, and arrange those coefficients as a square matrix. The determinant of that matrix is the resultant.

In our example, because the polynomials share a root, the determinant vanishes. If we replace x minus one by x minus four, the determinant is nonzero: four is not a root of the quadratic. The resultant is a test for a common factor, expressed directly in the coefficients. The associated coefficient matrix is now called a Sylvester matrix, and the determinant is the Sylvester resultant.

Notice how different this is from the later equation A times X minus X times B equals C. In the resultant, a matrix packages several scalar polynomial equations so that a determinant can detect their compatibility. In the matrix equation, the unknown itself is a matrix. They belong to different mathematical constructions, even though both carry Sylvester's name. The path between them is the growing habit of considering arrays and linear maps as mathematical objects in their own right.

The resultant idea has a modern geometric interpretation. A polynomial with a repeated root shares a root with its derivative. Therefore its discriminant can be expressed, up to a coefficient and sign convention, through the resultant of the polynomial and its derivative. This explains why the discriminant vanishes exactly when roots collide, provided we account correctly for the degree and leading coefficient. The argument turns a geometric event into a condition on a determinant.

For a listener accustomed to numerical computation, there is also a caution. A resultant can be algebraically exact yet numerically difficult to evaluate. High-degree coefficient matrices can be ill-conditioned, and a tiny nonzero determinant is not automatically a reliable numerical certificate. Here we can see the distance between symbolic algebra in Sylvester's century and the numerical analysis of matrices in the twentieth. The objects are continuous, but the questions asked of them have changed.

## Woolwich, age restrictions, and a second American beginning

After attempts to return to an academic mathematics post, Sylvester became professor at the Royal Military Academy at Woolwich in eighteen fifty-five. Mathematics there was connected to training military engineers and artillery officers. He remained for fifteen years, publishing and teaching but working under an institutional system different from that of a research university. He became the second president of the London Mathematical Society and won recognition from learned societies across Europe. Yet retirement regulations forced him out of Woolwich when he reached fifty-five, in eighteen seventy.

For several years after that he was again without a regular professorship. He devoted energy to poetry and literary questions, publishing a book called The Laws of Verse. The fact that he sought patterns in meter and language fits his broad interests, but we should not infer that a poem and a polynomial were secretly the same pursuit. They simply belonged to the interests of someone who refused to confine his curiosity to the subject for which he was famous.

A fresh opportunity arrived with the founding of Johns Hopkins University in Baltimore. Its first president, Daniel Coit Gilman, wanted a university in which advanced research and the training of graduate students could be central. Sylvester accepted a professorship there in eighteen seventy-six and began teaching in the new institution's early years. He was already in his sixties. Many modern accounts of mathematical careers would place him near the end of his working life. In fact, some of his most consequential institutional work was still ahead.

He had students eager for research. He organized mathematical meetings and seminars, circulated problems, encouraged ambitious calculation, and created a community around work that was still unfamiliar in much of American higher education. In eighteen seventy-eight he founded the American Journal of Mathematics, establishing an enduring outlet for mathematical research published in the United States. The journal was neither the first American periodical ever to print mathematics nor solely his private enterprise, but its continuity and research ambitions were significant. Johns Hopkins gave him a context in which his passion for algebra could shape a generation of students and a national research culture.

One of the students whose admission he supported was Christine Ladd, later known as Christine Ladd-Franklin. The episode is revealing. Women faced restrictions in access to formal graduate degrees and fellowships. Sylvester's support helped her study at Hopkins even though the institution refused to grant her the same recognition it granted men. Having himself suffered religious exclusion, he could sometimes challenge another barrier, though the structures around him remained discriminatory. His advocacy did not by itself end those restrictions.

His Baltimore work included combinatorial problems, partitions and algebraic forms. A partition is a way of writing an integer as a sum of positive integers without regard to order. Four, for example, has five partitions: four; three plus one; two plus two; two plus one plus one; and four ones. At larger values, counting partitions becomes a deep problem in combinatorics. It also connects to algebraic invariants, because counting monomials of certain degrees and weights is a way of measuring the possible forms an invariant can take. The same researcher who had worked with determinants and polynomial roots found new problems in counting structures.

These years are a reminder that a historical portrait should not be reduced to a modern eponym. Someone who teaches the Sylvester equation may meet him through a single line of linear algebra. His reputation while alive also involved invariant theory, elimination, combinatorics, educational reform, and the practice of creating mathematical institutions.

## The matrix equation becomes a problem of its own

In eighteen eighty-three Sylvester was called back to Britain to occupy the Savilian Professorship of Geometry at Oxford. He became the first Jewish holder of an Oxford or Cambridge professorial chair, after earlier institutions had excluded him from academic qualifications. In the following year he published notes in the French Academy's Comptes rendus on linear equations in matrices, including a paper whose title translates as the general solution of the linear equation in matrices of arbitrary order. These publications belong to the historical origin of the modern Sylvester equation.

Let us now work through the matrix problem in a way nineteenth-century algebraists could have recognized, while using modern notation for precision. We are given two square matrices A and B, possibly of different sizes. We want to find a rectangular matrix X satisfying A times X minus X times B equals C, where C is prescribed. The products make sense if A acts on the output space and B on the input space. The dimensions of X are determined by those spaces.

Start with diagonal matrices. Suppose A has entries two and five down its diagonal, while B has entries one and four. An unknown two-by-two matrix has four entries, which we may name x eleven, x twelve, x twenty-one and x twenty-two. Multiplying by A on the left scales the first row of X by two and the second by five. Multiplying by B on the right scales the first column by one and the second by four. Subtract the results. Each unknown entry receives a coefficient equal to one difference of diagonal entries.

Those four differences are one, negative two, four and one. If C is a matrix of ones, the solution is immediate: the top row of X is one and negative one half; the bottom row is one quarter and one. Every entry has been recovered. There is exactly one answer because none of the four coefficients is zero. And we have learned something more useful than the answer itself: the danger lies in the differences between the two sets of diagonal values.

Now change B so that its second diagonal entry is five. The coefficient multiplying x twenty-two becomes zero. If the bottom-right entry of C is one, the corresponding equation reads zero equals one. There is no solution. If that entry of C is zero, x twenty-two can be any value, and uniqueness fails. When the two spectra share a value, the map taking X to A X minus X B cannot be invertible. It can have both a nontrivial kernel and an image smaller than the whole space of possible right-hand sides.

A natural objection is that most matrices are not diagonal. Some are diagonalizable only after a complicated change of coordinates; some are not diagonalizable at all. Could two matrices have no common eigenvalue yet still cause a failure of uniqueness? In finite dimensions over the complex numbers, the answer is no. The modern solvability criterion is exact: the equation has a unique solution for every C precisely when the spectra of A and B are disjoint.

It is worth understanding why. The equation is linear in X, even though it contains products of matrices. That means it defines a linear transformation on the vector space of all matrices of the required shape. There is a finite number of entries in X, so the familiar principle applies: a linear map between vector spaces of equal finite dimension is invertible exactly when its kernel contains only zero.

Suppose first that A and B share an eigenvalue lambda. Choose a nonzero right eigenvector of A for lambda. Choose a nonzero left eigenvector of B for the same lambda. Their outer product is a nonzero matrix X, and A X equals X B. So the linear map has a nonzero element in its kernel. The use of a left eigenvector here is necessary: multiplying X on the right by B acts on its rows, not on the columns in the way A does. For complex matrices, a left eigenvector may be considered as a nonzero row vector satisfying row times B equals lambda times row.

Now suppose they share no eigenvalue. Take an invertible change of basis that puts A into upper triangular form and a change of basis that puts B into upper triangular form. Because the triangular forms have the same eigenvalues as the original matrices, no diagonal entry of the first equals a diagonal entry of the second. If we write the equation in those changed bases, its unknown entries can be solved successively, beginning at one corner and moving in an order suited to the triangular factors. Each step divides by a difference of diagonal entries. Each such difference is nonzero. The solution exists and is unique.

The companion gives a shorter proof using a Kronecker product. Vectorize X by stacking its columns. The entire equation becomes one ordinary system of linear equations in the entries of X. Its coefficient matrix has eigenvalues equal to every difference of an eigenvalue of A and an eigenvalue of B. Invertibility of this larger coefficient matrix is therefore exactly the nonintersection of the two spectra.

We have reached a result that is stronger than the diagonal calculation and weaker than many infinite-dimensional claims one might be tempted to make. It is finite-dimensional. On infinite-dimensional Banach spaces, analogous statements require a careful theory of bounded operators and spectra, and an argument appropriate to the spaces involved. The same algebraic question survives, but we should not smuggle every functional-analytic conclusion into a nineteenth-century matrix result.

## Solvability is different from conditioning

The criterion tells us whether there is a unique answer. It does not by itself tell us whether the answer will be moderate in size or sensitive to errors. Consider two diagonal one-by-one matrices. One contains one; the other contains one plus one millionth. The spectra are disjoint, so the solution is unique. But if C equals one, the unknown X has magnitude one million. We have divided by a number close to zero. A tiny perturbation of the data can produce a large change in the answer.

In this elementary example, the smallest spectral difference measures the inverse problem's sensitivity. But there is a further complication for nonnormal matrices. Consider A equal to a two-by-two upper triangular matrix with one in the upper-left corner, two in the lower-right, and a large off-diagonal entry. Let B be the one-by-one matrix containing zero. Then the equation A X minus X B equals C is just A X equals C. The eigenvalues one and two stay fixed as we increase the off-diagonal entry. They remain a distance at least one from the eigenvalue of B. Nevertheless, the inverse of A can have entries that grow in proportion to that off-diagonal term.

For example, with an off-diagonal entry of one hundred, the inverse of A sends an input in the second coordinate to an output with a first coordinate of magnitude fifty. A spectral gap of one has not prevented a large amplification. The issue is that a nonnormal matrix may have eigenvectors that are almost parallel, so its eigenvalues alone do not control the norm of its inverse.

This distinction is central to matrix perturbation theory. A bound involving the reciprocal of a spectral gap is immediate for certain self-adjoint or normal operator settings. For general nonnormal problems, one often needs a separation quantity defined through the smallest singular value of the Sylvester operator itself, or estimates involving resolvents and eigenvector conditioning. The existence criterion and the numerical norm estimate are separate facts.

Sylvester lived before the modern language of operator norms and singular values had reached its present form. We can still use his historical work to arrive at the modern distinction. The question 'Can the matrix equation be solved?' creates a second question, 'How trustworthy is the solution when the inputs are approximate?' Much twentieth-century analysis begins at that second question.

## Inertia, signs, and what a change of coordinates preserves

There is another Sylvester theorem that reinforces the central idea of his algebraic career: a mathematical object may have features independent of the way we represent it. Sylvester's law of inertia concerns real quadratic forms. Let Q of x be a quadratic expression represented by a real symmetric matrix. By choosing suitable invertible real coordinates, we can make Q a sum of positive squares, negative squares, and possibly zero terms. The exact coefficients may change. But the numbers of positive, negative and zero squares do not.

Here is a concrete example. Consider the quadratic form x squared plus four x y plus three y squared. Complete the square: the expression is x plus two y, squared, minus y squared. Therefore it has one positive direction and one negative direction. The coordinate change that reveals those signs is invertible. The quadratic form is neither positive everywhere nor negative everywhere; on some nonzero vectors it is positive and on others negative.

We could describe the same form by a symmetric matrix whose diagonal entries are one and three and whose off-diagonal entries are two. The determinant is negative one. That negative determinant is consistent with one positive and one negative eigenvalue. But a determinant alone is not enough to recover the entire inertia in high dimensions. The general theorem tells us that any real invertible change of coordinates, even if it is not orthogonal, preserves the counts of the three kinds of directions.

Why does this matter for the history of matrices? A similarity transformation, which changes the basis of a linear operator, preserves eigenvalues. A congruence transformation, which changes the coordinates of a quadratic form, preserves inertia. These are different transformation laws. In nineteenth-century invariant theory, recognizing which quantities survive which transformations was one of the central intellectual tasks. Sylvester's name attaches to both the equation of a transformation unknown and a theorem about the signs of forms, but we should keep their hypotheses and mathematical roles distinct.

It is possible to see the law of inertia without relying on a heavy calculation. A maximal subspace on which the quadratic form is strictly positive has some dimension p. An invertible coordinate transformation maps positive subspaces bijectively to positive subspaces of the transformed form, so that maximum dimension cannot change. A parallel argument gives the maximal negative dimension q. The remaining dimension accounts for the null directions. Thus the signature records properties of the form itself rather than the coordinates used in its expression.

This kind of reasoning later appears in geometry, mechanics and the study of differential equations. Positive and negative quadratic directions distinguish stable and unstable behaviors in many settings. The law is a statement about congruence, not about the behavior of the eigenvalues under arbitrary changes of basis. Keeping that precise distinction is part of seeing what Sylvester's algebra accomplished.

## Latent roots and a changing vocabulary

In eighteen eighty-three Sylvester published an account relating matrix characteristic equations to the secular inequalities of planetary theory. He used the term latent roots for quantities we now call eigenvalues. It is a useful phrase. An eigenvalue is a special scalar that is hidden within the transformation: along a corresponding nonzero direction, the transformation behaves as multiplication by that number.

For our earlier diagonal example, the latent roots were simply the entries written on the diagonal. For a non-diagonal transformation they are found by solving a determinant equation. These roots help classify the operator, but they do not capture everything about it. Two matrices may share the same eigenvalues and still behave very differently under perturbation, as the upper triangular example has shown. The later distinction between spectrum and pseudospectrum has roots in exactly that limitation, though the terminology and theory of pseudospectra came much later.

Sylvester also pursued formulas for functions of matrices. Suppose we want to square a transformation, or compute an exponential that describes its repeated action over time. For a diagonal matrix, we simply apply the scalar function to each diagonal entry. For a diagonalizable matrix, a change of basis does the same calculation in different coordinates. When the eigenvalues are distinct, polynomial interpolation provides a convenient route: find a polynomial matching the desired function at each eigenvalue and apply that polynomial to the matrix. Sylvester studied such constructions in the eighteen eighties. The general theory has many contributors, but his interest helps explain why matrices were becoming more than containers for determinants.

Consider a matrix with distinct eigenvalues two and five. We can find a linear polynomial that takes the value four at two and twenty-five at five. Applying this polynomial to the matrix gives exactly the matrix square, because the two functions agree on its spectrum and the matrix has no repeated eigenvalue obstruction. For a general nonlinear function, the same interpolation idea gives a polynomial in the matrix with the correct values at the eigenvalues. Repeated eigenvalues and nontrivial Jordan blocks require additional derivative information, a development associated with later interpolation theory.

The intellectual continuity is clear. Elimination asks which polynomial relationships force a common root. Invariant theory asks which relationships survive transformations. Spectral theory asks which scalars and subspaces remain tied to the action of a matrix. A matrix equation asks whether a transformation can be recovered from its relations to two known transformations. These are distinct mathematical questions, but they share a search for structure beneath coordinate calculations.

## Later years and a human legacy

Sylvester moved from Baltimore to Oxford in the eighteen eighties. His Oxford professorship marked a late institutional triumph after the exclusion he had suffered as a young student. At Oxford he continued to pursue algebra and mathematical patterns, including his work on reciprocants, a species of differential invariant. His health eventually declined, and he was less active in his final years. He died in London on March fifteenth, eighteen ninety-seven.

It would be easy to present the life as a triumph over every obstacle, but that would miss its texture. He endured prejudice and unstable appointments, and his own teaching and personal relationships could be difficult. His collaboration with Cayley did not erase the differences in their methods. His writings can be energetic and hard to follow by present standards. His publications sometimes introduced new names in rapid succession. Historical work by Karen Hunger Parshall, using his correspondence and the records of the institutions around him, gives a much richer account than anecdotes about temperament alone.

We should also remember the changing scale of the mathematical world. When Sylvester studied, mathematics in Britain was deeply shaped by examinations, private tutoring, learned societies and the restrictions attached to educational institutions. By the time he left Johns Hopkins, the idea of a research department with graduate students, seminars and a specialist journal had acquired a stronger foothold in the United States. He had contributed both to the mathematical vocabulary and to the structures that let future mathematicians use and extend it.

Return finally to the unknown matrix X. In a diagonal example, we discovered that its entries could be divided by differences of eigenvalues. In general finite dimensions, the absence of any shared eigenvalue ensures that the linear map from X to A X minus X B is invertible. When the spectra meet, we can construct a nonzero solution of the homogeneous equation. And even when they do not meet, a solution may be sensitive if the corresponding linear operator is poorly conditioned.

Those three ideas belong together: the unknown is a transformation, spectral overlap determines exact solvability, and numerical separation measures the trustworthiness of a computed answer. The modern form of that statement draws on a century of algebra and analysis after Sylvester. His lasting contribution was to help give mathematicians both the objects and the language needed to ask the question in the first place.

<!-- END SPOKEN LECTURE -->

---

## Mathematical and historical companion (display only)

### 1. Finite-dimensional Sylvester criterion

For complex matrices \(A\in\mathbb C^{m\times m}\), \(B\in\mathbb C^{n\times n}\), and \(C\in\mathbb C^{m\times n}\), define
\[
\mathcal S_{A,B}:\mathbb C^{m\times n}\to\mathbb C^{m\times n},\qquad
\mathcal S_{A,B}(X)=AX-XB.
\]
Column-major vectorization gives
\[
\operatorname{vec}(AX-XB)=\bigl(I_n\otimes A-B^{\mathsf T}\otimes I_m\bigr)\operatorname{vec}(X).
\]
The Kronecker-sum coefficient matrix has eigenvalues \(\lambda_i(A)-\lambda_j(B)\), counted with algebraic multiplicity (triangularize A and B). Consequently,
\[
\forall C\ \exists!X:\ AX-XB=C
\quad\Longleftrightarrow\quad
\sigma(A)\cap\sigma(B)=\varnothing.
\]
For \(\lambda\) shared, select \(Av=\lambda v\) and \(w^{\mathsf T}B=\lambda w^{\mathsf T}\), with \(v,w\neq0\). Then \(X=vw^{\mathsf T}\neq0\) lies in the kernel. This uses *algebraic* transpose; it remains valid for complex matrices without conjugation.

### 2. The narrated 2-by-2 example

\[
A=\begin{pmatrix}2&0\\0&5\end{pmatrix},\quad
B=\begin{pmatrix}1&0\\0&4\end{pmatrix},\quad
C=\begin{pmatrix}1&1\\1&1\end{pmatrix},\quad
X=\begin{pmatrix}1&-\frac12\\\frac14&1\end{pmatrix}.
\]
Indeed \((AX-XB)_{ij}=(a_i-b_j)x_{ij}\), with differences \(\left(\begin{smallmatrix}1&-2\\4&1\end{smallmatrix}\right)\). If the last diagonal entry of B changes to 5, the lower-right coefficient vanishes, and the corresponding component of C must be zero for compatibility.

### 3. Nonnormal conditioning example

For \(A=\left(\begin{smallmatrix}1&100\\0&2\end{smallmatrix}\right)\), \(B=(0)\), and \(C=(0,1)^{\mathsf T}\), the equation is \(AX=C\) and \(X=(-50,1/2)^{\mathsf T}\), despite \(\operatorname{dist}(\sigma(A),\sigma(B))=1\). For nonnormal operators, spectral separation alone does not control \(\|\mathcal S_{A,B}^{-1}\|\) by the reciprocal of that distance.

### 4. Resultants and inertia

For \(p(x)=x^2-3x+2\), \(q(x)=x-a\), \(\operatorname{Res}(p,q)=p(a)\) under the standard monic convention. Thus \(a=1\) yields zero and \(a=4\) yields six. The quadratic discriminant \(\Delta(p)=(-3)^2-4(1)(2)=1\). For \(p_0(x)=x^2-3x+9/4\), \(\Delta(p_0)=0\).

The quadratic form \(x^2+4xy+3y^2=(x+2y)^2-y^2\) has inertia \((1,1,0)\). Sylvester's law of inertia concerns the signature under real invertible *congruence*, \(Q\mapsto T^{\mathsf T}QT\), and must not be confused with invariance of eigenvalues under *similarity*.

### 5. Historical chronology and attribution

- 1814: born in London into a Jewish family. 1837: Second Wrangler; excluded from a Cambridge degree by religious restrictions.
- 1841–42: University of Virginia appointment. Subsequent employment included actuarial and legal work.
- 1850: introduced “matrix” to describe an oblong array generating determinant minors; Cayley's 1858 memoir systematized a matrix algebra.
- 1855–70: Woolwich professorship. 1876–83/84: Johns Hopkins, research students and the *American Journal of Mathematics* (1878).
- 1883–84: Oxford professorship, 1884 series of *Comptes rendus* papers on linear equations in matrices; J. H. Maclagan-Wedderburn (1903) explicitly cites the series.
- 1897: died in London. Karen Hunger Parshall's archival scholarship is important for his institutional and personal history.

### 6. Readings and limits of attribution

The historical equation papers are not identical in notation and scope to the standard modern theorem stated above. The nineteenth-century work concerns linear matrix equations; the modern spectral criterion and later Banach-space generalizations should be attributed with that distinction. The lecture's mathematical examples are expository constructions, not claims about Sylvester's published numerical examples. Links and publication information are maintained in `metadata/sources.json`.
