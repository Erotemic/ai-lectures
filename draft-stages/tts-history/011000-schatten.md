# 011000 — Robert Schatten: How Do We Measure an Infinite-Dimensional Transformation?

**Track:** History · People and ideas. **Theme:** the Lwów school, tensor products of normed spaces, crossnorms, Schatten classes, trace duality, and operator ideals. **Background:** vectors, matrices, singular values, norms, and convergent numerical series. The lecture supplies its own tensor-product model. **Historical method:** primary publication details and biographical sources appear in the display-only companion.

<!-- BEGIN SPOKEN LECTURE -->

# Robert Schatten: How Do We Measure an Infinite-Dimensional Transformation?

Imagine that a laboratory gives you a matrix describing how a device transforms signals. It changes some directions dramatically and others hardly at all. You can ask for the largest possible amplification of a unit signal. You can ask for the total squared amplification over perpendicular input directions. Or you can try to add up the strengths of all the independent ways the device acts. Those are three different questions, even though all three concern the very same matrix.

Now imagine that the signals are functions, and the matrix has become an operator on an infinite-dimensional space. There may be infinitely many independent directions. Adding their strengths may give a finite number, or an infinite one. And there is a more fundamental question: when a transformation can be written as a sum of simple pieces, how should we measure the size of that sum? Does the answer depend on how we chose to break the transformation apart?

These questions lead to Robert Schatten, a mathematician born in 1911 in Lemberg, now Lviv, who worked in Poland and the United States. Schatten's name survives in the Schatten classes of operators. But starting with that familiar name misses his larger contribution. He was one of the mathematicians who made tensor products of Banach spaces into a systematic subject. He investigated how norms can be transported to spaces built from pairs of vectors, and how these new norms describe transformations. The operator ideals bearing his name grew out of that program.

There is a human history behind the mathematics. Schatten studied with Stefan Banach in Lwów, made his way to New York before the Second World War, worked with Francis Murray and John von Neumann, and built a teaching career that lasted decades. Members of his family were murdered in Europe during the war. A later biography, based on university and immigration records, has recovered a much sharper picture of his life than the short encyclopedia entries available for many years.

To understand what he added to mathematics, we will begin with an extremely small calculation. It will give us a problem whose solution is almost obvious in two dimensions, but whose infinite-dimensional version is demanding.

## One transformation, several meanings of size

Take a transformation of the ordinary plane. In one perpendicular direction it stretches by three; in the other it stretches by one. You could picture a circular rubber sheet turning into an ellipse. The ellipse's long semiaxis has length three, and its short semiaxis has length one.

If you only want the worst amplification, the answer is three. No unit vector can be stretched more than that. This is the operator norm. If you care about the aggregate squared stretching, calculate three squared plus one squared. The answer is ten; its square root is approximately three point one six. This is the Frobenius norm in finite dimensions, and the Hilbert–Schmidt norm in the operator setting.

A third measurement adds the stretching strengths themselves. Three plus one makes four. That is the trace norm, also called the nuclear norm in this matrix setting. Here the numbers three and one are the singular values. A singular value is a stretching factor after you choose suitable perpendicular input and output directions. Singular values remain unchanged if you rotate the coordinate systems before or after applying the transformation.

We have already learned something important. The answers three, approximately three point one six, and four all describe one transformation. None is a mistake. Each asks a different question about the same geometry.

You can build a whole family between these measurements. Raise each singular value to a power called p, add the resulting numbers, and then take the pth root. At p equal to one you get the sum. At p equal to two you get the square root of the sum of squares. As p becomes very large, the largest singular value dominates. These are the Schatten p norms, named for Robert Schatten, although the formulas have precursors and their systematic operator-theoretic development involved several people.

In two dimensions every such norm gives a finite answer. That makes the differences look like personal preferences. In infinite dimensions, the differences become structural. One norm may be finite and another infinite. The choice determines which transformations are available for a theorem, and which operations are continuous. We will return to that distinction, but first we need another idea Schatten studied even more directly: how two vector spaces can be combined.

## Lwów: where abstract spaces became concrete problems

Robert Schatten was born Rubin Schatten on 28 January 1911. His birthplace was called Lemberg under the Austro-Hungarian Empire, and Lwów after the creation of the Second Polish Republic. The city is now Lviv in Ukraine. The sequence of names reflects changes in state boundaries, but his mathematical education took place in the city during its Polish period.

He attended a Jewish secondary school and entered Jan Kazimierz University in 1929. Lwów was a center of the new field called functional analysis. Mathematicians there were asking what could be preserved from finite-dimensional linear algebra when vectors became infinite sequences, functions, or other abstract objects. Stefan Banach was among the leading figures. Hugo Steinhaus, Juliusz Schauder, and others worked in an environment where abstract concepts were judged by what they could actually prove about equations and functions.

The historical record gives a pleasingly specific connection. Surviving course lists show that Schatten attended Banach's lectures and exercises in analysis. In 1933 he wrote a master's thesis under Banach's supervision, with a title that translates as Abstract Spaces. The thesis explored how choices of neighborhood axioms distinguish families of topological spaces, and how different kinds of infinite-dimensional spaces may be compared. This was not yet the operator-ideal theory for which he became known. It reveals the starting point of his education: the structure of an infinite-dimensional space was itself a mathematical problem.

A later historical study by Lech Maligranda and Yaroslav Prytuła used archival records to reconstruct the thesis and his movements. One of the examples they discuss is the space of all real sequences. A sequence here is an infinitely long list of numbers. We can measure whether two such lists are near one another by comparing their first coordinate, then their second, and so on, assigning smaller and smaller weights to later coordinates. This gives a topology on a space that cannot be visualized as an ordinary plane or three-dimensional room.

That problem is related to our own. In a finite matrix, almost any familiar norm will do if we only need to know whether the entries are finite. In infinite dimensions, the definition of nearness can decide whether a sequence of approximations converges at all. Two spaces may have the same underlying formal expressions and behave very differently when equipped with different norms.

The Lwów tradition therefore supplied Schatten with a useful habit: when someone writes down a new space, ask what topology or norm they intend, and what operations survive after the space is completed. That habit will organize the mathematics in this lecture. It also helps explain why studying tensor products was a genuine research program rather than a change of notation.

It is worth remembering how concrete this apprenticeship was. Schatten was a young man attending lectures, solving exercises, and trying to turn new definitions into usable mathematical arguments. The seminar culture was famous, but it did not make every member's later career inevitable. The archive records the education he received; the subsequent history of war and migration explains why that education had to be carried into an entirely different institutional world.

## A pair of inputs, and the tensor-product problem

Suppose you have two independent kinds of data. The first lives in a vector space X, the second in a vector space Y. You might want a bilinear measurement: a number that depends linearly on the first input while the second is fixed, and linearly on the second while the first is fixed.

The simplest example is multiplication. If the first input is a number x and the second a number y, their joint contribution is x times y. For vectors, you can build similar paired objects. Write down a formal symbol meaning x paired with y. Mathematicians call it a simple tensor. The purpose is to encode the two-input linear structure in a single vector-like object.

Now allow sums of such pieces. Perhaps the first contribution is one pair and the second is another pair. Their sum is a tensor. It is crucial that a tensor can have several descriptions as a sum of simple tensors. Splitting one contribution into two, or changing the basis in either input space, can change the list of terms without changing the tensor itself.

Take a two-dimensional example. Let the first space have perpendicular unit vectors called e one and e two, and give the second space the same kind of basis. Form one paired object from e one with e one, and another from e two with e two. Add them. This object has two independent components. It is the tensor counterpart of the identity matrix: one unit of action in the first direction, another in the second.

If we change the orthonormal basis by rotating it, the identity transformation remains the identity. We can express it using the new basis pairs. A definition of its size should not be an arbitrary function of whichever particular list of pairs we wrote first.

This is where a norm becomes more than a formula. A norm assigns a nonnegative size to every tensor, gives size zero only to the zero tensor, scales predictably with multiplication by a scalar, and obeys the triangle inequality. But those familiar rules do not tell us which norm to choose on the tensor product of X and Y. Even if both starting spaces already have perfectly good norms, the combined space can admit several useful norms.

Schatten's central insight was to treat those choices systematically. He studied crossnorms: norms for which a simple tensor, one made from exactly one vector x and one vector y, has size equal to the product of the sizes of x and y. The rule sounds compulsory. If one input doubles, the paired object should double; if the other input triples, it should triple. Yet that requirement on simple tensors does not uniquely determine the size of a sum of simple tensors.

The freedom remaining after the simple case is exactly the interesting part. We need to decide how independent contributions can reinforce one another, cancel one another, or be combined in different representations. The finite example of the two-direction identity will make those choices audible.

## Two natural crossnorms give different answers

Return to the tensor formed from e one paired with e one, plus e two paired with e two. Imagine that a tensor is used as a rule for a bilinear measurement. Feed it two unit vectors, one in each space, and ask how large the resulting pairing can be. Maximize the absolute value over all possible unit inputs. In the two-dimensional identity example, that maximum is one. This is the idea behind the injective tensor norm: test the tensor using bounded measurements on the two constituent spaces, and take the largest response.

There is another approach. Instead of asking for the largest response to a pair of tests, try to assemble the tensor from simple pieces as economically as possible. For each proposed decomposition, multiply the norms of the two vectors in each piece and add those products. Then take the infimum over every possible decomposition. The resulting number is called the projective tensor norm. It measures the cheapest total budget of simple tensors needed to build the object.

For our two-direction identity, the projective norm is two. We can see an upper bound of two immediately: use the two obvious perpendicular pieces, each costing one. The matching lower bound comes from a trace test. Any decomposition of the identity into rank-one pieces must have a total product-of-lengths budget at least two, because the trace of the identity is two and each rank-one contribution can contribute no more than its product-of-lengths budget to the trace.

So the same tensor has injective norm one and projective norm two. Both respect the rule that a single simple tensor has norm equal to the product of its two vector lengths. Both are legitimate norms. They give different values only when several simple tensors interact. The difference is part of the mathematical structure, not an inconsistency.

In a Hilbert-space setting there is also a third natural measure. Regard the four possible pairs of perpendicular basis vectors as perpendicular directions in a new Hilbert space. Then our tensor has two coefficients equal to one, so its Hilbert-space norm is the square root of two. We now have a trio of measurements for the same object: one, square root of two, and two. They mirror the operator norm, Hilbert–Schmidt norm, and trace norm of the identity matrix.

This is more than a numerical coincidence. In the finite Hilbert-space case, tensors can be identified with matrices, after choosing the appropriate dual or conjugate space. Under that identification, the injective norm becomes the operator norm, the Hilbert tensor norm becomes the Hilbert–Schmidt norm, and the projective norm becomes the trace norm. The structures we met at the beginning are three ways of completing the same basic finite-rank objects.

Now the intellectual attraction of Schatten's work comes into focus. Rather than discovering one isolated formula for singular values, he asked how norms on products of spaces behave, how they interact with duality, and what happens when the finite linear combinations are completed. This was a route from finite-dimensional geometry to an architecture for infinite-dimensional operators.

## Leaving Europe, and a second mathematical education

The chronology of Schatten's move to America is now better documented than it was when early biographies were written. Passenger records show him arriving in New York in September 1936. Records also identify a subsequent entry from Cuba in February 1938. The precise details of where he lived in every intervening month are less certain. It is safer to describe his migration as a documented sequence than to turn it into a single dramatic moment whose details we do not know.

In New York, he studied at Columbia University. He earned a master's degree there in 1939 and worked for his doctorate under Francis Joseph Murray. Murray was already part of the operator-algebra story. In the 1930s he had collaborated with John von Neumann on rings of operators, a program in which infinite-dimensional transformations were studied as collections closed under operations such as multiplication and taking adjoints. Schatten entered a research environment interested in the same sort of question that had occupied him in Lwów: what structures survive when the spaces become infinite?

His doctoral research concerned the direct product of Banach spaces. A Banach space is a normed vector space in which Cauchy sequences converge. Completeness allows us to build approximations and know that their limits remain within our world of admissible objects. Schatten's early papers of 1943 treated norms and reflexive norms on direct products. A 1946 paper examined the cross-space of linear transformations. These were not merely chapters in a later book. They were part of the original research that made the theory possible.

During the Second World War, Schatten entered the United States Army. The same period severed the connections he had left behind in Europe: biographical accounts report that his relatives in Poland were murdered during the Holocaust. His professional life in America continued, but the war had altered both his family world and the conditions under which he could work.

During American military training, Schatten suffered a broken back that troubled him physically for the rest of his life. He had already crossed an ocean and rebuilt his academic career; now bodily pain became part of the conditions under which he worked. The surviving accounts do not let us reconstruct every private consequence of the injury. But they prevent us from imagining the papers written at Princeton and Kansas as the products of an entirely comfortable research life. He continued working on questions about norms and completions while the world around him and his own circumstances had changed radically.

After military service, Schatten taught at the University of Vermont. He held a National Research Council fellowship that took him to the Institute for Advanced Study and to Yale. There he collaborated with von Neumann and with Nelson Dunford. The Institute's own membership record confirms his successive stays in the mid-1940s and his later returns in 1950 and the early 1950s.

There is a direct line from this institutional history to the mathematics. Murray's study of operator rings, von Neumann's work on matrix norms and Hilbert spaces, Dunford's expertise in linear operators, and Schatten's study of tensor norms were related but distinct programs. Schatten was in a position to help connect them. He could move between the language of abstract Banach spaces and the concrete operators that act on Hilbert space. The published collaborations of the 1940s show that this was more than a retrospective description.

## Collaborating on the cross-space of linear transformations

Let us return to the finite tensor that represented the identity matrix. In finite dimensions the translation from a tensor to an operator is straightforward. A pair of vectors can represent a rank-one transformation: take the inner product of an input with one vector, then multiply the other vector by that number. Add several such rank-one pieces and you get a general matrix.

But in infinite dimensions, a sum of rank-one transformations might involve infinitely many terms. What does it mean for that series to converge? If we use the operator norm, we control only the worst amplification of an input. If we use the trace norm, we are controlling the total amount of rank-one activity in a stronger sense. Different completions of the same finite-rank operators produce different spaces.

This is the point of the papers written by Schatten and von Neumann in 1946 and 1948, both titled The Cross-Space of Linear Transformations, with the second and third installments published jointly. Schatten had published the first installment alone. The sequence investigated how crossnorms and their associated spaces can represent linear transformations. Their work was collaborative; it is a mistake to describe the whole project as either a consequence of von Neumann's earlier matrix norm theorem or a solo discovery by Schatten.

Here is a way to feel the role of completion. Begin with transformations that affect only finitely many perpendicular directions. On such finite-rank transformations, the operator norm is well defined. Complete them using that norm, and on an infinite-dimensional Hilbert space you obtain the compact operators: those that can be approximated in operator norm by finite-rank transformations.

Instead complete the finite-rank transformations using the trace norm. You obtain a smaller space, the trace-class operators. Membership now requires that all singular values have a finite sum. The same finite-rank operators are dense in both spaces, but the resulting spaces differ because the measurements of their approximation errors differ.

The operator associated with the identity on an infinite-dimensional Hilbert space cannot be approximated by finite-rank operators in operator norm. Any finite-rank approximation leaves at least one unit direction untouched, and the error on that direction is still one. Therefore the identity is not compact. This is a useful warning that finite-dimensional intuition does not extend merely by declaring that there are infinitely many rows and columns.

For a compact diagonal operator whose singular values tend to zero, finite-rank truncations do converge in operator norm. But their convergence in trace norm is a separate question: we must add the omitted singular values. This difference gives an audible meaning to Schatten's theory. Choosing a norm decides which sequences are Cauchy, which operators exist in the completed space, and which limiting arguments are legitimate.

## An infinite diagonal example that separates the ideals

Consider the Hilbert space of square-summable sequences. Its elements are infinite lists whose squared entries have a finite sum. Define a diagonal operator that multiplies the first coordinate by one, the second by one half, the third by one third, and so on. Let us call it T.

This transformation becomes weaker on later coordinate directions. The strengths one over n tend to zero, so T is compact. If we keep only the first hundred diagonal entries, the largest discarded singular value is one over one hundred and one. As we keep more entries, that operator-norm error tends to zero.

Now ask about the Hilbert–Schmidt norm. Square each singular value and add: one, one quarter, one ninth, and so on. That series converges. Thus T belongs to the Hilbert–Schmidt class. Moreover, the Hilbert–Schmidt error of a truncated approximation is the square root of the remaining sum of reciprocal squares. It also tends to zero.

The trace norm gives a different answer. Its defining sum is one plus one half plus one third and so forth. That harmonic series diverges. T does not belong to the trace class. In particular, there is no finite trace norm for this operator, even though its operator norm is one and its Hilbert–Schmidt norm is finite.

We can change the example slightly to see a whole family of thresholds. Suppose the nth singular value is one divided by n raised to the power three quarters. Its pth powers are reciprocal powers of n with exponent three quarters times p. That numerical series converges precisely when the resulting exponent is greater than one. Consequently, the operator belongs to the Schatten classes for p greater than four thirds, but not to the class at p equal to four thirds, and not to classes with smaller p.

This calculation makes ideal membership tangible. The word ideal here refers to an algebraic stability property, not to a subjective judgment about which measurement is best. If an operator belongs to one of these classes, multiplying it on either side by an arbitrary bounded operator keeps it in the same class. The norm changes by at most the appropriate operator-norm factor.

Think of an input being filtered by one device, passed through a trace-class transformation, and then filtered again by another bounded device. The bounded devices may rotate or scale directions, but they cannot transform finite total trace-class size into an infinite total. That stability is what makes an operator class useful inside proofs. One can move through factorizations without leaving the category of controlled transformations.

A second structural fact is easy to miss: smaller p imposes a stronger membership requirement. A finite sum of singular values is more demanding than a finite sum of their squares. So trace class is contained in Hilbert–Schmidt, which in turn is contained in the compact operators. The inclusions are genuine; the reciprocal-diagonal example shows that the first one cannot be reversed.

## Duality: why the trace turns two operators into one number

A major attraction of the tensor viewpoint is that it brings duality into the picture. A dual space consists of bounded linear measurements of vectors. If you know the measurements, you can often recover a great deal about the vector being measured. Schatten's crossnorm work paid close attention to how the dual of a completed tensor product relates to spaces of linear transformations.

In matrix form, there is a particularly useful pairing. Take two matrices, multiply the adjoint of the first by the second, and take the trace. The result is a number. This pairing measures how the two transformations align. It is the matrix analogue of an inner product when both matrices are Hilbert–Schmidt.

Start with diagonal matrices whose entries are three and one, and two and four. Their trace pairing is three times two, plus one times four, which makes ten. If you rotate one matrix's singular directions, the pairing can change. But there is a bound that depends only on the singular values: the absolute trace pairing is no larger than the sum obtained by matching the singular values in decreasing order. This is von Neumann's trace inequality, and its historical attribution belongs to von Neumann's 1937 work, not to a later eponymous Schatten norm.

The trace inequality suggests that different norms are linked by a generalized form of the familiar Cauchy–Schwarz inequality. If both operators are Hilbert–Schmidt, their trace pairing has absolute value no greater than the product of their Hilbert–Schmidt norms. If the first is trace class and the second is bounded, the pairing is controlled by the trace norm of the first times the operator norm of the second.

There are also intermediate versions. Let p and q be positive exponents at least one, chosen so that the sum of their reciprocals is one. If one operator is in the Schatten p class and the other in the Schatten q class, their product is trace class and its trace norm is bounded by the product of those two class norms. This is an operator version of Hölder's inequality. It is not a license to apply a scalar estimate to matrix entries one at a time; singular-value inequalities are doing the work.

For an especially clear case, choose p and q both equal to two. The product of two Hilbert–Schmidt operators is trace class. If their Hilbert–Schmidt norms are finite, the total singular-value size of the product is controlled. The conclusion is stronger than simply saying that the product is bounded.

One can understand the two endpoints through dual spaces. On a Hilbert space, bounded operators pair with trace-class operators through the trace. More precisely, the Banach dual of the compact operators is the trace class, and the dual of the trace class is the bounded operators. Between them, for p strictly between one and infinity, the dual of the Schatten p class is the corresponding conjugate-exponent class. These statements require the appropriate completed spaces and trace pairing, not merely finite matrices.

Schatten did not prove every theorem in this modern package first. The point of the history is to see how the abstract language of crossnorms and norms on transformation spaces made such theorems natural to formulate and organize.

## The 1950 and 1960 books: building a subject

In 1950, Schatten published A Theory of Cross-Spaces as a volume in Princeton's Annals of Mathematics Studies. The book collected and organized a program on normed tensor products. In its acknowledgments he recognized the importance of his work with John von Neumann and their later correspondence. The 1946 and 1948 joint papers were part of the published background, and the book was Schatten's sustained exposition of the subject.

A reader encountering a modern edition should watch the dates. The Princeton book originated in 1950, though a widely listed paperback was issued in 1985. Dating the mathematics by the paperback reissue would displace it by thirty-five years and obscure its position in the development of functional analysis.

The book answered a larger question than how to add the singular values of one operator. It classified ways of building normed tensor spaces, compared natural crossnorms, and studied dual and associated norms. The choice of a completion was tied to an intended kind of transformation. The resulting theory could be used to understand which linear maps admit approximation by finite-rank maps in a given sense.

The 1950s brought further developments in tensor products, especially in the work of Alexander Grothendieck. Historical accounts distinguish the early program of Schatten and his collaborators from Grothendieck's later general theory. It would be inaccurate to compress the whole sequence into one person's invention. Schatten established important terminology and constructions; other mathematicians extended and reorganized the field in ways that became central to subsequent research.

A decade later, in 1960, Schatten published Norm Ideals of Completely Continuous Operators. The older term completely continuous, in this Hilbert-space context, refers to compact operators. The book presented classes of operators equipped with norms strong enough to control more than their worst-case action. It explored the geometry of the ideal norms and how they sit within bounded-operator theory. The volume was short, but its subject was a demanding one: identifying stable categories of infinite-dimensional transformations and the dual relationships among them.

These books also illustrate why historical names can mislead. We often meet a mathematical concept in the simplified form suitable for a course: take singular values, raise them to a power, add them. The original research program frequently begins somewhere else, with questions about constructing new spaces and proving that they behave properly. The formula is the convenient visible surface of a much larger structure.

## A problem of approximation, and a surprising limit

There is another way Schatten's theory affects mathematical practice. Take a compact operator with singular values five, two, and one. Suppose you can afford to keep only one independent direction. Which rank-one approximation should you choose?

The natural answer is to keep the strongest direction, the one with singular value five, and discard the other two. For the operator norm, the remaining error is two: the largest omitted singular value. For the Hilbert–Schmidt norm, the error is the square root of two squared plus one squared, or the square root of five. For the trace norm, the error is two plus one, which is three.

The best rank-one approximation has the same geometric form in all three cases, but its reported error depends on the norm. This is an instance of the Eckart–Young–Mirsky approximation theorem and related singular-value inequalities. Schatten's contribution is not that he alone discovered this rank-approximation theorem. His theory supplies a vocabulary of norms and operator ideals in which such a question can be asked and generalized.

In the infinite-dimensional setting, approximate a compact diagonal operator by keeping only its first many singular directions. The operator-norm error is the next singular value. The Hilbert–Schmidt error comes from the sum of the squares in the remaining tail. The trace-norm error comes from the sum of the remaining singular values. Thus convergence of the same sequence of finite-rank approximations depends on which notion of total error we choose.

This is useful whenever a finite calculation is being asked to stand in for an infinite problem. A small operator-norm error means no single unit input suffers a large discrepancy. A small Hilbert–Schmidt error controls aggregate squared discrepancy across an orthonormal family. A small trace-norm error controls an even stronger aggregate quantity and behaves well when paired with bounded observables.

Think of approximating a quantum state by a finite-dimensional density matrix. Trace norm is valuable because it controls the change in expectation against every bounded observable with operator norm at most one. Think instead of approximating a noisy linear transformation by a low-rank model. Hilbert–Schmidt error may describe the total squared residual energy. There is no universally correct norm; the mathematical task determines which kind of control has meaning.

## Teaching, students, and a life in American universities

Schatten joined the University of Kansas in 1946. He spent many years there, first as an associate professor and later as a professor, interrupted by research visits including returns to the Institute for Advanced Study. Later appointments took him to the University of Southern California, Stony Brook, and Hunter College in New York, where he taught from 1962 until his death in 1977.

The biographical picture includes something more personal than publication lists. Former students remembered a lecturer who often spoke without notes and used the blackboard sparingly. His arguments were organized so that students could write down an almost complete account as he spoke. He had a distinctive way of making abstract definitions concrete. To explain an infinite sequence, he imagined a long corridor with regularly spaced numbered hooks and a bag of numbers: the first number goes on the first hook, the second on the second, and so on. That is a teaching example reported by his students, not an invented scene.

The long corridor and its numbered hooks are especially fitting for the subject of this lecture. An infinite sequence is easy to write as three dots and hard to imagine as an object. Schatten offered a mental walk down a corridor to give every coordinate a definite place. Then the same class could ask what happens when the numbers hung on those hooks have to satisfy a summability condition. The move from a picture to a normed sequence space mirrors the way he organized his research: begin with an intelligible construction, and insist on the conditions that make the infinite object mathematically legitimate.

The former students' recollections are specific enough to let us hear the room. Schatten often dispensed with both a textbook and a blackboard. He dictated arguments at a pace carefully matched to the students' writing, and they were expected to take the words down accurately. The resulting notebooks, students said, could read almost like finished books. Even his endings had a recognizable formula: he would announce that the proof was concluded. This exacting performance could sound severe, but the same recollections insist that he cared deeply about whether students developed mathematical understanding. He was painstakingly orderly because, in his view, a difficult argument ought to be reconstructible.

One of his doctoral students was Elliott Ward Cheney, who became an influential figure in approximation theory. Other students worked on gauge functions and operator ideals. This is a direct intellectual continuation of Schatten's research: how to build norms, how to control approximations, and how to make infinite-dimensional spaces manageable.

Friends also remembered an exacting man with remarkably ordinary frustrations. He disliked noise, especially when it disturbed his sleep. A recollection from Lawrence, Kansas, has him out in the garden in pajamas, trying to drive noisy birds from a tree. He never became comfortable driving, and his battles with laundries that ironed his socks became part of the stories his friends told. More revealing for his professional life is another reported habit: he placed unpublished mathematical manuscripts in a bank safe-deposit box. The impulse toward careful preservation fits the lecturer who controlled every step of his proofs, though we need not invent a psychological theory to connect them.

His students could remember the rhythm of a lecture and his friends could recall the small battles of daily life. No such recollections give us his private response to family loss. But together with the surviving papers, they offer a fuller person than the name attached to a norm: a demanding teacher who cared about explanation, a migrant who continued working through upheaval, and a researcher whose carefully defined spaces became useful to many people.

Robert Schatten died in New York on 26 August 1977. His mathematical name lived on in textbooks, but his contributions extend beyond the particular symbols bearing his name. He helped construct a language in which abstract combinations of vector spaces and concrete transformations on Hilbert space could be studied together.

## A final connection: measuring an entire spectral subspace

Let us close with a question that ties his work to perturbation theory. Suppose an operator has a spectral subspace spanned by several perpendicular directions, and a small change in the operator rotates that subspace. We can describe each rotation by a principal angle. If there are many angles, which measure of total displacement should we use?

One possibility is to care only about the worst angle. Then an operator norm is natural. Another is to add up the squares of all the directional displacements, which leads to a Hilbert–Schmidt measurement. A third may weight the total amount of displacement through a trace norm. Each gives a different description of how many directions were affected and by how much.

In a finite-dimensional problem, these choices are available for every pair of subspaces. In infinite dimensions, one must ask whether the relevant displacement operator belongs to the chosen ideal. An operator with finite Hilbert–Schmidt displacement may fail to have finite trace-class displacement. A theorem expressed in one norm cannot be copied into another with the same bound simply because the norms share a formula involving singular values.

That is a modern application of the framework, rather than a claim that Schatten proved the later Davis–Kahan spectral-subspace perturbation bounds. Those bounds require their own hypotheses about spectral gaps and operator changes. Schatten's legacy is part of the infrastructure that lets us ask how much of a subspace moved, instead of reducing every problem to the single worst direction.

Return once more to the two-direction identity tensor. Depending on how we measure it, its size is one, the square root of two, or two. We learned that all three measurements are coherent because they ask different questions. Schatten's research explained how to carry such distinctions beyond matrices of fixed size, into completed spaces of infinite-dimensional transformations, without losing the algebraic and geometric controls needed for proofs.

The lasting answer to our opening question is therefore conditional and precise. To measure an infinite-dimensional transformation, choose the kind of behavior you need to control, construct the corresponding normed space, and verify that your transformation belongs to it. Only then does an infinite sum of singular values become a legitimate mathematical quantity. That is the path from a small matrix calculation to Robert Schatten's theory of operator ideals.

<!-- END SPOKEN LECTURE -->

---

## Mathematical and historical companion (display only)

### 1. Crossnorms and finite-dimensional Hilbert tensors

For normed spaces \(X,Y\), an algebraic tensor \(u\in X\otimes Y\) is a finite sum
\(u=\sum_{j=1}^m x_j\otimes y_j\), with equivalences arising from bilinearity.
A crossnorm \(\alpha\) obeys \(\alpha(x\otimes y)=\|x\|_X\|y\|_Y\). Two canonical choices are

\[
\begin{aligned}
\pi(u)&=\inf_{u=\sum_jx_j\otimes y_j}\sum_j\|x_j\|\|y_j\|,\\
\varepsilon(u)&=\sup_{\|f\|_{X^*}\le1,\,\|g\|_{Y^*}\le1}|(f\otimes g)(u)|.
\end{aligned}
\]

On \(H=\mathbb R^2\), identify \(H\otimes H\) with real \(2\times2\) matrices by \(x\otimes y\mapsto xy^T\). For
\(u=e_1\otimes e_1+e_2\otimes e_2\leftrightarrow I_2\),

\[
\varepsilon(u)=\|I_2\|_{\mathrm{op}}=1,\qquad
\|u\|_{H\otimes_2H}=\|I_2\|_{\mathrm{HS}}=\sqrt2,\qquad
\pi(u)=\|I_2\|_{S_1}=2.
\]

The upper bound \(\pi(u)\le2\) uses the displayed two-term decomposition.
For any \(I_2=\sum_j x_jy_j^T\),
\(2=\operatorname{Tr}I_2=\sum_jy_j^Tx_j\le\sum_j\|x_j\|\|y_j\|\), hence \(\pi(u)\ge2\).
For complex Hilbert spaces use \(H\otimes\overline H\) and map \(x\otimes\bar y\mapsto xy^*\).
The completions with \(\varepsilon\), Hilbert-tensor norm, and \(\pi\) correspond, respectively, to \(K(H)\), \(S_2(H)\), and \(S_1(H)\) in the standard Hilbert setting.

### 2. Singular-value gauges and Schatten classes

For a compact operator \(T\), let \(s_1(T)\ge s_2(T)\ge\cdots\to0\) be the eigenvalues of \(|T|=(T^*T)^{1/2}\), counted with multiplicity. For \(1\le p<\infty\),

\[
S_p(H)=\left\{T\in K(H):\sum_{j\ge1}s_j(T)^p<\infty\right\},\quad
\|T\|_{S_p}=\left(\sum_j s_j(T)^p\right)^{1/p}.
\]

\(S_1\) is trace class and \(S_2\) is Hilbert–Schmidt. Many authors write \(S_\infty=K(H)\) equipped with the operator norm, while others use \(S_\infty=B(H)\); the distinction is substantive and is specified when needed. Schatten's 1960 monograph develops norm ideals of compact operators; the modern pedagogical definitions here should not be mistaken for the precise original arrangement of his proofs.

For \(D=\operatorname{diag}(3,1)\):
\(\|D\|_{S_1}=4\), \(\|D\|_{S_2}=\sqrt{10}\), and \(\|D\|_{\rm op}=3\).
For \(T_ae_n=n^{-a}e_n\),

\[
T_a\in S_p\iff \sum_{n=1}^\infty n^{-ap}<\infty\iff ap>1.
\]

Thus \(T_1\in S_2\setminus S_1\), and \(T_{3/4}\in S_p\) exactly for \(p>4/3\) (finite \(p\)); both are compact. Finite-rank truncations \(T_a^{(N)}\) obey

\[
\|T_a-T_a^{(N)}\|_{\rm op}=(N+1)^{-a},\qquad
\|T_a-T_a^{(N)}\|_{S_p}^p=\sum_{n>N}n^{-ap},
\]

with the latter expression finite only if \(ap>1\). For \(T_1\), the Hilbert–Schmidt tail tends to zero while the trace-norm tail diverges for every finite \(N\).

### 3. The operator-ideal property, Hölder and duality

For \(T\in S_p(H)\) and \(A,B\in B(H)\),

\[
ATB\in S_p(H),\qquad
\|ATB\|_{S_p}\le\|A\|_{\rm op}\|T\|_{S_p}\|B\|_{\rm op}.
\]

For \(1/p+1/q=1\) with \(1\le p,q\le\infty\), the Schatten Hölder estimate is
\(\|AB\|_{S_1}\le\|A\|_{S_p}\|B\|_{S_q}\),
with the bounded-operator endpoint interpreted as \(B(H)\) rather than only compact operators. At \(p=q=2\) this becomes the Hilbert–Schmidt product estimate. Also,

\[
|\operatorname{Tr}(A^*B)|\le\sum_j s_j(A)s_j(B)
\]

for finite matrices, with appropriate trace-class products in infinite dimensions. This is the 1937 von Neumann trace inequality; no exclusive attribution to Schatten is intended.

Under the trace duality, \(K(H)^*\cong S_1(H)\),
\(S_1(H)^*\cong B(H)\), and \(S_p(H)^*\cong S_q(H)\) for \(1<p<\infty\), \(1/p+1/q=1\).

### 4. Low-rank approximation and comparison of objectives

For \(D=\operatorname{diag}(5,2,1)\), best rank-one approximation (in every Schatten \(p\)-norm, and in operator norm) is \(D_1=\operatorname{diag}(5,0,0)\); the remaining singular values are \((2,1)\). Hence

\[
\|D-D_1\|_{\rm op}=2,\qquad
\|D-D_1\|_{S_2}=\sqrt5,\qquad
\|D-D_1\|_{S_1}=3.
\]

This is a modern Eckart–Young–Mirsky example, not an original theorem attributed to Schatten.
A trace-class perturbation of a density operator obeys
\(|\operatorname{Tr}((\rho-\sigma)B)|\le\|\rho-\sigma\|_{S_1}\|B\|_{\rm op}\).
A spectral-subspace displacement measured using \(S_p\) similarly requires ideal membership for the relevant operator. This is mathematical application, not attribution of a later Davis–Kahan bound to Schatten.

### 5. Historical chronology and attribution

- **1911–1933:** Born Rubin Schatten on 28 January 1911 in Lemberg/Lwów (now Lviv); educated at Jan Kazimierz University and completed a 1933 master's thesis *Przestrzenie abstrakcyjne* under Stefan Banach. The 2023 archival study supplies documentary evidence including the thesis cover and university records.
- **1936–1938:** Passenger records document the September 1936 arrival from Gdynia and a February 1938 entry from Havana. The exact intervening itinerary is incompletely documented; do not assert a single uninterrupted or simple arrival narrative.
- **1939–1943:** M.A. at Columbia in 1939, doctoral research with Francis J. Murray; accounts variously date degree award to 1942 and formal promotion to 1943. The 1943 papers originate in the doctoral work. Served in the U.S. Army 1942–43 and sustained a serious lasting training injury.
- **1943–1948:** Vermont, IAS, Yale; coauthored 1946 paper with Nelson Dunford, and 1946/1948 *Cross-Space of Linear Transformations* II/III with John von Neumann. Part I was Schatten's 1946 single-author paper. IAS membership dates are independently documented.
- **1946–1977:** University of Kansas; later USC, Stony Brook, and Hunter College; mentored Elliott W. Cheney, Peter Falley, and Charles Masiello. Student recollections in Cheney's memorial biography describe his precise, mostly oral classroom exposition.
- **1950 / 1960:** *A Theory of Cross-Spaces* originally 1950, reissued 1985; *Norm Ideals of Completely Continuous Operators* originally 1960, reprinted 1970. Do not use modern reprint dates to date the mathematical work.
- **Personal loss:** Family members were killed during the Holocaust. The research record gives meaningful documentation without supporting imagined dialogue, detailed private motives, or a reconstruction of all family relationships.
- **Mathematical priority:** Schatten was a pioneer of Banach-space tensor norms and normed operator ideals. Von Neumann's unitarily invariant matrix-gauge theorem dates to 1937. Grothendieck's 1950s tensor-product program made additional, substantially different contributions. The mathematical consequences named in this companion should not be assumed to be individually original to Schatten.

### 6. Recommended research entry points (non-spoken)

Read Lech Maligranda and Yaroslav Prytuła, *Rubin (Robert) Schatten (1911–1977)* (2023), for archival biography, primary-paper bibliography, and technical historical context. The MacTutor biography, authored by Elliott W. Cheney, preserves student recollections. Consult Schatten's 1943 papers and the coauthored 1946/1948 papers for the historical tensor-norm development, the 1950 monograph for the completed cross-space program, and the 1960 book for norm-ideal theory. The Institute for Advanced Study membership record independently documents the Princeton visits. All source IDs and verified links are in the adjacent `metadata/011000.json` sidecar.
