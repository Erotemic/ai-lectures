# Claims, logical language, and methods of proof

<!-- BEGIN SPOKEN LECTURE -->

# Claims, logical language, and methods of proof

## What Counts as a Mathematical Proof?

A mathematical argument is not just a persuasive story. It is an account of why a conclusion must follow from assumptions that have been stated. The word 'must' matters. Suppose someone claims that the sum of two odd numbers is always even. Checking three plus five, seven plus nine, and a hundred other examples makes the claim plausible. But the claim covers infinitely many pairs of odd integers. A proof must explain why a counterexample is impossible, not merely why we have failed to encounter one.

The argument can begin with an arbitrary odd integer. By definition it is twice an integer plus one. Take another odd integer and write it the same way. Adding their expressions gives twice the sum of those two integers plus two, which is twice an integer. So the result is even. The important step was not the arithmetic alone. It was replacing a particular example by an arbitrary pair, while keeping the information that makes them odd. That is how a finite argument can establish an infinite collection of claims.

### Statements and the world they describe

A mathematical statement is a sentence that can be evaluated as true or false once its meaning and the objects under discussion are fixed. 'Seven is prime' is a statement. 'A triangle has three sides' is a statement once triangle has been defined. 'The number is prime' may not yet be a statement, because we have not said which number. Instead, it may be a property of a variable, something that becomes a statement after we supply a number or quantify over it.

Definitions give the words in a statement precise meanings. A theorem says that one statement follows from declared assumptions. An example illustrates a definition or a theorem. A counterexample defeats a claim that asserted more than is actually true. A conjecture is an unproved claim, no matter how compelling the evidence. These roles are different, and confusing them makes mathematical writing hard to evaluate.

Consider the assertion that every even number greater than two is the sum of two primes. It has been checked for immense ranges of integers, but an enormous finite computation cannot by itself settle the entire infinite assertion. Conversely, a single even number for which no such prime decomposition exists would refute it. The logical asymmetry between supporting examples and a disproof by counterexample is one of the first things a proof writer learns to notice.

### Assumptions are part of the theorem

A claim can change truth value when the domain changes. 'Every nonzero number has a multiplicative inverse' is true for nonzero real numbers, but false for nonzero integers if the inverse is also required to be an integer. The phrase 'number' has hidden a crucial choice. 'A function with derivative zero everywhere is constant' is true on an interval, but if its domain consists of two separated intervals, it can take different constants on each. An assumption about connectedness, not merely differentiability, was doing work.

A complete proof therefore has a beginning and an end. At the beginning, it declares the objects and hypotheses. In the middle, each inference uses a definition, an earlier result, an allowed algebraic operation, or a justified construction. At the end, the requested conclusion has been reached. That skeleton does not require stiff writing. It requires the reader to be able to locate the reason for every important step.

For our odd-number example, the key question is not whether we used advanced mathematics. We used almost none. The questions are whether every odd integer has the required representation, whether the symbols denote integers, and whether the final expression meets the definition of evenness. If so, the argument is sound regardless of how short it is.

### Looking for the weak joint

Here is a tempting but invalid argument. We want to prove that multiplying two positive real numbers gives a positive number. Someone writes: let the numbers be a and b. Their product is positive, as required. The conclusion has merely been restated. A valid argument must use a known property of the ordered real numbers, such as the axiom that the product of positive elements is positive, or derive it from a set of more basic order rules.

Another common failure is to prove only a special case. If we want all triangles, drawing an equilateral triangle does not give a general proof. That drawing might help discover a relationship, but the proof must either apply to arbitrary triangles or explain why every triangle reduces to the chosen case.

When you read a theorem, ask three questions. What would count as one admissible input? What are we promised about it? What must we establish about every such input? When you write a proof, start by answering those questions. The rest of the course develops methods for moving from one side of that contract to the other. The reward is not formality for its own sake. It is the freedom to rely on a result because its limitations and reasons are visible.

## And, Or, Not, and If: Reading Mathematical Logic

Suppose I tell you: if a number is divisible by four, it is even. You understand the claim without a truth table. Yet translating it into precise logic reveals why some very familiar errors are errors. The statement is a conditional: when the premise holds, the conclusion must hold. It does not say that every even integer is divisible by four. It does not say that a number not divisible by four must be odd. Those would be different statements.

We will use letters P and Q for propositions. 'P and Q' requires both. 'P or Q' in ordinary mathematical logic means at least one of the two; it permits both. 'Not P' says P fails. 'If P, then Q' rules out exactly the situation in which P is true but Q is false. If we work in classical logic, these meanings can be displayed completely in a short table of truth values.

### What the conditional actually promises

Why do mathematicians accept a conditional with a false premise as true? Imagine a guarantee: for every integer that enters a certain machine, if the integer is a multiple of four, its output is even. The machine encounters the number six, which is not a multiple of four. The guarantee places no constraint on this case. Whatever happens to six cannot violate the conditional promise. This is the mathematical meaning of an implication, not a claim that the premise somehow caused the conclusion.

An implication is different from its converse. 'Multiple of four implies even' is true. 'Even implies multiple of four' fails at six. The inverse, 'not a multiple of four implies not even,' fails at six as well. The contrapositive, 'not even implies not a multiple of four,' is equivalent to the original implication in ordinary classical mathematics. The contrapositive changes both the direction and the truth status of the two conditions, and it is a valid route for proving the original.

A mathematician may write 'P if Q' to mean that Q implies P. 'P only if Q' reverses the role: it means P implies Q. 'P if and only if Q' asks for both directions. These short phrases are responsible for many errors when readers skim a proof. Try translating each into a plain conditional before doing any algebra.

### Combining information

Suppose a number is divisible by both two and three. We can say that it satisfies two properties joined by 'and.' If we learn a statement of the form 'it is divisible by two or by three,' we know at least one property holds but cannot assume which one. A valid argument from such an 'or' statement may need two cases. In the first, the number is divisible by two; in the second, by three. If both cases lead to the desired conclusion, then we may conclude it without deciding which alternative actually held.

Negation is also structural. The negation of 'P and Q' is 'not P or not Q.' The negation of 'P or Q' is 'not P and not Q.' These are De Morgan's laws. One way to remember them is to imagine what would have to go wrong for a two-part requirement to fail: at least one part is missing. For an either-or promise to fail, neither option is available.

Consider 'the integer is positive and even.' Its negation is 'the integer is not positive, or it is not even.' It would be wrong to demand both failures. Three is not even, so it already defeats the original conjunction even though it is positive.

### Sound inference versus convincing language

There are standard patterns of correct inference. From P and 'if P then Q,' conclude Q. This is sometimes called modus ponens. From 'if P then Q' and 'not Q,' conclude 'not P.' This is modus tollens. In contrast, from 'if P then Q' and Q, we cannot conclude P. The fact that a number is even does not tell us it is divisible by four. This error is called affirming the consequent. Likewise, knowing that P is false does not make Q false; denying the antecedent is not a valid inference.

These patterns matter inside longer arguments. A proof may contain correct computations while making an incorrect logical transition between them. When a step feels dubious, replace the mathematical nouns with the neutral names P and Q. The bare pattern often makes the missing information obvious.

### Meaning before notation

Truth tables are helpful for finite combinations of propositions, but mathematics quickly goes beyond any fixed list of statements. We ask what happens for every integer, every function, or some particular witness. That requires quantifiers. For now, keep one discipline: every time you use an implication, state what you are assuming and what you intend to obtain. Every time you use an 'or,' make sure the argument handles all alternatives. And every time you use an 'if and only if,' check that neither direction has been left unproved. The symbols are shorthand for obligations, not substitutes for reasoning.

## For Every and There Exists: Quantifiers and Their Scope

There are two short phrases that let mathematics make claims about infinitely many objects: 'for every' and 'there exists.' Their order, scope, and domain can change a theorem completely. A listener who understands those three details already understands much of the structure of a formal proof.

Start with the claim that every natural number has a larger natural number. Read it as follows: take any natural number n. There is some natural number m, which may depend on n, such that m is larger. We can prove it by selecting n plus one. Notice that our choice is allowed to change when n changes. A different claim would say that there exists one natural number m which is larger than every natural number n. That claim is false. The two sentences contain the same words and comparisons, but the quantifiers appear in the opposite order.

### Domains control the meaning

The sentence 'for every x, x squared is nonnegative' is true when x ranges over the real numbers. Without a domain it is incomplete, and over complex numbers 'nonnegative' has no usual order meaning. Likewise, 'there exists an x with x squared equal to minus one' is false over the reals and true over the complex numbers. A good proof names its universe before starting its argument.

An unrestricted variable is not an invitation to choose your favorite example. When a theorem begins 'for every integer n,' you introduce an arbitrary integer n and reason in a way that does not depend on a special value. For an existential claim, by contrast, one successful witness is enough. To prove there exists an even prime, choose two and verify both properties. To prove every prime is even, that single example is useless; three refutes the claim.

### Negating a quantified statement

Imagine the assertion, 'every student in a class solved at least one problem.' To show it is false, it is enough to identify one student who solved none. The negation of a universal assertion is an existential counterexample. Similarly, to deny that there exists a student who solved every problem is to say that each student failed at least one problem. This is a universal statement with an existential failure inside it.

In classical logic, the negation of 'for every x, P of x' is equivalent to 'there exists an x for which P fails.' The negation of 'there exists an x with P of x' is equivalent to 'for every x, P fails.' The classical qualification is important in foundational mathematics: intuitionistic and constructive logics distinguish some directions that classical mathematics treats as interchangeable. The everyday proof methods in this course will use classical logic, and later a constructive logic track can explain which witnesses become computational data.

Now combine the patterns. Negate 'for every real x there exists a real y greater than x.' The result is 'there exists a real x such that every real y fails to be greater than x.' This says that the real numbers have a greatest element. That is false, as expected, because adding one always gives a greater number. Negating one quantifier at a time, while flipping its kind, keeps the dependencies straight.

### Moving quantifiers changes the claim

Compare two statements about students and books. First: every student has read some book. Second: there is a book every student has read. In the first, each student may name a different book. In the second, all students share a single book. We must not swap the order just because both sentences contain 'every' and 'some.'

The same issue appears in analysis. A sequence converges to L when, for every positive error tolerance, there exists a sufficiently late index after which all terms lie within that tolerance of L. The index may depend on the tolerance. If we accidentally require one fixed index that works for every positive tolerance, we demand that all sufficiently late terms equal L exactly. That is much stronger than convergence.

Uniform continuity adds another dependency question. The required input tolerance may depend on the desired output error, but must work at every point in the domain. Ordinary pointwise continuity allows the input tolerance also to depend on the chosen base point. This is why quantifier order matters even when the formulas look nearly identical.

### A method for reading dense definitions

When confronted with a quantified claim, translate it into a game. The opponent chooses the objects governed by universal quantifiers. You must provide witnesses for existential quantifiers at the moment they become available. In the convergence definition, the opponent presents an epsilon. You then produce a threshold N. They choose a later index n, and you must verify the required inequality. A proof wins only if its choices work for every legal move.

This game is not a complete theory of logic, but it is an excellent reading discipline. It reveals why some proposed proofs fail: they secretly pick a witness before seeing the universal input on which it needs to depend, or they check just one value rather than all values. Quantifiers are the grammar of mathematical dependence. Learning to hear that grammar makes much of advanced mathematics less mysterious.

## Definitions and If-and-Only-If: Keeping Both Directions

A mathematical definition is a contract for how a word may be used. Suppose we define an integer to be even exactly when it equals twice another integer. This gives us two directions: if an integer is even, there is an integer that doubles to it; and if an integer equals twice an integer, it is even. Both directions are available because 'even' has been defined by an equivalence.

That may sound obvious, but many proofs fail because they use only one part of a definition or silently replace a precise definition by a picture. To prove a number is even, we can exhibit the required integer. To use the assumption that a number is even, we can introduce the integer promised by the definition. Definitions are tools we can unpack in either direction.

### Necessary and sufficient

If P implies Q, then Q is a necessary condition for P: P cannot occur without Q. The same implication says that P is sufficient for Q: P alone guarantees Q. If we assert P if and only if Q, each is necessary and sufficient for the other. These words are easiest to read by converting them back into the implication they describe.

For example, being divisible by four is sufficient for being even, but not necessary. Being even is necessary for divisibility by four, but not sufficient. Six is the concrete counterexample to the reverse direction. One short example is often enough to separate two claims that sound interchangeable in casual speech.

An equivalence proof requires two complete arguments. To show that an integer n is even if and only if n squared is even, first assume n is even. Write n as twice an integer, and its square is divisible by four, hence even. For the reverse direction, assume n squared is even. If n were odd, writing n as twice an integer plus one shows that its square is odd. That contradiction tells us n cannot be odd; since every integer is even or odd, n must be even. The two arguments have distinct work to do.

### Definitions with several clauses

Consider a function being injective. The definition says: for every two inputs x and y in its domain, if the outputs are equal, then the inputs are equal. To prove injectivity, begin with arbitrary x and y, assume equal outputs, and derive equal inputs. To use injectivity in a proof, you may conclude x equals y only after showing that the corresponding outputs match. You cannot conclude that an arbitrary output has an input: that is surjectivity, a separate property.

Now define a relation to be an equivalence relation when it is reflexive, symmetric, and transitive. That is a three-part conjunction. A proof that a relation is an equivalence relation must establish all three properties. Conversely, whenever we know we have an equivalence relation, we can use each property independently. Words such as 'continuous,' 'compact,' 'normal,' and 'measurable' will later hide more elaborate contracts, but the reading method is the same.

### Definitions are not all theorems

Definitions introduce names; theorems establish facts about the objects named. We may define a prime number as an integer greater than one with no positive divisors except one and itself. That does not establish that every integer greater than one is a product of primes. Factorization requires a proof. Likewise, defining a limit does not prove that every sequence has a limit. Existence remains a mathematical question.

Sometimes a single object has several equivalent descriptions. A topology course may prove that a set is closed exactly when its complement is open; depending on the chosen starting axioms, one side may be a definition and the other a theorem. In metric spaces, the sequential criterion for closedness is another equivalent characterization. The fact that mathematicians freely exchange these descriptions is earned by an equivalence proof, not by the similarity of the words.

### How to audit a definition-based argument

When reading a long proof, underline every use of a defined term. Ask whether the writer is using the term to obtain information or trying to prove the term applies. In the first situation, unpack the assumption. In the second, check all the requirements of the definition. Be alert to missing domain restrictions: 'n is prime' means a positive integer greater than one, not a negative integer or a unit. Be alert also to vacuous cases. The statement 'every element of the empty set has a certain property' is true because there is no violating element, but it does not assert that such an element exists.

This habit keeps mathematical explanations honest without making them cumbersome. A definition tells us exactly what has been promised and what must be delivered. Most of the reasoning methods that follow are ways of carrying those promises from hypotheses into conclusions.

## Direct Proof: Turning a Hypothesis into a Conclusion

The most straightforward kind of proof begins where a theorem begins. You assume its hypotheses and move, by justified steps, toward its conclusion. This is called a direct proof. Its power is easy to overlook because it may not involve a named trick. It does involve a reliable discipline: use the exact information given, introduce witnesses when definitions promise them, and keep track of what sort of object each symbol denotes.

Take the claim: if an integer is divisible by six, then it is divisible by three. Let n be an arbitrary integer divisible by six. That means there is an integer k with n equal to six times k. Rewrite six times k as three times two k. Since two k is an integer, n satisfies the definition of divisibility by three. The entire proof is the movement from one witness to another.

### Witnesses make existential conclusions concrete

To prove that an integer is divisible by d, exhibit an integer quotient. To prove a set is nonempty, identify an element. To prove a function is not injective, find two distinct inputs with the same output. These are existential obligations. They cannot be met merely by restating the desired property. A useful question while writing is: what object is the theorem asking me to build?

Consider two integers a and b each divisible by five. Then a equals five r and b equals five s for integers r and s. Their sum equals five times r plus s. Thus it is divisible by five. The witness for the conclusion is r plus s. We did not need to know the numerical values of a or b. We needed only the representations supplied by divisibility.

The same reasoning proves that multiples of five are closed under subtraction, because r minus s remains an integer. The word 'closed' here means the operation stays within the set under discussion. Later, a subspace or subgroup proof will repeat this pattern: take arbitrary elements of the candidate set, apply an operation, and demonstrate that the result still satisfies the defining property.

### Direct proof with inequalities

Suppose we want to prove: if x and y are nonnegative real numbers, then x plus y is nonnegative. This follows from the compatibility of the order on the real numbers with addition. Starting with zero less than or equal to x, add y to both sides. We get y less than or equal to x plus y. Combining zero less than or equal to y with that inequality gives zero less than or equal to x plus y. The conclusion is now derived from declared assumptions and order rules.

It is important to notice which operations preserve inequalities. Adding the same real number does. Multiplying by a nonnegative number does; multiplying by a negative number reverses the inequality. A proof that divides by a variable without establishing its sign may be invalid. The same kind of audit applies to algebraic cancellation: canceling a factor requires that factor to be nonzero.

### Generalizing an example

Take the numerical identity that three times five minus three times two equals three times three. One may see a pattern and conjecture the distributive law. A general proof works with arbitrary real numbers a, b, and c and uses the field axiom a times b minus a times c equals a times the difference b minus c. This may itself be an axiom or an earlier derived theorem, depending on how algebra has been developed. A proof is always relative to accepted starting rules. It is not required to rebuild arithmetic from set theory in every lecture.

A useful technique is to transform the expression appearing in the hypothesis until it resembles the target. For claims about divisibility, factor out the needed integer. For claims about functions, start from the definition at an arbitrary input. For claims about subset inclusion, pick an arbitrary element of the left-hand set and show it belongs to the right-hand set. The action changes with the conclusion's logical form.

### A complete set inclusion proof

Let A, B, and C be sets. We want to show that if A is contained in B and B is contained in C, then A is contained in C. Start with an arbitrary element x of A. Since A is a subset of B, x is in B. Since B is a subset of C, x is in C. Therefore every element of A belongs to C, which is exactly the definition of A being a subset of C.

Notice that this argument does not require A to contain any element. If A is empty, the universal claim has no counterexample. Nothing goes wrong. The proof does not rely on choosing an actual element in advance; 'take an arbitrary element' introduces a hypothetical element for a conditional argument.

Direct proofs teach the central skill of all proof writing: matching a conclusion to the data that would establish it. Later techniques, such as induction or contradiction, will change the route. They do not change the need to know exactly what has been proved.

## Contraposition and Cases: Changing the Route, Not the Claim

Sometimes the conclusion of a theorem is a negative statement, and approaching it directly is awkward. We can change the route without changing the claim. Contraposition does this for a conditional statement. A second technique, proof by cases, divides the possible inputs into exhaustive alternatives and handles each one. Both methods depend on a precise understanding of which possibilities have been covered.

Take the theorem: if an integer n squared is even, then n is even. A direct approach might begin by trying to extract information about n from the parity of its square. A more convenient approach is to prove the contrapositive: if n is not even, then n squared is not even. Every integer that is not even is odd. Write n as twice k plus one. Expanding the square gives four k squared plus four k plus one, which is twice the integer two k squared plus two k, plus one. Hence n squared is odd. We have proved the contrapositive, so the original conditional follows in classical mathematics.

### Why the direction works

The original implication forbids a case where n squared is even but n is odd. The contrapositive forbids exactly the same case, described from the opposite direction. In elementary classical logic, 'if P then Q' and 'if not Q then not P' have the same truth conditions. This justifies proving one in place of the other. It does not justify proving the converse, 'if Q then P,' or the inverse, 'if not P then not Q.' Their counterexamples may differ.

Contraposition is particularly useful when a conclusion says that an object is injective, nonzero, independent, or impossible. Instead of forcing the desired positive structure, assume its failure and derive the failure of the hypothesis. One should still check that the negation of the conclusion has been written correctly. 'Not all' and 'all not' are different.

### A proof by exhaustive cases

Suppose a whole number n is any integer. We want to show that n times n plus one is even. Every integer is either even or odd. If n is even, then n is twice k, and n times n plus one contains the factor two. If n is odd, n equals twice k plus one, so n plus one equals twice k plus two and is even. In either case one factor in the product is even, so the product is even. We have handled every integer because parity exhausts the possibilities.

One can also observe that two consecutive integers always have opposite parity, which compresses the proof. But that shorter sentence is itself a theorem about parity. If a learner does not yet know it, the two-case argument makes its content explicit.

A case split does not need to be an 'either-or' that excludes overlap. If we know that P or Q holds and both cases separately imply R, then R follows even when P and Q are both true. The important condition is completeness: every admissible input falls under at least one case. Disjoint cases can simplify bookkeeping but are not always required.

### Case splits can hide gaps

A common example is dividing a proof into x positive and x negative, forgetting x equals zero. Another is dividing functions into increasing and decreasing without considering functions that are neither. Before you proceed, ask whether your alternatives are really exhaustive.

Even a correct split may leave details unproved. Suppose an expression depends on the sign of a denominator. If the denominator might be zero, neither positive nor negative cases permit division. You must establish nonzeroness first or add a separate case. Hypotheses are not decorations; they prevent illicit operations.

### Selecting a technique rather than memorizing it

How should you choose between direct proof, contraposition, and cases? Read the goal. If it asks for a witness or an identity, direct proof is often natural. If it says that a bad outcome cannot occur, contraposition may turn the negative conclusion into a concrete assumption. If the domain comes with a natural finite classification, such as even versus odd, signs, or residues modulo three, cases can turn a general claim into manageable subclaims.

For example, the square of any integer has remainder zero or one when divided by four. Prove this by even and odd cases. In the even case n equals twice k, and n squared is divisible by four. In the odd case the expansion gives four times the sum of k squared and k, plus one. This small lemma later becomes useful in proving that certain Diophantine equations have no integer solutions. The point of a proof technique is not to display cleverness. It is to expose the structure that makes a theorem true.

## Contradiction: Proving Something Cannot Happen

There is a way to prove a claim by examining what would happen if it were false. Assume the denial of the desired conclusion. Reason carefully from that assumption together with the standing hypotheses. If the result is impossible, the denial cannot hold. In ordinary classical mathematics, this is proof by contradiction.

One of the first famous examples says that the square root of two is irrational. Irrational does not mean mysterious or unknowable. It means the number cannot be expressed as a fraction of two integers with nonzero denominator. A proof must rule out every such fraction at once.

### A complete irrationality proof

Suppose, seeking a contradiction, that the square root of two equals a fraction p over q in lowest terms, where p and q are integers and q is nonzero. Lowest terms means p and q share no common positive divisor greater than one. Square the equation. It says p squared equals twice q squared. Therefore p squared is even. The parity result established earlier tells us p itself must be even. Write p as two times r.

Substitute that into the squared equation. Four r squared equals twice q squared. Dividing by two gives q squared equals twice r squared. Hence q squared is even, and so q is even. But now both p and q are divisible by two, contradicting that the fraction was in lowest terms. No such representation exists, so the square root of two is irrational.

Where exactly is the contradiction? It is the simultaneous claim that p and q have no common factor greater than one and that both have the factor two. We did not derive a numerical impossibility such as zero equals one. We derived two incompatible statements under the same assumptions.

### Assumptions that make the argument work

The proof uses the fact that a rational number can be expressed as a fraction in lowest terms. That fact comes from elementary properties of the integers, such as division by a greatest common divisor or well-ordering. If we omit it, learning only that p and q are even is not itself contradictory: many fractions have even numerator and denominator. The choice of reduced fraction is the piece that closes the loop.

Likewise, when we square an equality, the resulting equation follows from the original. But squaring is not always reversible without additional sign information. From x squared equals four we get x equals two or minus two, not only two. Contradiction arguments often contain algebraic transformations; they must be checked just as carefully as any direct proof.

### Refuting an existence claim

Suppose someone claims that there exists a greatest integer. Assume there is one, call it M. The integer M plus one is larger. This contradicts the assumed maximality. Therefore no greatest integer exists. In this proof the negation of the existential statement is the desired universal negative: every candidate fails to be greatest.

We can also prove a universal negative by showing any hypothetical counterexample produces a contradiction. For example, no integer is both even and odd. If n equals twice a and also twice b plus one, subtraction gives twice the difference between a and b equals one. The left side is even, and the right side is odd, impossible by parity. The proof is simply the direct incompatibility of the two definitions.

### Classical reasoning and a useful distinction

In classical logic, to establish P by contradiction we may assume not P, reach an impossibility, and conclude P. Constructive logic distinguishes that from proving not P by assuming P and reaching an impossibility. The latter pattern is valid constructively; the unrestricted step from 'not not P' to P is a classical principle. The advanced constructive-logic course develops this distinction further. For elementary proof writing, what matters is that we identify which proposition was negated and what actually caused the contradiction.

Do not treat contradiction as a license for circular reasoning. If the supposed contradiction relies on the very theorem being proved, we have gained nothing. Likewise, an unfamiliar or surprising conclusion is not a contradiction. The conclusion must violate a known fact, a definition, an assumption, or an earlier proved theorem.

A good contradiction proof identifies its incompatible statements explicitly. If you cannot point to both sides of the conflict, the argument may still be missing its final step. With that discipline, contradiction becomes a precise tool rather than a rhetorical flourish.

## Counterexamples: How One Example Defeats a General Claim

Mathematical theorems often contain the word 'every.' That makes them powerful, but it also makes them vulnerable: one counterexample disproves a universal claim. The counterexample must satisfy the claim's hypotheses while violating its conclusion. Failing a hypothesis is not a refutation. Showing that a different theorem is false is not a refutation either.

Take the assertion that every prime number is odd. The number two is a prime and it is even. One example settles the matter. More complicated assertions may resist such quick searches because the dangerous cases lie at the boundary of the hypotheses: zero, empty sets, disconnected domains, repeated eigenvalues, or functions that behave badly at one point.

### Diagnosing a false converse

Recall that if an integer is divisible by six, it is divisible by three. The converse says that if it is divisible by three, it is divisible by six. The integer three refutes the converse. It meets the antecedent, divisibility by three, and violates the consequent, divisibility by six. Notice that our counterexample does not contradict the original theorem. It isolates a logical direction that was never promised.

Try a claim about functions: 'if a function has derivative zero at a point, it has a local maximum there.' Consider x cubed at zero. Its derivative is zero there, but values on one side are smaller and on the other larger. The claim confuses a necessary condition for a differentiable interior extremum with a sufficient one. The counterexample is not just an isolated fact; it tells us which missing hypothesis to examine. A negative second derivative can guarantee a strict local maximum under suitable smoothness assumptions, while a zero first derivative alone cannot.

### Boundary examples reveal missing assumptions

Suppose a theorem seems to say that every bounded sequence converges. The sequence alternating between one and minus one is bounded but does not converge. Yet it has convergent subsequences. This suggests a repair: boundedness on the real line guarantees at least one convergent subsequence, not convergence of the original sequence. The repaired theorem is the Bolzano–Weierstrass result, and its proof requires the completeness of the real numbers.

Consider another proposed theorem: a continuous function on a set attains its largest value. On the open interval from zero to one, the function f of x equal to x has no maximum. Every value can be exceeded by another point still inside the interval. The closed interval from zero to one does have a maximum for the same function. The boundary condition, expressed precisely through compactness, is not incidental.

### How to search responsibly

When testing a conjecture, first classify its logical form. If it claims all objects have a property, try the simplest and most degenerate admissible objects. If it claims an implication, seek an object where the hypothesis is true and the conclusion false. If it claims two sets are equal, try to find an element belonging to one but not the other. If it claims uniqueness, look for two distinct witnesses. If it claims an operation is well-defined, choose two representatives of the same object and see whether the operation produces incompatible answers.

Computations can help discover a counterexample, but a mathematical refutation still requires verifying it. A floating-point approximation showing a small negative value might be a rounding artifact. An alleged graph counterexample should have its edges and claimed properties checked. If a result depends on a subtle domain condition, write that condition down rather than trusting a picture.

### Repairing rather than merely rejecting

A good counterexample can become a guide to a true theorem. 'Every bounded function on an interval has a maximum' fails for discontinuous functions or open intervals. Continuity on a nonempty compact interval supplies the missing conditions. 'Every square matrix is diagonalizable' fails for a Jordan block, but real symmetric matrices are orthogonally diagonalizable. 'Every subset of a compact space is compact' fails, but every closed subset of a compact space is compact.

This is how much of mathematical understanding grows. A naive claim fails; the counterexample tells us what feature matters; a sharper statement emerges. We learn not just whether a theorem is true, but why each assumption belongs in it.

There is also a limitation to remember: an unsuccessful search for counterexamples does not prove a theorem. A million positive trials remain finite evidence unless a separate argument shows they exhaust all possibilities. By contrast, one correctly verified negative trial can settle a universal conjecture. Learn to use that asymmetry carefully. It is one of the fastest ways to become a better proof reader and a better theorem writer.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### What Counts as a Mathematical Proof?

**Track:** Mathematical Reasoning and Proof from First Principles. **Background:** Everyday arithmetic; no prior proof training. **Purpose:** teach an actual proof obligation and the reasoning required to discharge it.

---

#### Mathematical companion (not spoken)

##### Formal proof patterns

The claim that sums of odd integers are even has the quantified form
\[
\forall a,b\in\mathbb Z\;[(\exists r\in\mathbb Z\;a=2r+1)\land(\exists s\in\mathbb Z\;b=2s+1)\Rightarrow(\exists t\in\mathbb Z\;a+b=2t)].
\]
Choose the witnesses promised by the antecedent and let \(t=r+s+1\):
\[
a+b=(2r+1)+(2s+1)=2(r+s+1).
\]
Checking examples illustrates but cannot justify the universal quantifier. The Goldbach conjecture is mentioned only as an example of the distinction between a conjecture and a theorem; no claim of its resolution is intended.

##### Exercises with answers

1. State the domain required for 'every nonzero number has a multiplicative inverse.' **Answer:** it is true in a field such as \(\mathbb R\) with the inverse in that field, but false over \(\mathbb Z\), where \(2\) has no integer inverse.
2. Prove that the difference of two odd integers is even. **Answer:** \((2r+1)-(2s+1)=2(r-s)\).
3. What is the logical role of \(n=2\) in the claim 'every prime is odd'? **Answer:** a counterexample; it satisfies the hypothesis 'prime' but violates the conclusion 'odd'.

##### Sources and further reading

- [Richard Hammack, Book of Proof, third edition (current online edition)](https://richardhammack.github.io/BookOfProof/).
- [Eric Lehman, F. Thomson Leighton and Albert R. Meyer, Mathematics for Computer Science, MIT OCW 6.042J](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/).
- [Wikipedia: Mathematical proof](https://en.wikipedia.org/wiki/Mathematical_proof).

### And, Or, Not, and If: Reading Mathematical Logic

**Track:** Mathematical Reasoning and Proof from First Principles. **Background:** Statements and counterexamples. **Purpose:** teach an actual proof obligation and the reasoning required to discharge it.

---

#### Mathematical companion (not spoken)

##### Propositional truth conditions

| \(P\) | \(Q\) | \(P\land Q\) | \(P\lor Q\) | \(P\Rightarrow Q\) |
|---|---|---|---|---|
| T | T | T | T | T |
| T | F | F | T | F |
| F | T | F | T | T |
| F | F | F | F | T |

The converse is \(Q\Rightarrow P\). The inverse is \(\neg P\Rightarrow\neg Q\). The contrapositive is \(\neg Q\Rightarrow\neg P\), classically equivalent to the original. In fact \(P\Rightarrow Q\) is equivalent to \(\neg P\lor Q\) in classical propositional logic.

##### Exercises with answers

1. Translate 'A only if B.' **Answer:** \(A\Rightarrow B\).
2. Translate 'A if B.' **Answer:** \(B\Rightarrow A\).
3. Is \((P\lor Q)\land\neg P\Rightarrow Q\) valid? **Answer:** yes; the \(P\) branch is excluded.
4. Find a counterexample to 'divisible by three implies divisible by six.' **Answer:** \(n=3\).

##### Sources and further reading

- [Richard Hammack, Book of Proof, third edition (current online edition)](https://richardhammack.github.io/BookOfProof/).
- [Eric Lehman, F. Thomson Leighton and Albert R. Meyer, Mathematics for Computer Science, MIT OCW 6.042J](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/).
- [forall x: Calgary, A Free and Open Introduction to Formal Logic (Open Logic Project)](https://forallx.openlogicproject.org/).
- [Wikipedia: Logical connective](https://en.wikipedia.org/wiki/Logical_connective).

### For Every and There Exists: Quantifiers and Their Scope

**Track:** Mathematical Reasoning and Proof from First Principles. **Background:** Basic logical connectives. **Purpose:** teach an actual proof obligation and the reasoning required to discharge it.

---

#### Mathematical companion (not spoken)

##### Quantified forms

\[
\forall n\in\mathbb N\;\exists m\in\mathbb N\;(m>n)
\qquad\text{versus}\qquad
\exists m\in\mathbb N\;\forall n\in\mathbb N\;(m>n).
\]
The first is proved by \(m=n+1\); the second is false.

Classically:
\[
\neg\forall x\,P(x)\iff\exists x\,\neg P(x),\qquad
\neg\exists x\,P(x)\iff\forall x\,\neg P(x).
\]
A sequence \((a_n)\) converges to \(L\) if
\[
\forall\varepsilon>0\;\exists N\in\mathbb N\;\forall n\geq N:\ |a_n-L|<\varepsilon.
\]
The choice of \(N\) may depend on \(\varepsilon\).

##### Exercises with answers

1. Negate \(\forall x\in\mathbb R\;\exists y\in\mathbb R\;(y>x)\). **Answer:** \(\exists x\in\mathbb R\;\forall y\in\mathbb R\;(y\leq x)\).
2. Why is \(\forall n\,\exists m>n\) true but \(\exists m\,\forall n\,(m>n)\) false on \(\mathbb N\)? **Answer:** \(n+1\) is an allowed dependent witness; there is no fixed maximum natural number.
3. Negate 'some student solved every problem.' **Answer:** every student failed at least one problem.

##### Sources and further reading

- [Richard Hammack, Book of Proof, third edition (current online edition)](https://richardhammack.github.io/BookOfProof/).
- [Eric Lehman, F. Thomson Leighton and Albert R. Meyer, Mathematics for Computer Science, MIT OCW 6.042J](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/).
- [forall x: Calgary, A Free and Open Introduction to Formal Logic (Open Logic Project)](https://forallx.openlogicproject.org/).
- [Wikipedia: Quantifier (logic)](https://en.wikipedia.org/wiki/Quantifier_(logic)).

### Definitions and If-and-Only-If: Keeping Both Directions

**Track:** Mathematical Reasoning and Proof from First Principles. **Background:** Implications and quantifiers. **Purpose:** teach an actual proof obligation and the reasoning required to discharge it.

---

#### Mathematical companion (not spoken)

##### Directions of a biconditional

To prove \(P\iff Q\), supply two implications \(P\Rightarrow Q\) and \(Q\Rightarrow P\).

Example for \(n\in\mathbb Z\):
\[
n\equiv0\pmod 2\iff n^2\equiv0\pmod2.
\]
For the forward direction \(n=2k\) gives \(n^2=2(2k^2)\). For the reverse, prove the contrapositive: if \(n=2k+1\), then \(n^2=2(2k^2+2k)+1\), hence it is odd.

##### Exercises with answers

1. Is 'multiple of six' necessary or sufficient for 'multiple of three'? **Answer:** sufficient, not necessary.
2. Prove \(n\) divisible by \(10\) iff it is divisible by \(2\) and \(5\). **Answer:** necessity follows from \(10=2\cdot5\). For sufficiency, write \(n=5k\); its evenness forces \(k\) even (since \(5k\) and \(k\) have the same parity), so \(n=10m\).
3. Why does a proof of \(P\Rightarrow Q\) not automatically establish \(P\iff Q\)? **Answer:** the reverse implication remains to be shown.

##### Sources and further reading

- [Richard Hammack, Book of Proof, third edition (current online edition)](https://richardhammack.github.io/BookOfProof/).
- [Eric Lehman, F. Thomson Leighton and Albert R. Meyer, Mathematics for Computer Science, MIT OCW 6.042J](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/).
- [forall x: Calgary, A Free and Open Introduction to Formal Logic (Open Logic Project)](https://forallx.openlogicproject.org/).
- [Mathematics in Lean, Lean community documentation](https://leanprover-community.github.io/mathematics_in_lean/index.html).
- [Wikipedia: Necessity and sufficiency](https://en.wikipedia.org/wiki/Necessity_and_sufficiency).

### Direct Proof: Turning a Hypothesis into a Conclusion

**Track:** Mathematical Reasoning and Proof from First Principles. **Background:** Definitions of integers and divisibility. **Purpose:** teach an actual proof obligation and the reasoning required to discharge it.

---

#### Mathematical companion (not spoken)

##### Witness-based divisibility proof

For \(d\neq0\), \(d\mid a\) means \(\exists k\in\mathbb Z\;(a=dk)\). If \(5\mid a\) and \(5\mid b\), choose \(r,s\) with \(a=5r\), \(b=5s\); then \(a-b=5(r-s)\), so \(5\mid(a-b)\).

For subset transitivity,
\[
A\subseteq B\land B\subseteq C\Rightarrow A\subseteq C,
\]
fix arbitrary \(x\in A\), use each hypothesis to obtain \(x\in B\) then \(x\in C\). This works for \(A=\varnothing\).

##### Exercises with answers

1. Show that if \(3\mid a\) and \(3\mid b\), then \(3\mid(2a-5b)\). **Answer:** writing \(a=3r,b=3s\) gives \(2a-5b=3(2r-5s)\).
2. Prove that the sum of two nonnegative reals is nonnegative. **Answer:** add the two inequalities \(0\leq x\) and \(0\leq y\).
3. Which step is invalid when multiplying an inequality by an unknown real \(t\)? **Answer:** preserving its direction before establishing \(t\geq0\).

##### Sources and further reading

- [Richard Hammack, Book of Proof, third edition (current online edition)](https://richardhammack.github.io/BookOfProof/).
- [Eric Lehman, F. Thomson Leighton and Albert R. Meyer, Mathematics for Computer Science, MIT OCW 6.042J](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/).
- [Wikipedia: Direct proof](https://en.wikipedia.org/wiki/Direct_proof).

### Contraposition and Cases: Changing the Route, Not the Claim

**Track:** Mathematical Reasoning and Proof from First Principles. **Background:** Implication and direct proof. **Purpose:** teach an actual proof obligation and the reasoning required to discharge it.

---

#### Mathematical companion (not spoken)

##### Parity calculation

For any \(n\in\mathbb Z\), \(n^2\equiv 0\) or \(1\pmod4\).

- If \(n=2k\), then \(n^2=4k^2\).
- If \(n=2k+1\), then \(n^2=4k(k+1)+1\).

Thus no integer square is congruent to \(2\pmod4\).

##### Exercises with answers

1. Prove that if \(n^2\) is odd, then \(n\) is odd by contraposition. **Answer:** if \(n=2k\), then \(n^2=4k^2\) is even.
2. Show \(n(n+1)\) is even. **Answer:** for even \(n\), the first factor is even; for odd \(n\), \(n+1\) is even.
3. Why do cases \(x<0\) and \(x>0\) not exhaust the reals? **Answer:** \(x=0\) is omitted.

##### Sources and further reading

- [Richard Hammack, Book of Proof, third edition (current online edition)](https://richardhammack.github.io/BookOfProof/).
- [Eric Lehman, F. Thomson Leighton and Albert R. Meyer, Mathematics for Computer Science, MIT OCW 6.042J](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/).
- [Wikipedia: Proof by contrapositive](https://en.wikipedia.org/wiki/Proof_by_contrapositive).

### Contradiction: Proving Something Cannot Happen

**Track:** Mathematical Reasoning and Proof from First Principles. **Background:** Even and odd integers; direct proof. **Purpose:** teach an actual proof obligation and the reasoning required to discharge it.

---

#### Mathematical companion (not spoken)

##### Reduced-fraction contradiction

Assume \(\sqrt2=p/q\) with \(p,q\in\mathbb Z\), \(q\neq0\), and \(\gcd(|p|,|q|)=1\). Then \(p^2=2q^2\). Since an odd integer has odd square, \(p\) must be even: \(p=2r\). Hence \(q^2=2r^2\), making \(q\) even. Now \(2\mid p\) and \(2\mid q\), contrary to coprimality.

##### Exercises with answers

1. Prove there is no greatest integer. **Answer:** if \(M\) were greatest, \(M+1\) would be an integer greater than \(M\).
2. Does learning that both numerator and denominator are even contradict an arbitrary fractional representation? **Answer:** no; it contradicts a *reduced* representation.
3. Distinguish contradiction proving \(\neg P\) from classical contradiction proving \(P\). **Answer:** the first assumes \(P\) and derives falsehood; the second assumes \(\neg P\), derives falsehood, and uses double-negation elimination.

##### Sources and further reading

- [Richard Hammack, Book of Proof, third edition (current online edition)](https://richardhammack.github.io/BookOfProof/).
- [Eric Lehman, F. Thomson Leighton and Albert R. Meyer, Mathematics for Computer Science, MIT OCW 6.042J](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/).
- [forall x: Calgary, A Free and Open Introduction to Formal Logic (Open Logic Project)](https://forallx.openlogicproject.org/).
- [Wikipedia: Proof by contradiction](https://en.wikipedia.org/wiki/Proof_by_contradiction).

### Counterexamples: How One Example Defeats a General Claim

**Track:** Mathematical Reasoning and Proof from First Principles. **Background:** Universal statements and implication. **Purpose:** teach an actual proof obligation and the reasoning required to discharge it.

---

#### Mathematical companion (not spoken)

##### Counterexamples and repaired claims

| False statement | Counterexample | Useful repair |
|---|---|---|
| Every bounded real sequence converges | \(a_n=(-1)^n\) | Every bounded real sequence has a convergent subsequence |
| Every critical point is a maximum | \(f(x)=x^3\) at \(0\) | A negative second derivative yields a strict local maximum under standard smoothness hypotheses |
| Every continuous function on an interval attains a maximum | \(f(x)=x\) on \((0,1)\) | Every continuous real function on a nonempty compact set attains its maximum and minimum |

##### Exercises with answers

1. Refute 'every square of an integer is strictly positive.' **Answer:** \(0^2=0\).
2. Refute 'if \(f(A)=f(B)\), then \(A=B\)' for arbitrary functions. **Answer:** \(f(x)=x^2\), \(A=\{-1\}\), \(B=\{1\}\).
3. Explain the logical requirement for a counterexample to \(P\Rightarrow Q\). **Answer:** exhibit an admissible object with \(P\) true and \(Q\) false.

##### Sources and further reading

- [Richard Hammack, Book of Proof, third edition (current online edition)](https://richardhammack.github.io/BookOfProof/).
- [Eric Lehman, F. Thomson Leighton and Albert R. Meyer, Mathematics for Computer Science, MIT OCW 6.042J](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/).
- [Wikipedia: Counterexample](https://en.wikipedia.org/wiki/Counterexample).
