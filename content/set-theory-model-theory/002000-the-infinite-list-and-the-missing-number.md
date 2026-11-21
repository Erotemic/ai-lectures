# The Infinite List and the Missing Number: Countability and the Diagonal

<!-- BEGIN SPOKEN LECTURE -->

Imagine an infinitely long hotel in which every room is occupied. The rooms are numbered one, two, three, and so on. A new guest arrives. The clerk announces that each current guest should move from room n to room n plus one. Room one is now empty. With infinitely many occupied rooms, the hotel has still made room for someone else.

This story is often presented as a surprise about infinity. But it has a precise mathematical explanation: the positive integers and the positive integers other than one can be placed in a bijection. Moving every guest by one is an explicit bijection between the old rooms and the new rooms. We can make a second bijection between all natural numbers and the even natural numbers by doubling. Each even number has exactly one preimage, and every input yields an even number. The set of even numbers is a proper subset of the naturals, yet it has the same cardinality.

The harder question is how to compare two infinite collections when we cannot simply count their elements to the end. Cantor's answer is to compare them by functions. We will first build some surprising bijections, then prove that no such bijection can enumerate the real numbers. Finally we will prove a theorem that makes cardinal comparison much more robust: if each of two sets embeds into the other, then they are the same size.

## Countability is about being enumerable

Call a set countably infinite if there is a bijection between it and the natural numbers. A set is at most countable if it is finite or countably infinite. To say a collection can be listed means that its elements may be arranged as a finite or infinite sequence which eventually includes each one. Repetitions do not help, but they need not spoil a list; duplicates can be removed from an enumeration when the set is infinite and the first appearances can be selected.

The integers are countable. One enumeration goes zero, one, negative one, two, negative two, three, negative three, and so on. Nothing restricts the integers to the positive direction. The rational numbers are also countable, despite being dense in the real line. Between any two distinct rationals there are infinitely many other rationals. Density describes order, not cardinality.

To enumerate the positive rationals, arrange fractions p over q in a grid, where p and q are positive integers. Sweep the grid by increasing p plus q. At each finite diagonal there are only finitely many pairs. Every positive rational has at least one representation and so appears somewhere in this sweep. Skip duplicate values, such as two over two after one over one. Include zero and negative rationals by interleaving signs. This gives an enumeration of all rationals.

An important detail is hidden in that construction. To show countability, we need an enumeration or an injection into the naturals, not merely a story that says we could probably arrange the elements. Here the bound on p plus q supplies an actual finite-stage order. It is also why a countable union of countable sets is countable when the relevant enumerations are given. In general ZF, the stronger statement for arbitrary countable families without already chosen enumerations can use a weak form of the axiom of choice; one should not silently assume those choices in a foundations discussion.

## Why decimals refuse to fit

Now suppose someone claims to list all real numbers between zero and one. Imagine the list extends forever, and write each listed number in a decimal expansion that never ends with an infinite tail of nines. Such a convention removes the familiar ambiguity between a decimal ending in zeros and a second decimal ending in nines.

Read the first digit of the first number, the second digit of the second number, the third digit of the third, and so on. Construct a new number by changing each digit. To avoid decimal ambiguity entirely, choose the new digit to be one if the diagonal digit is not one, and two if the diagonal digit is one. Every digit of the new number is either one or two, so it cannot end in a tail of nines. It is a legitimate number in the interval from zero to one.

It cannot equal the first listed number because their first digits differ. It cannot equal the seventeenth because their seventeenth digits differ. And it cannot equal the nth number because their nth digits differ. Thus the claimed list omits the constructed number. This proves that the interval from zero to one is uncountable.

Notice what the argument does not require. We did not search the real line to find an overlooked point. We did not need to know the order of the list. We defined a new number using the list itself and arranged for a different digit at each index. No cleverer listing avoids the contradiction, because the construction adapts to whatever list is proposed.

There is an even cleaner version using infinite binary sequences. Each natural number labels a row, each row is a function from the naturals to a two-element set, and we flip the nth bit of the nth row. This is exactly Cantor's power-set proof applied to the natural numbers. The decimal and subset versions are two presentations of the same obstruction: a set cannot enumerate all of its own yes-or-no assignments.

## Two injections are enough

Infinite cardinalities produce a problem that finite counting usually conceals. Suppose A can be injected into B, and B can be injected into A. Is it necessarily true that A and B are bijective? For finite sets, yes, by counting. For arbitrary sets, it is also yes, by the Cantor–Schröder–Bernstein theorem. Crucially, this theorem does not require the axiom of choice.

We can understand its proof using a pair of noncolliding maps. Let f send A injectively into B, and let g send B injectively into A. Think of a directed graph whose vertices are the elements of two disjoint copies of A and B. Draw an arrow from each A element to its f-image in B, and from each B element to its g-image in A. Alternatively, compose to obtain an injection h from A into A, where h equals g after f.

Look at the A elements not reached by g from any B element. Call that set A zero. Starting from those elements, repeatedly apply h. This produces a forward-invariant set C, consisting of A zero, h of A zero, h twice of A zero, and so forth. Because h is injective, these successive layers do not create conflicting assignments, and C can be described as their union.

On C we use f to map elements into B. Outside C we use the inverse of g on the range of g. Why is the inverse available there? Every element outside C cannot be in A zero, so it lies in the image of g. Because g is injective, its preimage is unique.

We must check two things. First, the two pieces do not collide. If f of a from C equaled the g-inverse of some a prime outside C, then applying g would give h of a equals a prime. But C is closed under h, contradiction. Second, the two pieces cover B. Take any b in B. If g of b lies outside C, then b appears through the inverse-of-g branch. Otherwise g of b lies in C. Since g of b is in the image of g, it is not in A zero. It must therefore be h of some a in C, and injectivity of g yields b equals f of a. So b appears through the f branch. The combined map is a bijection.

The construction may sound technical, but its governing idea is simple: the injections already supply enough information to match nearly everything, and only some forward chains need to be handled in one direction instead of the other. We never arbitrarily choose an element from every set. The matching rule is determined by the two given injections.

## Cardinal arithmetic is not ordinary arithmetic

For finite sets, adding one element raises cardinality by one. For infinite countable sets, adding one element leaves cardinality unchanged. The naturals paired with a new object are still countably infinite. The set of all ordered pairs of natural numbers is also countable; a diagonal sweep of the integer grid proves it.

This lets us understand some familiar mathematical constructions. A polynomial with integer coefficients is determined by a finite list of integers. For each fixed degree there are countably many coefficient lists, and they can be encoded explicitly; therefore there are countably many integer polynomials. Every nonzero polynomial has only finitely many real roots. It follows that the algebraic real numbers are countable, with the usual countable-enumeration argument. Since the real numbers are uncountable, there exist transcendental real numbers. We can prove they exist without exhibiting one particular example.

There is a subtlety here: an existence proof by counting often gives less computational information than a named construction. We know almost every real number in a cardinal sense is not algebraic, but that does not hand us a decimal expansion. Numbers such as e and pi require separate proofs of transcendence.

Cantor's theorem says the power set of the naturals is strictly larger than the naturals. Its cardinality is often written two to the aleph nought; it agrees with the cardinality of the reals. The continuum hypothesis asks whether there is a cardinal size strictly between the size of the naturals and that of the real numbers. Relative to the usual consistency assumptions, the axioms ZFC neither prove nor refute it. That statement needs a much deeper development than diagonalization alone; it is a claim about the limits of a particular axiom system, not a license to count infinite sets however we please.

## What counting actually proves

When we say the rationals are countable, we have a construction. When we say the reals are not, we have an obstruction that defeats every possible enumeration. When we say two sets injecting into one another have equal size, we have a bijection built from those injections. These are different proof styles: exhibit a map, prohibit a map, or transform given maps into a stronger one.

This vocabulary travels into analysis, topology, theoretical computer science, and formalization. A finite string is countable data even when it describes a complicated proof. The set of all algorithms expressible by finite programs is countable. But the functions from natural numbers to yes-or-no answers form an uncountable collection. Hence not every such function is computable. This is an immediate cardinality argument, though it does not by itself give a concrete noncomputable function.

Infinity is not one undifferentiated size. More importantly, mathematical comparisons of infinity are not analogies about endlessness. They are precise claims about injections, surjections, and bijections, proved with constructions as exact as any finite algorithm. The hotel story offers the first example. The diagonal produces the first impossibility theorem. The injection theorem tells us how to compare sizes without ever finishing a count.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

**Definitions.** \(A\preceq B\) means there is an injection \(A\to B\); \(A\approx B\) means there is a bijection. \(\mathbb N\times\mathbb N\) is countable by the diagonal enumeration sorted by \(m+n\). \(\mathcal P(\mathbb N)\) is uncountable by \(D=\{n:n\notin f(n)\}\).

**Cantor–Schröder–Bernstein construction.** Let \(f:A\hookrightarrow B\), \(g:B\hookrightarrow A\), \(h=g\circ f\). Set \(A_0=A\setminus g[B]\), \(C=\bigcup_{n<\omega}h^n[A_0]\). Define
\[
F(a)=\begin{cases}f(a),&a\in C,\\g^{-1}(a),&a\notin C.\end{cases}
\]
The second case is defined because \(a\notin C\Rightarrow a\in g[B]\). Injectivity on and across cases and surjectivity follow as described in the lecture.

**Decimal diagonal.** Use the canonical expansion without an eventually-all-nines tail. For row \(n\), let \(d_n=1\) if its \(n\)-th digit is not 1, otherwise \(d_n=2\). The real \(0.d_1d_2\dots\) differs from every row. The binary sequence diagonal is often conceptually cleaner.

**Exercises and solutions.** (1) List the first ten positive rationals in any diagonal enumeration, skipping duplicates; explain why every rational eventually appears. *Answer:* any order increasing \(p+q\) and skipping equivalent fractions suffices. (2) Show that the rational interval \((0,1)\) is countably infinite. *Answer:* it is an infinite subset of the countable set of rationals. (3) Why is the set of finite binary strings countable? *Answer:* it is a union over lengths of explicitly finite sets; order first by length, then lexicographically. (4) Can an injection \(\mathbb R\to\mathbb N\) exist? *Answer:* no, since it would make \(\mathbb R\) at most countable.

### Sources and reading

- Open Logic Project, *Set Theory*: https://builds.openlogicproject.org/content/set-theory/set-theory.pdf
- Stanford Encyclopedia of Philosophy, *Set Theory*: https://plato.stanford.edu/entries/set-theory/
- Open Logic Project, *Sets, Logic, Computation*: https://slc.openlogicproject.org/

The hotel and diagonal narrations use standard constructions with independently written examples.
