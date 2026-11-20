# The Small World of D, R, and S: Why the Decomposition Fits in a Table

<!-- BEGIN SPOKEN LECTURE -->

A tree with forty edges has an enormous collection of possible edge contractions. We can contract any subset of its edges, and a single contracted tree may be reachable in several different ways. If an algorithm tried to visit every possible contraction of both input trees, its dynamic program would hardly deserve the name. It would have exchanged the original problem for an exponential search through smaller trees.

Yet Lozano and Valiente's 2004 algorithm for maximum common embedded ordered subtrees is polynomial. The crucial observation is not that there are few contractions. There can be many. It is that the particular recurrence needed to compare two balanced words visits a much smaller family of intermediate words. Section 2 of the paper constructs that family and proves that it is small enough to index.

The authors call the main family the decomposition, written D. Two auxiliary families, R and S, make it possible to count its members. We will derive all three, follow a concrete four-edge word through them, and examine how the counting proof turns depth and number of leaves into an upper bound. At the end we will read what the existing Lean formalization has actually proved, including a correction to a leaf-count equation printed in the paper.

## First, the kind of object being counted

Represent a rooted ordered tree by a sequence of zeros and ones. Each downward traversal of an edge emits zero, and the return emits one. The resulting word is balanced: zeros and ones occur in equal numbers, and no prefix has more ones than zeros. Its size, in the paper's notation, is the number of zero-one pairs. It is the number of tree edges, not the number of characters. A one-vertex tree has the empty balanced word, with zero edges.

Every nonempty balanced word has a unique first-return decomposition. We can say it aloud as zero, x, one, y. The first zero is matched with that first one. The interior x describes the first child's descendants; y describes the remaining siblings of that first child. The two shorter words x and y are themselves balanced. If we contract that first edge, its pair disappears, and the result is x followed by y.

This gives us three ways to take a nonempty word apart. Keep only its interior x. Keep only its tail y. Or contract its first pair and keep the concatenation x y. These are not arbitrary string deletions; every operation preserves balanced structure.

Definition 4 creates D of a word by starting with the word itself, repeatedly applying those three operations, and keeping no other words. The empty word has a decomposition containing just the empty word. For a nonempty word zero-x-one-y, its decomposition consists of that word together with the decompositions of x, y, and x y. The repeated phrase here is important: we are forming a set. If two routes lead to the same word, that word gets one state, not two.

One could implement this recursion literally. But it does not yet show us why the set is small. Even though each step reduces size, three recursive branches can overlap in a complicated way. A naive recurrence for the number of calls could still grow exponentially. The counting proof must exploit that overlap instead of ignoring it.

## R is a chain, not a tree of possibilities

Imagine repeatedly contracting the first edge and doing nothing else. Starting from zero-x-one-y, the next word is x y. Then we contract its first pair, and continue until no pairs remain. R of the original word is the set of words encountered along this single route, including the starting word and the empty word.

It is easy to count R without enumerating it. Each first-edge contraction removes exactly one matched pair. No two stages can produce the same word because every stage has a different number of edges. If the original has n edges, we have the original size n, then n minus one, all the way down to zero. That is exactly n plus one members of R.

This is Fact 2 in the paper. It is an exact cardinality, not merely an upper bound. The Lean formalization names its counterpart `frontContractions_card`.

R is useful because first-edge contraction is the operation the eventual common-word recurrence uses when it skips one tree's first edge. A long chain of skipped first edges does not create a combinatorial explosion. But D also allows us to step into an interior x rather than contract everything before it. The second auxiliary family records that missing possibility.

## S records the heads exposed along that chain

As R walks forward by first-edge contractions, a new first pair becomes exposed at each stage. Take the interior of that current first pair, and look at every word reachable by repeatedly contracting the first pair inside that interior. Collect those words across the R chain. This is S.

Formally, if the word is zero-x-one-y, S is the union of R of x and S of x y. If the word is empty, S contains the empty word. Unlike R, S branches across the different interior words exposed at successive stages. But each individual contribution from an interior x is still a simple contraction chain.

Here is the first real surprise. D is exactly the union of R and S. The paper proves the inclusion from D into that union; the Lean development also proves the reverse inclusion, which gives equality. So every state created by exploring head, tail, and first contraction can be found either on the first-contraction chain itself or by examining a head exposed somewhere along that chain.

This is not obvious from Definition 4. In particular, a state inside the tail y looks as if it might require independently exploring a new tree of possibilities. The inclusion lemmas explain how to account for that state without inventing a third kind of auxiliary family.

## Six states from a four-edge word

Take the eight-character word zero-zero-zero-one-one-one-zero-one. Written compactly it is 00011101. Its first child is a three-edge path, followed by another leaf at the root. The tree has four edges, two leaves, and root-to-leaf vertex depth four.

Its first-return split is zero, 0011, one, 01. The head is 0011, a two-edge path, and the tail is 01, a single edge. Contract the first pair and you get 001101. Continue contracting first pairs and you pass through 0101, then 01, then the empty word.

So R contains five words: 00011101, 001101, 0101, 01, and the empty word. Their edge counts are four, three, two, one, and zero. That is Fact 2 in miniature.

Now examine S. The head exposed at the first stage is 0011. Contracting the first pair within that head gives 01, and another contraction gives the empty word. Other heads exposed along the chain add nothing new. Thus S contains 0011, 01, and the empty word.

The word 0011 is a decomposition state we could not find along the simple R chain. It arose because D lets us descend into the first child's interior. Taking the union of R and S gives six distinct words. R has five, S has three, and their overlap consists of 01 and the empty word. Five plus three minus two is six.

That example does two jobs for us. It demonstrates why S is needed, and it shows why counting set members, rather than recursive visits, is the relevant quantity. The same one-edge word can arise by several paths, but a canonical table index can store it once.

## The chain of inclusions

Let's trace the main combinatorial ideas. Lemma 1 says that if we concatenate balanced words x and y, any decomposition state of y also belongs to the decomposition of x y. The intuitive operation is to work through the balanced first components of x until the remaining suffix is y, then continue there. The proof is an induction on the number of pairs in x.

Lemma 2 is a little more subtle. A decomposition state of x must appear either as a decomposition state of x y or along the simple front-contraction chain R of x. Some states are preserved when a suffix y is attached; the troublesome ones correspond to contracting away the front of x, and those are explicitly charged to R of x.

Lemma 3 applies the preceding two results to a word of the form zero-x-one-y. Its decomposition states are covered by the original word, decompositions of the contracted word x y, and R of x. The full definition had the decompositions of x, y, and x y; the lemmas show that many of those states are already counted by x y. This is the first compression of a recursive tree into a linear chain plus a small residue.

Lemma 4 supplies the more technical bridge. When z is on the front-contraction chain of x, the decomposition states of z followed by a suffix y are covered by three groups: decompositions of y, members of R of x with y appended, and members of S of x. It is a statement about how adding a suffix interacts with contractions. Rather than independently recurse on every concatenation, we can account for the states using previously identified families.

By taking the suffix to be empty, the paper gets Corollary 1: D of x is contained in R of x union S of x. This is the step on which the eventual state bound depends. In Lean, the theorem `states_subset_front_union_head` proves the source inclusion; `states_eq_front_union_head` proves equality after establishing that both auxiliary families are themselves included in D.

Lemma 5 says that S of x y is contained in S of x union S of y. You might initially expect an extra term for states straddling the concatenation boundary. There is none. The front-contraction progression encounters whole balanced components, and the head states obtained while walking through x can be accounted for within x; after x is exhausted, it walks through y. The lemma controls S under concatenation and is the tool that makes the counting induction work.

We now have the mechanism: represent an apparently branching decomposition by a chain R and an auxiliary union of exposed heads S, with a concatenation lemma to bound how large S can become.

## Charging the heads to depth

Let n be the number of edges. Let d be the maximum number of vertices on a root-to-leaf path, so even the single-vertex tree has depth one. The paper's Lemma 6 bounds the cardinality of S by n times d, plus one.

Why does depth enter? At every front-contraction step, we expose an interior x. That interior is one level shallower than the tree currently being considered. S collects contractions of those interiors, but the recurrence for S under concatenation lets us avoid treating all of them as unrelated. Induction on the number of edges bounds the chain of exposed heads by a sum controlled by the possible nesting depth. The depth equation for zero-x-one-y is the maximum of the depth of x plus one and the depth of y.

This is a counting proof, not a new tree algorithm. We are assigning states to structural positions and showing that only a bounded number of depth levels can be charged to each edge. The precise inequality, including its plus one, appears in the companion. The paper and the Lean formalization both prove a depth-sensitive bound for S.

A different structural quantity is the number of leaves. A long, thin path can have very large depth but only one leaf. If we bounded S only by n times depth, a path of n edges would get a quadratic upper bound, despite its very simple structure. The leaf-sensitive estimate improves it to n times the number of leaves, plus one. Combining the two gives n times the smaller of depth and leaves, plus one.

That sounds like a small technical refinement, but it determines the algorithm's headline complexity. Some trees are deep and thin; some are shallow and bushy. The minimum adapts to whichever of those measurements gives the stronger state bound.

## A correction that formalization makes visible

The paper prints a recurrence for a quantity it calls the number of leaves. It assigns one to the empty balanced word, and for zero-x-one-y it adds the values at x and y. If you apply that formula literally to the word 01, it gives two. But the corresponding tree has one edge and exactly one leaf. The printed recurrence is therefore not a correct recurrence for actual tree leaves.

More generally, the literal printed recurrence yields n plus one for every word with n edges. It does not distinguish a path from a star. The authors' intended leaf-sensitive theorem can be rescued, but not by simply renaming this function and pretending it counts leaves.

The proof repository does something more careful. It defines `printedLeafMeasure` and proves what the printed recurrence actually computes. Separately it defines `trueLeafMeasure`, with a case distinction: when the outer pair is the only root child, the leaves are those of its interior; when there is also a nonempty tail, the leaves of the first child and the remaining forest add together. The source then connects `trueLeafMeasure` to the independent ordered-tree `leafCount`.

The corrected leaf estimate is not assumed. It is proved, in `card_true_leaf_bounds`, and transferred from Dyck words to trees in `TreeStateBounds.lean`. So we can retain the claim involving actual leaves without asserting that the printed leaf recurrence was right. This is exactly the kind of distinction a formalization should force into the open.

## Assemble Theorem 1

We are ready to finish the argument. Fact 2 gives exactly n plus one states in R. The depth and corrected actual-leaf bounds give at most n times the minimum of depth and leaves, plus one states in S. D is contained in their union. Moreover, both R and S contain the empty word. That common member can be subtracted once when bounding the union.

The resulting number of decomposition states is at most n times the quantity one plus the minimum of depth and leaves, plus one. That is the paper's Theorem 1, now understood with genuine tree leaves.

For our four-edge example, d is four and the number of leaves is two. The theorem gives an upper bound of thirteen states. We found six. The theorem does not promise tightness for every tree; it promises a bound for every tree. It proves that the possible branching in the recursive definition can be compressed into a polynomial-size universe of states.

The bound is mathematically independent of how we store those words. A set of six states remains a set of six states whether we represent each member by a linked structure, a flat array of characters, or a small integer identifier. But a fast algorithm needs the last step: identifying repeated states and using their identifiers without repeatedly copying whole words. Counting and implementing are different jobs.

## The formalization's named landmarks

The entry point in Lean is `Paper2004/Decomposition.lean`. It defines `states`, `frontContractions`, and `headContractions` as finite sets of `DyckWord`, corresponding to D, R, and S. It proves the recursive equations, the inclusion lemmas, the n-plus-one cardinality of R, and the bounds on S. It also proves that the finite executable `states` function is the least family closed under the three decomposition rules. That last statement prevents a sleight of hand: an implementation cannot claim a small state set by silently leaving out some allowed decomposition.

`TreeStateBounds.lean` then translates word-depth and actual leaves into independently defined tree depth and leaf count. Its `decomposition_card_bound` establishes the form of Theorem 1 for any ordered tree. Its stronger leaf-only estimate is proved as well.

Theorem 1 is now not simply an interesting estimate in a research paper. It is a theorem about a concrete finite state construction, proved from the tree and word definitions rather than introduced as a hypothesis. The recursion comparing two input words can use these state families. The next mathematical question is whether the comparison recurrence really considers every possible maximum common contraction.

That is Lemma 8. We have established that the table need not be enormous. We must now show that filling it with just three alternatives at each pair of states cannot miss the best answer.

<!-- END SPOKEN LECTURE -->

## Non-spoken companion: paper equations

For a nonempty Dyck word `w = 0x1y`, write `c(w)=xy` and let `n=|w|` denote the **number of matched pairs**.

\[
\begin{aligned}
D(\epsilon)&=\{\epsilon\}, & D(0x1y)&=\{0x1y\}\cup D(x)\cup D(y)\cup D(xy),\\
R(\epsilon)&=\{\epsilon\}, & R(0x1y)&=\{0x1y\}\cup R(xy),\\
S(\epsilon)&=\{\epsilon\}, & S(0x1y)&=R(x)\cup S(xy).
\end{aligned}
\]

### Worked set computation

For `w=00011101`, `head(w)=0011`, `tail(w)=01`, and `c(w)=001101`:

| Family | Members | Size |
| --- | --- | ---: |
| `R(w)` | `00011101`, `001101`, `0101`, `01`, `ε` | 5 |
| `S(w)` | `0011`, `01`, `ε` | 3 |
| `D(w)=R(w)∪S(w)` | `00011101`, `001101`, `0101`, `0011`, `01`, `ε` | 6 |

The overlap is `{01, ε}`. The corresponding tree has `n=4` edges, `d=4` vertex depth, and `ℓ=2` actual leaves.

### Source implication chain

- Lemma 1: `D(y) ⊆ D(xy)`.
- Lemma 2: `D(x) ⊆ D(xy) ∪ R(x)`.
- Lemma 3: `D(0x1y) ⊆ {0x1y} ∪ D(xy) ∪ R(x)`.
- Lemma 4: for `z∈R(x)`, `D(zy) ⊆ D(y) ∪ {ry : r∈R(x)} ∪ S(x)`.
- Corollary 1: `D(x) ⊆ R(x)∪S(x)`; the repository proves equality.
- Lemma 5: `S(xy) ⊆ S(x)∪S(y)`.
- Fact 2: `|R(x)|=|x|+1`.
- Lemma 6: `|S(x)|≤|x|d(x)+1`.
- Corrected leaf lemma: `|S(x)|≤|x|ℓ_true(x)+1`.
- Theorem 1, using shared `ε` in `R` and `S`:

\[
|D(x)|\le |x|\bigl(\min(d(x),\ell_{\rm true}(x))+1\bigr)+1.
\]

`d` counts vertices on the longest root-to-leaf path, so `d(ε)=1`. The paper prints `ℓ(ε)=1` and `ℓ(0x1y)=ℓ(x)+ℓ(y)`, which yields `ℓ(x)=|x|+1`, **not** actual leaf count. In particular `ℓ(01)=2`, whereas the one-edge tree has one leaf. The Lean development replaces this with `trueLeafMeasure` and proves the actual-leaf version.

### Lean reading guide

1. `proofs/SubtreeProofs/Paper2004/Decomposition.lean`: `states`, `frontContractions`, `headContractions`; `states_closed` and `states_least`.
2. Same file: `states_suffix`, `states_prefix`, `states_nest_subset`, `states_front_append`, `states_subset_front_union_head`, `headContractions_append`.
3. Same file: `frontContractions_card`, `headContractions_card_depth`, `printedLeafMeasure_eq`, `card_true_leaf_bounds`, `states_card_min_depth_leaf`.
4. `proofs/SubtreeProofs/Paper2004/TreeStateBounds.lean`: `sequenceDepth_encodeDyck`, `trueLeafMeasure_encodeDyck`, `decomposition_card_bound`.

**Primary source:** [Lozano and Valiente (2004), Section 2, Definition 4–Theorem 1](https://www.cs.upc.edu/~antoni/subtree.pdf), especially printed pp. 5–8.

**Broader optional link:** `mathematical-proof:009000` for structural induction and finite-set arguments.
