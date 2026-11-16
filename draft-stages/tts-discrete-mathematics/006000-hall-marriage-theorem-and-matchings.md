# 006000 — Matchings and Hall's Marriage Theorem

**Track:** Discrete Mathematics and Combinatorics. **Background:** sets, neighborhoods, paths and bipartite graphs. **Question:** when can every request be assigned a different acceptable resource?

<!-- BEGIN SPOKEN LECTURE -->

# Matchings and Hall's Marriage Theorem

Imagine four students and four available projects. Each student lists the projects they would accept. We want to give every student exactly one project, without assigning any project to more than one student. It is easy to try individual assignments and get stuck. The mathematical question is whether *some* assignment works, even if a particular greedy choice fails.

The correct model is a bipartite graph: vertices are divided into a left set of students and a right set of projects, and edges join only a student to an acceptable project. A matching is a set of edges with no shared endpoints. We want a matching that covers every vertex on the left. We do not necessarily require every right vertex to be used, because there may be more projects than students.

A condition on all subsets of students gives an exact answer. It is called Hall's marriage theorem, after Philip Hall.

## The obstruction that no clever assignment can bypass

Take any group S of students, not necessarily all of them. Let N of S be the collection of projects accepted by at least one student in S. If there are five students in S and only four projects in N of S, those five students cannot all receive distinct acceptable projects. This is a counting obstruction: each of those students would require a different project from a pool of size four.

Hall's condition says that for *every* subset S of the left vertices, the number of neighbors is at least the number of vertices in S. The theorem states that this necessary condition is also sufficient. If no group of students collectively has too few available projects, then some assignment covering every student exists.

The phrase every subset is important. Checking only that each student has at least one acceptable project is far too weak. Three students may all accept only the same two projects, even though each has multiple choices. Looking at the full set also is not enough: the total number of distinct projects may exceed the number of students while a small subgroup still has a shortage.

## Proof by splitting a tight set

We can prove sufficiency by induction on the number of left vertices. If there is one student, Hall's condition ensures at least one neighboring project, so assign it. Now suppose there are several students and every subset satisfies the condition.

First consider the case where some nonempty *proper* subset S of students has exactly as many neighboring projects as students. Call it a tight set. By induction, Hall's condition on subsets of S lets us match all students in S into its neighborhood N of S. That uses every project in N of S.

What about the remaining students? Delete S and the projects N of S. The remaining bipartite graph also satisfies Hall's condition. To see this, take any subset T of the remaining students. In the original graph, the neighborhood of S together with T has size at least the size of S plus the size of T. Since the neighborhood of S has exactly the size of S, at least the size of T neighbors lie outside the deleted neighborhood. Those are available to T in the reduced graph. Induction therefore matches the remaining students. Combining the two matchings solves the whole assignment problem.

The other case is that no nonempty proper subset S is tight. Since neighbor counts are integers, every such subset has at least one more neighbor than member. Choose any student x and any one of the projects y that x accepts. Assign x to y and delete both. For any subset T of the remaining students, the original neighborhood had at least the size of T plus one, unless T is empty. Deleting y can remove at most one project, so the remaining neighborhood still has at least the size of T. By induction we can match everyone else.

That completes the proof. Either a tight subgroup splits the problem into two smaller independent assignments, or every proper subgroup has enough slack that we may commit to one arbitrary edge. Notice the strength of this dichotomy: a naive greedy assignment can fail in general, but in the strict-slack case it cannot destroy Hall's condition.

## An alternating path repairs a bad choice

There is another way to understand matchings. Suppose we currently have a matching, but some student remains unmatched. Search for a path that starts at that student, alternates between edges not in the matching and edges in the matching, and ends at an unmatched project. Such a path is called augmenting.

Flip the status of every edge along the path: previously unmatched edges become matched, and previously matched edges become unmatched. Every internal vertex on the path still has exactly one matching edge, but both endpoints become matched. The total matching size increases by one.

Here is a concrete example. Student A accepts projects one and two. Student B accepts only project one. If we first assign A to one, B appears stuck. But the alternating path runs from B to project one, then back along A's matched edge, then from A to project two. Flip it. B gets project one and A gets project two. Nothing about the acceptable pairs changed. Only the initial choice was wrong.

This yields a useful characterization: a matching is maximum in size if and only if it has no augmenting path. One direction is immediate: an augmenting path would make the matching larger. For the other direction, compare a proposed matching with a larger one. In their symmetric difference, components are alternating paths and cycles. Because the second matching has more edges overall, some alternating path contains one more edge of the larger matching and begins and ends at unmatched vertices of the proposed matching. That is an augmenting path.

## Failure has a certificate too

If no matching covers all left vertices, Hall's theorem guarantees a set S with fewer neighbors than vertices. This set is a concise certificate of impossibility. It does not depend on guessing which assignment an algorithm ought to try. It names the collective shortage.

There is also a famous relationship between matching and vertex covers. A vertex cover is a set of vertices touching every edge. Every matching edge needs a separate covered endpoint, so any vertex cover has at least as many vertices as a matching has edges. In bipartite graphs, König's theorem says equality is always possible: the maximum matching size equals the minimum vertex-cover size.

A constructive proof starts with a maximum matching. From every unmatched left vertex, traverse alternating paths, going along unmatched edges from left to right and matching edges from right to left. Let Z be the set of vertices reached. Then take all left vertices *not* in Z together with all right vertices *in* Z. This is a vertex cover whose size equals the matching size. If the sizes differed, the alternating reachability structure would expose an augmenting path. This argument connects the matching problem to the broader idea of mathematical certificates: a feasible matching gives a lower bound, while a vertex cover gives an upper bound, and equality proves optimality.

## Where the theorem is useful

The theorem is not only about students and projects. It appears whenever scarce, distinguishable resources must be assigned injectively: jobs to machines, rooms to events, representatives to sets, or variables to constraints in a structural model. The exact same proof works with abstract finite sets, independent of the story attached to their vertices.

The condition quantifies over exponentially many subsets, so it does not itself provide the most efficient computational test by brute force. Alternating-path algorithms can construct a maximum matching and, when full coverage fails, identify a violating set. The mathematical point comes first: Hall gives a complete characterization of when distinct representatives exist, and matching algorithms exploit that structure.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Let \(G=(L\sqcup R,E)\) be a finite bipartite graph and \(N(S)\subseteq R\) the neighborhood of \(S\subseteq L\). **Hall:** a matching saturating all of \(L\) exists iff
\[
|N(S)|\ge |S|\qquad\text{for every }S\subseteq L.
\]

**Proof by induction:** If a nonempty proper \(S\subset L\) satisfies equality, match within \(S\cup N(S)\), then match in the remainder; Hall holds there by applying Hall to \(S\cup T\). Otherwise every nonempty proper \(S\subset L\) has \(|N(S)|\ge|S|+1\); remove any edge \(xy\) and apply induction to the remaining graph.

**Augmenting path criterion:** a matching \(M\) is maximum iff it admits no \(M\)-augmenting path. In a bipartite graph, \(\nu(G)=\tau(G)\) (König's theorem), where \(\nu\) is the maximum matching size and \(\tau\) the minimum vertex-cover size.

### Exercises with answers

1. Three students all accept precisely two projects. Can every student be assigned a different one? **Answer:** no; their joint neighborhood has size two, violating Hall.
2. If each of four students accepts three projects and each of those projects accepts at most three students, must Hall hold? **Answer:** yes, by double counting the edges leaving any subset \(S\): at least \(3|S|\) incidences and at most \(3|N(S)|\).
3. Why does flipping an augmenting path increase matching size by one? **Answer:** it has one more previously unmatched edge than matched edge, with all internal endpoints retaining one match.
4. What proves a matching of size six is maximum when a vertex cover of size six is given? **Answer:** every matching has size at most every vertex cover's size, so both are optimal.

### Reading

MIT OpenCourseWare, [Mathematics for Computer Science](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/pages/readings/), matching and graph-theoretic counting; MIT, [6.854 course notes](https://courses.csail.mit.edu/6.854/18/Notes/), flow and matching relationships.
