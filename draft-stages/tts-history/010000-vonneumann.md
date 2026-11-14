# 010000 — John von Neumann: What Can Remain Invariant When the World Changes?

**Track:** History · People and ideas. **Theme:** the mathematics of quantum states, operator algebras, matrix norms, ergodic averages, and computation. **Background:** elementary matrices, eigenvalues, probability, and inner products; more advanced operator language is introduced where it is needed. **Historical method:** sources and contested attributions are documented in the non-spoken companion.

<!-- BEGIN SPOKEN LECTURE -->

# John von Neumann: What Can Remain Invariant When the World Changes?

Imagine three laboratories studying the same physical system. The first describes it with a matrix. The second records probabilities of measurement outcomes. The third writes a computer program that approximates the system's behavior over time. They seem to be dealing in different objects: arrays of numbers, experimental frequencies, and instructions stored in memory. Yet each laboratory faces a related problem. It must decide which properties survive a change of representation, which predictions survive an approximation, and which conclusions the available evidence actually supports.

John von Neumann spent much of his career moving among these kinds of questions. He helped establish the Hilbert-space language of quantum mechanics. He developed operator algebras, a way to study collections of transformations together rather than one matrix at a time. He proved results about matrices that remain meaningful when their coordinate descriptions change. He contributed to the mathematical theory of repeated motion, to games in which opponents make competing decisions, and to the development of electronic computing. Several of those efforts had difficult consequences beyond mathematics.

It is easy to turn a career this broad into a list of celebrated inventions. But that would leave the interesting mathematics unexplained, and it would conceal the people whose work intersected his. We will pursue one question through different settings: how do we recognize reliable structure when the choice of coordinates, the passage of time, or the available means of calculation changes? We will do the calculations in small examples before considering the larger theory.

## Budapest, Berlin, and the problem of foundations

Von Neumann was born in Budapest on December twenty-eighth, nineteen hundred and three. His birth name was Janos Neumann. He grew up in an affluent Jewish family in a city whose mathematical culture produced several internationally important figures in the same generation. His father's later acquisition of a noble title helps explain the form of the name by which his son became known. Stories about astonishing feats of memory and calculation survive in biographies, but they should not substitute for the education and research through which ability became achievement.

The recollections of his colleagues make the childhood stories more believable, and also more interesting, when seen beside the adult who emerged from them. He was extraordinarily fast at calculation, but he was also sociable, playful, and fond of jokes. This was the son of a prosperous Budapest household with private tutors and access to several languages, not a child whose gifts developed outside society. Later friends called him Johnny. That familiar name belonged to someone who could talk mathematics at tremendous speed and then enjoy a lively evening with friends. Both parts of the personality would travel with him into his academic life. The speed could dazzle; it could also make his lectures hard to follow. A brilliant solution and a good explanation do not automatically come together.

He studied mathematics at the University of Budapest while also pursuing chemistry and chemical engineering. He received a chemical engineering diploma in Zurich in nineteen twenty-five and a doctorate in mathematics in Budapest in nineteen twenty-six. This was not an undergraduate training path organized around one narrow specialty. It exposed him to abstract mathematics and to the problems of physical science at the same time.

In mathematics, the foundations of the subject were under pressure. Set theory had made it possible to describe enormous collections of objects, but it had also produced paradoxes. What should count as a legitimate set? How could mathematics distinguish a useful infinite construction from an inconsistent one? David Hilbert's research program was asking what formal rules would make mathematical reasoning secure. Von Neumann contributed to axiomatic set theory and to the analysis of formal systems during the nineteen twenties. The details belong to a history of logic, but the methodological lesson is already relevant: a mathematical language must say which operations are permitted and which conclusions follow from them.

A Rockefeller fellowship took him to Gottingen, where Hilbert's influence was considerable. He also held positions in Berlin and Hamburg. By the end of the decade a new physical theory was demanding urgent mathematical attention. Quantum mechanics had working formulas for experimental predictions, but the mathematics used in different formulations did not yet present a single, consistently rigorous picture. A young researcher interested in both abstract structure and physical interpretation had a compelling problem to solve.

## Why one matrix cannot explain quantum mechanics

Start with a familiar two-dimensional vector. Suppose it has two complex coordinates and total squared length one. We can think of the coordinates as amplitudes associated with two possible outcomes of a measurement. If the squared magnitudes are three quarters and one quarter, the predicted probabilities of those outcomes are three quarters and one quarter. The phases of the coordinates, invisible to that one measurement, may become important when we measure in a different basis.

Now represent an observable by a self-adjoint matrix. Self-adjoint means that the matrix equals its conjugate transpose. This condition ensures that its eigenvalues are real and that, in finite dimensions, its eigenvectors can be chosen orthonormally. If the observable has two distinct eigenvalues, a measurement can yield either one, with probabilities determined by how much of the state vector lies in each eigendirection.

Take the simplest case. Let an observable have eigenvalues negative two and positive one. Suppose the state has squared amplitude one quarter in the negative-two direction and three quarters in the positive-one direction. The expected measured value is negative two times one quarter, plus one times three quarters. That is one quarter. The individual measurement does not always return one quarter. It returns one of the eigenvalues, and one quarter is the average predicted over many similarly prepared systems.

This distinction between possible outcomes and their expectation becomes crucial when several observables do not commute. If measuring one property changes the effective description of another, there is no reason to expect both to behave as though they were ordinary simultaneously recorded numbers. A coordinate picture that works for one observable may fail to diagonalize the other.

The new quantum theory of the nineteen twenties had arrived through several mathematical routes. Werner Heisenberg's matrix mechanics and Erwin Schrodinger's wave mechanics looked different on the page. Paul Dirac developed a powerful notation and transformation theory. Von Neumann helped establish a rigorous common setting in the geometry of Hilbert spaces. His major book on the mathematical foundations of quantum mechanics appeared in nineteen thirty-two. The book did not invent quantum mechanics or the rule connecting probabilities to squared amplitudes; those were achievements involving many researchers, including Max Born. It provided a systematic mathematical framework in which states, observables, and probabilities could be treated together.

Princeton brought a change in setting as well as subject. Von Neumann arrived in the United States in nineteen thirty with his first wife, Marietta Kövesi. Their daughter Marina was born in nineteen thirty-five. His friendship with Stanisław Ulam became one of the enduring relationships of his American life, built partly on shared Hungarian-speaking and Central European mathematical worlds and partly on a taste for repartee. At the Institute for Advanced Study, Israel Halperin recalled von Neumann animating the afternoon tea table, delighting in explaining difficult problems to other mathematicians. Yet students also remembered that he could erase the blackboard faster than anyone could copy it. This contrast is useful when approaching his operator theory: the conclusions are remarkably unified, but a student needs time to see how the mathematical pieces fit.

## Spectral projections: asking questions of an operator

The finite matrix example works because we can diagonalize the observable. But many physical systems do not have only finitely many independent states. A wavefunction may describe a particle's position along a line. An operator acting on wavefunctions may have a continuous range of possible spectral values, without a normalizable eigenvector for each value.

Here is a concrete model. Take square-integrable functions on the interval from zero to one. Give the space an inner product by multiplying one function by the complex conjugate of the other and integrating. Define an operator that multiplies each function by the coordinate at which it is evaluated. A function concentrated near one quarter is affected mostly like multiplication by one quarter; a function concentrated near three quarters is affected mostly like multiplication by three quarters.

Ask whether this operator has a nonzero eigenvector with exact eigenvalue one half. Such an eigenvector would have to vanish everywhere except where the coordinate equals one half. A single point has zero length, so a square-integrable function supported only there represents the zero vector. There is no nonzero eigenvector of that sort. Yet the number one half still belongs to the operator's spectrum. It is a location at which approximate eigenvectors can concentrate.

How can we talk about a measurement when a neat list of ordinary eigenvectors is no longer available? Instead of asking for the vector associated with one exact value, ask for the subspace associated with a range of values. For example, keep only the part of a function supported between zero and one half. This operation is an orthogonal projection: applying it twice does the same thing as applying it once. It answers the question whether the spectral value lies in a specified interval.

For the constant function one, normalized on the unit interval, the squared size of that projected part is one half. The model therefore assigns probability one half to the lower half of the spectral interval. No single point had to carry an eigenvector. The projection associated with a set is the useful object.

This is the mental model behind a projection-valued spectral measure. To each suitable set of possible spectral values, associate a projection. Disjoint sets give orthogonal projections, and the projection of a union can be assembled as a suitable limit. An observable can then be reconstructed from these spectral pieces through an integral. The spectral theorem had a long development involving several mathematicians. Von Neumann's role includes important work on the operator-theoretic foundations appropriate to quantum mechanics. The core idea for our purposes is that spectral geometry can be encoded by projections even when the spectrum is continuous.

## States as vectors, and states as statistical mixtures

There is another obstacle. A physical preparation may be a mixture of distinct preparations. Imagine that half the time an experimenter prepares the first basis state and half the time the second. The laboratory has a probability distribution over preparations. That is different from deliberately preparing the coherent superposition with equal amplitudes.

The two preparations give the same outcome probabilities when measured in that basis: one half for each result. But they need not give the same predictions for measurements in a rotated basis. The coherent superposition has a definite relative phase. The statistical mixture does not retain that phase information.

A density operator is a way to represent this distinction. In a two-dimensional model, the equal statistical mixture has a diagonal matrix with one half on each diagonal entry. The pure coherent superposition has off-diagonal entries as well. The diagonal entries are the same, but the matrices are different.

For a measurement projection, the probability is calculated by taking the trace of the density operator multiplied by that projection. Trace means the sum of the diagonal entries of a matrix, or the appropriate extension of that idea to operators for which the trace is defined. This formula includes pure states and mixtures within one language. The density-operator formalism is an important part of von Neumann's contribution to quantum foundations, while the broader theory developed through work by others as well.

The point is broader than the example. A matrix can describe an observable, a projection can describe a yes-or-no question about that observable, and another operator can describe a statistical state of knowledge or preparation. Different kinds of operators interact through multiplication, trace, and limits. That suggests studying entire collections of operators instead of treating each matrix separately.

## Operator algebras: what if the observables form a world?

Consider all two-by-two complex matrices. You can add two of them, multiply them, take adjoints, and include the identity matrix. The result stays within the collection. This is an algebra of operators. It also carries a geometric structure because the matrices act on a Hilbert space.

But take just the diagonal matrices instead. They still form an algebra, and any two of them commute. We can think of them as observables that can be simultaneously described using one basis. Add a matrix that swaps the two coordinate directions, and commutativity may disappear. The collection now contains questions that cannot all be reduced to ordinary functions of one shared observable.

In an infinite-dimensional Hilbert space, we need to specify what it means for a collection of operators to be closed under limits. Norm convergence is one possibility, but other notions of convergence watch what each operator does to individual vectors. The distinction is important: approximations can converge on every fixed vector without converging uniformly over all unit vectors.

Von Neumann developed a theory of operator rings beginning in the late nineteen twenties. With Francis Murray, he produced a foundational series of papers in the nineteen thirties and early forties on what are now called von Neumann algebras. A central definition is an algebra of bounded operators that is closed under adjoints and under the weak operator topology, with the identity included. One also has equivalent descriptions in terms of commutants, under appropriate hypotheses.

Why study such a collection? Because an operator may be too poor a description of a physical system considered in isolation. What matters is which measurements are available, how their projections are related, and what other operators commute with all of them. The algebra can preserve structure that an arbitrary change of matrix coordinates obscures.

An especially important concept is the center of an algebra: the operators that commute with every operator in the collection. In the algebra of all two-by-two matrices, the center consists only of scalar multiples of the identity. Such algebras are examples of factors. For a commutative algebra, by contrast, every element lies in the center. This simple distinction becomes the starting point for a much richer classification in infinite dimensions.

## When dimension stops being a whole number

In finite-dimensional geometry, the rank of a projection is an integer. A projection onto a line has rank one; onto a plane, rank two. The algebra of all matrices on an n-dimensional complex space is a type one factor in the modern classification. In that setting, the normalized trace of a projection is its rank divided by n, so only certain fractions can occur.

Murray and von Neumann discovered factor types whose projection geometry is different. In a type two-one factor, there is a finite normalized trace, yet projections can have continuously varying trace values between zero and one. It is possible to have a projection of trace one third or one seventh, and in fact every value in that interval. This is a form of dimension that is not limited to counting basis vectors.

The first reaction may be that the space must have a fractional number of dimensions. That would be misleading. The underlying Hilbert space is infinite dimensional. The trace is measuring a projection relative to the operator algebra's internal structure, not assigning it an ordinary finite vector-space dimension. Murray and von Neumann developed this theory collaboratively; attaching only one name to the result would erase essential mathematical history.

Von Neumann also investigated continuous geometry, motivated partly by hopes of finding a satisfactory broader mathematical language for quantum theory. Not every hoped-for physical application materialized. That is worth remembering: an exceptionally productive mathematical development can arise from a research program whose proposed interpretation does not succeed in its original form. The structure of operator algebras remained fertile independently of that ambition.

For students of spectral perturbation, the practical connection is less exotic. A spectral projection identifies a subspace, products of projections measure their relative geometry, and operator algebras provide a language for manipulating those projections in finite and infinite settings. We can now see why comparing matrices without privileging a coordinate basis was such a natural next question.

## The singular values that survive a rotation

Take a matrix whose action is to stretch one perpendicular direction by five and another by one. In the corresponding basis it is diagonal, with entries five and one. Change the orthonormal coordinates used at the input or output, and the entries of the displayed matrix may change completely. Yet the two intrinsic stretching magnitudes, called singular values, remain five and one.

Singular values are the square roots of the eigenvalues of the positive matrix obtained by multiplying a matrix's adjoint by the matrix itself. They are nonnegative. They tell us the principal stretching magnitudes even when the original matrix is not self-adjoint. Rotating the input or output coordinate system by a unitary matrix does not change them.

Consider three ways to measure matrix size. The operator norm is the largest singular value, five. The Frobenius norm squares the singular values, adds them, and takes a square root: here that is the square root of twenty-six. The nuclear norm adds them directly and gives six. They are all unchanged by unitary changes of input and output coordinates, but they answer different quantitative questions.

Now compare a matrix with singular values three and one with another having singular values two and two. Both have nuclear norm four. Their largest singular values are different, and so are their Frobenius norms. A single ordering of total size is not forced by the requirement that a norm be insensitive to coordinates.

Von Neumann's nineteen thirty-seven study of matrix inequalities helped explain this family of norms systematically. The general insight is that a unitarily invariant matrix norm can be described by a norm on the singular-value list that is unchanged by permutations and sign changes. Such a norm on lists is called a symmetric gauge function. The characterization gives an organizing principle: start with a legitimate symmetric gauge on numbers, apply it to singular values, and obtain a coordinate-independent matrix norm.

This is one reason singular values became so important in perturbation theory. An angle between subspaces can be represented through a projection or a related operator. Instead of bounding that operator using one favorite notion of size, one can compare its entire singular-value list and then apply a family of norms. The theorem about gauges is a foundation for that way of thinking.

## Align the directions: a trace inequality

The most concrete part of the matrix-norm story is a matching problem. Suppose one matrix stretches two perpendicular directions by five and one. A second stretches them by four and two. If their strongest directions coincide, multiply the corresponding diagonal matrices. The trace of the product is five times four, plus one times two. That is twenty-two.

If the second matrix's strong and weak directions are interchanged, the corresponding trace is five times two, plus one times four. That is fourteen. The lists of singular values of the two matrices are unchanged. What changed was the alignment of their directions.

Von Neumann's trace inequality puts a ceiling on this interaction. For any two matrices of the same size, the absolute value of the trace of the first adjoint times the second is no greater than the sum obtained by pairing their singular values in decreasing order. In this example that ceiling is twenty-two. The inequality remains valid for matrices with complex entries and without a shared eigenbasis.

Here is the conceptual leap. We began with an ordinary rearrangement calculation on two diagonal matrices. The general inequality says that however complicated the coordinate relationship becomes, the same sorted pairing supplies an upper bound. A trace measures an interaction; singular values bound how strong that interaction can be after the directions have been aligned as favorably as possible.

This is a variational principle with a geometric flavor. It underlies many later arguments about matrix approximation, optimal alignment, and norm duality. It also supplies a warning. A bound on the trace alone does not control every singular value or every unitarily invariant norm. More structure is needed for stronger conclusions. Von Neumann's inequalities become most powerful when their exact hypotheses are respected.

## Subspaces and a thirty-degree calculation

Let us bring this matrix language back to spectral geometry. Take a line in the plane and its orthogonal projection. Take a second line tilted thirty degrees away, with its own projection. One can multiply the projections and take a trace. The result is the square of the cosine of thirty degrees, or three quarters. This number measures how much the two lines overlap.

Now subtract the two projections and ask for the operator norm. The answer is the sine of thirty degrees, or one half. The two calculations answer complementary questions. The trace of the product measures overlap, while the norm of the difference measures how far the projectors can move a unit vector apart.

Nothing about the line depends on how we name the horizontal and vertical axes. Rotate the entire diagram and the angles are the same. This is why projection-based descriptions are effective for eigenspaces. An individual eigenvector may be changed by its sign or complex phase, and a repeated eigenspace admits many different orthonormal bases. The projection describes the subspace without privileging one of those choices.

This little example is a modern pedagogical connection among several subjects, rather than a claim that von Neumann proved the later Davis-Kahan sine-theta theorem. His part of the story includes the spectral and norm structures that make such theorems intelligible. The later perturbation bounds add essential estimates about how operators and their spectral subspaces move.

## Averaging motion without watching every moment

Von Neumann also worked on a problem that sounds very different: what happens when a system evolves for a long time? Statistical mechanics often studies the average of a physical quantity along a trajectory. One hopes that a long observation will settle down to a stable prediction. But in which sense should that average converge?

Think of a rotation through ninety degrees in a plane. Apply it to an arrow, then apply it again, and again. Over four steps the arrow visits four orientations and returns to where it started. Average the four arrows as vectors, and the result is zero. If we keep averaging longer, the contribution from any incomplete four-step cycle becomes less and less important. The average approaches zero even though the arrow itself keeps rotating.

Now attach an additional coordinate that the rotation never changes. In three dimensions, suppose the first coordinate remains fixed and the other two rotate. Time averaging keeps the fixed coordinate and washes out the rotating component. In operator language, the long-run average becomes the orthogonal projection onto the vectors fixed by the evolution.

The mean ergodic theorem says much more. For a unitary operator on a Hilbert space, average the identity, the operator, its square, and so on through the first many iterations. Applied to any fixed vector, these averages converge in Hilbert-space norm to the projection onto the operator's fixed-vector subspace. The theorem does not promise convergence in operator norm, and it is different from a theorem about almost-everywhere convergence along individual sample paths.

In nineteen thirty-one and thirty-two, von Neumann and George David Birkhoff developed distinct ergodic results with a complicated but documented chronology. Von Neumann communicated his mean-convergence result before Birkhoff's pointwise theorem appeared in print. Their publication order does not by itself establish discovery order. The distinction between convergence in mean and convergence almost everywhere is mathematical, not merely a question of priority.

The reusable idea is that repeated motion can reveal an invariant subspace through averaging. This is another way for a projection to emerge from a problem that initially appears to concern an entire infinite sequence of transformations.

## Games: an invariant prediction under opposed decisions

In nineteen twenty-eight von Neumann proved a minimax theorem for finite two-person zero-sum games. The problem is to find a rational guarantee when two players have opposing goals, each aware that the other will try to exploit predictable choices. It is a theory of mathematical games under explicit assumptions, not a universal theorem about every human conflict.

Consider a game with two choices for each player. If both choose their first option, the first player receives two points. If both choose their second option, the first receives one point. If their choices differ, the payoff is zero. The second player wants that payoff as small as possible.

If the first player always makes the same choice, the second can choose the opposite option and hold the payoff to zero. So the first player may randomize. Let the first option be chosen one third of the time, and the second option two thirds of the time. Against the opponent's first choice, the expected payoff is two thirds. Against the opponent's second choice, it is also two thirds. The opponent cannot drive it below two thirds by selecting either pure option or mixing between them.

Symmetrically, the second player can randomize with the same probabilities, making the expected payoff to the first player two thirds whichever pure option the first player picks. The guarantees meet. That common value is the value of this game.

The minimax theorem generalizes the agreement of those opposing guarantees for finite zero-sum games when mixed strategies are allowed. Years later, von Neumann and Oskar Morgenstern published Theory of Games and Economic Behavior in nineteen forty-four. The theorem is a striking example of using mathematical structure to reason about decision-making, but it has different hypotheses from the min-max principle for eigenvalues. Shared terminology is not a license to identify the two theorems.

Games were an appropriate subject for a researcher who enjoyed company as much as formal calculation. His Princeton household became famous for parties, hospitality, and an irreverent sense of humor. That is a contemporary recollection, not proof that his social life caused the minimax theorem. It does show that the man who analyzed adversarial decisions was not simply a solitary figure working through abstractions. The same group of colleagues moved between serious mathematics, political argument, and ordinary friendship. The boundaries between these conversations grew especially consequential when war changed the direction of their work.

The historical connection is that von Neumann was repeatedly attracted to problems in which a robust conclusion survives the worst legitimate choice of representation or opponent. But we should resist treating that observation as a complete explanation of his personality. It is a useful theme for reading his mathematics, not a substitute for the actual scientific record.

## The computer and the problem of credit

The Second World War brought von Neumann into applied calculation on an enormous scale. Work on explosives, fluid motion, shock waves, and military engineering required numbers that were hard to obtain with hand computation or the available machines. Electronic computing offered the prospect of solving systems of equations that had previously been out of practical reach.

At the University of Pennsylvania, J. Presper Eckert and John Mauchly led the engineering work on ENIAC. Other participants, including Herman Goldstine and Arthur Burks, were central to the broader effort. Von Neumann joined discussions of the proposed successor, EDVAC, during the war. In nineteen forty-five, a report circulated under his name describing an electronic computer whose instructions and data could be stored in memory.

This was an important intellectual and engineering development, but the familiar expression von Neumann architecture can mislead if it is read as a statement of sole invention. Eckert and Mauchly had considered storing instructions before von Neumann joined the project. Alan Turing had developed the theory of universal computation years earlier. The EDVAC design emerged through collaboration and debate. Von Neumann's report gave the proposed organization a powerful presentation and helped disseminate it widely. Historians have documented how circulation of the report under one name created lasting disputes over priority and credit.

What does the stored-program idea accomplish? Picture a machine that can add, compare, move data, and jump to another instruction depending on the result. Instead of rewiring the hardware to change the calculation, one can load a different sequence of instructions into memory. The same electronic equipment can solve many problems. Programs become objects that can be stored, copied, modified, and, in some designs, processed by the machine itself.

This changes the scale of scientific experimentation. A numerical model can be rerun with different initial conditions. A weather prediction can evolve its approximations through many time steps. A matrix calculation can be repeated until an error criterion is met. Von Neumann's Electronic Computer Project at the Institute for Advanced Study pursued those possibilities. His work on numerical weather prediction and other computational research showed that high-speed computing was more than a faster way to produce printed arithmetic tables.

One person's contribution is especially easy to lose behind the phrase von Neumann computer. In nineteen thirty-eight he married Klára Dán, and she later became a pioneering programmer in her own right. The Library of Congress preserves both of their papers, including family correspondence and material documenting her computing career. She helped turn mathematical calculations into instructions a machine could execute, a task requiring detailed decisions about numerical operations and machine behavior. Here the personal and technical histories cannot be separated. A computer design is a promise; programming it makes the promise operational. The large-scale calculations associated with the Institute's project depended on many such people, with different kinds of expertise.

## Calculation, war, and responsibility

Von Neumann worked on the Manhattan Project and on subsequent military and strategic problems. He brought formidable mathematical skills to shock-wave and implosion calculations. After the war he continued to advise the United States government on national-security questions and became a member of the Atomic Energy Commission in the nineteen fifties.

That scientific work contributed to destructive weapons. His forceful public positions on strategy have remained controversial. The institutions he worked for, the advice he gave, and the political choices he made publicly are part of his career, even where his private reasoning is harder to reconstruct.

Friends and colleagues could disagree sharply with his postwar strategic judgments. His concerns about Soviet power and his support for thermonuclear weapons development were substantial political commitments, not a theatrical footnote to his brilliance. Nor can we read a private conscience directly from the dramatic anecdotes that later circulated. The historically sound picture is more difficult: a warm and sometimes mischievous friend who also helped shape policies and technologies with grave consequences. His capacity to make abstract structures usable had become a source of government power.

The ethical question is inseparable from the history of computing as well. Wartime calculation helped drive the investment, urgency, and institutional networks that built early electronic machines. Those machines later found uses in scientific research, business, and countless civilian applications. Neither later civilian success nor wartime purpose alone tells the complete story of the people who built them.

Von Neumann died in Washington in February nineteen fifty-seven, at the age of fifty-three, after serious illness. By then the subjects he had helped develop were already extending far beyond his direct work. His name appeared on theorems, computer designs, algebras, and institutions. Their common label can make their different histories seem simpler than they were.

His last illness makes the familiar image of effortless intellect painfully incomplete. Colleagues who had watched him move from problem to problem at extraordinary speed now encountered the vulnerability of a man who could no longer control his own circumstances. Marina's later career in economics, and Klára's work in computing, are reminders that his life continued in family histories as well as in equations. The mathematics remained public, but the relationships behind it were particular and irreplaceable.

## What survives when the description changes?

Let us gather the mathematics without flattening it. A quantum observable becomes intelligible through its spectral projections. A density operator records probabilities of measurement outcomes, including mixtures that cannot be described by one coherent state vector. An operator algebra captures the relations among a collection of observables. A unitarily invariant matrix norm measures a transformation using its singular values rather than arbitrary matrix entries.

A trace inequality tells us how large the interaction between two matrices can be, regardless of how their strongest directions are oriented. A mean ergodic theorem extracts the fixed subspace from repeated motion. A minimax theorem finds the guarantee available when two players optimize against one another. And a stored-program computer lets instructions become data that a general machine can execute. These are distinct mathematical and technological constructions. None can be derived from the others by a slogan about invariance.

The connections become meaningful at the level of examples. The line tilted thirty degrees has an overlap measured by projection products and a displacement measured by a sine. The stretching matrix has singular values that survive a rotation of coordinates. The endlessly rotating arrow has a time average that settles onto a fixed subspace. The game has a predictable value even though neither player's individual move is predictable. Each example establishes precisely which quantity is stable, under precisely which changes.

Von Neumann's work helped make several of those quantities mathematically available. It also demonstrates why attribution should be as exact as a theorem statement. He developed quantum foundations in a scientific community, not in isolation. His operator-algebra theory included Francis Murray. His game-theory book was written with Oskar Morgenstern. Early computer design involved Eckert, Mauchly, Goldstine, Burks, Turing, and many others. His wartime and postwar work connected mathematics to military technology and public policy, with consequences far beyond the seminar room.

Return to the three laboratories. The matrix, the probability calculation, and the computer model now share a vocabulary of operators and invariants, but they still make different claims. A mathematical theorem supplies a bound only under its hypotheses. An experiment supplies evidence only for the questions it measures. A computer produces an approximation whose reliability depends on the model and its numerical errors.

A lasting lesson from von Neumann's career is that the choice of mathematical representation can create new questions worth asking. Once we represent observations by projections, matrices by singular values, and long-run motion by averages, problems that looked intractable acquire structure. That does not eliminate the work of proving theorems, designing machines, or making responsible choices. It gives us clearer tools with which to do that work.

<!-- END SPOKEN LECTURE -->

---

## Mathematical and historical companion (display only)

### 1. Self-adjoint observables and spectral probabilities

For a finite-dimensional self-adjoint observable
\(A=\sum_j\lambda_jP_j\), where the \(P_j\) are orthogonal
spectral projections, a normalized state vector \(\psi\) gives

\[
\mathbb P_\psi(\lambda_j)=\|P_j\psi\|^2,\qquad
\mathbb E_\psi[A]=\langle\psi,A\psi\rangle.
\]

With \(A=\operatorname{diag}(-2,1)\) and
\(\psi=(1/2,\sqrt 3/2)\), the expectation equals
\(-2(1/4)+1(3/4)=1/4\). These are modern elementary examples,
not historical reproductions of von Neumann's arguments.

### 2. Continuous spectrum and projection-valued measures

On \(H=L^2([0,1])\), let \((Mf)(t)=t f(t)\). For a Borel set
\(E\subset[0,1]\), \((P(E)f)(t)=\mathbf1_E(t)f(t)\). Then

\[
M=\int_0^1 t\,dP(t),\qquad
\|P([0,1/2])1\|_2^2=\tfrac12.
\]

There is no nonzero \(L^2\) eigenfunction at \(t=1/2\), but
\(1/2\in\sigma(M)\) by approximate concentration on shrinking
intervals around \(1/2\).

### 3. Mixtures and density matrices

Let \(\psi_+=(e_1+e_2)/\sqrt 2\). The pure state and incoherent
mixture have

\[
\rho_{\rm pure}=|\psi_+\rangle\langle\psi_+|=
\begin{pmatrix}\tfrac12&\tfrac12\\\tfrac12&\tfrac12\end{pmatrix},
\quad
\rho_{\rm mix}=\tfrac12|e_1\rangle\langle e_1|+
\tfrac12|e_2\rangle\langle e_2|=
\begin{pmatrix}\tfrac12&0\\0&\tfrac12\end{pmatrix}.
\]

For any spectral projection \(Q\),
\(\Pr(Q=1)=\operatorname{Tr}(\rho Q)\). Measuring \(Q=\rho_{\rm pure}\)
gives probabilities \(1\) and \(1/2\), respectively.

### 4. Operator algebra and center

\(M_2(\mathbb C)\) has center
\(Z(M_2)=\{\lambda I:\lambda\in\mathbb C\}\). The diagonal
subalgebra is commutative, hence its center is itself. In a type
\(\mathrm{II}_1\) factor, the normalized trace of projections
runs over \([0,1]\), unlike the rank-quantized values of finite
matrix algebras. This is Murray--von Neumann classification,
not a statement about finite-dimensional vector-space rank.

### 5. Singular-value gauges and trace pairing

Let \(s(A)=(s_1(A),\ldots,s_n(A))\) be the decreasing singular values.
A unitarily invariant norm has the form \(\|A\|=g(s(A))\) with a
symmetric gauge \(g\). Examples:

\[
\|A\|_{\rm op}=s_1(A),\quad
\|A\|_F=(\sum_j s_j(A)^2)^{1/2},\quad
\|A\|_*=\sum_j s_j(A).
\]

Von Neumann's trace inequality is

\[
|\operatorname{Tr}(A^*B)|\leq\sum_j s_j(A)s_j(B).
\]

With \(A=\operatorname{diag}(5,1)\),
\(B=\operatorname{diag}(4,2)\), the trace is \(22\). Conjugating
\(B\) by the swap matrix produces \(\operatorname{diag}(2,4)\),
with trace \(14\), leaving singular values unchanged. For
\(C=\operatorname{diag}(3,1)\) and \(D=\operatorname{diag}(2,2)\),
\(\|C\|_*=\|D\|_*=4\), but \(\|C\|_{\rm op}=3\) and
\(\|D\|_{\rm op}=2\).

### 6. Projections and principal angles

For \(u=e_1\) and \(v=(\cos\theta,\sin\theta)\), set
\(P=uu^*\) and \(Q=vv^*\). Then

\[
\operatorname{Tr}(PQ)=\cos^2\theta,\quad
\|P-Q\|_{\rm op}=|\sin\theta|.
\]

At \(\theta=30^\circ\), these are \(3/4\) and \(1/2\).
This is a pedagogical bridge to later subspace perturbation theory,
not an attribution of the Davis--Kahan result to von Neumann.

### 7. Mean ergodic projection

For a unitary \(U\) on Hilbert space,

\[
\frac1N\sum_{k=0}^{N-1}U^k x\xrightarrow[N\to\infty]{\|\cdot\|}
P_{\ker(I-U)}x.
\]

As a concrete model, take \(U=1\oplus R_{90^\circ}\) on
\(\mathbb R^3\). The invariant coordinate remains unchanged,
while the rotating two-dimensional component averages to zero.
No operator-norm convergence is claimed in general.

### 8. Minimax game calculation

For row payoff matrix \(G=\operatorname{diag}(2,1)\), row player
chooses the first strategy with probability \(p\). The expected
payoffs against the two pure columns are \(2p\) and \(1-p\).
The optimal guaranteed value occurs at \(p=1/3\), yielding
\(v=2/3\). The column player's symmetrical mixture achieves
the matching upper guarantee. This is finite zero-sum game minimax,
not Courant--Fischer eigenvalue min--max.

### 9. Primary and historical attribution notes

- **Mathematical foundations:** von Neumann's 1932 monograph is a
  comprehensive operator-theoretic synthesis of quantum mechanics;
  Heisenberg, Schrodinger, Dirac, Born, and others made independent
  foundational contributions. The no-hidden-variables argument in the
  1932 book used assumptions later criticized by Bell in 1966;
  do not interpret it as ruling out all hidden-variable theories.
- **Operator algebras:** operator-ring work began in 1929; the 1936,
  1937, 1941 and 1943 series with Francis Murray was collaborative.
- **Matrix norms:** the 1937 symmetric-gauge characterization and trace
  bound are the historical focus most directly tied to the DKPS
  curriculum. Later singular-value and symmetric-ideal theory has
  additional authors.
- **Ergodic history:** von Neumann communicated his mean ergodic result
  in October 1931; Birkhoff's pointwise paper appeared in the December
  1931 PNAS issue; von Neumann's was published in January 1932. These
  establish distinct convergence statements, not rival proofs of the
  identical theorem.
- **Computing:** the 1945 EDVAC draft involved ideas from the
  Eckert--Mauchly team, with Goldstine and others. Its single-name
  circulation does not establish sole invention of stored programming.
- **War:** IAS and other biographies document wartime weapons work and
  later government service. Retrospective psychological explanations
  and anecdotal claims are intentionally excluded.

## Reading notes (non-spoken)

Readings are indexed in `metadata/010000.json` and
`metadata/sources.json`. They include institutional biographies,
primary publication bibliographies, specialist mathematical histories,
Bell's 1966 critique, and computing-history research. The narration
separates original contributions from later applications and
terminology.
