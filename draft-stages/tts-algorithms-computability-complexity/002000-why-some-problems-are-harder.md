# Why Some Problems Are Harder Than Others

**Track:** Algorithms, Computability, and Complexity  
**Lecture:** 002000 — Complexity Foundations  
**Assumed background:** Basic logarithms, sequences, elementary multiplication, and the distinction between a problem and an algorithm.  
**Companion:** Comparison lower bound, recurrences, bit complexity, and source-to-claim map below.

<!-- BEGIN SPOKEN LECTURE -->

Suppose you need to locate a word in a dictionary. If the words are arranged alphabetically, you can open near the middle, compare the word you find with the one you want, and discard half the remaining pages. If the words are in an arbitrary order, that strategy fails. You might need to inspect nearly every entry. Two objects that both look like dictionaries pose different computational problems because one comes with a structural promise and the other does not.

That observation is the start of complexity theory. Speed is not just an attribute of clever code. It depends on what the input promises, what operations the algorithm is allowed to perform, what counts as an operation, and how we measure the size of an input.

Imagine an array containing one million sorted, distinct numbers. To determine whether a number appears in that array, a binary search can compare it with the middle entry. Each answer restricts the remaining candidate interval. After one comparison, roughly half remains; after two, roughly one quarter; after twenty, roughly one millionth. The decisive relationship is that two raised to the twentieth power is a little more than one million. The number of comparisons grows logarithmically with the number of entries.

But the phrase 'binary search is logarithmic' has assumptions hidden inside it. The data must be sorted according to the same ordering used by the search. We must be able to reach the middle entry without walking through all the earlier entries. An array can often provide such access in constant time under a suitable random-access machine model. A singly linked list, by contrast, may require a linear walk to reach a chosen middle node. Identical high-level search logic does not imply identical access cost.

Now compare binary search with a scan of an unsorted list. A scan examines successive entries until it finds a match or runs out. In the worst case, it may make as many comparisons as there are entries. Does that mean a scan is poorly designed? Not necessarily. If there is no useful order and comparisons are all we have, finding a particular element may require inspecting the whole list. We cannot judge an algorithm without understanding which information the input contains.

The central mathematical maneuver is to replace a stopwatch reading with a function of input size. If an input has n items, we might count comparisons, additions, memory accesses, or the number of elementary bit operations. We use expressions such as n, n squared, n times the logarithm of n, or two raised to n. These expressions are not timing predictions on their own. They describe how a chosen resource bound behaves as the input grows.

Big O notation expresses an asymptotic upper bound. To say that a function is big O of n squared means that, beyond some sufficiently large input size, it is no greater than a fixed constant times n squared. Big Omega expresses a lower bound. Big Theta means upper and lower bounds match up to constant factors for sufficiently large inputs. The constants matter in practical engineering even when the notation suppresses them. An algorithm with a better growth rate can still lose on small instances because of allocation, cache misses, instruction overhead, or a large constant.

Here is a simple experiment in thought. One procedure performs ten thousand times n elementary operations. Another performs n squared operations. At n equal to a hundred, the first uses one million and the second uses ten thousand: the quadratic procedure wins under that simplified model. At n equal to a million, the first uses ten billion and the second uses a trillion: the linear-growth procedure wins. An asymptotic statement is a long-run comparison, not a claim about every input size or every processor.

There is another distinction. A *worst-case* bound covers every input of the stated size. An *average-case* bound needs a probability distribution over inputs. An *expected* bound may instead involve randomness chosen by the algorithm. These are different sources of probability and should not be confused. If someone promises an 'average constant-time lookup,' ask: average under what distribution, and which adversarial inputs might invalidate it? An amortized bound is different again: it distributes expensive operations across a sequence of updates without necessarily invoking probability at all.

Let's study sorting. You are given n distinct items, and your task is to arrange them in increasing order. One possible algorithm repeatedly inserts the next item into its correct position among those already processed. If the input is already sorted, it can be quick; if the input is reversed, it may move many items over and over, requiring work proportional to n squared. Another algorithm, merge sort, splits the input into two smaller parts, sorts each part, and merges the two sorted results. When the input length is doubled, the number of divide-and-merge levels increases by roughly one. Across each level we process a linear number of elements. So the total work grows on the order of n times logarithm of n, assuming constant-cost comparisons and ordinary linear merging.

There is a satisfying recurrence underneath this description. Let T of n denote the running time for n items. For a power-of-two length, merge sort recursively solves two half-size problems and performs a merge costing time proportional to n. Thus T of n is twice T of n over two, plus a linear term. At the top level the merge costs about n. The next level contains two merges, each costing about n over two, so their total is again about n. The next level again costs about n. There are logarithmically many levels. Multiplying the number of levels by the cost per level explains the result. This is not a memorized magic formula; it is an accounting of the work actually done.

Could a much cleverer comparison-based sorting algorithm improve all the way to linear worst-case time? Surprisingly, no. Here we can prove a limitation that applies not merely to one program, but to an entire model of algorithms.

Suppose the items are all distinct and the sorting method learns their order solely by comparing pairs. Every comparison has two relevant outcomes: one item is smaller, or the other is smaller. Think of the algorithm as following a path through a decision tree. At each comparison, an answer sends it left or right. Each possible ordering of the original input items must reach a leaf that distinguishes the correct ordering. There are n factorial possible input permutations. A binary tree of depth d has at most two raised to d leaves. Therefore, to distinguish all n factorial cases, the tree must have depth at least the base-two logarithm of n factorial. For large n, that grows on the order of n times logarithm of n.

For eight distinct items, there are forty thousand three hundred twenty permutations. Fifteen comparisons can produce at most thirty-two thousand seven hundred sixty-eight binary outcome sequences. That is not enough to distinguish every permutation; at least sixteen comparisons are needed in the worst case. This is a lower bound for the whole comparison model, not a complaint about the implementation of merge sort.

Now the model matters more than ever. Counting sort can arrange integer keys from a sufficiently small known range using counts rather than only comparisons. Its standard cost is proportional to n plus the size of the key range, subject to representation and memory assumptions. That does not contradict the comparison lower bound. It changes which operations are available and brings additional information about the keys into the problem. A theorem about one model cannot be silently promoted to a theorem about every model.

This is one of the deepest habits in algorithms research: upper bounds and lower bounds answer different questions. An upper bound says, 'Here is a particular method; I can prove it uses no more than this much work.' A lower bound says, 'Every method in a specified class must sometimes do at least this much work.' When the bounds match, we learn that improving the algorithm's growth rate requires changing the model, changing the problem, or exploiting additional assumptions. We have learned something about the task, not merely about the code.

So far, n has meant the number of elements. But suppose the input is a single whole number N. Is its size N? Usually not. Written in binary, a positive number near one billion requires about thirty bits, not one billion bits. Input length is the length of an encoding, not necessarily the numerical magnitude of the value represented.

Consider a procedure that repeats an operation N times. If N is given in binary, then N can be roughly two raised to the length of its input. Consequently an algorithm that is 'linear in N' can be exponential in the number of bits used to specify N. This is the distinction behind *pseudopolynomial* algorithms: a running time that is polynomial in numerical values, perhaps as well as instance dimensions, need not be polynomial in the encoded input length. The distinction becomes especially important in dynamic programming for optimization problems with numeric capacities and targets.

A related danger appears when we call arithmetic operations constant time. Adding two ten-bit integers and adding two ten-million-bit integers are mathematically both one addition. Physically they involve different amounts of information. In a bit-operation cost model, the costs grow with operand size. In a word-RAM model, operations on fixed-size machine words may be counted as constant time, but the word-size assumption must be stated. There is no contradiction between the resulting theorems; they answer different questions.

Let us return to the dictionary. If the word sought is absent, the sorted array with random access still supports logarithmic comparison count. The unsorted list might need to be read from beginning to end. But suppose the words are very long strings. Comparing two words can take time proportional to the length of their common prefix. A bound on the *number of comparisons* may understate the number of character inspections. What appears to be an efficient algorithm at one level of abstraction may need a more careful cost analysis at the next.

What, then, do people mean by a problem being computationally hard? Sometimes they mean there is a lower bound in a specified model, like comparison sorting. Sometimes they mean that no efficient method is presently known despite decades of effort. Those statements are not equivalent. In the theory of complexity classes, one eventually studies reductions that show how the ability to solve one problem efficiently would allow us to solve many others efficiently. The most famous open question asks whether the classes P and NP are equal. The existence of an efficient algorithm for every problem in NP is not known, and neither is a general proof that none exists. It would be false to claim that NP-complete problems have already been proved to require exponential time.

Nor should we equate 'polynomial' with 'fast enough.' A bound of n to the fiftieth power is polynomial but can be useless. A carefully bounded exponential algorithm may solve small, constrained real problems quickly. Complexity is a language for guarantees and limitations, not a replacement for implementation measurements. Practical engineering adds distributional assumptions, memory hierarchy, parallelism, numerical precision, and input scale.

A useful practice is to separate four levels of an efficiency claim. First: name the input size, including how numerical values are encoded. Second: name the allowed operations and their costs. Third: prove an upper bound for the algorithm, or a lower bound for the problem under the model. Fourth: measure actual performance on representative instances, without pretending those measurements prove the asymptotic theorem. If one of those levels changes, the conclusion may change with it.

The bigger insight is that computational difficulty is not a mysterious aura attached to a problem. It is a carefully stated relationship among information, constraints, models, and resources. Some problems are easy because their inputs carry exploitable structure. Some are hard because even the most economical allowed computation must distinguish an enormous number of possibilities. And some remain open because we do not know whether an ingenious method exists. Learning to tell these situations apart is how we avoid confusing a slow implementation with a difficult problem, or a fast demonstration with a general solution.

<!-- END SPOKEN LECTURE -->

## Mathematical companion — not narrated

### Asymptotic definitions

For eventually nonnegative functions `f, g`, with `g(n)>0` eventually:

- `f(n)=O(g(n))` if there exist `c>0, n₀` such that `f(n)≤c g(n)` for every `n≥n₀`.
- `f(n)=Ω(g(n))` if `g(n)=O(f(n))`.
- `f(n)=Θ(g(n))` if both bounds hold.

These describe a function (cost), and require a specified size parameter and resource model.

### Mergesort recurrence

For `n=2^k`, `T(n)=2T(n/2)+cn`, `T(1)=d`. Expanding by levels gives

\[
T(n)=dn+cn\log_2 n=\Theta(n\log n),
\]

for fixed `c,d>0`. Arbitrary `n` follows by floor/ceiling accounting or comparison with powers of two. This is an operation-count argument, not a cache or allocation benchmark.

### Decision-tree lower bound

For a deterministic comparison-only sort of `n` *distinct* elements, there are `n!` relative orderings. A worst-case decision tree of depth `d` has at most `2^d` leaves, so

\[
d\ge \lceil\log_2(n!)\rceil=\Omega(n\log n).
\]

For `n≥2`, sum `log₂ i` for `i` from `ceil(n/2)` to `n`, obtaining `log₂(n!) ≥ (n/2) log₂(n/2)` up to floors. The upper bound follows from `n! ≤ n^n`. This bound does **not** apply to algorithms permitted to inspect bounded integer keys, to randomized algorithms with unstated success requirements, or to unconstrained computational models without further argument.

### Bit length example

If `N≥1` is written in ordinary binary without padding, its representation length is `L=floor(log₂ N)+1`. A loop of exactly `N` iterations is `Θ(N)` in iteration count but can be `Θ(2^L)` on L-bit inputs near the upper end of the range.

### Evidence map

- **Demaine, Ku, Solomon, MIT 6.006, Lecture 1**: correctness and complexity, upper/lower/tight bounds, computational model. [MIT OCW](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/477c78e0af2df61fa205bcc6cb613ceb_MIT6_006S20_lec1.pdf).
- **MIT 6.006 Spring 2020 lecture notes**, especially Lectures 3, 5, 18, and 19. [Index](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/pages/lecture-notes/).
- **Michael Dinitz and Jessica Sorrell, Johns Hopkins 601.433/633, Lecture 6 (2025)**, Theorem 6.2.1, pp. 1–3: explicit comparison-model sorting lower bound and linear-time integer alternatives. [Lecture notes](https://introalgorithmsfall25.cs.jhu.edu/schedule/Lectures/Lecture6/lecture6.pdf).
- **Stanford CS161 course reading/schedule**, asymptotics, mergesort, and recurrences. [CS161](https://cs161-stanford.github.io/lectures/).
- **MIT 6.006 Lecture 19: Complexity**, P, NP, reductions, and hardness. [MIT OCW](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/resources/lecture-19-complexity/).

### Reasoning exercises

1. Identify the failed assumption if binary search is applied to an unsorted array.
2. For `n=8`, show why a comparison sort must sometimes make at least 16 comparisons.
3. Give an example of an algorithm polynomial in a numerical parameter that is exponential in the parameter's bit length.
4. Explain why counting sort does not disprove the comparison lower bound.
5. Which claims about NP-complete problems are established by reductions, and which would require resolving a major open problem?
