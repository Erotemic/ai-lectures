# 003000 — Balanced Words and Ordered-Tree Contractions

**Track:** NX Common Subtree Papers & Formalization. **Section:** Lozano–Valiente prerequisites. **Background:** Rooted ordered trees, sequences, structural induction. **Focus:** Dyck encoding, edge-pair deletion, first-return decomposition and the 2004 dynamic-programming state family.

<!-- BEGIN SPOKEN LECTURE -->

# Balanced Words and Ordered-Tree Contractions

Take an ordered tree, remove all the vertex names, and try to write its entire structure as a string of zeros and ones. It is possible to do this without losing which children belong to which parent, how deeply they nest, or which child comes first. The trick is to record the moments when a depth-first walk crosses an edge in each direction.

When the walk goes from a parent to a child, write zero. When it returns from that child to the parent, write one. Every edge contributes one zero and one one. The resulting string is balanced: while reading left to right, we never see more closing ones than opening zeros, and at the end the counts agree.

This encoding is the conceptual entrance to Lozano and Valiente's 2004 paper. The paper studies a common-subtree problem on rooted ordered trees by translating it into a problem about balanced sequences. It is not merely assigning names to vertices. It is using the recursive grammar of balanced words to expose exactly the operations that a dynamic program needs to consider.

## From a tree to a word

Start with a root and no edges, a single vertex. Our walk never crosses an edge, so its word is empty. Add one leaf child. We cross the edge down and return, producing zero-one. Add two leaf children in that order. We explore the first child and return, then the second, producing zero-one-zero-one.

Now give the root only one child, and give that child one child. We descend twice and return twice. The word is zero-zero-one-one. This is a different tree from the two-leaf star, and it has a different balanced word, even though both have two edges.

Finally, give the root one child, which in turn has two leaf children. We first descend to the branching child, explore its two children in order, then return to the root. The word is zero-zero-one-zero-one-one. If we use parentheses rather than digits, the four examples are empty, a single pair, two neighboring pairs, a pair containing another pair, and a pair containing two neighboring pairs. The nested structure is the tree.

Why is the representation unique? Each opening symbol has a matching closing symbol determined by the first point at which the running balance returns to its previous level. For a nonempty word, the first zero matches a particular one. Everything strictly between those two symbols describes the first child's descendants; everything after the matching one describes the remaining children of the current root. That gives a unique recursive decomposition, and therefore a unique ordered tree.

Conversely, every rooted ordered tree can be encoded recursively by writing zero, then the child's word, then one, for each child in order. The two translations are inverses. This is a bijection between finite rooted ordered trees and balanced words, if we understand the empty word as representing the one-vertex tree. When the paper counts the size of a balanced word, it often uses the number of matched pairs, which equals the number of tree edges. That is different from the string's number of symbols, which is twice as large, and from the number of tree vertices, which is one larger than the edge count.

These conventions are easy to mix up. The difference will appear at every base case of a proof and every stated size bound. A single-vertex tree is a legitimate nonempty tree with zero edges. Its balanced word is empty. An algorithm that returns zero retained pairs may represent a common singleton, not necessarily an absent graph. If an API also supports empty forests, that needs a separate representation and a separate statement about what is being counted.

## What a contraction does to the word

In the ordered-tree problem, an edge contraction merges a child into its parent. The child's own children are promoted to the parent's child list, retaining their order and appearing at the position formerly occupied by the contracted child.

In the balanced word, we erase the zero and the one that represent that specific edge. Nothing else moves except that the symbols between them are now adjacent to the surrounding symbols. Erasing a complete matched pair does not make the word unbalanced. All the nested material between the erased symbols survives, so the grandchildren have indeed been promoted.

Take zero-zero-one-one, a two-edge chain. Delete the outermost matched pair. The remaining string is zero-one, a single-edge tree. Delete the inner pair instead. Again we get zero-one. The outcomes coincide as unlabeled structures, but the contractions occurred at different original edges. If we care about original vertex identities, those witnesses should not automatically be conflated.

Take zero-zero-one-zero-one-one, the root with one branching child and two leaf grandchildren. Delete the outermost pair. We get zero-one-zero-one: the branching child is merged with the root, and its two children become the root's two children. Delete the matched pair belonging to one of the leaves instead. We get zero-zero-one-one: a two-edge chain. Both are legal contractions, but they produce different tree shapes.

There is a precise subtlety in the phrase “delete a matched pair.” We mean a pair that is matched in the current balanced word. After a deletion, the surviving pairs still match correctly. The operational containment relation permits any finite sequence of such deletions, including pairs nested deeply inside other pairs. It is not the same as deleting an arbitrary zero and an arbitrary one, and it is not restricted to deleting a first or outermost pair.

## The first-return split

For a nonempty balanced word s, let the first opening zero match some closing one. We can write s in the form: opening symbol, head, closing symbol, tail. The head is the balanced word inside the first matched pair. The tail is the balanced word after that pair. Both are balanced.

In zero-zero-one-zero-one-one, the first zero matches the last one, so the head is zero-one-zero-one and the tail is empty. In zero-one-zero-zero-one-one, the first zero matches the second symbol, so the head is empty and the tail is zero-zero-one-one. The split is unique because the matching closing symbol is the first return to balance zero.

We can interpret that decomposition as a tree operation. The head describes the children of the first child of the current root. The tail describes the remaining children of the current root. If we delete the first outer pair and concatenate head with tail, we have contracted the edge to the first child. If we retain the first pair, then head and tail form independent regions that can be compared with corresponding regions in another ordered tree.

That is the combinatorial basis of the three branches in the paper's dynamic program. Either the first edge of both trees survives and those first edges correspond, or the first edge is contracted in the left tree, or the first edge is contracted in the right tree. In the first branch, we gain one surviving edge and solve head against head and tail against tail. In the other branches, we replace a word by the concatenation of its head and tail, which is exactly what deleting its first pair does.

To prove this recurrence, we need to show any optimal common contraction can be put into one of these cases. If both first edges survive and are paired, their interior pieces must correspond to each other, as must the following tails. If at least one first edge is absent from the matched structure, we can contract an appropriate first edge and continue with a smaller instance. The recurrence also needs the reverse construction: the solutions from each branch must genuinely assemble into valid common contractions.

The final step looks familiar from longest common subsequence, but the splitting is richer. A standard subsequence algorithm can drop one letter. Here the unit being deleted is a matched structural pair, and when it survives it splits the work into both an inside comparison and a following comparison. The algorithm is exploiting a context-free nested structure, not treating the digits as unrelated characters.

## Why the printed containment definition needs attention

The original paper gives a recursive definition of balanced-sequence containment and explains it through the deletion of edge annotations. The explanatory operation permits deleting any pair at any depth. But the least relation generated by the literal printed recursive clauses is too restrictive.

Return to the six-symbol word zero-zero-one-zero-one-one. Delete the matched pair representing the second leaf under the branching child. The result is zero-zero-one-one. It is a valid one-step edge contraction in the tree, and a valid matched-pair deletion in the word.

The literal recursive containment relation printed in Definition 2 cannot derive that result. According to the repository's finite analysis, the printed rules permit the original word, zero-one-zero-one, zero-one, and the empty word. They omit zero-zero-one-one. This is not a conjecture based on a diagram. The supplied Lean development keeps a separate inductive relation for the printed clauses, proves the relation is sound for operational contractions, and proves a counterexample to the converse.

Why preserve the printed relation instead of simply changing it? Because two mathematical claims are being distinguished. One says the paper's exact written clauses generate the intended contraction relation. That claim is false. Another says deleting matched pairs corresponds to ordered-tree edge contraction. That relation is the intended operational semantics, and the repository proves the correspondence. We want the theorem about the algorithm to use the latter while recording the mismatch in the former.

This is an ideal example of a specification audit. A long formal proof based on a silently modified definition could be mathematically valid, but it would conceal which assertion in the source had required correction. Maintaining the separate definitions makes the scope of the theorem legible.

## Which subproblems need to be stored?

A naive recursive solver could repeatedly create balanced words by contracting first pairs, then descend into heads and tails, and recompute identical word pairs many times. The paper instead identifies a finite family of states generated by the decomposition operations and gives structural bounds on its size.

The names D, R and S are useful to recognize when reading Section 2. D is the decomposition family on which the algorithm needs to operate. R records a family generated by contractions at the front, while S records a related family of head contractions. The paper proves that the decomposition family is controlled by those two simpler collections, then establishes counting bounds using the number of edges, depth and leaves.

There is an important difference between stating that the number of *all possible contractions* is small and stating that the number of *decomposition states used by this recurrence* is small. An ordered tree can have many distinct contraction outcomes. The proof does not need to store all of them. It needs a closed family sufficient to cover each recurrence call. That family can be bounded more sharply because its generation rules are restricted.

The published theorem bounds the number of relevant decomposition states by a quantity on the order of edge count times the minimum of depth and leaf count. The formalization contains a stronger explicit bound in terms of actual tree depth and actual leaves. The single-vertex and leaf-count conventions have to be addressed carefully, because the paper uses a printed leaf recurrence that does not coincide with the number of leaves in every tree. This is another reason to connect abstract word measures back to an independent tree definition.

After enumeration, a dynamic program can assign unique identifiers to states and fill a table indexed by a pair of identifiers, one from each input. The paper obtains an expected-time bound under assumptions about dictionary operations. The source repository proves several concrete state and memoization counts, including for an actual reference implementation. But a complete cost theorem for all structural word copying and comparisons remains open. Nothing about the correctness of the recurrence depends on pretending that hashing a long structural word is free.

## Reading the Lean development in layers

The proof repository develops this mathematics in a deliberately separated sequence. First comes a direct inductive definition of ordered trees and edge contractions. Then comes the balanced-word type and the encoding between trees and words. Then comes the equivalence of operational contractions and matched-pair deletions. Then come the decomposition family, its cardinality bounds, and the recurrence's correctness. Later files connect those results to memoized computation, original token positions, and extracted Rust code.

The separation lets us read one theorem at a time. An encoding round-trip theorem tells us every represented tree maps to a word and back correctly. A contraction soundness theorem tells us each tree contraction maps to a valid pair deletion. The converse tells us every word deletion can be realized as a tree contraction. A longest-common optimum theorem builds on both directions. A dynamic-program theorem establishes that its numerical calculation or witness agrees with the independent optimum. A Rust refinement theorem must still address how the actual program stores and returns those values.

This chain is the reason a parenthesis-string problem can support a substantive project in formal verification. The clever part is not merely the encoding. It is the chain of precise correspondences from tree operations to word operations to finite state families to algorithmic choices and back to original tree witnesses.

When you open the 2004 paper, the opening definitions should now feel concrete. You can draw a small ordered tree, write its balanced word, identify the first-return split, delete a matched pair and observe the promoted children. With that small example established, the paper's three-branch recurrence is no longer an unexplained formula. It is an exhaustive argument about what can happen to the first edge of two ordered trees.

<!-- END SPOKEN LECTURE -->

## Non-spoken companion: exact encoding and recurrence

### Grammar and examples

A balanced word `s` over `{0,1}` has every prefix satisfying `#0 ≥ #1` and total `#0 = #1`. A rooted ordered tree with child forest `(T₁,…,Tₖ)` encodes as

\[
E(T) = (0\,E(T_1)\,1) \cdots (0\,E(T_k)\,1).
\]

Here a one-vertex tree encodes as `ε` and semilength `|E(T)|_0` counts **edges**, not vertices.

| Tree | Balanced word | Parentheses |
|---|---|---|
| Singleton | `ε` | empty |
| Root → leaf | `01` | `()` |
| Root → two leaves | `0101` | `()()` |
| Two-edge path | `0011` | `(())` |
| Root → branch → two leaves | `001011` | `(()())` |

### First return

For nonempty `s`, there is a unique decomposition

\[
s = 0 \cdot head(s) \cdot 1 \cdot tail(s),
\]

where `head(s)` and `tail(s)` are balanced. Contracting the first edge corresponds to

\[
contractFirst(s) = head(s)\cdot tail(s).
\]

### Lemma 8 (operational containment)

For nonempty `s,t`, define `L(s,t)` as the maximum number of matched pairs in a balanced word obtainable from each by arbitrary matched-pair deletions:

\[
L(s,t)=\max\left\{\begin{array}{l}
1 + L(head(s), head(t)) + L(tail(s), tail(t)),\\
L(contractFirst(s),t),\\
L(s,contractFirst(t)).
\end{array}\right.
\]

`L(s,ε)=L(ε,t)=0`. In the first branch, retaining the two first matched pairs leaves independent head and tail comparisons. The other branches eliminate a first pair on one side. Both upper-bound and constructive lower-bound directions are needed for correctness.

### Small counterexample to printed Definition 2

- Original: `001011` = `(()())`.
- Delete the matched third pair: `0011` = `(())`.
- Operational relation accepts this one-step contraction.
- Least literal printed relation does not derive it. Its reachable results here are `001011`, `0101`, `01`, `ε`.

See `docs/planning/lozano_valiente_2004_containment_definition_audit.md` and `proofs/SubtreeProofs/Paper2004/PrintedContainmentCounterexample.lean`.

### Source landmarks

- `proofs/SubtreeProofs/Paper2004/OrderedTree.lean`
- `proofs/SubtreeProofs/Paper2004/BalancedSequence.lean`
- `proofs/SubtreeProofs/Paper2004/EncodingEquivalence.lean`
- `proofs/SubtreeProofs/Paper2004/ContractionCompleteness.lean`
- `proofs/SubtreeProofs/Paper2004/Decomposition.lean`
- `proofs/SubtreeProofs/Paper2004/TreeStateBounds.lean`
- `proofs/SubtreeProofs/Paper2004/DynamicProgram.lean`

**Primary source:** [Lozano & Valiente (2004), Sections 2–4](https://www.cs.upc.edu/~antoni/subtree.pdf).

**Optional broader preparation:** `algorithms-computability-complexity:009000` explains stack behavior and nested structure; `algorithms-computability-complexity:011000` develops dynamic programming; `logic-types:004000` covers inductive definitions.
