# Two Bridges from Trees to Words: A Complete Representation Proof

<!-- BEGIN SPOKEN LECTURE -->

Consider a rooted tree whose root has one child, and that child has two leaf children. It has three edges. Now write its shape as six bits: zero, zero, one, zero, one, one. The bits record opening and closing parentheses in the order we encounter the three edges. If we remove the pair belonging to one of the leaf edges, the sequence becomes zero, zero, one, one. That new sequence describes the tree after contracting that leaf edge.

There is an attractive story here: tree edges and pairs of parentheses are interchangeable. But the sentence hides two separate mathematical assertions. First, every rooted ordered tree corresponds to exactly one balanced sequence, and every balanced sequence corresponds to exactly one rooted ordered tree. Second, contracting an edge of a tree corresponds to deleting an enclosing matched pair from the sequence, at any depth. The first assertion is about representation. The second is about operations. A proof of the first does not automatically establish the second.

The Lozano–Valiente formalization in our repository proves both, in separate modules, and it also preserves the distinction between these operational facts and the recursive containment wording printed in the 2004 paper. We are going to read those proofs as a connected mathematical argument. The reward is a method you can use on other verification projects: prove that an encoding is reversible; prove that operations are preserved; prove the converse so the encoding does not admit spurious operations; then add the identity information needed to reconstruct an answer in the original input.

## The tree has an implicit root

The mathematical tree type in OrderedTree.lean is pleasantly small. A tree is a node containing an ordered list of child trees. The tree with no children is a singleton vertex. The tree with one singleton child has one edge. The fork with two singleton children has two edges.

We use one matched parenthesis pair for each edge, not each vertex. The distinguished root is implicit in the encoding. Thus the singleton is represented by the empty balanced word. The one-edge tree is represented by a single matching pair, written zero one. The fork with two leaf children is zero one, zero one. And the path of two edges is zero zero one one. This convention is easy to confuse with balanced-parenthesis encodings that surround every vertex. Those encodings are valid in other contexts, but they are not the one used here. An exact correspondence theorem must name the particular encoding, including this off-by-one choice.

The recursive rule is simple. To encode a tree, encode its ordered forest of children. For each child, place an opening parenthesis, then the encoding of the child's own children, then a closing parenthesis; append the encodings of the next siblings in order. In the Boolean representation used later by the Rust interface, opening is false, which we will call zero, and closing is true, which we will call one.

For the example in the opening, the root has one child whose children form a fork. The fork forest is zero one, zero one. Surround it with the pair for the root's only edge and we obtain zero, zero, one, zero, one, one. Each pair is still associated with one actual edge. The outer pair is the edge from root to internal child; the inner two pairs are the edges to the leaves.

An arbitrary string of zeros and ones would not represent a tree. At every prefix, the number of closing ones must be no greater than the number of opening zeros, and the totals must balance at the end. A balanced word is therefore a structured mathematical value, not just an unvalidated string. The proof uses Mathlib's Dyck-word type to preserve that invariant.

## Why a binary tree appears in the middle

You might expect the decoder simply to count parentheses with a stack. That is one possible executable parser. The formalization chooses another route for its mathematical equivalence. It passes through a first-child, next-sibling binary tree.

In this representation, a binary node holds the first member of an ordered child forest. Its left branch encodes that child's own children, and its right branch encodes the rest of the siblings. An empty forest becomes the empty binary tree. The original tree's distinguished root contributes no binary node. One binary node corresponds to one edge of the original ordered tree.

This gives a clean reversible transformation between ordered trees and binary trees carrying trivial unit labels. One function converts an ordered tree to its child-forest binary tree. Another recovers the ordered child list from a binary tree and attaches an implicit root.

What would we need to prove for these functions to be inverses? Two equations. Start with an ordered tree, convert it to binary form, then decode it. The result must be the original ordered tree. Start with a binary tree, decode it as an ordered tree, then re-encode it. The result must be the original binary tree. Both directions are necessary if we want all ordered trees and all binary trees to correspond without information loss or unwanted extra representations.

The Lean source proves both directions. One direction requires mutual induction over trees and forests, because a child's structure and the list of following siblings call back into one another. That is a representative formalization issue. Mathematically, you might describe the recursion in one sentence. In the proof assistant, the mutually recursive structure becomes explicit, and so does the induction principle that justifies it.

Mathlib already supplies a corresponding bijection between its binary trees and Dyck words. The project proves that its own recursive ordered-tree encoding agrees with the Mathlib binary-tree encoding. It then composes the two reversible transformations. The result is a decoder from Dyck words to ordered trees, together with both round-trip equations.

The first equation says: decode the encoding of an ordered tree, and recover that tree. The second says: encode the decoding of a Dyck word, and recover that word. The source gives these names as decodeDyck_encodeDyck and encodeDyck_decodeDyck. It packages them in an equivalence called orderedTreeEquivDyck.

An equivalence is stronger than a function being convenient. It proves the representation neither merges distinct trees nor invents extra legal balanced words with no tree interpretation. Injectivity follows immediately: if two trees have the same encoding, decode that common word, and the round-trip theorem says the two original trees were equal.

We have now proved that we can exchange representations without changing tree shapes. We have not yet proved that deleting arbitrary pairs models edge contraction. That is the second bridge.

## What an edge contraction actually does

Consider a tree with children in a definite order. Select one child of a parent. Contract the edge from the parent to that child. The child vertex disappears as a separate vertex, and its own ordered children are spliced into the parent's child list at precisely the position formerly occupied by the child. Children before it stay before it; children after it stay after it. The root of the entire tree remains distinguished.

If the selected child was a leaf, the contraction simply removes it. If the child had two children, the contraction promotes both of them into the parent's ordered list. That second case shows why contraction is more subtle than deleting a leaf or selecting a connected induced subtree. Edge contraction may change which vertices are adjacent while preserving the underlying ordered structure.

The Lean definition ContractStep records a witness for one operation. It specifies the ancestor context around the location of the contraction, the sibling trees before and after the selected child, and the child tree whose incoming edge is removed. The before tree is the context with the original child inserted. The after tree is the same context with that child's own children spliced into the same position.

The context is important because a contraction can happen far below the overall root. A rule that handles only root-adjacent edges would be incomplete. A context provides a precise way to say: keep all the surrounding tree unchanged while modifying one selected position. The source has a theorem that a contraction at the root is a valid step, and another theorem that lifts a contraction through a surrounding child context.

The relation Embeds is then the reflexive, transitive closure of ContractStep, oriented so that the smaller tree is obtainable from the larger one by zero or more contractions. Zero steps allow equality. Several steps allow a sequence of contractions at different depths.

It is worth noticing the direction of the arguments. In ordinary speech, we say the small tree embeds in the large tree. But an elementary contraction step runs from the large tree to the small tree. The Lean definition writes a closure of the forward contraction relation, then supplies large before small. Reversing those arguments by accident can turn a true theorem into a false one.

## One pair deletion is one contraction

Now turn to the Dyck-word operation. One balanced pair encloses an interior balanced word. Removing the pair leaves its interior in place. If the word is the encoding of a parent and one of its children, this is exactly the promotion of the child's children into the parent's child list. The surrounding siblings remain in their original order.

The source calls a one-step word deletion DyckContractStep. Its witness consists of a Dyck context and an interior balanced word. Before deletion, the context contains the interior wrapped in a pair. After deletion, the context contains just the interior. The context can place the pair among siblings or inside another enclosing pair, so this is not restricted to deletions visible at top level.

There is a crucial safety condition: the context is itself built from balanced pieces and nesting. We are not allowed to choose two arbitrary bits that happen to be zero and one. They must form an actual matched pair in the structured Dyck word. Without that condition, one could transform a balanced word by operations that do not correspond to any edge contraction.

The lemma contractStep_encodeDyck is the first operation bridge. Given a real ContractStep on ordered trees, it proves that encoding the before and after trees yields a DyckContractStep. The proof uses a tree-context-to-Dyck-context translation, together with the equations for how root contraction changes the local forest encoding. It shows that each actual tree edge contraction has a legitimate corresponding pair deletion.

From this one-step lemma the source derives embeds_encodeDyck: every finite sequence of tree contractions maps to a finite sequence of matching-pair deletions. The induction is over the reflexive/transitive closure of the contraction relation. In the zero-step case the word is unchanged. In a nonzero case, append the encoded one-step contraction to the encoded sequence already established.

This is soundness of the encoding with respect to contraction. But soundness alone is not enough for using a word algorithm as a tree algorithm. What if the word algorithm found a legal sequence that had no interpretation as a tree contraction? The forward theorem cannot exclude that possibility.

## The converse is a theorem of its own

The reverse direction lives in ContractionCompleteness.lean. Rather than assume that every Dyck pair deletion somehow corresponds to a tree contraction, the source proves it. The proof works through decoded ordered forests, because a Dyck context can describe sibling concatenation as well as nesting.

Start with the simplest context: a hole. Removing one enclosing pair changes a singleton child tree into the list of its children. That is one forest splice. Now suppose the pair is surrounded by sibling words on the left and right. Decoding concatenation makes those words ordinary adjacent lists of ordered trees. The same forest contraction can be lifted while retaining the siblings. Finally, suppose the pair is nested inside another pair. Decoding the outer pair creates a parent tree, and the contraction is lifted beneath that parent. The proof proceeds by induction on the structure of the Dyck context.

The result is named dyckContext_decodeForest_contract. It builds a genuine forest contraction from a balanced-word deletion in any context. The theorem dyckContractStep_decodeDyck then wraps this as an ordinary single edge contraction of decoded rooted trees. And dyckEmbeds_decodeDyck extends the result to any finite sequence of deletions.

At last, the theorem embeds_iff_dyckEmbeds combines the two directions. The left-to-right implication is the soundness theorem from the previous module. For the right-to-left implication, decode the alleged word-deletion sequence into a tree-contraction sequence. Then simplify both decoded encoded endpoints using the round-trip equations. We have proved that the original smaller tree is obtainable from the original larger tree by contractions.

The equivalence really is biconditional. There is no gap left in this semantic representation bridge. And its proof is modular: reversible encoding, one-step soundness, one-step completeness, then closure over sequences. If you encounter another encoding problem, this is a strong design to imitate.

## Watch the example change under contraction

Return to the six-bit example: zero, zero, one, zero, one, one. The outer pair surrounds the fork inside the internal child. The two inner pairs each represent a leaf edge. Delete the second inner pair. The result is zero, zero, one, one. In tree language, contract the edge from the internal child to its second leaf. The internal child now has one leaf child, so we have a two-edge path.

Notice that removing the outer pair does something different. It promotes both leaves to be children of the original root. The resulting balanced word is zero, one, zero, one: a fork with two edges. Both are valid single-edge contractions of the same original tree, but they produce different shapes. A formal relation has to permit both. It cannot encode contraction merely as deleting the first enclosing pair, or as deleting a pair at the top level.

This example also exposes a discrepancy documented in the uploaded repository. The paper's printed Definition 2, interpreted as the least relation generated by its two stated clauses, is not equivalent to operational deletion in arbitrary balanced contexts. The Lean module PaperContainment.lean defines that printed relation separately. A further theorem proves that the six-bit tree can contract to the four-bit path operationally, but this one-pair reduction is not admitted by the literal printed relation.

That is not a failure of the operational equivalence theorem. It is evidence that the formalization has carefully separated two candidate specifications. The completeness theorem proves that edge contraction matches arbitrary matched-pair deletion. It does not falsely proclaim that every printed recursive rule is equivalent to that operational definition. This is exactly why proof assistants are valuable in research: two descriptions that sound interchangeable in prose can have different mathematical consequences.

## A final bridge: preserving identity, not only shape

Even with a perfect tree-to-word equivalence, a program returning a four-bit word has not yet told us which original edges survived. If the input had repeated labels, two visually identical branches might correspond to different input edges. An output shaped like a path does not identify which of two possible contractions was chosen.

The next layer in the project annotates matched pairs with original identities and token positions. A pair in the original six-token word occupies an opening and closing position. Using zero-based indexing, the outer pair occupies positions zero and five; the first inner leaf pair occupies one and two; the second occupies three and four. If we delete the second leaf pair, the remaining word is four tokens long, but its retained original positions are zero, one, two, and five. We must not pretend the closing token formerly at position five was originally at position three merely because it now appears at the end of a shortened word.

The TokenEncoding module defines original pair positions using the independent binary shape and a starting offset. It proves that the coordinates lie in the actual original encoded range and that exactly one record is generated for each pair. The indexed-word modules prove that retained pair identities are ordered sublists of the original identities. The token-reading modules connect those identities to the Boolean input. These are additional representation results. They strengthen a shape-level theorem into the kind of provenance information an implementation needs when it returns original graph nodes.

Still another theorem would be needed to connect every operation of a particular compiled Rust or Python program to these mathematical objects. The existence of a correct encoding and a correct contraction relation does not certify a particular parser, allocator, index mapping, or foreign-function boundary. Each bridge has its own input and output contracts.

## How to reuse the proof pattern

When reading another formalization, separate four questions. Can every source object be encoded, and can every encoded object be decoded without loss? Does every source operation map to a target operation? Does every target operation map back to a source operation? And do the output values carry enough original identity to satisfy the user-facing contract?

The exact proof techniques may differ. Here we needed structural induction over trees and forests, contextual reasoning about one local rewrite, and induction over a finite sequence of rewrites. In another project, we might need equivalence of graph representations, preservation of a transition relation, and a refinement of stored indices. But the direction of the argument is the same.

The key is not to use the word equivalent too early. An encoder with an inverse is equivalent as a representation. A one-way simulation is sufficient for some soundness claims but not for a complete search procedure. A two-way simulation can establish that an abstract algorithm searches exactly the intended objects. A provenance theorem then ensures that the answer refers to the original input rather than to a reconstructed shadow of it.

That gives us a practical foundation for the harder formalization proofs ahead. When a dynamic program says that a table entry is the optimum of some family of witnesses, we can ask which representation those witnesses live in, how the algorithm transforms them, and whether both inequalities of the recurrence have constructive witness translations. We now have a concrete example where Lean proves those translations, and a concrete counterexample showing why the definitions must be chosen with care.

<!-- END SPOKEN LECTURE -->

## Companion: the two equivalences in actual Lean

**Pinned project:** `networkx_algo_common_subtree`, source snapshot uploaded 2026-11-19. These names and theorem statements are inspected from the supplied `proofs/SubtreeProofs/Paper2004/` modules.

### Representation equivalence (`EncodingEquivalence.lean`)

```lean
def decodeDyck (word : DyckWord) : OrderedTree :=
  fromBinaryTree word.toTree

@[simp] theorem decodeDyck_encodeDyck (tree : OrderedTree) :
    decodeDyck (encodeDyck tree) = tree := by
  ...

@[simp] theorem encodeDyck_decodeDyck (word : DyckWord) :
    encodeDyck (decodeDyck word) = word := by
  ...

def orderedTreeEquivDyck : OrderedTree ≃ DyckWord where
  toFun := encodeDyck
  invFun := decodeDyck
  left_inv := decodeDyck_encodeDyck
  right_inv := encodeDyck_decodeDyck
```

The source uses first-child/next-sibling binary forests (`toBinaryForest`, `fromBinaryForest`) to establish the two inverse equations, then Mathlib's `DyckWord.ofTree`/`toTree` inverse laws. This proves a bijection of **shapes**, not yet a correspondence of contractions.

### Semantic relation and one-step bridge (`OrderedTree.lean`, `ContractionSoundness.lean`)

```lean
def Embeds (small large : OrderedTree) : Prop :=
  Relation.ReflTransGen ContractStep large small

def DyckContractStep (before after : DyckWord) : Prop :=
  ∃ (ctx : DyckContext) (interior : DyckWord),
    before = ctx.plug (interior.nest) ∧ after = ctx.plug interior

def DyckEmbeds (small large : DyckWord) : Prop :=
  Relation.ReflTransGen DyckContractStep large small
```

`ContractStep` itself is defined using a tree context `ctx` and left, right, and child witnesses. `contractStep_encodeDyck` proves one-step soundness. `embeds_encodeDyck` extends it to a closure of steps.

### Converse and final equivalence (`ContractionCompleteness.lean`)

```lean
theorem dyckContractStep_decodeDyck {before after : DyckWord}
    (step : DyckContractStep before after) :
    ContractStep (decodeDyck before) (decodeDyck after) := by
  ...

theorem dyckEmbeds_decodeDyck {small large : DyckWord}
    (h : DyckEmbeds small large) :
    Embeds (decodeDyck small) (decodeDyck large) := by
  ...

theorem embeds_iff_dyckEmbeds {small large : OrderedTree} :
    Embeds small large ↔
      DyckEmbeds (encodeDyck small) (encodeDyck large) := by
  constructor
  · exact embeds_encodeDyck
  · intro h
    have decoded := dyckEmbeds_decodeDyck h
    simpa only [decodeDyck_encodeDyck] using decoded
```

In the source, the converse is built from `dyckContext_decodeForest_contract`, an induction over three `DyckContext` constructors: hole, siblings, and nested.

### Distinguish the printed relation

`PaperContainment.lean` defines `PrintedContains` as the least inductive relation generated by reflexivity and the printed recursive `remove` clause. `PrintedContainmentCounterexample.lean` proves `branching_example_not_printed`. The operationally valid `001011 → 0011` contraction is not a `PrintedContains` step in that least-relation interpretation. The operational biconditional above must **not** be restated as a biconditional about `PrintedContains`.

### Concrete words and original coordinates

| Shape | Boolean/Dyck word | Number of edges |
| --- | --- | ---: |
| Implicit root only | empty | 0 |
| One root-to-leaf edge | `01` | 1 |
| Root with two leaf children | `0101` | 2 |
| Two-edge chain | `0011` | 2 |
| Root → child with two leaf children | `001011` | 3 |

The last word has original matched pairs at `(0,5)`, `(1,2)`, and `(3,4)`. Deleting `(3,4)` yields `0011`, while retaining original token coordinates `(0,1,2,5)`. `TokenEncoding.positionPairs_bounds` and `positionPairs_toTree_length` establish bounds and cardinality; `IndexedWord.Retains.tokenIndices_sublist` and `TokenReading.retained_readsTokens` contribute identity/reading guarantees.

### Self-checks

1. Why does `orderedTreeEquivDyck` not itself imply `embeds_iff_dyckEmbeds`?
2. For `001011`, what contraction produces `0101`, and what contraction produces `0011`?
3. Which theorem prevents a balanced-word deletion from describing a fictitious tree operation? Which theorem proves that a genuine contraction is not lost in the encoding?
4. Why would a parser that returns the correct shortened word still need an original-position theorem to return original input nodes?

**Background cross-links:** `003000` (balanced words), `008000` (printed containment counterexample), `009000` (indexed witnesses), `logic-types:004000`–`006000` (induction and equality). The mathematical paper is [Lozano and Valiente (2004)](https://www.cs.upc.edu/~antoni/subtree.pdf). No new proof or source-code change is claimed by this lecture.
