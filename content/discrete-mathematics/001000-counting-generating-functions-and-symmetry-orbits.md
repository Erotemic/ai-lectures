# Counting, generating functions, and symmetry orbits

<!-- BEGIN SPOKEN LECTURE -->

# Counting, generating functions, and symmetry orbits

## Counting by correspondence, cancellation, and generating series

### Bijections and Double Counting: Proving Equations by Counting Objects

Suppose a committee of five people must choose a chair and a secretary, and the roles must go to different people. There are five choices for the chair, followed by four choices for the secretary: twenty assignments. If we reverse the order of selection, there are still twenty. That is unsurprising. But what if someone offers a much more complicated formula for the same count? Can we prove the two formulas agree without expanding them algebraically?

Combinatorics turns this into a method. Describe a finite collection of objects, count it in two ways, and use the equality of the counts to prove an identity. The power is not in clever arithmetic. It is in being precise about what constitutes one object, and about why none is omitted or counted twice.

#### The product rule is a reversible description

If a construction has a first choice from a set of m possibilities, followed by a second choice from n possibilities regardless of the first, then there are m times n ordered pairs. If the second choice depends on the first, we add the number of available second choices over all first choices instead. Confusing these two cases is one of the easiest ways to miscount.

For a chair and a secretary chosen from five people, the second role has four choices after the first is fixed. The answer is five times four. We cannot use five squared because selecting the same person twice is forbidden. If we do allow the same person in both roles, we do get five squared. The numerical difference encodes a difference in the objects being counted.

A bijection is a one-to-one correspondence between two sets. If the sets are finite, a bijection proves they have the same size. A particularly useful bijection may be simple to describe even when the two sets look unrelated. For instance, a subset of a set of n labeled elements corresponds to a string of n yes-or-no choices, one per element. Every subset determines exactly one string, and every such string determines exactly one subset. There are two choices at each position, hence two to the n subsets.

Notice that the proof has two parts. We defined a map from subsets to strings and explained its inverse. Merely saying “it seems like the same information” would not be enough if different objects could lead to the same string.

#### Choose k elements without remembering order

Suppose a group of n people must choose a committee of exactly k people. We can first count ordered lists of k distinct people. The first position has n choices, the second n minus one, and so on, through n minus k plus one. Each actual committee, however, gives rise to k factorial different orders. Divide by that number to count committees rather than arrangements.

This produces the binomial coefficient: n factorial divided by k factorial times n minus k factorial. The formula is valid for integers n at least zero and k between zero and n. Outside that range we may adopt the convention that the coefficient is zero, but the original combinatorial interpretation has to be stated carefully.

There is a second way to understand the same coefficient. Fix a distinguished person, call her Ada. Committees of size k split into two disjoint cases: those containing Ada and those not containing Ada. In the first case we choose k minus one more members from the other n minus one people. In the second case we choose all k from those n minus one. Therefore the number of k-subsets of n elements equals the number of k-minus-one subsets of n-minus-one plus the number of k-subsets of n-minus-one.

This is Pascal's identity. We proved it by partitioning a single collection into disjoint cases, not by simplifying factorials. The same argument generates Pascal's triangle, where each interior entry equals the sum of the two entries directly above it.

#### Double count an incidence relation

Now take an undirected graph with a finite collection of vertices and edges. A vertex's degree is the number of incident edge ends; a loop contributes two, because it has two ends at the same vertex. Count all pairs consisting of a vertex and an edge end incident to it.

If we choose the vertex first, the count is the sum of the degrees of all vertices. If we choose an edge first, every edge has exactly two ends, so the count is twice the number of edges. Both procedures count exactly the same incidences. We have proved the handshake lemma: the sum of degrees in a finite undirected graph is twice the number of edges.

An immediate result is that the number of vertices of odd degree is even. The sum of all even degrees is even, and the sum of all degrees is even. So the sum of the odd degrees is even. But a sum of an odd number of odd integers is odd. Therefore there must be an even number of odd-degree vertices.

This conclusion may be used to rule out a proposed network without drawing every possible edge. A claimed graph with exactly three vertices of odd degree cannot exist. An identity obtained by counting becomes a structural constraint.

#### A more demanding double count

Consider all subsets of an n-element set, and ask for the total number of times an element appears across every subset. One way to count is to look at each of the n possible elements. Once an element is required to be present, each of the other n minus one elements may be independently included or excluded. So each element occurs in two to the n-minus-one subsets. Across all n elements, the total number of element-subset incidences is n times two to the n-minus-one.

Another way is to group the subsets by their size. There are n choose k subsets containing k elements, so the total number of incidences is the sum, over k from zero to n, of k times n choose k. The two counts are equal.

That gives a binomial identity with a particularly transparent explanation. It also demonstrates how to choose the right object to count. We did not count subsets alone. We counted pairs consisting of a subset and a distinguished member of that subset. The extra mark made the identity visible.

This trick generalizes. If an identity contains a factor k, perhaps choose an object of size k and mark one of its components. If it contains a factor k times k minus one, perhaps mark an ordered pair of distinct components. The algebra can suggest which combinatorial object to invent.

#### The pigeonhole principle is also counting

Suppose n plus one letters are placed in n labeled boxes. At least one box contains two or more letters. If each box contained at most one, the total number of letters would be at most n, contradicting the premise. This is the pigeonhole principle in its simplest form.

A more quantitative version says that putting N objects into m boxes forces some box to contain at least the ceiling of N divided by m objects. If every box held fewer, the total capacity would be too small.

The principle becomes powerful when boxes represent mathematical patterns. Among thirteen people, at least two were born in the same month. Among six integers, two have the same remainder modulo five. Subtract those two integers and their difference is divisible by five. We have proved the existence of a divisible difference without examining any actual values.

The second example is especially revealing. Pigeonhole does not tell us which pair works; it proves that some pair must. Combinatorial existence theorems often work this way. A construction or an algorithm might be a separate problem.

#### What makes a counting proof rigorous

Every successful counting argument answers three questions. What are the objects? Why does the first procedure count every one exactly once? Why does the second procedure do the same? If we divide by a symmetry factor, why does each object have exactly that many descriptions? If we split into cases, are the cases disjoint and exhaustive? If we use a bijection, can we construct its inverse?

When those questions are settled, the identity is not a lucky algebraic simplification. It is a theorem about a finite structure.

The discipline carries into algorithm analysis, probability, graph theory, algebra, and geometry. A graph's degree sum, the coefficients in a binomial expansion, and the number of subsets containing a designated element are all instances of the same intellectual move: count what really exists, and compare two faithful descriptions of it.

### Inclusion–Exclusion: Counting When Cases Overlap

Imagine a conference registration list. Some attendees requested vegetarian meals. Some requested a seat near the front. We want to count people who made at least one of those requests. If we add the two request counts, someone who made both requests gets counted twice. Subtract the overlap, and the problem is solved.

With two conditions, this correction is familiar. With ten conditions, the overlaps form a complicated web: pairwise intersections, triple intersections, and so on. Inclusion–exclusion gives a systematic way to untangle that web. It also leads to a celebrated answer to a different question: if n letters are randomly placed into n addressed envelopes, how many arrangements have no letter in its own envelope?

#### One overlap, then three

Let A be the set of people requesting vegetarian meals and B the set requesting front seating. Each person in only A or only B is counted once by the sum of the sizes of A and B. Each person in both is counted twice. Therefore the size of their union equals the size of A plus the size of B minus the size of their intersection.

With three conditions, begin by adding the sizes of A, B, and C. An object satisfying exactly two conditions is counted twice; subtract the three pairwise overlaps and it is counted once. But an object satisfying all three conditions was counted three times initially and subtracted three times, leaving zero. It needs to be added back once. The correct formula adds the three individual sizes, subtracts all three pairwise intersection sizes, and adds the size of the triple intersection.

The alternating pattern continues. For any finite family of conditions, sum the counts for single conditions, subtract the counts for pairs, add the counts for triples, and continue with alternating signs. If there are many conditions, writing every term may be impractical, but the principle is exact.

#### Why alternation works

Consider a particular object that satisfies exactly r of the conditions, with r positive. In the alternating sum, it is counted r times at the first stage, subtracted once for each pair of satisfied conditions, added once for each triple, and so on. Its total coefficient is r choose one, minus r choose two, plus r choose three, continuing through r.

The binomial theorem says the alternating sum of all the binomial coefficients from zero through r is zero when r is positive. Because the zero-th coefficient is one, removing it and changing the sign shows that the alternating sum starting at one equals one. So our object is counted exactly once, regardless of how many conditions it satisfies.

An object satisfying none of the conditions appears in no intersection and is counted zero times. That is precisely what we want for a union. This argument is a proof of inclusion–exclusion for any finite number of sets. It is also a warning about infinite families: extending the same alternating expression to infinitely many sets requires separate convergence and measure-theoretic justification. Our theorem is a finite counting statement.

#### The envelope problem

Suppose n different letters need to be placed into n distinct addressed envelopes, one letter per envelope. There are n factorial permutations of the letters. Let A sub i be the set of permutations that place letter i into its correct envelope. We want to count permutations outside every A sub i. Such permutations are called derangements.

For a fixed letter i, the number of permutations fixing i is n minus one factorial: arrange the other letters freely. For two specified letters, the count is n minus two factorial. For any chosen collection of k letters that must all remain in the correct envelopes, we can permute the remaining n minus k letters in n minus k factorial ways. There are n choose k ways to choose which k letters are prescribed to stay fixed.

Inclusion–exclusion first counts all permutations, subtracts those fixing at least one letter, adds back those fixing two specified letters, and so forth. The resulting count of derangements is n factorial times the alternating sum of one, minus one, plus one over two factorial, minus one over three factorial, continuing through the term at n.

For three letters this is six times the quantity one minus one plus one half minus one sixth, which is two. You can check the two surviving permutations directly: both are three-cycles. For four letters, the calculation gives nine derangements.

The formula is a pleasing example of why inclusion–exclusion is needed. We cannot count arrangements without fixed points by simply saying “each letter has n minus one choices.” Those choices are coupled: sending a letter into someone else's envelope removes a destination for all the others. The result must remain a permutation. Inclusion–exclusion respects that global constraint.

#### A surprising limiting fraction

Divide the derangement count by n factorial. We obtain the probability that a uniformly random permutation has no fixed points. As n grows, the finite alternating sum approaches the infinite series for the exponential function evaluated at negative one. Its limit is one divided by the mathematical constant e, approximately zero point three six eight.

The probability of no fixed points does not approach zero, even though there are more and more letters. Each additional letter provides a new opportunity to be correct, but the dependencies among destinations are balanced so the chance of avoiding all correct placements approaches a positive constant.

We can also bound the approximation error. The alternating-series theorem gives an error smaller than the magnitude of the first omitted term. Therefore the probability differs from one over e by at most one over n plus one factorial. Multiplying back by n factorial shows that the derangement count differs from n factorial divided by e by less than one over n plus one. For n at least one, that is at most one half, with strict inequality when n is positive. Hence the number of derangements is the nearest integer to n factorial divided by e. We reached an exact integer-counting formula by combining finite combinatorics with a controlled infinite-series estimate.

#### Counting surjections

The same method answers a different problem. How many functions from a set of n labeled inputs onto a set of m labeled outputs use every output at least once? Begin with all m to the n functions. For each target label, define the bad condition that this label is never used. To exclude one specified label, there are m minus one choices for every input; to exclude two, m minus two choices; and so on.

Inclusion–exclusion gives the alternating sum over k from zero to m of m choose k times m minus k to the n, with a sign that is negative for odd k and positive for even k. This counts onto functions, also called surjections.

For three inputs and two outputs, there are eight possible functions total. Two fail to be onto because all three inputs go to the first output or all three to the second. Thus there are six surjections. The formula gives eight minus two, agreeing with our direct count.

This result connects to set partitions. Every surjection onto m labeled boxes partitions the inputs into m nonempty fibers. If we erase the labels on the boxes, each partition has m factorial different labelings. So dividing the surjection count by m factorial gives the number of partitions of an n-element set into exactly m nonempty blocks, known as a Stirling number of the second kind. Here the division is justified because the output labels can be permuted freely and each resulting labeled arrangement is distinct.

#### Where inclusion–exclusion ends and judgment begins

The formula is exact, but using it efficiently depends on the problem. With many unrelated conditions, there can be exponentially many intersections to evaluate. In some problems those intersections have a simple form, as they did for fixed points of a permutation. In others, a recurrence, a generating function, a dynamic program, or a probabilistic bound may be preferable.

Another important distinction: inclusion–exclusion counts a finite union exactly, while the union bound in probability merely says the probability of at least one event is no greater than the sum of the event probabilities. The union bound drops all the overlap corrections. It may be coarse, but it remains useful when we cannot compute the intersections. A less precise theorem can be more computationally accessible.

The central lesson is that overlapping cases are not an obstacle to counting, provided we name the overlaps. Inclusion–exclusion is a disciplined accounting identity. Every object that satisfies r conditions receives an alternating coefficient of exactly one, and every object that satisfies none receives zero. Once we understand that, the envelope problem and the surjection formula cease to be isolated puzzles. They are applications of one mechanism.

### Generating Functions: Turn Counting into Algebra

Imagine that a shop sells packets containing two or three identical tokens. You want exactly twelve tokens. How many ways are there to choose a collection of packets, if the order of purchasing them does not matter? It is possible to solve this by trying a few cases. But what if the target were twelve thousand, or there were twelve packet sizes instead of two?

A generating function turns a count for every target into the coefficients of one formal expression. It is a way to make the operations we perform on objects correspond to algebraic operations on series.

#### Coefficients carry the information

Given numbers a-zero, a-one, a-two, and so on, write the expression a-zero plus a-one times x plus a-two times x squared, continuing indefinitely. This is the ordinary generating function of the sequence. The coefficient of x to the n is a-n. The variable x is initially only a marker of size, not a value to be chosen.

For example, the sequence one, one, one, one, continuing forever has generating function one plus x plus x squared and so on. Formally, this is one divided by one minus x, because multiplying by one minus x cancels every positive power of x and leaves one.

If you have seen geometric series in calculus, you may expect a condition such as the absolute value of x less than one. That condition matters when assigning a numerical value to an infinite sum. But we can work in the ring of formal power series instead. Two series are equal when all their coefficients agree. A coefficient of a product uses only finitely many terms, so the algebra makes sense without asking whether the series converges as a function of a real or complex number.

That distinction is particularly valuable in combinatorics: a generating function may encode an enormous sequence even when we never intend to substitute a numerical x.

#### Why multiplication counts combinations

Suppose a-n counts choices of an object of size n from one category, and b-n counts choices of an object of size n from another. To choose a pair with combined size n, we can give the first object size zero and the second size n, or size one and size n minus one, and so forth. The number of pairs is the sum of a-k times b at n minus k over all k from zero to n.

Exactly the same sum appears as the coefficient of x to the n when we multiply the generating functions. This coefficient rule is called convolution. Ordinary multiplication of power series is not merely an analogy for pairing choices: the distributive law explicitly lists every possible size split.

For example, a single kind of packet containing two tokens can be purchased zero, one, two, or more times. Its generating function is one plus x squared plus x to the fourth and so on: one divided by one minus x squared. Packets of size three similarly give one divided by one minus x cubed. Combining independent choices means multiplying the expressions.

The coefficient of x to the twelfth in one divided by the product of one minus x squared and one minus x cubed counts nonnegative integer solutions to two a plus three b equals twelve. We may choose six two-token packets and no threes, three twos and two threes, or no twos and four threes. There are exactly three possibilities.

The coefficient calculation encoded all of that. We did not need to write a separate expression for each target.

#### A product for many independent choices

If objects may have sizes one through k, with an unlimited number of each size, the generating function is the product over those sizes of one divided by one minus x to that size. The coefficient of x to the n counts partitions of n using only the allowed part sizes. Here order does not matter: a collection with two size-one parts and one size-three part is the same collection regardless of the order in which the parts are listed.

If each category may be used at most once instead, the factor becomes one plus x to the category's size. The product of these two-term factors counts subsets by total weight. If each category has exactly one item that must be chosen, we would use only x to that size. These are different counting problems, and the factors express the differences unambiguously.

A common source of errors is to use an unlimited-choice factor for a problem about arrangements, or a subset factor for a problem where repeated choices are permitted. The generating function cannot rescue an incorrect model of the combinatorial objects.

#### Stars, bars, and repeated factors

Take k distinguishable containers and place n indistinguishable tokens among them, allowing empty containers. Every container contributes the series one plus x plus x squared and so on. Because the containers are independently chosen and distinguishable, their combined generating function is one divided by one minus x, raised to the k-th power.

How many assignments are there? One combinatorial argument arranges n identical stars and k minus one separators in a line. The separators divide the stars into k possibly empty groups. There are n plus k minus one total positions, and we choose the k minus one separator positions. Hence the coefficient of x to the n is the binomial coefficient with upper entry n plus k minus one and lower entry k minus one.

This identity gives a nontrivial power-series expansion without differentiating anything. It also shows how a bijective proof and generating-function algebra can describe the same construction from different directions.

For k equal to two, the coefficient is n plus one: the first container gets any number from zero through n, and the second gets the rest. Its generating function is one divided by the square of one minus x. Do not confuse that with one divided by one minus x squared. The first expression counts ordered pairs of nonnegative integers with a prescribed sum; the second counts only even sizes, with one choice at each allowed size.

#### Counting sequences instead of multisets

Suppose we build a positive integer n as an *ordered* sequence of positive parts. For n equal to four, the decompositions include four, one plus three, three plus one, two plus two, and one plus one plus two, among others. Order now matters.

One part of positive size has generating function P equal to x plus x squared and so on, or x divided by one minus x. A sequence of exactly k parts has generating function P to the k. If we allow any number of parts, including the empty sequence of size zero, the generating function is one plus P plus P squared and so on. Formally that is one divided by one minus P. Substituting P and simplifying gives the fraction one minus x divided by one minus two x.

Expand it: the constant term is one. For every positive n, the coefficient is two to the n minus one. There is a simple independent proof. Write n identical marks in a row. There are n minus one gaps between consecutive marks. Choose independently whether each gap is a break between parts. Each subset of gaps specifies exactly one composition. The two proofs agree because they describe the same objects: sequences of positive parts.

#### What the algebra buys us

Generating functions do not replace combinatorial understanding. We still need to know what our factors mean, whether objects are distinguishable, and whether order matters. But once we have modeled those choices, algebra gives a uniform way to combine them, manipulate them, and extract answers.

The most useful shift is conceptual. Instead of solving one counting problem for each n, we construct an object whose coefficients solve all of them simultaneously. In the next layer of combinatorics, a recurrence relation will turn into an equation for a generating function, and that equation may reveal the long-term growth of a sequence. Even before that, products, geometric series, and coefficient extraction give us a language for complex counting problems that would be difficult to manage case by case.

### Recurrences, Rational Generating Functions, and Growth

Some sequences are defined not by a formula for their n-th term but by a rule that looks backward. A population count depends on previous populations. The number of tilings of a board depends on tilings of shorter boards. An algorithm's workload can depend on smaller subproblems. Such rules are recurrences, and they often seem to require laborious step-by-step computation.

A generating function can turn the recurrence into a single algebraic equation. Solving that equation may give an exact formula for every term and, just as importantly, a clear description of how the terms grow.

#### Tilings give a recurrence

Imagine a row of n unit cells to be tiled using one-cell squares and two-cell dominoes. Let t-n count the tilings. An empty row has one tiling, so t-zero is one. A one-cell row also has one tiling. For a longer row, inspect the first tile. If it is a square, the remainder is a row of n minus one cells. If it is a domino, the remainder is a row of n minus two cells. These cases are disjoint and exhaustive. Therefore t-n equals t at n minus one plus t at n minus two for n at least two.

The first values are one, one, two, three, five, eight. The same recurrence produces the Fibonacci numbers, but with a shifted index. Calling a sequence Fibonacci-like does not supply a proof; the first-tile argument supplies a combinatorial reason for the recurrence.

#### Encode the rule in one equation

Let T of x be the sum of t-n times x to the n, beginning at n equals zero. Multiply the recurrence by x to the n and sum over n at least two. The left side becomes T minus t-zero minus t-one x. The first shifted sum on the right becomes x times T minus x times t-zero. The second becomes x squared times T.

Substituting the initial values gives T minus one minus x equals x T minus x plus x squared T. The x terms cancel, leaving T times one minus x minus x squared equal to one. Therefore T equals one divided by one minus x minus x squared.

That rational function encodes every tiling count. The denominator records the recurrence coefficients. The numerator records the initial conditions. This separation is especially useful when we change the starting values without changing the recurrence rule.

The Fibonacci sequence itself, conventionally beginning with F-zero equals zero and F-one equals one, has generating function x divided by one minus x minus x squared. The two sequences differ by one index, exactly as their initial conditions suggest.

#### Solving the recurrence with roots

Try a solution of the form r to the n for the recurrence a-n equals a at n minus one plus a at n minus two. Substitution gives r squared equals r plus one. There are two roots, phi equal to one plus square root of five over two, and psi equal to one minus square root of five over two. Any linear combination of phi to the n and psi to the n obeys the recurrence. The two initial conditions determine the coefficients.

For Fibonacci numbers, the result is F-n equals phi to the n minus psi to the n, divided by square root of five. This is an exact identity, often called Binet's formula. It looks surprising because it produces integers from irrational powers. The recurrence and starting values ensure that exact cancellation occurs.

The expression also shows the growth. Phi is about one point six one eight, while the absolute value of psi is less than one. As n increases, psi to the n approaches zero. So F-n is asymptotic to phi to the n divided by square root of five. The ratio of successive nonzero terms approaches phi. The recurrence, the rational generating function, and the growth estimate are three views of the same structure.

#### General linear recurrences

Suppose a-n equals c-one times a at n minus one, through c-k times a at n minus k, with constant coefficients, once n is at least k. The same summation strategy gives a rational generating function whose denominator is one minus c-one x minus c-two x squared and so on through c-k x to the k. Its numerator is a polynomial determined by the initial values.

The roots of the characteristic polynomial explain the solutions. Distinct characteristic roots produce terms proportional to their n-th powers. Repeated roots require extra factors that are polynomials in n. For instance, the recurrence a-n equals two a at n minus one minus a at n minus two has characteristic polynomial r minus one squared. The general solution is A plus B times n. Check it directly: the second finite difference of a linear function of n vanishes.

A repeated dominant root can introduce factors such as n times r to the n, so a growth estimate based only on the largest root may miss the correct asymptotic factor.

#### A different kind of recurrence: branching structure

Not every recurrence is linear. Let C-n count rooted full binary tree shapes with n internal nodes, where each internal node has an ordered left and right subtree. There is one empty tree, so C-zero is one. A nonempty tree has a root, a left subtree with k internal nodes, and a right subtree with n minus one minus k internal nodes. Summing over k gives C-n equals the convolution of C-k and C at n minus one minus k.

The generating function C of x therefore satisfies C equals one plus x times C squared. Rearranging gives a quadratic equation for C. Its formal-power-series solution with constant term one is the quantity one minus the square root of one minus four x, divided by two x. The other algebraic root does not have a formal power-series expansion with the required constant term.

Extracting coefficients yields the Catalan numbers: C-n equals one over n plus one times the binomial coefficient two n choose n. Their initial values are one, one, two, five, fourteen. A Catalan sequence grows on the scale of four to the n divided by n to the power three halves, with a constant factor. The contrast with Fibonacci's phi to the n is instructive: the branching tree recurrence creates a different functional equation, a different singularity, and a different growth rate.

The exact asymptotic claim is more advanced than the coefficient calculation. It follows from a standard estimate for the central binomial coefficient. We do not need to pretend it follows just by looking at the first few terms.

#### When the technique is appropriate

A recurrence can be a constructive counting proof, a computational procedure, or an algebraic identity. Generating functions connect those roles. Rational generating functions are characteristic of constant-coefficient linear recurrences. Nonlinear structural recurrences may produce algebraic generating functions instead. Neither type requires analytic convergence merely to justify coefficient manipulations.

When we do want growth estimates, however, it becomes useful to treat the series as analytic functions and study where they become singular. That is a separate analytical step, and its hypotheses matter. For now, the central lesson is that an infinite collection of local equations can be turned into a finite algebraic relation. A recurrence tells us how a sequence is assembled; its generating function lets us reason about the whole assembly at once.

## Pólya Enumeration: Counting Colorings without Double-Counting Symmetry

If we color the four corners of a square black or white, there are sixteen assignments when the corners are labeled. But if a painted square can be rotated or turned over, some assignments that looked different are actually the same design. The obvious strategy of dividing sixteen by eight fails: the square has eight symmetries, but some colored designs are fixed by several of them, while others are not. Different designs have orbits of different sizes.

Burnside's lemma solves the problem by averaging the number of colorings fixed by each symmetry. Pólya enumeration goes further. It organizes the symmetries by their cycle structure and produces a polynomial that can count colorings with specified numbers of each color. The method makes a complicated counting problem into substitution in a single expression.

### What a symmetry fixes

Take any permutation of the four corners. Write its action as disjoint cycles. If a permutation exchanges corners one and two, those two corners must have the same color for the coloring to remain unchanged. If a permutation cycles three corners, all three must share a color. In general, a coloring is fixed exactly when each cycle is monochromatic.

With q available colors, a permutation having c cycles fixes q to the power c colorings: there is one independent color choice for each cycle. This observation is the complete bridge from the group action to enumeration.

For the square, the identity permutation has four cycles of length one, so it fixes q to the fourth power colorings. Each quarter turn forms one cycle of length four, so it fixes q colorings. A half turn consists of two cycles of length two, so it fixes q squared colorings.

Reflections require care. A reflection across a diagonal through opposite corners fixes those two corners individually and exchanges the other two. It has three cycles and fixes q cubed colorings. A reflection across a line through the midpoints of opposite edges exchanges two disjoint pairs of corners. It has two cycles and fixes q squared colorings. There are two reflections of each type.

Add these contributions and divide by eight. We obtain q to the fourth, plus two times q, plus three times q squared, plus two times q cubed, all divided by eight. For two colors the answer is six. The six possible designs can also be classified directly: none black, all black, one black, three black, two adjacent black corners, and two opposite black corners.

For three colors the answer is twenty-one. Rotations alone would give twenty-four designs, so allowing reflections identifies some additional pairs. Which transformations are considered equivalent is part of the mathematical problem, not a minor detail.

### The cycle index records more than the answer

Rather than evaluate each number of fixed colorings immediately, assign a variable a-one to a cycle of length one, a-two to a cycle of length two, and so forth. For each symmetry multiply one variable for each of its cycles. Average the resulting monomials over the group. This is the cycle index polynomial of the action.

For the square acting on its corners, the cycle index is one eighth times the following sum: a-one to the fourth power; two times a-four; three times a-two squared; and two times a-one squared times a-two. The four terms correspond to identity, quarter turns, half turn plus two edge reflections, and the two diagonal reflections.

Why collect terms this way? Because setting every a-k equal to q recovers the number of colorings with q unrestricted colors. But we can make more informative substitutions.

Suppose we have red and blue paint and want to record how many corners receive each. Replace a-k by x to the kth power plus y to the kth power. Choosing the first term means making that cycle red, contributing k red corners. Choosing the second means making it blue, contributing k blue corners. After substitution and expansion, the coefficient of x squared y squared is the number of essentially different designs with exactly two red and two blue corners.

There are exactly two: the red corners are adjacent or opposite. The cycle-index calculation reproduces that distinction without needing to draw every assignment.

### Why Burnside's lemma is already inside Pólya's method

Burnside's lemma states that the number of orbits equals the average number of fixed objects. We can derive it by counting pairs consisting of a group element and an object fixed by that element. Count first by group elements: the result is the sum of the sizes of all fixed-point sets. Count instead by objects: each object contributes the size of its stabilizer. A whole orbit has size the group order divided by the stabilizer size, so each orbit contributes exactly the group order to the count of pairs. Dividing by the group order gives one per orbit.

Pólya enumeration uses the same double count, but the objects are colorings and their fixed-point counts depend only on cycles. Each fixed coloring contributes a product of weights, so the same argument holds for a weighted count. That is why the cycle-index substitution works: it is Burnside's averaging performed with bookkeeping variables still attached.

We can also use the method for necklaces with n beads. Rotations form a cyclic group. A rotation by k steps has greatest-common-divisor of n and k cycles, so the number of colorings up to rotation is the average, over k from zero through n minus one, of q raised to the greatest common divisor of n and k. Adding reflections changes the acting group and the corresponding terms.

The formula is valuable when n is large, because generating and sorting every coloring would require examining q to the n possibilities. Group structure can compress that count into sums indexed by divisors of n.

### From colorings to larger combinatorial structures

The same idea appears when counting molecular substitution patterns, tilings of finite regions, and many classes of labeled objects modulo automorphisms. It is tempting to say that we are simply dividing by symmetry, but that phrase conceals the delicate part. We must account for the stabilizers of different objects, and the cycle structure of each symmetry tells us which choices survive.

The important lesson is not a single formula for squares. It is a reusable method: identify the action, compute the cycle types, build the cycle index, choose weights that encode the feature you want to count, and substitute. The resulting polynomial answers not only how many distinct objects exist, but often how their colors or components are distributed.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Counting by correspondence, cancellation, and generating series

### Counting by correspondence, cancellation, and generating series

#### Companions, sources, and study material (not spoken)

##### Bijections and Double Counting: Proving Equations by Counting Objects

**Track:** Discrete Mathematics and Combinatorics. **Background:** finite sets and basic algebra. **Question:** why can two descriptions of the same collection prove a mathematical identity?

###### Mathematical companion (not spoken)

For \(0\le k\le n\),
\[
\binom nk=\frac{n!}{k!(n-k)!},\quad
\binom nk=\binom{n-1}{k-1}+\binom{n-1}k,
\quad \sum_{k=0}^n\binom nk=2^n.
\]
Double counting marked subsets gives
\[
\sum_{k=0}^n k\binom nk=n2^{n-1}\qquad (n\ge1).
\]
For a finite undirected multigraph, loops contributing degree two,
\[
\sum_{v\in V}\deg(v)=2|E|,
\]
so the number of odd-degree vertices is even.

##### Exercises with answers

1. How many three-person committees contain a fixed member of a ten-person group? **Answer:** \(\binom 92=36\).
2. Why isn't the number of two-person committees \(n(n-1)\)? **Answer:** That counts both orders of each pair; divide by two.
3. Can a finite graph have exactly five vertices of odd degree? **Answer:** No, by the handshake lemma.
4. Prove there are two integers among any eight with the same remainder modulo seven. **Answer:** Eight objects occupy seven remainder classes; by pigeonhole two share a class.

##### Reading

MIT 6.042J, *Mathematics for Computer Science*, chapters on graphs, cardinality rules, and combinatorial proofs.

##### Inclusion–Exclusion: Counting When Cases Overlap

**Track:** Discrete Mathematics and Combinatorics. **Background:** basic set operations, factorials, binomial coefficients. **Question:** how can we count objects that violate several conditions without counting some objects twice?

###### Mathematical companion (not spoken)

For finite subsets \(A_1,\ldots,A_m\) of a finite universe,
\[
\left|\bigcup_{i=1}^m A_i\right|
=\sum_{\varnothing\ne S\subseteq\{1,\ldots,m\}}
(-1)^{|S|+1}\left|\bigcap_{i\in S} A_i\right|.
\]
An object in exactly \(r\ge1\) sets receives coefficient
\(\sum_{j=1}^r(-1)^{j+1}\binom rj=1\).

Derangements of \(n\) labeled objects:
\[
D_n=n!\sum_{k=0}^n\frac{(-1)^k}{k!},
\qquad D_3=2,\ D_4=9,\quad
\left|D_n-\frac{n!}{e}\right|<\frac1{n+1}.
\]
Surjections from an \(n\)-set to an \(m\)-set:
\[
\#\mathrm{Surj}(n,m)=\sum_{k=0}^m(-1)^k\binom mk(m-k)^n=m!S(n,m).
\]
The \(0^0\) convention may matter for empty-domain edge cases; lectures above assume \(n,m\ge1\) where appropriate.

##### Exercises with answers

1. How many derangements of two letters exist? **Answer:** One: they swap positions.
2. How many onto functions go from a four-element domain to two labeled values? **Answer:** \(2^4-2=14\).
3. Why can't we multiply \((n-1)^n\) to count derangements? **Answer:** The individual destination choices are not independent under the permutation constraint.
4. What would double counting do to an item in three overlapping sets if we only subtracted pairwise intersections? **Answer:** It would be counted zero times; add the triple intersection back once.

##### Reading

MIT 6.042J, *Mathematics for Computer Science*, chapter on inclusion–exclusion and counting techniques; standard results on permutations and surjections.

##### Generating Functions: Turn Counting into Algebra

**Track:** Discrete Mathematics and Combinatorics. **Background:** elementary counting and polynomial multiplication. **Question:** how can a single algebraic expression store an entire sequence of counting answers?

###### Mathematical companion (not spoken)

For \(A(x)=\sum_{n\ge0}a_nx^n\), write \([x^n]A(x)=a_n\). In formal power series over a commutative ring,
\[
[x^n](A(x)B(x))=\sum_{k=0}^n a_kb_{n-k}.
\]

**Unlimited packet sizes 2 and 3:**
\[
A(x)=\frac1{(1-x^2)(1-x^3)},\qquad [x^{12}]A(x)=3.
\]
**Stars and bars:**
\[
\frac1{(1-x)^k}=\sum_{n\ge0}{n+k-1\choose k-1}x^n.
\]
**Compositions:**
\[
1+P+P^2+\cdots=\frac1{1-\frac{x}{1-x}}=\frac{1-x}{1-2x}
=1+\sum_{n\ge1}2^{n-1}x^n.
\]

##### Exercises with answers

1. What is \([x^6](1-x^2)^{-1}(1-x^3)^{-1}\)? **Answer:** two; solutions are \((a,b)=(3,0),(0,2)\).
2. Give the series for choosing each of three labeled objects of weights one, two, and four at most once. **Answer:** \((1+x)(1+x^2)(1+x^4)\).
3. What does \((1-x)^{-3}\) count? **Answer:** assignments of a total of n indistinguishable items to three labeled containers; coefficient \({n+2\choose2}\).
4. Count ordered compositions of five. **Answer:** sixteen, by choosing cuts in four gaps.

##### Reading

MIT 6.042J, *Mathematics for Computer Science*, generating functions and counting; Herbert S. Wilf, *generatingfunctionology*, chapters on ordinary generating functions.

##### Recurrences, Rational Generating Functions, and Growth

**Track:** Discrete Mathematics and Combinatorics. **Background:** ordinary generating functions, coefficient extraction, elementary algebra. **Question:** how can a local recurrence predict an entire infinite sequence and its rate of growth?

###### Mathematical companion (not spoken)

For \(t_0=t_1=1\), \(t_n=t_{n-1}+t_{n-2}\) for \(n\ge2\),
\[
T(x)=\sum_{n\ge0}t_nx^n=\frac1{1-x-x^2}.
\]
For Fibonacci numbers \(F_0=0,F_1=1\):
\[
F(x)=\frac{x}{1-x-x^2},\qquad
F_n=\frac{\varphi^n-\psi^n}{\sqrt5},
\quad \varphi=\frac{1+\sqrt5}{2},\quad \psi=\frac{1-\sqrt5}{2}.
\]

The recurrence \(a_n=\sum_{j=1}^kc_j a_{n-j}\) yields a rational generating function with denominator \(1-\sum_{j=1}^kc_jx^j\).

For Catalan numbers,
\[
C_0=1,\quad C_n=\sum_{k=0}^{n-1}C_kC_{n-1-k},\quad
C(x)=1+xC(x)^2,\quad C_n=\frac1{n+1}{2n\choose n}.
\]
A standard Stirling approximation gives \(C_n\sim 4^n/(\sqrt\pi\,n^{3/2})\).

##### Exercises with answers

1. Count tilings of a length-four board by squares and dominoes. **Answer:** five.
2. What are the first four Fibonacci numbers? **Answer:** \(0,1,1,2\) with the chosen indexing.
3. Solve \(a_n=2a_{n-1}-a_{n-2}\), \(a_0=2\), \(a_1=5\). **Answer:** \(a_n=2+3n\).
4. Compute \(C_3\) from its recurrence. **Answer:** \(C_0C_2+C_1C_1+C_2C_0=2+1+2=5\).

##### Reading

MIT 6.042J, *Mathematics for Computer Science*, recurrences and generating functions; Herbert S. Wilf, *generatingfunctionology*, rational generating functions and recurrences.

### Pólya Enumeration: Counting Colorings without Double-Counting Symmetry

**Track:** Discrete Mathematics and Combinatorics. **Background:** group actions, Burnside's lemma, cycle notation, and generating functions. **Question:** how many colorings genuinely differ when rotating or reflecting an object does not produce a new design?

#### Mathematical companion (not spoken)

For \(G\le S_n\) acting on \(n\) positions, let \(c_k(g)\) be the number of cycles of length \(k\) in \(g\). Define the cycle index
\[
Z_G(a_1,\ldots,a_n)=\frac1{|G|}\sum_{g\in G}\prod_{k=1}^n a_k^{c_k(g)}.
\]
For \(q\) available colors, the orbit count is \(Z_G(q,\ldots,q)\). For color inventory \((x_1,\ldots,x_q)\), substitute \(a_k\mapsto x_1^k+\cdots+x_q^k\); the coefficient of \(x_1^{m_1}\cdots x_q^{m_q}\) counts colorings with that inventory modulo \(G\).

**Dihedral action on a square's vertices.** With \(G=D_4\) of order eight,
\[
Z_{D_4}=\tfrac18\bigl(a_1^4+2a_4+3a_2^2+2a_1^2a_2\bigr).
\]
Thus
\[
N(q)=\tfrac18(q^4+2q+3q^2+2q^3),\quad N(2)=6,\quad N(3)=21.
\]
With red weight \(x\) and blue weight \(y\), \([x^2y^2]Z_{D_4}(x+y,x^2+y^2,x^3+y^3,x^4+y^4)=2\).

**Necklaces under rotation only.** For \(C_n\),
\[
N_{C_n}(q)=\frac1n\sum_{k=0}^{n-1}q^{\gcd(n,k)}=\frac1n\sum_{d\mid n}\varphi(d)q^{n/d}.
\]
Including reflections requires the dihedral cycle index, not the cyclic one.

##### Exercises with answers

1. How many square-corner colorings with exactly one red corner exist up to all square symmetries? **Answer:** one.
2. Why does a cycle of length four permit only q fixed colorings? **Answer:** every position in that cycle must have the same color.
3. Count square colorings in three colors up to rotations only. **Answer:** \((3^4+3^2+2\cdot3)/4=24\).
4. Count length-three binary necklaces up to rotation. **Answer:** \((2^3+2+2)/3=4\).

##### Reading

Sasha Patotski, [Pólya Enumeration Theorem, Cornell notes](https://pi.math.cornell.edu/~apatotski/IHS2015/Lecture%2010.pdf); MIT OCW, [Mathematics for Computer Science](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/pages/readings/), counting and group actions.
