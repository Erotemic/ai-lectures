# 003000 — Generating Functions: Turn Counting into Algebra

**Track:** Discrete Mathematics and Combinatorics. **Background:** elementary counting and polynomial multiplication. **Question:** how can a single algebraic expression store an entire sequence of counting answers?

<!-- BEGIN SPOKEN LECTURE -->

# Generating Functions: Turn Counting into Algebra

Imagine that a shop sells packets containing two or three identical tokens. You want exactly twelve tokens. How many ways are there to choose a collection of packets, if the order of purchasing them does not matter? It is possible to solve this by trying a few cases. But what if the target were twelve thousand, or there were twelve packet sizes instead of two?

A generating function turns a count for every target into the coefficients of one formal expression. It is a way to make the operations we perform on objects correspond to algebraic operations on series.

## Coefficients carry the information

Given numbers a-zero, a-one, a-two, and so on, write the expression a-zero plus a-one times x plus a-two times x squared, continuing indefinitely. This is the ordinary generating function of the sequence. The coefficient of x to the n is a-n. The variable x is initially only a marker of size, not a value to be chosen.

For example, the sequence one, one, one, one, continuing forever has generating function one plus x plus x squared and so on. Formally, this is one divided by one minus x, because multiplying by one minus x cancels every positive power of x and leaves one.

If you have seen geometric series in calculus, you may expect a condition such as the absolute value of x less than one. That condition matters when assigning a numerical value to an infinite sum. But we can work in the ring of formal power series instead. Two series are equal when all their coefficients agree. A coefficient of a product uses only finitely many terms, so the algebra makes sense without asking whether the series converges as a function of a real or complex number.

That distinction is particularly valuable in combinatorics: a generating function may encode an enormous sequence even when we never intend to substitute a numerical x.

## Why multiplication counts combinations

Suppose a-n counts choices of an object of size n from one category, and b-n counts choices of an object of size n from another. To choose a pair with combined size n, we can give the first object size zero and the second size n, or size one and size n minus one, and so forth. The number of pairs is the sum of a-k times b at n minus k over all k from zero to n.

Exactly the same sum appears as the coefficient of x to the n when we multiply the generating functions. This coefficient rule is called convolution. Ordinary multiplication of power series is not merely an analogy for pairing choices: the distributive law explicitly lists every possible size split.

For example, a single kind of packet containing two tokens can be purchased zero, one, two, or more times. Its generating function is one plus x squared plus x to the fourth and so on: one divided by one minus x squared. Packets of size three similarly give one divided by one minus x cubed. Combining independent choices means multiplying the expressions.

The coefficient of x to the twelfth in one divided by the product of one minus x squared and one minus x cubed counts nonnegative integer solutions to two a plus three b equals twelve. We may choose six two-token packets and no threes, three twos and two threes, or no twos and four threes. There are exactly three possibilities.

The coefficient calculation encoded all of that. We did not need to write a separate expression for each target.

## A product for many independent choices

If objects may have sizes one through k, with an unlimited number of each size, the generating function is the product over those sizes of one divided by one minus x to that size. The coefficient of x to the n counts partitions of n using only the allowed part sizes. Here order does not matter: a collection with two size-one parts and one size-three part is the same collection regardless of the order in which the parts are listed.

If each category may be used at most once instead, the factor becomes one plus x to the category's size. The product of these two-term factors counts subsets by total weight. If each category has exactly one item that must be chosen, we would use only x to that size. These are different counting problems, and the factors express the differences unambiguously.

A common source of errors is to use an unlimited-choice factor for a problem about arrangements, or a subset factor for a problem where repeated choices are permitted. The generating function cannot rescue an incorrect model of the combinatorial objects.

## Stars, bars, and repeated factors

Take k distinguishable containers and place n indistinguishable tokens among them, allowing empty containers. Every container contributes the series one plus x plus x squared and so on. Because the containers are independently chosen and distinguishable, their combined generating function is one divided by one minus x, raised to the k-th power.

How many assignments are there? One combinatorial argument arranges n identical stars and k minus one separators in a line. The separators divide the stars into k possibly empty groups. There are n plus k minus one total positions, and we choose the k minus one separator positions. Hence the coefficient of x to the n is the binomial coefficient with upper entry n plus k minus one and lower entry k minus one.

This identity gives a nontrivial power-series expansion without differentiating anything. It also shows how a bijective proof and generating-function algebra can describe the same construction from different directions.

For k equal to two, the coefficient is n plus one: the first container gets any number from zero through n, and the second gets the rest. Its generating function is one divided by the square of one minus x. Do not confuse that with one divided by one minus x squared. The first expression counts ordered pairs of nonnegative integers with a prescribed sum; the second counts only even sizes, with one choice at each allowed size.

## Counting sequences instead of multisets

Suppose we build a positive integer n as an *ordered* sequence of positive parts. For n equal to four, the decompositions include four, one plus three, three plus one, two plus two, and one plus one plus two, among others. Order now matters.

One part of positive size has generating function P equal to x plus x squared and so on, or x divided by one minus x. A sequence of exactly k parts has generating function P to the k. If we allow any number of parts, including the empty sequence of size zero, the generating function is one plus P plus P squared and so on. Formally that is one divided by one minus P. Substituting P and simplifying gives the fraction one minus x divided by one minus two x.

Expand it: the constant term is one. For every positive n, the coefficient is two to the n minus one. There is a simple independent proof. Write n identical marks in a row. There are n minus one gaps between consecutive marks. Choose independently whether each gap is a break between parts. Each subset of gaps specifies exactly one composition. The two proofs agree because they describe the same objects: sequences of positive parts.

## What the algebra buys us

Generating functions do not replace combinatorial understanding. We still need to know what our factors mean, whether objects are distinguishable, and whether order matters. But once we have modeled those choices, algebra gives a uniform way to combine them, manipulate them, and extract answers.

The most useful shift is conceptual. Instead of solving one counting problem for each n, we construct an object whose coefficients solve all of them simultaneously. In the next layer of combinatorics, a recurrence relation will turn into an equation for a generating function, and that equation may reveal the long-term growth of a sequence. Even before that, products, geometric series, and coefficient extraction give us a language for complex counting problems that would be difficult to manage case by case.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For \(A(x)=\sum_{n\ge0}a_nx^n\), write \([x^n]A(x)=a_n\). In formal power series over a commutative ring,
\[
[x^n](A(x)B(x))=\sum_{k=0}^n a_kb_{n-k}.
\]

**Unlimited packet sizes 2 and 3:**
\[
A(x)=\frac1{(1-x^2)(1-x^3)},\qquad [x^{12}]A(x)=3.
\]
**Stars and bars:**
\[
\frac1{(1-x)^k}=\sum_{n\ge0}{n+k-1\choose k-1}x^n.
\]
**Compositions:**
\[
1+P+P^2+\cdots=\frac1{1-\frac{x}{1-x}}=\frac{1-x}{1-2x}
=1+\sum_{n\ge1}2^{n-1}x^n.
\]

### Exercises with answers

1. What is \([x^6](1-x^2)^{-1}(1-x^3)^{-1}\)? **Answer:** two; solutions are \((a,b)=(3,0),(0,2)\).
2. Give the series for choosing each of three labeled objects of weights one, two, and four at most once. **Answer:** \((1+x)(1+x^2)(1+x^4)\).
3. What does \((1-x)^{-3}\) count? **Answer:** assignments of a total of n indistinguishable items to three labeled containers; coefficient \({n+2\choose2}\).
4. Count ordered compositions of five. **Answer:** sixteen, by choosing cuts in four gaps.

### Reading

MIT 6.042J, *Mathematics for Computer Science*, generating functions and counting; Herbert S. Wilf, *generatingfunctionology*, chapters on ordinary generating functions.
