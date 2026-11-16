# 010000 — Functions: Images, Preimages, Injections, and Inverses

**Track:** Mathematical Reasoning and Proof from First Principles. **Background:** Sets, quantifiers, and basic algebra. **Purpose:** teach an actual proof obligation and the reasoning required to discharge it.

<!-- BEGIN SPOKEN LECTURE -->

# Functions: Images, Preimages, Injections, and Inverses

A function is a rule assigning exactly one output to each input in a specified domain. The word 'specified' matters. The same algebraic expression can represent different functions when its domain or codomain changes. The squaring rule from the real numbers to the real numbers is not injective, because two and minus two have the same square. Restrict its domain to nonnegative reals, and it becomes injective. Restrict its codomain to nonnegative reals as well, and it becomes bijective.

Mathematical proofs about functions rely on four related ideas: images, inverse images, injectivity, and surjectivity. Each has its own quantifier pattern.

## Images and inverse images

For a subset A of the domain, the image f of A contains the values attained by f at inputs in A. For a subset B of the codomain, the inverse image of B contains inputs whose outputs belong to B. The latter makes sense for every function, whether or not it has an inverse function.

Let f of x be x squared on the real line. The image of the interval from minus one to two is the interval from zero to four. The inverse image of the interval from one to four is the union of the intervals from minus two to minus one and from one to two. The set we started with determines what kind of input or output we are testing. Mixing images with inverse images leads to incorrect inclusions.

There is a particularly useful identity: the inverse image of an intersection equals the intersection of the inverse images. To prove it, take an arbitrary x. Its output belongs to B intersect C exactly when its output belongs to B and belongs to C. That happens exactly when x lies in the inverse image of B and the inverse image of C. Both directions are built into the word 'exactly.' The same argument works for unions, complements, and arbitrary indexed unions or intersections.

## When images do not preserve intersections

For forward images we always have f of A intersect B contained in f of A intersect f of B. Equality may fail because the same output can come from different inputs. Let f be the squaring map, A contain only minus one, and B contain only one. Their intersection is empty, so its image is empty. But each set has image containing one, so the intersection of their images contains one. If f is injective, equality does hold: equal outputs then force equal inputs.

This is a small example of a powerful theorem-writing habit. We establish an inclusion unconditionally, construct a counterexample to equality, and then identify the extra hypothesis that restores equality.

## One-to-one and onto

A function is injective if equal outputs imply equal inputs. To prove injectivity, start with arbitrary inputs x and y and assume f of x equals f of y. For f of x equal to two x plus three on the real line, subtract three and divide by two to obtain x equals y. A function is surjective onto its codomain if every target value has at least one input. To prove this, take an arbitrary target y and solve for a valid input. For the same affine function, x equal to y minus three divided by two works for every real y.

Bijective means both injective and surjective. The first property guarantees at most one preimage of a target; the second guarantees at least one. Together they give exactly one, so an inverse function can be defined. For the affine example, that inverse sends y to y minus three divided by two.

## Composition and proof obligations

If f goes from A to B and g goes from B to C, their composition sends x to g of f of x. If both functions are injective, so is their composition. Suppose two inputs have equal composed outputs. Injectivity of g gives equality of their f outputs, and injectivity of f gives equality of the original inputs. This is a proof whose sequence of cancellations mirrors the structure of the composition.

If both functions are surjective, their composition is surjective too. Given a target c in C, surjectivity of g supplies an intermediate b in B. Surjectivity of f supplies an a in A mapping to b. Their composition maps a to c. Observe how the witnesses are selected in reverse order from the function composition.

These ideas will appear in coordinate maps, quotient constructions, optimization, and topology. The inverse image of an open set is central to continuity; bijections express equivalence between sets; linear maps impose special structure. The important habit is to read each property as the exact input-output obligation it represents, rather than relying on the vague phrase 'invertible-looking.'

<!-- END SPOKEN LECTURE -->

---

## Mathematical companion (not spoken)

### Image and preimage identities

For \(f:X\to Y\), \(A\subseteq X\), and \(B,C\subseteq Y\),
\[
f^{-1}(B\cap C)=f^{-1}(B)\cap f^{-1}(C),\qquad f^{-1}(Y\setminus B)=X\setminus f^{-1}(B).
\]
Here \(f^{-1}(B)\) denotes an inverse **image**, which requires no inverse function.
In general \(f(A\cap A')\subseteq f(A)\cap f(A')\); equality follows when \(f\) is injective. For the square map with \(A=\{-1\}\), \(A'=\{1\}\), the inclusion is strict.

### Exercises with answers

1. For \(f(x)=x^2\) on \(\mathbb R\), find \(f^{-1}([1,4])\). **Answer:** \([-2,-1]\cup[1,2]\).
2. Prove the composition of two injections is injective. **Answer:** from \(g(f(x))=g(f(y))\), injectivity of \(g\) gives \(f(x)=f(y)\); injectivity of \(f\) gives \(x=y\).
3. Why is \(f(x)=x^2\) not surjective as a map \(\mathbb R\to\mathbb R\)? **Answer:** no real input maps to \(-1\).

### Sources and further reading

- [Richard Hammack, Book of Proof, third edition (current online edition)](https://richardhammack.github.io/BookOfProof/).
- [Eric Lehman, F. Thomson Leighton and Albert R. Meyer, Mathematics for Computer Science, MIT OCW 6.042J](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/).
- [Wikipedia: Function (mathematics)](https://en.wikipedia.org/wiki/Function_(mathematics)).
