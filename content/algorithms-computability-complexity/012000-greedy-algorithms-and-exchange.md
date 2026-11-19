# Greedy Algorithms: When the Next Choice Can Be Trusted

**Track:** Algorithms, Computability, and Complexity  
**Lecture:** 012000 — Greedy choice, exchange arguments, counterexamples, and matroids  
**Assumed background:** Finite sets, sorted lists, induction, and the idea of an optimal solution.  
**Companion:** Two proofs for interval scheduling, weighted counterexamples, a matroid exchange statement, complexity analysis, and an executable oracle comparison.

<!-- BEGIN SPOKEN LECTURE -->

You have one room and several meetings that people would like to hold in it. Each meeting has a fixed start and finish time. Your objective is to fit as many meetings as possible into the day. Should you accept the meeting that begins soonest? The meeting with the shortest duration? The one that ends soonest? Or is it necessary to compare every possible schedule?

This is a question about greedy algorithms: procedures that make choices now without later retracting them. Greedy is sometimes described as taking the best-looking available option. That description is dangerously incomplete. It does not tell us what best means, nor whether the chosen local criterion is related to global optimality. The defining mathematical task is to find a property that makes some local choice safe.

Our scheduling model is precise. Each meeting occupies a half-open interval, from its start time inclusive to its finish time exclusive, and the start is strictly earlier than the finish. Two meetings are compatible if they do not overlap. Meetings may touch: one can finish at time three, and another can start at time three. There are no weights yet. The objective is the largest number of pairwise compatible meetings, not their total duration, total importance, or profit.

Try the intuitive rule of accepting whichever meeting starts first. Suppose one meeting fills the room from zero to ten, while three others run from one to two, two to three, and three to four. The earliest-start rule takes the long meeting and cannot take any of the other three. An optimal schedule takes all three short meetings. The earliest start time says little about how much room remains for future meetings.

How about choosing the shortest duration? Consider three meetings: one from zero to three, one from two to four, and one from three to six. The middle meeting is shortest, but it overlaps both neighbors. Choosing it permits only one meeting overall, whereas choosing the first and third permits two. Duration alone does not measure the opportunity cost imposed on subsequent decisions.

Now choose the meeting that finishes earliest. Once it is selected, remove every meeting that starts before that finish time. Among the remaining meetings, choose the one that finishes earliest. Repeat until no compatible meeting remains. The algorithm is easy to execute. But ease of execution is not the reason to trust it. We need a proof that selecting the earliest-finishing meeting can never reduce the maximum number of meetings we can ultimately accommodate.

Here is an exchange argument. Let g be a meeting with the earliest finish time among all meetings under consideration. Take an optimal schedule, and let o be its first meeting in chronological order. If that optimal schedule already begins with g, nothing needs to change. Otherwise, replace o with g. Because g finishes no later than o, every later meeting in the optimal schedule starts after g finishes as well. Therefore the replacement preserves feasibility. It also preserves the number of selected meetings: we have exchanged one meeting for one meeting, without losing anything from the remainder.

So an optimal schedule exists that contains our greedy first choice. Once g is fixed, the remaining problem is exactly the same kind of scheduling problem, restricted to meetings that start when g finishes or later. Repeating the exchange reasoning proves that there is an optimal schedule whose first choice, then second choice, then third choice, agrees with the greedy algorithm. By induction, the greedy algorithm returns a maximum-cardinality compatible set.

Notice the structure of this proof. We did not show that every optimal schedule contains g. That would be false when several meetings allow the same maximum count. We showed something weaker and sufficient: there exists an optimal schedule that contains g. The exchange transforms a hypothetical optimum into another optimum that agrees with the greedy choice. This existential step is the bridge between local action and global correctness.

There is a second proof, often called staying ahead. Write the greedy meetings in the order selected, and compare them with the meetings of any other feasible schedule, also in chronological order. Claim that the greedy first meeting finishes no later than the other schedule's first meeting. That is true by the choice rule. Suppose the greedy first i minus one meetings finish no later, position by position, than those of the other schedule. The other schedule's i-th meeting starts no earlier than its preceding meeting finishes. Since the preceding greedy meeting finishes no later, the other schedule's i-th meeting was available as a candidate for the greedy algorithm's i-th choice. The greedy algorithm chose a candidate finishing no later. The induction continues.

If some feasible schedule contained more meetings than greedy, its next meeting after greedy stopped would still be available after greedy's last finish time. That contradicts the stopping condition. This proof does not exchange schedules explicitly. Instead, it maintains an invariant comparing how much future time each partial schedule has preserved. Exchange and staying ahead are two ways of revealing the same essential structure.

How expensive is the computation? Sort meetings by finish time, then scan them once, accepting a meeting exactly when its start is at or after the finish of the last accepted meeting. Sorting requires O of n log n comparisons in the usual comparison model; the scan is linear. If meetings already arrive in finish-time order, the scan itself requires only linear time and constant additional state apart from storing the answer. The proof of optimality makes no assumption about the input's original order, but the implementation must establish the order it relies on.

Now change just one word in the objective. Instead of the maximum number of meetings, each meeting earns a numerical reward. The goal is to maximize the sum of rewards. Does earliest finish still work? No. Suppose the two compatible short meetings, from zero to two and from two to four, are each worth four. One long meeting from zero to four is worth twelve. The earliest-finish algorithm picks the two short meetings for total reward eight. The optimum is the long meeting for twelve. The very same first choice that was safe for cardinality can be unsafe for weight.

Perhaps we should then choose the highest-weight meeting first. That, too, can fail. Make each short meeting worth six and the long meeting worth eleven. A highest-weight-first rule takes the long meeting for eleven; the two compatible short meetings total twelve. No single scalar label attached to one meeting captures all interactions with the compatible meetings that remain. The dynamic-programming method for weighted interval scheduling succeeds because it considers both including and excluding each job and remembers the exact best value of the relevant predecessor prefix.

These counterexamples teach an important discipline. Greedy correctness belongs to a problem specification together with a particular choice rule. It does not belong to the word scheduling, the fact that intervals are sorted, or the intention to make an efficient algorithm. The proof must identify the exact objective, feasibility relation, and structural property that make the choice safe.

Sometimes the structure is much more general than interval geometry. Matroids provide one famous explanation of when a weight-ordered greedy algorithm can be justified. A matroid starts with a finite set of elements and a family of subsets called independent. The family includes the empty set, and whenever a set is independent, all its subsets are independent. But those hereditary conditions are not enough. There is an additional augmentation property: whenever one independent set has fewer elements than another, we can add at least one element from the larger set to the smaller and remain independent.

Think of choosing a set of linearly independent vectors. Removing vectors preserves independence. If you have fewer independent vectors than another independent set, at least one vector from the larger set can extend the smaller one. This is an example of the exchange structure captured by matroids. Another example is choosing edges of a graph without forming a cycle: those edge sets are forests and form a graphic matroid. They are the abstract setting behind the correctness of classic spanning-tree greedy algorithms.

On a matroid, if every element has a nonnegative weight, sorting elements from highest to lowest weight and accepting each when it preserves independence yields a maximum-weight independent set. We can understand the proof through basis exchange. Imagine an optimal solution and the greedy choices already accepted. If the next greedy element is not in that optimum, the matroid's exchange structure permits replacing some still-unfixed element of the optimum by the greedy element while keeping feasibility. Because the greedy element was the highest-weight feasible choice at that stage, the replacement does not decrease weight. Repeat until an optimal solution agrees with all greedy choices. The algorithm is not correct because it is greedy; it is correct because the matroid axioms support precisely the replacements its choices require.

Does interval compatibility form a matroid? Surprisingly, no, even though our earliest-finish algorithm works for the unweighted problem. Take a long interval from zero to four, and two shorter, compatible intervals from zero to two and from two to four. The set containing only the long interval is feasible, and the set containing both short intervals is feasible. The augmentation property would require that we can add one of the short intervals to the long one and remain feasible. We cannot: both short intervals overlap the long one. The independent-set family is hereditary but fails augmentation. This is why weighted greedy scheduling has no general matroid guarantee.

The distinction matters beyond scheduling. Many engineering problems have a family of feasible partial solutions that looks plausible for greedy selection. We may even have a counterexample-free history of test cases. But the relevant question is whether the family's structure allows local choices to be exchanged into a global optimum. Sometimes the answer is yes by an interval-specific theorem. Sometimes yes because the feasible sets form a matroid. Sometimes no, and we need dynamic programming, a graph algorithm, an approximation guarantee, or a fundamentally different approach.

It is worth being precise about historical credit here. Greedy strategies appeared in many algorithms long before there was one general theorem about them. Jack Edmonds's nineteen seventy-one paper, *Matroids and the Greedy Algorithm*, made a central connection between matroid structure, weighted optimization, and efficient greedy selection. That paper also treats more than the simple classroom statement we just used. The theorem does not imply that every greedy algorithm is matroidal, as our interval example already demonstrates.

There is another trap: proving correctness by assuming the algorithm's first choice must belong to the unique best solution. The best solution need not be unique. Even if no optimal solution uses the first choice in exactly the way we imagined, a constructive exchange may turn one optimal solution into another. A robust proof gives an explicit transformation, checks feasibility after the transformation, and compares objective values. A claim that the choice just seems optimal because it leaves more room is not enough without those inequalities.

A final trap is confusing a correct proof with an efficient implementation. Suppose the feasibility test for adding an element takes time exponential in the number of previously selected elements. A greedy loop might still make mathematically optimal choices and yet run very slowly. To establish its overall complexity, specify how candidates are ordered, how feasibility is tested, how the answer is represented, and what each operation costs. For interval scheduling, checking compatibility with the last selected finish time is constant work after sorting. For independence in a vector system or a graph, a different data structure and cost analysis may be necessary.

The companion code uses one small interval dataset in several roles. It computes the earliest-finish greedy schedule, the weighted dynamic-programming schedule, and independently enumerates compatible subsets for small inputs. It also checks the size of the greedy solution against brute force and checks the weighted value against the dynamic program. These tests are designed to catch errors in the code and in the worked examples. They are not an argument that no larger counterexample exists. That universal guarantee belongs to the exchange proof.

So when should you use a greedy algorithm? Not whenever you want something fast, and not whenever the data can be sorted. Use one when you can write down a local rule and prove that a globally optimal solution can be transformed to respect that rule without harming feasibility or objective value. If you cannot produce that transformation, consider which additional state would make the remaining decision problem exact. That question points back toward dynamic programming.

Divide-and-conquer, dynamic programming, and greedy selection are often introduced as rival techniques, as though a problem has a label that determines the right code. But their deeper commonality is proof. Divide-and-conquer establishes what information a partition preserves. Dynamic programming identifies all relevant cases and the state required to remember them. Greedy reasoning identifies an exchange that makes one case safe to commit to immediately. The algorithm is the visible result of that mathematical structure.

<!-- END SPOKEN LECTURE -->

## Exact mathematical companion

**Problem.** Given finitely many half-open, positive-duration intervals `[start_i,finish_i)`, maximize the *number* of pairwise disjoint intervals. No weights appear in the objective.

### Greedy earliest-finish algorithm and exchange proof

Sort jobs by ascending `finish` (deterministic tie-break optional). Maintain `last_finish`, initially no constraint. Scan sorted jobs, accepting `j` exactly when `start_j >= last_finish` and updating `last_finish = finish_j`.

Let `g` be the earliest-finishing candidate and let `O=(o_1,...,o_m)` be an optimal schedule in chronological order. Since `finish(g) <= finish(o_1)` and every `o_i` for `i>=2` starts no earlier than `finish(o_1)`, the schedule `(g,o_2,...,o_m)` is feasible, has the same cardinality `m`, and begins with the greedy first choice. The residual instance consists of intervals starting at or after `finish(g)`; induction proves optimal cardinality of the greedy continuation.

**Staying ahead.** If `g_i` is greedy's i-th selected interval, and `o_i` is the i-th interval of any feasible alternative of length at least i, induction establishes `finish(g_i) <= finish(o_i)`. The induction step uses `start(o_i) >= finish(o_{i-1}) >= finish(g_{i-1})`, hence `o_i` was an available candidate for greedy. If an alternative had an additional interval after greedy stopped, that interval would also be available after greedy's last finish, a contradiction.

### Counterexamples under altered specifications

- **Earliest-start failure:** `[0,10)` versus `[1,2)`, `[2,3)`, `[3,4)`: earliest-start achieves cardinality 1; optimum cardinality 3.
- **Shortest-duration failure:** `[0,3)`, `[2,4)`, `[3,6)`: shortest picks `[2,4)` and achieves 1; the first and third give 2.
- **Earliest-finish for weighted value:** `[0,2)` weight 4, `[2,4)` weight 4, `[0,4)` weight 12. Greedy maximum count is 2 with weight 8, but maximum weight is 12.
- **Highest-weight-first for weighted value:** `[0,2)` weight 6, `[2,4)` weight 6, `[0,4)` weight 11. Heaviest-first returns 11, optimum 12.

### Matroid comparison

A finite matroid is `(E,I)` where `I` contains `∅`, is hereditary under subsets, and obeys augmentation: for `A,B ∈ I` with `|A|<|B|`, there exists `b∈B\A` with `A∪{b}∈I`. On a matroid with nonnegative element weights, descending-weight greedy acceptance of independent elements yields a maximum-weight independent set. A standard proof extends greedy's current prefix into an optimal basis, then exchanges an element of that basis for the next greedy choice, without reducing weight. The required exchange property follows from the matroid axioms (equivalently, its circuit/basis exchange characterizations).

Interval-compatible families are **not** generally matroids. For `A={[0,4)}` and `B={[0,2),[2,4)}`, both are feasible, `|A|<|B|`, but neither element of `B\A` can be added to `A`. The interval-specific earliest-finish proof therefore cannot be generalized to weighted sorting by simply invoking a matroid theorem.

### Complexity conditions

Sorting by finishing time takes `O(n log n)` comparisons and scanning costs `O(n)`. Feasibility is `O(1)` per job because accepted meetings are kept in chronological order and only the last finish time is needed. For matroid greedy, total complexity also depends on the implementation and cost of the independence oracle, not just on sorting.

## Sources, provenance, and further reading

- **Primary historical matroid treatment:** Jack Edmonds, [*Matroids and the Greedy Algorithm*, Mathematical Programming 1 (1971), 127–136](https://deltadbu.github.io/UCAS_algorithm_course/Lectures/Edmonds1971.pdf), especially pp. 127–130. This primary text concerns weighted independent/basis optimization and its larger combinatorial-programming setting.
- **Modern interval-scheduling analysis:** Jon Kleinberg and Éva Tardos, *Algorithm Design*, chapter 4, section 4.1; [Kevin Wayne's official course slides on greedy algorithms](https://www.cs.princeton.edu/~wayne/kleinberg-tardos/pdf/04GreedyAlgorithmsI.pdf), interval scheduling and the exchange argument, plus counterexamples for local heuristics.
- **Related modern dynamic-programming contrast:** [Kleinberg–Tardos slides, chapter 6](https://www.cs.princeton.edu/~wayne/kleinberg-tardos/pdf/06DynamicProgrammingI-2x2.pdf), weighted interval scheduling.
- **Original examples and proofs:** The chosen intervals, explicit augmentation counterexample, and two detailed correctness presentations are independently assembled for this manuscript and checked on finite instances by `examples/algorithm_design_lab.py`. These are not attributed as quotations from Edmonds or Kleinberg–Tardos.

Claim map: `metadata/012000.json`.
