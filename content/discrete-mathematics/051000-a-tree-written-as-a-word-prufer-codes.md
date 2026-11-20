# A Tree Written as a Word: Prüfer Codes and Cayley's Formula

**Track:** Discrete Mathematics and Combinatorics  
**Lecture:** 051000  
**Preparation:** Labeled finite sets, trees as connected acyclic graphs, degrees and leaves, and bijections.  
**Companion:** Encoding and decoding pseudocode, the degree-sequence enumeration formula, and worked examples.

<!-- BEGIN SPOKEN LECTURE -->

Imagine that a network connects six named locations. Every location can reach every other, but there are no cycles. This is a tree. If we forget the names, we can describe its branching shape. If we keep the names, there are many different trees with the same shape: moving the branching point from location four to location six changes the network, even though its unlabeled drawing may look identical.

Here is a question with an answer that initially seems too simple. For n labeled vertices, how many different undirected trees can we build? There are n choose two possible edges, and a tree must have exactly n minus one edges. But simply choosing n minus one of the possible edges counts disconnected graphs and graphs containing cycles. Filtering those possibilities seems to require a complex calculation.

Instead, the answer is n raised to the power n minus two, for n at least two. This is Cayley's formula. It counts labeled trees, not unlabeled tree shapes, and it says nothing about ordering children. Today our aim is to see why the exponent n minus two is right by constructing a reversible encoding of each tree as a word of length n minus two.

## The first surprise: a tree has a removable label

Every finite tree with at least two vertices has at least two leaves, meaning vertices of degree one. One way to see this is to take a longest simple path. If an endpoint had another neighbor outside the path, we could make a longer path; if it had a neighbor already on the path other than its adjacent path vertex, that would create a cycle. Thus both endpoints have degree one.

This elementary observation lets us dismantle a labeled tree without ambiguity. At each stage, choose the leaf with the smallest label. Record the label of its unique neighbor. Delete the leaf and its incident edge. Continue until only two vertices remain. Do not record the final edge. We began with n vertices and removed n minus two leaves, so the record is a word of exactly n minus two labels, each drawn from the original set.

Let us actually do it. Use vertices one through six. Connect one to four, two to four, three to four, four to five, and five to six. This is a tree: vertex four is the central branching location, while five extends a little chain to six.

At the beginning, the leaves are one, two, three, and six. The smallest leaf is one, whose neighbor is four. Our first recorded symbol is four. Delete one. Now two is the smallest leaf; record another four. Delete two. Next delete three and record four again. We are left with the path four, five, six. Its leaves are four and six. Four has the smaller label, so delete four and record its neighbor five. Two vertices remain, five and six, and we stop.

The resulting word is four, four, four, five. Four symbols for six vertices. We have turned a graph into an ordinary finite sequence. If every possible four-symbol sequence reconstructs one and only one tree, the count follows immediately: each symbol has six choices, independently, hence six to the fourth possibilities, or one thousand two hundred ninety-six.

But recording information is only half of a bijection. Could two different trees produce the same word? Could some words fail to describe a tree? The decoder answers both questions.

## Reconstructing what was removed

Suppose we are handed the word four, four, four, five, together with the original label set one through six. A vertex whose label does not occur in the remaining word should be a leaf of the remaining tree. Among those labels, choose the smallest. Connect it to the first symbol of the word, remove the chosen leaf from the available labels, and remove that first word symbol. Repeat. When only two labels remain, connect them with an edge.

Initially, the labels absent from the word are one, two, three, and six. Choose one and connect it to four. Remove the first four. The remaining word is four, four, five, and the smallest unused label absent from it is two. Connect two to four. Repeat with three. Then the remaining word is just five, and the unused labels are four, five, six. Among those absent from that remaining word, four is smallest, so connect four to five. Finally connect five to six. We have recovered exactly the original tree.

Consider a seemingly problematic input: a word in which the same label occurs at every position. For six labels, take four, four, four, four. The decoder connects each of the other five labels directly to four, producing a star. There is no need to restrict the words to some special subset. Repetition is allowed and carries structural information.

Why can the decoder always find a label that is absent from the remaining suffix? Suppose k labels remain. The word suffix has length k minus two. A list of that length cannot contain all k distinct labels, so at least two labels are absent. The first symbol of the suffix is present, so our chosen absent label cannot be the vertex it is about to connect to. The procedure makes a valid edge between distinct vertices at every step.

The construction cannot create a cycle. Each added edge attaches one label that is immediately retired, and that label receives no more edges except the one just created at that step; we can imagine building the graph backward from the final edge, repeatedly attaching a new leaf. Attaching a leaf preserves connectedness and acyclicity. The final result is a tree on all n labels.

## Why the decoder really is the inverse

A working example is reassuring but not a proof. The decisive invariant is a relationship between the remaining word and the degrees in the remaining tree. At any stage of the encoding, a vertex of degree d appears exactly d minus one times in the *remaining* code produced by the tree. In particular, degree-one vertices are precisely those whose labels do not appear.

We can justify this by induction on the size of the tree. In the two-vertex case the word is empty, and each vertex has degree one, so the claim holds. For a larger tree, the first removed leaf has degree one and its label cannot be a neighbor symbol in the remaining code. Its neighbor loses one degree when the leaf is removed, and the neighbor's label contributes one new symbol to the front of the code. All other vertices retain their degrees and occurrence counts. The invariant is preserved when we add that first deletion back.

Therefore, when decoding an actual Prüfer word, the smallest absent label is exactly the smallest leaf that the encoder would have deleted. Its neighbor is the first symbol of the word. The decoder reconstructs that edge and reduces to the same smaller problem. Induction shows that decoding after encoding returns the original tree. Conversely, encoding a tree produced by decoding returns the original word, since the same leaf choices occur in reverse order.

We now have a bijection between labeled trees on n vertices and words of length n minus two over an alphabet of n labels. Thus there are n to the n minus two trees. The extraordinary-looking formula has a pedestrian explanation once we have found the right representation.

The proof contains a minor boundary case. With two vertices, there is exactly one tree and the corresponding code has length zero. There is one empty word, agreeing with two to the zeroth power. With one vertex, there is also exactly one tree, but the formula n to the n minus two uses a negative exponent and is better treated by a separate convention rather than by the encoding algorithm.

## Degrees are written in the code

The occurrence invariant does more than prove the bijection. If a vertex label appears r times in the full Prüfer word, its degree in the tree is r plus one. For our example, four appears three times, so vertex four has degree four. Five appears once, so its degree is two. Every other label appears zero times, so those vertices are leaves. The code remembers the degree sequence without reconstructing a single edge.

This immediately gives a more refined counting theorem. Fix positive integers d one through d n whose sum is twice n minus two. That sum is necessary by the handshake lemma: the sum of degrees in any tree is twice its n minus one edges. To obtain a tree with these degrees, its Prüfer word must contain label i exactly d i minus one times.

How many such words exist? There are n minus two total positions. We choose which d one minus one positions contain label one, which d two minus one contain label two, and so on. The count is the multinomial coefficient with numerator n minus two factorial and denominator the product of all d i minus one factorials. Each such word corresponds to exactly one tree, so this is also the number of labeled trees having that degree sequence.

For six vertices, suppose one vertex has degree five and every other vertex has degree one. Its code must repeat the central vertex's label four times. There is exactly one such tree for a specified choice of center: the star. But if we merely ask for a star without fixing the center, there are six choices. The degree sequence with named vertices and the unlabeled shape are different questions.

Consider instead a path on six labeled vertices. Its degree sequence has two endpoints of degree one and four internal vertices of degree two. Once we specify exactly which two labels are endpoints, the code contains each of the four internal labels exactly once, in any order. There are four factorial, or twenty-four, possible words. That is a useful cross-check: reverse the orientation of a labeled path and the undirected edge set does not change. With prescribed endpoints, there are four factorial orders of the internal labels.

## A random tree hidden inside a random word

The same bijection gives a clean way to choose a labeled tree uniformly at random. Select n minus two labels independently and uniformly from the n labels, then decode the resulting word. Every word is equally likely, and every tree has exactly one word. Thus every labeled tree is equally likely. No rejection of disconnected graphs is required.

Fix a particular vertex, say vertex one. Its number of appearances in the random word counts how often independent choices produce that label. It has a binomial distribution with n minus two trials and success probability one over n. Its degree is one plus that count. Therefore its expected degree is one plus n minus two divided by n, which simplifies to two minus two divided by n.

That is exactly what symmetry and the handshake lemma predict. Every tree has total degree two n minus two. If labels are exchangeable in a uniform random labeled tree, each of the n vertices has expected degree two n minus two divided by n. The two derivations agree. One uses Prüfer's coding theorem and elementary probability; the other uses degree counting and symmetry. This agreement tests both pictures.

We should be careful about what uniform means. A uniformly random labeled tree is not the same distribution as first choosing an unlabeled tree shape uniformly and then assigning labels. Some shapes have many distinct labelings; some have more automorphisms and therefore fewer distinct labeled realizations. Those weighting differences are central if we use a random-tree model.

## Two very different senses of tree counting

The Catalan numbers count rooted *ordered* trees by their number of edges. Cayley's formula counts undirected *labeled* trees by their number of vertices. The first problem remembers the positions of children and discards labels. The second remembers vertex identities but does not give a left-to-right order to neighbors. It is therefore no paradox that the two answers grow at different rates.

Both proofs use encodings, but their logic is different. In the Catalan encoding, the parenthesis word records a depth-first traversal and must satisfy a balancing restriction. In the Prüfer encoding, an arbitrary word is allowed; the smallest-leaf convention controls how the word is interpreted. The freedom to use every word of the required length makes Cayley's counting formula exceptionally direct.

There are other proofs of Cayley's formula, including determinant-based arguments related to the matrix-tree theorem. Those reveal a connection between counting spanning trees and linear algebra. Prüfer's code gives something different: a concrete conversion both ways, a way to count trees by degree sequence, and a straightforward sampler of uniformly random labeled trees.

The most important question to ask when seeing a purported combinatorial encoding is not whether it compresses an object. It is whether the decoding is well defined and whether both compositions return the starting data. Here the leaf invariant supplies exactly that theorem. An astonishing formula becomes convincing not because the code is clever, but because we can prove it loses no information.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Let \(S=\{1,\ldots,n\}\), \(n\ge 2\). A *labeled tree* is a simple connected acyclic undirected graph whose vertex set is exactly \(S\). Cayley's formula states

\[
|\mathcal T_n|=n^{n-2}.
\]

**Encoding:** Repeat \(n-2\) times: remove the least-labeled leaf \(\ell\), append its unique neighbor to the code. The resulting word belongs to \(S^{n-2}\).

**Decoding:** Given a word \(p=(p_1,\ldots,p_{n-2})\), start with available labels \(S\). For each symbol \(p_i\), choose the smallest available label \(\ell\) absent from the remaining suffix \((p_i,\ldots,p_{n-2})\), add \(\{\ell,p_i\}\), and retire \(\ell\). Join the final two available labels.

**Example:** Edges \(\{1,4\},\{2,4\},\{3,4\},\{4,5\},\{5,6\}\) give code \((4,4,4,5)\). Its degree sequence indexed by labels 1 through 6 is \((1,1,1,4,2,1)\).

**Degree invariant:** For any tree and label \(v\),

\[
\deg_T(v)=1+\#\{i:p_i=v\}.
\]

This implies the degree-constrained count: if all \(d_i\ge 1\), \(\sum_i d_i=2(n-1)\), then

\[
\#\{T:\deg_T(i)=d_i\}=\frac{(n-2)!}{\prod_{i=1}^n(d_i-1)!}.
\]

**Exercises with solutions**

1. Decode \((2,2)\) on labels \(\{1,2,3,4\}\). *Answer:* edges \(\{1,2\},\{2,3\},\{2,4\}\), a star centered at 2.
2. Count labeled trees on four vertices. *Answer:* \(4^{4-2}=16\).
3. How many labeled six-vertex trees have vertex 1 of degree five? *Answer:* one, the star with center 1.
4. What degree does a label occurring twice in a Prüfer word have? *Answer:* three.
5. For a uniformly random labeled tree on n vertices, compute the expected degree of a fixed vertex. *Answer:* \(1+(n-2)/n=2-2/n\).
6. Why does reversing a labeled path not produce a second tree? *Answer:* its edges are undirected and therefore unchanged by reversing the traversal order.

**Sources and attribution**

- Mathematics for Computer Science, MIT 6.042J, Spring 2015, tree counting and Cayley's formula: https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/pages/readings/
- Paul Johnson, “Lecture 8: Prüfer code,” University of Sheffield graph theory notes: https://ptwiddle.github.io/MAS341-Graph-Theory-2017/lecturenotes/lecture8.html
- Jonathan S. Bloom, “Cayley's Formula,” Lafayette College Math 374 notes: https://sites.lafayette.edu/bloomjs/files/2016/03/Cayleys-formula.pdf
- The six-vertex example, probability comparison, and spoken narrative are original worked exposition.
