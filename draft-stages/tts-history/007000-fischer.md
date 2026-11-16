# 007000 — Ernst Fischer I: Vienna, Brünn, and the problem of mathematical existence

**Track:** History · People and ideas. **Theme:** Vienna, mathematical education, Brünn, the beginnings of modern spectral and function-space analysis. **Background:** elementary linear algebra and integration; examples are explained in the narration.

<!-- BEGIN SPOKEN LECTURE -->

# Ernst Fischer I: Vienna, Brünn, and the problem of mathematical existence

## A Vienna household and a mathematical education

In July eighteen seventy-five, Ernst Sigismund Fischer was born in Vienna, capital of an empire whose cities were linked by universities, railway lines, professional societies, and several languages of scholarship. He grew up in a household associated with the city's musical profession. His father, Jacob Fischer, taught at the Vienna Academy and composed music. His mother, Emma Grädener, was the daughter of the composer Karl Grädener; another member of the family, Hermann Grädener, also pursued music professionally. There is a temptation to make this a charming origin story for Fischer's later work on Fourier series. Nothing in the available record establishes that childhood music suggested his mathematical investigations. What the family history establishes is the setting he came from: a serious professional household in which creative work and teaching were ordinary occupations.

In eighteen ninety-four Fischer entered the University of Vienna. The city was an important cultural capital, but Vienna's mathematical teaching was also part of a larger network of German-language universities. Fischer studied with Franz Mertens and Leopold Gegenbauer, and completed his doctorate in eighteen ninety-nine. His work did not remain confined to the university where he earned the degree. After a year in Berlin he continued his mathematical formation in Zürich and Göttingen, encountering the research of Hermann Minkowski. Those moves mattered: what counted as an important problem could change from one university and teacher to another. The young researcher was learning to work across mathematical traditions rather than settling immediately into a single specialization.

In nineteen-oh-two Fischer joined the German Technical University in Brünn, in the Austro-Hungarian lands, now Brno in the Czech Republic. He served as an assistant to Emil Waelsch. A technical university trained engineers and other professionals, but its mathematicians also developed research in geometry, algebra, and analysis. The job was not yet the secure senior professorship that a later reader might imagine. Fischer qualified to teach independently in nineteen-oh-four, became an extraordinary professor in nineteen ten, and only in nineteen eleven moved on to a full professorship at Erlangen. Before that promotion, some of the work for which he is best remembered had already appeared.

Brünn was not Göttingen or Paris, yet Fischer's publications joined a Europe-wide discussion. In nineteen-oh-five he published work on real quadratic forms. Two years later his French-language notes in the proceedings of the Paris Academy treated convergence in the mean and the problem of reconstructing a function from orthogonal coefficients. In nineteen-oh-eight he returned to positive quadratic forms through a determinant inequality. One should not imagine a researcher looking at a modern textbook chapter called functional analysis and choosing which theorem to add. The discipline's familiar organizing language was still being assembled. Researchers argued about which functions existed, what it meant for approximations to converge, and which identities remained valid when a finite calculation became infinite.

Fischer's early papers also belong to the history of scholarly credit. The variational characterization of eigenvalues now bears the names of Courant and Fischer, although Fischer's finite-dimensional contribution preceded Courant's treatment of physical eigenvalue problems. The theorem on square-integrable Fourier data bears the names of Riesz and Fischer, whose publications in nineteen-oh-seven approached related questions by different routes. An eponym is a useful pointer, but it cannot tell us what either mathematician knew when he wrote, or make independently published arguments a single collaboration.

At this point, before following Fischer to Erlangen, we can examine what the papers asked. The mathematical sections that follow use modern terminology and simple examples to explain problems his work helped solve. The examples are not stories of actual calculations performed at his desk in Brünn. They help us understand why a mathematical existence theorem could become an event in the history of ideas.

## A numerical calculation is not yet a mathematical object

A complicated musical note can be described by the strengths of its harmonics. Measure the first, the second, the third, and so on. Each measurement produces a number, and the list is infinite. Even if the individual numbers grow smaller, how can you be sure that all those numbers describe an actual sound? You might be able to write down every finite partial reconstruction while never obtaining a legitimate limiting function. A recipe that works for the first thousand tones must still survive the transition to infinitely many tones.

Now imagine a different problem: you have a symmetric matrix with a hundred eigenvalues. The largest and smallest have an immediate characterization through the Rayleigh quotient, the energy of a unit vector. But how could you identify the forty-third eigenvalue without first finding forty-two eigenvectors? Is there a geometric property that makes this number unavoidable, regardless of which trial subspaces you examine?

These sound like different questions. One concerns the existence of an infinite sum, the other the ordering of finitely many spectral values. Both depend on the geometry of a space of possible solutions. Both ask whether numbers extracted from a calculation truly correspond to an object in that space. And both were subjects of work by Ernst Sigismund Fischer, an Austrian mathematician born in Vienna in 1875.

Fischer's name survives in two major theorems, and there is a third inequality worth including in the story. The Courant–Fischer principle characterizes the eigenvalues of a symmetric matrix by choosing subspaces and optimizing a quotient. The Riesz–Fischer theorem concerns square-integrable functions, square-summable coordinates, and the existence of limits. A determinant inequality due to Fischer measures how correlations between blocks reduce the determinant of a positive matrix. The three results belong to a time when mathematicians were learning to think of functions, matrices, and infinite sequences as members of geometric spaces.

Our mathematical question will be simple enough to hold in mind throughout: when does a finite calculation give reliable information about something larger than the calculation itself? We will approach it first through a three-dimensional matrix and then through infinitely many functions. The recurring lesson comes from the proofs, not from an analogy. Geometry tells us what finite approximations must do. Completeness tells us when an infinite limiting object exists.

## The problem of a middle eigenvalue

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

In 1907, while Fischer was working in Brünn, Riesz was teaching in Hungary and visiting Göttingen. Their closely related findings took shape independently and appeared within the same season. The papers did not come from a joint laboratory or a planned two-author project. That matters because the shared theorem name now makes their work look like a single event. In fact it belonged to a mathematical conversation spreading across European cities: new integration theory, infinite orthogonal systems, and questions about how a sequence of approximations could converge to a genuine function. Fischer's own phrase, convergence in the mean, is a sign of how he expressed that problem.

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

The important historical distinction is that the papers did not solve every question later associated with Hilbert spaces. They made precise a particular passage from finite numerical data and approximate functions to a completed space of possible answers. That mattered in Brünn in nineteen-oh-seven, and it would matter still more to the generation that learned to treat integral equations, quantum states, and spectral measurements in a common language. Fischer's next appointment would reveal another side of his mathematics: an interest in algebra, and an important intellectual connection with Emmy Noether.

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

### Portrait readings (non-spoken)

- Ernst Sigismund Fischer, MacTutor: https://mathshistory.st-andrews.ac.uk/Biographies/Fischer/
- Fischer, *Neue Deutsche Biographie*: https://www.deutsche-biographie.de/sfz19606.html
- John Horváth, *On the Riesz–Fischer theorem* (original-source analysis): https://nuhag-old.univie.ac.at/FEICOURS/ws0506/Riesz-Fisher.pdf
- Ernst Fischer, Wikipedia orientation: https://en.wikipedia.org/wiki/Ernst_Sigismund_Fischer

The historical record distinguishes his 1905 quadratic-form theorem, two 1907 mean-convergence notes, and 1908 determinant work. The worked matrices and Fourier examples in the spoken text are modern pedagogical reconstructions.
