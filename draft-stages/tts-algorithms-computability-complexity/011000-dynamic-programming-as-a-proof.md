# Dynamic Programming: A Proof Hidden in the Table

**Track:** Algorithms, Computability, and Complexity  
**Lecture:** 011000 — State, recurrence, ordering, and solution recovery  
**Assumed background:** Sorted lists, mathematical induction, sums, and elementary recursion.  
**Companion:** Weighted interval scheduling recurrence and proof, full table trace, reconstruction invariant, contrasting state designs, references, and executable checks.

<!-- BEGIN SPOKEN LECTURE -->

Imagine a laboratory with one instrument and several proposed experiments. Each experiment needs an uninterrupted interval of machine time and produces a specified scientific value. Two experiments can be scheduled together only if their time intervals do not overlap. Which collection should the laboratory run?

One temptation is to schedule whichever experiment finishes first, then repeat. Another is to take the most valuable experiment available. A third is to try every compatible subset. The first two can fail when the objective is total value rather than the number of experiments; the third can find the answer but may explore an exponential number of possibilities. We need to expose the structure of the problem before choosing a method.

Call each proposed experiment a job. Job j has a start time, a finish time, and a nonnegative weight. We will use half-open intervals: a job that runs from time two to time four is compatible with a job beginning exactly at time four. Start must be strictly earlier than finish, and no instrument time may be shared by overlapping jobs. A feasible schedule is any set of pairwise compatible jobs, and the objective is to maximize the sum of its weights. The empty schedule is permitted and has weight zero.

The distinction between maximizing count and maximizing weight is decisive. Consider two short jobs, one from zero to two and another from two to four, each worth four. The earliest-finishing strategy would select both and earn eight. But one long job from zero to four may be worth twelve. Selecting it instead earns twelve. An algorithm for the maximum number of nonoverlapping jobs is not automatically an algorithm for maximum total value, even though both problems mention intervals and compatibility.

Here is the dynamic-programming question: can we describe many possible schedules using only a small collection of states? Instead of remembering the entire chain of experiments already accepted or rejected, sort the jobs by nondecreasing finish time. Break ties deterministically, but the exact tie rule is not relevant to optimal value. Number the sorted jobs from one to n. Let D of j mean the maximum total value obtainable from the first j jobs. Let D of zero be zero. That is our state definition, and it is more important than the first line of any code.

For each job j, define p of j as the number of earlier jobs whose finish times are at most the start time of job j. Because jobs are sorted by finish time, these earlier compatible jobs form a prefix. If j finishes at time six and begins at time four, p of j points to the end of the sorted prefix that finishes by time four. Computing this number is not an optimization guess. It records a mathematical consequence of the chosen ordering.

Now consider any optimal schedule drawn from the first j jobs. Either it does not include job j, or it does. There is no third possibility. If it omits job j, its best possible value is D of j minus one. If it includes job j, no job finishing after j begins can accompany it. Every remaining selected job must belong to the first p of j jobs. Therefore the best possible value for a schedule that includes j is the weight of j plus D of p of j.

Take the larger of those two values. That is the entire recurrence: D of j equals the maximum of D of j minus one, and the weight of j plus D of p of j. The base case is D of zero equals zero. The answer to the original problem is D of n.

Why are we allowed to replace the schedule before j by an optimal one on the smaller prefix? Because the only way the earlier schedule interacts with j is through compatibility. All jobs in that prefix finish before j starts; changing one feasible earlier subset for a better feasible earlier subset cannot create a new overlap with j. If a purported optimum containing j used a suboptimal earlier subset, replacing it with an optimal earlier subset would improve the total value. That contradicts optimality. This is the optimal-substructure argument, and it depends on the precise state we chose.

Listen to the proof as two inequalities. Every feasible schedule for the first j jobs falls into one of the two cases, so no feasible schedule can exceed the larger branch value. Conversely, the best schedule for the first j minus one jobs is feasible for the first j jobs, and the best schedule for the first p of j jobs remains feasible when we append j. So each branch value is achievable, and the larger branch is achievable. An upper bound that is attainable is the exact optimum. That establishes the recurrence, rather than merely making it plausible.

Let's follow a small instance. Job A runs from zero to two and has weight four. Job C runs from zero to four and has weight twelve. Job B runs from two to four and has weight four. Job D runs from four to six and has weight five. Job E runs from three to seven and has weight seven. This order is nondecreasing by finish time; when finishes tie, job C precedes B under our chosen tie rule.

Start with D of zero equal to zero. For A, we either omit it for zero or take it for four, so D of one is four. For C, there is no earlier compatible job; its take value is twelve, which exceeds four, so D of two becomes twelve. For B, A is an earlier compatible job, so its take value is four plus four, or eight. Omitting B preserves twelve, so D of three stays twelve. For D, all three earlier jobs finish by time four; taking D after the best of them gives twelve plus five, or seventeen. For E, only A finishes by its start time three; its take value is four plus seven, or eleven. D of five remains seventeen. The optimal total value is seventeen, achieved by C followed by D.

The numbers expose a subtlety. A schedule is not optimal because it has the most jobs. The three-job schedule A, B, D is feasible, but its weight is thirteen. The two-job schedule C, D has weight seventeen. If a lecture swaps those objectives without saying so, even its beautifully written algorithm can solve the wrong problem.

There is an implementation detail worth dwelling on. In the recurrence, p of j is an index into a sorted prefix, not a time value and not an arbitrary earlier job. To compute it efficiently, sort all finish times alongside the jobs, and use binary search to find how many earlier finish times are no later than the current start time. The use of no later than, rather than strictly earlier than, is what correctly permits touching half-open intervals. On a zero-based programming language, we must also keep the prefix-count convention consistent when translating D of j into an array entry.

Once all p values are available, fill D of zero, D of one, and so on through D of n. Every dependency of D of j has a smaller index: j minus one or p of j, and p of j is strictly below j because a job has positive duration. The computation therefore follows a directed acyclic graph of subproblems. It terminates without recursion and never requests a value that has not yet been computed. The numerical invariant at step j is that every D entry through j equals its defined optimum.

How long does it take? Sorting the n jobs takes on the order of n times log n comparisons. We perform at most n binary searches on the sorted finish array; together these also take on the order of n times log n operations. Computing each D entry takes constant time once its predecessor and earlier values are known, for n entries in total. Under the ordinary word-cost model, the overall time is O of n log n and the auxiliary storage is O of n. This is a bound for the specified representation and cost assumptions, not a claim that arithmetic on arbitrarily large weights has constant bit cost.

A recursive program can use exactly the same mathematical recurrence. Without caching, however, it can solve the same subproblem many times, branching repeatedly into overlapping computations. Memoization stores each solved state, making later calls cheap. Bottom-up tabulation computes those states in an order where their prerequisites are ready. In this example both are valid; the table makes the dependency order and reconstruction steps particularly visible. Dynamic programming is not defined by writing for-loops, and it is not made correct by adding a cache to an incorrect recurrence.

We have computed the optimal value. But a laboratory needs the actual schedule. To recover it, return from state n through the table. At state j, compare the value of omitting job j with the value of taking it. If taking j is strictly better, record j and jump to state p of j. Otherwise, move to state j minus one. Continue until reaching zero, and reverse the recorded jobs to put them in chronological order. Equal branches may yield different optimal schedules, so our implementation has to choose a deterministic tie policy if repeatable output is important.

The reconstruction proof mirrors the value proof. At every step, the still-unexplained part of the recorded optimal value is exactly the D value of the current state. Choosing a branch attaining the maximum preserves that equality; taking a job also preserves compatibility because the next state is its compatible predecessor prefix. When the walk reaches zero, the recorded jobs are feasible and their weights sum to D of n. In other words, storing the optimum's value is not the same thing as providing a witness, but the recurrence supplies a route to one.

Richard Bellman's work in the nineteen-fifties gave a general mathematical language to optimizing multistage decisions. His principle of optimality says, in substance, that after the first decisions of an optimal policy, the remaining policy must be optimal for the resulting state. The principle is not a magic phrase that excuses us from checking our state design. The phrase resulting state carries the burden: if we have forgotten information that changes future feasibility or cost, the recurrence may be false.

For intervals, the finish-time ordering makes the state surprisingly small. What if a job additionally uses one of three machines, or jobs have setup costs depending on which experiment ran immediately before? Then the state consisting only of a prefix index may be insufficient. We may need to remember which machine is free, the last chosen operation, or other boundary information. Adding state dimensions can restore correctness but also multiply the number of reachable states. The design task is to remember exactly the information that affects future choices, no more and no less.

Consider a different problem to see the pattern. For two sequences of symbols, the longest common subsequence is the longest sequence obtainable by deleting some positions from each without changing the order of what remains. Define a state using a prefix length from each input. If the final symbols match, we can extend a best common subsequence of the two preceding prefixes by that symbol. If they differ, a best solution must omit the last symbol from at least one side, so we take the better of the two shorter-prefix solutions. This produces a two-dimensional dynamic program rather than the one-dimensional interval table. Its correctness again follows from an exhaustive case split and an attainable bound, not from a mysterious optimization trick.

Dynamic programming can also fail as a practical strategy even when its recurrence is correct. A state can require exponential space to describe, or there can be exponentially many reachable states. A weighted problem whose weights are enormous integers may make arithmetic cost significant. A table indexed by every possible total weight can take time polynomial in the numerical magnitude of a weight while being exponential in the number of bits needed to write that weight. State counts and input encodings matter. The existence of a recurrence does not establish an efficient algorithm.

The executable lab accompanying this lecture checks weighted interval schedules against a separate brute-force specification for small inputs. It verifies optimal value, compatibility of reconstructed jobs, and agreement with the value recurrence. These are useful checks, especially around touching intervals, equal finish times, zero weights, and tie choices. They do not replace the induction showing that the state definition and branch split are valid for all finite inputs.

The central habit to practice is this: before writing a table, say exactly what each entry means. Then prove that the possible first or last decisions exhaust the feasible cases. Then prove that the remaining instance really has the state your recurrence names. Only then decide whether to memoize or tabulate, and only after that count how many states exist and how much work each one requires. Dynamic programming, at its best, is a mathematical proof translated into a controlled computation.

<!-- END SPOKEN LECTURE -->

## Exact mathematical companion

**Problem.** Jobs `j` have integer `start_j < finish_j` and nonnegative integer `weight_j`. A schedule is compatible when every two half-open intervals `[start, finish)` are disjoint. Maximize total weight over all compatible subsets; the empty subset has value zero.

Order jobs by nondecreasing finish time and number them 1 through n. Define `p(j)` as the number of jobs with index `< j` and `finish_i <= start_j`. Since finish times are sorted, these form a prefix of length `p(j)`. Define `D(j)` to be the optimal weight achievable among jobs 1 through j.

\[
D(0)=0,\qquad D(j)=\max\{D(j-1),\ w_j+D(p(j))\},\quad j\ge 1.
\]

**Correctness proof.** By induction, assume smaller `D` entries equal their specified optima. A feasible subset among the first `j` jobs either omits `j`, in which case its weight is bounded above by `D(j-1)`, or includes `j`, in which case its other jobs lie in the predecessor prefix and their total is bounded by `D(p(j))`. Thus its weight is at most the proposed maximum. Conversely, a schedule attaining `D(j-1)` is feasible without `j`, while a schedule attaining `D(p(j))` remains feasible after including `j`; both branch totals are attainable. So the maximum equals `D(j)`.

### Explicit table trace

| j | Job | Interval | Weight | p(j) | Exclude | Include | D(j) |
|---|---|---|---:|---:|---:|---:|---:|
| 0 | empty | — | 0 | — | — | — | 0 |
| 1 | A | [0,2) | 4 | 0 | 0 | 4 | 4 |
| 2 | C | [0,4) | 12 | 0 | 4 | 12 | 12 |
| 3 | B | [2,4) | 4 | 1 | 12 | 8 | 12 |
| 4 | D | [4,6) | 5 | 3 | 12 | 17 | 17 |
| 5 | E | [3,7) | 7 | 1 | 17 | 11 | 17 |

The optimal witness is C and D, weight 17. The feasible A, B, D schedule has *greater cardinality* (three jobs) but value only 13. Because a job has positive duration, `p(j) < j`, guaranteeing the table's dependency order.

### Witness reconstruction

Starting at `j=n`, when `w_j + D(p(j)) > D(j-1)`, select `j` and continue at `p(j)`; otherwise continue at `j-1`. Ties consistently favor skipping. The invariant is that selected weight plus remaining `D(j)` equals the original `D(n)`, and every selected job is compatible with subsequent selected jobs. Run time after sorting and predecessor computation is `O(n)`, with an `O(n)` traceback.

### Contrast: longest common subsequence

Let `L(i,j)` be the maximum length of a common subsequence of prefixes `a[:i]` and `b[:j]`. The boundary values are `L(i,0)=L(0,j)=0`. For `i,j>0`,

\[
L(i,j)=\begin{cases}
1+L(i-1,j-1) & a_{i-1}=b_{j-1},\\
\max\{L(i-1,j),L(i,j-1)\} & a_{i-1}\ne b_{j-1}.
\end{cases}
\]

When the last symbols match, an optimal common subsequence can be chosen to end in that symbol. When they differ, any common subsequence omits the last position of at least one sequence. Inductively, the recurrence is exact. This illustrates a state space with `O(|a||b|)` states and constant transitions per state.

## Sources, provenance, and further reading

- **Original framework and attribution:** Richard Bellman, [*The Theory of Dynamic Programming*, Bulletin of the American Mathematical Society 60 (1954), 503–515](https://doi.org/10.1090/S0002-9904-1954-09848-8), especially pp. 503–506 and his explicit *principle of optimality*. The lab's interval example is not attributed to Bellman's 1954 paper.
- **Modern weighted-interval derivation:** Jon Kleinberg and Éva Tardos, *Algorithm Design*, chapter 6, sections 6.1–6.2; [Kevin Wayne's companion lecture slides](https://www.cs.princeton.edu/~wayne/kleinberg-tardos/pdf/06DynamicProgrammingI-2x2.pdf), slides on weighted interval scheduling, its two-case recurrence, memoization, and running time. This is a teaching source, not a historical original algorithm claim.
- **Additional methodology:** Erik Demaine, Jason Ku, and Justin Solomon, [MIT 6.006 Spring 2020 lecture notes index](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/pages/lecture-notes/), lectures 15–18 on state selection, recursive relations, and dependency order.
- **Original lecture material:** laboratory-specific five-job instance, its D table and reconstruction, and the independently written exhaustive checker. The source-backed general theorem and the original instance are distinguished in `metadata/011000.json`.

Claim map: `metadata/011000.json`.
