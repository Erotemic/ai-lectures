# 015000 — Jacques Dixmier: What can two infinite-dimensional closed subspaces share?

**Track:** History · People and ideas. **Theme:** Jacques Dixmier, relative position in Hilbert space, closed operators, operator algebras, and mathematical exposition. **Background:** vectors, inner products, projections, and elementary linear algebra; the infinite-dimensional arguments are developed with concrete sequences.

<!-- BEGIN SPOKEN LECTURE -->

# Jacques Dixmier: What can two infinite-dimensional closed subspaces share?

Two straight lines through the origin of a sheet of paper can meet at an angle. One may be horizontal, and the other may rise at thirty degrees. From that angle alone, we can answer a surprising number of questions. We know how much of a unit vector on the first line survives when projected onto the second. We know how badly a vector's component along one line can be confused with its component along the other. And we know that the two lines, taken together, span the plane unless they coincide.

Now replace these lines by two closed subspaces of a Hilbert space. Think of a Hilbert space as a setting where vectors still have lengths and angles, but there may be infinitely many independent directions. There can be directions that belong to both subspaces, directions held by one and orthogonal to the other, and a whole spectrum of intermediate angles. The word *closed* tells us that each subspace contains the limits of its convergent sequences. It does not say that the pair behaves as simply as two lines.

One question will guide us: can two closed subspaces fail to share any nonzero vector, yet come arbitrarily close to sharing one? In a finite-dimensional space the answer is no. In an infinite-dimensional space the answer is yes, and the distinction changes how geometry, operator theory, and numerical approximation work.

Jacques Dixmier helped establish the language in which questions like this could be posed and settled. In nineteen forty-eight he published a study of the relative position of two closed linear subspaces in a Hilbert space. In nineteen forty-nine he published an extensive thesis about what were called Julia varieties and operators, as well as a substantial study of certain rings of operators. Later, his work and books shaped the theory of von Neumann algebras, C-star algebras, and enveloping algebras. One of his constructions even permits a kind of trace on operators for which the ordinary sum of diagonal entries diverges.

The mathematical range is broad. The biographical path to it was quite specific: a boy educated in Versailles, a student in occupied Paris, a young researcher learning the work of von Neumann, a participant in the collective enterprise called Bourbaki, and a teacher who prepared lectures word for word. We will follow that life while returning repeatedly to the original geometric problem: how can two infinite-dimensional spaces almost intersect without actually intersecting?

## Versailles, a vocation, and an occupied university

Jacques Dixmier was born in Saint-Étienne, France, in May of nineteen twenty-four. Both of his parents taught school. His father's subjects included French, Latin, and Greek; his mother taught younger children. The family's moves took them through Rouen and Lille before they settled in Versailles when Jacques was nine. Because of those moves, he later said in an interview that he did not identify his upbringing with a single French city. Versailles, though, was the place most closely associated with his education.

An important part of his account is the quality of the teaching he received. Mathematics had attracted him at school, but he did not initially imagine himself as a research mathematician. He thought he could become a good teacher. That modest starting ambition makes his later insistence on the quality of classroom explanation more understandable. Apart from a disappointing first year, he remembered a succession of excellent mathematics teachers. He considered their influence one of the principal reasons he chose mathematics. He also remembered an initial disagreement at home. His father preferred that he train as an engineer; his mother supported his wish to pursue mathematics through the École Normale Supérieure. Eventually he followed that plan.

Preparation for the École Normale required two demanding years beyond the baccalaureate, in courses known as mathématiques supérieures and mathématiques spéciales. He pursued them in Versailles. One year of his school education had been displaced to Saint-Brieuc in Brittany because of the war. France's political catastrophe was present throughout these years, even where ordinary teaching continued.

Dixmier entered the École Normale Supérieure in Paris in nineteen forty-two, under German occupation. His later recollections are valuable because they describe both the persistence of academic life and its danger. Students wanted to finish their examinations quickly. They could not know what new restrictions or emergencies would arrive a few months later. Some of his friends fled France to avoid compulsory labor in Germany. Dixmier said that he himself became involved in resistance activity only near the end of the occupation, attending small meetings; he did not portray himself as an armed partisan.

A few days before the liberation of Paris in August nineteen forty-four, Gestapo officers came to the École Normale. Dixmier was there. In his account, the officers fired in his direction, detained him, and arrested other students. The students were subsequently released. The director, Georges Bruhat, and the school's general secretary, Jean Baillou, were taken prisoner. Baillou survived deportation. Bruhat died in captivity at the Buchenwald concentration camp.

Those events deserve more than a passing chronological sentence. When a later mathematician writes about a clean decomposition of an infinite-dimensional space, the argument may look untouched by history. Yet the people who worked out such arguments had to live through disrupted institutions, damaged infrastructure, and the prospect of arrest. The nineteen forty-four raid is documented in Dixmier's own recollection, and it forms part of the circumstances in which he learned his subject.

Two teachers were particularly important to him: Henri Cartan and Gaston Julia. Cartan's classes could be hard to follow, but his influence would grow through seminars and the Bourbaki group. Julia's lectures, delivered during Dixmier's first year, made Hilbert spaces feel familiar. Dixmier explained the importance of that familiarity with a simple comparison: after Julia's instruction, Hilbert space felt as accessible to him as ordinary geometric space. It was a foundation for the direction of his research.

There was tension in the relationship with Julia. The older mathematician's extreme-right political sympathies were known to Dixmier. Julia also had connections to the family: he and Dixmier's father had attended the École Normale at around the same time, and the two families knew one another in Versailles. Julia became associated with Dixmier's doctoral work, but Dixmier later made clear that the specific thesis problem was not assigned by Julia. He had absorbed a subject and developed his own questions within it.

## A thesis about subspaces that refuse to be closed

To understand those questions, begin with something elementary. In the ordinary plane, the graph of a function can be a line. For example, the equation that sends every number x to twice x has a graph consisting of points whose second coordinate is twice the first. The graph is itself a one-dimensional subspace of the plane, and it is closed: if points on this line converge, their limit remains on it.

Now imagine an operator on an infinite-dimensional Hilbert space. A vector is an infinite sequence of numbers whose squares have a finite sum. An operator might multiply the first entry by one, the second by two, the third by three, and so on. There are sequences for which this operation is harmless, and others for which the resulting sequence fails to have finite squared length. Consequently, the operator cannot be defined on every vector in the space.

Its *domain* is the collection of sequences on which the formula makes sense. That domain is a linear subspace, but it need not be closed. Here is a concrete way to see why. Consider the sequence whose entries are one, one half, one third, and in general one divided by the index. The sum of their squares converges, so the sequence belongs to our Hilbert space. Multiplying the entries by their indices produces a sequence of all ones, whose squares have an infinite sum. The original vector therefore lies outside the domain of the multiplying operator.

On the other hand, truncate that sequence after its first ten entries. Every truncated sequence belongs to the domain, because applying the operator leaves only finitely many nonzero entries. As we allow ten, then a hundred, then a thousand entries, the truncated vectors converge in Hilbert-space length to the full one-over-index sequence. The limit is outside the domain. So the domain is dense, but not closed.

This is more than a pathological example. Partial differential equations, differential operators, and quantum observables often act on restricted domains. If we pretend every operator is defined everywhere, we can conceal the most delicate part of the problem. The operator itself may still be *closed*, meaning that its graph contains the limits of convergent sequences of input-output pairs. Closedness of the graph and closedness of the domain are different statements.

Dixmier's thesis studied special linear sets of this kind. He called them Julia varieties, following a line of work associated with Gaston Julia. The class includes domains of closed operators and ranges obtained by projecting suitable closed subspaces. In his nineteen forty-nine thesis, published by the Bulletin of the French Mathematical Society, he examined how such spaces fit inside Hilbert space and how their geometry reflects properties of operators.

This subject was a logical first home for a young mathematician who had made Hilbert space his native language. A closed graph is a geometric object. A nonclosed domain is a set of inputs on which an analytic transformation is allowed. Projecting the graph onto its first coordinate space gives precisely the domain. Thus the distinction between a closed graph and a nonclosed domain can be understood by asking how one closed subspace sits relative to another.

That connection leads directly to the pair-of-subspaces problem. If projection can turn a closed subspace into a nonclosed range, what should we record about two subspaces to predict when that happens? How can an exact geometric classification detect a phenomenon that no finite-dimensional drawing can show?

## First, the finite-dimensional picture

Before taking on infinitely many coordinates, let us return to two lines. Take a horizontal line and a line at sixty degrees. A unit vector on the horizontal line has length one. Its projection onto the tilted line has length one half, because the cosine of sixty degrees is one half. The remaining perpendicular component has length the square root of three divided by two. Neither line is equal to the other, and the angle gives a numerical measure of their separation.

If we rotate the tilted line to ten degrees, the cosine is closer to one. Its vectors resemble horizontal vectors more closely, and the decomposition of an arbitrary point into contributions along the two lines becomes more sensitive. At one degree, the sensitivity is greater. At zero degrees, the lines coincide, and their sum no longer fills the entire plane in the same way.

The familiar projection formula supplies a precise calculation. For a unit vector on the first line, the length of its projection onto the second equals the cosine of the angle. Equivalently, the largest possible absolute inner product between unit vectors from the two lines is that cosine. This suggests a definition for larger subspaces: find the greatest possible overlap between a unit vector in the first and a unit vector in the second.

There is one catch. If the subspaces share even a single nonzero vector, we can choose that vector from both, obtain an inner product of one, and report an angle of zero. This is perfectly reasonable as a measure of the closest approach between the full subspaces. It is less informative if the aim is to describe how the *remaining*, nonshared portions meet. We therefore need two related notions.

One is often called the Dixmier angle, or minimal angle. Its cosine is the supremum of the absolute inner products of unit vectors, one from each subspace. Supremum means the least upper bound; the best possible overlap need not actually be achieved by any pair of vectors. The other is the Friedrichs angle. To define it, first take out the common intersection from each space, using orthogonal complements within the subspaces. Then measure the largest overlap of these remaining portions.

Here is a finite-dimensional illustration of why we keep both. Let the first subspace be the plane spanned by the first two coordinate axes in three-dimensional space. Let the second plane share the first coordinate axis but tilt away from the second by forty-five degrees toward the third. The two planes intersect along the first axis. Their Dixmier cosine is one, because they literally share that direction. After removing the shared axis, however, each plane contributes a single line. Those lines meet at forty-five degrees. Their Friedrichs cosine is the square root of two divided by two. The two definitions answer different questions about the same pair.

In finite dimensions there is an additional reassurance: once the shared part is removed, the remaining subspaces have a definite positive angle unless one of them vanishes. There are finitely many angular modes, so a positive minimum among the nonzero angles exists. The infinite-dimensional case defeats this last step. A collection of positive angles can creep closer and closer to zero without containing zero itself.

## A pair that almost intersects forever

We can now build a counterexample from elementary sequences. Start with the Hilbert space of square-summable sequences. Call it little ell two. Make two copies of it, placed side by side. A vector in the combined space is an ordered pair of sequences, and its squared length is the sum of the squared lengths of the two components.

Our first subspace, K, contains all pairs whose second sequence is zero. In a picture, K is the horizontal coordinate space. For our second subspace, begin with an operator A that divides the nth coordinate by n. Its first coefficient stays the same, its second is halved, its third divided by three, and so forth. This operator is bounded; it never increases the length of an input sequence.

Let L be the graph of A. A typical vector of L is a pair consisting of a sequence x and the transformed sequence A of x. In a plane, this would be a tilted line. Here it is an infinitely dimensional graph. Because A is bounded, its graph is closed. K is also closed.

Do they share any nonzero vector? A point in K has zero second component. A point in L has second component A of x. To belong to both, A of x must vanish. But A divides each coordinate by a nonzero number, so no nonzero x is sent to zero. Therefore the intersection of K and L contains only the zero vector.

So far this looks like two different lines. The surprise appears when we examine high-numbered coordinates. Take a unit sequence supported in its nth coordinate, with a one there and zeros elsewhere. Its graph vector has one in that coordinate of the first sequence and one divided by n in the corresponding coordinate of the second. Its distance from the horizontal subspace K is one divided by n. For n equal to ten, that distance is a tenth. At a hundred it is a hundredth. At a million it is one millionth.

The full graph vectors have lengths just a little greater than one. Normalize them to unit length, and their distances from K still approach zero. We have two closed subspaces, with no nonzero shared vector, containing unit directions that are closer than any specified positive distance. Their minimal angle is zero even though the intersection is trivial. The best overlap is one as a supremum, but no nonzero vector realizes perfect overlap.

Pause over what this means. Every coordinate direction has a positive angle. In the first direction, the graph rises noticeably. In the thousandth, the rise is extremely shallow. The pair contains a sequence of increasingly horizontal directions. There is no single nonzero graph vector exactly horizontal. The loss of a positive angular bound happens only by moving farther and farther out into the infinitely many coordinates.

This is why a basis-independent supremum is more natural than hoping for a smallest attained angle. The answer is controlled by the tail behavior of an operator, and that behavior may not be visible in any single finite truncation. A computer examining the first fifty coordinates would report a positive smallest angle. Increasing the truncation would make that reported angle shrink. The exact infinite-dimensional result is zero.

There is another consequence. What happens if we take sums of vectors from K and L? The first component can be anything, because K supplies arbitrary horizontal sequences. The second component must lie in the range of A. So the sum of K and L consists of all pairs with arbitrary first component and a second component in the range of A.

The range of A is not closed. To see this, return to the one-over-index sequence. It is a legitimate square-summable output, and we can approximate it by finitely supported outputs of A. But producing the full one-over-index output would require an input sequence of all ones. That input is not square summable. Thus the target lies in the closure of the range, while remaining outside the range itself.

Consequently, the sum of K and L is not closed, even though K and L individually are. This answers the question that began the lecture. Two closed subspaces can fail to intersect and yet approach one another through a sequence of directions so closely that their algebraic sum loses closedness.

The Friedrichs angle packages this phenomenon. For two closed subspaces, a positive Friedrichs angle is equivalent to the closedness of their sum. In the special case where their intersection is zero, the Friedrichs and Dixmier angles agree. Our example has zero angle and a nonclosed sum. The finite-dimensional rule survives as a theorem only when we impose a uniform separation condition.

## From an angle to an operator

The geometric test can be written without selecting the special coordinate directions. Let P and Q be the orthogonal projections onto K and L. Project a vector onto L, then onto K. The operator obtained by composing the projections tells us how much of one subspace can survive projection through the other. The norm of that operator is the largest amount of overlap achievable, or approached, by unit vectors.

In this sense the Dixmier cosine equals the norm of the product of the two orthogonal projections. If the subspaces share a vector, the product fixes it and the norm is one. If they do not share a vector, the norm can still be one, as in our graph example. Operator norm detects both exact overlap and asymptotic overlap; it does not distinguish them by itself.

For the Friedrichs cosine, we remove the common intersection. The corresponding expression subtracts the orthogonal projection onto the intersection from the product. The norm of that difference measures the overlap of the portions left after shared directions are removed. The distinction is small in notation and enormous in meaning.

One can see a practical use immediately. Suppose an algorithm repeatedly projects onto two constraint spaces, seeking a vector that satisfies both constraints. Von Neumann's alternating-projections principle gives convergence under the Hilbert-space hypotheses, even when the angle is zero. But the rate can differ drastically. A positive Friedrichs angle supplies a uniform geometric rate in the standard two-subspace setting. An angle of zero permits convergence without such a uniform rate. Our sequence-space construction explains what goes wrong: some high-coordinate modes barely move under each projection. There is no single finite worst-case angle controlling all of them.

This also clarifies what a good perturbation theorem must assume. If a proof needs a subspace to stay uniformly separated from another, the condition must be an estimate. Saying the two spaces merely have zero intersection will not be enough. In finite-dimensional geometry that distinction can seem pedantic. In Hilbert space it is the difference between stable decomposition and an arbitrarily ill-conditioned one.

The same distinction emerges in spectral methods. A spectral subspace is often represented by a projection. Comparing an original operator with a perturbed operator leads to two projections, and hence to two subspaces. Angles between the spaces measure their motion. If the theorem controls those angles, it is controlling a particular operator quantity. If it asserts a uniform lower bound, it is ruling out the asymptotic-contact behavior just constructed.

Dixmier's nineteen forty-eight investigation of the relative position of closed linear subspaces stands in the history of these ideas. It preceded Paul Halmos's nineteen sixty-nine paper *Two Subspaces*. Halmos explicitly credited Dixmier with an earlier theorem classifying pairs of subspaces up to unitary equivalence and presented a new proof using his own graph and cosine–sine normal forms. We should keep that priority straight: the later block matrices are associated with Halmos's exposition, while the earlier equivalence classification was Dixmier's.

## The geometry of two closed graphs

The pair we just built used an operator that was defined everywhere and shrank higher coordinates. There is a complementary construction that returns to the thesis. Let B multiply the nth coordinate by n, rather than divide it. The operator B is defined only for sequences whose index-weighted entries remain square summable. It is unbounded, yet it has a closed graph.

Why is the graph closed? Imagine a sequence of input-output pairs from the graph that converges in the product Hilbert space. For each fixed coordinate, the inputs converge and the outputs converge. The nth output coefficient was always n times the nth input coefficient, so that relation survives in the limit. The limiting output is square summable, because we assumed convergence in Hilbert space. The limiting input therefore belongs to the operator's domain, and the limiting pair lies on the graph.

Project this graph onto the horizontal coordinate space. Its image is the domain of B. We have already seen that this domain is dense and nonclosed. A closed subspace has produced a nonclosed projected range. This is the basic geometric mechanism behind the Julia-variety discussion, and it is why studying the relative position of closed subspaces naturally leads to domains of unbounded operators.

There is a second asymptotic contact here, in a different direction. The normalized graph vector associated with the nth coordinate has first component of size approximately one divided by n and second component of size approximately one. As n increases, the graph approaches the vertical coordinate space along these directions, yet shares no nonzero vector with that vertical space. The angle between them tends to zero without an exact intersection.

The two graph examples are mirror images in an instructive sense. Dividing by n makes a bounded operator whose graph lies arbitrarily close to the horizontal coordinate space. Multiplying by n makes a closed unbounded operator whose graph approaches the vertical coordinate space. In the first example, the range of the operator is not closed. In the second, its domain is not closed. Both are visible through pairs of closed subspaces.

This is a useful lesson in choosing abstractions. A coordinate sketch shows only two-dimensional lines, each with a positive angle. A Hilbert-space operator can collect infinitely many such sketches. The sequence of angles, and whether they admit a uniform bound, is part of the geometry. An operator is a way to store that entire collection without demanding that every angle be listed individually.

## From subspace geometry to rings of operators

The next part of Dixmier's career moved from individual operators to families of operators that are closed under algebraic operations. A ring or algebra of operators lets us add operators, multiply them by composition, and in the usual Hilbert-space setting take adjoints. That last operation is analogous to transposing a matrix and conjugating its complex entries. Such algebras become richer when they are closed under suitable limits of operators.

The work of John von Neumann and Francis Murray had shown that these families could be classified in ways that bore little resemblance to counting the rows and columns of matrices. Some have a notion of dimension that behaves like ordinary integer dimension. Others permit continuous dimension scales. The classification of factors into types had already become a central framework. Dixmier did not invent that framework, but he was one of the people who extended it, organized it, and made it more accessible to a generation of researchers.

His nineteen forty-nine paper on finite-class rings of operators is a major early step in this direction. Its references include the Murray–von Neumann papers and his own study of two closed subspaces. The connection is natural: projections live in operator algebras, and the way projections can be combined and compared is part of their structure. To classify an algebra, one often asks what the projections inside it look like, and how those projections relate to one another.

A finite-dimensional analogy makes the point. Consider all two-by-two matrices. Inside that algebra lie the projections onto the horizontal axis, the vertical axis, and any line through the origin. Unitary changes of coordinates can rotate one rank-one projection into another. Rank is an integer-valued measure of the size of a projection. In an infinite-dimensional factor, an analogous comparison becomes considerably subtler. Classifying projections may require a trace or dimension function, and the possible values need no longer be integers.

Dixmier learned von Neumann's writings carefully. In his later interview, he said that quantum mechanics was not the main route by which he understood them. His particular interest was unitary representations: the ways groups can act by length-preserving transformations on Hilbert spaces. Roger Godement, slightly older than Dixmier, introduced him to important results in representation theory, including some work Godement had not published. The two subjects reinforced one another. Group representations generate operator algebras, and operator algebras help describe representations.

Dixmier met von Neumann briefly in Paris in nineteen forty-seven. Von Neumann, visiting after the war, was staying at the Hôtel Lutetia. The much younger Dixmier had only early papers to show him, and remembered the invitation with gratitude. They later corresponded. This was a meeting between researchers at very different stages of their careers, during a period when the language of operator algebras was still settling into place.

A terminology detail reveals the collaborative nature of that process. The label *von Neumann algebra* is closely associated with Dixmier's famous book. Yet when he was asked whether he had coined the name, Dixmier gave the credit to Jean Dieudonné, who proposed it during a Bourbaki discussion. The name appeared prominently in Dixmier's nineteen fifty-seven book on algebras of operators in Hilbert space. The distinction between proposing a name and making it standard is part of accurate mathematical history.

## The role of the C-star algebra

Another direction led to C-star algebras. A C-star algebra is an algebra of bounded operators closed under adjoints and under the operator norm, equipped with a compatibility condition between the norm and adjoint. In the concrete bounded-operator setting, the condition says that the squared norm of an operator equals the norm of the product of its adjoint with itself.

A finite-dimensional example is the algebra of all complex matrices of a fixed size. The algebra contains identities and products, and the adjoint turns rows into columns while conjugating coefficients. Taking matrix limits causes no difficulty, because all norms on a finite-dimensional vector space define the same convergence. In an infinite-dimensional Hilbert space, completion becomes a substantive condition. Infinite sequences of approximating operators can converge to an operator that must remain in the algebra if the algebra is to be complete.

Why study an algebra instead of a single transformation? A single matrix can describe one operation. An algebra records a system of operations and how they fit together. It can contain the projections selecting measurements, the functions of an observable, and the transformations generated by symmetries. Its representations describe how the abstract algebra acts on concrete Hilbert spaces. The same algebraic object may admit different representations, just as a group may act in many different spaces.

Dixmier's nineteen sixty-four book on C-star algebras and their representations was part of the consolidation of this field. It followed the nineteen fifty-seven monograph on von Neumann algebras and was later joined by his nineteen seventy-four book on enveloping algebras. The latter arise from Lie algebras, where an operation called the bracket measures noncommutativity. Enveloping algebras turn Lie-algebra information into an associative algebraic setting. That allows methods of representation theory to connect with the operator-algebra questions he had studied for years.

The breadth was real, but the subjects were connected. A group may act unitarily; its infinitesimal symmetries may form a Lie algebra; representations generate operator algebras; projections inside those algebras encode geometric subspaces; and traces help measure operators and projections. One can trace a route through that chain without claiming that each result is a consequence of the others. Dixmier spent decades working across these intersections.

## A trace at the edge of summability

There is one more construction worth understanding, because it returns to the question of what infinite-dimensional behavior requires us to change. For a finite square matrix, the trace is the sum of the diagonal entries. It is invariant under a change of orthonormal coordinates, and it satisfies the cyclic rule: the trace of A times B equals the trace of B times A, whenever these finite products are defined.

For an infinite-dimensional positive compact operator, the eigenvalues may be positive numbers decreasing toward zero. When they sum to a finite value, the ordinary trace works. But consider an operator whose eigenvalues, arranged in decreasing order, are one, one half, one third, and so on. Their sum diverges. The ordinary trace is infinite, even though every individual eigenvalue tends to zero.

Look instead at partial sums. After the first N terms, the sum grows roughly like the natural logarithm of N. Divide that sum by the logarithm of N. The resulting ratio approaches one. We have extracted a finite coefficient from a divergent sum. If the eigenvalues were twice as large, the coefficient would be two. If they decayed much faster, the coefficient could be zero.

This suggests a new kind of measurement for operators just outside the trace-class world. In nineteen sixty-six, Dixmier constructed a non-normal trace associated with this borderline logarithmic growth. Later mathematics calls it a Dixmier trace. The complete construction uses a generalized limiting procedure and an appropriate ideal of operators. It is not enough to take the limit of the normalized partial sums in every case, because that limit need not exist. The sophisticated part is defining a linear, unitarily invariant trace in a wider setting while preserving the essential algebraic properties.

This construction later became important in Alain Connes's noncommutative geometry. For our purposes the key idea is accessible: an infinite sum can diverge in a controlled manner, and its leading rate of divergence may carry geometric information. The ordinary trace forgets that rate by reporting infinity. The Dixmier trace can retain the coefficient under suitable hypotheses. Here again, the infinite-dimensional setting does not abolish familiar finite-dimensional ideas. It forces us to distinguish which features survive and which require a new definition.

## Bourbaki, books, and the craft of explanation

Dixmier joined the Bourbaki group in nineteen forty-nine, after Jean-Pierre Serre and Pierre Samuel invited him. Bourbaki was a collective project to write systematic, rigorously organized mathematics under a shared pseudonym. Its drafts were debated and revised, often by different authors over several rounds. The work exposed participants to areas beyond their own research specialties and demanded a very particular precision of language.

Dixmier later said that without Bourbaki he might have remained within Hilbert-space theory throughout his career. In the group he worked on topics including Lie algebras and root systems. He credited Pierre Cartier with an important move toward treating root systems as an independent axiomatic subject, and Armand Borel with algebraic proofs that improved the presentation. Dixmier described his own strength in the project chiefly as writing and organizing material. The point is not false modesty. It is evidence that he recognized exposition as a demanding mathematical contribution in its own right.

There is an interesting contrast between the way Bourbaki books read and the way their drafts were produced. The finished pages are formal and carefully ordered. The meetings, by Dixmier's account, could be noisy, discursive, and contentious. A polished mathematical text may emerge from an extended social argument over definitions, priorities, and exact hypotheses.

His own books carried that concern for structure. The great monographs on von Neumann algebras, C-star algebras, and enveloping algebras were reference works for researchers. He also wrote texts for undergraduates, as well as books on integration and topology. Reviewers praised the clarity and compression of the exposition. He acknowledged that brevity can have drawbacks, especially for students who need time to connect a definition to an example.

His spoken teaching practice was more revealing still. In the interview, he explained that he prepared mathematical talks word for word. He paid attention to writing large enough for students to see and to facing the audience rather than speaking toward the blackboard. He rejected the idea that getting stuck in front of the class is necessarily a good way to demonstrate the difficulty of mathematical work. He knew what it felt like to hear a lecturer whose ideas, speech, and board work diverged.

He had arrived at those preferences through experiences as a student. Dixmier recalled leaving an analysis course after only two lectures because he could not follow the instructor. Older textbooks could require a reader to jump back and forth by dozens of pages to reconstruct a proof. His preference for a theorem followed by a clearly organized proof was a response to frustration, not merely allegiance to a fashionable style. At the same time, he accepted that a lecture benefits from pictures and motivation. Written mathematics and spoken mathematics ask different things of their audiences.

These preferences connect directly to the problem of explaining a Hilbert-space theorem. A few terse symbols can state that two subspaces have zero intersection and that the norm of the product of their projections is one. Unless the audience has followed the one-over-index example, those facts may sound contradictory. The successful explanation is not the shortest correct statement. It is the one in which the listener can reconstruct why the two facts coexist.

Dixmier's academic positions took him from Toulouse in nineteen forty-seven to Dijon in nineteen forty-nine and Paris in nineteen fifty-five. The early years were marked by housing shortages, long train journeys, and the rebuilding of France after the war. Later, at the Conservatoire des Arts et Métiers, he recalled teaching in an auditorium with around five hundred students. He remained associated with Parisian mathematics for the main portion of his career.

His students included Alain Connes, Michel Duflo, and Michèle Vergne. In the interview, he spoke carefully about the differences among students. Some developed their research with considerable independence; others needed closer guidance. He described recognizing the importance of a short paper Connes brought to his seminar and later following Connes's work with interest. The relationship between teacher and student was therefore not reducible to one uniform pattern of supervision.

Dixmier retired at sixty, in nineteen eighty-four, under a law that allowed retirement at that age. He then spent several years working regularly at the Institut des Hautes Études Scientifiques in Bures-sur-Yvette. He pursued invariant theory and partitions, and valued the mathematical conversation around him. He also wrote fiction in later life, including science fiction and novels with Alain Connes and Danye Chéreau, and collaborated on a book introducing quantum ideas through dramatic dialogue. The participation of a writer of rigorous operator-algebra treatises in fiction complicates the picture of Dixmier as an austere formalist. His work in Bourbaki demanded compression and impersonal organization; his literary collaborations depended on other kinds of voice and invention. Those activities sit alongside a career whose center was exact analysis and algebra.

A later scene gives a particularly concrete view of his relationships. At a small dinner in Paris for his hundredth birthday, in May two thousand twenty-four, Alain Connes remembered Dixmier speaking without notes to the guests he had personally chosen. He recalled details of their histories together, including the family connections of former students. He thanked Jean-Pierre Serre for treating him as an equal during their decades in Bourbaki. Connes describes a man who was attentive to the people around him, even while defending demanding standards in mathematics. The gathering also celebrated a late return to research after a long interruption. That is a better ending to the personal story than imagining Dixmier fixed forever in the postwar seminar room.

## What the geometry has taught us

Let us return to the pair of subspaces. We began with two lines in the plane, where an angle describes how they meet. We then built two closed infinite-dimensional spaces with no shared nonzero vector, yet with unit directions whose distance approaches zero. The very same construction made their sum nonclosed. We used a bounded diagonal operator to build the first graph and an unbounded closed operator to build a second example, whose projected domain is nonclosed.

Each step sharpened the question. Intersection records exact common directions. The Dixmier angle measures the closest approach of the whole subspaces. The Friedrichs angle measures the approach of their nonshared parts. The product of orthogonal projections encodes that comparison without committing to coordinates. Closedness of the sum tells us whether a uniform separation remains after the common part is removed.

Dixmier's early study belongs to the moment when the geometry of Hilbert spaces, the theory of unbounded operators, and the structure of operator algebras were being worked into a common language. His later books and research helped make that language available across several mathematical communities. The social history illuminates the intellectual one. A frightened student in occupied Paris learned to trust Hilbert-space geometry; a colleague in Bourbaki learned to edit claims in public; an older teacher continued to discuss problems with students and friends. The surprising mathematical fact remains the same: in infinite dimensions, two closed subspaces can be separated at every individual direction and still have no positive separation that works for all directions at once.

That fact is worth remembering whenever a proof treats “they do not intersect” as sufficient for “they stay uniformly apart.” One statement concerns exact equality. The other is a quantitative theorem. Jacques Dixmier's mathematics helped give us the tools to tell them apart.

<!-- END SPOKEN LECTURE -->

---

## Mathematical and historical companion (display only)

### 1. The two angle conventions

Let \(M,N\) be closed subspaces of a (real or complex) Hilbert space \(H\), with orthogonal projections \(P_M,P_N\), and \(E=M\cap N\). Use unit-ball suprema so that zero subspaces are covered without special cases. The **Dixmier cosine** is

\[
 c_0(M,N)=\sup\{|\langle x,y\rangle|:x\in M,\ y\in N,\ \|x\|\le 1,\ \|y\|\le 1\}
 =\|P_MP_N\|.
\]

The **Friedrichs cosine**, with the exact intersection removed, is

\[
 c(M,N)=c_0(M\ominus E,N\ominus E)
 =\|P_MP_N-P_E\|.
\]

For \(M,N\) closed, \(c(M,N)<1\) if and only if \(M+N\) is closed; equivalently, the addition map \((m,n)\mapsto m+n\) on \((M\ominus E)\oplus (N\ominus E)\) has a bounded inverse onto its range. If \(M\cap N=\{0\}\), then \(c=c_0\). In finite dimensions, the supremum on unit spheres is attained; in infinite dimensions it may be only approached.

### 2. A finite-dimensional plane pair

In \(\mathbb R^3\), take \(M=\operatorname{span}(e_1,e_2)\) and \(N=\operatorname{span}(e_1,(e_2+e_3)/\sqrt2)\). Then \(E=\operatorname{span}(e_1)\), so \(c_0(M,N)=1\), while \(c(M,N)=1/\sqrt2\). The first measure notices the common line; the second measures the remaining forty-five-degree angle.

### 3. Bounded diagonal graph: disjoint closed spaces with zero angle

Set \(H=\ell^2(\mathbb N)\oplus\ell^2(\mathbb N)\), \(K=\ell^2\oplus\{0\}\), and let \(A:\ell^2\to\ell^2\) be \((Ax)_n=x_n/n\). Set \(L=\operatorname{graph}(A)=\{(x,Ax):x\in\ell^2\}\). Then:

- \(K,L\) are closed (bounded graph theorem in the forward direction: a bounded operator has a closed graph).
- \(K\cap L=\{0\}\), because \(A\) is injective.
- Unit-normalized \(v_n=(e_n,\frac1n e_n)/\sqrt{1+n^{-2}}\in L\) satisfy \(\operatorname{dist}(v_n,K)=1/\sqrt{n^2+1}\to0\). Hence \(c_0(K,L)=c(K,L)=1\), the corresponding angle is zero, and the supremum of the cosine is not attained by any nonzero common vector.
- \(K+L=\ell^2\oplus\operatorname{ran}(A)\). The vector \(b=(1/n)_{n\ge1}\) belongs to \(\ell^2\) but not to \(\operatorname{ran}(A)\), since \(A^{-1}b=(1,1,\ldots)\notin\ell^2\). Its finite truncations do lie in \(\operatorname{ran}(A)\), so \(K+L\) is not closed.

Each finite-coordinate truncation has a positive minimum angle; the lower bound vanishes as the truncation increases.

### 4. Unbounded graph with a nonclosed projection

On \(\ell^2\), define the closed unbounded diagonal operator

\[
 (Bx)_n=nx_n,\quad D(B)=\{x\in\ell^2:\sum_{n\ge1}n^2|x_n|^2<\infty\}.
\]

The graph \(G(B)\subset \ell^2\oplus\ell^2\) is closed: coordinatewise equality \(y_n=nx_n\) passes to limits of input-output pairs. Yet its horizontal projection equals \(D(B)\oplus\{0\}\), dense and nonclosed. The vector \((1/n)\) is in \(\ell^2\setminus D(B)\). Normalized graph vectors \((e_n,n e_n)/\sqrt{1+n^2}\) approach the vertical subspace with zero intersection. This shows how domains of closed operators arise naturally as projections of closed subspaces.

### 5. Relative position and historical priority

Dixmier's *Position relative de deux variétés linéaires fermées dans un espace de Hilbert* appeared in *Revue Scientifique* 86 (1948). The bibliography of Dixmier's 1949 thesis lists pp. 367–380; Halmos's 1969 bibliography lists pp. 387–399. These are conflicting bibliographic records; confirm against the original volume before choosing pagination. The substantial, documented historical attribution is secure: Halmos's 1969 *Two Subspaces* explicitly calls his equivalence-classification corollary a new proof of **Dixmier's theorem**. Halmos's three graph/CS/half-angle models belong to Halmos's 1969 presentation, and should not be retroactively assigned in their exact form to the 1948 paper.

### 6. Normalized projection and alternating projection remarks

The alternating projections \((P_MP_N)^k\) approach \(P_E\) strongly as \(k\to\infty\). If \(c(M,N)<1\), convergence is in operator norm with geometric control. The graph example \(K,L\) above has \(c=1\) and exhibits arbitrarily slowly changing high-coordinate modes. These claims concern the standard setting of two orthogonal projections; no rate is claimed for arbitrary projection schemes.

### 7. What is and is not the Dixmier trace

For a positive compact operator with singular values \(\mu_n=1/n\),

\[
 \sum_{n=1}^N\mu_n\sim \log N,\qquad \lim_{N\to\infty}\frac{\sum_{n=1}^N\mu_n}{\log N}=1.
\]

The full Dixmier trace, originating with the 1966 construction, requires an appropriate weak trace ideal (often \(\mathcal L^{1,\infty}\) under a specified convention) and a suitable generalized limit or dilation-invariant state. The displayed ordinary limit is an illustrative special case, not the general definition. Dixmier traces vanish on finite-rank operators and extend the idea of traces to certain operators outside trace class. The 2015/2016 Guichardet historical review describes the original construction and its later use by Connes.

### 8. Context: operator algebras and the historical record

- 1949: *Les anneaux d'opérateurs de classe finie*, *Annales scientifiques de l'École Normale Supérieure* 66, 209–261, develops the analysis of finite-class rings of operators.
- 1957: *Les algèbres d'opérateurs dans l'espace hilbertien (Algèbres de von Neumann)*. Dixmier credited Jean Dieudonné with proposing the term “von Neumann algebra” in a Bourbaki discussion.
- 1964: *Les C*-algèbres et leurs représentations*.
- 1966: short construction initiating what became the Dixmier trace.
- 1974: *Algèbres enveloppantes*.
- Interview: Martin Raussen, “Interview with Jacques Dixmier,” *Newsletter of the European Mathematical Society* 72 (June 2009), pp. 34–40. This oral-history source grounds the occupation account, tutoring, 1947 career transition, Bourbaki drafting, research priorities, students, and the teaching philosophy. Biographical claims about teachers and resistance reflect Dixmier's own recollections; claims about others' motives are presented accordingly.

## Reading notes (non-spoken)

The interview is the most informative first-person life source. The 1949 thesis and rings-of-operators papers are available from Numdam with stable bibliographic records. Halmos's 1969 paper supplies a clear historical attribution for the pair-classification theorem. For the two modern cosine conventions and the equivalence between the Friedrichs bound and closed sums, consult a specialist reference on angles between subspaces. The mathematics above provides independent worked examples rather than reproducing a source's proof.
