# A Slow Operation Does Not Mean a Slow Algorithm: Amortized Analysis

**Track:** Algorithms, Computability, and Complexity  
**Lecture:** 017000  
**Preparation:** Arrays, powers of two, summing geometric series, and worst-case running time.  
**Companion:** Aggregate, accounting, and potential-method analyses.

<!-- BEGIN SPOKEN LECTURE -->

You have an array that stores a growing collection of values. Most of the time, appending one item is nearly free: put it in the next open slot. But sometimes the array is full. To append another item you must allocate a larger array, copy every existing item, then add the new one. That particular append can take time proportional to the entire collection. Does this mean that appending n items one after another must take time proportional to n squared?

No. The conclusion confuses the worst cost of one operation with the cost of a whole sequence of operations. The difference is the subject of amortized analysis. It is not probability, and it does not require a distribution of inputs. We make a worst-case guarantee about every sequence of operations, even when an adversary knows exactly when each resize will occur.

Suppose the array starts with capacity one. Whenever it fills, allocate a new array with twice the capacity and copy all existing elements. Count a write to the new element as one unit, and count each copied element as one additional unit. The first append costs one. The next triggers a copy of one and costs two. When capacity two fills, the next append copies two and costs three. At the next doubling it copies four and costs five. Large spikes occur, but only when the length crosses powers of two.

After n appends, the ordinary append writes cost exactly n. The copies occur at capacities one, two, four, eight, and so on, up to the largest previous capacity less than n. Their sum is a geometric series less than twice n. Thus the total counted work, copies plus one new write per append, is below three n for this convention, apart from initialization and allocation overheads. The average counted cost per append is bounded by a constant. We say the operation takes constant amortized time even though some individual appends take linear time.

The exact constants depend on the cost model and starting capacity. If allocating a block has a cost beyond copying and writing elements, it must be accounted for too. What matters is that doubling produces enough unused space to pay for many subsequent cheap appends before another expensive copy. If instead we enlarged the array by exactly one slot each time, appending the n-th item would copy n minus one previous items. The total would be a triangular sum, growing quadratically. The growth policy, not just the fact that arrays can resize, determines the bound.

That first proof is an aggregate analysis. Add all actual operation costs and divide by the number of operations. A second method uses an imagined bank account. Charge each append a few units, pay its immediate write, and save the remainder as credit associated with the elements or free slots that will need copying later. By the time the array becomes full, enough credit has accumulated from the cheap appends since the previous resize to pay for copying the old contents. The stored credits are not real time units or measured electrical energy. They are accounting devices that produce a rigorous upper bound on cumulative work.

A third method formalizes the bank account with a potential function. Let the potential be a nonnegative number assigned to the current state of the data structure. Define the amortized cost of an operation to be its actual cost plus the change in potential. A cheap operation may increase potential, storing money for later. An expensive operation may decrease it, releasing stored money. Sum this definition over a whole sequence. Every intermediate potential cancels with its neighbor, leaving total actual cost equal to total amortized cost plus initial potential minus final potential.

If potential is always nonnegative and starts at zero, an upper bound on the sum of amortized costs is also an upper bound on the sum of actual costs. The choice of potential has to fit the data structure. It is not enough to announce that some future cheap operations will compensate for an expensive one; the potential must make the compensation visible in a single algebraic inequality.

Here is a clean potential for a doubling array that only supports append. Let n be the current number of elements and C the current capacity, with C a power of two, and use potential equal to two n minus C, except clamp it to zero if that expression would be negative. After the very first insertion, it is convenient to normalize the initial state separately. Between doublings, the potential typically increases by two for each added element. When the array doubles at full capacity, it drops by an amount proportional to the number of copied elements. With a slight adjustment to initialization and counting conventions, one can bound the amortized append cost by a small absolute constant. The companion gives an exact version with no hand-waving about the initial state.

Potential functions are useful far beyond resizable arrays. Consider a binary counter represented by bits. Incrementing the counter may flip several trailing ones to zero before it flips the first zero to one. If the counter currently ends with ten ones, one increment flips eleven bits. But over many increments, the lowest bit flips every time, the next bit every second time, the next every fourth time, and so on. The total number of flips over n increments is bounded by n plus n over two plus n over four, continuing to a total less than two n. Again, a single expensive operation does not imply an expensive sequence.

We can attach one unit of potential to every bit currently set to one. When an increment flips k trailing ones to zero and then one zero to one, its actual cost is k plus one. The potential changes by one minus k. Add actual cost and potential change: the amortized cost is exactly two. This is a particularly transparent potential proof. Each flipped-off one pays for itself by releasing its stored credit. The argument is deterministic, and it applies to every sequence of binary increments starting from zero.

Amortized analysis is sometimes confused with average-case analysis. They answer different questions. Average-case analysis requires a probability distribution over inputs or operation sequences, and computes an expectation. Amortized analysis takes an arbitrary sequence and distributes its total cost across its operations, without assuming those operations are randomly drawn. A hash table's expected constant-time operation under a specified hashing model and a dynamic array's amortized constant-time append are distinct kinds of guarantee, though a real implementation may involve both.

The distinction also matters in real-time systems. A constant amortized cost does not prevent an occasional long pause. If a control loop must finish every operation within a strict deadline, average or amortized guarantees may not be sufficient. A data structure can be efficient in total work and still violate a latency requirement. Incremental resizing or a different storage layout may be needed to bound individual operations.

We began with an apparent paradox: a single append might copy everything, yet a long sequence of appends can be cheap. The resolution is that expensive events cannot occur frequently under a doubling policy. Amortized reasoning makes a time-scale distinction mathematically precise. To understand an algorithm, sometimes the right unit of analysis is not an isolated step but an entire history of steps.

<!-- END SPOKEN LECTURE -->

## Mathematical companion

A doubling array starts with \(n=0,C=1\). An append costs one for the new item, plus \(C\) copies if \(n=C\), then updates \(C\leftarrow2C\). For \(N\ge1\), copying costs occur at old capacities \(1,2,4,\ldots,2^{k}\), with \(2^k<N\). Their total is \(2^{k+1}-1<2N\). Thus total element moves and writes are less than \(3N\), for this simplified cost model.

**Exact potential bound for append.** Define \(\Phi(n,C)=2n-C+1\) after the first insertion and \(\Phi(0,1)=0\); for reachable nonempty states of a doubling-only array, \(C/2<n\le C\), so \(\Phi\ge1\). For an append without resizing, actual cost is 1 and \(\Delta\Phi=2\), giving amortized cost 3. For a resizing append at \(n=C\ge1\), actual cost is \(C+1\); new state \((C+1,2C)\) has potential \(3\), old potential \(C+1\), so \(\Delta\Phi=2-C\) and amortized cost 3. For the first insertion, actual cost 1 and \(\Delta\Phi=2\), also 3. This deliberately loose but uniform three-unit bound handles initialization exactly.

**Binary-counter potential.** If a counter increment flips \(k\) trailing ones to zero and then a zero to one, actual cost \(k+1\), and with \(\Phi=\#\text{one bits}\), the potential change is \(1-k\). Thus the amortized cost is 2. Over \(N\) increments starting at zero, the total flips are at most \(2N\). For fixed-width counters, exclude overflow or define its behavior explicitly.

### Exercises with answers

1. **Linear growth.** If the capacity increases by one every time, how many copies occur over N appends? **Answer:** \(0+1+\cdots+(N-1)=N(N-1)/2\).
2. **Amortized versus worst-case.** Can a constant amortized append still take a million copy operations? **Answer:** Yes, if a resize copies about a million elements; the total bound distributes that spike over many earlier cheap operations.
3. **Binary counter.** Incrementing 0111 to 1000 flips how many bits and changes the number of one-bits by how much? **Answer:** Four flips and a potential change of negative two; amortized cost two.
4. **Real-time requirement.** Does an amortized cost bound guarantee every call meets a fixed-time deadline? **Answer:** No, it bounds cumulative work, not the largest individual latency.

### Reading and attribution

- MIT OpenCourseWare, *Introduction to Algorithms* (6.006), lecture on table doubling: https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/pages/lecture-notes/.
- Kevin Wayne, *Algorithm Design*, Data Structures I (amortized analysis), and cited CLRS material: https://www.cs.princeton.edu/~wayne/kleinberg-tardos/.
- The array and counter proofs are standard elementary amortized-analysis examples, independently derived here.
