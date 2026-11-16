# 018000 — Entropy as a Counting Tool: Shearer's Inequality

**Track:** Discrete Mathematics and Combinatorics. **Background:** elementary probability, set families, projections, conditional probability. **Central question:** how can uncertainty place sharp limits on how many combinatorial objects are possible?

<!-- BEGIN SPOKEN LECTURE -->

# Entropy as a Counting Tool: Shearer's Inequality

Suppose you are given an enormous family of possible configurations. Listing them is impossible, but perhaps you can look at the configurations through smaller windows: a few coordinates at a time, or a few overlapping subsets of variables. Can those limited views tell you how many full configurations there could be?

A powerful answer comes from information theory. Entropy measures uncertainty, and a uniform random choice from a finite family has entropy equal to the logarithm of the family's size. This turns a counting problem into an inequality about random variables. The surprising part is that overlapping partial views can be combined without counting the same information too many times.

## Why logarithms make counting easier

Take a finite set F of permitted binary strings, all of the same length. Choose one string uniformly at random, and call its coordinates X one through X n. Knowing the whole random string is equivalent to identifying one of the members of F. In base-two units, the uncertainty is the logarithm of the number of strings.

If the coordinates were independent fair bits, the entropy would simply be n. Constraints introduce dependence and can lower the entropy. For example, if every string must have its last bit equal to its first bit, those two coordinates contribute only one independent choice. The entropy of the complete string is not the sum of the entropies of its coordinates.

The chain rule tells us how to account for dependence. Reveal the coordinates one at a time. The entropy of the entire string is the entropy of the first bit, plus the additional uncertainty of the second bit after learning the first, and so on. Each term is a conditional entropy, and conditioning on more information cannot increase it.

This simple observation does much of the work in combinatorial entropy arguments.

## The covering inequality

Imagine selecting several subsets of the coordinate positions. For each subset, observe only the coordinates it contains. Assume that every coordinate position is included in at least r of these selected subsets. Shearer's inequality says that the entropy of the full vector, multiplied by r, cannot exceed the sum of the entropies of the observed subvectors.

The factor r prevents double-counting. If each coordinate is observed twice, the total entropy of all the partial observations must be at least twice the entropy of the original vector. Overlap is not a nuisance that invalidates the estimate; the proof uses the coverage multiplicity explicitly.

Here is the proof idea. Fix an order in which all coordinates will be revealed. For each chosen subset, expand the entropy of its projection using the chain rule. The conditional uncertainty of one coordinate given earlier coordinates inside the subset is at least the conditional uncertainty given all earlier coordinates in the full vector. A subset knows less history, so it cannot be more certain. Add the resulting lower bounds over all subsets. Every full-vector chain-rule term appears at least r times. That gives the claimed inequality.

There is nothing asymptotic about the result. It works for any finite collection of discrete random variables, and the subsets need not be the same size. The ordering of coordinates is arbitrary, yet the final inequality does not depend on it.

## From entropy back to counting

For a concrete combinatorial use, let F be the family of valid assignments and choose an assignment uniformly. The entropy of the full vector is log base two of the size of F. Each projected vector takes values in the projection of F onto its chosen coordinates, so its entropy cannot exceed the logarithm of the size of that projection.

Combining these statements gives a counting inequality. The size of F, raised to the power r, is at most the product of the sizes of all its selected coordinate projections. It is a bound on a high-dimensional collection using lower-dimensional shadows.

Consider a finite set S of points in a three-dimensional integer lattice. Project it onto the three coordinate planes. Every coordinate appears in exactly two of these three projections. Shearer's inequality says that the square of the number of points in S is at most the product of the numbers of points in its three shadows. This is the discrete Loomis–Whitney inequality.

For a rectangular box of grid points, equality holds. If there are a choices of first coordinate, b of second, and c of third, the whole box has a times b times c points. Its coordinate-plane projections have a times b, a times c, and b times c points. Their product is the square of the original count. Thus the inequality is tight, not merely a loose estimate with the right general shape.

## A four-string example

Take the four binary strings of length three having at most one coordinate equal to one. There are four possibilities: all zero, or a single one in one of three positions. Each projection onto a pair of coordinates has three possible values: zero-zero, one-zero, and zero-one. If we observe all three pairs of coordinates, every original coordinate is represented in two observations.

The counting inequality tells us that four squared cannot exceed three cubed. Sixteen is indeed no greater than twenty-seven. This particular example does not attain equality, but it lets us see exactly how a restriction on full configurations is reflected in limited views.

Notice what the method did not need. We did not derive a recurrence for the family, enumerate all allowed objects, or solve a generating function. The argument used only a random choice, projections, and an entropy inequality.

## When the method is useful and when it is not

Entropy bounds are particularly effective when a complicated combinatorial object has several overlapping descriptions, each of which is easy to count. They can control families of subsets, incidence structures, arrangements, and constrained configurations. Some sharp graph-theoretic counting theorems use considerably more sophisticated entropy decompositions, but this is the essential starting point.

The method does not produce an exact count by itself. If the projections are large or if their overlap structure is poorly chosen, the bound may be weak. Choosing the right coordinate subsets is a mathematical decision, not an automatic consequence of writing down an entropy expression.

It is also important not to confuse the entropy of a particular distribution with the logarithm of the entire possible support. Equality holds for a uniform distribution on the support; otherwise entropy is smaller. In counting proofs we often choose the uniform distribution precisely to make the two coincide.

The deeper lesson is that information cannot be manufactured by viewing the same system through several windows. Once we quantify how often each coordinate has been observed, we can turn this conservation of uncertainty into rigorous bounds on the number of combinatorial possibilities.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For finite discrete random variables \(X=(X_1,\ldots,X_n)\), entropy in bits is \(H(X)=-\sum_x p(x)\log_2 p(x)\). The chain rule and monotonicity under conditioning give
\[H(X)=\sum_{i=1}^n H(X_i\mid X_1,\ldots,X_{i-1}),\quad H(Y\mid Z,W)\le H(Y\mid Z).\]
**Shearer's inequality:** let \(\mathcal A\) be a collection of subsets of \([n]\), counted with multiplicity if desired, such that each i belongs to at least r members. Then
\[r H(X)\le\sum_{A\in\mathcal A} H(X_A).\]
Proof: for each A use the chain rule in the global coordinate order and bound each \(H(X_i\mid X_{A\cap[i-1]})\ge H(X_i\mid X_{[i-1]})\); sum over A.

For a finite family \(F\subseteq\prod_i\Omega_i\), let X be uniform over F. Since \(H(X)=\log_2|F|\), and \(H(X_A)\le\log_2|\pi_A(F)|\), we conclude
\[|F|^r\le\prod_{A\in\mathcal A}|\pi_A(F)|.\]
**Discrete Loomis–Whitney:** if \(S\subseteq A\times B\times C\) is finite, then
\[|S|^2\le |\pi_{AB}(S)|\,|\pi_{AC}(S)|\,|\pi_{BC}(S)|.\]
Equality holds for Cartesian-product boxes. For \(F=\{000,100,010,001\}\), all three pair projections have size 3, yielding \(4^2\le3^3\).

### Exercises with answers

1. Why is \(H(X)=\log_2|F|\) when X is uniform on F? **Answer:** each outcome has probability \(1/|F|\), so the sum gives log of the cardinality.
2. Explain why observing coordinates \(1,2\) and \(2,3\) alone does not permit r=2. **Answer:** coordinates 1 and 3 appear only once; r can be at most 1.
3. Verify equality for a box \(S=A\times B\times C\). **Answer:** the product of projection sizes is \((|A||B|)(|A||C|)(|B||C|)=|S|^2\).
4. Can the counting inequality prove an exact enumeration for an arbitrary family? **Answer:** not in general; it supplies bounds, with equality only under additional structural conditions.

### Reading and source notes

- [*Entropy Methods in Combinatorics* (ICM 2026 survey)](https://epubs.siam.org/doi/full/10.1137/25M180874X), treatment of Shearer's inequality and its history.
- Jaikumar Radhakrishnan, [*Entropy and Counting*](https://bpb-us-e1.wpmucdn.com/sites.harvard.edu/dist/7/800/files/2024/10/spring2016-cs229r-radhakrishnan_survey.pdf), lecture notes on combinatorial entropy methods.
- [MIT OpenCourseWare, Mathematics for Computer Science](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/), probability and counting prerequisites.
