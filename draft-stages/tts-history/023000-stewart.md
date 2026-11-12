# 023000 — G. W. Stewart: How should matrix perturbation bounds guide actual numerical work?

**Track:** History · People and ideas. **Theme:** G. W. “Pete” Stewart, the transformation of numerical linear algebra from isolated formulas to reliable algorithms; the QZ algorithm, Sylvester equations, invariant subspaces, separation, LINPACK, matrix factorization updates, stochastic perturbation theory, and mathematical history. **Background:** vectors, matrix multiplication, least squares, eigenvalues and orthogonality; the local examples introduce the needed subspace and conditioning concepts.

<!-- BEGIN SPOKEN LECTURE -->

# G. W. Stewart: How should matrix perturbation bounds guide actual numerical work?

Imagine that an engineering program has returned two numbers: the natural frequencies of a machine, computed from a model of its parts. The first frequency is close to one. The second is close to two. You ask the program how confidently it knows those numbers. It reports that every entry in the computed matrices is accurate to three decimal places. The frequencies are separated by a whole unit, so perhaps that sounds reassuring.

But there is something missing from that report. How do errors in matrix entries influence the frequencies? What if the matrix describing this machine is strongly non-symmetric? What if two directions of motion are nearly indistinguishable? And what if the algorithm was itself affected by floating-point rounding? An error of a thousandth in the matrix need not mean an error of a thousandth in the desired result.

Gilbert Wright Stewart the Third, known to colleagues as Pete Stewart, devoted much of his mathematical life to making such questions answerable. He built algorithms that engineers could actually run. He worked out ways of measuring whether a calculated subspace would survive small perturbations. He helped design software that could move from one machine to another. He also argued, through the structure of his research, that a statement about the sensitivity of a mathematical problem and a statement about the reliability of an algorithm have to be combined before one can trust a computed result.

Stewart lived from nineteen forty to twenty twenty-six. His career stretched from the era of specialized laboratory computers to the era when large matrix calculations became part of routine scientific and engineering software. Along the way he helped develop the QZ algorithm for generalized eigenvalue problems, the Bartels–Stewart method for matrix equations, and the LINPACK numerical software library. His work with Ji-guang Sun became a major reference on matrix perturbation theory. Yet his life also includes an early curiosity about history, a formative period at Oak Ridge, a profound influence from Alston Householder, and a late project translating the mathematical writings of Gauss.

To understand the questions Stewart chose, begin with the world in which he learned to compute.

## Knoxville, Oak Ridge, and the problem of making mathematics run

Pete Stewart was born on October first, nineteen forty, in Washington, D.C. His father worked as a journalist, and the family moved several times before settling in Knoxville, Tennessee. He completed high school there in nineteen fifty-seven. The future mathematical researcher was also a reader of history, a taste that survived his decades of work on algorithms.

He entered the University of Tennessee that year. His interests shifted among engineering physics, psychology, medicine, and mathematics. The categories made sense for someone whose questions crossed boundaries: how does an abstract idea work in an actual physical system, and what can a calculation tell us about a phenomenon that cannot be solved exactly by hand?

In nineteen fifty-nine, after his second year, a summer job at the Oak Ridge gaseous diffusion plant introduced him to practical computation. Oak Ridge had emerged from the enormous scientific and engineering projects of the preceding decades. Numerical calculation there was tied to equipment, measurement, design, and physical models. A formula could be beautiful, but it had to be translated into instructions for a machine, and those instructions had to cope with finite storage and finite precision.

Stewart graduated from Tennessee in nineteen sixty-three. A Woodrow Wilson fellowship took him to Princeton for graduate study, but he stayed for one year. He returned to Oak Ridge, spent a period programming for General Electric, and eventually resumed graduate work at Tennessee while remaining connected with the laboratory. The route was less linear than a conventional academic biography might suggest. Its practical center was continuous: build and examine computational methods under actual operating conditions.

One influence arrived through the work of James Wilkinson, whose analysis had made rounding error a mathematical subject in its own right. In numerical linear algebra, Wilkinson had shown the importance of asking whether a computed answer could be interpreted as the exact answer to a nearby problem. His work on eigenvalue algorithms offered a new model of what mathematical analysis of software could achieve.

At Tennessee, Stewart studied with Alston Householder, whose orthogonal transformations were among the essential tools of reliable numerical computation. Householder reflections can turn a vector toward a coordinate axis without stretching its length. They let algorithms eliminate matrix entries using transformations that control the propagation of rounding error. Stewart completed his doctorate under Householder in nineteen sixty-eight, studying the numerical behavior of methods for polynomial zeros and improvements to orthogonal iteration.

Pause at the phrase orthogonal iteration. Suppose a matrix repeatedly transforms a group of vectors. Instead of following each vector until it becomes enormous or nearly zero, periodically orthogonalize the group. The calculation can then follow the subspace spanned by the vectors. This is the beginning of a major distinction in Stewart's later work: individual coordinates may become unreliable long before the invariant subspace they describe becomes unreliable.

## From Austin to two algorithms that solved different problems

After his doctorate, Stewart joined the University of Texas at Austin. In that environment, he was close to numerical analysts asking how to compute eigenvalues, solve matrix equations, and exploit existing matrix algorithms. His work with Richard Bartels and Cleve Moler produced two influential methods within a few years of one another.

First consider a matrix equation. Most students meet an equation in which a matrix multiplies a vector. Here the unknown is an entire matrix. You are given two square matrices, one acting on the rows of the unknown, the other acting on its columns, and you need to determine the unknown matrix from their combined action.

The standard form is called a Sylvester equation. In one common sign convention it asks for a matrix X such that A times X, plus X times B, equals C. Such equations occur when one changes coordinates in block matrices, studies dynamical systems, or tries to decouple two interacting groups of variables.

The scalar version is almost embarrassingly simple. Suppose A is the number two, B is the number three, and C is ten. We seek a number x for which two x plus three x is ten. The answer is two. The coefficient five is the sum of the two scalar coefficients. The answer becomes sensitive when that sum approaches zero. At exactly zero, uniqueness disappears.

The matrix case inherits that idea, though the entries of X interact. Richard Bartels and Pete Stewart published their numerical method in nineteen seventy-two as Algorithm Four Hundred Thirty-Two in Communications of the ACM. It used a powerful reduction: first transform the two input matrices into Schur, or triangular, form. The unknown then obeys a triangular matrix equation that can be solved systematically, column by column or entry by entry. Finally transform the answer back into the original coordinates.

Why triangular form? In a triangular matrix, one part of an equation depends only on entries that have already been determined. The method preserves the original equation through orthogonal or unitary coordinate changes. That avoids the need to solve one enormous, unstructured system for every entry of the unknown at once.

There is also a condition for unique solvability. No eigenvalue of A may have the negative of an eigenvalue of B as a partner. For scalar coefficients two and three, their sum five is safely separated from zero. If one coefficient were negative two, the equation would no longer determine x uniquely. In larger matrices, spectral disjointness guarantees uniqueness, while the numerical sensitivity of the solution demands a more careful measurement that we will return to.

The algorithm is still known as the Bartels–Stewart method. The name records an instance of practical mathematical invention: an abstract equation, reduced to a sequence of reliable computational operations.

The second method came from a different problem. The usual eigenvalue equation asks for a direction that a single matrix merely stretches. But models of vibration, mechanical structure, and constrained physical systems often require two matrices. One represents stiffness or an operator. The other can represent mass or a second system of constraints. The equation says that A acting on a vector equals a scalar multiple of B acting on that vector. This is the generalized eigenvalue problem.

If B is invertible, it is tempting to multiply by its inverse and turn the problem into an ordinary eigenvalue calculation. Yet explicitly forming that inverse can amplify errors, and B may be singular. Singular mass or constraint matrices can have a meaningful physical interpretation. An algorithm cannot simply assume them away.

Stewart and Cleve Moler developed the QZ algorithm, published in nineteen seventy-three. The name echoes the QR algorithm but signals that two matrices must be transformed together. Instead of replacing a generalized problem by the eigenvalue problem of a newly inverted matrix, QZ applies coordinated orthogonal transformations and obtains compatible triangular forms. Those forms reveal generalized eigenvalues, including behavior that requires care when the second matrix is singular.

In their paper, Moler and Stewart emphasized precisely this feature: the algorithm makes no inversions of B or its submatrices. Think of a model that specifies one equation as a constraint rather than as an ordinary dynamic degree of freedom. Such a model may contain a zero row or a singular block in B. A computation that begins by dividing through by B fails before it has interpreted the model. A generalized Schur approach has a framework for proceeding.

These two algorithms, appearing close together, established a pattern. Stewart was interested in the algebraic structure of the problem, the transformations that preserved that structure, and the numerical consequences of choosing one computational route over another.

## The distinction between a small error and a trustworthy answer

To see why that distinction is necessary, return to a system of linear equations. Imagine an algorithm reports an approximate vector. The residual is the difference between the desired right-hand side and the product of the matrix with that vector. A tiny residual means the returned vector nearly satisfies the equations. That is valuable information, but how much does it tell us about the distance to the true solution?

Try a concrete two-variable system. The first equation says that the sum of two unknowns equals one. The second says that one thousandth of the second unknown equals zero. The exact solution is first unknown one, second unknown zero.

Now imagine a new measurement changes the right-hand side of the second equation from zero to one thousandth. The second unknown becomes one. To satisfy the first equation, the first unknown becomes zero. A thousandth of change in one measurement moved the solution by roughly one unit in each coordinate.

Nothing went wrong with the algebra. The second equation had very little leverage over the second unknown. The system was sensitive to errors in precisely that direction. In linear algebra this is quantified by a condition number. A large condition number warns us that modest changes in the data can produce much larger changes in the solution.

There are two distinct questions. An algorithm may be backward stable: its output solves a problem with inputs very close to those actually given. The mathematical problem may still be ill conditioned: those small input changes may produce large changes in its answer. A good implementation can be unable to rescue a badly determined inference. Conversely, a well-conditioned problem may be damaged by an unstable algorithm.

For square, invertible systems, the familiar normwise condition number is the matrix norm multiplied by the norm of its inverse. It roughly measures the maximum relative amplification of small relative perturbations, within the relevant hypotheses. If the input matrix has nearly dependent columns, the inverse has a large norm. Multiplication by it amplifies the residual.

Stewart's work returned repeatedly to the meeting point between the algorithm and the problem. A backward-error estimate describes the nearby problem an algorithm has solved. Perturbation theory then controls how much the answer to that nearby problem may differ from the original answer. Only when the two are combined do we have a quantitative explanation for an apparently accurate result.

## When a whole subspace is more reliable than a single direction

Eigenvalues and their eigenvectors introduce a further complication. Suppose two eigenvalues are almost equal. A tiny perturbation can change which eigenvector we assign to which of them, and can rotate their individual directions substantially. But a plane formed by those two directions may change very little if the pair is well separated from every other eigenvalue.

Imagine a three-dimensional system. Two directions lie in a nearly degenerate plane. Any orthonormal pair spanning that plane represents the same geometric object. If your application cares about the plane, asking for the error in each chosen basis vector measures an arbitrary coordinate choice as much as it measures the actual geometry. You need a distance between subspaces.

One way to compare equal-dimensional subspaces is by their largest principal angle. Two lines making an angle of six degrees have a well-defined separation, regardless of which unit vectors you choose to represent the lines. For planes in a higher-dimensional space, principal angles generalize that idea. Their sines describe how far vectors in one space can reach outside the other.

In nineteen seventy-three, Stewart published a major paper in SIAM Review on error and perturbation bounds for subspaces associated with eigenvalue problems. The treatment covered ordinary eigenvalue problems, generalized eigenvalue problems, and singular value decompositions. It tied the existence of a nearby invariant subspace to an iterative construction and provided computable estimates for its distance from an approximate one.

The basic thought can be explained without a large theorem. Suppose our trial subspace is a line along the first coordinate axis. A matrix nearly preserves that line, but every time it acts on a vector in the line, it pushes a small amount into the perpendicular direction. That perpendicular component is an invariance residual. If the matrix acts very differently in the perpendicular direction, we may be able to correct the trial line by a small rotation and obtain an exactly invariant line.

Take the simplest example. Along the first coordinate direction, the matrix acts with strength zero. Along the second direction, it acts with strength two. There is also a small coupling from the first direction into the second, of size two hundredths. The first axis is only approximately invariant: applying the matrix to its basis vector leaves a second-coordinate component of two hundredths.

To find an invariant line, we seek a vector with first coordinate one and second coordinate some unknown t. In this triangular example, the first coordinate of its image is zero, while the second becomes two hundredths plus two times t. For the line to be invariant with eigenvalue zero, we set that second component equal to zero. The answer is t equal to negative one hundredth.

So the exactly invariant line is tilted by about one hundredth of a radian. Its rotation is governed by the coupling of two hundredths divided by the separation of two. The calculation offers a geometric interpretation of a perturbation bound: a small residual divided by a sufficiently strong separation produces a small correction.

The word sufficiently is important. For general non-symmetric matrices, separating eigenvalues as points on the number line or in the complex plane does not by itself guarantee that subspaces are well conditioned. Stewart's work helped clarify how the operator connecting the two blocks of the matrix enters the analysis. We can now examine why.

## A spectral gap can hide a fragile geometry

Start with a two-by-two matrix whose diagonal entries are zero and one. Add a large entry, say one hundred, in the upper right corner. The two eigenvalues remain exactly zero and one. Their gap is one. If you looked only at that gap, you might imagine the eigenvectors were securely separated.

But examine the directions. An eigenvector for eigenvalue zero points along the first coordinate axis. For eigenvalue one, an eigenvector is proportional to the vector whose first coordinate is one hundred and whose second is one. The two directions are almost parallel. In other words, the eigenvalues are separated while the eigenvectors are nearly aligned.

Now add a small entry to the lower left corner, just one thousandth. The change in the matrix has norm one thousandth. The two new eigenvalues can be computed with a quadratic equation. Their separation depends on the square root of one plus four times one hundred times one thousandth. The original eigenvalue zero moves to about negative point zero nine one six, and the eigenvalue one moves to about one point zero nine one six.

A perturbation of one thousandth moved the eigenvalues by more than nine hundredths. We did not shrink the original eigenvalue gap. We changed the coupling between two nearly parallel eigendirections. This is a characteristic danger of non-normal matrices: the spectrum alone can give an incomplete picture of sensitivity.

There is a precise way to express the relevant distinction. When a matrix is partitioned into two blocks, correcting an approximately invariant subspace leads, at first order, to an equation in which one block multiplies the unknown correction from the left and the other block multiplies it from the right. That is another Sylvester equation, with a minus sign between the terms.

We saw earlier that such equations have unique solutions when their spectra are separated appropriately. But uniqueness and numerical stability are different questions. Even when no eigenvalue of one block equals an eigenvalue of the other, the mapping from an unknown correction to its residual may come close to losing information. We need to know how small the output of that mapping can be for a correction of unit size.

Stewart's separation measure, often written as sep, captures this idea. Take the smallest possible norm of the Sylvester expression when its matrix argument has norm one. A large separation means every proposed correction produces a substantial response. A small separation means some correction can almost disappear under the map, so reversing the map can magnify residuals.

To hear why this is more than a technical definition, consider a tiny example. Let the wanted block be a two-by-two matrix with both diagonal entries zero and an off-diagonal entry twenty. Let the unwanted block be the scalar one. Every eigenvalue in the first block is zero; the other block has eigenvalue one. The spectral gap is again one.

The Sylvester correction in this case is a row vector with two entries. If its entries are x and y, the Sylvester expression has first entry x and second entry y minus twenty x. Choose x to be roughly one twentieth and y to be about one. The input vector then has length nearly one, but the output has length only about one twentieth. The separation measure is around point zero five, far below the eigenvalue gap of one.

This is the practical meaning of the problem. In a symmetric or normal setting, geometric and spectral separation behave in particularly controlled ways. In general non-normal settings, a matrix may have well-separated eigenvalues and still possess directions along which the correction equation is almost singular. A sensible perturbation estimate has to recognize those directions.

The full invariant-subspace equation is more complicated than its first-order Sylvester approximation. When we represent a corrected subspace as the graph of a small matrix, nonlinear terms enter. We must show that the correction is small enough for those terms to remain controlled and that an invariant graph actually exists. Stewart's nineteen seventy-three analysis used constructive iteration to establish such conclusions under appropriate conditions. The residual, separation, and nonlinear correction all have distinct jobs in that reasoning.

This is why a bound is genuinely useful only when its hypotheses match the structure of the problem. Dividing an error norm by an eigenvalue gap may be an excellent estimate for one class of matrices. Applying the same formula indiscriminately to every non-symmetric matrix can be dangerously optimistic.

## Maryland, the mathematics of reliable software, and LINPACK

In nineteen seventy-two Stewart moved to Carnegie Mellon University, and in nineteen seventy-four he joined the University of Maryland. He stayed at Maryland for the rest of his full-time academic career, retiring in two thousand eight. His appointments connected computer science with applied mathematics and scientific computation. By then, numerical linear algebra was becoming a discipline in which published theorems and practical libraries had to develop together.

For many researchers, a computational method was initially represented by a mathematical paper and a local program. The program might be written for one machine, rely on its arithmetic conventions, and be revised by its original author when the hardware changed. That approach could not support the expanding use of numerical linear algebra across engineering and scientific computing.

LINPACK was a response to this problem. Stewart joined Cleve Moler, James Bunch, and later Jack Dongarra in developing a portable library of routines for dense matrix computations. Stewart chaired the project group. The library supplied methods for matrix factorization, linear systems, and related problems, accompanied by careful documentation and tests.

The project was built on elementary routines called Basic Linear Algebra Subprograms, or BLAS. A fundamental operation might multiply a vector by a scalar, add one vector to another, or compute a dot product. More sophisticated methods called these smaller operations rather than repeating machine-specific details everywhere.

That architecture gave library developers a practical lever. A new computer might execute vector operations differently from its predecessor. Instead of rewriting every factorization algorithm, implement or optimize the basic operations for that machine and retain much of the higher-level numerical code. In this way the structure of software mirrored the structure of the mathematics: isolate reliable transformations, then compose them.

Consider solving a linear system by factoring its matrix into two triangular matrices. The factorization is a general mathematical procedure. But its working life in a software library includes pivot selection, representation of data, scaling, detection of nearly singular behavior, and documentation that tells a scientist how to use the result. An algorithm without these details may be correct in a theorem and disappointing on a machine.

LINPACK also helped establish a culture of making numerical software portable and widely available. Its benchmark routines later became a familiar way to compare computers, though a benchmark should never be mistaken for a complete measure of scientific computing performance. The more consequential change was the confidence that a researcher could build on tested matrix routines rather than begin each new project by recoding the basics.

The LINPACK users' guide, published in nineteen seventy-nine, exemplified this combination of theory, implementation, and communication. Stewart's role in the project is documented by the other developers and by his own oral history, recorded in two thousand six. It was collaborative software work, not the invention of a single person working alone.

## Least squares and the moving geometry of a data set

Stewart's work on matrix factorizations extended beyond the original design of LINPACK. In a data-fitting problem, a matrix may change because another measurement arrives. Or a sensor may be taken out of service, removing one observation. If we have already factored the data matrix, repeating the entire factorization may be expensive. We would like to update it after the change.

Suppose a collection of measurement vectors spans a two-dimensional plane. We use a QR factorization: Q contains orthonormal directions for the plane, and R records how the original data columns are expressed in that basis. A new measurement may add information along an already known direction, or it may introduce a new direction. The efficient calculation should identify the new geometry without rebuilding everything from zero.

Updating adds information. Downdating removes it. The distinction is more dangerous than it first appears. An update of a positive definite matrix formed by adding a positive contribution tends to preserve positive definiteness. A downdate can bring the matrix toward singularity, or cross that boundary altogether. The loss of information can cause both genuine mathematical sensitivity and algorithmic difficulty.

A simple example makes this visible. Two measurements nearly agree on a linear relation between two unknowns. A third measurement strongly distinguishes them. With all three, the fit may be stable. Remove the third, and the remaining observations are nearly redundant. The best-fitting coefficients can now react violently to tiny data changes. The downdate did not create an implementation bug; it exposed the loss of an independent direction in the data.

Stewart contributed research on updating and downdating matrix decompositions and on the perturbation of QR and related factorizations. His nineteen seventy-seven paper examined the sensitivity of the QR factors when a full-rank rectangular matrix changes. It was important to keep track of both sides of the factorization. The orthonormal directions represented by Q can move, and the triangular coordinates in R can change differently. Their uncertainties cannot always be summarized by a single error on the original matrix entries.

For rank-deficient least squares, the pseudoinverse introduces another decision. If a data matrix has a tiny singular value, reversing it multiplies measurement noise by a large factor. Dropping that singular direction may produce a more useful estimate, but it changes the effective rank of the problem. Stewart's work on perturbations of pseudoinverses and projections clarified the sensitivity of these related geometric objects.

The practical lesson is that rank is not just a count supplied by software. In exact algebra, a singular value is either zero or nonzero. In experimental data and floating-point arithmetic, a tiny singular value may reflect a weakly measured direction. The size of that singular value relative to noise and modeling error determines whether treating it as informative is defensible.

A good library can expose the singular values and provide a reliable factorization. Perturbation analysis helps the scientist interpret them.

## A different way to ask what typical errors will do

Worst-case perturbation bounds are designed to survive every allowed perturbation. If we know only the largest possible error in the data, that protection is appropriate. But experimental errors often have a statistical description. Their components may have different variances, may be approximately independent, or may be correlated through a known measurement mechanism.

In nineteen ninety, Stewart published a paper called *Stochastic Perturbation Theory*. Its starting point was simple: approximate the change in a matrix-derived quantity by a first-order expansion, then treat the small perturbation as random. Instead of asking only for the largest conceivable deviation, estimate the mean, variance, or likely scale of the response under the chosen stochastic model.

Consider a smooth scalar quantity depending on two measurements. Suppose an error in the first measurement changes the quantity by twice that error, and an error in the second changes it by three times that error. A worst-case bound adds the two possible contributions in the most damaging alignment. If both errors can have magnitude one hundredth, the bound can reach five hundredths.

Now suppose the errors are independent, centered, and each has standard deviation one hundredth. The first-order response has variance equal to four times one ten-thousandth, plus nine times one ten-thousandth. Its standard deviation is the square root of thirteen, times one hundredth: about point zero three six. That value estimates typical scale under the model. It is smaller than the worst-case five hundredths, but it is no guarantee for an individual observation.

There is no contradiction between the two answers. One answers an adversarial question and the other answers a probabilistic question. The stochastic estimate depends on a specified distribution or covariance model, and first-order approximations may fail when perturbations are too large or when the quantity is near a singularity.

Stewart applied this style of analysis to linear systems, least squares, eigenvalues, eigenvectors, and invariant subspaces. His work is a reminder that numerical analysis can make use of information about how data were actually obtained. The right uncertainty calculation depends on the error mechanism, the geometry of the quantity of interest, and the purpose for which the answer will be used.

## A book that organized an expanding theory

Stewart's decades of perturbation work led to a major collaboration with Ji-guang Sun. Their book *Matrix Perturbation Theory*, published in nineteen ninety, organized the subject from norms and distances through linear systems, least squares, eigenvalues, invariant subspaces, and generalized eigenvalue problems. It treated both classical results and the complications introduced by non-symmetric and generalized settings.

An essential feature of this organization is that different questions require different measures of distance. When comparing vectors, the choice of norm affects what we count as a large error. When comparing matrices, a norm can emphasize the largest stretching direction or aggregate effects over many entries. When comparing subspaces, principal angles respect the fact that a plane has many equally legitimate choices of basis.

These choices are part of the statement of a theorem. Suppose a bound controls the sine of the largest angle between two subspaces. It does not immediately claim that every coordinate of every computed basis vector is accurate. The bound concerns the geometry of the subspaces. Choosing a basis within either subspace may involve an additional arbitrary rotation. A mathematically precise conclusion keeps those levels separate.

The same is true of spectral gaps. For a Hermitian matrix, a separation between a cluster of desired eigenvalues and the remaining spectrum is a powerful control on the change of its invariant subspace. For a general non-normal matrix, an appropriate Sylvester separation or other conditioning measure may be needed. For a generalized eigenvalue problem, both matrices of the pencil can change, and their roles must be included in the perturbation model.

The book also connected perturbation questions to unitarily invariant matrix norms, the kind of norms that depend on singular values rather than on the particular coordinate bases. Such norms are natural when an error should have the same size after an orthogonal change of coordinates. They make numerical estimates express geometric information rather than arbitrary choices of axes.

Stewart and Sun's achievement was to bring a large collection of delicate mathematical results into a coherent framework useful to researchers building and interpreting algorithms. That framework retained the differences between classes of problems rather than hiding them under a single convenient slogan.

## The historian of numbers, and the teacher of computation

There is another dimension of Stewart's career that belongs in a portrait of the mathematician. His early interest in history did not disappear as computer hardware advanced. During lunch breaks he studied Latin so he could read Carl Friedrich Gauss in the original. In nineteen ninety-five he published an English translation, with commentary, of Gauss's writings on the combination of observations.

Gauss's work was directly connected to the modern numerical subject of least squares. The historical question was therefore a technical question as well. How did people reason about measurement errors before digital computing? What assumptions about observations did they make? How did mathematical methods for combining uncertain evidence develop?

That interest adds depth to Stewart's work on condition numbers and stochastic perturbations. Numerical analysis asks what calculations can legitimately infer from imperfect data. Historical research shows that the problem of imperfect data long predates the computer. The twentieth century added vast computing power and new sources of rounding error, but the underlying demand for justified inference had been present for generations.

Stewart was also a committed writer and teacher. Among his books were *Introduction to Matrix Computations*, volumes on matrix decompositions, and the two volumes of *Afternotes*, written from graduate lectures. Colleagues described the care with which he developed both proofs and programs. His writing often moved between a small calculation, the geometry behind it, and the general algorithm it motivated.

His honors reflected the breadth of that work. He received the Friedrich L. Bauer Prize in nineteen ninety-eight, was elected to the National Academy of Engineering in two thousand four, became a Distinguished University Professor at Maryland in two thousand six, and was named a SIAM Fellow in two thousand nine. The academy recognized his development of numerical algorithms and software used in engineering computation.

Colleagues recalled a man who sometimes walked the halls thinking through a proof or a program, with coffee in hand, and whose office could send classical music into the surrounding corridor. Those recollections should not be confused with a theorem. They tell us something about the intellectual environment in which the theorems and software were made: a working department, a group of collaborators, and an individual who returned repeatedly to problems until the mathematics and the implementation could be explained together.

In two thousand ten, Misha Kilmer and Dianne O'Leary edited *G. W. Stewart: Selected Works with Commentaries*. It brought together many of his papers and commentaries on topics ranging from matrix decompositions to perturbation bounds and updating algorithms. The book itself is evidence of the range of his contributions. It also demonstrates why a mathematical career cannot be reduced to one named theorem.

Pete Stewart died on June ninth, twenty twenty-six, at the age of eighty-five. The University of Maryland and SIAM commemorated a long career whose outcomes included algorithms in routine use, generations of students and colleagues, a body of mathematical theory, and a substantial written record of how numerical computation became dependable.

## What a numerical answer needs in order to earn trust

Return to our opening machine with two computed frequencies. We now know to ask a sequence of precise questions. What matrices encode the model, and how accurately are their entries known? Is the eigenvalue problem ordinary or generalized? Are the matrices symmetric, or might non-normal effects make their eigenvectors fragile? Does the application need individual frequencies, individual eigenvectors, or a subspace representing a cluster of modes?

Next ask how the numbers were computed. Did the algorithm use transformations that preserve the structure of the problem? Can the output be interpreted as the exact solution of a nearby input? Is there a residual we can calculate? Can the relevant separation be estimated, and does it measure the correction equation that actually controls our desired subspace?

Finally, ask how uncertainty in the original measurements should be represented. A worst-case guarantee is appropriate when only a bound on error is justified. A stochastic estimate can be more informative when an error distribution is defensible. Each conclusion has its own hypotheses and its own meaning.

Stewart's career connected these questions to mathematics that could be used. The Bartels–Stewart method showed how a matrix equation could be reduced to triangular work. The QZ algorithm handled a generalized eigenproblem without demanding an inverse that might not exist. His invariant-subspace analysis measured the response of a geometric object to a residual and to the correct notion of separation. LINPACK turned reliable methods into portable tools. His later books explained the assumptions under which the computed answers should be trusted.

The small example of the non-normal two-by-two matrix is worth keeping in mind. The eigenvalues were separated by one. The perturbation was only one thousandth. The movement of the eigenvalues was almost a hundred times larger than that perturbation. A familiar gap gave an incomplete answer until we examined the geometry and sensitivity of the operator.

That is the enduring mathematical question behind Stewart's work: given the answer a computation has produced, what exactly has been established about the original problem? The reply is a chain of explicit reasoning, from input uncertainty through algorithmic error and problem conditioning to the geometric quantity that we actually intended to know.

<!-- END SPOKEN LECTURE -->

---

## Mathematical and historical companion (display only)


### 1. Backward error and forward error are different quantities

For nonsingular square `A`, exact solution `x=A^{-1}b`, approximation `x_hat`, and residual `r=b-A x_hat`:

\[
A(x-\widehat x)=r,\qquad
\|x-\widehat x\|\leq \|A^{-1}\|\,\|r\|.
\]

In particular, `A x_hat=b-r`: the approximation exactly solves the nearby right-hand side `b-r`. The normwise condition number is `κ(A)=||A|| ||A^{-1}||`, and relative forward error bounds require accounting for the size of the right-hand side or exact solution.

**Two-equation example.**

\[
A=\begin{pmatrix}1&1\\0&10^{-3}\end{pmatrix},\quad b=\binom10,
\quad x=\binom10.
\]

Replace `b` by `b'=(1,10^{-3})^T`. Then `x'=(0,1)^T`; `||b'-b||_2=10^{-3}` and `||x'-x||_2=\sqrt2`. This is *sensitivity of the mathematical problem*, with no floating-point algorithm involved.

### 2. Nonnormal eigenvalue sensitivity with a fixed eigenvalue gap

\[
A_K=\begin{pmatrix}0&K\\0&1\end{pmatrix},\qquad
E_\varepsilon=\begin{pmatrix}0&0\\\varepsilon&0\end{pmatrix}.
\]

`σ(A_K)={0,1}`, and eigenvectors can be chosen `v_0=(1,0)^T`, `v_1=(K,1)^T`. For `K=100`, they are nearly parallel. The perturbed characteristic polynomial is

\[
\det(\lambda I-(A_K+E_\varepsilon))
=\lambda^2-\lambda-K\varepsilon,
\quad
\lambda_{\pm}=\frac{1\pm\sqrt{1+4K\varepsilon}}{2}.
\]

With `K=100, ε=10^{-3}`, `||E||_2=0.001` and the displacements from the old eigenvalues are `(\sqrt{1.4}-1)/2 \approx 0.091608`. The original point-spectrum gap is 1. This demonstrates why an unqualified Davis–Kahan-style `||E||/gap` estimate does not apply to general nonnormal matrices.

### 3. From an approximate subspace to the Sylvester equation

In orthonormal trial/complement coordinates, partition

\[
A=\begin{pmatrix}B&F\\G&C\end{pmatrix},\qquad
B\in\mathbb C^{p\times p},\ C\in\mathbb C^{q\times q},\ G\in\mathbb C^{q\times p}.
\]

The trial subspace is the graph `T=0`, and `G` is the off-diagonal invariance residual. A candidate invariant subspace is the graph of `T\in C^{q\times p}`, spanned by columns of `\binom{I}{T}`. Invariance under `A` means that there exists a `p×p` matrix `M` with

\[
\begin{pmatrix}B+FT\\G+CT\end{pmatrix}
=\begin{pmatrix}I\\T\end{pmatrix}M.
\]

Thus `M=B+FT`, and the *exact graph Riccati equation* is

\[
G+CT-TB-TFT=0.
\]

The linearized correction has the Sylvester form

\[
\mathcal L(T)=CT-TB=-G.
\]

The Frobenius separation is

\[
\operatorname{sep}_F(C,B)
=\min_{\|Z\|_F=1}\|CZ-ZB\|_F
=\sigma_{\min}(I_p\otimes C-B^T\otimes I_q).
\]

When positive, `||\mathcal L^{-1}||_{F\to F}=1/sep_F(C,B)`; hence the first-order candidate obeys `||T||_F\le ||G||_F/sep_F(C,B)`. For exact graph `T` the largest principal angle satisfies

\[
\|\sin\Theta\|_2
=\frac{\|T\|_2}{\sqrt{1+\|T\|_2^2}}
\]

when the graph and base subspace have equal finite dimension. This graph formula alone does **not** prove existence of an invariant graph; a suitable contraction/iteration and control of `TFT` are needed. For the scalar example

\[
A=\begin{pmatrix}0&0\\0.02&2\end{pmatrix},\quad
T=-0.01,\quad
\operatorname{sep}_F(2,0)=2,\quad
\sin\theta=\frac{0.01}{\sqrt{1.0001}}.
\]

### 4. Point-spectrum separation versus Sylvester separation

Let

\[
B=\begin{pmatrix}0&K\\0&0\end{pmatrix},\qquad C=(1),\quad Z=(x,y).
\]

The eigenvalues of `B` are both zero, while `C` has eigenvalue one, yet

\[
CZ-ZB=(x,y-Kx).
\]

This row-vector mapping is represented by `M_K=\begin{pmatrix}1&0\\-K&1\end{pmatrix}`. Its smaller singular value is

\[
\operatorname{sep}_F(C,B)
=\frac{\sqrt{K^2+4}-K}{2},
\]

which is about `0.0498756` for `K=20` and tends to zero as `K` grows. The distance between the spectra remains one. This is a useful finite-dimensional witness for the role of nonnormality. It does not imply that every general-matrix perturbation theorem is stated solely in terms of `sep_F`; precise hypotheses and norms differ.

### 5. Bartels–Stewart and QZ algorithms

For `A X+X B=C`, choose Schur factorizations `A=U T_A U^*`, `B=V T_B V^*`. Put `Y=U^* X V` and `D=U^* C V` to obtain

\[
T_A Y+Y T_B=D.
\]

Solve the resulting triangular/quasi-triangular equations, then recover `X=U Y V^*`. Algebraic uniqueness requires `σ(A)\cap(-σ(B))=\varnothing`. Numerically, the conditioning is governed by the Sylvester operator, not solely by distinct eigenvalues. Real Schur forms use one-by-one and two-by-two diagonal blocks; the complex Schur form is triangular.

For a regular generalized eigenvalue pencil `A-λB`, the Moler–Stewart QZ approach uses orthogonal/unitary equivalence transformations on the **pair**, schematically `Q^* A Z=S`, `Q^* B Z=T` with triangular or generalized Schur forms, then relates the finite eigenvalues to diagonal ratios where defined. It does not start from `B^{-1}A`. The 1973 article addresses singular `B`; singular `B` does not alone imply a regular pencil has no meaningful finite eigenvalues. Singular *pencils* require separate qualifications.

### 6. QR factorization and changing data

For full-column-rank `A\in\mathbb R^{m\times n}`, `A=QR` with `Q^TQ=I_n` and `R` invertible upper triangular. The least-squares solution for `min_x ||Ax-b||_2` satisfies `R x=Q^Tb`. If a data row is inserted or removed, updating/downdating changes the factorization and can change conditioning. Stewart (1977) analyzed factor perturbations; his later work explored algorithms for update/downdate and projector representations. This topic is distinct from the claim that every downdate remains full rank or positive definite.

### 7. Worst-case and stochastic perturbations

For a scalar first-order response `δf \approx 2ε_1+3ε_2` with `|ε_i|\le0.01`, the deterministic bound is `|δf|\le0.05`. For independent, mean-zero errors of standard deviation `0.01`,

\[
\operatorname{Var}(\delta f)\approx(2^2+3^2)10^{-4}
=0.0013,
\quad \operatorname{sd}(\delta f)\approx0.036056.
\]

The latter is a first-order standard deviation **under the assumed error law**, not a worst-case bound. Stewart's 1990 *Stochastic Perturbation Theory* developed related probabilistic first-order analysis for matrix problems.

### Chronology and primary references

- **1940–1968:** Born Washington, D.C., October 1, 1940; childhood and high school in Knoxville; Tennessee B.A. 1963; Princeton fellowship; Oak Ridge and General Electric programming; Ph.D. Tennessee 1968 under Alston Householder. Biographical sources: Stewart's 2006 interview with Thomas Haigh, SIAM History of Numerical Analysis; Iain Duff, *Biography of G. W. Stewart* (2010); SIAM obituary (2026).
- **1968–1974:** Appointments at Texas at Austin and Carnegie Mellon; Bartels–Stewart, *Communications of the ACM* **15** (1972), 820–826, DOI `10.1145/361573.361582`; Moler–Stewart, *SIAM Journal on Numerical Analysis* **10** (1973), 241–256, DOI `10.1137/0710024`.
- **1973:** Stewart, *Error and Perturbation Bounds for Subspaces Associated with Certain Eigenvalue Problems*, *SIAM Review* **15**, 727–764, DOI `10.1137/1015095`. A constructive approach to approximate invariant subspaces across ordinary and generalized eigenproblems and SVD.
- **1974–2008:** Professor, University of Maryland, with related applied mathematics and scientific computing appointments. LINPACK collaboration with Moler, Bunch, and Dongarra; *LINPACK Users' Guide* (1979).
- **1977:** Stewart, *On the Perturbation of Pseudo-Inverses, Projections and Linear Least Squares Problems*, *SIAM Review* **19**, 634–662, DOI `10.1137/1019104`; *Perturbation Bounds for the QR Factorization of a Matrix*, *SIAM Journal on Numerical Analysis* **14**, 509–518, DOI `10.1137/0714030`.
- **1990:** Stewart, *Stochastic Perturbation Theory*, *SIAM Review* **32**, 579–610, DOI `10.1137/1032121`; G. W. Stewart and Ji-guang Sun, *Matrix Perturbation Theory* (Academic Press, 1990).
- **1995:** Stewart's English translation and commentary on Gauss's work on the combination of observations, published by SIAM.
- **1998–2010:** F. L. Bauer Prize 1998; National Academy of Engineering 2004; Distinguished University Professor 2006; SIAM Fellow 2009; Misha Kilmer and Dianne O'Leary, eds., *G. W. Stewart: Selected Works with Commentaries* (Birkhäuser, 2010).
- **2026:** Died June 9, 2026; memorials from the University of Maryland (July 9) and SIAM (October 16).

The direct historical sources, linked in `metadata/sources.json`, distinguish documentary career facts from the reconstructed calculations used here as teaching examples. The calculations in sections 1–7 are self-contained and are **not** claimed to appear with these exact numbers in Stewart's papers.

## Reading notes (non-spoken)

An excellent historical pairing is the 2006 oral-history interview and the October 2026 SIAM obituary by Kilmer, O'Leary, and Michael Stewart. The first gives Stewart's account of early computation and his collaborators; the second incorporates later career, teaching and remembrance. The 2010 *Selected Works with Commentaries* provides thematic assessments, with Iain Duff's biography and chapters devoted to matrix algorithms, rounding and perturbation analysis. For the mathematical spine use Bartels–Stewart (1972), Moler–Stewart (1973), Stewart (1973) on subspaces, Stewart (1977) on QR and pseudoinverses, Stewart (1990) on stochastic perturbations, and Stewart–Sun (1990). Citations and anchors are recorded in `metadata/023000.json`.
