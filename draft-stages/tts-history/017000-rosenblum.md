# 017000 — Marvin Rosenblum: How does separating two spectra allow an operator equation to be solved?

**Track:** History · People and ideas. **Theme:** Marvin Rosenblum, continuous-spectrum perturbations, Sylvester equations, normal operators, Toeplitz theory, and the mathematical life of a teacher. **Background:** elementary matrices, eigenvalues, and norms; all operator-theoretic terms are introduced in the narration.

<!-- BEGIN SPOKEN LECTURE -->

# Marvin Rosenblum: How does separating two spectra allow an operator equation to be solved?

Imagine that you have calculated how a system behaves in two separate groups of directions. You know the action of one matrix on the first group and another matrix on the second. Then someone asks what happens when the groups are coupled. The unknown is not a number or even a vector. It is a whole matrix describing how one group responds to the other.

Here is an equation for that unknown. Multiply the matrix X on the left by B. Multiply it on the right by A. Subtract the second result from the first. The answer is a given matrix Q. In symbols this is usually written B X minus X A equals Q.

That looks like a minor rearrangement of a familiar equation. But its behavior changes dramatically with the positions of the eigenvalues of A and B. When the two sets of eigenvalues meet, information can be lost. When they are separated, the equation has a unique solution, even when the matrices are replaced by bounded operators on infinite-dimensional spaces. The way we recover that solution is one of the cleanest meetings between linear algebra and complex analysis.

Marvin Rosenblum explored this question in a nineteen fifty-six paper. But it would be a mistake to make his life a footnote to that one equation. His earlier research concerned the continuous spectrum of a self-adjoint operator: the part that behaves more like an entire band of frequencies than a list of isolated notes. His work helped establish what is now called the Kato–Rosenblum theorem. He later investigated Toeplitz operators, gave an elegant proof about operators that intertwine normal transformations, and collaborated on books linking complex function theory with operators. For forty-five years he taught at the University of Virginia.

Our main calculation will explain how spectral separation solves an operator equation. His other work will deepen the question: when an operator changes, which parts of its structure can survive?

## The first denominator

Start with the simplest possible case. Both A and B are single numbers. Let A be two, let B be five, and suppose Q is twelve. Our equation becomes five times X minus two times X equals twelve. Three X equals twelve. So X is four.

The denominator is five minus two. If B were also two, the left side would be zero for every X. With Q equal to twelve there would be no solution. With Q equal to zero there would be infinitely many. Either way uniqueness disappears exactly when the two spectral values coincide.

Now let A have two eigenvalues, negative one and positive one. Let B have eigenvalues zero and two. Assume both matrices are diagonal in the coordinates we are using. The unknown X has four entries. Multiplying on the left by B scales each row. Multiplying on the right by A scales each column. Consequently each entry solves its own small equation. The entry in row i and column j satisfies B's i-th eigenvalue minus A's j-th eigenvalue, times the unknown entry, equals the corresponding entry of Q.

Listen to the four denominators. From zero minus negative one we get one. From zero minus positive one we get negative one. From two minus negative one we get three. And from two minus positive one we get one. None is zero. Each entry of X can therefore be recovered by dividing by its own denominator.

This finite calculation already raises three distinct questions. Is the answer unique? How large can the answer be if Q is small? And can we find it without diagonalizing both operators? The first question requires the denominators to stay away from zero. The second depends on what we mean by the size of a matrix. The third demands a method that survives in infinite dimensions, where an operator may have no basis of eigenvectors at all.

In the diagonal calculation A and B act on different sides. We are not requiring a common eigenbasis for them. Their coordinate systems can even belong to different Hilbert spaces, with X carrying vectors from the A-space into the B-space. This flexibility is precisely why the equation appears so frequently in perturbation theory.

## From Brooklyn to Berkeley

Marvin Rosenblum was born in Brooklyn, New York, in nineteen twenty-six. His early university training included a bachelor of science in electrical engineering. He went on to the University of California at Berkeley, earning advanced degrees in mathematics, including his doctorate in nineteen fifty-five. This move from engineering into mathematical analysis is documented in the University of Virginia's later account of his career.

The subject of his Berkeley thesis was the perturbation of continuous spectra. It is worth hearing that title carefully. A perturbation is a change to an operator, often an added term assumed small in a particular sense. The spectrum generalizes the eigenvalues of a matrix. In infinite dimensions it may contain continuous ranges even when no vector has any one of those values as an eigenvalue. Rosenblum was studying how such a range behaves under a change of the governing operator.

His doctoral adviser was František Wolf. The mathematician Barry Simon later reconstructed a useful piece of this history. Rosenblum submitted his thesis in March nineteen fifty-five. A Berkeley technical report circulated in December of that year, before the result appeared in a journal. That timing becomes important when we try to understand the origins of a famous perturbation theorem.

When he arrived at Virginia in nineteen fifty-five, he was starting a career that would keep him in one department for forty-five years. Such continuity meant that later students could encounter him as a teacher, doctoral adviser, and senior colleague, not merely as the author of a spectral theorem. An institutional tribute after his death describes his generosity and a habit of treating people with respect and good humor. Those recollections provide a different view of the same scholar whose papers are concise and technical.

Charlottesville became the center of his academic career. He was a member of the Institute for Advanced Study in Princeton from September nineteen fifty-nine to August nineteen sixty, but the main institutional continuity was Virginia. He eventually served as department chair, became a Commonwealth Professor, and continued to supervise research students. Those are facts we can document without inventing a story about what motivated every turn of his work.

The questions he pursued were closely connected. An operator equation asks whether spectral information is enough to recover an unknown transformation. Perturbation theory asks whether spectral information survives when a known transformation changes. Both force us to look beyond a short list of eigenvalues.

## What a continuous spectrum means

Consider an operator that acts on functions defined between zero and one. It takes a function and multiplies its value at each point by the coordinate of that point. If a function is called f, its new value at x is x times f of x. The operator is self-adjoint on the ordinary square-integrable function space. Self-adjoint is the infinite-dimensional analogue of a real symmetric matrix: the inner product of A f with g equals the inner product of f with A g.

The possible spectral values of this multiplication operator fill the interval from zero to one. Yet there is no nonzero square-integrable function concentrated at exactly one point. So the operator has a full interval of spectrum without an ordinary eigenvector for every point in the interval. Its spectral mass is spread continuously along the interval.

For a self-adjoint operator, a spectral measure tells us how much of a vector's energy lies in any chosen interval of spectral values. The measure can have atoms, corresponding to eigenvectors; it can be absolutely continuous, meaning that its mass is described by an integrable density relative to ordinary length on the real line; and it can also have a singular continuous part. The distinctions are genuinely infinite-dimensional. A finite symmetric matrix has only point spectrum.

The phrase absolutely continuous deserves an example. If we start with a function f in our multiplication model, the spectral mass between a and b is the integral of the squared magnitude of f over that interval. When an interval becomes short, its contribution becomes small in the manner governed by an integrable density. If instead the operator were diagonal with an eigenvalue at one half, a vector along that eigendirection would place a positive mass at a single point. Such a point has zero length, so that mass cannot be described by an ordinary density.

For Rosenblum, this was a problem with consequences beyond the choice of one basis. In an engineering model, a small change to a system may move resonances, but what happens to the part of the dynamics carried by a whole band of frequencies? His electrical-engineering background makes this comparison accessible, though his dissertation investigated the abstract spectral question. It is the distinction between a whole band of frequencies and a list of isolated resonances that needs explaining.

Rosenblum was concerned with how the absolutely continuous part changes after a perturbation. To say that two such parts are unitarily equivalent means that there is a length-preserving invertible transformation carrying one to the other and respecting their operators. It is stronger than saying merely that their spectra cover the same interval: it preserves the multiplicity and operator structure of the absolutely continuous component.

A natural guess would be that a tiny change in operator norm preserves this structure. That guess is false in general. Even perturbations compact enough to have finite sums of squared singular values can destroy absolutely continuous behavior. The decisive condition in the theorem associated with Kato and Rosenblum is stricter and has its own mathematical meaning.

## Trace class and the preservation theorem

For a finite matrix, take its singular values and add them. Singular values are the nonnegative stretching factors of a matrix, including the effects of directions that the matrix rotates. In finite dimensions their sum is called the trace norm. A rank-one matrix has only one nonzero singular value, so its trace norm is exactly that singular value.

For a compact operator on an infinite-dimensional Hilbert space, there may be infinitely many singular values tending to zero. We say it is trace class when the sum of those singular values converges. One can think of trace class as a strong control over the cumulative size of the perturbation. Each term can be tiny while there are infinitely many of them, and the convergence of the full sum is what the theorem needs.

Here is the result in its familiar general form. Take two self-adjoint operators on the same Hilbert space. Suppose their difference is trace class. Then their absolutely continuous parts are unitarily equivalent. More precisely, suitable wave operators exist and identify those parts, including their spectral multiplicities. The conclusion makes no promise that every individual eigenvalue stays put or that the singular continuous parts agree.

Rosenblum's early work established a special case for operators with purely absolutely continuous spectrum. Kato proved the general trace-class version in nineteen fifty-seven. We should be precise about the sequence. Rosenblum's result was present in his nineteen fifty-five thesis, initially with extra technical conditions, and the version that became his nineteen fifty-seven Pacific Journal paper was already circulating as a nineteen fifty-five technical report. Kato's work developed its own route, including results on finite-rank perturbations, and then obtained the general theorem.

Barry Simon's historical study traces the exchange closely. Kato had spent time at Berkeley while Rosenblum was a graduate student. Kato later referred to Rosenblum's work and acknowledged receiving a technical report. Simon describes the evidence for the mathematical influence without assuming that one researcher simply copied the other. The chronology explains why the compound name Kato–Rosenblum can conceal the independent sequence of questions and improvements that produced the theorem.

What makes trace class the right boundary? Imagine trying to weaken the hypothesis from summable singular values to square-summable singular values. These latter operators are called Hilbert–Schmidt operators. Square summability permits longer tails than summability. There are perturbations with arbitrarily small Hilbert–Schmidt norm that turn a self-adjoint operator into one with pure point spectrum. Thus the broad absolutely continuous preservation theorem cannot survive such a replacement. It is the particular way infinitely many small changes accumulate that determines what is stable.

This was a result about spectral structure, not a guarantee that the entire operator remains unchanged. It tells us there is an equivalence of one specified part under one specified class of perturbations. That exactness is why the result can be used: a theorem that claimed all spectral features were preserved would be false.

## Returning to the equation with an unknown operator

In his nineteen fifty-six Duke Mathematical Journal paper, Rosenblum approached the equation B X minus X A equals Q in the setting of bounded operators. Bounded means that the operator never stretches a unit vector by more than a fixed finite amount. The operators A and B need not be self-adjoint. Their spectra may be curves, disks, or complicated sets in the complex plane.

The theorem gives a surprisingly concise condition. If the spectrum of A and the spectrum of B are disjoint, then for each bounded Q there is one and only one bounded solution X. This applies to bounded operators acting on suitable complex Banach spaces, and in particular on Hilbert spaces. The spectrum of an operator is the set of complex numbers where subtracting that number times the identity does not leave an invertible bounded operator.

In a finite diagonal example, disjointness means every denominator B-eigenvalue minus A-eigenvalue is nonzero. But in an infinite-dimensional space there may be no diagonal decomposition. We need a substitute for entrywise division.

The substitute is the resolvent. Given an operator A and a complex number z outside its spectrum, the resolvent is the inverse of z times the identity minus A. Think of it as a response to a forcing term at a chosen complex parameter. Far from the spectrum the inverse exists; at the spectrum it cannot be used in that bounded way. As z moves through the resolvent set, this inverse changes analytically. That means it can be integrated around curves using the rules of complex analysis.

For a concrete picture, put a point for each eigenvalue of A on a sheet of paper and another for each eigenvalue of B. Draw a closed curve around all of A's points, but none of B's. The curve is oriented counterclockwise. The disjointness of the spectra lets us find such a curve in the finite-dimensional case, and a suitable finite collection of curves in the general compact-spectrum setting.

Now place Q between two inverses. On its left put the inverse of B minus z times the identity. On its right put the inverse of z times the identity minus A. Integrate this whole operator-valued expression around the curve, and divide by two pi times the imaginary unit. That integral is X.

There is a reason for the different signs. They make the scalar example come out correctly. Let A be two, B be five, and Q be twelve. A contour about two sees a simple pole from the factor one over z minus two. The other factor, one over five minus z, is perfectly regular there and takes the value one third. The contour integral therefore returns twelve divided by three, which is four. The integral has performed spectral division without calling on eigenvectors.

The heart of the proof uses an identity simpler than the formula looks. Multiply the integral by B on the left and subtract the integral multiplied by A on the right. In the integrand, write B as B minus z plus z, and write A as z minus the quantity z minus A. The terms with z cancel. What remains is a resolvent involving A alone, plus a resolvent involving B alone, both multiplied appropriately by Q.

When we integrate, the A-resolvent contributes the identity operator, because our contour encloses A's whole spectrum. The B-resolvent contributes zero, because no part of B's spectrum lies inside. The result is Q. That proves our integral solves the equation. To get uniqueness, suppose Y solves the same equation with Q equal to zero. Then B times Y equals Y times A. This identity also makes the resolvent of B, multiplied by Y, equal to Y multiplied by the resolvent of A, wherever both resolvents are defined. Integrate around the same contour. The B side has no spectral points inside and contributes zero. The A side contributes Y, because the contour encloses all of A's spectrum. So Y must be zero. There can be only one solution.

Notice how much work the complex plane has done. We never requested eigenvectors. The proof treats nonnormal matrices and infinite-dimensional bounded operators, even when a neat orthonormal diagonalization is unavailable. The cost is that we must keep track of resolvent norms and the position of the contour, not just distances between eigenvalues.

## Separation is enough for a solution, but how good is the estimate?

We can make the distinction precise by testing two norms. The Hilbert–Schmidt norm of a finite matrix is the square root of the sum of the squares of the magnitudes of all its entries. The ordinary operator norm asks instead for the greatest length produced from any input vector of length one. These norms answer different questions.

Return to our diagonal pair A with eigenvalues negative one and one, and B with eigenvalues zero and two. The smallest difference in absolute value between any B-value and any A-value is one. Every entry of X is an entry of Q divided by one of those differences. Therefore, when we square the entries and sum, the Hilbert–Schmidt norm of X cannot exceed the Hilbert–Schmidt norm of Q. This is a clean constant-one estimate for that norm.

It is tempting to announce the same inequality for the operator norm. But the operator norm is sensitive to correlations among matrix entries. Dividing different entries by different signed numbers can change how contributions reinforce or cancel. A coefficientwise bound alone is not enough.

We can hear the failure with a two-by-two example. Keep the same A and B. Choose Q to be one over the square root of two times the matrix whose first row is one, one, and whose second row is negative one, one. This Q is a rotation, so its operator norm is exactly one. When we solve the equation entry by entry, the first row of X becomes one, negative one, divided by the square root of two. The second row becomes negative one third, one, again divided by the square root of two.

Compute the largest stretching factor of that X. It is approximately one point two one seven. The spectra are separated by at least one, Q has norm one, and yet X has norm greater than one. A naive bound of Q's operator norm divided by the minimum spectral distance would have predicted at most one. The prediction fails, even with perfectly self-adjoint diagonal matrices.

That does not mean all operator-norm estimates fail. If the entire spectrum of A lies below the entire spectrum of B on the real line, a stronger geometric condition holds. The two sets are ordered. Then a remarkably simple integral gives the correct constant-one estimate. We should distinguish this ordered situation from disjoint, interlaced spectral sets.

## An integral over time

Assume A and B are bounded self-adjoint operators. Assume every spectral value of A is at most a number a, every spectral value of B is at least a number b, and b is greater than a. Call the positive difference b minus a the gap.

For positive time t, take an exponential of negative t times B, multiply by Q, and then multiply by an exponential of positive t times A. Add these expressions over all times from zero to infinity. The result is X.

Why should this converge? Along a spectral direction of B, the first exponential contributes decay determined by B's spectral value. Along a direction of A, the other contributes growth determined by A's spectral value. Since every B-value exceeds every A-value by at least the gap, the combined effect decays at least as fast as the exponential of negative t times the gap.

That gives a direct estimate. The norm of the integrand is at most Q's norm times that decaying exponential. Integrate the exponential from zero to infinity and you get one divided by the gap. Thus the norm of X is at most Q's norm divided by the gap.

We can verify the equation by differentiating. The time derivative of the integrand is the negative of B times that integrand, plus that integrand times A. In other words, it is the negative of exactly the combination B X minus X A, before integration. Integrate the derivative from zero to infinity. The expression vanishes at infinity and equals Q at time zero. Rearranging gives the required equation.

The scalar example is once again transparent. If A is two and B is five, the integrand is twelve times the exponential of negative three t. Its integral is twelve divided by three, exactly four. The contour integral and the time integral produce the same answer, but they reveal different structures. The contour method exploits separation in the complex plane. The time integral exploits a common ordering of two real spectral sets.

Now revisit the interlaced example. A has eigenvalues negative one and positive one; B has zero and two. Some differences are positive, one is negative. There is no single positive time direction in which all terms decay under the formula we just used. We cannot apply the ordered-spectrum proof there. The contour method still works, because the two spectral sets remain disjoint. The gap condition and the choice of inverse representation are related but distinct pieces of the analysis.

## A second obstruction: nonnormality

It would be convenient if the minimum distance between two spectra always controlled the norm of the inverse Sylvester map. Our previous example already showed that the best constant may exceed one. For nonnormal operators the situation can be much more severe.

Take A to be a two-by-two matrix whose diagonal entries are zero, whose lower-left entry is zero, and whose upper-right entry is a large number M. Take B to be the identity matrix. Both eigenvalues of A are zero, and both eigenvalues of B are one. The spectral distance is exactly one, regardless of how large M becomes.

Let Q also be the identity. Our equation becomes X minus X A equals the identity. We can factor the left side as X times the identity minus A. Since A squared is zero, the inverse of the identity minus A is simply the identity plus A. Thus X equals the identity plus A.

Feed X the unit vector pointing along the second coordinate. It sends that vector to a vector with components M and one. Its length is the square root of M squared plus one. Make M a thousand and the solution amplifies a unit input by more than a thousand, despite a fixed spectral separation of one. The eigenvalues alone cannot see this effect.

A nonnormal matrix can have resolvents that are large even far from its spectrum. The word pseudospectrum is used for the associated sensitivity, although we do not need a formal theory of pseudospectra to understand this example. The point is simpler: a theorem about existence from disjoint spectra does not automatically give a bound controlled only by spectral distance. If you need quantitative stability, the structure of the operators and the norm in use both enter the answer.

## Rosenblum and the geometry of intertwining

The equation B X minus X A equals Q has a special case with Q equal to zero. Then B X equals X A. We say that X intertwines A with B. Every vector transformed by A and then carried across by X agrees with the result of crossing by X first and then applying B. It expresses a structural relationship rather than an approximation error.

For normal operators there is a related theorem, historically associated with Fuglede and Putnam. Normal means that an operator commutes with its adjoint; self-adjoint and unitary operators are both examples. Suppose A and B are bounded normal operators and B X equals X A. Then B's adjoint times X also equals X times A's adjoint.

Try a small example. If A and B are diagonal matrices with complex entries, an entry of X can be nonzero only when the corresponding diagonal entries match. Conjugating those entries preserves equality. So the same X also intertwines the adjoints. The theorem says this remains true for all bounded normal operators, without requiring a simultaneous diagonal representation.

In nineteen fifty-eight Rosenblum published a notably economical proof of this fact. The idea brings us back to complex analysis, but this time through an entire function rather than a contour integral. Build an operator-valued function of a complex variable using exponentials of B's adjoint, X, and exponentials of the negative of A's adjoint. Because X already intertwines A and B, and because A and B are normal, the exponentials can be rearranged so that the resulting function is bounded for every complex value of its argument.

A version of Liouville's theorem says that an entire bounded complex-valued function must be constant. The same principle applies to a bounded entire function taking values in a Banach space. The operator-valued function therefore stays equal to its value at zero, which is X. Differentiate at zero, and the desired adjoint-intertwining identity appears.

This is a beautiful example of technique moving between subjects. A relation involving algebraic multiplication becomes a statement about analytic functions. Entire-function rigidity completes a proof that might otherwise look like a difficult exercise in operator matrix entries. Rosenblum's short paper remains a standard example of how complex analysis can simplify an operator-theoretic argument.

## Beyond bounded operators

The nineteen fifty-six solvability theorem has a limitation that was visible in its hypotheses. It concerns bounded operators with disjoint spectra. In applications to differential equations and mathematical physics, self-adjoint operators are frequently unbounded. The multiplication operator that sends f of x to x times f of x on the whole real line is an example. Defining products with an unbounded operator requires care about which vectors belong to its domain.

In nineteen sixty-nine Rosenblum returned to the operator equation with self-adjoint A and B that could be unbounded. Here a bounded solution X must send vectors from the domain of A into the domain of B if the expression B X minus X A is to make sense on that domain. It is no longer enough to write down the formal matrix equation.

Rosenblum used a perturbation procedure. Shift B slightly upward into the complex plane and shift A slightly downward. For a positive parameter y, the shifted operators B plus i y times the identity and A minus i y times the identity have disjoint spectra. Their operator equation has a resolvent-based solution. Then examine what happens as y approaches zero.

The difficulty is that a family of solutions to the shifted equations can become arbitrarily large. If the norms remain bounded, weak compactness provides a way to extract a limiting solution. A weak limit means that the scalar inner products against test vectors converge, even if there is no convergence in operator norm. This allows the method to reach cases where the original spectra overlap and the simple disjoint-spectrum theorem cannot be applied directly.

The important step is the control of the regularized solutions, not a claim that every overlapping-spectrum equation is solvable. The method turns a difficult existence question into an estimate for a family of better-behaved equations. That logic is common in analysis: introduce a small parameter, solve a regularized problem, obtain uniform control, and then pass to a limit.

## Spectral bands, Toeplitz matrices, and analytic functions

Rosenblum's research did not remain within the Sylvester equation. Starting in the late nineteen fifties, he studied Toeplitz operators. A Toeplitz matrix has constant entries along each diagonal: moving one row down and one column right leaves the entry unchanged. Such matrices arise naturally from Fourier coefficients of a function on the circle.

Imagine recording a periodic signal and computing its Fourier coefficients. Place those coefficients into an infinite matrix so that the entry depends only on the difference between row and column numbers. That is a Toeplitz matrix. The finite sections resemble structured numerical matrices, but the infinite operator carries information about the underlying signal and its spectral distribution.

Take the simplest example with zeros on the diagonal and ones immediately above and below it. This corresponds to the trigonometric symbol two times the cosine of an angle. On the space of square-summable sequences indexed by nonnegative integers, the operator is a discrete version of coupling neighboring sites along a half-line. Its spectrum fills the interval from negative two to positive two. A useful way to recognize its continuous behavior is to compare the recurrence for its generalized eigenvectors with the trigonometric identities satisfied by sine waves.

The operator's spectral values fill an interval, but ordinary square-summable eigenvectors do not account for the whole band. This brings us directly back to the continuous-spectrum problem that occupied Rosenblum in his thesis. His nineteen sixty paper, *The Absolute Continuity of Toeplitz's Matrices*, investigated this question for a broad class of real symbols. Later papers in the nineteen sixties developed concrete spectral analysis for self-adjoint Toeplitz operators.

In a Toeplitz problem the matrix representation is available but often inconvenient. The analytic symbol on the unit circle can offer a better route. The symbol controls Fourier coefficients; those coefficients form the operator; and the operator's spectral behavior reflects properties of the function. One has to prove the correspondence with appropriate hypotheses, rather than merely reading eigenvalues off a symbol as if the matrix were finite.

He also worked on singular integral operators, which turn a function into another through an integral whose kernel may become singular, and on questions involving analytic functions. The shift from one kind of operator to another was mathematically continuous. In each case, operator structure is encoded in a function or a transform, and complex analysis makes that encoding useful.

The turn toward Hardy spaces also meant a sustained collaboration with James Rovnyak, rather than a solitary excursion into another subject. They worked together on books whose organization brought difficult function theory and operator theory within reach of graduate readers. Rosenblum's lectures at Virginia formed part of the background to the later volume, linking his writing to a department where students had heard the material develop in the classroom.

With James Rovnyak he wrote *Hardy Classes and Operator Theory*, published in nineteen eighty-five. Hardy classes are families of analytic functions controlled by the size of their boundary values. They supply natural spaces for shift operators, Toeplitz operators, and interpolation problems. A shift takes a sequence and moves its entries one position; on a Hardy space of analytic functions, multiplication by the variable performs the analogous job.

Why is the shift worth a whole theory? Many operators can be studied through models built from shifts, much as a complicated signal can be reconstructed from simpler frequency components. The Hardy-space setting converts geometric questions about invariant subspaces into analytic questions about functions and factorization. An interpolation problem then asks for an analytic function with prescribed values while obeying a bound. Operator theory and complex analysis meet again in a more systematic form.

Rosenblum and Rovnyak later published *Topics in Hardy Classes and Univalent Functions* in nineteen ninety-four. Its foundations came from lectures given at Virginia over the preceding decades. The book develops harmonic and subharmonic functions, Hardy and Nevanlinna classes, and the theory of one-to-one analytic maps, including the major univalent-function conjectures proved in the nineteen eighties. These were not simply appendices to the nineteen fifty-six Sylvester equation; they show the broader range of a researcher who remained interested in analytic methods for operators and functions.

## Forty-five years at Virginia

Rosenblum's biography also belongs to the history of a mathematics department. He joined the University of Virginia in nineteen fifty-five. He chaired its mathematics department from nineteen sixty-nine to nineteen seventy-three and became Commonwealth Professor in nineteen seventy-eight. University records credit him with directing eighteen doctoral dissertations. He was also an editor of *Integral Equations and Operator Theory*, a journal devoted to the subject that connected so many of his papers.

The surviving institutional accounts emphasize how he worked with people. A former student remembered him as someone who treated others fairly and with grace, intelligence, kindness, and humor. We do not have a transcript of a particular office-hour conversation that would let us dramatize this; the recollection itself is meaningful. It tells us that a student who experienced his mathematical authority also remembered the way Rosenblum exercised it. Advising eighteen dissertations requires sustained attention to the unfinished work of other people, a different kind of mathematical labor from proving a theorem alone.

His membership at the Institute for Advanced Study from nineteen fifty-nine to nineteen sixty coincided with his early work on Toeplitz operators and spectral theory. His later mathematical path included operator equations, function-theoretic models, and collaborations on monographs. He retired from Virginia in May two thousand and died in two thousand three.

His wife, Elizabeth Parker Rosenblum, and their five children were also part of the life remembered in Virginia's account. One son, Mendel, became a computer scientist. The connection between generations later took a tangible institutional form: a gift in memory of a father who had taught and advised at the university for decades.

The University approved a professorship in his name in twenty ten. A gift from his son Mendel Rosenblum and Mendel's wife, Diane Greene, supported the endowment, and the university announced it publicly in twenty eleven. Mendel Rosenblum became a prominent computer scientist and co-founded VMware with Greene and colleagues. That later family connection has an interesting symmetry with Marvin's early electrical-engineering training, but the institutional record does not require us to invent a direct intellectual line between their careers. The concrete connection is the endowment honoring Marvin's scholarship, teaching, and service.

That gift carries the human part of this story into the future. Mendel and Diane could not preserve every office discussion or lecture; they could help a department offer a professorship to another scholar. The memorial is thus about the kind of working life Rosenblum made possible for others.

A university is an institution that transmits mathematics through more than published theorems. It trains students, sustains seminars, builds journals and libraries, and gives researchers decades in which to pursue a connected group of problems. Rosenblum's forty-five years at Virginia are an important part of his mathematical legacy alongside his publications.

## Why the equation keeps returning

Let's finish with the expression that opened this lecture: B times X minus X times A equals Q. We learned first that it is a collection of scalar divisions when the two operators are diagonal. We then replaced those divisions with a resolvent contour, allowing the same equation to be solved for bounded operators without a basis of eigenvectors. We saw that separated spectra provide existence and uniqueness, while good quantitative bounds require attention to the norms and the operator structure.

We found two distinct warnings. Even for self-adjoint operators, interlacing spectra can invalidate a constant-one operator-norm estimate based only on minimum distance, although the analogous Hilbert–Schmidt estimate works for diagonal operators. For nonnormal operators, the spectral distance may remain fixed while the solution becomes arbitrarily large. Those are exact reasons to avoid treating all measures of separation as interchangeable.

The equation also describes a common step in eigenvector perturbation theory. Suppose a vector nearly belongs to a chosen invariant subspace but has a residual component in an unwanted spectral subspace. Projecting the governing equation onto the unwanted directions produces a Sylvester-type equation for the error or for the transformation connecting subspaces. The two spectral sets then determine how a residual can be converted into an angular or operator error. The calculation is the descendant of our very first denominator: B-value minus A-value.

Rosenblum's other results explain why this local calculation fits a larger history. In the preservation of absolutely continuous spectrum, a trace-class perturbation respects a deep part of an operator's structure. In Toeplitz theory, analytic functions describe infinite matrices and their spectral bands. In the Fuglede–Putnam argument, an intertwining relation and normality become an entire bounded function, and complex analysis supplies the conclusion.

All these problems ask what can be recovered or preserved when operators are related. The answers depend on precise hypotheses: disjoint spectra for one theorem, ordered self-adjoint spectra for a sharp time-integral estimate, trace-class difference for preservation of the absolutely continuous component, normality for adjoint intertwining. Their power comes from stating exactly enough to prove a useful conclusion. That was the mathematics Marvin Rosenblum helped develop, and it remains useful wherever a change in an operator must be understood rather than merely computed.

<!-- END SPOKEN LECTURE -->

---

## Mathematical and historical companion (display only)

### 1. The bounded Sylvester equation and the contour sign

Let \(A\in\mathcal B(H_A)\), \(B\in\mathcal B(H_B)\), \(Q\in\mathcal B(H_A,H_B)\) be bounded complex operators, with disjoint compact spectra \(\sigma(A)\cap\sigma(B)=\varnothing\). The Sylvester map
\[
\mathcal S_{B,A}(X)=BX-XA
\]
is invertible on \(\mathcal B(H_A,H_B)\). With \(\Gamma\) a positively oriented cycle enclosing \(\sigma(A)\) and excluding \(\sigma(B)\), use **the fixed convention**
\[
\boxed{X=\frac1{2\pi i}\int_\Gamma (B-zI)^{-1}Q(zI-A)^{-1}\,dz.}
\]
The opposite signs on the two resolvents are intentional. In the scalar case \(A=a\), \(B=b\), the residue is \(Q/(b-a)\). To check the equation, use
\[
B(B-zI)^{-1}=I+z(B-zI)^{-1},\qquad
(zI-A)^{-1}A=z(zI-A)^{-1}-I.
\]
Thus
\[
B[(B-zI)^{-1}Q(zI-A)^{-1}]-[(B-zI)^{-1}Q(zI-A)^{-1}]A
=Q(zI-A)^{-1}+(B-zI)^{-1}Q.
\]
The first contour integral is \(Q\) and the second vanishes. For uniqueness, any \(Y\) with \(BY=YA\) has \((B-zI)^{-1}Y=Y(A-zI)^{-1}\) on the common resolvent set; the two spectral idempotents obtained by integration around \(A\)'s spectrum force \(Y=0\). See Rosenblum (1956) and Rosenblum (1969), §1.

### 2. Diagonal and interlaced examples

For diagonal \(A=\operatorname{diag}(a_j)\), \(B=\operatorname{diag}(b_i)\),
\[
X_{ij}=\frac{Q_{ij}}{b_i-a_j}.
\]
If \(\delta=\min_{i,j}|b_i-a_j|>0\), then \(\|X\|_F\le\delta^{-1}\|Q\|_F\) (and analogously for a Hilbert–Schmidt operator with compatible diagonal bases). This does *not* give the same operator-norm estimate.

For a self-adjoint counterexample to the constant-one operator-norm claim, take
\[
A=\begin{pmatrix}-1&0\\0&1\end{pmatrix},\quad
B=\begin{pmatrix}0&0\\0&2\end{pmatrix},\quad
Q=\frac1{\sqrt2}\begin{pmatrix}1&1\\-1&1\end{pmatrix}.
\]
Here \(\delta=1\), \(\|Q\|_{\rm op}=1\), but
\[
X=\frac1{\sqrt2}\begin{pmatrix}1&-1\\-1/3&1\end{pmatrix},\qquad
\|X\|_{\rm op}=\frac{\sqrt{7+2\sqrt{10}}}{3}\approx1.21676>1.
\]
This is a **counterexample to the specific bound** \(\|X\|_{\rm op}\le\|Q\|_{\rm op}/\delta\) for interlaced self-adjoint spectra, not to solvability and not to all possible spectral-gap bounds.

### 3. Ordered self-adjoint spectra and a sharp bound

Assume \(A=A^*\), \(B=B^*\), \(\sup\sigma(A)\le a<b\le\inf\sigma(B)\), and set \(\delta=b-a>0\). Then
\[
X=\int_0^\infty e^{-tB}Qe^{tA}\,dt,\qquad
\|X\|\le\int_0^\infty e^{-t\delta}\|Q\|dt=\frac{\|Q\|}{\delta}.
\]
Differentiate \(e^{-tB}Qe^{tA}\) and integrate its derivative from \(0\) to \(\infty\) to verify \(BX-XA=Q\). For scalar \((a,b,Q)=(2,5,12)\), \(X=\int_0^\infty 12e^{-3t}dt=4\). This argument requires an ordered real gap; it does not cover interlaced spectra by simply reversing time.

### 4. Nonnormal spectral-gap warning

Set \(A_M=\bigl(\begin{smallmatrix}0&M\\0&0\end{smallmatrix}\bigr)\), \(B=I\), and \(Q=I\). Both spectral sets remain \(\{0\}\) and \(\{1\}\), at distance one. Because \(A_M^2=0\),
\[
X(I-A_M)=I,\qquad X=(I-A_M)^{-1}=I+A_M,
\qquad \|X\|\ge\sqrt{M^2+1}.
\]
Thus the separation of \(\sigma(A_M)\) and \(\sigma(B)\) alone cannot yield a uniform operator-norm bound independent of nonnormality.

### 5. Rosenblum's 1969 extension

The 1969 paper, *The Operator Equation BX−XA=Q with Selfadjoint A and B*, treats possibly unbounded self-adjoint \(A,B\) and bounded \(Q\). A bounded solution \(X\) must respect domains: \(X\mathcal D(A)\subseteq\mathcal D(B)\), and \(BXf-XAf=Qf\) for \(f\in\mathcal D(A)\). The regularized equations
\[
(B+i y I)T_y-T_y(A-i y I)=Q,\qquad y>0,
\]
have separated spectra and unique bounded solutions. Rosenblum proves a bounded-solution criterion in terms of uniform boundedness of \(\{\|T_y\|:y>0\}\), with suitable weak convergence. The spectral shifts are *opposite*; this is an existence criterion, not a promise that arbitrary overlapping-spectrum equations are solvable.

### 6. Fuglede–Putnam, Rosenblum's 1958 analytic proof

For bounded normal \(A,B\), \(BX=XA\) implies \(B^*X=XA^*\). Consider
\[
F(z)=e^{izB^*}Xe^{-izA^*},\qquad z\in\mathbb C.
\]
From \(e^{i\overline z B}X=Xe^{i\overline z A}\), insert the identity \(X=e^{-i\overline z B}Xe^{i\overline z A}\) to get
\[
F(z)=e^{i(zB^*-\overline z B)}X\,e^{i(\overline z A-zA^*)}.
\]
Normality makes the exponent pairs commute. Both factors multiplying \(X\) are unitary, so \(\|F(z)\|=\|X\|\). Banach-valued Liouville gives \(F(z)=X\), hence \(F'(0)=i(B^*X-XA^*)=0\). Cite Rosenblum (1958); acknowledge Fuglede and Putnam for the theorem, Rosenblum for this proof.

### 7. Continuous-spectrum perturbation history

For self-adjoint \(H_0,H_1\), if \(H_1-H_0\) is trace class, the absolutely continuous parts are unitarily equivalent; the corresponding wave operators exist and are complete. This is the general **Kato–Rosenblum theorem**, proved by Kato in 1957 building on a line of research to which Rosenblum made a priority early contribution. Rosenblum's 1955 dissertation and report preceded his 1957 Pacific Journal publication. His result concerned the purely absolutely continuous case, with restrictions in the dissertation formulation. Barry Simon (2019), §13, pp. 24–25, gives detailed chronology and Kato's acknowledgment of Rosenblum's report. Do not assert equality of point or singular-continuous spectra. Nor replace trace class with Hilbert–Schmidt: the Weyl–von Neumann–Kuroda phenomena show the boundary.

### 8. Toeplitz and Hardy-space examples

On \(\ell^2(\mathbb N_0)\), \(T(2\cos\theta)\) has ones on the immediate off-diagonals and zeros elsewhere. It is the half-line Jacobi matrix, with absolutely continuous spectrum on \([-2,2]\) (multiplicity one in this example). Rosenblum (1960) studied absolute continuity of semibounded Toeplitz operators with real symbols; related spectral analyses appeared in 1963 and 1965, and he later coauthored Hardy-space and univalent-function books with James Rovnyak (1985, 1994). The Toeplitz results should be stated with their hypotheses, not as a claim that every self-adjoint Toeplitz-like operator automatically has a.c. spectrum.

### Chronology and sources (non-spoken)

- 1926: Birth in Brooklyn (IAS *Community of Scholars*, p. in author index).
- 1955: Berkeley Ph.D., *Perturbation of the Continuous Spectrum*; adviser František Wolf; UVA appointment. Technical report distributed December 1955 (Simon 2019).
- 1956: *On the Operator Equation BX−XA=Q*, *Duke Mathematical Journal* **23**, 263–269.
- 1957: *Perturbation of the Continuous Spectrum and Unitary Equivalence*, *Pacific Journal of Mathematics* **7**, 997–1010. Kato's trace-class general theorem also appeared in 1957.
- 1958: *On a Theorem of Fuglede and Putnam*, *Journal of the London Mathematical Society* **33**, 376–377.
- 1959–1960: Institute for Advanced Study membership.
- 1960: *The Absolute Continuity of Toeplitz's Matrices*, *Pacific Journal of Mathematics* **10**, 987–996.
- 1965: *A Concrete Spectral Theory for Self-adjoint Toeplitz Operators*, *American Journal of Mathematics* **87**, 709–718.
- 1969: *The Operator Equation BX−XA=Q with Selfadjoint A and B*, *Proceedings of the AMS* **20**, 115–120. UVA department chair 1969–1973.
- 1978: Commonwealth Professorship at Virginia.
- 1985: With James Rovnyak, *Hardy Classes and Operator Theory* (Oxford).
- 1994: With James Rovnyak, *Topics in Hardy Classes and Univalent Functions* (Springer).
- 2000: Retirement from Virginia, later Professor Emeritus.
- 2003: Death. In 2010 the UVA Board of Visitors recorded his career, and a professorship honoring him was funded and announced in 2011.

Source IDs, claim anchors, and URLs are in `metadata/017000.json` and `metadata/sources.json`. The chronology follows the Institute for Advanced Study, UVA Board of Visitors, his publication records, and Barry Simon's detailed reconstruction of the Kato–Rosenblum sequence. All formulas above are editorially derived from the indicated mathematical sources and checked by finite-matrix calculations where applicable.
