# Counting After Forever: Ordinals and Transfinite Induction

<!-- BEGIN SPOKEN LECTURE -->

There are two ways to ask how big a collection is. One asks how many members it has. The other asks what it means to proceed through its members in a definite order. For three objects, these questions can look interchangeable. Every sequence of three distinct objects has the same length, regardless of their order. For an infinite collection, the two questions separate.

Imagine a queue with one person at every position numbered one, two, three, and so on. There is no last person. Now imagine the same queue, followed by one final person who waits until all those numbered positions have been passed. Both queues have countably many people. But the second queue has a last person and the first does not. No order-preserving bijection can identify them.

Cardinal numbers compare sizes without regard to order. Ordinal numbers classify well-ordered arrangements. The distinction lets us speak about a first infinite stage and then a next stage, and a next one after that. It also gives a form of induction stronger than the induction on ordinary natural numbers. We will build this idea carefully, and then use it to explain a proof principle that appears across set theory, termination proofs, and formal mathematics.

## Order is extra information

An ordering relation tells us which element precedes another. A well-order is a linear order in which every nonempty subset has a least element. The natural numbers with their usual ordering are well-ordered: take any nonempty collection of natural numbers, and it has a smallest member. The integers with their usual ordering are not well-ordered, because the set of negative integers has no smallest member.

The word well is doing substantial work. A linear order might let us move indefinitely toward smaller and smaller elements. A well-order does not. That is why well-ordering is such a natural setting for induction. If some property first fails somewhere, there is a least counterexample. Everything smaller satisfies the property. A proof showing that any element with all smaller elements good must itself be good then rules out that least counterexample.

Two well-ordered sets have the same order type if there is an order-preserving bijection between them. For finite well-orders, cardinality determines order type. For infinite ones, it does not. The naturals in their usual order have order type omega. Append one extra point at the end and the order type is omega plus one. Place an extra point before every natural number, and the result is order-isomorphic to the naturals themselves; that order type is one plus omega, which equals omega.

These equations are about order, not size. Omega plus one is not omega as an ordinal, because it has a greatest member. One plus omega is omega because we can renumber the first new point as zero and shift all old naturals up one place. Ordinal addition is therefore not commutative. For example, one plus omega equals omega, while omega plus one is strictly larger than omega.

## Ordinals as sets of predecessors

There is a concrete representation of the ordinals in ordinary set theory. Begin with zero as the empty set. Let one be the set containing zero. Let two contain zero and one. At each finite stage n, the set n contains precisely its predecessor ordinals. Define the successor of an ordinal alpha to be alpha together with a singleton containing alpha.

The first infinite ordinal omega is the set of all finite ordinals. Its successor, omega plus one, contains every finite ordinal and omega itself. The membership relation orders these objects: beta comes before alpha when beta is an element of alpha. This way of constructing ordinals makes each ordinal equal to the set of its predecessors. It also makes the statement beta is less than alpha literally a membership statement for ordinals.

An ordinal is not simply any set assembled by these operations; formally it is a transitive set well-ordered by membership. Transitive means that whenever x belongs to the set and y belongs to x, y belongs to the set too. This prevents gaps in the predecessor structure. Every ordinal has a unique position among the ordinals, and any two ordinals are comparable by membership or equality.

There are successor ordinals and limit ordinals. A successor ordinal has an immediate predecessor. A nonzero limit ordinal does not. Omega is our first example of a limit ordinal. Omega plus one is a successor. Omega times two, the order type of two consecutive copies of the naturals, is another limit. There is no final ordinal containing every ordinal. The ordinals form a proper class, and the argument resembles the impossibility of a universal set.

## Induction when there is no previous step

Ordinary induction proves a property of all naturals by checking zero and showing that truth at n implies truth at n plus one. That argument follows the successor structure of the natural numbers. Beyond omega, we also need to handle limit stages. A general transfinite-induction principle is simpler to state than its three familiar cases.

Suppose P is a property of ordinals. Show this: for every ordinal alpha, if P holds at every beta smaller than alpha, then P holds at alpha. Then P holds for every ordinal. If there were a failure, take the least ordinal alpha where P fails. All earlier ordinals satisfy P by minimality, so the hypothesis forces P at alpha, a contradiction.

In practice, proofs often divide this into the zero case, the successor case, and the limit case. At a successor, use the result at the predecessor. At a limit, use all preceding results. But the unified statement makes clear why the limit case is not optional. A property might hold through every finite stage and fail at omega unless we provide a reason that the property survives passage to that limit.

For an example, consider the cumulative hierarchy of sets. At stage zero it begins with the empty set. A successor stage takes the power set of the previous stage. At a limit stage it takes the union of all earlier stages. To show the hierarchy is increasing, prove that each stage is contained in every later stage. The successor argument uses the fact that every set in an appropriate previous stage is included in its power set at the next stage: because those earlier stages are transitive and built cumulatively, membership of their elements provides the needed subset relation. At limits, the union contains each earlier stage. The full induction then establishes monotonicity.

A more direct example avoids the machinery of the hierarchy. Define a sequence of sets by starting with a set A zero, extending it at successor stages, and taking unions at limits. If each successor step includes the old set, then every earlier stage is contained in every later stage. The proof proceeds by transfinite induction. When the current stage is a limit, every earlier stage is literally a component of the union; no new argument by a nonexistent immediate predecessor is available.

## Transfinite recursion is a different theorem

Induction proves a property of an already defined structure. Recursion constructs the structure itself. On the natural numbers, a recursive definition gives a starting value and a rule for computing the next value from the preceding one. Transfinite recursion allows the value at ordinal alpha to depend on the entire preceding segment of values, not just one previous value.

One might define a function F on ordinals by saying that F at alpha is some specified construction applied to the function already defined below alpha. At zero there is no previous information. At a successor the previous segment includes the immediate predecessor. At a limit it includes all earlier stages. A transfinite recursion theorem establishes existence and uniqueness under suitable functional rules and set-theoretic hypotheses, for a chosen set-sized ordinal domain; class recursion requires its own careful formulation.

Here is a simple ordinal-valued example. Start with zero. At each successor, apply the ordinal successor operation. At a limit, take the supremum of all earlier values. The result is the identity function: at every ordinal alpha the value is alpha. This sounds circular as a definition, but the recursion theorem supplies the argument that the values can be constructed consistently along the well-order.

The cumulative hierarchy is a more important example. Its definition uses power sets at successors and unions at limits. The hierarchy is not computed by a finite machine running through every ordinal. It is a mathematical recursion across a well-ordered domain. The distinction between an existence theorem and an executable program is essential in formal verification too.

## Why ordinal arithmetic is not cardinal arithmetic

The countably infinite ordinals omega, omega plus one, omega times two, and omega squared all have the same cardinality, aleph nought. Yet they are different order types. Omega times two represents one countable sequence followed by another. Omega squared represents a sequence of countably many countable blocks. The total elements remain countable in both cases, but the shape of the ordering changes.

Think of ordinal multiplication as repeating blocks in order. Two times omega is a succession of omega many two-element blocks. That has order type omega. Omega times two is two consecutive blocks, each with order type omega. That has a second infinite segment after the first is complete. Hence two times omega equals omega, while omega times two is larger. We cannot rearrange the blocks without changing the order type.

This matters because ordinal arithmetic appears in ranking arguments. Suppose a process has two phases, each capable of an arbitrarily large finite number of steps. A natural-number ranking may be awkward: at the boundary, the next phase can begin with an arbitrarily large counter. An ordinal ranking of omega times two can express two layers of progress. During the later phase we occupy an ordinal segment above omega. Once we leave it, the remaining process has rank below omega. Every individual step strictly decreases the ordinal. Since no ordinal supports an infinite strictly decreasing sequence indexed by the natural numbers, the process terminates.

Here is an illustrative rank. Give states in phase two rank omega plus n, where n is a finite remaining-work counter, and states in phase one rank n. Within either phase a step decreases n. The transition from phase two to phase one decreases from omega plus n to a finite ordinal, regardless of how large the new finite counter becomes. The rank proves termination if transitions follow these rules. It does not tell us a fixed numerical time bound: there may be no single finite bound uniform across all starting configurations.

## How much set theory is hidden in the word order?

Every explicitly given well-order has an order type, an ordinal, and we can develop ordinals in ZF without the axiom of choice. But the assertion that every set can be well-ordered is stronger. It is equivalent, over ZF, to the axiom of choice. We should not silently say every arbitrary set has an ordinal ordering without naming that assumption.

Similarly, the assertion that every collection has a least member belongs to a particular well-order, not to an arbitrary partial ordering. The set of real numbers in its usual order does not have that property. An arbitrary family of subsets ordered by inclusion might have incomparable members. When we use transfinite induction, a specified well-founded or well-ordered relation is doing the work.

The main gain is a form of reasoning that is not limited to finite stages. A successor tells us how to go one step further. A limit tells us what accumulated information means when there is no last step. Induction tells us that a proposed counterexample would have had to be the first, and cannot exist. Recursion tells us how to define a mathematical object along the ordering. With these tools, the infinite becomes structured enough to support proofs as precise as any argument about a finite loop.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

An ordinal is a transitive set well-ordered by \(\in\). For every ordinal \(\alpha\), the successor is \(\alpha+1=\alpha\cup\{\alpha\}\). The least infinite ordinal is \(\omega=\{0,1,2,\dots\}\). Every ordinal is the set of its predecessor ordinals. Ordinals are classified as zero, successor, or nonzero limit.

**Order types versus cardinality.** \(1+\omega=\omega\), but \(\omega+1>\omega\). Likewise \(2\cdot\omega=\omega\), \(\omega\cdot2>\omega\). Cardinally, all of \(\omega\), \(\omega+1\), \(\omega\cdot2\), and \(\omega^2\) are countable.

**Transfinite induction.** If \(\forall\alpha\,[\,(\forall\beta<\alpha\,P(\beta))\Rightarrow P(\alpha)\,]\), then \(\forall\alpha\,P(\alpha)\). On a fixed ordinal domain, transfinite recursion constructs \(F(\alpha)\) from \(F\restriction\alpha\) when the defining functional meets the relevant hypotheses.

**Ranking example.** For a two-phase process, let \(\rho(\text{phase 2},n)=\omega+n\) and \(\rho(\text{phase 1},n)=n\). A transition from phase 2 to phase 1 strictly decreases \(\rho\) whatever finite counter the second state has. Every other transition must strictly lower the counter. This yields termination for individual executions, not a uniform finite runtime bound.

**Exercises and solutions.** (1) Why is \(\omega+1\ne\omega\)? *Answer:* the first ordered set has a greatest point; the second does not. (2) Why is \(1+\omega=\omega\)? *Answer:* place the new first point at zero and shift old points up one. (3) Give a property true at every finite ordinal but false at \(\omega\). *Answer:* being finite. A proof that only handles successor stages cannot conclude it holds at all ordinals. (4) Explain the limit clause for cumulative stages. *Answer:* at limit \(\lambda\), take \(V_\lambda=\bigcup_{\beta<\lambda}V_\beta\).

### Sources and reading

- Stanford Encyclopedia of Philosophy, *Set Theory*: https://plato.stanford.edu/entries/set-theory/
- Open Logic Project, *Set Theory*: https://builds.openlogicproject.org/content/set-theory/set-theory.pdf
- Stanford Encyclopedia of Philosophy, *The Axiom of Choice*: https://plato.stanford.edu/entries/axiom-choice/
