# 007000 — Ernst Fischer: What Does It Mean for an Infinite Calculation to Have an Answer?

**Track:** History · People and ideas. **Theme:** Spectral min–max geometry, mean-square completeness, positive matrices and institutional history. **Background:** introductory eigenvalues, inner products, and integration; all local notation is established in the recording.

<!-- BEGIN SPOKEN LECTURE -->

# Ernst Fischer: What Does It Mean for an Infinite Calculation to Have an Answer?

Imagine trying to describe a sound by its pure tones. You listen to a complicated note and identify the strength of its first harmonic, its second harmonic, its third, and so on. Each measurement produces a number. But the list is infinite. Even if the individual numbers grow smaller, how can you be sure that all those numbers describe an actual sound? You might be able to write down every finite partial reconstruction while never obtaining a legitimate limiting function. A recipe that works for the first thousand tones must still survive the transition to infinitely many tones.

Now imagine a different problem: you have a symmetric matrix with a hundred eigenvalues. The largest and smallest have an immediate characterization through the Rayleigh quotient, the energy of a unit vector. But how could you identify the forty-third eigenvalue without first finding forty-two eigenvectors? Is there a geometric property that makes this number unavoidable, regardless of which trial subspaces you examine?

These sound like different questions. One concerns the existence of an infinite sum, the other the ordering of finitely many spectral values. Both depend on the geometry of a space of possible solutions. Both ask whether numbers extracted from a calculation truly correspond to an object in that space. And both were subjects of work by Ernst Sigismund Fischer, an Austrian mathematician born in Vienna in 1875.

Fischer's name survives in two major theorems, and there is a third inequality worth including in the story. The Courant–Fischer principle characterizes the eigenvalues of a symmetric matrix by choosing subspaces and optimizing a quotient. The Riesz–Fischer theorem concerns square-integrable functions, square-summable coordinates, and the existence of limits. A determinant inequality due to Fischer measures how correlations between blocks reduce the determinant of a positive matrix. The three results belong to a time when mathematicians were learning to think of functions, matrices, and infinite sequences as members of geometric spaces.

There is also a human history that cannot be reduced to those theorems. Fischer moved among Vienna, Brno, Erlangen, and Cologne. He worked in algebra as well as analysis, influenced Emmy Noether in the formative years of her mathematical career, served during the First World War, and was forced out of his Cologne professorship in 1938 under Nazi racial policy. He resumed teaching after the war. His biography brings both the creative reach of European mathematics and the destruction inflicted on its institutions into view.

Our mathematical question will be simple enough to hold in mind throughout: when does a finite calculation give reliable information about something larger than the calculation itself? We will approach it first through a three-dimensional matrix and then through infinitely many functions. The recurring lesson comes from the proofs, not from an analogy. Geometry tells us what finite approximations must do. Completeness tells us when an infinite limiting object exists.

## Vienna, matrices, and an emerging geometric language

Fischer grew up in a musical family. His father Jacob Fischer was a composer and professor at the Vienna Academy; his mother's family also included musicians and composers. It is tempting to turn that into a childhood explanation for his later work on Fourier series. The record does not establish such a connection, and we do not need it. The documented contrast is more useful: Fischer grew up around music and became a mathematician whose research helped make the mathematical analysis of complicated signals rigorous.

Beginning in 1894 he studied mathematics at the University of Vienna. His academic formation included Franz Mertens and Leopold Gegenbauer, and he received a doctorate in 1899. He spent time in Berlin and subsequently studied with Hermann Minkowski in Zürich and Göttingen. These moves placed him among several mathematical traditions. Number theory and algebra flourished alongside the new analysis of functions and integral equations. The language of linear transformations, quadratic forms, and invariants was becoming a shared way of stating problems.

In 1902 Fischer became an assistant at the German Technical University in Brünn, the city now called Brno. He gained the right to teach independently in 1904 and became an extraordinary professor in 1910. He was building a career during a period when the basic mathematical meaning of infinite-dimensional geometry was still being worked out. There was no universal modern textbook definition of a Hilbert space waiting to be applied. Analysts were asking which operations with infinite series and square-integrable functions were justified, and algebraists were learning when a change of coordinates could expose the essence of a calculation.

A quadratic form is a useful entry into that world. Take a symmetric matrix and a vector of numbers. Multiply the vector by the matrix, then take the dot product with the original vector. You obtain a single real number, an energy-like quantity. Divide by the squared length of the vector, and you have its Rayleigh quotient. Scaling the vector changes neither the quotient nor the directional information. That makes the quotient a function on directions rather than on lengths.

In two dimensions, picture a shallow valley whose cross sections are ellipses. The quadratic form is smallest in one principal direction and largest in the perpendicular direction. In three dimensions there are three orthogonal principal directions, with three ordered eigenvalues. The smallest eigenvalue is the least possible Rayleigh quotient over all unit directions; the largest is the greatest. The intermediate eigenvalues are where Fischer's work becomes interesting. They cannot be described merely by asking for a global extreme, because the same extreme would appear every time.

In 1905 Fischer published a paper on quadratic forms with real coefficients. Its modern legacy includes a method of forcing the middle spectral values to appear by varying the dimension of a trial subspace. The result is now associated with both Fischer and Richard Courant. The chronology is worth preserving: Fischer's finite-dimensional treatment came first; Courant's 1920 work developed variational characterization for eigenvalue problems arising in mathematical physics. A shared eponym does not make their individual contributions identical.

To see why the method works, we can calculate its core argument using just three numbers. No complex functional analysis is needed. The geometry of intersecting planes supplies the crucial step.

## The eigenvalue that every plane must encounter

Suppose a symmetric operator has three mutually perpendicular eigenvectors. In their coordinate system, it multiplies the first direction by one, the second by three, and the third by seven. For an arbitrary unit vector with coordinates x, y, and z, its Rayleigh quotient is one times x squared, plus three times y squared, plus seven times z squared. Since the squares add up to one, the quotient is a weighted average of one, three, and seven.

You can immediately recover the extreme values. Put the whole unit vector in the first direction and the quotient is one. Put it in the third direction and the quotient is seven. But what distinguishes three? A weighted average can be three for many reasons, and finding a single vector with quotient three tells us surprisingly little. There might be many such vectors that are not eigenvectors.

Fischer's idea is to stop choosing one direction at a time and choose an entire plane. Within any chosen two-dimensional plane, look at the smallest Rayleigh quotient available to its unit vectors. Then compare those minimum values for every possible two-dimensional plane. Which plane makes its own minimum as large as possible?

There is an obvious candidate. Choose the plane spanned by the second and third eigenvectors. Every unit vector in this plane has energy between three and seven. The smallest energy in that plane is exactly three, attained in the second eigenvector direction. So the largest attainable minimum is at least three.

Could some more cleverly tilted plane have minimum energy greater than three? To answer, consider the plane spanned by the first and second eigenvectors, where every Rayleigh quotient is at most three. Any two planes through the origin in three-dimensional space share at least one nonzero direction. In particular, any trial plane must intersect this low-energy plane. Choose a unit vector in that intersection. Its quotient is at most three. Since the minimum quotient of the trial plane cannot be larger than the quotient of one of its vectors, every trial plane has minimum at most three.

The two inequalities meet. One plane achieves a minimum of three, and no plane can do better. The maximum over two-dimensional planes of the minimum quotient in the plane is precisely the middle eigenvalue, three. We found it without first locating the individual second eigenvector by an algorithm. We only used the known structure of a symmetric operator and the dimension of an intersection.

There is a second way to trap the same number. For every two-dimensional plane, look at its largest Rayleigh quotient, and ask which plane makes that maximum as small as possible. The plane spanned by the first and second eigenvectors has maximum three. Any trial plane intersects the high-energy plane spanned by the second and third eigenvectors, so every trial plane contains some direction with quotient at least three. Hence the smallest possible maximum is again three.

These two descriptions sound like a puzzle: maximize a minimum or minimize a maximum. The puzzle disappears when you see two competing geometric requirements. A plane trying to avoid the low-energy directions has to include enough high-energy space to have a minimum of at least three. A plane trying to avoid the high-energy directions has to include enough low-energy space to have a maximum of at most three. Dimension forces a common spectral threshold.

For a matrix with many eigenvalues, the same proof uses the fact that subspaces whose dimensions add to more than the ambient dimension must intersect. If you want the kth eigenvalue in increasing order, you can take every k-dimensional trial subspace, find its worst, meaning largest, Rayleigh quotient, and minimize that over trial subspaces. Alternatively, you can take subspaces of dimension n minus k plus one, find their best, meaning smallest, quotient, and maximize that. A dimension count places the target eigenvalue between the opposing bounds, and the spans of suitable eigenvectors attain them.

A practical benefit follows. Suppose a laboratory or computer can only test vectors in a smaller trial space. The largest quotient of that space provides an upper bound for the corresponding low eigenvalue. Restricting an infinite physical problem to finite trial functions may therefore produce a useful number even before the full problem is solved. The precise direction of the bound depends on the variational formulation. It is valuable because the choice of a trial subspace is often much easier than the solution of the original eigenvalue equation.

But a min–max theorem does not automatically tell you the angle between an approximate eigenvector and the exact one. Think of a nearly repeated eigenvalue. Two neighboring energy levels can be separated by a tiny amount. A modest perturbation may rotate their corresponding individual eigenvectors substantially while barely shifting their eigenvalues. This is one reason spectral geometry developed beyond scalar inequalities. Fischer's variational control orders the levels; later subspace perturbation theory asks how their associated directions move. Those are complementary questions, not interchangeable guarantees.

## Why the finite proof can be trusted—and where it stops

It is useful to examine a small alteration of our three-dimensional example. Suppose you add a small symmetric error matrix whose operator norm is no more than one tenth. The Rayleigh quotient of any unit vector changes by at most one tenth. Because Fischer's min–max formula optimizes over exactly the same families of vectors and subspaces before and after the change, each ordered eigenvalue changes by at most one tenth. This is the geometric core of an eigenvalue perturbation bound.

That conclusion survives regardless of how complicated the error matrix looks. Its eigenvectors need not line up with those of the original operator. The proof never diagonalizes the perturbation. It uses only the uniform energy bound on every vector. For a numerical analyst, that is powerful: a bound on the error in the operator gives a bound on the error in the ordered spectrum.

Still, two limitations deserve attention. First, if the target eigenvalue lies close to another, the theorem controls its numerical location without guaranteeing its individual eigenvector. Second, the finite-dimensional proof relies on having n ordered eigenvalues and enough eigenvectors to span the entire space. An infinite-dimensional differential operator may have an unbounded sequence of eigenvalues, and it may have continuous spectrum rather than a discrete list at all. Extending variational reasoning then requires assumptions about domains, self-adjointness, and where isolated eigenvalues occur relative to the essential spectrum.

This is where the history of analysis meets the history of algebra. In a finite matrix problem, the input is a vector with finitely many coordinates and the output is another finite vector. In a problem with a vibrating string, the input is an entire function. A trial space of polynomials or trigonometric functions produces a sequence of finite approximations. At the end of the calculation, you need an answer to a new question: when those approximate functions become arbitrarily close according to the natural energy or mean-square measure, does a genuine limit exist in the same function space?

That question was urgent in the first decade of the twentieth century. The new Lebesgue integral allowed analysts to handle functions too irregular for the older integration rules. Fourier coefficients could be treated as coordinates in an enormous geometric space. But making this analogy rigorous required a theorem about limits, not just a suggestive picture.

Fischer helped supply it in 1907, and his work here is more central to the later language of Hilbert spaces than the short min–max portrait alone would lead you to expect.

## The problem with infinitely many Fourier coefficients

Consider the interval from zero to one, and imagine a function representing a sound or a temperature profile along a string. Its square-integrable energy is the integral of the square of its magnitude over that interval. Two such functions are close in the mean-square sense if the integral of the square of their difference is small. We take the square root and call that their L two distance. It measures average squared discrepancy, rather than the largest discrepancy at any single point.

Choose a collection of mutually orthogonal oscillations. For concreteness, use the sine waves that make an integer number of half oscillations along the unit interval, scaled so each has squared integral equal to one. Their orthogonality means that the integral of the product of any two distinct members is zero. This is the functional counterpart of the perpendicular coordinate axes in our three-dimensional matrix.

Now choose a coefficient for each sine wave. Let the nth coefficient be one divided by n. The first few strengths are one, one half, one third, one quarter, and so on. If you add the absolute values, that numerical series diverges; their total absolute strength has no finite sum. But if you add the squares of the coefficients, the result converges. It is the famous sum of reciprocal squares, equal to pi squared over six.

What happens when you use the first N sine waves to build a partial function? Take another partial function with more terms. The difference consists exactly of the added sine waves. Orthogonality makes the squared L two length of that difference equal to the sum of the squares of the newly added coefficients. This calculation is the infinite-dimensional analogue of the Pythagorean theorem. And because the tail of a convergent series of positive numbers tends to zero, the partial reconstructions become arbitrarily close to one another in L two distance.

That proves the sequence is Cauchy. Notice the missing step. It does not yet prove that there is a square-integrable function to which the sequence converges. In a space with missing limit points, you can find a Cauchy sequence whose expected limit simply does not belong to the space. Rational numbers provide the elementary analogy: rational approximations to the square root of two can become as close to each other as you please while their common real limit is not rational.

In the Fourier problem, the missing-limit possibility would mean that every finite sound reconstruction is legitimate but the limiting sound is not present in the chosen function space. The Riesz–Fischer theorem resolves the difficulty. The space of square-integrable functions, after identifying functions that differ only on sets of measure zero, is complete. Every Cauchy sequence in that mean-square metric converges in mean square to an actual square-integrable function.

For our example, a genuine function exists whose sine-wave coordinates are one, one half, one third, and so on. Its squared L two norm is the sum of the squared coefficients, because the sine system is complete as well as orthonormal. That norm is pi squared over six, so the norm itself is pi divided by the square root of six. What looked like an infinite list of measurements has become a real object of analysis.

There are two separate claims hidden inside this result, and it helps to hear them separately. The first is completeness of the function space: the limit exists. The second is coefficient realization: every square-summable list of desired coordinates can be produced by some square-integrable function. For any orthonormal sequence, the partial sums are Cauchy when the coefficients are square-summable, so completeness delivers a function with those coefficients. If the orthonormal sequence spans the whole Hilbert space, the coefficients determine that function uniquely. If it does not, you can add a component perpendicular to every listed wave and the coefficients will stay the same.

When a physicist uses the language of a complete set of modes, that extra adjective therefore carries a real mathematical responsibility. Orthogonality makes coefficients independent. Completeness of the mode system makes them sufficient to specify the function. Completeness of the function space guarantees that convergent coordinate recipes actually land somewhere.

## Convergence in mean is a different way to listen

Fischer's 1907 papers used the language of convergence in the mean. The phrase is not merely a different name for ordinary pointwise convergence. It answers a different question about what information should count as negligible in a limit.

Imagine a sequence of narrow spikes. At step n, the function is zero almost everywhere, except on the first one-nth of the unit interval. On that short interval, its height is the square root of n. At any fixed point strictly greater than zero, the spike eventually moves completely to the left of that point, so the sequence converges pointwise to zero there. Yet the squared height is n and the interval width is one divided by n. Their product, the integral of the squared spike, remains one at every step. In the L two metric, the function never gets closer to zero at all.

This one example tells us why pointwise convergence is too weak to control the energy of a signal. You can hide a fixed amount of squared energy inside a narrower and taller region. Conversely, mean-square convergence does not by itself require a whole sequence to converge at every point. It is a statement about average squared discrepancy, and it may leave room for changes on small sets. Additional hypotheses are needed to infer pointwise conclusions.

Why would a mathematician choose the mean-square distance rather than the maximum difference between two functions? Because the natural algebra of Fourier coefficients is a sum of squares. If two oscillations are orthogonal, the energy of their sum is the sum of their energies. The mean-square metric turns that physical and geometric rule into a Pythagorean identity. Maximum distance does not satisfy the corresponding identity. For orthogonal expansions, the L two metric is the one that makes the coefficient-space picture exact.

To appreciate the completeness result rather than only memorize it, consider the skeleton of a proof. Start with any Cauchy sequence of square-integrable functions. Because its terms eventually get as close together as you want, choose a subsequence whose successive differences have L two lengths smaller than one half, one quarter, one eighth, and so on. We have deliberately chosen the steps so their lengths have a finite total sum.

Now look at those successive differences as functions. On a finite interval, the integral of the absolute value of a function is bounded by its L two norm. Therefore the sum of the integrals of the absolute successive differences is finite. Except on a set of measure zero, the infinite sum of their absolute values converges. At almost every point we can add the successive differences and obtain a limiting value. Adding those differences to the first function in the subsequence defines a candidate limiting function.

There is one more step. We need to show that the candidate is square-integrable and that the convergence is in L two, not merely pointwise along our chosen subsequence. The triangle inequality bounds every finite sum of difference functions by the sum of their L two norms. A standard limiting argument for nonnegative integrals then puts the candidate in L two and makes the tails small in L two norm. The original sequence was Cauchy, so once the subsequence converges, the full sequence converges to that same function.

This proof sketch contains the essential mechanism. We extracted a carefully controlled subsequence, made an almost-everywhere limit from the summable differences, and used integration to show the limit stays inside the space. A complete space is one in which no Cauchy construction escapes. Fischer's work helped establish that the new integration theory had exactly that property.

The reward is enormous. If a differential equation is solved approximately by an increasingly fine series of trial functions, mean-square convergence can produce a genuine limiting function. That alone may not prove it satisfies every boundary condition or every derivative equation; those require the correct stronger hypotheses. But the existence of the limit is no longer a question left open at the end of the computation.

## One theorem, two researchers, and a question about credit

The theorem now called Riesz–Fischer did not emerge from a single publication or a single route through the proof. Frigyes Riesz, a Hungarian mathematician, and Fischer published closely related results in 1907. Riesz's note on orthogonal systems appeared in the Paris Academy's proceedings in March. Fischer's note on convergence in the mean appeared there in May, followed by a second applications note later that month. The modern joint name acknowledges work that came from both sides of a rapidly developing subject.

These are not just dates to place on a timeline. They show how mathematicians were trying to understand the same new territory from different directions. Riesz emphasized constructing coordinate descriptions for function spaces. Fischer emphasized the convergence and completeness properties that make those constructions legitimate. A later historical account by John Horváth examines the actual 1907 papers and points out that the two forms sometimes casually presented as the Riesz–Fischer theorem should not simply be declared equivalent in every abstract inner-product space. A statement about realizing square-summable coefficients and a statement about every Cauchy sequence converging can have different logical behavior when the space lacks completeness.

You can see the issue without difficult measure theory. Take the space of numerical sequences in which only finitely many entries are nonzero. Give it the ordinary sum-of-squares inner product. It contains every finite coordinate vector, and those coordinate vectors are mutually perpendicular unit vectors. Now take finite sequences whose first N coordinates are one, one half, one third, and so on. They get arbitrarily close in the sum-of-squares norm because the squared tail is small. But the infinite limit with coordinates one over n is not in the finite-support space. The space has missing points. Its completion is the full space of square-summable sequences.

If a theorem says that every square-summable prescription of coefficients should correspond to a vector in this finite-support space, our example refutes it. If a theorem says that every Cauchy sequence in this space converges inside the space, the same example refutes that too. They fail together here, but the example is enough to show what is being assumed when we use the familiar Hilbert-space version: the limiting objects must have been included. The precise relationships among stronger and weaker abstract versions require careful formulation, as Horváth's paper emphasizes.

There is an appealing way to read the historical collaboration without inventing a conversation between the two men. Imagine an analyst asking: which numerical measurements are permitted? The square-summability condition answers the numerical part. Another analyst asks: what entity, if any, carries those measurements? The completeness theorem answers the existence part. Both questions are needed before infinite-dimensional coordinates become a trustworthy language.

Later expositions sometimes compress the story into the sentence that L two is isomorphic to ell two. This is accurate for a separable infinite-dimensional Hilbert space after choosing a complete orthonormal system, but it hides several achievements. One must show that Fourier coefficients preserve squared length, that sufficiently many functions are represented, and that all square-summable coordinate lists produce members of the function space. Those are substantive analytic steps. The theorem deserved the attention it received because it connected the new Lebesgue integral to a usable geometry of infinitely many coordinates.

## What a determinant says about mixing two sets of variables

Fischer did not stop working on quadratic forms when he turned to Fourier analysis. In 1908 he published an extension of Hadamard's determinant inequality for positive definite matrices, now often called the Hadamard–Fischer or Fischer inequality. It provides a third way to see the same interest in geometry through algebraic quantities.

A determinant measures how a linear transformation scales volume. For a positive definite matrix, its determinant is positive, and it can also be interpreted as a squared volume when the matrix is a Gram matrix of vectors. A Gram matrix records the inner products among a collection of vectors: its diagonal entries are their squared lengths, and its off-diagonal entries measure their mutual alignment.

Start with two vectors of squared lengths two and three. Suppose their inner product is one. Their Gram matrix has two on the first diagonal, three on the second, and one in each off-diagonal position. Its determinant is two times three minus one squared, which equals five. If the two vectors were perpendicular while preserving those squared lengths, the determinant would be six. Correlation reduced the squared area spanned by the vectors. The two vectors contain less independent geometric spread because they lean toward one another.

Hadamard's inequality says more generally that the determinant of a positive definite matrix is no larger than the product of its diagonal entries. Fischer's version allows you to group coordinates into blocks. If a positive definite matrix is divided into two principal diagonal blocks, its full determinant is no larger than the product of the determinants of those blocks. When the cross-block interaction vanishes, equality holds. For a strictly positive definite matrix, any nonzero cross-block interaction makes the inequality strict.

One way to understand the formula is to imagine two groups of measured variables. Analyze each group internally, and its determinant describes its independent volume. When you combine the groups, cross-correlations tie some directions together. They cannot increase the total independent volume beyond the product you would obtain by treating the groups as orthogonal. The proof can be expressed using a positive Schur complement, although Fischer's original treatment came from the matrix techniques of his own time.

The inequality later became part of matrix analysis, statistics, and the study of positive operators. The historical sources credit Fischer's 1908 extension specifically. The modern theorem is not merely a new notation for Hadamard's one-coordinate-at-a-time inequality: it retains information about whole interacting blocks. That makes it a useful addition to the account of a mathematician whose public identity is often reduced to two other hyphenated names.

## Erlangen, Emmy Noether, and a change in algebraic thinking

In 1911 Fischer became a professor at Erlangen, succeeding Paul Gordan. This brings us to one of the most consequential personal relationships in his mathematical career. Emmy Noether had completed her doctorate under Gordan in 1907 and was continuing mathematical work in an environment where women faced severe barriers to academic appointment and habilitation. She was already a capable, ambitious researcher. Fischer entered this setting with an interest in abstract reasoning shaped by the algebraic methods associated with Hilbert.

The older invariant theory had often proceeded through extensive symbolic calculations. A difficult problem might ask for a catalogue of polynomial expressions left unchanged by specified transformations. The computational methods could be formidable. Hilbert's approach encouraged researchers to ask instead about structural properties of the collections of invariants: which ideals, relations, and finite-generation statements organize all the calculations at once? Fischer's mathematical conversations with Noether helped expose her to that shift.

Noether herself acknowledged his influence on the arithmetical and abstract direction of her algebra. Hermann Weyl later emphasized Fischer's role in her intellectual development. These are strong historical testimonies. They should be read without reducing Noether's later achievements to Fischer's instruction. A formative influence helps explain a transition; it does not transfer authorship of a mature research program. Noether developed far-reaching algebraic methods of her own, and her contributions to ideals, rings, and symmetry reshaped the field. Her statement about Fischer is best understood as testimony to a meaningful intellectual exchange during a period of change.

There is a mathematical connection between that episode and Fischer's work on infinite-dimensional analysis. In both fields, the pressure came from problems that became unmanageable when treated as long lists of individual formulas. In algebra, structure can replace repeated symbolic elimination. In functional analysis, an inner product and a completeness theorem can replace a separate convergence argument for each Fourier series. These are not the same theorem or even the same branch of mathematics. They are related changes in mathematical practice: identify the properties of an entire space that make many particular calculations possible.

Fischer's own publications also covered finite abelian groups, invariant fields, and questions about irreducibility, alongside his work on Fourier analysis and determinants. The biographical record therefore presents someone engaged with both algebra and analysis. His career illustrates how porous the boundaries between those subjects were during the early formation of modern abstract mathematics.

Fischer served during the First World War from 1915 to 1918. He married Elisabeth Strauss in 1917, and the couple had a daughter. In 1920 he moved from Erlangen to a professorship at the University of Cologne. These dates locate his career across two very different political eras: the international expansion of mathematics before 1914, and the dislocation of European academic life after 1933.

## Cologne, persecution, and the limits of an institutional record

Fischer remained at Cologne through the years when the Nazi regime began expelling scholars from German universities. The record for his own retirement deserves to be stated precisely. A university biographical register gives the date of his emeritus status as October 1, 1938, and describes it as retirement for political reasons. Historical research on the Nazi-era dismissal of mathematicians identifies him as a Cologne professor of partly Jewish ancestry who was prematurely retired in 1938. His retirement was forced by the regime's racial policy. This was persecution, not a voluntary withdrawal from mathematics.

Other distinguished scholars were expelled earlier, among them Emmy Noether in 1933 because she was Jewish. The dates differ because the Nazi apparatus made distinctions among people it categorized according to its racial laws, while continually extending exclusion and tightening control. Such distinctions did not make the later victims safer or the earlier exclusions less destructive. The consequence for mathematics was the forced removal of people from their positions, the interruption of teaching and research, and the breaking apart of academic communities.

It is important not to let a short biographical entry erase that history. Some general biographies say only that Fischer retired in 1938. That is chronologically correct but materially incomplete. Conversely, the documents do not justify an invented detailed account of his private reactions, conversations, or activities in every year of the dictatorship. We can state the documented forced retirement and the context of racial persecution while leaving unrecorded personal experience unclaimed.

The Erlangen university faculty register records his return to teaching in the winter semester of 1945–46. That detail makes his later career more than a date of dismissal. Fischer lived until November 1954, dying in Cologne at the age of seventy-nine. His surviving mathematical name belongs to results developed decades before the Nazi regime, but his professional life was nevertheless shaped by its persecution. A historically responsible account has room for both facts.

There is also a lesson about the way mathematical memory works. A theorem name is a compressed citation, and a compressed citation leaves out almost everything about the people involved. Courant–Fischer can obscure the difference between Fischer's finite-dimensional 1905 paper and Courant's 1920 applications. Riesz–Fischer can obscure the two researchers' independent methods and the detailed chronology of their 1907 notes. The determinant inequality may be omitted altogether. Noether's acknowledgment of Fischer may disappear behind the achievements of her later Göttingen career. And a neutral phrase like retired in 1938 may conceal political coercion.

Restoring these details does not weaken the mathematical results. It helps explain how they were made, why they mattered, and which parts of the story the familiar names leave out.

## Return to the infinite calculation

We began with a list of sound frequencies and asked whether it could describe a real signal. We also began with a hidden middle eigenvalue and asked whether geometry could identify it. Fischer's career supplies a rigorous answer to each question.

For the matrix, dimension forces trial subspaces to intersect, and the Rayleigh quotient traps the desired eigenvalue. For the Fourier series, orthogonality converts differences of partial sums into sums of squared coefficients, and completeness turns a Cauchy recipe into an actual function. For the determinant, positivity tells us that cross-correlations cannot increase the independent volume of two blocks. These are different results with different hypotheses, united by a practice of turning an apparently enormous calculation into a small set of structural facts.

A calculation with finitely many terms can be persuasive because it agrees with physical intuition. A mathematical theory asks for more. It asks what remains true for every possible trial plane, every square-summable list of coefficients, or every positive definite block matrix. Fischer was among the people who helped articulate and answer those questions as modern spectral and functional analysis took shape.

The enduring value of his work is therefore concrete. When we use a finite basis to approximate a vibrating structure, when we reconstruct a function from Fourier measurements, or when we bound the eigenvalues of an approximate operator, we depend on the relationship between a coordinate calculation and the space in which it is supposed to make sense. Fischer helped turn that relationship into a theorem. And his life reminds us that the institutions which sustain that work have a history that deserves just as careful an accounting as the proofs.

<!-- END SPOKEN LECTURE -->

---

## Mathematical and historical companion (display only)

### I. Matrix variational principle and Fischer's 1905 theorem

Let \(A=A^*\in\mathbb C^{n\times n}\) have eigenvalues
\(\lambda_1\le\cdots\le\lambda_n\), and put
\(R_A(x)=\langle Ax,x\rangle/\langle x,x\rangle\), \(x\ne0\).
With eigenvectors \(e_1,\dots,e_n\), for any \(k\),
\[
\lambda_k=\min_{\dim S=k}\ \max_{x\in S\setminus0}R_A(x)
=\max_{\dim S=n-k+1}\ \min_{x\in S\setminus0}R_A(x).
\]
Proof of the first identity: take \(S_0=\operatorname{span}(e_1,\ldots,e_k)\)
to attain \(\max_{x\in S_0} R_A(x)=\lambda_k\). For any \(k\)-plane \(S\),
\(\dim S+\dim\operatorname{span}(e_k,\ldots,e_n)=n+1\), so their
intersection contains \(x\ne0\); this \(x\) has \(R_A(x)\ge\lambda_k\).
The second identity uses the analogous low-energy intersection.

For \(A=\operatorname{diag}(1,3,7)\) and \(k=2\),
\[
\begin{aligned}
3&=\max_{\dim S=2}\min_{0\ne x\in S}R_A(x),\\
3&=\min_{\dim S=2}\max_{0\ne x\in S}R_A(x).
\end{aligned}
\]
For the max-min, every \(S\) intersects \(\operatorname{span}(e_1,e_2)\);
\(\operatorname{span}(e_2,e_3)\) attains the maximum. For the min-max,
every \(S\) intersects \(\operatorname{span}(e_2,e_3)\);
\(\operatorname{span}(e_1,e_2)\) attains the minimum.

For Hermitian \(E\), \(|R_{A+E}(x)-R_A(x)|\le\|E\|_{\mathrm{op}}\);
applying min-max gives \(|\lambda_k(A+E)-\lambda_k(A)|\le\|E\|_{\mathrm{op}}\).
This bound does not control individual eigenspace angles without a gap.

Historical anchors: Fischer, *Über quadratische Formen mit reellen Koeffizienten*,
*Monatshefte für Mathematik und Physik* **16** (1905), 234–249; Courant,
*Über die Eigenwerte bei den Differentialgleichungen der mathematischen Physik*,
*Math. Z.* **7** (1920), 1–57. Attribution and the difference between the
finite- and infinite-dimensional formulations are discussed in the sources below.

### II. Mean-square geometry and the Riesz–Fischer step

Work in complex \(L^2([0,1])\), identifying a.e.-equal functions, with
\(\langle f,g\rangle=\int_0^1 f\overline g\). The sine system
\(\phi_n(x)=\sqrt2\sin(n\pi x)\), \(n\ge1\), is a complete orthonormal
system. Define \(s_N=\sum_{n=1}^N n^{-1}\phi_n\). Then
\[
\|s_M-s_N\|_2^2=\sum_{n=N+1}^M\frac1{n^2}\longrightarrow0,
\qquad \|s_N\|_2^2=\sum_{n=1}^N\frac1{n^2}.
\]
Completeness of \(L^2\) gives \(s_N\to f\) in \(L^2\), and continuity of
\(g\mapsto\langle g,\phi_n\rangle\) gives
\(\langle f,\phi_n\rangle=1/n\). Completeness of the **sine system**
additionally gives uniqueness of \(f\) from these coefficients and Parseval:
\[
\|f\|_2^2=\sum_{n\ge1}1/n^2=\pi^2/6,
\qquad\|f\|_2=\pi/\sqrt6.
\]
For a noncomplete orthonormal family, coefficients alone do not determine the
orthogonal-complement component.

A counterexample distinguishing pointwise convergence from mean-square
convergence is \(u_n(x)=\sqrt n\,\mathbf1_{[0,1/n]}(x)\):
\(u_n(x)\to0\) for every \(x>0\), but \(\|u_n\|_2=1\) for all \(n\).

**Completeness sketch (finite-measure interval):** from \(L^2\)-Cauchy
\(f_n\), choose a subsequence \(f_{n_k}\) such that
\(\|f_{n_{k+1}}-f_{n_k}\|_2\le2^{-k}\). Write the differences \(g_k\).
Since \(\sum_k\|g_k\|_1\le\sum_k\|g_k\|_2<\infty\), the
pointwise sum \(\sum_k|g_k(x)|\) is finite a.e. The partial sums
\(|f_{n_1}|+\sum_{k=1}^{N}|g_k|\) have uniformly bounded \(L^2\) norms
by Minkowski. Fatou's lemma gives an \(L^2\) dominating limit; hence
\(f=f_{n_1}+\sum_k g_k\in L^2\) and \(\|f-f_{n_K}\|_2\le
\sum_{k\ge K}2^{-k}\to0\). Cauchyness upgrades convergence to the full
sequence. The construction is not a proof of uniform or pointwise convergence
for the original entire sequence.

Finite-support sequences with the \(\ell^2\) norm supply an incomplete
pre-Hilbert space: \((1,1/2,\ldots,1/N,0,0,\ldots)\) is Cauchy but its
\(\ell^2\) limit is not finitely supported. This cautions against transferring
Hilbert-space statements to arbitrary inner-product spaces.

Historical anchors: Fischer's notes in *Comptes rendus* **144** (1907),
1022–1024 and 1148–1151; Frigyes Riesz, *Sur les systèmes orthogonaux de
fonctions*, **144** (1907), 615–619. For the distinct historical formulations
and their abstract consequences, see John Horváth, *On the Riesz–Fischer theorem*.

### III. Positive matrices and the Hadamard–Fischer inequality

For real/complex positive definite Hermitian block matrix
\[
G=\begin{bmatrix}A&B\\B^*&D\end{bmatrix}>0,
\qquad A>0,\quad D>0,
\]
block Gaussian elimination yields
\[
\det G=\det A\,\det(D-B^*A^{-1}B).
\]
Since \(0<D-B^*A^{-1}B\le D\), determinant monotonicity among positive
definite matrices gives \(\det G\le\det A\det D\). Equality forces
\(B=0\). Example: \(G=\begin{bmatrix}2&1\\1&3\end{bmatrix}\)
is positive definite and \(\det G=5<6=\det(2)\det(3)\).
For Gram matrices this is a block-volume statement. Fischer's 1908 theorem
extends Hadamard's inequality beyond individual diagonal entries.

### IV. Context and source distinctions

- The 1905 Fischer paper concerns finite-dimensional real quadratic forms;
  Courant's 1920 work concerns eigenvalue problems of mathematical physics.
- The Riesz and Fischer papers appeared separately in 1907. They provide
  different mathematical routes into what is now presented as Hilbert-space
  completeness and coordinate realization. Avoid collapsing the exact
  historical formulations into an unsupported claim of abstract equivalence.
- Emmy Noether credited Fischer for an intellectual impulse toward abstract
  algebra. This records influence without claiming he authored her theorems.
- Fischer was forced into retirement at Cologne in 1938 because of his
  partial Jewish ancestry. The Erlangen faculty register dates his retirement
  to October 1, 1938, for political reasons, and his resumption of teaching
  to winter 1945–46. Some short biographies simply list "retired 1938";
  this is insufficient context. No claims are made about undocumented private
  conduct under the regime.

## Reading notes (non-spoken)

Biographical and scholarly sources below distinguish the individual historical
claims from later mathematical formulations. The 1905, 1907, and 1908 publication
records are treated separately, with Noether's acknowledgment and the history of
1938 supported by specialist sources. See `metadata/007000.json` for the
identified reading set and `metadata/sources.json` for persistent source URLs.
