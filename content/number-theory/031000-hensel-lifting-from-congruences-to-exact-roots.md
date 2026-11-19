# 031000 — Hensel's Lemma: From Approximate Roots to Exact Roots

**Track:** Number Theory from First Principles. **Background:** 010000 (modular simple-root lifting) and 030250–030750 (p-adic completeness and coherent residues). **Aim:** prove Hensel's lemma in Z_p, derive the stronger Newton criterion, and distinguish simple roots from singular roots by explicit examples.

<!-- BEGIN SPOKEN LECTURE -->

# Hensel's Lemma: From Approximate Roots to Exact Roots

Consider the equation x squared equals two. It has no rational solution, but it has a solution in the real numbers. Does it have a solution in the seven-adic numbers? Instead of asking where two lies on an ordinary number line, begin with a finite question: is two a square modulo seven?

Three squared is nine, which is congruent to two modulo seven. So three is a root of the equation modulo seven. That is not yet a seven-adic root. It is a first approximation. We must find roots modulo forty-nine, then three hundred forty-three, and every higher power, choosing each new root to agree with the previous approximation.

Hensel's lemma says that a simple root modulo p can be lifted uniquely through all these levels and then becomes an exact p-adic root. The word *simple* is essential. It means that the derivative of the polynomial is not zero at that root modulo p. We will prove why this derivative condition is sufficient, show how the correction is computed, and then examine what can go wrong without it.

## One more correct digit

Let f be a polynomial with coefficients in Z-p, the p-adic integers. Suppose a one is a root modulo p: f of a one is divisible by p. Suppose also that f prime of a one is not divisible by p. The derivative condition says that f prime is invertible modulo p.

Assume we already have a root a n modulo p to the n. To keep all previously correct digits, the next approximation must have the form a n plus t times p to the n, where t is a single new digit between zero and p minus one. We need to choose t so that f of the new approximation is divisible by p to the n plus one.

Expand f around a n. For polynomials, the difference between f of a n plus h and the sum f of a n plus h times f prime of a n is divisible by h squared. Here h is t times p to the n. The remainder is divisible by p to the two n, which is certainly divisible by p to the n plus one when n is positive.

Thus, modulo p to the n plus one, the new polynomial value is congruent to the old value plus t times p to the n times the derivative. Divide this congruence by p to the n. What remains is a linear congruence modulo p: t times f prime of a n must be the negative of f of a n divided by p to the n. The first factor, f prime of a n, is a unit modulo p. So there is *exactly one* choice of the next digit t.

The derivative remains a unit at each stage, because all the approximations agree modulo p. We can therefore repeat the correction forever. The successive approximate roots agree modulo higher and higher powers of p, making them Cauchy. Their limit a exists in Z-p. Since f is continuous, the values f of a n tend to f of a. But f of a n is divisible by p to the n, so its limit is zero. We have built an exact solution.

To prove uniqueness, suppose a and b are two exact roots with the same reduction modulo p. The polynomial difference f of a minus f of b can be factored as a minus b times another polynomial in a and b. When a and b both reduce to the original root, that second factor reduces to the derivative of f at the original root. It is a unit. Since the product is zero in a field and the second factor is not zero, a minus b must be zero. There is just one p-adic root above each simple residue root.

This completes the simple-root version of Hensel's lemma without invoking a black-box existence theorem.

## Square root of two, seven-adically

Return to f of x equals x squared minus two, with p equal to seven. The starting root is three modulo seven, and its derivative is two x. At three the derivative is six, which is invertible modulo seven.

To lift from modulo seven to modulo forty-nine, write the next root as three plus seven t. Three squared minus two is seven, and the derivative at three is six. Dividing by seven leaves the congruence one plus six t equals zero modulo seven. Since the inverse of six modulo seven is six, t equals one. The new root is ten. Indeed, ten squared minus two is ninety-eight, divisible by forty-nine.

For the next digit, write ten plus forty-nine t. Divide ten squared minus two by forty-nine to obtain two, and reduce the derivative twenty modulo seven to six. We need two plus six t to be zero modulo seven, so t equals two. The new root is one hundred eight, and its square differs from two by a multiple of three hundred forty-three.

Continue and the compatible roots define a number in Z-seven whose square is exactly two. The other root modulo seven, four, lifts to the negative of this one. The exact roots exist even though the equation has no rational solution. This is a case where the completion adds algebraic solutions that were not rational, but not because every polynomial has a root in Q-seven. We will soon see examples that have none.

## A singular root can mislead us

Now consider x squared equals three, with p equal to three. Modulo three, zero is a root. But the derivative of x squared minus three is two x, and at zero it is divisible by three. The root is singular. There is no guarantee of a lift.

In this case no three-adic solution exists. Every nonzero three-adic number x has an integer valuation, and the valuation of x squared is twice that integer. It must be even. The valuation of three is one, which is odd. The equality x squared equals three is impossible. The congruence root modulo three was a false lead.

Compare x squared equals nine. Its only root modulo three is again zero, again singular. Yet the exact three-adic roots are three and negative three. Singularity does not mean a lift is impossible; it means the simple-root theorem does not decide the issue. The polynomial may have no lifts, one distinct root, several roots, or a different branching pattern as we refine the modulus.

A classic pair of examples is useful to remember. A root modulo p tells us about the *first* digit. A nonzero derivative tells us that the correction of *every subsequent* digit is uniquely determined. Without that condition, there can be obstructions or choices, and extra analysis is required.

## A stronger condition and Newton's method

The derivative need not be a unit for every Hensel argument. There is a powerful strengthening that begins with an approximate p-adic integer a and measures two valuations: s, the valuation of f of a, and t, the valuation of f prime of a. Suppose the derivative is nonzero and s is strictly greater than twice t.

Then there is a root in Z-p near a. More precisely, the root differs from a by a multiple of p to the s minus t, and it is the only root in the ball of all numbers congruent to a modulo p to the t plus one.

Here is why the inequality has this shape. Take a Newton correction h equal to negative f of a divided by f prime of a. The correction has valuation s minus t, which is greater than t and hence nonnegative. So the new approximation a plus h is still integral and is much closer to a than the scale at which the derivative changes its valuation.

Expand the polynomial again. The linear term cancels f of a *exactly*, leaving a remainder divisible by h squared. Therefore the new error has valuation at least twice s minus t, while the derivative at the new approximation retains valuation t. This gives a new pair of valuations satisfying the same inequality, with the excess s minus twice t growing at least twofold. The Newton corrections tend to zero rapidly in p-adic distance.

The sequence of approximations converges to a root because Q-p is complete and the errors tend to zero. To see uniqueness in the stated ball, compare two possible roots there. The divided difference of f at those points is congruent to f prime of a modulo p to the t plus one, so it has valuation t and is nonzero. Their difference must be zero. This is the p-adic analogue of Newton's method, but with a rigorous arithmetic starting condition.

For a concrete example, take p equal to two and f of x equals x squared minus seventeen. Start at a equal to one. The polynomial error is negative sixteen, of two-adic valuation four. The derivative is two, of valuation one. Four is greater than twice one, so the stronger lemma produces a two-adic square root of seventeen congruent to one modulo four. The basic simple-root test modulo two could not do this: the derivative there is zero.

This example explains why it is worth learning the strengthened version rather than treating Hensel's lemma as only a one-digit correction algorithm. Some genuine roots first become visible after we know a more accurate approximation than merely a root modulo p.

## From local computation to existence

There is another route from modular roots to exact p-adic roots. We proved that Z-p is compact. If a polynomial has a root modulo *every* power of p, compactness gives an exact root in Z-p even if the roots chosen at different levels are not compatible. Hensel's lemma is stronger in a different direction: a simple root at just the first level guarantees the entire compatible tower, and the proof tells us exactly how to compute it.

A polynomial with no solutions modulo some power of p plainly has no solution in Z-p. Conversely, by compactness, solvability at all finite levels is sufficient. This turns p-adic polynomial solving into a bridge between finite computation and exact local arithmetic.

But note the limits of the bridge. Hensel lifting does not prove a rational or integer solution exists. It proves an exact solution in a completion. To understand the difference between local and rational solvability, we need the structure of p-adic squares and some explicit examples of local obstructions.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Let f∈Z_p[X] and let \(\bar a\in\mathbb F_p\) satisfy \(\bar f(\bar a)=0\) and \(\bar f'(\bar a)\ne0\).

### Simple-root Hensel lifting, complete proof

Choose a_1 lifting \(\bar a\). Inductively suppose f(a_n)≡0 modp^n and a_n≡a_1 modp. Write a_{n+1}=a_n+p^n t with t∈{0,...,p-1}. Taylor's identity in Z_p[X,Y] yields

\[
f(a_n+p^n t)\equiv f(a_n)+p^n t f'(a_n) \pmod{p^{n+1}}.
\]

Hence choose the unique \(t\equiv-(f(a_n)/p^n)f'(a_n)^{-1}\pmod p\). The sequence (a_n) is Cauchy; its limit α obeys f(α)=0. If α,β are two roots in the same residue class,

\[
0=f(\alpha)-f(\beta)=(\alpha-\beta)G(\alpha,\beta),\quad
G(\alpha,\beta)\equiv f'(a_1)\not\equiv0\pmod p,
\]

so α=β.

### Strengthened Newton criterion

Suppose a∈Z_p, t=v_p(f'(a))<∞ and s=v_p(f(a))>2t. For a'=a+h with h=-f(a)/f'(a), v_p(h)=s-t>t and

\[
f(a')=h^2 G(a,h),\qquad v_p(f(a'))\ge 2(s-t),\qquad
v_p(f'(a'))=t.
\]

Iteration doubles at least the positive surplus \(s_n-2t\), and corrections tend to zero. Its limit α satisfies f(α)=0 and \(v_p(\alpha-a)\ge s-t\). In the ball a+p^{t+1}Z_p, the divided difference of f has valuation t, so a zero there is unique. If f(a)=0 to start, there is nothing to lift.

### Computed examples

- \(p=7, f(X)=X^2-2\): a_1=3 mod7; a_2=10 mod49; a_3=108 mod343; a_4=2166 mod2401. Squares at each stage agree with 2.
- \(p=3, f(X)=X^2-3\): root 0 mod3 is singular; no root in Q_3 since valuations of squares are even.
- \(p=3, f(X)=X^2-9\): singular 0 mod3 lifts to ±3.
- \(p=2, f(X)=X^2-17, a=1\): s=4, t=1, and 4>2, so 17 is a square in Q_2.

### Exercises

1. Derive the formula for the next Hensel digit from the quadratic Taylor remainder.
2. Verify 108²≡2 mod343 and 2166²≡2 mod2401.
3. For p=5, lift the root 2 of X²+1 modulo 5 to a root modulo 125.
4. Give a singular polynomial root modulo p that does not lift to Q_p, and another that does.
5. In the strengthened Newton criterion, explain why v_p(f'(a+h)) remains t and why the corrections stay integral.

### Reading and source notes

- Keith Conrad, [Hensel's Lemma](https://kconrad.math.uconn.edu/blurbs/gradnumthy/hensel.pdf), especially §§2–3, lifting, uniqueness and the stronger valuation criterion.
- Andrew V. Sutherland, MIT 18.785, [Lecture 9: Local Fields and Hensel's Lemmas](https://math.mit.edu/classes/18.785/2021fa/LectureNotes9.pdf).
- Wikipedia: [Hensel's lemma](https://en.wikipedia.org/wiki/Hensel%27s_lemma), [Newton's method](https://en.wikipedia.org/wiki/Newton%27s_method), [p-adic number](https://en.wikipedia.org/wiki/P-adic_number).
