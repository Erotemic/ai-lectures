# Five Ways to Count a Balanced Shape: Catalan Numbers

**Track:** Discrete Mathematics and Combinatorics  
**Lecture:** 050000  
**Preparation:** Finite sets, binomial coefficients, elementary recurrences, and the idea of a bijection.  
**Companion:** Reflection principle, Catalan recurrence, generating function, and explicit correspondences among parenthesis words, ordered trees, and binary trees.

<!-- BEGIN SPOKEN LECTURE -->

A row of six parentheses may look like punctuation rather than mathematics. But there are exactly five ways to arrange three opening and three closing parentheses so that, reading from left to right, no closing parenthesis appears before the opening parenthesis it needs. Five is also the number of ways to fully parenthesize four factors if the order of the factors cannot change. It is the number of shapes of a full, ordered binary tree with three internal nodes. It is the number of ways to divide a convex pentagon into triangles by noncrossing diagonals.

Why should one number turn up in so many different problems? We could learn a separate counting formula for every example. A better answer is to build reversible translations between the objects. Then there is only one counting theorem, seen from several directions. The resulting sequence begins one, one, two, five, fourteen, forty-two. Its entries are the Catalan numbers.

## What balanced really means

Take a string containing exactly three opening parentheses and three closing parentheses. There are twenty possible strings if we choose which three of the six positions are openings. Yet only five are properly balanced. The five are: three openings followed by three closings; two openings, a closing, an opening, then two closings; two openings and two closings followed by an opening and a closing; an opening, a closing, two openings and two closings; and three successive opening-closing pairs.

A balanced word has two properties. First, its total number of openings equals its number of closings. Second, every initial segment has at least as many openings as closings. The second condition distinguishes the legitimate words from strings that try to close a parenthesis that has not yet opened. It is a condition on every prefix, not merely on the total.

Translate the string into a walk along the integers. An opening parenthesis is a step up by one; a closing parenthesis is a step down by one. The walk starts at height zero, never becomes negative, and finishes at height zero. For three pairs, it takes six steps, three up and three down. This is called a Dyck path, though we could just as well draw the same walk in a square lattice by taking steps north and east and insisting that it stay on the permitted side of a diagonal.

Already we have our first bijection. Reading a balanced word gives one such path; reading the steps of the path gives the word back. The prefix condition becomes the geometric requirement never to cross below the axis. The count is the same because the descriptions contain exactly the same information.

The unrestricted strings are easy: among two n positions, choose n to be openings, so there are two n choose n possibilities. The difficult part is excluding those strings that go below zero. This is where the reflection principle becomes useful.

## A reflection that counts the bad paths

Imagine following a bad path from the origin. Because it is bad, there is a first moment when it reaches height negative one. Stop at that first moment. Reflect every step of the path up to and including that moment: turn each up step into a down step and each down step into an up step. Leave the rest of the path untouched.

Before reflection, the stopped prefix contains exactly one more down step than up steps. After reflection, it contains one more up step than down steps. Consequently the entire transformed walk has n plus one up steps and n minus one down steps. It starts at zero and ends at height two.

So we have turned each bad balanced candidate into an unrestricted word with n plus one ups among two n positions. There are two n choose n plus one such words. But to use that number, we must know the translation is reversible; otherwise distinct bad candidates could collapse onto one output.

It is reversible. Any path with n plus one up steps and n minus one down steps ends at height two, so it must have a first moment when it reaches height plus one. Reflect its prefix through that first arrival. The new path has n ups and n downs, finishes at zero, and its reflected prefix reaches negative one. Running the two operations in succession gives back the original word. We have a genuine bijection between bad candidates and unrestricted paths ending at height two.

Therefore the number of good words is two n choose n, minus two n choose n plus one. A familiar binomial identity simplifies this to one over n plus one, times two n choose n. That is the Catalan number C sub n.

For n equal to three, the unrestricted count is twenty. The bad count is fifteen. The good count is five. The formula did not come from observing five examples. It came from pairing every forbidden object with exactly one object in a simpler collection.

The reason this proof is worth learning is the stopping rule. Reflect at the *first* forbidden event. That makes the inverse visible. Reflections of this kind also appear in ballot problems, lattice walks, and probability, where the object to count is often a path that must remain on one side of a boundary.

## Cutting a balanced word at its first return

A different proof gives a recurrence instead of a closed formula. Every nonempty balanced word has a unique shape. It begins with an opening parenthesis. Find the closing parenthesis paired with that very first opening. Everything between them is one balanced word, and everything after that closing parenthesis is another. So the whole word is an opening parenthesis, then a balanced word A, then a closing parenthesis, then a balanced word B.

This decomposition is unique because the matching close is the first return of the height walk to zero. If the original word has n pairs, A uses some number k of pairs, while B uses n minus one minus k. We can choose A in C sub k ways and B in C sub n minus one minus k ways. Sum over all possible k, from zero to n minus one.

Thus C sub n is the sum of C sub k times C sub n minus one minus k. The empty word has C sub zero equal to one. That may sound like a technical convention, but the empty word is a real possibility: A or B may be empty. Without it, the decomposition would not work at the edges of the sum.

The recurrence generates the sequence without any factorials. C sub one is one. C sub two is one plus one, so two. C sub three is two plus one plus two, so five. C sub four is five plus two plus two plus five, so fourteen. The products appear because the left and right pieces are chosen independently. The sum appears because the possible sizes of the left piece are mutually exclusive cases.

Notice something about this proof. It not only counts words; it describes how to construct every word. An algorithm can recursively enumerate them by choosing a size for A, then a word A and a word B. The combinatorial recurrence is also a specification of a generator.

## Binary trees are the same recursive equation

Now consider a rooted, ordered, *full* binary tree. Full means that every internal node has exactly two children. Ordered means that left and right children are distinguished, even if their shapes happen to agree. Count such trees by their number of internal nodes. We regard a single leaf, with no internal nodes, as the empty case.

A nontrivial full binary tree consists of a root together with a left full binary tree and a right full binary tree. If the whole tree has n internal nodes, the subtrees have k and n minus one minus k. That is exactly the decomposition of a balanced parenthesis word.

Here is an explicit reversible translation. Map a leaf to the empty word. Map an internal node to an opening parenthesis, followed by the word for its left subtree, followed by a closing parenthesis, followed by the word for its right subtree. The first-return rule tells us how to undo the translation: the word inside the first matched pair encodes the left subtree, and the remaining suffix encodes the right subtree.

Consequently, full ordered binary trees with n internal nodes are counted by C sub n. This is not a coincidence deduced from seeing the same recurrence twice. We have produced a specific bijection and explained its inverse.

We need to preserve the adjectives. If left and right children are not distinguished, this bijection fails: swapping them may leave the same unordered tree, but generally changes the parenthesis word. If we count all nodes rather than internal nodes, the formula has a different index. A full binary tree with n internal nodes has n plus one leaves and two n plus one total nodes. A statement about “binary trees with n vertices” is therefore incomplete until the conventions are clear.

## The walk of an ordered tree

There is a second tree connection with a different parameter. Consider a rooted tree whose children have a specified order, but whose vertices may have any number of children. A leaf has zero children; another vertex might have three or seven. Count the tree by its edges, not by its vertices.

Imagine walking around the tree in depth-first order. Whenever we traverse an edge away from the root, record an opening parenthesis. Whenever we traverse the same edge back toward the root, record a closing parenthesis. Each edge contributes exactly one of each. At every stage the number of outward traversals cannot be less than the number of returns, since a walk cannot return across an edge that has not been entered. We obtain a balanced word.

Can we recover the tree? Yes. Begin with a root. At each opening parenthesis, create a new child of the current vertex, in the next position of its ordered child list, and move to that child. At each closing parenthesis, return to its parent. Balancedness ensures that we never try to return above the root, and the final count ensures that we end at the root. This inverse construction is deterministic.

So rooted ordered trees with n edges are also counted by C sub n. The walk does not remember labels, and it crucially remembers sibling order through the sequence in which the children were visited. A rooted unordered tree with n edges belongs to a different counting problem.

This tree encoding is useful in algorithms because a parenthesis word can serve as a compact description of hierarchical structure. But an encoding is not automatically a proof that some operation on the words matches a proposed operation on trees. If we later define pruning, contraction, or embedding, we must separately show how that operation behaves under the translation.

## A generating function is a compressed recurrence

Let C of x be the formal power series whose coefficient of x to the n is C sub n. “Formal” means that for our purposes x is a bookkeeping symbol: we can compare coefficients without first asking whether the series converges as a numerical function.

The empty tree contributes one. A nonempty binary tree contributes one factor of x for its root, and then an arbitrary left tree and an arbitrary right tree. Multiplication of generating functions represents the independent choice of those two subtrees. Thus C of x equals one plus x times C of x squared.

This little equation contains the entire Catalan recurrence. The coefficient of x to the n in the square is a sum of products of earlier coefficients; the outer factor of x accounts for the root. If we solve the quadratic equation for C of x, we obtain two algebraic branches. Only one has a formal power series beginning with constant term one, and it is the branch with one minus the square root of one minus four x, divided by two x.

Here we have three explanations of the same sequence: the reflection principle gives a closed formula, recursive decomposition gives a recurrence, and generating functions package that recurrence in an algebraic equation. These are not competing tricks. They illuminate different features of the objects.

## Why this is a foundation rather than a curiosity

A Catalan count often signals a recursively nested structure with an order: parentheses, rooted ordered trees, noncrossing choices, or a first-return decomposition. But the signal is only a clue. Two sets having the same cardinality does not tell us how to translate between them, and a plausible translation may forget ordering or a distinguished root. The intellectual work is to define the map and test whether it is invertible.

This also suggests a way to study a new combinatorial family. Try to identify a smallest piece that splits the object into independent subobjects. Ask whether the split is unique. Decide what quantity the generating function should record. If there is a prefix or barrier condition, look for a reflection at the first violation. And if several descriptions produce the same numbers, try to build a bijection rather than declaring the coincidence explained.

The Catalan numbers are memorable because their formula is compact. Their deeper value is that they teach four distinct habits of proof: translating between objects, reflecting a bad case into a countable one, decomposing at a unique structural boundary, and turning a recursive construction into an exact algebraic identity. These habits reappear in graph theory, algorithms, formal languages, and mathematical formalization long after the numbers one, one, two, five, and fourteen have faded into the background.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

A **Dyck word of semilength** \(n\) has \(n\) opening and \(n\) closing parentheses and every prefix has nonnegative excess of opens over closes.

**Reflection bijection:** Let \(B_n\) be all length-\(2n\) balanced-count (\(n\) opens, \(n\) closes) candidates that visit height \(-1\). Reflect the prefix ending at their first visit to \(-1\). This maps \(B_n\) bijectively to all paths with \(n+1\) upsteps and \(n-1\) downsteps. The inverse reflects through the first visit to height \(+1\). Hence

\[
C_n=\binom{2n}{n}-\binom{2n}{n+1}=\frac{1}{n+1}\binom{2n}{n}.
\]

**First return:** Every nonempty Dyck word is uniquely \( (A)B \), where \(A,B\) are Dyck words. Thus \(C_0=1\) and

\[
C_n=\sum_{k=0}^{n-1} C_k C_{n-1-k}\quad(n\ge 1),\qquad C(x)=1+x C(x)^2.
\]

The unique formal power-series solution with constant term \(1\) is \(C(x)=(1-\sqrt{1-4x})/(2x)\). This is interpreted as a formal series, not an assertion that every value of \(x\) defines a convergent sum.

**Explicit encodings:**

1. Full rooted ordered binary trees with \(n\) internal nodes: leaf \(\mapsto\epsilon\), internal root with left/right subtrees \(L,R\mapsto (\operatorname{enc}(L))\operatorname{enc}(R)\).
2. Rooted ordered (plane) trees with \(n\) edges: record `(` upon descent of an edge in left-to-right depth-first traversal, `)` upon return; the inverse uses a stack and creates an ordered child on each descent.
3. Fully parenthesized products of \(n+1\) distinguishable, ordered factors correspond to full binary trees with \(n\) internal nodes via their expression trees.

**Exercises with solutions**

1. Compute \(C_4\) from the recurrence. *Answer:* \(5+2+2+5=14\).
2. Encode the root with two leaf children as a plane-tree word. *Answer:* `()()`.
3. Decode `(())()` as a plane tree. *Answer:* the root has two children in order; the first has one child, the second is a leaf.
4. Explain why simply dividing the number of ordered binary trees by \(2^n\) cannot count unordered trees. *Answer:* subtree-swap symmetries differ from shape to shape; not every unordered tree has \(2^n\) distinct ordered descriptions.
5. Identify the unique two-piece split of `(()())`. *Answer:* `( ()() )` with \(A=()()\) and \(B=\epsilon\).

**Sources and attribution**

- NIST Digital Library of Mathematical Functions, §26.5, “Lattice Paths: Catalan Numbers”: https://dlmf.nist.gov/26.5
- Alexander Yong, University of Illinois Math 413, Lecture 22 on Catalan numbers: https://ayong.web.illinois.edu/Spring2025Math413/lecture22.html
- Richard P. Stanley, *Catalan Numbers*, Cambridge University Press (book reference and published excerpt). The specific narration, step-by-step bijections, and exercises are original synthesis.
