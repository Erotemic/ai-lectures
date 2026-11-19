# Sets, functions, quotients, induction, and existence

<!-- BEGIN SPOKEN LECTURE -->

# Sets, functions, quotients, induction, and existence

## Sets and Subsets: Proving Two Collections Are Equal

A set is a collection of objects, and the most important statement about a set is whether a particular object belongs to it. That simple relation allows us to define subsets, unions, intersections, complements, and products. It also gives an efficient proof technique: to establish a set identity, reason about an arbitrary element and show that membership is equivalent on both sides.

Suppose A is the set of integers divisible by two, and B is the set of integers divisible by three. Their intersection contains the multiples of six. The union contains integers divisible by at least one of two or three. These are different operations. If an integer belongs to A intersect B, it satisfies both conditions. If it belongs to A union B, it satisfies at least one.

### Proving inclusion and equality

To prove A is a subset of B, take an arbitrary x in A and prove x is in B. To prove A equals B, prove both A is a subset of B and B is a subset of A. A one-direction argument gives only inclusion, and examples cannot establish a set identity for arbitrary sets.

Consider the distributive law: A intersect the union of B and C equals the union of A intersect B with A intersect C. Begin with an element x on the left. It belongs to A, and it belongs to B or C. If it belongs to B, then it lies in A intersect B. If it belongs to C, it lies in A intersect C. So it lies on the right. Conversely, if x lies in either A intersect B or A intersect C, then it belongs to A and to at least one of B and C, putting it on the left. The algebraic identity has become a pair of logical arguments about membership.

### Complements and De Morgan's laws

Complements are always relative to a universe U. The complement of A consists of the elements of U not in A. If we forget U, expressions such as 'everything outside A' become ambiguous. De Morgan's laws say that the complement of A intersect B is the union of the complements, and that the complement of A union B is the intersection of the complements. Translate membership in the complement into 'not,' then use the corresponding logical law.

A similar method shows that A minus B equals A intersect the complement of B, again relative to a universe containing both sets. This is not a slogan about drawing overlapping circles. It is a membership proof that works for arbitrary sets, finite or infinite, even when drawing them is impractical.

### Subsets, elements, and the empty set

Distinguish 'x is an element of A' from 'A is a subset of B.' An element is an object in a collection; a subset is itself a collection whose elements all occur in another collection. The empty set is a subset of every set because there is no element of it that violates containment. However, the empty set is not automatically an element of every set. For example, it is not an element of the set containing only the number three.

The power set of A is the set of all subsets of A. If A contains exactly two distinct objects, its power set has four members: the empty set, the first singleton, the second singleton, and A itself. For a finite set with n elements, there are two to the n subsets, because each element may independently be included or excluded. This is an elementary counting proof with the structure of a binary choice for every element.

### Why unrestricted collections need care

One might try to define a set of all sets that are not members of themselves. If such a set R belonged to itself, its defining property would say it did not. If it did not belong to itself, the defining property would say it did. This is Russell's paradox. Modern axiomatic set theory avoids allowing every verbal property to define an unrestricted set. In everyday mathematical work, we often form subsets of an already specified universe, which avoids this immediate problem.

The lesson is not that sets are unreliable. It is that the domain and the rules for forming collections are part of mathematical foundations, just as domains mattered for quantifiers. The basic proof method—start with an arbitrary member and verify its properties—remains enormously useful.

Once you are comfortable with these arguments, set operations stop being decorative notation. They become a language for logical conditions. In topology, open-set arguments use unions and finite intersections. In probability, events are sets and probabilities apply to their unions and complements. In analysis, measurability is a property of collections of subsets. In all these subjects, a set identity is proved by controlling membership, not by trusting a diagram.

## Functions: Images, Preimages, Injections, and Inverses

A function is a rule assigning exactly one output to each input in a specified domain. The word 'specified' matters. The same algebraic expression can represent different functions when its domain or codomain changes. The squaring rule from the real numbers to the real numbers is not injective, because two and minus two have the same square. Restrict its domain to nonnegative reals, and it becomes injective. Restrict its codomain to nonnegative reals as well, and it becomes bijective.

Mathematical proofs about functions rely on four related ideas: images, inverse images, injectivity, and surjectivity. Each has its own quantifier pattern.

### Images and inverse images

For a subset A of the domain, the image f of A contains the values attained by f at inputs in A. For a subset B of the codomain, the inverse image of B contains inputs whose outputs belong to B. The latter makes sense for every function, whether or not it has an inverse function.

Let f of x be x squared on the real line. The image of the interval from minus one to two is the interval from zero to four. The inverse image of the interval from one to four is the union of the intervals from minus two to minus one and from one to two. The set we started with determines what kind of input or output we are testing. Mixing images with inverse images leads to incorrect inclusions.

There is a particularly useful identity: the inverse image of an intersection equals the intersection of the inverse images. To prove it, take an arbitrary x. Its output belongs to B intersect C exactly when its output belongs to B and belongs to C. That happens exactly when x lies in the inverse image of B and the inverse image of C. Both directions are built into the word 'exactly.' The same argument works for unions, complements, and arbitrary indexed unions or intersections.

### When images do not preserve intersections

For forward images we always have f of A intersect B contained in f of A intersect f of B. Equality may fail because the same output can come from different inputs. Let f be the squaring map, A contain only minus one, and B contain only one. Their intersection is empty, so its image is empty. But each set has image containing one, so the intersection of their images contains one. If f is injective, equality does hold: equal outputs then force equal inputs.

This is a small example of a powerful theorem-writing habit. We establish an inclusion unconditionally, construct a counterexample to equality, and then identify the extra hypothesis that restores equality.

### One-to-one and onto

A function is injective if equal outputs imply equal inputs. To prove injectivity, start with arbitrary inputs x and y and assume f of x equals f of y. For f of x equal to two x plus three on the real line, subtract three and divide by two to obtain x equals y. A function is surjective onto its codomain if every target value has at least one input. To prove this, take an arbitrary target y and solve for a valid input. For the same affine function, x equal to y minus three divided by two works for every real y.

Bijective means both injective and surjective. The first property guarantees at most one preimage of a target; the second guarantees at least one. Together they give exactly one, so an inverse function can be defined. For the affine example, that inverse sends y to y minus three divided by two.

### Composition and proof obligations

If f goes from A to B and g goes from B to C, their composition sends x to g of f of x. If both functions are injective, so is their composition. Suppose two inputs have equal composed outputs. Injectivity of g gives equality of their f outputs, and injectivity of f gives equality of the original inputs. This is a proof whose sequence of cancellations mirrors the structure of the composition.

If both functions are surjective, their composition is surjective too. Given a target c in C, surjectivity of g supplies an intermediate b in B. Surjectivity of f supplies an a in A mapping to b. Their composition maps a to c. Observe how the witnesses are selected in reverse order from the function composition.

These ideas will appear in coordinate maps, quotient constructions, optimization, and topology. The inverse image of an open set is central to continuity; bijections express equivalence between sets; linear maps impose special structure. The important habit is to read each property as the exact input-output obligation it represents, rather than relying on the vague phrase 'invertible-looking.'

## Equivalence Relations: Building New Objects by Identifying Old Ones

Sometimes different descriptions represent the same mathematical object. The fractions one half and two quarters are different ordered pairs of integers, but they represent the same rational number. The clock readings one o'clock and thirteen o'clock denote the same hour modulo twelve. In geometry, points on the two ends of a strip may be identified to make a cylinder. To reason rigorously about such constructions, we need equivalence relations and quotient sets.

An equivalence relation on a set satisfies three properties. Every element is related to itself; this is reflexivity. If a is related to b, then b is related to a; this is symmetry. If a is related to b and b is related to c, then a is related to c; this is transitivity. These are not arbitrary decorations. They guarantee that 'being the same for the purpose at hand' behaves consistently.

### Congruence as a complete example

On the integers, define a relation: a is equivalent to b when a minus b is divisible by three. Reflexivity holds because a minus a is zero, which is divisible by three. Symmetry holds because if a minus b equals three k, then b minus a equals three times minus k. Transitivity holds because if a minus b and b minus c are multiples of three, their sum a minus c is also a multiple of three.

The integers fall into three equivalence classes: those congruent to zero, one, and two modulo three. We can give each class a convenient representative, but a class contains every integer related to that representative. The quotient set consists of classes, not of a particular three-element list chosen by fiat.

### Why 'well-defined' deserves a proof

We want to add two congruence classes by choosing representatives, adding the integers, and taking the class of the sum. But what if we choose different representatives? Suppose a is congruent to a prime and b to b prime, modulo three. Then a minus a prime and b minus b prime are multiples of three. Their sum is a plus b minus a prime minus b prime, also a multiple of three. Thus both choices produce the same output class. Addition on the quotient is well-defined.

The word 'well-defined' means the rule depends only on the mathematical object, not on the accidental description we used to compute it. This is a frequent issue in advanced mathematics. A vector in a quotient space has many representatives. A differential form's coordinate formula varies across charts. A function on equivalence classes must give the same answer no matter which representative is used.

### Not every proposed operation descends

Suppose we try to assign to a congruence class modulo three the ordinary integer 'the square of its representative' rather than the square class. Zero and three represent the same class, but their integer squares are zero and nine. The proposed integer-valued rule is not well-defined. If instead we take the class of the square, it is well-defined, because congruent integers have congruent squares. The target of an operation matters as much as its formula.

A quotient is not simply permission to erase distinctions. It is permission to erase distinctions that a carefully checked construction does not depend on. Whenever you encounter a new quotient, ask what its elements are, what relation defines them, and why later formulas respect that relation.

### Partitions and equivalence relations

The equivalence classes form a partition of the original set: every element lies in a class, no class is empty, and two classes are either identical or disjoint. Conversely, a partition into nonempty pieces defines an equivalence relation by declaring two objects equivalent exactly when they belong to the same piece. This duality explains why quotient sets are a natural way to organize all the possibilities.

The relation need not come from arithmetic. Two words may be equivalent if one is an anagram of the other. Two paths may be identified if they can be continuously deformed into each other under specified endpoint restrictions. Two functions may be considered equivalent if they differ only on a set of measure zero. Each of those cases requires care in defining the relation and proving the three properties.

Equivalence relations connect basic logic to algebra and topology. A quotient construction is a definition combined with a proof obligation: show the identification is coherent, then show the operations you wish to use descend to the identified objects. Once that obligation is satisfied, the quotient becomes a legitimate mathematical space rather than a shorthand for inconsistent choices.

## Induction: Why Proving One Step Can Prove Infinitely Many

How could we prove one statement about every natural number without checking infinitely many numbers one by one? Mathematical induction provides an answer when the statements have a structure that passes from one integer to the next. It is not a prediction that a pattern will continue because we saw it continue many times. It is a proof that the mechanism forcing the next case works for every case.

The principle has two parts. First establish a base case. Then prove that whenever the claim holds at a generic natural number n, it also holds at the next number. The base case starts the chain, and the general step ensures it never stops. Together they establish the claim for all natural numbers in the chosen range.

### A sum formula from the ground up

Consider the sum of the first n positive integers. We claim it equals n times n plus one, divided by two. For n equals one, the sum is one, and the formula also gives one. This is the base case. Now assume, for some arbitrary positive integer n, that the formula is correct. This is the induction hypothesis. The sum through n plus one is the old sum plus n plus one. Replace the old sum using the hypothesis. Factor the resulting expression: it becomes n plus one times n plus two, divided by two. That is exactly the formula with n replaced by n plus one.

The algebra completes the step. The induction principle completes the universal conclusion. It is worth distinguishing them. A correct calculation of the step does not help without a valid starting case. A correct starting case does not help unless the step handles an arbitrary n rather than just the first few values.

### Why the induction hypothesis is allowed

At first, induction sounds suspicious: how can we assume what we are trying to prove? We do not assume the theorem for all numbers. We prove a conditional statement: if it holds at an arbitrary n, then it holds at n plus one. That conditional can be valid even before we know whether the antecedent holds at any particular n. Once the base case is established, repeated application of the conditional covers each natural number.

A useful analogy is a staircase. You prove you can stand on the first step. You prove that from any occupied step you can move to the next. It follows that you can reach any step, provided the steps are the natural-number sequence and there are no missing links. The analogy is intuitive, but the mathematical principle is the well-ordering structure of the natural numbers.

### Induction can prove divisibility

Prove that seven divides eight to the n minus one for every nonnegative integer n. At n equals zero, eight to the zero minus one is zero, divisible by seven. Assume eight to the n minus one equals seven times some integer k. Then eight to the n plus one minus one equals eight times eight to the n minus one plus seven. Substitute the hypothesis and obtain seven times eight k plus one. Therefore the next value is divisible by seven. The witness for divisibility is eight k plus one.

This proof illustrates an important technique: rewrite the n plus one expression in terms of the n expression. A successful induction step almost always relies on finding that connection. If the new expression looks unrelated, try factoring, splitting the final summand, or using a recursive description.

### Invariants in algorithms

Induction also explains loop invariants. A loop invariant is a property true before the first iteration and preserved by every iteration. If the program terminates, the invariant is true when it stops. But an invariant alone does not prove termination, and it may not establish the desired output without a final argument connecting the stopping condition to the result.

For example, a running-sum algorithm maintains the claim that its accumulator equals the sum of entries already processed. At initialization no entries have been processed, and the accumulator is zero. Processing one more entry adds its value to both the intended sum and the accumulator, preserving equality. At termination all entries have been processed, so the invariant identifies the accumulator with the total sum.

### Indexing discipline

If a theorem starts at n equals zero, check zero. If it starts at one, check one. If a step needs n minus one or division by n, confirm that the values under discussion permit those operations. One can accidentally prove a statement only for n at least two while claiming it for all natural numbers.

The value of induction extends far beyond numerical formulas. It underlies recursive data structures, combinatorial arguments, finite graphs, formal verification, and constructive proofs. To use it well, identify the statement that needs to be preserved and make the move from one stage to the next explicit. The point is a justified infinite conclusion from a finite pattern of reasoning, not a pattern of successful numerical trials.

## Strong Induction, Recursion, and Well-Ordering

Ordinary induction proves a statement at n plus one from its truth at n. Sometimes a problem needs information about several earlier stages, not just the immediately preceding one. Strong induction says we may assume the statement for every smaller natural number when proving it for n, provided we have established the appropriate starting point. Strong induction is not a stronger conclusion than ordinary induction; it is a different way of organizing the same well-ordering structure.

### Factoring a natural number into primes

Every integer greater than one is a product of primes. To prove this, consider any integer n greater than one and suppose the claim is already known for every integer strictly between one and n. If n is prime, it is a product of one prime, itself. Otherwise n is composite, so n equals a times b for integers a and b strictly between one and n. By the strong induction hypothesis, both a and b can be expressed as products of primes. Concatenating those factorizations gives a prime factorization of n.

The proof would be awkward using only the case n minus one, because the factors a and b need not be n minus one. Strong induction permits us to use whatever smaller values the structure of the number actually supplies. We must still show that a and b are smaller than n; otherwise the use of the induction hypothesis would be unjustified.

### The least-counterexample viewpoint

Suppose the theorem were false. Then there would be at least one integer greater than one with no prime factorization. By the well-ordering principle, the set of counterexamples has a least element n. It cannot be prime. If it is composite, its two proper positive factors are smaller than n and therefore are not counterexamples. They have prime factorizations, so n does too, a contradiction. This proof is the strong-induction argument told from the other direction.

Well-ordering says every nonempty subset of the natural numbers has a least element. It is more than the assertion that we can sort a finite list. It applies to arbitrary nonempty sets of natural numbers, even infinite ones. This principle can be used to prove ordinary induction and vice versa, given the standard natural-number setting.

### Recursive descriptions and algorithms

A recursive definition expresses a new value through earlier ones. The factorial function satisfies factorial of zero equals one, and factorial of n plus one equals n plus one times factorial of n. These clauses specify a value at every natural number because each evaluation moves toward the base case. A recursive program that calls itself on the same input may not terminate; the mere presence of recursive syntax does not establish a well-defined finite computation.

For the greatest common divisor, the Euclidean algorithm repeatedly replaces a pair of nonnegative integers by the smaller member and its remainder. The key fact is that the remainder is strictly smaller than the previous positive divisor. That quantity is a decreasing nonnegative integer, so the process cannot continue forever. The algorithm also preserves the set of common divisors because a number divides both a and b exactly when it divides b and the remainder after dividing a by b. Together, preservation and termination justify its result.

This is a common two-part proof in algorithms: an invariant establishes correctness if the algorithm stops, and a well-founded measure establishes that it must stop. In discrete mathematics, structural induction on trees, lists, and expressions follows the same idea: prove a property for basic constructors, then show that building a larger object from smaller ones preserves it.

### A recurrence with two predecessors

Consider the Fibonacci sequence, defined by its first two values and by each later value being the sum of the previous two. To prove that all terms are nonnegative, the base requires both starting values. In the step for term n plus one, we need nonnegativity of two earlier terms. Strong induction provides both, or we can strengthen the ordinary induction invariant to cover a consecutive pair. This choice illustrates proof design: sometimes a more informative induction hypothesis makes an argument easier.

Induction is not only a technique for statements involving an n in a formula. It is a way of exploiting well-founded construction. Whenever a mathematical object is made from smaller objects, ask what the notion of 'smaller' is and why descending forever is impossible. The answer may be a natural number, tree height, expression size, or another well-founded order. Once that structure is explicit, a proof that initially looked infinite becomes a finite case analysis plus a justified recursive step.

## Countable and Uncountable: Comparing Infinite Sets

Two finite sets have the same number of elements when there is a pairing that matches each element of one set with exactly one element of the other, with nothing left over. This idea extends to infinite sets. A bijection—one-to-one and onto—becomes the definition of equal cardinality. It can lead to surprising results, but the surprises become manageable when we prove the pairings carefully.

The natural numbers and the even natural numbers can be paired by sending n to two n. Every natural number has a unique even image, and every even natural number is twice a unique natural number. The even numbers form a proper subset of the natural numbers, yet the two infinite sets have the same cardinality. This would be impossible for finite sets. Infinity changes how containment relates to size.

### Enumerating the integers

The set of all integers is countable: one can list zero, one, minus one, two, minus two, and continue. Every integer appears after finitely many steps, and no integer needs to appear more than once. A countably infinite set is one whose members can be matched bijectively with the natural numbers. Some authors include finite sets under the label countable; whenever the distinction matters, say 'at most countable' or 'countably infinite.'

Fractions require more work. Every positive rational number has some representation as a positive numerator divided by a positive denominator. Arrange the pairs of positive integers in an infinite grid. Traverse the grid along diagonals of fixed numerator plus denominator. This ensures that each pair is eventually visited. Some pairs represent the same rational number, so skip repetitions in reduced form. The resulting list contains every positive rational number. Include zero and negative rationals by interleaving, and the full set of rational numbers is countable.

The argument is about an explicit enumeration, not an unexplained slogan that a grid is 'obviously' countable. The diagonal order is what ensures no pair is permanently postponed.

### Why the real numbers are different

Consider the set of all infinite sequences of zeros and ones. Suppose someone claims to list every such sequence. Read the first entry's first digit, the second entry's second digit, and so on. Construct a new sequence that differs from the first entry in digit one, from the second in digit two, and generally from entry n in digit n. Change zero to one and one to zero at the diagonal position. The new sequence differs from every listed sequence somewhere, so it cannot be in the list. No claimed enumeration is complete.

This is Cantor's diagonal argument. It does not rely on choosing a large number of counterexamples; it builds one counterexample tailored to any proposed infinite list. The universal part is the phrase 'any proposed list.'

To connect this to real numbers without getting tangled in nonunique binary decimal representations, encode each zero-one sequence as a real number whose base-three digits are only zero and two. Distinct such sequences give distinct real numbers in the Cantor set; restricting to those digits prevents the standard ambiguous expansion from equating two different restricted sequences. The set of these reals is therefore uncountable. Since it sits inside the real interval from zero to one, that interval is uncountable too.

### What the diagonal proof does and does not show

A diagonal argument disproves the existence of a complete enumeration. It does not provide a physical procedure that prints every real number, and it does not claim that one could inspect infinitely many rows in finite time. It is a mathematical construction specified for any hypothetical list, with a clear reason that the new object evades each entry.

The distinction between countable and uncountable often appears when interpreting 'almost every,' genericity, and the size of families of functions. The real line contains infinitely more possibilities in cardinality than the natural numbers, but cardinality is not probability or length. The rationals are countable and dense on the real line; between any two distinct reals lies a rational. A dense set need not have large cardinality or positive length.

### Proofs about infinite sets require explicit maps

When you claim two sets have equal cardinality, write down a bijection or combine precise inequalities using a theorem such as Cantor–Bernstein. When you claim a set is countable, exhibit an enumeration or an injection into the natural numbers. When you claim a set is uncountable, explain why no enumeration can work. The subject is often introduced through paradoxes, but its proof obligations are the same as in elementary functions: construct maps, check domains, verify injectivity or surjectivity, and justify every quantifier.

## Existence, Uniqueness, and Constructive Descriptions

Many theorems say that an object exists. A stronger theorem may say that there is exactly one such object. These are two separate responsibilities. To prove existence, supply a construction or an argument that rules out nonexistence. To prove uniqueness, suppose there are two admissible objects and show they must be equal. An existence proof does not establish uniqueness, and a uniqueness proof can be valid even when nothing exists.

### A simple equation with a unique solution

Take the equation two x plus three equals eleven, with x required to be a real number. We produce x equals four, and direct substitution verifies that it works. This is existence. For uniqueness, suppose x and y both solve the equation. Then two x plus three and two y plus three both equal eleven, so two x equals two y. Dividing by two gives x equals y. There is at most one solution. Combining both parts shows there is exactly one.

Notice the two different logical structures. Existence states 'there is some x with the property.' Uniqueness states 'for all x and y with the property, x equals y.' A writer who says 'the solution' before establishing either requirement may be silently assuming what needs proof.

### Nonconstructive existence and explicit construction

Some existence proofs identify a witness. Others derive existence without a formula for the witness. The intermediate value theorem states that a continuous real function on a closed interval takes every value between its endpoint values. Under its hypotheses, if f at a is negative and f at b is positive, a root exists somewhere in the interval. The theorem does not by itself tell us a finite exact expression for that root.

The bisection method builds nested intervals containing a root and can approximate it to any prescribed accuracy when the sign and continuity assumptions are satisfied. An approximation procedure is extra information beyond the bare existence theorem. Separating the claim that an object exists from the claim that we can calculate it efficiently becomes essential in optimization, numerical analysis, and computability.

### Well-definedness is a third obligation

Suppose we define a function on rational numbers by taking a fraction p over q and sending it to p plus q. This does not define a function of the rational number: one half can be written one over two or two over four, producing outputs three and six. The rule depends on a choice of representation. To construct a function on equivalence classes, prove that different representatives always give the same output. Only then is there a well-defined object to discuss.

A proof may therefore have several stages: define a candidate, show it is well-defined, show it has the required property, and show it is unique. Textbooks sometimes compress these into a single paragraph. When learning the argument, it helps to separate them so no obligation is lost.

### Uniqueness in linear algebra

Suppose v one through v k is a basis of a vector space. By spanning, every vector can be written as a linear combination of the basis vectors: existence of coordinates. By linear independence, those coordinates are unique. If two coefficient lists represented the same vector, subtract the expansions to obtain a linear combination equal to zero. Independence forces each coefficient difference to vanish. The proof of a coordinate system is therefore an existence-and-uniqueness theorem in disguise.

The same structure appears in differential equations. A theorem may guarantee that an initial-value problem has a solution and that no two distinct solutions satisfy the same initial condition. But without hypotheses such as appropriate regularity of the vector field, uniqueness may fail. For example, the equation y prime equals the square root of the absolute value of y, with initial value y of zero equal to zero, allows a zero solution and delayed-start solutions. Continuous right-hand sides alone need not guarantee uniqueness.

### Reading a theorem with an existential conclusion

Ask whether the theorem claims one witness, at least one, at most one, or exactly one. Ask which assumptions are used for each part. If a proof defines something by a choice of representative, ask whether the result is independent of that choice. If it defines an object as a limit, ask whether the limit exists and is independent of the approximating sequence. If it defines a map as 'the unique' solution of an equation, check the uniqueness argument rather than trusting the definite article.

These questions may sound elementary, but they reappear at every level: the uniqueness of a derivative, existence and uniqueness for differential equations, the construction of a completed metric space, the definition of an integral, and the classification of algebraic structures. A reliable proof tells us what exists, why it exists, and whether other choices could change the answer.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Sets and Subsets: Proving Two Collections Are Equal

**Track:** Mathematical Reasoning and Proof from First Principles. **Background:** Logic and quantified definitions. **Purpose:** teach an actual proof obligation and the reasoning required to discharge it.

---

#### Mathematical companion (not spoken)

##### Membership proof of distributivity

For any \(x\),
\[
\begin{aligned}
x\in A\cap(B\cup C)
&\iff (x\in A)\land[(x\in B)\lor(x\in C)]\\
&\iff [(x\in A)\land(x\in B)]\lor[(x\in A)\land(x\in C)]\\
&\iff x\in(A\cap B)\cup(A\cap C).
\end{aligned}
\]
As the equivalence holds for every \(x\), the sets are equal.

##### Exercises with answers

1. Prove \(A\setminus B=A\cap B^c\) relative to universe \(U\). **Answer:** both sides contain exactly the elements of \(A\) that are not in \(B\).
2. Is \(\varnothing\subseteq A\) always true? **Answer:** yes; no element violates inclusion.
3. Is \(\varnothing\in A\) always true? **Answer:** no; e.g. \(A=\{3\}\).
4. List the power set of \(\{a,b\}\). **Answer:** \(\{\varnothing,\{a\},\{b\},\{a,b\}\}\).

##### Sources and further reading

- [Richard Hammack, Book of Proof, third edition (current online edition)](https://richardhammack.github.io/BookOfProof/).
- [Eric Lehman, F. Thomson Leighton and Albert R. Meyer, Mathematics for Computer Science, MIT OCW 6.042J](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/).
- [Wikipedia: Set (mathematics)](https://en.wikipedia.org/wiki/Set_(mathematics)).

### Functions: Images, Preimages, Injections, and Inverses

**Track:** Mathematical Reasoning and Proof from First Principles. **Background:** Sets, quantifiers, and basic algebra. **Purpose:** teach an actual proof obligation and the reasoning required to discharge it.

---

#### Mathematical companion (not spoken)

##### Image and preimage identities

For \(f:X\to Y\), \(A\subseteq X\), and \(B,C\subseteq Y\),
\[
f^{-1}(B\cap C)=f^{-1}(B)\cap f^{-1}(C),\qquad f^{-1}(Y\setminus B)=X\setminus f^{-1}(B).
\]
Here \(f^{-1}(B)\) denotes an inverse **image**, which requires no inverse function.
In general \(f(A\cap A')\subseteq f(A)\cap f(A')\); equality follows when \(f\) is injective. For the square map with \(A=\{-1\}\), \(A'=\{1\}\), the inclusion is strict.

##### Exercises with answers

1. For \(f(x)=x^2\) on \(\mathbb R\), find \(f^{-1}([1,4])\). **Answer:** \([-2,-1]\cup[1,2]\).
2. Prove the composition of two injections is injective. **Answer:** from \(g(f(x))=g(f(y))\), injectivity of \(g\) gives \(f(x)=f(y)\); injectivity of \(f\) gives \(x=y\).
3. Why is \(f(x)=x^2\) not surjective as a map \(\mathbb R\to\mathbb R\)? **Answer:** no real input maps to \(-1\).

##### Sources and further reading

- [Richard Hammack, Book of Proof, third edition (current online edition)](https://richardhammack.github.io/BookOfProof/).
- [Eric Lehman, F. Thomson Leighton and Albert R. Meyer, Mathematics for Computer Science, MIT OCW 6.042J](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/).
- [Wikipedia: Function (mathematics)](https://en.wikipedia.org/wiki/Function_(mathematics)).

### Equivalence Relations: Building New Objects by Identifying Old Ones

**Track:** Mathematical Reasoning and Proof from First Principles. **Background:** Sets and functions. **Purpose:** teach an actual proof obligation and the reasoning required to discharge it.

---

#### Mathematical companion (not spoken)

##### Congruence and quotient operations

Define \(a\sim b\iff3\mid(a-b)\) on \(\mathbb Z\). The relation is reflexive, symmetric, and transitive. Classes are \([0],[1],[2]\). For addition,
\[
[a]+[b]:=[a+b].
\]
If \(a\sim a'\) and \(b\sim b'\), then
\[
(a+b)-(a'+b')=(a-a')+(b-b')
\]
is a multiple of three; hence the operation is independent of representatives. By contrast, \([a]\mapsto a^2\in\mathbb Z\) is not well-defined because \([0]=[3]\) but \(0^2\neq3^2\).

##### Exercises with answers

1. Show that congruence modulo \(m>0\) is an equivalence relation. **Answer:** use divisibility of \(0\), closure under negation, and closure under addition.
2. Is \([a]\mapsto[a^2]\) well-defined modulo three? **Answer:** yes, as \(a^2-b^2=(a-b)(a+b)\) is divisible by three whenever \(a-b\) is.
3. Why must equivalence classes be either disjoint or equal? **Answer:** a shared element \(z\) yields \(a\sim z\sim b\) and hence each representative is related to the other.

##### Sources and further reading

- [Richard Hammack, Book of Proof, third edition (current online edition)](https://richardhammack.github.io/BookOfProof/).
- [Eric Lehman, F. Thomson Leighton and Albert R. Meyer, Mathematics for Computer Science, MIT OCW 6.042J](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/).
- [Wikipedia: Equivalence relation](https://en.wikipedia.org/wiki/Equivalence_relation).

### Induction: Why Proving One Step Can Prove Infinitely Many

**Track:** Mathematical Reasoning and Proof from First Principles. **Background:** Natural numbers, algebra, implications. **Purpose:** teach an actual proof obligation and the reasoning required to discharge it.

---

#### Mathematical companion (not spoken)

##### Sum and divisibility inductions

For \(n\geq1\), let \(P(n):\sum_{k=1}^n k=n(n+1)/2\). Base \(n=1\) holds; the step is
\[
\sum_{k=1}^{n+1}k=\frac{n(n+1)}2+(n+1)
=\frac{(n+1)(n+2)}2.
\]
For \(n\geq0\), \(7\mid(8^n-1)\). With \(8^n-1=7k\),
\[
8^{n+1}-1=8(8^n-1)+7=7(8k+1).
\]

##### Exercises with answers

1. Show \(1+3+\cdots+(2n-1)=n^2\) for positive \(n\). **Answer:** add \(2n+1\) to \(n^2\) and obtain \((n+1)^2\).
2. Why does the step \(P(n)\Rightarrow P(n+1)\) alone not prove all \(P(n)\)? **Answer:** no base case has been established.
3. Give the invariant of an array-summing loop. **Answer:** after processing the first \(k\) entries, the accumulator is their sum.

##### Sources and further reading

- [Richard Hammack, Book of Proof, third edition (current online edition)](https://richardhammack.github.io/BookOfProof/).
- [Eric Lehman, F. Thomson Leighton and Albert R. Meyer, Mathematics for Computer Science, MIT OCW 6.042J](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/).
- [Wikipedia: Mathematical induction](https://en.wikipedia.org/wiki/Mathematical_induction).

### Strong Induction, Recursion, and Well-Ordering

**Track:** Mathematical Reasoning and Proof from First Principles. **Background:** Mathematical induction and divisibility. **Purpose:** teach an actual proof obligation and the reasoning required to discharge it.

---

#### Mathematical companion (not spoken)

##### Strong induction and a termination measure

Let \(P(n)\): 'if \(n\geq2\), then \(n\) is a finite product of primes.' Assuming \(P(k)\) for every \(2\leq k<n\), either \(n\) is prime or \(n=ab\) with \(2\leq a,b<n\). By the hypothesis both factors have prime factorizations. This proves \(P(n)\).

For the Euclidean algorithm, if \(a=qb+r\), \(0\leq r<b\), then
\[
\gcd(a,b)=\gcd(b,r).
\]
The positive divisor in the recursive pair strictly decreases, guaranteeing termination by well-ordering of \(\mathbb N\).

##### Exercises with answers

1. Prove a finite rooted binary tree has an odd number of vertices when each internal vertex has two children. **Answer:** by structural induction: a leaf has one; joining two trees under a new root changes the count to \(1+(2a+1)+(2b+1)=2(a+b+1)+1\).
2. Explain why a recursive function with a base clause might still fail to terminate. **Answer:** recursive calls may not approach a well-founded smaller argument.
3. State a measure proving termination of repeated subtraction from a positive integer. **Answer:** the nonnegative integer current value, provided each step strictly decreases it and remains nonnegative.

##### Sources and further reading

- [Richard Hammack, Book of Proof, third edition (current online edition)](https://richardhammack.github.io/BookOfProof/).
- [Eric Lehman, F. Thomson Leighton and Albert R. Meyer, Mathematics for Computer Science, MIT OCW 6.042J](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/).
- [Mathematics in Lean, Lean community documentation](https://leanprover-community.github.io/mathematics_in_lean/index.html).
- [Wikipedia: Well-ordering principle](https://en.wikipedia.org/wiki/Well-ordering_principle).

### Countable and Uncountable: Comparing Infinite Sets

**Track:** Mathematical Reasoning and Proof from First Principles. **Background:** Functions and injections. **Purpose:** teach an actual proof obligation and the reasoning required to discharge it.

---

#### Mathematical companion (not spoken)

##### Explicit countability and diagonal arguments

\(\mathbb Z\) is countable by \(0,1,-1,2,-2,\ldots\). The positive rationals are covered by pairs \((p,q)\in\mathbb N_{>0}^2\) ordered by \(p+q\), skipping duplicate fractions.

Given any alleged enumeration \(s_1,s_2,\ldots\) of binary sequences \(s_n\in\{0,1\}^{\mathbb N}\), define
\[
t_n=1-s_n(n).
\]
Then \(t\neq s_n\) for every \(n\), since they differ at position \(n\). Thus binary sequences are uncountable.

To inject binary sequences into \([0,1]\), use
\[
(b_n)_{n\ge1}\mapsto\sum_{n=1}^\infty\frac{2b_n}{3^n}.
\]
This map is injective: at the earliest differing digit \(k\), the difference in that digit's contribution, \(2/3^k\), exceeds the entire maximal tail difference \(\sum_{n>k}2/3^n=1/3^k\).

##### Exercises with answers

1. Give a bijection between \(\mathbb N\) and the even nonnegative integers. **Answer:** \(n\mapsto 2n\).
2. Why does the diagonal sequence differ from every listed sequence? **Answer:** it differs from row \(n\) at coordinate \(n\).
3. Does density imply uncountability? **Answer:** no; \(\mathbb Q\) is countable and dense in \(\mathbb R\).

##### Sources and further reading

- [Richard Hammack, Book of Proof, third edition (current online edition)](https://richardhammack.github.io/BookOfProof/).
- [Eric Lehman, F. Thomson Leighton and Albert R. Meyer, Mathematics for Computer Science, MIT OCW 6.042J](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/).
- [Wikipedia: Cantor%27s diagonal argument](https://en.wikipedia.org/wiki/Cantor%27s_diagonal_argument).

### Existence, Uniqueness, and Constructive Descriptions

**Track:** Mathematical Reasoning and Proof from First Principles. **Background:** Quantifiers, functions, and direct proofs. **Purpose:** teach an actual proof obligation and the reasoning required to discharge it.

---

#### Mathematical companion (not spoken)

##### Existence versus uniqueness

To prove \(\exists!x\,P(x)\), give a witness \(x_0\) satisfying \(P\) and prove
\[
\forall x,y\;(P(x)\land P(y)\Rightarrow x=y).
\]
For \(2x+3=11\), existence comes from \(x=4\); uniqueness from \(2x+3=2y+3\Rightarrow x=y\).

The initial value problem \(y'=\sqrt{|y|}\), \(y(0)=0\) has nonunique differentiable solutions on \(t\geq0\): \(y(t)\equiv0\), and for each \(c\geq0\),
\[
y_c(t)=\begin{cases}
0,&t\leq c\\
(t-c)^2/4,&t>c.
\end{cases}
\]
Each satisfies the same initial condition and differential equation. This motivates additional hypotheses in uniqueness theorems.

##### Exercises with answers

1. Prove that a vector has at most one coordinate list relative to a linearly independent family. **Answer:** subtract two representations; independence makes every coefficient difference zero.
2. Why does 'at most one solution' not imply 'there is a solution'? **Answer:** a problem may have none.
3. Is \([p/q]\mapsto p+q\) a well-defined map on rational numbers? **Answer:** no; \(1/2=2/4\) but the proposed outputs differ.

##### Sources and further reading

- [Richard Hammack, Book of Proof, third edition (current online edition)](https://richardhammack.github.io/BookOfProof/).
- [Eric Lehman, F. Thomson Leighton and Albert R. Meyer, Mathematics for Computer Science, MIT OCW 6.042J](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/).
- [Wikipedia: Uniqueness theorem](https://en.wikipedia.org/wiki/Uniqueness_theorem).
